---
name: COLDCARD - コサイン
description: Co-Sign機能を発見し、COLDCARDでご利用ください。
---

![cover](assets/cover.webp)


*注意：このチュートリアルは、マルチシグネチャ・ウォレット、コインカイト・デバイス、Sparrow walletやNunchuk.*などのソフトウェアをすでにある程度使ったことがある人を対象としています。



![video](https://youtu.be/MjMPDUWWegw)




**なぜコールドカード・コサインなのか？



この機能により、ColdCard (Q または Mk4) デバイスにハードウェア・セキュリティ・モジュール (HSM) の方法で **使用条件** を追加し、資金を保護しながら、資金を柔軟に管理することができます。



支出条件としては、例えば以下のようなものがある：





- 大きさの制限**：1回の取引で使用できるビットコインの量に上限があります。
- ベロシティ制限：**単位時間あたり（1時間、1日、1週間など）に実行可能なトランザクション数を決定し、トランザクション間に最低ブロック数を要求する。
- 事前に承認されたアドレス:** 事前に承認されたアドレスへのビットコインの送信のみを許可します。
- 二要素認証：** インターネットにアクセスできるNFC対応スマートフォン/タブレットで、サードパーティの2FAモバイル・アプリケーション（TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)）からの確認が必要。



**仕組み



2 つ目の seed を ColdCard Mk4 または Q デバイスに追加することで、"Spending Policy Key" (このチュートリアルでは "C Key" と呼びます) が作成されます。


この追加seedに加えて、Wallet Multisig 2on-Nを作成するために、「バックアップ・キー」と呼ぶことにするが、少なくとも1つの追加キー（XPUB）をSupplyに要求される。



まとめると、Wallet Multisig を作成し、ColdCard デバイスには、資金を支出するために必要な秘密鍵のうち、デバイスの seed マスターと「支出ポリシー鍵」の 2 つが含まれることになります。



C キー」が署名を要求されるたびに、指定された利用条件が適用され、コールドカードはその取引 が条件に適合する場合にのみ署名する。



これらの利用条件を省きたい場合は、そうすることができる：




- バックアップキーの1本とseedハンド、またはMultisigのサイズによってはバックアップキー2本でサインする。
- を入力することで、設定することができます。 **後者はデバイス上で直接参照することはできません。そうでなければ、誰でも設定した支出条件をキャンセルすることができます。




## ColdCard Co-Sign の設定



