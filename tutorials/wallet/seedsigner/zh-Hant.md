---
name: SeedSigner
description: Hardware Wallet 是 DIY、無狀態、經濟實惠且完全空氣封裝的產品
---

![cover](assets/cover.webp)



SeedSigner 是一個開放原始碼的 Hardware Wallet Bitcoin，任何人都可以使用廉價的通用電子元件自行製作。與 Ledger、Coldcard 或 Trezor 等商業產品不同的是，這不是由公司製造的即用型裝置：它是一個社群專案，讓每個人都能創造自己的裝置，並控制每個步驟。



SeedSigner 的設計是 100% ***air-gapped ***：它從不連線至網際網路，沒有 Wi-Fi 或藍牙 (以 Raspberry Pi Zero v1.3 為例)，也從不連線至電腦以 Exchange 資料。通訊完全透過 QR code Exchange 系統進行。具體來說，您的投資組合管理軟體 (例如 Sparrow wallet)會以 QR 碼的形式顯示要簽署的交易；您使用 SeedSigner 的相機掃描這些 QR 碼，然後裝置會使用暫存於其 RAM 中的私人金鑰簽署交易。最後，它會產生包含已簽署交易的 QR 碼，您使用軟體掃瞄這些 QR 碼，將交易傳送至 Bitcoin 網路。



![Image](assets/fr/001.webp)



SeedSigner 也是 ***Stateless*** 的。換句話說，與其他硬體錢包不同，它不會永久儲存您的 seed 或私人金鑰。每次您重新啟動時，它的記憶體就會完全清空，除非您設定裝置將您的設定儲存在 microSD 卡上。因此，每次使用時您都必須重新輸入您的 seed，最實際的方法是以 QR 代碼的形式儲存，以便在啟動時使用 SeedSigner 的相機掃描。這種操作模式大大降低了攻擊面：即使小偷竊取了您的裝置，他也不會在上面找到任何資訊，因為預設情況下它永遠是空的。



另一個儲存 seed 並與 SeedSigner 搭配使用的方法是使用 *SeedKeeper* 智慧卡與相容的讀卡機。這提供您一個非常強大的 *secure element* 來儲存您的 seed，同時使用 SeedSigner 螢幕來簽署交易。但這種特殊的配置是另一個專門教學的主題。在此，我們將專注於 SeedSigner 的基本使用：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner 專案在 Bitcoin 生態系統中佔有重要地位，因為它讓世界各地的每個人都有可能受益於先進的安全性，以保護他們的比特幣。它的主要優勢在於它的可及性：所需的硬體只需不到 50 美元即可購買。更重要的是，它能讓生活在受限制國家的人們使用標準電腦元件建立自己的 Hardware Wallet，這些元件很容易找到，也較少受到法規限制。



但即使不在這些特殊情況下，SeedSigner 對您來說也是一個有趣的選擇：它是開放源碼、無狀態且空中封鎖，並可減少與 Hardware Wallet 的 Supply 連結的攻擊媒介。



## 1.所需設備



要建立您的 SeedSigner，您需要以下元件：





