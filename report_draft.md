# 観光業（OTA・Google等）におけるAIエージェント活用 総合調査レポート（草稿）

**作成日：2026年3月2日**
**調査対象：オンライン旅行業（OTA）およびGoogle等プラットフォームにおけるAIエージェント活用**
**調査範囲：技術の誕生（1990年代）〜現在（2026年）および今後3〜5年の展望**

---

## エグゼクティブサマリー

旅行業界は現在、インターネットの誕生以来最大の変革期を迎えている。1990年代のOTA（オンライン旅行代理店）誕生から30年を経て、2022〜2023年のLLM（大規模言語モデル）の一般公開を契機に、AIエージェントが旅行計画・予約・管理の全工程を自律的に担う時代が現実のものとなりつつある。

**主要な調査発見事項：**

1. **市場規模：** グローバルOTA市場は2024年に約2,532億ドル（CAGR 6.74%で成長中）。旅行特化型AI技術市場は2030年に100〜140億ドル規模に達する見込み（複数調査機関の予測が一致）。

2. **技術成熟度：** AIパーソナライズ推薦・チャットボット・動的価格設定は「生産性の安定期」に到達し業界標準化。一方、完全自律型旅行予約はまだ「過度な期待のピーク」段階にあり、商用主流化は2028〜2030年と予測される。

3. **競争構造：** Booking Holdings（時価総額約1,883億ドル）とExpedia Group（同214億ドル）の2強が市場をリードするが、GoogleのAgentic Booking参入がOTA各社の最大の脅威となっている。

4. **日本市場の特殊性：** 旅館・ホテル業の75.5%が人手不足という深刻な構造的課題があり、AI活用の必要性は欧米以上に高い。楽天トラベルのAIホテル探索やじゃらんの分析工数削減（最大1/15）など実用化が進んでいる。

5. **規制リスク：** EU AI Act（2026年8月完全施行）・GDPR・各国プライバシー法への対応コストが普及の阻害要因となりうる。

---

## 目次

