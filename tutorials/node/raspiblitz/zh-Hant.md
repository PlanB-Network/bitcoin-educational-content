---
name: RaspiBlitz
description: 設定 RaspiBlitz 的指南
---

![image](assets/0.webp)


RaspiBlitz 是一個可自己動手完成的 Lightning 節點 (LND 和/或 Core Lightning)，可與 Bitcoin-Fullnode 一起在 RaspberryPi (1TB SSD) 上執行，並配備漂亮的顯示器，方便設定與監控。


RaspiBlitz 的主要目標是學習如何在家裡分散運行自己的節點 - 因為：不是您的節點，不是您的規則。成為 Lightning Network 生態系統的一份子，探索並發展這個不斷成長的生態系統。您可以將 Lightning Network 作為工作坊的一部分，或是週末自己的專案。


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - 如何運行閃電和 Bitcoin Full node by BTC session


# Parman's Raspiblitz 設定指南


Raspiblitz是一個優秀的系統，用於運行比特幣節點和相關應用。我向大多數用戶推薦它和MyNode節點（理想情況下應有兩個節點以實現冗餘）。一個主要優勢是Raspiblitz節點是「Free Open Source Software」，而MyNode或Umbrel則不是。[為什麼這很重要？Vlad Costa 解釋。](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) 你還可以通過WiFi連接而不是以太網運行Raspiblitz – 這裡有一個[補充指南](https://armantheparman.com/headless-wifi/)供參考。（我還沒有找到在MyNode上實現這一點的方法）。


您可以購買附有迷你螢幕的現成節點，也可以自己製作（您不需要螢幕）。


[GitHub頁面上的指南](https://github.com/rootzoll/raspiblitz)非常出色，但對於具有中等經驗的用戶來說可能過於詳細。我的說明將更簡潔，希望更容易遵循。


基本上，該過程與使用Raspberry Pi 4設置[MyNode節點](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/)的過程非常相似。Raspiblitz指南建議您購買顯示器，但實際上您並不需要，而且我也不會建議這樣做。您甚至不需要額外的鍵盤或滑鼠。只需通過同一家庭網路上的電腦訪問設備的終端選單，並在終端中使用ssh指令即可。這在Linux/Mac（簡單）上可行，而在Windows上則稍微困難一些。


## 步驟 1：購買設備。


您需要與執行 MyNode 節點完全相同的設備。您可以試試其中一種，唯一的差別在於 micro SD 卡上的資料。



- Raspberry Pi 4，4Gb 記憶體或 8Gb（4Gb 已經足夠）。
- 官方 Raspberry Pi 電源 (非常重要！不要買到一般的，說真的)
- Pi 的外殼。(FLIRC 機殼非常棒。整個機殼都是散熱器，您不需要風扇，因為風扇會很吵)
- 32 Gb microSD 卡 (您需要一張，但幾張也很方便。)
- 記憶卡讀卡器 (大多數電腦都沒有 microSD 卡插槽)。
- 外接式 SSD 1Tb Hard 硬碟機。
- 乙太網路線（連接到您的家用路由器）。


您不需要顯示器（或鍵盤或滑鼠）


注意：這是錯誤的 Hard 硬碟機：這是可攜式外接 Hard 硬碟機。這不是 SSD。SSD 是關鍵。這就是它便宜的原因 (價格以澳幣計算)


![image](assets/1.webp)


這種類型才是正確的選擇：


![image](assets/2.webp)


這會更快，但不必要地昂貴：


![image](assets/3.webp)


## 步驟 2：下載 Raspiblitz Image


導航到 [Raspiblitz GitHub 網站](https://github.com/rootzoll/raspiblitz)，然後找到「download image」連結：


![image](assets/4.webp)


下載的檔案的 sha-256 雜湊值在網站上提供。它會隨著每次更新而改變。如果你不明白這是什麼，你應該明白，所以我寫了一份[你可以在這裡閱讀的指南。](https://armantheparman.com/gpg/)


![image](assets/5.webp)


## 步驟 3：驗證影像


在繼續之前，如果您不熟悉命令列上的檔案系統，很容易學會，而且您應該學會。


這是一個[對 Linux 有用的影片，但也適用於 Mac](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK)。


對於 Windows，這裡有一個[簡單的教學](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s)。


_更新：pgp/gpg 驗證現已可用。您需要 Openoms 的公鑰。[在這裡](http://parman.org/downloadable/openoms.txt)（連結可能需要隱身模式才能運作 – http，而非 https）_
Mac/Linux


等待檔案下載完成 (重要！)，然後開啟終端機，導覽到下載檔案的位置，並輸入以下指令：

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


其中 `xxxxxxxxxxxxxx` 是您剛下載的檔案名稱。如果您不在該檔案所在的目錄中，則必須輸入完整路徑。


電腦思考 20 秒左右。檢查輸出的雜湊檔是否與上一步從網站上下載的相符。如果完全相同，就可以繼續。

視窗


開啟命令提示符並導航至下載檔案的位置，然後輸入此命令：


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


其中 `xxxxxxxxxxxxxx` 是您剛下載的檔案名稱。如果您不在該檔案所在的 Director 中，則必須輸入完整路徑。


電腦思考 20 秒左右。檢查輸出的雜湊檔是否與上一步從網站上下載的相符。如果完全相同，就可以繼續。


## 步驟 4：快閃記憶卡


您可以使用 Balena Etcher 來完成此操作。[在此下載](https://www.balena.io/etcher/)。


Etcher 的使用方法很簡單。插入您的 micro SD 卡，並將 Raspiblitz 軟體 (.img檔案) 更新至 SD 卡。


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


一旦完成，磁碟機將不再可讀。您可能會收到作業系統的錯誤訊息，而硬碟機應該會從桌面消失。拔出記憶卡。


## 步驟 5：設定 Pi 並插入 SD 卡


零件（未顯示外殼）：


![image](assets/10.webp)


![image](assets/11.webp)


連接乙太網路線和 Hard 磁碟機 USB 接頭 (尚未連接電源)。避免連接中央藍色的 USB 連接埠。使用 USB 2 連接埠，即使硬碟機可能具備 USB 3 功能（更可靠）。


![image](assets/12.webp)


micro SD 卡放在這裡：


![image](assets/13.webp)


最後，連接電源：


![image](assets/14.webp)


## 步驟 6：尋找 Pi 的 IP Address


使用 Raspiblitz 絕不需要顯示器。但是，您需要在家庭網絡上安裝另一台電腦。如果您的 Pi 沒有使用乙太網路，而您想使用 WiFi，那麼尋找 IP 需要一些電腦技能。幫不上忙，抱歉。您需要乙太網路連線。(問題來自需要存取顯示器和作業系統，才能連接 WiFi 並輸入密碼)。


檢查路由器，查看所有連接設備的 IP 清單。


我在瀏覽器中輸入 192.168.0.1 (路由器隨附的說明)，登入後就可以看到 IP 位址為 192.168.0.191 的裝置。請注意，這些 IP 位址不會公開顯示於網際網路 (它們會先經過路由器)，它們只是家庭網路中裝置的識別碼。


找到 IP 是至關重要的。


**註：** 您可以使用 Mac 或 Linux 機器上的終端機，使用「arp -a」指令找出家庭網路中所有乙太網路連線裝置的 IP Address。雖然輸出結果不如路由器所顯示的那麼漂亮，但您需要的所有資訊都在這裡。如果不清楚哪個是 Pi，請進行試誤。


## 步驟 7：SSH 登入 Pi


記得在開機前將 SD 卡放入 Pi。等待幾分鐘，然後在另一台 Linux/Mac 上開啟終端機。


對於 Mac/Linux，在終端機中輸入：


```bash
ssh admin@You_Pi's_IP_address
```


在 Windows 上，你需要安裝 [putty](http://putty.org/) 才能透過 ssh 連線至 Pi。輸入與上面相同的指令。


第一次這樣做，或每當您透過切換 SD 卡來變更 Pi 的作業系統時，您可能會或可能不會收到此錯誤...


![image](assets/15.webp)


修復它的方法是導航到 "known_hosts" 檔案所在的位置（它會在錯誤訊息中告訴您），然後刪除它。命令是 "rm known_hosts"


然後，重複 ssh 指令登入。這將會發生...


![image](assets/16.webp)


輸入 yes（完整字元）繼續。


如果成功，您會被要求輸入密碼。這不是您電腦的密碼，而是 raspiblitz 的密碼。一般的密碼是 "raspiblitz"，您稍後可以修改。終端機視窗會變成藍色，您會看到像舊式 DOS 選單一樣的選單選項。使用方向鍵或滑鼠導航。


![image](assets/17.webp)


按照提示，設定您的密碼，然後它會偵測到您的 Hard 磁碟機，並在需要時提供您格式化的選項。


接著會詢問您是否要從其他來源複製 Blockchain 資料，或是重新下載。複製是一個學習的過程，說明也相當不錯，好讓您隨時隨地....。


![image](assets/18.webp)


簡單但較慢的方法是從頭下載整個鏈...


![image](assets/19.webp)


許多文字會在終端螢幕上閃爍。您可能會誤以為這是 Blockchain 下載的過程，但對我來說，它看起來像是在產生通訊用的私人密碼匙。


接著會出現閃電選項。


![image](assets/20.webp)


製作一個新的密碼來鎖定您的照明 Wallet，然後建立一個新的 Wallet，並給您 24 個字來寫下...


![image](assets/21.webp)


請務必寫下並妥善保管。我聽說有個人因為不打算使用閃電而沒有這樣做，但是一年後他決定使用閃電，並且開啟了頻道。然後，他意識到他說的話沒有備份，而且我記得不可能再從裝置中提取出這些話，所以他不得不關閉所有通道，重新開始。他逃過一劫，但其他人可能就沒那麼幸運了。


接下來，終端機視窗會捲下幾分鐘的文字。然後...


![image](assets/22.webp)


您將會登出 ssh 會話。登入後，系統會要求您輸入密碼 C，以解鎖您的 Lightning Wallet。


現在我們等待。兩星期後見。您可以關閉終端機，它不會對 Pi 做任何事，只是一個通訊視窗。


![image](assets/23.webp)


如果因為任何原因，您想要在 Blockchain 完成下載之前關閉 Pi，只要您做得正確就沒問題。一旦您重新連線，Blockchain 會繼續下載之前的程式。


按 CTRL+c 退出藍螢幕。您將存取 Pi 的 Linux 終端。在此您可以輸入「menu」（功能表），載入以下畫面，從那裡您可以關閉 Pi 的電源。


![image](assets/24.webp)


導覽結束


從現在開始，您的 node si 已準備就緒。如果您仍需要導覽更多選項，請參閱 github 上的更多教學和指南 https://github.com/raspiblitz/raspiblitz#feature-documentation。