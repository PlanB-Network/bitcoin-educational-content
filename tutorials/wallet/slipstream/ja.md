---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![カバー](assets/cover.webp)

通常、トランザクションに署名すると、それはネットワーク上のすべてのBitcoinノードへ自動的にブロードキャストされます。その後、マイニングされるのを待ちます。

しかし、ブロックに含まれていない間は、あなたの秘密鍵を入手した攻撃者がそのトランザクションを置き換え、資金を盗むことができます。これは、ColdCardハードウェアウォレットを使用している場合に典型的に起こり得ます。

マイニング企業MARAのSlipstreamツールを使うと、トランザクションをネットワークへブロードキャストせずに済みます。トランザクションはマイナーへ直接（かつそのマイナーにだけ）送信され、非公開に保たれるため、ネットワーク上に公開されることを避けられます。トランザクションがマイニングされるまでの時間は長くなる可能性がありますが、置き換え攻撃から保護されます。

以下では、[Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)のユーザー、および[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)ウォレットのユーザーが、[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)ページを通じてマイナーMARAのSlipstreamツールを使用するためのチュートリアルを紹介します。

⚠️ **警告**: このツールは、主にLianaウォレット、miniscriptウォレット、一部の種類のマルチシグなど、特定のプロファイルだけを対象としています。Wizardsardineは、資金がすでに盗難の差し迫った重大リスクにさらされているウォレットでこのツールを使用しないよう、**明示的に勧告しています**。たとえば、乱数生成器の脆弱性の影響を受けたColdCardデバイスでリカバリーフレーズが生成されたウォレットが該当します。その状況では、攻撃者との競争は秒単位の問題であり、単一のマイナーに送られたトランザクションは、通常どおりブロードキャストされたトランザクションよりも承認までにはるかに長い時間がかかります。これに当てはまる場合は、まず専用チュートリアルを読んでください。

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Lianaユーザー向け

Lianaは、[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)ページの提供元であるWizardsardineによって保守されているため、手順は直接的です。ブロードキャストする代わりに、署名済みPSBTファイルをエクスポートするだけです。

*前提条件: Lianaウォレットに資金があること。*

### ステップ1: Lianaでトランザクションを作成する

通常どおり、送信先アドレス、説明、金額（ここではウォレットで利用可能な最大額）を追加してトランザクションを作成します。

手数料率を設定するには:

- 左下の「Coins selection」の下にある小さなボックスをクリックして、使用したいコインを選択します。
- 次に手数料率を入力します。このページで説明されているように、推奨レートよりもかなり高い手数料を設定することを忘れないでください: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

最後に、「Next」をクリックします。

![Lianaでトランザクションを作成する](assets/fr/01.webp)

### ステップ2: トランザクションの詳細を確認する

「Sign」をクリックする前に、トランザクションの詳細を確認してください。特に:

- 送信額。
- トランザクション手数料に割り当てられるサトシ数。
- そして何より、資金の送信先アドレス（"address poisoning"攻撃を避けるため、アドレスの先頭5/6文字、末尾5/6文字、そしてアドレス中央の5/6文字を確認することを忘れないでください）。

![トランザクションの詳細を確認する](assets/fr/02.webp)

### ステップ3: 署名に使うウォレットを選択する

次に、トランザクションへの署名に必要なソフトウェアウォレットおよび/またはハードウェアウォレットを選択します。簡単に確認すると、2-of-2マルチシグウォレットの場合は、2つ中2つの署名が必要です。

### ステップ4: トランザクションのPSBTファイルをエクスポートする

Bitcoinトランザクションは、適切な鍵によって署名されました。「Broadcast」をクリックしないでください。クリックするとネットワーク全体に共有され、ColdCardハードウェアウォレットを使用している場合、あなたのトランザクションが公開され、資金が危険にさらされます。

これで「Export」をクリックし、PSBTファイルをコンピューター上にローカル保存できます。

![LianaからPSBTファイルをエクスポートする](assets/fr/03.webp)

### ステップ5: outofband.wizardsardine.com経由でトランザクションをマイナーへ送信する

ここから最後の手順です。トランザクションをマイナーへ送信するには、PSBTファイルを取り、指定されたエリアへドラッグ＆ドロップするだけです。

![PSBTファイルをoutofband.wizardsardine.comにドロップする](assets/fr/04.webp)

すると、トランザクションは以下のように表示されます。

![キュー内のトランザクション](assets/fr/05.webp)

### ステップ6: Slipstream経由でトランザクションを送信する

最後に、「Send」をクリックするだけで、トランザクションがSlipstream経由でMARAへ送信されます。

![Slipstream経由でトランザクションを送信する](assets/fr/06.webp)

数秒以内に、トランザクションは「Sending」から「Accepted」に変わります。

![Slipstreamに受け入れられたトランザクション](assets/fr/07.webp)

