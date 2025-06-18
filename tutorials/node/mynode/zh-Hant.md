---
name: 我的節點
description: 設定您的 Bitcoin MyNode
---

![image](assets/0.webp)


[My Node](https://mynodebtc.com/) 是運行 Bitcoin 和 Lightning 節點的最簡單、最強大的方式！我們結合最好的開放原始碼軟體與我們的 Interface、管理和支援，讓您可以輕鬆、私密且安全地使用 Bitcoin 和 Lightning。


## 節點設定類型


有多種 Node 設定。MyNode 非常出色。有許多隨附的應用程式，如果您付費購買高級版本，應用程式會更多。否則自己下載所有這些應用程式是非常乏味的。MyNode 讓這一切變得相當簡單，您將會看到。


另一個類似選擇是 RaspiBlitz。它的 GUI 沒那麼漂亮，應用程式也與 MyNode 隨附的應用程式有許多重疊，但 Raspiblitz 是免費的開放原始碼軟體 (FOSS)，而 MyNode 則不太一樣。另一個差異是 MyNode 是在 Docker 容器中執行。我覺得 Docker 讓人望而生畏，而且 Hard 也很難排除故障。這只有在遇到錯誤或 bug 時才會有問題。開發人員為高級使用者提供協助，而且還有 Telegram 聊天群組。


RaspiBlitz 只是在 Linux 上安裝多個程式，不需要 Docker。外接式 Hard 硬碟機可輕鬆連接至另一台配備 Bitcoin Core 的 Linux 機器，如有需要，即可使用。


另一個選擇是直接在作業系統上安裝 Bitcoin Core 和 Electrum 伺服器種類（有好幾種）。我有 Linux（Raspberry Pi）、Mac 和 Windows 的指南。


## 購物清單



- Raspberry Pi 4，4Gb 記憶體或 8Gb（4Gb 已經足夠）。
- 官方 Raspberry Pi 電源 (非常重要！不要買到一般的，說真的)
- Pi 的外殼。FLIRC 機殼太棒了。整個機殼都是散熱器，您不需要風扇，因為風扇會很吵。
- 16 Gb microSD 卡（您需要一張，但多備幾張也很方便）
- 記憶卡讀卡器 (大多數電腦都沒有 microSD 卡插槽)。
- 外接式 SSD 1Tb Hard 硬碟機。

注意：固態硬碟是關鍵。不要使用可攜式外接 Hard 硬碟機，即使它比較便宜。


- 乙太網路線（連接到您的家用路由器）
- 您不需要顯示器


## 下載 MyNode Image


導覽到 MyNode 網站 連結


![image](assets/1.webp)


按一下 `立即下載


下載 Raspberry Pi 4 版本：


![image](assets/2.webp)


這是一個很大的檔案：


![image](assets/3.webp)


下載 SHA 256 雜湊值


![image](assets/4.webp)


開啟 Mac 或 Linux 的終端機，或 Windows 的 Command Prompt。輸入


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


電腦思考 20 秒左右。然後檢查輸出的雜湊檔是否與上一步從網站上下載的相符。如果完全相同，就可以繼續。

閃存 SD 卡


## 下載並安裝 Balena Etcher。連結


我無法找到相關的數位簽章。如果您知道方法，請告訴我，我會更新這篇文章。


Etcher 的使用方法不言自明。插入 micro SD 卡，然後將 Raspberry Pi 軟體 (.img檔案) 快閃到 SD 卡上。


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


一旦完成，磁碟機將不再可讀。您可能會收到作業系統的錯誤訊息，硬碟機應該會從桌面消失。拔出記憶卡。


## 設定 Pi 並插入 SD 卡


零件（未顯示外殼）：


![image](assets/12.webp)

![image](assets/13.webp)


連接乙太網路線和 Hard 磁碟機 USB 接頭 (尚未連接電源)。避免連接中央藍色的 USB 連接埠。MyNode 建議您使用 USB 2 連接埠，即使硬碟機可能具備 USB 3 功能。


![image](assets/14.webp)


micro SD 卡放在這裡：


![image](assets/15.webp)


最後，連接電源：


![image](assets/16.webp)


## 找出 Pi 的 IP Address


使用 MyNode 絕不需要顯示器。不過，您需要在家庭網路中再安裝一台電腦。如果您的 Pi 並未透過乙太網路連線，而您想使用 WiFi，那麼尋找 IP 需要高階電腦技能。幫不上忙，抱歉。您需要乙太網路連線。(問題來自需要存取顯示器和作業系統，才能連接到 WiFi 並輸入密碼）。


檢查您的路由器，查看所有連接裝置的 IP 清單。


我在瀏覽器中輸入 192.168.0.1 (路由器隨附的說明)，登入後就可以看到 IP 位址為 192.168.0.18 的裝置「MyNode」。請注意，這些 IP 位址不會公開顯示於網際網路 (它們會先經過路由器)，它們只是家庭網路中裝置的識別碼。


找到 IP 是至關重要的。


**註：** 您可以使用 Mac 或 Linux 機器上的終端機，使用「arp -a」指令找出家庭網路中所有乙太網路連線裝置的 IP Address。雖然輸出結果不如路由器所顯示的那麼漂亮，但您需要的所有資訊都在這裡。如果不清楚哪個是 Pi，請進行試誤。


## SSH 登入 Pi


您可以選擇使用 SSH 指令遠端登入裝置，但這並非必要的 (RaspiBlitz Node 才需要)。無論如何，我會教您怎麼做，因為這非常方便。


開啟 Mac 或 Linux 電腦 (Windows 請下載 putty，一種 SSH 工具)，然後輸入：


```bash
ssh admin@192.168.0.18
```


使用您自己的 IP Address。MyNode 裝置的使用者名稱預設為 "admin"。密碼預設為 "Bolt"。


如果您之前使用過 Pi，並將 micro SD 卡調換了位置，就會出現此錯誤：


![image](assets/17.webp)


您需要做的是導航到 "known_hosts" 檔案所在的位置並刪除它。這樣做是安全的。錯誤訊息會顯示路徑。對我來說是 /Users/MyUserName/.ssh/


別忘了 ssh 前的 "."，這表示這是隱藏目錄。


然後再試一次 ssh 指令。


這次您會看到這個輸出：


![image](assets/18.webp)


您刪除的檔案已經刪除，您要新增一個新的指紋。輸入 yes，然後按 <enter>。


您會被要求輸入密碼。密碼是 "Bolt"


現在您可以在沒有螢幕的情況下，透過終端存取 MyNode Pi，並確認它已順利載入。


![image](assets/19.webp)


## 透過 Web 瀏覽器存取


開啟瀏覽器。必須是家庭網路中的電腦，不能從外面進行。有一個方法，但它是 Hard。我還沒有測試過。


在瀏覽器 Address 視窗中輸入 IP Address。這將會發生


![image](assets/20.webp)


輸入密碼 "Bolt" - 稍後再變更。


然後就會發生這樣的事情：


![image](assets/21.webp)


選擇格式化磁碟機


![image](assets/22.webp)


現在我們等待。


在某個時候，您會被問到是否要輸入產品金鑰，或是使用免費的「社群版」 - 我要展示的是高級版。如果您負擔得起，我建議您付費購買高級版，這是非常值得的。


![image](assets/23.webp)


然後您就會看到區塊下載的進度。這需要好幾天的時間：


![image](assets/24.webp)


如果需要，在下載過程中關閉機器是安全的。進入設定，找到關機按鈕。不要直接拉扯電線，您可能會損壞安裝或 Hard 磁碟機。


請務必在一開始就進入「設定」並停用快速同步。它會從頭開始下載初始區塊。


![image](assets/25.webp)


我想要繼續建立指南，所以這裡是我之前準備的另一個 MyNode。這是 Blockchain 已經同步，且幾個「應用程式」已經啟用並同步後的頁面：


![image](assets/26.webp)


請注意，Electrum 伺服器也需要同步，所以一旦 Bitcoin Blockchain 同步後，請點選按鈕啟動該程序 - 需要一兩天的時間。一旦您選擇啟用，其他一切都會在幾分鐘內啟用。您可以按一下東西並進行探索。您不會弄壞任何東西。如果有東西壞了 (這種情況發生在我身上，但我想是因為我用的是便宜的零件)，你必須重新刷機，然後再開始下載。我使用 MyNode 時遇到的問題是，如果您需要「重新刷新」，您最後需要從頭再開始 Blockchain 同步。有一些技術方法可以解決這個問題，但並不容易。


如果您也想嘗試另一個節點，例如 RaspiBlitz，您需要額外的 SSD 外接式 Hard 硬碟機，以及另一張 micro SD 卡來閃存。否則，這是相同的設備，只是您顯然無法同時執行 MyNode 和 RaspiBlitz。如果您想這麼做，是時候選購另一台 Raspberry Pi 了。


既然您有一個正在運行的節點，那就使用它吧，不要讓它就這麼放著什麼都不做。按照我的文章（和視頻）如何將您的 Electrum Desktop Wallet 連接到 Electrum Server 和 Bitcoin Core 這裡。