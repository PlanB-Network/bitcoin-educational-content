---
name: Ntopng
description: 使用 ntopng 監控您的網路
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian Duchemin 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



**無論是檢查網路流動性、清楚瞭解使用情況或進行效能統計，網路流量監控都是企業網路**的重要部分。它有助於預測基礎結構的變更，並有助於確保使用者的使用品質 (也稱為 QoE，與 QoS 不同，QoE 是指 * 體驗品質*)。



要做到這一點，有許多技術和軟體/協定可用。例如，由 Cisco 開發的 Netflow 可用於從 Interface 擷取 IP 流量統計資料，但其使用僅限於相容的設備。



這就是為什麼我要在本教程中介紹 **Ntop**，並教您如何在基礎架構中使用它來監控網路使用情況。



Ntop 是開放原始碼軟體，可安裝在任何 Linux 機器上。它是免費的，可以收集下列資料：





- 頻寬使用率
- 主要客戶
- 主要目的地
- 使用的通訊協定
- 使用的應用程式
- 使用的連接埠
- 等等。



現在更名為 **Ntopng（新世代）**，免費提供許多基本功能。此外，還提供商業版本，可將設定的警報匯出至 SIEM 類型的軟體，或使用探針直接定義的規則過濾流量。



## II.先決條件



Ntop 探針的安裝依設備和環境而有所不同。因此，我不會在此給您一步一步的指導，但會概述各種可能性。



### A.板載模式



如果您在生產中有 pfSense、OPNSense 或 Endian 防火牆，甚至是有 NFTables 的 Linux 工作站，好消息來了！您可以直接安裝 Ntopng 並開始監控您的介面。



此技術的優點是不需要額外的硬體。另一方面，它會增加資源使用率，因此請確定您有足夠的硬體或足夠大小的虛擬機器 (至少 2 核心和 2BG RAM)。



### B.TAP / SPAN 模式



** 分路器是 ** 複製通過它的流量並傳送至另一個裝置的網路裝置。** 此裝置的優點在於不需要對現有基礎架構進行任何修改，可以放置在任何地方以監控特定網路區段，或放置在核心交換器與邊緣路由器之間以分析往返網際網路的流量。



這類設備的最大缺點是成本。在現今的 Gigabit 網路中，被動式分路器無法正確擷取網路流量，因此您需要成本約 200 歐元（最低）的主動式設備。



**SPAN**模式，也稱為**連接埠鏡像**，是交換器用來將流量從一個連接埠轉送到另一個連接埠。到目前為止，這是我的首選方法，因為它設定簡單，而且就像 tap 一樣，可以讓您隨意監控部分網路或整個網路。但有兩個缺點：交換器必須整合此功能，而且使用此功能會增加交換器的處理器負載。



### C.路由器模式



在 Linux 下掛載路由器並安裝 ntopng 是完全可能的。這個方法唯一的缺點是它會修改您的網路，無論是它的內部位址，或是您的 「真正」 路由器與您新增的路由器之間的位址。



注意：對於文章 [Create a Wifi router with Raspberry Pi and RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) 的讀者來說，完全可以在您的 Rpi 上安裝 ntopng 來獲得準確的統計資料！



### D.橋接模式



一個有趣的替代方法是使用**橋接模式的 Linux 機器。**放置在兩台設備之間，可以擷取所有流量，而無需介入基礎架構或其設備的組態。由於一台舊機器即可完成這項工作，因此此方法的成本也相當吸引。請注意，為了達到最佳效果，裝置應該有三張網卡，兩張用於橋接模式，一張用於存取 Interface 和 SSH。也可以只使用兩張網卡，但這樣裝置管理流量也會被擷取...



因此，我將使用**後一種模式。基於實際理由，我將使用虛擬機器來進行示範，但在實體機器上使用的方法仍然相同。



## III.使用 Interface 電橋準備探針



針對探針，我選擇了一台**Debian 11** 的機器進行最小化安裝。



第一步，總是一樣，更新 .NET Framework：



```
apt-get update && apt-get upgrade
```



接著安裝 **bridge-utils** 套件，這樣我們就可以建立我們的橋接器：



```
apt-get install bridge-utils
```



安裝完成後，第一件要注意的事就是網卡的目前名稱。在 Debian 下，這個名稱可以有多種形式，我們需要它來進行設定。



