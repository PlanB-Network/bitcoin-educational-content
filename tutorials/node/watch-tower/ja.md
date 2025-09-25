---
name: Lightning Watchtower
description: LightningノードのWatchtowerを理解し、使用する
---
![cover](assets/cover.webp)



## ウォッチタワーの仕組みは？



Lightning Networkエコシステムの重要な部分である_Watchtowers_は、ユーザーのライトニング・チャンネルに特別な保護レベルを提供します。その主な役割は、チャネルの状態を監視し、チャネルの一方が他方を騙そうとした場合に介入することです。



Watchtowerはどのようにしてチャネルが侵害されたかどうかを判断できるのか？Watchtower は顧客（チャネルの当事者の一人）から、侵害を正しく識別し、対処するために必要 な情報を受け取る。この情報には、直近のトランザクションの詳細、チャネルの現在のステータス、ペナルティ・トランザクションの作成に必要なElementsが含まれる。このデータをWatchtowerに送信する前に、顧客はデータを暗号化して機密性を保持することができる。そのため、Watchtowerがデータを受信しても、実際に違反が発生するまで解読することはできない。この暗号化メカニズムにより、顧客のプライバシーを保護し、Watchtowerが機密情報に不正アクセスすることを防ぐことができる。



このチュートリアルでは、**Watchtower**を使用する3つの方法を見ていきます：




- まず、LNDを経由する古典的な生の方法だ、
- その後、Satoshiのアイで再アプローチ、
- そして最後に、UmbrelでホストされているLightningノード上のWatchtowerの簡単な構成です。



## 1 - Watchtower または LND 経由のクライアントの設定



*このチュートリアルは[LND公式ドキュメント](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md)から引用しています。原文に変更が加えられている場合があります。



v0.7.0 以降、`LND` は `LND` の完全に統合されたサブシステムとして、プライベートな利他的 Watchtower の実行をサポートする。ウォッチタワーは、カスタマー・ノードがオフラインまたは侵害時に応答できない場合に、悪意のあるまたは偶発的な侵害シナリオに対する第二の防御線を提供し、チャネル資金に高度なセキュリティを提供する。



報酬型監視塔は、そのサービスの見返りとしてチャンネルの資金の分配を要求するのとは異なり、利他主義者型監視塔は、手数料を請求することなく、被害者の資金（On-Chainの手数料を差し引いた額）をすべて返還します。リワード・ウォッチタワーは後のバージョンで有効になります。



加えて、`LND`は他の利他的な監視塔から暗号化された侵害救済トランザクション（いわゆる「正義のトランザクショ ン」）を保存する「監視塔クライアント」として機能するように設定できるようになった。Watchtowerは固定サイズの暗号化されたブロブを保存し、違反者が取り消されたCommitmentの状態をブロードキャストした後にのみ、正義のトランザクションを復号して公開することができる。顧客↔Watchtowerの通信は暗号化され、エフェメラルなキー・ペアを使用して認証されるため、Watchtowerが長期的な認証情報によって顧客を追跡する能力は制限される。



このリリースでは、`LND` ユーザーのためにすでに重要なセキュリティーを提供している機能の限定されたセットを配備することにしたことに注意してください。他の多くのWatchtower関連の機能は完成間近か、あるいはかなり進んでいます。私たちはそれらをテストし、安全と判断され次第、配信し続けます。



HTLC出力の保存は、プロトコルが暗号化されたblob._に追加の署名データを含むように拡張できるため、将来のバージョンで展開される予定です。



### Watchtowerの設定



Watchtowerをセットアップするには、コマンドラインユーザーはオプションの `watchtowerrpc` サブサーバーをコンパイルする必要があります。公開されているバイナリには `watchtowerrpc` サブサーバーがデフォルトで含まれている。



Watchtowerをアクティブにするための最小コンフィギュレーションは`Watchtower.active=1`である。



Watchtower の設定情報は `lncli tower info` で取得できます：



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Watchtower の全設定オプションは `LND -h` で利用できる：



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### リスニング・インターフェース



デフォルトでは、Watchtower は `:9911` でリッスンします。これはすべての利用可能なインターフェースのポート `9911` に対応します。ユーザーは `--Watchtower.listen=` オプションでリスニングするインターフェースを定義することができる。設定は `lncli tower info` の `"listeners"` フィールドで確認できる。Watchtower に接続できない場合は、`<port>` が開いているか、プロキシがアクティブな Interface に正しく設定されているかを確認してください。