あとは、トランザクション識別子（TXID）をコピーし、[mempool.space](https://mempool.space/)に貼り付けて、マイニングされる様子を確認するだけです。

![mempool.spaceでTXIDを調べる](assets/fr/08.webp)

注意: マイナーであるMARAがブロックをマイニングし、その中にあなたのトランザクションを含めるまで、トランザクションは「Transaction not found」と表示されます。MARAが保有するBitcoinネットワークのハッシュレートは約4.5%にすぎないため、これには数十分、あるいは数時間かかることがあります。2026年8月4日時点では、これはおよそ3時間45分ごとに1ブロックをマイニングすることに相当します。

## 他のウォレットのユーザー向け

[Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)を使用していないものの、このツールを使いたい場合のために、ここでは2-of-2マルチシグウォレットを使ったチュートリアルを紹介します。そのために、[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)ソフトウェアウォレットを使用します。

*前提条件: Sparrowウォレットに資金があること。*

### ステップ1: トランザクションを作成する

[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)で、マルチシグウォレット上にトランザクションを作成します。このページで説明されているように、推奨レートよりもかなり高い手数料を設定することを忘れないでください: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

作成したら、「Create Transaction」をクリックします。

![Sparrowでトランザクションを作成する](assets/fr/09.webp)

### ステップ2: トランザクションを確定する

トランザクションを確定するには、ここで署名する必要があります。そのために、「Finalize Transaction for Signing」をクリックします。

![署名のためにトランザクションを確定する](assets/fr/10.webp)

### ステップ3: 異なる鍵でトランザクションに署名する

ここでトランザクションに署名します。使用しているソフトウェアウォレットまたはハードウェアウォレットで署名するだけです。

![マルチシグ鍵でトランザクションに署名する](assets/fr/11.webp)

### ステップ4: 署名済みトランザクションをダウンロードし、ネットワークへブロードキャストしない

Bitcoinトランザクションは、これで私たちの2-of-2マルチシグの両方の鍵によって署名されました。「Broadcast Transaction」をクリックしないでください。クリックするとネットワーク全体に共有され、ColdCardハードウェアウォレットを使用している場合、あなたのトランザクションが公開され、資金が危険にさらされます。

![署名済みトランザクション、準備済みだが未ブロードキャスト](assets/fr/12.webp)

### ステップ5: 署名済みトランザクションスクリプトを表示する、またはPSBTファイルをダウンロードする

署名済みBitcoinトランザクションを表示するには、「View Final Transaction」をクリックします。その後、署名済みBitcoinトランザクションスクリプトをコピーできます。

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![署名済みトランザクションスクリプトを表示する](assets/fr/13.webp)

トランザクションファイルをダウンロードしたい場合は、次のどちらかを行えます。

- 「File」をクリックし、次に「Save transaction…」をクリックする。
- または、右下のネットワーク接続ボタン（黄色のボタン）をクリックし、次に「Save Final Transaction」をクリックする。

すると、トランザクションはコンピューター上にローカル保存されます。

![最終トランザクションをローカルに保存する](assets/fr/14.webp)

### ステップ6: outofband.wizardsardine.com経由でトランザクションをマイナーへ送信する

ここから最後の手順です。トランザクションをマイナーへ送信するには、次の操作を行うだけです。

- [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)にアクセスする。
- 前のステップでコピーした署名済みトランザクションスクリプトを貼り付け、その下の「ADD TO QUEUE」をクリックする。

![トランザクションスクリプトをツールに貼り付ける](assets/fr/15.webp)

- または、ファイルを取り、指定されたエリアへドラッグ＆ドロップする。

![トランザクションファイルをツールにドロップする](assets/fr/16.webp)

すると、トランザクションは以下のように表示されます。

![キュー内のトランザクション](assets/fr/17.webp)

トランザクション内のサトシの入力合計額が不明である（その結果、手数料のサトシ数を計算できない）というメッセージが表示された場合は、サトシの入力合計額を手動で入力するだけで済みます。それを確認するには、Sparrow内の図の中央に表示されているトランザクションをクリックしてください。

![Sparrowに表示された入力合計額](assets/fr/18.webp)

次に、その金額（この例では15,904 sats）を[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)ツールに入力します。

![入力合計額を手動で入力する](assets/fr/19.webp)

最後に、手数料率が正しいことを確認します。

### ステップ7: Slipstream経由でトランザクションを送信する

最後に、「Send」をクリックするだけで、トランザクションがSlipstream経由でMARAへ送信されます。

![Slipstream経由でトランザクションを送信する](assets/fr/20.webp)

数秒以内に、トランザクションは「Sending」から「Accepted」に変わります。

![Slipstreamに受け入れられたトランザクション](assets/fr/21.webp)

あとは、トランザクション識別子（TXID）をコピーし、[mempool.space](https://mempool.space/)に貼り付けて、マイニングされる様子を確認するだけです。

![mempool.spaceでTXIDを調べる](assets/fr/22.webp)

注意: マイナーであるMARAがブロックをマイニングし、その中にあなたのトランザクションを含めるまで、トランザクションは「Transaction not found」と表示されます。MARAが保有するBitcoinネットワークのハッシュレートは約4.5%にすぎないため、これには数十分、あるいは数時間かかることがあります。2026年8月4日時点では、これはおよそ3時間45分ごとに1ブロックをマイニングすることに相当します。
