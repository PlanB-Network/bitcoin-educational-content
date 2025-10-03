---
name: ダイエットピー
description: 低性能マシン向けに最適化された軽量オペレーティング・システム。セルフホスティングを好む
---

![cover](assets/cover.webp)



非技術界では、「Odroid」、「Raspberry Pi」、「Orange Pi」、「Radxa」といったブランドはほとんど知られていない。しかし、技術界に目を向けるだけで、**SBC**コンピュータ--単一のマザーボード上に構築され、一般的に使用されているコンピュータと比較すると、しばしば極小サイズ--が、あらゆる個人的なプロジェクトのサポートとして、なくてはならないものになっていることがわかる。



これらのコンピュータは、多種多様なモデルで製造されている。これらのコンピュータはLinuxディストリビューションをホストしていることが好ましく、多くの場合、これらのパワー不足のマシンでスムーズに動作するように調整されている。



**DietPiも例外ではありません**: Debianベースのオペレーティングシステムで、可能な限り軽量になるように最適化されており、最も性能の低い`SBC`でも非常に高速に動作します。ちょうどこのチュートリアルを書いているときに Debian12 Bookworm から Debian13 Trixie に切り替わり、オープンソースの `RISC-V` プロセッサベースの SBC もサポートするようになりました。DietPiはさらなる研究に値する、嬉しい発見だ。



## 強み



これは小さなラズベリータイプのボード用の Debian の「通常の複製」ではありません。DietPiがそうです：




