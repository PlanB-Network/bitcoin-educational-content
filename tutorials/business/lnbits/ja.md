---
name: LNbits
description: マーチャント会計プラットフォーム
---
![presentation](assets/lnbits-intro.webp)

# 会計システム

LNbitsには、入出金資金のコントロールやチャネリング、ウェブストアの接続、さらにはハードウェアウォレットや自作ATMのようなデバイスを接続するためのツールがたくさん詰まっています。ユーザータイプは以下の通りです：


- LNbitsを資金管理のインターフェースとして、またその追加機能として利用したいウォレット所有者。
- ビットコインのオンチェーンおよびライトニングネットワーク決済を受け入れたいオンラインおよびオフラインの加盟店またはサービスプロバイダー。
- Lightning Networkアプリケーションを構築したい開発者。
- ノードをLNbitsシステムと統合して会計処理を行いたいノードオペレータ。
- そのニーズはそれぞれ異なります。LNbitsは、すべてのユーザーが自分に最適な方法で機能を利用できるよう、モジュール方式で構築しています。

# ウォレットマネージャー

LNbitsはフリーでオープンソースの会計システムであり、ノードマネージャーではない。チャンネル管理は、LNDやc-lightningのようにLNbitsに資金源として接続されているLightningノードの領域です。LNbitsシステムのスーパーユーザーまたはアドミンユーザーは、アカウンティング機能と内部拡張機能の全体的なアクセス可能性と設定を管理する責任があります。

LNbitsは、ユーザーとLightningノードの間のインターフェイスとして機能し、決済ネットワークを管理し、相互作用するためのシンプルでユーザーフレンドリーな方法を提供します。

LNbitsは、あなたのノードのための「ワードプレス・モジュラー・フレームワーク」のようなものだと考えてください。多くのユースケースに組み合わせることができる拡張機能をベースにした、管理しやすいプラットフォームです。

LNbitsはあなた自身の銀行財務管理ソフトウェアだと考えてください。LNbitsはあなたのノードを拡張し、あなたのノードに搭載されている複数のライトニングウォレットを実行できるようにします。これらのウォレットは必ずしもあなた自身のものである必要はありません。例えば、LNノードのランナーであるあなたが、既に十分なチャネルの流動性と資金を持っていて、友人や家族、自分の店や他の普通の商店にビットコインバンキングサービスを提供したいとします。

あなたのノードの他のウォレットやすべてのノードの流動性にアクセスすることなく、あなたのノードに「銀行口座」を開設する簡単な方法を提供します。あなたのノード（銀行）は、彼らの支払い（イン/アウト）のためのトランスポートプロバイダとしてのみ機能します。

注意：あなたの「顧客」があなたのノードのLNbits銀行口座に入金した資金は、すべてあなたのノードのLNチャンネルに直接入金されます。つまり、これらの資金の実際の所有者はあなたです。あなたは彼らの資金に対して大きな責任を負うことになります。邪悪になって資金を持ち逃げしたり、邪悪になって高い手数料を請求したりしないでください。私たちは不換紙幣の銀行家とやりたいのであって、お互い（ビットコインユーザー）とやりたいのではありません。

# デモプラットフォーム

