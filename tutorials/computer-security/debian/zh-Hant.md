---
name: Debian
description: 以穩定、堅固和相容性見稱的 Linux 發行版。
---

![cover](assets/cover.webp)



Debian 是一個自由的 GNU/Linux 發行版，以其穩健性和可靠性而聞名。它的 Linux 核心和所有套件都經過嚴格的測試，以確保堅若磐石的穩定性和高度的安全性。Debian 適用於伺服器和工作站，提供簡單易用的體驗和豐富的軟體目錄。無論您是在尋找日常使用的安全系統還是生產環境，Debian 都是您的不二之選。



## 為什麼選擇 Debian？





- 免費且開放**：Debian 完全開放原始碼，保證透明且無授權費用。
- 穩定性與安全性**：每個發行版本都經過徹底的測試，讓 Debian 成為市場上最可靠、最安全的發行版之一。
- 活躍的社群**：龐大的社群和豐富的文件，隨時為您提供支援。
- 輕量且可擴充**：您可以在資源有限的機器上安裝 Debian，同時維持良好的效能。
- 廣泛的軟體目錄**：透過套件庫提供超過 50,000 個官方套件。



## 選擇 Interface 圖形



Debian 提供多種桌面環境來滿足您的需求：





- GNOME**：現代、直覺的 Interface，初學者的理想選擇。它提供流暢、易用的圖形化選單來存取應用程式。
- XFCE**: 又輕又快，非常適合效能較低的機器。
- KDE Plasma**：高度客製化，擁有類似 Windows 的外觀。
- Cinnamon**：簡單、優雅的 Interface，靈感來自 Windows。
- LXDE / LXQt**：超輕薄，適合較舊的電腦。
- MATE**：簡單、經典，接近舊版的 GNOME。



💡 要獲得舒適、易於握持的體驗，強烈建議**GNOME。



## 安裝和設定 Debian


### 硬體需求



開始安裝前，請確認已具備下列設備：





- USB 密鑰**：至少 8 GB，以存放可開機 ISO 映像。
- 隨機存取記憶體 (RAM)**：4 GB，可順暢安裝與操作。
- 磁碟空間**：至少 15 GB 的可用空間供系統和更新使用。



### 下載



Debian 映像的選擇取決於您的處理器架構：





