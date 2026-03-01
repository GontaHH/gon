# 観光業（OTA・Google等）におけるAIエージェント活用：調査レポート

**作成日：2026年3月1日**
**調査対象：オンライン旅行業（OTA）およびGoogle等プラットフォームにおけるAIエージェント活用の歴史・現状・展望**

---

## 1. 技術・市場の誕生背景

### 1-1. OTA（Online Travel Agency）の登場とデジタル化の流れ

オンライン旅行代理店（OTA）の登場は、1990年代のインターネット普及と不可分の関係にある。それ以前、旅行の予約は実店舗の旅行代理店に出向くか、航空会社や鉄道会社に電話で問い合わせるしかなく、価格の透明性も低く、消費者の選択肢は限られていた。

インターネットが職場のみならず一般家庭にも普及し始めた1990年代後半、旅行業界に革命をもたらす企業群が相次いで登場した。

**Travelocity（1996年）：** アメリカン航空傘下のSabre部門内でTerry Jonesが設立。世界初の大規模コンシューマー向けオンライン旅行予約サービスの一つとして、消費者が自ら航空券をネットで検索・予約できるプラットフォームを提供した。Travelocityのルーツは1980年代の「eAAsySabre」にまでさかのぼる。

**Expedia（1996年）：** 1996年10月22日、マイクロソフト社内プロジェクトとしてRichard (Rich) Barton率いるチームが創設。航空券・ホテル・レンタカーの価格を消費者に直接透明な形で提供することを目指した。当初は航空会社やホテルから直販への抵抗を受けながらも急成長し、2001年にマイクロソフトから独立してNasdaq上場を果たす。

**Priceline（1997年）／Booking Holdings：** 1997年創業のPricelineは「Name Your Own Price（価格を自分で決める）」という斬新なモデルで登場。後にBooking.comを傘下に収め、Booking Holdingsとして世界最大のOTA企業グループに成長する。Booking.comはオランダで1996年に設立されたが、2005年にPricelineに買収され、以後急拡大した。

**Airbnb（2008年）：** 2008年の世界金融危機直後、Brian Chesky、Joe Gebbia、Nathan Blecharczykによってサンフランシスコで創業。個人宅の空き部屋を民泊として提供するマーケットプレイスという革新的なモデルで、ホテル業界に根本的な変革をもたらした。

**ドットコムバブルとその後：** 2000年のドットコム崩壊で多くの旅行系スタートアップが倒産したが、Expedia・Priceline・TripAdvisorなどの生存者は2002年以降の経済回復期に急速に力をつけた。この時期、伝統的旅行代理店は急速に市場シェアを失い、OTAへの移行が加速した。

### 1-2. 旅行業界でのAI・ML活用の始まり

旅行業界でのデータ活用は、GDS（Global Distribution System：グローバル流通システム）の登場に始まる。1960年代にアメリカン航空が開発したSabre、その後のAmadeus（1987年）・Galileo（1987年）・Worldspan（1990年）といったGDSが、コンピュータによる旅行データの集中管理基盤を形成した。

本格的なAI・機械学習の活用は2010年代に入ってから加速した：

- **2010年代前半：** ビッグデータ技術の成熟に伴い、OTA各社はユーザーの行動データを大規模に収集・分析し始めた。Booking.comは協調フィルタリング（「あなたと似た旅行者はこちらを選びました」）や購買履歴ベースの推薦を実装した。
- **2015年頃：** 機械学習アルゴリズムの実装が旅行推薦システムに本格的に導入され始め、200以上のコンテキスト変数をリアルタイムに処理して個人向け推薦を行うシステムが登場した。
- **2018年：** Airbnbがディープラーニングを用いた宿泊施設ランキングシステムを実装。100以上の変数（価格感度・過去の予約傾向・視覚的嗜好など）を評価してリスト表示順位を決定する手法を採用した。

### 1-3. AIエージェント（自律型AI）が旅行業界に登場した背景

2022年11月30日、OpenAIが一般向けにChatGPTをリリースしたことが、旅行業界のAIエージェント化の起爆剤となった。それまでのAIは特定タスクに特化した「弱いAI」だったが、大規模言語モデル（LLM）の登場により、自然言語で複雑な要求を理解・実行できる「汎用的な会話AI」が実現した。

