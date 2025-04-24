---
name: 翡翠

description: 如何設定您的 JADE 裝置
---

![image](assets/cover.webp)


## 教學影片


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - Mobile Bitcoin Hardware Wallet FULL TUTORIAL by BTCsession


## 完整的寫作指南


![image](assets/cover2.webp)


### 先決條件


1.下載最新版本的 Blockstream Green。


2.安裝此驅動程式，以確保 Jade 能被電腦識別。


### 桌面設定


![full guide](https://youtu.be/0fPVzsyL360)


開啟 Blockstream Green，然後按一下「裝置」下的 Blockstream 標誌。


![image](assets/1.webp)


使用隨附的 USB 連接線，將 Jade 插入桌上型電腦。


**注意：** 如果電腦無法識別 Jade，請確認已安裝必要的驅動程式，並檢查是否可能是 USB 權限問題所致。


一旦您的 Jade 出現在 Green 中，請按一下檢查更新來更新 Jade，並選擇最新的韌體版本。使用 Jade 上的滾輪或切換鍵確認並繼續更新。請確定您的 Jade 仍顯示「Initialize」（初始化）按鈕，否則您必須等到設定完 Jade 後才能進行升級。如有必要，請使用「返回」按鈕回到此畫面。


![image](assets/2.webp)


更新 Jade 的韌體之後，在您想要使用的網路和安全政策上選擇 Setup Jade。


**Tip:** 安全政策列在下圖登入畫面的類型之下。如果您不確定是選擇 Singlesig 還是 Multisig Shield，請查看我們的指南 [這裡](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


接下來，選擇建立新的 Wallet，然後選擇 12 個字來 generate 您的復原短語。按一下 Advanced（進階），您就可以選擇 12 個字和 24 個字的復原短語。


![image](assets/4.webp)


在離線狀態下，將復原語句記錄在紙上（或使用專用的復原語句備份裝置，以提高安全性）。然後，使用 Jade 頂端的滾輪或切換鍵來驗證您的復原短語。這一步驟可確保您正確記下。


![image](assets/5.webp)


設定並確認您的六位數 PIN 碼。每次您登入 Wallet 時，都會使用此密碼來解鎖 Blockstream Jade。


![image](assets/6.webp)


現在，只要在 Green 桌面應用程式上選擇前往 Wallet，您就會看到您的 Wallet 在 Blockstream Green 上開啟。Blockstream Jade 也會顯示已就緒！現在您可以使用 Jade 來發送和接收 Bitcoin 交易。


![image](assets/7.webp)


使用完Wallet後，請中斷Blockstream Jade與裝置的連接。下次您要在 Blockstream Jade 上使用 Wallet，只需重新連接您的裝置並根據提示操作即可。


來源：https://help.blockstream.com/hc/en-us/articles/17478506300825


### 附錄 A - 驗證 Green Wallet 下載檔案


驗證下載是指檢查您所下載的檔案自開發者釋出後是否有被修改。


我們透過檢查簽章 (由開發者的私密金鑰所產生)、下載的檔案和開發者的公開金鑰在通過 gpg -verify 函數時是否回傳 TRUE 結果來達成這個目的。接下來我會告訴你怎麼做。


首先，我們取得簽署金鑰：


對於 Linux，請開啟終端機，並執行此指令 (您應該直接複製並貼上文字，並加上引號)：


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


對於 Mac，除了需要先下載並安裝 GPG Suite 外，您也可以執行相同的動作。


對於 Windows，除了需要先下載並安裝 GPG4Win 之外，您也要做同樣的事情。


您會收到一個輸出，說明公開金鑰已經匯入。


![image](assets/9.webp)


此影像的 alt 屬性為空；其檔案名稱為 image-3-1024x162.webp


接下來，我們需要取得包含軟體 Hash 的檔案。它儲存在 Blockstream 的 GitHub 頁面上。首先前往他們的資訊頁面，點選「桌面」的連結。它會帶您到 GitHub 上的最新發佈頁面，在那裡您會看到一個指向 SHA256SUMS.asc 檔案的連結，那是一個包含 Blockstream 發佈的 Hash 的文字檔。


![image](assets/10.webp)


GitHub：


![image](assets/11.webp)


這並非必要，但在儲存到磁碟後，我將「SHA256SUMS.asc」重新命名為「SHA256.txt」，以便更容易在 Mac 上使用文字編輯器開啟檔案。這是檔案的內容：


![image](assets/12.webp)


我們要找的文字在最上方。根據我們下載的檔案，有相對應的 Hash 輸出，我們稍後將與之比較。


文件的底部包含在上面的訊息上所做的簽名 - 這是一個二合一的檔案。


順序並不重要，但在檢查 Hash 之前，我們要先檢查 Hash 訊息是否真實（即未被竄改）。


開啟終端機。您需要進入下載 SHA256SUMS.asc 檔案的正確目錄。假設您下載到 "Downloads "目錄，對於 Linux 和 Mac，請變更到像這樣的目錄（區分大小寫）：


```bash
cd Downloads
```


當然，您必須在這些指令後按 <enter>。對於 Windows，請開啟 CMD（命令提示符），然後輸入相同的內容（雖然不分大小寫）。


對於 Windows 和 Mac，您需要按照之前的指示分別下載 GPG4Win 和 GPG Suite。對於 Linux，作業系統自帶 gpg。從終端機 (或 Windows 的 CMD)，輸入此指令：


```bash
gpg --verify SHA256SUMS.asc
```


檔案名稱 (紅色) 的確切拼法在您取得檔案當天可能會有所不同，因此請確定指令與下載的檔案名稱相符。您應該會得到此輸出，請忽略關於信任簽章的警告 - 這只表示您還沒有手動告訴電腦您信任我們之前匯入的公開金鑰。


![image](assets/13.webp)


此影像的 alt 屬性為空；其檔案名稱為 image-4-1024x165.webp


此結果證實簽章是好的，而且我們相信「info@greenaddress.it」的私鑰簽署了資料（Hash 報告）。


現在我們應該 Hash 下載的 zip 檔案，並比較已發佈的輸出。請注意，在 SHA256SUMS.asc 檔案中，有一段文字寫著「Hash：SHA512" 這讓我感到困惑，因為檔案中顯然有 SHA256 輸出，所以我打算忽略這一點。


對於 Mac 和 Linux，打開終端機，導航到下載 zip 檔案的位置（可能您需要再次輸入「cd Downloads」，除非您之後一直沒有關閉終端機）。順便說一下，您可以隨時輸入 PWD (「列印工作目錄」) 來檢查您所在的目錄，如果這些都是陌生的，那麼搜尋「如何瀏覽 Linux/Mac/Windows 檔案系統」來觀看 YouTube 視訊是很有用的。


若要儲存檔案，請輸入以下字元：


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


您應該檢查您的檔案名稱，必要時修改上面藍色的文字。


您會得到這樣的輸出 (如果檔案與我的不同，您的輸出也會不同)：


![image](assets/14.webp)


接下來，目視比較 Hash 輸出與 SHA256SUMS.asc 檔案中的內容。如果相符，則 -> 成功！恭喜您。


來源：https://armantheparman.com/jade/


### 在 Sparrow 上使用


如果您已經知道如何使用 SParrow，那就跟以往一樣：


**註：** 以 Specter 為例，過程相同


使用這裡提供的連結下載 Sparrow。


![image](assets/14.5.webp)


按一下下一步，依照設定指南了解不同的連線選項。


![image](assets/15.webp)


選擇您所需的伺服器，然後選擇「建立新 Wallet」。


![image](assets/16.webp)


輸入 Wallet 的名稱，然後按一下建立 Wallet。


![image](assets/17.webp)


選擇所需的政策和指令碼類型，然後選擇「連線的 Hardware Wallet」。


**註：** 如果您之前使用 Blockstream Jade 作為 Singlesig Wallet 與 Blockstream Green，並希望在 Sparrow 中檢視您的交易，請確定腳本類型與 Green 中包含您資金的帳戶類型相符。您也需要派生路徑相匹配。


![image](assets/18.webp)


插入您的 Blockstream Jade，然後按一下掃描。接著會提示您在 Jade 上輸入 PIN。


**祕訣：** 在連接您的 Jade 之前，請確定 Blockstream Green 應用程式並未開啟。如果 Green 開啟，可能會導致 Sparrow 無法偵測到您的 Jade。


![image](assets/19.webp)


選擇 Import Keystore 匯入預設帳戶的公開金鑰，或選擇箭頭手動選擇您要使用的衍生路徑。


![image](assets/20.webp)


匯入所需的金鑰後，按一下套用。


![image](assets/21.webp)


現在您已成功設定您的 Wallet，您可以開始使用 Sparrow 和 Blockstream Jade 接收、儲存和消費您的 Bitcoin。


**註：** 如果您之前使用 Jade 與 Blockstream Green 作為 Multisig Shield Wallet，您不應期望您的新麻雀 Wallet 會顯示相同的餘額 - 這些是不同的錢包。若要再次存取您的 Multisig Shield Wallet，只需將您的 Jade 連回 Blockstream Green。


![image](assets/22.webp)


來源：https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green 應用程式


如果您比較喜歡行動導覽，可以搭配 Blockstream Green 使用



- 如何使用 Green 設定 Blockstream Jade | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- 如何將 Bitcoin 接收至 Jade Wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA