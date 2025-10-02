---
name: Zen Browser
description: 如何使用 Zen 瀏覽器進行有效率且保密的瀏覽？
---

![cover](assets/cover.webp)



在今日的網頁瀏覽器領域中，Google Chrome 擁有超過 65% 的市場佔有率，但這種霸權地位卻引發了有關隱私權和技術多樣性的重要問題。Chrome 和大多數流行的瀏覽器一樣，會大量收集瀏覽資料，供 Google 的廣告演算法使用。



![Parts de marché des navigateurs](assets/fr/01.webp)



面對這樣的現實，新的瀏覽器正以不同的理念出現：調和現代使用者體驗與尊重隱私權。於 2024 年推出的 Zen 瀏覽器就是這種方法的一部分，它以 Firefox 為基礎，但針對現今使用者重新設計，提供創新的替代方案。



Zen Browser 以其獨特的 Interface 脫穎而出，擁有垂直標籤、可整理會話的工作空間，以及分割檢視等生產力功能。但除了這些符合人體工學的創新之外，最重要的是它對隱私權的 Commitment 讓它變得有趣：無遙測、強化的反追蹤保護，以及透明的社群開發。



在本教程中，我們將發現 Zen Browser 如何結合生產力、個人化和隱私，改變您的瀏覽方式。



## 安裝 Zen 瀏覽器



### 官方下載



Zen Browser 適用於 Windows、macOS 和 Linux。請造訪官方網站：zen-browser.app/download



![Site officiel Zen Browser](assets/fr/02.webp)



網站會自動偵測您的系統，並提出適當的連結：



![Page de téléchargement](assets/fr/03.webp)





- **Windows:** .exe 安裝程式，適用於 Windows 10/11 (x64 與 ARM64 版本)
- **macOS:** Intel 與 Apple Silicon 相容的 .dmg 磁碟映像檔 (macOS Monterey 與更新版本)
- **Linux:** 提供多種選項：
- **Flatpak** (建議)：`flatpak install flathub app.zen_browser.Zen`.
- **AppImage**：可攜式、直接執行
- 檔案 **tar.gz** ：要手動解壓縮
- **AUR** (Arch Linux) ：Zen-browser 套件



### 逐步安裝



**在 Windows 上：**




- 下載 .exe 檔案
- 執行安裝程式 (如果 SmartScreen 有警示，請按一下「其他資訊」，然後按一下「無論如何執行」)
- 選擇安裝目錄
- 勾選「啟動 Zen 瀏覽器」以立即啟動



**在 macOS 上：**




- 下載 .dmg 檔案
- 掛載磁碟影像
- 將 Zen Browser 拖曳到「應用程式」資料夾中
- 首次啟動時：按滑鼠右鍵 > 「開啟」切換至 Gatekeeper



**在 Linux 上：**




- **Flatpak:** 透過套件管理員自動安裝
- **AppImage:** `chmod +x ZenBrowser.AppImage` 然後按兩下
- **tar.gz:** 解壓縮並執行 zen-browser 可執行檔



### 首次發射與初始組態



初次啟動時，Zen Browser 會引導您完成幾個設定步驟：



![Import de données](assets/fr/04.webp)


*可選擇從其他瀏覽器匯入您的資料（我的最愛、歷史記錄、密碼）*。



![Configuration initiale](assets/fr/05.webp)


*選擇預設搜尋引擎和設定針標籤*



![Personnalisation visuelle](assets/fr/06.webp)


*選擇工作區的顏色，並驗證存取瀏覽器*



