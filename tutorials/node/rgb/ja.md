---
name: RGB
description: RGBに関する導入とアセット作成
---

![cover](assets/cover.webp)

## 導入

2009年1月3日、サトシ・ナカモトは最初のBitcoinノードを立ち上げました。その瞬間から新しいノードが参加し始め、Bitcoinはまるで新しい生命形態のように振る舞い始めました。この生命形態は進化を止めることなく、徐々に世界で最も安全なネットワークになりました。これはサトシが経済的インセンティブを通じて、通常マイナーと呼ばれるユーザーを引き付け、エネルギーと計算能力の投資を促すことでネットワークのセキュリティに貢献するという、非常によく考えられた独自の設計の結果です。

Bitcoinが成長と採用を続ける中で、スケーラビリティの問題に直面しています。Bitcoinネットワークは、約10分の時間でトランザクションを含む新しいブロックをマイニングすることを許可していますが、1日に144ブロックでブロックあたり最大2700トランザクションの値を仮定すると、Bitcoinは秒間わずか4.5トランザクションしか許可していませんでした。サトシはこの制限を認識しており、2011年3月にMike Hearnへ送ったメール1で、今日私たちが支払いチャネルとして知っているものがどのように機能するかを説明しています。確認を待たずに迅速かつ安全にマイクロペイメントを行うことができます。ここでオフチェーンプロトコルが登場します。

Christian Decker2によると、オフチェーンプロトコルは通常、ユーザーがブロックチェーンのデータを使用し、最後の瞬間までブロックチェーン自体に触れることなく管理するシステムです。この概念に基づき、Lightning Networkが誕生しました。このネットワークはオフチェーンプロトコルを使用してBitcoinの支払いをほぼ瞬時に行うことができ、これらの操作がすべてブロックチェーンに書き込まれないため、秒間数千のトランザクションを可能にし、Bitcoinのスケールを可能にします。

Bitcoinのオフチェーンプロトコルの分野における研究と開発はパンドラの箱を開いたようなもので、今日私たちは分散型の方法で価値転送以上のことを達成できることを知っています。非営利のLNP/BP Standards Associationは、BitcoinとLightning Network上のレイヤー2および3プロトコルの開発に焦点を当てており、これらのプロジェクトの中でRGBが際立っています。

## RGBとは何か？

RGBは、2016-2019年にGiacomo ZuccoとコミュニティによってBitcoinとLightningネットワークのためのより良いアセットプロトコルとして考案された、Peter Todd3による一回限りのシールとクライアントサイド検証の研究から生まれました。これらのアイデアのさらなる進化により、RGBはMaxim Orlovskyが2019年からコミュニティの参加を得て実装をリードしている完全なスマートコントラクトシステムへと発展しました。

RGBは、複雑なスマートコントラクトをスケーラブルで機密性の高い方法で実行できるオープンソースプロトコルのセットとして定義できます。これは特定のネットワーク（BitcoinやLightningのような）ではなく、各スマートコントラクトは単に契約参加者のセットであり、異なる通信チャネル（デフォルトはLightningネットワーク）を使用して相互作用できます。RGBはBitcoinブロックチェーンを状態コミットメントの層として使用し、スマートコントラクトのコードとデータをオフチェーンで維持することで、スケーラブルにし、Bitcoinトランザクション（およびScript）をスマートコントラクトの所有権制御システムとして活用します。スマートコントラクトの進化はオフチェーンスキームによって定義されますが、最終的にはすべてがクライアントサイドで検証されることが重要です。

簡単に言うと、RGBはユーザーがスマートコントラクトを監査し、実行し、いつでも個別に検証できるシステムです。これには追加のコストがかからず、「伝統的」なシステムが行うようにブロックチェーンを使用しません。複雑なスマートコントラクトシステムはEthereumによって先駆けられましたが、各操作に大量のガスを消費する必要があるため、約束されたスケーラビリティを達成することはなく、結果として現在の金融システムから排除されたユーザーを銀行化する選択肢にはなりませんでした。
現在、ブロックチェーン業界では、スマートコントラクトのコードとデータはブロックチェーンに保存され、ネットワークの各ノードによって実行されるべきだと推進されています。これは、サイズの過剰な増加や計算リソースの誤用にかかわらずです。RGBが提案するスキームは、スマートコントラクトとデータをブロックチェーンから分離し、他のプラットフォームで見られるネットワークの飽和を避けることで、ブロックチェーンのパラダイムを断ち切ることにより、はるかに賢明で効率的です。また、各ノードが各契約を実行する必要はなく、関係する当事者だけがこれを行うため、これまでにないレベルの機密性を追加します。
![RGB vs Ethereum](assets/1.webp)

## RGBにおけるスマートコントラクト

