---
name: 開始9

description: 建立 Start9 私人伺服器的教學

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*以下是來自 Southern Bitcoiner 的視訊教學，這個視訊指南告訴你如何設定和使用 Start9 / StartOS 個人伺服器，以及如何執行一個 bitcoin 節點*。


## 1️⃣簡介


### Start9 究竟是什麼？


Start9 是一家成立於 2020 年的公司，以開發 [**StartOS**,](https://github.com/Start9Labs/start-os) 一套專為個人伺服器設計、以 Linux 為基礎的作業系統而聞名。它能讓使用者輕鬆地自行託管各種軟體服務 - 例如 Bitcoin 和 Lightning 節點、訊息應用程式或密碼管理員，同時保持對其資料的完全控制，並消除對集中式科技平台的依賴。StartOS 的特色在於友善的瀏覽器介面、用於安裝服務的精選市集，以及內建的隱私權工具，例如 Tor 整合和全系統 HTTPS 加密。Start9 也提供預載 OS 的硬體裝置，不過軟體也可以安裝在相容的硬體或虛擬機器 (VM)。


### 有哪些選項？


Start9 提供預製和 DIY 部署選項。[**Server One**](https://store.start9.com/collections/servers/products/server-one) 和 [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) 是官方硬體設備，採用高效能元件：Server One 使用 **AMD Ryzen 7 5825U** 處理器，搭配可配置的 RAM (16GB-64GB) 和儲存設備 (2TB-4TB NVMe SSD)，而 Server Pure 則配備 **Intel i7-10710U**，同樣提供可配置的 RAM 和儲存設備選項。若直接向 Start9 購買，兩者皆包含**終身技術支援**。對於偏好彈性的使用者，StartOS 可免費安裝在各種現有硬體上，包括筆記型電腦、桌上型電腦、迷你 PC 和單板電腦，或是虛擬機器內。


![image](assets/en/01.webp)


### 與 Umbrel 有何不同？


StartOS 和 Umbrel 都能簡化自助式服務的安裝，但在架構和功能上有所不同。Umbrel 作為 Debian/Ubuntu 系統或虛擬機器上的應用程式層，而 Start9 則是需要直接安裝硬體或虛擬機器的專用作業系統。Umbrel 採用精巧、受 macOS 啟發的介面，而 Start9 則以功能性、簡約設計為優先考量。Umbrel 提供較多的 [應用程式選擇](https://apps.umbrel.com/)，而 [Start9 市集](https://marketplace.start9.com/) 則以先進的技術功能來彌補。Start9 透過有效的 UI 表單簡化進階設定的存取，減少指令列互動的需求。它在備份管理方面也很出色，提供一鍵式加密系統備份，這是 Umbrel 原生缺乏的功能。StartOS 提供內建的監控工具，並針對本機網路存取強制執行 HTTPS 加密，以加強安全性。Umbrel 在本機使用未加密的 HTTP，不過兩個平台都支援透過 Tor 進行安全的遠端存取。Umbrel 適合重視豐富應用程式生態系統和完美使用者介面的使用者。對於重視安全性、可配置性、備份可靠性和進階服務管理而不需要命令列專業知識的使用者來說，Start9 是一個強大的選擇。若要進一步瞭解 Umbrel 以及與 Start9 的差異，請造訪此課程：


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY 先決條件：最低與建議規格


對於使用最少服務的基本用途，**最低規格**為 **1 個 vCPU 核心 (2.0GHz+ boost)、4GB 記憶體、64GB 儲存空間**，以及乙太網路埠。雖然如此，我還是建議您遠遠超過這個標準，尤其是當您正在執行 Bitcoin 節點時。就我個人而言，我一開始使用 1 TB，但很快就用光了。最好的目標是 ** 至少 2 TB 儲存空間**，以及 ** 四核心 CPU (2.5GHz 以上)** 和 ** 8GB 以上 RAM**。這對效能和使用壽命有極大的影響。如果您想深入瞭解，這裡有一個關於 [可執行 StartOS 的硬體](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229) 的最新社群主題。


## 3️⃣下載及更新韌體


要開始設定，請使用另一台電腦造訪 [Start9 網站](https://start9.com/)，點選 `DOCS` 導覽到文件部分。從那裡，進入`Flashing Guides`找到適當版本的StartOS。有兩個選項：



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


本教學涵蓋 `x86/ARM` 選項。


最新的作業系統版本可從 [Github 發佈頁面](https://github.com/Start9Labs/start-os/releases/latest) 下載。也提供 [Pre-release](https://github.com/Start9Labs/start-os/releases) 版本給想要測試新功能的使用者。在頁面底部的 `Assets` 下，下載 `x86_64` 或 `x86_64-nonfree.iso`。  x86_64-nonfree.iso`映像檔包含 Server One 和大多數 DIY 硬體所需的非自由 (封閉原始碼) 軟體，尤其是對於圖形和網路裝置的支援。


建議使用 GitHub 上列出的 SHA256 切細值來檢查檔案的完整性。對於 Linux，可使用指令 `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`，其他作業系統請參閱說明文件。


下載並驗證 StartOS 映像檔之後，必須將其複製到 USB 磁碟機上。BalenaEtcher」是這項任務的推薦軟體。這是一個免費的開放原始碼工具，用來將作業系統映像檔寫入 USB 磁碟機和 SD 卡，適用於 Windows、macOS 和 Linux。從 [Balena Etcher 官方網站](https://www.balena.io/etcher/) 下載適當的版本，並執行安裝程式。連接目標 USB 磁碟機或 SD 卡，開啟 Balena Etcher，點選 `Flash from file` 選擇下載的作業系統映像檔。Etcher 會自動偵測已連接的磁碟機；如果有多個磁碟機，請選擇正確的目標。點選`Flash!`開始寫入映像。完成後，Etcher 會自動驗證寫入過程。完成後，安全地移除硬碟，並用它來啟動裝置。


![image](assets/en/19.webp)


## 4️⃣初始設定


有關初始設定，請參閱 Start9 [documentation](https://docs.start9.com/0.3.5.x/) 頁面下的 `USER MANUAL` 後面的 `Getting Started - Initial Setup`。  最新資訊應參考此官方指南。


提出了兩個選項：



- 重新開始
- 復原選項


若要安裝新伺服器，請選擇「從新開始」。首先，將伺服器連接至電源和乙太網路線。確保用於安裝的電腦位於相同的區域網路上。從電腦移除新刷新的 USB 磁碟機，並將其插入伺服器。


您可以從同一網路中的任何電腦遠端控制伺服器。開啟網頁瀏覽器，並導航至 `http://start.local`。


**註**：如果此地址發生連線問題，通常是由於家庭網路無法解析 `.local` 網域名稱所致。可透過 IP 位址直接存取伺服器來解決問題。登入路由器的管理介面 (通常位於 `192.168.1.1` 或類似的位址)，並在 DHCP 用戶端或網路地圖清單中找到該裝置，即可找到 IP。然後在瀏覽器中輸入完整的 IP 位址 (例如 `http://192.168.1.105`)。這樣可以繞過 DNS 解析。如果問題仍然存在，請參閱 [Common Issues page](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) 或 [reach out to their support.](https://start9.com/contact/)。


StartOS 設定畫面應該會出現。按一下 `Start Fresh` 以開始新伺服器的設定。


![image](assets/en/03.webp)


下一步是選擇儲存 StartOS 資料的儲存磁碟機。


![image](assets/en/04.webp)


為伺服器設定強大的「密碼」。按照 Start9 的建議記錄，然後按一下「完成」。


![image](assets/en/05.webp)


畫面會顯示 StartOS 正在初始化並設定伺服器。下一步是`下載位址資訊`，因為`start.local`位址僅供設定之用，之後將無法使用。


![image](assets/en/06.webp)


組態檔案包含兩個關鍵存取位址：一個用於「本機網路 (LAN)」，另一個用於透過「Tor」進行安全存取。這兩個位址都應該儲存在安全的密碼管理器中。下一步是「信任您的 Root CA」。開啟新的瀏覽器索引標籤，並依照指示信任 Root CA 及登入。您也可以點選下載檔案中的「下載證書」來下載 Root CA 證書。


## 5️⃣信任您的根 CA


下載證書後，伺服器的 `Root CA` 必須受到作業系統的信任。按一下 `View Instructions` 並找到特定作業系統的指引。


![image](assets/en/07.webp)


對於 Linux 系統，會使用下列指令。首先，開啟 Terminal 並安裝必要的套件：


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


導覽到下載證書的目錄，通常是 `~/Downloads` 。執行這些指令以將證書加入 OS 的信任存放區。使用 `cd ~/Downloads` 變更至 downloads 資料夾。使用 `sudo mkdir -p /usr/share/ca-certificates/start9` 建立所需的目錄。複製證書檔案，使用 `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`，並以實際檔案名稱取代 `your-filename.crt`。使用 `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`，將憑證的路徑附加到系統設定，以永久註冊該憑證。最後，使用 `sudo update-ca-certificates` 重建信任儲存。在執行這些指令之前，必須使用實際的憑證檔案名稱並驗證所有路徑。這個過程會為 Start9 伺服器的 HTTPS 連線建立永久信任。


安裝成功後，輸出會顯示 `1 added`。之後，大多數應用程式就可以透過 `https` 安全地連線。如果使用 Firefox，需要額外的 [最後步驟](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff)。若使用 Chrome 或 Brave，則需要不同的 [最後步驟](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome)，以設定瀏覽器尊重 Root CA。刷新頁面，測試連線。如果問題仍然存在，請退出並重新開啟瀏覽器，然後再重新瀏覽該頁面。


![image](assets/en/08.webp)


## 6️⃣開始使用 StartOS


現在應該可以使用安全的 HTTPS 連線登入。輸入「密碼」以存取「歡迎畫面」。


![image](assets/en/09.webp)


此畫面提供入門的實用捷徑。左側側邊欄包含導覽用的主要功能表項目。


## 7️⃣系統


StartOS 中的系統索引標籤可存取管理個人伺服器的核心系統功能。它提供用於系統維護、安全性、診斷和配置的工具，而不需要命令列的專業知識。


備份」區塊允許建立完整的系統備份，包括服務、組態和資料，以便日後還原。這對於災難復原或遷移至新硬體非常重要。備份可儲存於外部磁碟機，並使用主密碼加密。


系統」索引標籤中的「管理」區段允許控制關鍵的系統功能。使用者可以手動檢查和套用 StartOS 更新，維持對系統更新流程的控制。可以側載官方市場上沒有的自訂或第三方服務。如果伺服器未透過乙太網路連線，則可從此區段設定 Wi-Fi 設定。進階使用者可以啟用 SSH 存取，進行終端層級的系統管理。


![image](assets/en/10.webp)


Insights" 部分提供伺服器效能和健康狀況的即時監控，透過圖表顯示 CPU、RAM 和磁碟使用量。它還會顯示系統溫度，這對於 Raspberry Pi 等缺乏主動式冷卻的裝置非常有用。正常運行時間和平均負載指標有助於評估系統的穩定性，而即時日誌可用於排除服務或系統問題。


支援」部分提供內建的常見問題解答、官方文件和社群支援頻道。可從此區下載除錯紀錄，與 Start9 支援分享，以更快地解決問題。


![image](assets/en/11.webp)


## 8️⃣市集


市場」用於發現、安裝和管理個人伺服器上的服務。它提供對 Bitcoin Core、BTCPay Server 和 electrs 等軟體的存取。StartOS支援多個市場，包括官方的Start9註冊表和社群經營的註冊表。這些都可以通過點擊 "CHANGE 「並切換到 」Community Registry "來添加，它提供了對更廣泛服務的訪問。


![image](assets/en/12.webp)


## 9️⃣安裝 Bitcoin Full 節點


在 StartOS 上安裝 Bitcoin full node 可提供對 Bitcoin 體驗的完全主權。它可以驗證交易，並透過消除對可能記錄活動的外部服務的依賴來增強隱私性和安全性。可完全控制交易，允許交易直接廣播至網路。預設選項為「Bitcoin Core」，可與 StartOS 整合，並允許與 Specter、Sparrow 或 Electrum 等錢包連線，進行自我保管設定。另一個選項 `Bitcoin Knots`，也可透過社群註冊處取得。


若要安裝 Bitcoin Core，請導航至 Marketplace。在預設的註冊表下，找到並安裝 Bitcoin Core 服務。安裝完成後，會出現「Needs Config」提示，要求在服務執行前完成設定。這通常會在更新或全新安裝後發生，並提示檢視「RPC 設定」。繼續使用預設設定，然後按一下「儲存」。


![image](assets/en/13.webp)


一旦完全同步，您的節點就可以作為 Sparrow 等錢包的私人後端，提供更強的隱私性和交易驗證。然而，對於儲存大量資金的使用者而言，了解這種直接連線的安全權衡是非常重要的。當 wallet 直接連線至 Bitcoin Core 時，可能會暴露敏感資料，因為 Bitcoin Core 會在主機上未加密地儲存公開金鑰 (xpubs) 和 wallet 結餘。如果系統受到攻擊，攻擊者可能會發現您持有的資金並瞄準您。


為了降低此風險並達到更強大的安全模式，您可以設定一個私人 Electrum Server。此伺服器扮演中介角色，為區塊鏈編制索引，但不儲存任何 wallet 特定的資訊。透過將您的 wallet 連接到自己的 Electrum 伺服器，而非直接連接到 Bitcoin Core，您就可以防止 wallet 存取節點的敏感資料。


![image](assets/en/14.webp)


## 🔟 設定電器


`electrs` (Electrum Rust 伺服器) 是一個快速、有效率的索引器，可連接到您的 Bitcoin 核心節點，讓 Electrum 相容的錢包能即時查詢交易歷史和餘額。透過在 StartOS 上執行 electrs，您可以免除對第三方 Electrum 伺服器的依賴，大幅提升隱私性與安全性-您的 wallet 查詢會直接傳送到您的自行託管節點。


若要設定，請先從 StartOS Marketplace 安裝 electrs 服務。在繼續之前，系統需要 Bitcoin Core 完全同步。安裝完成後，以建議的預設值確認「Needs Config」設定，electrs 就會開始為區塊鏈編制索引，這可能需要一天的時間，視您的硬體而定。


![image](assets/en/15.webp)


完成後，您可以連接 Sparrow 或 Specter 等錢包。連接成功後，您的 wallet 就可以直接與您的節點同步，提供安全、私密且自行託管的 Bitcoin 體驗。


## 1️⃣ 1️⃣連接 Sparrow Wallet


要使用 electrs 實作將 `Sparrow Wallet` 連接到 StartOS 節點，請先確保 Bitcoin Core 已完全同步，且 electrs 已安裝並執行。在您的裝置上開啟 Sparrow Wallet，並導航到 `File` -> `Settings` -> `Server`。然後選擇 `Private Electrum Server`。在 URL 欄位中輸入 electrs 的 `Tor hostname` 和 `Port` ，您可以在 StartOS 中的 `Services` -> `electrs` -> `Properties` 下找到 (通常以 `.onion:50001` 結尾)。


![image](assets/en/16.webp)


接下來，勾選「使用代理」啟用 Tor，將代理位址設定為「127.0.0.1」，連接埠設定為「9050」。按一下 `Test Connection ` 並等待片刻。連線成功會顯示 `Connected to electrs` 等確認訊息。確認後，關閉設定，繼續建立或還原您的 wallet。此設定可確保您的 wallet 透過 electrs 查詢您自己的節點，提供完全隱私和無信賴的操作。


![image](assets/en/17.webp)


## 🎯 結論


StartOS by Start9 是一個人性化、注重隱私的平台，專為自行託管 Bitcoin 和 Lightning 節點、錢包和個人應用程式等必要服務而設計。它提供簡潔的圖形化介面、自動備份、健康監控和安全的 Tor 存取，讓非技術使用者不再需要命令列技能。它的模組化架構支援與 electrs 或 Sparrow 等工具的無縫整合，讓您完全掌控自己的財務與數位主權。StartOS 著重於透明度、本地控制和可擴充性，讓使用者能夠從集中式平台收回所有權，並運作他們自己的私有、彈性基礎架構。