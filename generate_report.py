#!/usr/bin/env python3
"""
レポートをHTML/PDF形式に変換するスクリプト。

使い方:
    python3 generate_report.py [--pdf]

オプション:
    --pdf    HTML 変換後に PDF 生成も試みる（weasyprint が必要）
"""

import argparse
import os
import sys
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

# ─── 定数 ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
INPUT_MD = BASE_DIR / "report_draft.md"
OUTPUT_HTML = BASE_DIR / "report_final.html"
OUTPUT_PDF = BASE_DIR / "report_final.pdf"

CSS = """
/* ─── リセット ────────────────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── 基本レイアウト ─────────────────────────────────────────────────────── */
body {
    font-family: "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Meiryo",
                 "Yu Gothic", sans-serif;
    font-size: 15px;
    line-height: 1.8;
    color: #1a1a2e;
    background: #f8f9fc;
}

.page-wrapper {
    max-width: 960px;
    margin: 40px auto;
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
    overflow: hidden;
}

/* ─── ヘッダー ───────────────────────────────────────────────────────────── */
.report-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: #ffffff;
    padding: 48px 56px 40px;
}

.report-header h1 {
    font-size: 1.75rem;
    font-weight: 700;
    line-height: 1.4;
    margin-bottom: 16px;
    letter-spacing: 0.02em;
}

.report-meta {
    font-size: 0.85rem;
    color: #a8c0e8;
    line-height: 2;
}

/* ─── 目次 ───────────────────────────────────────────────────────────────── */
.toc-section {
    background: #f0f4ff;
    border-left: 4px solid #0f3460;
    padding: 28px 40px 28px 48px;
}

.toc-section h2 {
    font-size: 1rem;
    font-weight: 700;
    color: #0f3460;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.toc-section ul {
    list-style: none;
    padding: 0;
    columns: 2;
    column-gap: 32px;
}

.toc-section li {
    padding: 3px 0;
    break-inside: avoid;
}

.toc-section a {
    color: #1a1a2e;
    text-decoration: none;
    font-size: 0.9rem;
}

.toc-section a:hover { color: #0f3460; text-decoration: underline; }

/* ─── 本文コンテンツ ─────────────────────────────────────────────────────── */
.content {
    padding: 40px 56px 56px;
}

/* ─── 見出し ─────────────────────────────────────────────────────────────── */
h1, h2, h3, h4 {
    font-weight: 700;
    line-height: 1.4;
}

h2 {
    font-size: 1.35rem;
    color: #0f3460;
    border-bottom: 2px solid #0f3460;
    padding-bottom: 8px;
    margin: 48px 0 20px;
}

h3 {
    font-size: 1.1rem;
    color: #16213e;
    border-left: 4px solid #e94560;
    padding-left: 12px;
    margin: 32px 0 14px;
}

h4 {
    font-size: 1rem;
    color: #1a1a2e;
    margin: 24px 0 10px;
}

/* ─── 段落・リスト ───────────────────────────────────────────────────────── */
p { margin: 0 0 14px; }

ul, ol { margin: 0 0 14px 24px; }
li { margin-bottom: 6px; }

/* ─── テーブル ───────────────────────────────────────────────────────────── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0 28px;
    font-size: 0.88rem;
}

th {
    background: #0f3460;
    color: #ffffff;
    font-weight: 600;
    padding: 10px 14px;
    text-align: left;
}

td {
    padding: 9px 14px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td { background: #f8faff; }
tr:hover td { background: #eef2ff; }

/* ─── 強調 ───────────────────────────────────────────────────────────────── */
strong { color: #0f3460; font-weight: 700; }
em { font-style: normal; color: #e94560; font-weight: 600; }

/* ─── エグゼクティブサマリーボックス ─────────────────────────────────────── */
.content > h2:first-of-type + p,
.executive-summary {
    background: #f0f4ff;
    border-radius: 8px;
    padding: 20px 24px;
    margin-bottom: 20px;
}

/* ─── 水平線 ─────────────────────────────────────────────────────────────── */
hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 40px 0;
}

/* ─── コードブロック ─────────────────────────────────────────────────────── */
code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    background: #f1f5f9;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 0.88em;
    color: #e94560;
}

pre code {
    display: block;
    padding: 16px;
    overflow-x: auto;
    color: #1a1a2e;
}

/* ─── リンク ─────────────────────────────────────────────────────────────── */
a { color: #0f3460; }
a:hover { color: #e94560; }

/* ─── フッター ───────────────────────────────────────────────────────────── */
.report-footer {
    background: #1a1a2e;
    color: #a8c0e8;
    text-align: center;
    padding: 20px;
    font-size: 0.82rem;
}

/* ─── 印刷スタイル ───────────────────────────────────────────────────────── */
@media print {
    body { background: #fff; font-size: 12px; }
    .page-wrapper { box-shadow: none; border-radius: 0; margin: 0; }
    .report-header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    h2 { page-break-before: auto; }
    table { page-break-inside: avoid; }
    a { color: inherit; text-decoration: none; }
    a[href]::after { content: " (" attr(href) ")"; font-size: 0.75em; color: #666; }
}
"""

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
{css}
  </style>
