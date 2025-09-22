---
name: Phoenixd
description: Phoenixdで最小限のLightningノードをデプロイする
---

![cover](assets/cover.webp)



金融の自律性とは、Lightningインフラストラクチャをコントロールすることでもあります。Bitcoin Lightningをアプリケーションに統合したい開発者や企業にとって、**Phoenixd**は理想的なソリューションです。



PhoenixdはACINQが開発したLightningサーバーで、HTTP APIを介したLightning決済の送受信に特化して設計されています。LNDやCore Lightningのようなフル機能の実装とは異なり、Phoenixdは資金の自己保護を維持しながら、チャネル管理の複雑さをすべて抽象化します。



このチュートリアルでは、Phoenixd をインストール、設定、および使用して、セルフホストインフラストラクチャと使いやすい API を備えた Lightning アプリケーションを開発する方法について説明します。



## Phoenixdとは？



Phoenixdは、ACINQが開発した最小限のLightning専用ノードです。Full nodeのような複雑な管理を必要とせず、Lightningをアプリケーションに統合したい開発者や企業のために設計されたソリューションです。



### 動作原理



**Phoenixdは、ACINQをLSP（Lightning Service Provider）として使用し、自動的に流動性を確保する最小限のLightningノードです。Lightningの支払いを受けると、自動的にACINQノードとチャネルを開き、必要な受信容量を割り当てます。この「オンザフライ」リクイディティは瞬時に行われますが、受信金額の**1% + Mining手数料**が課金されます。



**自動化された管理：**システムは3つの主要なElementsを管理する：




- ライトニング**チャンネル：必要に応じて自動的に開設、閉鎖、管理
- 入出力流動性**：スプライシングとチャネル・オープニングによる自動プロビジョニング
- 料金クレジット** ：チャネルを正当化するには不十分な少額の支払いは、将来の料金のための引当金として保存されます。



### フェニックスのメリット



**秘密鍵（12ワードのseed）と資金を管理します。Phoenixdは、あなたの鍵を共有することなく、あなたのWalletをローカルに生成します。



**個人インフラ:** Phoenixdはお客様のサーバー上で動作するため、詳細なログ、設定、APIコントロールにアクセスできます。資金へのアクセスをサードパーティのサービスに依存する必要がなくなります。



**統合API：** Phoenixdは、他のサービスとの統合、ネイティブLNURLサポート、カスタムアプリケーション開発のためのHTTP APIを備えています。



**簡単なREST APIにより、PhoenixdはLightning決済を必要とするあらゆるアプリケーションやサービスに統合することができます。



**重要:**自動流動性は、LSP（Lightning Service Provider）としてACINQから提供されます。PhoenixdはPhoenix mobileと同じメカニズムで自動チャネル管理を行います。



## Phoenixdのインストール



### 前提条件



Phoenixdを使用するには、Linux環境（Ubuntu/Debian推奨）と基本的なコマンドラインスキルが必要です。最適なパフォーマンスを得るためには、：





- Linuxサーバー**：VPSまたは安定した接続のあるローカルマシン
- OpenJDK 21** ：Java実行環境
- 安定したインターネット接続**：Lightning Networkとの同期用
- ドメイン名**（オプション）：APIへの安全なHTTPSアクセス用



### ダウンロードとインストール



**1.Phoenixd**のダウンロード



