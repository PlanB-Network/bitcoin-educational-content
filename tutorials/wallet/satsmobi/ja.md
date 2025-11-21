---
name: Sats.mobi

description: 電報でアクセス可能なカストディアルWallet
---

![cover](assets/cover.webp)


このチュートリアルを書いたのは_ [Bitcoinキャンパス](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobiはTelegram上で動作するWalletであり、Lightning Network（カストディアン）のWalletのすべての機能に加えて、非常に楽しい一連の機能を備えています。このForkは、現在は廃止されているLightningTipBotのForkから派生したもので、そのすべての機能を継承しつつ、最新の機能を追加することで、より現代的なものとなっています。LNTipBotと同様、Sats.Mobiもオープンソースの理念を採用しています。Walletは、この[リポジトリ](https://github.com/massmux/SatsMobiBot)からクローンすることで、独立して設定・管理することができます。


シンプルに使いたい場合は、Telegramでチャットを始めるとボットであることがわかる。


## 設定

テレグラムの検索バーから「satsmobi」を探すと、[bot](@SatsMobiBot)へのリンクが表示されます。


**注意**：テレグラムでの検索が不安な場合は、以下の[リンク](https://t.me/SatsMobiBot)を使って安全にボットにアクセスしてください。


![image](assets/it/01.webp)


開始するために必要なことは、_START_を押すだけです。


![image](assets/it/02.webp)


Walletを探索するには、左下の_Menu_を選択します。


![image](assets/it/03.webp)


ここで、主要コマンドの中から_/help_を選ぶ。


![image](assets/it/04.webp)


Sats.Mobiは、すべての主な機能をリストアップしたメッセージを表示して私たちを歓迎します。起動すると、ボットはLNのAddressも作成し、Telegram上で選択したハンドルネーム（デフォルトでは一意である）にリンクする。このWalletでSatsを送受信するコマンドが表示され、後で見る他の機能も表示される。また、_/advanced_メニューを見てみるのも面白い。


![image](assets/it/05.webp)


Sats.Mobiは、プライバシーを得るために、匿名のLN Addressも作成した。ボットはコマンドで動作します。対応する単語をクリックするか、メッセージバーにスラッシュ「/」を入力し、その後に実行したいコマンドを入力するだけです。Walletを作ったばかりでも、例えば_/transactions_を選んでください。


![image](assets/it/06.webp)


このコマンドは最新のトランザクションのリストを表示する。


![image](assets/it/07.webp)


## Satsを迎える

Invoiceを作成してSatsを受け取るコマンドは_/invoice_です。Sats.MobiはBitcoinの最小単位であるSatoshiのみで動作するため、Invoiceを作成するにはメッセージバーにSatsで金額を書き、ボットとのチャットで送信する必要があります。

![image](assets/it/08.webp)


次の例では、210Satsを受け取ることを選択した。


![cover](assets/it/09.webp)


Invoiceが準備されるまでしばらく待つと、テキストとQRコードとして利用できるようになる。Invoiceを支払うと、Walletに残高が表示される。何らかの理由で合計が更新されない場合は、_/balance_と書いて`enter`キーを押す。


![image](assets/it/10.webp)


## 送信 Sats


Satsは非常に貴重な資産であり、軽々しく手放すことはできないが、Sats.Mobiはこの部分を魅力的なものにしているので、簡単なテスト（つまり、2、3のトライアル取引）を行うことは問題ないだろう。


### Invoiceの支払い


Invoiceを支払う最も簡単な方法は、`lnbc1xxxxxx`というメッセージ文字列をコピーし、_/pay_コマンドを入力した後にメッセージバーに貼り付けることです。 **正しい構文**では、コマンドの後にスペースを空ける必要があります。


![image](assets/it/11.webp)


Walletは確認を求めるメッセージを送る。Pay_をクリックすると、Invoiceに支払いが行われる。


![image](assets/it/12.webp)


Sats.Mobiは、効率的で接続の良いLightningノードに頼ることができ、常に正しいルーティングを見つけることに成功するため、支払いが失敗することはほとんどない。


### モバイルからの快適な支払い


テレグラムで閲覧できるSats.Mobiはモバイルでも利用できる。モバイルでの支払いに最も便利な機能はQRコードのスキャンだが、このWallet.Mobiは独立したアプリではなく、ソーシャルネットワークに含まれているため、設計上QRコードが欠けている。そのため、Sats.Mobiはできるだけモバイルで利用しやすいようにプログラムされている。実際、支払いたいInvoiceのQRコードを撮影した写真のような画像をデコードすることができる。


例えば、Invoiceに50Satsを支払うとする。


![image](assets/it/20.webp)


これを見せられたら、関連するQRコードの写真を撮ることができる。


![image](assets/it/21.webp)


そして、モバイルでTelegramを開き、Sats.Mobiとのチャットで、先ほど撮影したQRコードの写真を添付する。


![cover](assets/it/22.webp)


選択されると、ボットに送信される：


![image](assets/it/23.webp)

Sats.Mobiは写真を解読し、**即座に正しい説明とともに支払い要求**を提示します。チャットが確認を求めますので、_/pay_を押してください。

![image](assets/it/24.webp)


お支払いが処理されるまでしばらくお待ちください。


![image](assets/it/25.webp)


50Sats用のInvoiceは、カメラと統合されたスキャン機能を使用せずに達成された結果である。


### テレグラム・グループのSats.Mobi


![image](assets/it/27.webp)


LNTipBotを有名にし、Sats.MobiがTelegramにもたらす機能の中には、グループ内のメンバーにとって楽しくインタラクティブな体験をもたらすものがある。

オーナーはボットをグループチャットに招待し、Sats.Mobiを管理者に指名します。その瞬間から、メンバーはグループへの貢献に対して他のユーザーに報酬を与えることができるようになり、楽しみが始まります。


- _/tip_は、メッセージに返信することでチップを追加する；
- /send_は、LN Addressまたはテレグラム・ハンドルを受取人に指定して資金を送る；
- (_/advanced_メニューの)_/faucet_では、_/collect_をクリックすることで、グループの最も速いメンバーが収集できる一連のヒントを作成することができます；
- (_/advanced_メニューの_/tipjar_)は、グループ内のユーザーに送信できる別のタイプのディストリビューションを作成します。


これらのコマンドにはそれぞれ構文があり、メインコマンドメニューで説明されている。


もし私たちがグループのオーナーでなければ？問題ありません。創設者にSats.Mobiを招待するよう依頼し、グループの管理者として追加すれば完了です！


## 販売時点情報管理（POS）


Sats.Mobiの初回起動時に、ボットはユーザーのためにもう一つの機能を作成します： **POS**です。この「デバイス」は、ユーザーが_/pos_コマンドを実行するか、右下のコンソールから関連ボタンをクリックすることで起動します。実際、POSはウェブアプリで、Telegramのチャット上でポップアップとして開きます。


![image](assets/it/14.webp)


Interfaceは、ユーザーの個人的なTelegramハンドルを左上に表示し、他のPOSと同じように、キーパッドに金額を入力するだけで使用できる。例えば、あるサービスに対して21ユーロセントを徴収したいとしよう。Sats.MobiはSatsしかネイティブに管理していないので、頭の中で変換するのは簡単ではない。逆に、POSではユーロが会計単位として表示され、同時にSatoshiでの換算も表示される。


![image](assets/it/15.webp)

OK_をクリックするとInvoiceが表示され、QRコードで顧客に見せることもできるし、インスタント・メッセージで文字列として送信し、支払いを済ませることもできる。

![image](assets/it/16.webp)

![image](assets/it/17.webp)


もちろん、POSは携帯電話でも利用可能で、先に示したのと同じ方法でアクセスできる。


![image](assets/it/18.webp)


携帯電話の画面にもよく表示される：


![image](assets/it/19.webp)


## その他の特徴


Sats.MobiのWalletを完成させる機能は他にもあり、これまで見てきたように、Walletのコンセプトは支払いの受送信というオペレーションを超えたところにまで広がっている：


- _/nostr_：Walletを自分のNostrユーザーに接続してザップを受け取る；
- _/cashback_：購入時にキャッシュバックを得るために加盟店に提示できるコードを示す；
- ユーロでSatsを購入することができます；
- _/activatecard_：Sats.Mobi Walletでチャージ可能なNFCデビットカードのアクティベーションを要求する；
- _/link_：自分のZeusやBlue Walletのリンクを作成し、このWalletのリモコンとして使用できる。


## 結論

Sats.Mobiは、LNBitsの高度な機能を使ってLNTipBotで経験したことを思い出させてくれる、使って楽しいWalletです。ただし、「預かりサービス」であることを忘れてはならない。したがって、ごく少数のSatsを保持するために使用されるべきであり、Lightning Network資金のためのメインのWalletではありません。また、50万Satsに等しい本質的な容量制限もあり、この制限を超えないことが推奨される。


もし、非保護のLightning Network財布を探しているのなら、間違いなく他の製品を見ることをお勧めする。


---
### ドキュメンテーション


- [Github](https://github.com/massmux/SatsMobiBot)
- 動画](https://www.youtube.com/results?search_query=Sats.mobi)デモのプレイリスト