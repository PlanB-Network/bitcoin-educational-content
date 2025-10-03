---
name: Canaan Avalon Nano 3S
description: 設定您的 ASIC Avalon 用於獨採或 Miner 匯集
---

![cover](assets/cover.webp)



在本教學中，我們將介紹如何設定 Canaan Avalon Nano 3S，讓您輕鬆在家使用 Miner。



直到目前為止，專門為執行特定任務而設計的 ASIC（*特定應用整合電路*）機器 - 在這種情況下，Bitcoin 的 Miner 的 Hash 計算（SHA-256） - 特別不適合家庭使用。噪音的滋擾、產生的熱量，以及需要調整您的電力裝置以支援這些裝置的巨大能量，都讓我們大多數人無法參與其中。



如今，ASIC 機器的領導製造商之一 Canaan 已決定針對想要在家中使用 Miner 的個人市場，提供一系列相對安靜且非常容易安裝 (隨插即用) 的產品。



這些裝置在市場上的銷售方式有兩種，一種是**Avalon Nano 3S (140W)** 的輔助加熱器，另一種是**Avalon Mini 3** 的迷你散熱器，輸出功率為 **800W**。



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

請注意，在絕大多數情況下，與同等功率的傳統加熱器之間的價格差異不會讓您獲得財務利潤。除非您能獲得免費（剩餘）或非常便宜的電力，否則 Mining 的活動所產生的 Satoshis 絕對無法彌補這種價格差異。



在我看來，這些裝置應該更多地被視為一種簡單的方式，讓那些基於個人原因而希望在家中進行 Miner 的人可以這樣做： *獲得非 KYC Satss / 通過 Solominating 玩「彩票」 / 參與 Hashrate 分散化等等...*.，同時從所產生的熱量中受益**作為獎勵**，以便在冬天為自己的房間供暖。但至少在大多數情況下（西方國家），這並不是一種省錢的方式。



## 開箱與功能



首先，讓我們看看 Avalon Nano 3S 盒子裡有什麼。



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



打開包裝盒後，您會發現一個紙套，裡面有一個 WIFI 接收器，稍後我們會看到，您需要將該接收器插入裝置的 USB 連接埠，使其能與您的本機網路連線。此外，還有說明書和一個金屬針，必要時可以將裝置重設為出廠設定。



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



當一切都從盒子裡拿出來之後，以下是手邊的東西：當然是機器本身、使用者手冊、WIFI 接收器、前述的金屬尖端，以及裝置的電源 Supply。附贈的信用卡在我們看來不值一提。



![image](assets/fr/05.webp)



以下表格總結了 Nano 3S 的一般技術規格：



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## 開啟電源並連線至本機網路



拆開包裝後，盡可能將 Avalon Nano 3 S 放在相對開放的地方，讓熱能流通。然後如下圖所示，開始插入小型 WIFI 接收器模組：



![image](assets/fr/06.webp)


然後將電源 Supply 的 USB-C 插頭插入裝置的 USB-C 連接埠，即可為裝置供電。



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



裝置開機後，螢幕上會出現 Avalon Nano 標誌，接著會出現一個「手機」標誌，上面寫著「請使用 Avalon Family App 設定網路」。



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



若要執行此操作，請前往您的行動應用程式商店，搜尋並下載 **Avalon Family** 應用程式。



![image](assets/fr/11.webp)


安裝完成後，按一下右上角的「略過」，然後按一下「新增」按鈕，最後按一下「搜尋」，即可開啟。請確定您的智慧型手機已啟用藍牙功能，以便順利偵測裝置。



![image](assets/fr/12.webp)


應用程式偵測到裝置後，按一下裝置並選擇「連線」。接著您會進入輸入 WIFI 連線詳細資訊的畫面。


![image](assets/fr/13.webp)


裝置連線至您的區域網路後，螢幕現在會變成這樣：



![image](assets/fr/14.webp)



它會顯示「虛構」的 Hashrate，因為還沒有設定任何池，以及裝置的時間、日期、電源和 IP Address - 如果您要透過 PC 和瀏覽器存取裝置的 Interface，這將會非常有用（稍後會詳細說明）。



![image](assets/fr/15.webp)




## 連接至 Mining pool



** 這部分是 Nano 3s 和 Mini 3 的共通點，因為製程完全相同**。



無論我們想要「獨佔」或 Miner 「匯集」，都必須連線到 Mining pool。事實上，我們的裝置只是一個 Hash 製造器，對 Bitcoin 網路毫無感覺。將它連線到一個池讓它可以存取 Bitcoin 網路，並允許它接收區塊範本來工作。



### 使用應用程式連線至 Mining pool



在 Avalon Family 應用程式上，選擇裝置，如下圖所示。接著會自動要求您變更機器的管理員密碼。如果您想這麼做，請點選「OK」；如果想保留預設存取密碼「admin」，請點選「cancel」。


![image](assets/fr/16.webp)


然後選擇「設定」，再選擇「池配置」，並輸入 3 個要求的池的參數。


池 #2 和 #3 將作為其中一個失敗時的備份，這樣您的 Miner 就不會白白工作。預設情況下，Hashrate 會指向 1 號池



在我們的案例中，我們選擇




- 1 - 公共游泳池、
- 2 - CkPool、
- 3 - 海洋。



![image](assets/fr/17.webp)



有關如何連接 Mining pool 的詳細資訊，請參閱這些教學：



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

總括而言，我們需要





- 池 Address，通常是 **stratum+tcp://xxxxxxxx:port**。





- 由 *your Bitcoin Address* 和您為裝置選擇的 *pseudo* 組成的 "worker" 名稱，兩者以 *dot* 分隔，例如：**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- 密碼，通常總是 "**x**"



輸入水池資訊後，按一下「儲存」。



![image](assets/fr/18.webp)


按照指示重新啟動裝置，並等待幾分鐘，直到 Hashrate 指向您的首選池 (#1)。



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



在 Avalon 系列應用程式中，按一下 Avalon Nano 3S 對應的圖示。


接下來會出現 3 個功能表：「工作模式」、「燈光控制 」和 「設定」。首先，按一下「工作模式」。接下來會提供您 3 種電源模式。



**Low**: 以 70 瓦的耗電量為您帶來約 3 Th/s 的 Hashrate


**中**：100 瓦的耗電量可為您帶來約 4.5 Th/s 的 Hashrate。


**高**：在 140 瓦的最大消耗量下，可提供約 6 Th/s 的 Hashrate。



![image](assets/fr/31.webp)


讓我們退一步探索「光線控制」功能表。這純粹是裝飾性的。有一大堆選項可以改變顏色、強度、熱度、在夜間關閉裝置的 LED 等等...很容易就能自己發現。



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



最後，我們可以使用的最後一個功能表是「設定」功能表，我們已經見過連接 Mining 池的功能表。在這裡您可以管理您的池，變更裝置的管理員密碼，並觀察各種指標，例如保固到期日、濾網清潔度，或發生故障時如何聯絡支援人員。



![image](assets/fr/35.webp)


為了維護和盡可能保持濾網清潔，我們建議使用吸塵器，並定期吸淨進氣口和出氣口，以防止堵塞。



本教學已接近尾聲，我們已學會如何將 Avalon Nano 3 S 連接到本機網路、如何將 Hashrate 指向 Mining 池，以及如何使用 Avalon Family 應用程式瀏覽選項與設定。



若要瞭解更多資訊，請參閱我們關於 Avalon 高階版本：Mini 3 的教學。



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7