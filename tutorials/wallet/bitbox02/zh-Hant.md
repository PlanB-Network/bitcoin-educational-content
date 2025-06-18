---
name: BitBox02

description: 設定與使用 BitBox02
---

![cover](assets/cover.webp)


BitBox02 (https://bitbox.swiss/) 是專為保護您的比特幣而設計的瑞士製實體 Wallet。它的一些主要功能包括使用 microSD 卡輕鬆備份和還原、簡約低調的設計以及全面支援 Bitcoin。


![device](assets/1.webp)


它提供由專家設計的尖端安全性，具有雙晶片設計，包括安全晶片。它的源代碼已通過安全研究人員的全面審核，並且完全開放源碼。BitBox02 隨附簡單但功能強大的 BitBoxApp，可安全管理您的比特幣。它支援 Full node for Bitcoin，並確保應用程式與裝置之間的端對端加密通訊。BitBox02 於瑞士製造，在用戶中贏得了良好的聲譽。


![video](https://youtu.be/sB4b2PbYaj0)


以下是 Wallet 的規格：



- 連接性：USB-C
- 相容性：Windows 7 及更新版本、macOS 10.13 及更新版本、Linux、Android
- 輸入：電容式觸控感應器
- 微控制器：ATSAMD51J20A；120 Mhz 32 位元 Cortex-M4F；真正的隨機數字產生器
- 安全晶片：ATECC608B; 真正的隨機數字產生器 (NIST SP 800-90A/B/C)
- 顯示器：128 x 64 px 白色 OLED
- 材質：聚碳酸酯
- 尺寸：54.5 x 25.4 x 9.6 mm (含 USB-C 插頭)
- 重量：裝置 12 克；連包裝及配件 160 克


在其網站上下載資料表 https://bitbox.swiss/bitbox02/


## 如何使用 BitBox02 Hardware Wallet


### 設定 BitBox02


BitBox02 的外殼附有 USB-C 連接埠。如果您的電腦使用一般的 USB 連接埠，您必須使用裝置隨附的轉接頭。


將它連接到電腦，裝置就會開機（先別做）。


它的上方和下方都有感應器，會提示您觸控上方或下方，以您想要的方式調整螢幕方向。


![image](assets/2.webp)


### 下載 BitBox02 應用程式


請造訪 https://shiftcrypto.ch/，點選上方的「App」連結即可進入下載頁面：


![image](assets/3.webp)


按一下藍色的 Download 按鈕：


![image](assets/4.webp)


若要驗證下載（會增加複雜性，但建議使用，尤其是當您儲存大量 Bitcoin 時），請參閱附錄 A。


下載完成後，您可以解壓縮檔案。在 Mac 上，只要按兩下下載的檔案，BitBox App 圖示就會出現在您的下載目錄中。您可以將它拖曳到桌面（或任何地方），以方便存取。


按兩下應用程式來執行它（它不會被「安裝」）。


在 Mac 上，您的電腦保姆會給您警告。請忽略它並按一下「開啟」：


![image](assets/5.webp)


然後您會看到這個：


![image](assets/6.webp)


繼續將裝置連接至電腦。


它會顯示配對碼。檢查它們是否相符，然後輕觸感應器選擇核取標記。然後回到螢幕，繼續按鈕將可供您使用。


![image](assets/7.webp)


接下來您可以選擇建立新的 seed，或是還原 seed。我將示範建立一個新的 seed（在您將任何 Bitcoin 載入 Wallet 之前，也必須還原您建立的 seed，以測試備份的品質）。


![image](assets/8.webp)


本裝置隨附 microSD 卡。如果您沒有，請繼續插入。


![image](assets/9.webp)


為裝置命名並按一下繼續，然後在裝置上確認。


![image](assets/10.webp)


接著會要求您為裝置設定密碼。這不是您 seed 的一部分。它也不是 passphrase（那是您的 seed 的一部分）。它只是鎖定裝置的密碼。當您開啟裝置時，每次都會要求您輸入這個密碼。在裝置清除所有記憶體之前，您有 10 次連續失敗的允許時間，所以請小心。螢幕上的動畫會教您如何使用裝置控制項來設定密碼。


![image](assets/11.webp)


閱讀下一個畫面，勾選每個方塊，然後繼續。


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


這就是 Wallet 準備就緒後的樣子。


![image](assets/15.webp)


### 不要這麼快！！


很奇怪的是，BitBox02 告訴我們可以使用裝置了，但卻沒有允許我們寫下 seed 字元！我們唯一的備份是儲存在 microSD 卡上的檔案。這並不足夠。這些儲存裝置不會永遠存在（因為「位元腐蝕」）。我們需要紙張備份，以及保存在保險箱中的複本 (如一般如何使用硬體-錢包指南中所說明)


若要取得我們的 seed 詞組並將其寫下來，請移至左側的 「管理裝置」 標籤，然後按一下 「顯示恢復字詞」。


![image](assets/16.webp)


然後您就可以經過確認，裝置就會呈現這些字。將它們工整地寫下來，而且絕對不要讓任何人看到這些字。


![image](assets/17.webp)


之後，您可以按一下左邊的 Bitcoin 標籤，取得您的收件地址。


![image](assets/18.webp)


它一次顯示一個，但至少可以讓您從前 20 個中選擇使用哪一個 Address：


![image](assets/19.webp)


按一下藍色按鈕將顯示完整的 Address，並會提示您檢查 Address 是否與螢幕上的顯示相符。這是很好的做法，可確認電腦上沒有惡意軟體騙您傳送 Bitcoin 到攻擊者的 Address。


![image](assets/20.webp)


要發送 Bitcoin 到這個 Wallet，您可以複製 Address，然後貼到您的硬幣所在的 Exchange 的提款頁面。我建議您先發送一小筆測試金額，然後練習將其花費回 Exchange 或 Wallet 中的第二個 Address。


如果數量較多，我建議您建立一個 passphrase（見下圖）。原始的 Wallet（沒有 passphrase）可以作為您的誘餌 Wallet（裡面需要有合理的數量，才能成為可信的誘餌）。


### 連接至節點


BitBox02 會自動連線到一個節點。讓我們看看它連接到哪裡。按一下左邊的設定索引標籤，然後按一下「連結您自己的 Full node」。


![image](assets/21.webp)


這裡我們可以看到它連接到 shiftcrypto 的節點。不太好。我們已經將我們所有的 Bitcoin 位址背叛給他們，還有我們的 IP Address（當然不是 seed；他們可以看到我們的位址/餘額，但不能花掉）。我們可以在這個頁面輸入我們自己的節點詳細資料（超出了本特定指南的範圍），或者我們可以使用更好的軟體，如 Sparrow Bitcoin Wallet、Electrum Desktop Wallet 或 Specter Desktop。我稍後會在指南中示範 Sparrow Bitcoin Wallet。


![image](assets/22.webp)


新增 passphrase


現在我們已經用 BitBox02 App 設定了裝置 (並且揭露了我們的位址，這對於這個特殊的 Hardware Wallet 是無法避免的)，我們可以在我們的 seed 詞組中加入 passphrase。這將允許我們使用相同的 seed 建立新的 Wallet，而 ShiftCrypto 永遠不會看到我們的新地址。我們只會將這個 Wallet 連接到我們自己的軟體。


### 啟用 passphrase


現在繼續「啟用」passphrase 功能（但我們還沒有設定 passphrase）。進入「管理裝置」標籤，然後按一下「啟用 passphrase」（下圖紅圈）。


![image](assets/23.webp)


閱讀步驟...


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


現在中斷裝置連接，並關閉 BitBox02 App


Parman 的 bitbox02 部分結束。


您的 divice 現在可以在任何桌面解決方案上完全運作，例如 specter、sparrow 和使用 bitbox Interface。