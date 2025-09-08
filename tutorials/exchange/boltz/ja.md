---
name: ボルツ
description: コントロールを維持したまま、異なるBitcoinレイヤーを入れ替える。
---


![cover](assets/cover.webp)



2009年の導入以来、Bitcoinのピアツーピア電子キャッシュシステムは飛躍的な成長を遂げ、Lightning Networkをはじめとする私たちの日常生活で即座に利用できるシステムへと進化した。



しかし、Bitcoinプロトコルのレイヤー間には、流動的な相互運用性という大きな問題が残っていた。Bitcoinの可能性を最大限に活用するためには、プロトコルの異なるレイヤー間のトランザクションを可能にするソリューションを見つけることが不可欠だった。この必要性から2019年、複数のBitcoinレイヤーをつなぐブリッジ、Boltzが誕生した。



## ボルツとは？



[Boltz](https://boltz.Exchange)は、Bitcoinプロトコルの異なるレイヤー間で取引を行いたい人にとって理想的な非保護プラットフォームである：




- on chain**：Bitcoinのメイン・チェーンでは、平均10分ごとに取引が確認されるため、取引手数料が高くなりがちで、必ずしもユーザーのニーズを満たしていない；
- Lightning Network**：Bitcoinのオーバーレイを使用することで、低手数料で即時決済が可能となり、Bitcoinを日々の決済に使用することができる；
- Liquid Network**：ブロックストリームが作成したBitcoinのオーバーレイで、高速のConfidential Transactionsと他のBitcoinベースの金融商品の使用を可能にする；
- RootStock**：Bitcoinプロトコルに基づくスマートコントラクトを開発するためのソリューション。



![layers](assets/fr/01.webp)



これらの異なるレイヤー間の相互運用性は、Bitcoinエコシステムが提供するすべてのものをフルに活用するために必要な柔軟性をユーザーに与えるため、非常に重要である。



Boltzはアトミックスワップを採用している。この技術により、ビットコインを2つのレイヤー間で（例えばExchangeのBTCオンチェーンからLightningのBTCへ）、信頼の必要も仲介者の必要もなく直接交換することができる。このような交換は2つの結果しか生まないため、「アトミック」と呼ばれる：




- Exchangeが成功し、2人の参加者がBTCを交換したことになる；
- Exchangeは失敗し、参加者全員が元のBTCを持って退場する。



Exchangeが成功しても失敗しても、どちらの当事者も相手の資金を盗むことはできない。



アトミックExchangeはスマート・コントラクト[HTLC](https://planb.network/resources/glossary/htlc)(*ハッシュド・タイムロックContract*)と連動する。このタイプのContractでは、金額は双方向チャネルで「ロック」され、時間制限が導入されるため、一定時間内に取引が完了しない場合、残高は預金者に戻る。これはBoltzプラットフォームが採用している仕組みである。



## ボルツとの最初の交流



Boltzは、お客様の個人情報を必要としない非預託型ウェブプラットフォームです。Boltzは最小主義で流動的なInterfaceを採用しており、1分以内に取引を開始することができます。



![boltz](assets/fr/02.webp)



プラットフォーム上では、Bitcoinエコシステムの異なるレイヤー間でアトミックなやり取りを行うことができる。



![home](assets/fr/03.webp)



Boltzを通じて取引できるサトシ（Bitcoinの最小単位）の最小数と最大数が表示されます。これにはネットワーク手数料とBoltzが課す0.1％～0.5％のパーセンテージが含まれます。



![fees](assets/fr/04.webp)



次に、アトミックExchangeを作りたいLayerを選択し、ビットコインを受け取りたいLayerを選択する。



![couches](assets/fr/05.webp)



このチュートリアルでは、メインのLayerからLightning NetworkまでのアトミックExchangeに焦点を当てる。



オプションを選択することで、ベースユニットを交換用に設定できます：




- BTC ；
- Sats。



![unités](assets/fr/06.webp)



基本的な設定が完了したら、アトミックExchangeの金額を挿入し、同等の金額分のライトニングInvoiceを作成するか、単にLNURLを挿入します。



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



念のため、原子Exchangeのパラメータを確認し、Exchangeにリンクされたバックアップキーをエクスポートしてください。



Settings**アイコンで、バックアップ・キーをダウンロードし、ファイルを適切に保存します。



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



このファイルには、原子交換に関連するポートフォリオの12のキーワードが含まれています。



その後、**原子Exchange**を作成するボタンをクリックし、表示された金額の支払いを進めてください。



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

お支払いが完了し確認されると、自動的にライトニングWalletに相当する金額が支払われます。



払い戻し**メニューで、アトミックExchangeの履歴を検索し、払い戻しを希望するExchangeを特定します。また、他の機器で交換した履歴をインポートすることもできます。例えば、これらの交換に関連するバックアップ・キー・ファイルを使用します。



![refund](assets/fr/11.webp)



履歴**メニューでは、**バックアップ**ボタンをクリックすることで、レスキューキーに関連する交換のより詳細な履歴をダウンロードすることができます。



![backup](assets/fr/12.webp)



⚠️ このファイルには、あなたの取引に関連するすべての情報と、これらの取引にリンクされたバックアップ・キーが含まれていますので、このファイルも漏らさないでください。



Boltzは、Torネットワーク上の`.onion`リンク経由でアクセスすることにより、高い機密性を提供します。ブラウザでTorブラウジングを有効にした後、**Onion**メニューを選択することで、原子交換を完全に匿名化できます。



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Bitcoinエコシステムの異なるレイヤー間の相互運用性を可能にするユニークなExchangeプラットフォームであるBoltzについては、もうお馴染みだろう。