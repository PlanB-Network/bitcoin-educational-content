---
name: Misty Breez
description: 弓のないライトニングWallet。
---

![misty-breez-cover](assets/cover.webp)



Misty Breezは、Breezが同社のソフトウェア開発キットとBlockStreamが開発した**Liquid**ネットワークに基づいて開発したライトニング自己保持型Walletです。


Bitcoinのネットワーク間移動において、**GAME CHANGER**となる可能性を秘めている。


このチュートリアルでは、このポートフォリオがどのように機能するかを説明し、完全な概要をお伝えします。



## Misty Breezの仕組みは？



Misty Breez は Lightning ノードをバックエンドとしない実装です。Breez SDK と Liquid をベースに開発されています。



LiquidはBitcoinネットワークと並列のLayerであり、スピードと取引コストの大幅な改善を提供します。このLayerにより、ミスティ・ブリーズはライトニング・ノードを廃止し、代わりにLiquid NetworkとLightning Network間の相互運用性を確保するため、**Boltz**のようなサードパーティのExchangeサービスを利用することができる。急がないで、この話はまた後で。



とりあえず、ミスティ・ブリーズWalletから冒険を始めよう。



## Misty Breezを使い始める



Misty Breezモバイルアプリは、Google Playストア（Androidの場合）やApple Store（iOSの場合）などの公式ダウンロードプラットフォームで入手できます。また、[Misty Breez]公式ウェブサイト(https://breez.technology/misty/)から正しいアプリにリダイレクトすることもできます。



⚠️ ミスティ・ブリーズとブリーズWalletを間違えないように。



⚠️ **重要です**：**重要**：ビットコインの安全性を確保するために、公式プラットフォームからアプリケーションをダウンロードすることが不可欠です。



![download-misty-breez](assets/fr/01.webp)



このチュートリアルでは、Androidデバイスから始めます。とはいえ、このセクションで詳述する各ステップと特定の機能はiOSにも適用されます。



インストールすると、Misty Breezは新しいWalletを作成するか、リカバリーワードを持っている古いLightning Walletをリストアするかを選択できます。


このチュートリアルでは、新しいポートフォリオを作成することにします。



⚠️Misty Breezは現在開発段階ですので、無理のない金額から始めることをお勧めします。



![create-wallet](assets/fr/02.webp)


### リカバリーの言葉を保存する：


新しいポートフォリオを作るときに最初にすべきことのひとつは、12個のリカバリーワードをバックアップすることだ。


ここでは、バックアップフレーズをバックアップする方法について、いくつかのヒントを紹介します。



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

フレーズをバックアップするには、**Preferences > Security** メニューを選択し、**Check your Backup Phrase** オプションを選択します。



![backup](assets/fr/03.webp)


さらにセキュリティを高めるために、Walletへのアクセスを認証するPINコード**を作成することもできます。**




Misty Breezでご利用可能な多数の通貨から、お住まいの地域の通貨をお探しください。**Preferences > Fiat Currencies** メニューから通貨を設定し、必要な通貨を選択してください。



![devises](assets/fr/04.webp)



### 初めての取引


すでにブリーズのポートフォリオをご存知の方なら、ミスティ・ブリーズの直感的なInterfaceにまったく気後れすることはないだろう。



Interfaceの**残高**メニューで、**受け取り**オプションをクリックすると、Walletでビットコインを受け取るための請求書が作成されます。



⚠️ Misty Breezは、Lightning Addressの権利を得るために、携帯電話の設定でアプリケーションの通知を有効にするよう求めます。



ミスティ・ブリーズを使えば、あなたは：




- Lightning Networkに**100サトシ**から**25,000,000サトシ**までのビットコインをお受け取りください。
- Bitcoinメインネットワークでビットコインを**25,000サトシ**から受け取る。



![transactions](assets/fr/05.webp)



ミスティ・ブリーズの魔法はここから始まる。


Breez WalletがLightningノードを提供し、支払いチャネルの開閉にかかる費用を自分で負担するよう求めるのとは異なり、Misty Breezはあなたに何も求めません。前述したように、Misty BreezはLightningノードを前提に動いているわけでもない。



その舞台裏を詳しく見てみよう。



現実には、あなたはMisty Breezポートフォリオに関連するLiquidポートフォリオを所有しています。論理的には、あなたはL-BTC（Liquid Bitcoin）を、Lightning Networkとの相互運用を可能にするサードパーティの海底サトシコンバージョンサービスに関連した固定レートで取り扱うことになります。



あなたのMisty Breez Walletで支払いを受け取ると、送金者はあなたにサトシを送り、そのサトシはBoltz（現在Misty Breezが使用）のような変換サービスを経て、あなたのMisty Breez Wallet（関連するLiquid Wallet）で受け取れるL-BTCに変換されます。


舞台裏のプロセスを簡略図にしてみた。



![lnswap-in](assets/fr/06.webp)



**Balance**メニューの**Interface**をクリックし、**Send**オプションをクリックしてライトニング**Invoice**を支払う。


Lightning Invoice、または受取人のLightning Addressを挿入するか、InvoiceのQRコードをスキャンするだけでお支払いが完了します。



![send-bitcoins](assets/fr/07.webp)



裏側では、あなたのMisty Breez Walletに関連するLiquid Walletを有効にして、Boltz経由でL-BTC相当額をサトシに変換し、このサトシを受取人のLightning Wallet（Lightning Networkに存在）に送金します。



![send-bitcoin-bts](assets/fr/08.webp)



Misty Breezのインフラストラクチャのこの機能により、Misty Breezがオフラインの場合でも、ユーザは取引を行うことができます。



経験豊富な方には、**Preferences > Developers** というメニューもあります：




- Breez Software Development Kit のバージョン。
- Misty Breez Walletの公開鍵。
- 借り手。一次公開鍵に由来する一意の識別子。
- ポートフォリオの残高
- チップLiquid、少額のL-BTC送金用。
- 少量のBitcoinを送るためのBitcoinチップ。



また、Liquid Networkとの同期、キーのバックアップ、アクティビティログの共有、Liquid Networkの再スキャン選択など、特定のアクションを実行することもできます。



![dev-mode](assets/fr/09.webp)


おめでとうございます！これでMisty BreezのポートフォリオとBitcoinネットワーク間取引への貢献について十分ご理解いただけたと思います。このチュートリアルがお役に立ちましたら、Greenの親指をお付けください。ご連絡をお待ちしております。



さらに進んで、ミスティ・ブリーズと同様の働きをするAqua Walletのチュートリアルをご覧になることをお勧めします：



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125