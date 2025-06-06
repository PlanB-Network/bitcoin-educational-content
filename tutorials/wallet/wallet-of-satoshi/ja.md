---
name: SatoshiのWallet（WoS）
description: 最もシンプルなWallet（カストディアル）から始めよう
---
![cover](assets/cover.webp)

このチュートリアルを書いたのは_ [Bitcoinキャンパス](https://linktr.ee/bitcoincampus_)

# SatoshiのWalletをダウンロード、設定、使用する

SatoshiのWalletは、WalletのLightning Network、カストディアル、非常にシンプルな使い方。

コース[BTC105 - Finding Yourself Now](https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5)では、Redeem Lightning Networkのバウチャーに使用されます。

**いつも忘れないでください：鍵でもコインでもない

Walletのカストディアルでは、ユーザーは資金を完全に処分することはできない。ゼロから始める場合を除き、通常は推奨されない。WoSはWalletの入り口として、あるいはお小遣いを貯めるために使うべきであり、長期的に資金を貯めるために使うべきものではない。

---
SatoshiのWallet（WoS）はカストディアル商品だが、一定の評価を受けている。たとえば、流動性を受け取る能力を高めるために、WoSのようなツールを利用するのは合理的だ。私たちは一時的に、チャネルの流動性を管理する「汚れ仕事」をWoSに委任する。一定量に達したら、WoSのOn-ChainをWalletの非保管で空にする。

**ATTENZIONE⚠️：先に進む前に、チュートリアル全体を読むことをお勧めします。

## SatoshiのWalletをダウンロード

プレイストアに行き、WoSをダウンロードしよう。

![image](assets/it/01.webp)

**WoSは公式ストアからのみダウンロード可能です。端末のOSがプログラムされている場合、WoSを開く前にOS自身による検証が行われます。検証段階が終了したら、_Open_を選択してください。

![image](assets/it/02.webp)

SatoshiのWalletが以下のような画面で開きますので、_Start_をクリックしてください。

![image](assets/it/03.webp)

## WoSのアカウント登録

この時点でWalletは稼働していますが、セキュリティを高めるためにログインを設定しましょう：これはデバイスの故障や紛失時に資金を回収するために使用されます。次に左上のメニューを選択します。

![image](assets/it/04.webp)

メニュー・ウィンドウ全体が開くので、好みに応じて通貨（SatoshiのWalletはデフォルトで米ドルを参照通貨として提示する）とテーマ・カラー（明るい／暗い）を設定するだけでよい。他のコントロールは使用しないでください。

WoSは管理ツールであるため、WalletをMnemonicのフレーズでバックアップすることはできません。

![image](assets/it/07.webp)

電子メール Address を入力するウィンドウが表示される。携帯電話の紛失や盗難、故障の際にWalletの資金を回収するためのものだからだ。

![image](assets/it/08.webp)

SatoshiのWalletが、報告されたメールボックスにメッセージを送信した。

![image](assets/it/09.webp)

受信箱の中に2つの単語があるので、アプリが提示するスペースに、その単語を書き換えて入力しなければならない。


- 翻訳機を作動させないでください：単語は英語のままであるべきです**。
- 大文字と小文字に注意して2つの単語を書き換える。

![image](assets/it/10.webp)

2つの単語を書き起こしたら、_OK_をクリックします。

![image](assets/it/11.webp)

その結果、図が上部に表示され、確認のためのチェックマークが付きます。

![image](assets/it/12.webp)

の赤い帯は、ユーザーの電子メールAddressを表示するようになりました。

![image](assets/it/13.webp)

## 支払いの受領

WoSで受信するには_Receive_をクリックすると、一連のコマンドが表示される。

![image](assets/it/14.webp)

を受け取ることができる。


- LN-Address経由 **a** **a**経由
- LN経由、Invoice設定 **b**
- on chain（WoSはBitcoinのネットワークをサポートするが、有料でサブマリン・スワップを行う） **c**
- LNurl-pのQRコードをフレーミングする **d**

![image](assets/it/15.webp)

## Invoice クリエーション

Receive_をクリックし、Lightning Networkの記号を持つコマンドを選択する。

![image](assets/it/16.webp)

Invoiceの作成メニューが表示されるので、_Add Amount_をクリックして正確な金額を記入し、説明文（この例では "My first Invoice"）を追加する。

![image](assets/it/17.webp)

キーボードを使って金額を設定する

![image](assets/it/18.webp)

そしてInvoiceの支払いを受ける。支払いはこのように表示される：

![image](assets/it/19.webp)

## POSからの回収

SatoshiのWalletはデフォルトで興味深い機能を備えており、特に加盟店に適している：POSです。それを有効にする方法を見てみよう。

メイン画面から右上のメニューを選択

![image](assets/it/20.webp)

その後、_Point of Sale_を選択する。

![image](assets/it/21.webp)

WoSの最新リリースでは、_Keypad_を選択することに注意してください。

![image](assets/it/22.webp)

を入力し、キーパッドに金額を入力します。以下の例では、18セント/118Satsとなります。コレクションの説明を追加します。この例では、"My second with POS "です。大きなGreenボタンが点灯するので、それをクリックします。

![image](assets/it/23.webp)

Invoiceをgenerateにしてクライアントに見せるためだ。

![image](assets/it/24.webp)

この支払いも徴収される！

![image](assets/it/25.webp)

## 支払いの送信

シンプルさはWoSのメイン画面の強みである。Invoiceの支払いをするには、_Send_をクリックする。

![image](assets/it/26.webp)

初回使用時、WoSはカメラへのアクセス許可を求める

![image](assets/it/27.webp)

この瞬間からカメラは起動する

![image](assets/it/28.webp)

Invoiceのフレームを見ると、210Satsの支払いが要求されていることがわかる。また、請求者が説明文を設定している場合は、その説明文も表示される。この画面は概要であり、また確認の要求でもある：WoSは支払いを送る許可を求めており、Greenの_Send_ボタンをクリックすることで許可される。

![image](assets/it/29.webp)

支払いが目的地に到着すると、WoSは次のような画面で警告を発します。

![image](assets/it/30.webp)

プリンシパル画面から、_履歴_（残高のすぐ下）をクリックすると、取引リストが表示される。

![image](assets/it/31.webp)

### WoSアカウント回復

Walletがインストールされた携帯電話が盗難にあったり、紛失したり、操作できなくなったりした場合にも便利です。再インストール後は、先ほど説明したアカウント登録の手順をやり直す必要があるが、1つだけバリエーションがある。前回設定したメールアドレスでのログイン要求の最後に、WoSがこのように表示される：

![image](assets/it/33.webp)

アカウントを再有効化する手続きがEメールで送信されたことを知らせるメッセージが表示される。メールボックスを開く必要がある。

**重要**：メールはPCから、あるいはWoSアカウントを取得するデバイス以外から開いてください。受信トレイには、次のようなQRコードが表示されている。

![image](assets/it/34.webp)

QRコードをフレームにはめると、検索された口座がWoSのメインページに表示され、残高と履歴が表示される。