---
name: Mullvad Browser
description: 如何使用 Mullvad 瀏覽器來保護隱私
---

![cover](assets/cover.webp)



在數位監控無所不在的世界裡，保護您的線上隱私從未如此重要。公司使用精密的技術追蹤您：





- 第三方 cookie：外部網站存儲的小檔案，用於跟隨您從一個網站到另一個網站。
- 指紋：收集您瀏覽器和裝置的獨特特性（螢幕解析度、安裝的字型、外掛程式等），以便在沒有 cookies 的情況下識別您的身份。
- 追蹤腳本：分析您瀏覽行為 (點選、捲動、花費時間) 的隱形 JavaScript 程式碼
- **IP Address 分析**：地理位置和您的網際網路服務供應商識別



然後，這些資料會結合起來，建立您在線上行為的詳細資料，並在您不知情的情況下，將這些資料賺錢。這個現實提出了一個基本問題：您如何才能在上網的同時保持您的匿名性和機密性？



答案主要在於您所選擇的網路瀏覽器。這個我們每天用來存取資訊、購物或溝通的工具，在保護我們的個人資料方面扮演著決定性的角色。不幸的是，Google Chrome 等流行瀏覽器 (約佔全球市場的 65%)，都是以大量收集使用者資料為基礎的商業模式所設計。



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad 瀏覽器以其異常有效的追蹤器封鎖功能脫穎而出，遠遠超越一般消費性瀏覽器*。



面對這樣的挑戰，新的競爭者正以不同的哲學崛起：將隱私放在設計的核心。其中，Mullvad 瀏覽器以創新的解決方案脫穎而出，結合了最佳的隱私權保護與流暢、易用的瀏覽體驗。



傳統的瀏覽器會透過收集您的資料來尋求個人化的體驗，而 Mullvad Browser 則不同，它採取相反的方式：讓所有使用者看起來與網站完全相同，因此幾乎不可能進行個人化追蹤。



在本教程中，我們將一併探索 Mullvad Browser 如何改變您瀏覽網際網路的方式，在不犧牲易用性的前提下，為您提供強大的防監視保護。




## 介紹 Mullvad 瀏覽器



**Mullvad Browser**是一款注重隱私的網路瀏覽器，由瑞典公司Mullvad VPN與Tor Project合作開發，並免費發佈。該瀏覽器於 2023 年 4 月推出，以 **「沒有 Tor 網路的 Tor 瀏覽器」** 自居，旨在盡量減少線上追蹤和指紋，同時允許使用者透過可信賴的 VPN 而非 Tor 網路進行瀏覽。



Mullvad Browser 是一款免費的開放原始碼瀏覽器，以 Firefox ESR（Mozilla Firefox 的長效版本）為基礎，並經過 Tor Project 專家的強化。具體而言，它包含 Tor 瀏覽器的大部分**保護功能，但不透過 Tor 網路流量**。反之，使用者可以（也應該）將它連結至可信賴的加密 VPN，以匿名化其 IP Address。



就使用者體驗而言，Mullvad Browser 類似經典瀏覽器，提供流暢的導覽。它可在 Windows、macOS 和 Linux（無行動版）上免費使用。您無需成為 Mullvad VPN 訂戶即可使用；然而，**在未遮蔽 IP 的情況下使用 Mullvad Browser 並無法提供完全的匿名** - 因此強烈建議您搭配可靠的 VPN 一起使用。



### 目標：隱私與反追蹤



Mullvad 瀏覽器的設計有一個主要目標： **保護使用者的線上隱私**，並對抗常見的追蹤和側寫技術。其主要目標包括





- 大幅減少網站和廣告代理商的廣告追蹤和追蹤。預設情況下，Mullvad Browser 會封鎖可辨識您身份的第三方追蹤器、追蹤 cookies 和指紋腳本。





- 將瀏覽器的指紋標準化，**「融入人群」**。指紋就像是結合瀏覽器所有特徵而產生的獨特「身分證」。Mullvad Browser 可確保所有使用者都擁有完全相同的「身分證」，讓使用者無法個別區分。





- 提供即時保護，無需額外的擴充套件。**Mullvad Browser 採用「即開即用」的配置：使用者無需安裝一系列的擴充套件或修改任何設定即可獲得保護**。





- 不要犧牲任何必要的效能或人體工學。在沒有 Tor 路由的情況下，Mullvad 瀏覽器提供比 Tor 瀏覽器更快的瀏覽速度，接近標準瀏覽器加上 VPN 的效能。



### Mullvad 瀏覽器的主要功能



Mullvad Browser 包含一系列直接受 Tor Browser 啟發的**安全與隱私功能**：





- 隨時隱私瀏覽：**隱私瀏覽模式預設啟動，無法停用。從一個會話到下一個會話不會儲存任何歷史記錄、cookies 或快取。**一旦關閉 Mullvad Browser，所有瀏覽資料都會被刪除。





