---
name: LibreWolf
description: 如何使用 LibreWolf 隱私瀏覽器
---

![cover](assets/cover.webp)



每次點擊、每次搜尋、每次造訪網站：您的網頁瀏覽器已成為全球商業監控系統的精密告密者。超過 30 億人使用的 Google Chrome 瀏覽器，將您每天的瀏覽記錄轉換成廣告巨頭有利可圖的資料。即使是 Firefox，儘管有「道德」瀏覽器的美譽，預設也會啟動遙測機制，將您的瀏覽習慣傳送給 Mozilla。



這個現實提出了一個基本的問題：是否仍有可能在網際網路上自由瀏覽，而不會不斷被監視和側寫？幸運的是，答案是肯定的，這要歸功於社區計畫，這些計畫讓使用者重新成為他們關心的焦點。



LibreWolf 體現了這種數位反抗的哲學。這個瀏覽器是獨立開發者社群的心血結晶，它將 Firefox 轉變為名副其實的防線上監控的盾牌。當商業瀏覽器試圖賺取您的注意力時，LibreWolf 卻反其道而行：讓您不受追蹤者的影響，同時保留流暢、現代的瀏覽體驗。



在本教程中，我們將發現 LibreWolf 如何改變您上網的方式，在不犧牲效能或網頁相容性的情況下，提供強大的防追蹤保護。



![LIBREWOLF](assets/fr/01.webp)


*網頁瀏覽器市場佔有率：Chrome 佔據了 65% 的市場，其次是 Safari 和 Edge。這種支配地位引起了關於網路多樣性和隱私權的問題*。



## 介紹 LibreWolf



**FreeWolf** 是源自 Mozilla Firefox 的開放源碼網頁瀏覽器，由自由軟體愛好者的獨立社群開發和維護。其主要目標是提供以使用者隱私、安全與自由為重點的瀏覽功能。



具體來說，LibreWolf 使用 Firefox 的 Gecko 引擎，但卻有截然不同的理念：Firefox 必須平衡隱私與易用性，而 LibreWolf 則選擇預設隱私。該專案移除任何可能侵犯您隱私的東西 (遙測、資料收集、贊助模組)，同時整合增強的安全設定。



### 目標：隱私與自由



LibreWolf 的目標是在加強瀏覽器安全性的同時，最大程度地保護瀏覽器不被追蹤和識別指紋。其主要目標包括





- 在 Firefox 中消除所有遙測和資料收集**
- 停用違反使用者自由的功能**，例如專屬 DRM 模組
- 一開始就套用隱私/安全設定**和特定修補程式
- 社區發展保證了透明度和獨立性**，不受商業利益的影響



簡而言之，LibreWolf 以「若隱私是最優先考量的話，Firefox 應該會是這樣」自居 - 這是一個預設尊重您的瀏覽器，不需要額外的設定。



### 主要功能



LibreWolf 從一開始就提供一系列以隱私為導向的功能：



**沒有遙測或資料收集：** 不像 Chrome 或 Firefox 會傳送某些使用統計資料，LibreWolf 絕對不會從您的瀏覽中收集任何資料。沒有碰撞報告，沒有用戶研究，沒有贊助建議。



**LibreWolf 原生整合了 uBlock Origin 擴充套件，市面上最好的廣告封鎖與追蹤軟體之一。預設情況下，LibreWolf 會主動過濾任何可能會追蹤您的網路資訊（侵入性廣告、追蹤腳本、加密貨幣 Mining）。



**預設的隱私搜尋引擎：** LibreWolf 預設使用 DuckDuckGo 作為初始搜尋引擎，它不會保留您的查詢記錄。其他以隱私為導向的替代品 (Searx、Qwant、Whoogle) 也是可用的。



