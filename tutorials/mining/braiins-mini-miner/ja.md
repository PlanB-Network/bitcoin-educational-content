---
name: Braiins Mini Miner
description: 自宅で簡単にMiningを作る。
---
![cover](assets/cover.webp)



### はじめに



Mini Miner braiins BMM 100は、Mining pool Braiinsの製品です。このデバイスは魅力的なデザインで、非常に静かである。1.1Th/sの演算能力を発揮し、消費電力は約40ワット。他のデバイスとは異なり、オープンソースではありませんが、インストールは本当に簡単で、数クリックで完了します！Mini Miner BMM 100は、リリースされた最初のバージョンです。現在、BMM 101と呼ばれるバージョン2が生産中で、初代とはディスプレイが大きくなり、Wi-Fiが搭載されている点が異なるが、インストール手順は同じである。



また、[メーカーサイト](https://braiins.com/hardware/mini-Miner-bmm-100)の完全ガイドを直接チェックすることで、より多くの重要な情報を得ることができる。



### BMM100の概要



前面にディスプレイがある平行六面体のようなデバイス



![image](assets/en/01.webp)



上側のファン



![image](assets/en/02.webp)



裏側には、電源用の穴、SDカード用のスペース（アップデートに必要かもしれない）、「IP REPORT」と書かれた小さなボタンがあり、ミニMinerのIP Addressを知ることができる（どのAddressがデバイス・ダッシュボードにアクセスするのに必要なのか）。ボタンが押されると、IP Addressが約5秒間表示され、その後消えてセット画面が再び現れます。しかし、何か設定を変更する必要がある場合は、当該ボタンをもう一度押すだけで、IP Addressが再び画面に表示される。続けて、イーサネット・ポートとデバイス・リセットを実行するためのアクセスを見つけることができ、mini Minerのすべての設定をリセットするには、ピンをつかんで10秒間保持する必要があります。最後に、Minerのステータスを示すGreenと赤の2つのインジケーター・ライトがあります。



![image](assets/en/03.webp)



### ミニMinerの接続



デバイスをイーサネット経由でインターネットに接続する必要がありますが、新しいバージョン（BMM 101）ではその必要はありません。このミニMinerに戻り、場所を特定したら、まずインターネット回線に接続し、次に電源に接続する必要があります。



### 構成



ブラウザーを開き、検索バーにmini Minerを表示するIP Addressを入力する必要があります。ネットワーク上のデバイスを見つけるには、ローカルである必要があるので、使用しているコンピューターがmini Minerと同じネットワークに接続されている必要があります。IP Addressを入力したら、Enterキーを押し、mini Minerのオペレーティング・システム（Braiins OS）へのログイン・ページが画面に表示されます。



![image](assets/en/06.webp)



ログインするには、ユーザー名として `root` を入力し、パスワードは空白のままでかまいません。ログインをクリックすると、ミニMinerダッシュボードが表示されます。



![image](assets/en/07.webp)



### 一般設定



システム



![image](assets/en/24.webp)



設定内には、テーマ（ライトまたはダーク）、言語、タイムゾーン、パスワード変更などの一般的な設定がある。



![image](assets/en/25.webp)



代わりに「ミニMiner画面」を開くと、ミニMinerの画面表示などの設定がある。時刻を表示するか、Bitcoinの価格を表示するか、あるいはHashの製品、温度、消費ワット数など、マシンのステータス情報を画面に表示するかを選ぶことができる。また、画面の明るさを変えたり、ナイトモードを設定したり、12時間表示や24時間表示もできる。



![image](assets/en/26.webp)



変更が完了したら、「変更を保存」をクリックしてください。



![image](assets/en/27.webp)



### Mining poolへの接続



Miningを開始するにはプールに接続する必要があるため、"Configuration "にアクセスする必要があります。



![image](assets/en/08.webp)



で、最初のエントリーは `Pools` だけである。



![image](assets/en/09.webp)



ここで、どのプールを使うかを決めなければならない。このチュートリアルでは、2つのオプションを紹介する。1つ目は、このチュートリアルからわかるように、プロのマイナーも使用しているMining pool Braiinsに接続することです：



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

2つ目のオプションは、パブリックプールのようなソロでミナを行うMining poolに接続することである：



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### ブレイインズ・プール



このプールに接続するには、アカウントを作成する必要がある。このプールもLightning Networkを使って支払いを行うので、1日に数Satsを受け取ることができる。そのためには、報酬を受け取るためのAddressライトニングを設定する必要がある。braiinsプールのアカウント作成方法やAddressライトニングのセットアップ方法がわからない場合は、こちらのガイドに従ってください：



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

これが完了したら、Braiinsプールのダッシュボードに入ります。私たちがしなければならないのは、マイナーの1人と接続したいことをプールに伝えることである。"ワーカー "に行く必要があります。



![image](assets/en/04.webp)



右側の "Connect workers "と書かれた紫色のボタンをクリックする必要がある。



![image](assets/en/05.webp)



ミニMinerをプールに接続するために必要な情報が表示される。ここで唯一変更できるのは、Stratum V2を選択することである。Stratum v2が何であるかは、[glossary](https://planb.network/en/resources/glossary/stratum-v2)のエントリーを参照のこと。



![image](assets/en/10.webp)



stratumv2で始まるこの文字列をコピーする必要がある。コピー」マークをクリックし、ミニMinerのダッシュボードに移動する。新しいプールの追加をクリックする。



![image](assets/en/11.webp)



にコピーした文字列をプールのURLの下のスペースに貼り付ける。



![image](assets/en/12.webp)



次に、ユーザー名とパスワードを追加する必要がある。プールのdashboadに戻ってみよう。その下にuserIDとpasswordがある。userIDとusernameは、アカウントを作成するときにつけたもので、さらにMinerの名前を入れる。プールに接続するデバイスに名前をつけるかどうかは、オプションで決めることができる。代わりに何も入れたくない場合は、`workerName`のままにしておくことができる。



![image](assets/en/13.webp)



次にミニMinerに行き、ユーザー名を入力します。私の場合、"finalstepbitcoin "と入力する。これは私が決めたデバイスの名前です。もし名前をつけたくなければ、userid dot workernameと書けばいい。私の場合はfinalstepbitcoin.workernameとなります。ユーザー名を入力したら、パスワードを決めて空欄に書きます。プール画面にも表示されているanithing123を入力することもできますが、単に好きなパスワードを入力できることを示したいだけです。



すべてのデータを入力したら、右側の保存ボタン（フロッピーディスクのような形をしたボタン）を押す。



![image](assets/en/14.webp)



プール・ダッシュボードに戻り、"Connected！戻る"



![image](assets/en/15.webp)



ミニMinerをブレイインズ・プールに接続した！ワーカーリストに表示されます。もし表示されない場合は、更新してしばらく待ってください。表示されたら、ステータスが "OK "になっていて、Greenのチェックマークがついていることを確認してください。



![image](assets/en/17.webp)



ダッシュボードに戻ると、グラフに動きが見え始め、我々のデバイスのHashrateが表示されているはずだ。これは、プールが私たちの仕事を受け取っていることを意味し、したがって、私たちはあらゆる意味で劣勢に立たされていることになる。



![image](assets/en/16.webp)



#### 公共プール



このプールを通じて、運を試し、プールに寄りかかってソロで採掘することができる。この場合、報酬は受け取れないが、ブロックを採掘することができれば、報酬は全額受け取ることができる。次に、完全にオープンソースのMining専用プールであるパブリック・プールにリンクする。ブラウザで新しいウィンドウを開き、[web.public-pool.io](https://web.public-pool.io/#/)にアクセスする。



![image](assets/en/18.webp)



そこに、必要な情報がすべて載っているページがある。そして、そこにAddressの地層をコピーする。



![image](assets/en/19.webp)



そして、ミニMinerのダッシュボードに戻り、コンフィギュレーションからプールに移動し、新規プールの追加をクリックし（上記と同じプロセス）、プールのURLに「stratum Address」を貼り付ける。



![image](assets/en/20.webp)



さて、プールのページに戻り、ユーザー名としてBitcoin Addressを入力する必要があることを確認しよう。これは、ブロックを弱体化させた場合に報酬を受け取ることになるもので、次にドット、そして以前Braiinsプールで行ったように、デバイスの名前を入力する。



![image](assets/en/21.webp)



ミニMinerに戻り、ユーザー名の下にAddress Bitcoinとピリオド、そして名前を貼り付ける。パスワードにはtestと入力する。



![image](assets/en/22.webp)



ここで設定を保存し、Braiinsプールを無効にする。



![image](assets/en/23.webp)



良かった！パブリックプールでMiningとなった！



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)