2023年初頭には、Auto-GPT・BabyAGI・AgentGPTといったオープンソースのエージェント型AIが登場し、LLMを複数のツールと組み合わせて自律的にタスクを実行する「AIエージェント」の概念が広まった。

旅行業界においてこの変化が特に重要だった理由：
- 旅行計画は本質的に多段階の意思決定プロセス（目的地選択→交通手段→宿泊→アクティビティ→保険など）であり、AIエージェントの「マルチステップ推論」能力と親和性が高い
- 旅行中のリアルタイムな状況変化（フライト遅延・天候変化など）への即時対応を自動化できるメリットが明確
- 個人旅行の増加（コロナ後のFIT：Foreign Independent Travel化）により、個別最適化された旅行計画へのニーズが急増していた

---

## 2. 主要な技術的マイルストーン（年表）

### 1990年代：OTA誕生期

| 年 | 出来事 |
|---|---|
| 1987 | Amadeus GDS設立（エールフランス・ルフトハンザ等が共同出資） |
| 1994 | Microsoft Travelの前身となる旅行サービス実験開始 |
| 1995 | eBayが類似のオークションモデルを構築（OTAのビジネスモデルに影響） |
| 1996 | **Travelocity**創設（アメリカン航空Sabre部門、Terry Jones） |
| 1996 | **Expedia**創設（Microsoft内プロジェクト、Richard Barton） |
| 1996 | **Booking.com**オランダで設立 |
| 1997 | **Priceline**設立（独自の「Name Your Own Price」モデル） |
| 1997 | **Booking Holdings**前身企業（Priceline.com）設立 |
| 1999 | Trip.com（Ctrip）が中国で設立 |
| 2000 | **TripAdvisor**設立（Stephen Kaufer、Greg Menyuk他） |

### 2000年代：市場確立とモバイル化の端緒

| 年 | 出来事 |
|---|---|
| 2001 | Expedia、マイクロソフトから独立・Nasdaq上場 |
| 2001 | 9.11テロ後、旅行業界が大打撃。オンライン予約は一時的に急増（安全確認のニーズ） |
| 2002 | Orbitz、航空会社の合弁OTAとして本格拡大 |
| 2004 | Google、Googleマップをローンチ（旅行業界の位置情報活用の基盤） |
| 2005 | PricelineがBooking.comを買収（約1.35億ドル、後に歴史的名買収と称される） |
| 2006 | TripAdvisorがExpediaから独立 |
| 2007 | iPhoneローンチ、モバイル旅行予約時代の幕開け |
| 2007 | Kayakが正式サービス開始 |
| 2008 | **Airbnb**設立（Brian Chesky、Joe Gebbia、Nathan Blecharczyk） |
| 2009 | Googleがホテル・フライト検索強化へ向けてITAソフトウェア買収交渉開始（2010年成立） |

### 2010年代：ビッグデータとMLの実装期

| 年 | 出来事 |
|---|---|
| 2010 | Google、ITA Softwareを7億ドルで買収（フライト検索機能の基盤取得） |
| 2011 | Booking.com、機械学習を活用したA/Bテストフレームワークを全面展開 |
| 2011 | Google Hotelsの前身となるフライト・ホテル統合検索を試験導入 |
| 2012 | Airbnb、価格最適化アルゴリズム「Aerosolve」開発開始 |
| 2013 | Booking Holdings（Priceline）、Kayakを18億ドルで買収 |
| 2014 | Expedia、Orbitzを16億ドルで買収 |
| 2015 | 機械学習ベースの旅行推薦システムが業界標準に。個人化推薦で予約転換率23%向上が報告される |
| 2015 | TravelocityがExpediaグループに売却 |
| 2016 | Airbnb、ディープラーニングを用いた検索ランキングシステムを実装 |
| 2016 | Google、「Google Trips」アプリをローンチ（旅程管理AI） |
| 2017 | Booking.comがAI駆動のカスタマーサービスを本格展開、自動応答率向上 |
| 2018 | Google Duplex発表（AIによる自律的な電話予約デモ、旅行業界に衝撃） |
| 2018 | HotelPlanner、AIを活用した予約システムの試験運用開始 |
| 2019 | BERT（Googleの大規模言語モデル）が旅行検索クエリの理解に革新をもたらす |
| 2019 | Trip.com（Ctrip）、NLP活用のカスタマーサービスAIを導入 |

