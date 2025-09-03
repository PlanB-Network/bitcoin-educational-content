---
name: Whonix
description: 保護您的隱私和機密。
---

![cover](assets/cover.webp)



**Whonix**是基於**Debian**的Linux發行版，旨在提供一個結合**安全性**、**匿名性**和**隱私性**的環境。它簡單易學，相容於不同的介面 (虛擬機、Qubes OS、Live mode)，預設包含透過**Tor**進行的網路流量路由、**雙重防火牆** (一個防火牆位於閘道，另一個位於工作站)、**完整的 IP/DNS 洩漏防護**，以及有效遮蔽網路觀察者 (包括您的 ISP) 的活動的工具。不只是匿名系統，**Whonix**更是完整的安全開發環境。



## 為何選擇 Whonix？





- 免費**：和大多數 Linux 發行版一樣，Whonix 是完全免費授權的開放原始碼系統。它以開放原始碼開發，擁有活躍且透明的社群。
- 隱私、安全和匿名** ：Whonix 的主要目標是提供一個超安全的環境，您的所有資料都會受到保護，您的通訊也會透過 Tor 網路加密。
- 易於使用**：Whonix 提供直覺、預設的圖形化 Interface，甚至適合新手使用者。不需要成為專家，也能從進階保護中獲益。
- 安全開發的理想環境**：Whonix 可讓您開發、測試、審計或執行程式，而絕不會洩露您的真實 IP Address，或暴露您的瀏覽或網路通訊習慣。
- 一次性會話與 Live 模式**：Whonix 可以在 Live 模式下啟動，或透過拋棄式機器 (例如透過 **Qubes OS**) 啟動，讓關鍵任務得以執行，而不會在會話結束後留下持續的痕跡。
- 相對簡單的安裝**：提供即用型映像檔，可快速安裝於虛擬機器 (VirtualBox、KVM、Qubes)。系統有文件記錄並會定期更新。



## 安裝與設定



在開始安裝 Whonix 之前，請務必注意這個發行版**尚未正式推出**為可直接安裝在 Hard 磁碟上的主系統（裸機模式）。換句話說，您**還不能將 Whonix 安裝為經典的主機作業系統**，例如 Ubuntu 或標準 Debian。



不過，Whonix 有多個版本可供使用，讓您可以**揮發性**（即時模式、臨時會話）或**持久性**（透過虛擬機器或整合至 Qubes OS）。



若要長期穩定使用，**虛擬化是目前官方唯一推薦的方法**。您可以使用 **VirtualBox**（Whonix-Gateway 和 Whonix-Workstation）執行 Whonix，或者將其整合到像 **Qubes OS** 之類的系統中。在本教程中，我們將專注於 VirtualBox 的安裝。



### 先決條件



在以虛擬模式安裝 Whonix 之前，請確定您的電腦符合最低技術要求。虛擬化需要某些資源，並非所有電腦都能提供。因此，您的處理器必須支援虛擬化技術 (Intel VT-x 或 AMD-V)，並在 BIOS/UEFI 中啟用此選項。



以下是使用 Whonix 順暢穩定體驗的建議規格：





- 隨機存取記憶體 (RAM)**：強烈建議至少 **8 GB**。記憶體越多，分配給虛擬機器 (Gateway 和工作站) 的資源就越多，可提高效能。
- 可用磁碟空間**：請預留至少 30 GB 的可用磁碟空間**。這包括兩個虛擬機、系統檔案和任何資料或快照所需的空間。
- 處理器**：建議使用至少 **4 個實體核心** (8 個邏輯執行緒) 的處理器，尤其是當您想要並行執行其他服務或工具時。



### 下載 Whonix



