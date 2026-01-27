---
name: BTCPay Server - Umbrel
description: UmbrelにBTCPayサーバーをインストールして使用し、BitcoinとLightningを受け入れる
---

![cover](assets/cover.webp)



Bitcoinのエコシステムにおいて、決済の受け入れは加盟店や企業にとって大きな課題です。従来のソリューションは、銀行（クレジットカード、Stripe、PayPal）であろうと、Bitcoin（BitPay、Coinbase Commerce）であろうと、多額の手数料を徴収し、機密性の高いビジネスデータを収集し、気まぐれに取引をブロックしたり検閲したりする仲介者を課します。このような依存は、分散化、機密性、金融主権というBitcoinの基本原則に反している。



BTCPay Serverは、この問題に対するオープンソースの答えとして登場しました。このセルフホストペイメントプロセッサーは、あなた自身のBitcoinノードをプロフェッショナルなインフラに変え、仲介者、追加処理手数料、プライバシーの妥協がありません。2017年以来、貢献者のグローバルコミュニティによって開発されたBTCPay Serverは、BitcoinとLightningの支払いを直接ウォレットに受け取ることができ、常に資金を完全に管理することができます。



従来、BTCPayサーバーのインストールには高度な技術スキルが必要でした：Linuxサーバーの設定、Dockerのマスター、SSL証明書の管理、ネットワークセキュリティなどです。Umbrelは、BitcoinおよびLightningノードに直接統合されたワンクリックのインストールにより、このアプローチに革命をもたらします。この簡素化により、以前は経験豊富な技術者のためのものであったものが、誰でもアクセスできるようになります。



**理解することが重要です**：Umbrel 上の BTCPay サーバーは、デフォルトではローカルネットワークでのみ動作します。請求書の作成、Lightning および Bitcoin による支払いの受付、会計管理は、ホームネットワークに接続されたデバイス（コンピュータ、スマートフォン、タブレット）から行うことができます。この構成は、対面サービスでの請求、対面での支払い管理、またはローカルネットワークからBTCPayサーバーを使用する場合に最適です。一方、BTCPay Serverをインターネット上で一般公開されているオンラインストアに統合するには、一般公開するための追加設定が必要です（この問題はチュートリアルの最後に説明します）。



このチュートリアルでは、UmbrelへのBTCPay Serverの完全なインストール、Bitcoin walletおよびLightningノードの設定、請求書の作成と支払い、会計レポートの管理について説明します。ローカルネットワークでBTCPay Serverを効率的に使用する方法を発見し、eコマースサイトと統合したい場合は、公開するためのソリューションを見ていきます。



## 前提条件



このチュートリアルに従うには、Umbrel が正しくインストールされ、設定されている必要があります。まだインストールしていない場合は、Umbrel のインストールに関するチュートリアルを参照してください。



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin Coreノードはブロックチェーンと完全に同期している必要があります（UmbrelのBitcoinアプリケーションで100％）。この初期同期には、ハードウェアやインターネット接続にもよりますが、通常3日から2週間かかります。



インスタント ライトニング決済を利用するには、Umbrel に LND (Lightning Network Daemon) をインストールする必要があります。この機能を有効にしたい場合は、Umbrel への LND のインストールと設定に関するチュートリアルを参照してください。



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

BTCPayサーバー、そのデータベース、およびライトニングデータ用に、少なくとも50GBの空きディスク容量を確保してください。切断を避けるため、イーサネットケーブルによる安定したインターネット接続を強く推奨します。



## UmbrelにBTCPayサーバーをインストールする



Umbrelインターフェース（`umbrel.local`）からApp Storeにアクセスし、Bitcoinカテゴリで「BTCPay Server」を検索します。



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



インストールをクリックします。Umbrel は自動的に Bitcoin Core と LND がインストールされていることを確認し、デプロイを開始します（2-5 分）。



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



インストールしたら、アプリケーションを開きます。強力な認証情報で管理者アカウントを作成する必要があります。



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



アカウントが作成されると、BTCPayサーバーはすぐに最初のストアを設定するよう促します。ビジネス名を選択し、参照通貨（EUR、USDまたはBTC）を選択します。



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## ローカルネットワーク上のBTCPayサーバーにアクセスする



BTCPayサーバーは、ローカルネットワーク（WiFiまたはイーサネット）上のどのデバイスからでもアクセスできます。ブラウザから ：



```url
http://umbrel.local
```



または直接：



```url
http://umbrel.local:3003
```



