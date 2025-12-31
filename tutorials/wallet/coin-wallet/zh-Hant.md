---
name: Coin Wallet
description: 有關 Coin Wallet 以及加強隱私權和安全性的方法的教程
---

![cover](assets/cover.webp)


本教學涵蓋 [Coin Wallet](https://coin.space/) - 適用於行動裝置的自加密 wallet，以及如何在使用行動 wallet 應用程式時提高安全性和隱私權。



## 關於 Coin Wallet


**Coin Wallet** 是由 Bitcoin 發燒友團隊於 2015 年創造的自監/非監、開源 wallet。它一開始是網頁應用程式，隨後在 2017 年推出 iOS 應用程式，並在 2020 年推出 Android 應用程式 - 可在 Google Play、Samsung Galaxy Store 和 Huawei AppGallery 上使用。


主要優勢：


- 非監護架構
- 完全 [開放原始碼](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- 簡潔乾淨的設計
- 專注於核心目的 - 安全地儲存加密貨幣，沒有不必要的功能
- 跨平台支援：行動裝置 (iOS & Android)、桌上型電腦、網頁
- RBF (Replace-By-Fee) 支援 - 隨時加速卡住的交易
- 使用 [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 鑰匙的硬體 2FA
- 內建 Tor 支援 - 透過 Tor 網路路由所有流量，以獲得最大的隱私權



## 1️⃣ 安裝 Coin Wallet

Coin Wallet 可在所有主要平台上使用。



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [所有發佈連結](https://github.com/CoinSpace/CoinSpace/releases)


也適用於桌上型電腦 (Windows、Linux、macOS)、Web 應用程式及透過 Tor。


![image](assets/en/01.webp)


## 2️⃣建立 Wallet 及設定 PIN 碼


wallet 是使用 passphrase 建立的 - 由 [2048 個單字的清單](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts) 產生的 12 個以空格分隔的單字隨機序列。

Coin Wallet 支援從其他錢包匯入的 12、15、18、21 或 24 字元密碼。


passphrase 是主私人密碼匙的人類可讀形式。它必須安全地儲存。passphrase 是存取或恢復 wallet 所需的全部資料。如果 passphrase 遺失，wallet 和所有資金將永久遺失。切勿共用 passphrase。Coin Wallet 不會將金鑰儲存於任何伺服器或資料庫。


**12 個字的 passphrase 是否安全？

每個位置有 2048 個可能的字，因此有 2048¹² ≈ 10³𠞙 組合 - 提供 ~128 位元的安全性，與 Bitcoin 私密金鑰相當。這個等級被廣泛認為是足夠的。


![image](assets/en/02.webp)


寫下 passphrase 並確認之後，應用程式會要求設定**4 位數的 PIN**，以便日常存取。為了增加便利性，您可以啟用生物辨識認證 (指紋或臉部辨識) 來取代使用 PIN 碼。


![image](assets/en/03.webp)



無帳號、無金鑰恢復、無 passphrase 重設、無交易逆轉。安全性完全由使用者負責。


如需儲存記憶詞組的詳細最佳做法：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣口令 + PIN。何時及如何使用


**何時需要 passphrase?

只有在這些罕見的情況下：


- 在新裝置上設定 wallet
- 重新安裝 Coin Wallet 應用程式
- 清除應用程式/瀏覽器資料 (本機儲存)
- 從帳戶中移除硬體金鑰
- 輸入錯誤的 PIN 碼三次（應用程式會鎖定以確保安全）


在日常使用中，4 位數 PIN 碼足以解鎖 wallet。


**密碼 + PIN：如何運作**

passphrase 是真正的主私人密碼匙，可在任何裝置上使用。

由於每次輸入 12-24 個字會很不方便，因此 Coin Wallet 使用 4 位數的 PIN 碼，以便在目前裝置上進行快速的日常存取。

單靠簡單的 PIN 碼並不夠安全，無法直接保護主密鑰，因此絕對不能用來加密。取而代之的是



- PIN 會傳送至伺服器，並交換一個長密碼 token。
- 此 token 可解譯只儲存在裝置上的加密主金鑰。


如果 PIN 輸入錯誤三次，伺服器會永久刪除 token。本機儲存的金鑰就無法使用，要恢復 wallet 的唯一方法就是輸入原始的 passphrase。

這種設計既方便又提供了強大的後備保護。



## 4️⃣接收₿itcoin - Address 種類和隱私權


Coin Wallet 支援所有三種 Bitcoin 位址格式：



- 原生 SegWit (Bech32)** - 以 **bc1q** 開始 - 費用最低，建議使用
- 嵌套 SegWit (P2SH)** - 以 **3** 開始
- 傳統 (P2PKH)** - 以 **1** 開始


![image](assets/en/04.webp)


**為什麼每次存款後地址都會改變？

這是有意為之，可保護隱私。每次收到硬幣時，Coin Wallet 會自動產生一個新的未使用地址。如果重複使用相同的地址 (例如，每月的薪水)，任何人都可以輕鬆地在區塊鏈探索器上總結所有收到的交易，並知道總收入。


舊地址永遠有效 - 您仍然可以向它們收件 - 但每次都使用新地址是建議的隱私權最佳做法。


**如何接收 Bitcoin:**

1.打開硬幣

2.點選 **接收**

3.選擇所需的位址類型 (最好是 **bc1q** - `Native SegWit`)

4.顯示 QR 代碼或複製地址並發送給付款人


**選項 - Mecto（用於當面支付）：**

在同一個 Receive 畫面上有一個 `Mecto` 按鈕。

開啟時


- 您會被要求輸入**暱稱** (gravatar)
- 您目前的位置 + 接收位址會暫時與其他同樣啟用 Mecto 的 Coin Wallet 使用者分享
- 他們可以在小地圖上發現您，並且不用打字或掃描就能傳送硬幣。


資料只對其他 Mecto 使用者可見，並在 1 小時後自動刪除 (或在您關閉時立即刪除)。

Mecto 完全是可選擇性的 - 如果您想要最大的隱私性，請關閉它。


![image](assets/en/05.webp)


## 5️⃣發送₿itcoin


發送 Bitcoin：


1.開啟硬幣 → 點選 ** 傳送**

2.貼上地址或掃描 QR 代碼

3.輸入金額 (或點選 **Max**)

4.選擇交易速度：


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5.使用 4 位數密碼確認 → 交易已廣播


### 如何加速待處理的₿itcoin 交易 (RBF)


如果您選擇了緩慢的費用，而交易被卡住：


1.前往 **歷史** 標籤

2.點選待處理交易

3.點選 **加速** (按費替換)

4.確認 → 交易將以較高費用重新廣播


RBF 加速目前支援下列項目：

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


更多關於 Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣匯出私人密碼匙


**何時需要私密金鑰？

(99 % 的使用者從來不會這樣做 - 12 個字的 passphrase 就夠了）


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### 如何在 Coin Wallet 匯出私密金鑰


1.開啟 **Bitcoin (BTC)**

2.滾動到頁面底部 - 點選 **匯出私人密碼匙**

3.應用程式會以 **WIF** 格式 (以 5、K 或 L 開頭) 顯示每個地址的餘額 + 其私人金鑰以及 QR 代碼。


只有非空的位址才會出現。


**WIF key**範例

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**下一步該做什麼（建議）**


- 開啟 Electrum、Sparrow、BlueWallet 或任何硬體 wallet
- 匯入/掃描私人密碼匙
- 所有資金立即移至您目前 seed 下的新安全位址


切勿以純文字方式數位儲存私人密碼匙。掃描之後，可以安全地將其刪除。


有關私人密碼匙和衍生路徑的完整指南： [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣技術細節 - BIP39、BIP32 和衍生路徑


Coin Wallet 嚴格遵循官方的 Bitcoin 標準，幾乎所有嚴謹的錢包都採用此標準。


`BIP39` - passphrase 如何成為主私人密碼匙


- 預設字數：12
- 可選 passphrase/密碼：無 ("")
- 初始熵：128 位元 (12 個字元) → 256 位元 (24 個字元)
- 開放原始碼實作：https://github.com/paulmillr/scure-bip39
- 詞彙表：標準英語詞彙表，包含 2048 個詞彙
- 支援從任何其他 BIP39 wallet 匯入 12、15、18、21 及 24 字元的詞組


`BIP32 + BIP44/BIP49/BIP84` - 確定產生所有位址

從一把主鑰匙，wallet 可以按照嚴格規定的順序 generate 數十億個地址。這就是為什麼在 Electrum、Sparrow、Trezor、Ledger、BlueWallet 等輸入相同的 12 個字，會顯示完全相同的地址和餘額。


**Derivation paths used in Coin Wallet for Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

每條路徑的內部：


- `/0` - 外部連鎖（您顯示要接收付款的地址）
- `/1` - 內部鏈 (變更 wallet 本身使用的位址)


由於 Coin Wallet 遵循這些公共標準，不做任何變更，因此即使在 10-20-30 年後，您的資金仍可在任何其他相容的 wallet 中收回。


## 8️⃣使用 Tor 增強匿名性


**Why use Tor in Coin Wallet**

Tor 會向 Bitcoin 節點、交換機和觀察者隱藏您的真實 IP 位址。

所有流量 (結餘、交易、交換) 都會經過 Tor 網路 - 沒有直接連線，也不會洩漏 IP。

這會直接在應用程式的原始碼中實作 (請參閱 [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31))。


Coin Wallet 具有隱藏的 .onion 位址，並自 v6.6.3 (2024 年 12 月) 起，**直接在行動應用程式中內建 Tor 支援**。


### 如何在 Android 和 iOS 上啟用 Tor


1. **安裝 Orbot** - Tor Project 官方應用程式 (免費)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **開啟 Orbot → 點選開始**

從清單中選取 **Coin Wallet** 以便只有 wallet 使用 Tor (選用但建議使用)

等待直到顯示 **「已連線」** (10-30 秒)


3. **開啟 Coin Wallet → 設定 → 網路**

開啟 **使用 Tor**


4. **檢查狀態**

頂部欄位出現**紫色 Tor 洋蔥圖示** → 現在所有流量都透過 Tor 傳送


![image](assets/en/06.webp)


就是這樣 - 您的行動裝置 Coin Wallet 完全匿名。


享受私人密碼管理！


## 📝 結論


[Coin Wallet](https://coin.space/)-真正的 Bitcoin wallet 先驅之一，擁有 10 年的發展歷史。

它刻意保持簡單，並專注於其核心任務：安全地儲存您的加密貨幣。

沒有廣告、沒有新聞饋送、沒有訂閱、沒有社交功能、沒有令人分心的東西 - 只有乾淨、快速、自我監控的 wallet，完全做它應該做的事。

Coin Wallet 將簡單性和安全性放在第一位 - 過去如此，將來也是如此。


## 📖 資源


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39