---
name: Joinstr
description: 主権Bitcoinの機密保持のためのNostrネットワークを介した分散型CoinJoins
---

![cover](assets/cover.webp)



Bitcoinブロックチェーンの透明性により、取引履歴を追跡することが可能である。CoinJoinsは、複数の同時取引を混在させることでこうしたつながりを断ち切り、現金に匹敵するレベルの機密性を回復する。



しかし、従来のソリューションでは、単一障害点となる中央のコーディネーターに依存していた。ワサビとサムライは、規制当局の圧力により2024年に事業を停止した。



**Joinstr**は、分散型Nostrネットワークを調整に使用することで、この弱点を解消している。このオープンソースのアプリケーションは、中央当局が検閲、監視、サービスを中断することができない、真に主権的なCoinJoinsを可能にする。



## Joinstrとは？



Joinstrは、調整インフラとしてNostrプロトコルを活用することで、CoinJoinsのアプローチに革命を起こすオープンソースツールです。専用サーバーを必要とする集中型ソリューションとは異なり、JoinstrはNostrリレーの分散型ネットワークに依存し、参加者がピア間で直接調整することを可能にします。



**分散型アーキテクチャ** ：Nostrネットワークが中央コーディネーターの代わりとなる。参加者はNostrリレーを通じて暗号化されたアナウンスを投稿することで、「プール」を作成したり参加したりする。この情報(金額、参加者、アドレス)はリレーには理解できないままであり、中央組織がCoinJoinsを監視、検閲、フィルタリングできないことを保証します。



**SIGHASH_ALL|ANYONECANPAYメカニズム**：JoinstrはこのBitcoin署名フラグを悪用し、各参加者がすべての出力を検証しながら、自分の入力のみに署名することを可能にする。各ユーザーは自分のPSBTをローカルに生成し、それをNostr経由で配布する。各ユーザーは自分のPSBTをローカルで生成し、それに署名し、Nostr経由で配布する。あなたのビットコインは、最終的な署名まであなたの独占的な管理下に置かれます。



**理念**：JoinstrはBitcoinのサイファーパンクの理念に従い、3つのゴールを目指しています： **検閲への抵抗**（いかなる権力もサービスを止めることはできない）、**完全な非拘束性**（秘密鍵は保持される）、**平等な扱い**（いかなるUTXOも差別されることはない）。



### 主な特徴



**フレキシブル・プール**：固定額面とは異なり、どのユーザーも希望額と目標参加者数でプールを作成することができ、人為的な分割をすることなくUTXOの使用を最適化することができます。



**透明な料金**：調整費なし。Bitcoinの取引手数料のみ参加者間で均等に負担（一人当たり数千サトシ）。



**エフェメラル**：ユーザーデータは保持されない。情報は暗号化されたエフェメラルなNostrメッセージでやり取りされ、取引後はすぐに忘れ去られます。



### 利用可能なプラットフォーム



このチュートリアルは**Androidアプリケーション**に焦点を当てています。Electrumプラグインも存在しますが、互換性の問題があり不安定です。ウェブインターフェースは現在開発中です。



## Bitcoin コア構成



Joinstr AndroidはRPC経由でBitcoinノードに接続する必要があります。まず、携帯電話からの接続を受け付けるようにコンピュータ上でBitcoin Coreを設定する必要があります。



**注**：Bitcoin Coreの完全な設定についての詳細は、専用のチュートリアルをご覧ください：



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### ネットワーク要件



#### ローカルIPアドレスを見つける



Android携帯がローカルネットワーク上のBitcoinノードに到達できる必要があります。コンピューターのIPアドレスを検索します：



**macOSの場合** ：



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



シンプルな代替案だ：



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Linuxの場合** ：



```bash
hostname -I | awk '{print $1}'
```



**Windowsの場合** ：



```cmd
ipconfig
```



IPv4アドレス（フォーマット `192.168.x.x`または`10.0.x.x`）を検索する。



### RPCの構成



#### bitcoin.confを編集する



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



bitcoin.conf`ファイルを探してください：




- Linux**：ビットコイン/bitcoin.conf
- macOS**：ライブラリ/アプリケーションサポート/Bitcoin/bitcoin.conf
- Windows**：`%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



