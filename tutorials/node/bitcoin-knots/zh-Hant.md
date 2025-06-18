---
name: Bitcoin 結
description: 如何使用 Bitcoin Knots 替代用戶端啟動節點？
---
![cover](assets/cover.webp)


Bitcoin Knots 是 Bitcoin 協定的另一種實作，源自 Bitcoin Core。由 Luke Dashjr 設計和維護，它提供了一些額外的功能和 Mempool 的規則調整，同時仍與網路中的其他節點相容。Bitcoin Knots 整合了 Bitcoin Wallet，但也可以作為一個簡單的 Bitcoin 節點，與其他 Wallet 軟體一起使用。


## 為什麼使用結而不是核心？


目前，Core 是 Bitcoin 通訊協定在網路上的大多數實作。Bitcoin 通訊協定只是一組規則。它需要軟體來應用這些規則。執行 Bitcoin 通訊協定軟體的機器稱為節點，所有這些節點共同組成 Bitcoin 網路。


在 Bitcoin 的歷史中，出現了許多由 Satoshi Nakamoto 開發的初始軟體衍生出來的用戶端。如今（2025 年 3 月），Bitcoin Core 佔據壓倒性的大多數，Bitcoin 網路上幾乎 98% 的節點都在使用此用戶端。


不過，也有替代軟體。這些不是 Altcoin 連結的節點，例如 Bitcoin Cash，而是與真正 Bitcoin 網路相容的替代用戶端。其中，Bitcoin Knots 最為人所知。它目前約佔網路的 1.4%。其他替代客戶仍是少數。


![Image](assets/fr/01.webp)


使用 Knots 等替代用戶端而非 Core 的主要原因有兩個：




- 技術**：這些用戶端通常會為 Core 提供不同的選項，尤其是在 Mempool 管理方面，它們會決定您的節點接受和廣播哪些交易。
- 政策**：有些人基於非技術上的理由，喜歡使用 Knots 等替代用戶端，主要是為了支持 Core 的替代方案，從而減少 Core 的壟斷。如果 Core 遭到攻擊，擁有可靠、維護良好的替代用戶端，而且知道如何使用它們，將是非常有用的。其他人使用 Knots 是為了抗議目的，因為他們對 Core 開發人員失去信心，或不認同大多數用戶端的管理。


## 如何安裝 Bitcoin 結？


