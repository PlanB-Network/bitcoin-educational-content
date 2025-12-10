---
name: Windows 11
description: 透過設定檔自動安裝 Microsoft Windows 11
---
![cover](assets/cover.webp)


在本教程中，我們將學習如何使用標準 Windows 安裝程序以外的方法自動安裝 Windows 11。


## 下載！


您首先需要的是安裝檔案。最安全可靠的地方是直接從 Microsoft 的官方網站下載。


只要造訪以下提供的連結，並依照指示下載 [Windows 11 ISO 檔案](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


進入下載頁面後，向下捲動到下載 ISO 檔案的部分。


![Image](assets/en/01.webp)


選擇適當的版本。


![Image](assets/en/03.webp)


選擇 Windows 11 之後，按一下 Confirm（確認）按鈕。


在此步驟，可能需要幾秒鐘的時間來處理請求，然後您會看到以下頁面：


![Image](assets/en/04.webp)


確認請求後，您需要選擇您偏好的語言。


![Image](assets/en/05.webp)


選擇語言並按一下「確認」按鈕後，該請求將被處理。此步驟可能需要幾秒鐘。


請求成功處理後，您會看到一個包含 .iso 檔案下載連結的頁面。按一下 64 位元下載按鈕開始下載。


檔案大小約為 5.5 GB，產生的連結有效期為 24 小時。


## 自動化！


在此階段，我們需要對標準 Windows 安裝進行變更。在此階段，使用 Unattended install，我們決定要安裝哪些項目，而不需要使用者事後輸入。事實上，在此方法中，會使用 XML 檔案來設定 Windows 中安裝的步驟和服務。換句話說，使用 Unattended.xml 檔案可在安裝期間建立自動化程序，避免需要選擇多個選項，並避免安裝期間通常需要的繁瑣步驟。此方法是微軟推出的不尋常但標準的方法。更多資訊請參考 [微軟官方網站](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11)。


網際網路上有各種工具可用來產生 Unattended 檔案。有些是線上工具，有些則是離線工具。[此網站](https://schneegans.de/windows/unattend-generator) 是其中一個建立此檔案的線上工具。打開之後，我們會看到以下頁面：


![Image](assets/en/06.webp)


如頁面頂端所述，此方法可用於安裝 Windows 10 和 11。第一步，我們選擇 Windows 語言。如果我們需要在 Windows 顯示和鍵盤語言清單中新增第二甚至第三種語言，可以使用下方的方塊：


![Image](assets/en/07.webp)


下一步，我們選擇所需的位置。


![Image](assets/en/08.webp)


在這個階段，我們也可以指定電腦的處理器架構。在這個步驟中，我們可以

1.決定是否忽略 Windows 安全功能，例如 TPM 和 Secure Boot。安全開機功能可確保在開機過程中，如果任何核心 Windows 檔案遭到竄改，問題會被偵測出來，並防止其執行。此功能也有助於保護系統不會在 Windows 上安裝惡意更新。啟用選項以繞過這些功能在某些電腦上有時是無法避免的，尤其是較舊的機型。不過，一般建議保持啟用安全開機等功能。

2.忽略需要網際網路連線才能完成程序的要求。這在無法使用有線 LAN 連線的情況下非常有用，因為在大多數情況下，Windows 安裝時尚未識別無線網卡，需要透過纜線存取網際網路。啟動此選項可解決與此步驟相關的問題。


下一步，我們可以為電腦選擇一個名稱。


![Image](assets/en/09.webp)


我們也可以讓 Windows 為系統選擇名稱。在這個步驟中，我們可以選擇 Windows 的類型，是壓縮或非壓縮，或讓 Windows 根據電腦的規格來決定適當的版本。時區也可以在此階段設定。


下一步涉及磁碟分割設定：


![Image](assets/en/10.webp)


在此階段，我們可以指定安裝 Windows 的磁碟分割類型，以及安裝 Windows 復原環境所需的設定。選擇第一個選項後，磁碟分割的選擇和磁碟分割的設定會延遲到 Windows 安裝時進行，在安裝過程中，這些問題會像一般安裝方法一樣被詢問。


在此步驟，我們選擇要安裝的 Windows 版本：


![Image](assets/en/11.webp)


如果有產品金鑰，也可以在此階段輸入。


下一步是設定 Windows 登入帳戶：


![Image](assets/en/12.webp)


## 帳戶會議


在這個階段：


1.我們可以為管理帳戶定義名稱和密碼。也可以建立多個使用者或管理員帳號。

2.在此，我們指定 Windows 安裝後首次登入的帳戶。本節的不同選項如圖所示。

3.如果您不希望建立任何帳戶，請清除所有帳戶，並選取此選項。在這種情況下，Windows 安裝完成後，您會自動登入 Windows 管理員帳戶。


下一步涉及設定密碼和主機檔案設定：


![Image](assets/en/13.webp)


在此階段，我們會決定密碼是否應該有失效期。此外，本節還包括與登入嘗試失敗相關的安全性設定，可根據您的需求啟用或停用。


在本節底部，有檔案顯示的設定。這些選項在標準 Windows 安裝期間都不可用，必須在安裝後設定。相比之下，使用「無人看管」安裝方法時，這些設定都很容易取得。


下一步是設定 Windows 安全設定：


![Image](assets/en/14.webp)


## 安全設定


在這個階段：


1.Windows Defender 可以啟用或停用。此功能的作用類似 Windows 中的安全軟體，有助於防止執行惡意檔案、某些網路攻擊等。

2.Windows 自動更新可以停用。這是 Windows 使用者常面臨的挑戰之一！

3.本節允許啟用或停用 UAC（使用者帳戶控制）。此功能可防止可疑的應用程式以較高的讀寫權限執行。

4.Windows 使用此功能來偵測可能有害的軟體。

5.啟用或停用 Windows 應用程式 (例如 PowerShell 及其他) 對長路徑的支援。

6.啟用或停用遠端桌面，以便遠端存取系統。


視使用的 Windows 版本而定，其中某些功能可能受支援，也可能不受支援。


下一步是設定圖示：


![Image](assets/en/15.webp)


在本節中：


1.列出桌面圖示，可根據需要新增或移除。

2.列出了開始功能表圖示，也可根據需求新增或移除。

3.本節允許設定是否安裝虛擬化相關工具。此選項專屬於 Windows 11，不適用於 Windows 10。


下一步是設定 Wi-Fi 設定：


![Image](assets/en/16.webp)


在本節中，可以設定 Wi-Fi 網路設定。如前所述，在大多數情況下，Windows 安裝期間無法識別 Wi-Fi 卡，因此在安裝期間通常無法連線。但是，透過設定本節，如果偵測到無線網卡，系統就可以連線到網際網路。


下一步涉及到一個重要的設定：


![Image](assets/en/17.webp)


在本節中，我們指定系統問題資訊是否應該傳送至 Microsoft。


下一步是設定預設應用程式：


![Image](assets/en/18.webp)


## 預設軟體啟用/停用


在此部分中，我們可以選擇不希望預設安裝的任何應用程式。例如，我們可以選擇不安裝 Cortana 或 Copilot。


下一步涉及與應用程式執行相關的安全性設定：


![Image](assets/en/19.webp)


透過套用 WDAC 設定，可以阻止某些應用程式的執行。


最後，套用所需的設定後，就可以下載產生的 XML 檔案：


![Image](assets/en/20.webp)


按一下 Download XML File（下載 XML 檔案），即可下載 autounattend.xml 檔案。要使用此檔案，只需將下載的 ISO 掛載到 USB 磁碟機，將 autounattend.xml 檔案放入根目錄中，然後繼續進行 Windows 安裝。


Rufus 是可用於製作可開機 USB 磁碟機的工具之一。Rufus 可以使用指定的 Windows 安裝 ISO 檔案製作可開機的 Windows 安裝隨身碟。它既快速又簡單，您可以 [在此](https://rufus.ie/en/#download) 下載。


![Image](assets/en/21.webp)


在此軟體中，選擇所需的 USB 磁碟機和適當的 ISO 檔案後，我們按一下「開始」。


![Image](assets/en/22.webp)


在此階段，我們停用所有選項，因為啟用這些選項可能會在使用產生的 Unattend 檔案時造成衝突。檔案複製到 USB 隨身碟後，我們將 autounattend.xml 檔案放在根目錄中：


![Image](assets/en/23.webp)


此時，USB 磁碟機已準備好用來自動安裝 Windows，可以使用此磁碟機開始安裝。


## ISO 編輯


如果您需要在虛擬機器上安裝 Windows，可以使用軟體來建立和編輯 ISO 檔案。AnyBurn 就是其中一種軟體。擷取從 Microsoft 網站下載的 ISO 檔案內容後，將 autounattend.xml 檔案置於根目錄中。然後使用 AnyBurn，以更新的內容建立新的 ISO。


AnyBurn 是處理 ISO 檔案的多功能軟體。它提供各種處理 ISO 檔案的功能，其中之一是建立可開機 ISO 映像；[這裡](https://www.anyburn.com/download.php) 是原始網站。


在軟體主畫面上，選擇「從檔案/資料夾建立影像」：


![Image](assets/en/24.webp)


在下一頁，選擇從 ISO 擷取的所有檔案以及 autounattend.xml 檔案。


![Image](assets/en/25.webp)


在此步驟，我們會設定使 ISO 檔案可開機的設定：


![Image](assets/en/26.webp)


在此階段，必須設定 bootfix.bin 檔案的路徑，才能使 ISO 可開機。這個檔案位於 ISO 的根目錄，在開機資料夾內。此外，建議在「內容」部分同時啟用 ISO9660 和 UDF 選項。


![Image](assets/en/27.webp)


完成此步驟後，按一下下一步即可建立 ISO 檔案。此檔案可用於虛擬化軟體，例如 Oracle VirtualBox。以下是關於 VirtualBox 的教學：


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65