---
name: スワップマーケット
description: BitcoinとLightningのスワップ・サービス・アグリゲーター
---

![cover](assets/cover.webp)



Bitcoin、On-Chain、Lightning Network間の資金移動には、通常、ライトニング・チャネルを手動で開設するか（技術的でコストがかかる）、KYCを伴う集中スワップ・プラットフォームを利用する必要がある。SwapMarketは代替手段を提供している：Trustlessのアトミックスワップは、KYCなしで、競争力のあるプロバイダーを経由する。



革新性：プロバイダーは仲介業者であるが、HTLC（*Hash Time Locked Contracts*）はお客様の資金がお客様の管理下にあることを数学的に保証する。複数のプロバイダー（Boltz、ZEUS Swaps、Eldamar、Middle Way）の集合体が価格競争を生み出します。Interfaceウェブ・オープンソース・セルフホスティング可能。



## SwapMarketとは？



2024年に開始されたオープンソースのアグリゲーターであるSwapMarketは、Bitcoin/Lightningスワッププロバイダーのコンパレーターとして機能する。ユーザーは即座に条件（手数料、流動性、限度額）を比較し、最適なプロバイダーを選択する。



### テクニカル・アーキテクチャ



**フロントエンド・クライアントサイド**：100％クライアントサイドのアプリケーション（Fork Boltz Web App）はGitHub Pagesにホストされている。コードは、バックエンドサーバーなしでブラウザで実行されます。履歴はローカルに保存（クッキー/キャッシュ）。公開・監査可能なソースコード。



**プロバイダー発見** ：src/configigs/Mainnet.ts`にHardでコーディングされたリストを追加しました。新しいプロバイダーはPull Requestかメールで追加。



**独立したバックエンド**：各プロバイダーは独自のBoltzバックエンドを運営しています。InterfaceはリアルタイムでAPIを照会し、即座に見積もりを比較します。



**HTLC アトミック・スワップ**：Hash時間ロック契約は、スワップが実行されるか、各当事者が資金を回収するかのいずれかである。カウンターパーティ・リスクは数学的に排除される。



### 哲学



SwapMarketは、手数料と流動性をめぐるプロバイダー間の競争を生み出すことで、中央集権化を抑制します。KYCなし、オープンソースのセルフホスト可能なコード、単一障害点を回避するための独立したオペレータの増殖。



## 主な特徴



### プロバイダー・マーケットプレイス



Interfaceは、すべてのアクティブなプロバイダーを表示します：プロバイダー名、適用される手数料（パーセンテージおよび/または固定）、利用可能な最小/最大金額、およびサポートされているスワップタイプ。アプリケーションは、設定ファイルで参照されている各プロバイダーのAPIに直接問い合わせ、リアルタイムで相場を取得します。プロバイダー間の競争によって最適なレートが保証され、標準的なスワップでは通常0.5%前後である。



### 双方向スワップ



**スワップイン（On-Chain → Lightning）**：On-ChainのBTCをLightningのサトシに変換する。使用例：モバイルWallet Lightningに電力を供給する、ノードの受信容量を得る、または即時流動性を持つ。



**スワップアウト（Lightning → On-Chain）**：LightningのサトシをOn-ChainのBTCに変換する。使用例：WalletのLightningをColdのストレージに捨てるか、レイヤー間の流動性をリバランスする。



### 安全性と回復



**Trustless アトミックスワップ：HTLCは、Exchangeが完全に完了するか、各当事者が出資金を回収することを保証する。カウンターパーティ・リスクは数学的に排除される。



**償還メカニズム各スワップには有効期限がある（TIMELOCK）。スワップが失敗した場合、期限切れ後に資金は自動的に払い戻されます。ユーザーは常にビットコインを取り戻すオプションを保持します。



**リカバリ・キー**：SwapMarket では、スワップ中のリカバリ・キーをエクスポートできます。問題が発生した場合、これらのキーを使用して、どのデバイスからでもスワップを確定またはキャンセルできます。



## インストールとアクセス



### Interfaceウェブ



SwapMarketはインストール不要です。アクセスはブラウザからhttps://swapmarket.github.io。最大限の機密性を確保するには、Brave、トラッキング防止拡張機能付きFirefox、またはLibreWolfをご利用ください。ネットワークの匿名性にはTorブラウザをお勧めします。



登録、Eメール、本人確認は不要です。



### セルフホスティング（オプション）



公式GitHub Pagesドメインへの依存を排除したい技術的なユーザーのために、SwapMarketはローカルで実行することができます：



**Via npm** ：


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Docker経由** ：


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



アプリケーションは `http://localhost:3000` からアクセスできる。セルフホスティングはInterfaceに対する完全なコントロールを保証し、公式ドメインの検閲のリスクを排除し、実行前にソースコードを監査することを可能にします。