簡單的 **ip add** 指令就會輸出這些資訊：



![Image](assets/fr/016.webp)



在這裡，我看到 3 個介面：





- Lo**：這是迴路 Interface；它是在設備上「迴路」的虛擬 Interface。基本上，這個 Interface 的 Address 是 127.0.0.1 (不過 127.0.0.0/8 內的任何 Address 都可以，因為這個範圍是預留給這個用途的)，用來與設備本身連線。如果您在工作站上安裝了網站 (例如使用 WAMPP)，您可能曾經使用 "*localhost*"Address 來顯示您自己電腦上的網站。此主機名稱與 Address 127.0.0.1 相關聯，因此也與 Interface 環回相關聯。
- ens33**: 這是我的第一台 Interface，它從我的 DHCP 收到一台 Address。
- ens36**: 我的第二台 Interface



現在我有了所有的資訊，我可以修改 */etc/network/interfaces* 檔案來建立我的網橋。以下是目前的樣子 (可能會有所不同)：



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



第一部分是關於我的環回 Interface，我不會碰它，接下來是 Interface ens33。修改包括新增第二台 Interface (ens36) 並使用這兩個介面設定橋接器：



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



以下是對這些第一批變更的一些說明：





- auto *Interface***：會在系統啟動時自動「啟動」Interface
- iface *Interface* inet manual** : 使用 Interface 而不使用任何 IP Address。像關鍵字 "static「 定義靜態 IP Address 或 」dhcp" 使用動態位址



修改仍在繼續：



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



在此再次說明幾點：





- iface br0 inet static**: 在這裡，我將 Interface 橋接 (*br0*) 定義為靜態 Address。
- Address、網路遮罩、閘道**：板卡位址資訊
- bridge_ports**：橋接器中要包含的介面
- bridge_stp**：在交換器互連時，會使用生成樹通訊協定來偵測冗餘連結並避免迴路。由於網橋可以插入兩個網路路徑之間，因此它可能是迴路的來源，因此有可能啟用此通訊協定。我這裡不需要它，所以要停用它。



儲存變更並重新啟動網路：



```
systemctl restart networking
```



若要檢查變更，請再次顯示 **ip** add 指令的結果：



![Image](assets/fr/021.webp)


您可以清楚看到 ** 我的新 Interface "*br0*「 與我指派給它的 IP Address。** 順便一提，您也可以看到我的兩個實體介面確實是 」UP"，但沒有 IP Address。



## IV.安裝 NtopNG



現在我們的探測器已經可以嗅探我的網路和路由器之間的流量，剩下要做的就是安裝 ntopng。要做到這一點，首先修改 */etc/apt/sources.list* 檔案，並在以 **deb** 或 **deb-src** 開頭的每一行的末尾加入 **contrib**。



預設情況下，套件來源只包含符合 DFSG (*Debian Free Sotftware Guidelines*) 的套件，並以 **main** 關鍵字識別。您也可以新增這些套件來源：





- contrib**：包含符合 DFSG 的軟體，但使用不屬於 **main** 分支的相依性的套件
- non-free**: 包含不符合 DFSG 的套件



/etc/apt/sources.list 中的行示例 ：



```
deb http://deb.debian.org/debian/ bullseye main
```



因此，我只會在像這樣的行文中加上 **contrib** 一詞。



