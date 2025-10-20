---
name: スタッシュペイ
description: ミニマリストのためのBitcoin Wallet
---

![cover](assets/cover.webp)



ユーザー・エクスペリエンスは、世界中でBitcoinソリューションが採用される重要な要因である。多くのウォレットやExchangeプラットフォームにとって、スムーズでシンプル、かつ技術的に邪魔されない体験を提供することが優先事項となっている。この点で、StashPayはその最小限のアプローチで際立っており、同時にLightning Networkのパワーを実証しています。



このチュートリアルでは、このポートフォリオがどのように機能するのか、また中小企業や個人事業主にどのように最適なのかをご紹介します。



## StashPayを始める



StashPayはLightningセルフカストーディアルWalletで、そのミニマリストでユーザー中心のユーザーエクスペリエンスで知られています。  このWalletを使えば、専門的な知識は一切必要なく、初めてのサトシを受け取ったり送ったりすることができます。



StashPayはReact Nativeで開発されたオープンソースのプロジェクトで、Bitcoinプロトコルのメインチェーン上の取引であっても取引手数料が高いという問題を解決することを目指している。ウェブサイト](https://stashpay.me/)にあるダウンロードリンクから、AndroidとiOSプラットフォームのモバイルアプリとして利用できる。



![introduce](assets/fr/01.webp)



アンドロイド用アプリケーションはグーグルプレイストアでは入手できないので、ウェブサイトからダウンロードすることが重要である。


ダウンロードが完了したら、Android携帯にアプリケーションをインストールできるように、必要な許可を与えてください。



アプリケーションをインストールすると、StashPay を初めて開いたときに初期 Bitcoin Wallet が作成されます。お取引の前に、このWalletのバックアップを取ることをお勧めします。以下に、リカバリフレーズが適切にバックアップされていることを確認するためのガイドラインを示します。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

設定」アイコンをクリックしてStashPayの設定にアクセスし、**バックアップを作成**オプションをクリックします。次に、回復フレーズの表示を許可します。お使いの携帯電話にインストールされている他の不正アプリケーションからアクセスできる可能性があるため、回復フレーズを携帯電話のクリップボードにコピーしないでください。



![backup](assets/fr/02.webp)



また、**Recover Wallet**オプションをクリックし、12または24のリカバリーワードを挿入することで、すでに使用しているBitcoin Walletを取り出すこともできます。



### StashPayで最初のサトシを受け取る



ホーム画面で**Receive**ボタンをクリックし、赤で指定された金額以上の金額を設定します。この例では、StashPay Walletで0.11米ドル未満を受け取ることはできません。



![receive](assets/fr/03.webp)



金額を決めたら、**Invoiceを作成**ボタンをクリックし、Invoiceをスキャンまたはコピーして、サトシの送り主に送ることができます。



![receive_sats](assets/fr/04.webp)



ホームページの「時計」アイコンをクリックすると、取引履歴を見ることができます。



![network_fee](assets/fr/05.webp)



サトシを受け取るには、ネットワーク手数料を支払わなければならないことにお気づきだろう。これらの手数料は、これから受け取るサトシから差し引かれます。これは、StashPayがBreez Development KitをベースとしたWalletであるためです。キットのライトニングノードフリー実装でサトシを受け取るために、Breezは顧客（私たちの場合はStashPay）に`0.25% + 40サトシ`を請求します。詳しくはMisty Breezチュートリアルをご覧ください。



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### StashPayでビットコインを送る



StashPayでのビットコインの送信は、最小限のInterfaceのおかげでかなり直感的です。ホーム画面で**送信**ボタンをクリックします。QRコードをスキャンするか、サトシを送りたいAddressを貼り付けます。StashPayは、ビットコインを送りたいBitcoinプロトコルチェーンを自動的に検出します。



![send](assets/fr/06.webp)



StashPayはBreez Development KitをベースとしたWalletであるため、メインチェーン上でビットコインを低コストで送信できるという興味深い利点があります。Breezは、Bitcoinプロトコルの異なるチェーン間のトランザクションを実行するためにBoltzサービスを使用しており、開発キットを実装する顧客は、アプリケーションで直接このサービスの恩恵を受けることができます。



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

しかし、Breez SDKは、メインチェーン上のAddressにビットコインを送ることができる最低額を課しています。



![onchain](assets/fr/07.webp)



受信者のライトニングAddressを使用してビットコインを送信することもできます。取引の詳細を確認し、**送信**ボタンをクリックして確定します。



![confirm](assets/fr/08.webp)



## より多くの構成



StashPayの設定では、Walletの使用をカスタマイズするための設定を調整できます。



StashPayを使用すると、選択した現地通貨に基づいてExchangeサトシを支払うことができます。Currencies**オプションをクリックし、StashPayが提供する113の通貨リストからご希望の通貨を検索します。



![currencies](assets/fr/09.webp)



Receive options**メニューには、StashPayでビットコインを受け取るためのすべての設定があります。例えば、**Choose Lightning or Onchain**を選択すると、Walletがメインチェーンからビットコインを受け取れるようになります。



![receive-onchain](assets/fr/10.webp)



OnChainアドレスのスキャン**オプションを使用すると、さまざまなアドレスにリンクされているすべてのUTXO（まだ使用していないビットコイン）をチェックすることにより、Walletの残高をリフレッシュすることができます。



![rescan](assets/fr/11.webp)



Export log** メニューには、Bitcoin プロトコルチェーン間のトランザクションとアトミック交換に関す る Breez と Boltz のインフラストラクチャーのアクションがすべてリストアップされます。



![export](assets/fr/12.webp)



StashPayのミニマリストBitcoin Walletを使いこなしたところです。このチュートリアルが役に立ったなら、Bitcoinを始めて最初のビットコインを獲得する方法のチュートリアルをお勧めします。



https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f