デモは[https://legend.lnbits.com](https://legend.lnbits.com)にあります。このデモは完全に機能し、ライトニングネットワークやLNbits、LNURLの特徴について学ぶことができます。私たちは、あなたがこれを使用することを妨げることはできませんが、あなたの本番セットアップには使用しないようお願いします。私たちは新機能をテストするために頻繁にサーバーに取り組んでいるだけでなく、あなた自身のノードとLNbitsを主権的な方法で運用することを奨励したいと思います。LNbitsをOpennode、Luna、Votageのようなクラウド上のカストディアン・ファンディング・サービスに接続することもできますし、Telegram上のLightning Tipbotに接続することもできます。

# LNbitsチラシ

加盟店や建築関係の友人に基本的な情報を渡したいですか？この度、皆様にご利用いただけるフライヤーを作成いたしました。サイズは6ページ（2つ折り）、横3508、縦2480pxの世界的に一般的なフライヤーです。

マーチャント用LNbits：[EN](/assets/lnbits-merchants-ja.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

ビルダー向けLNbits：[EN](/assets/lnbits-builders-ja.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# いくつかの基本

LNbitsはLNURLプロトコルに基づいて動作します。つまり、リクエストはhttps:// クリアネットリンク（自己署名証明書不可）またはhttp:// v2/v3 オニオンリンクの2つの形式で有効です。LNURLp/wのQRコードやNFCカードのようなLNbitsサービスを提供するためには、LNbitsをclearnet（https）に開放する必要があります。

LNbitsをインストールする前に、LNbitsとは何か、LNbitsがどのような可能性をあなたにもたらすかについて、以下の一般的なガイドを読み、理解していることを確認してください。


- [LNDガイド](https://docs.lightning.engineering/)｜LNDのインストール
- [LND設定例](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND設定
- [CLNガイド](https://docs.corelightning.org/docs/installation)｜CLNのインストール
- [LUDs](https://github.com/lnurl/luds) LNURLスペック｜[NIPs](https://github.com/nostr-protocol/nips) Nostrスペック
- [監視塔の運営](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower)｜とても重要だ！

LNbitsを具体的なユースケース・シナリオで使用する、より詳細なガイドはこちら：


- [LNbits入門](https://darthcoin.substack.com/p/getting-started-lnbits)｜サブスタックガイド
- [LNbitsで安全を確保するためのToDo](https://youtu.be/i5FQf96e6zg)｜Youtube動画
- [ライトニング・ネットワーク上のプライベートバンク](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning)｜サブスタック・ガイド
- [友人や家族のために財布を管理する](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [小さなレストラン/ホテルのためのLNbits](https://darthcoin.substack.com/p/lnbits-for-small-merchants)｜サブスタックガイド
- [LNbits Streamerコパイロットの使用](https://darthcoin.substack.com/p/lnbits-streamer-copilot)｜サブスタックガイド
- [LNbitsで始めるNOSTRマーケット](https://darthcoin.substack.com/p/lnbits-nostr-market)｜サブスタックガイド
- [学校プロジェクトやフェスティバル・イベントでのLNbitsの使用](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) サブスタック・ガイド

# LNbitsのインストール

## 基本インストールガイド

LNbitsはどのLinux OSマシンにもインストールできます。強力なマシンやサーバーは必要なく、十分なRAMメモリとデータベース用のディスク容量があれば十分です。BTC/LNノード（ローカルPCまたはリモートVPS）とは別に、またはノードと同じマシン上で一緒に、またはバンドルノードソフトウェアマシンにインストール済みで実行することができます。

poetryやnixのような一般的なパッケージマネージャから選択できます。デフォルトでは、LNbitsはデータベースとしてSQLiteを使用します。負荷の高いアプリケーションには PostgreSQL を使うことをお勧めします。[poetryやnixを使った基本的なインストールガイドはこちら](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)を参照してください。

LNbitsを初めてお使いになる方のために、特定の環境でLNbitsを動作させるための、より詳細なステップ・バイ・ステップのガイドをご覧いただけます：


- [クリアネットのLNbits](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [VPS上のLNbits](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [クラウドフレアのLNbits](https://www.nodeacademy.org/lnbits) by Leo

また、[dockerised Setup on a VPS with PostgreSQ, LightningTipBot as funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) のビデオもご覧ください。

[その他の設置シナリオはこちら](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server)。

バンドルソフトウェアノードについては、それぞれのLNbitsに関するドキュメントを参照してください：[Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

技術的なことに興味がなく、資金源やLNbitsを自分でホスティングしたくない場合は、[LNbits SaaSバージョン](https://saas.lnbits.com)(Software-as-a-service)をご利用ください。基本的にはクラウド上のLNbitsのようなものですが、資金源（ノード、LNbitsウォレット、LNtipbot、fakewalletなど）と環境変数を自分で定義することができます。

[LNbits SaaSの具体的な利用方法については、こちらをご覧ください](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools)。

## 資金源

LNbitsはノード管理ソフトウェアではなく、LNDまたはCLNの資金源の上にLNに焦点を当てた会計システムです。最初のインストール後、http://localhost:5000/。

.envファイルに`adminUI=TRUE`を設定している場合は、`LNBITS_BACKEND_WALLET_CLASS`を必要なソースに変更して.envファイルを編集してください。

lnbits/ または lnbits/apps/data フォルダ内の .env ファイルを見つけるには、コマンドを拡張して `ls -a` でディレクトリ内のファイルをリストアップします。

また、追加のパッケージをインストールしたり、希望する資金源を選択して追加のセットアップ手順を実行する必要があるかもしれません。再起動後、新しいセットアップが有効になります。

LNbitsにはどのような資金源がありますか？

LNbitsは、多くのライトニングネットワークの資金源の上で実行することができます。現在、CoreLightning、LND、LNbits、LNPay、OpenNodeがサポートされており、定期的に追加されています。

流動性が高く、良いピアとつながっているソースを選ぶことが重要です。公共サービスにLNbitsを使えば、ユーザーの支払いは双方向にハッピーに流れるだけです。

バックエンドウォレット(資金源)は、`.env`ファイルまたはスーパーユーザアカウントのManage-Serverセクションにある以下のLNbits環境変数を使用して設定できます。

.envバージョンを使用したい場合は、ここにパラメータがあります：

### コアライトニング


- シーエルエヌ
  - lnbits_backend_wallet_class`： **CoreLightningWallet**
  - corelightning_rpc`：/ファイル/パス/lightning-rpc
- スパーク（Cライトニング）
  - lnbits_backend_wallet_class`： **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - SPARK_TOKEN`: シークレット・アクセス・キー

### ライトニング・ネットワーク・デーモン


- LND (REST)
  - lnbits_backend_wallet_class`： **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - lnd_rest_cert`：/ファイル/パス/tls.cert
  - lnd_rest_macaroon`：/file/path/admin.macaroon または Bech64/Hex
  - LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - lnbits_backend_wallet_class`： **LndWallet**
  - LND_GRPC_ENDPOINT`: ip_address
  - LND_GRPC_PORT`: ポート
  - lnd_grpc_cert`：/ファイル/パス/tls.cert
  - lnd_grpc_macaroon`：/file/path/admin.macaroon または Bech64/Hex

AESで暗号化されたマカロン（詳細はこちら）を使うこともできます。


  - LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

マカロンを暗号化するには、`./venv/bin/python lnbits/wallets/macaroon/macaroon.py`を実行する。

### LNbits（別のLNbitsインスタンス）


- クラウドサーバーまたはご自宅のサーバーにLNbitsインスタンスをホスト
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - lnbits_endpoint`: https://lnbits.mydomain.com
  - LNBITS_KEY`: my-lnbits-AdminKey
- LNbits レジェンド・デモ・サーバー (!!本番/商用目的には使用しないでください。テスト用のみです!!)
  - lnbits_backend_wallet_class`： **LNbitsWallet**
  - lnbits_endpoint`: https://legend.lnbits.com
  - LNBITS_KEY`: legend-lnbits-AdminKey

### ライトニング・チップボット

テレグラムから[Lightning Tipbot](https://t.me/LightningTipBot)に接続するには、以下のパラメータを設定する必要があります：


  - lnbits_backend_wallet_class`： **LnTipsWallet**
  - lnbits_endpoint`: https://ln.tips
  - LNBITS_KEY`：キーを取得するには、テレグラムの LightningTipbot とのプライベートチャットで /api を実行する必要があります。

LNbits with LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)のインストール方法はこちらもご覧ください。

### IBEX HUB

こちら](https://ibexpay.ibexmercado.com/onboard)に登録し、そこからキー/トークンを取得する。エンドポイントはhttps://ibexpay-api.ibexmercado.com。

詳細は[IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api)を参照。

### LNPay

請求書リスナーを動作させるには、LNbitsに一般にアクセス可能なURLを設定し、[LNPay webhook](https://dashboard.lnpay.co/webhook/)を`<your LNbits host>/wallet/webhook`を指すように設定する必要があります。https://mylnbits/wallet/webhook`は支払いに関する通知を受けるエンドポイントのURLになります。


  - lnbits_backend_wallet_class`： **LNPayWallet**
  - lnpay_api_endpoint`: https://api.lnpay.co/v1/
  - LNPAY_API_KEY`: sak_apiKey
  - LNPAY_WALLET_KEY`: waka_apiKey

### オープンノード

インボイスを利用するには、LNbitsに一般からアクセス可能なURLが必要です。ウェブフックの設定はオプションです。


  - lnbits_backend_wallet_class`： **OpenNodeWallet**
  - opennode_api_endpoint`: https://api.opennode.com/
  - OPENNODE_KEY`: opennodeAdminApiKey

### アルビー

Albyは、LNbitsの資金源として使用できるLNウォレット機能とLNDHUBアカウントを備えたブラウザ拡張機能です。[詳細はこちら](https://getalby.com/)。

インボイスをご利用いただくには、LNbitsに一般からアクセス可能なURLが必要です。手動でのWebhook設定は不要です。Albyのアクセストークンはこちらから生成できます: https://getalby.com/developer/access_tokens/new


- lnbits_backend_wallet_class`：AlbyWallet
- alby_api_endpoint`: https://api.getalby.com/
- alby_access_token`：AlbyAccessToken

## 追加／トラブルシューティングガイド

以下は補足説明です。矢印をクリックすると説明が拡大します。

### キルスウィッチ🚨」。

最近、LNbitsだけでなく世界的に危険なバグが多発しているため、LNbitsでも対策を講じることにしました。脆弱性や資金喪失につながるバグが再び発生した場合、警告を受けたり、直接アクションを起こすことができるようになりました。

![killswitchn](assets/lnbits-killswitch.webp)

void-walletに切り替えた場合、インスタンス上のすべてのユーザータイプは、テーマ/言語エリアの右隣にある "LNbits is in Beta "の黄色いバナーを見ることになります。ウィンドウの左側で緑色にハイライトされている新しいサーバータブを見てください。

仕組みは？killswitchを有効にすると、LNbitsコアチームのみが利用できる秘密のgithubリポジトリがX分間隔（指定可能）でチェックされます。このリポジトリで脆弱なバグが公開された場合、そのバグをトリガーとして、購読しているすべてのインスタンスでkillswitchが作動し、あなたのlnbitsインスタンスがvoid walletを使用するように移行します。雲行きが怪しくなり、セキュリティアップデートをインストールした場合は、サーバーの管理セクションから資金源をノードやウォレットなどに設定することができます。このwikiには資金源の切り替えに関するセクションがあります。

### 管理者とスーパーユーザーの違い

LNbits Admin UI は LNbits フロントエンドから LNbits の設定を変更するためのものです。デフォルトでは無効になっており、最初に `.env` ファイルに環境変数 `LNBITS_ADMIN_UI=true` を設定すると、設定が初期化されて使用されます。それ以降は.envファイルの設定ではなくデータベースの設定が使用されます。

### スーパーユーザー

管理者用UIでは、サーバーにアクセスできるスーパーユーザーを導入し、フロントエンドやapiからサーバーをクラッシュさせたり、反応しなくさせたりするような設定を変更できるようにしました。スーパーユーザーは、データベースの設定テーブル内にのみ保存されます。設定を "デフォルトにリセット "して再起動すると、新しいスーパーユーザーが作成されます。また、スーパーユーザーの存在をチェックするために、APIルートにデコレーターを追加しました。そのIDはapiやフロントエンドに送られることはなく、スーパーユーザーかどうかのbool(yes/no)を受け取るだけです。

スーパー・ユーザーだけが、「トップアップ」セクションから異なるウォレットにサトシを送金することができる。

スーパーユーザが作成されたときに、Webhook経由でスーパーユーザを別のサービスにポストすることもできます。詳細は https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings` を参照してください。

フロントエンドでは、サーバーの管理セクションを開き、テーマ -> カスタムロゴを選択することで、"財布の作成 "ページに表示されるショップイメージを変更することができます。

### 管理者ユーザー

環境変数：LNBITS_ADMIN_USERS`、カンマ区切りのユーザーIDリスト。管理者ユーザは管理画面の設定を変更することができます - ただし、資金源の設定は例外です。また、`LNBITS_ADMIN_EXTENSIONS`で指定されたすべての拡張機能にアクセスすることができます。

### 許可されたユーザー

環境変数：LNBITS_ALLOWED_USERS`、カンマ区切りのユーザーIDリスト。これらのユーザを定義することで、LNbitsは一般ユーザから利用できなくなります。定義されたユーザと管理者のみがLNbitsフロントエンドにアクセスできます。

#### LNbitsの更新

LNbitsローカルインスタンスの通常のアップデートは、以下のCLIコマンドをコピーペーストするだけです：

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

RaspiblitzまたはMyNodeを実行している場合は、さらに

```
sudo systemctl restart lnbits
```

これはLNbitsをサービスとして動かしているからだ。

Umbrel/Citadelの場合、コマンドは次のようになる。

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### SQLiteからPostgreSQLへの移行

LNbitsをSQLiteデータベース上にインストールし、運用している場合、LNbitsを大規模に運用するのであれば、postgresに移行することを強くお勧めします。

簡単に移行できるスクリプトが含まれています。Postgresが既にインストールされており、ユーザのパスワードが設定されている必要があります（上記のPostgresインストールガイドを参照してください）。さらに、LNbitsインスタンスをpostgres上で一度実行し、データベーススキーマを実装しておく必要があります：

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

うまくいけば、すべてが動作し、移行されます。もう一度LNbitsを起動して、すべてが正しく動作しているか確認してください。

#### データベースのバックアップとリストア

バックアップ＆リストアプロセスに関する非常に詳細なガイド](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore)を参照してください。

#### ノードからLNbitsウォレットへの資金注入がうまくいかない

LNbitsのファンディング・ソースと同じノードから衛星を送信したい場合は、lnd.confファイルを編集する必要があります。

含まれるパラメータは以下の通りである：allow-circular-route=1`である。

lnd.conf の Application options セクションでそうしてください。そうしないと、バンドルノードによっては LND の起動に失敗することがあります。

注意: LNbits口座への資金追加は、新しいadminUI拡張機能の "TopUp "オプションを使用することをお勧めします。

#### エラー 426

エラーが出ました："lnurlは、一般的にアクセス可能なhttpsドメインまたはtorで配信する必要があります。426アップグレードが必要です。

このエラーは通常、ngnixトンネルの背後にあるLNbitsがLNURLアドレスを正しく転送していないために発生します。LNbitsを停止し、.envファイルを編集して次の行を追加してください：

forwarded_allow_ips=*`。

また、ngnixのセットアップを使用している場合は、ngnixの設定にこれらのヘッダーがあることを確認してください：

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### ネットワークエラー

QRをスキャンすると、「httpsエラー」や「ネットワークエラー」などが発生する</summary>。

悪い知らせですが、これはルーティングエラーで、多くの原因が考えられます。まず[Lightning Decoder](https://lightningdecoder.com/)でQRのLNURLをチェックしてみてください。可能性の高い問題とその解決策をいくつか試してみましょう。

LNbitsはTor経由でのみ動作しています。lnbits.yourdomain.comのようなパブリックドメインでは開けません。


- この設定を維持したい場合は、.onion URIを使用してLNbitsウォレットを開き、再度作成します。こうすることで、.onion URIからtor経由でのみアクセスできるQRが生成されます。.localURIからQRを生成しないでください。インターネット経由ではアクセスできません。
- QRのスキャンに使用したLNウォレットアプリを開き、今度はtorを使用する（ウォレットアプリの設定を参照）。アプリがtorを提供していない場合は、代わりにOrbot（Android）を使用することができます。clearnet/https用のLNbitsを開く方法の詳細については、インストールセクションをご覧ください。

#### 他人が私のLNbitsでウォレットを生成するのを防ぐ

クリアネットでLNbitsを運用すると、基本的に誰もがその上でウォレットを生成することができます。あなたのノードの資金はこれらのウォレットに束縛されるので、それを防ぎたいと思うかもしれません。そのためには2つの方法があります：

.env`ファイル([envの例はこちら](https://github.com/lnbits/lnbits/blob/main/.env.example))で許可するユーザーと拡張子を設定する。これは、.envファイルで `adminUI=FALSE` という設定を使用した場合のみ機能します。そうでない場合は、Manage Server セクション -> Users -> Allowed Users で設定する必要があります。そうでなければ、サーバーの管理セクション -> ユーザー -> 許可されたユーザーでこれを行う必要があります。

#### 請求書の有効期限をカスタマイズする

カスタム期限付き請求書を作成できるようになりました。バックエンドと互換性があります：LndRestWallet、LndWallet、CoreLightningWallet、EclairWallet、LnbitsWallet、SparkWallet！

.envファイルで`LIGHTNING_INVOICE_EXPIRY`を設定するか、AdminUIを使用してすべての請求書のデフォルト値を変更することができます。また、/api/v1/paymentsエンドポイントに新しいフィールドが追加され、JSONデータで有効期限を設定できるようになりました。

## ウォレット-URL削除

### デモサーバーlegend.lnbitsのウォレット

自分のウォレット用のWallet-URL、Export2phone-QR、LNDhubのコピーは常に安全な場所に保存してください。LNbitsでは紛失時の復旧はできません。

### 自分の資金源／ノードの財布

自分のウォレット用のwallet-URL、Export2phone-QR、LNDhubのコピーは常に安全な場所に保存してください。全てのLNbitsユーザーとwallet-IDは、LNbitsユーザーマネージャ拡張機能またはsqliteデータベースで見つけることができます。LNbits データベースを編集したり読んだりするには、LNbits /data フォルダに行き、sqlite.db というファイルを探します。エクセルや[SQLite browser](https://sqlitebrowser.org/)のような専用のSQLエディタで開いて編集できます。

また、cli経由でウォレットをダンプし、データベース内のすべてのウォレットを見ることができます。

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

出力は次のようになる。

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

そして、これらの値を次のようなurlに入れたい。

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

ここで、f8a43fc363ea428db5c53b3559935f1fを名前の前の値（この例ではf8a43fc363ea428db5c53b3559935f1f）に置き換え、1280ff5910a9c485a782a2376f338b6cがあなたのユーザーで、名前の後に表示される値になるはずです。sqlite3を終了するには

```
.quit
```

#### LNURLをライトニングアドレスにする。

fiatjafの[encoder](https://lnurl-codec.netlify.app/)か、[this one](https://lightningdecoder.com/)をお試しください。LNURLpの支払いやチェックには、[LNurlpay](https://wwww.lnurlpay.com/)を使うこともできます。HTTP ではなく HTTPS である必要があります。

#### 私のLNURLp QRに支払いをする際に人々が見るコメントを設定する

LNURL-pを作成する際、デフォルトではコメント欄は埋められません。つまり、支払いにコメントを添付することはできません。

コメントを許可するには、ボックスの文字数を1～250の間で追加します。そこに数字を入れると、支払いプロセスでコメント欄が表示されます。また、すでに作成されているLNURL-pを編集して、その数字を追加することもできます。

![lnbits comments](assets/lnbits-comments.webp)

#### オンチェーンBTCをLNbitsに入金する

オンチェーンBTCからLN BTC（またはLNbits）への交換には2つの方法がある。

##### 外部のスワップサービス経由。

あなたのLNbにアクセスできない他のユーザーは、[Boltz](https://boltz.exchange/)、[FixedFloat](https://fixedfloat.com/)、[DiamondHands](https://swap.diamondhands.technology/)、[ZigZag](https://zigzag.io/)のようなスワップサービスを利用できます。これは、LNbitsインスタンスからLNURL/LNインボイスのみを提供する場合に便利ですが、支払者はオンチェーンサットしか持っていないため、まず支払者側でそれらのサットをスワップする必要があります。手順は簡単です。ユーザーはスワップサービスにオンチェーンBTCを送り、スワップの宛先としてLNbitsのLNURL/LNインボイスを提供します。

##### OnchainとBoltzのLNbitsエクステンションを使用。

これは別個のウォレットであり、LNbitsによって「あなたのウォレット」としてLN資金源で表現されるLN btcのものではないことに留意してください。このオンチェーンウォレットは、LNbitsのBoltzまたはDeezyエクステンションを使用することで、LN btcを（ハードウェアウォレットなどに）スワップするためにも使用できます。LNbitsとリンクしているウェブショップをLN決済のために運営している場合、定期的にLNからonchainにすべてのsatsを排出することは非常に便利です。そうすることで、LNチャンネルに空きができ、新しい新鮮なサットを受け取ることができるようになります。

ビットコインのハードウェアウォレットを持っていない人のための手続き：


- ElectrumまたはSparrowウォレットを使って新しいオンチェーンウォレットを作成し、バックアップシードを安全な場所に保存します。
- 財布の情報に行き、xpubをコピーする。
- LNbits - Onchain extensionにアクセスし、そのxpubを使って新しいウォッチ専用ウォレットを作成する。
- LNbits - Tipjar extensionにアクセスし、新しいTipjarを作成します。LNウォレットの他にonchainオプションも選択してください。
- オプション - LNbits - SatsPay extensionにアクセスし、onchain btcの新しいチャージを作成します。onchainとLNのどちらか、または両方を選択できます。その後、共有可能な請求書が作成されます。
- オプション - LNbitsをWordpress + Woocommerceページにリンクして使用する場合、時計専用ウォレットをLN btcショップウォレットに作成/リンクすると、顧客は同じ画面で両方の支払いオプションを利用できます。

LNbitsで支払いを受けると、取引ログには再開された取引のみが表示されます。

![lnbits payment details](assets/lnbits-payment-details.webp)

お取引の概要では、小さな緑色の矢印が受信した資金、赤い矢印が送信された資金を示します。

これらの矢印をクリックすると、詳細ポップアップが表示され、添付されたメッセージや送信者名が表示されます。

LNbits では、支払い時に表示される名前を設定することは現在できません。これは、送信者のLNウォレットが[OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents)のような[LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc)をサポートしている場合にのみ可能です。

LNbitsの取引詳細（矢印をクリック）に偽名が表示されます。この場合、任意の名前を指定することができますが、実際の送金者の名前とは異なる場合があります。

![lnbits namedesc](assets/lnbits-namedesc.webp)

ウォレットアプリでLNbitsアカウントをインポートするには、使用したいアカウント/ウォレットでLNbitsを開き、"拡張機能の管理 "に進み、LNDHUB拡張機能を有効にします。LNDHUB拡張機能を開き、使用したいウォレットを選択し、そのウォレットのセキュリティレベルに応じて "admin "または "invoice only "のQRをスキャンします。

Zeus](https://zeusln.app/)または[Bluewallet](https://bluewallet.io/)をlndhubアカウントのウォレットアプリとして使用することができます。

その際、LNネットワークURIを自分のノードのものに設定することをお勧めします。LNbitsインスタンスがTorのみの場合、Torを有効にしてこれらのアプリを使用する必要があります。またこの場合、Tor .onionアドレスを通してLNbitsのページを開く必要があります。

On-chain拡張でypubを使用する際に "unsupported hash type "というエラーが発生する場合、LNbitsインスタンスがpython 3.10を使用しているか確認してください。[この問題](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python)の影響を受けている可能性があります。stackoverflowの回答にあるようにopenssl.cnfを編集し、LNbitsを再起動してください。

## LNbitsでツーリング＆ビルド

LNbitsには、あらゆる種類の[オープンAPI](https://legend.lnbits.com/docs)とツールがあり、膨大な数のユースケースのために、さまざまなデバイスをプログラムし、接続することができる。

初めて作る場合は、LNbitsをベースにしたガジェットの作り方について、Ben Arcの[MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos)から始めましょう。

### 重要：


- LNbitsはLNURLプロトコルに基づいて動作し、https:// クリアネットリンク（自己署名証明書不可）またはhttp:// v2/v3 オニオンリンクの2つの形式でリクエストが有効です。LNURLp/wのQRコードやNFCカードのようなLNbitsサービスを提供するためには、LNbitsをclearnet（https）にオープンする必要があります。
- esp32への電源供給にはDATAケーブルのみを使用してください。すべてのケーブルがespへの電源供給に加えてデータもサポートしているわけではありません。 espに付属のケーブルが電源のみのものであれば、それは初めてのことではありません。
- 他のデバイスを接続したままUSB-Hubを使用しないようにしてください。これは、デバッグが困難な奇妙な効果（例えば、起動しない、停止しないなど）につながる可能性があります。
- MacOSでespプロジェクトを実現するには、UARTブリッジドライバが必要です。MacやLinuxシステムでドライバに問題がある場合は、こちらで見つけることができます。Windowsで接続に問題がある場合は、古いバージョン11.1.0をダウンロードしてください！また、接続を確認するためのシリアルターミナルもこちらで見つけることができます。
- Platform.ioを使う方がはるかに快適だが（依存関係が自動的にインストールされるなど）、初めてビルドする人にはArduinoを使うことをお勧めする。
- TT-GoディスプレイS3：スクリーン保護フィルムのタブの色で、どのコントローラ（ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...）で作られたかがわかります。自分でプログラムを組んでいて、画面がグラフィックを正しく表示しない場合（例えば、色がおかしい、画像がミラーリングされている、端のピクセルが浮いているなど）にデバッグできるように、これを保存しておいてください。このようなことが必要になった場合は、さまざまなディスプレイ用に調整するための壮大なガイドがあります。
- LNURLl239xxではなく、常に小文字のlnurl239xxを使用してください。
- lightning:lnurl1234xyzを追加すると、スキャン時にこの請求書のためにユーザーのウォレットを開くよう要求するQRが作成されます（iOSでは最後にインストールしたlightningアプリ、Androidでは設定）。
- ウェブ経由でesp32をフラッシュする場合は、これらのブラウザ（TL:DR Chrome、Edge、Opera）でしか動作しません。
- espのPIN-OUTリファレンスにご注意ください。
- FOSSoftwareやFOSGuidesを使用する際は、必ず作者をリンクしてください。誰もが自分の赤ちゃんが成長するのを見るのが大好きで、それはまた、見ていてとても素晴らしい構築の連鎖を引き起こします :)

プロジェクトで助けが必要な場合は、[Makerbits Telegram Group](https://t.me/makerbits)に来てください！

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

LNbitsで構築できるプロジェクトカテゴリーをいくつかご紹介します：


- [ノストル署名装置](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [アーケード・マシン](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [ガーティ](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [ノストル・ザップ・ランプ](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [ライトニング・ピギー](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [ハードウェア・ウォレット](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [ビットコイン・スイッチ](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [自動販売機](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [ボルティ](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [ナードマイナー](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [ビットコイン・ティッカー](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [ローラとメッシュ・ネットワーキング](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [ヘルパー＆リソース](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Powered by LNbits」プロジェクトのその他の例はこちら](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits)。
- [LNbitsの使用例](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)