#### 外部IPアドレス



また、`Watchtower.externalip=`でWatchtowerの外部IP Address(es)を指定することができ、RPCまたは`lncli tower info`を介してWatchtowerの完全なURI（pubkey@host:port）が公開される：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



WatchtowerのURIは、以下のコマンドで接続して使用するように顧客に伝えることができる：



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Watchtowerの顧客がリモートでアクセスする必要がある場合は、：




- 9911番ポート（または`Watchtower.listen`で定義したポート）を開く。
- プロキシを使って、開いているポートからのトラフィックをWatchtowerのリスニングしているAddressにリダイレクトする。



#### Torの隠れたサービス



Watchtowers は Tor の隠しサービスをサポートしており、以下のオプションで起動時に自動的に generate を設定できる：



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



.onionのAddressは、`lncli tower info`クエリ中に`"uris"`フィールドに表示される：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



注：Watchtower の公開鍵は `LND` ノードの公開鍵とは異なる。Watchtowerの公開鍵は、`LND`ノードの公開鍵とは別個のものです。Watchtowerをインターネット全体に公開する覚悟がない限り、この公開鍵を公開しないことをお勧めします。



#### Watchtowerデータベースディレクトリ



Watchtowerデータベースは`Watchtower.towerdir=`オプションを使って移動することができる。Bitcoin/Mainnet/Watchtower.db`という接尾辞が、データベースを文字列で分離するために選択したパスに追加されることに注意してください。したがって、`Watchtower.towerdir=/path/to/towerdir` と設定すると、`/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db` にデータベースが作成されることになる。



例えばLinuxでは、Watchtowerのデフォルト・データベースは：


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Watchtowerクライアントの設定



Watchtowerクライアントを設定するには、2つのアイテムが必要です：





- --wtclient.active`オプションでWatchtowerクライアントをアクティブにする。



```shell
$  lnd --wtclient.active
```





- アクティブなWatchtowerのURI。



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



このようにして複数の監視塔を構成することができる。



#### 法律取引手数料



wtclient.sweep-fee-rate`オプションはsat/byteで指定できる。デフォルト値は10sat/byteであるが、ピーク料金時に高い優先度を達成するために、より高いレートを目指すことが可能である。sweep-fee-rate`を変更すると、daemon再起動後のすべての新規更新に適用される。



#### 監督