### 初期設定



**Walletライトニング動作可能なWalletライトニング（Phoenix、Zeus、BlueWalletなど）があることを確認してください。スワップインの場合、generateにLightning Invoiceを支払います。スワップアウトの場合は、ライトニングInvoiceをお支払いいただきます。



**Wallet On-Chain**：Wallet Bitcoin On-Chain: スワップインの場合、送金には Wallet Bitcoin On-Chain が必要です。スワップアウトの場合は、Addressを受け取るBitcoinをご用意ください。



**オプション設定**：SwapMarketはスワップ履歴とプリファレンスをブラウザのクッキーに保存します。アカウント作成は不要です。



## 設定とレスキュー・キーへのアクセス



最初のスワップを行う前に、**レスキューキー**をダウンロードすることを強くお勧めします。この緊急キーを使用すると、技術的な問題やデバイスへのアクセスが失われた場合に資金を回復することができます。



### アクセスパラメーター



SwapMarketのメインページから、Interfaceの右上、スワップ・フォームの隣にある歯車アイコン（⚙️）をクリックします。



![Accès aux paramètres](assets/fr/01.webp)



### ページ設定



設定ページが開き、いくつかの設定オプションが表示されます：





- デノミネーション**：BTCまたはSatsから選択
- 小数点セパレーター**：小数点以下の区切り記号（,または.）
- オーディオ/ブラウザ通知**：オーディオとブラウザ通知
- レスキューキー** ：リカバリーキーをダウンロードする
- ログ**：ログの表示、ダウンロード、削除



![Page Settings](assets/fr/02.webp)



### レスキューキーのダウンロード



Rescue Key "の隣にある**Download**ボタンをクリックしてください。



**重要なポイント** ：




- レスキュー・キーは、**ワンストップの緊急キー**であり、将来のすべてのスワップに対応します。
- この鍵を**安全で永続的**な場所に保管してください（パスワード管理者、デジタル金庫）。
- スワップに問題が発生した場合（タイムアウト、技術的な障害）、このキーにより資金を回復することができます。



## スワップ作成ステップ



### スワップアウトライトニング → Bitcoin



この最初の例では、ライトニングのサトシをOn-Chainビットコインに変換する方法を示している。



**ステップ1：構成を入れ替える



メインページから、スワップ・フォームを選択する：




- LIGHTNING**（上部フィールド）：Satsライトニングで送りたい金額を入力（例：30,000Sats）
- Bitcoin**（下欄）：手数料を差し引いた金額が自動的に表示されます（例：Sats 29,320）。



一番下の欄に、**受取Bitcoin Address**を貼り付けてください。このAddressをよく確認してください。



デフォルトのプロバイダーは通常Boltz Exchange。ネットワーク料金とプロバイダー料金は明確に表示される。



![Configuration swap-out](assets/fr/03.webp)



**ステップ2：プロバイダー選定



プロバイダーのドロップダウンメニュー（デフォルト：「Boltz Exchange」）をクリックすると、利用可能なすべての流動性プロバイダーが表示されます。



モーダルウィンドウが開き、比較表が表示される：




- ステータス**：Green：プロバイダがアクティブであることを示すインジケータ
- 通称**：プロバイダー名（Boltz Exchange、Middle Way、Eldamar、ZEUS Swaps）
- 手数料**：プロバイダーが課す手数料（通常0.49％～0.5）
- 最大スワップ**：スワップの上限額



手数料と上限額を比較し、お好みのプロバイダーをお選びください。



**ご注意ください：プロバイダ選択 Interface では、各プロバイダの**最低金額**は表示されません。この情報は、プロバイダーを選択した後のスワップ作成 Interface でのみ表示されます。最低限度額および最高限度額はプロバイダによって異なり、また時間の経過とともに変更される場合があります。 **スワップを希望される金額がプロバイダーの限度額を超えている場合は、より適切なプロバイダーを選択することができます。



![Sélection du provider](assets/fr/04.webp)



**ステップ3：スワップ作成とライトニング**支払い



黄色の**"CREATE ATOMIC SWAP "**ボタンをクリックしてください。SwapMarketはあなたのWallet Lightningから支払うための**Lightning Invoice** (BOLT11)をgenerateします。



と表示されます：




- スワップID**：一意のスワップ識別子（例：J4ymFIMVR6Hm）
- ステータス**："swap.created"（スワップ作成、支払い待ち）
- QRコード**：Wallet Lightningでスキャンしてください。
- Invoice Lightning**：lnbc "で始まる文字列（例：lnbc300u1p50whiv...gn5dk2szgqkvfkzc）



Walletライトニング（Phoenix、Zeus、BlueWalletなど）からこのInvoiceを支払う。正確な支払額が表示されます（例：30,000 Sats）。



![Paiement Lightning](assets/fr/05.webp)



