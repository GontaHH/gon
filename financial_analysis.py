#!/usr/bin/env python3
"""
企業財務分析スクリプト
指定した企業の過去10年分の財務データをネット検索で収集し、
企業価値算定（DCF・マルチプル）と財務分析（各種財務指標）を行います。

使い方:
    python3 financial_analysis.py <企業名>
    python3 financial_analysis.py --company <企業名> [--output report.txt]
    python3 financial_analysis.py  # インタラクティブ入力

認証（優先順）:
    1. CLAUDE_SESSION_INGRESS_TOKEN_FILE 環境変数が指すファイルのトークン
    2. ANTHROPIC_API_KEY 環境変数
"""

import os
import sys
import re
import json
import argparse
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import Optional

import anthropic

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 8192

JST = timezone(timedelta(hours=9))
CURRENT_YEAR = datetime.now(JST).year
START_YEAR = CURRENT_YEAR - 10


# ── データ構造 ──────────────────────────────────────────────────────


@dataclass
class AnnualFinancials:
    """1会計年度分の財務数値（単位: 百万円 or 百万USD）"""
    year: int
    revenue: Optional[float] = None
    operating_income: Optional[float] = None
    ebitda: Optional[float] = None
    net_income: Optional[float] = None
    total_assets: Optional[float] = None
    total_equity: Optional[float] = None
    total_debt: Optional[float] = None
    cash: Optional[float] = None
    operating_cashflow: Optional[float] = None
    capex: Optional[float] = None
    shares_outstanding: Optional[float] = None
    stock_price_high: Optional[float] = None
    stock_price_low: Optional[float] = None
    dividend_per_share: Optional[float] = None


@dataclass
class CompanyProfile:
    """企業基本情報"""
    name: str
    ticker: Optional[str] = None
    exchange: Optional[str] = None
    sector: Optional[str] = None
    currency: str = "JPY"
    market_type: str = "japanese"
    current_stock_price: Optional[float] = None
    market_cap: Optional[float] = None
    enterprise_value: Optional[float] = None


@dataclass
class FinancialReport:
    """最終レポートに含まれる全データ"""
    profile: CompanyProfile
    annual_data: list = field(default_factory=list)
    ratios: dict = field(default_factory=dict)
    valuation: dict = field(default_factory=dict)
    data_sources: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    raw_claude_output: str = ""


# ── 認証 ────────────────────────────────────────────────────────────


def get_client() -> anthropic.Anthropic:
    """認証済みの Anthropic クライアントを返す。"""
    token_file = os.environ.get("CLAUDE_SESSION_INGRESS_TOKEN_FILE", "")
    if token_file and os.path.exists(token_file):
        with open(token_file) as f:
            token = f.read().strip()
        return anthropic.Anthropic(auth_token=token)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key:
        return anthropic.Anthropic(api_key=api_key)

    print(
        "[ERROR] 認証情報が見つかりません。\n"
        "  ANTHROPIC_API_KEY 環境変数を設定するか、\n"
        "  CLAUDE_SESSION_INGRESS_TOKEN_FILE を正しく設定してください。",
        file=sys.stderr,
    )
    sys.exit(1)


# ── 引数パース ───────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    """コマンドライン引数を解析する。引数なしの場合は対話入力。"""
    parser = argparse.ArgumentParser(
        description="企業財務分析ツール - 過去10年の財務データを収集・分析します"
    )
    parser.add_argument(
        "company",
        nargs="?",
        help="分析対象の企業名（例: トヨタ自動車、Apple Inc、7203）",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        help="レポートをファイルに保存する場合のパス",
    )
    parser.add_argument(
        "--market",
        choices=["japanese", "international", "auto"],
        default="auto",
        help="市場タイプ（デフォルト: auto で自動判定）",
    )
    args = parser.parse_args()

    if not args.company:
        args.company = input("分析する企業名を入力してください: ").strip()
        if not args.company:
            print("[ERROR] 企業名が入力されませんでした。", file=sys.stderr)
            sys.exit(1)

    return args


# ── 市場判定 ─────────────────────────────────────────────────────────


