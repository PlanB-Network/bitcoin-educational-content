---
name: Ginger Wallet
description: 開放原始碼、自我保管的 Bitcoin wallet 軟體、來自 Wasabi Wallet 的 fork，整合 Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet 是一個開放原始碼、非監管式的 Bitcoin 產品組合，著重於機密性與隱私權。它的前身是來自 Wasabi Wallet 的 fork（2.0.7.2 版之後 - MIT 授權）。



Ginger Wallet 保留了 Wasabi 的技術架構，同時增加了一些特定功能。根據 [Ginger Wallet 文件](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet)，Wasabi 強調**自主性與控制**，而 Ginger 則著重**易用性、安全性與簡化的體驗**，讓那些不太熟悉技術層面的人也能使用。



Ginger Wallet 是 wallet 軟體，僅適用於電腦（無行動應用程式）。



## 什麼是 Coinjoin？



**coinjoin** 是一種特殊的 Bitcoin 交易結構，可將多位參與者聚集在單一合作交易中。此機制將不同使用者的入帳項混入共同交易中，使得追蹤資金變得極為困難 - 如果不是經常不可能的話 (如果操作得宜的話)。因此，外部觀察者幾乎不可能確定所涉及的比特幣的來源和目的地，這與傳統的 Bitcoin 交易不同。



對於作為用戶的您，coinjoin 幫助您保密。例如，如果您在一個 Bitcoin 地址上收到 10,000 sats 的捐款，發件人可以追蹤這些資金，並在某些情況下推斷出您持有更大數量的比特幣，或觀察您的活動。在這筆 10,000 sats 的捐款之後進行一次 Coinjoin，您就打破了這種可追溯性：發貨人將無法再從這筆款項中獲得任何關於您的資訊。



Chaumian coinjoin 提供了高度的安全性，因為資金在任何時候都由用戶獨自控制。即使是協調伺服器的操作者也無法在任何情況下轉移參與者的比特幣。使用者和協調者都不需要相互信任： 每個人都保留對自己私人金鑰的控制權，並保持唯一的交易驗證授權。因此，任何第三方都無法在 Coinjoin 期間挪用您的 bitcoins，也無法在您的輸入和輸出之間建立直接連結。



要瞭解更多關於 coinjoin 的資訊，請查看 Plan ₿ Academy 的 BTC 204 課程 ：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 安裝 Ginger Wallet



