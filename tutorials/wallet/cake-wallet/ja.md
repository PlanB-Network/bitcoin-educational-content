---
name: ケーキ Wallet
description: Cake Walletとサイレント・ペイメントについてのチュートリアル
---

![cover](assets/cover.webp)


このガイドでは、[**Cake Wallet**](https://cakewallet.com/): Android、iOS、macOS、Linux、Windowsで利用可能な、オープンソース、非保護、プライバシー重視の多通貨Walletについて説明します。Bitcoin特有のプライバシー機能、**Silent Payments** (改良されたOn-Chainプライバシープロトコル)を介したBitcoinの送受信、そして非同期トランザクションのためのPayJoin v2の実装について説明します。


## 主な特徴



- [サイレントペイメント(BIP-352)**](https://BIPs.dev/352/)は、以前の[BIP 47ペイメントコード](https://silentpayments.xyz/docs/comparing-proposals/bip47/)を改良したもので、再利用可能なステルスアドレスで「PayNyms」とも呼ばれています。送信者がサイレント・ペイメントAddressを使用すると、送信者のWalletは異なるキーを使用してユニークなワンタイム・Addressを導き出し、それがユニークなワンタイム・Taproot Addressに結合される。Blockchainの記録は関連性のないトランザクションを示し、着信した支払いの連結を防ぎます。サイレント・ペイメントには、以下のような利点があります：
    - 再利用可能なアドレス：取引のたびに新しいAddressを作成する必要がないため、より良いユーザー・エクスペリエンスとプライバシーの向上を実現する。
    - コスト増はゼロ：サイレント・ペイメントは取引の規模やコストを増加させない。
    - 匿名性の強化：外部のオブザーバーは、サイレント・ペイメントAddressと取引を結びつけることができない。
    - 送り手と受け手のやり取りが不要：当事者間のコミュニケーションなしに取引を行うことができる。
    - 各支払いに固有のアドレス：誤ってAddressを再利用するリスクを排除。
    - サーバー不要：サイレントペイメントは専用サーバーを必要としません。
- PayJoin v2**は、送信者と受信者の入力を単一のトランザクションにマージすることで、トランザクショングラフ解析を緩和する。ケーキWalletは2つの重要な進歩を実装している：
    - 非同期トランザクション**：プライベート・トランザクションを完了するために、送信者と受信者が同時にオンラインである必要はなくなった。
    - サーバーレス通信**：どちらの当事者もPayJoinサーバーを実行する必要がないため、大きな技術的障壁が取り除かれます。
- Coinコントロール**は、トランザクション中にUTXOを手動で選択できるようにする。これにより、異なる起源の複数のUTXOを使用する際に、アドレスの偶発的な連結を防ぐことができる。
- TOR**のサポートにより、ユーザーはネットワーク・トラフィックをTorネットワーク経由でルーティングできる。
- RBF**（Replace-By.Fee）は、トランザクション送信後に手数料を調整することができます。


## 1️⃣ Wallet のセットアップ


Cake Walletは幅広いプラットフォームに対応しています。Android」、「iOS / macOS」、「Linux」、「Windows」から選択できます。  まずは、https://docs.cakewallet.com/get-started/、OSを選択してください。


![image](assets/en/01.webp)


インストール後、`PIN`（4桁または6桁）を設定します。すると


1.Walletの新規作成` (新規ユーザー用)

2.Walletの復元` (既存の財布用)


![image](assets/en/02.webp)


次の画面では、幅広い暗号通貨から選択することができる。Bitcoin`を選択して`次へ`をタップし、Walletを識別するために`Wallet名`を入力する。詳細設定」をタップすると、「プライバシー設定」が表示される。これらを変更する：



- フィアットAPI:** `Tor Only`を選択する（Torを経由して価格要求を行う）。
- Swap:** select `Tor Only` (Exchange のトラフィックを匿名化)


デフォルトでは BIP-39 seed タイプが生成されるが、オプションで Electrum seed タイプに変更することもできる。派生パスは以下の通り：



- Electrum：`m/0'`
- BIP-39`m/84'/0'/0`


もしLayerのセキュリティをさらに強化したいのであれば、`passphrase`を設定することができる。  passphraseの主な目的は、物理的な攻撃に対する追加の保護を提供することである。攻撃者がseedのフレーズを見つけたとしても、正しいpassphraseがなければWalletにアクセスすることはできません。言い換えれば、seedフレーズだけで1つのWalletを表し、seedフレーズ＋passphraseで元のWalletとは何のつながりもないまったく別のWalletを作ることができる。この機能により、passphraseで保護された「秘密の財布」も可能になり、もっともらしい否認ができる。強制的な状況では、passphraseで保護されたWalletに大きな資産を安全に保管しながら、seedのフレーズを明らかにすることができます。


既に自分のノードを運用している場合は、`Add New Custom Node` を切り替えて、自分のインフラ内でトランザクションとブロックを検証するための `Node Address` を提供する。完了したら `Continue` と `Next` をタップして Wallet を作成します。


![image](assets/en/03.webp)


次の画面では、免責事項が表示される：


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Mnemonicフレーズを保存するためのベストプラクティスについては、こちらのチュートリアルをご参照ください：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

わかりました。私のseedを見せてください！そして「seedを確認」をタップし、確認後「Walletを開く」をタップしてください。


## 2️⃣ 設定


ホーム画面」と「設定」を見てみよう。


ホーム画面にはさまざまな項目が表示されている：



- ハンバーガーメニューから「設定」を選択する。
- 利用可能残高
- サイレントペイメントAddressに送信されたトランザクションのスキャンを開始するサイレントペイメントカード
- プライバシー保護と料金節約機能としてPayJoinを「有効」にするPayJoinカード
- Walletの概要」、「受信」、「Bitcoinと他通貨とのスワップ」、「送信」、「購入」へのショートカットがある。


![image](assets/en/11.webp)


ハンバーガーメニュー」アイコンをタップすると、設定メニューが開きます。オプションを確認しよう。


![image](assets/en/05.webp)


### A - コネクション＆シンク 🔗 ．


ここでは、Walletの再接続、ノードの管理、自分のノードへの接続（推奨）ができる。Silent Payments Scanning`では、`BLOCKの高さからスキャンする`または`日付からスキャンする`を指定してスキャンをカスタマイズできる。


![image](assets/en/06.webp)


アルファ版の機能として、Torネットワークを介してトラフィックをルーティングするために、内蔵のTorを有効にするオプションもあります。


### B - サイレント・ペイメント設定 🔈.


この機能を表示するには、ホーム画面の Silent Payments カードをトグルします。Alwaysスキャン」を有効にすると、WalletはBlockchainにサイレント・ペイメントが着信していないか継続的にモニターすることができます。スキャン・パラメータを指定して、スキャン・プロセスをカスタマイズすることができます。


![image](assets/en/07.webp)


### C - セキュリティとバックアップ 🗝️


Walletを保護するために、アプリ内の指示に従ってバックアップを作成することができます。これにより、秘密鍵の安全なコピーが確保され、Walletを紛失または盗難された場合でも、Walletを復元することができます。さらに、seedのフレーズと秘密鍵の表示、PINの変更、生体認証の有効化、Sign / Verify、2FAのセットアップを行い、Layerをさらに保護することができます。


![image](assets/en/08.webp)


*注***：2025年9月現在、Androidデバイスの指紋バイオメトリクス認証は、少なくともクラス2のバイオメトリクス実装で機能することが要求されています。詳細は[こちら](https://source.android.com/docs/security/features/biometric/measure#biometric-classes)をご覧ください。ただし、この要件は将来変更される可能性があります。


### D - プライバシーの設定 🔒.


また、Torを使ってインターネット接続を暗号化し、外部ソースにアクセスする際のプライバシーを保護することで、Walletのセキュリティを強化することができます。さらに、Walletの情報の機密性を保つためにスクリーンショットを防止したり、取引ごとに新しいアドレスを作成するために自動生成アドレスを有効にしたり、不正な取引を防止するために売買アクションを無効にしたりすることができます。さらに、PayJoinを有効にすることもできる。


![image](assets/en/09.webp)


### E - その他の設定 🔧.


その他の設定により、手数料の優先順位を管理し、取引のデフォルト手数料レベルを設定することができます。これにより、現在のネットワーク利用状況を考慮しながら、サイレント・ペイメントに関連する取引手数料を管理することができます。


![image](assets/en/10.webp)


## 3️⃣ サイレントペイメントを使った₿ビットコインの受け取り


Bitcoinの受信にはいくつかのオプションとAddressのタイプがある。SegWit(P2WPKH)`*(bc1q...で始まる)*はデフォルトのオプションです。  この例では`Silent Payments`を選択してみよう。


サイレント・ペイメントを受け取るには、まず Wallet ケーキの「受け取る」アイコンをタップします。次に、受け取る予定の金額を入力します。Addressの種類を指定するには、もう一度画面上部の`Receive`をタップし、オプションから`Silent Payments`を選択します。


メイン画面には、再利用可能なサイレント・ペイメントQRコードとAddressが表示されます。予想通り、Addressはかなり長い：


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


ここで、BIP-352対応のWallet（Blue Walletなど）でこのQRコードを読み取り、支払いを送信します。Walletは、あなたのサイレントAddressからユニークな宛先Addressを導き出すことがわかります。


![image](assets/en/13.webp)


## 4️⃣ サイレントペイメントを使った₿イットコインの送金


Blue Walletはサイレント・ペイメントの「送信」しかできませんので、別のBIP 352対応Walletを受信側として使用します。この流れは通常のBitcoinの取引と同じです。



- ホーム画面で「送信」をタップする。
- 再利用可能な `sp1qq...` Address を貼り付けるか、アプリ内で直接QRコードをスキャンしてください。
- 利用可能残高から利用金額を選択する
- 画面下部の「送信」をタップし、トランザクションを確認する。


sp1qq...`Addressを入力すると、Walletは自動的に対応する`bc1p...`Taproot Address（P2TR）をバックグラウンドで派生させ、これがサイレント・ペイメントに使われる。


Coinコントロール」機能を使って、取引ごとに内部メモを書いたり、手数料設定を調整したり、特定のUTXOを選択したりすることも可能です。


![image](assets/en/14.webp)


右にスワイプして取引を確定する。


取引を送信すると、この連絡先をAddressブックに追加するかどうか尋ねられます。


![image](assets/en/15.webp)


## 6️⃣ PayJoin


PayJoinとは何なのか、おさらいしておこう(https://docs.cakewallet.com/cryptos/Bitcoin/#PayJoin)：


Payjoin v2は、Bitcoinのプライバシー保護と手数料節約のための機能であり、トランザクションの送信者と受信者が協力して単一のトランザクションを作成することを可能にします。このトランザクションは送信者と受信者の両方からの入力を持ち、Bitcoinに対する最も一般的な監視技術を破り、状況によってはより良いスケーリングと手数料の節約を可能にします。


PayJoinについてもっと知りたい方は、以下のチュートリアルもご覧ください。


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

PayJoinを使用するには、双方ともPayJoinと互換性のあるWalletが必要であり、受信者は少なくとも1つのCoinを持っているか、Walletに出力する必要があります。まずは以下の手順に従ってください：


1.ハンバーガーメニュー」をタップし、「プライバシー」ボタンをタップします。

2.PayJoinを使う」オプションの切り替え

3.  ホーム画面で「受信」をタップすると、PayJoinのQRコードとコピーボタンが表示されます（SegWitを選択した場合）。


![image](assets/en/16.webp)


## 7️⃣ その他の機能


その他にも、多通貨スワップ、異なるベンダーとの売買オプション、プリペイドカードやギフトカードを購入できるCake PayのようなCake特有のプログラムなど、いくつかの機能がある。


![image](assets/en/17.webp)


## 結論


これは、サイレント・ペイメント（BIP-352）やPayJoin v2などの機能により、Bitcoinの実用的なプライバシーを提供するCake Walletのレビューである。


サイレント・ペイメントは、使い捨てのアドレスを再利用可能なステルス・アドレスに置き換え、On-Chain における着信取引の連結を防止する。以前のバージョンの同期の問題は著しく改善されましたが、サイレント・ペイメントをスキャンして検出するために必要な計算要件がいくつか増加し、より多くのリソースと帯域幅が要求されます。


PayJoin v2は、余分な手数料や中央調整なしに、送り手と受け手の入力を1つのトランザクションに統合することで、連鎖分析を混乱させる。これは、すべての入力が送信者に属すると仮定できないことを意味するため、重要な利点である。


金銭的な匿名性を優先するユーザーにとって、Cake Walletは実行可能な選択肢である。Cake Walletは、プライバシープロトコルをコア機能に直接組み込んでおり、技術的な複雑さを伴わずにプライバシープロトコルにアクセスできる。パブリック・ブロックチェーン上の監視が強化される中、このようなツールは最も重要な取引上のプライバシーを維持するのに役立つ。Walletのランドスケープにおいて、これらの標準がより広く実装されることは歓迎すべきことだろう。


## リソース


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://BIPs.dev/352/](https://BIPs.dev/352/)


https://PayJoin.org/