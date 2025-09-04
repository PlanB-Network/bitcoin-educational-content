---
name: Pi-Hole
description: 適用於整個網路的廣告封鎖程式
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian Duchemin 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



只要一開啟我們最愛的瀏覽器，我們都會這麼做：安裝***adblocker**（廣告封鎖程式）。然而，當使用電視瀏覽器或 Android 裝置等...要找到有效的東西就比較麻煩了。而且，如果家中有超過一台裝置，那麼您必須針對每個瀏覽器重複操作！



在本教程中，我們將解決一個簡單的問題**：為網路上的所有機器提供廣告封鎖程式，並集中管理。



為此，我們將使用專為此目的開發的工具： **Pi-Hole**



Pi-Hole 是 DNS sinkhole。它會使用您的裝置提出的 DNS 請求來驗證或拒絕流量，從而保護您免受已知會散佈廣告、惡意軟體等的位址和網域的影響。



DNS 是 Domain Name System（網域名稱系統）的縮寫。那麼什麼是網域名稱？it-connect.fr」只是其中一個例子。域名是一個或多個資源的唯一識別碼，通常由單一實體管理。



機器名稱加上網域名稱為 FQDN，即 *Fully Qualified Domain Name*。它允許您通過 「呼叫 」特定的機器。例如，當您鍵入「www.trucmachin.com」時，您實際上是在呼叫屬於網域名稱「trucmachin.com」的機器「www」。



只是我們的電腦不懂人類的語言，他們只懂二進位，所以他們需要一個 IP Address，相當於電話號碼，才能到達網站。



因此，每次您在瀏覽器中輸入網站名稱或點擊連結時，您的電腦會先向 DNS 伺服器查詢與該名稱相對應的 IP Address。



**Pi-Hole 會檢查這些要求（每天都有數百個要求！），並自動封鎖那些已知會寄存廣告甚至惡意檔案的要求。



## II.安裝 Pi-Hole



有了像 Pi-Hole 這樣的名稱，您可能會正確地假設您需要一個 Raspberry-Pi...。但事實並非如此。 **Pi-Hole 可以安裝在任何 Linux 電腦上（Debian、Fedora、Rocky、Ubuntu 等）。



另一方面，您需要記住，**這個裝置必須每天 24 小時運行，原因很簡單：沒有 DNS，就沒有網際網路！**因此，Raspberry 是個好主意，因為它幾乎不消耗能源。



若要安裝，只需透過 SSH 連線至您的 Linux 機器，並以「*root*」的身份輸入下列指令：



```
curl -sSL https://install.pi-hole.net | bash
```



> **註**：在正常情況下，在未瞭解腳本的作用之前，不建議「入侵」該腳本。如果您不確定，請使用瀏覽器進入頁面，或將內容下載為檔案。
>


> **注意：在 Debian 11 的最小版本上，Curl 並未安裝，因此您需要在輸入上述指令之前，使用 **apt-get install curl** 指令手動安裝。

腳本執行後，會執行一系列測試，而安裝本身會自行處理：



![Image](assets/fr/019.webp)



安裝 Pi-Hole



安裝完成後，您會看到此畫面：



![Image](assets/fr/020.webp)



Pi-Hole 啟動螢幕



> **註**：如果您的機器使用 DHCP，您會收到相關的警告訊息。當然，為了正確使用，我們強烈建議您為您的機器指定一個固定 IP。

在此畫面之後，您會收到一些資訊訊息，接著就會進入設定精靈，首先會問您 Pi-Hole 要將請求轉寄到哪個 DNS 伺服器。就我而言，我選擇了有使用者隱私權約章的 Quad9。



![Image](assets/fr/021.webp)



DNS 選擇 - Pi-Hole



> **注意：如果您在公司裡，您目前的 DNS 伺服器很可能是 Active Directory 網域控制器。不過不用擔心，您稍後可以指定一個條件重定向器，用於您所選擇的網域。通常，您可以將任何有關您本機網域名稱的請求重定向到您的 DNS 伺服器。