![video](https://youtu.be/MjMPDUWWegw)



### 1- 機能の有効化



まず、お使いのデバイスのファームウェアのバージョンが最新であることをご確認ください：




- Mk4: v5.4.2
- Q: v1.3.2Q




Mk4 または ColdCardQ で、[Advanced Tools] > [ColdCard Co-Signing] を選択します。



![Co-Sign](assets/fr/01.webp)



*以下のチュートリアルでは、便宜上 ColdCardQ のスクリーンショットを使用しますが、手順とメニューは Mk4 と Q.* で同一です。



機能の概要が表示されます。


これから作る2対3のマルチシグネチャーWalletでもまた使うことになるだろうが、キーを指定するために使われる用語は次の通りだ：



キーA = コールドカード・マスター seed


キーB = バックアップ・キー


キー C = 支出方針キー



ENTER "**をクリックする。



![Co-Sign](assets/fr/02.webp)



次のステップは、どの秘密鍵が "Spending Policy Key "または "Key C "として機能するかを決めることである。



私たちにはいくつかの選択肢があることがわかる：





- または、**"ENTER "**を押して、12語の新しいseed文章をgenerateします。





- 既存の12ワードのseedをインポートする場合は**"(1) "**を、既存の24ワードのseedをインポートする場合は**"(2) "**をクリックしてください。





- または**"(6) "**を押して、デバイスの保管庫からseedをインポートします。



このチュートリアルでは、既存の12ワードのseedを、**"(1) "**を押してインポートすることにした。これは、あなたがすでに所有しているseed BIP39のどれでも構いませんし、明らかにバックアップがあるものです。



キーボードでseedの12ワードを入力します。この例では、seedの有効フレーズ「beef x 12」を選びます。そして**"ENTER "**を押してください。


*注意：このseedのバックアップをお持ちでない場合、ご利用条件を変更するために、デバイス上で「共同署名」の設定を変更することができなくなります*。



これで "Co-Sign "機能はデバイス上で有効になりました。次に支出条件を選択し、マルチ署名Walletの作成を完了する必要がある。



![Co-Sign](assets/fr/03.webp)



### 2- 支出条件または "*支出方針*"を選択する。



ここでは、**"C Key "**または**"Spending Policy Key**"がトランザクションに署名する際に満たさなければならない支出条件を指定する。



共同署名 "**"メニューで、**"支出規定**"をクリックしてください。



次に、最大マグニチュード、つまり1回の取引で使用できるサトシの最大数を選択することができます。



この例では、最大マグニチュードを**21212** satoshisとします。ENTER "をクリックしてください。




![Co-Sign](assets/fr/04.webp)



次に、最大ベロシティ、つまりデバイスが単位時間当たりに署名できるトランザクション数を設定します。このチュートリアルでは、速度無制限、つまりトランザクション数の制限なしを選択します。




![Co-Sign](assets/fr/05.webp)



### 3-クリエイト Wallet Multisig 2-on-N



デバイスの**マスターseed**(キーA)と**"支出ポリシー・キー "**(キーC)に加えて、Wallet Multisigの3つ目のキー、つまり**"バックアップ・キー "**(キーB)を選択する必要がある。



私たちの "Bキー "は、SDカード経由でインポートするか、ColdCardQの場合はQRコード経由でインポートする必要があります。


そのためには、2台目のColdCard Mk4またはQデバイスが必要です。



バックアップ・キー "**（この例では ColdCard Mk4）が入っている 2 台目のデバイスで、メイン・メニューから **"設定 "**、次に **"Multisig Wallet"**、最後に **"Xpub をエクスポート "** してください。


(2台目のデバイスがColdCardQの場合は、もちろんQRコード経由でXpubをエクスポートするオプションがあります）。





![Co-Sign](assets/fr/06.webp)





次の画面でSDカードを挿入し、右下の**"validate "**ボタンをクリックします。次に、**"(1) "**をクリックして、SDカードにファイルを保存します。



ファイル名には公開鍵フィンガープリント（*fingerprint*）が含まれ、`ccxp-0F056943.json`という形式になる。




![Co-Sign](assets/fr/07.webp)



次に、SD カードを「初期」の ColdCardQ に挿入し、「バックアップ キー」 (キー B) をインポートします。


ColdCard Co-Signing "メニューで "Build 2-of-N "を選択し、次の画面で**"ENTER "**をクリックし、再度**"ENTER "**をクリックしてSDカードから "Backup Key "をインポートする。



![Co-Sign](assets/fr/08.webp)



次の画面で、"Account Number "を空白のままにして（何をやっているのかよく分かっている場合を除く）、もう一度**"ENTER "**をクリックする。



![Co-Sign](assets/fr/09.webp)



ようやく、新しいWallet Multisig 2-sur-3を使う準備が整った：



キーA＝コールドカードQマスターseed


キー B= バックアップ・キー (2 台目の Coldcard デバイスからインポートしたもの)


キーC= 支出ポリシー・キー（署名に使用される場合、事前に定義された支出条件を課す）



## Sparrow walletとの共同署名



必要に応じて、以下のチュートリアルを参照し、Sparrow walletのソフトウェアに慣れてください：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1-輸出 Wallet Multisig 2-サー-3～Sparrow wallet



WalletのMultisigをSparrowにエクスポートし、そこに最初のサトシを置く必要がある。



ColdCardQ のメインメニューから **"設定 "** を選択し、次に **"Multisig 財布 "** を選択します。


ColdCard に登録されている Multisig ウォレットが表示され、鍵の数が「2/3」（2-sur3）と表示されます。先ほど作成した Multisig **"ColdCard Co-Sign "** を選択し、**"ColdCard Export "** をクリックします。



![Co-Sign](assets/fr/10.webp)




最後に、WalletをSparrowにエクスポートする方法を選択します。ここではSDカードを選択するので、本体のスロットAにSDカードを挿入した後、**"(1) "**をクリックする。



![Co-Sign](assets/fr/11.webp)



次にSparrow walletで「Walletをインポート」を選択する。



![Co-Sign](assets/fr/12.webp)



次に、**"Import File "**をクリックします。次に、SDカード上の**"export-Coldcard_Co-sign.txt "**ファイルを選択します。



![Co-Sign](assets/fr/13.webp)



WalletにSparrowで表示される名前を付け、Walletを暗号化するためのパスワードを選択する（または選択しない）。



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



最初のサトシを受け取り、Walletに適用した支出条件をテストする準備が整った。



![Co-Sign](assets/fr/16.webp)



### 2- あらかじめ設定された支出方針のテスト



注意点として、我々はWallet Multisigの最大金額を21212サトシと決めていた。これは、支出ポリシー鍵(鍵C)がトランザクションに署名するたびに、支出額が21212サトシ以下である場合のみ、後者が有効であることを意味する。



テストしてみよう。


まず、Sparrowの "Receive "タブをクリックし、このチュートリアルで使用するWalletに数個のサッツをドロップしよう。



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



では、50,000Satsの取引をシミュレートして、21212サトシの許容額を超えて使ってみよう。



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



ColdCardQで*未署名の*取引を表すQRコードをスキャンして取引をインポートすると、このような画面が表示されます。消費条件が満たされていないことを示す警告メッセージが表示される。いずれにせよ、この取引に署名する場合、2 つの鍵のうち 1 つ（デバイス上の seed マスター鍵であり、"Key C "ではない）のみが署名することになる。




![Co-Sign](assets/fr/23.webp)



ここで、トランザクションをSparrowにインポートした後、1つの署名だけがトランザクションに適用されていることがわかる。



![Co-Sign](assets/fr/24.webp)




では、このWalletに設定した最大マグニチュード（21212 Sats）よりも小さい、21,000サトシの取引で実験を繰り返してみよう。




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



ColdCardQでこの取引に署名してみよう。



今回は問題なく、警告メッセージも表示されず、署名されたトランザクションをSparrow walletにインポートすると、今度は2つの署名が適用され、トランザクションが有効で配布できる状態になった。




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## ヌンチャクで共同サイン



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- ウェブ2FAとホワイトリストのアドレス



この段落では、Wallet Multisig Co-Sign with Nunchukを使い、新たな支出条件を適用して様子を見ることにする。



詳細ツール > コールドカード共同署名*」に進みます。


支出条件を変更するためのメニューにアクセスするために、「支出ポリシーキー」を入力するよう求められる。ここでは、12×"牛肉 "を入力する。



このチュートリアルに関連した実用的な理由から、21212Satsのマグニチュードと最大 "Limit Velocity "を維持することにした。一方、私たちは資金を使うことができるアドレスを指定するために、**"Whitelist Addresses "**メニューを使うつもりです。




![Co-Sign](assets/fr/31.webp)




ホワイトリストに追加したいアドレス（ここでは2つを選びます）に関連するQRコードをスキャンし、**"ENTER "**をクリックします。ENTER "**を連続して押してアドレスを確認すると、マグニチュードと受取人のアドレスに制限が適用されていることがわかります。



![Co-Sign](assets/fr/32.webp)



最後に、「Co-Sign」が提供する可能性の全体像を把握するために、「Web 2FA」オプションを有効にしてみよう。


この機能により、Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / Aegis AuthenticatorなどのTOTP RFC-6238準拠のアプリケーションを使用して、Layerのセキュリティを追加することができます。



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

具体的には、取引にサインする前に、NFC対応のインターネット接続機器をColdcardに近づける必要がある。すると自動的にcoldcard.comのウェブ・ページが表示され、そこで申請用の6桁のコードを入力するよう求められます。正しいコードを入力すると、ウェブページに ColdCardQ 用にスキャンする QR コード、または Mk4 に入力する 8 桁のコードが表示され、デバイスに署名を許可します。





![Co-Sign](assets/fr/33.webp)



二重認証アプリケーションに表示される QR コードをスキャンし、ColdCard Co-Sign (CCC) アカウントを追加した後、2FA コードを入力してすべてが正しいことを確認するよう求められます。



ColdCard を NFC デバイスの背面に入力します。



![Co-Sign](assets/fr/34.webp)



開いたウェブページで、お気に入りのアプリケーションの 2FA コードを入力します。次に、ColdCardQ で表示される QR コードをスキャンします (または、Mk4 に表示される 8 桁のコードを入力します)。



![Co-Sign](assets/fr/35.webp)




我々は現在、規模（21212 Sats）、宛先アドレス、二重認証に制限を課している。



![Co-Sign](assets/fr/36.webp)



### 2- Wallet Multisig 2on3をヌンチャクへ輸出



前回のSparrowに引き続き、今回はWallet Multisig 2on3をヌンチャクにエクスポートしてみよう。


設定 > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



今度は、同じ名前のColdcardQボタン**"NFC "**をクリックして、エクスポートのNFCオプションを選択します。



![Co-Sign](assets/fr/37.webp)



ヌンチャクで、初めてアプリケーションを開く場合は、**"Recover existing Wallet"**をクリックします。



![Co-Sign](assets/fr/38.webp)



すでにWalletをお持ちの場合は、右上の**"+"**をクリックし、**"Recover existing Wallet"**をクリックしてください。



![Co-Sign](assets/fr/39.webp)




次に、**"COLDCARDからWalletを復元 "**を選択し、**"Multisig Wallet"**を選択します。



![Co-Sign](assets/fr/40.webp)



最後に、スマートフォンの背面をColdCardQの画面にタップして、NFC経由でWalletをインポートする。



![Co-Sign](assets/fr/41.webp)



以前、Sparrow wallet経由で預けたサトシと口座が戻ってきた。



![Co-Sign](assets/fr/42.webp)



### 3- あらかじめ設定された支出方針のテスト



ここで、設定した 2 つの支出条件に違反する取引を試してみましょう。 **未承認のAddressに対して21212 Sats以上の支出を試みます。**ランダムなAddressに対して22222 Satsを送信してみます。



![Co-Sign](assets/fr/43.webp)



取引が作成されたら、右上隅にある 3 つの小さな点をクリックして ColdCard にエクスポートします。



![Co-Sign](assets/fr/44.webp)



次に、**"BBQR経由でエクスポート "**を選択し、ColdCardQと一緒に表示されるQRコードをスキャンします。



![Co-Sign](assets/fr/45.webp)



その後、ColdcardQ は警告を表示し、画面を下までスクロールすると、その取引が予想通り支出条件に違反していることを明確にします。



**潜在的な攻撃者が制限を回避しようとするのを防ぐために、どのような支出条件が関係しているのか、この装置では教えてくれないことに注意してほしい。




![Co-Sign](assets/fr/46.webp)



ENTER "**を押して認証すると、署名された取引のQRコードが表示されます。ヌンチャクで取り込むと、署名が1つだけ適用されていることがわかります。



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






全く同じ操作を行ってみよう。しかし今回は、マグニチュードの制限（21212Sats）を尊重するトランザクションで、事前に設定した2つのアドレスのうちの1つにサトシを費やしてみよう。



Nunchuk 12121 Sats を 2 つのアドレスのいずれかに送信します。その後、前回と同様に ColdCard にトランザクションをエクスポートします。



![Co-Sign](assets/fr/49.webp)




未署名のトランザクションを ColdCardQ にインポートした後、今度は何が表示されるかを見てみよう。



警告は常に表示されるが、今回は画面を一番下までスクロールすると、2FAによる取引の認証が必要であることがわかる。インターネットに接続されたNFC端末（スマートフォンやタブレット）にColdcardQを近づけるよう端末に求められるので、近づける。



![Co-Sign](assets/fr/50.webp)



スマートフォンでウェブページが開き、2FAコードを入力するよう求められるが、Proton Authenticatorのおかげで入力できた。



![Co-Sign](assets/fr/51.webp)





次に、ウェブページに表示される QR コードをスキャンして、ColdCard を認証し、取引に署名します。


トランザクションは2つの鍵によって署名され、有効なものとなった。



ColdCardQ で「Push Tx」が有効になっている場合、スマートフォンの背面をタップするだけで、取引をネットワークに直接ブロードキャストできます。



![Co-Sign](assets/fr/52.webp)




Push tx "を有効にしていない場合は、ColdCardQ の "QR "ボタンを押して署名されたトランザクションを QR コードとして表示し、前の例と同じ方法でそれを Nunchuk にインポートします。



![Co-Sign](assets/fr/53.webp)



今回、2つの署名が適用されたことに気づく。したがって、トランザクションはBitcoinネットワーク上でブロードキャストされる準備ができている。



![Co-Sign](assets/fr/54.webp)




CoinkiteのColdCardQとMk4デバイスに統合されたCo-Sign機能と、SparrowやNunchukのようなウォレットを使ったCo-Signの可能性について説明します。