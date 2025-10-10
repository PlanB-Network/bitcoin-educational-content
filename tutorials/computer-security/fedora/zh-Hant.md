---
name: Fedora
description: 為您提供免費、完整且安全工作空間的 Linux 發行版。
---


![cover](assets/cover.webp)





Fedora 是 2003 年推出的免費、開放源碼 Linux 作業系統，由 **Fedora Project** 社群開發，並由 **Red Hat Linux** 提供支援。它以穩定性、良好的效能和易用性而聞名，無論對初學者或進階使用者而言，都是極佳的選擇。該系統可在大多數現代處理器架構上執行，因此幾乎可以輕鬆安裝到任何電腦上。Fedora 也有多種預先設定的版本，稱為「Fedora Spins」或「Fedora Editions」，專為特定需求 (視訊遊戲、天文、開發...) 而設計。



## Fedora Linux 架構



正如您之前所讀到的，Fedora 是基於 Linux 核心的免費作業系統。Linux 核心是作業系統中與電腦硬體通訊及管理系統資源 (如記憶體和處理能力) 的部分。



Fedora Linux 包含在 Linux 核心之上執行作業系統所需的各種軟體工具和應用程式。Fedora 的模組化架構意味著它主要是由個別元件的集合所組成，這些元件可以很容易地依需要新增、移除或更換。這可讓您只使用所需的資源來塑造作業系統。



Fedora 也包含桌面環境，也就是使用者執行任務和存取應用程式的 Interface。Fedora 的預設桌面環境是 GNOME，這是一個友善、易用且高度客製化的桌面環境。



## 為何選擇 Fedora？



在眾多可用的 Linux 發行版中，Fedora 因 .NET 而特別突出：





- 模組化：與不同的處理器架構相容，Fedora 可以安裝在大多數的電腦上，甚至是低功率的電腦，完全符合您的需求。





- 簡單直覺的 **Interface**：Fedora 結合了現代化的圖形化 Interface 與功能強大的命令列 Interface，讓所有設定檔都能輕鬆使用。





- 核心穩定**性**：Fedora 以 Red Hat 為基礎，以更新的可靠性聞名，尤其是核心更新，由於來自大型社群的免費貢獻，因此在執行更新時不會出現重大錯誤。





- 快速、簡易安裝：映像大小僅 3 GB，即使在資源有限的機器上也能**快速簡易安裝**。



## Fedora 版本



根據您的設定和用途，Fedora 提供符合您需求的版本。您主要可以找到.NET版本：





- Fedora 工作站：適合個人及/或專業人士在電腦上使用，此版本安裝了一般公用程式，例如瀏覽器、辦公室套件 (文字編輯器) 及媒體播放軟體。





- Fedora 伺服器**：此版本專門用於伺服器管理。**Fedora Server 包含各種工具，可協助您根據自己的規模部署和管理伺服器。





- **Fedora CoreOS**：想要輕鬆執行與部署雲端應用程式嗎？Fedora CoreOS 就是能讓您使用 Docker 和 Kubernets 等工具來建立和管理映像的版本。



在本教程中，我們將負責 Fedora Workstation 版本。不過，以下詳述的程序對於其他版本也大同小異。



## 安裝和設定 Fedora Workstation



安裝 Fedora Workstation 需要下列硬體配置：




- 至少 **8 GB ** 的 USB 鑰匙，以啟動作業系統。
- 電腦的 Hard 磁碟上至少有 **40 GB 可用空間**。
- **4 GB RAM** 提供流暢體驗。



### 下載 Fedora 工作站