您會發現有些選擇包含 DNSSEC 選項。基本上，DNS 通訊協定並不安全（當時設計時並沒有考慮到這一點）。DNSSEC 透過對交換進行加密和簽章來增加 Layer 的安全性，從而解決了這個問題：[DNS 安全性](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



任何廣告封鎖程式都依賴一個或多個清單來執行其工作。Pi-Hole 標準配備單一清單，因此請選擇此清單，稍後再新增更多清單。



![Image](assets/fr/022.webp)



關於 Interface web 的問題，它的安裝是可選的，因為該工具有自己的命令列來進行管理和可視化。但這個 Interface 相當令人愉悅，而且做得很好，所以我建議您同時安裝：



![Image](assets/fr/023.webp)



如果您要在已經有 Web 伺服器的機器上安裝 Pi-Hole，您可以對下面的問題回答「否」。但請注意，這需要 PHP 和幾個模組才能運作。否則，**lighttpd 將安裝所有必要的模組**。



![Image](assets/fr/024.webp)



接著會詢問您是否要記錄 DNS 請求。 **如果您想保留歷史記錄，請將此選項設定為「是」；否則，請將此選項設定為「否」，但您將會失去部分功能** (請參閱下一螢幕)。



![Image](assets/fr/025.webp)



對於其 Interface 網路，Pi-Hole 使用自己的一個稱為 FTLDNS 的函式，提供 API 並從 DNS 請求產生統計資料。此功能可包含「隱私」模式，可隱藏請求的網域名稱、請求背後的客戶或兩者。如果您想在不侵犯他人隱私的情況下進行監控，或者只是想在公共網路使用的情況下遵守相關法規，這就非常方便了。



![Image](assets/fr/026.webp)



選擇私人生活方式



一旦回答了最後一個問題，腳本就會執行它應該執行的工作：下載 GitHub 套件庫並設定 Pi-Hole。安裝結束時，會顯示一個摘要畫面，其中包含重要資訊：



![Image](assets/fr/027.webp)



安裝摘要畫面



記下 Interface 的網頁密碼和網路資訊。現在是時候在我們目前的位置設定 DHCP 服務了。



## III.DHCP 設定



為了運作，Pi-Hole 需要「解析」客戶端提出的 DNS 請求，因此客戶端必須知道要將請求傳送給它。有幾種方法可以做到這一點：





- 修改 DHCP 伺服器中的 DNS 設定 (例如您的 Box)
- 停用此伺服器，並使用 Pi-Hole 提供的伺服器
- 手動修改每個裝置以使用 Pi-Hole 作為 DNS



我個人選擇第一個解決方案。您所在的地方**可能已經有 DHCP 伺服器 (通常是您的機箱)。所以不必麻煩。



由於有許多可能性，介於不同運營商的 box（我不知道所有的運營商）和那些有自己路由器的運營商，我不打算提供這些修改的截圖。無論如何，您需要進入 DHCP 設定，修改「DNS」參數，加入您 Pi-Hole 的 IP Address。



完成此步驟後，如果有任何裝置之前已開啟，它們會保留舊設定，因此您需要重新啟動組態請求。



在 Windows 工作站上，使用命令提示符 ：



```
ipconfig /renew
```



在 Linux 工作站上 ：



```
dhclient
```



對於所有其他裝置，必須關閉後再開啟。



所以他們應該取得正確的參數，來進行檢查：



```
ipconfig /all
```



在 DNS 欄位中，您應該輸入 Pi-Hole 的 Address，我的情況是 192.168.1.42：



![Image](assets/fr/029.webp)



## IV.使用 Interface 網路 Pi-Hole



為了方便管理，**Pi-Hole** 使用精心設計的 Interface 網頁 Interface。使用方便且容易上手，可讓您 ：





- 即時檢視要求數量、封鎖的要求等。
- 管理白名單和黑名單
- 新增靜態項目、別名等。
- 新增清單
- 以及許多其他功能！



就我而言，我要新增一個封鎖清單。如上所述，與 Soft 同時安裝的只有一個清單。廣告網站的清單有很多，但最好至少選擇一個專門針對您所居住國家的清單。最著名的清單之一是 **EasyList**，其中一個是專門針對法國的：[EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



若要新增，請先連線至 Interface 管理員： **http://<ip_du_PiHole>/admin**



管理員密碼已經生成（請參閱安裝結束時的螢幕截圖），因此您只需輸入該密碼即可訪問 Interface ：



![Image](assets/fr/030.webp)



Interface 來自 Pi-Hole



舉例來說，我們可以看到有兩個客戶連線到 Pi-Hole，它已經處理了 442 個請求，其中有 8 個請求被封鎖。這些圖表可以成為很好的資訊來源，尤其是在專業的情況下。



若要新增我們的名單，請前往「**群組管理**」和「**名單**」功能表：



![Image](assets/fr/031.webp)



我們可以看到我們的第一個清單 "**StevenBlack**「，要加入我們的清單，複製我上面給您的連結，並將其插入欄位 」**Address**"，對於描述，我選擇放入清單的名稱：



![Image](assets/fr/032.webp)



在 Pi-Hole 中加入清單



剩下的就是點選「**新增**」來新增它。要啟動它，我們需要執行一個額外的步驟，「警告」Pi-Hole 接管此清單。要做到這一點：





- 使用內建的指令列
- 無論是 Interface 網路



我個人選擇了第二個，因為如果您仔細看過，執行更新的 PHP script 的連結直接在我們所在的頁面上 (「線上」字樣)。所以您只要點選它，就會進入一個只有一個選項的頁面：



![Image](assets/fr/033.webp)



完成後，頁面會顯示腳本的結果，表示清單已被考慮在內（當然，除非顯示錯誤訊息）。



正如本教學一開始所說，Pi-Hole 也可讓您**封鎖已知會散佈惡意軟體的網域。為了強化這項功能，我建議您也加入 Abuse.ch 發佈的定期更新網域清單**，這將大幅強化您的網路安全，請參考 [this Address](https://urlhaus.abuse.ch/downloads/hostfile/)。



當然，您可以新增任何您認為相關的清單，或透過黑名單功能表手動管理您的黑名單。



## V.Pi-Hole 測試



現在一切就緒，您要做的就是測試解決方案，以確保它能正常運作。



例如，我會嘗試連接到網域 *http://admin.gentbcn.org/*，這個網域在 Abuse.ch 清單上，因為已知它會寄存惡意軟體：



![Image](assets/fr/034.webp)



很明顯，我在某處被封鎖了。為了確定是 Pi-Hole 做的手腳，我們可以檢查 Interface 網頁「Query Log」中的查詢記錄，看看是否是來自清單項目的封鎖：



![Image](assets/fr/035.webp)



## VI.總結



在本教程中，我們向您介紹了如何設定 DNS 伺服器，它不僅可以消除大部分廣告，讓您舒適地瀏覽網頁，還可以透過封鎖網路釣魚和惡意軟體散佈的網域，增加***的 Layer 安全性。



如果安裝在 Raspberry-Pi 上，全部免費且經濟實惠 (就耗電量而言)。