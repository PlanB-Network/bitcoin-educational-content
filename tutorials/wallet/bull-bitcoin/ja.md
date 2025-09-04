---
name: ブル Bitcoin Wallet
description: WalletブルBitcoinの使い方はこちら
---

![cover](assets/cover.webp)



このガイドでは、Bull Bitcoin Mobileのインストール、設定、使用方法について説明します。onchain、Liquid、Lightningの3つのネットワークで資金を受取り、送金する方法、そしてBitcoinを1つのネットワークから別のネットワークに移行する方法を学びます。付録として、リソースや連絡先、背景情報、技術的コンセプトの簡単な説明が掲載されています。



## はじめに



**ブルBitcoinモバイル**は、**[ブルBitcoin](https://www.bullbitcoin.com/)**（[アカウント作成](https://app.bullbitcoin.com/registration/orangepeel)）によって開発された**自己完結型**Bitcoin Walletであり、サードパーティに依存することなく、秘密鍵、ひいては資金を完全に管理することができます。オープンソースでCypherpunkの哲学に根ざしたこのWalletは、シンプルさ、機密性、そしてクロスネットワークスワップやPayJoinサポートなどの高度な機能を兼ね備えています。3つのネットワークでビットコインを管理することができます： **Bitcoin onchain**、**Liquid**、**Lightning**の3つのネットワークでビットコインを管理できます。



### 開発の背景



Walletは大きな課題に対応する：Bitcoinのネットワーク料金は、少額の支払いや、小規模な自営ライトニング・チャネルの開設には不向きです。WalletブルBitcoinモバイルは、3つの主要なBitcoinネットワークに依存しながら、セルフ・カストディアル・ソリューションを提供します：





- Bitcoinネットワーク（onchain）**：UTXOの中長期保管や大口取引に最適で、手数料はごくわずか。
- Liquid Network**：高速（～2分）、より機密性（金額を隠す）、低コストの取引用に設計されており、少額の積み立てやプライバシーの保護に最適です。
- Lightning**ネットワーク：インスタントで低コストの決済に最適化されており、日常的な小額から中額の取引に適している。



例えば、ブルBitcoinモバイルでは、**Liquid**や**ライトニング**のポートフォリオに少額を積み立て、相当額に達したら、：





- Liquidおよび/またはLightningの上流で機密性が向上し、1回の取引にオンチェーン手数料がかかるため、安全な中長期保管のためにオンチェーンネットワークに転送する。



### 絶え間ない進化



Walletは常に進化しているので、このチュートリアルとあなたの最新のアプリケーションの間に矛盾が見つかっても驚かないでください。




- 例えば、2025年7月19日現在、**"Buy / Sell / Pay "**ボタンは表示されていますが、アプリケーション内ではグレーアウトされています。これは、Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel) で利用可能なこれらのオプションが間もなく統合され、統一されたエクスペリエンスになるためです。これらの使用は完全にオプションのままです。マルチWallet管理、passphrase、ハードウェアウォレットとの互換性...。
- BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)では、現在のトピックや今後の開発をチェックすることができます。このプロジェクトは100%オープンソースで「公開で構築」されているため、あなたの提案や遭遇したバグを私たちに送ることもできます。




## 1.前提条件



BULL Bitcoin Mobile**を使い始める前に、以下のものが揃っていることを確認してください：





- 対応スマートフォンiOS**（iPhoneまたはiPad）または**Android**デバイス
- インターネット接続
- 安全なバックアップメディア**：あなたの**回復フレーズ**（12語）を紙や金属に書き、安全な場所に保管してください。
- 基礎知識**：Bitcoinの概念（アドレス、トランザクション、手数料）を最低限理解していると便利ですが、このチュートリアルでは初心者向けに各ステップを説明しています。



## 2.インストール





