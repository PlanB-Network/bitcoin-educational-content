---
name: Pop!_OS
description: Linux 發行版 Pop!_OS 安裝指南
---

![cover](assets/cover.webp)



## 簡介



Pop!OS 是由**System76**所開發的以 Linux 為基礎的作業系統，System76**是一家美國製造商，專門為開發人員、設計師和進階使用者製造機器。



Pop!OS 旨在提供現代、穩定、高效能的環境，其特色在於簡單的體驗、強大的工具以及對生產力的高度重視。



### 誰是 System76？



System76 是一家成立於 2005 年的美國公司，總部設在丹佛，專門製造專為 Linux 設計的筆記型電腦、桌上型電腦和伺服器。



與傳統製造商不同的是，System76 所開發的機器設計為開放式、可維修且以軟體自由度為導向。



System76 不僅製造電腦。



該公司還開發了.NET技術：




- Pop！OS**，它自己的 Linux 作業系統；
- COSMIC** 是 Pop!OS .NET 所使用的現代化高效能桌面環境；
- Open Firmware**，基於 Coreboot 的開放原始碼韌體；
- 開發人員和設計人員的工具。



其目的是提供高品質的硬體與軟體整合，可媲美 Apple 的生態系統，但完全開放且以 Linux 為中心。



## 現代化、穩定且容易存取的系統



Pop!OS 建立在 Ubuntu 的基礎上，使其具有優異的穩定性、廣泛的硬體相容性，並可存取龐大的軟體生態系統。


它提供了優雅的介面，即 COSMIC 桌面，設計流暢、直觀且可自訂，即使是新使用者也能輕鬆使用。



## 開發人員、設計師和要求嚴格的使用者的理想選擇



Pop！OS 特別受到 .NET 和 .NET 人士的喜愛：





- 開發人員（預載工具、進階平鋪管理）、
- 使用 Nvidia 或 AMD 顯示卡的使用者、
- 尋找可靠系統的學生和專業人士、
- 希望進行簡單轉換的 Windows 使用者。



它包括自動平鋪、清晰的軟體中心和整合的生產力工具，讓日常使用更輕鬆。



## Pop！OS 亮點





- 優化的效能**歸功於定期更新。
- 提供兩個 ISO 版本**：標準與 Nvidia 最佳化。
- 增強安全性** (安裝時提供 LUKS 加密功能)。
- Interface COSMIC** 符合人體工學，現代感十足。
- 與 Ubuntu 及 Flatpak 軟體高度相容**。



## 安全下載 POP!



### 1.先決條件



在下載並安裝 POP!OS 之前，您需要做幾件事來正確準備安裝環境。



### 所需設備





- 一台相容的電腦**：Intel 或 AMD 處理器、Intel / AMD / Nvidia GPU。
- 至少 4 GB 記憶體** (建議使用 8 GB 記憶體，才能舒適使用)。
- 最少 20 GB 可用空間** (建議 40 GB 或以上)。
- 至少 4 GB 的 USB 密鑰**，以建立安裝媒體。



### 網際網路連線



穩定的連線對 ：





- 下載 ISO 映像、
- 安裝更新後。



Pop!OS 可以在沒有連線的情況下執行，但在網際網路上安裝會更順暢。



### 資料備份



如果 Pop!OS 要取代其他系統 (Windows、Ubuntu 等) 或與其他系統共存，建議在進行之前先備份重要檔案。



### 檢查是否有 Nvidia GPU（如適用）



對於配備 Nvidia 顯示卡的電腦，您需要下載包含 Nvidia 驅動程式的特殊 ISO 映像。


這項檢查非常簡單：





- 請參閱 PC 規格、
- 或在系統設定中查詢顯示卡型號。



### 從官方網站下載



