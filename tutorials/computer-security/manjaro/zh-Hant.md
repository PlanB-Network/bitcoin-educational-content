---
name: Manjaro
description: 讓 Arch Linux 的強大功能更易於使用
---
![cover](assets/cover.webp)



Arch Linux 憑藉其強大的穩定性，在許多領域都是廣受歡迎的作業系統。不過，對於新手使用者來說，要上手操作可能會有困難。正是為了 Address 這個問題，**Manjaro** 應運而生：提供 Arch Linux 的強大功能，但以直覺、易學的 Interface 為基礎，提供更簡單、更容易上手的體驗。



## 開始使用 Manjaro



Manjaro 最大的資產之一就是其**簡單且有效率的更新系統。不需要手動管理：Manjaro 會為您處理！當有更新可用時，通知區域（位置依版本而異）中的圖示會提醒您。您所要做的就是依照指示操作，過程快速且毫不費力。



Manjaro 也提供**大量的應用程式目錄**。由於 Manjaro 是以 Arch Linux 為基礎，因此可以直接存取 Arch Linux 的官方套件庫，其中有豐富的軟體，包括專屬應用程式。Manjaro 會稍微延遲一些 Arch Linux 更新，以進行額外的測試；這樣可以提高穩定性，但代價是會稍微延遲新版本的發行。如果這樣的選擇還不夠，您也可以存取 **AUR (*Arch User Repository*)**，這是一個由社群管理的龐大資料庫。如果官方資源庫中沒有某個程式，很可能 AUR 中就有。



Manjaro 的另一個優點是，它對資源的需求**遠低於 Windows 或 macOS 等系統。它消耗較少的 RAM 和運算能力，使其成為較舊或功能較弱電腦的理想選擇：您的機器將增進流暢度和速度，重拾第二次青春。



除此之外，Manjaro 是**完全免費的**。與 Windows 或 macOS 不同的是，您無需支付任何費用即可安裝並獲得最大效益。最後，由於定期、快速的更新，它提供了**增強的安全性**，限制了暴露於漏洞的機會。其活躍的社群也確保任何問題都能快速修正，並提出有效的解決方案。



## 探索 Manjaro OS



在您開始安裝 Manjaro 之前，請務必瞭解此發行版有多種版本。每個版本都提供獨特的桌面環境，影響您的工作流程和系統資源消耗。Manjaro 有三個主要的官方版本。



![0_01](assets/fr/01.webp)





- **KDE Plasma** 版是最可自訂的版本。如果您正在尋找一個視覺上優雅且高效能的系統，KDE Plasma 是一個絕佳的選擇。這個穩定的桌面環境非常適合想要完全控制和量身打造體驗的使用者。





- 對於資源較有限的電腦，**Xfce** 版是理想的解決方案。它的 Interface 既輕巧又直覺，即使在較舊的電腦上也能保證流暢的操作。更重要的是，其佈局讓人聯想到 Windows，讓新使用者更容易過渡到 Linux。





- 最後，**GNOME** 版提供了完全不同的方法。它的流線型設計透過虛擬工作區強調生產力與組織。這種以活動為重點的工作流程，對於已經熟悉 Linux 並正在尋找簡約、高效率環境的使用者來說，特別具有吸引力。



### 其他 Manjaro 版本



![0_02](assets/fr/02.webp)



除了官方版本之外，Manjaro 社群也提供其他版本。這些替代版本旨在滿足特定需求，並提供各種桌面環境。



如果您剛開始使用 Interface，**肉桂**版是您的絕佳選擇。它的設計簡單易用，同時保留了傳統辦公室環境的經典習慣。



對於更進階的使用者，還有一些版本，例如 **i3 Window Manager** 或 **Sway**。這些版本更輕巧、更快速，但仍需要精通命令列才能完全設定和使用。這些環境非常適合想要完全控制系統、且將效率放在首位的使用者。



## 技術要求



為了讓 Manjaro 最佳運作，您的電腦必須符合幾項最低需求。我們建議您至少要有 .NET Framework 2.0 或以上：





- 64 位元 (x86_64)** 處理器
- 建議使用 4 GB RAM (最低 2 GB)** (請參閱下文)
- 30 GB 的磁碟空間 (如果您建立專屬的 `/home` 磁碟分割，空間會更大)**



## 安裝 Manjaro



