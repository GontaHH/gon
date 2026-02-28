#!/usr/bin/env python3
"""
貨物鉄道ニュース要約スクリプト
その日の貨物鉄道に関するニュース記事を収集し、要約を出力します。

使い方:
    python3 freight_railway_news.py

認証（優先順）:
    1. CLAUDE_SESSION_INGRESS_TOKEN_FILE 環境変数が指すファイルのトークン
    2. ANTHROPIC_API_KEY 環境変数
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import anthropic


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


def get_today_str() -> str:
    """今日の日付を日本語文字列で返す。"""
    jst = timezone(timedelta(hours=9))
    return datetime.now(jst).strftime("%Y年%m月%d日")


def fetch_and_summarize_news(client: anthropic.Anthropic) -> str:
    """
    Claude API のウェブ検索ツールを使って本日の貨物鉄道ニュースを
    収集・要約し、結果を文字列で返す。
    """
    today = get_today_str()

    system_prompt = (
        "あなたは鉄道業界のニュースリサーチャーです。"
        "貨物鉄道に関する最新情報を収集し、分かりやすく日本語で要約することが得意です。"
        "必ず検索ツールを使って情報を確認してから回答してください。"
    )

    user_prompt = f"""本日（{today}）の貨物鉄道に関するニュースを調査して、日本語で要約してください。

検索のヒント:
- 「貨物鉄道 ニュース {today}」
- 「JR貨物 {today}」
- 「freight railway news today 2026」
- 英語・日本語の両方で検索してより多くの情報を収集してください

以下の形式で出力してください:

【本日の貨物鉄道ニュース要約】（{today}）

■ 主要トピック
（全体のトレンドや主なテーマを2〜3文で）

■ 注目記事
（重要な記事を箇条書きで。タイトル・概要・出典を含める）

■ 業界動向・今後の展望
（業界への影響や今後の動向があれば）

※ 本日のニュースが見つからない場合は、直近の重要なニュースを紹介してください。"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=system_prompt,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": user_prompt}],
    )

    # レスポンスからテキストブロックを結合して返す
    text_parts = []
    for block in response.content:
        if hasattr(block, "text") and block.text.strip():
            text_parts.append(block.text.strip())

    return "\n\n".join(text_parts) if text_parts else "（要約テキストが生成されませんでした）"


def main() -> None:
    today = get_today_str()
    print(f"=== {today} の貨物鉄道ニュース ===\n")
    print("ニュースを収集・要約中です。しばらくお待ちください...\n")

    client = get_client()

    try:
        summary = fetch_and_summarize_news(client)
        print(summary)
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
