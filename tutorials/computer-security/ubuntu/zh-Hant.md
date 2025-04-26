---
name: Ubuntu
description: 安裝和使用 Ubuntu 作為 Windows 替代方案的完整指南
---
![cover](assets/cover.webp)


## 簡介


作業系統 (OS) 是管理電腦所有資源的主要軟體。選擇 Ubuntu 之類的替代作業系統可以在安全性、成本和隱私方面提供許多優勢。


### 為何選擇 Ubuntu？




- 增強的安全性** ：Linux 發行版本以其安全性和穩定性著稱
- 零成本**：Ubuntu 和大多數 Linux 發行版都是免費的
- 大型社群**：隨時準備透過論壇和教學提供協助的使用者社群
- 尊重隱私**：開放原始碼系統，提高透明度
- 簡單**：使用者友善的 Interface 和易用性
- 豐富的生態系統** ：廣泛的開放原始碼軟體目錄
- 定期支援**：來自 Canonical 的安全更新


## 安裝與設定


### 1.先決條件


**所需設備：**




- 至少 12 GB 的 USB 隨身碟
- 至少有 25 GB 可用空間的電腦


### 2.下載




- 前往 [ubuntu.com/download](https://ubuntu.com/download)。
- 選擇穩定版本 (建議使用 LTS)
- 下載 ISO 映像


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3.建立可開機的 USB 密鑰


您可以使用多種工具，例如 Balena Etcher ：




- 下載並安裝 [Balena Etcher](https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- 開啟 Balena Etcher，然後選擇 Ubuntu ISO 映像
- 選擇 USB 隨身碟為目的地媒體
- 按一下 Flash 並等待程序完成


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4.安裝和保護 Ubuntu


**4.1 從 USB 隨身碟開機** (法文)




- 關閉電腦
- 插入 USB 密鑰 (內含 Ubuntu)
- 開啟電腦。在最近的 PC 上，系統應該會自動識別 USB 開機金鑰。如果不是這樣，請按住 BIOS/UEFI 存取鍵 (通常是 F2、F12 或 Delete，視品牌而定) 重新開機。
 - 在 BIOS/UEFI 功能表中，選擇 USB 密鑰為開機裝置
 - 保存並重新啟動


**4.2 啟動安裝** (法語)


**Start-up screen**


從 USB 隨身碟開機時，您會看到這個畫面，可讓您啟動 Ubuntu。


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**語言選擇


選擇您偏好的安裝和系統語言。


![Sélection de la langue](assets/fr/07.webp)


**無障礙選項


必要時設定存取選項（螢幕閱讀器、高對比等）。


![Options d'accessibilité](assets/fr/08.webp)


**鍵盤配置


選擇您的鍵盤配置。可使用測試欄位檢查按鍵是否符合您的配置。


![Configuration du clavier](assets/fr/09.webp)


** 網路連線**


在安裝過程中，連接到您的 Wi-Fi 或有線網路以下載更新。


![Configuration réseau](assets/fr/10.webp)


** 安裝類型


選擇「Try Ubuntu」（測試而不安裝）或「Install Ubuntu」。


![Choix du type d'installation](assets/fr/11.webp)


**安裝方法


選擇互動式安裝。


![Mode d'installation](assets/fr/12.webp)


**應用選擇


可選擇預設安裝或擴充的應用程式選項。


![Sélection des applications](assets/fr/13.webp)


**第三方應用程式


決定是否安裝額外的驅動程式和專屬軟體。


![Installation applications tierces](assets/fr/14.webp)


**分區類型


您有兩個主要選項：




- "刪除磁碟並安裝 Ubuntu」： 將整個磁碟用於 Ubuntu
- "手動安裝：與 Windows 建立雙重開機或自訂磁碟分割


![Choix du partitionnement](assets/fr/15.webp)


**建立使用者帳號


為您的 Ubuntu 帳戶設定使用者名稱和密碼。


![Création du compte](assets/fr/16.webp)


**時區


選擇您的地理區域以設定系統時間。


![Sélection du fuseau horaire](assets/fr/17.webp)


** 安裝摘要**


在開始最終安裝之前，請檢查您的所有選擇。按一下「安裝」後，安裝程序即告開始。


![Résumé de l'installation](assets/fr/18.webp)


**4.3 安裝後升級 Ubuntu** (法語)


更新系統是新安裝後的重要步驟。您有兩個選擇：


**選項 1：透過圖形使用者 Interface**




- 在應用程式功能表中搜尋「軟體與更新」。
- 應用程式會自動檢查可用的更新
- 按照螢幕上的指示安裝更新


**選項 2：透過終端




- 開啟終端機 (Ctrl + Alt + T)
- 鍵入下列指令以檢查可用的更新：


```bash
sudo apt update
```




- 按提示輸入密碼
- 若要安裝更新，請輸入 ：


```bash
sudo apt upgrade
```




- 輸入「Y」確認安裝，然後輸入「Enter」。


### 5.發現基本任務


**5.1 瀏覽網際網路


預設情況下，您通常會在啟動列中找到 Firefox。


啟動 Firefox 並開始瀏覽。


其他瀏覽器（Chrome、Brave 等）可透過軟體管理員或 .deb 套件安裝。


**5.2 文字處理


Ubuntu 隨附 LibreOffice 套件 (Writer 用於文字處理)。


若要開啟：活動 > 搜尋「LibreOffice Writer」，或按一下列中出現的圖示。


您可以建立、編輯和儲存各種格式的文件 (包括 .docx)。


**5.3 安裝應用程式


軟體管理員（稱為「Ubuntu Software」）：圖形化 Interface，用於搜尋和安裝應用程式。


從終端機，使用命令 ：


```bash
sudo apt install nom-du-paquet
```


範例：


```bash
sudo apt install vlc
```


### 6.結論與其他資源


現在您已準備好每天使用 Ubuntu：確保系統安全、瀏覽、執行辦公室工作、安裝軟體並保持作業系統更新！


為了讓您數位生活的安全性更進一步，我們建議您看看我們的加密訊息服務，它完全適合保護您的隱私，並與您的 Ubuntu 安裝相輔相成：


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2