GitHub releases]ページ(https://github.com/ACINQ/phoenixd/releases)にアクセスし、お使いのアーキテクチャの最新バージョンをダウンロードしてください：



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2.最初のスタートアップ



Phoenixdを起動して初期化を行う：



```bash
./phoenixd
```



初回起動時には、2つの重要なステップを確認するために「I understand」と入力するよう求められます：



**メッセージ1 バックアップ


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**この12個の言葉**を保存しておくことだ。



*メッセージ2 - 自動流動性：***。


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



それぞれの確認に「了解しました」と入力してください。



![Premier démarrage](assets/fr/01.webp)



*Phoenixdの初回起動：バックアップ確認と自動流動性*。



**3.使用中の構成**（フランス語のみ）



継続的な運用を行うには、systemd .NET を作成する：



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Phoenixdサービスは、systemdと`auto-liquidity`を経由して、2m sat*でアクティブに動作している。



## 設定とセキュリティ



### 設定ファイル



Phoenixd は自動的に `~/.phoenix/phoenix.conf` を作成し、必要なパラメータを設定します：



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**主なパラメーター




- 自動流動性`：自動的にオープンされるチャンネルのサイズ (デフォルト: 2M Sats)
- http-password`：APIの管理者パスワード（Invoiceの作成と支払い発送）
- http-password-limited-access`：パスワード制限（Invoice作成時のみ）



### HTTPSによるセキュアなアクセス



デフォルトでは、Phoenixd API にはローカルの HTTP (`http://127.0.0.1:9740`) でのみアクセスできます。外部（モバイルアプリケーション、他のサーバ、ウェブ統合）からノードを使用するには、セキュアな HTTPS アクセスを設定する必要があります。



**逆プロキシの原則


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx**は**リバースプロキシ**として動作します。ポート443でインターネットからのHTTPSリクエストをリッスンし、ローカル（ポート9740）のPhoenixdにリダイレクトし、暗号化されたレスポンスをクライアントに送り返します。



**SSL/TLS**証明書は、.NET Frameworkが提供するデジタルファイルである：




- サーバーの身元を証明する**（中間者攻撃を防ぐ）
- HTTPS**暗号化を有効にする：APIパスワードを含むすべてのデータは、転送中に暗号化されます。
- Let's Encryptがcertbotツールで無料発行**。



このコンフィギュレーションでは、：




- インターネットからAPIへのセキュアなアクセス**。
- 転送時にAPI**パスワードを暗号化する（平文で転送されるのを防ぐ）。
- HTTPS を必要とする外部アプリケーションに Phoenixd** を組み込む
- 金融APIのセキュリティ標準**への準拠



このHTTPSリバース・プロキシをnginxで設定する：



**1.Nginx**の設定



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2.SSL**証明書



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### 機能テスト



Phoenixdが正常に動作していることを確認する：



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



これらのコマンドは、ノードのステータスと残高に関するJSON情報を返す必要がある（最初は空）。



![Commandes CLI](assets/fr/03.webp)



*ノードの状態を確認するための Getinfo コマンドと getbalance コマンド*。



## APIの使用



### 最初の受信テスト



**1.ライトニングを作る** Invoice



APIを使用して最初のInvoiceを作成します：



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### 自動流動性メカニズムを理解する



**基本原則:** ライトニング決済を受け取る際、Phoenixdは新しいチャネルを開設しなければならないことがあります。このチャネル開設には手数料がかかり、この手数料は受け取った金額から**自動的に差し引かれます。



**10万Satsの具体例:**。



![Premier test de réception](assets/fr/04.webp)



*最初の受入テスト：Sats 10万ドル受領、流動性コスト*控除後のSats最終残高75.561ドル



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**料金計算:**。




- サービス料**：チャンネル容量の1％（211万5000Sats）＝2万1150Sats
- Miningの手数料**：~3,289 Sats（On-Chainの取引の場合）
- 合計**：24,439 Satsが自動的に差し引かれる



*CLIコマンドによる検証：***。


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*入金後の最終残高：ライトニング発送後257Satsの残り*。



**少額の支払いに対する手数料クレジット:** チャネルを開設するには少額すぎる支払い（<約25kSats）を受け取った場合、払い戻し不可の「手数料クレジット」に保管されます。このクレジットは、あなたが十分な金額を受け取ったときに、将来のチャンネル料金の支払いに使用されます。



**2.チャンネル開口部に従う**。



Phoenixdのログを見る：



```bash
journalctl -u phoenixd -f
```



チャネルの開設と流動性手数料の自動引き落としが表示されます。手数料はMempool Bitcoinの条件によって異なりますが、常に1％のサービス料と現在のMining手数料が含まれています。



**3.チャンネルを確認する**。



```bash
./phoenix-cli listchannels
```



このコマンドは、アクティブなチャンネルとそのステータスとバランスを表示します。



### 完全なAPI操作



Phoenixdは9740番ポートでREST APIを公開しており、.NET Frameworkの利用を可能にしています：



**基本業務


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**コスト面で重要なこと:**。




- レシート**：自動流動性の場合、1% + Mining手数料
- 送料**： 0.Lightning Networkに4％の配送料がかかります。



**Webhooks:**Webhooksを使用すると、Phoenixdはイベント発生時(入金、Invoice支払い、チャネルオープンなど)にアプリケーションに**自動的に通知**することができます。Phoenixdに常に更新を要求する代わりに、アプリケーションは即座にHTTP通知を受け取ります。



**顧客が注文の代金を支払うと、オンラインストアは自動的に通知を受信し、トランザクションの即時検証を可能にします。



phoenix.conf`の設定 ：


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## 高度なアプリケーション



### LNURLの統合



Phoenixdは、高度な統合のためにLNURLプロトコルをネイティブにサポートしています：



**LNURL-Pay:**LNURLと互換性のあるサービスに対して支払う。


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** LNURLサービスからの資金回収


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:**サービスにアクセスするためのLightningによる認証


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### LNbitsとの統合



LNbitsは、その[公式文書](https://docs.lnbits.org/guide/wallets.html)によれば、Phoenixdを資金源として使用することができる：



**LNbitsのコンフィギュレーション


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



この統合により、PhoenixdノードからLNbitsのサブアカウントを作成し、ウェブベースのInterfaceで複数のLightningウォレットを管理することができます。



### カスタムアプリケーション



その包括的なREST APIにより、.NET Frameworkを開発することができます：



**Eコマース:** Lightning決済を店舗に直接統合する。


**寄付サービス：** 請求書と自動ウェブフックを備えた寄付システム


**ソーシャル・ネットワーキング・ボット：** チップ機能を持つテレグラム／ディスコード・ボット


**ペイウォール・ライトニング:** ライトニング料金で利用できるプレミアム・コンテンツ



## 安全性とベストプラクティス



### アクセス保護



**APIパスワード:** 自動生成されたパスワードは、Lightning宝物庫の鍵です。絶対に共有せず、疑わしい場合は変更してください。



**ファイアウォール：**ポート9740をインターネットに直接開いたままにしないこと。常にHTTPSでnginxを使用してください。



**認証の強化:** VPNまたはTailscaleを検討し、サーバーへのアクセスを許可されたデバイスのみに制限する。



### 重要なバックアップ



**seed のリカバリー：**サーバーから離れた安全な場所に 12 の単語を保存してください。これが回復の唯一の保証です。



*~/.phoenix ディレクトリ:** このフォルダを定期的にバックアップすることで、(Phoenixd がシャットダウンされた後でも) チャネルの状態を保持し、復元を高速化します。



**また、Phoenixで2FAを有効にしたすべてのサービスのバックアップコードも保管してください。



### モニタリングとメンテナンス



*モニタリング・ログ：***。


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**アップデート:** 新しいバージョンは[GitHub releases](https://github.com/ACINQ/phoenixd/releases)を見てください。アップデートはバイナリを置き換えてサービスを再起動するだけです。



## 代替品との比較



### フェニックスd vs フェニックス・スタンダード



**フェニックス・スタンダード(モバイル) :**。




- 即時インストール、設定不要
- Interfaceの直感的な携帯電話
- Phoenixdと同じ自動保存機能
- ❌ 開発者向けAPIがない
- ❌ 詳細なログにアクセスできない



**Phoenixd（サーバー） :**。




- 統合のための ✅ HTTP API
- ✅ ログへのフルアクセス
- 個人インフラ
- 技術的スキルが必要
- サーバーのメンテナンスが必要



**どちらも自動流動性のためにACINQをLSPとして使用している。



### フェニックスド対LND/コアライトニング



**LND/Core Lightning :**。




- トータル・コントロール、フル・ライトニング・プロトコル
- ✅ 大規模なコミュニティ、成熟した生態系
- ❌ 複雑な手作業による流動性管理
- 学習曲線が大きい



**フェニックス




- ✅ 自動流動性管理（フェニックス・モバイルのように）
- 開発者向け API
- 簡素化された構成
- ACINQをLSPとして使用（独立ルーティングなし）
- 完全なノードよりも柔軟性が低い。



## よくある問題の解決



### APIアクセスの問題



**認証に失敗しました。


1.ファイル `~/.phoenix/phoenix.conf` のパスワードをチェックする。


2.認証形式 `-u:password` をチェックする


3.Phoenixdが起動していることを確認する (`./phoenix-CLI getinfo`)



**接続タイムアウト




- Phoenixdが正しいポート（9740）でリッスンしていることを確認する。
- HTTPSを設定する前にローカルアクセスをテストする
- ログを確認する：journalctl -u phoenixd -f`.



### 流動性の問題



**支払いが届かない。


1.金額が最低基準額（～3万Sats）を超えていることを確認する。


2.チャンネルエラーを特定するためにログを参照する


3.必要に応じてPhoenixdを再起動する



*費用貸勘定」の残高：***。


少額の支払いは引当金として保管される。より大きな金額を受け取ると、チャネル・オープンのトリガーとなり、これらの資金が解放される。



## 結論



Phoenixdは、開発者にとって使いやすさと技術的主権の優れた妥協点です。シンプルかつパワフルなLightning APIと自動流動性管理を提供し、従来のLightningノードの複雑さを解消します。



このソリューションは、.NET Frameworkを使用したい開発者や企業に特に適しています：




- Bitcoin Lightningをアプリケーションに統合する
- ライトニングチャネル管理の複雑さを回避
- セルフホスト型インフラストラクチャのメリット
- シンプルで信頼性の高いAPI



Phoenixdを使用すると、最新のREST APIと技術的側面の自動管理により、独自のプライベートLightningインフラストラクチャを構築できます。プロジェクトにおけるLightning統合を民主化するための理想的なソリューションです。



## 有用なリソース



### 公式文書




- GitHub Phoenixd** ：[github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - ソースコードとリリース
- Phoenix Server**のサイト：[phoenix.acinq.co/server](https://phoenix.acinq.co/server) - ドキュメント全文
- FAQ Phoenixd** ：[phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - よくある質問



### 地域支援




- GitHub Issues** ：[github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - 技術サポート
- ツイッター ACINQ** ：[@ACINQ_co](https://twitter.com/ACINQ_co) - ニュースとお知らせ