---
name: WireGuard
description: 在 Debian 和 Windows 上設定 WireGuard VPN
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



在本教程中，我們將學習如何設定基於 WireGuard 的 VPN，這是一個免費的開放原始碼 VPN 解決方案，可在不忽略安全性的情況下提升效能。



WireGuard 是一個相對較新的解決方案，自 2020 年 3 月起已推出穩定版本，並自版本 5.6** 起直接整合至**Linux 核心。但這並不表示使用不同版本內核的舊版 Linux 發行版無法存取。與 OpenVPN 和 IPSec 等解決方案相比，WireGuard 使用起來更簡單，速度也更快，我們會在本文結尾看到。



關於 WireGuard 的一些要點 ：





- 簡單、輕量、超高效！
- 僅 UDP 作業 (在穿越某些防火牆時可能會有缺點)
- 以點對點模式而非用戶端伺服器模式運作
- 透過金鑰 Exchange 進行驗證，原理與使用私人/公開金鑰的 SSH 相同
- 使用多種演算法：ChaCha 的對稱加密20、Poly1305 的訊息驗證，以及 Curve25519、BLAKE2 和 SipHash24 等其他演算法。
- 支援 IPv4 和 IPv6
- 多平台：Windows、Linux、BSD、macOS、Android、iOS、OpenWRT (並在 ProtonVPN 中實作)
- 只需 4,000 行程式碼，其他解決方案則需數十萬行程式碼



在加密部分，所使用的各種演算法都是經過精心挑選、多方審核，並由該領域的專業安全研究人員進行檢驗。



