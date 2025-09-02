---
name: Orion 瀏覽器
description: 如何在 Mac 和 iPhone 上使用 Orion 瀏覽器保護您的隱私？
---

![cover](assets/cover.webp)



## 簡介



在大多數瀏覽器大量收集我們個人資料的情況下，選擇隱私友好的瀏覽器變得非常重要。Chrome 佔據了全球 65% 的市場，但其商業模式是以剝削您的瀏覽資料為基礎。Safari 雖然已整合到 Apple 的生態系統中，但缺乏先進的保護功能，而且無法彈性支援第三方擴充套件。



![Répartition du marché des navigateurs](assets/fr/01.webp)


*網頁瀏覽器市場細分：Chrome 擁有超過 65% 的市場佔有率，其次是 Safari、Edge 和 Firefox*。



**Orion 瀏覽器**是 Apple 使用者的創新選擇。此瀏覽器由 Kagi 開發，結合了 WebKit 引擎的速度與零遙測理念。與競爭對手不同的是，Orion 不會將任何資料傳送至遠端伺服器，並可阻擋 99.9% 的廣告與追蹤程式，包括 YouTube。



它的獨特之處是什麼？Orion 是唯一可安裝 Chrome 和 Firefox 擴充套件的 WebKit**瀏覽器，提供兩者的最佳效能。這種相容性，加上比其他瀏覽器低 2 到 3 倍的記憶體消耗，以及與 Apple 生態系統 (iCloud、Keychain) 的無縫整合，使其成為注重隱私的 Mac 和 iPhone 使用者的理想選擇。



## 為何選擇 Orion Browser？



### 主要效益



**開箱即享最大保護**：Orion 預設會封鎖 99.9% 的廣告 (包括 YouTube) 以及所有第一方和第三方追蹤者。其技術結合了 WebKit 的 Intelligent Tracking Prevention 與 EasyPrivacy 清單，以達到最高效率。獨特功能：Orion 可在執行指紋腳本之前**將其封鎖，讓追蹤無法實現 - 這比其他僅嘗試「遮罩」資料的瀏覽器更激進。



**零可驗證的遙測**：Orion 採取激進的隱私保護方式，設計上採用零遙測。其他瀏覽器會在啟動時提出數百個網路請求 (IP Exponent、瀏覽器指紋、個人資訊)，Orion 則不同，它絕不會「打電話回家」。這個根本性的差異完全消除了資料意外洩漏的風險。



**卓越的效能**：Orion 以最佳化版本的 WebKit 為基礎，在 Mac 上的速度等同甚至超越 Safari。在 Speedometer 2.0/2.1 測試中，Orion 在 Apple Silicon 處理器上一直名列第一。原生廣告封鎖功能可進一步加速頁面載入 20% 至 40%。



*** 全球擴充套件支援**：作為一項重大創新，Orion 允許您從 Chrome Web Store **和**Mozilla 附加元件安裝擴充套件。WebExtensions 支援目前是實驗性的，目標是在 beta 版發佈時達到 100% 相容。您甚至可以在 iPhone 上使用許多熱門的擴充套件，例如 uBlock Origin、Bitwarden - 這是 iOS 上的全球首創，雖然有些可能無法完美運作。



### 需要注意的限制





- 供應有限**：目前保留給 macOS 和 iOS/iPadOS。Linux 版本已達到開發里程碑 (2025 年達到里程碑 2)，但尚未提供公開版本。由於資源不足，Windows 和 Android 尚未進行開發。
- 封閉的原始碼**：雖然有些元件是開放原始碼，但 Orion 仍以專屬程式為主，這也是隱私權社群爭論的焦點。
- 實驗性擴充套件** ：擴充套件支援仍處於測試階段，經常發生不相容的情況。擴充套件可能會影響效能，有些甚至完全無法運作。
- WebKit 安全性**：與 Chromium 不同，WebKit 並未提供如此強大的每網站程序隔離功能，在某些情況下可能會造成安全風險。
- 封鎖測試**：Orion 在線上廣告測試中故意表現不佳 (26-35%)，因為 Kagi 認為這些測試是「有基本缺陷」的。日常使用中的實際效能遠勝於此。



## Orion 瀏覽器安裝



### 在 macOS 上



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*Kagi 首頁介紹 Orion Browser 為「無廣告瀏覽器，提供全面隱私保護和通用擴充支援」*。