Pop！OS的ISO映像檔應直接從System76官方網頁下載：[system76.com/pop](https://system76.com/pop/).



本頁面始終提供最新版本，適合您的硬體。



![capture](assets/fr/03.webp)



### 選擇版本：標準或 Nvidia，或 Raspberry Pi (ARM64)



Pop!OS 有三種版本：



### 標準版本



建議使用 ：





- intel 或 AMD 處理器；
- 整合式 Intel 或 AMD GPU；
- AMD Radeon 顯示卡。



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia 版本



建議使用配備 Nvidia 顯示卡的電腦。


此映像檔已包含 Nvidia 驅動程式，讓安裝更容易，並減少顯示卡問題。



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Raspberry Pi 版本 (ARM64)



適用於 Raspberry Pi 4 和 400 (ARM 處理器)。


適用於 ARM 架構，是這些迷你電腦的專用版本。



![Utilisation de Balena Etcher](assets/fr/06.webp)



## 建立可開機的 USB 密鑰



您可以使用多種工具，例如 Balena Etcher ：





- 下載並安裝 [Balena Etcher](https://etcher.balena.io/)。



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- 開啟 Balena Etcher，然後選擇 Pop!OS ISO 映像。
- 選擇 USB 隨身碟作為目的地媒體。
- 按一下 Flash，等待程序完成。



![Utilisation de Balena Etcher](assets/fr/09.webp)



## 安裝及保護 Pop!OS



### 從 USB 隨身碟開機





- 關閉電腦。
- 插入 USB 密鑰 (內含 Pop!OS).
- 開啟電腦。在最新的 PC 上，系統應該會自動識別 USB 開機鍵。如果不是這樣，請按住 BIOS/UEFI 存取鍵 (通常是 F2、F12 或 Delete，視品牌而定) 重新開機。
  - 在 BIOS/UEFI 功能表中，選擇 USB 鑰匙作為開機裝置。
  - 儲存並重新啟動。



### 啟動安裝



選擇可開機 USB 隨身碟作為啟動裝置後，電腦就會開機進入 Pop!OS Live 環境。



選擇您的語言。



![Capture](assets/fr/10.webp)



選擇位置。



![Capture](assets/fr/11.webp)



選取鍵盤輸入語言。



![Capture](assets/fr/12.webp)



選取鍵盤配置。



![Capture](assets/fr/13.webp)



選擇「Clean Install」選項進行標準安裝。這是新 Linux 使用者的最佳選擇，但請注意這會刪除目標磁碟機的所有內容。或者，您可以選擇`Try Demo Mode`，繼續在實際環境中測試 Pop!OS 。



![Capture](assets/fr/14.webp)



選擇「自訂 (進階)」以存取 GParted。此工具可讓您設定進階功能，例如雙重開機、建立獨立的 `/home` 磁碟分割，或將 `/tmp` 磁碟分割置於不同的磁碟機上。



按一下「刪除並安裝」，將 Pop!OS 安裝在選取的磁碟機上。



![Capture](assets/fr/15.webp)



### 使用者帳號設定



安裝程式的下一節將引導您建立使用者帳戶，以便您可以登入新的作業系統。



提供全名（可包括您選擇的任何文字，大寫或小寫），以及使用者名稱（必須為小寫）：



![Capture](assets/fr/16.webp)



建立帳戶後，系統會提示您設定新密碼。



![Capture](assets/fr/17.webp)



### 全磁碟加密



系統磁碟加密並非必要，但可在有人未經授權實體存取裝置時，保證使用者資料的安全性。



勾選 `加密密碼與使用者帳號密碼相同`，即可使用您的登入密碼為磁碟機加密。您也可以取消勾選此方塊，然後選擇底部的 ` 設定密碼 `。選取 `Don't Encrypt` 可忽略磁碟加密程序。



![Capture](assets/fr/18.webp)



如果您選擇「設定密碼」按鈕，您會看到一個額外的提示來設定您的加密密碼。



進入安裝程式的下一步。現在 Pop!OS 將開始在磁碟上安裝。



![Capture](assets/fr/19.webp)



安裝完成後，請重新啟動電腦並登入以完成使用者帳戶設定程序。



如果您已更改開機順序，在啟動時優先啟動 Live USB 密鑰，請完全關閉電腦，並移除安裝 USB 密鑰。如果您處於雙重開機模式，請按適當的按鍵存取設定，並選擇包含 Pop!OS 安裝的磁碟機。



![Capture](assets/fr/20.webp)



### NVIDIA 顯示卡



如果您從 Intel/AMD ISO 安裝，而您的系統有獨立的 NVIDIA 顯示卡，或您在較後時間新增了顯示卡，您需要手動安裝顯示卡的驅動程式，以達到最佳效能。在命令終端執行以下命令來安裝驅動程式：



```bash
sudo apt install system76-driver-nvidia
```



您也可以從 Pop!_Shop 安裝 NVIDIA 顯示卡驅動程式。



![Capture](assets/fr/20.webp)



## 安裝必要工具



Pop！OS透過其Pop！Shop提供廣泛的軟體，但許多必要的工具也可以透過終端機使用`apt`或`flatpak`安裝。以下是如何為完整的工作環境安裝主要工具。



### 終端安裝



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### 透過 Pop.Shop 安裝Shop (圖形介面)





- 從主功能表開啟 **Pop!
- 使用搜尋列尋找您想要的應用程式 (例如「Brave」)。
- 按一下每個應用程式的 ** 安裝**。
- Pop!_Shop 會自動管理相依性和更新。



## 系統更新



### 選項 1：透過圖形使用者介面 (GUI)



Pop!OS 具有簡單、直覺的圖形化更新管理器。



1.按一下 **主功能表**（圖示左下方）。


2.開啟 **"Pop！_Shop "**。


3.在 Pop!_Shop 中，按一下 **「更新」** 標籤。


4.系統會自動檢查可用的更新。


5.按一下 **「全部更新」** 開始安裝更新。


6.如果需要，請輸入您的密碼。


7.讓程序結束，必要時再重新啟動。



### 選項 2：透過終端



開啟終端機並輸入 ：



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### 使用者管理



我們建議使用具有 sudo 權限的標準使用者帳戶進行日常操作。



若要建立新使用者 ：



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



登出，然後用這個新使用者重新登入。



### 顯示卡驅動程式管理





- 對於 Nvidia 顯示卡，請檢查是否已安裝專屬驅動程式：



```bash
sudo apt install system76-driver-nvidia
```





- 對於 AMD/Intel，驅動程式通常預設已包含在內。



### 啟動防火牆 (UFW)



Pop!OS 預設不封鎖網路流量。啟動 UFW 以加強安全性：



```bash
sudo ufw enable && sudo ufw status verbose
```



### 設定自動更新



保持系統更新，無需手動介入：



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### 自訂外觀與行為





- 開啟 ** 系統設定** → ** 外觀**，選擇淺色或深色主題。
- 透過 COSMIC 管理員設定活動角落、動畫和延伸功能。
- 調整桌面佈局以最佳化工作流程。



### 設定自動備份



Pop!OS 整合了 Deja Dup 等工具來進行備份：





- 從功能表啟動 **備份**。
- 選擇外部磁碟機或網路位置。
- 排定定期備份。



### 安裝有用的 GNOME/COSMIC 擴充套件



以下是一些可提升使用者體驗的建議擴充套件：





- Dash to Dock**：應用程式列永遠可見。
- GSConnect**：與 Android 同步處理。
- 剪貼板指示器**：進階剪貼板管理。



透過 .NET 安裝



```bash
sudo apt install gnome-shell-extensions
```



然後在設定中啟動它們。



### 最佳化記憶體與交換管理



檢查您的交換狀態：



```bash
swapon --show
```



如有必要，請增加交換大小或設定交換檔案 ：



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



將它新增至 `/etc/fstab` 檔案，以便自動掛載。



## 套件與儲存庫管理



### 瞭解套件來源



Pop!OS 基於 Ubuntu，主要使用 .NET Framework：





- 官方 Ubuntu** 儲存庫：用於大部分穩定的軟體。
- System76** 套件庫：用於驅動程式、韌體和特定工具。
- Flatpak**：存取廣泛的沙盒應用程式。
- Snap** (選用)：另一種通用套件格式。



---

### 新增和管理 PPA 套件庫



若要安裝經常更新的軟體，可以新增某些 PPA (Personal Package Archives，個人套件存檔)：



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## 總結



Pop!OS 是現代、穩定的 Linux 發行版，適合初學者和進階使用者。



由於其直覺的 COSMIC 介面和整合工具，無論是開發、創作或日常使用，都能提供流暢且具生產力的體驗。



本教程涵蓋主要階段：準備、下載、安裝、初始設定和必要工具。



歡迎您進一步探索 Pop!OS 並自訂您的環境，以充分發揮它的功能。