官方專案網站：[wireguard.com](https://www.wireguard.com/)



看完這篇介紹後，您是否對這個解決方案深信不疑？剩下要做的就是繼續閱讀了！



## II.實驗室 WireGuard 圖表



在我介紹我設定 WireGuard 的實驗室之前，您應該知道您可以想像**使用 WireGuard 將兩個遠端基礎建設**互連，也可以**將遠端用戶端與基礎建設（例如公司網路或您的家庭網路）**互連。這與 OpenVPN 的精神相同，就像我們最近在教學「[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)」中看到的一樣。



如果 WireGuard 並非直接設定在路由器或防火牆上 (如 OpenWRT 的情況)，您需要設定連接埠轉送，讓流量可以到達 WireGuard 對。



![Image](assets/fr/034.webp)



現在我會告訴你我的實驗室，以及我們今天要建立的實驗室。



我將使用 Debian 11 作為 WireGuard 伺服器，並使用 Windows 用戶端作為 WireGuard VPN 用戶端。雖然說到客戶端與伺服器的關係有點誤導，因為 **WireGuard 是以「點對點」** 模式運作。當您嘗試建立「客戶端對客戶端」連線時，這種說法就有點名不副實了。比方說，我將有兩對或**兩個 WireGuard 連線點**（如果您願意的話）：一個在 Debian 11 下，另一個在 Windows 下。



這兩對機器可以雙向溝通，也就是說，從我的 Windows 機器可以存取 Debian 11 機器的遠端區域網路，反之亦然：這完全取決於隧道的設定和 WireGuard 對等機器的防火牆。



在本範例中，我將著重於以下情況： **from my Windows Peer 1 connected to my home network, I want to access my corporate network in order to access the company's servers via the WireGuard VPN tunnel**.這會得到以下圖表：



![Image](assets/fr/035.webp)



就 IP 位址而言，這提供 ：





- 家庭網路**： 192.168.1.0/24
- 公司網路**： 192.168.100.0/24
- WireGuard 隧道網路**： 192.168.110.0/24


+ 通道中 Peer 1 (Windows) 的 IP Address： 192.168.110.2/24


+ 對等端 2 (Debian) 在隧道中的 IP Address： 192.168.110.121/24



就是這麼多了！讓我們開始配置！



**注意：預設情況下，WireGuard 在 ** 埠 51820** 上以 UDP 模式運作。



## III WireGuard 伺服器安裝與設定



在本教程中，我將使用「客戶端」來表示 Windows 機器，而「伺服器端」則表示 Debian 機器，因為即使它是點對點，似乎也更有意義。



### A.在 Debian 11 上安裝 WireGuard



WireGuard 安裝套件可在 Debian 11 官方套件庫中找到，因此我們只需更新套件快取並安裝即可：



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



WireGuard 伺服器部分將會安裝，同時還會安裝各種工具，讓您可以使用有用的指令來管理組態。



### B.安裝 Interface WireGuard



使用 ** 指令 "wg "** 我們需要 generate 私密金鑰和公開金鑰，這是兩對金鑰之間進行認證的必要條件，也就是伺服器和用戶端 (也需要一對金鑰)。



我們將使用此指令序列建立私密金鑰「**/etc/wireguard/wg-private.key**」和公開金鑰「**/etc/wireguard/wg-public.key**」：



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



公開金鑰的值會傳回控制台。在 WireGuard 設定檔中，我們需要**加入私人密碼匙的值**。若要擷取此值，請輸入以下指令並複製值 ：



```
sudo cat /etc/wireguard/wg-private.key
```



是時候在 "**/etc/wireguard/**"中建立一個設定檔了。例如，我們可以將這個檔案命名為「**wg0.conf**」，如果我們認為與 WireGuard 相關聯的 Interface 網路將會是「wg0」，原理與「eth0」等同。



```
sudo nano /etc/wireguard/wg0.conf
```



在這個檔案中，我們必須先加入下列內容（稍後再來完成）：



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



章節 `[Interface]` 用來宣告伺服器部分。以下是一些資訊：





- Address**：VPN 通道內 Interface WireGuard 的 IP Address（與遠端 LAN 不同的子網路）
- SaveConfig**：只要 Interface 啟用，組態就會被儲存（並受到保護
- ListenPort**：WireGuard 的監聽埠。在本例中，51820 是預設連接埠，但歡迎您自訂。
- PrivateKey**：我們伺服器的私密金鑰值 (*wg-private.key*)



儲存檔案並關閉。使用「**wg-quick**」指令，我們可以指定 Interface 的名稱（wg0，因為檔案名稱是 wg0.conf）來啟動它：



```
sudo wg-quick up wg0
```



如果您列出 Debian 11 伺服器的 IP 位址，您會看到一個名為「wg0」的新 Interface，其 IP Address 定義在設定檔 ：



```
ip a
```



![Image](assets/fr/027.webp)



基於同樣的精神，我們可以透過「wg show」指令來顯示 Interface "wg0 "的設定：



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



最後，我們需要啟動 Interface wg0 WireGuard 的自動啟動功能：



```
sudo systemctl enable wg-quick@wg0.service
```



我們暫時不談 WireGuard 伺服器端的設定。



### C.啟用 IP 轉發



為了讓我們的 Debian 11 機器能夠在不同網路之間**路由封包 (就像路由器一樣)**，也就是在 VPN 網路和本地網路之間**路由，我們需要啟用 [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/)。預設情況下，此功能是停用的。



修改此設定檔 ：



```
sudo nano /etc/sysctl.conf
```



在檔案末尾加入下列指令並儲存 ：



```
net.ipv4.ip_forward = 1
```



僅此而已。



### D.啟用 IP 防偽



為了讓我們的伺服器能正確地路由封包，並讓遠端區域網路能被 Windows 機器存取，我們需要在 Debian 伺服器上啟動 IP Masquerade。這是一種 NAT 啟用。我將透過我習慣使用的 UFW 在 Linux 防火牆上執行這項設定 ([ufw tutorial on Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/))。



如果您還沒有 UFW 而且想要設定它（您也可以使用 Nftables），請先安裝 .NET Framework：



```
sudo apt install ufw
```



首先，您需要啟用 SSH，以免失去對遠端伺服器的控制 (調整連接埠號)：



```
sudo ufw allow 22/tcp
```



UDP 中的連接埠 51820 也必須經過授權，因為我們將其用於 WireGuard（再次調整連接埠號）：



```
sudo ufw allow 51820/udp
```



接下來，我們要繼續設定啟用 IP masquerade。為此，我們需要擷取連線到本機網路的 Interface 的名稱。如果您不知道名稱，請執行「ip a」查看網卡的名稱。在我的例子中，它是 "**ens192**" 卡。



![Image](assets/fr/036.webp)



我們要使用這些資訊。編輯以下檔案：



```
sudo nano /etc/ufw/before.rules
```



在檔案末尾加入這幾行，以在本機防火牆 NAT 表的 POSTROUTING 字串中 ** 啟用 Interface ens192** 上的 IP masquerade (調整 Interface 名稱)：



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



圖片顯示 ：



![Image](assets/fr/037.webp)



保持開啟此組態檔案，並進行下一步。



### E.WireGuard 的 Linux 防火牆設定



還是在相同的設定檔中，我們要宣告企業網路「192.168.100.0/24」，以便我們可以與它聯繫。以下是要新增的兩個規則 (最好是在 "*# ok icmp code for FORWARD*"部分之後，以便將規則分組在一起)：



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



如果您只想授權一台主機，例如「192.168.100.11」，就很容易：



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



現在您可以儲存檔案並關閉。剩下的工作就是啟動 UFW 並重新啟動服務以套用我們的變更：



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Debian 伺服器設定的第一部分至此完成。



## IV.適用於 Windows 的 WireGuard 客戶端



WireGuard 客戶端適用於 Windows、macOS、Android 等平台...這是個好消息。本頁面提供所有下載：[WireGuard Client](https://www.wireguard.com/install/)。在這個範例中，我要在 Windows 上設定用戶端。要在 Linux 上設定 WireGuard 用戶端，請遵循在 Debian 機器上建立 wg0.conf 檔案的相同原則 (不包含所有 NAT 等)。



### A.安裝 WireGuard Windows 用戶端



下載可執行檔或 MSI 套件後，安裝就很簡單：只要啟動安裝程式，然後...瞧，就完成了！ 🙂



![Image](assets/fr/038.webp)



### B.建立 WireGuard 設定檔



首先打開軟體建立一個新的隧道。若要這樣做，請按一下「**新增隧道**」按鈕右邊的箭頭，然後按一下「**新增空隧道**」按鈕。



![Image](assets/fr/028.webp)



設定視窗將會開啟。每次建立新的隧道組態時，WireGuard 都會產生此組態專用的私人/公開金鑰對。 **在此設定中，我們需要宣告「對等」，也就是遠端伺服器：



```
[Interface]
PrivateKey = <la clé privée du PC>
```



我們需要完成這項設定，特別是在此 Interface 上宣告 IP Address（*Address*），同時也要透過 [Peer] 區塊宣告遠端 WireGuard 伺服器。下圖應該可以提醒您我們在 Linux 伺服器端建立的設定檔。



讓我們從 `[Interface]` 區塊開始，加入 IP Address "**192.168.110.2**「；記得伺服器在此網段上有 IP Address 」**192.168.110.121**"。這樣就得到 ：



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



接下來，我們需要宣告具有三個屬性的 "Peer" 區塊，結果就是這樣的設定：



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



圖片 ：



![Image](assets/fr/029.webp)



**關於 [Peer] 區塊的一些說明：





- PublicKey**：這是 WireGuard Debian 11 伺服器的公開金鑰 (您可以使用「*sudo wg*」指令取得其值)
- AllowedIPs**：這些是透過 WireGuard VPN 網路存取的 IP 位址/子網路，在本例中為我的 WireGuard VPN (*192.168.110.0/24*) 和我的遠端 LAN (*192.168.100.0/24*) 所指定的子網路。
- 端點**：這是 Debian 11 主機的 IP Address，因為這是我們的 WireGuard 連線點（您需要指定公共 IP Address）。



最後，在「**名稱**」欄位中輸入名稱（不含空格），並複製和貼上客戶端公開金鑰，因為我們需要在伺服器上宣告它。按一下「**註冊**」。



### C.在 WireGuard 伺服器上宣告用戶端



現在是時候回到 Debian 伺服器，在 WireGuard 設定中宣告「**Peer**」，也就是我們的 Windows PC。首先，我們需要**停止 Interface "wg0"** 以修改其設定：



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



接下來，修改先前建立的組態檔案：



```
sudo nano /etc/wireguard/wg0.conf
```



在這個檔案中，在`[Interface]`區塊之後，我們需要宣告一個`[Peer]`區塊：



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



此 [Peer] 區塊包含 Windows 10 PC 的公開金鑰 (**PublicKey**) 和 PC 的 Interface 的 IP Address（**AllowedIPs**）：伺服器在此 WireGuard 通道中通訊只會聯絡 Windows 用戶端，因此值為「**192.168.110.2/32**」。



剩下的就是儲存檔案 (*CTRL+O 然後按 Enter，然後透過 Nano* 按 CTRL+X)。重新啟動 Interface "wg0"：



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



若要檢查對等宣告是否有效，您可以使用此指令：



```
sudo wg show
```



一旦遠端主機設定了 WireGuard 連線，其 IP Address 將會上移到「端點」值。



![Image](assets/fr/033.webp)



最後，我們會保護組態檔案以限制 root 存取：



```
sudo chmod 600 /etc/wireguard/ -R
```



### D.第一次 WireGuard 連線



現在設定已經就緒，我們可以從 Windows PC 啟動。要做到這一點，請在 "**WireGuard**「用戶端中，點擊 」**啟動**「按鈕：連接將從 」關閉 「變為 」開啟 "**，但這並不意味著它將工作。這完全取決於您的設定是否正確。 **當連線建立後，我們的兩台機器會透過各自配置的 Interface WireGuard 進行通訊！



![Image](assets/fr/030.webp)



如果發生問題，這將會在 "**Logbook**" 標籤中看到。兩台主機會定期傳送 Exchange 封包以檢查連線狀態，因此會出現「*Receiving keepalive packet from peer 1*」訊息。



![Image](assets/fr/031.webp)



如果 WireGuard 的「**日誌**」標籤顯示類似下圖的訊息，您需要檢查雙方宣告的公開金鑰是否正確。



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



從我的遠端電腦，我可以 ping 到伺服器端的 Interface WireGuard 的 IP Address，以及遠端 LAN 上的主機。



![Image](assets/fr/032.webp)



### E.效能：OpenVPN vs WireGuard



從我連接至 WireGuard VPN 的遠端電腦，我可以存取檔案伺服器，並透過 [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/) 傳輸檔案，看看傳輸速率。 **使用 WireGuard，我的最高傳輸速率約為 45 Mb/s，這非常好，因為我使用的是 WiFi。



![Image](assets/fr/025.webp)



在相同的條件下，但這次是透過 OpenVPN 連線 (在 UDP 中)，在相同的操作下，吞吐量完全不同：約 3 MB/s。差異是顯而易見的！



![Image](assets/fr/026.webp)



這是很有趣的，因為舉例來說，如果您從 WiFi 連線切換到 4G/5G 連線，重新連線的速度會快到看不出中斷的情況。



### F.獎勵：全隧道 WireGuard



在目前的配置下，部分流量流經 VPN，其餘則流經客戶的網際網路連線，包括網際網路瀏覽。如果我們要切換到 WireGuard **全隧道模式**，讓所有流量都透過 VPN 隧道，我們需要對配置進行一些變更....



首先，您需要在 .NET Framework 上安裝「resolvconf」套件：



```
sudo apt-get update
sudo apt-get install resolvconf
```



完成後，您需要修改 Debian 機器上的「wg0.conf」檔案：停止 Interface、修改它，然後再重新啟動。



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



接下來，**在`[Interface]`區塊中，我們加入要使用的 DNS 伺服器**。在我的例子中，它是我實驗室的網域控制器，但我們也可以在 Debian 機器上安裝 Bind9 來使用本機解析器。



```
DNS = 192.168.100.11
```



儲存檔案，然後重啟 Interface ：



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



最後，在 Windows 10 工作站的隧道設定中，您需要修改「AllowedIPs」部分，以表示所有東西都必須通過隧道。取代 ：



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



作者：



```
AllowedIPs = 0.0.0.0/0
```



您可以看到這也啟用了「**殺手開關*」選項。



![Image](assets/fr/040.webp)



最後，我利用這條滿載的隧道進行了一次小型流量測試，結果如下：



![Image](assets/fr/039.webp)



WireGuard 的設定相當簡單易懂，最重要的是容易維護。 **WireGuard被認為是VPN的未來**，所以我們最好密切注意！我們也可以看到，在效能方面，WireGuard 的優勢是相當顯著的，與 OpenVPN 相比，這是 WireGuard 的一大優勢。



其他文件 ：





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Man - Command wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**您的 WireGuard VPN 已開始運作！恭喜您