def detect_market(company_name: str) -> str:
    """
    企業名から市場タイプ（"japanese" / "international"）を推定する。
    4〜5桁の数字はTSE証券コード、日本語文字を含む場合は日本企業と判定。
    """
    if re.fullmatch(r"\d{4,5}", company_name.strip()):
        return "japanese"

    if re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", company_name):
        return "japanese"

    jp_keywords = [
        "toyota", "honda", "sony", "softbank", "nintendo",
        "panasonic", "hitachi", "toshiba", "ntt", "rakuten",
        "fujitsu", "canon", "nikon", "murata", "keyence",
        "fast retailing", "uniqlo", "kddi", "docomo", "jal",
        "ana", "mitsubishi", "mitsui", "sumitomo", "nomura",
    ]
    if any(kw in company_name.lower() for kw in jp_keywords):
        return "japanese"

    return "international"


# ── プロンプト生成 ────────────────────────────────────────────────────


def _build_system_prompt(market_type: str) -> str:
    if market_type == "japanese":
        source_guidance = (
            "日本企業のデータ収集には以下のソースを優先してください:\n"
            "- EDINET: 有価証券報告書（開示情報）\n"
            "- IR Bank (https://irbank.net/): 長期財務データ\n"
            "- 株探/Kabutan (https://kabutan.jp/): 財務・株価データ\n"
            "- Macrotrends (https://www.macrotrends.net/): 長期トレンド\n"
            "- 企業のIR公式ページ"
        )
    else:
        source_guidance = (
            "国際企業のデータ収集には以下のソースを優先してください:\n"
            "- SEC EDGAR: 10-K年次報告書\n"
            "- Macrotrends (https://www.macrotrends.net/): 長期財務トレンド\n"
            "- Yahoo Finance (https://finance.yahoo.com/): 財務諸表\n"
            "- Stockanalysis.com: 財務比較データ"
        )

    return (
        "あなたは財務アナリストです。企業の財務諸表を正確に収集・分析することが専門です。\n\n"
        "必ずウェブ検索ツールを使って実際のデータを取得してから回答してください。\n\n"
        f"{source_guidance}\n\n"
        "重要なルール:\n"
        "- データが入手できない年度は null と記載（文字列の \"N/A\" は使用しない）\n"
        "- 通貨単位を一貫させ、必ず単位（百万円 / 百万USD）を明記する\n"
        "- 財務データは必ず ```json ... ``` ブロックに含める（後続の自動処理で使用）\n"
        "- 推計値を使用した場合は必ず注記する"
    )


def _build_user_prompt(company_name: str, market_type: str) -> str:
    today_str = datetime.now(JST).strftime("%Y年%m月%d日")

    if market_type == "japanese":
        search_hints = (
            f'- 「{company_name} 有価証券報告書 財務諸表 過去10年」\n'
            f'- 「{company_name} IR Bank 財務」\n'
            f'- 「{company_name} 株探 財務」\n'
            f'- 「{company_name} 売上高 営業利益 純利益 推移」\n'
            f'- 「{company_name} 株価 EPS BPS 時価総額」'
        )
        currency_note = "単位は百万円（M JPY）で統一してください。"
        json_currency = "JPY"
    else:
        search_hints = (
            f'- "{company_name} annual revenue operating income 10 year history"\n'
            f'- "{company_name} 10-K SEC filing financial statements"\n'
            f'- "{company_name} macrotrends revenue net income"\n'
            f'- "{company_name} total debt equity market cap EPS annual"'
        )
        currency_note = "単位は百万USD（M USD）で統一してください。"
        json_currency = "USD"

    return f"""本日（{today_str}）、「{company_name}」の財務分析を依頼されました。

## Phase 1: データ収集
以下の検索ヒントを使い、{START_YEAR}年〜{CURRENT_YEAR}年（最大10年分）の財務データを収集してください:

{search_hints}

## Phase 2: 構造化データ出力
収集したデータを以下のJSON形式で出力してください（必ず ```json で囲む）:

```json
{{
  "company_name": "{company_name}",
  "ticker": null,
  "exchange": null,
  "sector": null,
  "currency": "{json_currency}",
  "current_stock_price": null,
  "market_cap_millions": null,
  "annual_data": [
    {{
      "year": {START_YEAR},
      "revenue": null,
      "operating_income": null,
      "ebitda": null,
      "net_income": null,
      "total_assets": null,
      "total_equity": null,
      "total_debt": null,
      "cash": null,
      "operating_cashflow": null,
      "capex": null,
      "shares_outstanding_millions": null,
      "stock_price_high": null,
      "stock_price_low": null,
      "dividend_per_share": null
    }}
  ],
  "data_sources": []
}}
```
{currency_note}
annual_data には {START_YEAR}年から{CURRENT_YEAR}年まで全年度を含めてください。
取得できた数値は必ず記入し、不明な項目のみ null にしてください。

## Phase 3: 財務分析テキスト
JSONの後に、以下の分析を日本語テキストで記載してください:

【企業概要】
（事業内容、業界でのポジション、主要製品・サービス）

【過去10年の業績トレンド】
（売上高・利益の推移、特筆すべき変化点と背景要因）

【財務健全性の所見】
（収益性・安全性・成長性に関するコメント）

【データの信頼性・注意事項】
（データが入手できなかった年度、推計値を使用した箇所、データソースの信頼性）"""


