---
name: Canaan Avalon Mini 3
description: 設定您的 ASIC Avalon 用於獨採或 Miner 匯集
---

![cover](assets/cover.webp)



在本教學中，我們將介紹如何設定 Canaan Avalon Mini 3，讓您輕鬆在家使用 Miner。



直到目前為止，專門為執行特定任務而設計的 ASIC（*特定應用整合電路*）機器 - 在這種情況下，Bitcoin 的 Miner 的 Hash 計算（SHA-256） - 特別不適合家庭使用。噪音的滋擾、產生的熱量，以及需要調整您的電力裝置以支援這些裝置的巨大能量，都讓我們大多數人無法參與其中。



如今，ASIC 機器的領導製造商之一 Canaan 已決定針對想要在家中使用 Miner 的個人市場，提供一系列相對安靜且非常容易安裝 (隨插即用) 的產品。



這些裝置在市場上的銷售方式有兩種，一種是**Avalon Nano 3S (140W)** 的輔助加熱器，另一種是**Avalon Mini 3** 的迷你散熱器，輸出功率為 **800W**。



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

請注意，在絕大多數情況下，與同等功率的傳統加熱器之間的價格差異不會讓您獲得財務利潤。除非您能獲得免費（剩餘）或非常便宜的電力，否則 Mining 的活動所產生的 Satoshis 絕對無法彌補這種價格差異。



在我看來，這些裝置應該更多地被視為一種簡單的方式，讓那些基於個人原因而希望在家中進行 Miner 的人可以這樣做： *獲得非 KYC Satss / 通過 Solominating 玩「彩票」 / 參與 Hashrate 分散化等等...*.，同時從所產生的熱量中受益**作為獎勵**，以便在冬天為自己的房間供暖。但至少在大多數情況下（西方國家），這並不是一種省錢的方式。



## 開箱與功能



### Avalon Nano 3S



首先，讓我們看看 Avalon Mini 3 包裝盒內有什麼。



![image](assets/fr/24.webp)



打開盒子後，操作說明書就在眼前，但更重要的是，WIFI 接收器模組就隱藏在操作說明書左側的圓形白色貼紙下方。您稍後就會用到它。



![image](assets/fr/25.webp)



泡沫塊下方是裝置，從盒子中取出後就是電源 Supply 裝置。



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## 開啟電源並連線至本機網路



拆開包裝後，如果可能的話，請將 Avalon Mini 3 放置在相對開放的地方，讓熱能正常循環。然後，先將小型 WIFI 接收器模組插入裝置底部的 USB 連接埠，插入電源 Supply，並確保電源按鈕在 "1 "的位置。



![image](assets/fr/28.webp)



完成這些步驟後，裝置的 LED 顯示器會亮起並顯示「Bluetooth」符號，表示已準備好透過 Avalon Family 應用程式與您的區域網路連線。



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



若要執行此操作，請前往您的行動應用程式商店，搜尋並下載 **Avalon Family** 應用程式。



![image](assets/fr/11.webp)


安裝完成後，按一下右上角的「略過」，然後按一下「新增」按鈕，最後按一下「搜尋」，即可開啟。請確定您的智慧型手機已啟用藍牙功能，以便順利偵測裝置。



![image](assets/fr/12.webp)


應用程式偵測到裝置後，按一下裝置並選擇「連線」。接著您會進入輸入 WIFI 連線詳細資訊的畫面。


![image](assets/fr/13.webp)


一旦連接到您的區域網路，您的 Mini 3 將會顯示 IP Address、時間、Hashrate 和電力等資訊。



以下是 Mini 3 的一般技術規格摘要表：



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## 連接至 Mining pool



**此部分與 Nano 3s 和 Mini 3 裝置共通，因為製程完全相同 **



無論我們想要「solominate」或 Miner 「pool」，都需要連接到 Mining pool。事實上，我們的裝置只是一個 Hash 製造器，對 Bitcoin 網路毫無感覺。將它連線到一個池，就可以存取 Bitcoin 網路，並允許它接收區塊範本來進行工作。



### 使用應用程式連線至 Mining pool



在 Avalon Family 應用程式上，選擇裝置，如下圖所示。接著會自動要求您變更機器的管理員密碼。如果您想這麼做，請點選「OK」；如果想保留預設存取密碼「admin」，請點選「cancel」。


![image](assets/fr/16.webp)


然後選擇「設定」，再選擇「池配置」，並輸入 3 個要求的池的參數。


池 #2 和 #3 將作為其中一個失敗時的備份，這樣您的 Miner 就不會白費。預設情況下，Hashrate 會指向 1 號池