您可以從 Fedora 專案的官方網站下載 [Fedora Workstation] 版本 (https://fedoraproject.org/fr/workstation/download)。然後選擇與您的處理器架構相對應的版本 (32 位元 - 64 位元)，並點選 **下載** 圖示。



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### 建立可開機的 USB 密鑰



若要安裝 Fedora，您需要使用 [Balena Etcher](https://etcher.balena.io/) 等軟體建立可開機的 USB key。



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



完成安裝 Balena Etcher 後，開啟應用程式並選擇下載的 Fedora Workspace ISO 映像。選擇您的 USB 密鑰為目標媒體，然後按一下 **Flash** 按鈕，開始建立可開機的密鑰。



![boot](assets/fr/05.webp)


### 安裝 Fedora



完成啟動 USB 密鑰後，關閉電腦。


開啟電腦，然後在啟動過程中按下 `F2`、`F12` 或 `ESC`鍵 (視您的電腦而定) 存取 BIOS。



在開機選項中，選擇您的 USB 隨身碟作為主要開機裝置。確認此選擇後，您的電腦將會重新啟動，並自動啟動 USB 隨身碟上的 Fedora 安裝程式。



電腦從 USB 隨身碟開機後，會出現 **GRUB** 畫面。



在此階段，您有下列選項：




- 測試媒體：此選項可讓您檢查 USB 隨身碟的完整性，並確保存在正確安裝所需的所有相依性。這是可選的步驟，但如果您對 USB 隨身碟有任何疑問，建議使用此步驟。



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- 啟動 **Fedora**：這會以「即時」模式啟動 Fedora，無需安裝。



在 Fedora 桌面（即時模式）上，點選 ** 安裝 Fedora**（或安裝在 Hard 磁碟上）開始安裝程序。您可以選擇稍後安裝，無須安裝即可測試 Fedora。



![install-live](assets/fr/08.webp)



第一步是選擇 Fedora 的 ** 安裝語言 ** 和 ** 鍵盤配置 **



![language](assets/fr/10.webp)





- 選擇安裝磁碟 ：



選擇要安裝 Fedora 的 Hard 磁碟。



如果磁碟是空的，Fedora 會自動使用所有可用空間。否則，您可以自訂磁碟分割 (手動或自動)。



![disk](assets/fr/11.webp)





- 加密 ：



在這個階段，Fedora 建議加密您的磁碟，以增加額外的 Layer 安全性。這可確保您的資料只能由您的 Fedora 系統讀取。



![chiffrement](assets/fr/12.webp)



在啟動安裝之前，Fedora 會顯示您的選擇摘要。確認後按一下安裝按鈕，開始 Fedora 安裝。



![resume](assets/fr/13.webp)



在安裝過程中，Fedora 會複製檔案並配置系統。完成後，電腦會自動重新開機。



![installation](assets/fr/14.webp)



### 基本設定


第一次使用時，您需要確定一些設定：




- 必要時變更系統語言。



![language](assets/fr/15.webp)





- 選擇符合您喜好的鍵盤配置。



![keyboard](assets/fr/16.webp)





- 在搜尋列中輸入您的城市名稱，選擇您的時區，然後按一下對應的建議。



![timezone](assets/fr/17.webp)





 - 啟用或停用有需要的應用程式存取您的位置，以及自動傳送錯誤報告。



![location](assets/fr/18.webp)





- 決定是否要啟用第三方軟體儲存庫。



![logs](assets/fr/19.webp)





- 輸入您的全名，並定義帳戶的使用者名稱。



![name](assets/fr/20.webp)





- 為您的會話創建一個安全的密碼：盡可能長（至少 20 個字元）、盡可能隨機且包含多種字符（小寫、大寫、數字和符號）。請記得儲存您的密碼。



![mdp](assets/fr/21.webp)



完成所有這些步驟後，啟動 Fedora 並立即開始使用，無需再重新開機。



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



安裝完成後，您可以使用一些預先安裝的公用程式來諮詢 Interface Home。



![install-now](assets/fr/09.webp)



## 探索基本任務



### 瀏覽網際網路


Fedora 的預設瀏覽器是 **Firefox**。它簡單易用，適合大多數的需求。


如果您偏好其他瀏覽器，可以從 ** 軟體管理員** 或透過 ** 終端** 安裝。


### 文字處理


Fedora 預設包含 **LibreOffice** 辦公室套件，提供多種有用的工具：




- **Writer** 用於文字處理。
- **Calc** 用於試算表。
- **Impress** 來建立簡報。


## 安裝應用程式


若要安裝新的應用程式，您可以使用 Fedora 的 ** 軟體管理員** (稱為 _Software_)，它可以讓安裝變得簡單、直觀。  不過，使用 ** 終端** 通常會更快更準確。



在安裝任何軟體之前，請務必記得更新 ** 儲存庫**，以確保您能存取可用的最新版本。



然後使用下列指令啟動所需應用程式的安裝：


sudo dnf install software_name`


## 更新您的作業系統


安裝之後，更新 Fedora 以利用最新的安全修補程式和軟體更新是很重要的。


### 選項 1：透過 Interface 圖形




- 開啟 Fedora **設定**，然後到 ** 系統** 區段。
- 按一下 **軟體更新**。
- 開始下載更新，並等待該過程完成。



安裝更新後，可能需要重新啟動。


### 選項 2：透過終端




- 開啟終端機，首先更新 ** 儲存庫**，以確保您擁有 .NET Framework 的最新版本：



```shell
sudo dnf check-update
```





- 接下來，使用下列指令更新所有已安裝的軟體：



```shell
sudo dnf upgrade
```



現在您的 Fedora 系統已經是最新版本，可以用來處理所有日常工作。探索我們關於另一個 Linux 發行版 Linux Mint 的教學，以及如何為您的 Bitcoin 交易設定一個健康且安全的環境。



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5