---
name: OPNsense
description: 如何安裝和設定 OPNsense 防火牆？
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



在本教程中，我們將介紹 OPNsense 開放原始碼防火牆。我們將探討其主要功能、先決條件，以及如何安裝這個以 FreeBSD 為基礎的解決方案。



在開始之前，您應該知道**OPNsense 和 pfSense 都是基於 FreeBSD 的開放原始碼防火牆**。我們可以說 pfSense 算是 OPNsense 的大哥大，因為後者是 2015 年創建的 Fork。最後，需要指出的是，自 2017 年起，**OPNsense 已改用 HardenedBSD 取代 FreeBSD**。HardenedBSD 是 FreeBSD 的增強版，具有進階的安全功能



OPNsense 以其更現代化的使用者 Interface 及更頻繁的更新頻率**而脫穎而出。事實上，OPNsense的更新時間表包括每年兩個主要版本，每兩週左右更新一次（導致次要版本）。如果我們看看這些解決方案的社群版本，與 pfSense 相較之下，這個後續行動是非常有趣的。



![Image](assets/fr/050.webp)



## II.OPNsense 功能



OPNsense 是一個設計用來當作防火牆和路由器的作業系統，雖然它的功能眾多，但可以透過安裝額外的套件來擴充。適合生產使用，主要用於網路安全和流量管理。



### A.主要特點



以下是 OPNsense 的一些主要功能：





- 防火牆與 NAT**：OPNsense 提供進階的狀態過濾防火牆功能，以及網路 Address 轉換 (NAT) 功能。





- DNS/DHCP**：OPNsense 可設定為管理網路上的 DNS 和 DHCP 服務。它可以當作 DHCP 伺服器，也可以當作本機網路上機器的 DNS 解析器。預設也整合了 Dnsmasq。





- VPN**：OPNsense 支援多種 VPN 通訊協定，包括 IPsec、OpenVPN 及 WireGuard，可為遠端存取行動工作站或網站互連提供安全連線。





- 網頁代理**：OPNsense 內含網路代理，可控制並過濾網際網路存取。它也可用於過濾內容和管理網路存取。





- 頻寬管理 (QoS)**：OPNsense 提供服務品質（QoS）管理功能，可為網路流量排定優先順序，並更好地管理網路頻寬。





- Captive portal**：此功能可讓您透過認證頁面（本機基地台、憑證等）管理使用者對網路的存取。這是公共 Wi-Fi 網路常部署的功能。





- IDS/IPS**：OPNsense 整合 Suricata 以提供入侵偵測與防禦 (IDS/IPS) 功能，保護網路免受攻擊。





- 高可用性（CARP）**：OPNsense 支援 CARP (*Common Address Redundancy Protocol*)，可在多個 OPNsense 防火牆之間提供高可用性，即使發生硬體故障，也能確保服務維持運作。





- 報告與監控**：OPNsense 提供即時報告與監控工具，藉由建立日誌來追蹤網路效能 (使用 NetFlow) 並偵測潛在問題。這包括圖形。Monit 工具已整合至 OPNsense，並可監控防火牆本身。



### B.額外套裝



這只是 OPNsense 所提供功能的概覽。此外，從 OPNsense 管理 Interface 存取的**套件目錄**，可讓您**豐富防火牆的附加功能**。這些功能包括 ACME 客戶端、Wazuh 代理、NTP Chrony 服務，以及作為反向代理的 Caddy。



![Image](assets/fr/051.webp)



## III.OPNsense 的先決條件



首先，您需要決定要將 OPNsense 安裝在何處。有幾種可能的解決方案，包括安裝在 .NET Framework 上：





- 作為虛擬機器的管理程序，不論是 Hyper-V、Proxmox、VMware ESXi 等。
- 作為*裸金屬*系統的機器。這可以是一台充當防火牆的迷你 PC。



您也可以透過我們的線上商店購買**一台 OPNsense 機架式裝置**。



