---
name: BIP-39 Passphrase SeedSigner
description: passphraseをSeedSignerのポートフォリオに追加するにはどうすればよいですか？
---

![cover](assets/cover.webp)



passphrase BIP39 はオプションのパスワードで、ニーモニックフレーズと組み合わせることで、決定論的で階層的な Bitcoin ウォレットに追加のセキュリティレイヤーを提供します。このチュートリアルでは、SeedSignerで使用されるBitcoin walletにpassphraseをセットアップする方法をご紹介します。



![Image](assets/fr/01.webp)



## パスフレーズを追加する前の前提条件



このチュートリアルを始める前に、もしあなたがpassphraseのコンセプト、その仕組み、そしてあなたのBitcoin walletに対するその影響についてよく知らないのであれば、私がすべてを説明しているこの他の理論的な記事を参照することを強くお勧めします（これは非常に重要です、passphraseの仕組みを完全に理解しないままpassphraseを使用すると、あなたのビットコインが危険にさらされる可能性があるからです）：



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

このチュートリアルを始める前に、SeedSignerの初期化とニーモニックフレーズの生成が済んでいることを確認してください。まだの場合、またSeedSignerが新しい場合は、プラン₿アカデミーのチュートリアルに沿ってください。このステップを完了したら、このチュートリアルに戻ることができます：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## SeedSignerにpassphraseを追加するには？



SeedSignerで管理するポートフォリオにpassphraseを追加すると、全く新しいポートフォリオが作成され、全く別の鍵セットが生成される。その結果、すでにSatsを含むポートフォリオを持っている場合、passphraseを使用すると、まったく別のポートフォリオが生成されるため、そのポートフォリオにアクセスすることができなくなる。



passphraseをSeedSignerに適用するには、デバイスの電源を入れ、通常通りSeedQRをスキャンします。すると、SeedSignerは現在のwalletのフィンガープリントを表示します。passphraseを搭載したwalletは異なるフィンガープリントを持ちます。



BIP-39パスフレーズ`ボタンをクリックしてください。



![Image](assets/fr/02.webp)



次に、画面上のキーボードを使用して、選択したpassphraseを入力します。この passphrase を紛失すると、ビットコインに永久にアクセスできなくなります。 **wallet を復元するには、ニーモニックと passphrase の両方が不可欠です。



入力が完了したら、SeedSignerの右下にある「KEY3」ボタンを押して認証を行います。



![Image](assets/fr/03.webp)



*この例では、passphraseの`pba`を使った。しかし、あなたの場合は、堅牢なpassphraseを選ぶようにしてください。最適なpassphraseを定義する方法については、こちらの記事を参照してください。



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSignerはあなたのpassphrase walletの新しいフィンガープリントを表示します。このフィンガープリントは、passphraseでwalletを使用する際に重要です。passphraseを入力するたびに、入力ミスがないか、正しいwalletにアクセスしているかを確認することができるからです。



例えば、私の場合、SeedSignerを起動するときに、`pba`ではなく、間違ってpassphraseの`Pba`と書いてしまったとすると、この小文字から大文字への単純な変更によって、私がアクセスしたいポートフォリオとはまったく別のポートフォリオが作成されてしまうことになる。



このフィンガープリントは、wallet のセキュリティーや機密性を脅かすことはない。あなたの鍵について、公開、非公開を問わず、いかなる情報も開示しない。したがって、ニーモニックや passphrase とは異なり、フィンガープリントをデジタル媒体に保存することができる。紙やパスワード・マネージャーなど、いくつかの場所にコピーを保存しておくことをお勧めする。



指紋を保存したら、`Done`をクリックします。



![Image](assets/fr/04.webp)



その後、従来のSeedSignerと同様に、ポートフォリオのすべての機能にアクセスすることができます。



![Image](assets/fr/05.webp)



これでSparrow Walletにキーストアをインポートし、walletを通常通り使うことができる。再起動するたびに、SeedQRをスキャンし、passphraseをキーボードで再入力する必要があります。



実際にpassphraseでwalletを使用する前に、フルエンプティリカバリーテストを行うことを強くお勧めします。これにより、ニーモニック・フレーズとpassphraseのバックアップが有効であることを確認できます。このチェックの方法については、以下のチュートリアルを参照してください：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895