若要下載，請前往 [Manjaro 官方網站](https://manjaro.org/)，選擇最適合您需求的版本。下載檔案後，您需要使用 Manjaro ISO 映像建立可開機的 USB 密鑰。



然後前往 [Rufus] 軟體網站 (https://rufus.ie/fr/) 下載。執行程式，插入您的 USB 密鑰，選擇 Manjaro ISO 映像並開始閃存。在移除鑰匙之前，請等待程序完成。然後您就可以重新啟動電腦。



![0_03](assets/fr/03.webp)



要在電腦上安裝 Manjaro，首先要完全關機。然後插上 USB key，重新開機，並按 **F2、F10、F12、Escape** 或 **Delete**（視製造商而定）來存取開機選單或 UEFI/BIOS 韌體。



然後選擇 USB key 作為開機裝置，開始作業系統安裝程序。



### 啟動畫面



第一次從 USB key 啟動 Manjaro 時，會直接進入安裝選單。在啟動安裝之前，您可以變更鍵盤配置或系統語言。



然後選擇 ** 使用開放原始碼驅動程式開機** 選項，開始安裝 Manjaro。這些開放原始碼驅動程式與大多數硬體相容，在大多數情況下足以應付需求。例如，如果您有 NVIDIA 顯示卡，或需要更高的顯示卡效能，您可以選擇 ** 使用專屬驅動程式**開機，這會使用專屬驅動程式。



![0_04](assets/fr/04.webp)



系統將以 ** 預設的 Live 模式**啟動。這可讓您在永久安裝之前測試 Manjaro 的功能，看看它是否符合您的需求。準備就緒後，按一下 ** 安裝 Manjaro Linux** 選項。



選擇安裝時所需的語言，然後按一下 **下一步**。



![0_06](assets/fr/06.webp)



然後選擇您的位置，設定正確的時區。在此階段，您也可以變更語言和日期格式。



![0_07](assets/fr/07.webp)



選擇鍵盤配置。可使用測試欄位檢查輸入的按鍵是否符合預期的字元。



![0_08](assets/fr/08.webp)



### 磁碟分割


您有兩個磁碟分割選項。





- 第一，也是最簡單的，就是刪除整個磁碟，然後在上面安裝 Manjaro。
- 第二種允許**手動分割**。



![0_09](assets/fr/09.webp)



若要進行乾淨的安裝，我們建議至少建立三個磁碟分割：





- 第一個磁碟分割為 **516MB**（主磁碟分割），用於**boot**。
- 第二個 **2GB**（邏輯）磁碟分割用於 **交換**。
- 第三個磁碟分割存放您的**個人資料。



如果您希望同時安裝其他系統，您需要分割最後一個磁碟分割，並只分配一部分給 Manjaro (至少 **15 GB** 以確保系統正常運作)。


### 建立使用者帳號



填寫必要資訊，在系統上建立使用者帳戶。最後，設定管理員的密碼 (**root**)。此管理員為**超級使用者**，擁有系統上的全部權限，並能執行進階指令。



![0_10](assets/fr/10.webp)



### 選擇合適的辦公室套件



Manjaro 可讓您在 **FreeOffice** 和 **LibreOffice** 之間進行選擇。





- LibreOffice** 更為完整，擁有更多軟體和進階功能。
- 另一方面，FreeOffice** 較為輕巧，只包含基本的功能： **TextMaker**、PlanMaker** 和 Presentations**。



![0_11](assets/fr/11.webp)



### 組態摘要



摘要畫面會顯示您設定的所有參數。如有必要，您可以返回進行變更，而不會影響您已進行的其他設定。



然後按一下 **安裝**，並確認以開始實際安裝。



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### 安裝結束



在程序結束時，勾選 ** 立即重新啟動** 方塊，然後按一下 **完成**。系統將會重新啟動，**Manjaro 即可開始使用**。



![0_13](assets/fr/14.webp)



## 使用 Manjaro 的第一步



安裝 Manjaro 只是第一步。為了讓您的系統發揮最大效用，以下是一些有用的知識。



### 更新系統



Manjaro 大幅簡化更新程序。要更新您的套件 ：



```shell
sudo pacman -Syu
```



此指令會下載並安裝可用的最新版本。我們建議您定期執行，以保持系統的**安全與穩定。



### 設定開發環境



要在 Manjaro 上開發 Web 應用程式，只需在單一指令中安裝必要的工具：



```shell
sudo pacman -S nodejs npm git yarn
```



此指令會安裝 Node.js 和 npm 來執行和管理 JavaScript 與 TypeScript 專案，安裝 Git 來進行版本管理，並安裝 Yarn 作為替代的套件管理員。



### 安裝 Bitcoin Wallet



要在 Manjaro 上管理您的 bitcoins，您可以安裝 **Electrum**，一個輕量且安全的 Wallet .NET Framework：



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum 讓您**輕鬆地接收和發送比特幣，同時提供多個 Wallet 管理和 passphrase 保護等先進功能。如需完整的 Electrum 使用指南，請查看我們的專門教程，其中解釋了如何創建 Wallet、保護您的資金安全以及進行交易。



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## 保護您的 Manjaro 系統



安全性是任何 Linux 安裝的重要一環。保護資料的機密性和完整性對您來說非常重要。



### 防火牆設定



Manjaro 包含 UFW (*Uncomplicated Firewall*)，這是一個管理網路過濾防火牆的程式，但您必須手動啟動它：



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### 管理使用者權限



1. **建立一個非授權使用者**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Sudoers 檔案設定**



```shell
sudo EDITOR=nano visudo
```



現在您已準備好在您的機器上使用 Manjaro Linux。由於其**簡單的安裝**、**容易的更新**以及**彈性**，您將擁有一個強大、高效能的系統，適合開發、日常使用以及使用 Electrum 等工具管理您的比特幣。



Manjaro 結合了**穩定性、速度和安全性**，同時保持**完全免費**，使其成為初學者和進階使用者的理想選擇。花點時間探索它的各種功能，自訂符合您需求的環境。如果您想要更多的專業知識並探索 Arch Linux 系統，強烈建議您參考我們的教學。



https://planb.network/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973