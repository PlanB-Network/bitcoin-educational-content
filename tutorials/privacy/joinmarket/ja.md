---
name: JoinMarket

description: JoinMarketを使用し、コマンドラインからCoinJoin over Bitcoinを行う方法についてのガイドとチュートリアル
---

![cover](assets/cover.webp)



---

JoinTmarket "をネットで検索してこのページにたどり着いたのなら、心から感謝している。しかし、あなたは全く異なる、しかし非常に興味深いトピックを扱うガイドにつまずきました！🚬🍁



このチュートリアルの目的は、コマンドラインを通してJoinMarketの理論と実践的な操作を説明することです。🐢 💚



## JoinMarketの理論的定義



私たちはJoinMarketを、完全にTrustless的な方法で、中央のコーディネーターなしに他のユーザーとCoinJoinを可能にするツール、あるいはWalletと定義することができる。



このツールの理論的な部分は非常に幅広いので、私のポッドキャストの特定のエピソードでAddressすることにしました。イタリア語を理解できる人には、このプログラムを正しく使うための基本的なコンセプトをよりよく吸収するために、このエピソードを聞いた後に続けて読むことを強く勧める。



このエピソードは以下のリンクからご覧いただけます：




- [スポティファイ](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [グーグル・ポッドキャスト](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep)（こちらはブラウザから直接聴けます）。
- [Antenna pod](https://antennapod.org/)は、登録不要の無料かつオープンソースのポッドキャストマネージャーです。エピソードを見つけるには、アプリをダウンロードし、_feed rss_セクションに[このリンク](https://Anchor.fm/s/bd5d5b20/podcast/rss)を貼り付けて私のポッドキャストを手動で追加し、JoinMarketに特化したエピソードを検索します。



## インストール



オペレーティングシステム：





- ラスピブリッツ
- アンブレル
- マイノード
- ラスピボルト



## 設定ファイル



JoinMarketは無限の設定を持つカスタマイズ可能なソフトウェアである。これらの設定は`Joinmarket.cfg`と呼ばれるメインプログラムディレクトリに位置する設定ファイルで指定される。



このセクションでは、あなたのニーズに応じて、探求したり変更したりするのが面白いと思われるいくつかのフィールドについて説明します。以下に挙げる変更点はすべて、ソフトウェアの操作を個人のニーズに合わせるために知っておくと便利なものであり、必須ではないことを強調しておきます。



まず、`joinmarket/scripts`フォルダに移動し、コマンドを実行してみよう：



```bash
python wallet-tool.py generate
```


この時点でエラーが出るはずだが、そうすることでソフトウェアが事前に設定した設定ファイルをgenerateしてくれる。この設定ファイルをターミナルから編集することができる：



```bash
nano joinmarket.cfg
```



あるいは



```bash
vim joinmarket.cfg
```



一度開けば、様々な設定とその説明が英語で書かれた多数の行に気づくだろう。具体的には、最も興味深い変数を以下に分析する：





- merge_algorithm`（マージ・アルゴリズム）このフィールドは、ソフトウ ェアが未使用のアウトプットをどの程度積極的に統合するかを調整する。統合するUTXOがたくさんある場合、_gradual_から_greedy_に切り替えるのが理にかなっているかもしれない。
- tx_fees`はトランザクションの支払いにかかる手数料を調整するもので、タンブラーを頻繁に使用する場合にはこの設定を変更すると非常に便利である（これについては後述する）。後者の実行中に手数料が急増した場合、このフィールドを正しく設定しないと、CoinJoinのために多くのSatsを費やすことになる危険性があるからだ。数千の値（例えば2000）を設定すれば2Sats/vBytes、3500なら3.5Sats/vBytesといった具合だ。ニーズに応じて 1500 から 6000 までの数値をお勧めします。
- max_cj_fee_abs`はCoinJoinの間に私たちが選んだメーカーに絶対的にいくら払ってもいいかを指定するために使われます。デフォルトでは、このフィールドは200Satsとなっています。
- max_cj_fee_rel`は上記のフィールドと同じ機能を持つが、各取引相手に支払う相対手数料（パーセント）を指定する。これは `パーセンテージ` の値であるため、大きな金額の CoinJoin でコストが高くならないように、高い値を設定しないように注意してください。メーカーのデフォルト値は _0.00002_ です。
- minimum_makers`は、CoinJoinを行う他の取引相手の数を指定するフィールドである。デフォルトでは、joinMarketは常に4～9の取引相手を選択するが、よりプライバシーを確保したい場合は、この値を5または6に上げることができる（ただし、取引コストは高くなる）。
- cjfee_a`は、私たちがメーカーである場合、私たちの流動性を借りるために、絶対値で何Satsを集めたいかを指定します。このフィールドは完全に主観的なものであり、デフォルトの値はすでに非常に良いものである（したがって、我々はメーカーとしてのより良いプライバシーを持つことになる）我々はより少ない時間でより多くのCoinJoinを作りたい場合は、0にすることを検討することができます。
- cjfee_r` 上記のフィールドと同じだが、絶対値ではなくパーセンテージで表示する。ここでもデフォルト値のままか、より多くの買い手を獲得するために値を下げることをお勧めします。
- ordertype`このフィールドで、絶対価格(absoffer)かパーセント価格(reloffer)かをメーカーから選択する。通常、買い手は経済的な問題については絶対入札を好む。
- minsize` もしメーカーとしてUTXOをあまり小さくしたくないのであれば、参加するための最小CoinJoinを指定することができる。このフィールドはSatoshiで表され、完全に主観的なものです。このフィールドは0のままでもいいし、500000(Sats)、1000000(Sats)と増やしていくこともできる。



joinmarket.cfgファイルのいくつかの変数が誤って設定された場合、ソフトウェアの機能が損なわれたり、プライバシーが完全に破壊される可能性があります！



## 作業環境の設定



ノードによっては、joinmarket.cfgファイル内のこれらのフィールドに正しい値が自動的に設定されますが、手動で再チェックすることをお勧めします：





- `rpc_user = あなたのユーザー名-Bitcoin.confにあるように`。
- rpc_password = yourpassword-as-in-Bitcoin.conf`。
- rpc_host = localhost #デフォルトは通常正しい`。
- rpc_port = 8332 # Mainnet`のデフォルト



この時点で、JoinMarket内でWalletの作成を進めることができます：



```bash
python wallet-tool.py generate
```



このコマンドは、Walletを暗号化するためのパスワードと、Walletにつけたい名前を入力させる。フィデリティーボンドをサポートするかどうかを聞いてくるので、_yes_オプションを使うことをお勧めする：



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


エラーが表示される場合は、上記の4つのRPCフィールドの設定が間違っている可能性が高いです。JoinMarketのドキュメントにある[このガイド](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure)に従ってください。



作業環境のセットアップが完了したので、最も役に立つコマンドを調べ始めることができる。これから説明するスクリプトはすべてコンソールで起動することができ、その後に`--help`を入力すると詳しい説明が表示される。



これで打ち上げを試すことができる：



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



このコマンドは、Walletの様々なミックスデプスを、様々なアドレスに分類して表示してくれる：




- 新品（Address未使用）
- チェンジアウト（前取引の残り）
- Cj-out（CoinJoinの出力）



これがその結果の実例である：



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


このように、Wallet内で異なるプライバシー・レベルを持つサトシを別々に保つことができるのだ。



## CoinJoinシングルでBitcoinを送る



これでサトシを動かすことができる。このソフトの主なコマンドのひとつにスクリプトがある：



```bash
pyhton sendpayment.py
```


これにより、CoinJoinの有無にかかわらず、他のアドレスにトランザクションを送信できるようになる。では、その仕組みと実際の例について説明しよう。デフォルトでは、コマンドの書式は次のようになっている（記号 < と > で囲まれたテキストを置き換えることを忘れずに）：



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



基本的な使用例は次のようなものだ：



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


この場合、CoinJoin(デフォルト・オプション)のカウンターパートを4～9から選択し、mixdepth 0(デフォルト・オプション)から1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btcすなわち5000000 SatoshiをAddressに送ります。



どのUTXOをどのように使うかをもっとコントロールするために、このコマンドの追加オプションを説明しよう：



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


この例では、2つの指定を追加している： -Nはミックスするカウンターパーティーの数、-mは資金を引き出すミックスの深さです。実際には、100,000,000 Sats (1 btc) を Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c に送金しています。



mixdepthを指定して送信値に0を指定すると、joinMarketはいわゆる`sweep`を実行する、つまり、そのmixdepthに含まれるすべての資金を互いに統合して送信する：



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



ここでは、ミックスデプス0（デフォルトなので指定しないこともできた）の資金をすべて7つのカウンターパートとミックスして送った。



sendpaymentコマンドはjoinMarketから外部のWalletに資金を移動したり、Layerのプライバシーを追加してSatoshiを送金するために使用されます。UTXOで十分なレベルのプライバシーを得るには、このガイドの後半で説明するtumbler.pyコマンドを使うのがより適切です。



## メーカーであること



このセクションで取り上げるスクリプトは以下の通り：



```bash
yg-privacyenhanced.py
```



このプログラムはjoinMarketでメイカーとして行動するために使用されます。このソフトウェアはBitcoinノードとプラットフォームの内部マーケットプレイスに接続し、そこではメイカーが流動性の入札者として自らを提示し、テイカーが取引相手を探します。フィデリティボンドを使用したい場合は、このフォーマットで作成することができます：



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



例えば



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



の場合、弊社に返送される出力はBitcoin Address（つまり、フィデリティに割り当てたい資金を入金する必要がある出力）となります。



**注意：フィデリティ・ボンド（通称FB）を作る場合、細心の注意を払うべきことが2つある；**





- 一度入金された資金は、期限が切れるまで再び動かすことはできない。Addressに送信するSatsの数と日付の書式に注意してください。間違いは許されない！
- フィデリティボンドはオンチェーンで容易に認識されるため、CoinJoinを経由し、あなたの身元とは無関係の出所で資金を入金することをお勧めします。同じことは、JoinMarketから期限切れのフィデリティボンドを移動したい場合にもお勧めします。



UTXOを複数回利用する場合は、最も大きい取引のみがFBとして有効とみなされる。



この段落の冒頭で述べたスクリプトを扱いましょう。フィデリティボンドを作成したら（これはオプションであることを覚えておいてください）、joinMarketでメーカーとしての役割を果たすための実行ファイルを実行する準備ができました。Satsが様々なアドレスとmixdepthに預けられたら、コマンドを実行できます：



```bash
python yg-privacyenhanced.py <wallet name>
```



この時点から（ネットワークに接続して数分後）、スクリプトを停止するまで、私たちのJoinMarketクライアントはプロトコル上のアクティブメイカーリストに表示され、CoinJoinを作るために様々な取引相手に私たちの流動性を提供します。Walletに莫大な資金と大きな流動性を預けていない限り）1日に何十回もCoinJoinすることを期待しないでください。また、必要な手数料や預けたSatoshisなどの要素が、あなたがメーカーになる頻度に影響することも忘れないでください。



以下のコマンドを実行することで、Walletで行われたすべての取引の履歴と、Walletの有効期間中に得た利益（メーカーである場合）または手数料（テイカーである場合）を見ることができます。



```bash
python wallet-tool.py <wallet name> history
```



サトシがCoinJoinをすると、最後のCoinJoinになるまでmixdepthからmixdepthに移動します。ColdのWalletに移動させる前に、どれだけプライバシーを確保するかはあなた次第ですが、Walletのサイクルを完全に終了させることをお勧めします。



## タンブラー



いよいよJoinMarketの最も魅力的な部分、タンブラーです！ポッドキャストをお聞きの方なら、これがどういうことかもうお分かりでしょう。始める前に1つお勧めがあります： **手数料に注意！** joinmarket.cfgファイルで制限を設定することを忘れずに（冒頭で説明したように）、そしてオンチェーン手数料が比較的低いとき（10Sats/vB以下）だけプログラムを実行することを検討してください。



タンブラーを起動させるには、スクリプトをメーカーから停止させる必要がある：



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



タンブラーの出力アドレスは少なくとも3つ入力する必要がある。いつものようにコマンドに`--help`をつけると、追加情報を見ることができる。高度なルールを持つ、より複雑な例を見てみよう：



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



この場合、デフォルトのカウンターパート数を使用せず（-Nパラメータは、最大分散2の7カウンターパートが必要であることを示しているため、5から9までのメーカーの乱数）、ミックスデプスあたりのCoinJoinの数を多くするタンブリングスクリプトを起動しました（デフォルトでは、このスクリプトはWalletのセクションごとに1から3までのCoinJoinの乱数を作成し、代わりに-c 3 1コマンドを使用すると、2から4になります）。こうすることで、より多くのSatsをフィーに費やすことになるが、より大きな匿名性が設定される。



また、出力アドレスはいくつでも追加することができる（最小3個、常識的な上限はない）。ただし、Satoshiを出力先として指定したアドレスにどのように振り分けるかは、プライバシーの問題から決められない。



Tumblerは意図的に長いプロセスを経ているため、時折、何かが動作しなくなることがあるが、ほとんどの場合、数時間以内に解決する。完全にクラッシュした場合は、コマンドで再起動を試みることができる：



```bash
python tumbler.py --restart
```



または、単に新しいタンブリングコマンドを再開する。この場合、前のタンブラーのスケジューリングは開始されないが、新しいミキシングサイクルが開始される。ノードのSSHターミナルを閉じるとスクリプトが停止する場合は、コマンドと一緒にインストールできる`TMUX`プログラムを利用することができる：



```bash
sudo apt install tmux
```



シェルから `tmux` と入力して起動すると、ターミナルが開き、リモート接続を終了してもバックグラウンドでアクティブな状態が維持されます。コマンドでノードに再接続するとtmux attach` コマンドでノードに再接続すると、バックグラウンドでアクティブになっていたシェルが再び開きます。



## 結論



JoinMarketは無限のカスタマイズ可能なソフトウェアです。このガイドでは、我々はそれが可能であるように、主要な機能を発見した（または少なくとも私は試してみました、私はこのソフトウェアを使用することは公園で散歩ではないことを認識）誰でもそれを使用することができます。JoinMarketの最大の問題の一つは、ちょうどそれです：それを使用して、メーカーである人々の数。少数のユーザーがこのソフトウェアを利用する場合、全体のプライバシー（アノンセット）が低下します。だからこそ、このガイドが利用を促し、CoinJoinを作るために私のお気に入りのソフトウェアをダウンロードしてインストールすることを納得させることを願っています。いくつかの側面についてさらに深く知りたい場合は、githubにある様々な詳細なドキュメントを読むことをお勧めする。



カメを混ぜてハッピー！🐢💚。



[こちら](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) Turtlecuteをサポートすることができます。