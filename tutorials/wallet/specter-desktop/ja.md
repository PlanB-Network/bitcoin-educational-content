---
name: Specter Desktop
description: マルチシグネチャーのBitcoinポートフォリオを、あなた自身のノードで完全に主権を持って管理する。
---

![cover](assets/cover.webp)



Specter Desktopは、2019年からCryptoadvanceによって開発されたオープンソースアプリケーション（MITライセンス）で、ハードウェアウォレット（Ledger、Trezor、Coldcard、BitBox02、Passportなど）と独自のBitcoinインフラストラクチャ（Bitcoin CoreノードまたはElectrumサーバー）によるBitcoinウォレットの管理を容易にします。このアプリケーションは、特にマルチシグネチャ構成に優れており、複数の独立したハードウェアウォレット間で署名パワーを分散することで、大金を保護することができます。



**このチュートリアルでは、次のことを学びます。




- お使いのコンピュータ（Windows、macOS、Linux）にSpecter Desktopをインストールし、設定します。
- ElectrumサーバーにSpecterを接続する（この例ではUmbrelを使用する）。
- walletハードウェア（コールドカード）でシンプルなwalletを作る
- 完全な主権でビットコインを送受信する
- 複数のハードウェア・ウォレットで2対3のマルチシグネチャーwalletをセットアップする
- UmbrelサーバーにSpecterをインストールする（上級ボーナス）



すべての取引は、外部サーバーに情報を送信することなく、お客様のインフラを通してローカルで検証され、お客様の機密性と金融主権を保証します。サインをする前に、必ずwalletのハードウェア画面で取引を確認してください。



## ダウンロードとインストール



アプリケーションをダウンロードするには、Specter Desktopの公式ウェブサイトをご覧ください。



