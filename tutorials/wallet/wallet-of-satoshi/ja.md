---
name: SatoshiのWallet
description: 最もシンプルなカストーディアルWallet
---
![cover](assets/cover.webp)

このチュートリアルを書いたのは_ [Bitcoinキャンパス](https://linktr.ee/bitcoincampus_)


## Satoshiのダウンロード、セットアップ、Walletの使い方


SatoshiのWalletは、Lightning NetworkのWallet、カストーディアル、そして非常にシンプルな使い方。

BTC105 - Finding Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5)のコースでは、Redeem Lightning Networkのバウチャーに使用されます。


**いつも忘れないでください：鍵でもコインでもない。


カストディアル・ウォレットは、ユーザーが資金を完全にコントロールすることはできません。初心者を除き、通常は推奨されません。WoSは長期的な資金蓄積のためではなく、過渡的なWalletとして、またはポケットマネーを保持するために使用されるべきです。


---

SatoshiのWallet（WoS）はカストディ商品だが、一定の評価を受けている。私たちは、たとえば流動性を受け取る能力を高めるために、WoSのようなツールを利用することが合理的にできる。私たちはWoSに、チャンネルの流動性を管理するという「汚れ仕事」を一時的に委任する。一定量に達したら、WoSのOn-Chainを我々の非保管Walletに空ける。


**警告⚠️：先に進む前にチュートリアル全体を読むことをお勧めします。


### SatoshiのWalletをダウンロード


Playストアにアクセスし、WoSをダウンロードする。


![image](assets/it/01.webp)


**WoSは公式ストアからのみダウンロード可能です。デバイスのOSがプログラムされている場合、WoSを開く前にOS自身による検証部分があります。確認の後、「開く」を選択してください。


![image](assets/it/02.webp)


SatoshiのWalletが以下の画面で開くので、_Start_をクリックする。


![image](assets/it/03.webp)


### WoSのアカウント登録


この時点でWalletはすでに操作可能ですが、より安全性を高めるため、ログインの設定を進めます：デバイスの故障や紛失の際に資金を回収するために必要となります。従って、左上のメニューを選択してください。


![image](assets/it/04.webp)


メニュー・ウィンドウ全体が開くので、通貨（SatoshiのWalletはデフォルトで米ドルを基準通貨として表示する）とテーマ・カラー（明暗）を好みに応じて設定する。他のコマンドは使わないでください。


WoSは管理ツールであるため、WalletをMnemonicのフレーズでバックアップすることはできませんが、モバイルデバイスの紛失や不使用の場合、_ログイン/登録_をクリックすることで、WoSが資金を回収できるようになります。

電子メール Address を入力するウィンドウが表示されます。プロトンメール**（推奨）でも構いませんが、携帯電話の紛失・盗難・破損の際にWallet内の資金を回収できるよう、機能的なものでなければなりません。


![image](assets/it/08.webp)


SatoshiのWalletが、指定されたメールボックスにメッセージを送信した。


![image](assets/it/09.webp)


メールボックスの中に2つの単語があるので、アプリが提供するスペースに書き換えて入力する。


- 翻訳機を作動させないでください。
- 大文字と小文字に注意して2つの単語を書き換える。


![image](assets/it/10.webp)


2つの単語を書き起こしたら、_OK_をクリックします。


![image](assets/it/11.webp)


その結果、上部に画像が表示され、確認のためのチェックマークが表示されるはずです。


![image](assets/it/12.webp)


設定セクションで、赤い_Login/Register_バーにユーザーのEメールAddressが表示されるようになりました。


![image](assets/it/13.webp)


### 支払いの受領


WoSで受信するには、_Receive_をクリックすると一連のコマンドが表示される。


![image](assets/it/14.webp)


を受け取ることができる。


- LN-Address経由 **a** **a**経由
- Invoiceの**b**を設定することで、LNを経由する。
- on chain（WoSはBitcoinネットワークをサポートするが、有料のサブマリン・スワップが必要） **c**
- のQRコードをスキャンしてください。


![image](assets/it/15.webp)


### Invoiceの作成


Receive_をクリックし、Lightning Networkのシンボルのコマンドを選択する。


![image](assets/it/16.webp)


Invoiceの作成メニューが表示されるので、_Add Amount_をクリックして正確な金額を記入し、説明文（この例では "My first Invoice"）を追加する。


![image](assets/it/17.webp)


キーボードで金額を設定する。


![image](assets/it/18.webp)


そしてInvoiceの支払いを受ける。支払いはこのように表示される：


![image](assets/it/19.webp)


### POSからの回収


SatoshiのWalletにはデフォルトの機能がある。POSを有効にする方法を見てみよう。


メイン画面から右上のメニューを選択。


![image](assets/it/20.webp)


次に_Point of Sale_を選択する。


![image](assets/it/21.webp)


WoSの最新リリースでは、必ず「キーパッド」を選択してください。


![image](assets/it/22.webp)

を入力し、キーパッドに金額を入力します。次の例では、10セント/118Satsです。コレクションの説明を追加します。この例では "my second with POS "です。大きなGreenボタンが点灯し、クリックします。

![image](assets/it/23.webp)


をgenerateに入れて、たとえば顧客に見せる。


![image](assets/it/24.webp)


この支払いも徴収される！


![image](assets/it/25.webp)


### 支払いの送信


シンプルさはWoSのメイン画面の強みである。Invoiceを支払うには、_Send_をクリックする。


![image](assets/it/26.webp)


初回使用時、WoSはカメラへのアクセス許可を求める


![image](assets/it/27.webp)


この瞬間からカメラは起動する


![image](assets/it/28.webp)


Invoiceの枠に210Satsの支払いが要求されていることがわかる。また、依頼者が設定した場合は、説明文も表示される。この画面は要約であり、また確認要求でもある：WoSは支払いを送るための "承認を求め"、Greenの_Send_ボタンをクリックすることで承認される。


![image](assets/it/29.webp)


支払いが目的地に到着すると、WoSは以下の画面で通知します。


![image](assets/it/30.webp)


メイン画面から「履歴」（残高のすぐ下）をクリックすると、取引リストが表示される。


![image](assets/it/31.webp)


#### WoSアカウントの復旧


Walletがインストールされた携帯電話が盗難にあったり、紛失したり、操作できなくなったりした場合にも便利です。再インストール後は、先ほど説明したアカウント登録の手順をやり直す必要があるが、その際に1つだけ異なる点がある。それは、前回設定したメールアドレスでのログイン要求の最後に、WoSがこのように表示されることである：


![image](assets/it/33.webp)


アカウントを再有効化する手順を記載した電子メールが送信されたことを警告するメッセージが表示されます。メールの受信箱を開いてください。


**重要**：電子メールはPCから、あるいはいかなる場合でも、WoSアカウントを回復しようとしているものとは別のデバイスから開いてください。受信トレイに、フレームを作成するためのQRコードを示すメッセージがあります。


![image](assets/it/34.webp)


QRコードに枠をはめると、WoSのメインページに復旧した口座が表示され、残高と履歴が表示される。