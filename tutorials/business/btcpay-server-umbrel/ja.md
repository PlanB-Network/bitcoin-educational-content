---
name: BTCPAY SERVER - アンブレル
description: BitcoinとLightningを受け入れるためのUmbrelへのBTCPAY SERVERのインストールと使用
---

![cover](assets/cover.webp)



Bitcoinのエコシステムにおいて、決済の受け入れは加盟店や企業にとって大きな課題となっている。従来のソリューションは、銀行（クレジットカード、Stripe、PayPal）であろうと、Bitcoin（BitPay、Coinbase Commerce）であろうと、多額の手数料を課す仲介者を課し、あなたの機密のビジネスデータを収集し、彼らの気まぐれであなたの取引をBLOCKまたは検閲することができます。この依存は、分散化、機密性、金融主権というBitcoinの基本原則に反している。



BTCPAY SERVERは、この問題に対するオープンソースの答えとして登場しつつある。このセルフホスト型決済プロセッサーは、中間マージン、追加処理手数料、プライバシーの妥協なしに、あなた自身のBitcoinノードをプロフェッショナルなインフラに変えます。2017年以来、貢献者のグローバル・コミュニティによって開発されたBTCPAY SERVERは、あなたのウォレットに直接BitcoinとLightningの支払いを受け取ることを可能にし、あなたの資金を常に完全にコントロールします。



従来、BTCPAY SERVERのインストールには高度な技術スキルが必要だった：Linux サーバー設定、Docker マスター、SSL 証明書管理、ネットワーク・セキュリティなどです。Umbrelは、BitcoinとLIGHTNING NODEに直接統合されたワンクリック・インストールにより、このアプローチに革命をもたらします。この簡素化により、以前は経験豊富な技術者のためのものであったものが、誰でもアクセスできるようになります。



**理解することが重要です**：BTCPAY SERVER on Umbrel は、デフォルトではローカルネットワークでのみ動作します。請求書の作成、Lightning および Bitcoin による支払いの受付、会計管理は、ホームネットワークに接続されたデバイス（コンピュータ、スマートフォン、タブレット）から行うことができます。この構成は、対面サービスでの請求、対面での支払い管理、またはローカルネットワークからBTCPAY SERVERを使用する場合に最適です。一方、BTCPAY SERVERをインターネット上で公開されるオンラインストアに統合するには、公開するための追加設定が必要になります（この問題はチュートリアルの最後に説明します）。



このチュートリアルでは、BTCPAY SERVER の Umbrel への完全なインストール、Bitcoin Wallet LIGHTNING NODE の設定、請求書の作成と支払い、会計レポートの管理について説明します。BTCPAY SERVERをローカルネットワークで効果的に使用する方法、そしてeコマースサイトと統合したい場合の公開用ソリューションについて説明します。



## 前提条件



このチュートリアルに従うには、Umbrel が正しくインストールされ、設定されている必要があります。まだインストールしていない場合は、Umbrel のインストールに関するチュートリアルを参照してください。



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Bitcoin coreノードはBlockchainと完全に同期している必要があります（UmbrelのBitcoinアプリケーションでは100％）。この初期同期には、ハードウェアやインターネット接続にもよりますが、通常3日から2週間かかります。



インスタント ライトニング決済を利用するには、Umbrel に LND (Lightning Network Daemon) をインストールする必要があります。この機能を有効にしたい場合は、Umbrel への LND のインストールと設定に関するチュートリアルを参照してください。



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

BTCPAY SERVER、データベース、ライトニングのデータ用に最低50GBの空き容量を確保してください。切断を避けるため、イーサネットケーブルによる安定したインターネット接続を強く推奨します。



## BTCPAY SERVERをアンブレルに取り付ける



Umbrel Interface (`umbrel.local`)からApp Storeに行き、Bitcoinカテゴリで「BTCPAY SERVER」を検索する。



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



インストールをクリックします。Umbrel は自動的に Bitcoin core と LND がインストールされていることを確認し、デプロイを開始します（2-5 分）。



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



インストールしたら、アプリケーションを開きます。強力な認証情報で管理者アカウントを作成する必要があります。



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



アカウントが作成されると、BTCPAY SERVERはすぐに最初のストアを設定するよう促します。プロフェッショナル名を選択し、参照通貨（EUR、USDまたはBTC）を選択します。



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## ローカルネットワークでBTCPAY SERVERにアクセスする



BTCPAY SERVERは、ローカルネットワーク（WiFiまたはイーサネット）上のどのデバイスからでもアクセスできます。ブラウザから ：