RGBのスマートコントラクト開発者は、契約が時間とともにどのように進化するかのルールを指定するスキームを定義します。このスキームはRGBにおけるスマートコントラクトの構築の標準であり、発行者が発行用の契約を定義する際や、ウォレットや取引所も特定のスキームに従い、その契約を検証しなければなりません。検証が正しい場合のみ、各当事者はリクエストを受け入れ、資産を扱うことができます。

RGBのスマートコントラクトは、常に一部のグラフのみが知られており、残りにアクセスできない状態変化の有向非巡回グラフ（DAG）です。RGBスキームは、スマートコントラクトが開始するこのグラフの進化のための核となるルールセットです。契約参加者はこれらのルールに追加することができ（スキーマによって許可されている場合）、結果として得られるグラフはこれらのルールの反復的な適用から構築されます。

## 可換資産

RGBの可換資産は、LNPBP RGB-20仕様に従います。RGB-20が定義されると、"genesis data"として知られる資産データがライトニングネットワークを通じて配布され、資産を使用するために必要なものが含まれます。最も基本的な形式の資産は、二次発行、トークンの燃焼、再ノミネーション、または置換を許可しません。

時には、発行者は将来的により多くのトークンを発行する必要があります。例えば、USDTのようなステーブルコインは、各トークンの価値をUSDのようなインフレ通貨の価値に結びつけています。これを実現するために、より複雑なRGB-20スキーマが存在し、ジェネシスデータに加えて、発行者は預託品を生成する必要があり、これもライトニングネットワークで流通します。この情報により、資産の総流通供給量を知ることができます。資産の燃焼や名前の変更にも同じことが適用されます。

資産に関連する情報は公開または非公開にすることができます。発行者が機密性を要求する場合、トークンに関する情報を共有せずに、絶対的なプライバシーで操作を行うことを選択できます。しかし、発行者と保有者が全プロセスを透明にする必要がある反対のケースもあります。これは、トークンデータを共有することで達成されます。

## RGB-20の手続き

燃焼手続きはトークンを無効にし、燃焼されたトークンはもはや使用できません。

置換手続きは、トークンが燃焼され、同じトークンの新しい量が作成されるときに発生します。これは資産の歴史データのサイズを減らすのに役立ち、資産の速度を維持することが重要です。

トークンを置換せずに燃焼することが可能なユースケースをサポートするために、トークンの燃焼のみを許可するRGB-20のサブスキームが使用されます。

## 非可換資産
非代替性資産は、RGBでLNPBP RGB-21仕様に従います。NFTを扱う際、私たちは主スキームとサブスキームを持っています。これらのスキームには彫刻手順があり、トークン所有者によるカスタムデータを添付することができます。今日のNFTで最も一般的に見られる例は、トークンにリンクされたデジタルアートです。トークン発行者は、RGB-21サブスキームを使用してこのデータ彫刻を禁止することができます。他のNFTブロックチェーンシステムとは異なり、RGBはBifrostと呼ばれるLightning P2Pネットワークへの拡張を利用して、大容量メディアトークンデータを完全に分散化され、検閲に抵抗する方法で配布することを可能にします。これは、多くの他の形式のRGB特有のスマートコントラクト機能を構築するためにも使用されます。
代替性資産とNFTに加えて、RGBとBifrostはDEX、流動性プール、アルゴリズム安定コインなど、他の形式のスマートコントラクトを生成するために使用することができます。これらについては、将来の記事で取り上げます。

## RGBのNFT vs 他のプラットフォームのNFT

- 高価なブロックチェーンストレージの必要がない
- IPFSの必要がなく、代わりにLightningネットワークの拡張（Bifrostと呼ばれる）が使用される（そしてそれは完全にエンドツーエンドで暗号化されている）
- 特別なデータ管理ソリューションの必要がない - 再び、Bifrostがその役割を果たす
- NFTトークンや発行された資産/契約ABIに関するデータを維持するためにウェブサイトを信頼する必要がない
- 組み込みのDRM暗号化と所有権管理
- Lightning Network（Bifrost）を使用したバックアップのためのインフラ
- コンテンツの収益化の方法（NFT自体の販売だけでなく、コンテンツへのアクセスも複数回）

## 結論

ビットコインの発売からほぼ13年が経過し、この分野では多くの研究と実験が行われてきました。成功と失敗の両方が、分散型システムが実際にどのように振る舞うか、何がそれらを本当に分散型にするのか、どのような行動がそれらを中央集権化に導く傾向があるのかを少し理解するのに役立ちました。これらすべてが、真の分散化は稀で達成が難しい現象であるという結論に導きました。真の分散化はビットコインによってのみ達成されており、この理由から私たちはそれを基盤として構築する努力をしています。

