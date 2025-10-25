---
name: COLDCARD - 聯署
description: 發現 Co-Sign 功能並在您的 COLDCARD 上使用它
---

![cover](assets/cover.webp)


*注意：本教學的對象為已經對多重簽章錢包、Coinkite 裝置以及 Sparrow wallet 或 Nunchuk.* 等軟體有一定經驗的人。



![video](https://youtu.be/MjMPDUWWegw)




**為什麼要 ColdCard Co-Sign？



此功能可讓您以硬體安全模組 (HSM) 的方式，在 ColdCard (Q 或 Mk4) 裝置中加入**支出條件**，以保護您的資金，同時保留相當大的彈性與控制權。



支出條件可以是，例如





- 幅度限制**：限制您在單一交易中可以花費的比特幣數量。
- 速度限制：** 決定每單位時間（每小時、每天、每週等）可進行多少筆交易，要求交易之間最少有多少個區塊。
- 預先核准的地址：** 僅允許將 bitcoins 傳送至預先核准的地址。
- 雙因素驗證：** 需要由可存取網際網路的 NFC 智慧型手機/平板電腦上的第三方 2FA 行動應用程式 (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238))確認。



**如何運作



在您的 ColdCard Mk4 或 Q 裝置中加入第二個 seed，稱為「消費政策鑰匙」，在本教程中我們將稱之「C 鑰匙」。


除了這個額外的 seed 之外，您會被要求 Supply 至少一個額外的金鑰 (XPUB)，我們稱之為 「備份金鑰」，以便建立 Wallet Multisig 2-on-N。



總而言之，我們要建立一個 Wallet Multisig，而您的 ColdCard 裝置將包含花費資金所需的 2 個私人金鑰，裝置的 seed 主金鑰和「花費政策金鑰」。



每次要求「C Key」簽名時，指定的消費條件都會適用，ColdCard 只有在交易符合這些條件時才會簽名。



如果您希望免除這些消費條件，您可以這樣做：




- 使用其中一個備份按鍵和 seed 手柄，或 2 個備份按鍵（取決於您 Multisig 的大小）簽名。
- 在「共同簽署」功能表中輸入「消費政策鍵」或「C 鍵」。 *** 後者不能直接在裝置上查詢，否則任何人都可以取消設定的花費條件。




## 設定 ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- 啟動功能



首先，請確定您的裝置至少有最新的韌體版本：




- Mk4: v5.4.2
- Q: v1.3.2Q




在您的 Mk4 或 ColdCardQ 上，移至 *Advanced Tools > ColdCard Co-Signing*。



![Co-Sign](assets/fr/01.webp)



*在以下教學中，為了方便起見，截圖將在 ColdCardQ 上進行，但 Mk4 和 Q 的步驟和功能表完全相同*。



顯示功能摘要。


在我們即將建立的 2 對 3 多重簽章 Wallet 中，用來指定鑰匙的術語是：



鍵 A = 冷卡主機 seed


鍵 B = 備份鍵


鍵 C = 開銷政策鍵



按一下 **"ENTER "**。



![Co-Sign](assets/fr/02.webp)



下一步是決定哪個私人密碼匙會作為「支出政策密碼匙」或「密碼 C」。



我們可以看到，我們有多種選擇：





- 或按下 **"ENTER "**，generate 會產生一個新的 seed 句子，共 12 個字。





- 點選 **"(1) 「** 匯入現有的 12 字 seed，或選擇 **」(2) "** 匯入現有的 24 字 seed。





- 或按下 **"(6) "**，從裝置的儲存庫匯入 seed。



為了本教程的目的，我們決定按**"(1) "**來匯入現有的 12 字元 seed。這可以是您已經擁有的任何 seed BIP39，而且您顯然也有備份。



使用鍵盤輸入 seed 的 12 個字。在這個範例中，我們選擇 seed 有效詞組 beef x 12。然後按下 **"ENTER "**。


*注意：如果您沒有備份此 seed，您將無法再修改裝置上的「共同簽署」設定，以變更您的消費條件*。



現在裝置上的「共同簽署」功能已啟動。接下來我們需要選擇我們的消費條件，然後完成多重簽名 Wallet 的建立。



![Co-Sign](assets/fr/03.webp)



### 2- 選擇支出條件或 「*支出政策*」



在此我們指定當 **「C Key」** 或 **「Spending Policy Key**」簽署交易時必須符合的支出條件。