在我們的案例中，我們選擇




- 1 - 公共游泳池、
- 2 - CkPool、
- 3 - 海洋。



![image](assets/fr/17.webp)



有關如何連接 Mining pool 的詳細資訊，請參閱這些教學：



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

總括而言，我們需要





- 池 Address，通常是 **stratum+tcp://xxxxxxxx:port**。





- 由 *your Bitcoin Address* 和您為裝置選擇的 *pseudo* 組成的 "worker" 名稱，兩者以 *dot* 分隔，例如：**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- 密碼，通常總是 "**x**"



輸入水池資訊後，按一下「儲存」。



![image](assets/fr/18.webp)


按照指示重新啟動裝置，並等待幾分鐘，直到您的 Hashrate 指向您偏好的水池 (#1)。



### 使用瀏覽器連線至 Mining pool



您也可以連接至 Mining pool，更廣泛而言，您可以透過喜愛的瀏覽器存取裝置的 Interface 管理系統。



若要執行此操作，請在瀏覽器的搜尋列中輸入以下畫面所示裝置的 IP Address，在我們的範例中為**192.168.144.6**。



![image](assets/fr/15.webp)



將會出現以下頁面，要求您開啟 Avalon Family 應用程式，並掃描隨應用程式顯示的 QR 代碼。



![image](assets/fr/20.webp)



開啟應用程式，然後按一下右上方的 3 個破折號，再按一下掃描。掃描瀏覽器的 QR 碼，然後輸入應用程式的管理員密碼，然後按一下確定。



![image](assets/fr/21.webp)



這裡是讓您與 Avalon 互動的網頁。與其說是設定，不如說是顯示機器指標的儀表板。



但池設定仍可透過這種方式存取，只要按一下右下角的 **「Pool Config」** 即可。



![image](assets/fr/22.webp)



與手機應用程式相同，您可以在此輸入水池參數。



![image](assets/fr/23.webp)



## 透過 Avalon Family 應用程式控制裝置



我們現在已將家用 Miner 連接到本機網路，並將 Hashrate 指向 Minings 池。現在讓我們透過 Avalon Family 應用程式來發現我們機器的基本功能。



在 Avalon 系列應用程式的主功能表中，按一下與 Avalon Mini 3 相對應的圖示。您將直接進入管理操作模式的功能表。



提供 3 個選項：「加熱 」模式、"Mining 「模式或 」夜間 "模式。





- 在「加熱」模式下，您有 2 個功率等級「Eco」或「Super」。


環保」等級相當於加熱功率為 500 瓦，Hashrate 約為 25 Th/s，聲級為 40 dB。


超級 "等級相對應於約 30Th/s 和 45 dB 時 650 W 的輸出功率。此模式允許您設定最高環境溫度，超過此溫度時，裝置將停止工作。



![image](assets/fr/36.webp)




- 在 "Mining "模式下，機器以最大速度運轉，無需設定目標溫度（當然，除了內建的過熱限制外）。其目的是充分利用 Miner 的性能。在此模式下，輸出功率接近 800 W，速度約為 37.5 Th/s，噪音等級為 50-55 dB。



![image](assets/fr/37.webp)


最後，在「夜間」模式下，您的 Mini 3 會以最低的速度運作，並將噪音降至最低。400 W、20 Th/s 和約 33 dB。



您也可以在此設定一個目標溫度，當溫度超過此溫度時，機組會進入非作用模式並停止 Miner。如果溫度下降，機組將重新啟動，恢復加熱和 Miner。在此模式下，顯示 LED 預設為關閉，但您可以選擇在需要時開啟，以便在黑暗中照亮房間，就像夜燈一樣（見下圖）。



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



最後，您可以透過「顯示」功能表來操控 Avalon 的 LED。您可以選擇捲動相關的操作資訊、選擇顯示時間，甚至是自訂 (像素化) 圖像。



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



與 Avalon Nano 3S 一樣，「設定」功能表可讓您變更管理員密碼、水池設定、檢查濾網障礙（位於裝置底部）、聯絡支援或檢視裝置記錄。



![image](assets/fr/42.webp)



同樣地，裝置底部的過濾器可用吸塵器清潔，越經常清潔越好。



本教學到此為止，我們已學會如何將 Avalon Mini 3 連接到本機網路、如何將 Hashrate 指向 Mining 池，以及如何使用 Avalon Family 應用程式瀏覽選項和設定。



若要瞭解更多資訊，請參閱我們關於 Avalon 較小版本：Nano 3S 的教學。



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6