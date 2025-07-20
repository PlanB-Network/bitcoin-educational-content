---
name: 虛擬主機
description: 在 Windows 11 上安裝 VirtualBox 並建立第一台虛擬機器
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian Burnel 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___




## I.簡報



在本教程中，我們將學習如何在 Windows 11 上安裝 VirtualBox 以建立虛擬機器，無論是執行 Windows 10、Windows 11、Windows Server 或 Linux 發行版 (Debian、Ubuntu、Kali Linux 等)。



這篇 VirtualBox 入門教學將幫助您開始使用這個由 Oracle 開發的開放原始碼虛擬化解決方案，而且完全免費。稍後，我們會將其他教學放到線上，帶您深入瞭解這個主題。



說到虛擬化工作站，無論是作為專案的一部分進行測試，或是在 IT 學習期間，VirtualBox 顯然都是很好的解決方案。它也是其他解決方案的替代方案，例如整合在 Windows 10 和 Windows 11 (以及 Windows Server) 中的 Hyper-V，以及 VMware Workstation (收費) / VMware Workstation Player (個人使用免費)。



我的配置： **一台 Windows 11 工作站，我要在其中安裝 VirtualBox**，但您可以在 Windows 10（或舊版本）以及 Linux 上安裝 VirtualBox。就虛擬機器而言，VirtualBox 支援多種系統，包括 Windows (例如 Windows 10、Windows 11、Windows Server 2022 等)、Linux (Debian、Rocky Linux、Ubuntu、Fedora 等)、BSD (PfSense) 和 macOS。



## II.下載 VirtualBox for Windows 11