お好きなテキストエディタでファイルを開き、この設定を追加してRPCサーバーを有効にしてください。



**スタート時の推奨設定（ブックマーク）** ：



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**mainnet**構成（本番用） ：



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**重要** ：




- アプリケーションはまだ開発中（ベータ版）であり、バグが存在する可能性があります。Signetでは、実際の資金をリスクにさらすことなく、無料でテストすることができます。
- 192.168.1.0/24`をあなたのネットワークのサブネットに置き換えてください（例えば、あなたのIPが`192.168.68.57`であれば、`192.168.68.0/24`を使用してください）。



**セキュリティ**：強力なパスワードを生成する：



```bash
openssl rand -base64 32
```



### 初期設定



#### 再起動して確認する



1.Bitcoinコアを完全にシャットダウンする


2.設定を適用するために再起動する




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Bitcoinコアが初めて起動すると、ブックマーク・ブロックチェーンをダウンロードして同期する。この操作はmainnetよりもはるかに高速です（わずか数分）。同期が完了するまでお待ちください。



![CRÉATION DE WALLET](assets/fr/04.webp)



同期したら、"Create a new wallet "をクリックして新しいポートフォリオを作成する。tuto_joinstr_signet`のような明示的な名前をつける。



![WALLET CRÉÉ](assets/fr/05.webp)



これであなたのwalletは作成され、テスト用にブックマークされたビットコインを受け取る準備ができました。



#### ブックマークされたビットコインを入手する（テスト）



ブックマークでJoinstrをテストするには、無料のテストビットコインを必要とする ：



![SIGNET FAUCET](assets/fr/06.webp)



のようなパブリック・ブックマークを使用する：




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Bitcoin Coreで、generateに新しい受信アドレス（「受信」タブ）を作成し、コピーして蛇口フォームに貼り付ける。必要であればキャプチャを解いてください。数秒以内に無料のブックマークビットコインを受け取ります。



## Androidアプリケーション



### インストール



![APPLICATION ANDROID](assets/fr/07.webp)



[gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)にアクセスして、最新のAPKバージョンをダウンロードしてください。Androidブラウザでファイルをダウンロードし、開いてインストールを開始する。必要に応じて、携帯電話のセキュリティ設定で不明なソースからのインストールを許可する必要があります。



### アプリケーション構成



![PERMISSIONS VPN](assets/fr/08.webp)



初回起動時、JoinstrアプリケーションはビルトインVPNを制御するためのパーミッションを要求します。両方の許可要求を受け入れる：OpenVPNコントロールとVPN接続。これらのパーミッションは、ネットワークプライバシーを保護するVPN統合に必要です。



![INTERFACE APPLICATION](assets/fr/09.webp)



Joinstrアプリケーションは3つのメインタブで構成されている：




- ホームホーム画面
- プール**：CoinJoinプールの作成と管理
- 設定**：アプリケーションの設定



![CONFIGURATION SETTINGS](assets/fr/13.webp)



設定」タブで設定を行う：



**1.Nostrリレー**：プール調整用Nostrリレーアドレス




- 例：`wss://relay.damus.io`。
- その他の推奨リレー： `wss://nos.lol`、`wss://relay.nostr.band`、`wss://nostr.fmt.wiz.biz`。
- ⚠️ **重要**：すべての参加者が同じプールを見たり参加したりするには、**同じNostrリレー**を使用する必要があります。異なるリレーを使用した場合、他のリレーで作成されたプールは表示されません。



**2.ノードURL**：BitcoinノードのIPアドレス（ポートなし）




- フォーマットhttp://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3.RPC ユーザ名** ：bitcoin.conf の `rpcuser=` で設定したユーザー名。




