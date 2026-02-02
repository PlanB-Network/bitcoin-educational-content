---
name: Kali
description: 在 VirtualBox 上安裝 Kali Linux、安裝成可開機 USB 隨身碟或雙重開機，一步一步來。
---

![cover-kali](assets/cover.webp)



## 簡介



### 為何選擇 Kali Linux？



**Kali Linux** 是專門用於 IT 安全的 Linux 發行版。


以下是我們使用 Kali Linux 的原因：





- 它預先設定了多種 pentesting 工具 (系統與網路安全測試)。
- 它是 ** 開放原始碼且免費 **，因此您可以自由使用和修改。
- 它**可靠、**安全，是學習網路安全的理想選擇。
- 它可讓您學習如何在可測試的環境中使用 Linux。
- 它可以用不同的方式安裝： ***VirtualBox**、**可開機 USB key**，或**雙重開機**。



## 安裝與設定



### 1.先決條件



**所需設備：**





- 64 位元處理器** (Intel 或 AMD)。
- 最低 8 GB 記憶體** (4 GB 可能足夠輕量安裝或虛擬機器使用)。
- 50 GB 可用磁碟空間** 以安裝 Kali Linux。
- 網際網路連線**，以下載 ISO 映像和更新。
- 至少 8 GB 的 USB 密鑰**，以建立可開機媒體 (如果您要在 PC 上安裝 Kali 或在 Live USB 上測試)。



在現有 PC 上安裝之前，備份資料非常重要。



### 2.下載





