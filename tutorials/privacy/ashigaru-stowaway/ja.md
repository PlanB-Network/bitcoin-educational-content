---
name: 足軽 - 密航者
description: 足軽でPayjoin取引をするにはどうすればいいですか？
---
![cover](assets/cover.webp)



> *ブロックチェーンのスパイは、自分たちが知っていると思っていることをすべて考え直さなければならない。

Payjoin は Bitcoin のトランザクション構造であり、支払先と直接連携することでユーザーの機密性 を高めるように設計されている。Payjoinの実装を容易にし、プロセスを自動化するためにいくつかの実装が存在する。その中で最もよく知られているのは間違いなくStowawayであり、当初はSamurai Walletチームによって開発され、現在はfork Ashigaruに統合されている。



## Stowawayの仕組みは？



前述の通り、足軽はPayJoinツール`Stowaway`を統合している。これはAndroidの足軽アプリで利用できる。Payjoinを行うには、受取人（協力者）がStowawayと互換性のあるソフトウェアを使用している必要があります。



Stowawayは、Samuraiが「Cahoots」と呼ぶ取引カテゴリーに基づいている。カフーツとは、Bitcoinブロックチェーンの外での情報交換を伴う、複数のユーザー間の共同取引である。足軽は現在、2つのカフーツ・ツールを提供している：Stowaway（Payjoins）とStonewallX2である。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahootsトランザクションでは、ユーザー間で部分的に署名されたトランザクションを交換する必要がある。このプロセスは、特に遠隔地で行う場合、長く退屈なものになる可能性がある。しかし、協力者が同じ場所にいる場合は、手作業で行うことも可能だ。具体的には、2人の参加者間で交換された5つのQRコードを連続してスキャンすることになる。



距離が離れると、この方法は複雑になりすぎる。これを改善するために、サムライは「*ソロバン*」と呼ばれるTorベースの暗号化通信プロトコルを開発した。ソロバンのおかげで、ペイジョインに必要なやり取りは自動化され、バックグラウンドで行われる。



これらの暗号化通信には、Cahoot参加者間の接続と認証が必要です。そのため、ソロバンはユーザーのPaynymsに依存しています。Paynymsの仕組みをまだよく知らない方は、こちらの専用チュートリアルをご覧ください：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

一言で言えば、Paynymはあなたのwalletに関連付けられた一意の識別子であり、暗号化された交換を含む様々な機能を有効にすることができます。識別子にはイラストが添えられています。例えば、これは私がTestnetで使っているものです：



![Image](assets/fr/01.webp)



**要約すると





- payjoin"＝特定の共同取引構造；





- Stowaway` = Payjoinの実装は足軽で利用可能；





- Cahoots`（カフーツ）＝サムライが彼らのあらゆる種類の共同取引につけた名前。特にペイジョインの「Stowaway（密航）」は、今日足軽で引き継がれた；





- soroban = Tor上で確立された暗号化通信プロトコルで、`Cahoots`トランザクションで他のユーザーとの共同作業を可能にする；





- paynym"＝"ソロバン "上で "チャフーツ "トランザクションを実行するために、他のユーザーとの通信を確立するために使用されるユニークなwallet識別子。



Payjoinsの仕組みとオンチェーンプライバシーにおける有用性については、こちらのチュートリアルをお勧めする：



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Paynyms間の接続を確立する方法を教えてください。



まずは足軽をインストールし、.NET Frameworkを作成してください：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

PayJoin(*Stowaway*)を含むCahootsのリモート取引を足軽経由で行うには、まず連携したいユーザーのPaynymを "フォロー "する必要があります。Stowawayの場合、これはビットコインを送りたい相手をフォローすることを意味します。他のPaynymをフォローする方法がまだわからない場合は、こちらのチュートリアルをご覧ください：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## 足軽でペイジョインをするには？



Stowawayの取引を行うには、画面左上のPaynymの画像をクリックし、`Collaborate`メニューを開きます。QRコードを直接交換する場合を除き、あなたと一緒に取引に参加する人も同じ操作を行う必要があります。



![Image](assets/fr/02.webp)



選択肢は2つあります：あなたが支払の送信者である場合は`Initiate`を選択し、あなたがこのpayjoinの受取人である場合は`Participate`を選択します。



![Image](assets/fr/03.webp)



