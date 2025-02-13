---
name: RGBライトニング・ノード
description: RLNでRGB対応のLightningノードを起動するには？
---
![cover](assets/cover.webp)

このステップバイステップのチュートリアルでは、Regtest環境でLightning RGBノードをセットアップする方法を学びます。RGB トークンを作成し、チャネルで流通させる方法を説明します。

## RLNプロジェクト

BitfinexのRGBチームは、完全な技術スタックを開発することによってRGBエコシステムを豊かにするために2022年から取り組んできた。単一の商業製品を目指すのではなく、その努力はオープンソースソフトウェアのレンガを利用可能にし、RGBプロトコル仕様に貢献し、実装リファレンスを作成することに重点を置いている。

RGBエコシステムへのBitfinexの注目すべき貢献の中には、[*RGBlib*ライブラリ](https://github.com/RGB-Tools/rgb-lib)があり、これはRustで書かれ、KotlinとPythonのバインディングを介してアクセス可能で、複雑な検証とエンゲージメントのメカニズムをカプセル化することにより、RGBアプリケーションの開発を大幅に簡素化する。

Bitfinexチームは、Androidで利用可能な「[*Iris Wallet*](https://iriswallet.com/)」と呼ばれるRGBモバイルウォレットも設計しました。このウォレットは、RGB上の*クライアントサイド検証*のためのオフチェーンデータ交換（*委託*）を簡単に管理するために、RGBプロキシサーバーの使用を統合しています。

Bitfinex は `rgb-lightning-node` (RLN) プロジェクトも開発した。これは `rust-lightning` (LDK) のフォークに基づく Rust デーモンで、チャネル内の RGB アセットの存在を考慮するように変更されている。チャネルがオープンされると、RGBトークンの存在を指定することができ、チャネルの状態が更新されるたびに、Lightning出力におけるトークンの分布を反映した状態遷移が作成される。これにより、：


- 例えばUSDTのライトニング・チャネルを開く；
- ルーティング経路に十分な流動性があれば、これらのトークンをネットワークを通じてルーティングする；
- コミットメントトランザクションの追加出力にRGBトランジションをアンカーするだけです。

RLNコードはまだアルファ段階です：**regtest**または**testnet**でのみ使用することをお勧めします。

## RGBプロトコルのリマインダー

RGBはビットコイン上で動作し、スマートコントラクト機能とデジタル資産管理をエミュレートするプロトコルであり、ベースとなるブロックチェーンに過度の負荷をかけることはない。例えばイーサリアム上のような）従来のオンチェーン・スマートコントラクトとは異なり、RGBは「*クライアント側の検証*」システムに依存しています。データおよびステータス履歴の大部分は、関係する参加者によってのみ交換され保存されるのに対し、ビットコイン・ブロックチェーンは（*Tapret*や*Opret*などのメカニズムを介して）小さな暗号コミットメントのみをホストします。したがって、RGBプロトコルでは、ビットコインブロックチェーンはタイムスタンプサーバーと二重支出保護システムとしての役割しか果たしません。

RGBコントラクトは、進化型ステートマシンのような構造になっている。それは、厳密に型付けされコンパイルされたスキーマに従って、初期状態（例えば、供給、ティッカー、またはその他のメタデータを記述する）を定義するジェネシスから始まる。その後、状態遷移と、必要に応じて状態拡張が、この状態を変更または拡張するために適用される。各操作は、カビ可能なアセット（RGB20）の転送であれ、ユニークなアセット（RGB21）の作成であれ、*シングルユースシール*を伴います。これらはビットコインUTXOをオフチェーンステートにリンクし、機密性とスケーラビリティを確保しながら、二重支出を防ぎます。

RGBプロトコルがどのように機能するかについてもっと学ぶには、この包括的なトレーニングコースを受講することをお勧めする：

https://planb.network/courses/csv402
## RGB対応Lightningノード搭載

rgb-lightning-node`バイナリをコンパイルしてインストールするには、まずリポジトリとそのサブモジュールをクローンし、：

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- recurse-submodules`オプションは、必要なサブデバイス（修正版の`rust-lightning`を含む）のクローンも作成する；
- shallow-submodules`オプションは、クローンの深さを制限してダウンロードを高速化しつつ、重要なコミットへのアクセスを提供する。

プロジェクト・ルートから以下のコマンドを実行し、バイナリ.NET Frameworkをコンパイルしてインストールする：

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- locked`は、依存関係のバージョンが尊重されることを保証する；
- debug`は必須ではありませんが、集中するのに役立ちます（お好みで`--release`を使うこともできます）；
- -path .` はカレントディレクトリからインストールするように `cargo install` に指示する。

このコマンドを実行すると、`$CARGO_HOME/bin/` に `rgb-lightning-node` の実行ファイルが作成されます。このパスが `$PATH` に含まれていることを確認してください。

## 前提条件

rgb-lightning-node`デーモンが機能するためには、.NET Frameworkの存在と設定が必要である：


- bitcoind`**ノード

各 RLN インスタンスは、オンチェーン取引をブロードキャストし監視するために `bitcoind` と通信する必要がある。認証（ログイン/パスワード）とURL（ホスト/ポート）をデーモンに提供する必要がある。


- インデクサー**（エレクトラムまたはエスプローラ）

デーモンは、チェーン上のトランザクションをリストアップし、探索することができなければなりません。特に、アセットがアンカーされたUTXOを見つけることができなければなりません。ElectrumサーバーまたはEsploraのURLを指定する必要があります。


- RGB**プロキシ

プロキシサーバーは、Lightningピア間でのRGB *コンサインメント*の交換を簡素化するためのコンポーネントです（オプションですが、強く推奨されます）。ここでもURLを指定する必要があります。

IDおよびURLは、デーモンがAPI経由で*アンロック*されるときに入力される。

## レグテスト開始

簡単な使い方としては、Docker経由で一連のサービスを自動的に起動する `regtest.sh` スクリプトがある：bitcoind`、`electrs`（インデクサ）、`rgb-proxy-server`である。

![RLN](assets/fr/03.webp)

これにより、ローカルで隔離された、設定済みの環境を起動できる。再起動するたびにコンテナとデータ・ディレクトリを作成・破棄する。まずは.NET Frameworkを起動する：

```bash
./regtest.sh start
```

このスクリプトは：


- .NET Frameworkを格納する`docker/`ディレクトリを作成する；
- regtest で `bitcoind` を実行し、インデクサ `electrs` と `rgb-proxy-server` も実行する；
- すべての準備が整うまで待つ。

![RLN](assets/fr/04.webp)

次に、複数のRLNノードを起動する。別々のシェルで、例えば（3つのRLNノードを起動するために）：

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- network regtest` パラメーターは、regtestコンフィギュレーションの使用を示す；
- --daemon-listening-port`は、LightningノードがAPIコール（JSON）をリッスンするRESTポートを示す；
- --ldk-peer-listening-port`は、リッスンするLightning p2pポートを指定する；
- dataldk0/`、`dataldk1/`はストレージ・ディレクトリへのパスである（各ノードは別々に情報を保存する）。

APIのおかげで、ブラウザからRLNノードのコマンドを実行できるようになった。特に、デーモンのアンロックが可能です。ノードと同じコンピューターでブラウザーを開き、URL ：

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

ノードがチャネルを開くには、まず以下のコマンドで生成されたアドレスにビットコインがなければなりません（例えばノードn°1の場合）：

```bash
curl -X POST http://localhost:3001/address
```

答えは住所を教えてくれる。

![RLN](assets/fr/06.webp)

bitcoind` Regtestで、ビットコインを少し採掘してみよう。実行する：

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

上記のノード・アドレスに送金する：

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

その後、取引を確認するためにブロックを採掘する：

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## テストネットの立ち上げ（Dockerなし）

より現実的なシナリオをテストしたい場合は、RegtestではなくTestnet上でRLNノードを起動し、パブリックサービスやあなたがコントロールするサービスを指すことができます：

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

デフォルトでは、コンフィギュレーションが見つからない場合、デーモンは：


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

ログインが必要です：


- bitcoind_rpc_ユーザー名`: `user`
- bitcoind_rpc_username`: `password`

これらの要素は `init`/`unlock` API を使ってカスタマイズすることもできる。

## RGBトークンの発行

トークンを発行するには、まず "colorable "なUTXOを作ることから始める：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

もちろん、注文を変更することもできます。取引を確認するために、.NET Frameworkを採掘します：

```bash
./regtest.sh mine 1
```

これで RGB アセットを作成できます。コマンドは作成したいアセットの種類とパラメータによって異なります。ここでは、"PBN" という名前の NIA (*Non Inflatable Asset*) トークンを 1000 ユニットで作成します。precision`でユニットの分割率を指定します。

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

レスポンスには、新しく作成されたアセットのIDが含まれます。この識別子を覚えておいてください。私の場合は、：

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

その後、オンチェーンで転送したり、Lightningチャネルに割り当てたりすることができます。次のセクションで行うのはまさにこれだ。

## チャンネルを開き、RGBアセットを転送する

まず、`/connectpeer`コマンドを使用して、自分のノードをLightningネットワーク上のピアに接続する必要がある。この例では、私は両方のノードをコントロールしている。そこで、2つ目のLightningノードの公開鍵をこのコマンドで取得する：

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

コマンドは私のノードn°2の公開鍵を返す：

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

次に、関連するアセット（`PBN`）を指定してチャンネルを開きます。openchannel` コマンドでは、チャンネルのサイズを satoshis で定義し、RGB アセットを含めるかどうかを選択できます。何を作成したいかによりますが、私の場合、コマンドは ：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

詳細はこちら：


- peer_pubkey_and_opt_addr`：接続したいピア (先ほど見つけた公開鍵) の識別子；
- capacity_sat`：総チャンネル容量 (satoshis) ；
- push_msat`：チャンネルがオープンされたときに、最初にピアに転送されるミリサット単位の量 (ここでは、ピアに後で RGB 転送ができるように、すぐに 10,000 サット転送します) ；
- asset_amount`：チャンネルにコミットされるRGBアセットの量；
- Asset_id` : チャンネルに参加しているRGBアセットの一意な識別子；
- public`：チャンネルをネットワーク上でルーティングするために公開するかどうかを示す。

![RLN](assets/fr/14.webp)

取引を確認するために、6ブロックが採掘される：

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Lightning チャネルはオープンされ、ノード n°1 側には 500 の `PBN` トークンがある。ノード n°2 が `PBN` トークンを受け取りたい場合は、インボイスを生成しなければならない。その方法は以下の通りです：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

と：


- amt_msat`：インボイスの金額 (最低3000sat)；
- expiry_sec` : インボイスの有効期限（秒） ；
- Asset_id` : 請求書に関連付けられたRGB資産の識別子；
- Asset_amount`：この請求書と共に譲渡されるRGB資産の金額。

これに対して、RGBの請求書が発行される：

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

PBN`トークンで必要な現金を保持している最初のノードから、この請求書を支払うことにする：

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

支払いが行われました。これは.NETコマンドを実行することで確認できる：

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

ここでは、RGBアセットを伝送するように変更されたLightningノードのデプロイ方法を説明します。このデモは.NET Frameworkをベースにしています：


- regtest 環境 (`./regtest.sh` 経由) または testnet ；
- Lightning ノード (`rgb-lightning-node`) は `bitcoind`、インデクサ、`rgb-proxy-server` をベースにしている；
- チャネルのオープン/クローズ、トークンの発行、Lightning経由でのアセット転送などを行うための一連のJSON REST API。

このプロセスのおかげだ：


- ライトニング・エンゲージメント・トランザクションには、RGBトランジションのアンカーを伴う追加出力（OP_RETURNまたはTaproot）が含まれる；
- 送金は従来のライトニング決済とまったく同じ方法で行われるが、RGBトークンが追加される；
- 複数のRLNノードは、経路上のビットコインと資産RGBの両方に十分な流動性があれば、複数のノードをまたいで支払いをルーティングし、実験するためにリンクすることができます。

もしこのチュートリアルが役に立ったと思ったら、下に「緑の親指」をつけていただけると大変ありがたいです。この記事をあなたのソーシャルネットワークでシェアしてください。ありがとうございました！

また、LNP/BP協会が開発したRGB CLIツールを使ってRGB契約を作成する方法を説明した、この別のチュートリアルもお勧めする：

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4