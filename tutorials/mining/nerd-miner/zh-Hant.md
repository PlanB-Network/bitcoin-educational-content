---
name: 書呆子
description: 開始 Mining Bitcoin，勝算接近 0
---

![cover](assets/cover.webp)

**設定您的 NerdMiner_v2**


在本教程中，我們將引導您完成設定 NerdMiner_v2 的必要步驟，NerdMiner_v2 是專用於 Bitcoin Mining 的硬體裝置 (ESP-32 S3)。

顯然，這種裝置的運算能力無法與業餘或專業礦工的 ASIC 相抗衡。不過，NerdMiner 是一個完美的教育工具，讓 Bitcoin Mining 變得具體。誰知道呢，如果運氣好的話，您也許會找到一個區塊以及隨之而來的獎勵。對於好奇的人，我們會在【獲勝機率的估算】(#estimation-de-la-probabilite-de-gain) 章節中看到。就耗電量而言，NerdMiner 的耗電量為 0.5W；相較之下，LED 燈的耗電量平均高出 20 倍。


在進行不同的步驟之前，讓我們先列出製作的必要設備：



- a [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- a [USB-C 電源 Supply](https://amzn.eu/d/gIOot90)
- 3D 機殼：如果您有 3D 印表機，您可以下載 [3D 檔案](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons)，否則您可以在 [Silexperience 線上商店](https://silexperience.company.site/NerdMiner_V2-p544379757) 購買。
- 安裝 Chrome 瀏覽器的個人電腦
- 網際網路連線
- a Bitcoin Address


您也可以從幾家經銷商購買預先組裝好的 NerdMiner 套件，例如：



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)


首先，我們會看到如何將軟體 flash 到 ESP-32 S3 上，然後我們會看到如何重新啟動 ESP-32 S3 以變更 wifi 網路。這些步驟適用於 Windows 使用者，如果您使用的是 Linux 作業系統，請執行 [初步步驟](#etapes-preliminaires-pour-utilisateurs-linux)，讓您的系統可以辨識 ESP-32 S3。


由於使用 webflasher，**安裝 NerdMiner_v2 軟體**的過程大大簡化。


## 步驟 1：準備 Webflasher


首先，您需要到 [線上 NM2 閃光燈](https://bitmaker-hub.github.io/diyflasher/)。


然後選擇與您的 ESP-32 相對應的韌體。大多數時候是預設的：T-Display S3。然後按一下「Flash」。


**Note⚠️ :** 您必須使用 Chrome 瀏覽器 - 因為它預設允許使用 flash 和存取 USB 連接埠。


![image](assets/webflasher.webp)


## 步驟 2：連接 ESP-32


啟動 webflasher 後，會開啟一個彈出視窗，顯示瀏覽器可辨識的不同 USB 連接埠。

接著您就可以連接 ESP-32，一個新的連接埠就會顯示出來 (在本例中，它是 ttyACM0 連接埠)。接下來您必須選取它，然後按一下「連接」。


![image](assets/flasher-port-serial.webp)


然後，軟體會在幾秒鐘內下載到您的 ESP32。


![image](assets/NM2-sucessfully-installed.webp)


## 步驟 3：NerdMiner 設定


您的 NerdMiner 設定將透過智慧型手機或電腦完成。

啟用 WiFi 並連線至本機 NerdMinerAP 網路。如果您使用智慧型手機，設定入口網站會自動開啟。否則，請在瀏覽器中輸入 Address 192.168.4.1。

然後選擇「設定 WiFi」。


現在您可以設定您的 NerdMiner。

首先，透過選擇您的網路名稱並輸入相關密碼，開始連線至您的 WiFi 網路。


然後您可以選擇想要參與的 Mining pool。事實上，在 Bitcoin Mining 行業中，匯集計算能力以增加在 Exchange 中找到區塊的機會，以按比例分享所提供的 Hashrate 獎勵是很常見的。

對於 NerdMiners，您可以選擇連接到其中一個池：


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

一旦您選擇了您的彩池，您需要輸入您的 Bitcoin Address 以在萬一 (例外) 發現區塊時獲得獎勵。


此外，請選擇您的時區，以便 NerdMiner 能正確顯示時間。

現在您可以按一下「儲存」。


![image](assets/wifi-configuration.webp)


恭喜您，現在您是 Bitcoin Mining 網路的一員！


## NerdMiner 作業


NerdMinerv2 軟體有 3 個不同的畫面，您可以按一下螢幕右邊的頂端按鈕進入：



- 主畫面可讓您存取 NerdMiner 的統計資料。
- 第二個畫面提供存取時間、您的 Hashrate、Bitcoin 的價格以及區塊高度。
- 第三個畫面提供存取全球 Bitcoin Mining 網路的統計資料。

![image](assets/NM2-screens.webp)


如果您想要重新啟動 NerdMiner，例如變更 WiFi 網路，您需要按下頂部按鈕 5 秒鐘。


按一次底部按鈕可關閉 NerdMiner。按兩下會旋轉螢幕方向。


### Linux 使用者的初步步驟


以下是 Chrome 在 Linux 上偵測序列埠的步驟。


1.識別相關連接埠：



- 將 ESP-32 連接到電腦。
- 開啟終端機。
- 輸入下列指令，列出所有連接埠：
  - `dmesg | grep tty`
  - 或 `ls /dev/tty*`
- 若要確定連接埠，您可以在沒有連接 ESP-32 的情況下重複命令，以排除法進行。


2.變更關聯埠的權限：



- 預設情況下，存取序列埠可能需要 root 權限，因此我們會將您的使用者加入 `dialout` 群組，使其可用。
  - `sudo usermod -a -G dialout YOUR_USERNAME`，將 `YOUR_USERNAME` 改為您的使用者名稱。
  - 然後登出，再以此使用者身分重新登入，或重新啟動系統，以確保群組變更生效。


現在您的 ESP-32 已經被系統辨識，您可以回到 [第一步](#etape-1-preparation-du-webflasher) 進行軟體安裝。


## 總結


就是這樣！您的 NerdMiner_v2 現在已經設定完成，可以開始使用了。


祝您 Mining 快樂，願運氣站在您這邊！


### 估算贏的概率


讓我們來估算一下贏得 Block reward 的概率。這個估算很粗略，只想獲得概率的數量級。

NerdMiner 可以連線到的 Pool 都只是「單獨 Mining pool」，也就是說，Pool 並不會將所有連線礦工的 Hashrate 相互化，而只是扮演一個協調者的角色。

現在假設我們的 NerdMiner 的 Hashrate 約為 45kH/s。


由於 Hashrate 的總速度約為 450 EH/秒 (或每秒 4.5 x 10^20 哈希值)，我們可以認為找到下一個區塊的機率是 1 億億分之一，這是非常非常非常不可能發生的事。因此，NerdMiner 除了可以當作教育工具和好奇心的對象之外，還可以當作 Bitcoin Mining 中的彩票，邊際電力成本僅為 0.5 W，雖然我們剛才已經看到中獎的機率低得令人髮指。然而，為何不挑戰一下您的運氣呢？


### 其他資訊


如果您想進一步閱讀相關內容，這裡有一些連結：



- [NerdMiner_v2 專案頁](http://github.com/BitMaker-hub/NerdMiner_v2)
- [NerdMiners完整文件](https://docs.bitwater.ch/nerd-Miner-v2/)