- 速度と軽さのために最適化されています**: [SBC用の他のDebianディストリビューションとの比較](https://dietpi.com/blog/?p=888), DietPiはすべてにおいて軽量です。DietPi ISO イメージの重さは 1 GB 未満で、古いモデルの Raspberry や Orange PI (例) 専用のものの中では圧倒的に小さいです。RAMとCPUリソースへの要求が非常に低いので、古いボードであっても、常に最高の性能を引き出すことができます。
- オートメーションとインストーラー**を内蔵：専用コマンドのスイートは、ユーザーがシステムリソースを監視するだけでなく、プログラムのインストールと起動、バージョンの更新、バックアップの作成、すべてのログのチェックなどのタスクを自動化するのに役立ちます。
- 実験指向の強力なコミュニティ**：DietPiコミュニティからの[チュートリアル](https://dietpi.com/forum/c/community-tutorials/8)やプロジェクトは、DietPiのおかげでワンクリックでインストールできるソフトウェアからインスピレーションを得るのに理想的です。



**SBCの性能を余すところなく引き出すことが、かつてないほど簡単になりました**。



## セルフホスティングの自動化


高度なネットワークソリューションを実行するための独自のサーバーや、Bitcoinの専門知識を進化させるためのツールを試してみたいですか？DietPiはあなたが探していたソリューションかもしれません。多くの人が自分のインフラを管理し、完璧に設定され保護されたサーバーを運用する方法を知っていますが、DietPiはゼロから始めたい人に適したステップです。



DietPiは、そのようなタスクに必要な複雑な作業をすべて手動で行う代わりに、`ウィザード`と独自のコマンドラインを使ってそれらを構築することを可能にする。ここでは、より高度なソリューションと同様に、あなた自身のパーソナルクラウド、_スマートホーム_デバイス管理、自動バックアップとcrontabを試すことができます。



![img](assets/en/01.webp)



## インストール



### ダウンロード



DietPiは、オペレーティングシステムを様々なデバイスに書き込むための、無数のISOイメージセットを提供しています。例えば、Raspberry PI5用のISOはまだテスト中ですが、あなたのボードに適したものを見つけられるでしょう。



このガイドでは、シンクライアントにインストールすることにしたので、選択肢は_PC/VM_の次に_Native PC_とした。これらのデバイスには2つのISOイメージがあり、ブートローダーの世代が異なります。チュートリアルで使用するマシンはかなり古いので、_BIOS/CSM_バージョンを選択しました。もし新しいマシンを使っているなら、正しいバージョンは `UEFI` かもしれません。



![img](assets/en/02.webp)



インストーラーの画像`、`sha256`、`Signatures`を含むページに移動します。



![img](assets/en/03.webp)



wget`で必要なファイルをダウンロードできるように、普段使っているコンピュータの`home`にディレクトリを用意する。



![img](assets/en/04.webp)



開発者の公開鍵は最低限調べる必要があったが、このリンクで見つけることができる：https://github.com/MichaIng.gpg。



![img](assets/en/05.webp)



ls -la` でディレクトリの中身をチェックし、`gpg --import` でMichaIngキーを鍵束にインポートする。



### 検証とフラッシュ



最後に、私が最もお勧めするのは、ダウンロードしてSBCにインストールしようとしているオペレーティング・システムの信頼性を確認することです。



![img](assets/en/06.webp)



sha256sumコマンドで`Good signature`の結果と同じHashコントロールが得られたら、ISOをUSBスティックにフラッシュすることができます。これにはWhale Etcherのようなアプリを使ってください。



![img](assets/en/07.webp)



## DietPiのインストール



![img](assets/en/09.webp)



フラッシュドライブをDietPiをホストするデバイスに移し、lime Greenオペレーティングシステムのインストールを開始します。この演習では、16GBのRAMと128GBのSSD、そして2つ目の1TBのデータディスクを搭載したシンクライアントを使用しています。インストールに要した時間は30分未満ですが、例えばラズベリーを使用する場合、リソースが少なくなり、時間がかかるかもしれません。インストール中に進行状況が表示されます。



![img](assets/en/08.webp)



Raspberryなどのために設計されたDietPiの本当の姿は、グラフィカルな環境を持たず、ネイティブな`shsh'アクセスで、いわゆる`ヘッドレス`インストールです。このガイドでは、代わりにグラフィカル環境、正確にはLXDEを紹介します。



このステップでは、デフォルトで使用するウェブブラウザをChromiumとFirefoxから選択するよう求められます。どちらも問題なく動作します。個人的な好み以外に、特に禁忌事項はありません。



最後の方で、インストーラーが何かプログラムをインストールするかどうか聞いてくるかもしれませんが、ここでは**何もプリロードしないことをお勧めします**。このステップの後、セキュリティ上の理由から、2人のユーザーのデフォルトパスワードを変更するよう求められます。最も重要なことは、**グローバル・ソフトウェア・パスワード（GSP）`**を設定することです。 **GSPを設定せずにOSのインストール中にソフトウェアをダウンロードすると、事実上アクセスできないままになってしまいます。グローバルソフトウェアパスワードを設定した後、アンインストールし、再度インストールする必要があります。(この不都合は確率的なもので、100%確実ではありません)。



インストールは、オペレーティングシステムの開発をサポートするために使用される自動データ収集サービスであるDietPi-Surveyの有効化を要求して終了する。ウェブサイトによると、データ収集は、DietPiが提供する自動化からいずれかのソフトウェアをダウンロードしたとき、または次のリリースにアップグレードしたときに有効になる。誰でもオプトイン（_Opt IN_）またはオプトアウト（_Opt OUT_）の選択ができる。



![img](assets/en/23.webp)



インストールが完了し、再起動すると、設定したとおりにDietPiが画面に表示される。チュートリアルのために、前述したように `LXDE` グラフィカル環境を選んだ。デスクトップには `htop` を起動するショートカットと、ターミナルを開くショートカットがあった。



![img](assets/en/10.webp)



### 「オペレーティングシステムの「ツール



Linuxディストリビューションで使っているプログラムのほとんどは忘れてしまいましょう-DietPiはとても最適化されているので、かなりの数が省かれています。基本的には多くのコマンドを手動でインストールしなければならないが、もし試してみたいだけなら、誘惑に負けず、DietPiの自動化をテストしてみよう。



新しいオペレーティング・システムを使い始めるための最初の便利なツールであり、電源を入れるたびに自動的に開くターミナルであることは間違いない。



![img](assets/en/11.webp)



ターミナル画面には、このオペレーティングシステムの[tools](https://dietpi.com/docs/dietpi_tools/)を表す`dietpi-`で始まる一連のコマンドがリストアップされている：




- dietpi-launcher`：オペレーティング・システムやファイル・マネージャーなどにアクセスする。
- dietpi-Software`：スイートで利用可能なすべてのソフトウェアをインストールするためのツールです。
- dietpi-config`: システムの設定にアクセスする。



![img](assets/en/14.webp)



### バックアップ



サーバーのバックアップは、システム管理者が最初の起動時から想定しておくべきルーチンである。



DietPiには`dietpi-Backup`コマンドがあり、理想的な解決策を見つけるために調べることをお勧めします：これは、定期的なバックアップを設定することができ、使用するアプリケーションに応じて、増分バックアップかそうでないか、ルーチンをカスタマイズするためのすべてのオプションがあります。



![img](assets/en/22.webp)



dietpi-Drive_Manager`を起動してバックアップ先のドライブをマウントし、この機能に使用します。



## 構成



セルフホスティングは、好奇心旺盛な人にも、単に熱心な人にも、誰にとっても望ましい経験だ。しかし、サーバーを立ち上げて設定するには、少なくない技術的な課題が伴います。そこで**DietPi**のシンプルさの出番となる。



![img](assets/en/24.webp)



基本的な設定から高度な設定まで、Interfaceコマンド1つで簡単に行えます：



ダイエットピコンフィグ


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi ソフトウェア


```