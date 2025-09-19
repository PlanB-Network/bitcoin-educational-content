---
name: Tailscale
description: Tailscale 進階教學
---
![cover](assets/cover.webp)



## 1.簡介



Tailscale 是下一代 VPN，可在您的裝置之間建立加密的網狀網路。它可讓您連接遠端機器，就像它們在相同的本地網路中一樣，無需複雜的設定或開啟連接埠。



對於自行託管，Tailscale 會在虛擬網路中為每個裝置指派固定的私有 IP，即使您的公用 IP 變更，也能穩定存取您的服務。這表示您可以遠端管理您的伺服器，而無需將您的服務直接暴露於網際網路。



**主要應用：**




- 從外部管理個人伺服器
- 管理 Umbrel/Lightning 節點的速度比 Tor 更快
- 安全存取 Raspberry Pi 或 NAS
- 透過 SSH 或 HTTP 連線至您的服務，無需複雜的網路設定



這種以簡化為重點的方法可讓自助主機使用者安全地存取服務，避免傳統 VPN 的隱患。



## 2.Tailscale 如何運作



傳統 VPN 會透過中央伺服器路由所有流量，而 Tailscale 則不同，它會建立一個網狀網路，讓裝置之間直接通訊。中央伺服器只處理驗證和金鑰分發，不會看到使用者資料。



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*圖 1：傳統 VPN 採用集線器架構，所有流量都經過中央伺服器*。



基於 WireGuard，每個裝置都會產生自己的加密金鑰。協調伺服器將公開金鑰分發給節點，然後節點之間直接建立端對端加密隧道。為了穿透防火牆，Tailscale 使用 NAT 穿透，最後使用能維持加密的 DERP 中繼。



![VPN maillé (mesh)](assets/fr/02.webp)


*圖 2：設備之間直接通訊的尾端尺度網狀網路*



所有通訊都使用 WireGuard 加密。Tailscale 只能看到元資料 (連線)，但絕不會看到交換的內容。為了更大的主權，Headscale 可讓協調伺服器自行託管。



**安全性和機密性：** 多虧了 WireGuard，Tailscale 上的所有通訊都經過端對端加密。Tailscale 無法讀取您的流量 - 只有您的裝置擁有必要的私人金鑰。服務只能看到元資料：IP 位址、裝置名稱、連線時間戳記和點對點連線記錄（不含內容）。



然而，此架構依賴 Tailscale Inc. 進行網路協調。為了消除這種依賴性，Headscale 提供了開放原始碼的替代方案，讓您可以在使用官方 Tailscale 用戶端時自行託管控制伺服器，從而保證您對網路基礎架構的完全主權，但代價是更高的技術配置。



**若要詳細解釋 Tailscale 的內部運作，包括控制平面管理、NAT 穿透和 DERP 中繼，我們推薦官方部落格上的優秀文章** [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works)**。這篇文章深入解釋了讓 Tailscale 如此強大的技術概念。**



## 3.安裝 Tailscale



Tailscale 可在最常見的**作業系統 (Windows、macOS、Linux、iOS、Android)** 上執行。據說在所有平台上安裝都非常「快速簡單」。讓我們先來看看 Interface 以及如何建立帳號，然後再看看不同環境的安裝程序。



### 3.1 建立 Tailscale 帳戶



