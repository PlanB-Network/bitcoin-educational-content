---
name: BIP-39 Passphrase Trezor
description: passphraseをTrezorのポートフォリオに加えるには？
---
![cover](assets/cover.webp)



passphrase BIP39 はオプションのパスワードで、Mnemonic フレーズと組み合わせることで、決定論的かつ階層的な Bitcoin ポートフォリオに追加の Layer セキュリティを提供します。このチュートリアルでは、Trezor（Safe 3、Safe 5、Model One）上の安全なBitcoin Walletにpassphraseを設定する方法をご紹介します。



![Image](assets/fr/01.webp)



このチュートリアルを始める前に、もしあなたがpassphraseのコンセプトやその仕組み、Bitcoin Walletへの影響についてよく知らないのであれば、私がすべてを説明している理論的な記事を参照することを強くお勧めします（これは非常に重要です：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Trezor上のpassphraseは、設定時にBIP39標準を選択した場合、古典的な方法で処理されます（*Multi-share Backup*が不要な場合は、これをお勧めします）。Trezorが特別なのは、Hardware Walletで直接passphraseを入力するか、Trezor Suiteソフトウェアを使ってコンピュータのキーボードから入力できることです。コンピュータはHardware Walletよりも攻撃対象が非常に大きいため、この2番目のオプションはかなり安全性に欠けます。しかし、複雑な passphrase を入力する場合、従来のキーボードの方が Hardware Wallet よりも速く入力できる可能性があります。したがって、passphrase を使用しないよりは、たとえタイピングが必要であったとしても、passphrase を使用する方が常にベターです。しかし、このことが意味する数値的な攻撃のリスクが高まることを認識しておくことは重要である。



これらのオプションは、すべてのTrezor対応ポートフォリオ管理ソフトウェアで利用できるわけではありません。例えば、Model One の場合、passphrase は Sparrow Wallet のキーボードから入力できます。Model T、Safe 3、Safe 5の場合は、Trezor Suiteを使用するか、Hardware Walletに直接passphraseを入力する必要があります。



![Image](assets/fr/02.webp)



Trezor Suiteでは、passphraseの需要を管理する2つの異なる方法があります。**Device**タブで **passphrase** オプションを有効にすることができます。このオプションを有効にすると、Trezor Suiteをはじめとするすべてのポートフォリオ管理ソフトウェアが、起動するたびにpassphraseの入力を求めてきます。passphraseの使用をより慎重に行いたい場合は、設定を **Standard** のままにしておくことができます。この場合、手動でHardware Walletの左上のメニューにアクセスし、起動するたびに「**+ passphrase**」ボタンをクリックする必要があります。



このチュートリアルを始める前に、Trezor を初期化し、Mnemonic フレーズを生成したことを確認してください。まだの場合、またTrezorが新しい場合は、Plan ₿ Networkのモデル別チュートリアルに従ってください。このステップを完了したら、このチュートリアルに戻ることができます。



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## セーフ3またはセーフ5へのpassphraseの追加



Walletを作成し、Mnemonicを保存してPINを設定すると、Trezor Suiteのホームメニューが表示されます。左上隅に、passphrase BIP39のアクティベーションを促すウィンドウが表示されるはずです。



![Image](assets/fr/03.webp)



このウィンドウが表示されない場合は、「*デバイス*」設定タブの「*passphrase*」オプションを手動で有効にする必要があります。



![Image](assets/fr/04.webp)



このウィンドウは、あなたのpassphraseを入力するよう求めます。強力なpassphraseを選び、すぐに紙や金属などの媒体に物理的なバックアップを取ってください。この例ではpassphraseを選んだ：`fH3&kL@9mP#2sD5qR!82`.これは一例ですが、もう少し長いpassphraseを選ぶことをお勧めします。30文字から40文字の間が理想的でしょう（良いパスワードのように）。



もちろん、このチュートリアルでやっているように、インターネット上でpassphraseを共有してはいけません。この例のWalletはTestnetでのみ使用し、チュートリアルの最後に削除します。



passphraseの選び方について、より具体的なアドバイスが必要な場合は、別の記事を参照していただきたい：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

