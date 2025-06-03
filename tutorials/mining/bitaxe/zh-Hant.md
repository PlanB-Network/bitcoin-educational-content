---
name: 設定 BitAxe
description: 如何設定 BitAxe？

---

### 簡介


BitAxe 是由 Skot 創建的開放原始碼專案，[可在 GitHub 上取得](https://github.com/skot/bitaxe)，可進行符合成本效益的 Mining 試驗。


它逆向工程了 ASIC 市場領導者 Bitmain 著名的 Antminer S19 的工作原理，也就是 Bitcoin Mining 的專用機器。現在，可以在新的開源專案中使用這些強大的晶片。與 Nerdminer 不同的是，BitAxe 有足夠的運算能力，連接 Mining pool，可以定期賺取一些 Satoshis。另一方面，Nerdminer 只能連接到所謂的 solopool，其功能就像彩票一樣：您贏得完整 Block reward 的機會微乎其微。


BitAxe 有多個版本，晶片和效能各不相同：


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

在本教程中，我們將使用配備 BM1366 晶片的 BitAxe Ultra 204，用於 Antminer S19XP。這顆晶片已經由零售商組裝好並開機。


### [零售商清單可在本頁取得](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


一般而言，電源 Supply 會隨附出售。如果沒有，您需要購買配備 5V 插孔電纜和至少 4A 的電源 Supply。


![signup](assets/1.webp)


### 組態

當您第一次插入 BitAxe 時，預設它會嘗試連線至 Wi-Fi 網路。嘗試五次之後，它會顯示自己的 Wi-Fi 網路名稱，以便您連線並進行設定。

要做到這一點，您可以使用任何電腦或智慧型手機。進入 Wi-Fi 設定，搜尋新網路，您會看到一個名為 Bitaxe_XXXX 的 Wi-Fi。這裡是 `Bitaxe_A859`。連接到此 Wi-Fi 網路，就會自動開啟一個視窗。


![signup](assets/3.webp)


在此視窗中，按一下左上方的三個小橫條，然後按一下「設定」。


![signup](assets/4.webp)


您需要手動輸入 Wi-Fi 網路資訊，因為沒有自動搜尋系統。


![signup](assets/5.webp)


因此，請指出 Wi-Fi 的 SSID，也就是您的網路名稱、密碼，以及您選擇的 Mining pool 資訊。請注意，此處的匯集 URL 並非以相同的方式呈現。例如，對於 Braiins，所提供的池 URL 為：`stratum+tcp://eu.stratum.braiins.com:3333`。


![signup](assets/6.webp)


正如您在螢幕上看到的，您需要移除 `stratum+tcp://` 和 `:3333` 部分，只留下 `eu.stratum.braiins.com`。然後，在 `Port` 欄位中輸入池所給的 URL 結尾的 4 位數字，但去掉 `:`。因此，這裡是 `3333`。


在本教程中，我們使用的是 Braiins Mining pool，但您也可以自由選擇其他產品。您可以在 [PlanB Network 網站上](https://planb.network/en/tutorials/mining) 找到我們有關 Mining 水池的教學。


接下來，在`使用者`中輸入您的識別碼，然後輸入`密碼`，通常是`"x「`或`」Anything123"`。


核心電壓」設定應保留預設值「1200」，「頻率」也應保留初始預設值。稍後可以調整此設定，以獲得更強的運算能力。但必須確保晶片溫度不超過 65-70°C，因為 BitAxe 並沒有在過熱時降低效能的系統。如果溫度過度超過 65°C，可能會損壞您的 BitAxe。


![signup](assets/7.webp)


正確輸入所有設定後，按一下底部的「儲存」按鈕，然後拔下 BitAxe 的電源插頭並插上即可重新啟動 BitAxe。

如果您輸入的資訊正確，裝置應該會很快連接到您的 Wi-Fi，然後連接到 Mining pool，並開始在其小螢幕上顯示一些資訊。可能需要幾分鐘的時間才能顯示在 Mining pool 的儀表板上。

### 儀表板和螢幕


三個不同的顯示頁面會捲動顯示。在第三頁，您會看到 `IP` 資訊，也就是允許您連線到儀表板的 IP Address。這裡，Address 是 `192.168.1.19`。


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


若要存取儀表板，只需在您的網際網路瀏覽器中輸入此 Address。


在儀表板上，您會發現所有資訊都顯示在小螢幕上，現在我們就來詳細瞭解一下。


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

您可以隨時變更 Wi-Fi 或 pool 設定，不會有任何問題。

根據您房間的通風和溫度，您可能需要提高或降低性能，使溫度不超過 65°C。如果您提高性能，您將賺取更多的 Satoshis，但您的 BitAxe 也會消耗更多的電力！