要下載 VirtualBox 安裝在 Windows 機器上，只有一個好的 Address：[VirtualBox 官方網站](https://www.virtualbox.org/wiki/Downloads) 的「**Downloads**」部分。只要點選「Windows 主機」，就可以開始下載這個執行檔，它的大小剛好超過 100 MB。



![Image](assets/fr/025.webp)



## III.在 Windows 11 上安裝 VirtualBox



### A.安裝 VirtualBox



安裝 VirtualBox** 非常簡單，而且所有 Windows 版本的安裝程序都相同。首先啟動剛下載的 VirtualBox 可執行檔，然後按一下「**下一步**」。



![Image](assets/fr/026.webp)



此安裝可自訂，但我建議您安裝所有功能：預設選項即是如此。在下面的圖片中，您可以看到各種 Elements，包括 .NET 和 .NET Framework：





- VirtualBox USB 支援** 可讓 VirtualBox 支援 USB 裝置
- VirtualBox 橋接網路** 以「橋接」模式整合網路支援 (虛擬機器可直接連接到您的本機網路)
- VirtualBox Host-Only Network** 以「Host-Only」模式整合網路支援 (在此模式下，虛擬機器只能與 Windows 11 實體主機和其他虛擬機器通訊)



按一下「**下一步**」繼續。



![Image](assets/fr/001.webp)



按一下「**是**」，請記住**網路會在您的 Windows 11 機器上中斷片刻**，VirtualBox 會進行網路修改以支援不同的網路類型，包括網橋模式。



![Image](assets/fr/002.webp)



確認後，安裝就會開始...然後會出現「**您要安裝此裝置軟體嗎？**」通知。勾選「**Always trust software from Oracle Corporation**」選項，然後按下「**Install**」。VirtualBox 實際上需要在您的電腦上安裝幾個驅動程式。



![Image](assets/fr/003.webp)



安裝至此完成！勾選「**安裝後啟動 Oracle VM VirtualBox 6.1.34**」選項，然後按「**點擊**」啟動軟體。



![Image](assets/fr/004.webp)



### B.新增擴充套件



您仍可在 VirtualBox 官方網站 (請參閱之前的連結)，點選「**所有支援的平台**」連結，即可在「**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**」區段下載官方擴充套件。此套件可讓您在 VirtualBox 中加入額外功能：並非必須加入，但可能很有用！例如，它包括在虛擬機器中支援 USB 3.0、支援網路攝影機和磁碟加密。



開啟 VirtualBox，按一下功能表中的「**檔案**」，然後按一下「**設定**」。



![Image](assets/fr/005.webp)



按一下左邊的「**擴充套件**」(1)，然後按一下右邊的「**+**」按鈕 (2)，以**載入您剛下載的 VirtualBox*** 擴充套件 (3)。



![Image](assets/fr/006.webp)



按一下「**安裝**」按鈕確認。



![Image](assets/fr/007.webp)



按一下「**OK**」：正式的擴充套件現在已安裝在您的 VirtualBox 虛擬主機上！



![Image](assets/fr/008.webp)



讓我們繼續建立第一台虛擬機器。



## IV.建立您的第一個 VirtualBox 虛擬機器



若要在 VirtualBox 上建立新的虛擬機器，只需按一下「**新**」按鈕，即可啟動虛擬機器建立精靈。由於這是您第一次啟動 VirtualBox，我想再為您介紹一下 Interface 和其他按鈕的細節。





- 設定**：一般 VirtualBox 設定 (預設 VM 資料夾、更新管理、語言、NAT 網路、擴充功能等)
- 匯入**：以 OVF 格式匯入虛擬裝置
- 匯出**：以 OVF 格式匯出現有虛擬機器，以建立虛擬裝置
- 新增**：以標準 VirtualBox 格式 (.vbox)或 XML 格式，新增現有的虛擬機器到您的 VirtualBox 庫存中



在左側，「**工具**」部分可存取**進階功能，主要用於管理虛擬網路，但也用於管理虛擬機器儲存**。在 「**工具**」項目下，稍後將新增您的虛擬機器。



![Image](assets/fr/009.webp)



### A.虛擬機器建立程序



**提醒一下，VirtualBox 支援多種作業系統，包括 Windows、Linux 和 BSD。在這個範例中，我要建立 Windows 11 的虛擬機。有幾個欄位需要填寫：





- Name**：虛擬機器名稱（這是將會顯示在 VirtualBox 中的名稱）
- 機器資料夾**：存放虛擬機器的位置，知道在此位置會建立以虛擬機器名稱命名的子資料夾
- Type**：作業系統類型，視您要安裝的作業系統而定
- Version**：您希望安裝的系統版本，在本例中為 Windows 11，因此為 "**Windows11_64**"



按一下「**下一步**」繼續。



![Image](assets/fr/010.webp)



根據您在上一步選擇的作業系統，**VirtualBox 會建議分配給虛擬機器的資源**。這裡，我們討論的是您希望分配給虛擬機器的 RAM。我們假設 4 GB，因為 Windows 11 建議使用 4 GB，但如果您的資源不足，請指定 2 GB。 **繼續



**註**： 稍後可以修改分配給虛擬機器的資源。



![Image](assets/fr/011.webp)



就虛擬 Hard 磁碟而言，我們是從零開始，因此需要選擇「**立即建立虛擬 Hard 磁碟**」，讓虛擬機器有儲存空間來安裝作業系統和儲存資料。按一下「**建立**」。



![Image](assets/fr/012.webp)



VirtualBox 支援三種不同格式的虛擬 Hard 磁碟，與其他解決方案 (如 VMware 和 Hyper-V) 相比，這是一大差異。有三種格式可供選擇：





- VDI**, 官方 VirtualBox 格式
- VHD**，這是官方的 Hyper-V 格式，雖然最近較常使用新的 VHDX 格式
- VMDX** 是 VMware Workstation 和 VMware ESXi 的官方 VMware 格式。



若要建立僅用於此 VirtualBox 虛擬機器，請選擇「**VDI**」。另一方面，如果虛擬 Hard 磁碟稍後要連接至 Hyper-V 主機，則一開始就使用 VHD 格式可能是個好主意，可避免轉換。按一下「**下一步**」。



![Image](assets/fr/013.webp)



**虛擬磁碟可以是動態或固定大小**。當它是動態時，代表**虛擬磁碟的檔案 (這裡是 .vdi 檔案) 會隨著資料寫入磁碟而增加**，直到達到最大大小為止，但如果刪除資料，它不會縮小。相反地，當它是固定大小時，**總儲存空間會立即分配（因此會保留）**，這會讓效能稍高，但在首次建立虛擬磁碟時需要較長時間。



就個人而言，使用 VirtualBox 測試虛擬機器時，我認為「**動態分配**」模式已經足夠。



![Image](assets/fr/014.webp)



**下一步是指定虛擬磁碟的大小**，請注意預設磁碟將儲存在虛擬機器目錄中（可在此階段變更）。為符合 Windows 11 的要求，我指定了 64 GB 的大小，但也可以指定較小的大小。按一下「**建立**」以建立虛擬機器！



![Image](assets/fr/015.webp)



此時，虛擬機器已在我們的庫存中，並已設定，但作業系統尚未安裝。在啟動虛擬機器之前，我們需要完成虛擬機器的設定。



### B.將 ISO 映像指定給 VirtualBox 虛擬機器



要安裝 Windows 11 或任何其他系統，我們需要安裝來源。在大多數情況下，我們會使用 ISO 格式的磁碟影像來安裝作業系統。 **有必要將 Windows 11 ISO 映像載入虛擬機器的虛擬 DVD 光碟機中



按一下 VirtualBox 庫存中的虛擬機器 (1)，然後按一下「**設定**」按鈕 (2)，即可存取此虛擬機器的一般設定。此功能表用於管理資源 (例如增加 RAM、設定 CPU 等)。按一下左側的 「**儲存**」（3），在 DVD 光碟機上暫時顯示 「**空**」（4），然後按一下 DVD 形狀的圖示（5）和 「**選擇磁碟檔案**」。



![Image](assets/fr/016.webp)



選擇要安裝的作業系統的 ISO 映像，然後按一下確定。這就是我得到的結果：



![Image](assets/fr/017.webp)



請留在虛擬機器的「**設定**」部分，我還有一些事情要說明。



### C.VM 網路連線



移至左側的「**網路**」區段。此部分可讓您管理虛擬機的網路：虛擬網路介面的數量 (每個虛擬機最多 4 個)、MAC Address 和網路存取模式 (NAT、橋接存取、內部網路等)。 **如果您想讓虛擬機器存取網際網路，請選擇「NAT」或「橋接存取」**，但這第二種模式需要 DHCP 伺服器在您的網路上啟用，否則您必須手動設定 IP Address。



注意：我會在專題文章中再詳細討論網路部分。



![Image](assets/fr/018.webp)



### D.虛擬處理器的數量



就像實體電腦一樣，虛擬機器需要 RAM、Hard 磁碟和處理器才能運作。當我們建立虛擬機器時，您可能已經注意到精靈並不包括處理器的設定。但是，您可以隨時透過「**系統**」索引標籤，然後是「**處理器**」來設定，在這裡您可以選擇虛擬處理器的數量。



注意：巢狀虛擬化需要「**啟用 VT-x/AMD-v 嵌套**」選項。



在我的情況下，虛擬機器有 2 個虛擬處理器：



![Image](assets/fr/019.webp)



**不要猶豫，看看設定選單的其他部分。



### E.首次開機與作業系統安裝



若要啟動虛擬機器，只需在清單中選取該虛擬機器，然後按一下「**Start**」按鈕。第二個視窗將會開啟，提供虛擬機器的視覺概觀。



![Image](assets/fr/020.webp)



哎呦，我收到一個令人討厭的錯誤，我的虛擬機器無法啟動！錯誤是「虛擬機器登入失敗...」，詳細資訊如下：



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



事實上，這是正常現象，因為 ** 我的電腦未啟用虛擬化功能！要糾正這個問題，您需要重新啟動電腦，存取 BIOS 並啟用虛擬化功能。



![Image](assets/fr/021.webp)



不用等待，我重新啟動電腦，**按下「SUPPR」鍵存取華碩主機板的 BIOS**（鍵值可能因機器而異，例如可能是 F2）。要啟動虛擬化，在我的情況下必須啟用「SVM 模式」。同樣地，不同的主機板、不同的製造商，名稱也可能會改變。請尋找**AMD-V** (針對 AMD CPU) 或**Intel VT-x** (針對 Intel CPU) 的功能。



![Image](assets/fr/022.webp)



完成後，儲存修改並重新啟動實體機器...這時，**VirtualBox 可以啟動虛擬機**，並載入 Windows ISO 映像來安裝作業系統！ 🙂



![Image](assets/fr/023.webp)



在我們安裝了 VirtualBox 的 Windows 11 實體主機上，我們可以看到 Windows 11 虛擬機器資料夾包含各種檔案。





- 與虛擬機器配置（RAM、CPU 等）相對應的 VBOX** 檔案（XML 格式）
- VBOX-PREV** 檔案是先前設定的備份
- VDI** 檔案對應動態模式下的虛擬 Hard 磁碟，因此目前只有 13 GB，而其最大大小為 64 GB。
- NVRAM** 檔案包含虛擬機器的 BIOS 狀態，相當於實體機器的非揮發性記憶體



![Image](assets/fr/024.webp)



## V.結論



**VirtualBox 現在已在我們的 Windows 11 實體機器上啟動並運作！剩下的就是利用它來建立虛擬機器了！** 我會在另一篇文章中再來介紹如何在 VirtualBox 虛擬機器中安裝 Windows 11。對於 Windows 10、Windows Server 或 Linux 發行版 (Ubuntu、Debian 等)，只要讓我們引導您即可！