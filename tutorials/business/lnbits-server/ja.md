---
name: LNbitsサーバー
description: PhoenixdまたはUmbrelを使用したUbuntu VPSへのLNbitsサーバーのインストールと設定
---

![cover](assets/cover.webp)



LNbitsは、あらゆるLightningバックエンド（LND、Core Lightning、Phoenixd）を完全なサービスプラットフォームに変換するオープンソースのWebインターフェースです。このセルフホストソリューションにより、資金を完全に管理しながら、複数のLightningポートフォリオを分離して管理したり、販売ポイントを展開したり、寄付システムや課金サービスを作成したりすることができます。



このチュートリアルでは、2つのインストール方法について説明します： **VPS Ubuntu with Phoenixd** (完全なBitcoinノードを使用しない軽量ソリューション) と **Umbrel** (既存のLNDノードとの統合) です。Plan ₿ Academyの一般的なLNbitsチュートリアルとは異なり、概念と拡張機能をカバーするこのガイドは、ステップバイステップの技術的なインストール手順に焦点を当てています。



## LNbitsとは？



LNbitsは、既存のバックエンド（LND、Core Lightning、Phoenixd）に接続するPython（FastAPI）で開発されたLightning会計システムです。従来のLightningノードとは異なり、LNbitsは独自のAPIキーを持つ複数の分離されたポートフォリオを管理するためのアクセス可能なインターフェースを提供します。家族、従業員、プロジェクトのためにサブアカウントを作成することができます。



分離されたアーキテクチャは、SQLite(デフォルト)またはPostgreSQL(プロダクション)に情報を保存し、資金はLightningバックエンドで管理されます。この分離により、ユーザーデータを失うことなく、PhoenixdからLNDへ移行することができます。



## 主な特徴



LNbitsは多彩な**拡張システム**を提供しています：TPoS（販売時点情報管理）、Paywall（コンテンツ収益化）、Event（チケット販売）、LndHub（BlueWallet用サーバー）、Bolt Cards（NFC決済）、Split Payments（自動配信）、User Manager（認証付きユーザー管理）。



ダッシュボード**には、リアルタイムの残高、取引履歴、請求ツールが表示されます。各walletはAPIキーを含むユニークなURLを持っており、従来のログインなしでアクセスできます。3段階のAPIキーシステム**（admin、invoice、read-only）は、安全な統合のためのきめ細かな権限制御を提供します。



LNbitsは**LNURL**（LNURL-pay、LNURL-withdraw、LNURL-auth）をネイティブに実装し、**Lightning Address**をサポートしているため、最新のLightningウォレットとの互換性が保証され、プロフェッショナルサービスの展開が容易になります。



## 対応プラットフォーム



**Ubuntu VPS**：フルBitcoinノードなしの軽量ソリューション。前提条件：1 vCPU、1-2 GB RAM、Ubuntu 22.04 LTS、Python 3.10+、Git、UV。公開にはHTTPS + ドメイン名が必要です（LNURLサービス）。



**Umbrel**：App Store から簡単にインストールできます。前提条件：同期された LND とオープンチャンネルを持つ機能的な Umbrel ノード。自動設定。



以下はUmbrelとUmbrel LNDのチュートリアルへのリンクです：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## PhoenixdによるUbuntu VPSへのインストール



### ステップ1：VPSサーバーの保護



**インストールの前に**、Ubuntu VPSサーバーをルールに従って保護する必要があります。このステップは、お客様のインフラとライトニング資金を保護するために**重要**です。