- 增強的防指紋保護：**瀏覽器採用嚴格的設定來阻擋數位指紋。這包括**
- 使用者代理**與瀏覽器版本**標準化
- 所有使用者的時區設定為 **UTC**
- 信箱：一種在網頁周圍自動添加灰色邊界的技術，以標準顯示尺寸，並防止根據您的螢幕尺寸進行識別
- 封鎖指紋 API：禁用 Canvas (2D 繪圖)、WebGL (3D 圖形) 和 AudioContext (音訊處理) 技術，因為它們會揭露您硬體的獨特詳細資訊
- 標準化的系統字型，可避免被安裝的字型識別





- 封鎖追蹤者與廣告：**Mullvad 瀏覽器原生整合了 uBlock Origin 擴充套件 (預先安裝)，附加保護清單可封鎖第三方追蹤者、廣告腳本與其他惡意內容**。此保護功能搭配**第一方隔離**：此技術可將 cookies 儲存在每個網站的獨立「罐子」中，防止一個網站讀取另一個網站存入的 cookies。





- 會話重設按鈕：**與 Tor 瀏覽器的 "New Identity "按鈕一樣，Mullvad 瀏覽器也提供了一個按鈕，快速地以新的空白會話重新啟動瀏覽器。**





- 可調整的安全層級：**您可以在設定中調整安全層級 (*Normal*、*Safer*、*Safest*)，就像在 Tor Browser 中一樣。**



## 預設內建延伸功能



Mullvad Browser 包含三個預先安裝的擴充套件，這些擴充套件構成其反追蹤保護的核心。**切勿移除這些擴充套件或修改其設定**，因為這將使您成為 Mullvad Browser 的唯一使用者：



### **uBlock Origin**


此廣告和追蹤器封鎖擴充套件預先設定了**優化的過濾清單**，可封鎖 .NET 和其他語言：




- 侵入性廣告
- 收集您資料的第三方追蹤器
- 惡意指令碼
- 行為追蹤 Elements



Mullvad Browser 中的 uBlock Origin 使用標準化參數，以確保所有使用者封鎖完全相同的 Elements，從而保持數位足跡的一致性。



### **NoScript**


NoScript 在背景中執行，以管理瀏覽器的 ** 安全層級**。此：




- 根據選取的等級 (一般/最安全/最安全) 控制 **JavaScript** 的執行
- 自動過濾 **XSS（跨站腳本）攻擊**
- 封鎖非 HTTPS 網站上的危險**活動內容**
- 其圖示預設為隱藏，但可透過「自訂工具列」顯示



### **Mullvad 瀏覽器** 擴充套件


這個 Mullvad 專用的擴充套件提供不同的功能，視您是否為 Mullvad VPN 客戶而定：



#### **未訂閱 Mullvad VPN：**




- **基本連線檢查**：顯示您目前的公用 IP 和一些連線資訊
- **隱私建議**：改善安全設定的提示 (DNS、僅限 HTTPS、搜尋引擎)
- **WebRTC** 控制：啟用/停用，以防止 IP Address 洩漏
- 如果您不使用 Mullvad VPN，可以刪除而不影響**您的數位足跡**



#### **訂閱 Mullvad VPN：**


擴充套件透過先進的功能充分展現其潛力：





- 整合式 SOCKS5 代理：一鍵連線至 Mullvad VPN 伺服器代理
- 固定 IP Address：VPN 可以變更其 IP Address，而代理伺服器則不同，它永遠保證相同的輸出 Address。
- 自動封鎖開關：如果 VPN 斷線，瀏覽器流量會立即被封鎖
- IPv6 支援：即使您的 VPN 連線未啟用 IPv6，仍可使用 IPv6 連線功能





- 多跳 (雙 VPN)：能夠變更代理位置，在隧道內建立隧道
 - 您的流量會先經過您的 VPN 伺服器，然後「跳轉」至另一個 Mullvad 伺服器
 - 僅對瀏覽器使用不同的本地化





- **進階連線監控**：即時監控您的 VPN 狀態、連線伺服器及 DNS 洩漏偵測





- 訪問 **Mullvad Leta**：專為訂戶保留的私人搜索引擎（雖然 Mullvad 基於與您帳戶相關的原因而不推薦）。



這三種擴充功能共同創造了一個連貫的保護生態系統，讓每位使用者都能從完全相同的防禦功能中獲益，而不會因為客製化而損害集體匿名性。



## Mullvad 瀏覽器的優缺點



### 優點





- 預設的優異隱私權保護：**Mullvad Browser 從一開始就應用非常嚴格的隱私權設定，無需手動設定。**