![Page d'accueil Zen Browser](assets/fr/07.webp)


*具有特色側邊欄的 Zen 瀏覽器首頁*



## 介紹 Zen 瀏覽器



**Zen Browser** 是源自 Mozilla Firefox 的免費開放原始碼網頁瀏覽器，自 2024 年 3 月起由一群熱情的志工社群所開發。與主要科技公司的瀏覽器不同，Zen Browser 沒有任何商業公司的支持，經費完全來自社群的貢獻。



**重要聲明：** Zen Browser 目前為 **Beta 版本**。雖然對於日常使用來說是穩定的，但仍預期會有頻繁的更新和偶爾的錯誤。



該專案的口號概括了其理念：「歡迎來到更平靜的網際網路」。這一理念詮釋為一款關心您的使用者體驗而非個人資料的瀏覽器，在美觀、速度和隱私之間尋求完美的平衡。



### 為提高生產力而重新設計的 Interface



Zen Browser 以多項創新技術徹底改變瀏覽體驗：



**垂直標籤：** 與傳統瀏覽器不同，Zen 會將您的標籤顯示在垂直側邊欄中，而非水平顯示。這個符合人體工學的選擇，靈感來自 Arc Browser，可將顯示空間最大化並改善導覽功能，尤其是當您開啟許多標籤頁時。



**工作空間：** 在專屬空間中，依專案或主題組織您的標籤。例如，「工作」空間放置您的專業標籤，「觀賞」空間放置您的閱讀，等等。您可以立即從一個空間切換到另一個空間。



**Split View：** 在單一視窗中並排顯示多個網站，是比較資訊或同時處理多個來源的理想選擇。



**Glance:** 可在臨時模式視窗中快速預覽連結，而無需開啟新標籤頁，非常適合在不遺失上下文的情況下查閱參考資料。



### 預設隱私權



Zen 瀏覽器原生整合了強大的隱私權保護功能：





- 增強的反追蹤功能：**自動封鎖追蹤程式、協力廠商 Cookie 和指紋腳本**
- 已停用遙測功能：**無資料傳送至外部伺服器**
- DNS over HTTPS：**加密您的 DNS 請求以防止監控**
- 減少對 Google 的依賴：**Zen 瀏覽器移除大部分與 Google 服務的連線，但仍保留部分連線 (安全瀏覽、更新)**



### 使用 Zen Mods 進階客製化



Zen 提供一個獨特的客製化生態系統，**Zen Mods**：一個由社群建立的主題與修改畫廊，可改變瀏覽器的外觀與行為。



**推薦的流行 Zen Mods：**





- **SuperPins** ⭐：將釘選標籤變成風格化按鈕，讓 Interface 看起來更專業
- **一致性**：一致、透明的樣式，統一 URL 列、側邊欄和書籤
- 更好的搜尋列：將搜尋列移至頂端，更符合人體工學
- 側邊欄在懸停時展開：懸停時自動擴充側邊欄，最大化螢幕空間
- 更好的卸載標籤：以視覺化指示器顯示非作用中標籤，優化記憶體管理
- 淨化 URL 棒：Interface 純化的 Address 條件，移除多餘的 Elements
- **Transparent Zen**：優雅的透明效果與流暢的動畫



**Zen Mod 安裝：**




- 前往 [官方 Zen Mods 圖庫](https://zen-browser.app/mods)
- 瀏覽可用主題的圖庫



![Galerie Zen Mods](assets/fr/12.webp)





- 點選所需 mod 的「安裝」。



![Installation SuperPins](assets/fr/13.webp)


*範例：安裝熱門的 SuperPins* Mod





- 主題即時適用
- 您可以隨時停用或嘗試其他功能



Zen Mods 不限於視覺主題：有些修改 Interface 的行為 (動畫、元素佈局、自訂捷徑)。這種模組化的方式讓每位使用者都能建立自己理想的瀏覽環境。



![Gestion des Zen Mods](assets/fr/16.webp)


*Interface 用於管理安裝在參數*中的 Zen Mods



**⚠️ 關於個人化和指紋的重要說明：**


您自訂 Zen 瀏覽器 (主題、擴充套件、mod) 越多，您的**數位足跡**就越獨特，因此也越可追蹤。這是根本性的妥協：




- **最大個人化** = 最佳使用者體驗 BUT 獨特、易於識別的印記
- **預設配置** = 較常見的足跡，但較少個人化的體驗



Zen Browser 選擇了使用者經驗而非完美的匿名性。如果您的優先考量是絕對匿名，請選擇 Tor 瀏覽器或 Mullvad 瀏覽器，它們會對所有使用者實施統一的設定。



此外，Zen 以 Firefox 為基礎，與整個 Firefox 延伸生態系統相容。



## 優點與缺點



### ✅ 亮點





- 隱私權設計：**啟用防追蹤保護，停用遙測功能，不收集資料**
- 創新的 **Interface**：垂直標籤、工作區、分割檢視可大幅提高生產力
- 快速更新：**在 72 小時內與 Firefox 同步處理安全修補程式**
- 進階自訂：**社群主題、微調、Firefox 延伸相容性**
- 開放原始碼與社群：**透明程式碼、協同開發、獨立於大科技公司**



### ❌ 電流限制





- 無行動版本：**僅適用於個人電腦 (Windows、macOS、Linux)**
- DRM 不相容：**Netflix、Disney+、Spotify 及其他串流服務目前無法運作**
- 年輕的專案：**小團隊、社群支援、偶爾出錯**
- 學習曲線：**Interface 不同，習慣使用水平標籤的人需要適應**



## 隱私與安全的進階設定



若要存取 Zen 瀏覽器設定 ：



![Accès aux paramètres](assets/fr/14.webp)


*按一下拼圖圖示 (擴充套件)，然後按一下底部的「Zen 設定」*。



![Interface des paramètres](assets/fr/15.webp)


*Zen 參數的一般檢視，包含所有可用的選項卡*。



### 最佳化預設設定



從一開始，Zen Browser 就應用了高隱私配置，優於大多數瀏覽器：





- 嚴格的防追蹤保護：**預設啟動「標準」等級，可封鎖 .NET 和 .NET 檔案**：
  - 跨站追蹤 Cookie 和 supercookies
  - 廣告追蹤腳本（Google Analytics、Facebook Pixel 等）
  - 使用您的 CPU 來 Miner 加密貨幣的 Cryptominters
  - 透過 Canvas、WebGL、AudioContext 進行指紋辨識





- 完全 cookie 隔離：**第一方隔離可防止一個網站讀取另一個網站的 cookie**
- Telemetry 基本上已停用：**大部分資料收集已移除，但某些 Mozilla/Google 服務的連線可能會保留，並需要額外的手動設定。**
- 預設的安全 DNS：**已啟用 DNS-over-HTTPS，以防止窺探您的要求**
- 只啟用 HTTPS：**在所有網站強制加密連線**



### 建議的隱私權設定



**1.選擇防追蹤保護等級：**


設定 > 隱私權與安全性 > 強化追蹤保護



![Protection anti-pistage](assets/fr/18.webp)



**標準（建議預設值）：**




- 平衡保護與效能，頁面正常載入
- 攔截：社交追蹤器、跨站 cookie、私人視窗中的追蹤內容、加密挖掘、指紋器
- 包括 ** 全面 Cookie 保護**：依據網站隔離 Cookie，防止跨站追蹤



**嚴格（最大保護）：**




- 加強保護，但可能會破壞某些網站或內容
- 攔截：社交追蹤器、跨站 cookie、****視窗中的追蹤內容、已知和可疑的瀏覽器
- 建議有經驗的使用者使用



**客製化（粒度控制）：**




- 精確選擇要封鎖的追蹤器和腳本
- 獨立選項：Cookies、追蹤內容、加密、已知/疑似追蹤器
- 根據您的需求進行微調的理想選擇



**2.變更搜尋引擎：**


設定 > 搜尋 > 預設搜尋引擎 ：



![Configuration moteur de recherche](assets/fr/20.webp)





- **DuckDuckGo**：無側寫，無過濾氣泡，中立的結果
- **Startpage**：匿名 Google 結果，位於荷蘭 (RGPD)
- **Searx**：分散式元搜尋引擎，無日誌，開放原始碼
- **Brave Search**：獨立索引，非來自 Google
- 避免：Google、Bing、Yahoo (大量資料收集)



**3.設定安全 DNS (DNS over HTTPS):**


設定 > 隱私權與安全性 > 透過 HTTPS 的 DNS (頁面底部)



![Configuration DNS sur HTTPS](assets/fr/19.webp)



**預設保護：**




- Zen 會自動決定何時使用安全 DNS
- 在可使用安全 DNS 的地區使用安全 DNS
- 如果安全供應商出現問題，則回復預設 DNS
- 透過 VPN、家長控制或企業政策自動停用



**增加保護（建議）：**




- 您可以控制何時使用安全 DNS，並選擇提供商
- 使用選定的提供者，必要時可回退至 DNS 系統
- 預設提供者：**Cloudflare (快速、匿名日誌)**
- 替代方案：**轉換至 Quad9、NextDNS 視可用性而定**



**最大保護（進階使用者）：**




- Zen **始終只使用安全的 DNS**
- 使用 DNS 系統前的安全警告
- 警告：**如果安全 DNS 無法使用，網站可能無法載入**



**4.僅啟用 HTTPS 模式：**


設定 > 隱私權與安全性 > 僅 HTTPS 模式 > **已啟用**




- 強制所有連線至 HTTPS
- 若網站僅支援 HTTP 則發出警示



**5.管理預設權限：**


設定 > 隱私權與安全性 > 權限 ：




- 地點：區塊（卡服務除外）
- 攝影機/麥克風：區塊（依個別情況授權）
- 通知：封鎖（防止垃圾郵件）
- 自動播放**：封鎖音訊與視訊**



### 建議的安全延伸



**基本擴充：**




- **uBlock Origin**：最有效的廣告封鎖和追蹤器
  - 推薦清單：EasyList、EasyPrivacy、Peter Lowe 的廣告與追蹤伺服器清單
  - 進階模式適合有經驗的使用者





- **ClearURLs**：刪除 URL 追蹤參數 (utm_source、fbclid 等)
- **Cookie AutoDelete**：關閉標籤頁時自動刪除 Cookie 和瀏覽資料
- **Decentraleyes**：在本機提供 JS 函式庫，以避免使用 Google/Cloudflare CDN



**進階擴充功能（經驗豐富的使用者）：**




- **NoScript**：細緻的 JavaScript 控制 (可能會破壞許多網站)
- **Privacy Badger** (EFF)：追蹤者的行為偵測
- 臨時容器：將每個標籤分隔在不同的容器中



## 瞭解 Zen Browser 中沒有 DRM 的情況



### 什麼是 DRM？



**DRMs (數位版權管理)** 是加密數位內容以防止複製的保護技術。它們需要專屬的瀏覽器模組 (例如 **Google Widevine**) 來解密和讀取受保護的媒體。



**需要 DRM 的服務：**




- 視訊串流：**Netflix、Disney+、HBO Max、Amazon Prime Video**
- 高級音樂：**Spotify Premium、YouTube Music、Deezer**
- 線上訓練：**Udemy、Coursera** (受保護的影片)



### 為什麼 Zen Browser 沒有 DRM？



**主要原因：**


1. **成本與複雜性：** Google Widevine 授權並非免費，需要經過繁瑣的核准程序


2. **專案理念：** DRM 是專屬的「黑盒」，與開放原始碼的方式和獨立於 Google 的方式不相容


3. ** 有限的資源：** 團隊專注於 Interface 的創新與保密性



### 實際影響



**❌ 無法取得的服務：**


Netflix、Disney+、Spotify Premium、YouTube Premium、Udemy/Coursera 付費訓練課程



![Erreur DRM Prime Video](assets/fr/17.webp)


*嘗試播放受 DRM 保護內容時的典型錯誤訊息*



**✅ 功能性服務：**


免費 YouTube、Twitch、Vimeo、新聞網站、社交網路、播客



**旁路解決方案：**




- 僅使用 Firefox/Chrome 進行串流
- 原生應用程式 (Netflix、Spotify)
- 選擇不含 DRM 的內容 (YouTube、Twitch、Bandcamp、PeerTube)



**Current status:** Zen 團隊已開始取得 Widevine 授權，但尚未給出時間表。這個過程完全取決於 Google 的批准。



## 每日使用



### Interface 和導航



**標籤式側邊欄：**




- 每頁的標題和縮圖
- 新標籤的「+」按鈕
- 拖放式重組
- 上下文相關動作：按滑鼠右鍵複製、關閉、移動



**工作領域：**




- 側邊欄頂端的選擇器
- 建立主題區域
- 快速切換上下文
- 所有空格中都可使用釘住的標籤



![Création d'un nouvel espace](assets/fr/11.webp)


*Interface 建立新工作區*



**進階功能：**




- 分割檢視：選取數個索引標籤 > 按滑鼠右鍵 > 「分割 x 索引標籤」。
- 一覽**：Alt + 按一下連結以進行預覽**



### 有用的捷徑





- ctrl+T`：新建索引標籤
- ctrl+空格`：工作區功能表
- ctrl+B`：顯示/隱藏側邊欄
- ctrl+Shift+P`：私人視窗
- alt+點選`：一瞥 (預覽)



### 最佳實踐





- 整理您的空間：建立主題空間 (工作、看護、個人)
- 使用釘選標籤：針對您最常造訪的網站
- 利用分割檢視：在大螢幕上執行多工作業的理想選擇
- 保持更新：定期檢查更新
- 探索 **Zen Mods**：自訂符合您品味的外觀



## 總結



Zen Browser 代表了網路瀏覽器生態系統中的一股新風。它結合了創新、高效的 Interface 與對隱私的嚴格尊重，為科技巨頭的瀏覽器提供了可靠的替代方案。



它的垂直標籤和工作區真正改變了那些同時處理多個專案的人的瀏覽體驗。其「不使用 Google」的理念與社群發展，讓它成為關心數位主權的使用者的一致選擇。



雖然它仍有一些限制 (沒有行動裝置、缺少 DRM)，但 Zen Browser 已經很成熟，足以滿足日常使用的需求，而且因為社群的活躍，Zen Browser 正在快速改進。



對於重視生產力和隱私的比特幣玩家和技術用戶來說，Zen Browser 絕對值得一試。您很可能會採用這種全新、更安靜、更有效率的瀏覽方式。



## 資源



### 官方連結




- [Zen Browser 官方網站](https://zen-browser.app)
- [完整文件](https://docs.zen-browser.app)
- [GitHub 原始碼](https://github.com/zen-browser/desktop)
- [下載頁面](https://zen-browser.app/download)


### 社群與支援




- [Official Discord](https://discord.gg/zen-browser)
- [Reddit r/zen_browser](https://reddit.com/r/zen_browser)
- [Zen Mods Gallery](https://zen-browser.app/mods)