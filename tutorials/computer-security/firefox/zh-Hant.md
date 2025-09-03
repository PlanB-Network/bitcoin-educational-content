---
name: Firefox
description: 如何設定 Firefox 以保護您的隱私？
---

![cover](assets/cover.webp)



## 簡介



我們都會花上數小時在線上，卻往往沒有意識到我們的瀏覽器揭露了我們什麼。我們的每一次點擊、每一次搜尋、每一次造訪的網站，都為個人資料收集提供了龐大的產業。



![Statistiques navigateurs 2024](assets/fr/01.webp)


*網頁瀏覽器市場佔有率：Chrome 佔據了 65% 的市場，其次是 Safari 和 Edge。資料來源[gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



如圖所示，Google Chrome 擁有全球 65% 以上的使用率，佔有極大的優勢。這種霸權意味著大多數的網際網路使用者將他們的瀏覽資料託付給 Google，而 Google 的商業模式是以針對性的廣告為基礎。Firefox 僅佔 3% 的市場，是由 Mozilla 開發的另一種選擇，Mozilla 是一個非營利組織，對於剝削您的資料沒有任何商業興趣。



但選擇 Firefox 只是第一步。在預設情況下，即使是 Firefox 也需要調整才能最大化您的保護。本指南從最簡單到最進階，一步一步帶領您將 Firefox 變成名副其實的防追蹤盾牌，同時保留愉快的瀏覽體驗。



### 為什麼是 Firefox？





- 免費且開放原始碼** (Gecko 引擎)：可稽核且透明的程式碼
- 非營利組織**：Mozilla 基金會，一般利益的使命
- 內建原生保護**：增強追蹤保護 (ETP)、全面 Cookie 保護 (TCP)、狀態分割、僅 HTTPS 模式、DNS over HTTPS (DoH)
- 進階自訂**：與 Chrome 不同，Firefox 可讓您深入修改其行為



### 開始前的重要原則





- 沒有通用的配方**：您修改得越多，您就越有可能脫穎而出 (指紋)。我們的目標是在不顯眼的情況下提供更好的保護。
- 循序漸進**：變更設定，測試您常用的網站，然後繼續。不需要一次過變更所有設定。
- 個人平衡**：在隱私權和易用性之間找到您的折衷。



## 快速安裝



![Téléchargement Firefox](assets/fr/02.webp)



**官方下載：**前往 [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/)。在此頁面中，選擇您的作業系統 (Windows、macOS、Linux)，以存取適當的下載頁面，其中包含特定的安裝說明。





- Windows**：下載 `.exe` 安裝程式，按兩下並依安裝精靈操作
- macOS**：下載 `.dmg` 檔案，開啟並將 Firefox 拖曳到「應用程式」資料夾。
- Linux**：有幾種選擇 - package `.deb`/`.rpm`、Flatpak (Flathub)、Snap，或透過套件管理員 (apt、dnf、pacman)。偏好 Mozilla 官方來源。



**小提示：** 安裝完成後，請透過說明 → **關於 Firefox** 檢查更新（對安全修補程式很重要）。



![Configuration initiale Firefox](assets/fr/03.webp)


*啟動 Firefox 時的第一個畫面：將 Firefox 設定為預設瀏覽器，並將其加入捷徑，然後按一下「儲存並繼續」*。



![Création compte Firefox](assets/fr/04.webp)


*可選步驟：建立或登入 Firefox 帳戶。您可以按一下右下方的「不是現在」跳過此步驟*。



![Page d'accueil Firefox](assets/fr/05.webp)


*設定完成後的Firefox主畫面。注意右上方的☰選單，可以進入設定和擴充套件，自訂Firefox*。



## 預設已啟動的保護（令人安心）





- 網站隔離 (Fission)**：逐步部署中。此功能在單獨的程序中執行每個網站，以防止一個惡意標籤存取另一個的資料。透過 `about:support` 檢查其狀態 (搜尋「Fission」)。如果未啟用，您可以在 `about:config` 中使用 `fission.autostart = true` 手動啟用。
- Total Cookie Protection (TCP)**：預設為啟用。Cookie 和其他儲存內容只限於第一方網站 (每個網站一個「罐子」)，可中和跨網站追蹤。必要時會透過儲存存取 API 作臨時例外處理 (整合登入按鈕)。
- 跳出/重定向追蹤保護**：Firefox 會自動偵測並清理跳出網站 (在目的地前透過追蹤器將您重新導向的連結) 所留下的 cookies，無須您採取任何行動即可減少此追蹤管道。



## 第 1 級 - 必備 (≤ 10 分鐘)



目標：在不破壞網路的情況下大幅提升隱私權。針對 90% 的使用者。



要進入設定，點擊右上方的菜單☰，然後點擊 **「設定 」** ：



![Paramètres généraux](assets/fr/07.webp)


*Firefox 設定頁 -「一般」標籤。這是您設定大部分隱私權選項的地方*。



**追蹤保護 (ETP)**




- 將 **ETP** 切換為 **Strict**。您可以封鎖更多追蹤器 (跨站 cookie、指紋、加密、社交小工具......)。
- 如果網站發生故障（視訊、登入按鈕......），請透過 🛡️ 盾停用僅針對該網站的保護，然後再刷新索引標籤。



以下是不同的 ETP 安全層級：




- 標準** (平衡、最大相容性)
  - 攔截：社交追蹤器、跨站 cookies (所有視窗)、私人瀏覽中的追蹤內容、加密貨幣礦工、指紋偵測器。
  - 包含 **Total Cookie Protection** (TCP)：每個網站一罐。
- 嚴格** (建議用於保密)
  - 同時封鎖所有視窗中的追蹤內容 + 已知及可疑的指紋。
  - 可能會破壞某些網站；請使用 🛡️ 護盾來做局部例外處理。
- 自訂** (進階)
  - 微調：Cookie、追蹤內容、未成年人、指紋（已知/疑似）。



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies 和網站資料




- 啟用 **「關閉時刪除 cookie 和網站資料 」**，以便每次重新啟動時都能乾淨地重新啟動。
- 如果您願意，可為 2-3 個必要網站（電子郵件、銀行）新增 ** 例外**。


**自動資料輸入、建議和首頁**




- 停用 ** 自動填寫** (身分證、地址、卡片)。改用密碼管理器。
- 搜尋**：停用 **「顯示搜尋建議」**。
- Address 欄**：切換 **「贊助建議」** 和 **「內容建議」**。
- 首頁**：停用 **Pocket** 和 **贊助內容**。



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**僅限**HTTPS




- 啟動 **「僅在所有視窗中使用 HTTPS 模式 」**。


![Configuration DNS over HTTPS](assets/fr/09.webp)



** 電話測量和廣告測量




- 在「Firefox 收集資料」中，**取消勾選所有**。
- 停用 **「隱私友善廣告措施」** (PPA)。
- 安全瀏覽**：保持啟用 (建議)。Firefox 會透過散列查詢和本機檢查，針對威脅清單檢查網站，以防禦網路釣魚和惡意軟體，並將隱私影響降至最低。



**全球隱私權控制（選購）**




- 啟動 **GPC** 以表示您拒絕出售/分享資料。



**搜尋引擎




- 切換至 **DuckDuckGo**、**Startpage**、**Qwant** 或 **Brave Search**（設定 → 搜尋）。



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**私人導航**




- 私人視窗 (Ctrl/Cmd+Shift+P) 用於一次性會話 (禮物、副帳號...)。避免 「總是隱私 」模式：擴充功能可能會失效，cookie 例外也會不太有用。



**Essential extensions** (從官方目錄安裝)




- uBlock Origin**：封鎖廣告和目前的追蹤，輕量級。
- Privacy Badger**：學習封鎖跟蹤您的內容；傳送 Do Not Track / GPC。
- ClearURLs** (選用)：Firefox (ETP Strict) 和 uBO 已經清理了很多；如果您仍然看到「骯髒」的 URL (utm、fbclid)，請保留它。
- Firefox 多帳號容器**： **isolates cookies/sessions and storage per container; parallel multi-accounts; less cross-site tracking**.官方擴充套件：`https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`。



![Extension Multi-Account Containers](assets/fr/12.webp)



**密碼和 2FA**




- 使用專用的密碼管理器** (Bitwarden, KeePassXC)。 **避免**在瀏覽器中儲存密碼。 **盡可能啟用 2FA**。



## 第 2 級 - 強化 (隔間與網路)



目標：分隔活動並減少網路洩漏。



**DNS over HTTPS (DoH)**




- 預設狀態**：在某些地區 (美國、加拿大、俄羅斯、烏克蘭) 自動啟動。其他地區則需要手動啟動。
- 設定** ：設定 → 一般 → 網路設定 → **啟用 DoH** → **Cloudflare**或**Quad9** → **最大保護**。
- 最大保護 = 僅 TRR**（無回退至系統 DNS）。如果企業/飯店網路阻擋，請切換回 **Standard** 或停用 DoH。
- 備援**：如果您已經在使用有自己安全 DNS 的可信賴 VPN，DoH 可以作為備援。
- 驗證測試**：`https://www.dnsleaktest.com/` 應該只顯示所選擇的 DoH 提供者。



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**使用容器和配置文件進行分隔




- 多帳戶容器**：建立空間 (個人、工作、財務、社交網路、購物、一次性)。為您的經常性網站設定 **「永遠在此容器中開啟」**。官方擴充名：`https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`。
- 為什麼要使用它們？
  - 按空間強制隔離** cookie/會話/儲存。
  - 減少跨站追蹤**：限制巨頭 (Facebook、Google)。
  - 在同一服務上同時擁有多個帳號**。
  - 分段式身分之間的 CSRF/XSS** 風險較低。
  - 提示：至少要為社交網路/Google、工作、財務設置專屬容器。
- Facebook Container** (選購)：專門用於 FB/Instagram 的簡化版本。
- 獨立的設定檔**：透過 `about:profiles` (主要設定檔、最小「超安全」設定檔、測試設定檔)。資料與擴充套件完全分隔。



**進階擴充** (待保留)




- Cookie AutoDelete**：關閉標籤頁時，立即刪除網站的 Cookie (如果 Firefox 長時間開啟，此功能很有用)。
- LocalCDN**：在本地提供目前的程式庫 (減少對 Google/Microsoft 的呼叫)。部分相容性。



**手機 (Android)**




- Firefox Android + uBlock Origin**：移動時提供類似的保護。



## 第 3 級 - 專家 (about:config & Arkenfox)



目標：在可接受的折衷方案下進行進階硬化。建議使用 ** 獨立檔案**。



在以下兩種方法中只選擇一種：



**方法 A - 手動修改**：透過 `about:config` 進行一些針對性的調整 (更簡單、更精確的控制)


**方法 B - Arkenfox user.js**：全自動配置（更複雜，最大程度的保護）



➡️ **Arkenfox已包含下面提到的所有關於：配置的變更** + 數百個更多。如果您選擇 Arkenfox，請忽略 about:config 部分。



### 方法 A：透過 about:config 進行手動修改



在 Address 欄中輸入 `about:config` → 接受風險。



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- 抗指紋（繼承自 Tor 瀏覽器）


```text
privacy.resistFingerprinting = true
```


效果：UTC 時區、**letterboxing** (標準視窗大小)、標準化 User-Agent/ 政策、Canvas/WebGL/AudioContext 限制。更統一，但有一些「怪癖」（偏移時間，有時候會有一點英文）。





- 停用 WebRTC（避免 IP 洩漏；破壞 Web visio）


```text
media.peerconnection.enabled = false
```





- Referer 加上相容 (預設)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


嚴格選項（可能會破壞付款/SSO）：


```text
network.http.referer.XOriginPolicy = 2
```





- 限制喋喋不休的 API 和猜測


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



黃金法則：如果有東西壞了，就回到上次的變更。



### 方法 B：Arkenfox user.js (全自動設定)



**Arkenfox**專案提供一個社群維護的「user.js」檔案，可自動套用數百個以隱私與安全為導向的 Firefox 偏好設定。重新啟動時，Firefox 會從您的設定檔讀取此檔案，並套用這些設定。





- 有什麼意義？從**一致的硬化基礎**開始，無需「到處點選」；減少疏失；節省時間。
- 變更內容（範例）：遙測切斷、cookie/cache/referrer/HTTPS 強化、**RFP** + letterboxing、**WebRTC 停用**、DoH/TLS 調整、聊天式 API 受限。
- 何時使用：如果您想要 Firefox 在 10 分鐘內強化，並接受少數例外 (DRM/串流、Web visio、SSO/付款)。
- 優點：快速、一致、**更新** (ESR 對齊)、非常完善的**記錄** (wiki + 註解)、**可透過覆寫**自訂。
- 限制：相容性 (某些網路應用程式)、舒適性 (UTC、視窗大小)，以及提醒事項： **它不是 Tor**（無網路匿名性）。



安裝 (最好是在**專用設定檔上**)


1.儲存個人資料/我的最愛並列出您的 Cookie 例外網址。


2.從 `https://github.com/arkenfox/user.js` 下載 `user.js` (ESR/stable 版本)。


3.透過 `about:profiles` 找到您的設定檔資料夾：




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4.關閉 Firefox 並將 `user.js` 移至設定檔資料夾的根目錄。


5.重新啟動；透過 `about:config` 或 overrides 檔案自訂。



更新




- 遵循 Arkenfox 發行版本 (ESR 對齊)，取代 `user.js`，重新啟動 Firefox；閱讀發行說明。



**透過覆寫功能進行自訂**



Arkenfox 的預設值是刻意限制的。若要調整某些設定以符合您的需求 (串流、visio、特定網站)，您可以在與 `user.js` 相同的資料夾中建立一個 `user-overrides.js` 檔案。此檔案可讓您在不修改主檔案的情況下，「覆寫」某些 Arkenfox 偏好設定。



建立 `user-overrides.js` 並加入您的客製化設定：


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



最佳實踐




- 使用獨立的 **「Arkenfox」設定檔**，並保留「正常」設定檔以保舒適。
- 最小化擴充套件 (uBlock Origin OK) 以限制攻擊面和唯一性。
- 必要時逐個網站加入例外 (如果使用，請屏蔽 🛡️、uBO、NoScript)。
- 每次變更後測試：WebRTC/DNS 洩漏、Cover Your Tracks、CreepJS。



## 最佳實踐





- 更新**：Firefox 和擴充套件為最新版本。
- 延長**：合理可靠；小心「可疑」的贖回。
- 下載**：請謹慎；在 VirusTotal 上測試敏感檔案。
- 密碼**： **專用管理器** (Bitwarden, KeePassXC)；啟用**2FA**；避免儲存在瀏覽器中。
- 衛生**：將 Google/Facebook 限制在容器中；定期關閉/開啟，以「重設」上下文。



## 限制與替代方案





- 強化瀏覽器 ≠ 網路匿名性：沒有**VPN**，您的 IP 仍然可見；即使有了它，關聯性仍然可能存在。
- 修改太多會讓你**獨一無二。 **RFP** 標準化；隨機化工具 (例如 Chameleon) 可以...讓您與眾不同。測試、比較、調整。
- 替代品/補充品：
 - Tor 瀏覽器：透過 Tor 進行網路匿名；速度較慢。請參閱我們完整的安裝與設定指南** ：



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad 瀏覽器：「沒有 Tor 的 Tor」，與 VPN 結合；標準化的足跡。了解如何在我們的專用教學中安裝它** ：



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- 建議組合：Firefox (Level 2) + VPN 適用於日常使用；Tor/Mullvad 適用於敏感活動；獨立設定檔可進行分隔。



## 總結



只要遵循這份逐步指南，您就能將 Firefox 變成真正防禦數位監控的堡壘。從基本的第 1 層設定到進階的 Arkenfox 配置，每一項變更都能在不影響瀏覽體驗的情況下強化您的隱私。



**您的隱私現在得到更好的保護**：攔截廣告追蹤者、分隔 Cookie、中和 IP Address 洩漏、停用遙測功能。Firefox 不再只是瀏覽器，而是為您量身打造的數位防禦工具。



**請記住：保密性永遠不是必然的。請定期測試您的防護功能、更新您的設定，並隨著您的習慣改變而毫不猶豫地調整您的配置。您的線上匿名性既取決於您的工具，也取決於您的習慣。



## 資源



### Plan ₿ Network




- SCU 202 - 改善您的個人數位安全：要進一步了解本教程所涵蓋的數位安全概念**



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla 文件




- [Enhanced Tracking Protection](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop) ：強化追蹤保護官方指南
- [狀態分割](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning)：狀態分割的技術文件
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security) ：網頁安全的完整參考資料



### Arkenfox




- [Wiki 與安裝指南](https://github.com/arkenfox/user.js/wiki)：完整的 Arkenfox 專案文件
- [Deposit and releases](https://github.com/arkenfox/user.js)：下載 user.js 檔案並追蹤更新



### 指南與社群




- [PrivacyGuides - 桌面瀏覽器](https://www.privacyguides.org/en/desktop-browsers/)：瀏覽器推薦與比較
- Reddit**：r/firefox、r/privacy 以獲得回饋與支援
- PrivacyGuides 論壇**：深入的技術討論



### 測試工具




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/)：數位指紋與反追蹤效能
- [DNS 洩漏測試](https://www.dnsleaktest.com/)：DNS 洩漏測試與 DoH 效率
- [BrowserLeaks](https://browserleaks.com/)：完整的測試套件 (WebRTC、Canvas、字型等)
- [BadSSL](https://badssl.com/)：SSL/TLS 憑證驗證測試
- [CreepJS](https://abrahamjuliot.github.io/creepjs/)：進階分析 50+ 指紋向量
- [Cloudflare DNS 測試](https://1.1.1.1/help) ：檢查 Cloudflare DoH 是否正常運作