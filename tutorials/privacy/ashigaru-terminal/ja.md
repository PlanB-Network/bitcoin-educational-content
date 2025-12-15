---
name: Ashigaru Terminal
description: デスクトップで足軽を使ってコインジョイントを作る
---

![cover](assets/cover.webp)



足軽ターミナルは、Whirlpoolコインジョインプロトコルを実装したSparrowサーバーを足軽チームが改良したものです。このソフトウェアは、Whirlpool GUIを中心に、Wallet Samouraiによって開始された作業の継続であり、その基本原則である自己保存と機密保持を採用しています。



このソフトウェアはSparrowサーバーのforkであり、Whirlpoolエコシステムと完全に統合するために修正・最適化されたものである。



足軽ターミナルは最小限のTUIインターフェイスで動作し、パーソナルコンピュータまたは専用サーバー上に配置することができます。Whirlpoolと直接対話し、"*Tx0*"を開始し、"*Deposit*"、"*Premix*"、"*Postmix*"、"*Badbank*"アカウントを管理し、パーツの機密性を強化するために自動リミックスを実行することができます。



つまり、足軽ターミナルは、Whirlpoolを使ってコインジョイントを作りたい場合に特に役立つのだ。



この最初のチュートリアルでは、足軽ターミナルのインストールと操作方法を説明します。2回目のチュートリアルでは、コインジョイントの作成について説明します。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1.足軽ターミナル設置