RGBはビットコインのウサギの穴の中に自身のウサギの穴を持っています。私がそれらを通って落ちていく間、私が学んだことを投稿します。次の記事では、LNPとRGBノードとそれらの使用方法についての紹介を行います。

## RGB-node チュートリアル

### はじめに

このチュートリアルでは、RGB-nodeを使用して代替性トークンを作成し、それを転送する方法を説明します。このドキュメントはRGB-nodeデモに基づいており、このチュートリアルでは実際のテストネットデータを使用し、そのためには、私たち自身の部分的に署名されたビットコイントランザクション、psbtを構築する必要があります。

### 必要条件

Linuxディストリビューションの使用が推奨されます。このチュートリアルはPop!OSを使用して書かれており、これはUbuntuに基づいています。そして、あなたは以下が必要になります：

- cargo
- Bitcoin core
- git
このチュートリアルでは、Linux端末でのコマンド実行を示しています。ユーザーが書き込んだものと端末での応答を区別するために、bashプロンプトを象徴する$記号を含めています。
いくつかの依存関係をインストールする必要があります：

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

ビルド＆実行

RGB-nodeは進行中の作業（WIP）です。そのため、正しくコンパイルして使用するためには、特定のコミット（3f3c520c19d84c66d430e76f0fc68c5a66d79c84）に位置を合わせる必要があります。これを実行するには、以下のコマンドを実行します。

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

今、それをコンパイルします。clapのバージョンに導入された破壊的変更があるため、--lockedフラグを使用することを忘れないでください。

```
$ cargo install --path . --all-features --locked

....
....
    Finished release [optimized] target(s) in 2m 14s
  Installing /home/user/.cargo/bin/fungibled
  Installing /home/user/.cargo/bin/rgb-cli
  Installing /home/user/.cargo/bin/rgbd
  Installing /home/user/.cargo/bin/stashd
   Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

rustコンパイラが教えてくれるように、バイナリは$HOME/.cargo/binディレクトリにコピーされました。コンパイラがそれらを異なる場所にコピーした場合は、そのディレクトリが$PATHに含まれていることを確認する必要があります。

インストールされたバイナリの中には、3つのデーモンまたはサービス（dで終わるファイル）とcli（コマンドラインインターフェース）があります。cliを使用すると、メインのrgbdデーモンと対話できます。このチュートリアルでは2つのノードを実行する予定なので、それぞれが自分のノードに接続する必要がある2つのクライアントも必要になります。そのために、2つのエイリアスを作成します。

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

エイリアスを実行するだけでなく、$HOME/.bashrcファイルの最後に追加してsource $HOME/.bashrcを実行することもできます。
前提

RGB-nodeは、ウォレット関連の機能を一切扱いません。RGB特有のタスクを外部ウォレット（例：bitcoin core）によって提供されるデータで実行します。特に、発行と転送の基本的なワークフローを示すために、以下が必要になります：

- 新しく発行されたアセットをバインドするためのissuance_utxo
- アセットを受け取るreceive_utxo
- アセットの変更を受け取るchange_utxo
- 転送へのコミットメントを含むように出力公開鍵が調整される部分的に署名されたビットコイントランザクション（tx.psbt）

bitcoin core cliを使用します。bitcoindデーモンをtestnetで実行している必要があります。これにより、相互運用性が得られ、最終的にはこのチュートリアルに従った他のRGBユーザーに自分のアセットを送信できるようになります。
簡単にするために、私たちは`~/.bashrc`ファイルの最後にこのエイリアスを追加します。
```
alias bcli="bitcoin-cli -testnet"
```

未使用の出力トランザクションをリストアップし、その中から2つを選びます。一つは`issuance_utxo`で、もう一つは`change_utxo`になりますが、どちらがどちらであるかは重要ではありません。重要なのは、発行者がこれら2つのUTXOを制御していることです。

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

さらに進む前に、アウトポイントについて話す必要があります。単一のトランザクションには複数の出力が含まれることがあり、アウトポイントには32バイトのTXIDと4バイトの出力インデックス番号（vout）が含まれ、コロン（:）で区切られた特定の出力を参照します。私たちのlistunspent出力では、2つのUTXOを見つけることができ、それぞれにtxidとvoutがあり、これらが私たちの`issuance_utxo`と`change_utxo`のアウトポイントです。

`receive_utxo`は受信者が制御するUTXOで、この場合は別のウォレットからのアウトポイントであるe40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0を使用します。
- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

これから、転送を含むコミットを含むように出力を調整する部分的に署名されたトランザクション（tx.psbt）を作成します。txidとvoutを自分のものに置き換えることを忘れないでください。宛先アドレスは重要ではありません。それはあなたのものでも他の人のものでも構いません。satsがどこに行くかは問題ではありません。重要なのは、issuance_utxoを使用することです。

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

この出力により、base64エンコーディングされたpsbtが得られました。これを使用してtx.psbtを作成します。
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt```

