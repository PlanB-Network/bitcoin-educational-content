---
name: スペクターデスクトップ
description: マルチシグネチャーのBitcoinポートフォリオを、あなた自身のノードで完全に主権を持って管理する。
---

![cover](assets/cover.webp)



Specter Desktopは、2019年からCryptoadvanceによって開発されたオープンソースアプリケーション（MITライセンス）で、ハードウェアウォレット（Ledger、Trezor、Coldcard、BitBox02、Passportなど）と独自のBitcoinインフラストラクチャ（Bitcoin coreノードまたはElectrum Server）によるBitcoinウォレットの管理を容易にします。このアプリケーションは、特にマルチシグネチャ構成に優れており、複数の独立したハードウェアウォレット間で署名パワーを分散することで、大金を保護することができます。



**このチュートリアルでは、次のことを学びます。




- お使いのコンピュータ（Windows、macOS、Linux）にSpecter Desktopをインストールし、設定します。
- スペクターをElectrum Serverに接続する（この例ではUmbrelを使用する）
- Hardware Wallet（コールドカード）でシンプルなWalletを作る
- 完全な主権でビットコインを送受信する
- 複数のハードウェアウォレットで2対3のマルチシグネチャーWalletを設定する
- UmbrelサーバーにSpecterをインストールする（上級ボーナス）



すべての取引は、外部サーバーに情報を送信することなく、お客様のインフラを通してローカルで検証され、お客様の機密性と金融主権を保証します。サインをする前に、Hardware Walletの画面で常に取引を確認してください。



## ダウンロードとインストール



アプリケーションをダウンロードするには、Specter Desktopの公式ウェブサイトをご覧ください。