- 申請書をダウンロードする** ：
 - [Google Playストア](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)**Android端末向けアプリケーションストアからダウンロードする。
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Androidデバイス用のAPKを直接ダウンロードする**。
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)**アップルデバイス用TestFlight経由でダウンロードする。
 - 不正な申請を避けるため、開発者名（Bull Bitcoin）を確認する。
 - ダウンロードしたバージョンが、GitHubに記載されている最新の安定版と一致していることを確認してください。
 - Bull Bitcoin Mobileは**オープンソース**です。コードを見るには[BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- アプリケーションをインストールする




## 3.初期設定



### 3.1 アプリケーションを起動します：



このアプリケーションでは、両ポートフォリオにユニークな12語のリカバリーフレーズを使用する：




 - 安全なBitcoin' Wallet**：Bitcoinネットワーク上の取引用（オンチェーン）
 - インスタント・ペイメントのWallet**：LiquidおよびLightningネットワークでの即時取引用



開くと、既存のリカバリーフレーズをインポートするか、新しいWalletを作成するかを尋ねられます：



![image](assets/fr/02.webp)



### 3.2 回復フレーズ：



既存のWalletを再利用する場合は、"**Recover Wallet**"をクリックし、回復フレーズの12語を記入してください。



そうでない場合は、"**Create New Wallet**"をクリックしてください：




- リカバリーのフレーズを細心の注意を払って書き留める。紙または金属に書き留め、安全な場所（貸金庫、オフラインの場所）に保管してください。このフレーズは、デバイスの紛失やアプリケーションの削除の際に、ビットコインにアクセスする唯一の手段となります。
- また、このフレーズを使っている人なら誰でも、あなたのビットコインをすべて盗むことができるという点にも注意が必要です。決してデジタルに保存しないでください：
 - スクリーンショットなし
 - クラウド、電子メール、メッセージングバックアップなし
 - コピー／ペーストができない（クリップボードに保存される危険性がある）



**!この点が重要です**。さらに詳しいサポートは：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 アクセスの確保 ：





- 設定から**PINコード**をクリックしてください。
- アプリケーションへのアクセスを保護するために、堅牢な**PINコード**を設定します。
- このステップはオプションですが、あなたの携帯電話にアクセスできる人があなたのWalletにアクセスするのを防ぐために強くお勧めします。



![image](assets/fr/03.webp)



### 3.4 個人ノードへの接続（オプション）：



WalletのBullBitcoinは、デフォルトでElectrumのサーバーに接続する。Bull Bitcoinが管理する最初のサーバーと、Blockstreamのセカンダリー・サーバーで、どちらもログを残さないと考えられ、トラッキングのリスクを軽減する。



より高い機密性を確保するために、Electrumサーバーを経由して自分のBitcoinノードにアプリケーションを接続することができます（手順は[BullBitcoinのGitHub](https://github.com/orgs/SatoshiPortal/projects/49)にあります）。




## 4.資金の受け取り



Bull Bitcoin Mobile**での資金のお受取りは、.NETをご利用の場合でも、お客様のニーズに合わせてシンプルに行うことができます：




  - Bitcoin (onchain)**ネットワークを長期保存する、
  - Liquid**ネットワークは、Confidential Transactionsをより高速にします、
  - Lightning**ネットワークで、即時、低額決済が可能。



このアプリケーションは、選択したネットワークに応じて、ライトニング受信またはInvoiceアドレスを自動的に生成します。各ネットワークの手順は以下の通りです。



### 4.1.オンチェーン（Bitcoinネットワーク）



ホーム画面では、：




- または、**Secure Bitcoin Wallet**を選択し、"**Receive "**をクリックします：



![image](assets/fr/04.webp)





- または "**受信 "**をクリックし、**Bitcoin**ネットワークを選択します：



![image](assets/fr/05.webp)



#### 4.1.1.コピーまたはスキャン Address のみ」オプション無効（デフォルト）



![image](assets/fr/06.webp)





- これにより、オプションの詳細パラメータにアクセスできる。指定できるのは ：
 - BTC、Satsまたはフィアットでの**金額**。
 - URI/QRコードのコピーに記載する**パーソナルノート**。
 - PayJoin**（詳細は付録3を参照）の有効化により、送信者と受信者のエントリーを組み合わせることで機密性を向上。





- 自動的に生成されるURIの例** ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- 使い方**：送信者と共有するためにURIをコピーするか、QRコードをスキャンさせる。



#### 4.1.2.コピーまたはスキャン Address のみ」オプション有効



![image](assets/fr/07.webp)





- Addressのみコピーまたはスキャン "**オプションを有効にすると、アプリケーションはBitcoin AddressをSegWit(bech32)フォーマットで生成します。





- 例



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



金額やメモを入力しても、QRコードやAddressの控えには含まれません。





- 使い方**：Addressをコピーして送信者と共有するか、送信者にQRコードをスキャンさせます。



#### 4.1.3.新しいAddressの生成





- なぜ取引のたびに新しいAddressを使うのですか？複数の支払いが同じAddressにリンクされるのを防ぎ、Blockchainでの追跡の可能性を制限することで、**プライバシーを保護**します。
 - デフォルトでは、ブルBitcoinは自動的に未使用のAddress.**を生成する。
 - 画面下部の**"New Address"**をクリックすると、強制的に新規Addressを作成することができる。
 - すべての住所はseedのフレーズにリンクされています：あなたが使用しているアドレスの数に関係なく、ポートフォリオは単一の残高を表示し、出荷が行われたときに自動的に資金を統合することができます。





- ヒントブルBitcoinが提供する新しいAddress**は、特別な必要がない限り、常に使用すること（例えば、寄付を受けるためのパブリックAddress）。



### 4.2.Liquid



ホーム画面では、：




- または、**即時支払いWallet**を選択し、**"受信 "**をクリックし、**"Liquid"**：



![image](assets/fr/08.webp)





- または "**受信 "**をクリックし、**Liquid**ネットワークを選択する：



![image](assets/fr/09.webp)



受信」**画面になったら、Liquid Addressをコピーしてください：





- 金額や注記はありません。例



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- または、URI/QRコードのコピーに含める**金額**（BTC、Satsまたはフィアット）および/または**個人メモ**を指定することによって。例



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**使用方法Address/URIをコピーして送信者と共有するか、QRコードをスキャンさせる。



### 4.3.雷



ホーム画面では、：




- または、**即時支払いWallet**を選択し、"**受信 "**をクリックします：



![image](assets/fr/10.webp)





- または "**Receive "**をクリックし、**Lightning**ネットワークを選択する：



![image](assets/fr/11.webp)



#### 4.3.1.操作、限界、利点





- メカニズムBull Bitcoin Walletは、Lightning経由での支払いを可能にするWalletです。Lightning経由で受け取った資金は、**Boltz**経由の自動スワップにより、**Liquid**ネットワーク（Wallet Instant Payments内）に保管されます。これにより、流動性チャネルを管理することなく、自己カストディのままライトニングとやり取りすることができます。





- 制限:**
 - generate、Invoiceをご利用の場合、最低金額**は100サトシ（2025年7月19日現在）。
 - Walletライトニングネイティブでは、送金額とは別に送金手数料を送金者が負担します。2025年7月19日現在、47Satsが送金額から差し引かれます。





- 福利厚生** ：
 - 自己管理**：お客様の資金はLiquid Networkに保管され、お客様の管理下にあります。
 - 高額なオンチェーン手数料が不要**：Liquidに保管することで、Lightningチャネルの開設や流動性の追加にかかる高額なオンチェーン入金を回避できます。これらの操作は、Liquidに蓄積された金額が手数料に見合うようになったときに、後で実行することができます。





- ヒント：** 送信者がWalletブルBitcoinを持っている場合、スワップ料金を避けるために直接Liquid Networkを使用してください。



#### 4.3.2.generate Invoice





- 金額**（BTC、Satsまたはフィアット）を入力します。





- Invoiceに統合される**パーソナルノート**を追加します。送信者がInvoiceを支払うと、Walletの取引詳細にもその旨が記載されます。





- Invoiceの有効期限：*** ライトニングInvoiceの有効期限は**12時間**です。この時間を過ぎると有効期限切れとなり、支払いはできなくなる。新しいInvoiceを作成する必要があります。





- 使い方**：Invoiceをコピーして送信者と共有するか、QRコードをスキャンさせてください。




## 5.資金を送る



### 5.1.基本原則



ホームページから、または財布から：



![image](assets/fr/12.webp)



をクリックして送信画面にアクセスします：



![image](assets/fr/13.webp)



**ブルBitcoinモバイル**は、入力（コピーまたはQRコードでスキャン）されたAddressまたはInvoiceに基づいてネットワーク（Bitcoin、Liquid、またはLightning）を自動的に検出することにより、送金を簡単にします。



### 5.2.オンチェーン伝送（Bitcoinネットワーク）



#### 5.2.1.送信画面



**アクションBitcoinのオンチェーンAddressを入力またはスキャンする。





- 金額が定義されていない場合、例えば：



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- その後、送信画面で選択することができます：
 - BTC、satまたはフィアットでの金額。最低額：546サトシ、22/07/2025。
 - 取引を識別するためのオプションのメモ。トランザクションの詳細で、あなただけが見ることができます。



![image](assets/fr/14.webp)





- 金額がすでに定義されている場合、例えば ：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



その後、以下の確認画面が表示されます。



#### 5.2.2 確認画面



すべてのパラメーター、特に金額、目的地Address、手数料を時間をかけてチェックすること。


それからパラメーターを調整することができる：



![image](assets/fr/15.webp)




- 料金**：をお選びいただけます：
  - お取引の実行速度**と関連手数料のいずれかが見積もられます。
  - 手数料**は、絶対手数料（サトシ単位の手数料合計）または相対手数料（バイト単位の手数料）のどちらかのモードで、お客様の取引速度が推定されます。





- 詳細設定** ：





 - Replace-by-fee (RBF)** ：この機能はデフォルトで有効になっており、高い手数料を支払うことで取引を高速化する（詳細は付録4を参照）。





 - UTXO**の手動選択：資金が複数の異なるWalletアドレスに保管されている場合、資金を送金するアドレスを選択することができます。なぜそうする必要があるのでしょうか？Bitcoinの普及に伴い、送金手数料が高騰しています。少額を複数のアドレスから送金することは、1つのAddressから送金するよりも割高になりますが、今やっておくことで、後で手数料がさらに高くなることを避けることができます。これを**UTXOの統合**と呼ぶ。



![image](assets/fr/16.webp)





- PayJoin**で送信する：この機能が、URIを提供した受信者によって有効化されている場合、例えば：



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



その後、Bull Bitcoin Mobileは、あなたのUTXOと受信者のUTXOを入力として組み合わせて送信を構成し、機密性を向上させます（詳細は付録3を参照）。



### 5.3.Liquidへ送信



#### 5.3.1 送信画面



Liquid**ネットワークは、高速取引（1分間に1ブロックのため～2分）、オンチェーンネットワークよりも高い機密性（マスクされた金額）、非常に低い手数料を可能にします。資金は**Instant Payments Wallet**から引き出されます。



**アクション**：Liquid Address を入力またはスキャンする。





- 金額が定義されていない場合、例えば：



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



その後、送信画面で選択することができます：




- BTC、satまたはフィアットでの金額。最低額なし、1Satoshi可能；
- 取引を識別するためのオプションのメモ。トランザクションの詳細で、あなただけが見ることができます。



![image](assets/fr/17.webp)





- 金額がすでに定義されている場合、例えば ：



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



その後、以下の確認画面に直接移動します。



#### 5.3.2 確認画面



すべてのパラメーター、特に量と行き先のAddressを時間をかけてチェックする。



![image](assets/fr/18.webp)





- 手数料**：取引の複雑さに比例し、通常0.1 sat/vBベース、つまり単純な取引で20～40 satoshis（2025年7月22日現在33 Sats）。



### 5.4.ライトニングに送信



#### 5.4.1 送信画面



Lightning**ネットワークは、少額決済を瞬時に低コストで行うことができ、日々の少額取引に最適です。



**アクションライトニング Invoice を入力またはスキャンする。





- 金額を設定できるLN-URL Addressをスキャンした場合


例: `orangepeel@walletofsatoshi.com`.


その後、送信画面で選択することができます：




 - BTC、Sat、またはフィアットでの金額。2025年7月23日に最低1000サトシから。
 - 取引を識別するためのオプションのメモ。受取人に送信されます。



![image](assets/fr/19.webp)





- ライトニングInvoiceをスキャンした場合、定義された量が含まれています。


例



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



その後、以下の確認画面が表示されます。



注：金額は2025年7月23日の21Satsを上回っていなければならない。



#### 5.4.2 運用、限界、メリット





- 仕組み資金は**インスタント・ペイメントWallet**（Liquid）から引き出され、**ボルツ**との**Liquid→ライトニング**スワップを通じて変換される。





- 制限:**
 - Walletライトニング・ネイティブ（上記参照）より高い最低額**。
 - 経費**＋Liquid → ボルツ経由でのライトニング交換





- 福利厚生** ：
 - 自己管理**：資金はLiquid Networkに保管され、必要に応じてLightning経由で送金可能です。
 - 高額なオンチェーン手数料が不要**：Liquidに保管することで、Lightningチャネルの開設や流動性の追加にかかるオンチェーン入金費用を節約できます。これらの操作は、Liquidに蓄積された金額が手数料に見合うようになったときに、後で実行することができます。





- ヒント：**受信者がWalletブルBitcoinを持っている場合は、スワップコストを避けるために直接Liquid Networkを使用してください。



#### 5.3.3 確認画面



時間をかけてすべてのパラメーター、特に量と行き先のAddressをチェックする。



![image](assets/fr/20.webp)




## 6.履歴を見る



**Bull Bitcoin Mobile** は、**Bitcoin (onchain)**、**Liquid**、**Lightning** ネットワークでの取引を簡単に追跡できます。履歴は2つの方法でアクセスでき、取引の種類ごとに詳細な情報が表示されます。また、外部ブロックブラウザを使用して取引を確認することもできます。



### 6.1.アクセス履歴





- ホーム画面経由** ：
 - Bitcoin Wallet**をクリックすると**オンチェーン**取引が、**Liquid**および**ライトニング**取引は**インスタント・ペイメント Wallet**をクリックしてください。
 - 履歴は、選択されたWalletのタイプに従ってフィルタリングされ、ポートフォリオ合計の真下に表示されます。



![image](assets/fr/21.webp)





- 専用ページ**から：
 - ホーム画面で、**履歴マーク**（時計のアイコンなど）をクリックします。
 - 全取引の一覧ページにアクセスする： **Send**、**Receive**、**Swap**、**PayJoin**、**Sell**、**Buy**（注：SellとBuyは開発中のため、2025年7月20日の現時点では利用できません）。



![image](assets/fr/22.webp)



### 6.2.取引内容



各トランザクションは、ネットワークとアクションのタイプ（送信または受信）に応じて特定の情報を表示します。以下は**トランザクション・オンチェーン**で利用可能な詳細である：



![image](assets/fr/23.webp)



### 6.3.Block explorerによるチェック



Bitcoinオンチェーン**、**Liquid**および**ライトニング**ネットワークの探検家のリストは付録4にある。



Lightning**の場合、パブリックブラウザでは取引が表示されません。詳細（BoltzのスワップIDを含む）はアプリでご確認ください。




## 7.設定



設定 "ページは、ブルBitcoinアプリケーションのホームページから直接アクセスでき、ポートフォリオとユーザーエクスペリエンスの様々な側面を設定、管理するために使用されます。



![image](assets/fr/24.webp)





- Walletバックアップ**：安全なバックアップのためのポートフォリオの復旧フレーズを表示します。リカバリーフレーズの管理と保存のベストプラクティスについては、ポートフォリオ作成のセクション3.を参照。





- Wallet 詳細** ：
 - Pubkey**：generate Bitcoin の受信アドレスに使用される Wallet に関連する公開鍵。
 - 派生パス**：generate Wallet のアドレスを秘密鍵から導出するために使用される導出パス。





- Electrumサーバー（Bitcoinノード）**：オンチェーン取引用にカスタマイズされたBitcoinノードへの接続を設定します。





- PIN コード**：アプリケーションおよびWallet機能へのアクセスを保護するために、セキュリティ・コードを有効化または変更します。





- 通貨**：金額をBTCで表示するかSatsで表示するか、またデフォルトの不換紙幣（ドル、ユーロなど）を選択します。





- オートスワップ設定**：オートスワップ設定**: オートスワップ設定**は、**インスタント・ペイメントWallet (Liquid)** から**Bitcoin On-Chain** Wallet へのBTCの送金を、取引手数料を正当化するのに十分な閾値に達した時点で自動化する機能です。





- ログ**：トラブルシューティングを容易にするために、テクニカルサポートと共有することができます。





- サポート用Telegramアクセス** ：公式Telegramチャンネルに直接リンクし、ユーザーサポートを受けることができます。





- Githubアクセス** ：Bull Bitcoin Githubリポジトリ](https://github.com/SatoshiPortal)にリンクし、オープンソースのコードを閲覧したり、問題を報告することができます。




## 付録



### A1.PayJoin（P2EP）の説明



![image](assets/fr/25.webp)



**定義** ：




- PayJoin、または**Pay-to-EndPoint (P2EP)**は、**オンチェーン**ネットワーク上の機密性を高めるBitcoinトランザクション技術である。PayJoinは送金者と受取人の入力を1つの取引にまとめ、金額と住所を追跡することをより困難にする。



**オペレーション：**。




- PayJoinトランザクションでは、送り手と受け手は、互換性のあるPayJoinサーバーを介して、generate共同トランザクションのために協力する。
- 送信者だけがエントリーを提供する(UTXO)代わりに、受信者もそれ自身のUTXOの1つで貢献する。これは、Blockchainに表示される情報をぼかす。実際の金額に対応する1つのエントリーの代わりに、現在2つのエントリーがあり、出力は交換された金額を直接反映しない。
- 最終的なトランザクションは標準的なBitcoinトランザクション（マルチ入力／マルチ出力）に似ているが、ステガノグラフィ構造によって実際の送信額とアドレス間のリンクを隠している。



**ブルBitcoinモバイル用**。




- 受信**（Address Supply）：PayJoinはデフォルトで有効。
- 送信** ：Walletは自動的にPayJoin URIを検出し、それに応じてトランザクションを構成する：



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**メリット




- 機密性の強化**：PayJoinは、トランザクションのすべてのエントリが単一のエンティティに属するという仮定を無効にする。PayJoinでは、入力は送信者と受信者の両方から行われるため、この仮定は崩れる。
- 金額のマスキング** ：交換された実際の金額は、出力には直接表示されない。受信者のUTXOのインバウンドとアウトバウンドの差として計算されるため、分析が誤解を招く。



**限界




- PayJoinでは、送信者と受信者が互換性のあるウォレットを使用する必要があり、そうでない場合は標準的なオンチェーン取引が使用される。
- 取引は若干複雑になり（インプットとアウトプットが増える）、その結果、コストは若干高くなる。
- 標準的なトランザクションに似せて設計されてはいるが、高度なヒューリスティック（あいまいな出力、既知のPayJoinサーバーなど）により、絶対的な確信はないものの、その使用を疑うことができる。



**詳細はこちら




- [用語集](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2.Replace-by-fee（RBF）の説明



**定義**：Replace-by-fee（RBF）はBitcoinネットワークの機能であり、送信者が高い手数料を支払うことに同意することで、**オンチェーン**トランザクションの確認を早めることができる。



**限界** ：




- RBFは、LiquidまたはLightning取引では利用できない。
- 最初のトランザクションは、作成時にRBF互換とマークされなければならない。



**詳細はこちら




- [用語集](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3.ベストプラクティス



Bull Bitcoin Mobile** を安全かつ効率的に使用するには、以下の推奨事項に従ってください。これらの推奨事項は、**Bitcoin (onchain)**、**Liquid**、および**Lightning**ネットワーク上でお客様の資金を保護し、取引を最適化し、機密性を保持するのに役立ちます。





- リカバリーフレーズの確保** ：
 - チュートリアル[Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- 安全な認証を使用する** ：
 - アプリケーションへのアクセスを保護するために、**強力な暗証番号**または**生体認証**（指紋または顔認証）を有効にします。
 - 暗証番号や生体認証データは絶対に共有しないでください。





- プライバシーの保護** ：
 - generateは、Blockchainのトレースを制限するために、オンチェーンまたはLiquidの受信ごとに新しいAddressを作成する。
 - PayJoinが利用可能な場合は、オンチェーンの送信量に関する機密性を高めるために使用する。
 - 最大限の機密性を確保するためには、Walletを公開ノードではなく、Electrumサーバー経由で自分のBitcoinノードに接続してください。





- お客様のニーズに最適なネットワークをお選びください：
 - オンチェーン**：長期保管や大口取引に有利（手数料は金額に対してごくわずか）。
 - Liquid**：機密性を高めた高速、低コストの転送に使用。
 - ライトニング**：少額を即座に低コストで送金する場合に選択します。Wallet Bull Bitcoinの2つのユーザーであれば、Boltz経由のLightning <> Liquidのスワップ手数料を避けるためにLiquidを選択してください。





- 発送先住所は必ずご確認ください：
 - 送金する前に、Addressをよく確認してください。間違った Address に送金された資金は永遠に失われます。コピー・ペーストか QR コード・スキャンを使用し、決して Address を手でコピー/変更しないでください。





- コストの最適化** ：
 - オンチェーン取引では、緊急度とネットワークの混雑度に応じて適切な手数料（低速、中速、高速）を選択する。
 - 少量の場合はLiquid、またはライトニングを使用する。
 - 確認を早める必要があると予想される場合は、Replace-by-fee（RBF）（付録4参照）をオンチェーン出荷用にアクティブにする。





- アプリケーションを最新の状態に保つ




### A4.追加リソース





- 公式リンクとサポート:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : サポートメール
 - [Bull Bitcoin公式サイト](https://bullbitcoin.com/) :** Bull Bitcoinのサービス、アカウント作成、アプリケーションへのアクセスに関する情報。
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** コード、進化、ロードマップの閲覧、開発への貢献...
 - [アカウントX - ツイッター・ブル Bitcoin](https://x.com/BullBitcoin_)**
 - Walletモバイル用Telegram**グループ：サポートとのグループチャット、「設定」ページをご覧ください。





- ブロック・エクスプローラー
 - on chain ： **[Mempool.space](https://Mempool.space/)**
 - Liquid ： **ブロックストリーム情報](https://blockstream.info/Liquid)**
 - ライトニング **[1ML (Lightning Network)](https://1ml.com/)**





- 学習と個別指導:** **[Plan ₿ Network](https://planb.network/)** ：
 - 回復フレーズの確保



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** ：
 - [用語集](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** ：
 - [用語集](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5.ブル Bitcoin



#### 会社概要



**Bull Bitcoin](https://www.bullbitcoin.com/fr)**は、2013年にカナダのモントリオールにあるBitcoin大使館で設立された、Bitcoinのみに特化した最古の非預託型Exchangeプラットフォームです。Bitcoinエコシステムのパイオニアとして知られるFrancis Pouliot氏が率いる同社は、金融主権とユーザーの自主性を促進する重要な役割を担っている。その使命は、Bitcoin以外の不換紙幣や暗号通貨を拒否する一方で、Bitcoinを自由と決済のツールとして使用することにより、個人が自分のお金をコントロールできるようにすることである。



![image](assets/fr/26.webp)



[アカウント作成](https://app.bullbitcoin.com/registration/orangepeel) Bitcoinの購入と販売に0.25%の割引が適用されます。



#### 価値観と哲学



ブルBitcoinは、CommitmentからCypherpunkの原則とBitcoinの倫理で際立っている：





- Bitcoinに独占フォーカス** ：このプラットフォームは、分散型で検閲に強い通貨というビジョンに忠実です。





- 非カストディアン** ：ユーザーは自分のポートフォリオに資金を送ることで、自分のビットコインを完全に管理することができます。





- 機密性**：個人情報の収集を最小限に抑え、999米ドル以下の取引ではKYC不要の購入オプションを提供。データは規制（カナダのFINTRAC、フランスのAMF）に従って保護されています。





- 透明性**：隠れた手数料はなく、費用はスプレッド（購入価格と売却価格の差額）に含まれています。





- 金融主権**：ブルBitcoinは、伝統的な銀行システムや中央集権的な機関からの独立を促進する。



#### 主なサービス





- フィアット入金** ：ユーザーはBull Bitcoin口座に不換紙幣（CAD、EURなど）を銀行振り込み、または一部のカナダの郵便局で現金/デビットカードで入金することができます。





- Bitcoinの購入** ：ユーザーはBitcoinを購入することができ、そのBitcoinは非預託ポートフォリオに直接送られるため、資金の完全な管理が保証される。





- Bitcoinの定期購入**：ブルBitcoinは、定期的な自動定期購入サービス（DCA - ドルコスト平均法）を提供し、利用可能な残高を引き出し、ビットコインをユーザーが管理するWalletに直接送金することで、価格変動の影響を軽減します。



AutoBuy "と呼ばれるオプションは、フィアットがブルBitcoinの残高に触れるとすぐに換金し、ビットコインをご自身のWalletに送ることができます。このオプションは、DCAを行うために銀行とスケジュールされた定期的な銀行送金と組み合わせることもできます。このオプションは、アプリケーションを開くことなく、Bitcoinの積み立てを自動化します。






- Bitcoinを固定価格で買う「指値注文」**：ユーザーがあらかじめ指定した価格でBitcoinを買うことができ、Bull Bitcoinの指数価格が設定した指値に達するか、または指値を下回ったときに自動的に約定します。





- Bitcoin**の売却：ユーザーはビットコインを売却し、銀行送金またはSEPA送金を介して直接銀行口座に不換紙幣で資金を受け取ることができます。





- 第三者決済**：Bull Bitcoinは、ユーザーがビットコインから銀行口座に不換紙幣を送金することを可能にする。





- ブルBitcoinプライム**：Bull Bitcoin Primeは、富裕層や企業のお客様向けのプレミアム・サービスで、カスタマイズされたソリューションとプレミアム・サポートを提供します。このサービスには、手数料の割引、専任の口座マネージャー、およびカスタマイズされた法人向けサービスのご利用が含まれます。このサービスは、詳細な専門知識と優先的な取り扱いを求める機関投資家、プロのトレーダー、法人のお客様を対象としています。





- モバイルWalletブルBitcoinは、オンチェーン、LiquidおよびLightning Networkトランザクションをサポートする、AndroidおよびiOSで利用可能なオープンソースの自己完結型モバイルWalletを提供しています。





- 教育サポート**：ユーザーがBitcoinポートフォリオを作成、確保、管理できるよう、無料のガイドと個別コーチングを提供。



#### コンプライアンスと安全性





- 規制**：FINTRAC（カナダ）およびAMF（フランス）に登録され、Bull BitcoinはKYC/AML要件に準拠しています。





- セキュリティ**：安全なポートフォリオの使用とオフラインストレージの推奨。個人データはBullのBitcoinインフラでホストされており、100％セルフホストで、いかなる第三者にも依存していません。