# ── API 呼び出し ──────────────────────────────────────────────────────


def search_financial_data(
    client: anthropic.Anthropic,
    company_name: str,
    market_type: str,
) -> tuple:
    """
    Claude のウェブ検索ツールを使って10年分の財務データを収集する。

    Returns:
        (raw_text, json_data) のタプル。json_data はパース済み dict または None。
    """
    system_prompt = _build_system_prompt(market_type)
    user_prompt = _build_user_prompt(company_name, market_type)

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": user_prompt}],
    )

    text_parts = []
    for block in response.content:
        if hasattr(block, "text") and block.text.strip():
            text_parts.append(block.text.strip())

    raw_text = "\n\n".join(text_parts) if text_parts else ""
    json_data = _extract_json_block(raw_text)

    return raw_text, json_data


def _extract_json_block(text: str) -> Optional[dict]:
    """
    テキストから ```json ... ``` ブロックを抽出してパースする。
    失敗した場合は None を返す（グレースフルデグラデーション）。
    """
    match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
    if not match:
        return None

    raw = match.group(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Python の None が混入している場合の修正を試みる
        raw = re.sub(r"\bNone\b", "null", raw)
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return None


# ── データ構造化 ──────────────────────────────────────────────────────


def build_report_from_json(
    company_name: str,
    market_type: str,
    json_data: Optional[dict],
    raw_text: str,
) -> FinancialReport:
    """ClaudeのJSONレスポンスをFinancialReportデータクラスに変換する。"""
    if not json_data:
        profile = CompanyProfile(name=company_name, market_type=market_type)
        report = FinancialReport(profile=profile, raw_claude_output=raw_text)
        report.warnings.append(
            "構造化JSONデータの抽出に失敗しました。アナリストコメントのみ表示します。"
        )
        return report

    profile = CompanyProfile(
        name=json_data.get("company_name", company_name),
        ticker=json_data.get("ticker"),
        exchange=json_data.get("exchange"),
        sector=json_data.get("sector"),
        currency=json_data.get("currency", "JPY"),
        market_type=market_type,
        current_stock_price=json_data.get("current_stock_price"),
        market_cap=json_data.get("market_cap_millions"),
    )

    annual_data = []
    for entry in json_data.get("annual_data", []):
        af = AnnualFinancials(
            year=entry["year"],
            revenue=entry.get("revenue"),
            operating_income=entry.get("operating_income"),
            ebitda=entry.get("ebitda"),
            net_income=entry.get("net_income"),
            total_assets=entry.get("total_assets"),
            total_equity=entry.get("total_equity"),
            total_debt=entry.get("total_debt"),
            cash=entry.get("cash"),
            operating_cashflow=entry.get("operating_cashflow"),
            capex=entry.get("capex"),
            shares_outstanding=entry.get("shares_outstanding_millions"),
            stock_price_high=entry.get("stock_price_high"),
            stock_price_low=entry.get("stock_price_low"),
            dividend_per_share=entry.get("dividend_per_share"),
        )
        annual_data.append(af)

    return FinancialReport(
        profile=profile,
        annual_data=sorted(annual_data, key=lambda x: x.year),
        data_sources=json_data.get("data_sources", []),
        raw_claude_output=raw_text,
    )


# ── 財務比率計算 ──────────────────────────────────────────────────────


def calculate_ratios(report: FinancialReport) -> None:
    """
    年次データから財務比率・企業価値指標を計算し、
    report.ratios と report.valuation を更新する（in-place）。
    """
    data = report.annual_data
    if not data:
        return

    ratios_by_year = {}
    for af in data:
        r = {}

        # 収益性指標
        if af.revenue and af.operating_income is not None:
            r["operating_margin_pct"] = round(af.operating_income / af.revenue * 100, 2)

        if af.revenue and af.net_income is not None:
            r["net_margin_pct"] = round(af.net_income / af.revenue * 100, 2)

        if af.total_assets and af.net_income is not None and af.total_assets != 0:
            r["roa_pct"] = round(af.net_income / af.total_assets * 100, 2)

        if af.total_equity and af.net_income is not None and af.total_equity != 0:
            r["roe_pct"] = round(af.net_income / af.total_equity * 100, 2)

        if af.revenue and af.ebitda is not None and af.revenue != 0:
            r["ebitda_margin_pct"] = round(af.ebitda / af.revenue * 100, 2)

        # 1株指標
        if af.shares_outstanding and af.net_income is not None and af.shares_outstanding != 0:
            r["eps"] = round(af.net_income / af.shares_outstanding, 2)

        if af.shares_outstanding and af.total_equity is not None and af.shares_outstanding != 0:
            r["bps"] = round(af.total_equity / af.shares_outstanding, 2)

        # FCF
        if af.operating_cashflow is not None and af.capex is not None:
            r["fcf"] = af.operating_cashflow - af.capex
            if af.revenue and af.revenue != 0:
                r["fcf_margin_pct"] = round(r["fcf"] / af.revenue * 100, 2)

        # 安全性指標
        if af.total_equity and af.total_debt is not None and af.total_equity != 0:
            r["debt_equity_ratio"] = round(af.total_debt / af.total_equity, 2)

        if af.total_debt is not None and af.cash is not None:
            r["net_debt"] = af.total_debt - af.cash

        if af.total_assets and af.total_equity is not None and af.total_assets != 0:
            total_liabilities = af.total_assets - af.total_equity
            r["debt_to_assets_pct"] = round(total_liabilities / af.total_assets * 100, 2)

        # 株価指標（年間高値・安値の中央値を基準）
        mid_price = None
        if af.stock_price_high and af.stock_price_low:
            mid_price = (af.stock_price_high + af.stock_price_low) / 2

        if mid_price and r.get("eps") and r["eps"] > 0:
            r["per"] = round(mid_price / r["eps"], 1)

        if mid_price and r.get("bps") and r["bps"] > 0:
            r["pbr"] = round(mid_price / r["bps"], 2)

        ratios_by_year[af.year] = r

    # 前年比成長率
    sorted_years = sorted(ratios_by_year.keys())
    for i, year in enumerate(sorted_years):
        if i == 0:
            continue
        prev_year = sorted_years[i - 1]
        prev_af = next((d for d in data if d.year == prev_year), None)
        curr_af = next((d for d in data if d.year == year), None)
        if not prev_af or not curr_af:
            continue
        if prev_af.revenue and curr_af.revenue and prev_af.revenue > 0:
            ratios_by_year[year]["revenue_growth_pct"] = round(
                (curr_af.revenue - prev_af.revenue) / prev_af.revenue * 100, 2
            )
        if prev_af.operating_income and curr_af.operating_income and prev_af.operating_income > 0:
            ratios_by_year[year]["operating_income_growth_pct"] = round(
                (curr_af.operating_income - prev_af.operating_income) / prev_af.operating_income * 100, 2
            )

    report.ratios = ratios_by_year
    _calculate_valuation(report)


def _calculate_valuation(report: FinancialReport) -> None:
    """EV/EBITDA、PER、PBR、DCFによる企業価値レンジを計算する。"""
    p = report.profile
    data = report.annual_data
    ratios = report.ratios
    val = {}

    if not data:
        return

    latest = max(data, key=lambda x: x.year)
    latest_r = ratios.get(latest.year, {})
    net_debt = latest_r.get("net_debt")

    # EV/EBITDA
    if p.market_cap and net_debt is not None and latest.ebitda:
        ev = p.market_cap + net_debt
        p.enterprise_value = ev
        ev_ebitda = round(ev / latest.ebitda, 1)
        val["ev_ebitda"] = ev_ebitda
        val["ev_ebitda_note"] = (
            f"EV/EBITDA = {ev_ebitda}x（参考: 製造業8〜12x, IT 15〜25x, 消費財10〜15x）"
        )

    # PER（現在株価ベース）
    current_eps = latest_r.get("eps")
    if p.current_stock_price and current_eps and current_eps > 0:
        current_per = round(p.current_stock_price / current_eps, 1)
        val["current_per"] = current_per
        # 過去5年平均PERで理論株価を算出
        historical_pers = [
            v["per"] for yr, v in ratios.items()
            if "per" in v and yr >= CURRENT_YEAR - 5
        ]
        if historical_pers:
            avg_per = round(sum(historical_pers) / len(historical_pers), 1)
            val["avg_5yr_per"] = avg_per
            val["implied_price_per"] = round(avg_per * current_eps, 0)

    # PBR
    current_bps = latest_r.get("bps")
    if p.current_stock_price and current_bps and current_bps > 0:
        val["current_pbr"] = round(p.current_stock_price / current_bps, 2)

    # 簡易 DCF
    recent_fcfs = []
    for yr in sorted(ratios.keys())[-3:]:
        fcf = ratios[yr].get("fcf")
        if fcf is not None:
            recent_fcfs.append(fcf)

    if recent_fcfs:
        avg_fcf = sum(recent_fcfs) / len(recent_fcfs)
        growth_rates = [
            ratios[yr].get("revenue_growth_pct", 0) / 100
            for yr in sorted(ratios.keys())[-3:]
            if ratios[yr].get("revenue_growth_pct") is not None
        ]
        g = sum(growth_rates) / len(growth_rates) if growth_rates else 0.03
        g = max(min(g, 0.15), -0.05)  # キャップ: -5% 〜 +15%

        wacc = 0.08          # 加重平均資本コスト（仮定: 8%）
        terminal_growth = 0.02  # 永続成長率（仮定: 2%）
        forecast_years = 5

        dcf_scenarios = []
        for scenario, g_factor in [("ベア（悲観）", 0.7), ("ベース", 1.0), ("ブル（楽観）", 1.3)]:
            scenario_g = g * g_factor
            pv_fcf = 0.0
            fcf_t = avg_fcf
            for t in range(1, forecast_years + 1):
                fcf_t *= (1 + scenario_g)
                pv_fcf += fcf_t / (1 + wacc) ** t

            terminal_fcf = fcf_t * (1 + terminal_growth)
            terminal_value = terminal_fcf / (wacc - terminal_growth)
            pv_terminal = terminal_value / (1 + wacc) ** forecast_years

            ev_dcf = pv_fcf + pv_terminal
            implied_price = None
            if net_debt is not None and latest.shares_outstanding:
                equity_value = ev_dcf - net_debt
                implied_price = round(equity_value / latest.shares_outstanding, 0)

            dcf_scenarios.append({
                "scenario": scenario,
                "ev_dcf": round(ev_dcf, 0),
                "implied_stock_price": implied_price,
            })

        val["dcf"] = {
            "avg_fcf": round(avg_fcf, 0),
            "assumed_growth_rate_pct": round(g * 100, 2),
            "assumed_wacc_pct": wacc * 100,
            "assumed_terminal_growth_pct": terminal_growth * 100,
            "scenarios": dcf_scenarios,
        }

    report.valuation = val


# ── レポートフォーマット ──────────────────────────────────────────────


def format_report(report: FinancialReport) -> str:
    """FinancialReport を端末表示用の文字列にフォーマットして返す。"""
    lines = []
    p = report.profile
    currency = "円" if p.currency == "JPY" else "USD"
    unit = "百万円" if p.currency == "JPY" else "百万USD"

    # ヘッダー
    lines.append("=" * 72)
    lines.append(f"【企業財務分析レポート】 {p.name}")
    if p.ticker:
        exchange_str = f" ({p.exchange})" if p.exchange else ""
        lines.append(f"  銘柄コード: {p.ticker}{exchange_str}")
    if p.sector:
        lines.append(f"  業種: {p.sector}")
    lines.append(f"  分析日時: {datetime.now(JST).strftime('%Y年%m月%d日 %H:%M JST')}")
    lines.append("=" * 72)

    # 株価・規模
    lines.append("\n■ 現在の株価・規模")
    if p.current_stock_price:
        lines.append(f"  現在株価:   {p.current_stock_price:>12,.1f} {currency}")
    if p.market_cap:
        lines.append(f"  時価総額:   {p.market_cap:>12,.0f} {unit}")
    if p.enterprise_value:
        lines.append(f"  EV:         {p.enterprise_value:>12,.0f} {unit}")

    # 10年財務サマリーテーブル
    if report.annual_data:
        lines.append(f"\n■ 過去10年 財務サマリー（単位: {unit}）")
        header = f"{'年度':>6}  {'売上高':>14}  {'営業利益':>12}  {'純利益':>12}  {'営業利益率':>8}  {'ROE':>6}  {'D/E':>6}"
        lines.append(header)
        lines.append("-" * 76)
        for af in report.annual_data:
            r = report.ratios.get(af.year, {})
            rev = f"{af.revenue:>14,.0f}" if af.revenue is not None else f"{'N/A':>14}"
            op  = f"{af.operating_income:>12,.0f}" if af.operating_income is not None else f"{'N/A':>12}"
            ni  = f"{af.net_income:>12,.0f}" if af.net_income is not None else f"{'N/A':>12}"
            om_val = r.get("operating_margin_pct")
            om  = f"{om_val:>7.1f}%" if isinstance(om_val, float) else f"{'N/A':>8}"
            roe_val = r.get("roe_pct")
            roe = f"{roe_val:>5.1f}%" if isinstance(roe_val, float) else f"{'N/A':>6}"
            de_val = r.get("debt_equity_ratio")
            de  = f"{de_val:>5.2f}x" if isinstance(de_val, float) else f"{'N/A':>6}"
            lines.append(f"{af.year:>6}  {rev}  {op}  {ni}  {om}  {roe}  {de}")

        # 成長率テーブル
        lines.append(f"\n■ 成長率トレンド（前年比）")
        lines.append(f"{'年度':>6}  {'売上成長率':>10}  {'営業利益成長率':>14}  {'FCFマージン':>10}")
        lines.append("-" * 50)
        for af in report.annual_data:
            r = report.ratios.get(af.year, {})
            rg_val = r.get("revenue_growth_pct")
            rg = f"{rg_val:>9.1f}%" if isinstance(rg_val, float) else f"{'N/A':>10}"
            og_val = r.get("operating_income_growth_pct")
            og = f"{og_val:>13.1f}%" if isinstance(og_val, float) else f"{'N/A':>14}"
            fm_val = r.get("fcf_margin_pct")
            fm = f"{fm_val:>9.1f}%" if isinstance(fm_val, float) else f"{'N/A':>10}"
            lines.append(f"{af.year:>6}  {rg}  {og}  {fm}")

        # 株価指標テーブル
        lines.append(f"\n■ 株価指標推移")
        lines.append(f"{'年度':>6}  {'EPS':>10}  {'BPS':>12}  {'PER':>7}  {'PBR':>7}  {'FCF':>16}")
        lines.append("-" * 64)
        for af in report.annual_data:
            r = report.ratios.get(af.year, {})
            eps_val = r.get("eps")
            eps = f"{eps_val:>10.1f}" if isinstance(eps_val, float) else f"{'N/A':>10}"
            bps_val = r.get("bps")
            bps = f"{bps_val:>12.1f}" if isinstance(bps_val, float) else f"{'N/A':>12}"
            per_val = r.get("per")
            per = f"{per_val:>6.1f}x" if isinstance(per_val, float) else f"{'N/A':>7}"
            pbr_val = r.get("pbr")
            pbr = f"{pbr_val:>6.2f}x" if isinstance(pbr_val, float) else f"{'N/A':>7}"
            fcf_val = r.get("fcf")
            fcf = f"{fcf_val:>16,.0f}" if isinstance(fcf_val, (int, float)) else f"{'N/A':>16}"
            lines.append(f"{af.year:>6}  {eps}  {bps}  {per}  {pbr}  {fcf}")

    # 企業価値算定
    val = report.valuation
    if val:
        lines.append("\n■ 企業価値算定 (Valuation)")
        lines.append("-" * 56)

        if "current_per" in val:
            lines.append(f"  現在のPER:          {val['current_per']:>6.1f}x")
        if "avg_5yr_per" in val:
            lines.append(f"  過去5年平均PER:      {val['avg_5yr_per']:>6.1f}x")
        if "implied_price_per" in val:
            lines.append(f"  PER基準の理論株価: {val['implied_price_per']:>10,.0f} {currency}")
        if "current_pbr" in val:
            lines.append(f"  現在のPBR:          {val['current_pbr']:>6.2f}x")
        if "ev_ebitda" in val:
            lines.append(f"  EV/EBITDA:          {val['ev_ebitda']:>6.1f}x")
        if "ev_ebitda_note" in val:
            lines.append(f"  　└ {val['ev_ebitda_note']}")

        if "dcf" in val:
            dcf = val["dcf"]
            lines.append(f"\n  【DCF分析（簡易版）】")
            lines.append(f"  　直近3年平均FCF:  {dcf['avg_fcf']:>12,.0f} {unit}")
            lines.append(f"  　想定FCF成長率:   {dcf['assumed_growth_rate_pct']:>6.1f}%")
            lines.append(f"  　WACC (仮定):     {dcf['assumed_wacc_pct']:>6.1f}%")
            lines.append(f"  　永続成長率 (仮定): {dcf['assumed_terminal_growth_pct']:>4.1f}%")
            lines.append(f"\n  　シナリオ別理論株価:")
            for s in dcf["scenarios"]:
                ev_str = f"{s['ev_dcf']:,.0f} {unit}"
                if s["implied_stock_price"] is not None:
                    price_str = f"{s['implied_stock_price']:,.0f} {currency}"
                    updown = ""
                    if report.profile.current_stock_price:
                        diff = (s["implied_stock_price"] - report.profile.current_stock_price)
                        pct = diff / report.profile.current_stock_price * 100
                        updown = f"（現在比 {pct:+.1f}%）"
                else:
                    price_str = "N/A（株式数データ不足）"
                    updown = ""
                lines.append(f"  　  {s['scenario']:16s}  EV={ev_str}  理論株価={price_str}{updown}")

    # Claude テキスト分析（JSONブロック除去）
    analysis_text = re.sub(r"```json[\s\S]*?```", "", report.raw_claude_output).strip()
    if analysis_text:
        lines.append("\n■ アナリストコメント（AI分析）")
        lines.append("-" * 56)
        lines.append(analysis_text)

    # データソース
    if report.data_sources:
        lines.append("\n■ データソース")
        for src in report.data_sources:
            lines.append(f"  - {src}")

    # 警告
    if report.warnings:
        lines.append("\n⚠  注意事項")
        for w in report.warnings:
            lines.append(f"  ! {w}")

    # 免責事項
    lines.append("\n" + "=" * 72)
    lines.append("【免責事項】本レポートは情報提供を目的としており、投資助言ではありません。")
    lines.append("  データはAI検索により収集したものであり、正確性を保証しません。")
    lines.append("  投資判断は必ず公式財務書類および専門家の助言に基づいて行ってください。")
    lines.append("=" * 72)

    return "\n".join(lines)


# ── ファイル保存 ──────────────────────────────────────────────────────


def save_report(content: str, filepath: str) -> None:
    """レポートをUTF-8テキストファイルとして保存する。"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\nレポートを保存しました: {filepath}")


# ── メイン ────────────────────────────────────────────────────────────


def main() -> None:
    args = parse_args()
    company_name = args.company

    market_type = (
        args.market if args.market != "auto" else detect_market(company_name)
    )
    market_label = "日本市場" if market_type == "japanese" else "海外市場"

    print(f"\n=== 企業財務分析: {company_name} ({market_label}) ===\n")
    print(f"対象期間: {START_YEAR}年〜{CURRENT_YEAR}年（最大10年分）")
    print("財務データを収集・分析中です。しばらくお待ちください...\n")

    client = get_client()

    try:
        raw_text, json_data = search_financial_data(client, company_name, market_type)
        report = build_report_from_json(company_name, market_type, json_data, raw_text)
        calculate_ratios(report)

        formatted = format_report(report)
        print(formatted)

        if args.output:
            save_report(formatted, args.output)

    except anthropic.AuthenticationError:
        print(
            "[ERROR] 認証に失敗しました。APIキーまたはトークンを確認してください。",
            file=sys.stderr,
        )
        sys.exit(1)
    except anthropic.APIConnectionError as e:
        print(f"[ERROR] APIへの接続に失敗しました: {e}", file=sys.stderr)
        sys.exit(1)
    except anthropic.APIStatusError as e:
        print(f"[ERROR] APIエラー (HTTP {e.status_code}): {e.message}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