### 2020年代：LLMとAIエージェント時代

| 年 | 出来事 |
|---|---|
| 2020 | COVID-19パンデミック。旅行業界の市場規模が60〜70%縮小。各社がデジタル投資を加速 |
| 2021 | Airbnb、IPO（2020年12月）後に急成長。AI活用の詐欺検知システムを強化 |
| 2022 | **ChatGPT（GPT-3.5）**、OpenAIが一般公開（11月30日）。旅行業界のAI活用議論が一気に加速 |
| 2023 | GPT-4リリース（3月）。各OTAがLLM統合を競って発表 |
| 2023 | **Expedia**、ChatGPTプラグインをExpediaアプリに統合（春） |
| 2023 | **Booking.com**、AI旅行プランナーの試験展開を発表 |
| 2023 | **TripAdvisor**、OpenAIとのパートナーシップを通じたAI旅行行程生成機能をベータ公開 |
| 2023 | **Kayak**、「Ask Kayak」機能（ChatGPTベース）をローンチ |
| 2023 | **Mindtrip**、700万ドルのシードラウンドを実施。AI旅行計画スタートアップとして注目を集める |
| 2023 | **Layla**（生成AI旅行プランナー）、330万ドル調達。Paris Hiltonらが出資 |
| 2024 | **Expedia**、AI旅行アシスタント「**Romie**」を発表（5月、年次カンファレンスExploreにて） |
| 2024 | **TripAdvisor**、AI旅行ビルダーを刷新（8月）。推薦保存率が2倍に向上 |
| 2024 | **Airbnb**、AI詐欺検知システムで不正予約を40%削減 |
| 2024 | **Google**、Geminiを活用した旅行計画機能を強化。フライト検索と地図情報を統合した新インターフェースを試験展開 |
| 2024 | **HotelPlanner**、世界初の完全自動AI音声予約オペレーターを展開。1日約1万件の通話を処理、15言語対応 |
| 2024 | **Mindtrip**、計2250万ドルに累計調達額拡大（Amex Ventures・Capital One Ventures・United Airlines Ventures等が参加） |
| 2025 | **Google**、「AI Mode Canvas」を旅行計画に統合。Google Flights・Hotels・Mapsのデータを統合したビジュアル旅程計画ツール |
| 2025 | **Google**、「Agentic Booking」を発表。レストラン予約から開始し、近くフライト・ホテルにも拡大予定 |
| 2025 | AI関連の旅行VC投資が全体の45%を占める（2023年の10%から急増） |
| 2025 | Expedia、「Romie」のWhatsApp・iMessage統合を正式展開 |

---

## 3. 市場規模の変遷と主要プレイヤーの興亡

### 3-1. OTA市場全体の規模推移

| 年 | 市場規模（推計） | 備考 |
|---|---|---|
| 2019 | 約8,000億ドル（グローバル旅行市場全体） | コロナ前のピーク |
| 2020 | 約2,200〜2,400億ドルに急縮小 | COVID-19による移動制限の直撃 |
| 2021 | 約3,000〜3,500億ドル | 国内旅行・ワーケーション需要で部分回復 |
| 2022 | 約5,000〜6,000億ドル | リベンジ旅行（Pent-up demand）による急回復 |
| 2023 | 約6,000〜6,500億ドル | 国際観光がほぼコロナ前水準に回復 |
| 2024 | OTA市場単独で約2,532億ドル | CAGR 7.9%で成長中 |
| 2033予測 | 約4,753億ドル（OTA市場） | CAGR 6.74%で拡大継続 |

**主要プレイヤーの2024年売上高：**
- **Booking Holdings：** 総収益約220〜240億ドル（グロス予約総額1,660億ドル、客室泊数11億泊）
- **Expedia Group：** 約140億ドル（過去最高売上を更新）
- **Airbnb：** 約110億ドル規模
- **Trip.com Group：** 約70億ドル規模