![Page d'accueil Specter](assets/fr/01.webp)



ダウンロードページで、お使いのオペレーティングシステムに対応するバージョンを選択してください：macOS、WindowsまたはLinux。



![Téléchargement selon l'OS](assets/fr/02.webp)



ダウンロードが完了したら、お使いのオペレーティングシステムの通常の手順に従ってアプリケーションをインストールしてください。macOSの場合は、アイコンを「アプリケーション」にドラッグします。Windowsの場合は、インストーラーを実行します。Linuxの場合は、パッケージの指示に従ってください。



## 初期設定



初回起動時に、Specter Desktopは接続タイプを選択するように尋ねます。Electrumサーバーに接続するか、Bitcoin Coreノードに接続するかを選択します。



![Choix du type de connexion](assets/fr/03.webp)



この例では、Umbrel上で動作するElectrumサーバーへの接続を使用する。



詳しくは、Umbrelのチュートリアルをご覧ください：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

このオプションは Bitcoin Core よりも高速な同期を提供します。Bitcoin Core" を選択し、ローカル・ノードへの接続を設定することもできます。以下の手順は、どちらを選択しても変わりません。



Electrum接続 "を選択し、"自分のものを入力 "を選択して、自分のElectrumサーバーを設定します。



![Configuration Electrum](assets/fr/04.webp)



Electrum サーバのアドレスを入力する。Umbrelの場合、アドレスは`umbrel.local`、ポートは`50001`です。Connect "をクリックして接続を確立する。



接続が完了すると、ウェルカムスクリーンが表示され、チェックリストが表示されます。ハードウェア・ウォレットを追加する必要があります。



![Écran d'accueil](assets/fr/05.webp)



## walletハードウェアの追加



左側のメニューで「Add device」をクリックし、walletのハードウェアを追加します。



Specter Desktopは、数多くのハードウェアウォレットをサポートしています：Trezor、Ledger、BitBox02、Coldcard、KeepKey、Keystone、Cobo Vault、その他多数。



もっと詳しく知りたい方は、ハードウェアwalletチュートリアルをご覧ください。



![Sélection du type de hardware wallet](assets/fr/06.webp)



walletハードウェアを選択します。この例ではColdcard MK4を使用しています。



以下は、このwalletハードウェアのチュートリアルです：



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcardの場合、walletハードウェアからUSB接続またはmicroSDカード経由で公開鍵をエクスポートする必要がある。



![Import des clés du Coldcard](assets/fr/07.webp)



表示される指示に従って、Coldcard からキーをエクスポートします。wallet ハードウェアに名前を付けます（ここでは「MK4 Tuto」）。鍵のインポートが完了したら、単一の鍵で wallet を作成するか、他のハードウェア・ウォレットを追加してマルチシグネチャ wallet を作成できます。



![Dispositif ajouté](assets/fr/08.webp)



## ポートフォリオの作成



walletハードウェアを追加した後、"Create single key wallet "をクリックして単一署名walletを作成します。



ポートフォリオに名前を付け（例："Wallet for tuto"）、アドレスタイプを選択する。取引コストを最適化するネイティブのbech32アドレスを使用するには、"Segwit "を選択します。



![Configuration du portefeuille](assets/fr/09.webp)



ポートフォリオが作成されると、Specter はポートフォリオの復元に必要なすべての公開情報（記述子、拡張公開鍵）を含むバックアップ PDF ファイルを保存します。このファイルには秘密鍵は含まれません。



![Sauvegarde du portefeuille](assets/fr/10.webp)



## ビットコインを受け取る



ビットコインを受け取るには、左側のメニューでwalletを選択し、「受け取り」タブをクリックします。



SpecterはQRコード付きの新しい受信アドレスを自動的に生成します。



![Génération d'une adresse de réception](assets/fr/11.webp)



アドレスをコピーするか、QRコードをスキャンしてください。誰かに渡す前に、必ずwalletのハードウェア画面でアドレスを確認してください。



## 履歴と住所を見る



ビットコインを受け取ったら、「取引」タブで取引を確認できます。



![Historique des transactions](assets/fr/12.webp)



Addresses "タブでは、ポートフォリオによって生成されたすべてのアドレスを、その使用状況と関連する金額とともに表示することができます。



![Liste des adresses](assets/fr/13.webp)



## ビットコインを送る



ビットコインを送信するには、「送信」タブをクリックします。受信者のアドレス、送信金額を入力し、UTXO（コインコントロール）を手動で選択したい場合は、詳細オプションをチェックします。



![Création d'une transaction](assets/fr/14.webp)



Create Unsigned Transaction "をクリックしてトランザクションを作成します。Specter は、wallet ハードウェアでトランザクションに署名するよう求めます。



![Signature de la transaction](assets/fr/15.webp)



コールドカードを使用している場合は、USB経由でのサインか、microSDカード（エアギャップ）を使用したサインかを選択することができます。walletのハードウェア画面で、宛先アドレスと金額を注意深く確認しながら、トランザクションを確認する。



トランザクションが署名されると、Bitcoinネットワーク上でブロードキャストすることができる。



![Options de diffusion](assets/fr/16.webp)



取引送信」をクリックして取引を送信します。Specterは取引が送信されたことを確認し、取引タブでステータスを追跡できます。



![Diffusion de la transaction](assets/fr/17.webp)



## マルチシグネチャー・ポートフォリオの作成と使用



Specter Desktopの大きな資産の一つは、マルチシグネチャ・ポートフォリオの管理を簡素化できることです。マルチシグネチャwalletは、トランザクションを承認するために複数の署名を必要とするため、単一障害点を排除することができます。例えば、2-on-3コンフィギュレーションでは、支出を検証するために3つのハードウェア・ウォレットから2つの署名を必要とする。



マルチシグ wallet を作成するには、まず「Add device（デバイスの追加）」を使用して、すべての 署名用ハードウェアウォレットを追加します。この例では、3つの異なるハードウェア・ウォレットを使用します：Coldcard MK4（先に追加済み）、Passport、Ledgerです。このようにメーカーを多様化することで、単一のサプライチェーンやファームウェアへの依存を避け、セキュリティを強化することができます。



以下はLedgerとパスポートのチュートリアルへのリンクです：



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

walletハードウェアに名前を付け（例："Passport multi"）、microSDカードまたはQRコード経由でキーをインポートしてパスポートを追加します。続けて "Continue "をクリックしてください。



![Ajout du Passport](assets/fr/23.webp)



次に、Ledger を USB 経由で接続し、wallet ハードウェア上で Bitcoin アプリケーションを開いて追加する。Ledgerに名前を付け（例："ledger multi"）、"Get via USB"、"Continue "の順にクリックして公開鍵をインポートする。



![Ajout du Ledger](assets/fr/24.webp)



Specterに3つのハードウェアウォレットを登録したら、「walletを追加」をクリックし、「マルチシグネチャ」オプションを選択してマルチシグネチャwalletを作成します。



![Choix du type de wallet](assets/fr/25.webp)



マルチシグネチャーのクォーラムに含めたい3つのハードウェアウォレットを選択します：MK4 Tuto、Passport multi、ledger multiです。続行」をクリックして次のステップに進みます。



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



マルチシグネチャーの設定を選択します。最適化された手数料の恩恵を受けるために、アドレスタイプとして "Segwit "を選択してください。Required Signatures to Authorize Transactions (m of 3) "パラメーターで、しきい値を定義できます：2対3の構成では、2つの署名が必要です。各walletハードウェアは、対応するマルチシグキーを表示します。Create wallet "をクリックして作成を確定する。



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



これで「Multi tuto」マルチシグネチャ・ポートフォリオが作成されました。Specterは直ちに、ポートフォリオ記述子を含むバックアップPDFファイルを保存することをお勧めします。バックアップPDFを保存」をクリックして、この重要なファイルをダウンロードしてください。



![Wallet multisig créé](assets/fr/28.webp)



Specterはまた、QRコードまたはファイル経由でwallet情報を各ハードウェアウォレットにエクスポートすることもできます。これにより、特定のハードウェアウォレット（ColdcardやPassportなど）はマルチシグ設定を直接メモリに保存することができます。



パスポートの場合、デバイスのロックを解除し、「アカウント管理」→「Walletを接続」→「Specter」→「Multisig」→「QRコード」と進み、Specterが生成したQRコードをスキャンします。その後、パスポートはマルチシグ設定を検証するために、walletからの受信アドレスをスキャンするよう要求します。



MK4の場合は、PCに接続してロックを解除します。次に「Save MK4 Tuto file」をクリックし、ファイルをMK4に保存します。次回walletハードウェアに署名する際、MK4はこのファイルを使用してマルチシグの設定を完了します。



![Export vers les hardware wallets](assets/fr/29.webp)



ちなみに、ポートフォリオの「設定」タブ→「エクスポート」からいつでもバックアップにアクセスできます：



![Accès au backup PDF](assets/fr/30.webp)



日常的な使い方は、シンプルな wallet と同様です。通常通り generate でアドレスを受け取ります。ビットコインを送るには、"Send "タブで受取人のアドレスと金額を入力し、"Create Unsigned Transaction "をクリックします。



![Création d'une transaction multisig](assets/fr/31.webp)



SpecterがPSBT（Partially Signed Bitcoin Transaction）を構築し、「Acquired 0 of 2 signatures」と表示する。ここで、3つのハードウェアウォレットのうち、少なくとも2つで署名する必要があります。最初の wallet ハードウェア（例：「MK4 Tuto」）をクリックして Coldcard で署名し、次に 2 番目のハードウェア（例：「Passport multi」）をクリックして必要な 2 番目の署名を取得します。



![Signature de la transaction](assets/fr/32.webp)



必要な2つの署名を取得したら（インターフェイスには「Acquired 2 of 2 signatures」と「Transaction is ready to send」と表示されます）、「Send Transaction」をクリックしてBitcoinネットワーク上でトランザクションをブロードキャストします。



![Transaction prête à être diffusée](assets/fr/33.webp)



このマルチシグネチャ・アプローチは、企業（複数の管理者が支出を承認する必要がある）、家族（複数世代にわたる相続の保護）、または大金を管理する個人（局地的な災害に耐えるためのハードウェア・ウォレットの地理的分散）に特に適している。



### マルチシグネチャ・バックアップの重要性



**ご注意ください**：マルチシグポートフォリオのバックアップは、シングルポートフォリオのバックアップとは根本的に異なります。リカバリー用フレーズ（seedフレーズ）だけでは、マルチシグポートフォリオを復元するのに十分ではありません。マルチシグポートフォリオの設定情報を含む**output descriptor**（output descriptor）もバックアップする必要があります。



output descriptorには、各共同署名者の拡張公開鍵（xpubs）、署名のしきい値（この例では2対3）、使用したスクリプトのタイプ（ネイティブ、ネスト、レガシーSegwit）、各walletハードウェアのバイパス・パスといった重要なデータが含まれています。この記述子がないと、3つのリカバリフレーズのうち2つがあっても、walletを再構築したり、ビットコインにアクセスしたりすることができません。この記述子は、あなたのソフトウェアに、あなたの資金に対応する Bitcoin アドレスの公開鍵を generate に結合する方法を知らせます。



Specter Desktopは、マルチシグポートフォリオ作成時に自動的にバックアップPDFファイルを生成します。このPDFファイルには、完全な記述子、各walletハードウェアのフィンガープリント、および復元に必要なすべての公開情報が含まれています。 **このファイルには秘密鍵**は含まれていないため、それ自体でビットコインを使用することはできませんが、このファイルにアクセスすることで、誰でもあなたの完全な取引履歴と残高を見ることができます。



マルチシグネチャーの設定を正しくバックアップするには、以下の手順に従ってください：ポートフォリオを作成した後、「設定」タブをクリックし、「エクスポート」から「バックアップPDFを保存」を選択します。このPDFのコピーを数部作成します。少なくとも2部は紙に印刷し、暗号化されたデジタルコピーも保管します。リカバリーフレーズと一緒にPDFのコピーを1部ずつ、地理的に離れた場所に保管してください。



リカバリーのフレーズを耐火・防水メタルプレートに刻み、その寿命を保証しましょう。コンピュータの `~/.specter` フォルダを紛失し、ディスクリプターのバックアップなしでハードウェアウォレットの1つを紛失した場合、2対3の構成であっても、すべての資金は回復不能に失われます。マルチシグネチャーの冗長性はwalletハードウェアの損失から保護しますが、walletのディスクリプタを正しくバックアップしている場合に限ります。



## Specter Desktopの利点と限界



**メリット**：サードパーティのサーバーを使用しない完全なローカル認証による最適な機密性。高度な構成（企業、家族、個人）のためのマルチ署名の柔軟性。完全な相互運用性（USBおよびエアギャップ）による広範なハードウェアwalletサポート。



**制限事項Bitcoinの高度な概念（UTXO、記述子、派生パス）にはかなりの学習曲線がある。



## ベストプラクティス



マルウェアから身を守るため、バリデーションの前に必ずハードウェアwalletの画面でアドレスと金額を確認すること。



PDFバックアップをシードとは別に保管してください。これらの公開ディスクリプタは、銀行の金庫室や暗号化されたクラウドに保存することができ、秘密鍵を公開することなくリカバリを容易にします。



大口資金でポートフォリオを使用する前に、tokenの金額でリカバリーをテストしてください。作成、テスト、削除、復元を行い、手順を検証してください。



Specterとファームウェアを常に最新の状態に保つ。マルチシグネチャーの連帯保証人を地理的（自宅／職場／近隣）に分散させ、局地的な災害に耐える。会計や税務申告を容易にするため、説明ラベルを使用する。



## おまけ：Bitcoinサーバーへのインストール（Umbrel、RaspiBlitz、Start9）



Umbrel、RaspiBlitz、MyNode、Start9などのBitcoinサーバーを既にお持ちの場合は、それらのアプリケーションストアから直接Specter Desktopをインストールすることができます。このアプローチにはいくつかの大きな利点があります：アプリケーションは自動的にローカルのBitcoin Coreノードに設定され、ネットワーク上のどのデバイスからでもWebインターフェース経由で24時間いつでもアクセス可能で、Tor経由で安全にリモートアクセスすることもできます。Bitcoinのインフラ全体が1台の専用サーバーに集約されるため、管理が簡素化され、主権が強化されます。



### Umbrel App Storeからのインストール



Umbrel インターフェースから App Store に移動し、Specter Desktop を検索します。インストール」をクリックして、インストールを開始します。



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



インストールが完了したら、UmbrelでSpecter Desktopを開きます。ウェルカム画面が表示されますので、接続タイプを選択してください。Umbrel で Specter を使用している場合は、「設定の更新」をクリックして接続を設定してください。



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



リモート Specter USB 接続」を選択すると、リモート Umbrel サーバーで Specter を使用している間、ローカルコンピューターに接続された USB ハードウェアウォレットの使用が可能になります。



![Configuration Remote Specter USB](assets/fr/20.webp)



表示される指示に従ってHWIブリッジを設定する。デバイスのブリッジ設定にアクセスし、ドメイン `http://umbrel.local:25441` をホワイトリストに追加する必要がある。Update "をクリックして設定を保存する。



![HWI Bridge Settings](assets/fr/21.webp)



ローカルコンピューターからもUSBハードウェアウォレットを使用したい場合は、Specter Desktopアプリケーションをコンピューターにダウンロードし、「はい、リモートでSpecterを実行します」に設定してください。保存」をクリックして設定を確定します。



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## 結論



Specter Desktopは、高度なBitcoin設定を民主化し、主権や機密性を犠牲にすることなくマルチシグネチャを利用できるようにします。多額の資金を管理するユーザーにとっては、組織的な慣行を個人でも導入可能なソリューションに変えます。



このアプリケーションは、インフラと学習への初期投資が必要ですが、検証インフラの制御、鍵の物理的所有権、第三者の監視から解放された取引など、完全な主権を提供します。個人で貯蓄を守る場合でも、家族で複数世代に渡る貸金庫を作る場合でも、企業でキャッシュフローを管理する場合でも、Specter Desktopは最大限のセキュリティと絶対的な主権を両立させるためのリファレンスツールです。



## リソース



### 公式文書




- [妖怪デスクトップ公式サイト](https://specter.solutions/desktop/)
- [GitHubソースコード](https://github.com/cryptoadvance/specter-desktop)
- [完全ドキュメント](https://docs.specter.solutions/)



### コミュニティとサポート




- [テレグラム妖怪ウォッチコミュニティグループ](https://t.me/spectersupport)
- [Redditディスカッションフォーラム](https://reddit.com/r/specterdesktop/)
- [GitHubバグレポート](https://github.com/cryptoadvance/specter-desktop/issues)