新しいディレクトリrgbdataを作成し、各ノードのデータディレクトリが格納されます。

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

$HOME/rgbdataに位置しているとき、各ノードを異なるターミナルで開始します。ここで、~/.cargo/binはrgb-nodeのインストール後にcargoがすべてのバイナリをコピーしたディレクトリです。

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## 発行

アセットを発行するには、fungible issueサブコマンドと引数、ティッカーUSDT、名前"USD Tether"をrgb0-cliで実行し、以下のように発行量とissuance_utxoを割り当てに使用します：

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

アセットが正常に発行されました。この情報を共有に使用してください：
アセット情報：

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"
私たちはassetIdを取得しました。これは、アセットを転送するために必要です。

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

### 盲目的なUTXOの生成

新しいUSDTを受け取るために、rgb-node-1は、アセットを保持するためのreceive_utxoに対応する盲目的なUTXOを生成する必要があります。

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

盲目的なアウトポイント: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
アウトポイント盲目化秘密: 1679197189805229975
```

このUTXOに関連する転送を受け入れることができるように、元のreceive_utxoとblinding_factorが必要になります。

### 転送

ある量のアセットをrgb-node-1に転送するためには、rgb-node-0が盲目的なUTXOに送るために、委託状と開示を作成し、それをビットコイントランザクションにコミットする必要があります。その後、コミットを含めるために変更するpsbtが必要になります。さらに、-iおよび-aオプションを使用して、アセットの起源となる入力アウトポイントを提供し、変更を受け取る割り当てを指定する必要があります。それを次のように示す必要があります @<change_utxo>。
$ rgb0-cli 可分トランスファー utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
トランスファーが成功し、委託書と開示書は "consignment.rgb" と "disclosure.rgb" に書き込まれ、部分的に署名された証人取引は "witness.psbt" に書き込まれました。
共有するための委託データ：consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
これは3つの新しいファイル、consignment、disclosure、そしてtweakを含むpsbtを書き込みます。このpsbtはwitness transactionと呼ばれ、consignmentはrgb-node-1に送られます。

### Witness

witness transactionは署名され、ブロードキャストされるべきです。これには、それをbase64でエンコードし直す必要があります。

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

walletprocesspsbtサブコマンドで署名してください。

```
```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
このテキストは、技術的な内容を含むため、専門用語や特定の形式（この場合はPSBT、つまりPartially Signed Bitcoin Transactionのデータ）を正確に翻訳する必要があります。以下は、指示に従った翻訳です。

```
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
```

これで、ヘックス形式に変換して完了です。

この翻訳では、元のテキストの技術的な内容や形式をそのまま保持し、翻訳することなく提示しています。これは、技術文書やコードの翻訳において、原文の意図や機能を正確に保持するために重要です。
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}

## ブロードキャスト

ブロックチェーンに確認されるように、sendrawtransaction サブコマンドを使用してブロードキャストします。
## 受け入れ

受け入れるためには、rgb-node-1はrgb-node-0から委託ファイルを受け取り、UTXOのブラインディング時に生成されたreceive_utxoと対応するblinding_factorを持っている必要があります。

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

アセット転送が成功しました。
```

これで、<receive_utxo>における100アセットユニットの新しい割り当てを（knownAllocationsフィールドで）確認できるようになりました。以下のコマンドを実行してください：

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ティッカー: USDT
```
```
name: USDテザー
description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: テストネット
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 1
      outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
      revealedAmount:
        value: 100
        blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0

送金時にreceive_utxoがブラインドされたため、支払人rgb-node-0は100USDTがどこに送られたかについての情報を持っておらず、knownAllocationsに位置情報は表示されません。

$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
```
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: テストネット
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

しかし、以下のように、rgb-node-0は、-a引数で転送コマンドに提供された900の資産変更を確認できません。変更を登録するために、rgb-node-0は開示を受け入れる必要があります。

```
$ rgb0-cli fungible enclose disclosure.rgb

開示データが正常に封入されました。
```

rgb-node-0が成功した場合、資産をリストアップすることで変更を確認できます。

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether
```
explanation: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        value: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2

## 結論

私たちは、交換可能な資産を作成し、それをプライベートな方法で一つのトランザクションから別のトランザクションへ移動することができました。ブロックエクスプローラーで確認されたトランザクションをチェックしても、通常のトランザクションと何も違いは見つかりません。これは、RGBがトランザクションを調整するために一回限りのシールを使用するためです。この投稿では、RGBの動作について簡単に紹介しています。

この投稿にはバグがあるかもしれません。何か見つけたら、このガイドを改善するために教えてください。提案や批判も歓迎します。ハッピーハッキング！🖖