```url
http://umbrel.local
```



または直接：



```url
http://umbrel.local:3003
```



**Tailscale**でリモートアクセス：世界中のどこからでも BTCPAY SERVER にアクセスするには、Tailscale をご利用ください。このセキュアな VPN により、ローカルネットワークにいるかのように Umbrel に接続できます。Umbrel上のTailscale専用のチュートリアルをご覧ください。



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Bitcoinポートフォリオの設定



支払いを受け付けるには、Bitcoin Wallet を設定する必要がある。BTCPAY SERVERはダッシュボードに設定オプションを表示する。



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Wallet Bitcoin の設定は、「Wallets」→「Bitcoin」で行います。



BTCPayで直接新しいポートフォリオを作成するか、既存のポートフォリオをインポートするかの2つのオプションがあります。インポートにはいくつかの方法があります：




- Hardware Wallet**に接続する（推奨）：Vaultアプリケーション経由で公開鍵をインポート
- Walletファイルをインポートする**（推奨）：ポートフォリオからエクスポートしたファイルをアップロードする
- 拡張公開鍵**を入力します：XPub/YPub/ZPubを手動で入力します。
- WalletのQRコードをスキャン** ：BlueWallet、Cobo Vault、Passport、またはSpecter DIYからQRコードをスキャンします。
- Wallet seed** (推奨しません) ：12語または24語のリカバリーフレーズを入力してください。



![Options de création de portefeuille](assets/fr/06.webp)



このチュートリアルでは、新しいHot Walletを作成します：したがって、秘密鍵はUmbrelサーバーに保存されます。この場合、大量の資金をサーバーに保管することを避けるため、定期的に資金をCold Walletに移動することを強くお勧めします。



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



一度設定されると、BTCPAY SERVERはWalletがOn-Chainの支払いを受け入れる準備ができていることを確認する。



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Networkをアクティブにする



Lightningによる即時支払いを受け入れるには、「Wallets」>「Lightning」に進みます。BTCPAY SERVERとLIGHTNING NODEの接続を確認するには、"Save "ボタンをクリックします。



![Configuration du nœud Lightning](assets/fr/09.webp)



## 請求書の作成と支払い



Interface BTCPAY SERVER で、「Invoices（請求書）」 > 「Create Invoice」に移動します。金額を入力し、任意の説明を追加し、「作成」をクリックします。