Booking HoldingsとExpedia Groupの2社で、グローバルOTA市場シェアの40%以上を占める。

### 3-2. 主要プレイヤーの戦略と競合構造

**Booking Holdings（本拠地：米コネチカット州ノーウォーク）：**
Booking.com・Priceline・Kayak・Agoda・Rentalcars.comなどを傘下に持つ最大グループ。2024年のグロス予約総額は前年比10%増の1,660億ドル。早期からA/Bテストと機械学習を組み合わせたデータドリブン経営を確立し、ヨーロッパ市場で特に支配的地位を築いた。2024〜25年にかけてAI旅行アシスタントへの投資を急拡大している。

**Expedia Group（本拠地：米ワシントン州シアトル）：**
Expedia・Hotels.com・Vrbo・trivago・Travelocity・Orbitzなどを傘下に持つ第2位グループ。2023年のChatGPT統合、2024年のRomie発表と積極的にAI戦略を打ち出している。2024年、Romieを通じてグループチャット（WhatsApp・iMessage）への統合など業界初の機能を発表。

**Airbnb（本拠地：米カリフォルニア州サンフランシスコ）：**
2008年創業、2020年12月にIPO。民泊・体験プラットフォームとして独自の市場を切り開いた。COVID-19期間中も農村部・長期滞在需要で相対的に底堅く推移。2024年にはAI詐欺検知で不正予約を40%削減。2025年にはLLMを核とした次世代検索エンジンの開発を進めている。

**Google（本拠地：米カリフォルニア州マウンテンビュー）：**
旅行業界の「メタサーチ」プレイヤーとして参入。2010年にITA Software（フライトデータ処理）を7億ドルで買収し、2011年に「Google Flights」をローンチ。Google Hotels・Google Maps・Google Travelを統合したエコシステムを構築。2024〜25年にかけてGeminiを活用した「AI Mode Canvas」や「Agentic Booking」を展開し、OTA各社の最大の脅威になりつつある。月間アクティブユーザー20億人超のGoogle Mapsを旅行推薦のインフラとして活用できる点が大きな差別化要因。

**TripAdvisor（本拠地：米マサチューセッツ州ニーダム）：**
2000年創設。10億件超のレビューを持つ世界最大の旅行クチコミプラットフォーム。自社の一次データを活用したAI推薦エンジンを開発し、OpenAI・Perplexity AIとのパートナーシップを通じて旅行計画機能を強化。2024年のAI旅行ビルダー刷新により、推薦保存率2倍・顧客満足度10%向上を達成。

### 3-3. AIエージェント関連スタートアップの動向

2023〜25年に旅行×AI分野のスタートアップが乱立し、その後淘汰・統廃合の段階に入りつつある：

**注目スタートアップ：**
- **Mindtrip（米国、2023年創業）：** シリコンバレー拠点のAI旅行計画・予約プラットフォーム。2023年に700万ドルのシード調達（Costanoa Ventures主導）、2024年に1,200万ドルの追加調達、累計2,250万ドルを調達。Amex Ventures・Capital One Ventures・United Airlines Venturesが出資。Skift「Hot 25 Travel Startups 2025」に選出。
- **Layla（フランス、2023年）：** Instagramのダイレクトメッセージで利用できるAI旅行プランナー。2023年11月に330万ドル調達。パリス・ヒルトンが出資者として注目を集める。2024年3月にRoam Aroundを買収。
- **Roam Around：** AIが旅程を自動生成するサービスとして2023年に注目を集めたが、2024年にLaylaに買収された。
- **GuideGeek：** WhatsAppやFacebook Messenger上で動作するAI旅行アシスタント。Matador Networkが開発。

**業界トレンド：**
AI旅行スタートアップへのVC投資比率は2023年の約10%から2025年上半期には約45%に急増。一方、LLMの汎用化により必要な開発リソースが低下し、バリュエーションは相対的に抑制されている。多くの小規模スタートアップは大手OTAや旅行企業に買収されるか、ニッチ特化の生存戦略をとる二極化が進んでいる。

---

## 4. 普及を加速・阻害した要因