** 強化反指紋保護：** 指紋技術允許瀏覽器透過其設定被唯一識別，即使沒有 cookies。為了對抗這一點，LibreWolf 啟動了 Tor 計畫的 RFP (Resist Fingerprinting) 技術，讓您的瀏覽器盡可能的通用。測試顯示，標準的 Firefox 瀏覽器在 coveryourtracks.eff.org 等工具上有 ~90% 的唯一性，而 LibreWolf 瀏覽器只有 ~10-20% (這些數字是指示性的，可能會因軟硬體配置及安裝的擴充套件不同而有所差異)。



![LIBREWOLF](assets/fr/07.webp)


*使用 TEST YOUR BROWSER 按鈕進行 EFF 測試頁 [Cover Your Tracks](https://coveryourtracks.eff.org/)。此頁面用於評估對追蹤器和指紋的保護。



![LIBREWOLF](assets/fr/08.webp)


*Cover Your Tracks 測試結果。顯示 「您擁有強大的網路追蹤保護 」訊息，顯示 LibreWolf.* 保護的有效性



**LibreWolf 預設啟動嚴格的安全設定。Firefox 的「增強追蹤保護」（Enhanced Tracking Protection）被推到「嚴格」（Strict）等級，可封鎖數千個追蹤程式、協力廠商 Cookie 和惡意內容。它也會啟動網站與 cookie 隔離 (*Total Cookie Protection*) 來分割每個網域的資料，並限制 WebRTC (限制 *ICE 候選者*，並在有代理時透過代理路由)，以降低 IP Address 洩漏的風險。



**快速的引擎更新：** 本專案非常密切地跟著 Firefox 的發展：LibreWolf 始終以最新的 Firefox 穩定版本為基礎，維護者努力在每次 Firefox 正式發行的 24 到 72 小時內發佈新版本。



## 優點與缺點



### 優點





- 沒有遙測或不必要的連接：** LibreWolf 不會傳輸任何使用資料，確保完全尊重您的隱私。





- 開放原始碼與社群為基礎：** 本專案為 100% 開放原始碼，並由志工維護。這種獨立性保證了任何廣告模式都不會影響開發。





- 預先設定隱私權：** LibreWolf 節省您寶貴的時間：您不需要花費數小時來強化 Firefox 的設定，一切都已經完成。





- 原生廣告攔截/追蹤器：** uBlock Origin 已整合為標準配備，因此您不需要做任何事就能保護自己不受廣告和錯誤的侵害。





- 優異的防指紋保護：** 多虧了 RFP 和許多隱私設定，LibreWolf 大幅減少您在網路上獨特的數位足跡。





- 改善效能與輕量：** 藉由移除遙測與某些非必要的功能，LibreWolf 可以比標準 Firefox 稍微快一點，耗電量也少一點。



### 缺點與限制





- 沒有內建自動更新：** LibreWolf 不會自行更新。為了安全起見，您必須在新版本發行時立即安裝。





- 與某些服務的相容性降低：** 由於其非常嚴格的設定，LibreWolf 在某些網站可能會遇到問題。Netflix 和 Disney+ 串流平台將無法運作，因為 LibreWolf 預設停用 Widevine DRM。





- 沒有內建匿名網路：** 與 Tor 瀏覽器不同，LibreWolf 本身不會透過 Tor 或 VPN 來路由流量。如果您需要匿名網路，您需要手動設定代理/VPN。





- 非持久性 cookies 與 session (預設):** 基於保密理由，LibreWolf 會在您每次關閉瀏覽器時刪除 cookies、歷史記錄與網站資料。您每次登入時都需要重新登入您的帳號。





- 無手機版或雲端同步：** LibreWolf 只在桌上型電腦（Windows、Linux、macOS）上提供。沒有行動應用程式，因此無法透過雲端同步帳號或書籤。



## 安裝 LibreWolf



** 官方網站:** [librewolf.net](https://librewolf.net)



LibreWolf 適用於所有主要的桌面作業系統：Linux、Windows 和 macOS。要下載 LibreWolf，請造訪官方網站：



![LIBREWOLF](assets/fr/02.webp)


*LibreWolf 首頁 (librewolf.net) 顯示瀏覽器標誌、藍色安裝按鈕、以及原始碼與說明文件連結。一個大的藍色箭頭指向安裝按鈕*。



按一下「安裝」按鈕，以存取您作業系統的詳細說明：



![LIBREWOLF](assets/fr/03.webp)


*LibreWolf.* 下載的作業系統選擇頁面



安裝依您的作業系統而有所不同：



### 在 Linux 上


LibreWolf 提供許多發行版的建置。在 Debian/Ubuntu 及其衍生版本上，可以使用官方 APT 套件庫。另外，LibreWolf 在 Flathub 上以 Flatpak 發佈：


```
flatpak install flathub io.gitlab.librewolf-community
```



### 在視窗上


從官方網站下載安裝程式 (.exe)，或使用 .NET Framework 2.0：




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`.



### 在 macOS 上


LibreWolf 以 .dmg 包的形式提供給 Mac。從官方網站下載磁碟映像檔，然後將 LibreWolf 應用程式拖曳到您的 Applications 資料夾。或者，您也可以透過 Homebrew 安裝。




## 配置和首次使用



首次啟動時，您會發現熟悉的 Firefox Interface，但它更為精簡：首頁只包含搜尋列，沒有贊助商的建議。您會在工具列上看到 uBlock Origin 圖示 - 表示封鎖程式已啟動。



![LIBREWOLF](assets/fr/04.webp)


*LibreWolf 首頁與擴充套件和選單。右上角的藍色箭頭表示選單圖示 (三條橫條)



LibreWolf 會自動以 "strict" (anti-tracking) 模式載入您的網頁，預設的搜尋引擎會是 DuckDuckGo。您可以嘗試造訪一個追蹤測試網站 (例如 amiunique.org) 來觀察暴露的足跡 - 它應該比使用標準瀏覽器時更一般。



### 隱私權設定



LibreWolf 已經為隱私做了最佳化的設定。在功能表 → 選項 → 隱私與安全，你會發現 LibreWolf 已設定為加強追蹤保護模式：嚴格。此模式會封鎖 ：




- 網站間追蹤器
- 第三方 cookie
- 已知追蹤內容
- 密碼挖掘
- 數位指紋偵測器



![LIBREWOLF](assets/fr/05.webp)


*安全與隱私索引標籤頁面顯示 LibreWolf.* 安全設定



WebRTC 已停用 (防止 IP 洩漏)，並已設定 Total Cookie Protection。Telemetry 和 Firefox 調查已完全停用。



### Cookie 和歷史記錄管理



根據預設，LibreWolf 會在每次關閉時刪除 cookies 和本機儲存。如果這個行為對您造成困擾，您可以在隱私與安全 → Cookies 與網站資料中調整，取消勾選「關閉 LibreWolf 時刪除 cookies 與網站資料」。



![LIBREWOLF](assets/fr/06.webp)


*再往下一點的相同頁面，顯示在瀏覽器關閉時刪除 cookie 的選項*



### 新增有用的擴充套件



原則上，LibreWolf 不鼓勵增加不必要的擴充套件，因為每個擴充套件都可能是追蹤向量。然而，一些有信譽的擴充套件可以提升您的使用經驗：




- Firefox 多帳號容器** (由 Mozilla 提供) 用於分隔瀏覽
- Decentraleyes** 或 **LocalCDN**，可在本機服務一般圖書館



尤其要避免使用「免費 VPN」擴充元件或可疑的代理伺服器 - uBlock Origin 已涵蓋 99% 的需求。



## 日常使用



### 每日網頁瀏覽


使用 LibreWolf 進行您的日常網際網路活動。與其他瀏覽器最大的不同是，您留下的廣告痕跡要少得多。由於 uBlock 的過濾清單，「接受 cookie」的橫幅廣告在許多網站上都消失了。



### 使用私人標籤來分隔


儘管 LibreWolf 會在 session 結束時刪除所有內容，但在 session 中開啟私人瀏覽器視窗 (Ctrl+Shift+P) 來執行某些任務，以區隔特定的身分，可能會很有用。



### 利用多帳戶容器的優勢


安裝 Multi-Account Containers 擴充套件可大大幫助您將活動分割成密不透風的筒倉。例如，您可以為銀行網站定義「銀行」容器，為 Facebook/Twitter 等定義「社交網路」容器。每個容器都有自己的 cookie、會話和隔離儲存。每個容器都有自己的 cookie、會話和隔離儲存。



### 依據網站微調權限管理


LibreWolf 可讓您依個別情況控制給予網站的權限 (位置、相機、麥克風、通知)。只授予您信任的網站必要的權限。



## 使用 LibreWolf 的最佳實務



1. **Keep LibreWolf up to date:**定期檢查網站的新版本，特別是在穩定的 Firefox 發行之後。



2. **避免將個人身分和私人瀏覽混為一談：** 理想的做法是，您不應在進行敏感研究的同一會話中使用個人帳戶登入。



3. **Don't overload LibreWolf with superfluous extensions:**您安裝的每個擴充套件都可能會帶來安全或指紋風險。



4. **另外使用 VPN 或 Tor 代理：** LibreWolf 並不能讓您對 ISP 匿名。對於網路匿名，您可以在可信賴的 VPN 後面使用 LibreWolf。



5. **保存您的重要資料：** 本機儲存的書籤和密碼。考慮使用外部密碼管理器（KeePassXC、Bitwarden），而不是瀏覽器的基本密碼管理器。



## 與其他瀏覽器的比較



LibreWolf 是隱私導向瀏覽器「工具箱」的一部分：



**LibreWolf vs. Firefox：** LibreWolf 已經加固且沒有任何遙測功能。Firefox 保留了多裝置同步化的優勢以及非常龐大的使用者群，但需要手動設定才能達到 LibreWolf 的保密等級。



**Brave 使用 Chrome/Chromium 程式碼，並透過可選的廣告計畫整合商業模式。LibreWolf 是 Firefox 的社群 Fork，保留 Mozilla 的免費生態系統，與 Google 無關。



**LibreWolf vs Tor 瀏覽器：** Tor 瀏覽器在面對強大的監控時，對於匿名是不可取代的，但在日常使用時，速度慢且不舒服。LibreWolf 適用於日常瀏覽經典網頁，速度更快、更實用。



**LibreWolf vs Mullvad Browser:** Mullvad Browser 在標準化方面更進一步，但代價是可用性降低 (無法保留登入 cookie)。LibreWolf 取得了平衡：非常隱私，但日常可用。



## 總結



LibreWolf 為那些尋找超隱私的「日常」瀏覽器，但又不想使用 Tor 的極端匿名性的使用者，提供了一個絕佳的解決方案。對於積極份子、記者、開發人員或想要經典網頁瀏覽 (快速、相容於現代網站) 並同時擺脫廣告追蹤和 Big Tech 的強大使用者而言，這是個理想的選擇。



雖然它有某些限制 (無法自動更新、與某些服務的相容性降低)，但對於希望重新掌控數位隱私權的人來說，LibreWolf 是非常有價值的工具。它的易用性和預設設定使其成為注重隱私的使用者的明智選擇。



## 資源



### 官方文件




- [LibreWolf 官方網站](https://librewolf.net)
- [Codeberg 上的原始碼](https://codeberg.org/librewolf)
- [官方常見問題](https://librewolf.net/docs/faq)



### 指南與比較




- [隱私權指南](https://www.privacyguides.org/en/desktop-browsers/)
- [比較隱私權測試](https://privacytests.org)



### 社區支援




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)