在 **「共同簽署」** 功能表中，按一下 **「支出政策**」。



然後，您可以選擇最大幅度，也就是單筆交易可花費的最大 Satoshis 數量。



在這個範例中，我們選擇最大幅值為 **21212** 衛星。按一下 **「ENTER」** 確認。




![Co-Sign](assets/fr/04.webp)



接著我們選擇設定最大速度，也就是裝置在單位時間內能簽署的交易數量。在本教程中，我們將選擇無限制速度，即交易數量不受限制。




![Co-Sign](assets/fr/05.webp)



### 3- 建立 Wallet Multisig 2-on-N



除了裝置的 ** 主 seed** (Key A) 和 ** "Spending Policy Key「 ** (Key C) 之外，我們仍需要為 Wallet Multisig 選擇第三個金鑰，也就是 **」備份金鑰 "** (Key B)。



我們的「B Key」必須透過 SD 卡或 ColdCardQ 的 QR code 匯入。


要做到這一點，我們需要第二台 ColdCard Mk4 或 Q 裝置，在這台裝置上使用我們的 "Key B"。



在第二台載有 **「備份鑰匙」** 的裝置（例如 ColdCard Mk4）上，從主功能表轉到 **「設定」**，然後轉到 **「Multisig Wallet」**，最後轉到 **「匯出 Xpub」**。


