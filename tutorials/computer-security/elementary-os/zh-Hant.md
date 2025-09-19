---
name: Elementary OS
description: Windows 和 MacOS 的理想替代品
---

![cover](assets/cover.webp)



Elementary OS 是基於 Ubuntu 的作業系統，設計簡單、快速、穩定，適合許多日常使用。它是 MacOS 和 Windows 的平衡 Linux 替代品。其流暢、直覺且簡潔的圖形化 Interface 使其易於學習，即使是初學者也不例外。它也著重於人體工學、安全性和效能。



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## 為何選擇 Elementary OS





- **簡單易用**：Elementary OS 的圖形 Interface 介於 MacOs 和 Windows 之間。這種熟悉感讓它即使對於沒有經驗的使用者也很容易上手。





- **安全性**：與大多數 Linux 發行版本一樣，Elementary OS 也受益於高度的安全性。定期更新、權限管理和不存在常見病毒使其成為一個可靠的系統。





- **速度**：Elementary OS 是一個輕量級的發行版。它需要的資源很少，因此速度很快，適合配置不高的電腦使用。





- **免費**：本系統完全免費。不過，當您下載時，您可以捐款支持開發人員。





- **活躍的社區**：Elementary OS 周邊的社群是多樣且回應迅速的。如果您遇到困難，您可以輕鬆地在論壇或社交網路中找到幫助。



## 安裝與設定


### 硬體先決條件



開始安裝前，請確認已配備下列設備：





- 至少 12 GB 的 **USB 鑰匙**
- **RAM** 記憶體至少 4 GB
- 20 GB** 或以上的 **Hard 磁碟，讓您使用更舒適



## 下載 ISO 映像



前往官方作業系統網站 [基本](https://elementary.io/)，選擇一個金額來支持該專案。此步驟可選。


如果您希望免費下載 ISO 映像，請在 **「其他 」** 欄位中輸入 0，然後開始下載系統 ISO 映像。



![0_01](assets/fr/01.webp)



## 建立可開機的 USB 密鑰



下載 ISO 映像後，您需要將其開機到 USB 隨身碟上，才能繼續安裝。



下載 [Balena Etcher](https://etcher.balena.io/) 等軟體或類似的工具，然後啟動軟體。


選擇先前下載的 **Elementary OS** ISO 映像，並將 USB 密鑰設定為目標。



按一下 **flash** 按鈕以啟動程序，並等待程序完成後再移除 USB 鑰匙。



![0_02](assets/fr/02.webp)



## 按鍵開機與 BIOS 存取



關閉要安裝 Elementary OS 的電腦，然後插上 USB 密鑰。


當您的電腦啟動時，請存取 BIOS (`ESC`、`F9` 或`F11`，視不同品牌而定)，並選擇 USB 隨身碟為開機裝置，然後按下`Enter`以啟動開機程序。



## 安裝初級作業系統



如果 USB 密鑰設定正確，安裝會自動開始。



### 語言選擇



選擇要安裝系統的語言。您也可以選擇區域變體。



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### 鍵盤配置



選擇與您的鍵盤相對應的配置。有一個欄位可檢查按鍵是否產生正確的字元。



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### 測試模式



Elementary OS 可讓您在安裝前先測試系統。此模式可讓您探索 Interface，而無需修改 Hard 磁碟上的任何內容。



### 啟動安裝





- 按一下 **「刪除磁碟並安裝」**，直接在整個磁碟上安裝。
- 若要手動管理磁碟分割，請按一下 **「自訂安裝」**。



![0_07](assets/fr/07.webp)



### 光碟選擇



選擇要安裝 Elementary OS 的磁碟，然後按一下「繼續」按鈕。



![0_08](assets/fr/08.webp)



### 磁碟加密



有一個選項允許您加密磁碟，以**保護**您的資料安全。您需要設定強大的密碼才能啟動此保護功能。不過，這是可選的。



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### 啟動安裝



在啟動安裝之前，您可以授權自動安裝額外的硬體驅動程式，這取決於您電腦的相容性。





- 按一下「清除並安裝」開始安裝。
- 等待直到程序完成。



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### 重新啟動



完成後，按一下 **enter** 按鈕重新啟動，然後在適當的時候移除 USB 鑰匙，以避免重新啟動安裝。



![0_13](assets/fr/13.webp)



## 安裝後的設定



重新開機後，需要幾個額外的步驟。



![0_14](assets/fr/14.webp)



### 語言選擇



登入時確認或變更系統語言。



![0_15](assets/fr/15.webp)



### 鍵盤配置



確定鍵盤配置是您想要的配置。



![0_16](assets/fr/05.webp)



### 建立使用者帳號



透過定義使用者名稱，將使用者帳戶與作業系統聯繫起來，然後以至少 20 個字元和符號的字母數字密碼保護資料存取權限。



![0_17](assets/fr/17.webp)



### 第一次連接



當您第一次登入時，Elementary OS 會讓您使用一些基本設定來個人化您的環境。



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## 系統更新



長時間使用前，請務必使用最新的修補程式更新系統。


### 選項 1：透過 Interface 圖形更新



進入 **AppCenter**，然後按一下右上角的更新圖示。等待更新列出，然後按一下 **「Update All」** 開始安裝。



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### 選項 2：透過終端更新



您也可以透過終端機從命令列執行更新：這是一個因其精確性而值得推薦的選項。



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



對於您的第一次更新，作業系統需要您的使用者密碼和確認才能更新軟體套件，即使在 Elementary 核心中也是如此。



## 工作環境配置



Elementary OS 只包含基本工具。為了讓您的環境符合您的需求，特別是如果您是開發人員，我們建議您安裝額外的工具。





- 您可以使用下列指令新增有用的相依性 (依您的需求調整)：



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



此指令會安裝 **Git**、**Python 3**、**pip**、**編譯器工具**、**wget**、**curl**、**zsh**、**make**、**snapd** 及 **vscode**，以準備基本的開發環境。



Elementary OS 已在您的機器上啟動並運行。其簡單、輕巧和優雅的理念使其成為個人和專業使用的絕佳選擇。您將獲得一個穩定、流暢、簡潔的系統，並可根據您的喜好進行自訂。無論是用於開發、辦公室使用或日常瀏覽，一切都已就緒，可建立一個有效率、直覺且愉快的工作環境。也請參考我們關於 Fedora 的教學，這是一個同樣簡單、穩健且模組化的 Linux 發行版。



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0