您需要考慮執行 OPNsense 所需的硬體資源。這在 [本文件頁面](https://docs.opnsense.org/manual/hardware.html) 有詳細說明。



**生產所需的最低資源和建議資源：**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

最後，**您的資源需求首先取決於要管理的連線數量**，因此也取決於**您的頻寬需求**。此外，您需要**記住將會啟動和使用的服務**（代理伺服器、入侵偵測等...），因為這些服務可能會消耗 CPU 和/或 RAM。



您還需要 OPNsense 安裝 ISO 映像檔，您可以從 [官方網站](https://opnsense.org/download/) 下載。若要在虛擬機器上安裝，請選擇 "**dvd**"作為映像類型，以取得 ISO 映像（然後隨您的便......）。若要透過可開機 USB key 安裝，請選擇「**vga**」選項，以取得「**.img**」檔案。



![Image](assets/fr/048.webp)



您還需要一台電腦來進行 OPNsense 管理和測試。



## IV.目標配置



我們的目標是





- 建立內部虛擬網路 (192.168.10.0/24 - LAN)** ，可透過 OPNsense 防火牆存取網際網路。對於生產用途，這可以是您的本機網路、有線網路和/或 Wi-Fi。
- 啟動並設定 NAT**，讓內部虛擬網路中的虛擬機器可以存取網際網路
- 啟動並設定 OPNsense** 上的 DHCP 伺服器，以便將 IP 設定分發給未來連接至內部虛擬網路的機器
- 設定防火牆**，僅允許 HTTP (80) 和 HTTPS (443) 的 LAN 至 WAN 流量流出。
- 設定防火牆**，允許虛擬區域網路使用 OPNsense 作為 DNS 解析器 (53)。



如果您使用的是 Hyper-V 平台，這會給您以下的表示：



![Image](assets/fr/033.webp)



## V.安裝 OPNsense 防火牆



### A.準備可開機 USB 密鑰



第一步是準備安裝媒體： **附有 OPNsense 的可開機 USB 隨身碟**。如果您是在虛擬環境中工作，這當然是可選的，但在任何情況下，您都需要下載 OPNsense 安裝 ISO 映像檔。



下載之後，您會得到一個包含".img "**格式映像的存檔。您可以使用各種應用程式**建立可開機 USB 隨身碟**，其中包括**balenaEtcher**：使用超簡單。更重要的是，該應用程式會識別存檔中的映像，因此您無需事先解壓縮。





- [下載 balenaEtcher](https://etcher.balena.io/)



應用程式安裝完成後，選擇您的影像、USB 密鑰，然後按一下「Flash」！稍等片刻。



![Image](assets/fr/049.webp)



現在您可以安裝了。



### B.安裝 OPNsense 系統



啟動 OPNsense 的主機。您應該會看到類似下圖的歡迎頁面。在幾秒鐘的時間內，視窗中會顯示如圖所示的畫面。讓程序運行...



![Image](assets/fr/019.webp)



OPNsense 映像會載入機器，因此可以在「**live**」模式下存取系統，也就是暫時儲存在記憶體中。



![Image](assets/fr/025.webp)



接著您會看到類似下面的 Interface。使用登入名稱「**installer**」和密碼「**opnsense**」登入。請注意，此時的鍵盤是**QWERTY**。此時，我們將**啟動 OPNsense 安裝程序**。



![Image](assets/fr/026.webp)



螢幕上會出現新的精靈。第一步是選擇與您的配置相對應的鍵盤配置。若要使用 AZERTY 鍵盤，請從清單中選擇「**French (accent keys)**」選項，然後按兩下**。



![Image](assets/fr/027.webp)



第二步是選擇要執行的任務。在此，我們要使用 **ZFS 檔案系統** 執行安裝。將自己置於 「**安裝 (ZFS)**」行，然後用 **Enter** 確認。



![Image](assets/fr/028.webp)



在第三步中，選擇「**條**」，因為我們的機器只配備了**個磁碟**：沒有備援可能來保護防火牆的儲存空間及其資料。當安裝在實體機器上，透過 RAID 原則防止磁碟發生硬體故障時，這一點尤其重要。



![Image](assets/fr/029.webp)



第四步，只需按 **Enter** 確認即可。



![Image](assets/fr/030.webp)



最後，選擇「**YES**」確認，然後按下 **Enter** 鍵。



![Image](assets/fr/031.webp)



現在您必須等待 OPNsense 安裝完成...這個過程大約需要 5 分鐘。



![Image](assets/fr/032.webp)



安裝完成後，我們可以在重新開機前變更 "**root**" 密碼。選擇「**Root Password**」，按下 **Enter**，然後輸入密碼「**root**」兩次。



![Image](assets/fr/020.webp)



最後，選擇「**完成安裝**」，然後按下**Enter**。趁此機會**從虛擬機器的 DVD 光碟機**退出磁碟。在虛擬機器設定中，您也可以設定第一次開機到磁碟。



![Image](assets/fr/021.webp)



虛擬機器會重新啟動，並從磁碟載入 OPNsense 系統，因為我們剛安裝了它。使用主控台中的 "root 「帳號和新密碼登入（否則預設密碼為 」**opnsense**"）。



### D.連結網路介面



將會出現下圖所示的畫面。選擇 "**1**"，然後按**Enter**，將機器的網卡與 OPNsense 介面聯繫起來。



![Image](assets/fr/022.webp)



首先，精靈會要求您設定連結聚合和 VLAN。請指定「**n**」以拒絕，每次請以 **Enter** 驗證您的答案。接下來，您需要將兩個介面「**hn0**」和「**hn1**」分派給 **WAN** 和 **LAN**。原則上，「**hn0**」對應 WAN，另一個 Interface 對應 LAN。



工作原理如下：



![Image](assets/fr/023.webp)



我們現在有：





- 與「**hn1**」網路卡及 OPNsense 預設 IP Address 相關聯的 Interface **LAN**，即 **192.168.1.1/24**。
- Interface **WAN**與 "**hn0**"網卡相關聯，並透過**DHCP**在本端網路上擷取 IP Address（感謝我們的外部虛擬交換器）。



預設情況下，基於明顯的安全理由，OPNsense 管理 Interface 只能從 LAN Interface 存取。因此，您必須連線至防火牆的 Interface LAN 來執行管理。如果無法連線，您可以暫時從廣域網路管理 OPNsense。這需要關閉防火牆功能。



為此，請透過「**8**」選項切換至 shell 模式，並執行下列指令：



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E.存取 OPNsense Interface 管理系統



可透過 HTTPS，使用 LAN** Interface（或 WAN）的 IP Address 存取 OPNsense 管理 Interface。瀏覽器會帶您進入登入頁面。使用您之前選擇的 "root "帳號和密碼登入。



![Image](assets/fr/034.webp)



等待幾秒鐘...系統會提示您依照精靈執行基本設定。按一下「**下一步**」繼續。



![Image](assets/fr/036.webp)



第一步是定義主機名稱、網域名稱、選擇語言並定義用於名稱解析的 DNS 伺服器。保留「**啟用解析器**」選項將允許防火牆用作 DNS 解析器，這對我們虛擬區域網路中的機器很有用。



![Image](assets/fr/037.webp)



進入下一步。精靈會讓您選擇**定義日期和時間同步的 NTP 伺服器**，雖然預設已設定有伺服器。此外，必須選擇與您的地理位置相對應的時區 (除非您有特殊需求)。



![Image](assets/fr/038.webp)



接下來是重要的一步： **配置 Interface WAN**。目前，它是以 DHCP 方式設定，除非您想要設定 Address 的靜態 IP，否則會一直維持此設定模式。



![Image](assets/fr/039.webp)



在 Interface WAN 設定頁面中，如果 WAN 端的網路使用私人位址，您需要取消勾選「**Block access to private networks via WAN**」選項。如果您正在執行實驗室，很可能會出現這種情況，因此可能會阻止您存取網際網路。



![Image](assets/fr/040.webp)



接下來，您可以 ** 定義「root」** 密碼，但這是可選的，因為我們已經做了。



![Image](assets/fr/041.webp)



繼續到最後，啟動組態重新載入。如果您需要繼續透過 WAN 控制，請在此程序完成後重新啟動上述指令。



![Image](assets/fr/042.webp)



僅此而已！



![Image](assets/fr/035.webp)



### E.DHCP 設定



我們的目的是使用 OPNsense DHCP 伺服器在虛擬區域網路上分配 IP 位址。為此，我們需要存取此功能表位置：



```
Services > ISC DHCPv4 > [LAN]
```



*** 如您所見，DHCP 在區域網路的預設值已經啟用 ** 如果您對這項服務不感興趣，就應該停用它。儘管它已經啟用，而且我們想要使用它，但仍有必要檢閱其設定。



如果需要，您可以變更要分發的 IP 位址範圍： **192.168.10.10** 到 **192.168.10.245**，視目前設定而定。



![Image](assets/fr/046.webp)



我們也可以看到「**DNS 伺服器**」、「**閘道**」、「**網域名稱**」等欄位預設為空。事實上，這些不同欄位的某些選項和預設值是會自動繼承的。例如，對於 DNS 伺服器，Interface 區域網路的 IP Address 將被分發，使 OPNsense 防火牆能夠作為 DNS 解析器使用。



如有必要，請在進行任何變更後保存組態。



![Image](assets/fr/047.webp)



要測試 DHCP 伺服器，您需要將一台機器連接到防火牆的 LAN 網路。



這台機器必須從 OPNsense DHCP 伺服器取得 IP Address，而且我們的機器必須能存取網路。網際網路存取必須正常運作。請注意，如果您已停用防火牆功能，從廣域網路存取 OPNsense，這將會停用 NAT，使您無法存取 Web。



**註**：目前發出的 DHCP 租約可從 OPNsense 管理 Interface 看到。若要執行此動作，請前往下列位置： **服務 > ISC DHCPv4 > 租約**。



![Image](assets/fr/045.webp)



### F.設定 NAT 和防火牆規則



好消息是，我們現在可以從 LAN 存取 OPNsense 管理 Interface。



```
https://192.168.1.10
```



登入 OPNsense 後，讓我們來發現 NAT 設定。前往此位置： **Firewall > NAT > Outbound**。在這裡您可以選擇自動（預設）或手動建立出站 NAT 規則。



通過 「**自動產生外向 NAT 規則**」選項選擇自動模式，然後點擊 「**儲存**」（原則上，此配置已經是活動配置）。在自動模式下，OPNsense會自行為每個網路建立NAT規則。



![Image](assets/fr/043.webp)



目前，所有連接到虛擬區域網路「**192.168.10.0/24**」的電腦都可以不受限制地存取網際網路。不過，我們的目標是在防火牆的 Interface LAN 上，將廣域網路的存取限制為 HTTP 和 HTTPS 通訊協定，以及 DNS。



因此，我們需要建立防火牆規則...瀏覽功能表如下： **Firewall > Rules > LAN**。



**預設情況下，有兩條規則可授權所有 IPv4 和 IPv6 的外寄 LAN 流量**。按一下每行開頭最左邊的 Green 箭頭，停用這兩條規則。



然後建立三個新規則，將 **LAN 網路** (即「**LAN net**」) 授權給 ：





- 使用 **HTTP** 存取所有目的地。
- 使用 **HTTPS** 存取所有目的地。
- 透過**DNS 通訊協定**，在其**Interface LAN**（即「**LAN Address**」）上請求**OPNsense**（這意味著使用防火牆作為 DNS），否則透過其 IP Address 授權您的 DNS 解析器。



這會得到以下結果：



![Image](assets/fr/044.webp)



剩下的工作就是按一下「**套用變更**」，將新的防火牆規則切換到生產中。 **請注意，預設會封鎖所有未明確授權的流量。



LAN 機器可以存取網際網路，使用 HTTP 和 HTTPS。所有其他通訊協定都會被封鎖。



![Image](assets/fr/018.webp)



## IV.結論



按照本指南，您就能安裝 OPNsense 並立即開始使用。OPNsense 提供廣泛的功能，可有效保護及管理您的網路流量，適合在專業環境中使用。



此安裝只是個開始：請隨意探索功能表並設定其他功能，使 OPNsense 適合您的需求。