---
name: Minibits Wallet
description: ミニビットWallet用ガイド
---

![cover](assets/cover.webp)


このチュートリアルでは、Minibits Walletがecashを使用できるように設定する手順を説明します。Bitcoinと連動する、プライバシー重視の強力な決済テクノロジーです。Minibitsは、ecashとLightningのWalletであり、即座に、安価に、プライベートな価値の移動を可能にするため、プライバシーが重要な日常的な取引に最適です。


Minibitsに飛び込む前に、ecashが何であり、何でないかを明確に理解しておこう。多くの人がecashをBitcoinやBlockchainテクノロジーと混同しているが、これらは根本的に異なる概念である。


EcashはBitcoinではありません。BitcoinのWalletを置き換えるものではなく、むしろ補完するものです。EcashはBlockchainではないし、公的なLedgerには存在しない。興味深いことに、エコキャッシュは新しい技術ではない。実際、1980年代から1990年代にかけて開発されたコンセプトで、ワールドワイド・ウェブよりも先行している。


ecashの特徴：非常にプライベートであり（取引履歴が残らない）、ピアツーピアであり（仲介者を介さない直接送金）、デジタル無記名証書として機能する（所有すれば管理できる）。重要な利点は、エコキャッシュをオフラインで使用できることである。また、Bitcoinの完璧な補完技術であり、Bitcoinが決済Layerとして機能する間、少額で頻繁な取引を処理する。


このMinibitsの設定は「custodial solution（預託型ソリューション）」であることに注意してください。これは、お客様が資金管理をMint運営者に委託することを意味します。


このプロジェクトには、この重要な免責事項が表示されている：


- このWalletは研究目的にのみ使用すること。
- Walletはベータ版であり、機能は不完全で、既知のバグも未知のバグもある。
- 多額の現金を使用しないでください。
- Walletに保管されたEcashは造幣局が発行する。
- 
- Walletが実装するカシューのプロトコルは、まだ広範なレビューやテストを受けていない。


ミニビットは貯蓄口座ではなく、日常のWalletのように扱い、決して大きな価値をここに保管しないこと。


## 1️⃣ Wallet のセットアップ