**Tailscale**によるリモートアクセス：世界中のどこからでもBTCPayサーバーにアクセスするには、Tailscaleを使用してください。この安全なVPNを使用すると、ローカルネットワーク上にいるかのようにUmbrelに接続できます。Umbrel上のTailscale専用のチュートリアルをご覧ください。



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoinポートフォリオの設定



支払いを受け入れるには、Bitcoin wallet を設定する必要があります。BTCPay Serverはダッシュボードに設定オプションを表示します。



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



wallet Bitcoin の設定は、「Wallets」→「Bitcoin」で行います。



BTCPayで直接新しいポートフォリオを作成するか、既存のポートフォリオをインポートするかの2つのオプションがあります。インポートにはいくつかの方法があります：




- ハードウェアwallet**（推奨）を接続します：Vaultアプリケーション経由で公開鍵をインポート
- walletファイルをインポートする**（推奨）：ポートフォリオからエクスポートしたファイルをアップロードする。
- 拡張公開鍵**を入力します：XPub/YPub/ZPubを手動で入力します。
- walletのQRコードをスキャン** ：BlueWallet、Cobo Vault、Passport、またはSpecter DIYからQRコードをスキャンします。
- wallet seed** (推奨しません) ：12語または24語のリカバリーフレーズを入力してください。



![Options de création de portefeuille](assets/fr/06.webp)



このチュートリアルでは、新しい Hot wallet を作成します: したがって、秘密鍵は Umbrel サーバーに保存されます。この場合、サーバーに大量の資金を保存しないように、定期的に資金をコールドwalletに移動することを強くお勧めします。



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



設定が完了すると、BTCPayサーバーはwalletがon-chainの支払いを受け入れる準備ができていることを確認します。



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Networkをアクティブにする



即時ライトニング決済を受け入れるには、「ウォレット」>「ライトニング」に進みます。LNDノードはすでにUmbrelに設置されているため、「保存」ボタンをクリックするだけで、BTCPayサーバーとLightningノード間の接続が認証されます。



![Configuration du nœud Lightning](assets/fr/09.webp)



## 請求書の作成と支払い



BTCPay Server インターフェースで、「Invoices（請求書）」 > 「Create Invoice（Invoiceを作成）」に移動します。金額を入力し、オプションの説明を追加して、作成をクリックします。