**ステップ4：確認と承認



ライトニング決済が確認されると、SwapMarketは即座にお客様の決済を受け取り、プロバイダーはBitcoin取引をお客様のAddressにブロードキャストします。



ステータスが**"Invoice.setted "**（Invoice有料）に変わり、確認メッセージが表示される。



あなたのOn-Chainビットコインは、取引が確認され次第（プロバイダーが選択したMining手数料にもよりますが、通常は数分から数時間以内）利用可能になります。



![Confirmation swap-out](assets/fr/06.webp)



OPEN CLAIM TRANSACTION "**をクリックすると、BlockchainのエクスプローラーでBitcoinのトランザクションを見ることができます。



### スワップインBitcoin → ライトニング



この2つ目の例は、On-ChainビットコインをLightningサトシに変換する方法を示している。



**ステップ1：構成を入れ替える



メインページから、スワップ・フォームを選択する：




- Bitcoin**（上欄）：Sats Bitcoinで送りたい金額を入力（例：63,400 Sats）
- LIGHTNING** （下欄）：手数料を差し引いた金額が自動的に表示されます（例：62 884 Sats）



下のフィールドには、Wallet Lightningから生成されたLightning** Invoice（BOLT11）を貼り付けるか、Walletが対応している場合はLNURL Addressを使用する。



![Configuration swap-in](assets/fr/07.webp)



**ステップ2：レスキューキーのチェック**」。



CREATE ATOMIC SWAP "**をクリックすると、モーダルウィンドウが表示され、レスキューキーの確認が求められます。



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**：初期設定時にリカバリーキーをアップロード済みであるため（前のセクションを参照）、**"VERIFY EXISTING KEY "**ボタンをクリックして保存したキーをインポートします。



先にダウンロードしたレスキュー・キー・ファイルを選択します。認証に成功すると、Interfaceは自動的に次のステップに進みます。



**ステップ3：Bitcoin** 預託金 Address



SwapMarketは、あなたのライトニングInvoiceにリンクされたHTLC Contractを含む**ユニークなBitcoin Address**を生成するようになりました。



と表示されます：




- スワップID**：一意の識別子（例：1kGmB6JyGqU4）
- ステータス** ："Invoice.set"（Invoiceセット、Bitcoin支払い待ち）
- QRコードBitcoinデポ Address
- Bitcoin** Address: 通常は "bc1p..." で始まる。(例：bc1p5mvtwxapjkds...9d4n9f)
- 黄色の警告** ："このスワップ作成後～24時間以内に取引が確定するようにしてください！"



この24時間以内がHTLC Contractの**タイムアウト**となります。Bitcoin取引がこの時間内に確認されない場合、スワップは失敗し、資金を回復するためにレスキューキーを使用する必要があります。



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Addressをコピーするには、**"Address"**ボタンをクリックするか、Wallet On-Chainから直接QRコードをスキャンします。



**ステップ4：ビットコインの送金



あなたのWallet Bitcoin On-Chainから、**正確に**指示された金額（例：63,400 Sats）を、Addressに送金してください。



**重要**：重要**：迅速な確認を保証するため、適切な Mining 手数料を使用してください。手数料が低すぎ、取引がタイムアウト（～24時間）を超えてMempoolに残っている場合、スワップは失敗する。



取引が送信されると、SwapMarketはそれがMempoolであることを検出し、.NETを表示します：




- ステータス** ："トランザクション.Mempool"
- メッセージ**：「取引はMempoolにあり、スワップ完了の確認待ちです。



![Transaction en mempool](assets/fr/10.webp)



**ステップ5：確認とライトニング**受信



Bitcoinの取引が最初に確認されるとすぐに、プロバイダーは自動的にあなたのLightning Invoiceに支払いを行います。Walletライトニングでサトシを即座に受け取ります。



ステータスが**"transaction.claim.pending "**に変わり、確認メッセージが表示される：



![Confirmation swap-in](assets/fr/11.webp)



ライトニングのサトシはWalletですぐに使える。



## 利点と限界



### メリット



**料金競争**：料金競争**：プロバイダーが集まることで、料金の引き下げ（0.49％から0.5％）という自然な競争が生まれる。



**機密性**：KYCなし、Interface 100%クライアントサイド（個人情報の送信なし）、Torブラウザ対応。



**非親告罪**：HTLCは、お客様の資金を独占的に管理することを数学的に保証します。スワップが成功するか、ビットコインを取り戻すかのどちらかです。



**オープンソースのセルフホスタブル**：監査可能な公開コードで、検閲に最大限対抗できるようローカルに展開可能。



### 制限事項



**流動性は限定的**：アクティブなプロバイダーの数は限られている（期間によってはBoltz、Eldamar、MiddleWay）。最大金額が制限される場合がある。