- 例: `satoshi



**4.RPC パスワード** ：bitcoin.conf の `rpcpassword=` で設定したパスワード。



**5.RPC ポート** ：ネットワークによりRPCポート




- Mainnet** ：`8332`
- ブックマーク**：`38332`



**6.Wallet**：混合するUTXOを含むBitcoin Coreポートフォリオを選択する。




- 例: `tuto_joinstr_signet`



**7.VPNゲートウェイ**：Riseup VPNサーバーを選択します。




- 例: `(Paris) vpn07-par.riseup.net`.
- その他あり：アムステルダム、シアトルなど
- ⚠️ **重要**：重要**: CoinJoin に参加するためには、同じプール内のすべての参加者が **同じ VPN ゲートウェイ** を使用する必要があります。ミキシングラウンドの間、ネットワーク分析が参加者を相関させるのを防ぐために、すべての参加者は同じ終了IPアドレスで表示されなければなりません。



Joinstrアプリケーションは、Riseup VPNを**ネイティブ**に統合し、参加者間の調整を簡素化します。



**重要** ：




- 携帯電話とコンピューターが同じローカルWiFiネットワーク上にあることを確認する。
- プールに参加すると、VPN接続が自動的に有効になります。
- すべてのパラメーターを設定したら、**"Save "**をクリックします。



## 実用



### プールの作成または参加



![CRÉATION POOL ANDROID](assets/fr/10.webp)



CoinJoinへの参加には2つの選択肢がある：



**オプション1：新しいプールを作る**。



プール」タブの「新規プールを作成」をクリックします。BTCの額面（例：0.002 BTC）と希望する参加者数を指定します（最小2人、匿名性を高めるには3～5人を推奨）。その後、アプリケーションは他のユーザーがあなたのプールに参加するのを待ちます。必要な人数に達すると、出力登録プロセスが自動的に開始され、ミックスするUTXOを選択して「登録」をクリックする必要があります。



**⏱️重要**：プールは**10分間**使用されないと失効します。必要な参加者数に達しない場合、プールは自動的に閉鎖されます。



**オプション2：既存のプールに参加する**。



他のプールを見る」タブで、他のユーザーが作成した利用可能なプールを閲覧します。自分の金額に対応するプールを選択し、そのプールに参加します。他の参加者と同じNostrリレーとVPNゲートウェイを設定していることを確認してください(設定のセクションを参照)。



**UTXO選択ルール**：あなたのUTXOはプールのデノミネーション（+500から+5000のsats余剰）よりわずかに高くなければならない。



**例0.002BTC（200,000sats）のプールには、200,500～205,000satsのUTXOを使用します。



![PROCESSUS COINJOIN](assets/fr/11.webp)



あなたの入力が登録されると、アプリケーションはすべての参加者が入力を登録するのを待ちます。すべての入力が登録されると、PSBTが作成され、あなたの鍵で自動的に署名され、他の参加者の署名と結合されます。最後に、完全なトランザクションが Bitcoin ネットワーク上でブロードキャストされる。ブロードキャストが完了すると、TXID（トランザクション識別子）を受け取ります。Androidでは、PSBTを手動で操作する必要はありません。



### on-chain検証



![TRANSACTION MEMPOOL](assets/fr/12.webp)



トランザクションがブロードキャストされると、TXID（トランザクション識別子）を受け取ります。これを[mempool.space](https://mempool.space)またはお好きなブラウザでご覧ください。ブックマークでテストするには、[mempool.space/signet](https://mempool.space/signet)を使ってください。



を観察することができる：





- Nエントリー**：参加者1名につき1エントリー（例では2エントリー）
- N個の同一出力**: デノミネーションの正確な金額（ここでは、それぞれ0.00199800 BTCの2つの出力）
- フローチャート**：mempool.spaceは、入力と出力の組み合わせを視覚的に表示する。
- 特徴** ：取引はSegWit、Taproot、RBFなどと識別できる。



主な出力はすべて同じ量であるため、どれが誰のものかを判断することは**不可能**である。これがCoinJoinの基本原則である「アウトプットの区別がつかないこと」である。



**トランザクション署名の例** ：[404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**ご注意ください：注意**：UTXO がプール額面より大きい場合、為替アウトプット（余剰）が発生します。これらの為替UTXOはトレーサビリティを維持し、匿名化されたアウトプットとは別に管理する必要があります。決してミックス・アウトプットと一緒にしないでください。



## CoinJoinの品質と匿名性パッケージ



CoinJoinの効率は、その**アノンセット**によって測定される。この数が多ければ多いほど、どの入力がどの出力に対応するかを判断するのが難しくなる。



Joinstrは現在、平均**2～5人の参加者**のプールを生成している。この数字は、Wasabi（参加者50～100人）やWhirlpool（参加者5～10人）のような従来の中央集権型コーディネーターより低いが、これが分散化の代償だ。



💡 **匿名性セットとその計算を詳しく理解する**には、フルコース: [匿名性セット](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431) をご覧ください。



### Joinstrと他のCoinJoinsの比較



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

その他の活性型CoinJoin溶液** ：




- 足軽**：Whirlpoolプロトコルをオープンソースで実装したもので、中央集権的なコーディネーターを持つが、分散配置が可能。2024年のWallet奪取後も活動を継続。
- JoinMarket**：メイカー "が流動性を提供し、"テイカー "が報酬を得るビジネスモデルに基づいている。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**基本的なトレードオフJoinstrとJoinMarketは中央コーディネーターを持たない唯一のソリューションである。JoinMarketは金銭的インセンティブを持つP2Pビジネスモデルを使用し、JoinstrはコストフリーのコーディネーションにNostrを使用する。Joinstrは、シンプルさ（メーカー／テイカー管理なし）と調整手数料が全くないことを優先し、即時の大規模匿名性を犠牲にしている。



**実際の推奨事項**：実践的な推奨事項**：プールが小さいことを補うために、CoinJoinのラウンドを異なる参加者で数回連続して行う。ラウンドの間隔を空け、各ラウンドの間にノストルリレーを変更することで、秘匿性を最大限に高めることができる。



このトピックの詳細については、ビットコインのプライバシーに関する完全なコースを参照してください：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 利点と限界



### ハイライト



**強化されたプライバシー**：Nostr通信の暗号化、参加者間の共有VPN、Torの推奨利用を組み合わせることで、迂回が困難な多層的な保護を実現します。



**透明で最小限のコスト**：調整費用はなく、mining の費用のみが参加者間で公平に分担される。どの事業者からもパーセンテージは徴収されない。



### 考慮すべき制約





- 流動性の変動**：小規模プール、参加者が集まるのを待つことができる
- プロジェクト進行中**：アプリケーションはベータ版です。まずはブックマークで少量テスト
- シビル攻撃**：1人の対戦相手が複数のプール参加者をコントロールする可能性



## ベストプラクティス



**UTXOの分離**：混合されたUTXOと混合されていないUTXOを決して一緒にしないでください。匿名化された出力には別のポートフォリオを使用してください。



**複数回のラウンドが不可欠**：異なる参加者と最低3ラウンド行う。パターンを避けるため、量と時間を変える。ラウンドの間隔を数時間あける。



**ネットワーク保護**：内蔵VPNに加えてTorを計画的に使用する。重要なセッションごとにエフェメラルなNostrキーを生成する。



**慎重な進行**：ブックマークは少量から始める。



## 結論



Joinstrは真に分散型のBitcoinプライバシー・ソリューションである。コーディネーションにNostrを使用することで、ユーザー主権を維持しながら中央コーディネータへの依存を排除している。



**検閲への耐性を重視し、少ないプールを補うためにCoinJoinを数ラウンド行う覚悟のあるユーザー向け。



財政的な監視が強化される中、プライバシーを保護する分散型ツールは不可欠になっている。



## リソース



### 公式文書




- [ジョインスト公式サイト](https://joinstr.xyz)
- [ユーザー・ドキュメント](https://docs.joinstr.xyz/users/using-joinstr)
- [技術資料](https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLabソースコード](https://gitlab.com/invincible-privacy/joinstr)
- [Androidアプリケーション](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### チュートリアル




- [Electrum プラグイン チュートリアル](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - 無修正技術による完全ガイド



### コミュニティとサポート




- [Telegram Joinstr Group](https://t.me/joinstr) - コミュニティサポートとブックマークコーナー
- [DelvingBitcoinに関する技術的議論](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### 追加ツール




- [ブックマーク Faucet](https://signetfaucet.com) - 無料テスト用ビットコイン
- [アルト・シグネット Faucet](https://alt.signetfaucet.com) - Faucet 代替品
- [Mempool.space](https://mempool.space) - Block explorer with プライバシー分析