- 比 Tor 瀏覽器更優異的效能：**在沒有洋蔥路由的情況下，Mullvad 瀏覽器比 Tor 瀏覽器明顯地更快速、反應更敏捷**。





- 熟悉的 Interface 簡潔性：**Mullvad 瀏覽器是基於 Firefox 的 Interface。如果您習慣使用 Firefox 甚至 Tor 瀏覽器，就不會感到不習慣。**





- 可信賴的合作與經過稽核的程式碼：**Mullvad Browser 得益於 Tor Project 的專業知識，所有的原始程式碼都可以供外部稽核。**



### 缺點





- 沒有 VPN 就沒有網路匿名：**最重要的一點是，Mullvad 瀏覽器不會自行隱藏您的 IP Address**（像所有其他瀏覽器一樣，除了 Tor 瀏覽器）。您的 IP Address 就像您在網際網路上的「郵政 Address」：它會顯示您的位置和您的 ISP。因此，它**嚴重依賴 VPN**（虛擬私人網路）來隱藏這項重要資訊。





- 沒有行動版：**到目前為止，Mullvad Browser 只能在 PC（Windows、Mac、Linux）上使用。**





- 與某些習慣不相容：** 永久隱私模式** 表示您無法在一次使用中保持連線。不可能從一個會話到下一個會話都保持連線到網路帳戶。





- 受限制的功能：**為了保持指紋的一致性，Mullvad Browser 已停用 Firefox 中的多項功能，且不打算用於自訂。**



## 安裝 Mullvad 瀏覽器