### 4-1. COVID-19の影響とデジタル化の加速

2020年のCOVID-19パンデミックは旅行業界史上最大の危機であると同時に、デジタル変革を強制的に加速させた触媒にもなった。

**マイナスの影響：**
- 2020年のグローバル旅行市場はピーク時比60〜70%の縮小
- Expedia・Booking Holdings・TripAdvisorなど主要OTAが数千人規模の人員削減
- AIへの投資は一時縮小（短期的な生き残りを優先）

**プラスの影響（逆説的な加速要因）：**
- セルフサービス化・非接触型サービスへの需要急増がAI自動化の投資を正当化
- 旅行制限が緩和された2022〜23年のリベンジ旅行（Pent-up demand）で、個人旅行（FIT）需要が急増→個別最適化AIへのニーズが拡大
- 国内旅行・農村部需要の高まりで、地域情報に強いAI推薦の価値が高まった
- Airbnbはホテルが苦境に立たされる中でもCOVID期間中に相対的に底堅く、長期滞在需要を取り込んだ

UN Tourismによると、2024年の国際観光は2019年比99%まで回復し、14億人の国際観光客を記録（前年比11%増）。この急速な回復期にAI活用のデジタル予約が標準化した。

### 4-2. 技術的障壁と突破要因

**主要な技術的障壁：**

1. **自然言語処理（NLP）の限界（〜2022年）：** 従来のチャットボットはルールベースで、「3月に家族4人で沖縄に行きたい。子どもが2人いて、海が好き。予算は1人5万円以内」といった複雑なクエリを正しく理解できなかった。GPT-3.5/4の登場が真のブレークスルーとなった。

2. **リアルタイムデータ連携の難しさ：** AIの推薦精度は、リアルタイムの価格・在庫・フライト情報との連携が不可欠。GDS・APIとのインテグレーションは依然として複雑で、「ハルシネーション（幻覚）」問題によりAIが実際に存在しない価格や便を提案するリスクがある。

3. **マルチステップトランザクションの複雑さ：** 旅行の予約は複数のサードパーティシステムをまたぐ複雑なトランザクション（航空会社GDS、ホテルPMS、決済ゲートウェイ等）であり、エラー発生時の責任範囲が不明確になりやすい。

4. **MCP（Model Context Protocol）の普及：** 2024〜25年にかけて注目を集めたAnthropicのMCPは、AIエージェントが旅行APIを「ネイティブに理解して呼び出す」ための標準プロトコルとして機能し始めている。LiteAPI Agenticがこれを活用したトラベルAPI統合を発表。

5. **消費者の信頼不足：** Skiftの「State of Travel 2025」レポートによると、人間の監視なしにAIが自律的に予約・変更することを「完全に任せられる」と答えた旅行者はわずか2%。一方、40%の旅行者が旅行計画にAIツールを利用した経験を持つ（Statista, 2024年11月調査）という矛盾した状況が続いている。

**突破要因：**
- LLMの文脈理解能力の飛躍的向上（GPT-3.5→4→4o→o1→o3）
- 旅行特化ファインチューニングと検索拡張生成（RAG）の実用化
- Voice Interface（音声入力）の普及（Siri・Google Assistant・Alexa経由の旅行検索）
- マルチモーダルAI（画像からの旅先推薦）の実用化（TripAdvisorのVision機能、Googleレンズ連携）

### 4-3. 規制・プライバシー問題

**GDPR（EU一般データ保護規則）の影響：**
2018年施行のGDPRは、OTAが欧州ユーザーのデータを活用したAIパーソナライゼーションを行う際に重大な制約となっている。同意管理・データ最小化原則・透明性要件がAI学習データの収集を制限する。

2025年は特に規制強化が顕著で、GDPRの制裁金総額は2024年の12億ユーロから2025年には23億ユーロに38%増加した。Booking.com・Expediaなどが欧州でのデータ活用方針を見直す動きが加速している。

**EU AI法（EU AI Act）：**
2024年に成立したEU AI Actは、AIシステムをリスクレベルで分類し、「高リスク」カテゴリに該当するシステムには透明性要件・バイアス検出・人間監視の義務を課す。旅行業界のAI自動予約・スコアリングシステムは、このフレームワークの適用可能性を慎重に評価する必要がある。

