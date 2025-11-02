---
name: BIP-39 passphrase シードシグナー
description: passphraseをSeedSignerのポートフォリオに追加するにはどうすればよいですか？
---

![cover](assets/cover.webp)



passphrase BIP39 はオプションのパスワードで、Mnemonic フレーズと組み合わせることで、決定論的で階層的な Bitcoin ウォレットに追加の Layer セキュリティを提供します。このチュートリアルでは、SeedSignerで使用されるBitcoin Walletにpassphraseを設定する方法をご紹介します。



![Image](assets/fr/01.webp)



## passphraseを追加する前の前提条件



このチュートリアルを始める前に、もしあなたがpassphraseのコンセプトやその仕組み、Bitcoin Walletへの影響についてよく知らないのであれば、私がすべてを説明している理論的な記事を参照することを強くお勧めします（これは非常に重要です：



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

このチュートリアルを始める前に、SeedSignerを初期化し、Mnemonicフレーズを生成したことを確認してください。もしまだの場合、またSeedSignerが新しい場合は、プラン₿アカデミーのチュートリアルにしたがってください。このステップを完了したら、このチュートリアルに戻ることができます：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## SeedSignerにpassphraseを追加するには？



SeedSignerで管理するポートフォリオにpassphraseを追加すると、まったく新しいポートフォリオが作成され、まったく別の鍵セットが生成されます。その結果、すでにSatssを含むポートフォリオを持っている場合、passphraseはまったく別のポートフォリオを生成するため、passphraseでそのポートフォリオにアクセスすることはできなくなります。



passphraseをSeedSignerに適用するには、デバイスの電源を入れ、通常通りSeedQRをスキャンします。すると、SeedSignerに現在お使いのWalletの指紋が表示されます。passphraseを搭載したWalletは異なる指紋を持ちます。



BIP-39 passphrase` ボタンをクリックします。



![Image](assets/fr/02.webp)



次に、画面上のキーボードを使用して、選択したpassphraseを入力します。この passphrase を紛失すると、ビットコインに永久にアクセスできなくなります。 **Walletを復元するためには、Mnemonicとpassphraseの両方が不可欠です。



入力が完了したら、SeedSignerの右下にある「KEY3」ボタンを押して認証を行います。



![Image](assets/fr/03.webp)



*この例ではpassphraseの`pba`を使った。しかし、あなたの場合は、堅牢なpassphraseを選ぶようにしてください。最適なpassphraseを定義する方法については、こちらの記事を参照してほしい。



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner はあなたの passphrase Wallet の新しいフィンガープリントを表示します。このフィンガープリントは、passphraseでWalletを使用する際に重要です。passphraseを入力するたびに、入力ミスがないか、正しいWalletにアクセスしているかを確認することができます。



たとえば、私の場合、SeedSignerを起動するときに、`pba`ではなく、間違ってpassphraseの`Pba`と書いてしまったとすると、この小文字から大文字への単純な変更によって、私がアクセスしたいポートフォリオとはまったく別のポートフォリオが作成されてしまうことになる。



このフィンガープリントは、Wallet のセキュリティーや機密性に対していかなるリスクも与えない。それは、あなたの鍵に関するいかなる情報、公的または私的な情報を開示しません。Mnemonic や passphrase とは異なり、フィンガープリントをデジタル媒体に保存することができます。紙やパスワード・マネージャーなど、いくつかの場所にコピーを保存しておくことをお勧めする。



指紋を保存したら、`Done`をクリックします。



![Image](assets/fr/04.webp)



その後、従来のSeedSignerと同様に、ポートフォリオのすべての機能にアクセスすることができます。



![Image](assets/fr/05.webp)



これでSparrow walletにキーストアをインポートし、Walletを通常通り使うことができる。再起動するたびに、SeedQRのスキャンとキーボードによるpassphraseの再入力の両方が必要です。



実際にWalletをpassphraseで使用する前に、フルエンプティリカバリーテストを行うことを強くお勧めします。これにより、Mnemonic のフレーズと passphrase のバックアップが有効であることを確認できます。この確認方法については、以下のチュートリアルをご参照ください：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895