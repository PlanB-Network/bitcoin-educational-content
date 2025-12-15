---
name: Seedkeeper x SeedSigner
description: 如何使用 SeedSigner 與 Seedkeeper？
---

![cover](assets/cover.webp)



*感謝 [Satochip](https://satochip.io/) 團隊同意在本教程中重複使用 [他們的影片](https://www.youtube.com/@satochip/videos)。也感謝 [Crypto Guide](https://www.youtube.com/@CryptoGuide/)提供 SeedSigner 韌體的 fork，使其能支援智慧卡。



---

SeedSigner 是一個 wallet 硬體，您可以利用標準硬體自行組裝，通常是以 Raspberry Pi Zero 為主。這種 wallet 被稱為 「*無狀態*」：與市場上大多數其他型號（Coldcard、Trezor、Ledger 等）不同，它不會在永久記憶體中儲存任何資料，僅在 RAM 中運行。因此，您的 seed 投資組合永遠不會儲存在 SeedSigner 上。每次重新啟動時，您都需要填入 seed 以啟用裝置簽署您的交易。最常見的方法是將 seed 儲存為 QR 代碼，每次使用時掃瞄 (*SeedQR*)。



不過，這種方法也有相當大的風險：seed 必須保持明碼存取，以便掃描。如果發生失竊或入侵事件，攻擊者可以輕易取得 seed 並竊取您的 bitcoins。



為了克服這個弱點，SeedSigner 可以與 Satochip 所開發的智慧卡 [**Seedkeeper**](https://satochip.io/product/seedkeeper/) 結合。這可讓記憶短語 (或其他秘密) 儲存在由 PIN 碼保護的 secure element 中。Seedkeeper applet 是開放原始碼，其 secure element 已通過 EAL6+ 認證。與 SeedSigner 結合使用，可提供非常有趣的安全功能：您的金鑰完全離線管理，您可在可信賴的螢幕上簽署交易，而 seed 則受到智慧卡的實體保護，可抵抗實體攻擊。



您只需要以下項目即可完成安裝：




- 經典 SeedSigner 所需的一般設備：一個 Raspberry Pi Zero、一個 Waveshare 1.3 吋螢幕、一個相容的相機和一張 microSD 卡 (您可以在下面的 SeedSigner 教學中找到更多細節)；
- SeedSigner 延伸套件，可 [於 Satochip 官方商店](https://satochip.io/product/seedsigner-extension-kit/)取得，可讓您直接從 SeedSigner 讀寫智慧卡。另一個選擇是使用外接式智慧卡讀卡器，它可以透過纜線連接到 Raspberry Pi 上的 Micro-USB 連接埠。不過，我自己還沒有測試過這個解決方案；
- 一張 Seedkeeper，或者一張空白的智慧卡，用來安裝 Seedkeeper applet（Satochip 出售的擴充套件已包含一張空白的智慧卡）。



![Image](assets/fr/01.webp)



本教程涵蓋兩種情況：




- 如果您已有透過 SeedSigner 管理的 Bitcoin 產品組合，只需安裝新的韌體即可。然後您可以繼續使用現有的 wallet，這次使用 Seedkeeper 以增加安全性。
- 如果您還沒有與 SeedSigner 相關聯的 Bitcoin wallet，您需要遵循下面提到的教程中的**5**和**6**步驟。這些章節說明了如何使用 SeedSigner 來 generate 一個助記語句、透過 *SeedQR* 來儲存它，然後將這個 wallet 連接到 Sparrow Wallet 來管理它。我不會在這裡詳述這些程序，而且 ** 我假設您已經有一個可以運作的 Bitcoin wallet，並與 Sparrow 和您的 SeedSigner**進行設定。



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1.安裝韌體



要將 SeedSigner 與 Seedkeeper 搭配使用，您需要安裝一個不同於原始 SeedSigner 的韌體，以支援智慧卡讀取。為此，[我建議使用 "*3rdIteration*" 的 fork](https://github.com/3rdIteration/seedsigner)。下載 [最新版本的映像檔](https://github.com/3rdIteration/seedsigner/releases) (`.zip`)，以對應您使用的 Raspberry Pi 型號。



![Image](assets/fr/02.webp)



如果您還沒有，請下載 [Balena Etcher] 軟體 (https://etcher.balena.io/)，然後按以下步驟操作：




- 將 microSD 卡插入電腦；
- 啟動蝕刻器 ；
- 選擇您剛下載的 `.zip` 檔案；
- 選擇 microSD 卡為目標；
- 按一下「Flash!」。



![Image](assets/fr/03.webp)



等待程序完成：您的 microSD 現在已準備就緒，可以使用。現在您可以繼續組裝您的裝置。



有關韌體安裝和軟體驗證的詳細資訊（我強烈建議您採取的步驟），請參閱下列教學：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2.組裝智慧卡閱讀器



![video](https://youtu.be/jqE8HDMCImA)



首先將攝影機安裝在 Raspberry Pi Zero 上，小心地將其插入攝影機針腳，並用黑色卡舌鎖定。然後將 Pi 放在機殼底部，確保將連接埠對齊對應的開口。



![Image](assets/fr/04.webp)



然後將智慧卡讀卡器連接至 Raspberry Pi Zero 的 GPIO 引腳。



![Image](assets/fr/05.webp)



將塑膠蓋滑動到智慧卡讀卡機上，直到位置正確。



![Image](assets/fr/06.webp)



然後將螢幕加入擴充的 GPIO 引腳。



![Image](assets/fr/07.webp)



最後，將載有韌體的 microSD 卡插入 Raspberry Pi Zero 的側邊連接埠。



![Image](assets/fr/08.webp)



現在您可以透過 Raspberry Pi Zero 的 Micro-USB 連接埠或擴充裝置的 USB-C 連接埠連接 SeedSigner。兩種方式都可以。等待幾秒鐘啟動，然後您應該會看到歡迎畫面出現。



![Image](assets/fr/09.webp)



有關 SeedSigner 初始設定的詳細資訊，我推薦您參考以下教學：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3.使用 Seedkeeper applet 閃存智慧卡 (選用)



![video](https://youtu.be/NF4HemyEcOY)



如果您已經擁有 Seedkeeper，您可以跳過這一步，直接進入步驟 4。在本節中，我們將介紹如何在空白的智慧卡上安裝 Seedkeeper applet（DIY 方法）。



若要開始使用，請開啟 SeedSigner 上的「工具 > 智慧卡工具」功能表。



![Image](assets/fr/10.webp)



然後選擇 `DIY Tools > Install Applet`。



![Image](assets/fr/11.webp)



將您的智慧卡插入 SeedSigner 閱讀器，晶片朝下，然後選擇 `SeedKeeper` applet。



![Image](assets/fr/12.webp)



安裝時請耐心等待：安裝過程可能需要數十秒鐘。



![Image](assets/fr/13.webp)



一旦成功安裝 applet，您就可以繼續進行步驟 4。



![Image](assets/fr/14.webp)



## 4.在 Seedkeeper 上儲存現有的 SeedQR



![video](https://youtu.be/X-vmFHU9Ec8)



現在您的 Seedkeeper 已經開始運作，您可以將您的 Bitcoin wallet 記號儲存在智慧卡上。首先，像往常一樣開啟您的 SeedSigner，然後掃描您 wallet 的 *SeedQR* 將它載入裝置中。一旦 seed 匯入後，只要選擇`完成`即可。



![Image](assets/fr/15.webp)



載入 seed 後，進入「備份種子」功能表。



![Image](assets/fr/16.webp)



然後將 Seedkeeper 插入 SeedSigner 磁碟機，並選擇「至 SeedKeeper」選項。



![Image](assets/fr/17.webp)



然後，SeedSigner 會要求您輸入 Seedkeeper 的 PIN 碼。由於這是一張空白卡，因此尚未定義任何代碼。請輸入任何代碼以跳過此步驟，然後驗證。



![Image](assets/fr/18.webp)



SeedSigner 偵測到 Seedkeeper 尚未初始化 (即尚未設定密碼)。按一下「我了解」繼續。



![Image](assets/fr/19.webp)



現在選擇 Seedkeeper 的新 PIN 碼，介於 4 到 16 個字元之間。為了增加安全性，請選擇一個隨機的長密碼：它是保護您的記憶短語實體存取的唯一障礙。



切記在建立 PIN 碼後，立即將其儲存於可靠的密碼管理器中，或儲存於獨立的實體媒體中，視您的策略而定。在後者的情況下，請確定切勿將載有 PIN 的媒體與您的 Seedkeeper 放在同一個地方，否則保護功能將會失效。備份副本非常重要： **沒有這個 PIN 碼，您將無法存取您的 seed，您的比特幣將會丟失**。



![Image](assets/fr/20.webp)



然後，您可以定義一個與您的助記詞組相關的`標籤`。如果您在 Seedkeeper 上儲存了多個秘密，這個標籤就很有用，這樣您就可以輕鬆地識別它們。



![Image](assets/fr/21.webp)



您的記憶詞組已儲存在智慧卡上。



![Image](assets/fr/22.webp)



在安全策略方面，有幾種方法是可行的，這取決於您的需求和風險暴露程度。我個人建議您至少保留 2 份 seed 副本：




- 這是智慧卡的首創，您可以讓智慧卡輕鬆處理日常操作，例如驗證地址或簽署交易。這個方法很實用（我們會在第五部分看到），而且由於 PIN 碼提供的保護，它仍然是安全的，所以您可以讓它隨時隨地存取，而不會有太大的風險；
- 第二份未加密的助記語句複本，作為您投資組合的最終備份，僅在 Seedkeeper 遺失或遭竊時使用。由於此版本未加密，因此必須保存在另一個更安全的位置，以防止兩個備份同時受到損害。



根據您的保護策略和風險狀況，您也可以在數個不同的 Seedkeepers 上複製 seed，或建立數個記憶體的實體副本。若要進一步瞭解這些做法，請參閱下列教學：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5.從 Seedkeeper 載入 seed



![video](https://youtu.be/ms0Iq_IyaoE)



現在您可以使用 Seedkeeper 在啟動時將您的助記短語載入 SeedSigner，從而簽署您的 Bitcoin 交易。首先，插入 SeedSigner 開機，然後開啟`Seeds`選單。



![Image](assets/fr/23.webp)



然後選擇 `From SeedKeeper` 選項。



![Image](assets/fr/24.webp)



將 Seedkeeper 插入智慧卡讀卡機，然後輸入 PIN 碼以解除鎖定。按右下方的確認按鈕 `KEY3`，確認您的輸入。



![Image](assets/fr/25.webp)



Seedkeeper 可以包含多個機密，因此 SeedSigner 會提示您選擇要載入的機密。顯示的標籤對應於您在步驟 4 中定義的名稱。如果您像我一樣，只註冊了一個 seed，則只有一個選項可用。



![Image](assets/fr/26.webp)



您的 seed 現已載入。請比較螢幕上顯示的指紋與 Sparrow Wallet 設定中指定的指紋，確認這是正確的 wallet。這個指紋也是在 wallet 第一次建立時提供的。



如果您使用的是 passphrase，可以在此階段套用（請參閱本教程的第 6 部分）。否則，只要按一下「完成」即可。



![Image](assets/fr/27.webp)



之後您就可以像往常一樣使用 wallet：檢查您的送貨地址並簽署交易，就像使用經典的 SeedSigner 一樣。若要瞭解更多使用方法，請參閱專用教學 ：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6.使用 Seedkeeper 與 passphrase BIP39



您是否使用 passphrase 來保護您的 Bitcoin 產品組合？您也可以將它與您的 seed 一起註冊在您的 Seedkeeper 中。此解決方案可讓您快速將 wallet 載入 SeedSigner，而無需每次使用時在小鍵盤上手動輸入 passphrase。



我覺得這種方法特別有趣，因為它可以讓您受惠於 passphrase 的安全優勢，同時消除與日常使用相關的限制。以下是我推薦的配置範例：




- 將您的 seed 和 passphrase 存放在 Seedkeeper 中，並使用強大的 PIN 碼保護（這很重要）。此備份可讓您每天輕鬆使用您的 wallet。如果您願意，可以在第二個 Seedkeeper 上複製此資訊；
- 此外，請以紙本或金屬本保存一份清晰的記憶體和 passphrase 副本。如果您遺失了 Seedkeeper 或其 PIN 碼，這是您最後的備份。請務必將這些複本存放在不同的地方，以免同時遭到竊取。



在這種配置下，如果有人單獨取得您的明文助記語句，他們就無法在不知道 passphrase 的情況下竊取任何東西 (當然，前提是 passphrase 的強度足以抵擋暴力攻擊)。相反地，如果有人發現您的 passphrase 純文字，若沒有相對應的助記語句，就無法使用。



最後，如果有人成功取得內含 seed 和 passphrase 的 Seedkeeper 的實體存取權，在不知道 PIN 碼的情況下，他們將無法提取任何東西。與 passphrase 不同的是，此密碼無法被嘗試破解，因為智慧卡會在 5 次無效嘗試後自動鎖定。



因此，此配置的安全性基於兩個基本要素：




- 一個 **passphrase 強**：它必須是長的、隨機的，並包含多種字符。它的複雜性對您來說不是問題，因為您只需要在初始化時在鍵盤上輸入一次；之後，它就會由 Seedkeeper .NET 傳送；
- Seedkeeper 的 ** 強大 PIN 碼**：也是隨機且由 16 個字元組成。



要設定此設定，請先以一般方式將您的 passphrase 載入 SeedSigner。您可以遵循本教學中詳細說明的程序：



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

當含有 passphrase 的投資組合正確載入 SeedSigner 後，打開 `Seeds` 功能表，選擇與此投資組合相對應的足跡。請注意，此腳印與不含 passphrase 的組合腳印不同。



![Image](assets/fr/28.webp)



然後按一下 `備份 Seed`，將 Seedkeeper 插入磁碟機，並選擇 `至 SeedKeeper`。



![Image](assets/fr/29.webp)



輸入您的 PIN 碼來解鎖 Seedkeeper，然後為這個秘密指定一個標籤。您可以將指紋留作標籤，以維持某種形式的可信推诿，或明確陳述 `Passphrase Wallet`，例如。



![Image](assets/fr/30.webp)



您的 passphrase 投資組合現已在 Seedkeeper 上註冊。



![Image](assets/fr/31.webp)



下次啟動時，只需將 Seedkeeper 插入磁碟機，然後導覽到「種子 > 從 SeedKeeper」。



![Image](assets/fr/32.webp)



輸入您的 PIN 碼來解鎖智慧卡，然後選擇與您的 passphrase 對應的 wallet。



![Image](assets/fr/33.webp)



檢查 passphrase 和您的 wallet 印記，然後確認。



![Image](assets/fr/34.webp)



您現在可以使用 passphrase 存取您的投資組合，並像平常一樣在 SeedSigner 上簽署您的交易。



## 7.額外選項



在「工具 > 智慧卡工具」功能表中，您可以找到數個管理 Seedkeeper 的選項：





- 在「常用工具」功能表中，您可以 ：
 - 檢查卡片真偽；
 - 變更 PIN 碼 ；
 - 變更與秘密相關的標籤 ；
 - 停用 NFC 功能（建議僅使用晶片讀卡機） ；
 - 執行出廠重設。





- 在 `SeedKeeper Functions` 功能表中，您可以 ：
 - 查看註冊機密清單 ；
 - 儲存新的秘密 ；
 - 刪除現有的秘密 ；
 - 儲存或載入您的描述符（對 multi-sig 投資組合非常有用的功能）。





- 在 `DIY Tools` 功能表中，您可以 ：
 - 編譯 Seedkeeper applet ；
 - 將小程式安裝在空白卡片上；
 - 刪除 Seedkeeper 小程式可將其重設，使其再次變成空白。



現在您知道如何結合 SeedSigner 使用 Seedkeeper 安全地備份您的投資組合了。



如果這個設定讓您信服，請不要猶豫，支持讓它成為可能的專案：




- 透過直接 [在 Satochip 網站上](https://satochip.io/shop/) 購買您的設備；
- 透過 [捐款給 SeedSigner 專案](https://seedsigner.com/donate/)；
- 透過訂閱 [Crypto Guide 的 YouTube 頻道](https://www.youtube.com/@CryptoGuide/)，該頻道由維護託管修改後韌體的 GitHub 倉庫的人所經營。