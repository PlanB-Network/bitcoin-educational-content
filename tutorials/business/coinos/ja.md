---
name: コイノス
description: Bitcoinの支払いを送受信するためのシンプルなウェブアプリケーション。
---
![cover](assets/cover.webp)



## はじめに



決済のデジタル化が進む中、Bitcoinは代替手段としての地位を徐々に確立しつつある。しかし、多くの初心者にとって、Walletの管理やBitcoinの支払いの受け入れは複雑に思えるかもしれない。



Coinosは、ウェブ開発者であるアダム・ソルティスによって設計されたプラットフォームで、彼の地域の商店がBitcoinの支払いを受け入れるのを助けるために最初のバージョンを作成した。



Coinosはシンプルで直感的に使えるプラットフォームです。Bitcoin、Liquid、Lightningのいずれでも、技術的なインストールをすることなく、ブラウザから直接、決済の送受信が可能です。誰でもアクセスできるCoinosは、Bitcoinの利点とウェブアプリケーション（*Progressive Web App*、またはPWA）のシンプルさを兼ね備えており、個人、商人、好奇心旺盛な人にとって理想的です。



***ビデオチュートリアル



![vidéo](https://youtu.be/GADLcQ4g8DU)



## コイノスの第一歩



Coinos**を手にする前に、技術的な知識や深い知識は必要ありません。ただし、Bitcoin、on chain、Lightning、Liquidの取引に関する基本的な理解があれば尚可。



### アカウントの作成



ブラウザで[Coinos]のウェブサイト(https://coinos.io/)にアクセスし、**Start in seconds**をクリックします。



![screen|220](assets/fr/03.webp)



ユーザー名**とパスワード**を入力し、**登録**をクリックしてください。



![screen|220](assets/fr/04.webp)



その後、メインのInterfaceポートフォリオにリダイレクトされます。パソコンでもスマートフォンでも、Interfaceは変わりません。



![screen|220](assets/fr/05.webp)



![screen](assets/fr/06.webp)



一番上、アバターの上にInterfaceのアイコンがあります：




- メイン**



![screen|220](assets/fr/07.webp)





- 領収書



![screen|220](assets/fr/08.webp)





- 取引履歴



![screen|220](assets/fr/09.webp)





- 出荷



![screen|220](assets/fr/10.webp)





- ドロップダウンメニュー



![screen|220](assets/fr/11.webp)



それなら




- あなたの**アバター** ；
- あなたの**ユーザー名** ；
- あなたのライトニングコイノスAddress、公開URL、支払いコード（LNURL Address）を含む**小さなドロップダウンメニュー**；
- と**鉛筆**のアイコンは、**アカウント**サブメニューにリダイレクトします。



![screen|220](assets/fr/12.webp)



中央には、**受信**と**送信**のアイコンがあります。受信**アイコンのすぐ上には、Walletの残高がSatoshiと選択した現地通貨で表示されます。



左下と右下には、選択した現地通貨建てのBitcoinの現在の価格と、選択した現地通貨建ての口座単位に相当するサトシの数が表示される。



![screen|220](assets/fr/13.webp)



Coinosは、ウェブWalletとして、PlayストアやApp Storeでは利用できません。しかし、インストールする方法はあります。ブラウザからCoinosにアクセスしたら、まず画面上部のCoinにある**3つの点**をクリックしてください。



![screen|220](assets/fr/14.webp)



次に、**ホーム画面に追加**を選択します。



![screen|220](assets/fr/15.webp)



最後に、**インストール**をクリックします。



![screen|220](assets/fr/16.webp)



ビンゴ！携帯電話のアプリケーションメニューに表示されるようになりました。



![screen|220](assets/fr/17.webp)



### ポートフォリオの構成



ドロップダウンメニュー**Interfaceボタンをクリックし、**Preferences**をクリックしてください。



![screen|220](assets/fr/18.webp)



Preferences**には4つのサブメニューがあり、ポートフォリオを設定することができます：





- アカウント**



このサブメニューでは、ユーザー名の変更、新しいパスワードの設定、アバター（プロフィール画像）の変更、バナー写真の追加、説明文の追加などができます。



![screen|220](assets/fr/19.webp)



![screen|220](assets/fr/20.webp)





- 販売時点情報管理**（POS）



ここで、言語と現地通貨を選択し、電子メールAddressを入力し、好みに応じて通知を有効にし、もしあなたがマーチャントなら、WalletをSquareに接続して支払いを促進することができる。



![screen|220](assets/fr/21.webp)



![screen|220](assets/fr/22.webp)





- ノストラ**



Nostrのアカウントを持っていれば、Coinosのアカウントとリンクさせることができます。



![screen|220](assets/fr/23.webp)





- 安全機能



このサブメニューでは、セキュリティコードの有効化、2ファクタ認証の有効化、さらに別のアカウントの追加ができる。



![screen|220](assets/fr/24.webp)



変更を加えるたびに**Save settings**をクリックして変更を保存することを忘れないでください。



![screen|220](assets/fr/25.webp)



設定が完了したら、Interfaceの**アイコンをクリックしてメイン画面に戻ります。



## Bitcoinの支払いの種類



Coinosは：





- メインチェーン（on chain）のBitcoin**とAddressのフォーマット（SegWit、Taproot、レガシーなど）；
- ライトニング** LNURL、Bolt 11、Bolt 12 ；
- 特に**Liquid**ネットワークと**ECASH**プロトコルを介して。



![screen|220](assets/fr/26.webp)



## ビットコインを受け取る



Coinosでビットコインを受け取るには、**受信**または**受信Interface**アイコンをクリックしてください。Interfaceを受け取ったら、どのAddressにビットコインを送るかを決めるために、送金者にどのネットワークでビットコインを送りたいかを尋ねてください。



### メインチャンネルでの受信



Bitcoin**をクリックしてください。



![screen|220](assets/fr/27.webp)



その後、QRコードと配達Addressが自動的に生成される。



![screen|220](assets/fr/28.webp)



特定の金額とメモ（ラベル）を定義することで、それらをパーソナライズすることができます。



![screen|220](assets/fr/29.webp)



![screen|220](assets/fr/30.webp)



あなたの**QRコード**と**あなた専用のBitcoin Address**の準備が整いましたので、あとは送信者に転送するだけでビットコインを受け取ることができます。



![screen|220](assets/fr/31.webp)



### Liquid経由のレセプション



その他のオプション**をクリックし、次に**Liquid**をクリックします。



![screen|220](assets/fr/32.webp)



![screen|220](assets/fr/33.webp)



QRコードとLiquid受信Addressも生成される。



![screen|220](assets/fr/34.webp)



Coinosは、Liquid **ビットコイン**（**L-BTC**）のみをこのAddressまたはこのQRコードに送付するよう注意を促しています。



金額とラベルを指定してパーソナライズすることができる。



![screen|220](assets/fr/35.webp)



それを送金者に渡し、**L-BTC**を受け取ってください。



![screen|220](assets/fr/36.webp)



### Lightning Networkレセプション



デフォルトでは、Interfaceの受付はLightningオプションで開きます。これにより、QRコードとライトニングAddressが表示され、特定の金額とメモでパーソナライズすることができます。



![screen|220](assets/fr/37.webp)



![screen|220](assets/fr/38.webp)



あなた専用の**QRコード**と**Lightning Address**が完成しました。送信者に送ると、すぐにサトシを受け取ることができます。



![screen|220](assets/fr/39.webp)



Lightning**で支払いを受けるには、メインのInterface Walletの小さなドロップダウンメニューを使用します。これにより、あなたのLightning Addressが表示されます。コピーしたり、QRコードに切り替えて簡単に共有することができます。



![screen|220](assets/fr/40.webp)



使用されているネットワークに関係なく、金額を入力するたびに、Coinosは自動的にサトシで相当する金額を表示します。



## ビットコインを送る



Coinos Walletからビットコインを送金する場合は、**送金アイコン**をクリックしてください。対応するInterfaceに移動すると、いくつかのオプションがあります：




- 受取人が提供するQRコードをスキャンする；
- コピーしたAddressをクリップボードに貼り付ける；
- 連絡先**」セクションで、すでに取引を行った相手のユーザー名を直接選択します；
- Bitcoin Address (On-Chain, Liquid or Bolt LN)、Invoice Lightning、または受取人のCoinosユーザー名を入力します。



![screen|220](assets/fr/41.webp)



Addressを入力または貼り付けた後、**Next**を押し、取引金額を入力し、再度**Next**を押す。



![screen|220](assets/fr/42.webp)



![screen|220](assets/fr/43.webp)



発送前の最後のステップは、情報を確認し、お客様に合ったネットワーク料金を調整することです。



![screen|220](assets/fr/44.webp)



手数料を調整するには、小さな三角形を押し、必要な執行速度に応じて希望の手数料レベルを選択します。取引の確認が早ければ早いほど、ネットワーク手数料は高くなります。また、Coinosは少額のサービス料を請求します。すべてのパラメータを確認し、お好みに合わせて調整したら、**送信**をクリックします。



![screen|220](assets/fr/45.webp)



おめでとうございます！お荷物が到着しました。



![screen|220](assets/fr/46.webp)



Coinosユーザー間で送金してみよう。ユニークなCoinos Addressを持っているAdam Soltysさんに21サトシを送ってみましょう： *adam*.




![screen|220](assets/fr/47.webp)



![screen|220](assets/fr/48.webp)



![screen|220](assets/fr/49.webp)



私のライトニングAddress経由でサトシを送ってみてもいい：Raimi@coinos.io。



Coinosユーザー間の取引にプラットフォーム手数料はかかりません。



## 取引履歴



取引履歴を見るには、**取引履歴Interfaceアイコン**をクリックしてください。



各取引について、金額、利用ネットワーク、日時が表示されます。メインのInterface Walletに表示される残高は統一残高ですが。



![screen|220](assets/fr/50.webp)



![screen|220](assets/fr/51.webp)




## その他の特徴



Coinosは.NETを含む多くの追加機能を提供している：





- コマーシャルのカルテ**（フランス語のみ）



Coinos Walletには、このプラットフォームを利用する加盟店のリストが地図上に掲載されている。掲載されている店舗はすべてBitcoinの支払いに対応しており、特にCoinos Walletでの支払いに対応しています。このマップを表示するには、**メニュー**をクリックし、**マップ**を選択します。すると、世界中のビジネスとその場所のリストが表示されます。



![screen|220](assets/fr/52.webp)



![screen|220](assets/fr/53.webp)



お店をクリックすると、そのお店のラベルが表示され、ラベルをクリックすると、そのお店のCoinosプロフィールが表示されます。Coinosを利用して、そのお店で買い物をすることができます。



![screen|220](assets/fr/54.webp)



![screen|220](assets/fr/55.webp)





- ヘルプデスク



Coinosを使用する上で問題がある場合は、：


1. または、アプリケーションのフォームに直接記入してください、


2. または、support@coinos.io まで直接メールをお送りください。



このメニューにアクセスするには、ドロップダウンメニューアイコンをクリックし、次に**アシスタンス**をクリックします。



![screen|220](assets/fr/56.webp)



![screen|220](assets/fr/57.webp)



## 安全性とベストプラクティス



ビットコインを使用する際、セキュリティは重要な問題です。Coinosはシンプルでシームレスな体験を提供しますが、ビットコインを保護することが重要です。





- 強力なパスワードを使う：パスワードは常にユニークで長く、推測されにくいものを選ぶ。
- デュアル認証（2FA）を有効にする。
- ログインは秘密にしてください：パスワードは決して誰にも教えないでください。CoinosがメッセージやEメールでパスワードをお尋ねすることはありません。
- ホスティングされたインスタンスに大金を保管しないこと：Coinosは日々の支払いには便利ですが、保管ソリューションであることに変わりはありません。日々の取引に必要な分だけを保管しましょう。より大きな金額については、非カストディアルのWalletを選択してください。



この記事を最後までお読みいただき、ありがとうございました。もしこのチュートリアルが役に立ったと思ったら、下にGreenの親指を残してください。お気軽にシェアしてください。ありがとうございました！



Aquaのチュートリアルをご覧になることをお勧めする。Bitcoin、Liquid、Lightningに対応したCoinosのようなWalletでもある。



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125