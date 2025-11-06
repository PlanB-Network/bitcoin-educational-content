---
name: Payjoin - Sparrow Wallet
description: Sparrow WalletでPayjoin取引を行う方法は？
---
![tutorial cover image sparrow payjoin](assets/cover.webp)

_**注意:** Samourai Walletの創設者が逮捕され、4月24日にサーバーが押収された後、Samourai WalletでのPayjoins Stowawayは、両方のユーザーが各自のDojoに接続していることを条件に、関係者間でPSBTを手動で交換することでのみ機能します。Sparrowの場合、BIP78経由のPayjoinsは依然として機能します。ただし、これらのツールは今後数週間で再開される可能性があります。その間、payjoinsの理論的な機能を理解するためにこの記事を読むことができます。_

_この問題の進展と関連ツールに関する進展を注意深く監視しています。新しい情報が利用可能になり次第、このチュートリアルを更新することをお約束します。_

_このチュートリアルは、教育および情報提供のみを目的としています。これらのツールを犯罪目的で使用することを支持または奨励するものではありません。各ユーザーは、自分の法管轄区域の法律を遵守する責任があります。_

---

> *"ブロックチェーンのスパイに、彼らが知っていると思っていることを全て見直させる。"*

Payjoinは、支払い受取人と協力して支出時のユーザープライバシーを強化する特定のBitcoin取引構造です。PayJoinの設定と自動化を容易にするいくつかの実装があります。これらの実装の中で最もよく知られているのは、[Samourai Wallet](https://samouraiwallet.com/stowaway)チームによって開発されたStowawayです。このチュートリアルは、Sparrow Walletソフトウェアを使用してStowaway Payjoin取引を行うプロセスを案内することを目的としています。

## Stowawayはどのように機能するのか？

前述のように、Samourai Walletは"Stowaway"と呼ばれるPayJoinツールを提供しています。これはPC上のSparrow WalletソフトウェアまたはAndroid上のSamourai Walletアプリケーションを通じてアクセス可能です。Payjoinを実行するには、受取人（協力者としても機能する）がStowawayと互換性のあるソフトウェア、つまりSparrowまたはSamourai Walletを使用する必要があります。これら二つのソフトウェアは相互運用可能であり、SparrowウォレットとSamouraiウォレット間、またその逆でもStowaway取引を可能にします。

Stowawayは、Samouraiが"Cahoots"と呼ぶ取引のカテゴリーに依存しています。Cahootは、オフチェーン情報交換を必要とする複数のユーザー間の協力的取引です。現在、Samouraiは二つのCahootsツールを提供しています：Stowaway（Payjoins）とStonewallX2（これについては将来の記事で探求します）。

Cahoots取引は、ユーザー間で部分的に署名された取引を交換することを含みます。このプロセスは、特に遠隔で行う場合には長くて煩雑になることがあります。しかし、協力者が物理的に近い場合には、手動で別のユーザーと行うことが便利です。実際には、連続してスキャンするための5つのQRコードを手動で交換することを含みます。

遠隔で行う場合、このプロセスは複雑すぎます。この問題に対処するために、SamouraiはTorに基づいた暗号化通信プロトコルである"Soroban"を開発しました。Sorobanを使用すると、Payjoinに必要な交換がユーザーフレンドリーなインターフェースの背後で自動化されます。これが、この記事で探求する第二の方法です。

これらの暗号化された交換には、Cahoots参加者間の接続と認証の確立が必要です。Soroban通信は、ユーザーのPaynymsに依存しています。Paynymsに馴染みがない場合は、この記事を参照してください：[BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
簡単に言うと、Paynymはウォレットにリンクされたユニークな識別子であり、暗号化されたメッセージングを含む様々な機能を可能にします。Paynymは識別子とロボットを表すイラストの形で提示されます。これがTestnet上の私の例です：![Paynym Sparrow](assets/en/1.webp)

**要約：**
- *Payjoin* = 協力的取引の特定の構造；
- *Stowaway* = SamouraiとSparrow Walletで利用可能なPayjoin実装；
- *Cahoots* = SamouraiがPayjoin Stowawayを含むすべての協力的取引タイプに与えた名前；
- *Soroban* = Tor上に確立された暗号化通信プロトコルで、Cahoots取引の文脈で他のユーザーとの協力を可能にします。
- *Paynym* = Cahoots取引を行うために、Soroban上で別のユーザーと通信するためのウォレットのユニークな識別子。
[**-> Payjoin取引とその有用性についてもっと学ぶ**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Paynyms間で接続を確立する方法は？

リモートでCahoots取引、具体的にはSamouraiやSparrowを介したPayJoin（Stowaway）を実行するには、協力する予定のユーザーのPaynymを「フォロー」する必要があります。Stowawayの場合、これはビットコインを送りたい人をフォローすることを意味します。

**この接続を確立する手順は以下の通りです：**

まず、受取人のPaynym識別子を入手する必要があります。これは、受取人のニックネームまたは支払いコードを使用して行うことができます。これを行うには、受取人のSparrowウォレットから`Tools`タブを選択し、`Show PayNym`をクリックします。
![Show Paynym](assets/en/2.webp)
![Paynym Sparrow](assets/en/1.webp)
あなたの側では、Sparrow Walletを開き、同じ`Show PayNym`メニューにアクセスします。Paynymを初めて使用する場合は、`Retrieve PayNym`をクリックして識別子を取得する必要があります。
![Retrieve paynym](assets/en/3.webp)
次に、`Find Contact`ボックスに協力者のPaynym識別子（ニックネームの`+...`または支払いコードの`PM...`）を入力し、`Add Contact`ボタンをクリックします。
![add contact](assets/en/4.webp)
その後、ソフトウェアは`Link Contact`ボタンを提供します。このチュートリアルでは、このボタンをクリックする必要はありません。このステップは、BIP47の文脈で示されたPaynymに対して支払いを行う予定がある場合にのみ必要ですが、このチュートリアルとは関係ありません。

受取人のPaynymがあなたのPaynymによってフォローされたら、この操作を逆方向で繰り返して、受取人もあなたをフォローするようにします。そうすれば、Payjoinを実行できます。

## Sparrow WalletでPayjoinを実行する方法は？
これらのいくつかの予備的なステップを完了したら、ついにPayjoin取引を実行する準備が整いました！これを行うには、私たちのビデオチュートリアルに従ってください：
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**外部リソース：**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.