まず、[Minibitsウェブサイト](https://www.minibits.cash/)にアクセスし、すべての主要プラットフォーム用のダウンロードオプションをご覧ください。iOSユーザーは[App Store](https://testflight.apple.com/join/defJQgTD)からダウンロードでき、EUのiOSユーザーは[Freedom Store](https://freedomstore.io/)からインストールする追加オプションがあります。Androidユーザーは[Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet)からアプリを入手するか、[GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases)ページから直接APKファイルをダウンロードできます。


Minibitsをインストールすると、基本的なコンセプトを説明する画面が表示されます。これらの初期ステップを完了すると、次のいずれかを選択するよう促されます：


- 新規ユーザーには「Got it, take me to Wallet」。
- バックアップから復元する場合は、`失われたWallet`を復元する。


![image](assets/en/01.webp)

初期設定が完了すると、ホーム画面が表示されます。ホーム画面には、いくつかの重要な Elements があります。画面上部のプロフィールアイコンは、あなたのMinibits Wallet Addressにアクセスし、`一括受信`オプションを選択できるプロフィールページに移動します。画面中央には使用可能なMintが表示され、デフォルトではMinibits mintが選択されています。その下のアクション列では、ecashやlightningの送信、QRコードのスキャン、支払いの受け取りが可能です。最後に、下のナビゲーションバーには、ホーム画面、取引履歴、連絡先、設定へのショートカットがあります。


![image](assets/en/02.webp)


## 2️⃣ ミントを管理する


デフォルトでは、アプリを起動すると Minibits ミントが有効になります。しかし、ecash の強みの一つは、分散化とセキュリティを高めるために複数のミントを使用できることです。別のミントを追加するには、`Settings` に移動し、次に `Manage mints` を選択し、最後に `Add mint` をタップします。


[Bitcoinmints.com](ビットコインミントドットコム)は、利用可能なミントの包括的なリストをユーザー評価と共に提供し、評判の良いオプションを選択するのに役立ちます。複数のミントを使用することで、リスクを軽減できます。1つのミントに問題が発生しても、他のミントの資金はアクセス可能なままです。


![image](assets/en/04.webp)


## 3️⃣ バックアップの作成


バックアップは、間違いなくセットアッププロセス全体の中で最も重要なステップです。バックアップオプションにアクセスするには、`Settings`-> `Backup` に移動してください：

1.seedフレーズには12個の単語が含まれています。この seed フレーズは、お客様が追加したすべてのミントのすべてのエコッシュに対するマスターキーです。物理的な媒体 (紙または金属) に書き留めて、複数の場所に安全に保管してください。seed フレーズは絶対にデジタルに保存しないでください。Wallet を保護するためのベストプラクティスについては、こちらの [チュートリアル](https://planb.network/en/tutorials/Wallet/backup/backup-Mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) をご覧ください。

2.長いバックアップ文字列を含む`Wallet backup`。


**注意**：このバックアップを使用してWalletをリカバリーする場合、seedのフレーズが必要です。


![image](assets/en/05.webp)


## 4️⃣ クリエイト・ミニビット Wallet Address


次に下部の「連絡先」に移動し、「変更」→「Wallet Addressを変更」をタップして、専用の「Minibits Wallet Address」をカスタマイズします。ご希望のAddressを入力し、空き状況を確認してください。


![image](assets/en/07.webp)


Addressを設定した後、このプロジェクトを支援するための少額の`寄付`を求めるプロンプトが表示されます。これは任意ですが、サービスを定期的に使用する予定がある場合は検討することを強くお勧めします。Minibitsのようなオープンソースプロジェクトは、開発とメンテナンスを継続するためにコミュニティのサポートに依存しています。少額の寄付でも、プロジェクトの存続に役立ちます。


![image](assets/en/08.webp)


## 5️⃣ Nostrセットアップ


Nostrでフォローしている人にチップを渡したい場合は、「連絡先」から「公開」を選択し、「npubキーを追加」してください。これにより、あなたのMinibits WalletがNostrソーシャルネットワークに接続され、シームレスなチップが可能になります。


また、`Settings`から`Privacy`を選択し、自分のNostr Addressとキーをインポートすることで、`Use your own profile`というオプションもあります。ただし、これを行うと、Walletがminibits.cash NostrおよびLNURL Addressサーバーと通信できなくなり、ザップや支払いを受け取るためのライトニングAddressの機能が使えなくなるので注意してください。


![image](assets/en/09.webp)


## 6️⃣ 資金を受け取る


最初に資金を受け取るには、ライトニングInvoiceを使ってWalletに資金を追加する必要があります。このプロセスは簡単です： `Topup` をタップし、追加したい `Amount` を入力し、オプションで `Memo` を追加し、`Create Invoice` をタップします。その後、別のライトニングWalletを使用してこのInvoiceを支払う必要があります。これにより、Bitcoinのライトニング支払いがMinibits Wallet内のecashトークンに変換されます。


![image](assets/en/10.webp)


## 7️⃣ 送金する


Walletの資金調達が完了したら、2つの異なる方法で資金を送金することができます。


### 電子マネーを送る


最初のオプションは、ecash を直接送ることです。送信`」をタップし、「ecashを送信`」を選択し、「金額`」を入力し、「tokenを作成`」をタップする。generateにQRコードが作成されるので、受信者と共有するか、受信者のデバイスで直接スキャンさせることができる。受け取った人は、Blockchain の手数料や確認の遅れなしに、ほぼ即座に Wallet にトークンが表示されるのを確認できます。


![image](assets/en/11.webp)


### Lightningで支払う


2つ目のオプションはLightningで支払う方法です。送信」をタップし、「Lightningで支払う」を選択します。Nostrの`連絡先`（npubに接続している場合）から選択するか、`貼り付け`または`スキャン`オプションを使ってLightningのAddress、Invoice、またはLNURLの支払いコードを入力/貼り付けします。受取人を確認した後、支払い金額を入力するプロンプトが表示されますので、必要に応じてメモを追加し、`Confirm`の後に`Pay now`をタップしてLightning決済を完了します。


![image](assets/en/12.webp)


## 8️ ↪NWC コネクションの作成


Minibitsのもう一つの強力な機能は、「Nostr Wallet Connect (NWC)`」接続を作成する機能であり、これにより他のアプリケーションは秘密鍵を公開することなくWalletからの支払いを要求することができる。


設定するには、`Settings`から`Nostr Wallet Connect`を選択し、`Add connection`をタップします。アプリケーションと関連するユーザーアカウントの両方を識別できるように、接続に分かりやすい名前を付けてください。この接続で使用できる金額をコントロールするために、1日の上限を設定し、`Save`をタップして設定を完了します。


この機能は、特にNostr Clientsのようなサービスで、各取引を手動で承認することなく自動チップを有効にしたい場合に便利です。


![image](assets/en/12.webp)


## 結論


Minibitsは、Bitcoinの保有を補完するプライバシー重視の支払いを提供し、ecashの世界へのアクセスしやすい入口を提供します。常に適切なバックアップを維持し、冗長性のために複数のミントを使用することを検討し、適切な量だけをこの保管ソリューションに保管することを忘れないでください。


その他のリソースについては、MinibitsのGitHubリポジトリ、公式ウェブサイト、およびコミュニティが開発について活発に議論し、問題のトラブルシューティングを行うTelegramチャンネルをチェックしてほしい。


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [ウェブサイト](https://www.minibits.cash/)
- [テレグラム](https://t.me/MinibitsWallet)


ecashのエコシステムはまだ発展途上だが、Minibitsのようなツールによって、この強力なプライバシー技術が日常的に利用できるようになってきている。