- AMD64**：從 [下載] 清單 (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/) 下載 "live hybrid" 版本。
- ARM64**: 從 [Debian] 官方網站 (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/) 取得 DVD 映像檔。
- 其他架構**：在 [此處](https://debian.obspm.fr/debian-cd/12.11.0/) 找到與您的架構相對應的 ISO。



![download](assets/fr/01.webp)



### 建立可開機的 USB 密鑰



下載適當的 ISO 映像後，請繼續建立安裝媒體：




- 從 [官方網站](https://etcher.balena.io/) 下載 Balena Etcher**，然後取得適合您系統的二進位檔並安裝。



![etcher](assets/fr/02.webp)





- 啟動 Etcher**：開啟軟體並選擇先前下載的 Debian ISO 映像檔。
- 選擇 USB 隨身碟**：指定您的隨身碟（8 GB 以上）為目標。
- 啟動 flash**：按一下 **Flash！** 並等待程序完成。



![flash](assets/fr/03.webp)



您的 USB 密鑰現在可以開始安裝 Debian 了。



## 在您的系統上安裝 Debian



### 從 USB 隨身碟開機



若要從 USB 隨身碟啟動安裝程式 ：




- 完全關閉**電腦。
- 重新開機**，然後立即按下`ESC`、`F2`、`F11`（或專用鍵，視您的品牌而定）存取 BIOS/UEFI。
- 在開機功能表中，**選擇您的 USB 隨身碟**為開機裝置。
- 用 Enter 鍵確認**，開始 Debian 映像檔：這會帶您到安裝程式的歡迎畫面。



### 啟動安裝



開始畫面 ：



![starting](assets/fr/04.webp)



從 USB 隨身碟開機時，Debian 的歡迎畫面會提供幾個選項：




- Live System**：無需安裝即可啟動 Debian，是測試環境的理想選擇。
- Start Installer**：直接在 Hard 磁碟上開始安裝。
- 進階安裝選項**：可讓您存取自訂的安裝模式。



要在 Live 模式下探索 Debian，請選擇 **Live System**，然後用 **Enter** 確認。之後您就可以在 Live 環境中點選 ** 安裝 Debian** 來啟動安裝。



![system](assets/fr/05.webp)





- 語言選擇** (選購)



從清單中選擇 Debian 系統的主要語言，然後按一下確定。



![language](assets/fr/06.webp)





- 時區** (GMT)



選擇您的地理區域，以自動設定日期和時間。



![timezone](assets/fr/07.webp)





- 鍵盤配置



選擇您的鍵盤語言和配置。使用內建的測試欄位檢查每個按鍵是否產生預期的字元。



![keyboard](assets/fr/08.webp)



### 磁碟分割





- 刪除磁碟**：如果您有專用的磁碟分割，此選項會刪除其所有內容。
- 手動分割**：選擇此選項可根據需要建立、調整大小或刪除分割區。



![disk](assets/fr/09.webp)





- 建立使用者帳號



輸入您的全名、帳戶名稱和強大的密碼，以確保您的會話安全。



![user](assets/fr/10.webp)





- 參數摘要**



您的選擇摘要會顯示出來：勾選每個項目，必要時再回去修改。



![settings](assets/fr/11.webp)





- 啟動安裝



按一下 ** 安裝**，開始複製檔案並設定系統，然後等待程序完成。



![install](assets/fr/12.webp)





- 重新啟動**



安裝完成後，請重新啟動電腦，套用所有設定並存取新的 Debian 系統。



![restart](assets/fr/13.webp)



啟動時，請輸入使用者名稱和密碼以存取系統。



![login](assets/fr/14.webp)



## 系統更新



在您開始使用您的系統之前，更新是非常必要的。這可讓您受惠於最新的軟體修補程式、最新的儲存庫，以及在某些情況下，作業系統本身的安全修補程式。



### 選項 1：透過圖形化 Interface (GNOME) 更新



如果您在 GNOME 桌面環境下安裝了 Debian，您可以圖形化的方式執行更新。要這樣做，打開 ** 軟體** 應用程式，然後到 ** 更新** 標籤。然後按一下 ** 重新啟動並更新** 以啟動更新程序。



### 選項 2：透過終端更新 (建議)



此方法提供更完整的控制。它允許您更新套件庫、軟體套件，並在必要時更新核心。




- 使用快捷鍵 `Ctrl + Alt + T` 開啟終端機。
- 使用下列指令更新可用套件清單：



```shell
sudo apt update
```



按提示輸入您的密碼（注意，輸入時不會顯示任何字符 - 這是正常的）。





- 若要安裝可用的更新 ：



```shell
sudo apt full-upgrade
```



## 探索基本任務



### 瀏覽網際網路



Debian 的預設網頁瀏覽器是**Firefox**。如果您喜歡其他瀏覽器，只要 Debian 套件庫中有提供，您可以安裝其他瀏覽器 (例如 Chromium、Brave...)。



### 文字處理



Debian 預設已安裝 **LibreOffice** 套件。





- 若要撰寫文件，請使用 **LibreOffice Writer**，相當於 Microsoft Word。
- 對於試算表，**LibreOffice Calc** 是 Excel 的替代品。
- 最後，**LibreOffice Impress** 可讓您建立簡報，就像 PowerPoint 一樣。



## 安裝應用程式



在 Debian 上安裝應用程式有兩種方法：



### 圖形方法 ：



您可以使用 ** 軟體管理員** (可透過圖形化 Interface 存取) 來輕鬆搜尋和安裝應用程式。



### 指令行方法 ：



如果您要找的應用程式沒有出現在圖形 Interface 中，或者您比較喜歡使用終端機，請使用下列指令：



```shell
sudo apt install <name>
```



將 `<name>` 改為套件名稱。例如，要安裝 `curl` ：



```shell
sudo apt install curl
```



### 安裝手動下載的套件 ：



如果您下載了 `.deb` 檔案 (Debian 套件)，您可以使用下列指令安裝：



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

您的 Debian 系統現在已經安裝完成，可以開始執行日常任務。


拜 **GNOME** 桌面環境所賜，您可以透過友善的圖形 Interface 存取各式各樣的應用程式，無論是初學者或進階使用者都非常適合。



您也可以改變您的桌面環境 (例如 XFCE、KDE 等)，而不需要重新安裝 Debian。要做到這一點，只需使用終端機安裝您所選擇的新環境。



若要進一步瞭解 Debian，以及更廣泛的 GNU/Linux 發行版本，我建議您參考此課程 ：



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1