(如果您的第二台裝置是 ColdCardQ，您當然可以選擇透過 QR code 匯出您的 Xpub）。





![Co-Sign](assets/fr/06.webp)





在下一個畫面中，插入 SD 卡並按一下右下方的 **「驗證 」**按鈕。然後按 **"(1) "**，將檔案儲存到 SD 卡上。



檔案名稱中會包含公開金鑰指紋 (*指紋*)，格式為 `ccxp-0F056943.json`。




![Co-Sign](assets/fr/07.webp)



然後將 SD 卡插入「初始」ColdCardQ，匯入我們的「備份金鑰」（金鑰 B）。


在 "ColdCard Co-Signing 「選單中選擇 」Build 2-of-N「，然後在下一個畫面中按**」ENTER 「**，再按一次**」ENTER 「**從 SD 卡中匯入 」Backup Key"。



![Co-Sign](assets/fr/08.webp)



在下一個畫面中，將「帳號」留空（除非您很清楚自己在做什麼），然後再按一次 **「ENTER」**。



![Co-Sign](assets/fr/09.webp)



最後，我們準備使用新的 Wallet Multisig 2-sur-3，組成如下：



鍵 A= 冷卡 Q 主控 seed


金鑰 B= 備份金鑰 (剛從第二台 Coldcard 裝置匯入)


金鑰 C= 支出政策金鑰（若用於簽署，會強制預先定義的支出條件）



## 與 Sparrow wallet 聯署



如有必要，請參閱下列教學以熟悉 Sparrow wallet 軟體：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.network/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- 出口 Wallet Multisig 2-sur-3 至 Sparrow wallet



現在我們需要將 Wallet Multisig 匯出到 Sparrow，以便在那裡放置第一個衛星。



從 ColdCardQ 的主功能表，選擇 **「設定」**，然後選擇 **「Multisig Wallets」**。


現在會顯示您的 ColdCard 所知道的 Multisig 錢包集合，這裡所涉及的金鑰數量為 "2/3" (2-sur3)。選擇我們剛建立的 Multisig **「ColdCard Co-Sign」**，然後按一下 **「ColdCard Export」**。



![Co-Sign](assets/fr/10.webp)




最後，選擇可以將 Wallet 匯出到 Sparrow 的方法。在我們的例子中，我們會選擇 SD 卡，因此在裝置的插槽 A 中插入 SD 卡後，點選 **"(1) "**。



![Co-Sign](assets/fr/11.webp)



然後在 Sparrow wallet 中選擇「匯入 Wallet」。



![Co-Sign](assets/fr/12.webp)



然後按一下 **「匯入檔案 」**。然後選擇 SD 卡上的檔案 **"export-Coldcard_Co-sign.txt "**。



![Co-Sign](assets/fr/13.webp)



為您的 Wallet 取一個名稱，就像它會出現在 Sparrow 中一樣，並選擇一個密碼來加密您的 Wallet（或不加密）。



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



我們現在已經準備好接收第一批衛星，並測試我們套用在 Wallet 上的消費條件。



![Co-Sign](assets/fr/16.webp)



### 2- 測試預先定義的支出政策



作為提醒，我們已決定 Wallet Multisig 的最大值為 21212 Satoshis。這表示每次花費政策金鑰 (Key C) 簽署交易時，只有當花費金額小於或等於 21212 Satoshis 時，後者才會有效。



我們來測試一下。


首先，讓我們按一下 Sparrow 中的「接收」標籤，然後將幾個 Satss 放到 Wallet，在本教程中我們會一直使用 Wallet。



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



然後，讓我們嘗試模擬 50,000 Sats 的交易，花費超過 21212 允許的 Satoshis。



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



使用 ColdCardQ 掃描代表*未簽名*交易的 QR 碼以匯入交易後，螢幕上顯示的就是這個畫面。一則警告訊息告訴我們消費條件尚未符合。如果我們還是簽署交易，那麼 2 個金鑰 (裝置上的 seed 主鑰，但不是「金鑰 C」) 中只有一個會簽署。




![Co-Sign](assets/fr/23.webp)



在這裡，將我們的交易匯入 Sparrow 之後，我們可以看到只有其中一個簽章套用在交易上。



![Co-Sign](assets/fr/24.webp)




現在讓我們重複實驗，但交易額為 21,000 衛星，也就是小於我們為這個 Wallet 設定的最大幅度 (21212 Sats)。




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



讓我們嘗試使用 ColdCardQ 簽署此交易。



這次沒問題，沒有出現警告訊息，而且當我們將已簽署的交易匯入 Sparrow wallet 時，這次已套用了 2 個簽章，使交易有效並可供分發。




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## 與雙節棍共同簽名



https://planb.network/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- 網路 2FA 與白名單地址



在本段中，我們將使用我們的 Wallet Multisig 與 Nunchuk 的 Co-Sign，並藉此機會套用新的消費條件，看看效果如何。



移至 *進階工具 > ColdCard Co-Signing*。


我們會被要求輸入「消費政策鍵」，以進入菜單允許我們變更消費條件。在我們的案例中，我們輸入 12 x 「牛肉」。



基於與本教程相關的實際原因，我們決定保留 21212 Sats 的幅度和最大「限制速度」。另一方面，我們要使用 **「白名單地址 」** 功能表來強制我們的資金可以用在哪些地址上。




![Co-Sign](assets/fr/31.webp)




掃描與您希望加入白名單的地址（我們將選擇 2 個）相關的 QR 代碼，然後按下 **"ENTER "**。連續按下 **"ENTER "**，驗證您的地址後，我們會看到 Magnitude 和受益人地址的限制已套用。



![Co-Sign](assets/fr/32.webp)



最後，為了完整了解「Co-Sign」提供的可能性，讓我們啟動「Web 2FA」選項。


此功能可讓您使用符合 TOTP RFC-6238 的應用程式，例如 Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / 或 Aegis Authenticator，以增加額外的 Layer 安全性。



https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

具體來說，在簽署交易之前，您需要將具備 NFC 功能、連線至網路的裝置靠近您的 Coldcard。這會自動帶您到一個coldcard.com網頁，在那裡您會被要求輸入您申請的六位數代碼。如果您輸入正確的代碼，網頁會顯示一個 QR 代碼讓您掃瞄 ColdCardQ，或是一個 8 位數的代碼讓您在 Mk4 上輸入，以授權您的裝置簽署。





![Co-Sign](assets/fr/33.webp)



掃描雙重認證應用程式中顯示的 QR 代碼，並新增您的 ColdCard Co-Sign (CCC) 帳戶後，系統會要求您輸入 2FA 代碼，確認一切正常。



在 NFC 裝置背面輸入您的 ColdCard。



![Co-Sign](assets/fr/34.webp)



在開啟的網頁上，輸入您最喜愛的應用程式的 2FA 代碼。然後掃描 ColdCardQ 顯示的 QR 碼 (或輸入 Mk4 顯示的 8 位數碼)。



![Co-Sign](assets/fr/35.webp)




我們現在對幅度 (21212 Sats)、目的位址和雙重驗證施加了限制。



![Co-Sign](assets/fr/36.webp)



### 2- 導出 Wallet Multisig 2 對 3 至雙節棍



這次讓我們把 Wallet Multisig 2 對 3 輸出到 Nunchuk 中，就像之前對 Sparrow 所做的一樣。


移至 *Settings > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*。



![Co-Sign](assets/fr/10.webp)



這次按一下同名的 ColdcardQ 按鈕 ** "NFC "**，選擇要匯出的 NFC 選項。



![Co-Sign](assets/fr/37.webp)



在 Nunchuk 中，如果您是第一次開啟應用程式，請按一下 **「恢復現有的 Wallet」**。



![Co-Sign](assets/fr/38.webp)



如果您的應用程式中已有 Wallet，請按一下右上方的 **"+「**，然後按一下 **」恢復現有的 Wallet"**。



![Co-Sign](assets/fr/39.webp)




然後選擇 **「從 COLDCARD 復原 Wallet」**，再選擇 **"Multisig Wallet"**。



![Co-Sign](assets/fr/40.webp)



最後，將智慧型手機背面輕觸 ColdCardQ 的螢幕，即可透過 NFC 匯入 Wallet。



![Co-Sign](assets/fr/41.webp)



我們的帳戶和之前透過 Sparrow wallet 存入的 Satoshis 又回來了。



![Co-Sign](assets/fr/42.webp)



### 3- 測試預先定義的支出政策



現在讓我們嘗試進行一筆違反我們所設定的 2 個消費條件的交易。 **我們嘗試花費超過 21212 Sats 到一個尚未核准的 Address。** 讓我們嘗試發送 22 222 Sats 到隨機的 Address。



![Co-Sign](assets/fr/43.webp)



建立交易後，按一下右上角的三個小圓點，即可將交易匯出到您的 ColdCard。



![Co-Sign](assets/fr/44.webp)



然後選擇 **「透過 BBQR 匯出」**，並掃描 ColdCardQ 顯示的 QR 代碼。



![Co-Sign](assets/fr/45.webp)



您的 ColdcardQ 隨後會顯示警告，當您滾動到螢幕底部時，會說明交易違反消費條件，一如所料。



*** 請注意，為了防止潛在攻擊者試圖規避限制，裝置並沒有告訴我們涉及哪些消費條件。




![Co-Sign](assets/fr/46.webp)



如果您仍然按 **"ENTER "**進行驗證，則會出現代表已簽署交易的 QR 代碼。如果您在 Nunchuk 上匯入，您可以看到只套用了一個簽章。



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






讓我們執行完全相同的作業，但這次的交易要遵守大小限制 (21212 Sats)，並將 Satoshis 支出到我們預先設定的 2 個位址之一。



我們將 Nunchuk 12121 Sats 傳送至我們的 2 個地址之一。然後，我們按照之前的方式將交易匯出到我們的 ColdCard。



![Co-Sign](assets/fr/49.webp)




將未簽署的交易匯入 ColdCardQ 之後，讓我們看看這次顯示的內容。



警告訊息總是會出現，但這次捲動到螢幕下方，我們看到要透過 2FA 來驗證交易。裝置要求我們將 ColdcardQ 靠近連線網路的 NFC 終端 (智慧型手機或平板電腦)，我們照做了。



![Co-Sign](assets/fr/50.webp)



我們的智慧型手機會開啟一個網頁，要求我們輸入 2FA 代碼，由於使用了 Proton Authenticator，我們輸入了代碼。



![Co-Sign](assets/fr/51.webp)





然後掃描網頁上出現的 QR 代碼，授權您的 ColdCard 簽署交易。


現在交易已由 2 個金鑰簽署，因此是有效的。



如果您的 ColdCardQ 已啟用「Push Tx」功能，您只需在智慧型手機背面輕輕一按，即可將交易直接廣播至網路。



![Co-Sign](assets/fr/52.webp)




如果您沒有啟動 "Push tx「，請按下 ColdCardQ 上的 」QR "按鈕，將已簽署的交易顯示為 QR 碼，並將其匯入 Nunchuk，方法與上一個範例相同。



![Co-Sign](assets/fr/53.webp)



這次我們注意到有 2 個簽章已被套用，因此交易已準備好在 Bitcoin 網路上廣播。



![Co-Sign](assets/fr/54.webp)




本教學已接近尾聲，我們將為您概述整合於 Coinkite 的 ColdCardQ 和 Mk4 裝置中的 Co-Sign 功能所提供的可能性，以及透過 Sparrow 和 Nunchuk 等錢包的使用方式。