**有効期限：24時間から48時間までのタイムアウト。有効期限内にOn-Chainトランザクションが確認できない場合、手動リカバリーが必要。



**Interfaceの一元化**：セルフホスト可能だが、公式InterfaceはGitHub Pagesにホストされている。GitHubがレポを検閲した場合、swapmarket.github.io経由のアクセスはブロックされます（解決策：セルフホスト）。



**On-Chainの痕跡**：HTLCスクリプトは、高度なBlockchain分析によって特定できる可能性がある。



## ベストプラクティス



### セキュアな構成



**レスキューキーのダウンロード**：最初のスワップの前に、設定からレスキューキーをダウンロードしてください（上記の専用セクションをご覧ください）。このユニークなキーは、今後すべてのスワップに使用でき、問題が発生した場合に資金を回復することができます。



**Tor Browser**を使用してください：最大限の機密性を確保するには、Torブラウザを使用してSwapMarketにアクセスし、IP Addressを隠してください。



**セルフ・ホスティング**をご検討ください：テクニカル・ユーザーにとっては、自分でSwapMarketインスタンスを運営することで、GitHub Pagesの公式ドメインへの依存をなくすことができます。



### スワップ最適化



**Mempoolから目を離さないでください：スワップインの前にMempool.spaceをチェックする。Miningのコストを最小限に抑えるために、アクティビティの少ない時間帯を選ぶ。



**住所を確認してください：スワップアウトの場合は、Addressの受信を入念にチェックすること。コピー＆ペーストを使用し、最初の5文字と最後の5文字をチェックしてください。



**少量でテストしてください：最小限の量（25,000～50,000 Sats）から始める。慣れてきたら徐々に増やしていく。



**スワップを記録してください：各スワップのID、償還Address、有効期限をメモしてください。この情報は、技術的な問題が発生した場合の追跡と復旧を容易にします。



### 利用戦略



**キャッシュフローをバランスさせましょう：SwapMarketを使って、On-Chain（貯蓄、長期的な安全性）とLightning（日々の支出、即座の支払い）の配分を、実際のニーズに応じて調整しましょう。



**収益性の計算**：Lightningの恒久的な流動性ニーズについては、スワップを繰り返した場合の累積コストと、Lightningチャネルを直接開設した場合の累積コストを比較してください。SwapMarketは単発の調整に優れており、必ずしも定期的な大きなフローに適しているわけではありません。



## SwapMarket vs Boltz：その違いは？



### ボルツ技術対サービス



**Boltzは、Bitcoin、Lightning、Liquidの間でHTLCを介してアトミックスワップを実装するオープンソース技術**（GitHubの`boltz-backend`）である。



**重要なポイント**：すべてのSwapMarketプロバイダー（Boltz Exchange、ZEUS Swaps、Eldamar、Middle Way）は、Boltzバックエンドの独自のインスタンスを導入しています。したがって、基礎となる技術は同一である。Boltzバックエンドの脆弱性はすべてのプロバイダーに影響を及ぼす可能性があるが、システムのオープンソースの性質により、コミュニティによる監査が可能である。



**Boltz Exchange**は、Boltzチームによって運営される単一のサービスであり、**SwapMarket**は、Boltzの技術を使用する複数のプロバイダーをまとめ、競争力のある価格環境を作り出している。



詳しくはボルツとゼウスのスワップ・チュートリアルをご覧ください：



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### 主な相違点



| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**SwapMarketの利点**：価格競争、バックエンドインスタンスの多様化、リアルタイムの比較。



**代替技術** (SwapMarket非対応)：Lightning Loop (Lightning Labs)、Muun Wallet、NLoop、Breez Wallet。これらのソリューションは、独自の海底スワップの実装を使用しています。



**推奨**：シンプルさを求めるならボルツExchangeを、競争によるコスト最適化ならSwapMarketを。どちらも安全性は同等（HTLCは非保護）。



## 結論



SwapMarketは、複数のプロバイダーを単一のInterfaceに集約することで、Bitcoin/Lightning交換を容易にします。HTLCアーキテクチャはスワップの非保護性を保証し、KYCの不在は機密性を保持し、オープンソースのセルフホスト可能なコードは検閲への耐性を強化する。



プロバイダー間の競争はレートを改善し、流動性の供給源を増やします。2つのLayer管理（On-Chainの節約、ライトニング費用）を最適化するために、SwapMarketは金融主権と機密性を保持する実用的なツールです。



## リソース



### 公式文書




- [SwapMarket - ウェブアプリケーション](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [技術資料](https://docs.boltz.Exchange/)
- [ガイドセルフホスティング](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### 関連プロジェクト




- [ボルツExchange](https://boltz.Exchange) - オリジナル・アトミック・スワップ・サービス
- [ZEUS Swaps](https://zeusln.com) - ライトニングスワップのプロバイダー