あなたが受信者の場合、手続きはとても簡単です。ソロバンネットワークを利用した遠隔コラボレーションを行う場合は、`Participate`をクリックし、使用するアカウントを選択した後、`LISTEN FOR CAHOOTS REQUESTS`を押して、支払側から送信されるリクエストを待ちます。



![Image](assets/fr/04.webp)



一方、QRコードスキャンによる対面コラボレーションの場合、walletのホームページにアクセスし、画面上部のQRコードアイコンを押し、取引を開始する支払者から提供されたQRコードをスキャンする。



![Image](assets/fr/05.webp)



もしあなたが支払者の役割、つまり取引を開始する役割であれば、`Collaborate`メニューに行き、次に`Initiate`を選択します。



![Image](assets/fr/06.webp)



トランザクションのタイプは、Payjoin Stowawayを使用するため、このオプションを選択します。



![Image](assets/fr/07.webp)



そして、オンライン・コラボレーション（*ソロバン*経由の*カフーツ*）か、QRコード交換による対面でのコラボレーションのどちらかを選択することができる。



![Image](assets/fr/08.webp)



### カフーツ・オンライン



オンライン`オプションを選択した場合は、フォローしているPaynymsから受取人を選択します。



![Image](assets/fr/09.webp)



Set up transaction`をクリックし、支出元口座を選択します。



![Image](assets/fr/10.webp)



次のページで、受取人への送金額とチャージ料金を入力します。PSBTの交換時に受取人自身が送信するので、受取アドレスを入力する必要はない。



次に`Review transaction setup`をクリックする。



![Image](assets/fr/11.webp)



情報を注意深くチェックし、協力者が*Cahoots*リクエストを聞いていることを確認したら、緑色の`BEGIN TRANSACTION`ボタンをクリックして、ソロバンを介したPSBTの交換を開始する。



![Image](assets/fr/12.webp)



両方の参加者がトランザクションに署名するまで待ち、それを Bitcoin ネットワークにブロードキャストする。



![Image](assets/fr/13.webp)



### 対面式ディスカッション



対面での交換を希望する場合は、`STONEWALL X2` トランザクションタイプを選択し、`In Person / Manual` オプションを選択します。



![Image](assets/fr/14.webp)



Set up transaction`をクリックし、支出元口座を選択します。



![Image](assets/fr/15.webp)



次のページでは、受取人への送金額とチャージレートを入力します。PSBTの交換時に受取人が自分で送信するので、受取アドレスを入力する必要はない。



次に`Review transaction setup`をクリックする。



![Image](assets/fr/16.webp)



詳細を確認し、緑色の「BEGIN TRANSACTION」ボタンを押すと、QRコードスキャンによるPSBTの交換が開始されます。



![Image](assets/fr/17.webp)



QR CODEを表示`をクリックすると、あなたのQRコードが共同作業者に表示され、共同作業者がQRコードをスキャンします。すると相手も `SHOW QR CODE` をクリックして自分のQRコードを表示し、あなたはそれを `LAUNCH QR Scanner` でスキャンします。このプロセスを5つの交換ステップがすべて完了するまで繰り返します。



![Image](assets/fr/18.webp)



すべての交換が完了したら、取引の詳細を確認し、画面下部の緑色の矢印をドラッグして解除します。



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96).その構造は以下の通りである：



![Image](assets/fr/20.webp)



*クレジット： [mempool.space](https://mempool.space/)*



この取引を分析すると、入力側には私のUTXOである`164,211 sats`があり、実際の受取人のUTXOである`190,002 sats`がある。アウトプット側では、私は`63,995sats`の交換UTXOを受け取り、受取人は`290,002sats`のUTXOを受け取る。インプットとアウトプットを比較すると、受取人は私の実際の支払額に相当する`100,000 sats`を確かに獲得し、私はminingのコストを加えた`100,000 sats`を失ったことがわかる。



明らかに、私自身がトランザクションを構築したため、この構造を説明することができる。しかし、外部のオブザーバーにとっては、どのUTXOがどの参加者に属しているのかを、インプットでもアウトプットでも判断することは一般的に不可能である。



Bitcoinのオンチェーンプライバシー管理に関する知識を深めるには、Plan ₿ AcademyのBTC 204トレーニングを受講することをお勧めします：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c