![Création d'une nouvelle facture](assets/fr/10.webp)



その後、「チェックアウト」ボタンをクリックすると、Invoiceが表示されます。BTCPayは、Bitcoin AddressとLightning Invoiceを含む統一QRコード（BIP21）でInvoiceを生成します。



![Détails de la facture générée](assets/fr/11.webp)



お客様は互換性のあるWalletでQRコードをスキャンできます。



![Page de paiement avec QR code](assets/fr/12.webp)



支払いが完了すると、Invoiceはライトニングにとって数秒のうちに "決済 "される。



![Confirmation de paiement réussi](assets/fr/13.webp)



## 支払管理とトラッキング



レポート」セクションの「請求書」タブでは、日付、金額、ステータス、支払い方法など、請求書の完全な履歴を見ることができます。必要に応じてエクスポートすることもできます。



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## 店舗構成



BTCPAY SERVERでは、複数のストアを個別のパラメータで管理できます。各ストアは、eコマース・ストア、実店舗、サービス課金といった個別のビジネス・エンティティを表します。



店舗設定には、いくつかの重要なセクションがあります：



![Paramètres du magasin](assets/fr/15.webp)





- 一般設定**：店舗名、参照通貨（BTC、EUR、USD）、Invoiceの有効期限（デフォルト15分）、Blockchainの必要確認回数
- レート**：Exchangeレートソースとフィアット/Bitcoin変換の設定
- チェックアウトの外観**：チェックアウトページの外観をカスタマイズ（ロゴ、色、パーソナライズされたメッセージ）
- メール設定**：入金通知メールの設定
- アクセストークン**：API token eコマース統合管理（WooCommerce、Shopifyなど）
- ユーザー**：さまざまなレベルの権限（オーナー、ゲスト）でストアへのユーザーアクセスを管理します。
- ウェブフック**：会計システムやERPシステムとのリアルタイム同期のためのWebhook設定



BTCPAY SERVERはまた、eコマース統合、POSシステム、追加ツールで機能を拡張するためのプラグインセクションも提供しています。



![Gestion des plugins](assets/fr/16.webp)



## 現地使用の利点と限界



**アンブレルのBTCPAY SERVERの利点** ：




- 完全な主権：秘密鍵と資金を排他的に管理し、第三者が支払いを凍結したり検閲したりすることはできません。
- 大幅な節約：Bitcoinのネットワーク・コストのみ（Lightningでは数セント）対、従来のプロセッサーでは2～3％。
- 最大限の機密性：登録、本人確認、第三者企業とのデータ共有はありません。
- オープンソースのアーキテクチャは、大規模な開発者コミュニティを通じて、透明性、監査可能性、持続可能性を保証する。
- 高度な技術スキルは不要で、Umbrel経由で簡単にインストールできる



**重要な制限** ：




- ローカルネットワークのみ**：アンブレルのBTCPAY SERVERは、ホームネットワークからのみアクセス可能です。対面課金、フリーランスサービス、小規模な物理的ビジネスに最適ですが、インターネット上で一般にアクセス可能なオンラインストアには不向きです。
- 技術的な全責任：ノードのメンテナンス、定期的なバックアップ、接続性の監視
- ライトニング流動性管理：十分なインバウンド・キャパシティを持つチャネルの開設と管理
- サポートはコミュニティの文書とフォーラムに限られ、商業的なカスタマーサービス部門よりも自主性が求められる。



このLANの制限は、顧客がインターネット上のどこからでも決済ページにアクセスできる必要がある電子商取引ストアにBTCPAY SERVERを統合する際の主な障害となる。



## ベストプラクティスと安全性



自動 Umbrel バックアップを有効にし、外部メディア（USB スティック、Hard ディスク、暗号化クラウド）にコピーを保存してください。Bitcoin のシード (リカバリ・フレーズ) を物理的に離れた安全な場所に保管してください。ライトニング・リカバリー用に LND チャンネル.backup ファイルを保存する。



Bitcoin coreの同期、ライトニング・チャンネル、BTCPAY SERVERのレスポンスを定期的にモニター。週1回の簡単なテスト：generateと数サトシの請求書を支払う。Umbrelを常に最新の状態に保つ（セキュリティパッチ、機能強化）。メジャーアップデートの前にバックアップを取る。プロフェッショナルな使用の場合、電子メール/SMSアラートによる外部監視（UptimeRobot）を検討する。



## BTCPAY SERVERをオンラインストアに公開



BTCPAY SERVERをウェブベースのEコマースストア（WooCommerce、Shopifyなど）に統合するには、顧客がローカルネットワークだけでなく、どこからでも決済ページにアクセスできる必要があります。



**解決策Nginx Proxy Manager**



Nginx Proxy Manager (Umbrel App Store で入手可能) を使用して、BTCPAY SERVER を公開することができます。このソリューションには .NET Framework が必要です：




- ドメイン名（DuckDNS、No-IP、Afraid.orgを利用したクラシックまたは無料のもの）
- ルーターでポート転送（ポート80と443）を設定する
- SSL証明書を自動的に管理するNginx Proxy Managerのインストール



この構成では、サーバーがインターネットに公開されるため、特に注意が必要です（強力なパスワード、2FA、定期的な更新）。この完全な手順については、専用のチュートリアルを準備する予定です。



## 結論



BTCPAY SERVER on Umbrelは、BitcoinノードのパワーとUmbrelのシンプルさを組み合わせ、誰もがアクセスできるセルフホスト型のプロフェッショナルな決済インフラを構築します。この金融主権にはメンテナンス責任が伴いますが、Umbrelは、処理手数料の排除、プライバシーの保護、検閲への耐性、資金の完全な管理といった利点に比べ、運用負担を大幅に簡素化します。



ローカルネットワークでの利用は、フリーランスサービスの課金、対面での支払い、小規模な実店舗、あるいは単にBitcoinやLightningを管理された環境で学習・実験するなど、すでに幅広い用途に及んでいます。公開が必要なeコマースのニーズには、Nginx Proxy Managerソリューションがありますが、追加の技術的設定が必要です。



ビジネス、駆け出しのプロジェクト、または単なる実験であろうと、BTCPAY SERVER on Umbrelは完全な財政的自律性を提供します。その道は、最初の店舗、最初のInvoice、あなたの主権基盤に直接入金される最初の支払いから始まります。



## リソース



### 公式文書




- [BTCPAY SERVER公式サイト](https://btcpayserver.org)
- [BTCPAY SERVER完全ドキュメント](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [テールスケールのドキュメント](https://tailscale.com/kb)


### コミュニティとサポート




- [フォーラムBTCPAY SERVER](https://chat.btcpayserver.org)
- [フォーラムの傘](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)