![Page d'accueil Specter](assets/fr/01.webp)



ダウンロードページで、お使いのオペレーティングシステムに対応するバージョンを選択してください：macOS、WindowsまたはLinux。



![Téléchargement selon l'OS](assets/fr/02.webp)



ダウンロードが完了したら、お使いのオペレーティングシステムの通常の手順に従ってアプリケーションをインストールしてください。macOSの場合は、アイコンを「アプリケーション」にドラッグします。Windowsの場合は、インストーラーを実行します。Linuxの場合は、パッケージの指示に従ってください。



## 初期設定



初回起動時に、Specter Desktop は接続タイプを選択するよう求めます。Electrum Serverまたは自分のBitcoin coreノードに接続することができます。



![Choix du type de connexion](assets/fr/03.webp)



この例では、Umbrel上で動作するElectrum Serverへの接続を使用する。



詳しくは、Umbrelのチュートリアルをご覧ください：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

このオプションはBitcoin coreよりも高速な同期を提供します。お望みであれば、"Bitcoin core "を選択し、ローカル・ノードへの接続を設定することができます。以下の手順は、どちらを選択しても変わりません。



Electrum接続」を選び、「自分で入力」を選ぶと、Electrum Serverの設定ができる。



![Configuration Electrum](assets/fr/04.webp)



Electrum ServerのAddressを入力する。Umbrelの場合、Addressは`umbrel.local`、ポートは`50001`となる。Connect "をクリックして接続を確立する。



接続が完了すると、ウェルカムスクリーンが表示され、チェックリストが表示されます。ハードウェア・ウォレットを追加する必要があります。



![Écran d'accueil](assets/fr/05.webp)



## Hardware Walletの追加



左側のメニューで "Add device "をクリックし、Hardware Walletを追加します。



Specter Desktopは、数多くのハードウェアウォレットをサポートしています：Trezor、Ledger、BitBox02、Coldcard、KeepKey、Keystone、Cobo Vault、その他多数。



もっと詳しく知りたい方は、Hardware Walletチュートリアルをご覧ください。



![Sélection du type de hardware wallet](assets/fr/06.webp)



Hardware Walletを選択します。この例ではColdcard MK4を使っています。



このHardware Walletのチュートリアルをご覧ください：



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Coldcardの場合、Hardware WalletからUSB接続またはmicroSDカード経由で公開鍵をエクスポートする必要がある。



![Import des clés du Coldcard](assets/fr/07.webp)



表示される指示に従って、Coldcard からキーをエクスポートします。Hardware Wallet に名前を付けます（ここでは "MK4 Tuto"）。キーのインポートが完了したら、単一のキーでWalletを作成するか、他のハードウェアウォレットを追加してマルチシグネチャーのWalletを作成できます。



![Dispositif ajouté](assets/fr/08.webp)



## ポートフォリオの作成



Hardware Walletを追加した後、"Create single key Wallet "をクリックして単一署名Walletを作成する。



ポートフォリオに名前を付け（例：「Wallet for tuto」）、Addressタイプを選択する。取引コストを最適化するBECH32のネイティブ・アドレスを使用するには「SegWit」を選択します。



![Configuration du portefeuille](assets/fr/09.webp)



ポートフォリオが作成されると、Specter はポートフォリオの復元に必要なすべての公開情報（記述子、拡張公開鍵）を含むバックアップ PDF ファイルを保存します。このファイルには秘密鍵は含まれません。



![Sauvegarde du portefeuille](assets/fr/10.webp)



## ビットコインを受け取る



ビットコインを受け取るには、左側のメニューでWalletを選択し、「受け取り」タブをクリックします。



SpecterはQRコード付きの新しい受信Addressを自動的に生成します。



![Génération d'une adresse de réception](assets/fr/11.webp)



Addressをコピーするか、QRコードをスキャンしてください。Addressを誰かに渡す前に、必ずHardware Walletの画面で確認してください。



## 履歴と住所を見る



ビットコインを受け取ったら、「取引」タブで取引を確認できます。



![Historique des transactions](assets/fr/12.webp)



Addresses "タブでは、ポートフォリオによって生成されたすべてのアドレスを、その使用状況と関連する金額とともに表示することができます。



![Liste des adresses](assets/fr/13.webp)



## ビットコインを送る



ビットコインを送信するには、「送信」タブをクリックします。受信者のAddress、送信金額を入力し、UTXO（Coinコントロール）を手動で選択したい場合は、詳細オプションをチェックします。



![Création d'une transaction](assets/fr/14.webp)



Create Unsigned Transaction "をクリックしてトランザクションを作成します。Specter が Hardware Wallet で取引に署名するよう要求します。



![Signature de la transaction](assets/fr/15.webp)



コールドカードを使用している場合は、USB経由でサインするか、microSDカード（エアギャップ）を使用するかを選択できる。Hardware Walletの画面で、送金先のAddressと金額を注意深く確認しながら、取引を確認する。



取引が署名されると、Bitcoinネットワーク上でブロードキャストすることができる。



![Options de diffusion](assets/fr/16.webp)



取引送信」をクリックして取引を送信します。Specterは取引が送信されたことを確認し、取引タブでステータスを追跡できます。



![Diffusion de la transaction](assets/fr/17.webp)



## マルチシグネチャー・ポートフォリオの作成と使用



Specter Desktopの大きな資産の一つは、マルチシグネチャ・ポートフォリオの管理を簡素化できることです。MultisigWalletでは、トランザクションを承認するために複数の署名が必要であり、単一障害点を排除します。例えば、2-on-3構成では、支出を検証するために3つのハードウェア・ウォレットから2つの署名が必要となる。



Multisig Wallet を作成するには、まず「Add device（デバイスの追加）」を使用して、すべての 署名用ハードウェアウォレットを追加します。この例では、3つの異なるハードウェア・ウォレットを使用します：Coldcard MK4（先に追加済み）、パスポート、Ledgerです。このようにメーカーを多様化することで、単一の Supply チェーンやファームウェアへの依存を避け、セキュ リティを強化することができます。



以下はLedgerとパスポートのチュートリアルへのリンクです：



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Hardware Walletに名前を付け（例："Passport multi"）、microSDカードまたはQRコード経由でキーをインポートしてパスポートを追加します。次に "Continue "をクリックして進みます。



![Ajout du Passport](assets/fr/23.webp)



次にLedgerをUSBで接続し、Hardware Wallet上でBitcoinアプリケーションを開いて追加する。名前を付け（例："Ledger multi"）、"Get via USB"、"Continue "の順にクリックして公開鍵をインポートする。



![Ajout du Ledger](assets/fr/24.webp)



Specterに3つのハードウェアウォレットを登録したら、「Walletを追加」をクリックし、「マルチシグネチャ」オプションを選択してマルチシグネチャWalletを作成します。



![Choix du type de wallet](assets/fr/25.webp)



マルチシグネチャーのクォーラムに含めたい3つのハードウェアウォレットを選択します：MK4 Tuto、Passport multi、Ledger multiを選択します。続行」をクリックして次のステップに進みます。



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



マルチシグネチャーの構成を選択してください。Addressのタイプとして "SegWit "を選択し、最適化されたチャージをご利用ください。Required Signatures to Authorize Transactions (m of 3) "パラメーターで閾値を定義することができます。各 Hardware Wallet は対応する Multisig キーを表示する。Create Wallet "をクリックし、作成を完了する。



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



これで、マルチ署名ポートフォリオ「Multi tuto」が作成されました。Specterは、ポートフォリオDescriptorを含むバックアップPDFファイルを保存することを直ちに推奨します。バックアップPDFを保存」をクリックして、この重要なファイルをダウンロードしてください。



![Wallet multisig créé](assets/fr/28.webp)



Specterでは、QRコードまたはファイルを介して、各ハードウェアウォレットにWallet情報をエクスポートすることもできます。これにより、特定のハードウェアウォレット（ColdcardやPassportなど）はMultisigの設定を直接メモリに保存することができます。



パスポートの場合は、デバイスのロックを解除し、「アカウント管理」>「Walletを接続」>「Specter」>「Multisig」>「QRコード」と進み、Specterが生成したQRコードをスキャンします。パスポートは、Multisigの設定を確認するために、Walletから受信Addressをスキャンするよう要求します。



MK4の場合は、PCに接続してロックを解除します。次に "Save MK4 Tuto file "をクリックし、ファイルをMK4に保存します。次にHardware Walletにサインするとき、MK4はこのファイルを使ってMultisigの設定を終了します。



![Export vers les hardware wallets](assets/fr/29.webp)



ちなみに、ポートフォリオの「設定」タブ→「エクスポート」からいつでもバックアップにアクセスできます：



![Accès au backup PDF](assets/fr/30.webp)



日常的な使い方は、シンプルなWalletと同様で、通常通りgenerateでアドレスを受け取ります。ビットコインを送るには、"Send "タブで受取人のAddressと金額を入力し、"Create Unsigned Transaction "をクリックします。



![Création d'une transaction multisig](assets/fr/31.webp)



SpecterがPSBT（Partially Signed Bitcoin Transaction）を構築し、「Acquired 0 of 2 signatures」と表示する。これで、3つのハードウェア・ウォレットのうち少なくとも2つで署名する必要があります。最初のHardware Wallet（例：「MK4 Tuto」）をクリックしてColdcardで署名し、次に2つ目のHardware Wallet（例：「Passport multi」）をクリックして2つ目の署名を取得します。



![Signature de la transaction](assets/fr/32.webp)



必要な2つの署名を取得したら（Interfaceは「Acquired 2 of 2 signatures」と「Transaction is ready to send」と表示します）、「Send Transaction」をクリックしてBitcoinネットワーク上でトランザクションをブロードキャストします。



![Transaction prête à être diffusée](assets/fr/33.webp)



このマルチシグネチャ・アプローチは、企業（複数の管理者が支出を承認する必要がある）、家族（複数世代にわたる相続の保護）、または大金を管理する個人（局地的な災害に耐えるためのハードウェア・ウォレットの地理的分散）に特に適している。



### マルチシグネチャ・バックアップの重要性



**ご注意ください**：マルチシグネチャーのポートフォリオのバックアップは、単一のポートフォリオのバックアップとは根本的に異なります。Multisigポートフォリオを復元するには、リカバリーフレーズ（seedフレーズ）だけでは不十分です。マルチシグネチャー・ポートフォリオの設定情報を含む**output descriptor**（output descriptor）もバックアップする必要があります。



output descriptorには、各共同署名者の拡張公開鍵（xpubs）、署名のしきい値（この例では2対3）、使用したスクリプトのタイプ（SegWitネイティブ、ネスト、レガシー）、各Hardware Walletの派生パスといった重要なデータが含まれている。このDescriptorがなければ、たとえ3つのリカバリフレーズのうち2つがあったとしても、Walletを再構築することも、ビットコインにアクセスすることもできません。Descriptorは、あなたのソフトウェアに、あなたの資金に対応するBitcoinアドレスのgenerateへの公開鍵の結合方法を知らせます。



Multisigポートフォリオを作成する際、Specter Desktopは自動的にバックアップPDFファイルを生成します。このPDFファイルには、完全なDescriptor、各Hardware Walletのフィンガープリント、および復元に必要なすべての公開情報が含まれています。 **このファイルにはあなたの秘密鍵**は含まれていないため、それ自体でビットコインを使用することはできませんが、このファイルにアクセスすることで誰でもあなたの完全な取引履歴と残高を見ることができます。



マルチシグネチャーの設定を正しくバックアップするには、以下の手順に従ってください：ポートフォリオを作成した後、「設定」タブをクリックし、「エクスポート」から「バックアップPDFを保存」を選択します。このPDFのコピーを数部作成します。少なくとも2部は紙に印刷し、暗号化されたデジタルコピーも保管します。リカバリーフレーズと一緒にPDFのコピーを1部ずつ、地理的に離れた場所に保管してください。



リカバリーフレーズを耐火・防水メタルプレートに焼き付け、長持ちさせましょう。これらのバックアップの重要性を過小評価しないでください：もしコンピュータの`~/.specter`フォルダを紛失し、Descriptorのバックアップなしでハードウェアウォレットの1つを紛失した場合、2対3の構成であっても、すべての資金は回復不能なほど失われてしまいます。マルチシグネチャーの冗長性はHardware Walletの紛失から保護しますが、WalletのDescriptorを正しくバックアップしている場合に限ります。



## Specter Desktopの利点と限界



**メリット**：サードパーティのサーバーを使用しない完全なローカル認証による最適な機密性。高度な設定（企業、家族、個人）のためのマルチ署名の柔軟性。完全な相互運用性（USBおよびエアギャップ）による広範なHardware Walletサポート。



**制限事項**：Bitcoinの高度な概念（UTXO、記述子、派生パス）については、かなりの学習曲線がある。



## ベストプラクティス



マルウェアから身を守るため、認証の前にHardware Walletの画面で住所と金額を必ず確認すること。



PDFバックアップをシードとは別に保管してください。これらの公開ディスクリプタは、銀行の金庫室や暗号化されたクラウドに保存することができ、秘密鍵を公開することなくリカバリを容易にします。



大口資金でポートフォリオを使用する前に、tokenの金額でリカバリーをテストしてください。作成、テスト、削除、復元を行い、手順を検証してください。



Specterとファームウェアを常に最新の状態に保つ。マルチシグネチャーの連帯保証人を地理的（自宅／職場／近隣）に分散させ、局地的な災害に耐える。会計や税務申告を容易にするため、説明ラベルを使用する。



## おまけ：Bitcoinサーバーへのインストール（Umbrel、RaspiBlitz、Start9）



Umbrel、RaspiBlitz、MyNode、Start9などのBitcoinサーバーを既にお持ちの場合は、それらのアプリケーションストアから直接Specter Desktopをインストールすることができます。このアプローチには、いくつかの重要な利点があります：アプリケーションは自動的にローカルのBitcoin coreノードに設定され、ネットワーク上のどのデバイスからでもInterfaceウェブ経由で24時間365日アクセス可能で、Tor経由で安全にリモートアクセスすることもできます。Bitcoinのインフラ全体が単一の専用サーバーに集中管理されるため、管理が簡素化され、主権が強化されます。



### Umbrel App Storeからのインストール



Umbrel Interface から App Store にアクセスし、Specter Desktop を検索します。インストール」をクリックし、インストールを開始します。



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



インストールが完了したら、UmbrelでSpecter Desktopを開きます。ウェルカム画面が表示されますので、接続タイプを選択してください。Umbrel で Specter を使用している場合は、「設定の更新」をクリックして接続を設定してください。



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



リモートの Umbrel サーバーで Specter を使用する際に、ローカルコンピューターに接続された USB ハードウェアウォレットを使用できるようにするには、「リモート Specter USB 接続」を選択します。



![Configuration Remote Specter USB](assets/fr/20.webp)



表示される指示に従ってHWIブリッジを設定する。デバイスのブリッジ設定にアクセスし、ドメイン `http://umbrel.local:25441` をホワイトリストに追加する必要がある。Update "をクリックして設定を保存する。



![HWI Bridge Settings](assets/fr/21.webp)



ローカルコンピューターからもUSBハードウェアウォレットを使用したい場合は、Specter Desktopアプリケーションをコンピューターにダウンロードし、「はい、リモートでSpecterを実行します」に設定してください。保存」をクリックして設定を確定します。



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## 結論



Specter Desktopは、Bitcoinの高度な設定を民主化し、主権や機密性を犠牲にすることなくマルチシグネチャにアクセスできるようにします。多額の資金を管理するユーザーにとっては、組織的な慣行を個人でも導入可能なソリューションに変えます。



このアプリケーションは、インフラと学習への初期投資が必要ですが、完全な主権を提供します：検証インフラの制御、キーの物理的なOwnership、第三者の監視から解放されたトランザクション。個人で貯蓄を守る場合でも、家族で複数世代に渡る貸金庫を作る場合でも、企業でキャッシュフローを管理する場合でも、Specter Desktopは最大限のセキュリティと絶対的な主権を両立させるためのリファレンスツールです。



## リソース



### 公式文書




- [妖怪デスクトップ公式サイト](https://specter.solutions/desktop/)
- [GitHubソースコード](https://github.com/cryptoadvance/specter-desktop)
- [完全ドキュメント](https://docs.specter.solutions/)



### コミュニティとサポート




- [テレグラム妖怪ウォッチコミュニティグループ](https://t.me/spectersupport)
- [Redditディスカッションフォーラム](https://reddit.com/r/specterdesktop/)
- [GitHubバグレポート](https://github.com/cryptoadvance/specter-desktop/issues)