足軽ターミナルをインストールするには、Tor Browserが必要です。バイナリはTorネットワーク経由でのみ配布されているからです。まだインストールしていない場合は、[あなたのマシンにインストールしてください](https://www.torproject.org/download/)。



### 1.1.足軽ターミナルをダウンロード



Tor Browserから[Gitリポジトリのリリースページ](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/)にアクセスし、あなたのOSに対応した最新版の足軽ターミナルをダウンロードしてください。



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



お使いのオペレーティング・システムに対応する以下の2つのファイルをダウンロードしてください：




- バイナリ（Debian/Ubuntuの場合は `ashigaru_terminal_v1.0.0_amd64.deb`、macOSの場合は `.dmg`、Windowsの場合は `.zip`）；
- 署名されたハッシュファイル：ashigaru_terminal_v1.0.0_signed_hashes.txt`。



### 1.2.足軽ターミナルをチェック



お使いのデバイスでソフトウェアを実行する前に、その真正性と完全性を確認する必要があります。これは重要なステップであり、ビットコインを危険にさらしたり、マシンを感染させたりする可能性のある不正なバージョンをインストールすることを防ぎます。



新しいブラウザのタブを開き、[Keybase verification tool](https://keybase.io/verify)にアクセスする。ダウンロードした`.txt`ファイルの内容を所定のフィールドに貼り付け、`Verify`ボタンをクリックする。



![Image](assets/fr/02.webp)



検証ソースを多様化するために、クリアネット[ashigaru.rs](https://ashigaru.rs/download/)の`/download`セクションにあるメッセージと比較することもできます。



![Image](assets/fr/03.webp)



署名が有効であれば、Keybaseはそのファイルが足軽の開発者によって署名されたことを確認するメッセージを表示します。



![Image](assets/fr/04.webp)



また、Keybaseによって表示された`ashigarudev`プロフィールをクリックし、その鍵指紋が`A138 06B1 FA2A 676B`と完全に一致することを確認することもできる。



![Image](assets/fr/05.webp)



この段階でエラーが表示された場合は、署名が無効です。この場合、**ダウンロードしたソフトウェアをインストールしないでください**。最初からやり直すか、コミュニティに助けを求めてから続けてください。



Keybaseはアプリケーションの認証済みハッシュを提供しました。次に、ダウンロードした `.deb`、`.zip`、`.dmg` ファイルのハッシュが、Keybase で認証されたものと一致するか確認する。これを行うには、[HASH FILE ONLINE](https://hash-file.online/)にアクセスする。



BROWSE...`ボタンをクリックし、ステップ1.1でダウンロードした `.deb`、`.zip`、`.dmg` ファイルを選択する。次に `SHA-256` ハッシュ関数を選択し、`CALCULATE HASH` をクリックしてファイルのハッシュを generate する。



![Image](assets/fr/06.webp)



すると、ソフトウェアのハッシュが表示されます。Keybase.ioで確認したハッシュと比較してください。両者が完全に一致すれば、真正性と完全性のチェックは成功です。その後、ソフトウェアを使用することができます。



![Image](assets/fr/07.webp)



### 1.3 足軽ターミナル打ち上げ





- Debian / Ubuntu



ソフトウェアをインストールするには、：



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



ダウンロードしたバージョンに従って順序を変更する。



それからインストールを確認する：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



その後、ソフトウェアを起動する：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- ウィンドウズ



ダウンロードしてチェックした`.zip`ファイルを右クリックし、`Extract All...`を選択して中身を取り出す。



解凍が完了したら、`Ashigaru-terminal.exe`ファイルをダブルクリックしてソフトを起動する。



![Image](assets/fr/08.webp)



## 2.足軽ターミナル



足軽ターミナルはTUI(*Text-based User Interface*)プログラムです。メニューやキーボードショートカットを使って操作しますが、古典的なグラフィック環境はありません。



![Image](assets/fr/09.webp)



使い方は簡単で、キーボードの矢印キーを使ってメニューを移動し、`Enter`キーを押してアクションを有効にしたり、選択を確定したりする。



## 3.足軽ターミナルにノードを接続する



デフォルトでは、足軽ターミナルはパブリックな Electrum サーバーに接続します。これでは機密保持や主権の面でリスクがあるのは明らかです。そこで、自分のElectrum Serverに直接接続するように設定します。



これを行うには、`Preferences > Server` メニューを開く。



![Image](assets/fr/10.webp)



Edit >`ボタンをクリックする。



![Image](assets/fr/11.webp)



プライベートElectrum Server`を選択し、`<Continue>`をクリックする。



![Image](assets/fr/12.webp)



サーバーのURLとポートを入力します。.onion`にTorアドレスを指定することができます。次に`< Test >`をクリックして接続を確認する。



![Image](assets/fr/13.webp)



接続に成功すると、サーバーの詳細とともに`Success`というメッセージが表示されます。



![Image](assets/fr/14.webp)



まだBitcoinノードをお持ちでない方は、このコースを受講されることをお勧めする：



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*このチュートリアルの場合、テストネットで作業しているので、Electrsのサーバーから切断する。しかし、mainnet.*でも操作は全く同じです。



## 4.足軽ターミナルでポートフォリオを作成



ソフトウェアが正しく設定されたので、Bitcoinのポートフォリオを追加することができる。



選択肢は2つある：




- walletを一から作成し、足軽ターミナルだけで使用することができます。この場合、walletを操作するたびにこのソフトを開く必要があります；
- また、既存の足軽walletを携帯電話から足軽ターミナルに直接インポートすることもできます。この方法のデメリットは、walletが1つではなく2つの危険な環境にさらされることになり、セットアップのセキュリティが若干低下することです。その反面、足軽ターミナルを起動したままコインをミックスしたり、足軽モバイルアプリから遠隔操作でコインを使うことができるというメリットがあります。



このチュートリアルでは、2番目の方法を選びます。ただし、全く新しいポートフォリオを作りたい場合でも、手順は同じです。唯一の違いは、作成中に新しいニーモニック・フレーズと新しいpassphraseを保存する必要があることです。



また、Ashigaru Terminal ではビットコインを直接使用することはできません。同じウォレットを Ashigaru Terminal と Ashigaru アプリ（このチュートリアルで私が行う方法）または Sparrow Wallet で同期させることができます。



まだ足軽アプリのwalletをお持ちでない方は、専用のチュートリアルをご覧ください：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Wallets`メニューに行く。



![Image](assets/fr/15.webp)



次に「walletを作成/復元...`」を選択します。Walletを開く...`を選択すると、足軽ターミナルに保存されているポートフォリオに後からアクセスすることができます。



![Image](assets/fr/16.webp)



ポートフォリオに名前をつける。



![Image](assets/fr/17.webp)



そしてポートフォリオタイプ`Hot Wallet`を選択する。






![Image](assets/fr/18.webp)



最初の選択によって手順が異なるのはこの段階だ：




- ゼロから新しいポートフォリオを作成したい場合は、`<Generate New Wallet>` をクリックし、passphrase BIP39 を定義してから、ニーモニックフレーズと passphrase を物理的な媒体に慎重に保存してください；



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- 足軽と同じwalletを使いたい場合は、ニーモニックフレーズの12語とpassphraseのBIP39を、対応するフィールドに直接入力してください。単語は小文字で、全角で、スペースで区切って、数字や余分な文字は入れずに、順番に書いてください。



このステップが完了したら、`< Next >`をクリックします。



*注意*：このボタンがクリックできない場合、あなたのニーモニック・フレーズは無効です。どの単語も間違っていないか、スペルミスがないかを注意深くチェックしてください。



![Image](assets/fr/19.webp)



パスワードを設定してください。このパスワードは、足軽ターミナルwalletのロックを解除し、不正な物理的アクセスから保護するために使用されます。つまり、このパスワードがなくても、ニーモニックフレーズとpassphraseがあれば、誰でもwalletを復元し、ビットコインにアクセスすることができます。



長く、複雑で、ランダムなパスワードを選ぶ。コピーを安全な場所に保管する：物理的な媒体か、安全なパスワード・マネージャーに保管するのが理想的です。



終了したら`< OK >`をクリックしてください。



![Image](assets/fr/20.webp)



## 5.ポートフォリオの使用



どのアカウントにアクセスするか選択できます。今のところ、ミックスを開始していないので、`Deposit`アカウントにアクセスする。



![Image](assets/fr/21.webp)



足軽ターミナルはSparrowサーバーのforkなので、操作はSparrowと同じです。メニューも同じです：



![Image](assets/fr/22.webp)





- 取引履歴」：この口座に紐づく取引の履歴を参照できる。私の場合、同じwalletの足軽アプリで何度か取引しているので、すでにいくつか表示されている。



![Image](assets/fr/23.webp)





- receive`: サッツを預金口座に入れるための、新しい空白の受取アドレスを生成する。



![Image](assets/fr/24.webp)





- addresses`: アカウントの内部チェーンに属しているか外部チェーンに属しているかに関わらず、すべてのアドレスのリストを表示します。



![Image](assets/fr/25.webp)





- UTXOs`：利用可能なUTXOをすべてリストアップする。



![Image](assets/fr/26.webp)





- 設定`: ポートフォリオの*ディスクリプタ*にアクセスできます。また、seedを参照したり、*ギャップリミット*を調整したり、ポートフォリオの作成日を変更したりすることもできます。



![Image](assets/fr/27.webp)



これで、Ashigaru Terminal のインストールと使用方法がわかりました。次のチュートリアルでは、このソフトウェアを使ってコインジョインを実行し、「*Postmix*」の資金を管理する方法を見ていきます。
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
