---
name: Stonewall x2
description: Stonewall x2トランザクションの理解と使用
---
![cover stonewall x2](assets/cover.webp)

> *すべての支払いをコインジョインにしましょう。*

## Stonewall x2トランザクションとは何ですか？

Stonewall x2は、支払い時のユーザーのプライバシーを高めることを目的とした、特定の形式のBitcoinトランザクションです。これは、その支払いに関与していない第三者と協力することで、2人の参加者間のミニコインジョインを模倣しながら、第三者への支払いを行います。Stonewall x2トランザクションは、Samourai WalletアプリケーションとSparrow Walletソフトウェアの両方で利用可能です。両者は相互運用が可能です。

その操作は比較的シンプルです：私たちは所有するUTXOを使用して支払いを行い、自身のUTXOを提供する第三者の助けを求めます。トランザクションは4つのアウトプットを生み出します：2つは同額で、1つは支払い受取人のアドレスに、もう1つは協力者のアドレスに送られます。3つ目のUTXOは協力者の別のアドレスに返され、彼らが初期額を回収できるようにします（マイニング手数料を除いて中立的な行動）、そして最後のUTXOは私たちのアドレスに戻り、これは支払いからのお釣りを構成します。

このように、Stonewall x2トランザクションでは3つの異なる役割が定義されます：
- 実際の支払いを行う送信者；
- トランザクションの全体的な匿名性を向上させるためにビットコインを提供し、最後には自分の資金を完全に回収する協力者（マイニング手数料を除いて中立的な行動）；
- トランザクションの特定の性質を知らずに単に送信者からの支払いを期待する受取人。

例を挙げてよりよく理解しましょう。Aliceはバゲットを買うためにパン屋にいます。その価格は`4,000 sats`です。彼女はビットコインで支払いをしながら、その支払いのプライバシーをある程度維持したいと考えています。そこで、彼女はこのプロセスで彼女を助けるために友人のBobに連絡します。
![schema stonewall x2](assets/en/1.webp)
このトランザクションを分析すると、パン屋がバゲットの代金として`4,000 sats`を受け取ったことがわかります。Aliceは`10,000 sats`を入力として使用し、`6,000 sats`を出力として受け取り、これはバゲットの価格に相当する`-4,000 sats`の純残高となります。Bobについては、`15,000 sats`を入力として提供し、`4,000 sats`と`11,000 sats`の2つの出力を受け取り、残高は`0`となります。
この例では、理解を容易にするために意図的にマイニング手数料を省略しました。実際には、トランザクション手数料は支払い送信者と協力者の間で均等に分けられます。

## StonewallとStonewall x2の違いは何ですか？

StonewallX2トランザクションはStonewallトランザクションと全く同じように機能しますが、前者は協力的であり、後者はそうではありません。見てきたように、Stonewall x2トランザクションは、支払いから外部の第三者の参加を伴い、トランザクションのプライバシーを高めるために自分のビットコインを提供します。典型的なStonewallトランザクションでは、協力者の役割は送信者によって担われます。

パン屋でのAliceの例を再訪しましょう。彼女がBobのような誰かを見つけることができなかった場合、彼女は一人でStonewallトランザクションを行うことができました。したがって、2つの入力UTXOは彼女のものであり、出力では3つを受け取っていたでしょう。
外部から見た場合、トランザクションのパターンは同じままであったでしょう。
![トランザクション ストーンウォール](assets/en/2.webp)
したがって、Samouraiの支出ツールを使用する際のロジックは以下の通りです：
- もし商人がPayjoin Stowawayをサポートしていない場合、Stonewall x2を使用して、支払い外の別の人と協力トランザクションを行うことができます。
- Stonewall x2トランザクションを行う人が見つからない場合は、Stonewall x2トランザクションの振る舞いを模倣して、一人でStonewallトランザクションを行うことができます。
- 最後の選択肢は、Samouraiが維持しているサーバーであるJoinBotとトランザクションを行うことで、要求に応じてStonewall x2トランザクションの協力者として機能することができます。

Stonewall X2トランザクションであなたを支援する意志のある協力者を見つけたい場合は、Samouraiユーザーが送信者と協力者を繋ぐために維持しているこのTelegramグループ（非公式）を訪れることもできます：[Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin)。