lncli wtclient`コマンドにより、ユーザーはWatchtowerクライアントと直接対話し、登録されているすべての監視塔の情報を取得または変更することができます。



例えば、`lncli wtclient tower`を使うと、上で追加したWatchtowerと現在ネゴシエートしているセッション数を知ることができ、`active_session_candidate`フィールドのおかげでバックアップに使われているかどうかを判断できる。



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Watchtowerセッションの情報を得るには、`--include_sessions`オプションを使う。



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Watchtower クライアントの設定オプションはすべて `lncli wtclient -h` で利用できる：



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Satoshiのアイを取り付ける



*このチュートリアルは、[Bitcoin夏のブログ](https://blog.summerofbitcoin.org/)の記事を一部抜粋したものです。原文に修正を加えています*。



Satoshiの目([Rust-TEOS](https://github.com/talaia-labs/Rust-teos))は、[Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)に準拠した非保管型Watchtowerライトニングである。主に2つのコンポーネントで構成されている：





- teos**: コマンドライン Interface (CLI) と Watchtower の基本的なサーバ機能を含んでいます。この_crate_がコンパイルされると、**teosd**と**teos-CLI**の2つのバイナリが生成されます。





- teos-common**：サーバーサイドとクライアントサイドの共有機能を含む（クライアントの作成に便利）。



Watchtower を正しく実行するには、**teosd** コマンドで Watchtower を起動する前に、**bitcoind** を実行する必要があります。この2つのコマンドを実行する前に、**Bitcoin.conf** ファイルを設定する必要があります。以下にその方法を示します：





- Bitcoin coreをソースからインストールするか、ダウンロードする。ダウンロード後、**Bitcoin.conf**ファイルをBitcoin coreのユーザーディレクトリに置きます。ファイルを配置する場所については、使用するオペレーティング・システムによって異なるため、こちらのリンクを参照してください。





- 場所を特定したら、以下のオプションを追加する：



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- サーバー**：RPCリクエスト用





- rpcuser**と**rpcpassword**：RPCクライアントをサーバーに認証する。





- regtest**: 必須ではないが、開発を計画している場合に役立つ。



rpcuser**と**rpcpassword**の値は、各自が選択する。これらは引用符を付けずに記述しなければならない。例えば



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



これで、**bitcoind**を実行するとノードが起動するはずだ。





- Watchtowerの部分については、まずソースから**teos**をインストールする必要がある。このリンクの指示に従ってください。





- システムに**teos**をインストールし、テストを実行したら、最後のステップ、teosユーザーディレクトリに**teos.toml**ファイルをセットアップします。このファイルは、ホームディレクトリの下の**.teos**（ドットに注意）という名前のフォルダに置く必要があります。例えば、Linuxでは**/home//.teos**です。場所が見つかったら、**teos.toml** ファイルを作成し、**bitcoind** での変更に合わせてこれらのオプションを設定します：



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



ここで、ユーザー名とパスワードは**引用符**で囲んで書かなければならないことに注意してください。前の例を使って ：



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



これが完了したら、Watchtowerを起動する準備ができているはずです。regtest**で実行しているため、Watchtowerが最初に接続したとき、Bitcoinテストネットワークでブロックが採掘されていない可能性があります（採掘されていた場合、何かが間違っています）。Watchtowerは**bitcoind**の直近100ブロックの内部キャッシュを構築するため、初回起動時に以下のようなエラーが発生する可能性があります：



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



regtest**を使用しているため、他のネットワーク（MainnetやTestnetなど）で見られる中央値10分の遅延を待つことなく、RPCコマンドを発行することでMinerブロックが可能です。Minerブロックの詳細については、**bitcoin-cli**のヘルプを参照してください。



![Image](assets/fr/01.webp)



以上、Watchtowerは無事終了しました。おめでとう。🎉




## 3 - Umbrel上のWatchtowerの設定



Umbrel では、Lightning ノードを保護するための Watchtower への接続は非常に簡単です。ノードにリモート接続した後、"**Lightning Node**"アプリケーションを開きます。



![Image](assets/fr/02.webp)



Interfaceの右上にある3つの小さな点をクリックし、"**詳細設定**"を選択します。



![Image](assets/fr/03.webp)



Watchtower**」メニューでは、2つのオプションが利用可能です：





- Watchtowerサービス**：このオプションを使用すると、Watchtower、つまり不正行為の試みを検出するために他のノードのチャネルを監視するサービスを運用できます。不正行為があった場合、あなたのWatchtowerはBlockchainにトランザクションを公開し、ユーザーはロックされた資金を取り戻すことができます。アクティブ化されると、WatchtowerのURIが表示され、他のノードに伝えることができます；





- Watchtowerクライアント**：このオプションを使用すると、自分のチャンネルを保護するために外部の監視塔に接続することができます。このオプションを有効にすると、Watchtowerサービスを追加することができ、ノードがチャンネルに関する必要な情報を送信します。これらの監視塔はチャンネルの状態を監視し、不正行為が試みられた場合に介入します。



あなたのノードを守るために*Watchtowerクライアント*を有効にすることがもちろん優先されますが、お返しに他のユーザーのセキュリティに貢献するために*Watchtowerサービス*を有効にすることもお勧めします。



![Image](assets/fr/04.webp)



次にGreenの "**Save and Restart Node**"ボタンをクリックしてください。LNDが再起動します。



同じメニューに、WatchtowerサービスのURIもあります。また、チャンネルを保護するために外部のWatchtowerのURIを追加することもできます。ADD**」をクリックしてください。



![Image](assets/fr/05.webp)



オンライン上にはいくつかのウォッチタワーがある。例えば、[LN+とボルテージは利他的なWatchtower](https://lightningnetwork.plus/Watchtower)を提供しており、これに接続することができます：



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



もう一つの選択肢は、あなたのWatchtower URIを仲間のビットコイナーとExchangeし、それぞれが相手のノードを守ることです。



また、ウォッチタワーを複数設置し、いずれかが使えなくなった場合のリスクを軽減することをお勧めする。



最後に、"**Watchtower Client Sweep Fee Rate**" パラメータを調整できます。これは、Watchtower ブロードキャスト処罰トランザクションがブロックに含まれるために支払ってもよい最大手数料率を定義します。チャンネルにロックされている金額に合わせて、十分に高い値を設定してください。