ここに、開始するのに役立つ詳細なガイドがあります： **[Ubuntu サーバー初期設定 - ステップバイステップガイド](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** by Daniel P. Costas.



このガイドでは、ユーザー設定、セキュアな SSH、ファイアウォール (UFW)、fail2ban、自動アップデート、および優れたシステム・セキュリティの実践について説明します。



### ステップ2：Phoenixdのインストール



サーバーの安全が確保されたら、Phoenixd のインストールと設定を行う必要があります。Plan ₿ Academy では、インストール、seed の生成、systemd サービスの設定をカバーする包括的な専用チュートリアルを提供しています：



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Phoenixdが起動したら（`./phoenix-cli getinfo`で確認してください）、`~/.phoenix/phoenix.conf`の**HTTPパスワード**をメモしておいてください。



### LNビット展開



UVをインストールし、LNbitsをクローンする：


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Phoenixd バックエンドを設定します：


```bash
cp .env.example .env && nano .env
```



.env`に追加する：


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



uv run lnbits --host 0.0.0.0 --port 5000`でテストし、`Wants=phoenixd.service`でsystemdサービスを作成する。



## 初期設定と初回使用



### スーパーユーザーのアクティベーション



.env`で管理者インターフェースを有効にする：


```
LNBITS_ADMIN_UI=true
```



LNbitsを再起動し（`sudo systemctl restart lnbits`）、SuperUser IDを取得する：


```bash
cat ~/lnbits/data/.super_user
```



管理画面は`http://<IP-VPS>:5000/wallet?usr=<SuperUserID>`にアクセスしてください。Server "メニューで資金源、拡張機能、ユーザーアカウントを設定できます。



### 安全なアカウント作成



**公開する場合は重要です：インターネットからアクセス可能なパブリックドメイン名でLNbitsインスタンスを公開する場合は、ユーザーアカウントを自由に作成できないようにすることが**重要**です。



SuperUserの管理インターフェイスから "設定 "に進み、"ユーザー管理 "セクションに進みます。そこに "新規ユーザーの作成を許可する "オプションがあります。



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**ドメイン名**での公募展のため：




- 新規ユーザーの作成を許可する」オプションを無効にする必要があります。
- この保護がなければ、インターネット上の誰もがあなたのインスタンスにアカウントを作成することができます。
- 攻撃者が知らないうちにアカウントを作成し、Lightningノードの流動性を使用する可能性がある。
- SuperUserインターフェイスから手動でユーザーアカウントを作成する必要があります。



**現地使用のみ** ：




- インスタンスがローカルにしかアクセスできない場合は、このオプションはそれほど重要ではありません (http://localhost:5000)
- しかし、このオプションを無効にすることは、一般的な安全対策として有効です。



一旦設定されると、SuperUser管理者のみが "Users "インターフェイスを通じて新しいユーザーアカウントを作成することができます。このアプローチは、誰がLightningインフラストラクチャにアクセスし、資金を使用できるかを完全にコントロールすることを保証します。



### 最初のチャンネルを開く



Phoenixdは自動流動性によって自動的にチャネルを管理する。LNbitsから～30,000satsのLightningインボイスを作成し、別のwalletから支払う。Phoenixdは自動的にACINQにチャネルを開設する。開設手数料（～2～3万sats）が差し引かれ、残金（～7～1万sats）はon-chainの確認後に表示される。



./phoenix-cli getinfo`でステータスをチェックする。それから、チャネルのオープンを制御するために自動流動性を無効にする (`phoenix.conf` の `auto-liquidity=off`) ことを検討する。



### 一般公開とHTTPS



**重要**：一般公開にはHTTPSが必須です（API鍵のセキュリティ＋LNURLの互換性）。ローカルでのみ使用する場合は、このステップをスキップしてください。



**Caddy (推奨)**: 自動SSL。sudo apt install -y caddy`, edit `/etc/caddy/Caddyfile` ：


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


再起動します：sudo systemctl restart caddy`.



**Nginx** ：より多くのコントロール。nginx certbot python3-certbot-nginx` をインストールし、`/etc/nginx/sites-available/lnbits` を作成する：


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


有効化: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`.



.env`に追加： `FORWARDED_ALLOW_IPS=*`



## アンブレルの設置



### App Storeからのデプロイメント



Umbrel App Storeで "LNbits "を検索し、"Install "をクリックしてください。



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel は必要な依存関係を自動的にチェックします。LNbits を動作させるには Lightning Node (LND) が必要です。Lightning ノードが既に動作している場合は、"Install LNbits" をクリックして確認してください。



![Dépendances LNbits](assets/fr/02.webp)



UmbrelはDockerイメージをダウンロードし、LNDとの接続を自動的に設定し、コンテナを起動する（2-5分）。インストールは完全にバックグラウンドで行われます。



### スーパーユーザーの初期設定



初回起動時、LNbits は SuperUser 管理者アカウントの作成を促します。管理インターフェイスへのアクセスを保護するために、ユーザ名と安全なパスワードを入力してください。



![Configuration SuperUser](assets/fr/03.webp)



**重要**：このSuperUserアカウントはLNbitsインスタンスの全権限を持ちます。パスワードは厳重に管理してください。



アカウントを作成すると、自動的にメインの管理インターフェイスに移動します。UmbrelはすでにLNDを資金源として設定しており、Lightningの支払いはすべて既存のチャネルを通じて行われます。



### 管理者インターフェースへのアクセス



左側のメニューで「設定」をクリックし、完全な管理パネルにアクセスします。



![Interface Settings](assets/fr/04.webp)



Wallets Management "セクションには、設定に関する主要な情報が表示されます：




- 資金源** ：LndBtcRestWallet (LND Umbrelノードへの直接接続)
- ノード残高** ：Lightningチャネルで利用可能な総流動性
- LNbitsの残高**：LNbitsシステムに割り当てられた資金（当初は0sats）



作成したすべてのLNbitsウォレットについて、Umbrelノードの流動性を直接利用できるようになりました。追加の設定は必要ありません。



### ユーザー管理



LNbitsの最も強力な機能の1つは、それぞれがパスワード認証と独立したウォレットを持つ複数の独立したユーザーを作成できることです。このアーキテクチャにより、ビジネス、家族、従業員、プロジェクトなど様々な用途のために完全に分離されたサブアカウントを提供しながら、Umbrelノードの流動性を活用することが可能になります。



サイドメニューの "Users "をクリックし、ユーザー管理にアクセスする。CREATE ACCOUNT "をクリックして新規ユーザーを追加します。



![Gestion des utilisateurs](assets/fr/05.webp)



ユーザー作成フォームに入力します：




- ユーザー名**：ログインユーザー名 (例: "satoshi")
- パスワードを設定する**：認証パスワードを設定するには、このオプションを有効にします。
- Password**および**Password repeat**：このユーザのパスワードを設定する



![Création utilisateur satoshi](assets/fr/06.webp)



オプションのフィールド（Nostr Public Key、Email、First Name、Last Name）は、最小限の設定のために空白のままにしておくことができます。CREATE ACCOUNT "をクリックしてください。



![Confirmation utilisateur créé](assets/fr/07.webp)



新しいユーザは、一意の識別子とユーザ名でユーザ一覧に表示されます。



![Liste des utilisateurs](assets/fr/08.webp)



**重要なポイント**：各ユーザーは自分のパスワードで完全に独立してログオンできます。SuperUser 管理者は、管理インターフェイスを介した完全なコントロールを保持します。



### ユーザーwallet管理



satoshi」ユーザーが作成されたので、彼にwalletライトニングを割り当てる必要があります。walletアイコン（2番目のアイコン）をクリックし、"CREATE NEW WALLET "をクリックしてください。



![Gestion des wallets](assets/fr/09.webp)



wallet の名前を入力するダイアログが表示されます。わかりやすい名前（例："Wallet Of Satoshi"）を入力し、表示通貨（CUC、USD、EURなど）を選択します。



![Création wallet](assets/fr/10.webp)



CREATE "をクリックしてください。LNbitsは、即座にこのユーザーのためのwallet Lightningを生成します。



![Confirmation wallet créé](assets/fr/11.webp)



デフォルトのwallet "LNbits wallet "と新しい "Wallet Of Satoshi "です。ユーザーエクスペリエンスを簡単にするために、削除アイコン（赤いゴミ箱）をクリックしてデフォルトのwalletを削除することができます。



![Wallet final unique](assets/fr/12.webp)



satoshi "ユーザーは現在、明確に識別された単一のwalletを持っています。各walletユーザーは、あなたの基礎となるLNDノードの流動性を使用しながら、完全に自律的に動作します。



**キーコンセプト**：これらのウォレットはすべて、あなたのUmbrelノードのグローバル流動性を共有します。LNbitsは、既存のLightningインフラ内で資金配分を管理するインテリジェントなアカウンティングレイヤーとして機能します。これがLNbitsのマルチwalletシステムのパワーです。



### ユーザーログイン



SuperUserアカウント（右上のアイコン）からログアウトし、LNbitsのログインページに戻ります。これで新しいユーザーの認証情報でログインできます。



![Connexion utilisateur satoshi](assets/fr/13.webp)



ユーザー名（"satoshi"）とパスワードを入力し、"LOGIN "をクリックします。ユーザーは、管理インターフェイスから完全に隔離された個人用walletに直接アクセスできるようになります。



### walletユーザーからのInterface



ログインすると、ユーザーはwalletライトニングの完全なインターフェイスにアクセスできる。



![Interface wallet utilisateur](assets/fr/14.webp)



インターフェイスの特徴




- 現在の残高**：satsと選択した通貨（この例ではCUC）で表示されます。
- 主な操作**：リクエストの貼り付け、請求書の作成、QRアイコン（クイックスキャン）
- 取引履歴** ：すべての支払いと受領の完全なリスト
- 右サイドパネル**：設定とアクセスオプション



### walletへのモバイルアクセス



右側のサイドパネルには、特に実用的な機能として、walletへのモバイルアクセスが用意されている。モバイル・アクセス」セクションを開くと、利用可能なオプションが表示されます。



![Mobile Access](assets/fr/15.webp)



LNbitsはこのwalletをスマートフォンで使用する方法をいくつか提供している：



**オプション1：対応モバイルアプリケーション




- App StoreまたはGoogle Playから**Zeus**または**BlueWallet**をダウンロードしてください。
- LNbitsの**LndHub**エクステンションをこのwallet用にアクティブにする。
- モバイルアプリでLndHubのQRコードをスキャンし、walletに接続します。



**オプション2：モバイルブラウザ経由の直接アクセス




- QRコードで電話へエクスポート」で表示されるQRコードには、認証機能を統合したwalletの完全なURLが含まれています。
- スマートフォンからこのQRコードをスキャンすると、モバイルブラウザで直接walletを開くことができます。
- ホーム画面にページを追加して素早くアクセス



**重要なセキュリティ**：この URL には wallet にフルアクセスするための API キーが含まれています。決して公開しないでください。このQRコードは、Bitcoinのプライベート・キーと同じように扱ってください - このQRコードをスキャンした人は、walletへのフル・アクセスが可能になります。



このモバイル機能は、あなたのLNbits Umbrelインスタンスを、あなたとあなたの友人のための本物のLightning walletサーバーに変えます。



### ユーザーアクセス共有



このマルチユーザー設定の主なユースケースは、**家族や親しいサークル**とウォレットを共有することです。専用のwallet（この例では "satoshi "など）を持つユーザーを作成したら、このログイン認証情報を家族の信頼できるメンバーと共有することができます。



**Umbrel**上のアクセスセキュリティ：Umbrel上のLNbitsインスタンスへのアクセスは、当然ながら保護されています：




- ローカルネットワーク** ：同じWiFi/イーサネット・ネットワークに接続されている家族のメンバーがインスタンスにアクセスできます。
- VPN 経由**：Umbrel サーバーに設定された Tailscale などの VPN を使用すると、許可されたユーザーは安全にリモートアクセスできます。



この二重の保護（ネットワークアクセス＋ユーザー認証）により、Umbrelの「新規ユーザーの作成を許可する」オプションはそれほど重要ではなくなります。ログインインターフェースにアクセスできるのは、既にネットワークまたはVPNにアクセスしている人だけです。



**典型的なシナリオ**：お父さん "アカウント、"お母さん "アカウント、"ビジネス "アカウントなどを作成します。各家族のメンバーは、Umbrelノードの共有流動性の恩恵を受けながら、独自の分離されたwallet Lightningを持っています。ユーザー名とパスワードを共有するだけで、ユーザーはローカルネットワーク上のどのデバイスからでも、Tailscale VPN経由でも接続できます。詳しくはTailscaleチュートリアルをご覧ください：



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### 利用可能なエクステンションを調べる



SuperUser インターフェースに戻り、左側のサイドパネルにある "Extensions" メニューにアクセスすると、LNbits の拡張機能エコシステムがすべて表示されます。



![Extensions disponibles](assets/fr/16.webp)



LNbitsは豊富なエクステンションカタログを提供し、インスタンスを真のLightningサービスプラットフォームへと変貌させます：





- ジュークボックス**：sats搭載ジュークボックスシステム（Spotify決済）
- サポートチケット**：有料サポートシステム(質問に答えるためのサツキを受け取る)
- TPoS**：小売業向けセキュアなモバイルPOS端末
- ユーザー・マネージャー**：高度なユーザーとwalletの管理（今使ったところです）
- イベント**：イベントチケットの販売と検証
- LNURLDevices**：POS管理、ATM、接続スイッチ
- SMTP**：ユーザーが電子メールを送信し、サッツを獲得できるようにする
- Boltcards**：ライトニング・タップ・ツー・ペイ決済用NFCカードのプログラミング
- NostrNip5**：ドメインにNIP5アドレスを作成する
- スプリットペイメント**：複数のウォレット間で支払いを自動分配



各エクステンションは、このインターフェイスからワンクリックで有効化できます。FREE "と表示されている拡張機能は無料ですが、"PAID "バージョンもあります。ビジネス、家族管理、Lightning Networkの機能の実験など、あなたのニーズに合ったものをカタログからお探しください。



## 利点と限界



**メリット**：財務主権（資金/鍵/データの完全管理）、アーキテクチャの柔軟性（ロスレスVPS→full node移行）、プロフェッショナルな拡張システム、直感的なインターフェース。



**制限事項** ：ソフトウェアがベータ版であること（量に注意）、セキュリティが管理者の責任下にあること、機密性の高い API キーを含む URL があること（HTTPS が必須）、複数ユーザーの管理は管理者の責任を意味する。



## ベストプラクティス



**バックアップ**：Phoenixd Seed/LND 認証情報、LNbits データベース、.env ファイル。毎日自動化し、本番サーバーから暗号化しておく。定期的なリストアのテスト。



**メンテナンス**：定期的にアップデートをチェックする（LNbits、Lightningバックエンド、オペレーティングシステム）。メジャーアップデートの前には必ずリリースノートを確認してください。





- Umbrel**で：App Store は自動的に新しいバージョンを通知します。拡張機能の管理] > [すべて更新] を使用して拡張機能を同期します。Umbrel の自動バックアップに SQLite データベースが含まれているか確認してください。
- VPS**の場合：cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`で手動でアップデート。システムログを監視する：sudo journalctl -u lnbits -f`.



## 結論



LNbitsセルフホスティングは、Lightning金融主権への具体的な道を提供します。VPS+Phoenixdは、既存のBitcoinノードと完全に統合された、高速サービスのための軽量ソリューションを提供します。スケーラブルなアーキテクチャは、シンプルなマルチユーザーwalletから洗練されたビジネスユースケースへの進化を可能にします。



シードをバックアップし、アクセスを保護し、小額から始める。これらの予防措置により、LNbitsは分散化と自律性を維持しながら、ライトニング・エコノミーのための強固なソリューションとなる。



## リソース



### 公式文書




- [LNbitsドキュメント](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [公式インストールガイド](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### コミュニティ・ガイド




- [Ubuntuサーバーの初期設定](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) by Daniel P. Costas (ステップバイステップのVPSセキュリティ)
- [Ubuntu VPSへのLNbits + Phoenixdインストール](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) by Daniel P. Costas (完全ガイド)
- [クリアネット上のLNbitsサーバー](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [VPS上のLNbits](https://github.com/TrezorHannes/vps-lnbits) by Hannes