[**-> Stonewallトランザクションについてもっと学ぶ**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Stonewall x2トランザクションの目的は何ですか？

Stonewall x2の構造はトランザクションに大量のエントロピーを追加し、チェーン分析を混乱させます。外部から見ると、このようなトランザクションは2人の個人間の小さなCoinjoinと解釈されるかもしれません。しかし実際には、それは支払いです。この方法はチェーン分析に不確実性を生み出し、さらには誤った手がかりにもつながります。

アリス、ボブ、そしてパン屋の例に戻りましょう。ブロックチェーン上のトランザクションはこのように見えるでしょう：
![stonewall x2 公開](assets/en/3.webp)
一般的なチェーン分析のヒューリスティックに依存する外部の観察者は、「アリスとボブがそれぞれ1つのUTXOを入力として、それぞれ2つのUTXOを出力として使用して、小さなcoinjoinを行った」と誤って結論付けるかもしれません。![stonewall x2の誤解釈](assets/en/4.webp)
この解釈は間違っています。なぜなら、ご存知の通り、UTXOはパン屋に送られ、アリスは変更出力を1つだけ持ち、ボブは2つ持っているからです。
![トランザクション ストーンウォール x2](assets/en/1.webp)
たとえ外部の観察者がStonewall x2トランザクションのパターンを特定できたとしても、彼らは全ての情報を持っているわけではありません。同じ金額の2つのUTXOのうち、どちらが支払いに対応しているかを判断することはできません。また、支払いを行ったのがアリスかボブかを知ることもできません。最後に、2つの入力UTXOが2人の異なる人から来たものなのか、それとも単一の人がそれらを統合したものなのかを決定することもできません。この最後の点は、上で議論した古典的なStonewallトランザクションが、まさにStonewall x2トランザクションと全く同じパターンに従うという事実によるものです。外部から、そして文脈に関する追加情報なしに、StonewallトランザクションとStonewall x2トランザクションを区別することは不可能です。しかし、前者は協力トランザクションではないのに対し、後者はそうです。これはこの支出についてさらに多くの疑問をもたらします。
![StonewallかStonewall x2か？](assets/en/5.webp)


## Sorobanを介してPaynyms間の接続を確立する方法は？
Samouraiの他の共同取引（*Cahoots*）と同様に、Stonewall x2を実行するには、送信者と協力者の間で部分的に署名された取引の交換が関与します。この交換は、物理的に協力者と一緒にいる場合は手動で行うことができますし、Soroban通信プロトコルを通じて自動的に行うこともできます。
2番目のオプションを選択した場合、Stonewall x2を実行する前にPaynyms間の接続を確立する必要があります。これを行うには、あなたのPaynymが協力者のPaynymを「フォロー」し、その逆も同様でなければなりません。

**協力者のPaynymにアクセスする：**

まず、協力者のPaynymの支払いコードを取得する必要があります。Samourai Walletアプリケーションでは、協力者は画面の左上にある自分のPaynym（小さなロボット）のアイコンを押し、その後`+...`で始まる自分のPaynymのニックネームをクリックする必要があります。例えば、私の場合は`+namelessmode0aF`です。

![samourai paynym](assets/en/6.webp)
協力者がSparrow Walletを使用している場合は、「Tools」タブをクリックし、次に「Show PayNym」をクリックする必要があります。![paynym sparrow](assets/en/7.webp)
**Samourai Walletから協力者のPayNymをフォローする：**

Samourai Walletを使用している場合は、アプリケーションを起動し、同様に「PayNyms」メニューにアクセスします。PayNymを初めて使用する場合は、その識別子を取得する必要があります。

![request paynym samourai](assets/en/8.webp)

次に、画面の右下にある青い「+」をクリックします。
![add collaborator paynym](assets/en/9.webp)
その後、「PASTE PAYMENT CODE」を選択して協力者の支払いコードを貼り付けるか、「SCAN QR CODE」を押してカメラを開き、彼らのQRコードをスキャンできます。
![paste paynym identifier](assets/en/10.webp)

「FOLLOW」ボタンをクリックします。
![follow paynym](assets/en/11.webp)
「YES」をクリックして確認します。
![confirm follow paynym](assets/en/12.webp)
その後、ソフトウェアは「CONNECT」ボタンを提供します。このチュートリアルでは、このボタンをクリックする必要はありません。このステップは、BIP47の一環として他のPayNymに支払いを行う予定がある場合にのみ必要ですが、このチュートリアルとは関係ありません。
![connect paynym](assets/en/13.webp)
あなたのPayNymが協力者のPayNymをフォローしたら、逆のプロセスを繰り返して協力者もあなたをフォローできるようにします。その後、Stonewall x2トランザクションを実行できます。

**Sparrow Walletから協力者のPayNymをフォローする：**

Sparrow Walletを使用している場合は、ウォレットを開き、「Show PayNym」メニューにアクセスします。PayNymを初めて使用する場合は、「Retrieve PayNym」をクリックして識別子を取得する必要があります。
![request paynym sparrow](assets/en/14.webp)
次に、「Find Contact」ボックスに協力者のPayNym識別子（ニックネーム「+...」または支払いコード「PM...」のいずれか）を入力し、「Add Contact」ボタンをクリックします。
![add contact paynym](assets/en/15.webp)
ソフトウェアは「Link Contact」ボタンを提供しますが、このチュートリアルではこのボタンをクリックする必要はありません。このステップは、BIP47の一環として指定されたPayNymに支払いを行う予定がある場合にのみ必要ですが、これは私たちのチュートリアルとは関係ありません。
あなたのPayNymが協力者のPayNymをフォローしたら、逆のプロセスを繰り返して協力者もあなたをフォローできるようにします。その後、Stonewall x2トランザクションを実行できます。

## Samourai WalletでStonewall x2トランザクションを行う方法は？

Paynymsの接続を完了したら、ついにStonewall x2トランザクションを行う準備が整いました！これを行うには、Samourai Walletのビデオチュートリアルに従ってください：
![Stonewall x2チュートリアル - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Sparrow WalletでStonewall x2トランザクションを行う方法は？

Paynymsの接続を完了したら、ついにStonewall x2トランザクションを行う準備が整いました！これを行うには、Sparrow Walletのビデオチュートリアルに従ってください：
![Stonewall x2チュートリアル - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**外部リソース:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.