パソコンのキーボードからpassphraseを入力する場合は、入力欄にpassphraseを入力し、「*passphrase Wallet*にアクセス」をクリックしてください。



![Image](assets/fr/05.webp)



Hardware Walletにpassphraseが表示されます。あなたの物理的なバックアップ（紙または金属）と一致していることを確認してから、画面をクリックして続行してください。



![Image](assets/fr/06.webp)



これにより、passphraseで保護されたポートフォリオにアクセスできるようになる。



![Image](assets/fr/07.webp)



passphraseをTrezorにのみ入力し、セキュリティを強化したい場合は、プロンプトが表示されたら、"*Enter passphrase on Trezor*"をクリックしてください。



![Image](assets/fr/08.webp)



TrezorにT9キーボードが表示され、passphraseを入力することができます。入力が完了したら、Greenのチェックをクリックし、passphraseをWalletに適用します。



![Image](assets/fr/09.webp)



passphraseの安全なWalletにアクセスできるようになります。



![Image](assets/fr/10.webp)



Sparrow Walletを使用する場合も同様の手順ですが、モデルT、Safe 3、Safe 5の場合、passphraseはパソコンのキーボードではなく、Hardware Walletで入力する必要があります。



Sparrow WalletがTrezorへのアクセスを必要とし、passphraseが前回の起動からまだ適用されていない場合は、T9キーボードを使って入力する必要があります。



![Image](assets/fr/11.webp)



## モデル・ワンにpassphraseを追加する



モデル・ワンでは、passphrase BIP39の使用がほぼ不可欠である。この装置にはセキュア・エレメントが組み込まれていないため、機密情報を抜き取ることは比較的容易である。そのため、物理的な攻撃に対する耐性はない。しかし、passphraseは電源を切った後はデバイスに保持されないため、強力な（ブルータブルでない）passphraseを使用すれば、このモデルで知られているほとんどの物理的攻撃から身を守ることができる。



モデル・ワンでは、Hardware Walletでpassphraseを直接入力することはできません。パソコンのキーボードから入力する必要がある。



Walletを作成し、Mnemonicを保存してPINを設定すると、Trezor Suiteのホームメニューが表示されます。左上に、passphrase BIP39のアクティベーションを促すウィンドウが表示されるはずです。



![Image](assets/fr/12.webp)



このウィンドウが表示されない場合は、設定の「*デバイス*」タブで「*passphrase*」オプションを有効にする必要があります。



![Image](assets/fr/13.webp)



このウィンドウでは、passphraseを入力するよう求められます。強力なpassphraseを選び、すぐに紙や金属などの媒体に物理的なバックアップを取る。この例では、`fH3&kL@9mP#2sD5qR!82`というpassphraseを選びました。これはあくまで例ですが、passphraseは少し長めのものを選ぶことをお勧めします。30文字から40文字の間が理想的でしょう（良いパスワードのようなものです）。



passphraseの選び方について、より具体的なアドバイスが必要な場合は、別の記事を参照していただきたい：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphraseを入力し、"*Access passphrase Wallet*"ボタンをクリックしてください。



![Image](assets/fr/14.webp)



Hardware Walletにpassphraseが表示されます。それがあなたの物理的なバックアップ（紙または金属）と一致していることを確認し、右側のボタンをクリックして続行します。



![Image](assets/fr/15.webp)



これでpassphraseで保護されたポートフォリオが表示されます。



![Image](assets/fr/16.webp)



その後、Sparrow Walletを使用する場合も、手順は変わりません。SparrowがHardware Walletにアクセスする必要があり、前回起動時からpassphraseが入力されていない場合は、その都度入力する必要があります。



![Image](assets/fr/17.webp)



おめでとうございます、これでpassphrase BIP39をTrezorハードウェアウォレットで使用するスピードが上がりました。Walletのセキュリティをさらに強化したい方は、Trezorの*マルチ共有*バックアップシステム（*シャミールの秘密共有スキーム*）のチュートリアルをご覧ください：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

このチュートリアルが役に立ったと思ったら、下にGreenの親指を残していただけるとありがたい。この記事をあなたのソーシャルネットワークでシェアしてください。ありがとうございました！