- 前往 [kagi.com/orion](https://kagi.com/orion/)
- 按一下「**下載 Orion for macOS**」。



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Orion Browser 下載頁面顯示 MacOS 和 iOS 的可用性，並提供至 App Store 的連結*。





- 開啟下載的 `.dmg` 檔案
- 將 Orion 應用程式拖曳到「應用程式」資料夾中
- 首次啟動時，macOS 會要求您確認開啟



**Alternative Homebrew** ：


```bash
brew install --cask orion
```



### 在 iPhone/iPad 上





- 開啟 ** 應用程式商店**
- 搜尋 "**Orion Browser by Kagi**"
- 安裝免費應用程式 (iOS 15+ 相容)



### 初始設定



第一次啟動時，Orion 會引導您完成幾個步驟：



**1.歡迎畫面


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion 瀏覽器歡迎畫面強調主要功能：更快的瀏覽速度、零遙測、廣告封鎖和延伸支援*。



**2.Interface** 客製化


![Options de personnalisation](assets/fr/05.webp)


*自訂畫面可讓您設定標籤和 Interface 的外觀，以符合您的喜好*。





- 資料匯入**：從 Safari、Chrome 或 Firefox 輕鬆傳輸我的最愛和密碼
- ICloud 同步**：啟用後可在所有 Apple 裝置上找到您的最愛和標籤



**3.安裝於行動裝置**


![Installation sur iOS](assets/fr/06.webp)


*iOS 上的安裝畫面顯示 QR 代碼，可從 App Store 快速下載 Orion Browser*



**4.Interface 歡迎與必備工具



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface 首頁：箭頭表示可從 Address 欄位直接存取的三個主要工具*。



設定完成後，您會發現 Orion 簡化的 Interface 配備了**三個基本工具**（箭頭所示）：





- Shield 🛡️**：顯示隱私權報告，其中包含目前頁面上被封鎖的項目數量
- 刷 🖌️**：自訂頁面顯示（主題、字型、移除分心的 Elements）
- Gear ⚙️**：設定網站特定參數 (權限、封鎖等)



這些工具隨時可用，可讓您逐一控制網站的瀏覽體驗。



**重要**：Orion 是免費的，不需要註冊或建立帳戶即可操作。



![Orion+ dans les préférences](assets/fr/08.webp)


*偏好設定中的 Orion+ 訂閱畫面，提供可選訂閱以支援開發*。



**Orion+ (選購)**：為了支援專案開發，Kagi 提供 Orion+ ($5/month, $50/year, or $150 lifetime)。




- 直接與開發團隊溝通
- 根據您的需求影響瀏覽器的演進
- 存取具有最新實驗性功能的 Nightly 版本
- 受益於最新的 WebKit 引擎
- 在回饋論壇上獲得與眾不同的徽章



Orion+ 保證專案的獨立性："您的財務貢獻可協助我們保持獨立，並信守承諾，成為用戶心目中的最佳瀏覽器」。正是這種使用者出資的模式，讓 Orion 保持無廣告、無遙測。



## 最大保密性配置



### 基本參數



透過 **Orion → 偏好設定** (或 ⌘,) 存取偏好設定：



**1.搜尋 - 私人搜尋引擎**



![Configuration du moteur de recherche](assets/fr/09.webp)


*預設搜尋引擎配置：選擇 DuckDuckGo 以獲得最大隱私*。





- 預設引擎**：選擇 **DuckDuckGo**、**Startpage** 或 **Kagi**，以獲得最佳隱私（避免使用 Google/Bing）。
- 搜尋建議**：停用搜尋建議，以防止鍵盤敲擊洩漏至搜尋引擎伺服器



**2.隱私權 - 一般**保護



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orion 隱私權設定顯示內容封鎖程式，包含 119,156 個有效規則、追蹤器移除選項和自訂使用者代理程式*。



**內容封鎖程式預設啟用** ：




- EasyList** ：119k+ 廣告封鎖規則
- EasyPrivacy**：防追蹤保護
- 管理篩選清單**：新增其他清單（建議使用 Hagezi）



** 隱私權選項** ：




- 從 URL 移除追蹤者**："僅供私人瀏覽」可清除複製的連結
- 分享碰撞報告**："請求批准後」尊重您的同意
- 自訂使用者代理**：可修改以繞過某些封鎖



![YouTube avec Privacy Report](assets/fr/10.webp)


*使用 Orion 觀看 YouTube 的範例：無廣告顯示，隱私權報告顯示許多 Elements 被封鎖*。



**3.網站設定 - 依網站控制**



![Website Settings pour YouTube](assets/fr/11.webp)


*顯示相容性選項、內容封鎖和特定網站權限*的 YouTube 網站設定



**快速存取**：按一下 Address 欄中的齒輪 ⚙️，調整 ：




- 相容性模式**：透過暫停擴充功能解決顯示問題
- 內容封鎖程式**：必要時停用特定網站的封鎖功能
- JavaScript/Cookies**：按網站進行粒度控制
- 權限**：攝影機、麥克風、個別設定的位置



**4.進階自訂篩選器** (請參閱下文)



**建立自訂篩選條件** (隱私權 → 管理篩選條件清單 → 自訂篩選條件) ：



**Simplified syntax** (Adblock Plus 相容) ：




- `reddit.com##.promotedlink`：隱藏贊助的 Reddit 帖子
- `||ads.example.com^`：完全封鎖廣告網域
- `@@@||site-utile.com^`：為網站建立例外



**提示：請造訪 [FilterLists.com](https://filterlists.com)，取得數以千計隨時可用的專用清單。



### 建議擴展



Orion 原生支援 Chrome 和 Firefox 擴充套件。請直接從官方商店安裝：



**Essentials** ：




- uBlock Origin**：為原生封鎖程式加入細粒度控制
- Bitwarden**：開放原始碼密碼管理器
- ClearURLs**：刪除 URL 追蹤參數



**選項** ：




- LocalCDN**：在本機服務共用程式庫
- Cookie AutoDelete**：關閉標籤頁後自動刪除 cookie
- NoScript**：完全控制 JavaScript 執行 (進階使用者)



若要安裝.NET Framework，請選擇 「安裝」：




- 請造訪 [chrome.google.com/webstore](https://chrome.google.com/webstore) 或 [addons.mozilla.org](https://addons.mozilla.org)
- 按一下「新增至 Chrome/Firefox」。
- Orion 會自動截取並安裝擴充套件



**注意**：由於擴充套件支援屬於實驗性質，許多擴充套件可能無法正常運作或影響效能。如果發生問題（網站不再運作、速度變慢），請逐一停用擴充套件，以找出問題來源。



## 每日使用



### Interface 和獨特功能




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orion 刷子選單可自訂顯示內容：字型大小、主題 (亮/暗)、停用黏貼式標題，以及移除分散注意力的 Elements*



**畫筆工具：進階自訂**



Orion 的 **brush** 工具是一項獨特功能，可讓您自訂每個網站的顯示內容：



**Theme 選項** ：




- 在每個網站的淺色和深色主題之間切換
- 自動適應您的系統偏好



** 排版控制** ：




- 字體大小**：使用 A- 和 A+ 按鈕調整可讀性
- 字體樣式**：變更字型系列 (預設或自訂)



**Interface 清潔** ：




- 停用黏住的標題**：移除捲動時停留在頂端的標題
- 刪除 Elements**：永久移除惱人的 Elements（廣告、快顯、cookie 廣告橫幅）
  - 按一下「+ 刪除」，然後選擇要隱藏的項目
  - 對於有持續性廣告或可視化追蹤 GW 的網站非常有用-13



**持久性**：所有這些設定都會儲存在每個網域中，並在您下次造訪時自動重新套用。



**進階標籤管理** ：




- 垂直標籤**：透過功能表列啟動 (側邊標籤功能)
- 壓縮標籤** ：在偏好設定 → 標籤 → 佈局「精簡」，以節省空間
- 標籤群組**：依主題組織您的課程
- 多重設定檔**：透過功能表列 (設定檔功能) 建立完全獨立資料的個人身分



**低耗電模式**：受到 iPhone 的啟發，此模式會在 5 分鐘後自動暫停不活動的標籤頁，最多可減少 90% 的能源消耗。在 Mac 上透過 Orion 的功能表列啟動，或在 iOS 的設定中啟動。



**內建工具**（編輯功能表及其他） ：




- 編輯頁面上的文字**：暫時修改任何文字（編輯功能表）
- 允許複製與貼上**：繞過複製限制（編輯功能表）
- 複製清潔連結**：在連結上按滑鼠右鍵移除追蹤參數
- 焦點模式**：免分心、全螢幕導航
- 畫中畫**：在浮動視窗中觀看影片
- 在 Internet Archive 中開啟**：直接存取存檔版本
- 隱私權報告**：按一下遮罩 🛡️，以查看各頁面所封鎖的項目



### 私人瀏覽管理



Orion 的私人導航 (⌘⇧N) 提供：




- 完全隔離 cookie 和會話
- 關閉時自動刪除
- 歷史和快取停用
- 強化防指紋功能



**Tip**：若要進階區隔，可透過功能表列 (設定檔功能) 建立 ** 獨立的設定檔**。每個設定檔都會在 Dock 中顯示為獨立的應用程式，並擁有自己的設定、擴充套件和資料，完全與外界隔離。



### 效能最佳化與隱私權



讓 Orion 保持快速和隱密




- 擴充** ：限制至最低限度 (可能會降低效能)
- 低耗電模式**：長時間使用時啟動 (可節省 90% 電力)
- 隱私報告**：按一下防護罩 🛡️ 即時查看阻塞情況
- 視覺自訂**：使用 🖌️ 筆刷調整顯示，並移除分心的 Elements
- 複製清潔連結**：按滑鼠右鍵複製沒有追蹤器的連結
- 獨立設定檔**：使用專屬的設定檔來分隔您的活動
- 網站設定**：按一下齒輪 ⚙️，依網站調整權限
- 定期清理**：透過 Orion 清除快取 → 清除瀏覽資料



## 與替代品比較



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**對比 Safari**：Orion 以其先進的封鎖程式和擴充支援提供優異的保護，同時維持 WebKit 的效能。



**Versus Chrome**：由於支援 Chrome 擴充套件，無與倫比的隱私性不會影響相容性。



**Versus Firefox**：在 Mac 上速度更快，Interface 更直覺，但細緻的控制較少，而且不是開放原始碼。



**Versus Brave**：理念類似，但 Orion 避免了加密/BAT 的爭議，並提供更好的 Apple 整合。



## 建議用例



**適用於** ：




- Apple 使用者尋求比 Safari 更多的隱私
- 想要在沒有擴充套件的情況下封鎖所有廣告 (包括 YouTube) 的人
- 開發人員需要具備整合式隱私權保護功能的 WebKit 開發工具
- IPhone 使用者希望在行動裝置上使用桌上型電腦擴充功能 (獨特的創新)
- 需要將活動分門別類的專業人員 (多重設定檔)
- 尋求更佳電池管理 (低功率模式) 的行動使用者



**Avoid if** ：




- 您主要使用 Windows/Linux (無版本)
- 完全開放原始碼對於您的威脅模型而言至關重要
- 您依賴的特定擴充套件可能無法運作
- 您需要 Apple 生態系統以外的跨平台同步功能
- 您偏好經過驗證、穩定的解決方案 (自 2021 年起為永久測試狀態)



## 注意事項與安全



### 獨特的安全功能



**革命性的防指紋保護**：Orion 是唯一能在指紋腳本掃描系統之前完全阻止其執行的瀏覽器。這種「無腳本執行 = 無指紋可能」的方法優於其他瀏覽器使用的傳統遮罩方法。



**透明白名單**：Orion 維護一個小型的公開網站清單 (browserbench.org、wizzair.com)，這些網站會自動解除封鎖以避免故障。這種透明性可讓使用者確切瞭解封鎖何時、為何會減輕。



**未經審核的擴充套件**：支援 Chrome/Firefox 擴充套件會帶來額外的風險，因為這些擴充套件並非針對 WebKit 設計，且未針對此環境進行特定審核。



### 維護與更新





- 自動更新**：Orion 透過 Sparkle 在 macOS 上自動更新
- 漏洞追蹤**：定期檢查版本注意事項中的安全修補程式
- 錯誤回報**：使用 [orionfeedback.org](https://orionfeedback.org) 回報問題




## 總結



Orion Browser 代表著 macOS 和 iOS 上的隱私權向前邁進了一大步。它的零遙測方式，加上超高效的原生封鎖程式和獨特的通用擴充支援，使它成為注重隱私的 Apple 使用者的絕佳選擇。



**重要**：Orion 自 2021 年起仍處於永久 beta 版，具有擴充相容性限制和 WebKit 的固有風險。請根據您的威脅模型評估這些權衡。



對於在 Mac 或 iPhone 上的日常使用，它可能是 Apple 生態系統中在機密性、效能和易用性之間的最佳折衷方案，前提是您接受它的限制。



請記住：保護您的隱私不僅取決於您的瀏覽器。結合 Orion 與最佳實務 (強大密碼、2FA、必要時 VPN) 以獲得最佳的線上安全性。



## 資源與支援



### 官方文件




- 官方網站**：[kagi.com/orion](https://kagi.com/orion/)
- 完整常見問題**：[browser.kagi.com/faq](https://browser.kagi.com/faq)
- 社區論壇**：[community.kagi.com](https://community.kagi.com)
- 錯誤追蹤**：[orionfeedback.org](https://orionfeedback.org)
- GitHub Orion** ：[github.com/OrionBrowser](https://github.com/OrionBrowser) - 開源元件
- 博客 Kagi** ：[blog.kagi.com](https://blog.kagi.com) - 新聞與更新



### 建議的驗證測試



設定完成後，測試您的設定：




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - 指紋測試
- [DNS 洩漏測試](https://www.dnsleaktest.com/) - 檢查 DNS 是否洩漏
- [BrowserLeaks](https://browserleaks.com/) - 完整的隱私權測試套件



### Plan ₿ Network 的替代方案


若要獲得最大程度的保護，請參閱我們的其他指南：




- [Firefox Hardened](https://planb.network/tutorials/computer-security/firefox) - 進階多平台設定
- [Tor 瀏覽器](https://planb.network/tutorials/computer-security/tor-browser) - 完整的網路匿名性
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - 最大程度的指紋保護



如果您想進一步瞭解瀏覽器的歷史和操作，以及日常生活中的主要數位物件，我邀請您探索我們新的免費培訓課程 SCU 202，可在 Plan ₿ Network 上獲得：



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1