若要安裝 Ginger Wallet，請造訪網站 [Ginger Wallet](https://gingerwallet.io)。



按 ** 下載** 下載適合您電腦的版本 (Windows / MacOs / Linux)。



![screen](assets/fr/03.webp)



另一個選擇是到專案的 [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) 下載。



![screen](assets/fr/04.webp)



然後執行安裝程式。



![screen](assets/fr/05.webp)




## 參數設定



### 初步配置



開啟 Ginger Wallet，選擇您偏好的語言。



![screen](assets/fr/06.webp)



從一開始，Ginger 就提醒您合併過程中所涉及的費用。



![screen](assets/fr/07.webp)



然後按 **Start**，再按 **New**，建立新的投資組合。



![screen](assets/fr/08.webp)



接下來，儲存並確認您的 seedphrase。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



為了增加安全性，Ginger Wallet 可讓您選擇加裝 passphrase。



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

此 passphrase 一經新增，您每次嘗試存取您的投資組合時，都會被要求使用。



![screen](assets/fr/12.webp)



當您建立投資組合時，Ginger 會自動啟動預設的 **Coinjoin**。您會收到通知，然後可以依您的需求自訂設定。



![screen](assets/fr/13.webp)




### 一般設定



當您建立第一個投資組合後，就會進入 Ginger Wallet 介面。



![screen](assets/fr/14.webp)



如果您想隱藏錢包中的餘額，請啟動**保密模式**。



![screen](assets/fr/15.webp)



您可以在 Ginger Wallet 上建立多個作品集。只要點選 **新增作品集**。



![screen](assets/fr/16.webp)



Ginger 支援透過標準 Bitcoin Core 介面使用硬體組合，不過目前尚未提供硬體組合之間的直接整合。



相容的硬體組合包括 (但不限於) ：




- Blockstream Jade
- 冷卡 MK4
- 冷卡 Q
- Ledger Nano S Plus
- Ledger 奈米 X
- Trezor T 型
- Trezor Safe 3
- 等等。



現在按一下 **設定**。



![screen](assets/fr/17.webp)



這些設定是一般應用程式的設定，您在此處所做的設定將適用於所有組合。



在 ** 設定** 中，您有以下選項卡 ：





- 一般**



![screen](assets/fr/18.webp)





- 外觀



在此標籤中，您可以變更語言、貨幣和費用顯示單位 (BTC/Satoshi)，等等。



![screen](assets/fr/19.webp)





- Bitcoin**



此標籤可讓您啟用 Bitcoin Knots 以在應用程式啟動時執行、選擇您的網路 (Main/RegTest) 以及您的收費率提供者 (Mempool Space/Blockstream info/Full Node) 等。



![screen](assets/fr/20.webp)





- 安全功能**



在「安全性」標籤中，您可以啟用雙重認證、啟用或停用 Tor，甚至在關閉 Ginger 應用程式後停用 Tor。



![screen](assets/fr/21.webp)



**NB** ：




- 對於雙重認證，請確定您的認證應用程式支援 SHA256 協定和 8 位元代碼。Ginger Wallet 需要 8 位數的 2FA 代碼來加強安全性。這種較長的格式使代碼更難猜測或破解，提供更強的保護，防止未經授權的存取。
- 預設情況下，所有 Ginger 網路流量都會通過 Tor，因此不需要手動設定。如果 Tor 已在您的系統上啟用，Ginger 會自動給予它優先權。



但是一旦您在設定中停用 Tor，您的隱私一般仍會保留，除了兩種情況：




- 在 Coinjoin 期間，協調員可以將您的輸入和輸出與您的 IP 位址相連結；
- 當廣播交易時，與您連線的惡意節點可能會將您的交易與您的 IP 聯繫起來。



不要忘記每次按 **完成** (在右下角)，以儲存您的設定。有些設定需要重新啟動 Ginger Wallet 才能生效。



此外，投資組合頂端的搜尋列可讓您搜尋並存取任何參數等...



![screen](assets/fr/22.webp)




### 投資組合配置



可在應用程式中建立多個組合，因此每個組合都可依您的需求進行設定。若要這樣做，請按一下組合名稱前面的**三點**，然後按一下 **組合設定**。



![screen](assets/fr/23.webp)



如您所見，除了 wallet 參數之外，您還能看到您的 UTXOs（您擁有的代幣清單）、統計資料和 wallet 資訊（例如擴充的公開金鑰等）。



若要返回我們的投資組合設定，點選投資組合參數後，您會看到下列標籤：




- 一般** (您可以在此變更投資組合名稱) ；



![screen](assets/fr/24.webp)





- Coinjoin** （您可在此自訂此 wallet 的 Coinjoin 設定） ；



![screen](assets/fr/25.webp)





- 工具** (在這裡您可以檢查您的 seedphrase、再次同步化您的投資組合，或刪除它)。



![screen](assets/fr/26.webp)




## 接收比特幣



![video](https://youtu.be/cqv35wBDWMQ)



要在 Ginger Wallet 上的 wallet 中接收比特幣：




- 按 ** 接收** ；



![screen](assets/fr/27.webp)





- 輸入您希望關聯地址的來源名稱。這是用來追蹤付款的標籤。這對 on-chain 沒有任何影響；這只是本機儲存於您應用程式中的可追蹤性資訊；



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- 按一下 **Generate** 左邊的小箭頭，選擇您的地址格式 (**SegWit** /**Taproot**) ，然後按一下 **Generate**，以 generate 產生地址和 QR 碼。



![screen](assets/fr/29.webp)



此地址或 QR 代碼將被您的發件人用作向您發送 bitcoins。



![screen](assets/fr/30.webp)




## 發送比特幣




![video](https://youtu.be/2nf5aAimfhg)



要做到這一點：




- 按下 ** 傳送** 按鈕；
- 輸入收件人地址、要寄送的金額和標籤；
- 檢查交易概觀，並確認發送。



![screen](assets/fr/31.webp)




## 花費比特幣



使用 Ginger Wallet 買賣 Bitcoin 非常簡單。只需幾個步驟，您就可以花費比特幣。



### 購買比特幣



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet 使用者可以購買比特幣。





- 按下**購買**按鈕。即使 wallet 是空的，此按鈕仍會顯示。



![screen](assets/fr/32.webp)





- 在進行比特幣購買之前，請選擇您的國家，甚至您的州（在某些地區，如加拿大）。事實上，當您第一次點擊**購買**功能時，您也需要指定您的地區。



![screen](assets/fr/33.webp)



按 ** 繼續** 進入購買程序。





- 然後在專用欄位中輸入您要購買的比特幣數量。您也可以選擇交易貨幣。



![screen](assets/fr/34.webp)



每種貨幣都有最低和最高購買限額。例如，美元的最高限額為 30,000 美元。



如果您已經購買，您可以按一下 ** 以前的訂單** 按鈕，檢視您的交易記錄。將會顯示過去的交易清單及其狀態。





- 選擇適合您的優惠。



此時，您會看到所有可用優惠的清單。對於每個優惠，您都有 ：




 - 供應商名稱 (1) ；
 - 與之前輸入的金額相等的比特幣數量、付款方式和購買費用 (2) ；
 - 按**接受**按鈕 (3)。



![screen](assets/fr/35.webp)



報價中顯示的費用不構成額外費用。這些費用已包含在報價的總金額中。



畫面右上角標有 **全部**，可讓您依付款方式篩選報價。您所選擇的付款方式將作預設設定，但可隨時變更。



![screen](assets/fr/36.webp)



如果您找到合適的報價，請點擊 **接受** 按鈕繼續購買。然後您會被轉到賣家的頁面，在那裡您可以完成交易。



### 出售比特幣



Ginger Wallet 使用者可以出售 Bitcoin。只有在投資組合中有可用資金時，才能看到**出售**按鈕。





- 按一下 ** 出售**。



![screen](assets/fr/37.webp)





- 與**購買**選項一樣，當您第一次使用賣出功能時，必須先選擇您的國家，才能進行比特幣銷售。





- 接下來，您需要輸入要出售的比特幣數量。您可以輸入 BTC 或美元 (USD) 等法定貨幣的金額。





- 完成此步驟後，您會看到可用優惠的清單。選擇適合您的銷售優惠，然後按一下 **接受**繼續。





- 現在您需要完成交易：
 - 接受報價後，您會被轉到供應商的頁面；
 - 請遵循供應商頁面上的指示 ；
 - 在某個時候，您會收到收件者地址和確切的寄送金額；
 - 然後再回到 Ginger Wallet 繼續處理；
 - 回到 Ginger Wallet 後，會出現對話方塊，讓您按一下 **Send** 繼續。



這將會開啟 **Send** 畫面，並預先填入收件者的地址和金額。您也可以使用主畫面上的 **Send** 按鈕。雖然您可以手動發送交易，但我們建議您透過對話方塊完成交易，以優化流程。



## 在 Ginger Wallet 上進行共同接合



![Vidéo](https://youtu.be/AJe67RDfB1A)



使用**Coinjoin**保護您比特幣的機密性，直接整合至 Ginger Wallet。wallet 使用 **WabiSabi**，這是一種 Chaumian 硬幣兌換協定，旨在促進更方便、更有效率的硬幣兌換。



您可以選擇最適合您的硬幣接合策略（自動或手動）。



只要下載 Ginger Coinjoin 即可使用（無需其他步驟）。Ginger Coinjoin 會自動在背景運行，以保護您每次交易的隱私。實際上，只要您有可以匿名的餘額，Coinjoin 播放器就會出現。



至於手動啟動coinjoin，則是一鍵式操作。啟動一輪，等待建立並確認 Coinjoin 交易。您會在介面中看到匿名分數。



可以進行多次混音，直到達到所需的匿名程度為止。您也可以從混音中排除某些部分。



預設情況下，Ginger 使用自己的協調器，並提供所有預設參數和保證費用。價值超過 0.03 BTC 的代幣的 Coinjoins 除 mining 費用外，還會產生 0.3% 的協調器費用。價值在 0.03 BTC 或以下的入幣以及混幣，即使在單次交易後，也免收協調費。因此，使用Coinjoin資金進行支付，發送人和接收人都可以重新混合他們的錢幣，而不會產生協調費。



Ginger 較喜歡參與人數較多的硬幣兌換，而非較小、速度較快的硬幣兌換。較大的硬幣接合提供更多的匿名性、更低的成本和更高的區塊空間效率。




## 安全與最佳實務



分散化的願望和隱私權的保護需要採用幾種最佳實務：




- 務必將 seedphrase 存放在離線的安全地方；
- 如果您遺失電腦或懷疑有人未經授權存取，請立即建立新的 wallet。將您的資金轉移至這個新的投資組合，並刪除舊的投資組合；
- 每次接待使用不同的地址，避免重複使用地址；
- 請務必僅從官方 GitHub 帳戶或官方網站下載您的作品集應用程式。



現在您已熟悉使用 Ginger Wallet 應用程式來傳送、接收和花費您的 bitcoins。



如果您覺得本教學有用，請在下方給我留下綠色拇指。請隨時透過您的社交媒體平台分享這篇文章。非常感謝



我也建議您看看這篇教學，了解如何使用 Liana 電腦應用程式來傳送和接收比特幣，以及執行自動化的遺產計畫。



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04