1. [技術・市場の誕生背景](#1-技術市場の誕生背景)
2. [主要な技術的マイルストーン（年表）](#2-主要な技術的マイルストーン年表)
3. [市場規模の変遷と主要プレイヤーの興亡](#3-市場規模の変遷と主要プレイヤーの興亡)
4. [国内外の最新導入事例（2023年以降）](#4-国内外の最新導入事例)
5. [現在進行中の技術トレンド（上位5つ）](#5-現在進行中の技術トレンド)
6. [主要ベンダーの最新戦略・製品ロードマップ](#6-主要ベンダーの最新戦略)
7. [普及を加速・阻害した要因](#7-普及を加速阻害した要因)
8. [現時点での技術的成熟度](#8-現時点での技術的成熟度)
9. [業界アナリストの予測・提言](#9-業界アナリストの予測提言)
10. [今後3〜5年の市場変化シナリオ](#10-今後35年の市場変化シナリオ)
11. [総合考察と提言](#11-総合考察と提言)
12. [参考文献・情報源](#12-参考文献情報源)

---

## 1. 技術・市場の誕生背景

### 1-1. OTA（Online Travel Agency）の登場とデジタル化の流れ

オンライン旅行代理店（OTA）の登場は、1990年代のインターネット普及と不可分の関係にある。それ以前、旅行の予約は実店舗の旅行代理店に出向くか、航空会社や鉄道会社に電話で問い合わせるしかなく、価格の透明性も低く、消費者の選択肢は限られていた。

インターネットが一般家庭にも普及し始めた1990年代後半、旅行業界に革命をもたらす企業群が相次いで登場した：

- **Travelocity（1996年）：** アメリカン航空傘下のSabre部門内で設立。世界初の大規模コンシューマー向けオンライン旅行予約サービスの一つ。
- **Expedia（1996年）：** マイクロソフト社内プロジェクトとしてRichard Barton率いるチームが創設。2001年に独立・Nasdaq上場。
- **Priceline（1997年）：** 「Name Your Own Price」という斬新なモデルで登場。後にBooking.comを傘下に収め世界最大のOTAグループに成長。
- **Airbnb（2008年）：** 民泊マーケットプレイスという革新的モデルで創業。ホテル業界に根本的な変革をもたらした。

2000年のドットコム崩壊で多くのスタートアップが倒産したが、生存者は2002年以降の経済回復期に急速に力をつけ、伝統的旅行代理店からの市場シェア移行を加速させた。

### 1-2. 旅行業界でのAI・ML活用の始まり

旅行業界でのデータ活用は、1960年代にアメリカン航空が開発したSabre等のGDS（グローバル流通システム）に始まる。本格的なAI・機械学習の活用は2010年代に加速した：

- **2010年代前半：** ビッグデータ技術の成熟に伴い、OTA各社がユーザーの行動データを大規模に収集・分析。Booking.comが協調フィルタリングを実装。
- **2015年頃：** 200以上のコンテキスト変数をリアルタイムに処理して個人向け推薦を行うシステムが登場。
- **2018年：** Airbnbがディープラーニングを用いた宿泊施設ランキングシステムを実装。

### 1-3. AIエージェント（自律型AI）が旅行業界に登場した背景

2022年11月30日、OpenAIがChatGPTを一般公開したことが、旅行業界のAIエージェント化の起爆剤となった。旅行業界においてこの変化が特に重要だった理由：

- 旅行計画は本質的に多段階の意思決定プロセスであり、AIエージェントの「マルチステップ推論」能力と親和性が高い
- 旅行中のリアルタイムな状況変化（フライト遅延・天候変化など）への即時対応を自動化できるメリットが明確
- コロナ後の個人旅行（FIT）化により、個別最適化された旅行計画へのニーズが急増

---

## 2. 主要な技術的マイルストーン（年表）

### 1990年代：OTA誕生期

| 年 | 出来事 |
|---|---|
| 1987 | Amadeus GDS設立（エールフランス・ルフトハンザ等が共同出資） |
| 1996 | **Travelocity**・**Expedia**・**Booking.com**が相次いで設立 |
| 1997 | **Priceline**設立（独自の「Name Your Own Price」モデル） |
| 1999 | Trip.com（Ctrip）が中国で設立 |
| 2000 | **TripAdvisor**設立 |

### 2000年代：市場確立とモバイル化

| 年 | 出来事 |
|---|---|
| 2005 | PricelineがBooking.comを買収（約1.35億ドル） |
| 2007 | iPhoneローンチ、モバイル旅行予約時代の幕開け |
| 2008 | **Airbnb**設立（Brian Chesky・Joe Gebbia・Nathan Blecharczyk） |

### 2010年代：ビッグデータとMLの実装期

| 年 | 出来事 |
|---|---|
| 2010 | Google、ITA Softwareを7億ドルで買収（フライト検索機能の基盤取得） |
| 2011 | Booking.com、機械学習を活用したA/Bテストフレームワークを全面展開 |
| 2018 | Google Duplex発表（AIによる自律的な電話予約デモ、旅行業界に衝撃） |
| 2019 | BERT（Googleの大規模言語モデル）が旅行検索クエリの理解に革新をもたらす |

### 2020年代：LLMとAIエージェント時代

| 年 | 出来事 |
|---|---|
| 2020 | COVID-19パンデミック。旅行業界の市場規模が60〜70%縮小 |
| 2022 | **ChatGPT（GPT-3.5）**、OpenAIが一般公開（11月30日） |
| 2023 | GPT-4リリース。Expedia・Booking.com・TripAdvisor等がLLM統合を競って発表 |
| 2023 | **楽天トラベル**AIエージェント試験、**Mindtrip**700万ドルシード調達 |
| 2024 | **Expedia「Romie」**発表（5月）、**Airbnb** AI詐欺検知で不正予約40%削減 |
| 2024 | **Google**、Geminiを活用した旅行計画機能を強化 |
| 2025 | **楽天トラベルAIホテル探索**正式提供開始（9月）、**Google** Agentic Booking発表 |
| 2025 | **Booking.com** Agentic AI Innovation発表、**KAYAK** AI Mode（ChatGPT統合）リリース |
| 2026 | アジェンティックAIの本格商用化元年（PhocusWright予測） |

---

## 3. 市場規模の変遷と主要プレイヤーの興亡

### 3-1. OTA市場全体の規模推移

| 年 | 市場規模（推計） | 備考 |
|---|---|---|
| 2019 | 約8,000億ドル（グローバル旅行市場全体） | コロナ前のピーク |
| 2020 | 約2,200〜2,400億ドルに急縮小 | COVID-19による移動制限の直撃 |
| 2022 | 約5,000〜6,000億ドル | リベンジ旅行による急回復 |
| 2024 | OTA市場単独で約2,532億ドル | CAGR 7.9%で成長中 |
| 2033予測 | 約4,753億ドル（OTA市場） | CAGR 6.74%で拡大継続 |

**主要プレイヤーの2024〜2025年売上高：**
- **Booking Holdings：** 2025年通年収益269億ドル（過去最高）、時価総額約1,883億ドル
- **Expedia Group：** 約140億ドル（過去最高売上を更新）
- **Airbnb：** 約110億ドル規模（時価総額約817億ドル）
- **Trip.com Group：** 約70億ドル規模

Booking HoldingsとExpedia Groupの2社で、グローバルOTA市場シェアの40%以上を占める。

### 3-2. 主要プレイヤーの戦略と競合構造

**Booking Holdings（本拠地：米コネチカット州ノーウォーク）：**
Booking.com・Priceline・Kayak・Agoda等を傘下に持つ最大グループ。2024年のAI・コネクテッドトリップへの再投資額は1億7,000万ドル。早期からA/Bテストと機械学習を組み合わせたデータドリブン経営を確立し、ヨーロッパ市場で特に支配的地位を築いた。

**Expedia Group（本拠地：米ワシントン州シアトル）：**
Expedia・Hotels.com・Vrbo・trivago等を傘下に持つ第2位グループ。2024年のRomie発表と積極的なAI戦略を打ち出し、2025年にクラウドインフラへの技術移行を完了してAIネイティブな開発基盤を確立した。

**Airbnb（本拠地：米カリフォルニア州サンフランシスコ）：**
CEOのBrian CheskyはAIを会社の「第四の柱」として位置づけ、「AIネイティブアプリ」への転換を宣言。トラフィックの90%がAIインターミディアリーを経由しない直接訪問であることが相対的な強みとなっている。

**Google（本拠地：米カリフォルニア州マウンテンビュー）：**
2010年にITA Software（フライトデータ処理）を7億ドルで買収し、Google Flights・Hotels・Mapsを統合したエコシステムを構築。2025年後半、AI Mode内でのAgentic Bookingを発表。ただし「OTAになる意図はない」と明言し協働モデルを模索している。

---

## 4. 国内外の最新導入事例

### 4-1. 日本国内の主要事例

#### 楽天トラベル：AIエージェント「楽天トラベルAIホテル探索」

楽天グループは2025年9月22日、AIエージェント「楽天トラベルAIホテル探索」の提供を開始した。

**主な特徴：**
- 自然言語を理解して要望を的確に捉える処理能力
- 楽天トラベルの分析データ＋ウェブ検索結果の両方を反映
- ユーザーのニーズを確認し、最適な宿泊施設を最大30軒ピックアップ
- スマートフォン用ページから全ユーザーが無料で利用可能

#### じゃらん（リクルート）：インバウンドマーケティング分析AI

リクルートのじゃらんリサーチセンターは2025年2月、生成AIを活用したインバウンドマーケティング支援の実証実験を熱海市で実施。マーケティング分析工数を**最大15分の1（約93%削減）**に削減することを実証した。

#### 大阪観光局：多言語AIチャットボット（JTB・Kotozna共創）

大阪公式観光情報サイト「osaka-info」に、日本初となる多言語生成AIチャットボットを導入。OpenAIのChatGPTを活用し、**20言語以上**に対応する観光情報提供を24時間365日自動化した。

#### 門司港レトロ観光案内所：問い合わせ対応AIの導入

生成AIを導入し、観光客からの問い合わせの**52%をAIが処理**できる体制を実現。スタッフの業務負担を大幅に軽減した。

#### 観光庁：生成AI活用手引書の整備と実証事業

令和7年度（2025年度）の「観光DX推進による地域活性化モデル実証事業」では、生成AI活用モデルとして**14件の事業**が採択され、国を挙げての観光業AI活用が推進されている。

### 4-2. 海外OTAの主要事例

#### Expedia Group：AIアシスタント「Romie」

2024年5月に発表された「Romie」は、旅行エージェント・コンシェルジュ・個人アシスタントの3役を担う次世代AI。2025年Q4にはAI活用が粗利益**11%増**（270億ドル）に貢献した。

**主な機能：**
- iMessage・WhatsAppグループチャットへの統合
- 自然言語によるスマート検索（「海の見えるルーフトップ付き」等）
- 天候変化・遅延時の代替プラン提案
- ユーザーの好みを継続学習するパーソナライゼーション

Expediaグループ全体でAIチャットボットが累計2,900万件以上の対話を処理している。

#### Booking.com：GenAIツール群の体系的展開

2023〜2025年にかけて段階的にリリース：

**2023〜2024年：**
- AI Trip Planner（6言語以上でグローバル展開）
- Smart Filter（自然言語による宿泊施設フィルタリング）
- Review Summaries（多数のレビューをAIが重要ポイント別に要約）

**2025年（Agentic AI）：**
- Smart Messenger & Auto-Reply（ホスト・ゲスト間のコミュニケーションを自律処理）
- AI Voice Support（音声による旅行管理、英語・ドイツ語対応）
- ChatGPT Integration（ChatGPT内からBooking.com施設を検索・閲覧可能）

#### Airbnb：AI第四の柱（AIネイティブアプリへの転換）

**主なAI活用：**
- パーソナライズされたレコメンデーション（AIレコメンデーション試験でユーザー満足度30%向上・予約完了率25%上昇）
- AI詐欺検知システム（2024年導入、不正予約を**40%削減**）
- Photo Tour AIツール（コンピュータビジョンによる施設写真の自動タグ付け）
- GamePlanner.AI買収（2023年、AI能力の強化を加速）

---

## 5. 現在進行中の技術トレンド（上位5つ）

### トレンド1：生成AI・LLMを活用した旅行プランニングエージェント

LLMを中核としたAIエージェントが旅行計画の全工程を担う方向で急速に発展している。**米国のアクティブ旅行者の58%**がAIを何らかの形で利用しており、ミレニアル世代の**58%**が情報過多対策にAIを活用している（Gen Zの45%、ベビーブーマーの11%と比較）。

**代表的な展開：**
- Expedia Romie（自然言語によるエンドツーエンドの旅行管理）
- Booking.com AI Trip Planner（6言語以上でグローバル展開）
- Google Flight Deals（Gemini AI活用の自然言語フライト検索、200カ国以上・60言語以上）
- KAYAK AI Mode（ChatGPT統合による自然言語旅行計画、2025年10月リリース）

### トレンド2：マルチモーダルAI（画像・動画・音声認識）の旅行体験への応用

テキストだけでなく、画像・動画・音声を統合的に処理するマルチモーダルAIが旅行体験に新たな次元をもたらしている。

**主な活用事例：**
- **Mindtrip**：TikTok/YouTube動画・Instagramリール・Redditの投稿から旅程を自動生成（2024年7月リリース）
- **Expedia Trip Matching**：Instagram Reelsをもとに旅行イテラリーを生成し、Expediaで直接予約
- **Booking.com AI Voice Support**：音声による旅行管理
- グローバルマルチモーダルAI市場は2024年に16億ドルと評価され、2025〜2034年のCAGRは**32.7%**で成長予測

### トレンド3：リアルタイム価格最適化・AIイールドマネジメント

AIを活用した動的価格設定が観光業全体で標準化しつつある。AIレベニューマネジメントシステムがホテル収益を**最大10%**向上させることが報告されており、AIチャットボットが顧客対応の**80%**を処理することで人件費も削減されている。

### トレンド4：パーソナライゼーション技術の進化（ハイパーパーソナライゼーション）

AIによるパーソナライゼーションは3世代の進化を遂げている：
1. **第1世代**（2015〜2020年）：過去の閲覧・予約履歴に基づく協調フィルタリング
2. **第2世代**（2020〜2023年）：機械学習による多変数モデル
3. **第3世代**（2023年〜現在）：LLMベースのリアルタイム対話型、グループ旅行・旅行中の動的更新に対応

Expediaは年間**8,000億件以上のAI予測**を処理しており、詐欺検知から動的旅行推薦まで多岐にわたる個別化サービスを提供している。

### トレンド5：Voice AI・チャットボットから自律型エージェントへの進化

旅行AIは単純な質問応答チャットボットから、リアルタイムで予約・変更・問題解決を自律的に実行する「アジェンティックAI」へと急速に進化している：

1. **チャットボット時代**（2016〜2022年）：ルールベースのFAQ対応
2. **生成AIアシスタント時代**（2022〜2024年）：LLMを活用した文脈理解・自然言語対話
3. **アジェンティックAI時代**（2025年〜）：自律的な意思決定・行動実行・継続学習

**MCP（Model Context Protocol）の登場：** 2025年に台頭したMCPは「AIエージェントのUSB-C規格」と称され、AIアシスタントが外部データソース・予約システムと標準的に通信できる基盤を提供している。

---

## 6. 主要ベンダーの最新戦略・製品ロードマップ

### 6-1. Google：Gemini × 旅行体験の全面統合

| 製品/機能 | 概要 | 展開時期 |
|---|---|---|
| Google Flight Deals | Gemini AIによる自然言語フライト検索 | 2025年（200カ国以上） |
| AI Mode Travel Canvas | 旅行全体をリアルタイムデータで管理するAIパネル | 2025年 |
| Agentic Hotel/Flight Booking | AIモード内でのホテル・フライト自律予約 | 開発中（2026年目標） |

GoogleのAI旅行予約機能の発表を受け、Booking Holdings株が4〜7%下落。ただし、Googleは「OTAになる意図はない」と繰り返し明言している。

### 6-2. Booking Holdings：コネクテッドトリップ戦略とAI全社展開

| ブランド | AI製品/機能 | 特徴 |
|---|---|---|
| Booking.com | AI Trip Planner | 6言語以上でグローバル展開 |
| Booking.com | Smart Messenger / Auto-Reply | ホスト・ゲスト間のAI自律コミュニケーション |
| KAYAK | AI Mode（ChatGPT統合） | 2025年10月リリース |
| Priceline | Penny（音声AIアシスタント） | 旅行履歴に基づくパーソナライズド推薦 |

2025年Q2時点で、コネクテッドトリップ取引が**前年比40%増**、複数サービスを使うユーザーは単一サービスユーザーより**25%多く**支出している。

### 6-3. 注目スタートアップ

**Mindtrip（米国）：**
- 2024年累計1,900万ドル調達（Costanoa Ventures・Forerunner Ventures等）
- PhocusWire Hot 25 Travel Startup for 2025、TravelTech Breakthrough AI Company of the Year（2025年）受賞
- TikTok/YouTube動画・Instagramリール・Redditポストからのイテラリー自動生成が主力機能

**Layla（欧州）：**
- 2024年2月にFLYR支援のAIイテラリー生成ボット「Roam Around」を買収
- Booking.com・Skyscannerとのパートナーシップで予約機能を統合

---

## 7. 普及を加速・阻害した要因

### 7-1. COVID-19の影響とデジタル化の加速

2020年のCOVID-19パンデミックは旅行業界史上最大の危機であると同時に、デジタル変革を加速させる触媒にもなった。

- **危機の規模：** 2020年のグローバル旅行市場はピーク時比60〜70%の縮小
- **逆説的な加速効果：** セルフサービス化・非接触型サービスへの需要急増がAI自動化の投資を正当化。コロナ後のリベンジ旅行（2022〜23年）で個人旅行（FIT）需要が急増し、個別最適化AIへのニーズが拡大
- **回復の速度：** UN Tourismによると、2024年の国際観光は2019年比99%まで回復し、14億人の国際観光客を記録（前年比11%増）

### 7-2. 技術的障壁と突破要因

**主要な技術的障壁：**

1. **自然言語処理（NLP）の限界（〜2022年）：** 従来のチャットボットはルールベースで複雑なクエリを正しく理解できなかった。GPT-3.5/4の登場が真のブレークスルーとなった。

2. **リアルタイムデータ連携の難しさ：** GDS・APIとのインテグレーションが複雑で、「ハルシネーション（幻覚）」問題によりAIが実際に存在しない価格や便を提案するリスクがある。

3. **消費者の信頼不足：** Skiftの「State of Travel 2025」レポートによると、AIが自律的に予約・変更することを「完全に任せられる」と答えた旅行者はわずか**2%**。一方、**40%**の旅行者が旅行計画にAIツールを利用した経験を持つという矛盾した状況が続いている。

**突破要因：**
- LLMの文脈理解能力の飛躍的向上（GPT-3.5→4→4o→o1→o3）
- 旅行特化ファインチューニングと検索拡張生成（RAG）の実用化
- マルチモーダルAI（画像からの旅先推薦）の実用化
- MCPによる標準的なAI-API統合基盤の整備

### 7-3. 規制・プライバシー問題

**GDPR（EU一般データ保護規則）の影響：**
OTAが欧州ユーザーのデータを活用したAIパーソナライゼーションを行う際に重大な制約となっている。2025年のGDPRの制裁金総額は2024年の12億ユーロから**23億ユーロに38%増加**した。

**EU AI法（EU AI Act）：**
2024年に成立。「高リスク」AIシステムには透明性要件・バイアス検出・人間監視の義務を課す。最大罰則は3,500万ユーロまたは全世界売上高の7%（2026年8月完全施行）。

---

## 8. 現時点での技術的成熟度

Gartnerの2025年AIハイプサイクルと旅行業界の実態を照合した成熟度評価：

| 機能 | 成熟度フェーズ | 業界への普及度 | 主な事例 |
|---|---|---|---|
| AIパーソナライズ推薦 | 生産性の安定期 | ◎ 業界標準 | Booking.com（予約転換率23%向上）・Airbnb（100以上の変数を評価）・TripAdvisor（収益2〜3倍向上） |
| チャットボット・カスタマーサービス | 生産性の安定期 | ◎ 大手は本番、中小は実装中 | Expedia Romie（累計2,900万件対話）・HotelPlanner（1日1万件の電話処理） |
| 動的価格設定 | 生産性の安定期 | ◎ 航空・ホテルで標準化 | AirbnbのSmart Pricing・Kayakの価格予測機能 |
| 自律型旅行予約 | 過度な期待のピーク | △ 概念実証〜限定試験 | Google Agentic Booking（開発中）・Expedia Romieは「コパイロット」モデルを採用 |
| マルチモーダル旅行計画 | 黎明期〜過度な期待のピーク | △ 実験的段階 | Mindtrip（動画から旅程生成）・Expedia Trip Matching（Instagram連携） |

**Gartner予測：** 「Machine Customers（機械顧客）」概念は2030年には80億台のデバイスに拡大する見込みだが、旅行の完全自律予約が主流になるのは2028〜2032年以降と予測される。

---

## 9. 業界アナリストの予測・提言

### 9-1. 旅行×AI市場規模予測（各社比較）

| 調査機関 | 2024年市場規模 | 2030年市場規模 | CAGR |
|---|---|---|---|
| MarketsandMarkets | 29.5億ドル | 133.8億ドル | 28.7% |
| Grand View Research | 33.7億ドル | 138.7億ドル | 26.7% |
| PhocusWright（旅行市場全体） | - | 1.67兆ドル（2026年） | - |

### 9-2. PhocusWrightの予測・提言（2025〜2026年）

- **旅行企業の61%以上**がアジェンティックAIの実験中または展開中
- 2026年がアジェンティックAIの年（「単なるコンテンツ出力ではなく、実際のタスクを完遂するGenAI」として定義）
- AI予約機能の「成熟版」は2年以内に登場する見通し（Expedia幹部発言）
- 「コネクティビティの時代以来最大の変革」と位置づけ、AIを無視する既存プレイヤーへの警告

### 9-3. Gartnerの予測・提言

- 2025年世界AI支出：**1.5兆ドル**、2026年には**2兆ドル超**へ
- 2028年までに、企業アプリケーションの**33%**に自律型エージェントが組み込まれ、作業決定の**15%**が自動的に行われる見込み

### 9-4. 日本国内の業界動向・観光庁の政策提言

- 旅館・ホテル業の**75.5%**が正社員不足（帝国データバンク調査、全業種でトップ）という深刻な構造的課題がAI導入を加速
- 日本の生成AI利用率は**27.0%**（中国81.2%・米国68.8%と比較して低い水準）
- 観光庁が令和7年度の実証事業で生成AI活用モデル14件を採択

---

## 10. 今後3〜5年の市場変化シナリオ（2026〜2030年）

### 10-1. 楽観シナリオ：AIエージェントが旅行体験を完全変革

**主要な前提条件：**
- AIエージェント技術の急速な成熟（精度・自律性・信頼性の向上）
- OTA・ホテル・航空会社のMCP対応が急速に普及
- 消費者のAI自律エージェントへの信頼が急激に高まる

**2027〜2028年の変化：**
- 旅行者の大半がAIエージェントに旅行計画・予約・変更の全工程を任せるようになる
- 「検索→比較→予約」というプロセスが「希望を伝える→AIが実行する」という体験に置き換わる

**2030年の到達点：**
- 旅行市場に占めるAIエージェント経由の取引比率が**50%超**に達する可能性
- デジタルアイデンティティとAIエージェントの統合により、空港・ホテルのチェックインが完全自動化

### 10-2. 中立シナリオ：段階的な機能強化と人間との協働（最も蓋然性が高い）

**主要な前提条件：**
- AI技術は進歩するが、自律型エージェントへの完全信頼は一部ユーザーに限定
- OTAは既存の強みを活かしながらAIを補完的ツールとして活用
- 規制環境が徐々に整備され、AI活用の範囲を段階的に拡大

**2030年の到達点：**
- AIアシスタントが旅行計画の「パートナー」として定着（完全自律ではなく、人間の承認が前提）
- 旅行企業の生産性がAI活用により**30〜50%向上**
- 観光業のAI関連技術市場が2030年に**100〜140億ドル**規模で安定成長

### 10-3. 悲観シナリオ：規制強化・プライバシー問題による普及鈍化

**主要なリスク要因：**
- EU AI Act（2026年8月完全施行）の厳格運用
- 旅行AIにおける個人データ漏洩・誤った推薦による事故の顕在化
- 各国の競合するAI規制が企業のグローバル展開を阻害

**2030年の到達点：**
- AIは観光業の「補助ツール」に留まり、自律的な旅行エージェントの普及は限定的
- AIガバナンスソフトウェア市場が2030年に**12.1億ドル**規模に拡大し、コンプライアンス対応コストが業界全体に重くのしかかる

---

## 11. 総合考察と提言

### 11-1. 旅行業界AIエージェントの競争軸

現在、旅行業界のAIエージェント競争は3つの軸で展開されている：

1. **既存OTA（Booking Holdings・Expedia）：** 膨大な取引データとグローバル在庫を武器に、AIによるパーソナライゼーションを深化させる戦略。Romieのようなコパイロット型AIで、人間の意思決定を支援しながら自律化を段階的に進める。

2. **テックジャイアント（Google・Apple・Meta）：** 検索・地図・SNSとの統合により、旅行計画の上流（インスパイレーション段階）から予約完了までの全プロセスを自社エコシステム内に取り込もうとする。Google Canvasはその象徴的な戦略。

3. **AI-First スタートアップ（Mindtrip・Layla等）：** GenAIネイティブな設計で差別化を図るが、OTAや大手テック企業との競争で資金・データ量の面で劣位。M&Aターゲットとなるか、ニッチ特化で生き残るかの二択に直面。

### 11-2. 残された技術的課題

旅行AIエージェントが「コパイロット」から「オートパイロット」に移行するための残課題：

1. **ハルシネーション（幻覚）の解消：** リアルタイム価格・在庫情報への確実なアクセスと、LLMの「知ったかぶり」問題の解決
2. **信頼構築：** キャンセル・返金・変更時の責任範囲の明確化。エラー発生時の人間へのescalation設計
3. **規制対応：** GDPR・EU AI Act・各国プライバシー法への対応コストの吸収
4. **エコシステム連携：** GDS・PMS・CRSなど旧来のレガシーシステムとのAPI統合の標準化

### 11-3. 日本市場への特別提言

日本の観光業界は「旅館・ホテル業の75.5%が人手不足」という深刻な構造的課題を抱えており、AIによる業務効率化の必要性は欧米以上に高い。一方で生成AI利用率（27%）の低さが示すように、技術普及には時間を要する可能性がある。

**提言：**
1. **即効性のある活用から始める：** 多言語チャットボット（大阪観光局のモデル）や問い合わせ対応AI（門司港レトロのモデル）は即座にROIを出しやすい
2. **インバウンド対応を最優先：** AI多言語対応はインバウンド観光客の急増に対応する緊急ニーズ。じゃらんの分析工数1/15削減モデルは横展開可能
3. **観光庁のモデル事業を活用：** 令和7年度の14件の実証事業の成果を業界全体で共有する仕組みを構築
4. **段階的な自律化を選択：** 完全自律型AIへの急速な移行よりも、人間と協働するコパイロット型AIを先行させることが日本市場では現実的

### 11-4. 最重要の示唆：情報過多を解決するAIの構造的ニーズ

旅行者が一回の旅行予約に閲覧するウェブページ数は平均**141ページ**（米国では277ページ）に達しており、この「情報過多」の問題を解決するAIエージェントの需要は構造的に存在する。旅行業界でAIエージェントが普及するのは、技術的な可能性があるからではなく、**消費者が強く必要としているから**である。

この構造的ニーズを前提にすると、AIエージェントが旅行業界に与えるインパクトは、中立シナリオにおいてでさえ、従来のOTAのビジネスモデルを根本的に変容させる可能性が高い。2026年〜2028年の期間が、業界の競争構造を決定づける最重要の変曲点となる。

---

## 12. 参考文献・情報源

### 市場調査・業界レポート

- [MarketsandMarkets: AI in Tourism Market](https://www.marketsandmarkets.com/Market-Reports/ai-in-tourism-market-114969018.html)
- [Grand View Research: AI in Tourism Market Report 2030](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-tourism-market-report)
- [Grand View Research: Online Travel Agencies Market Size | Industry Report, 2030](https://www.grandviewresearch.com/industry-analysis/online-travel-agencies-market-report)
- [GM Insights: Online Travel Agency Market Size, Growth Analysis 2025-2034](https://www.gminsights.com/industry-analysis/online-travel-agency-market)
- [Phocuswright 2026グローバル旅行市場予測 - TravelAge West](https://www.travelagewest.com/Industry-Insight/Business-Features/phocuswright-travel-forward-2026)

### Phocuswright・PhocusWire

- [Phocuswright：旅行企業の61%がアジェンティックAIを実験・展開中](https://www.phocuswright.com/Travel-Research/Research-Updates/2026/61-of-travel-business-surveyed-experimenting-with-or-scaling-agentic-ai)
- [PhocusWrightアナリストによる2026年予測 - PhocusWire](https://www.phocuswire.com/phocuswright-analyst-travel-predictions-2026)
- [Phocuswright: True automated AI in travel is coming](https://www.phocuswright.com/Travel-Research/Research-Updates/2024/True-automated-AI-in-travel-Is-coming)

### Gartner・IDC

- [Gartner: Hype Cycle for Artificial Intelligence 2025](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence)
- [Gartner：2025年世界AI支出は1.5兆ドル](https://www.gartner.com/en/newsroom/press-releases/2025-09-17-gartner-says-worldwide-ai-spending-will-total-1-point-5-trillion-in-2025)
- [Gartner：2026年の戦略的予測](https://www.gartner.com/en/articles/strategic-predictions-for-2026)
- [IDC：AI・GenAI予測2025 eBook](https://info.idc.com/futurescape-generative-ai-2025-predictions.html)

### 主要OTAの公式・報道情報

- [Expedia Newsroom: Romie Launch - Spring Product Release 2024](https://www.expedia.com/newsroom/spring-product-release-2024/)
- [Booking.comのAgentic AI Innovation発表](https://news.booking.com/bookingcom-debuts-agentic-ai-innovations-adding-to-its-robust-suite-of-genai-tools-for-customers/)
- [TripAdvisor: AI Travel Planning Product Launch](https://tripadvisor.mediaroom.com/Tripadvisor-launches-AI-powered-travel-planning-product)
- [KAYAK、AI Modeを発表 - AltexSoft](https://www.altexsoft.com/travel-industry-news/another-company-bets-on-ai-agents-kayak-launches-ai-mode/)

### Google

- [Google Blog: Explore new ways to plan and book travel with AI in Search](https://blog.google/products/search/agentic-plans-booking-travel-canvas-ai-mode/)
- [Skift: Google Is Building Agentic Travel Booking](https://skift.com/2025/11/17/google-is-building-agentic-travel-booking-plus-other-travel-ai-updates/)
- [Google Cloud: Reimagining travel and hospitality with agentic AI](https://cloud.google.com/transform/reimagining-travel-hospitality-agentic-ai)

### 日本国内

- [楽天トラベルAIホテル探索提供開始 - 楽天グループ公式プレスリリース](https://corp.rakuten.co.jp/news/press/2025/0922_01.html)
- [観光地・観光産業における生成AIの活用手引書 - 観光庁](https://www.mlit.go.jp/kankocho/topics12_00010.html)
- [生成AIが観光の課題をどう変える - 訪日ラボ](https://honichi.com/news/2025/07/23/generationai/)
- [JTB・じゃらん・楽天が語るAIの未来 - トラベルビジョン](https://www.travelvision.jp/news/detail/news-117913)

### スタートアップ・テクノロジー情報

- [Mindtrip - PhocusWire](https://www.phocuswire.com/mindtrip-ai-travel-discovery-planning)
- [Mindtrip：AIで旅行を再定義するスタートアップ - Eightception](https://eightception.com/mindtrip-ai-travel-startup/)
- [Laylaがai旅程ビルダーのRoam Aroundを買収 - TechCrunch](https://techcrunch.com/2024/02/12/travel-startup-layla-acquires-flyr-backed-ai-itinerary-building-bot/)
- [NVIDIA Technical Blog: Airbnb Turns to Deep Learning to Supercharge Search Rankings](https://developer.nvidia.com/blog/airbnb-turns-to-deep-learning-to-supercharge-their-search-rankings/)
- [Qdrant: How TripAdvisor Drives 2-3x More Revenue with Qdrant-Powered AI](https://qdrant.tech/blog/case-study-tripadvisor/)

### 規制・コンプライアンス

- [Secure Privacy: Compliance Challenges at the Intersection between AI & GDPR in 2025](https://secureprivacy.ai/blog/ai-gdpr-compliance-challenges-2025)
- [2026年AIリーガルフォーキャスト：イノベーションからコンプライアンスへ - CPO Magazine](https://www.cpomagazine.com/data-protection/2026-ai-legal-forecast-from-innovation-to-compliance/)
- [AI規制グローバルトラッカー - White & Case](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-united-states)

### 総合

- [Skift: The Definitive Oral History of Online Travel](https://skift.com/history-of-online-travel/)
- [McKinsey: Remapping travel with agentic AI](https://www.mckinsey.com/industries/travel/our-insights/remapping-travel-with-agentic-ai)
- [Booking Holdings AI戦略分析 - Klover.ai](https://www.klover.ai/booking-holdings-ai-strategy-analysis-of-dominance-in-new-era-of-travel/)
- [AirbnbのAI戦略 - Klover.ai](https://www.klover.ai/airbnb-ai-strategy-analysis-of-dominance-in-online-marketplaces-for-homestay-experiences-ai/)
- [PhocusWire: AIの新たなゲートキーパー：Booking.comとExpediaが旅行の未来を変える](https://www.phocuswire.com/ai-new-gatekeepers-how-booking-expedia-hijacking-future-of-travel)

---

*本レポートは `research_history.md`（技術・市場の歴史的背景調査）および `research_trends.md`（最新トレンド・事例調査）を統合・編集したものです。調査日：2026年3月2日。*