其餘步驟列於 [NtopNG] 網站 (https://packages.ntop.org/apt/)，對於 Debian 11，您需要新增 Ntop 原始碼以便日後安裝。這個新增動作是透過使用 .NET Framework 來自動完成的：



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



接下來就是實際安裝階段：



```
apt-get clean all
apt-get update
apt-get install ntopng
```



第一個指令會刪除 apt 套件管理員的快取。第二個會更新套件清單，第三個會安裝 NtopNG。



安裝之後，**NtopNG 軟體可以直接在 Debian 機器的 3000 連接埠**。所以對我來說是 `http://192.168.1.23:3000` 。



![Image](assets/fr/022.webp)



NtopNG 首頁



預設的登入名稱和密碼已顯示，您只需輸入即可！



## V.使用 NtopNG



當您第一次登入時，首先會要求您變更預設的管理密碼和語言。不幸的是，法文並不是其中之一。



接著您就會到達儀表板：



![Image](assets/fr/023.webp)



NtopNG 面板



不要習慣這個如果您注意到螢幕上方的黃色方框，您會看到這句話："*Licence expires in 04:57*"。預設情況下，安裝會啟動 NtopNG 完整版的試用版，但時間（非常）有限。一旦達到這個「倒數」，*社群*版本就會啟動，儀表板也會改變：



![Image](assets/fr/024.webp)



新的 NtopNG 社群儀表板



要做的第一件事是 ** 檢查是否有正確的 Interface 正在監聽**。在左上角，可用介面的下拉清單會讓您選擇我們感興趣的 Interface：BR0



![Image](assets/fr/025.webp)



Interface 選擇



新視窗會顯示「Top Flaw Talkers」，也就是通訊最頻繁的裝置。在這裡我只有兩個電台出現：



![Image](assets/fr/026.webp)



**來源主機顯示在左側，目的地顯示在右側 ** 這可讓您直觀看到每台主機使用的總頻寬，並獲得網路流量的整體檢視。還不賴，但我們可以更進一步...



舉例來說，如果我按一下「*主機*」，就會出現一個圖表，顯示我網路上每台主機的傳送和接收耗電量。以這裡為例，我可以看到僅 192.168.1.37 就佔了我 80% 的流量：



![Image](assets/fr/027.webp)



如果我按一下問題主機的 IP Address，就會轉到摘要頁面：



![Image](assets/fr/028.webp)



例如，我可以看到它是一台 VMWare 機器 (透過辨識我的 MAC Address 的 YES)，它的名稱是 DESKTOP-GHEBGV1 (所以肯定是一台 Windows 主機)，而且我有接收和傳送封包的**統計，以及資料量**。



您也會注意到本摘要頂端的新功能表。我建議您點選「**應用程式**」，看看是什麼在帶動這麼多的流量：



![Image](assets/fr/017.webp)


哈，看來我們找到答案了！在左側的圖表中，**我們看到 76.6% 的流量來自...Windows Update**，所以這台主機正在下載更新！



NtopNG 採用一種稱為 DPI 的技術 (*Deep Packet Inspection*)，可將每個網路流量分類，並定義其背後的應用程式 (或應用程式系列)。



為了示範，我在主機上啟動 YouTube 視訊：



![Image](assets/fr/018.webp)



**流量立即被識別和分類！



請注意：由於顯而易見的原因，此類軟體可能會引起隱私問題，因此請小心在適當的條件下使用。還要注意的是，可以**匿名化結果**，選項可在**設定 > 偏好設定 > 其他**中找到，名為「**遮罩主機 IP Address**」。



## VI.偵測與警示



NtopNG 也能針對某些饋送發出安全警示。這些警示可在左側橫幅上的 **Alerts** 功能表中找到。舉例來說，我這裡共有 2851 個警示，分為不同的嚴重程度：通知、警告和錯誤。



![Image](assets/fr/019.webp)



讓我們來看看高危急性警報，我有 17 個！



按一下此圖會出現警示的詳細資訊。這裡沒有什麼值得警惕的地方，這是一個假陽性，更新的下載被歸類為 HTTP 串流中的二進位檔案傳輸，這確實可能意味著一次攻擊。



![Image](assets/fr/020.webp)



然而，由於我使用的是免費版本，我無法排除作為警報來源的網域或主機，因此您必須留意它們，以免錯過更令人擔憂的事情。NtopNG 會在發生 .NET 和 .NET 的情況下發出 generate 警報：





- 透過 HTTP 下載二進位檔案
- 可疑的 DNS 流量
- 使用非標準連接埠
- SQL 注入偵測
- 跨站指令碼 (XSS)
- 等等。



## VII.結論



在本教程中，我們將介紹**如何使用 NtopNG 設定探測器**，使我們能夠**分析網路流量**，以直觀瞭解協定使用情況和每台主機的佔用率，同時還能偵測可疑流量。



不幸的是，我無法在這篇文章中涵蓋所有的功能和可能性，但請隨意探索！



此解決方案可在企業基礎架構中長期實施。NtopNG 也可以將結果匯出至 InfluxDB 資料庫，讓您可以使用 Graphana 等第三方工具建立自己的儀表板。