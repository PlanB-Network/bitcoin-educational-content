---
name: COLDCARD Q - Key Teleport
description: 什麼是 Key Teleport，該如何使用？
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Coinkite 旗艦產品 ColdCardQ 所提供的 **Key Teleport** 功能是什麼？



**Key Teleport** 可讓您在 2 張 ColdCardQ 之間安全地傳輸機密資料。傳輸通道甚至不需要加密，也可以是公開的。



這可以用來轉移：





- **gW-0 phrases** (ColdCard Q 的 seed master 或 ColdCardQ 的 [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault) 中儲存的秘密。
- 保密筆記與密碼：這可以是任何秘密或您 ColdCardQ 上的整個 **保密筆記與密碼** 目錄 (https://coldcard.com/docs/secure_notes/)。
- 整個 ColdCardQ 的備份：接收此備份的 ColdCardQ 必須沒有 seed Master 才能運作。
- gW-3（**部分簽署的 Bitcoin 交易**）作為多重簽署方案的一部分。



這需要您將 [裝置韌體升級至版本 v1.3.2Q](https://coldcard.com/docs/upgrade/) 或更高。



## 如何使用鑰匙傳送？



### 1- 傳輸任何類型的資料



在此，我們將檢視 seed 句子、筆記、密碼的傳輸，或 ColdCardQ 備份的整個傳輸。至於多重簽名交易的 PSBT 傳輸情況，則會在稍後進行處理。



#### 準備裝置以接收秘密



在 ColdCardQ 的 **「進階 / 工具**」功能表中，選擇 **「按鍵遠距傳送 (開始) 」**。


在下一個畫面中，會提出一個 8 位數的密碼，這裡是 "20420219"。您需要將這個密碼傳送給寄件者。例如，使用 sms 或您喜愛的安全訊息系統，甚至語音通話來傳送此密碼。



然後點擊 ColdCardQ 上的 **"Enter**"按鈕進入下一步。




![CCQ-key-teleport](assets/fr/01.webp)




螢幕上會產生一個 QR 碼。再一次，您需要將這個 QR 代碼傳達給 ColdCardQ 的「寄件者」。最簡單的方法是透過視訊通話。



**請勿透過傳送前一個 8 位數密碼的相同傳送通道傳送此 QR 碼**。



![CCQ-key-teleport](assets/fr/02.webp)



*對於有興趣的人，讓我們嘗試了解允許秘密透過不安全通道傳輸的基本機制*。



*我們在這裡實際上是透過 Diffie-Hellman 方法啟動秘密傳輸，這在我以下附上的 BTC204 課程中有所涵蓋*。



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*我們目前有：*




- 產生一組短暫金鑰 (公鑰/私鑰分別為 Ka 和 ka，Ka=G.ka，G 為 ECDH 產生點)，以及一個 8 位數的密碼。
- 使用此密碼透過 AES-256-CTR 加密公開金鑰 (Ka)，然後將此密碼透過通訊通道 A 傳送給「傳送」ColdCardQ。
- 最後，我們使用與第一個*不同的第二個通訊通道 B，透過上述 QR 碼將加密的封包傳送給寄件者。



#### 準備傳送秘密的裝置



從「發送」裝置，按一下 **「QR」** 按鈕，掃描接收裝置傳送給您的 QR 碼，然後透過另一個通道輸入上一步通訊給您的 8 位數密碼。現在我們已準備好從 「發送 」裝置開始傳送資料。



**請勿輸入錯誤的 8 位數密碼，因為不會顯示任何錯誤訊息，程序也會繼續。但是，最後的資料傳輸將會失敗，您必須重新開始**。



![CCQ-key-teleport](assets/fr/03.webp)



*對於好奇心較重的各位，讓我們再來看看我們在密碼學及秘密傳輸方面的成果：*




- 我們透過掃描接收裝置上的 QR 代碼來匯入加密資料。
- 然後我們使用經由第二管道*傳送給我們的 8 位數密碼來解密。
- 因此，我們擁有接收者最初所產生的公開金鑰 (Ka)。
- 然後，我們在傳送裝置上 generate 新的短暫金鑰對 (Kb/kb，Kb=G.kb)，用來對 Ka 應用 ECDH。因此，我們執行 kb.Ka=Ks 的操作，其中 Ks 稱為 **「會話金鑰」**。




現在會要求您選擇要在 2 張 ColdCardQ 之間傳輸的秘密的性質 (機密筆記、密碼、完整備份、儲存庫中的種子、seed 裝置主機)。



![CCQ-key-teleport](assets/fr/04.webp)



在此，我們的秘訣是選擇 **「快速文字訊息 」**，以傳送一則短訊。輸入您的訊息 (對我們來說是 "PlanB Network rocks「)，然後按 **」ENTER "**。


然後，裝置會產生一個新的隨機密碼，稱為 **「Teleport密碼 」**，範例為 "NE XG BT SK"。



![CCQ-key-teleport](assets/fr/05.webp)



按下 **"ENTER "**，您會看到一個新的 QR 代碼。讓接收裝置掃描這個 QR 碼。然後在不同的通訊頻道上，傳送 **「Teleport密碼 」** 給接收裝置。



![CCQ-key-teleport](assets/fr/06.webp)



*在此，為了讓好奇的人再次瞭解，在此階段：*




- 選擇要傳輸的秘密後，我們會 generate 一個新的隨機密碼，稱為 ***「Teleport Password」***。
- 然後我們使用上一步產生的 **「會話金鑰」**，「Ks」，透過 AES-256-CTR 加密秘密。
- 我們用 Kb 公開金鑰為已加密的 **「會話金鑰」** 封包加上前綴，然後再用 **「遠程傳輸密碼」** 再加上 Layer 的 AES-256-CTR 加密。然後整件事會編碼為 QR 碼




#### 完成傳送秘密至接收裝置



按下 **"QR "**按鈕，掃描發送設備透過 visio 通道顯示的 QR 代碼。您會被要求輸入您的**"Teleport Password 「**，以取得我們的 」NE XG BT SK"。



![CCQ-key-teleport](assets/fr/07.webp)





然後，資料會被解密，並讓接收裝置明白。接收到的訊息確實是 "PlanB Network rocks"。僅此而已。



![CCQ-key-teleport](assets/fr/08.webp)



**最後階段究竟發生了什麼事？**




- 我們已經用**"Teleport Password "**解密了寄件者傳送的資料。
- 因此，我們有公開金鑰 Kb，以及由 **「會話金鑰」**「Ks」加密的秘密訊息。但是，作為接收方，我們不知道由發送方建立的 Ks，那麼我們該如何做到這一點呢？
- 我們需要將初始步驟 **「準備接收資料的裝置」** 中的私人金鑰「ka」套用至公開金鑰 **Kb**。
- 事實上，透過計算 ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks ，我們可以找到 Ks。最後用來破譯秘密訊息。



### 2- 將 PSBT 移轉至 Multisig（進階）



前提是您的 Wallet Multisig 已經建立，而且您的 ColdCardQ 裝置已預設為可以執行多重簽名交易。如果情況並非如此，您可在 Coinkite 網站 [此處](https://coldcard.com/docs/Multisig/) 取得說明。



快速提醒一下什麼是多重簽章 Wallet（Multisig）。



通常，要使用您的 Wallet 資金，只需一個私人密碼匙即可解鎖與您地址相關的 UTXO。


在 Wallet Multisig 的情況下，可能需要多達 15 個私人密碼匙，因此也需要 15 個簽名才能使用資金。這就是所謂的「M out of N」組合，N 介於 1 到 15 之間，而 M 則是可動用資金所需的簽名數目。例如，Wallet Multisig 3 出 5 將需要在可能的 5 個簽名中至少 3 個簽名。



接下來的挑戰就是在簽署者之間協調，依次為「Partially Signed Bitcoin Transaction」簽署「PSBT」。在這種情況下，「**Key Teleport**」可用來在共同簽署人之間以簡單且保密的方式傳輸 PSBT。共同簽署人之間進行簡單的視訊通話即可達成此目的。



以下是在 Multisig 3 of 4 上的操作方法。



**簽署人：**



簽署人 1 匯入並簽署 PSBT。最後，他按一下 **"T 「**，使用 **」Key Teleport "**，將 PSBT 傳送至簽名者 2。



![CCQ-key-teleport](assets/fr/09.webp)




按**"ENTER"**選擇簽署人 2 後，會提供一個**"TELEPORT PASSWORD"**（此處為 JJ YC AB 6A），必須透過其他通訊管道傳送給簽署人 2。例如，SMS 或語音通話，但**不是視訊通話**。



再按一次 **"ENTER "**，就會出現代表 PSBT 的 QR 碼，該 QR 碼由 1 簽署，然後由「電信埠密碼」加密。



![CCQ-key-teleport](assets/fr/10.webp)



**簽署人2：**



簽名員 2 掃描簽名員 1 向其出示的 QR 代碼。然後輸入透過第二通訊管道傳送的「電信埠密碼」，以解密傳送的資料。



簽名員 2 簽署交易，然後點選 **"T "**，透過「Key Teleport」將 PSBT 傳送至簽名員 3。


很明顯，已經有 2 個簽名。要使交易有效，只差簽名人 3 了。按一下 **"ENTER "**，選擇簽署人 3。



![CCQ-key-teleport](assets/fr/11.webp)



並建立一個新的「電信埠密碼」，接著再以 QR 碼編碼由 1 和 2 簽署的 PSBT，然後以這個新的「電信埠密碼」加密 (GW YQ K3 LL)。



![CCQ-key-teleport](assets/fr/12.webp)



**簽署人：**



重複上述相同步驟。


簽名員 3 掃描簽名員 2 向其出示的 QR 代碼。然後輸入由第二通訊管道傳送的 "TELEPORT PASSWORD"。



簽名者 3 簽署交易，這一次，由於 4 個簽名中有 3 個已經完成，因此交易被顯示為已完成，並可透過各種媒體 (SD 卡、NFC、QR 等) 發佈。



![CCQ-key-teleport](assets/fr/13.webp)



如果 ColdCardQ 的「Push Tx」功能已啟動，只要將 ColdCardQ 貼在任何 NFC 網路連線裝置 (智慧型手機/平板電腦) 的背面，即可透過 Bitcoin 網路廣播交易。



![CCQ-key-teleport](assets/fr/14.webp)



*對於 PSBT 從一個簽名者傳輸到另一個簽名者，「金鑰遠傳」只需在每個階段透過「遠傳密碼」來使用，當 PSBT 從一個簽名者傳輸到另一個簽名者時，「金鑰遠傳」會對其進行加密。由於傳輸的資料不會被用來竊取資金，因此不需要像傳送高度機密的秘密 (seed、密碼等...)*一樣，使用 Diffie-Hellman 加密。



![CCQ-key-teleport](assets/fr/15.webp)



*來源：[ColdCard 官方網站](https://coldcard.com/)*