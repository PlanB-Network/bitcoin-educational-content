---
name: Coin Wallet
description: Coin Walletについてのチュートリアルとプライバシーとセキュリティを強化する方法
---

![cover](assets/cover.webp)


このチュートリアルでは、[Coin Wallet](https://coin.space/)-モバイルデバイス向けの自己完結型暗号wallet、およびモバイルwalletアプリを使用する際のセキュリティとプライバシーの向上方法について説明します。



## Coin Walletについて


**Coin Wallet**は、2015年にBitcoinの愛好家チームによって作成された自粛/非自粛、オープンソースのwalletです。ウェブアプリケーションとして始まり、2017年にiOSアプリ、2020年にAndroidアプリがリリースされ、Google Play、Samsung Galaxy Store、Huawei AppGalleryで入手できる。


主な利点


- 非監護建築
- 完全な[オープンソース・コード](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- シンプルでクリーンなデザイン
- 不要な機能を省き、暗号通貨を安全に保管するという核心的な目的に集中
- クロスプラットフォーム対応：モバイル（iOS & Android）、デスクトップ、ウェブ
- RBF (Replace-By-Fee) サポート - 行き詰まった取引をいつでもスピードアップ。
- YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/)/FIDO2キーによるハードウェア2FA
- 内蔵Torサポート - プライバシーを最大限に守るため、すべてのトラフィックをTorネットワーク経由でルーティングします。



## 1️⃣ Coin Wallet の取り付け

Coin Walletはすべての主要プラットフォームで利用可能。



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [アンドロイド・グーグル・プレイ](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [アンドロイド（ギャラクシーストア）](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [全リリースリンク](https://github.com/CoinSpace/CoinSpace/releases)


デスクトップ（Windows、Linux、macOS）、ウェブアプリ、Tor経由でも利用可能。


![image](assets/en/01.webp)


## 2️⃣ Walletの作成と暗証番号の設定


walletは、passphraseを使用して作成されます。passphraseは、[2048語のリスト](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts)から生成された、スペースで区切られた12語のランダムなシーケンスです。

Coin Wallet は、他のウォレットからインポートされた 12、15、18、21、または 24 ワードのパスフレーズをサポートしています。


passphraseは、マスター秘密鍵を人間が読める形にしたものである。これは安全に保存されなければならない。passphrase は wallet へのアクセスや復元に必要なすべてのものである。passphrase を紛失した場合、wallet とすべての資金は永久に失われる。passphrase は決して共有してはならない。Coin Wallet はいかなるサーバーやデータベースにも鍵を保存しない。


**12単語のpassphraseは安全か？

ポジションごとに2048語の可能性があるため、2048¹²≒10³⁹の組み合わせがあり、Bitcoin秘密鍵に匹敵する128ビットのセキュリティが得られる。このレベルで十分だと広く考えられている。


![image](assets/en/02.webp)


passphraseをメモして確認した後、アプリは日常的なアクセスのために**4桁のPIN**を設定するよう求めます。利便性を高めるために、暗証番号の代わりに生体認証（指紋または顔認証）を有効にすることができます。


![image](assets/en/03.webp)



アカウント、キーの回復、passphraseのリセット、トランザクションの取り消しはありません。セキュリティはユーザーの全責任である。


ニーモニック・フレーズの保存に関する詳細なベストプラクティスについては、こちらをご覧ください：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ パスフレーズ＋暗証番号。いつ、どのように使用されるか


**passphraseはいつ必要ですか？

このような稀なケースに限ってだ：


- 新しいデバイスにwalletをセットアップする
- Coin Walletアプリの再インストール
- アプリ／ブラウザのデータを消去する（ローカルストレージ）
- アカウントからハードウェアキーを削除する
- 暗証番号を3回間違えて入力する（セキュリティのためアプリがロックされます）


日常的な使用では、4桁の暗証番号でwalletのロックは解除できる。


**パスフレーズ＋暗証番号：どのように機能するか**について

passphraseは真のマスター秘密鍵であり、どのようなデバイスでも機能する。

毎回12～24の単語を入力するのは不便なので、Coin Walletでは4桁の暗証番号を使用し、現在のデバイスで日常的に素早くアクセスできるようにしている。

単純な暗証番号だけではマスター・キーを直接保護するのに十分な安全性を確保できないため、暗号化には決して使用されない。その代わりに



- 暗証番号はサーバーに送られ、長い暗号tokenと交換される。
- このtokenは、デバイスにのみ保存されている暗号化されたマスター・キーを復号化する。


PINが3回間違って入力されると、サーバーはtokenを永久に削除する。ローカルに保存された鍵は使用できなくなり、walletを回復する唯一の方法は、オリジナルのpassphraseを入力することである。

この設計は、利便性と強力なフォールバック保護の両方を提供する。



## 4️⃣ ₿の受け取り - GW_48の種類とプライバシー


Coin Walletは、Bitcoinの3つのアドレスフォーマットすべてに対応：



- ネイティブ SegWit (Bech32)** - **bc1q** で始まる - 最低料金、推奨
- ネストされたSegWit（P2SH）** - **3**で始まる。
- レガシー（P2PKH）** - **1**で始まる。


![image](assets/en/04.webp)


**入金のたびに住所が変わるのはなぜですか？

これは意図的なものであり、プライバシーを保護するものです。コインを受け取るたびに、Coin Walletは自動的に新しい未使用アドレスを生成する。もし同じアドレスが再利用されたら（例えば毎月の給与のために）、誰でも簡単にブロックチェーン・エクスプローラーですべての受信トランザクションを合計し、総収入を知ることができる。


古いアドレスは永久に有効であり、そのアドレスへの受信は可能ですが、毎回新しいアドレスを使用することが推奨されるプライバシーのベストプラクティスです。


**Bitcoinの受け取り方法:**.

1.コインを開ける

2.受信**」をタップする。

3.希望するアドレスタイプを選択する（**bc1q** - `Native SegWit` が望ましい）。

4.QRコードを提示するか、住所をコピーして支払人に送信する。


**オプション - メクト（対面支払い用）:**.

同じ受信画面に「メクト」ボタンがある。

スイッチを入れると


- ニックネーム**（グラビア）を入力してください。
- あなたの現在地と受信アドレスは、メクトを有効にしている他のCoin Walletユーザーと一時的に共有されます。
- 彼らは小さな地図上であなたを発見し、タイプしたりスキャンしたりすることなくコインを送ることができる。


データは他のメクトユーザーのみが見ることができ、1時間後に自動的に削除されます（または、電源を切るとすぐに削除されます）。

メクトは完全にオプションで、プライバシーを最大限に確保したい場合はオフにしてください。


![image](assets/en/05.webp)


## 5️ ⃣ 送金 ȋitcoin


Bitcoinを送る：


1.コインを開く→**送信**をタップ

2.住所を貼り付けるか、QRコードをスキャンする

3.金額を入力（または**Max**をタップ）

4.取引速度を選択する：


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5.4桁の暗証番号で確認 → 取引が放送される


### 保留中の₿イットコイン取引をスピードアップする方法 (RBF)


低料金を選択し、取引が滞った場合：


1.履歴**タブへ

2.保留中の取引をタップする

3.タップ **アクセラレート** (料金別交換)

4.確認する → 高い手数料で再放送される


RBFアクセラレーションは現在、以下のものに対応している：

Bitcoin - アバランチ - バイナンス・スマートチェーン - イーサリアム - イーサリアムクラシック - ポリゴン


Replace-by-fee（RBF）の詳細：https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ 秘密鍵のエクスポート


**秘密鍵はいつ必要なのか？

(99%のユーザーはそんなことはしない。12語のpassphraseで十分だ)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Coin Walletで秘密鍵をエクスポートする方法


1.オープン **Bitcoin (BTC)**

2.ページを一番下までスクロールし、**秘密鍵のエクスポート**をタップします。

3.このアプリは、残高と**WIF**形式（5、K、またはLで始まる）の秘密鍵、およびQRコードですべてのアドレスを表示します。


空でないアドレスのみが表示されます。


**WIFキーの例

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


*次に何をすべきか（推奨）***。


- Electrum、Sparrow、BlueWallet、またはハードウェアwalletを開く
- 秘密鍵のインポート/掃引
- すべての資金は、現在のseedの新しい安全なアドレスに即座に移動します。


秘密鍵は決してプレーンテキストでデジタル保存しないでください。掃き出した後は、安全に削除することができる。


秘密鍵と派生パスに関する完全なガイドは、[How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)を参照のこと。



## 7️ ⃣ 技術詳細 - BIP39、BIP32、派生パス


Coin Walletは、ほぼすべての本格的な財布が採用しているBitcoinの公式規格に厳密に準拠しています。


BIP39` - passphraseがマスター秘密鍵になるまで


- デフォルトの単語数：12
- オプション passphrase/パスワード：なし（""）
- 初期エントロピー：128ビット（12ワード）→256ビット（24ワード）
- オープンソースの実装：https://github.com/paulmillr/scure-bip39
- 単語リスト：2048語の標準英語リスト
- 他のBIP39 walletから12、15、18、21、24語のフレーズのインポートをサポート


BIP32 + BIP44/BIP49/BIP84` - すべてのアドレスの決定論的生成

walletは1つのマスターキーから、厳密に定義された順序で何十億ものアドレスをgenerateすることができます。このため、Electrum、Sparrow、Trezor、Ledger、BlueWalletなどに同じ12語を入力すると、まったく同じアドレスと残高が表示される。


**Coin WalletでBitcoin**に使用された派生パス。


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

それぞれのパスの内側：


- 0` - 外部チェーン（支払いを受け取るために表示するアドレス）
- 1` - 内部チェーン（wallet自身が使用するアドレスを変更する）


Coin Walletは、これらの公的基準を変更することなく踏襲しているため、10年後、20年後、30年後であっても、あなたの資金は他の互換性のあるwalletでも回収可能である。


## 8️⃣ Torによる匿名性の強化


**Coin Wallet**でTorを使う理由

TorはBitcoinノード、取引所、オブザーバーからあなたの本当のIPアドレスを隠す。

すべてのトラフィック（残高、取引、スワップ）はTorネットワークを経由します。

これはアプリのソースコードに直接実装されている（[.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)を参照）。


Coin Walletには.onionアドレスが隠されており、v6.6.3（2024年12月）以降、**モバイルアプリに直接Torサポートが組み込まれています**。


### AndroidとiOSでTorを有効にする方法


1. **Orbot** - Torプロジェクトの公式アプリ（無料）をインストールする。


   - アンドロイド → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Orbotを開く → Start**をタップ

リストから**Coin Wallet**を選択し、walletだけがTorを使うようにする（オプションだが推奨）

接続されました」と表示されるまで待つ。


3. **Coin Wallet → 設定 → ネットワーク** を開きます。

Tor**を使う


4. **ステータスの確認

トップバーに**紫のTorオニオンアイコン**が表示される → すべてのトラフィックがTorを経由するようになる


![image](assets/en/06.webp)


これであなたの携帯電話Coin Walletは完全に匿名となります。


プライベートな暗号管理をお楽しみください！


## 結論


[Coin Wallet](https://coin.space/) - Bitcoin walletのパイオニアのひとつで、10年の開発歴がある。

暗号通貨を安全に保管するという中核的な使命に焦点を当て、意図的にシンプルに作られている。

広告も、ニュースフィードも、購読も、ソーシャル機能も、気を散らすものもない。

Coin Walletはシンプルさと安全性を第一に考えています。


## 📖 リソース


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39