- Raspberry Pi Zero
    - 建議使用 1.3 版，因為它既沒有 Wi-Fi 也沒有藍牙，可確保完全隔離。
 - W 和 v2 版本也相容，但內建 Wi-Fi/Bluetooth 晶片。因此，建議您從卡片中取出無線電模組，以物理方式將其停用。操作相對簡單，但需要精確度（Zero W 使用細鉗即可，而 v2 則需要使用 Hot 筆來移除隱藏模組的金屬板）。我不會在本教學中詳細說明，但您可以在這份文件中找到所有說明： *[Disabling WiFi/Bluetooth by hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - 請注意：某些 Raspberry Pi Zero 型號在銷售時沒有預先焊接 GPIO 引腳。您可以直接購買整合引腳的版本 (最簡單的解決方案)，或是另外購買引腳並自行焊接 (較複雜的解決方案)。
 - 別忘了附上 micro-USB 電源 Supply。



![Image](assets/fr/002.webp)





- Waveshare 1.3 吋螢幕 (240×240 px)** (法文)
    - 選擇此特定機型非常重要：其他類似的螢幕也存在，但解析度不同。如果沒有 240×240 px 的解析度，顯示器就無法使用。
    - 顯示器包含三個按鈕和一個迷你手搖桿，可作為使用者的 Interface。



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**相容的相機
    - 選項 1：標準攝影機配備寬金色墊子（請檢查與您外殼的相容性）。
    - 選項 2：更精巧的「*Zero*」攝影機，專為 Pi Zero 設計。



![Image](assets/fr/004.webp)





- MicroSD** 卡
    - 建議容量：4 至 32 GB。





- 房屋（選擇性，但建議）** （選擇性，但建議）** （選擇性，但建議）** （選擇性，但建議）** （建議）
    - 保護裝置，使用方便。
    - 最受歡迎的型號是 「*橙色藥盒*」，其 [開放源碼 STL 檔案可供 3D 列印使用](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures)。
    - 盒子也可從 [與專案連結的獨立經銷商](https://seedsigner.com/hardware/) 取得。



![Image](assets/fr/005.webp)



您可以單獨購買這些元件，或者為了更簡單，選擇包含所有必要硬體的現成套件。就我個人而言，我[從這個法國網站](https://bitcoinbazar.fr/)訂購了我的套件，但你也可以在[SeedSigner 專案硬體頁面](https://seedsigner.com/hardware/)找到世界各個地區的供應商清單。如果您想單獨購買元件，可以在主要的電子商務平台或專賣店購買。



## 2.準備軟體



一旦您準備好硬體，您就需要在 microSD 卡上安裝 SeedSigner 系統。要做到這一點，請到您日常使用的個人電腦，並插入您為 SeedSigner 準備的 microSD。



### 2.1.下載



前往 [該專案的官方 GitHub 套件庫](https://github.com/SeedSigner/seedsigner/releases)。在最新版本的軟體上，下載 ：




- 與您的 Pi 型號對應的 `.img` 映像。
- .sha256.txt`檔案。
- .sha256.txt.sig`檔案。



![Image](assets/fr/006.webp)



開始安裝前，先檢查軟體。



### 2.2 在 Linux 和 macOS 下驗證



首先直接從 Keybase 匯入 SeedSigner 專案的官方公開金鑰：



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



終端機應該會告訴你已經匯入或更新了一個金鑰。接下來，在簽章檔上執行驗證指令 (記得根據您的版本修改指令，這裡是 `0.8.6.`)：



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



如果一切正確，輸出應為 `Good signature`。這表示檔案 `.sha256.txt` 已經由您剛剛匯入的金鑰簽章，而且簽章是有效的。請忽略警告訊息 `警告：此金鑰未經可信簽章認證`：這是正常的，因為現在要由您來檢查所使用的金鑰是否屬於 SeedSigner 專案。



要做到這一點，請將顯示的指紋的最後 16 個字元與 [Keybase.io/SeedSigner](https://keybase.io/seedsigner) 上、其 [官方 Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) 上或 [SeedSigner.com](https://seedsigner.com/keybase.txt) 上公佈的檔案中的指紋進行比較。如果這些識別碼完全吻合，您就可以確定該金鑰確實是該專案的金鑰。如果有疑問，請立即停止，並向 SeedSigner 社群（Telegram、X、GitHub......）求助。



當金鑰被驗證後，您可以檢查下載的映像是否被修改 (記得根據您的版本修改指令，這裡是 `0.8.6.`)：



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- 在 Linux 下，此指令是內建的。
- 警告：「Big Sur (11)」之前的 macOS 版本不識別「--忽略遺失」選項。在這種情況下，請移除該選項，並忽略遺失檔案的警告。



預期的結果是「.img」檔案旁邊的「OK」。這證明上傳的影像與專案所發佈的影像完全相同，且未經修改。



### 2.3 視窗驗證



在 Windows 上，程序類似，但指令不同。首先安裝 [Gpg4win](https://www.gpg4win.org/)，並開啟 *Kleopatra* 應用程式。從 URL Keybase 匯入 SeedSigner 專案的公開金鑰：



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



接下來，在下載檔案所在的資料夾中開啟 PowerShell (`Shift`+按滑鼠右鍵 > `在此開啟 PowerShell`)。執行下列指令以檢查艙單簽章 (記得根據您的版本修改指令，這裡是 `0.8.6.`)：



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



如果一切正確，輸出應為 `Good signature`。這表示檔案 `.sha256.txt` 已經由您剛剛匯入的金鑰簽章，而且簽章是有效的。請忽略警告訊息 `警告：此金鑰未經可信簽章認證`：這是正常的，因為現在要由您來檢查所使用的金鑰是否屬於 SeedSigner 專案。



要做到這一點，請將顯示的指紋的最後 16 個字元與 [Keybase.io/SeedSigner](https://keybase.io/seedsigner) 上、其 [官方 Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) 上或 [SeedSigner.com](https://seedsigner.com/keybase.txt) 上公佈的檔案中的指紋進行比較。如果這些識別碼完全吻合，您就可以確定該金鑰確實是該專案的金鑰。如果有疑問，請立即停止，並向 SeedSigner 社群（Telegram、X、GitHub......）求助。



驗證金鑰後，您需要檢查映像檔案是否已損毀。為此，請在 PowerShell 中使用下列指令 ：



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Raspberry Pi Zero 2 的範例 (記得根據您的版本修改指令，這裡是 `0.8.6.`)：



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



然後 PowerShell 會計算映像檔的 Hash SHA256。將此 Hash 與 `seedsigner.0.8.6.sha256.txt` 中的對應值比較。




- 如果兩個值完全相同，則檢查成功，您可以繼續。
- 如果它們不同，則表示檔案已損壞或損毀。不要使用它，重新開始下載。



![Image](assets/fr/013.webp)



驗證成功可保證您的「.img」檔案是真實的 (經 SeedSigner 簽署) 且未經修改 (未修改)。這樣您就可以安全地進入下一步。



### 2.4.閃爍影像



如果您還沒有，請下載 [Balena Etcher] 軟體 (https://etcher.balena.io/)，然後 ：




- 將 microSD 卡插入電腦。
- 啟動蝕刻器。
- 選擇已下載並驗證的 `.img` 檔案。
- 選擇 microSD 卡為目標。
- 按一下「Flash!」。



![Image](assets/fr/014.webp)



等到程序完成後：您的 microSD 即可使用。現在是組裝時間！



## 3.SeedSigner 組件



準備好 microSD 卡並使用 SeedSigner 軟體閃存之後，您就可以進行最後的組裝。請慢慢來，因為有些零件是易碎的（尤其是桌布、攝影機和 GPIO 引腳）。



### 3.1 機殼準備



首先，打開您的機殼。檢查是否乾淨，內部扣件是否有殘留的 3D 列印塑膠。注意：




- 攝影機位置（前方的小圓孔）。
- 螢幕的開口。
- Raspberry Pi Zero 的 micro-USB 連接埠和 microSD 插槽的開孔。



### 3.2 攝影機安裝



找到 Raspberry Pi Zero 上的攝影機帶狀連接器：它是板側面的一條黑色細條，可以輕微提起打開。小心提起，不要用力：它應該只是傾斜幾毫米。



![Image](assets/fr/015.webp)



插入相機蓋。棕色/銅色部分應朝下。確保它穩固地插入連接器中，不要扭曲。



![Image](assets/fr/016.webp)



關閉黑色橫條以鎖定桌布（您會感到輕微的喀嚓聲）。輕輕檢查桌布是否固定在原位，不會移動。



![Image](assets/fr/017.webp)



然後將攝影機模組放入外殼上適當的孔中。視機型而定，它可能會直接卡入或需要一小條膠條來固定。鏡頭必須完全對齊，朝外。



### 3.3 安裝 Raspberry Pi Zero



如果您使用的是外殼，請將 Raspberry Pi Zero 板插入其中。小心地將連接埠與提供的開口對齊。



然後將 Waveshare 顯示器放置在 Raspberry Pi Zero 的上方。Pi 的 GPIO 針腳應該與顯示器的母頭完全對齊。慢慢地將顯示器壓到針腳上，每邊都要平均用力以避免彎曲。



![Image](assets/fr/018.webp)



如果您有機殼，請加上前面板和搖桿，完成組裝。



最後，將包含已修復軟體的 microSD 卡插入 Raspberry Pi Zero 的邊緣插槽。確保卡入到位。



### 3.4 首次啟動



將 micro-USB 電源線連接至專用連接埠。等待約一分鐘。SeedSigner 標誌應該會出現，接著是主畫面。



![Image](assets/fr/019.webp)



首先，請到「設定 > I/O 測試」功能表檢查各種元件是否正常運作。



![Image](assets/fr/020.webp)



測試所有按鈕，確定它們反應正確。然後按一下 `KEY1` 按鈕，檢查相機是否如預期般運作。這會拍攝一張照片。



![Image](assets/fr/021.webp)



### 3.5 攝影機調整



視您安裝 SeedSigner 的方式而定，相機可能會顯示倒置的影像。若要糾正這種情況，請移至 `設定 > 進階 > 攝影機旋轉 `，必要時選擇 180° 旋轉。



![Image](assets/fr/022.webp)



如果您更改了相機方向或希望日後變更其他設定 (例如 Interface 語言)，您需要啟用 microSD 上的持久設定。否則，由於 Raspberry Pi Zero 沒有持久記憶體，每次重新開機時，您的設定都會回復預設值。



若要執行此操作，請開啟 ` 設定 > 持久設定 ` 功能表，然後選擇 ` 已啟用 `。



![Image](assets/fr/023.webp)



如果一切正常，您的 SeedSigner 就可以使用了！



## 4.SeedSigner 設定



在建立您的 Bitcoin Wallet 之前，讓我們先設定 SeedSigner。由於 SeedSigner 是在沒有持久記憶體的 Raspberry Pi Zero 上執行，因此除非您將設定儲存在 microSD 卡上，否則不會自動儲存。因此請確定您已啟用此選項，否則這些設定會在重新開機時遺失（請參閱步驟 3.5）。



### 4.1 參數功能表存取



啟動 SeedSigner 並等待主畫面出現。使用搖桿，導覽至「設定」選項，然後按下中央按鈕進行驗證。現在您進入主設定功能表。



![Image](assets/fr/024.webp)



### 4.2 選擇投資組合管理軟體



然後進入 `Coordinator software` 功能表。



![Image](assets/fr/025.webp)



協調器」是指您的 SeedSigner 將透過 QR 代碼與之通訊的投資組合管理軟體。這個軟體可以安裝在您的電腦或智慧型手機上。它可以讓您管理您的比特幣，但無需存取您的私人密碼鑰匙。SeedSigner 仍然是唯一能夠簽署您的交易的裝置。



目前的韌體版本支援多種軟體套件：Sparrow、Specter、BlueWallet、Nunchuk 和 Keeper。就我而言，我使用的是 **Sparrow wallet**，我特別推薦它，因為它簡單且功能豐富。



如果您不知道如何安裝，可以參考此教學：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

只需從選單中選擇您所需的軟體即可。



![Image](assets/fr/026.webp)



### 4.3 單位和數量顯示



在 `Denomination Display` 功能表中，您可以選擇顯示金額的單位：




- `BTC`
- mBTC`（毫歐元-23，或 0.001 BTC）
- gW-20（薩托希，或 1/100,000,000 BTC）



一般而言，**Sats** 裝置對於小量使用最為實用。



![Image](assets/fr/027.webp)



### 4.4 進階設定



現在前往 `Advanced`（進階）' 功能表。在這裡您可以找到幾個有用的選項：




- gW-22 network`：僅當您希望在 Testnet 上使用 SeedSigner 時才需修改。
- qR code density`（QR 代碼密度）：調整每個 QR 代碼所含的資訊量。您可以保留預設值，除非您覺得掃描時難以閱讀。
- `Xpub export`： 啟用或停用透過 QR 碼將您的擴充公開金鑰 (`xpub`、`ypub`、`zpub`) 匯出到投資組合管理軟體 (我們稍後會用到這項功能，所以暫時不啟用)。
- `Script types`: 定義允許鎖定比特幣的腳本類型。您不需要修改這個參數，因為腳本類型會直接設定為 Sparrow。在此，只涉及 SeedSigner 有權操作的腳本。



### 4.5 語言選擇



最後，在「語言」功能表中，您可以變更 Interface 的語言，以符合您的喜好。



![Image](assets/fr/028.webp)



## 5.建立並儲存 seed



seed（或 Mnemonic 短語）構成您 Bitcoin 組合的基礎。它用於衍生您的私人金鑰和地址，並提供存取您的資金。SeedSigner 提供了幾種生成它的方法，我們將在本節中探討。



在我們開始之前，有幾個必要的提醒：




- 這個詞組讓您可以完全、不受限制地存取您所有的 bitcoins。** 任何擁有這個詞組的人都可以盜取您的資金，即使沒有實體存取您的 SeedSigner ；
- 通常，如果 Hardware Wallet 遺失或被盜，會使用 12 個字的短語來還原 Wallet。但由於 SeedSigner 是 *Stateless* 裝置，它從來不會註冊您的 seed。因此，您的實體備份不只是備份副本，而是**使用 Wallet 的唯一方法。如果您丟失了這些備份，您的比特幣將會永久丟失。所以請仔細備份，備份在多種媒體上，並放在安全的地方；
- 如果您剛開始使用，我強烈建議您閱讀本教程，詳細瞭解管理 Mnemonic 短語所涉及的風險：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 存取 seed 建立工具



從 SeedSigner 首頁畫面，移至 `Tools` 功能表。



![Image](assets/fr/029.webp)



現在您將 generate 您的 seed。seed 簡單來說就是一個大隨機數。它產生的隨機性越高，就越安全。SeedSigner 提供了兩種方法：




- 照相機"：seed 由照片的視覺雜訊產生。您拍攝一張隨機環境 (物件、景觀、人臉等) 的影像，其像素變化會被用來計算 generate 熵。這是一種快速的方法，但無法重現。
- 擲骰子」：您擲骰子來產生必要的熵。這種方法比較費時，但可以重複，因此可以驗證。如果您選擇這種方法，請遵循本教學中的建議 (這裡不需要計算校驗和，SeedSigner 會處理這個問題)：



https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 使用照片建立 seed



如果您選擇拍照方式，請點選 `New seed`（有相機圖示），拍照並驗證。然後選擇您的句子長度（12 或 24 個字），螢幕上會出現您要儲存的句子。以下步驟與 5.3 部分相同。



### 5.3 使用骰子建立 seed



在本教程中，我們使用**擲骰**的方法。按一下 `New seed`（有骰子圖示）。



![Image](assets/fr/030.webp)



然後選擇 Mnemonic 詞組的長度。12 個字已經提供足夠的安全層級，所以這是我建議的選擇。



![Image](assets/fr/031.webp)



擲骰子並使用游標輸入結果數字。按下中央按鈕以驗證每次輸入。如果您犯了錯誤，您可以返回。使用多顆不同的骰子，以減少任何不平衡骰子的影響。請確定在此操作過程中沒有人在監視您。



![Image](assets/fr/032.webp)



當您輸入 50 個擲字後，SeedSigner 就會產生出您的句子。 **如果您剛開始學習，請仔細遵循本教學的指示：**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 顯示和儲存 seed



在合適的實物支撐物（紙或金屬）上仔細寫下您的 Mnemonic 詞組。



![Image](assets/fr/033.webp)



### 5.5 檢查備份



為避免任何備份錯誤，SeedSigner 會要求您驗證您的備份。按一下「驗證」。



![Image](assets/fr/034.webp)



然後根據所要求的詞在句子中的順序輸入該詞。例如，在此我必須選擇句子中的第三個單詞。



![Image](assets/fr/035.webp)



如果您出錯，SeedSigner 會通知您，您必須重新開始，並確保在給您 Mnemonic 詞組時記下它。這個驗證步驟會確保您的備份是正確和完整的。驗證完成後，螢幕會顯示「備份已驗證」。



![Image](assets/fr/036.webp)



如需更完整的還原測試，請遵循此教程 ：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 瞭解「無狀態裝置」的概念



SeedSigner 是一個沒有永久記憶體的裝置。這表示您的 seed 永遠不會儲存在裝置內（例如與 Ledger、Trezor 或 Coldcard 不同）。只要您關掉電源，seed 就會從 RAM 中完全消失。SeedSigner 重新啟動時，會回到空白狀態：您需要再次將 seed 交給它，才能簽署交易。



這提供了必要的保護。與其他硬體錢包不同，SeedSigner 是以 Raspberry Pi Zero 為基礎，沒有任何實體保護，包括 *secure element*。但由於沒有儲存任何敏感資料，即使裝置受到實體破壞，攻擊者也無法擷取您的私密金鑰或花費您的比特幣。



另一方面，此架構也意味著額外的責任：如果沒有備份，您的資金肯定會損失。這就是我建議**雙重備份**的原因。您已經有了您的復原短語：這是您的主要長期備份，將保存在安全的地方。現在，我們要以 **QR 代碼的形式來建立這個詞組的副本。



每次使用 SeedSigner 時，您都要用裝置的相機掃描這個 QR 碼，這樣它就會在您簽署交易時，將您的 seed 暫時載入其記憶體中。這個供日常使用的第二個備份也必須小心保管：任何持有這個 QR 代碼的人都可以完全存取您的比特幣。


我也建議您將 QR 代碼和 Mnemonic 詞組分別存放在兩個不同的地方，以免在索賠時遺失所有東西。



最後，一個更進階、更安全的選擇是使用 SeedSigner 搭配 **SeedKeeper**，將 seed 儲存在 secure element 中。要瞭解更多資訊，請參閱本教程 ：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 寫入主密鑰指紋



驗證完成後，SeedSigner 會顯示 Wallet 主密鑰的指紋。這個指紋可以識別您的 Wallet，並確保您將來使用正確的復原詞組。它不會透露任何關於您私人金鑰的資訊，因此您可以安全地將其儲存在數位媒體上。只要確保您保留一份可存取的複本，並且絕對不會遺失即可。



![Image](assets/fr/037.webp)



也是在這個階段，您可以添加一個 **passphrase BIP39** 來加強 Wallet 的安全性。根據您的備份策略，這個選項也許是值得的，但它也有風險：如果您遺失了 passphrase，您將永遠無法存取您的比特幣。



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

如果您還不熟悉 passphrase 的概念，我邀請您閱讀這份相關的全面教學：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 將 seed 儲存為 QR 格式 (*SeedQR*)



SeedSigner 可讓您將 seed 轉換成紙本 QR 碼，稱為 *SeedQR*。此方法可簡化重新載入您的 Wallet，因為它避免手動重新鍵入每個字。



要做到這一點，您需要與 Mnemonic 短語長度相對應的空白紙張或金屬 QR 碼。如果您已經為 SeedSigner 購買了完整的套件，範本通常都包含在內。如果沒有，您可以在這裡下載並列印（或手動複製） ：




- [12字格式](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24字格式](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [精簡格式 12 個字](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [精簡格式 24 個字](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



從 seed 畫面，選擇「備份 seed」。



![Image](assets/fr/039.webp)



然後選擇 `Export as SeedQR`。



![Image](assets/fr/040.webp)



然後根據可用的紙張範本，選擇所需的格式（普通或精簡）。



![Image](assets/fr/041.webp)



按一下 `Begin` 開始建立 *SeedQR*。SeedSigner 接著會顯示一系列網格 (A1、A2、B1 等)，每個網格對應程式碼的一部分。



![Image](assets/fr/042.webp)



仔細複製儲存表上的每個黑點，然後用搖桿移到下一個 BLOCK。慢慢來：一個簡單的錯位就可能導致 QR 代碼無法使用。



一些提示：




- 一開始使用鉛筆，這樣您可以修正任何錯誤，完成後再回到使用黑色細筆；
- 在正方形中間有一個居中的點就可以了，不需要完全填滿。



![Image](assets/fr/043.webp)



然後按一下「確認 SeedQR」，並掃描您的 QR 代碼以檢查是否正常運作。



![Image](assets/fr/044.webp)



如果顯示 `Success` 訊息，表示您的 *SeedQR* 有效：您可以進行下一步。



![Image](assets/fr/045.webp)



**請嚴格保存此表，就像您的復原短語一樣。任何持有此 QR 代碼的人都可以重建您的私人密碼匙並竊取您的 bitcoins。



恭喜您，您的 Bitcoin 產品組合現在已開始運作！我們現在要將它的公共元件匯入**Sparrow wallet**，以方便管理。



## 6.將 Wallet 匯入 Sparrow



一旦您的 SeedSigner 設定完成，您的 seed 正確生成並儲存，下一步就是將這個投資組合連接到管理軟體，如 Sparrow wallet。您的 seed 將永遠保持離線狀態，因為只有您的投資組合的公開部分會傳送到 Sparrow。這將使軟件能夠顯示您的地址、交易並建立新的交易，但卻無法花費您的比特幣。要使用您的比特幣，您的 SeedSigner 必須簽署 Sparrow 準備的交易。



### 6.1 準備 SeedSigner



插入包含作業系統的 microSD，開啟 SeedSigner，然後載入您剛從備份 QR 碼中建立的 seed。在主畫面上，選擇「掃瞄」，然後用 SeedSigner 掃瞄您的 SeedQR。



![Image](assets/fr/046.webp)



檢查主密鑰上的指紋是否與 Wallet 上的指紋相符。如果您使用的是 passphrase，請在此階段輸入。



![Image](assets/fr/047.webp)



這會帶您進入作品集的選單，我的作品集名為 `d4149b27`。如果您回到主畫面，選擇 `Seeds`，然後選擇與您的作品集相對應的印刷品。然後點擊 `Export Xpub`。



![Image](assets/fr/048.webp)



選擇投資組合類型。在我們的例子中，這是單一投資組合：選擇 `單一 Sig`。



![Image](assets/fr/049.webp)



接下來是腳本標準的選擇。就交易成本而言，最新且最經濟的是 `Taproot`。因此，我建議您選擇這個標準。



![Image](assets/fr/050.webp)



將會出現警告訊息。這是正常的：這個擴展的公開金鑰 (`xpub`)允許您查看所有從您的 seed (在第一個帳戶上) 衍生出來的地址。它不允許您使用您的資金，但會顯示您的投資組合結構。如果它洩露了，對您的隱私是個問題，但對您的比特幣安全卻不是：它允許您看到它們，但不能花掉它們。



如果您滿意顯示的資訊，請按一下 `I Understand`，然後按一下 `Export Xpub`。



SeedSigner 會以動態 QR 代碼的形式產生您的 xpub，其中包含您在 Sparrow wallet 中管理投資組合所需的所有資料。



![Image](assets/fr/051.webp)



您可以使用搖桿調整螢幕亮度，讓 QR 碼掃描更容易。



### 6.2 將新的組合匯入 Sparrow wallet



請確認您的電腦已安裝 Sparrow wallet 軟體。如果您不知道如何正確下載、檢查和安裝，請參閱我們的完整教學：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

在電腦上開啟 Sparrow wallet，然後在功能表列按一下 ` 檔案 → 匯入 Wallet`。



![Image](assets/fr/052.webp)



向下捲動到 `SeedSigner`，然後選擇 `Scan...`。您的網路攝影機將開啟：掃描 SeedSigner 螢幕上顯示的動態 QR 代碼。



![Image](assets/fr/053.webp)



為您的組合指定一個名稱，然後按一下「建立 Wallet」。Sparrow 接著會要求您設定密碼，以鎖定本機對此 Wallet 的存取權限。選擇一個強大的密碼：它可保護您存取 Sparrow 中的投資組合資料（公開金鑰、地址、標籤和交易歷史）。日後還原投資組合時不需要此密碼：此目的只需要您的 Mnemonic 短語（可能還需要您的 passphrase）。



我建議您將此密碼儲存在密碼管理器中，以免遺失。



![Image](assets/fr/054.webp)



您的關鍵程式庫現已成功匯入。



![Image](assets/fr/055.webp)



然後檢查 Sparrow 中顯示的 「主指紋」 是否與之前在 SeedSigner 中記錄的相符。



您的 SeedSigner 和 Sparrow wallet 現在已安全地連結在一起。Sparrow 充當一個完整的管理 Interface，而 SeedSigner 仍然是唯一能夠簽署您的交易的裝置。現在您可以在完全隔絕空氣的配置下接收和傳送比特幣了。



## 7.收發比特幣



您的 SeedSigner 和 Sparrow wallet 現在已經配置好一起工作了。在最後一節，我們將看一下如何使用此配置來接收和發送 bitcoins。



### 7.1 接收比特幣



#### 7.1.1 產生接收 Address



在您的電腦上，打開 Sparrow wallet，使用密碼解鎖您的 SeedSigner Wallet。確定軟體已連接到伺服器（右下方有缺口）。在側邊欄中，點擊 `接收`。



![Image](assets/fr/056.webp)



顯示新的 Bitcoin Address。您會看到 ：




- 文字 Address（如果您像我一樣使用 P2TR，則以 `bc1p...` 開頭）、
- 對應的 QR 代碼、
- 用於追蹤交易的 `Label` 欄位。



我強烈建議您在 Wallet 上的每張 Bitcoin 收據上加上標籤。這可讓您輕鬆識別每張 UTXO 的來源，並改善您的隱私權管理。若要深入瞭解這個重要主題，您可以查看 Plan ₿ Academy 上的專門訓練 ：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

若要新增標籤，只需在「標籤」欄位輸入名稱，然後確認即可。



例如：



```txt
Label : Sale of the Raspberry Pi Zero
```



您的 Address 現在與所有 Sparrow 區段中的此標籤相關聯。



![Image](assets/fr/057.webp)



#### 7.1.2 SeedSigner 上的 Address 驗證



在分享您接收的 Address 之前，檢查它是否屬於您的 seed 是非常重要的。此步驟可確保您的 SeedSigner 能夠簽署與此 Address 相關的交易。它也可以防止 Sparrow 顯示偽造 Address 的可能攻擊。請記住，Sparrow 是在不安全的環境 (您的電腦) 上執行，它的攻擊面遠大於您的 SeedSigner，因為您的 SeedSigner 是完全隔離的。這就是為什麼在您使用 Hardware Wallet 驗證之前，絕對不能盲目相信 Sparrow 上顯示的任何收件人 Address。



在 Sparrow 上，按一下 Address 的 QR 代碼可將其放大：然後就會全螢幕顯示。



![Image](assets/fr/058.webp)



在您的 SeedSigner 上，從主功能表中選擇 `Scan`。掃描顯示在電腦螢幕上的 QR 碼，然後選擇與您的 Wallet 相對應的 seed（在我的個案中，是 `d4149b27` 指紋）。



![Image](assets/fr/059.webp)



如果掃描的 Address 與您的 seed 所衍生的 Address 吻合，SeedSigner 螢幕將會顯示訊息：Address 已驗證」。



![Image](assets/fr/060.webp)



這證明 Address 屬於您的 Wallet，您可以放心地從 Wallet 接收比特幣。



#### 7.1.3 收到資金



現在，您可以將此 Address（以文字或 QR 代碼形式）傳達給需要向您發送 Satss 的個人或部門。一旦交易在網路上廣播，它就會出現在 Sparrow wallet 的「交易」標籤中。



![Image](assets/fr/061.webp)



### 7.2 傳送 bitcoins



使用 SeedSigner 傳送 bitcoins 需經過 3 個步驟：




- 在 Sparrow 中建立交易 ；
- 在 SeedSigner 上簽署交易 ；
- 透過 Sparrow 進行交易的最終分配。



兩台裝置之間的所有交換都完全使用 QR 代碼。



#### 7.2.1 在 Sparrow 中建立交易



在 Sparrow wallet 中，您可以點選左側邊欄的 `Send` 選項卡。不過，我比較喜歡使用`UTXOs`標籤，它可以讓您實踐 "*Coin Control*"。此方法可讓您精確控制所使用的 UTXOs，因此您可以控制交易過程中所透露的資訊。



在 `UTXOs` 標籤中，選擇您要花費的硬幣，然後按一下 `Send Selected`。



![Image](assets/fr/062.webp)



然後填寫交易欄位：




- 在「付款給」中，貼上收款人的 Address 或按一下相機圖示掃描 QR 代碼；
- 在 `Label` 中，新增追蹤此支出的標籤；
- 在「金額」中，輸入要傳送的金額；
- 最後，根據目前的市場狀況選擇收費率（估算值可參閱 [Mempool.space](https://Mempool.space/)）。



欄位填寫完成後，請仔細檢查資訊，然後按一下 `建立交易 >>`。



![Image](assets/fr/063.webp)



檢查交易詳細資訊，確認一切正確無誤，然後按一下 `Finalize Transaction for Signing` (完成簽署交易)。



![Image](assets/fr/064.webp)



交易已準備就緒，但尚未簽署。若要以 QR 碼顯示 [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/PSBT) ，請點選 `Show QR`。



![Image](assets/fr/065.webp)



#### 7.2.2 使用 SeedSigner 簽署交易



像往常一樣，開啟您的 SeedSigner 並掃描您的 SeedQR 來存取您的投資組合。從主畫面，選擇「掃描」，然後掃描 Sparrow 上顯示的 QR 代碼。



![Image](assets/fr/066.webp)



然後選擇與您的投資組合相匹配的 seed。



![Image](assets/fr/067.webp)



SeedSigner 會自動偵測這是 PSBT，並顯示交易摘要：




   - 發送的金額、
   - 輸出位址、
   - 相關交易成本。



按一下「檢視詳細資料」，並直接在 SeedSigner 螢幕上仔細檢查所有資訊。最重要的檢查項目是傳送的金額、收件人的 Address 以及任何收費的金額。



![Image](assets/fr/068.webp)



如果一切正確，請選擇 `Approve PSBT`，使用對應的私人密碼匙簽署交易。



![Image](assets/fr/069.webp)



簽署後，SeedSigner 會產生一個包含已簽署交易的新 QR 代碼，準備讓 Sparrow 掃描。



![Image](assets/fr/070.webp)



#### 7.2.3 廣播來自 Sparrow 的交易



既然交易是有效的，就需要在 Bitcoin 網路上廣播，讓它到達 Miner，由 Miner 將它加入到 BLOCK。



在 Sparrow 上，按一下「QR Scan」。



![Image](assets/fr/071.webp)



將 SeedSigner 顯示的 QR 碼（已簽署交易的 QR 碼）呈現在網路攝影機上。Sparrow 會解碼簽名，並顯示完整的交易詳細資訊。最後檢查所有資訊是否正確，然後按一下「廣播交易」以在 Bitcoin 網路上廣播。



![Image](assets/fr/072.webp)



您的交易已傳送到 Bitcoin 網路。您可以在 Sparrow wallet 的 「交易 」標籤中查看其進度。



![Image](assets/fr/073.webp)



您現在已經掌握了使用 SeedSigner 的基本知識。若要深化您的知識並探討更進階的用途，我邀請您參閱下列教學：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[您也可以透過比特幣捐款來支持 SeedSigner 開源專案的開發！](https://seedsigner.com/donate/)**



*信用：本教程中的部分圖片來自 [SeedSigner 專案官方網站](https://seedsigner.com/) 和 [GitHub 套件庫](https://github.com/SeedSigner/seedsigner)。*