Mullvad Browser 免費適用於 Windows、macOS 和 Linux。若要安裝，請前往 [Mullvad 官方網站](https://mullvad.net/browser)。



![MULLVAD BROWSER](assets/fr/02.webp)



**官方 Mullvad 瀏覽器首頁，高亮顯示下載按鈕。**



![MULLVAD BROWSER](assets/fr/03.webp)



*在 Mullvad Browser.* 下載頁面上選擇您的作業系統



按一下與您作業系統相對應的 **「下載 」** 按鈕。



對於 Linux，您可以根據您的發行版選擇不同的格式。下載完成後 ：



### 在視窗上


執行下載的 `.exe` 檔案，並依照安裝指示操作。



### 在 macOS 上


開啟下載的「.dmg」檔案，然後將 Mullvad Browser 應用程式拖曳到「應用程式」資料夾中。



### 在 Linux 上


將`.tar.xz`存檔解壓縮到您選擇的目錄中，並執行`start-mullvad-browser.desktop`檔案。



## 配置和首次使用



第一次啟動 Mullvad 瀏覽器時，您會看到與 Tor 瀏覽器非常相似的 Interface。瀏覽器已預先設定好隱私權，不需要特別修改。



![MULLVAD BROWSER](assets/fr/04.webp)



**Interface Mullvad 瀏覽器首頁的擴充功能、掃把圖示到 generate 的新身分，以及右上方的應用程式選單。**



**重要事項：** Mullvad 瀏覽器預設不會遮蔽您的 IP Address。為了提供完整的保護，我們強烈建議您同時使用 VPN。您可以使用 Mullvad VPN 或任何其他可信賴的 VPN 服務。



瀏覽器也包含**DNS-over-HTTPS (DoH)** 使用 Mullvad 的 DNS 服務：此技術會加密您的 DNS 請求 (將網站名稱轉換成 IP 位址)，以防止您的 ISP 監控您造訪的網站。



### 安全設定



您可以按一下右上方的 ** 應用程式功能表** (三個橫條)，然後按一下 **「設定」**，再按一下 **「隱私與安全」** 標籤，調整安全層級。向下捲動至 **「安全性」** 區段：



![MULLVAD BROWSER](assets/fr/05.webp)



*安全層級的選擇：箭頭顯示從應用程式功能表到「隱私與安全」標籤到安全選項的路徑*。



Mullvad Browser 提供三種安全層級：





- **Normal** (目前預設等級) ：啟用所有瀏覽器和網站功能





- 更安全：停用常有危險的網站功能，這可能會導致某些網站失去功能：
 - 非 HTTPS 網站的 JavaScript 已停用
 - 某些字型和數學符號已停用
 - 聲音和視訊（HTML5 媒體）以及 WebGL 均可 「點擊播放」。





- **最安全**：只允許靜態網站和基本服務所需的網站功能：
 - 所有網站都預設停用 JavaScript
 - 某些字型、圖示、影像和數學符號已停用
 - 聲音和視訊（HTML5 媒體）以及 WebGL 均可 「點擊播放」。



### 新會話按鈕



若要在不關閉瀏覽器的情況下以空白會話重新啟動，請按一下掃帚圖示，或使用應用程式功能表 > **「新會話 」**。



![MULLVAD BROWSER](assets/fr/06.webp)



*重設您的身份 "功能，以全新的會話重新啟動瀏覽器*。



## 日常使用



### 正常導航



Mullvad Browser 在日常瀏覽中表現與經典瀏覽器無異。所有網站都能像平常一樣存取，但有更強大的防追蹤功能。



### Cookie 管理和登入



由於永久隱私模式，您每次登入時都必須重新連線到您的帳戶。這是您為最大保密性所付出的代價。



### 擴展



Mullvad 瀏覽器在技術上允許您從 Firefox 目錄中安裝額外的擴充套件，但**重要的是要瞭解其影響**。每個新增的擴充套件都會改變您的數位足跡，並將您與其他 Mullvad Browser 使用者區分開來，這違反了瀏覽器的基本原則：讓所有使用者看起來都是一樣的。



正如 Mullvad 所解釋的： *"有時候，沒有特定的防禦措施總比有防禦措施好。由於想要增加線上隱私，您安裝的擴充套件最終會讓您更顯眼。"*



如果您還是選擇安裝擴充套件，請注意您正在建立一個獨特的指紋，可以用來追蹤您從一個網站到另一個網站。為了獲得最大的保護，最好使用預先安裝的三個擴充套件，這三個套件對所有使用者都是相同的。



## 使用 Mullvad 瀏覽器的最佳做法



1. **請務必使用 VPN：Mullvad 瀏覽器不會遮蔽您的 IP。VPN 是完全匿名的必要條件。**



2. **不要自訂瀏覽器**：避免變更設定或新增擴充套件，因為這可能會讓您的身分被識別。



3. **使用新會話按鈕**：在不同的活動之間，使用重設功能來分割您的階段。



4. **選擇最適合您需求的安全層級** ：




- **Normal (建議)**：適用於日常瀏覽。已提供極佳的保護，同時保持網站的功能。這是 95% 使用者的最佳平衡。
- 更安全：如果您正在造訪未知或有潛在危險的網站，或在公共 Wi-Fi 網路上需要額外的保護。某些網站可能會發生故障。
- 最安全：預留給高風險的情況 (調查性新聞、敏感通訊、敵對環境)。大多數現代網站都會被攻破，但這就是最高安全性的代價。



5. **定期檢查更新**：讓您的瀏覽器使用最新的安全修補程式。



6. **使用隱私權友善的搜尋引擎**：選擇 DuckDuckGo、Startpage 或 Searx 而非 Google。



7. **Enable HTTPS only mode**：在設定中，確定已啟用「僅 HTTPS」模式，以強制安全連線。



8. **請勿變更任何進階設定**：與其他瀏覽器不同，Mullvad Browser 的設計讓所有使用者擁有完全相同的設定。修改 `about:config` 中的設定或變更 uBlock Origin/NoScript 設定會讓您變得獨一無二，並完全取消瀏覽器的匿名性。



## 建議的 DNS 設定



Mullvad Browser 自動整合 Mullvad DNS-over-HTTPS。如果您正在使用 Mullvad VPN，擴充套件會建議您**停用 Mullvad DoH**，因為使用 VPN 伺服器的 DNS 伺服器會比較快。如果您沒有使用 Mullvad VPN，請保持啟用 Mullvad DoH，以避免 ISP 監控 DNS。



## 總結



Mullvad Browser 是一款出色的解決方案，適用於尋求隱私友好型網路瀏覽的用戶，且不受 Tor 網路效能的限制。結合優質的 VPN，它能提供強大的保護，防止線上追蹤和監視。



雖然 Mullvad Browser 有某些限制 (沒有行動版本、非持續會話)，但對於希望重新掌控數位隱私權的人來說，Mullvad Browser 是很有價值的工具。它的易用性和預設設定使其成為注重隱私的使用者的明智選擇，無論是初學者還是經驗豐富的使用者。



## 資源



### 官方文件




- [Mullvad瀏覽器官方網站](https://mullvad.net/fr/browser)
- [Mullvad 瀏覽器下載頁](https://mullvad.net/en/download/browser)
- [詳細技術規格](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad 瀏覽器擴充套件](https://mullvad.net/en/help/mullvad-browser-extension)



### 指南和說明




- [Why privacy matters](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor without Tor：Mullvad 瀏覽器概念](https://mullvad.net/en/browser/tor-without-tor)
- [如何選擇對隱私友善的瀏覽器](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [瞭解瀏覽器指紋](https://mullvad.net/en/browser/browser-fingerprinting)



### 支援與協助




- [Mullvad 瀏覽器說明中心](https://mullvad.net/en/help/tag/mullvad-browser)
- [線上隱私權的第一步](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### 社區資源




- [Mullvad 瀏覽器指南 - 隱私權指南](https://www.privacyguides.org/en/desktop-browsers/)
- [社區討論](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)