Whonix 有多個版本，視您要使用的環境類型而定。對於大多數使用者 (Windows、Linux 或 MacOs)，VirtualBox 版本是最容易設定的。您可以直接從 [官方網站](https://www.whonix.org/wiki/VirtualBox) 下載映像檔。



⚠️ Whonix **與使用 Apple Silicon 處理器 (ARM 架構) 的 MacBook 不相容**。



## 安裝 VirtualBox



若要執行 Whonix，您需要 VirtualBox、Qubes 或 KVM 等**管理程序。



下載檔案後，請像安裝其他軟體一樣安裝。接受預設選項，除非您有特殊需求。您迷失了嗎？查看我們的 VirtualBox 使用指南。



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### 匯入 Whonix



安裝 VirtualBox 後，您可以匯入之前下載的 Whonix `.ova` 檔案 (`Whonix-Gateway-Xfce.ova`和`Whonix-Workstation-Xfce.ova`)。



開啟 VirtualBox，然後按一下 ** 檔案 → 匯入裝置**。


選擇相應的 `.ova` 檔案 (從 Gateway 開始)。



![0_03](assets/fr/03.webp)



選擇儲存 Whonix 虛擬機器檔案的位置。



![0_04](assets/fr/04.webp)



接受使用條款，然後啟動匯入，等待程序完成。



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix 配置



在啟動 Whonix 之前，請務必調整一些**系統設定**，以確保效能更佳：



選取 **Whonix-Workstation-Xfce** 虛擬機，然後按一下 ** 設定**。



![0_06](assets/fr/07.webp)



移至**系統**索引標籤，預設 RAM 配置為 2048 MB。我們建議您**將其增加到 4096 MB (4 GB)**，以獲得更高的流暢性，尤其是當您打算開啟多個應用程式或長時間工作時。除非您並行使用大量 Tor 連線，否則 Gateway 可以維持在 2048 MB。



![0_08](assets/fr/08.webp)



### 開始使用 Whonix



為了讓 Whonix 正常且安全地運作，**您必須遵循下列啟動順序** ：



首先，啟動 **Whonix-Gateway-Xfce** 機器。這台機器負責將所有流量路由至 **Tor** 網路。如果沒有執行閘道，任何流量都不會經由 Tor 路由，您也會失去匿名性。



![0_09](assets/fr/09.webp)



一旦 Gateway 完全啟動 (您會看到 Tor 已連線)，您就可以啟動 **Whonix-Workstation-Xfce**，它會自動透過 Gateway 連線。



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### 系統更新



進入終端機，插入下列指令以更新套件清單：



```shell
sudo apt update
```



然後執行下列指令以安裝可用的更新：



```shell
sudo apt full-upgrade
```



## 探索 Whonix



**Whonix** 是一套專為提供**安全**、**匿名**和**保密**運算環境而設計的系統，是您在互聯網上衝浪的理想選擇，且不會洩露您的身分或資料。為了達到這個目標，它隨附了許多有用的日常應用程式，從一開始就能強化您的數位安全性。


### KeepassXC



**KeePassXC** 是 Whonix 的整合式密碼管理器。它可讓您**安全地建立、儲存和管理**您的密碼，而無需手動記住所有密碼。密碼儲存在**加密的資料庫中，並由主密碼保護。



### Tor 瀏覽器



**Tor Browser** 是 Whonix 的預設網頁瀏覽器。它依賴 **Tor** 網路，透過全球多個中繼站重新導向您的流量，幾乎不可能識別您真正的 IP Address。



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### 電子琴 Bitcoin Wallet



**Electrum** 是一個輕巧快速的 Bitcoin Wallet，預先安裝在 Whonix 上，讓您匿名管理**加密貨幣交易。它不會下載整個 Blockchain，而是使用遠端伺服器取得必要的資訊，因此比完整的 Wallet 要輕巧許多。



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix 不只是一個作業系統：它是一個真正的**安全環境**，旨在保護您的匿名性、隱私和敏感活動。由於它以 Tor 為基礎的架構、Gateway 和 Workstation 之間的智慧型分割，以及預先安裝的 Tor Browser、KeePassXC 和 Electrum 等工具，它為任何希望**匿名瀏覽**、**安全工作**或**處理機密資料**的人提供整套解決方案。



若要加強 Unix 系統的安全性，請參閱我們的稽核機器教學：檢查作業系統中的安全漏洞，並確保您的資料不會外洩。



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af