**個人情報保護とパーソナライゼーションのトレードオフ：**
より精度の高い旅行推薦を行うには、過去の行動・決済履歴・位置情報・旅行の同伴者情報などのセンシティブな個人データが必要となる。一方で消費者の間には「自分のデータがどう使われているかわからない」という不信感が根強く、OPT-OUT傾向が強まっている。

**クロスボーダーデータフローの複雑性：**
GDS経由で複数国にまたがるデータが流通する旅行業界では、EU-US Data Privacy Framework（2023年施行）・中国PIPL・インドDPDP法など各国規制への同時対応が求められ、グローバルなAIシステムの設計を著しく複雑にしている。

---

## 5. 現時点での技術的成熟度（Gartnerハイプサイクル的観点）

### 5-1. 旅行業界AIの全体的な成熟度マップ

Gartnerは旅行業界専用のハイプサイクルを公開していないが、2024〜25年のAI全般のハイプサイクルと旅行業界の実態を照合することで、各機能の成熟度を評価できる。

**2025年GartnerハイプサイクルにおけるAIエージェントの位置：**
Gartnerの2025年AIハイプサイクルでは、「AIエージェント」は最も急速に進化する技術として**「過度な期待のピーク（Peak of Inflated Expectations）」**に位置づけられている。企業ワークフローの完全自律化への野心的な期待が先行しており、期待が実態を大幅に上回る状態にある。

一方、生成AI（GenAI）全般は2023〜24年の爆発的注目から「幻滅のトラフ（Trough of Disillusionment）」に向かいつつあり、実際のROI証明に苦しむ企業が多い（AIへの平均投資190万ドルに対し、30%未満のCEOが投資リターンに満足）。

### 5-2. 機能別の成熟度評価

#### (A) AIパーソナライズ推薦 — 成熟段階：「啓蒙の斜面〜生産性の安定期」

**成熟度：高（業界標準）**

旅行業界でAIパーソナライズ推薦は最も成熟した機能領域であり、Booking.com・Expedia・Airbnbの全主要プレイヤーが本番運用している。

- Booking.comは協調フィルタリング＋コンテンツベースの推薦システムを長年運用し、ユーザーエンゲージメント平均31%向上・予約転換率23%向上を達成
- 最新システムは200以上のコンテキスト変数をリアルタイム処理
- Airbnbは100以上の変数を評価した宿泊推薦システムを実装済み
- TripAdvisorはQdrantのベクトル検索を活用した次世代推薦エンジンで収益を2〜3倍に向上

**課題：** LLMベースの推薦（ゼロショット学習）と従来のML推薦（大量の学習データ活用）の統合が技術的課題。

#### (B) チャットボット・カスタマーサービス — 成熟段階：「生産性の安定期」

**成熟度：高〜中（大手は本番、中小は実装中）**

AIチャットボットによるカスタマーサービス自動化は旅行業界で最も広く普及した応用領域。

- Expediaの「Romie」は2024年5月に正式発表。WhatsApp・iMessage統合、グループチャット連携、リアルタイム旅程更新などを実現
- Expediaグループ全体のAIチャットボットが累計2,900万件の対話を処理
- HotelPlannerのAI音声予約オペレーターは1日1万件の予約電話を処理、15言語対応、800万件以上の予約通話データで学習
- Booking.comはAI旅行プランナーを展開中
- TripAdvisorのAIアシスタントはチャットを通じた旅行計画・推薦を提供

**課題：** 複雑な変更・払い戻し対応・クレームはまだ人間オペレーターが必要なケースが多い。感情理解（Emotion AI）はまだ黎明期。

#### (C) 動的価格設定（ダイナミックプライシング） — 成熟段階：「生産性の安定期」

**成熟度：高（航空・ホテルで業界標準）**

AIを活用した動的価格設定は航空業界では1980年代から始まり（Revenue Management System）、現在は宿泊・ツアー・体験にまで拡大している。

- AirbnbのAIダイナミックプライシング（旧名：Smart Pricing）は需要・季節・競合・イベント情報を統合
- Kayakは機械学習による「フライト価格予測」機能（値上がり・値下がり予測）を提供
- Expedia・Booking.comも類似機能を実装