前往 [https://tailscale.com/](https://tailscale.com/)，按一下頁面右上方的「開始」按鈕。




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscale 首頁解釋了這個概念，並提供免費入門*。



若要使用 Tailscale，您首先需要透過身分提供者建立帳戶：



![Page de connexion Tailscale](assets/fr/04.webp)


*選擇與 Tailscale 連線的身份供應商 (Google、Microsoft、GitHub、Apple 等)*。



登入後，Tailscale 會要求您提供一些關於您的預期用途的資訊：



![Questionnaire d'utilisation](assets/fr/05.webp)


*表單以更了解您的使用個案（個人或專業）*



建立帳戶後，即可在裝置上安裝 Tailscale：



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale 可讓您在不同的系統上安裝應用程式*。



### 3.2 在不同平台上安裝





- 在 Windows 和 macOS 上：只需從 Tailscale 官方網站下載圖形化應用程式並安裝（Windows 上為 .msi 檔案，Mac 上為 .dmg 檔案）。安裝完成後，應用程式會啟動圖形 Interface，讓您 (透過瀏覽器) 連線至 Tailscale 帳戶以驗證機器。



![Connexion d'un appareil macOS](assets/fr/08.webp)


*將 MacBook 連接到尾網*



![Connexion réussie](assets/fr/09.webp)


*確認裝置已連線至 Tailscale* 網路





- 在 Linux (Debian、Ubuntu 等)：**您有幾種選擇。最簡單的方法是執行官方安裝腳本：例如，在 Debian/Ubuntu：**



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



這個腳本會新增 Tailscale 官方套件庫，並安裝套件。您也可以 [手動新增 APT 套件庫](https://pkgs.tailscale.com) 或使用一般的 Snap 或 apt 套件。安裝完成後，daemon `tailscaled` 會在背景執行。接下來您需要 ** 驗證節點** (請參閱下面的 Interface CLI vs web)。在其他發行版（Fedora、Arch...）上，也可以透過標準套件庫或通用安裝腳本取得套件。對於無頭伺服器，請使用 CLI：例如 `sudo tailscale up --auth-key <key>`，如果使用預先產生的驗證金鑰，或直接 `tailscale up` 進行互動式登入 (這將提供一個 URL 供您造訪以驗證裝置)。





- 在以 ARM 為基礎的系統 (Raspberry Pi 等)：**我們一般使用 Linux，所以方法與上述相同 (腳本或套件)。請注意，Tailscale 支援 ARM32/ARM64 架構沒有任何問題。許多使用者透過 apt 將 Tailscale 安裝在 Raspberry Pi OS 上，或安裝在輕量級發行版 (DietPi 等) 上，以便隨處存取他們的 Pi。**





- 在 iOS 和 Android 上：**Tailscale 提供官方行動應用程式**。只要從 [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) 或 [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android) 安裝 *Tailscale* 即可。



![Installation sur iPhone](assets/fr/11.webp)


*在 iPhone 上安裝 Tailscale 的步驟：歡迎、隱私、通知、VPN*。



![Connexion sur iPhone](assets/fr/12.webp)


*連線至 tailnet，選擇帳號並在 iPhone 上驗證*。



安裝應用程式後，第一次啟動時會要求您透過選擇的提供者（Google、Apple ID、Microsoft 等，視您使用的 Tailscale 類型而定）進行驗證 - 這與其他平台上的程序相同，通常會重定向至 OAuth 網頁。之後，行動應用程式會建立 VPN（在 iOS 上，您需要接受 VPN 配置附加元件）。之後，應用程式就可以在背景執行，讓您可以從任何地方存取您的 tailnet。**請注意：**在行動裝置上，您一次只能有**一**個有效的 VPN - 因此請確定您沒有同時連線其他 VPN，否則 Tailscale 無法建立自己的 VPN。在 Android 上，如果您想要隔離某些用途 (例如：在特定應用程式中使用 Tailscale 的設定檔)，您可以設定獨立的工作設定檔。



### 3.3 加入多個裝置和驗證



連接第一台裝置後，Tailscale 會提示您新增其他裝置到網路：



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface 顯示連接的第一台裝置，並等待其他裝置*。



當您加入數個裝置後，就可以檢查它們是否能互相通訊：



![Test de connectivité entre appareils](assets/fr/13.webp)


*確認裝置可透過 ping* 相互通訊



Tailscale 隨後會建議其他配置，以提升您的體驗：



![Suggestions de configuration](assets/fr/14.webp)


*設定 DNS、共用裝置和管理存取的建議*



### 3.4 管理儀表板



Web 管理主控台可讓您檢視和管理所有連接的裝置：



![Tableau de bord des machines](assets/fr/15.webp)


*連線裝置清單及其特性和狀態*



**Interface Web vs Interface CLI：** Tailscale 提供兩種互補的網路互動方式：**Interface Web 管理**和**指令行用戶端 (CLI)** 。





- Interface Web (管理主控台)：可從 [https://login.tailscale.com](https://login.tailscale.com)存取，此 Web 主控台是 Tailscale 網路的中央儀表板。它會列出所有裝置 (*機器*)、它們的線上/離線狀態、它們的 Tailscale IP 位址等等。在這裡，您可以**管理裝置** (重新命名、金鑰過期、授權路由、停用節點)、**管理使用者** (在組織情境中)，以及定義安全性規則 (ACL)。這也是您設定 MagicDNS、標籤或授權金鑰（generate 之前的授權金鑰，用於自動新增裝置）等全局選項的地方。Interface Web 非常方便您取得總覽，並套用將透過協調伺服器傳播到所有節點的變更。*範例：*啟動**子網路路由**或**退出節點**只需在主控台上按一下





- Interface 指令行 (CLI):** `tailscale` 指令可在 CLI 中安裝 Tailscale 的每個裝置上使用。此 CLI 允許您在本機執行所有操作：連線 (`tailscale上傳`)、檢視狀態 (`tailscale狀態`，查看哪些對等體已連線)、除錯 (`tailscaleping<ip>`)，等等。有些功能甚至是 CLI** 獨家或更進階的，例如：





  - `tailscale up --advertise-routes=192.168.0.0/24` 廣告子網路路由、
  - tailscale up --advertise-exit-node 會將您的機器列為退出節點、
  - `tailscale set --accept-routes=true` (或 `--exit-node=<IP>`)以消耗路由或使用出口節點、
  - `tailscale ip -4` 來顯示裝置的 Tailscale IP、
  - 尾巴鎖定/解除鎖定」（如果使用 *tailnet-lock* 進階安全功能）、
  - 或 `tailscale file send <node>` 來使用 **Taildrop**（裝置間的檔案傳輸）。


CLI 在沒有 Interface 圖形的伺服器上非常有用，也可以用來編寫某些動作的腳本。 **使用上的差異：** 大部分的基本設定都可以透過 Web 或 CLI 進行。例如，新增裝置可透過主控台提示，或在裝置上執行「tailscale up」並透過 Web 驗證。同樣地，重新命名裝置也可以透過主控台或使用 `tailscale set --hostname` 來完成。 **總括而言**，網頁主控台是全局網路管理的理想選擇 (尤其是在有多台機器/使用者的情況下)，而 CLI 則方便對指定機器、自動化腳本進行細緻控制，或在沒有 GUI 的系統上使用。



## 4.在 Umbrel 上使用 Tailscale



Umbrel 是一個廣受歡迎的自助託管平台（主要用於 Bitcoin/Lightning 節點和其他自助託管服務，透過其 App Store）。要安裝和設定 Umbrel，建議您按照我們的專用教學 ：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

將 Umbrel 和 Tailscale 搭配使用是一個特別有趣的使用個案，因為 Umbrel 原生整合了一個容易部署的 Tailscale 模組。以下是 Tailscale 如何與 Umbrel 整合及其帶來的效益：



### 4.1 傘筒安裝與配置





- 在 Umbrel 上安裝 Tailscale：**Umbrel 在其 App Store 中擁有官方的 Tailscale 應用程式。安裝再簡單不過：**



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Umbrel App Store 中的 Tailscale 應用程式頁面*



從 Interface Web Umbrel 開啟 App Store，搜尋 **Tailscale**，然後按一下 *Install*。幾秒鐘之後，應用程式就會安裝在 Umbrel 上。當您開啟時，Umbrel 會顯示一個頁面，讓您將您的節點連結至 Tailscale。



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Umbrel 的 Interface* 中的尾秤連接螢幕



只要 ** 點選「登入」**，就會轉到 Tailscale 認證頁面：



![Page d'authentification Tailscale](assets/fr/18.webp)


*透過身份供應商連線至 Tailscale*



您可以透過 Tailscale 帳戶 (Google/GitHub/etc.) 進行驗證，或是輸入您的電子郵件。通常在 Umbrel 上，Interface 會要求您造訪 [https://login.tailscale.com](https://login.tailscale.com)，然後登入 - 這會驗證 Umbrel Tailscale 應用程式。



![Confirmation de connexion réussie](assets/fr/19.webp)


*確認 Umbrel 裝置已連線至 Tailscale 網路*



一旦完成，您的 Umbrel 就「進入」您的 Tailscale 網路，並在您的主控台上出現一個名稱 (例如 *umbrel*)。接下來您可以點選裝置的 IP Address 來複製、擷取 IPv6 Address 或與裝置相關的 MagicDNS。



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscale 管理主控台顯示多個連接的裝置，包括 Umbrel*




### 4.2 遠端存取 Umbrel 服務



一旦 Umbrel 連接到 Tailscale，**您就可以從任何地方存取 Interface Umbrel 及其上執行的應用程式，就像在本地網路一樣**。這是 Tor 的主要優勢之一。



存取非常簡單：您不需要使用 `umbrel.local`（只能在您的區域網路運作），而是直接從任何連接到您 tailnet 的裝置使用 Umbrel 的 Tailscale IP Address (`http://100.x.y.z`)。無論您身在何處或使用何種網際網路連線 (4G、公眾 Wi-Fi、公司網路)，都能正常運作。



**可透過 Tailscale 存取的 Umbrel 託管應用程式範例：**





- Interface 主 **Umbrel**：只需在瀏覽器中輸入 `http://100.x.y.z` 即可存取您的 Umbrel 面板
- Bitcoin 節點：無延遲地管理您的 Bitcoin 節點、檢視同步與統計資料
- Lightning 節點：使用 ThunderHub、RTL 或其他 Lightning 管理介面，可立即回應
- **Mempool**：查看 Bitcoin 交易和 Mempool 無 Tor 延遲
- **noStrudel**：存取您託管在 Umbrel 上的 Nostr 服務



**透過 Tailscale 將外部錢包連接到您的 Bitcoin 或 lightning 節點:**



Tailscale 還能讓您安裝在其他裝置上的 Bitcoin 和 Lightning 錢包直接連接到您的 Umbrel 節點：





- **Sparrow wallet (Bitcoin)**：此外部 Wallet Bitcoin 可以使用 Tailscale IP Address 直接連接到您 Umbrel 的 Electrum 伺服器：



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*使用 Umbrel 的 Tailscale IP Address* 在 Sparrow wallet 中設定私人 Electrum 伺服器



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*在 Sparrow 中使用 Umbrel Tailscale IP Address* 的 Electrum 伺服器別名清單



請閱讀我們完整的 Sparrow wallet 與 Bitcoin 節點設定指南：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- 宙斯（閃電）：這個 Wallet Mobile Lightning 可以連接到您 Umbrel 上的 Lightning 節點。只需設定您 Umbrel 的 Tailscale IP 和 Lightning API 連接埠，而無需設定端點為 `.onion`。與 Tor 相比，連線將會是瞬間的。



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*設定 Zeus 透過 Tailscale* IP Address 連線至 Lightning 節點



若要設定 Zeus 與您的 Lightning 節點，請參閱我們的詳細教學：



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

若要瞭解更多關於 Lightning Network 及其如何在 Umbrel 上運作的資訊，請造訪 ：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 與 Tor 相比的優勢



Umbrel 原生提供透過 Tor 的遠端存取（透過為其 Web 服務提供 `.onion` 位址）。雖然 Tor 具備保密性（匿名性）和無需註冊的優點，但許多使用者覺得**Tor 在日常使用上既緩慢又不穩定**（頁面載入緩慢、超時等） - *「透過 Tor 的 Umbrel 實在太慢了 」* 有些人抱怨道。



Tailscale 通常提供**更快速、低延遲**的連線，因為流量會直接傳遞（或透過快速中繼），而不是透過 3 個 Tor 節點跳轉。更重要的是，Tailscale 提供「本機網路」體驗：使用私有 IP，並可直接映射應用程式 (例如 SMB 網路磁碟機上的 \100.x.y.z)。



話雖如此，Tor 的優勢在於它是分散式的，而且在 Umbrel 上是「開箱即用」，而 Tailscale 則需要信任第三方（或託管 headcale）。Tor 對於無用戶端存取也很有用 (從任何 Tor 瀏覽器，您都可以查看 Umbrel UI，而 Tailscale 則需要在存取裝置上安裝用戶端)。



**總括而言**，對於互動式使用 (Lightning wallets、頻繁的 Web 介面)，Tailscale 比 Tor 提供了顯著的舒適度和速度，但代價是會有一點外部依賴性。許多人選擇兩者並用：Tailscale 日常使用，而 Tor 則作為後備或與他人分享存取權限，而不需邀請他們進入自己的 VPN。



### 4.4 安全



將 Tailscale 與 Umbrel 搭配使用，可避免將 Umbrel 暴露於網際網路。Umbrel 節點只能由您在 tailnet 中的其他認證裝置存取，大幅降低攻擊面 (沒有連接埠開放給陌生人，沒有透過網際網路攻擊網路服務的風險)。



除了您的服務已經進行的任何加密（例如，即使內部 HTTP 也在隧道中）之外，通訊也會加密 (WireGuard)。您仍然可以套用 Tailscale ACL，例如，如果您想要分割網路，就可以防止特定的 tailnet 裝置存取 Umbrel。Umbrel 本身看不出差異 - 它以為是在提供本機服務。



---

在本節的最後，在 Umbrel 上整合 Tailscale 只需幾下點擊，就能**大大改善您自託管節點的存取**。您可以從任何地方安全且有效率地管理 Umbrel 及其服務，就像在家一樣。這對於受 Tor 延遲影響的即時應用程式 (Lightning) 來說是一個特別有用的解決方案，對於任何尋求簡單私人連線的自主存儲器來說也是如此。這一切都不需要暴露您電腦上的任何一個連接埠，也不需要複雜的網路設定。



## 5.進階管理與用例



### 5.1 Tailscale 進階功能



**網路管理：** 管理主控台 (login.tailscale.com) 可讓您管理裝置、檢視連線並設定存取規則。



**MagicDNS:** 自動解析裝置名稱 (例如：`raspberrypi.tailnet.ts.net`) 以避免記憶 IP 位址。



**ACL 與存取控制：** 透過 JSON 規則精確定義誰能存取網路中的哪些內容，非常適合隔離特定裝置或限制存取特定服務。



**Device Sharing** 可讓您邀請他人存取特定的機器，而不會讓他們存取您的整個網路。



**子網路路由器：** Tailscale 機器可作為整個子網路的閘道，透過單一設定的機器存取非 Tailscale 裝置 (物聯網、印表機等)。



**出口節點：** 使用機器作為網際網路閘道，以其 IP 出口。適用於公共 Wi-Fi 或繞過地理限制。



**Taildrop:** 是 AirDrop 的安全替代方案，可讓您在 Tailscale 裝置之間傳輸檔案，不論裝置的平台或位置為何。AirDrop 只限於 Apple 生態系統和實體距離，而 Taildrop 則不同，它可以在您所有的裝置 (Windows、Mac、Linux、Android、iOS) 之間傳輸，即使這些裝置位於不同國家。檔案會以端對端的加密方式直接在裝置之間傳輸，無須經過中央伺服器。根據您的系統，使用命令列 `tailscale file cp` 或圖形 Interface 應用程式。



### 5.2 與其他解決方案的比較



**Vs OpenVPN:** Tailscale 的設定簡單得多（無需開啟埠、無需證書管理），但需要依賴第三方服務。OpenVPN 可完全控制，但需要更多的專業知識。



**作為直接競爭對手，ZeroTier 運作於 Layer 2 (乙太網路)，支援廣播/群播，而 Tailscale 運作於 Layer 3 (IP)。ZeroTier 提供更大的網路彈性，而 Tailscale 則偏向於簡單易用。**



**Vs Tor:** Tor 提供 Tailscale 所沒有的匿名性，但速度要慢得多。Tor 是分散式的，不需要帳號，而 Tailscale 速度更快，並提供類似 LAN 的體驗。



**Vs WireGuard 手冊：** Tailscale 自動化所有 WireGuard 原本需要您手動處理的金鑰和連線管理。它基本上是 WireGuard + 簡化管理 Layer。



總而言之，Tailscale 將自己定位為現代化、簡單導向的解決方案，非常適合個人和小型團隊使用。對於需要完全控制的純粹使用者，Headscale 提供了一種自我託管的替代方案。



## 6.總結



**Tailscale 的優點：** Tailscale 為自行託管提供多項優點：





- **簡易與效能** - 可在所有平台上快速安裝，無須複雜的網路設定。流量遵循您的機器之間最直接的路徑 (P2P 網狀)，具有 WireGuard 通訊協定的效能，且無中央伺服器限制吞吐量。
- **安全性與彈性** - 端對端加密、降低攻擊面，以及進階功能 (ACL、SSO/MFA 認證)。即使在 NAT 後面或移動中也能運作，搭配子網路路由器和出口節點，讓網路符合您的需求。



**Limits:** 也請記住：





- **外部依賴性** - 在標準版本中，服務依賴於 Tailscale Inc.此依賴可透過 Headscale (自我託管替代方案) 繞過。
- **其他限制** - 部分封閉原始碼、免費版本對某些進階用途的限制、不支援 Layer 2 (廣播/群播)，以及需要網際網路存取才能建立連線。



**Tailscale 是個人自助主機和小型團隊、需要存取分散資源的開發人員、VPN 初學者和行動使用者的理想選擇。對於需要完全控制的公司，其他解決方案如 Headscale 或直接使用 WireGuard 可能會比較好。**



**探索 Headscale 的完全自助託管、API 和 DevOps 整合 (Terraform)，或 Innernet（類似但完全自助託管）和 Netmaker 等替代方案。**



Tailscale 是自我託管的必要工具，因為它簡單又有效率，讓您的私有基礎架構就像在雲端一樣容易存取，同時又能在家中進行控制。



## 7.有用資源



### 官方文件





- **Tailscale 文件中心**：[docs.tailscale.com](https://docs.tailscale.com) - 完整的英文說明文件、安裝指南、教學和技術參考。
- Tailscale 如何運作：[How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - 詳細說明 Tailscale 內部運作的文章。
- **Changelog**：[tailscale.com/changelog](https://tailscale.com/changelog) - 追蹤更新與新功能。



### 實用指南





- **Homelab** 教學：[tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - 自我託管的特定指南。
- 設定出口節點：[tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - 配置退出節點的詳細指南。
- 使用 **Taildrop**：[tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - 在 Tailscale 裝置之間傳輸檔案。



### 比較





- **Tailscale 與其他解決方案的比較**：[tailscale.com/compare](https://tailscale.com/compare) - 與其他 VPN 和網路解決方案 (ZeroTier、OpenVPN 等) 的詳細比較。



### 社區





- **Reddit**：[r/Tailscale](https://www.reddit.com/r/tailscale/) - 討論、問題與回饋。
- **GitHub**：[github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - 客戶原始碼，在此追蹤開發並報告問題。
- **Discord**：[discord.gg/tailscale](https://discord.gg/tailscale) - 使用者和開發人員的社群。



Tailscale 會定期提供新內容和功能。請參閱其 [官方部落格](https://tailscale.com/blog/) 以取得最新消息與案例研究。