</head>
<body>
  <div class="page-wrapper">
    <header class="report-header">
      <h1>{title}</h1>
      <div class="report-meta">
        <div>作成日：{date}</div>
        <div>調査対象：{target}</div>
        <div>調査範囲：{scope}</div>
      </div>
    </header>
    <main class="content">
{body}
    </main>
    <footer class="report-footer">
      <p>© 2026 観光業AIエージェント活用調査プロジェクト &nbsp;|&nbsp; 調査日：{date}</p>
    </footer>
  </div>
</body>
</html>
"""


def md_to_html(md_text: str) -> str:
    """Markdown テキストを HTML 断片に変換する。"""
    md = markdown.Markdown(
        extensions=[
            TableExtension(),
            TocExtension(baselevel=1),
            "extra",
            "nl2br",
            "sane_lists",
        ],
        output_format="html",
    )
    return md.convert(md_text)


def extract_meta(md_text: str) -> dict:
    """先頭の **key：value** 行からメタ情報を抽出する。"""
    meta = {
        "title": "観光業（OTA・Google等）におけるAIエージェント活用 総合調査レポート",
        "date": "2026年3月2日",
        "target": "オンライン旅行業（OTA）およびGoogle等プラットフォームにおけるAIエージェント活用",
        "scope": "技術の誕生（1990年代）〜現在（2026年）および今後3〜5年の展望",
    }
    for line in md_text.splitlines()[:10]:
        line = line.strip("*").strip()
        if line.startswith("作成日："):
            meta["date"] = line.replace("作成日：", "").strip()
        elif line.startswith("調査対象："):
            meta["target"] = line.replace("調査対象：", "").strip()
        elif line.startswith("調査範囲："):
            meta["scope"] = line.replace("調査範囲：", "").strip()
    return meta


def strip_header_block(md_text: str) -> str:
    """先頭の H1 タイトル・メタ情報ブロック・最初の --- を除去して本文を返す。"""
    lines = md_text.splitlines()
    # H1・メタ行・最初の区切り線をスキップ
    start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---" and i > 0:
            start = i + 1
            break
    return "\n".join(lines[start:])


def build_html(md_text: str) -> str:
    meta = extract_meta(md_text)
    body_md = strip_header_block(md_text)
    body_html = md_to_html(body_md)

    return HTML_TEMPLATE.format(
        title=meta["title"],
        date=meta["date"],
        target=meta["target"],
        scope=meta["scope"],
        css=CSS,
        body=body_html,
    )


def generate_pdf(html_path: Path, pdf_path: Path) -> bool:
    """weasyprint で PDF を生成する。利用不可の場合は False を返す。"""
    try:
        from weasyprint import HTML as WH  # type: ignore

        WH(filename=str(html_path)).write_pdf(str(pdf_path))
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"  [警告] PDF 生成中にエラーが発生しました: {e}", file=sys.stderr)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="レポートを HTML/PDF に変換する")
    parser.add_argument("--pdf", action="store_true", help="PDF も生成する")
    args = parser.parse_args()

    # ── Markdown 読み込み ──────────────────────────────────────────────────
    if not INPUT_MD.exists():
        print(f"[ERROR] 入力ファイルが見つかりません: {INPUT_MD}", file=sys.stderr)
        sys.exit(1)

    md_text = INPUT_MD.read_text(encoding="utf-8")
    print(f"入力ファイル : {INPUT_MD}")

    # ── HTML 生成 ──────────────────────────────────────────────────────────
    html_content = build_html(md_text)
    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    size_kb = OUTPUT_HTML.stat().st_size / 1024
    print(f"HTML 出力    : {OUTPUT_HTML}  ({size_kb:.1f} KB)")

    # ── PDF 生成（オプション） ────────────────────────────────────────────
    if args.pdf:
        print("PDF 生成中   : weasyprint を使用...")
        ok = generate_pdf(OUTPUT_HTML, OUTPUT_PDF)
        if ok:
            size_kb = OUTPUT_PDF.stat().st_size / 1024
            print(f"PDF 出力     : {OUTPUT_PDF}  ({size_kb:.1f} KB)")
        else:
            print(
                "  [情報] weasyprint が利用できないため PDF 生成をスキップしました。\n"
                "  PDF が必要な場合は以下を実行してください:\n"
                "    pip install weasyprint\n"
                "    python3 generate_report.py --pdf"
            )
    else:
        print("\n[ヒント] PDF も生成する場合は --pdf オプションを付けて実行してください:")
        print(f"  python3 {Path(__file__).name} --pdf")

    print("\n完了しました。")


if __name__ == "__main__":
    main()