![Création d'une nouvelle facture](assets/fr/10.webp)



その後、「チェックアウト」ボタンをクリックすると請求書が表示されます。BTCPayは、BitcoinアドレスとLightning請求書を含む統一QRコード（BIP21）で請求書を生成します。



![Détails de la facture générée](assets/fr/11.webp)



お客様は互換性のあるwalletでQRコードをスキャンできます。



![Page de paiement avec QR code](assets/fr/12.webp)



支払いが完了すると、Lightningでは数秒で請求書が「決済済み」になる。



![Confirmation de paiement réussi](assets/fr/13.webp)



## 支払管理とトラッキング



レポート」セクションの「請求書」タブでは、日付、金額、ステータス、支払い方法など、請求書の完全な履歴を見ることができます。必要に応じてエクスポートすることもできます。



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## 店舗構成



BTCPay Serverでは、個別のパラメータを持つ複数のストアを管理することができます。各ストアは、eコマースストア、実店舗、サービス課金などの個別のビジネスエンティティを表します。



店舗設定には、いくつかの重要なセクションがあります：



![Paramètres du magasin](assets/fr/15.webp)





- 一般設定**：ショップ名、参照通貨（BTC、EUR、USD）、請求書の有効期限（デフォルト15分）、ブロックチェーン確認の必要回数
- レート**：為替レートのソースとフィアット/Bitcoin変換の設定
- チェックアウトの外観**：チェックアウトページの外観をカスタマイズ（ロゴ、色、パーソナライズされたメッセージ）
- メール設定**：入金通知メールの設定
- アクセストークン**：Eコマース統合（WooCommerce、Shopifyなど）用のAPIトークンの管理
- ユーザー**：さまざまな権限レベル（オーナー、ゲスト）でストアへのユーザーアクセスを管理します。
- ウェブフック**：会計システムやERPシステムとのリアルタイム同期のためのWebhook設定



BTCPay Serverは、eコマース統合、POSシステム、および追加ツールで機能を拡張するためのプラグインセクションも提供しています。



![Gestion des plugins](assets/fr/16.webp)



## 現地使用の利点と限界



**Umbrelを上回るBTCPayサーバーの利点** ：




- 完全な主権：秘密鍵と資金を排他的に管理し、第三者が支払いを凍結したり検閲したりすることはできません。
- 大幅な節約：Bitcoinのネットワーク・コストのみ（Lightningでは数セント）、これに対して従来のプロセッサーでは2～3％。
- 最大限の機密性：登録、本人確認、第三者企業とのデータ共有はありません。
- オープンソースのアーキテクチャは、大規模な開発者コミュニティを通じて、透明性、監査可能性、持続可能性を保証する。
- 高度な技術スキルは不要で、Umbrel経由で簡単にインストールできる



**重要な制限** ：




- ローカルネットワークのみ**：Umbrel上のBTCPayサーバーは、お客様のホームネットワークからのみアクセス可能です。対面課金、フリーランスサービス、または小規模な物理的ビジネスに最適ですが、一般にアクセス可能なオンラインストアには適していません。
- 技術的な全責任：ノードのメンテナンス、定期的なバックアップ、接続性の監視
- ライトニング流動性管理：十分なインバウンド・キャパシティを持つチャネルの開設と管理
- サポートはコミュニティの文書とフォーラムに限られ、商業的なカスタマーサービス部門よりも自主性が求められる。



このローカルネットワークの制限は、顧客がインターネット上のどこからでも決済ページにアクセスできる必要があるeコマースストアにBTCPayサーバーを統合する際の主な障害となります。



## ベストプラクティスと安全性



Umbrel の自動バックアップを有効にし、外部メディア（USB メモリ、ハードディスク、暗号化されたクラウド）にコピーを保存してください。Bitcoin のシード（リカバリーフレーズ）を物理的に離れた安全な場所に保管してください。LNDのchannel.backupファイルをライトニングリカバリー用にバックアップしてください。



Bitcoin Coreの同期、Lightningチャンネル、BTCPayサーバーのレスポンスを定期的に監視します。週に一度の簡単なテスト：generate と数サトシの請求書を支払う。Umbrelを最新の状態に保つ（セキュリティパッチ、機能強化）。メジャーアップデートの前にバックアップを取る。プロフェッショナルな使用のためには、電子メール/SMSアラートによる外部監視（UptimeRobot）を検討してください。



## オンラインストアにBTCPayサーバーを公開する



BTCPayサーバーをウェブベースのeコマースストア（WooCommerce、Shopifyなど）に統合するには、顧客がローカルネットワークだけでなく、どこからでも決済ページにアクセスできる必要があります。



**解決策Nginx Proxy Manager**



Nginx Proxy Manager (Umbrel App Store で入手可能) を使用して、BTCPay Server を公開することができます。このソリューションには ：




- ドメイン名（DuckDNS、No-IP、Afraid.orgを利用したクラシックまたは無料のもの）
- ルーターでポート転送（ポート80と443）を設定する
- SSL証明書を自動的に管理するNginx Proxy Managerのインストール



この構成では、サーバーがインターネットに公開されるため、特に注意が必要です（強力なパスワード、2FA、定期的な更新）。この完全な手順については、専用のチュートリアルを準備する予定です。



## 結論



Umbrel上のBTCPayサーバーは、BitcoinノードのパワーとUmbrelのシンプルさを組み合わせ、すべての人がアクセスできるセルフホスト型のプロフェッショナルな決済インフラを作成します。この金融主権にはメンテナンス責任が伴いますが、Umbrelは、処理手数料の排除、プライバシーの保護、検閲への耐性、資金の完全な管理といった利点に比べ、運用負担を大幅に簡素化します。



ローカルネットワークでの利用は、フリーランスサービスの課金、対面での支払い、小規模な実店舗、あるいは単にBitcoinやLightningを管理された環境で学習・実験するなど、すでに幅広い用途をカバーしています。公開が必要なeコマースのニーズには、Nginx Proxy Managerソリューションがありますが、追加の技術設定が必要です。



ビジネス、駆け出しのプロジェクト、または単なる実験のいずれであっても、Umbrel上のBTCPayサーバーは、完全な財務的自律性を提供します。あなたの最初のストア、最初の請求書、最初の支払いをあなたの主権インフラストラクチャに直接受け取ることから道は始まります。



## リソース



### 公式文書




- [BTCPayサーバー公式サイト](https://btcpayserver.org)
- [完全なBTCPayサーバードキュメント](https://docs.btcpayserver.org)
- [GitHub BTCPayサーバー](https://github.com/btcpayserver/btcpayserver)
- [テールスケールのドキュメント](https://tailscale.com/kb)


### コミュニティとサポート




- [フォーラムBTCPayサーバー](https://chat.btcpayserver.org)
- [フォーラムの傘](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)