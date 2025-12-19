---
name: Satochip x SeedSigner
description: 如何在 SeedSigner 上使用 Satochip？
---

![cover](assets/cover.webp)



*感謝 [Crypto Guide](https://www.youtube.com/@CryptoGuide/)提供 SeedSigner 韌體的 fork 以支援智慧卡，我們將在本教學中使用此韌體。



---

Satochip 是一款 wallet 智慧卡格式硬體，具有最高安全標準之一的 EAL6+ 認證安全元件。它由比利時的同名公司 Satochip 設計和製造。



Satochip 的價格約為 25 歐元，因其優異的性價比而在競爭中脫穎而出。由於採用了安全晶片，它可以抵禦物理攻擊。更重要的是，它的 applet 原始碼完全開放原始碼，並已取得 *AGPLv3* 授權。



另一方面，其格式也造成某些功能上的限制。Satochip 的主要缺點是沒有整合式螢幕：因此使用者必須盲目地簽署交易，完全依賴電腦的顯示器。



為了克服這個弱點，一個特別有趣的配置是將其與 SeedSigner 結合使用。在此設定中，電腦與 Satochip 之間不再直接進行通訊，而是透過電腦與 SeedSigner 之間的 QR 代碼交換進行通訊。SeedSigner 則扮演信任螢幕的角色：顯示要簽署的資訊，而簽章本身則由 Satochip 執行。與傳統 SeedSigner 的使用方式不同（或甚至與 Seedkeeper 結合使用），seed 永遠不會載入 SeedSigner 中。SeedSigner 因此成為 Satochip 的螢幕，消除了與盲簽相關的風險。



如果我們反過來看這個問題，將 SeedSigner 與 Satochip 搭配使用，就能填補 SeedSigner 的一大缺點：在 secure element 中儲存和使用 seed 的能力。



在我看來，與傳統的硬體錢包相比，這種配置具有多項優勢：




- Satochip 的價格約為 25 歐元，由於 applet 是開放原始碼的，您可以自行安裝在空白的智慧卡上。然後，您需要加上 SeedSigner 元件和讀取智慧卡的擴充元件的成本：視您在何處購買這種硬體，總價應該在 70 到 100 歐元之間。
- 所有涉及設定的軟體都是開放源碼：SeedSigner 韌體和 Satochip applet。
- 您可從經過認證的安全元件中獲益。
- 配置可以完全 DIY 進行，不需要使用明確指定用於 Bitcoin 的硬體，這可以提供一種似是而非的隱蔽性，並抵抗某些外部威脅（視國家而定，包括國家壓力）。如果您所在的地區限制或無法取得商用硬體錢包，這也是一個有趣的解決方案。




## 1.所需材料



若要執行此設定，您需要下列項目：




- 經典 SeedSigner 所需的一般設備 ：
 - 具有 GPIO 引腳的 Raspberry Pi Zero、
 - 1.3" Waveshare 螢幕、
 - 相容的相機、
 - 一張 microSD 卡。



![Image](assets/fr/01.webp)





- SeedSigner擴充套件，可[從Satochip官方商店](https://satochip.io/product/seedsigner-extension-kit/)購買，可讓您直接從SeedSigner讀寫智慧卡。另一個選擇是使用 [外接式智慧卡讀取器](https://satochip.io/product/chip-card-reader/)，它可以透過纜線連接到 Raspberry Pi 上的 Micro-USB 連接埠。不過，我自己還沒有測試過這個解決方案；
- [一個 Satochip](https://satochip.io/product/satochip/)，或者是一張[空白智能卡](https://satochip.io/product/card-for-diy-project/)，在上面安裝 Satochip applet（Satochip 出售的擴展套件已經包含了一張空白智能卡）。Satochip的擴充套件也支援[SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/)格式。因此，如果您喜歡的話，可以選擇這種格式。



![Image](assets/fr/02.webp)



有關組裝 SeedSigner 所需設備的詳細資訊，請參閱本教程的第一部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2.安裝韌體



若要在 Satochip 上使用 SeedSigner，您需要安裝一個不同於原始 SeedSigner 的韌體，以支援智慧卡讀取。為此，[我建議使用 "**3rdIteration**" 的 fork](https://github.com/3rdIteration/seedsigner)。下載 [最新版本的映像檔](https://github.com/3rdIteration/seedsigner/releases) (`.zip`)，以對應您使用的 Raspberry Pi 型號。



![Image](assets/fr/03.webp)



如果您還沒有，請下載 [Balena Etcher] 軟體 (https://etcher.balena.io/)，然後按以下步驟操作：




- 將 microSD 卡插入電腦；
- 啟動蝕刻器 ；
- 選擇您剛下載的 `.zip` 檔案；
- 選擇 microSD 卡為目標；
- 按一下「Flash!」。



![Image](assets/fr/04.webp)



等待程序完成：您的 microSD 現在已準備就緒，可以使用。現在您可以繼續組裝您的裝置。



有關韌體安裝和軟體驗證的詳細資訊（我強烈建議您採取的步驟），請參閱下列教學：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3.組裝智慧卡閱讀器



首先將攝影機安裝在 Raspberry Pi Zero 上，小心地將其插入攝影機針腳，並用黑色卡舌鎖定。然後將 Pi 放在機殼底部，確保將連接埠對齊對應的開口。



![Image](assets/fr/05.webp)



然後將智慧卡讀卡器連接至 Raspberry Pi Zero 的 GPIO 引腳。



![Image](assets/fr/06.webp)



將塑膠蓋滑動到智慧卡讀卡機上，直到位置正確。



![Image](assets/fr/07.webp)



然後將螢幕加入擴充的 GPIO 引腳。



![Image](assets/fr/08.webp)



最後，將載有韌體的 microSD 卡插入 Raspberry Pi Zero 的側邊連接埠。



![Image](assets/fr/09.webp)



現在您可以透過 Raspberry Pi Zero 的 Micro-USB 連接埠或擴充裝置的 USB-C 連接埠連接 SeedSigner。兩種方式都可以。等待幾秒鐘啟動，然後您應該會看到歡迎畫面出現。



![Image](assets/fr/10.webp)



有關 SeedSigner 初始設定的詳細資訊，我建議您參考以下教學的第 4 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4.使用 Satochip applet 快閃智能卡（可選）



如果您已經擁有Satochip，您可以跳過這一步驟，直接進入第四步驟。在本節中，我們將介紹如何在空白的智能卡上安裝Satochip applet（DIY方法）。小程序只是一個在智能卡上運行的小程式，它使我們能夠管理特定的功能。



若要開始使用，請開啟 SeedSigner 上的「工具 > 智慧卡工具」功能表。



![Image](assets/fr/11.webp)



然後選擇 `DIY Tools > Install Applet`。



![Image](assets/fr/12.webp)



將您的智慧卡插入 SeedSigner 閱讀器，晶片朝下，然後選擇「Satochip」小程序。



![Image](assets/fr/13.webp)



安裝時請耐心等待：安裝過程可能需要數十秒鐘。



![Image](assets/fr/14.webp)



一旦成功安裝 applet，您就可以繼續進行步驟 4。



![Image](assets/fr/15.webp)




## 5.建立並儲存 seed



### 5.1.產生 seed



現在您的所有硬體和軟體都已經正常運作，您可以開始建立您的 Bitcoin 組合。要做到這一點，請插入您的 SeedSigner，然後像使用傳統 SeedSigner 一樣，通過擲骰子或拍照來 generate 您的 seed：




- 移至 `工具 > 攝影機 / 骰子捲軸` 功能表；
- 然後依照所選方法進行熵產生程序；
- 最後，將 seed 備份到實體媒體上，並仔細檢查備份。



![Image](assets/fr/16.webp)



如果您想查看此程序的詳細資訊，請參閱本教程的第 5 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2.在 Seedkeeper 上儲存 seed



一旦 seed 產生後，這是它唯一停留在 SeedSigner 的 RAM 中的時間。在我的情況下，我想把它儲存在[Seedkeeper](https://satochip.io/product/seedkeeper/)上，這是另一個專為儲存秘密而設計的 Satochip 產品。我將使用此裝置作為最後的手段，以防遺失我的 Satochip。



這裡所選擇的備份策略取決於您的喜好，但至少要有一份助記詞組的複本，可以是實體媒體 (紙張或金屬) 上的，也可以像這裡一樣，放在 Seedkeeper 中。您也可以依需要倍增備份數量。如需投資組合備份策略的更多資訊，建議您閱讀此教學 ：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

若要備份 Seedkeeper 上的 seed，請直接進入 `備份 Seed` 功能表。



![Image](assets/fr/17.webp)



然後將您的 Seedkeeper 插入智慧卡讀卡機，並選擇「至 SeedKeeper」。



![Image](assets/fr/18.webp)



輸入您的 PIN 碼以解除鎖定。



![Image](assets/fr/19.webp)



選擇「標籤」，輕鬆識別儲存在 Seedkeeper 上的不同秘密。舉例來說，您可以簡單地保留 wallet 的印記，或是明確標示「種子」。選擇取決於您的喜好和風險。



![Image](assets/fr/20.webp)



如果您的備份策略完全依賴此 Seedkeeper，我強烈建議您現在執行一次空復原測試，然後比較指紋以檢查備份是否正常。



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Seedkeeper PIN 碼應儘量長且隨機，以防止在卡片受到實體損害時發生暴力嘗試。您也應該保留此 PIN 碼的備份副本，並儲存在 Seedkeeper 以外的其他位置。如果沒有這個 PIN 碼，您將無法存取儲存在 Seedkeeper 中的助記符，您的比特幣將會永久遺失。



### 5.3.在 Satochip 上節省 seed



現在您的投資組合已經產生、儲存並驗證完成，我們要將其傳輸至 Satochip。為此，請確定 seed 已載入 SeedSigner 的 RAM。然後前往`工具 > 智慧卡工具 > Satochip 功能`。



![Image](assets/fr/21.webp)



將 Satochip 插入智慧卡讀卡器，然後選擇「使用種子初始化」。



![Image](assets/fr/22.webp)



裝置會提示您輸入 Satochip PIN 碼；由於卡是新的，尚未初始化，所以還沒有 PIN 碼。請輸入任何代碼以跳過此步驟（並非封鎖代碼）。



![Image](assets/fr/23.webp)



SeedSigner 偵測到您的 Satochip 尚未初始化。按一下 `I Understand` 來確認。



![Image](assets/fr/24.webp)



然後您可以設定 Satochip PIN 碼，從 4 到 16 個字元不等。為了加強 wallet 的安全性，請選擇一個長而隨機的密碼：這是唯一能防止您的記憶詞組被實體存取的方法。



根據您的個人策略，請記住在創建 PIN 碼後立即將其保存在安全的密碼管理器或實體介質中。在後者的情況下，請確定切勿將載有 PIN 的媒體與您的 Satochip 存放在同一地方，否則保護功能將變得毫無用處。備份副本非常重要： **如果沒有這個 PIN 碼，您將無法存取您的 seed，您的比特幣將會永遠丟失**。



![Image](assets/fr/25.webp)



SeedSigner 會詢問您要將哪個 seed 匯入 Satochip。選擇指紋與您剛剛建立的組合相符的 seed。



![Image](assets/fr/26.webp)



您的 seed 現在已匯入 Satochip。



![Image](assets/fr/27.webp)



現在您可以關閉 SeedSigner。



如果您想使用 passphrase BIP39 來加強 wallet 的安全性，請參閱本教學的第 6 部分：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6.將 wallet 匯入 Sparrow



現在您的投資組合已經建立並運行，我們會將其公開資訊（"*keystore*"）匯入 Sparrow Wallet 或其他投資組合管理軟體。此軟體將用於建立、分發和追蹤您的交易。但是，它無法簽署這些交易，因為只有 Satochip（以及任何備份）持有此操作所需的私人密碼匙。



### 6.1 準備 SeedSigner 和 Satochip



插入包含作業系統的 microSD 卡，然後開啟 SeedSigner。目前，它什麼也做不了，因為它還不知道您的 seed。您必須先將 Satochip 插入智慧卡讀卡機，因為它才是存放 seed 的裝置。



從主畫面，存取「工具 > 智慧卡工具 > Satochip 功能」功能表。



![Image](assets/fr/28.webp)



然後按一下 `Export Xpub`。



![Image](assets/fr/29.webp)



選擇投資組合類型。在我們的例子中，這是單一投資組合：選擇 `單一 Sig`。



![Image](assets/fr/30.webp)



接下來是腳本標準的選擇。選擇最新的：`Native SegWit`。



![Image](assets/fr/31.webp)



最後，選擇「Coordinator」，也就是您要使用的投資組合管理軟體。在此，我們會使用 Sparrow Wallet。



![Image](assets/fr/32.webp)



出現警告訊息：這是非常正常的。擴展公鑰 (`xpub`)允許您查看所有從您的 seed (第一個帳戶) 衍生出來的地址。但是，它不會讓您存取您的資金：它的洩露會危及您的隱私，但不會危及您比特幣的安全。換句話說，它允許您觀察您的餘額，但不允許您花掉它們。



按一下「我了解」。



![Image](assets/fr/33.webp)



然後輸入 Satochip 的 PIN 碼來解鎖。這是您在步驟 5 中定義並儲存的密碼。



![Image](assets/fr/34.webp)



最後，如果您滿意顯示的資訊，請按一下 `Export Xpub`。



![Image](assets/fr/35.webp)



SeedSigner 隨後會以動態 QR 代碼的形式生成您的 xpub，其中包含您在 Sparrow Wallet 中管理投資組合所需的所有資料。您可以使用搖桿調整螢幕亮度，讓掃描 QR 代碼更容易。



### 6.2 將新組合匯入 Sparrow Wallet



確保 Sparrow Wallet 軟體已安裝在您的電腦上。如果您不知道如何下載、檢查其真實性並正確安裝，請參閱我們關於此主題的完整教學 ：



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

在電腦上開啟 Sparrow Wallet，然後在功能表列中按一下`檔案 → 匯入 Wallet`。



![Image](assets/fr/36.webp)



向下捲動到 `SeedSigner`，然後選擇 `Scan...`。您的網路攝影機將啟動：掃描 SeedSigner 螢幕上顯示的動態 QR 代碼。



![Image](assets/fr/37.webp)



為您的組合指定一個名稱，然後點選 `建立 Wallet`。Sparrow 接著會要求您設定密碼，以鎖定本機存取此 wallet。選擇一個強大的密碼：它可以保護您在 Sparrow 中的資料（公開密鑰、地址、標籤和交易歷史）。但是，將來還原 wallet 時並不需要這個密碼：只需要您的助記短語（可能還有您的 passphrase）。



我建議您將此密碼儲存在密碼管理器中，以免遺失。



![Image](assets/fr/38.webp)



您的 keystore 已成功匯入。



![Image](assets/fr/39.webp)



現在檢查 Sparrow Wallet 中顯示的`主指紋`是否與之前在 SeedSigner 上找到的相符。



SeedSigner 接著會要求您從 Sparrow wallet 掃描隨機的接收位址，以確認匯入的有效性。



![Image](assets/fr/40.webp)



您的 Satochip（通過 SeedSigner）和 Sparrow Wallet 現在已安全連接。Sparrow 充當完整的管理介面，而 Satochip 則是唯一能簽署交易的裝置。現在您已準備好以完全隔絕空氣的配置接收和傳送比特幣。



![Image](assets/fr/41.webp)



## 7.收發比特幣



您的 Satochip 和 Sparrow Wallet 現在已經配置好一起工作了。在本節中，我們會逐步說明如何在此模式下接收和發送 bitcoins。



### 7.1 接收比特幣



#### 7.1.1 產生接收位址



在您的電腦上，開啟 Sparrow Wallet，並使用密碼解除鎖定您的「Satochip-SeedSigner」wallet。檢查軟體是否已連線至伺服器（右下方的指示器）。然後，在側邊欄點選「接收」。



![Image](assets/fr/42.webp)



會出現新的 Bitcoin 位址。您會發現 ：




- 文字格式的位址（如果您使用的是 P2WPKH，則以`bc1q...`開頭，就像本範例一樣） ；
- 相關的 QR 代碼 ；
- 一個 `Label` 欄位，用來追蹤您的交易。



我強烈建議您在 wallet 中的每個 bitcoin 收據上添加一個標籤。這將幫助您輕鬆識別每個 UTXO 的來源，更好地管理您的隱私。要瞭解更多關於這個重要主題的資訊，請查看 Plan ₿ Academy 上的專門培訓 ：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

若要新增標籤，只需在「標籤」欄位輸入名稱，然後確認即可。



例如：



```txt
Label : Sale of the Raspberry Pi Zero
```



您的地址現在會在所有 Sparrow 區段中與此標籤相關聯。



![Image](assets/fr/43.webp)



#### 7.1.2 SeedSigner 上的 Address 驗證



在向付款人傳達您的收款地址之前，必須檢查該地址是否屬於您的 seed。這一步驟可確保您的 Satochip 能夠簽署與此地址相關的交易。它還可以防止 Sparrow 顯示欺詐地址的潛在攻擊。請記住，Sparrow 在不安全的環境（您的電腦）上運行，其攻擊面遠遠大於您的 Satochip，因為 Satochip 是完全隔離的。這就是為什麼在 wallet 硬體上檢查之前，您絕對不能盲目相信 Sparrow 所顯示的位址。



在 Sparrow 中，按一下位址的 QR 代碼可將其放大：然後就會全螢幕顯示。



![Image](assets/fr/44.webp)



在您的 SeedSigner 上，將 Satochip 插入閱讀器，然後從主功能表中選擇`掃描`。掃瞄電腦上顯示的 QR 碼，然後選擇`使用 Satochip 卡`。



![Image](assets/fr/45.webp)



然後確認使用的腳本類型 (在本例中為 `Native SegWit`)，輸入 Satochip PIN 碼以解除鎖定，並驗證 `xpub` 資訊。



![Image](assets/fr/46.webp)



如果掃描的位址與您的 seed 所產生的位址相符，SeedSigner 將會顯示訊息：`Address已驗證`。



![Image](assets/fr/47.webp)



這樣您就可以確定該地址屬於您的投資組合。



#### 7.1.3 收到資金



現在您可以將這個地址以文字形式或透過其 QR 代碼傳送給需要寄送 sats 給您的人或部門。一旦交易在網路上廣播，它就會出現在 Sparrow Wallet 的「交易」標籤中。



![Image](assets/fr/48.webp)



### 7.2 傳送 bitcoins



使用 Satochip-SeedSigner 配置發送比特幣涉及 3 個步驟：




- 在 Sparrow 中建立交易 ；
- 在 Satochip 上簽署此交易，透過 SeedSigner ；
- 最後，交易會從 Sparrow 透過網路廣播。



兩台裝置之間的所有交換都完全透過 QR 代碼進行。



#### 7.2.1 在 Sparrow 中建立交易



在 Sparrow Wallet 中，您可以按一下左側邊欄中的 `Send` 選項卡來建立交易。不過，我比較喜歡使用 `UTXOs` 標籤，它可以讓您實踐 *Coin 控制*。此方法可精確控制所花費的 UTXOs，以限制交易過程中透露的資訊。



在 `UTXOs` 標籤中，選擇您要花費的硬幣，然後按一下 `Send Selected`。



![Image](assets/fr/49.webp)



然後填寫交易欄位：




- 在「付給」中，貼上收件人的地址或使用相機圖示掃描他們的 QR 代碼；
- 在 `Label` 中，新增標籤以追蹤此支出；
- 在「金額」中，輸入要傳送的金額；
- 最後，根據目前的網路狀況選擇充電率 (可在 [mempool.space](https://mempool.space/) 取得估算值)。



完成所有欄位後，請仔細審閱資訊，然後按一下 `建立交易 >>`。



![Image](assets/fr/50.webp)



最後一次檢查交易詳細資訊的正確性，然後按一下 `Finalize Transaction for Signing `。



![Image](assets/fr/51.webp)



交易已準備就緒，但尚未簽署。若要以 QR 碼顯示 [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) ，請點選 `Show QR`。



![Image](assets/fr/52.webp)



#### 7.2.2 與 Satochip 簽署交易



開啟 SeedSigner 並如往常一樣插入 Satochip。從主畫面，選擇`掃描`，然後掃描 Sparrow 上顯示的 QR 代碼。



![Image](assets/fr/53.webp)



選擇「使用 Satochip 卡」選項。



![Image](assets/fr/54.webp)



輸入您的 PIN 碼來解鎖智慧卡。



![Image](assets/fr/55.webp)



SeedSigner 會偵測到這是一個 PSBT，並顯示交易摘要：




   - 發送的金額、
   - 目的地地址、
   - 相關交易成本。



點擊「檢視詳情」，直接在 SeedSigner 螢幕上審查所有資訊。最重要的檢查點是發送的金額、目的地地址和交易費用。



![Image](assets/fr/56.webp)



如果一切正常，請選擇 `Approve PSBT`，使用 Satochip 簽署交易。



![Image](assets/fr/57.webp)



簽章完成後，SeedSigner 會產生一個包含已簽章交易的新 QR 代碼，準備讓 Sparrow 掃描。



#### 7.2.3 廣播來自 Sparrow 的交易



既然交易已經簽章和驗證，剩下的工作就是在 Bitcoin 網路上廣播，以便礦工將其納入區塊中。在 Sparrow 中，按一下 `掃描 QR`。



![Image](assets/fr/58.webp)



將 SeedSigner 上顯示的 QR 碼（包含已簽署交易的 QR 碼）對準網路攝影機。Sparrow 會顯示所有交易詳細資訊。檢查所有資訊是否正確，然後按一下「廣播交易」，即可在 Bitcoin 網路上廣播。



![Image](assets/fr/59.webp)



您的交易現在已傳送至網路。您可以在 Sparrow Wallet 的「交易」標籤中查看其確認情況。



![Image](assets/fr/60.webp)



## 8.取回您的 wallet



正如我們在前幾節所看到的，根據您的安全策略，除了 Satochip .NET Framework 之外，還有幾種備份復原片段的方法：




- 使用經典的 *SeedQR* 與 SeedSigner ；
- 將記憶詞組記錄在實體媒體上；
- 或透過 Seedkeeper 儲存，如第 5.2 節所述。



無論如何，有兩種主要情況您需要介入：遺失 Satochip 或遺失 SeedSigner。讓我們來看看在這兩種情況下該如何反應。



### 8.1.使用 Satochip 擷取您的 wallet



如果您仍擁有 Satochip，但您的 SeedSigner 壞了或遺失了，情況處理起來相當簡單，因為您的 wallet 仍在 Satochip 中。



最好的選擇是推薦必要的元件，並從頭重建一個新的 SeedSigner。由於這是一個「無狀態」裝置，所以無論您使用的是同一個或另一個 SeedSigner 都沒有關係：只要您能插入 Satochip，一切都能正常運作。



如果您不想重建一個，您也可以用傳統的方式使用 Satochip，也就是直接從您的電腦使用，而不需要經過 SeedSigner。這個方法可以完美運作，但卻大大降低了您的 Bitcoin wallet 的安全性：您失去了 "*air-gapped*"隔離功能，現在必須盲目簽署，因為 SeedSigner 充當了可信賴的畫面。不過，在緊急情況下，或是您無法重建 SeedSigner 時，這可以是一個臨時的解決方案。



要進行此操作，您需要一個 USB 智慧卡或 NFC 讀卡機。在 Sparrow 中開啟您要還原的 wallet，然後到「設定」標籤，按一下「取代」。



![Image](assets/fr/61.webp)



將您的 Satochip 插入連接至電腦的智慧卡讀卡器，然後按一下`Satochip`旁邊的`Import`。



![Image](assets/fr/62.webp)



最後，輸入您的智慧卡密碼即可解鎖。之後您就可以直接使用連接的 Satochip 存取您的 wallet、建立交易並簽名。



### 8.2.使用 SeedSigner 檢索您的投資組合



另一種更微妙的情況是，當您無法使用包含 seed 的 Satochip 時：無論是它壞了、丟失了、被盜了，還是您忘記了它的 PIN 碼。如果您的 Satochip 被盜或遺失，我們強烈建議您，一旦您的資金恢復存取權，請立即將您的比特幣轉移至全新的 wallet，並使用不同的 seed 產生。這可確保潛在的攻擊者永遠無法存取您的 sats。



若要重新取得您的投資組合並移動您的資金，只要將您的 seed 載入 SeedSigner 即可。根據您使用的備份媒體，您有幾種選擇：





- 在 `Seeds > Enter 12-word seed` 功能表中手動輸入您的助記語句。



![Image](assets/fr/63.webp)





- 按一下首頁的「掃描」按鈕，掃描您的 *SeedQR*。



![Image](assets/fr/64.webp)





- 或透過 `種子 > 來自 SeedKeeper` 功能表，從 Seedkeeper 載入您的 seed（這是我在本教程中使用的方法）。您只需輸入 Seedkeeper PIN，並選擇要在 SeedSigner 上作為 seed 使用的秘訣。



![Image](assets/fr/65.webp)



一旦 seed 被載入到 SeedSigner 中，無論您使用哪種方法，您都可以簽署一個或多個掃描交易，將您的比特幣移到一個新的、未加密的 wallet 中。要瞭解如何執行，請參閱以下教學的第 7.2 部分：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

現在您知道如何結合 SeedSigner 使用 Satochip 安全地管理您的 Bitcoin 投資組合。



如果這個設定讓您信服，請不要猶豫，支持讓它成為可能的專案：




- 透過直接 [在 Satochip 網站上](https://satochip.io/shop/) 購買您的設備；
- 透過 [捐款給 SeedSigner 專案](https://seedsigner.com/donate/)；
- 透過訂閱 [Crypto Guide 的 YouTube 頻道](https://www.youtube.com/@CryptoGuide/)，該頻道由維護 GitHub 倉庫的人經營，而 GitHub 倉庫中存放了我們在本教程中使用的修改過的韌體。