#### (D) 自律型旅行予約（AIエージェントによる完全自動予約） — 成熟段階：「過度な期待のピーク」

**成熟度：低〜中（概念実証〜限定的な試験運用段階）**

自律型AIエージェントが人間の介入なしに旅行を検索・比較・予約・変更まで行う機能は、2025年現在まだ本格的な商用展開には至っていない。

- GoogleのAgentic Bookingはレストランから開始し、フライト・ホテルへの拡大を計画（2025年発表）
- Expedia Romieは「自律予約」ではなく、人間が最終確認する「コパイロット（副操縦士）」モデルを採用
- HotelPlannerの音声AI予約オペレーターは最も完成度が高い商用事例（電話での完全自動予約）だが、ドメインが限定的
- Skift調査でAI単独の完全自律予約を許容する旅行者は2%のみ

**Gartner予測：** 「Machine Customers（機械顧客）」概念は2030年には80億台のデバイスに拡大する見込みだが、旅行の完全自律予約が主流になるのは2028〜2032年以降と予測される。

#### (E) マルチモーダル旅行計画（画像・音声入力） — 成熟段階：「黎明期〜過度な期待のピーク」

**成熟度：低〜中（実験的段階）**

写真をアップロードして「この場所に似た旅先を探して」と指示したり、音声で旅行計画を立てるインターフェースは登場しているが、精度・利便性・ユーザー習慣の面で普及途上にある。

- Googleレンズを活用した「写真から旅先推薦」機能
- Airbnbが2024年にGoogle Assistant連携の音声予約を追加し、声で宿泊先を予約できる機能を提供（音声予約で予約数15%増加）
- Googleの「Canvas」は旅行計画をビジュアルかつインタラクティブに表示する新インターフェース（2025年展開）
- GeminiのマルチモーダルAIにより、ホテルの写真から「ベッドルームのビュー評価」を自動分類する機能が試験中

---

## 6. 総合考察：旅行業界AIエージェントの将来展望

### 市場の3つの競争軸

現在、旅行業界のAIエージェント競争は3つの軸で展開されている：

1. **既存OTA（Booking Holdings・Expedia）：** 膨大な取引データとグローバル在庫を武器に、AIによるパーソナライゼーションを深化させる戦略。Romieのようなコパイロット型AIで、人間の意思決定を支援しながら自律化を段階的に進める。

2. **テックジャイアント（Google・Apple・Meta）：** 検索・地図・SNSとの統合により、旅行計画の上流（インスパイレーション段階）から予約完了までの全プロセスを自社エコシステム内に取り込もうとする。Google Canvasはその象徴的な戦略。

3. **AI-First スタートアップ（Mindtrip・Layla等）：** GenAIネイティブな設計で差別化を図るが、OTAや大手テック企業との競争で資金・データ量の面で劣位。M&Aターゲットとなるか、ニッチ特化で生き残るかの二択に直面。

### 技術成熟の課題

旅行AIエージェントが「コパイロット」から「オートパイロット」に移行するための残課題：

1. **ハルシネーション（幻覚）の解消：** リアルタイム価格・在庫情報への確実なアクセスと、LLMの「知ったかぶり」問題の解決
2. **信頼構築：** キャンセル・返金・変更時の責任範囲の明確化。エラー発生時の人間への escalation設計
3. **規制対応：** GDPR・EU AI Act・各国プライバシー法への対応コストの吸収
4. **エコシステム連携：** GDS・PMS・CRSなど旧来のレガシーシステムとのAPI統合の標準化

### 今後3〜5年の予測

- **2026〜2027年：** AIアシスト型（ヒト確認必須）の旅行エージェントが一般化。「旅行AIアシスタント」の利用率が全旅行者の50%超に
- **2027〜2028年：** 特定のユーザーセグメント（テック感度の高いミレニアル・Z世代、ビジネストラベラー）向けに「完全自律予約」が商用化開始
- **2028〜2030年：** Gartnerが予測する「Machine Customers」の普及期。AIエージェントが法人旅行・定期的な出張予約を完全自律で処理するケースが標準化
- **2030年代：** コンシューマー旅行の大部分でAI自律予約が選択肢になり、従来型OTAのビジネスモデルが根本的に変容