- 前往 [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- 為您的應用程式選擇 ISO 映像：
  - 安裝映像**：用於 PC 安裝。
  - 虛擬映像**：在 VirtualBox 或 VMware 上安裝 Kali。
- 下載 ISO 映像。



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3.建立可開機的 USB 密鑰



您可以使用多種工具，例如 Balena Etcher ：





- 下載並安裝 [Balena Etcher](https://etcher.balena.io/)。



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- 開啟 Balena Etcher，然後選擇 Kali ISO 映像。
- 選擇 USB 隨身碟作為目的地媒體。
- 按一下 Flash，等待程序完成。



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4.安裝和保護 Kali Linux



#### 4.1 以 USB 隨身碟開機





- 關閉電腦。
- 插入 USB 密鑰 (內含 Kali Linux)。
- 開啟電腦。在最新的 PC 上，系統應該會自動識別 USB 開機鍵。如果不是這樣，請按住 BIOS/UEFI 存取鍵 (通常是 F2、F12 或 Delete，視品牌而定) 重新開機。
  - 在 BIOS/UEFI 功能表中，選擇 USB 鑰匙作為開機裝置。
  - 儲存並重新啟動。



#### 4.2 啟動安裝



##### 啟動畫面



從 USB 隨身碟開機時，應該會出現 Kali Linux 開機畫面。在 ** 圖形安裝** 和 ** 文字安裝** 之間進行選擇。在本範例中，我們選擇圖形安裝。



![capture](assets/fr/06.webp)



如果您使用 **Live** 映像，您會看到另一種模式 **Live**，這也是預設啟動選項。



![Mode Live](assets/fr/07.webp)



##### 語言選擇



選擇您偏好的安裝和系統語言。



![Sélection de la langue](assets/fr/08.webp)



請註明您的地理位置。



![Options d'accessibilité](assets/fr/09.webp)



##### 鍵盤配置



選擇您的鍵盤配置。可使用測試欄位檢查按鍵是否符合您的配置。



![Configuration du clavier](assets/fr/10.webp)



##### 網路連線



安裝程式現在會掃描您的網路介面，搜尋 DHCP 服務，然後會提示您輸入系統的主機名稱。在下面的示例中，我們輸入 **"kali "** 作為主機名稱。



![Configuration réseau](assets/fr/11.webp)



您可以選擇性地提供本系統將會使用的預設網域名稱 (值可以從 DHCP 擷取，或如果存在預先存在的作業系統)。



![Choix du type d'installation](assets/fr/12.webp)



##### 使用者帳號



接下來，建立系統的使用者帳號 (全名、使用者名稱和強大的密碼)。



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### 時區



選擇您的地理區域以設定系統時間。



![Sélection du fuseau horaire](assets/fr/16.webp)



##### 分割類型



安裝程式會掃描您的磁碟，並根據您的組態顯示多個選項。



在本指南中，我們從**空白磁碟**開始，這樣就有**四種可能的選擇**。


我們要選擇 **Guided - use entire disk**，因為這裡我們要執行 Kali Linux 的一次性安裝 (單次開機)。這表示不會保留其他作業系統，而且可以刪除整個磁碟。



如果您的磁碟已包含資料，可能會顯示額外的選項 ** 導向 - 使用最大的連續可用空間**。



此替代方案可讓您在不刪除現有資料的情況下安裝 Kali Linux，因此非常適合與其他系統進行雙重開機。



在我們的案例中，磁碟是空的，所以沒有出現這個選項。



![Choix du partitionnement](assets/fr/17.webp)



選擇要分割的磁碟。



![capture](assets/fr/18.webp)



根據您的需求，您可以選擇將所有檔案保留在單一磁碟分割中 (預設行為)，或為一個或多個頂層目錄設定獨立的磁碟分割。



如果您不確定自己想要什麼，請選擇 ** 單一磁碟分割中的所有檔案** 選項。



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



在安裝程式進行任何不可逆轉的變更之前，您還有最後一個機會檢查您的磁碟組態。一旦您按下_Continue_，安裝程式便會啟動，而安裝工作也幾乎完成。



![capture](assets/fr/21.webp)



##### 加密的 LVM



如果在上一步中啟用了此選項，Kali Linux 現在會在要求您輸入 LVM 密碼之前執行安全硬碟刪除。



請使用強大的密碼，否則會顯示弱 passphrase 的警告。



##### 代理資訊



Kali Linux 使用儲存庫來散佈應用程式。如果您的環境使用代理，您需要輸入必要的代理資訊。



如果您**不確定**是否要使用代理，請**留空**。輸入虛假資訊將導致無法連線到儲存庫。



![capture](assets/fr/22.webp)



##### Metapets



如果尚未設定網路存取，您需要在出現提示時**進一步設定**。



如果您使用的是 **Live** 影像，則不會顯示下一步。



接下來您可以選擇想要安裝的 [metapackages](https://www.kali.org/docs/general-use/metapackages/)。預設選項會安裝標準的 Kali Linux 系統，所以您不需要修改任何東西。



![capture](assets/fr/23.webp)



#### 啟動資訊



然後確認安裝 GRUB 開機載入程式。



![capture](assets/fr/24.webp)



##### 重新啟動



最後，按一下「繼續」以重新啟動新的 Kali Linux 安裝。



![capture](assets/fr/25.webp)



#### 4.3 安裝後更新和設定 Kali Linux



更新系統是新安裝後的重要步驟。您有兩個選擇：



##### 選項 1：透過圖形使用者介面 (GUI)



Kali 和 Debian/Ubuntu 一樣，提供整合式圖形化更新管理員。



1.按一下 ** 主功能表** (左上方或下方，視您的桌面而定)。


2.開啟 **「軟體更新程式 」**。


3.該工具將 ：




    - 檢查要更新的套件。
    - 您會看到一張清單（包含尺寸和版本）。
    - 允許您按一下即可啟動更新。


4.按提示輸入管理員密碼 (`sudo`)。


5.讓它安裝，必要時重新啟動。



##### 選項 2：透過終端



開啟終端機並執行 ：



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



不建議使用 **root** 帳戶進行日常工作；請建立一個非 root 使用者。



在您的終端機，輸入這些指令：



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



登出並使用新使用者重新登入。



讓我們用表格來總結一些基本的 Kali Linux 任務。



### Kali Linux 下的基本任務




| **類別** | **基礎任務** | **描述 / 目標** | **主要方法** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **系統導航** | 打開終端機 | 訪問 Kali 的主命令行 | 點擊終端機圖標或使用 `Ctrl + Alt + T` |
| | 瀏覽文件夾 | 在系統目錄樹中移動 | `cd /路徑/到/文件夾`，使用 `ls` 列出文件 |
| | 創建 / 刪除文件夾 | 組織文件 | `mkdir 文件夾名`，`rm -r 文件夾名` |
| **文件管理** | 複製 / 移動文件 | 在終端機中操作文件 | `cp 文件 目的地`，`mv 文件 目的地` |
| | 刪除文件 | 釋放磁碟空間 | `rm 文件名` |
| | 顯示文本文件內容 | 快速讀取文件 | `cat 文件.txt`，`less 文件.txt` |
| **系統管理** | 更新 Kali Linux | 安裝最新版本和安全補丁 | `sudo apt update && sudo apt full-upgrade -y` |
| | 安裝軟件 | 添加新工具或實用程序 | `sudo apt install 軟件包名` |
| | 刪除軟件 | 清理系統 | `sudo apt remove 軟件包名` |
| | 清理不需要的依賴 | 節省磁碟空間 | `sudo apt autoremove` |
| **網絡和互聯網** | 檢查網絡連接 | 測試互聯網訪問 | `ping google.com` |
| | 識別 IP 地址 | 了解您的網絡配置 | `ip a` 或 `ifconfig` |
| | 更改 Wi-Fi 網絡 | 連接到另一個接入點 | 網絡圖標 → 選擇所需的 Wi-Fi |
| **帳戶和權限** | 執行管理員命令 | 臨時獲取 root 權限 | `sudo 命令` |
| | 創建新用戶 | 添加本地帳戶 | `sudo adduser 用戶名` |
| | 修改密碼 | 保護帳戶安全 | `passwd` |
| **外觀和舒適度** | 更改壁紙 | 個性化桌面 | 右鍵點擊桌面 → **桌面設置** |
| | 修改主題 / 圖標 | 提高可讀性和美觀性 | 設置 → 外觀 / 主題 |
| **Kali 工具** | 打開工具菜單 | 探索測試和安全工具 | **應用程式 → Kali Linux** 菜單 |
| | 啟動工具（如：nmap, wireshark） | 實際探索安全實用程序 | `sudo nmap`、`wireshark` 等 |
| **幫助和文檔** | 獲取命令幫助 | 在使用前了解命令 | `man 命令` 或 `命令 --help` |

## 總結



安裝 Kali Linux 只是探索這個專門用於網路安全的強大環境的第一步。透過掌握基本任務和系統管理，每個人都可以開始探索內建工具並瞭解 Linux 系統的內部運作。Kali 提供了一個絕佳的學習平台，既能強化技術技能，又能培養真正的 IT 安全文化。