前往 [Bitcoin Knots 官方網站](https://bitcoinknots.org/#download) 下載適合您作業系統的版本。別忘了下載指紋和簽章來驗證軟體。這些檔案也可以 [Bitcoin Knots GitHub 套件庫](https://github.com/bitcoinknots/Bitcoin) 下載。


![Image](assets/fr/02.webp)


在您的機器上安裝軟體之前，我們強烈建議您檢查其真實性和完整性。如果您不知道如何進行，請參閱此其他教學：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
驗證軟體後，請依照安裝面板上指示的步驟進行安裝。


![Image](assets/fr/03.webp)


## 啟動 IBD


第一次啟動 Bitcoin Knots 時，您可以選擇儲存節點資料（包括 Blockchain、UTXO 設定和參數）的本機目錄。


![Image](assets/fr/04.webp)


您也可以選擇修剪 Blockchain 資料，只保留最近的區塊。此選項可讓您的節點在設定的儲存限制內完整檢查每個區塊，從而逐漸移除最舊的區塊。如果您有足夠的磁碟空間 (目前約 650 GB，但這個數字還在成長中)，請不要勾選此選項。如果您的磁碟空間有限，請啟動修剪並指定允許的最大容量。


請注意：如果您的節點被修剪，而您使用它來同步化已復原的 Wallet，您將無法擷取本地儲存最舊區塊之前的交易。


![Image](assets/fr/05.webp)


另一個可用的選項是「*假設有效*」。它可以跳過特定區塊之前的區塊中包含的交易的簽名驗證，從而加快初始同步。


*Assume Valid*" 的目的是在不大幅降低安全性的情況下加快節點的第一次同步，方法是假設這些交易在之前已經被網路大量驗證過。唯一重要的折衷是，您的節點不會偵測到任何先前的 Bitcoin 盜竊，但仍會保證發行比特幣總數的準確性。您的節點會在指定區塊之後驗證所有交易簽章。這個方法是基於一個假設，即長期被網路接受而沒有被質疑的交易很可能是有效的。


例如，這裡的 「*假設有效*」設定為區塊 No.855 000 `0000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, 發佈於 2024 年 8 月 1 日。因此，在 IBD 期間，我的節點只會從這個區塊開始進行完整簽章驗證。


![Image](assets/fr/06.webp)


然後按一下「*OK*」按鈕，啟動 *初始區塊下載*。在初始節點同步期間，您需要耐心等待。如果您希望稍後恢復同步，只需關閉軟體並關閉您的電腦。下次開啟程式時，同步化將順利恢復。


![Image](assets/fr/07.webp)


## 設定您的 Bitcoin 結


按一下「*設定*」標籤，然後選擇「*選項*」。


![Image](assets/fr/08.webp)


在「*主要*」標籤中，您可以存取節點的主要參數：




- 「*Start...*」會在電腦啟動時自動啟動節點，立即開始同步處理；
- 如果您選擇修剪 Blockchain，"*Prune...*"會調整儲存限制；
- "*Database cache...*"設定允許您的節點使用的最大 RAM；
- 最後，如果您希望將 Bitcoin Knots 節點連接到其他 Wallet 軟體，例如 Sparrow Wallet 或 Liana，請啟動「*啟用 RPC 伺服器*」。


![Image](assets/fr/09.webp)


在 "*Wallet*"標籤中，您可以找到整合式 Wallet 的設定，您可以稍後在 Knots 上建立。我建議您啟動 RBF 和硬幣控制。您也可以定義要使用的腳本類型。


![Image](assets/fr/10.webp)


*Network*" 標籤包含網路參數，您可以調整這些參數以符合您的特定需求。


![Image](assets/fr/11.webp)


*Mempool*" 標籤可讓您設定 *Memory Pool*，即儲存於記憶體中未確認交易的管理，以及分配給此功能的最大大小 (預設為 300 MB)。


![Image](assets/fr/12.webp)


垃圾郵件過濾」標籤是 Bitcoin Knots 的一項功能。在這裡您可以找到許多設定，讓您選擇接受或拒絕廣播哪些交易。主要目的是限制 Bitcoin 的某些邊緣用途，特別是元協定，以打擊這些行為，同時避免您的節點負荷過重。這是一個政治選擇，取決於您個人對 Bitcoin 的看法。


您也可以找到經典的參數，例如「*Dust*」臨界值的定義。


然而，這些參數只會影響標準化規則。您的節點只有在區塊中包含未確認交易時，才會繼續接受未確認交易，以保持與 Bitcoin 網路的其他部分相容。這些設定只會修改您的節點處理未確認交易並將其分發給對等節點的方式。實際上，由於 Knots 屬於少數，因此在 Bitcoin Core 上預設建立的規則才會定義網路上的標準化。


![Image](assets/fr/13.webp)


*Mining*" 選項卡可讓您設定節點可能參與的 Mining，如果您希望啟動此功能。


![Image](assets/fr/14.webp)


最後，「*顯示*」標籤關乎與 Interface 圖形相關的參數，包括軟體語言。


![Image](assets/fr/15.webp)


## 建立 Bitcoin Wallet


初始同步完成後，您的 Bitcoin Knots 節點就可以完全運作了。現在您可以選擇將此節點連接到其他 Wallet 軟體，或直接使用內建的 Hot Wallet。若要這樣做，請按一下「*建立新的 Wallet*」按鈕。


![Image](assets/fr/16.webp)


為您的 Wallet 命名。您也可以按一下「*加密 Wallet*」，用 passphrase BIP39 來保護它。準備就緒後，按一下「*建立*」按鈕。


![Image](assets/fr/17.webp)


passphrase BIP39是一個可選的密碼，您可以在Mnemonic短語之外自由選擇，以增加Wallet的安全性。在配置此功能之前，我們強烈建議您閱讀以下文章，它詳細解釋了passphrase理論上是如何工作的，以及如何避免可能導致您永久損失比特幣的錯誤：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
如果您已啟動 passphrase 選項，請選擇穩健的選項，並小心保存在一個或多個安全的實體媒體上。


![Image](assets/fr/18.webp)


您的 Bitcoin Wallet 現已建立。


![Image](assets/fr/19.webp)


## 備份您的 Bitcoin Wallet


即使在您收到您的第一個比特幣之前，為您的 Bitcoin Wallet 做一個備份是非常必要的，這樣您可以在丟失或電腦故障的情況下恢復您的資金。要做到這一點，請點擊 「*檔案*」標籤，然後點擊 「*備份 Wallet*」。


![Image](assets/fr/20.webp)


此操作會產生一個單一檔案，可用於還原您所有的 bitcoins。所以要非常小心，並將其保存在安全的外部媒介上。


## 接收比特幣


要直接在您的 Knots Wallet 中接收比特幣，請點擊 「*接收*」按鈕。


![Image](assets/fr/21.webp)


為您的 Address 指定「*標籤*」，可輕鬆識別其用途，並方便日後使用「*錢幣控制*」。您也可以事先定義要在此 Address 接收的精確金額，或加入給付款人的訊息。設定好參數後，點選「*要求付款*」。


![Image](assets/fr/22.webp)


Bitcoin Knots 接著會顯示接收的 Address，您可以複製或掃瞄該 Address，然後寄給付款人。


![Image](assets/fr/23.webp)


一旦交易被廣播，您可以直接在「*交易*」功能表中追蹤其狀態。


![Image](assets/fr/24.webp)


## 發送比特幣


現在您的 Knots Wallet 中已有比特幣，您可以發送它們。要這樣做，請按一下「*傳送*」按鈕。


![Image](assets/fr/25.webp)


按一下「*輸入...*」按鈕，選擇您希望在此交易中使用的確切 UTXO。


![Image](assets/fr/26.webp)


輸入收件人的 Bitcoin Address。


![Image](assets/fr/27.webp)


新增標籤以記住此交易的目的。


![Image](assets/fr/28.webp)


輸入您要寄給此 Address 的金額。


![Image](assets/fr/29.webp)


按一下「*選擇...*」按鈕，根據目前的網路狀態，為您的交易選擇適當的費率。


![Image](assets/fr/30.webp)


如果一切都令您滿意，請按一下「*送出*」按鈕。如果您使用的是 passphrase，在此階段會要求您填寫。


![Image](assets/fr/31.webp)


最後一次檢查您的交易參數，如果一切正常，請再次按一下「*傳送*」按鈕，簽署並發送您的交易。


![Image](assets/fr/32.webp)


您等待確認的交易現在會出現在 「*交易*」標籤中。


![Image](assets/fr/33.webp)


## 將您的節點連接到另一個程式


Bitcoin Knots 用於管理您的 Bitcoin Wallet 的整合式 Interface 不一定是最直覺的，其功能仍然相對有限。不過，您可以將 Bitcoin Knots 節點連接到專門的 Wallet 管理軟體，輕鬆存取 Blockchain Bitcoin 資料並廣播交易。


程序取決於所使用的軟體，但主要有兩種情況：Bitcoin Knots 與您的 Wallet 軟體安裝在同一台電腦上，或是在獨立的機器上執行。


### 與本地 Bitcoin 結 ：


如果 Bitcoin Knots 已安裝在您的電腦上，請在軟體檔案中找到檔案 `Bitcoin.conf`。如果此檔案不存在，您可以建立它。用文字編輯器打開它，並插入以下一行：


```ini
server=1
```


然後儲存您的變更。


您也可以透過 Bitcoin-QT 的 Interface 圖形，導覽到 "*Settings*" > "*Options...*「 並啟用 」*Enable RPC server*" 選項。> "*Options...*「 並啟用 」*Enable RPC server*" 選項。


進行這些變更後，別忘了重新啟動軟體。


![Image](assets/fr/34.webp)


然後前往您的 Wallet 管理軟體 (例如 Sparrow Wallet 或 Liana)，輸入 cookie 檔案的路徑，通常與 `Bitcoin.conf` 位於同一資料夾，視您的作業系統而定：


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


保留其他參數為預設值，URL `127.0.0.1` 和連接埠 `8332`，然後按一下「*測試連線*」。


![Image](assets/fr/36.webp)


### 附遙控器 Bitcoin 節 ：


如果 Bitcoin Knots 安裝在另一台連接到同一個網路的機器上，請先在軟體檔案中找出 `Bitcoin.conf` 檔案。如果此檔案尚未存在，您可以建立它。使用文字編輯器開啟此檔案，並加入以下一行：


```ini
server=1
```


編輯檔案後，請確保將其儲存到您作業系統的適當資料夾：


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

此操作也可透過 Bitcoin-QT 的 Interface 圖形執行。進入 "*Settings*「 功能表，然後選擇 」*Options...*「，勾選對應的方塊以啟動 」*Enable RPC server*" 選項。如果「Bitcoin.conf」檔案不存在，您可以點選「*Open Configuration File*」直接從這個 Interface 建立它。


![Image](assets/fr/37.webp)


在您的區域網路中找出寄存 Bitcoin Knots 的機器的 IP Address。要做到這一點，您可以使用 [Angry IP Scanner](https://angryip.org/) 之類的工具。為了方便起見，我們假設您節點的 IP Address 是 `192.168.1.18`。


在 `Bitcoin.conf` 檔案中，新增下列幾行，設定 `rpcbind=192.168.1.18` 以符合您節點的 IP Address。


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


同時在 `Bitcoin.conf` 檔案中加入遠端連線的使用者名稱和密碼。請務必使用您的使用者名稱取代 `loic`，並使用強大的密碼取代 `my_password`：


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


修改並儲存檔案後，重新啟動 Bitcoin Knots。


現在您可以進入 Wallet 管理軟體 (例如 Sparrow Wallet 或 Liana)。在 Sparrow 上，進入「*使用者/密碼*」標籤。輸入您在「Bitcoin.conf」檔案中設定的使用者名稱和密碼。保留其他參數為預設值，即 URL `127.0.0.1` 和連接埠 `8332`。然後按一下「*Test Connection*」。


![Image](assets/fr/40.webp)


連線已建立。


現在您知道 Bitcoin 結的另一種實作方式了吧。


如果您覺得本教學有用，請在下方留下 Green 的拇指，我會非常感激。歡迎在您的社交網路分享。非常感謝


我也推薦您參考這篇教學，其中我介紹了如何建立您自己的 Lightning 節點：


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a