---

## 参考文献・情報源

本レポートは以下の公開情報・調査結果をもとに執筆した：

- [Skift: The Definitive Oral History of Online Travel](https://skift.com/history-of-online-travel/)
- [Expedia Wikipedia](https://en.wikipedia.org/wiki/Expedia)
- [Cloud Beds: What Are Online Travel Agencies? The Ultimate 2026 OTA Guide](https://www.cloudbeds.com/online-travel-agencies/)
- [CoaxSoft: AI agents and the future of online travel agencies](https://coaxsoft.com/blog/ai-agents-and-the-future-of-online-travel-agencies)
- [McKinsey: Remapping travel with agentic AI](https://www.mckinsey.com/industries/travel/our-insights/remapping-travel-with-agentic-ai)
- [Phocuswright: True automated AI in travel is coming](https://www.phocuswright.com/Travel-Research/Research-Updates/2024/True-automated-AI-in-travel-Is-coming)
- [Grand View Research: Online Travel Agencies Market Size | Industry Report, 2030](https://www.grandviewresearch.com/industry-analysis/online-travel-agencies-market-report)
- [Mize: Online Travel Agencies Market Share Across the World](https://mize.tech/blog/online-travel-agencies-market-share-across-the-world/)
- [Google Blog: Explore new ways to plan and book travel with AI in Search](https://blog.google/products-and-platforms/products/search/agentic-plans-booking-travel-canvas-ai-mode/)
- [Google Cloud: Reimagining travel and hospitality with agentic AI](https://cloud.google.com/transform/reimagining-travel-hospitality-agentic-ai)
- [Skift: Google Is Building Agentic Travel Booking](https://skift.com/2025/11/17/google-is-building-agentic-travel-booking-plus-other-travel-ai-updates/)
- [Gartner: Hype Cycle for Artificial Intelligence 2025](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence)
- [Gartner: Gartner Hype Cycle Identifies Top AI Innovations in 2025](https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025)
- [Expedia Newsroom: Romie Launch - Spring Product Release 2024](https://www.expedia.com/newsroom/spring-product-release-2024/)
- [Hotel Dive: Expedia debuts AI-powered virtual concierge Romie](https://www.hoteldive.com/news/expedia-ai-assistant-romie/716315/)
- [TripAdvisor: AI Travel Planning Product Launch](https://tripadvisor.mediaroom.com/Tripadvisor-launches-AI-powered-travel-planning-product)
- [TripAdvisor + ChatGPT Partnership](https://www.tripadvisor.com/ChatGPT)
- [Skift: Mindtrip Raises $12 Million](https://skift.com/2024/09/17/mindtrip-raises-12-million-in-tough-funding-environment-for-ai-trip-planners/)
- [Everite Solutions: How Airbnb is Using AI in 2025](https://everitesolutions.com/how-airbnb-is-using-artificial-intelligence-ai-to-transform-the-travel-experience-in-2025/)
- [Qdrant: How TripAdvisor Drives 2-3x More Revenue with Qdrant-Powered AI](https://qdrant.tech/blog/case-study-tripadvisor/)
- [Secure Privacy: Compliance Challenges at the Intersection between AI & GDPR in 2025](https://secureprivacy.ai/blog/ai-gdpr-compliance-challenges-2025)
- [NVIDIA Technical Blog: Airbnb Turns to Deep Learning to Supercharge Search Rankings](https://developer.nvidia.com/blog/airbnb-turns-to-deep-learning-to-supercharge-their-search-rankings/)
- [GM Insights: Online Travel Agency Market Size, Growth Analysis 2025-2034](https://www.gminsights.com/industry-analysis/online-travel-agency-market)
- [SAM Solutions: AI Agents for Travel: How AI Is Transforming the Tourism Industry](https://sam-solutions.com/blog/ai-agents-for-travel/)
- [ACI Infotech: Agentic AI in Travel: The Next Transformation](https://www.aciinfotech.com/blogs/agentic-ai-in-travel-transformation)
