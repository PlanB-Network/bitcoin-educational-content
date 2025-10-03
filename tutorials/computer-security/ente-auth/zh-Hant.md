---
name: Ente Auth
description: 開放原始碼、端對端加密的 2FA 認證器
---
![cover](assets/cover.webp)



雙因素驗證 (2FA) 已經成為保障我們線上帳戶安全不可或缺的工具。除了您常用的密碼外，它還需要一個臨時代碼，通常由專門的應用程式產生。這種機制被稱為 TOTP（Time-Based One-Time Password），可保證即使您的密碼被洩露，攻擊者也無法存取您的帳戶，除非擁有每 30 秒更新一次的第二因素。



然而，選擇正確的驗證應用程式並非易事。Google Authenticator 雖然很受歡迎，但卻有很大的限制：無法稽核的專屬程式碼、沒有端對端加密的同步化，以及在手機出問題時會有完全遺失程式碼的風險。其他解決方案，例如 Authy，需要電話號碼，而且無法保證完全保密。



**Ente Auth** 是一個現代化、安全的選擇。這個免費、開放原始碼、跨平台的應用程式，是由 [Ente Photos](https://ente.io) 背後的團隊所開發，提供端對端加密雲端備份，並在您所有裝置之間進行無縫同步。與專屬解決方案不同的是，Ente Auth 可讓您完全控制驗證碼，而不會損害您的隱私。



在本教程中，我們將逐步向您介紹如何安裝和使用 Ente Auth，以及此解決方案與傳統驗證器不同的原因。



## 介紹 Ente Auth



Ente Auth 是由 Ente Photos 背後的團隊所開發，Ente Photos 是一個端對端加密與隱私友善的相片儲存服務。Ente Auth 秉承 Ente 的理念（"Ente 「在馬拉雅拉姆語中的意思是 」我的"，象徵著對您資料的控制），旨在讓使用者重新完全控制他們的雙重驗證碼。



### 主要功能



**Standard TOTP codes**：Ente Auth 生成的臨時代碼與大多數服務（GitHub、Google、Binance、ProtonMail 等）相容。您可以根據需要新增多個 2FA 帳戶，應用程式會根據提供的秘密計算代碼。



**端對端加密雲端備份**：您的密碼會安全地儲存在線上。只有您自己才能解密 - 加密金鑰來自您的密碼，只有您自己知道。Ente (伺服器) 不知道您的秘密，甚至不知道您的帳號名稱，因為一切都使用零知識架構在客戶端加密。



**多裝置同步**：您可以在多部裝置（智慧型手機、平板電腦、電腦）上安裝 Ente Auth，並在所有裝置上存取您的密碼。任何變更都會透過加密雲端自動即時傳送至您的其他裝置，讓您的日常工作更具彈性。



**Minimalist, intuitive Interface**：本應用程式提供簡化的 Interface，即使非技術使用者也能輕鬆學習。2FA 帳號會顯示服務名稱，您的登入名稱和 6 位數字密碼，並即時更新。Ente Auth 還會提前幾秒顯示下一個代碼，以避免因過期而無法使用。



** 開放原始碼並已審核**：Ente Auth 的原始碼在 AGPL v3.0 授權下 [GitHub 上公開](https://github.com/ente-io/auth)。任何開發人員都可以對其進行審核，以檢查缺陷或不良行為。所執行的加密技術已經過 [獨立外部稽核](https://ente.io/blog/cryptography-audit/)，這是應用程式安全性的保證。



### 優點與限制



**福利：**




- 端對端加密的隱私權設計
- 所有裝置之間的安全同步
- 可稽核的開放原始碼
- Interface 清晰、直觀的使用者 Interface
- 自動備份以防止遺失代碼
- 適用於所有平台（行動和桌上型電腦）



**限制：**




- 同步需要網際網路連線
- 進階使用者可能會偏好 100% 離線解決方案，例如 Aegis (僅限 Android)
- 與既有的解決方案相比相對較新



## 安裝



Ente Auth 可在大多數常用平台上使用。您可以從 [官方網站](https://ente.io/auth) 或官方商店下載應用程式。



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth 下載頁面包含所有可用平台*



### 安卓


您有幾種選擇：




- Google Play 商店：搜尋「Ente Auth」以進行經典安裝
- **F-Droid**：可從 Android 開放原始碼應用程式目錄中取得，保證經過驗證的結構，且不含專屬內容
- **手動安裝**：APK 檔案可從 [專案的 GitHub 頁面](https://github.com/ente-io/auth/releases) 下載，並整合新版本通知功能



### iOS (iPhone/iPad)


透過搜尋應用程式名稱，直接從 Apple App Store 安裝 Ente Auth。iOS 應用程式也可透過 Mac App Store 在配備 Apple Silicon 晶片 (M1/M2) 的 Mac 上執行。



### 電腦（Windows、macOS、Linux）


Ente Auth 提供本機桌面應用程式。請造訪 [ente.io/download](https://ente.io/download) 或 [GitHub 的 Releaseases 部分](https://github.com/ente-io/auth/releases) ：





- **Windows**：提供 EXE 安裝程式
- **macOS**：在應用程式中拖放 DMG 磁碟影像
- **Linux**：提供多種格式 (AppImage 可攜式、.deb 適用於 Debian/Ubuntu、.rpm 適用於 Fedora/Red Hat)



**註：** 本教學以 Ente Auth v4.4.4 及更新版本為基礎。早期版本可能與 Interface 有微小差異。



### Interface 網路


無需安裝，您可以從任何瀏覽器透過 [auth.ente.io](https://auth.ente.io)存取您的代碼。Interface Web 只限於檢視代碼 (有助於疑難排解)，因為基於安全理由，新增帳號需要使用行動或桌上型應用程式。



## 第一組態



### 建立帳戶



首次啟動 Ente Auth 時，您有兩個選項：



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Ente Auth 首頁畫面，包含帳戶建立選項*。



**有帳號（建議）**：選擇「建立帳號」，並輸入您的電子郵件 Address 和密碼。 **重要**：此密碼可作為加密資料的主密碼。請選擇強大、獨特的密碼，因為沒有不遺失資料的傳統重設程序。如果您放錯位置，您的加密資料將無法復原。



**離線模式**：選擇「無備份使用」，即可在本機使用應用程式，無需雲端。在此模式下，您的代碼會保留在裝置上，但您需要手動匯出以避免遺失。



![Vérification email et récupération de clé](assets/fr/03.webp)



*電子郵件驗證程序和產生 24 個字的復原金鑰*



可能會要求電子郵件驗證，以驗證帳戶的建立，並啟用新裝置上的復原功能。Ente Auth 還會為您提供 24 個字的復原密鑰（基於 BIP39 方法）。 **請務必將此密碼**保存在安全的地方：這是您忘記密碼時恢復資料的唯一方法。



### 當地安全



我強烈建議您啟用密碼或生物辨識的本機保護。前往 ** 設定 → 安全性 → 鎖定螢幕** 並設定 ：





- 生物辨識解鎖：臉部 ID、指紋，視您裝置的功能而定
- 應用程式特定的 **PIN/密碼**
- 自動鎖定延遲：例如「立即」或 30 秒未活動後



此保護可在有人取得您未鎖定手機的存取權時，防止未經授權存取您的密碼。請注意，此鎖是額外的障礙：即使沒有此保護，您的資料仍然是端對端加密的。



## 新增 2FA 帳戶



### 標準程序



要新增 2FA 帳戶，讓我們以在 Bull Bitcoin 上啟動 2FA 為具體範例：



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auth 的主 Interface 已準備好新增第一個 2FA* 帳戶



**服務端 (Bull Bitcoin)**：登入您的 Bull Bitcoin 帳戶，前往安全設定，並啟用雙重認證。



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* 安全設定功能表



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*在 Bull Bitcoin* 上啟用雙重因素驗證的選項



服務隨後會顯示一個 QR 代碼，供您使用驗證應用程式掃描：



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*Bull Bitcoin 產生的 QR 代碼，可用您的驗證器掃描*。



**在 Ente Auth**：按一下「輸入設定金鑰」，然後掃描 Bull Bitcoin 顯示的 QR 代碼。Ente Auth 會自動識別帳戶並填寫欄位。



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*在 Ente Auth* 中設定 Bull Bitcoin 帳戶詳細資料



您可以自訂服務名稱和登入名稱，以便更容易找到。進階設定 (SHA1 演算法、30 秒週期、6 位數) 預設值一般都是正確的。



**服務端驗證**：返回 Bull Bitcoin，輸入由 Ente Auth 生成的 6 位數代碼以完成啟用。



![Saisie du code 2FA](assets/fr/09.webp)



*輸入 Ente Auth 生成的代碼以驗證 2FA* 啟用



![2FA activée](assets/fr/10.webp)



*確認公牛 Bitcoin* 上的 2FA 啟動成功



**備份代碼**：Bull Bitcoin 將提供您復原碼。**將它們保存在安全的地方，與您的驗證器分開。**



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*公牛 Bitcoin 上的 generate 緊急備援碼選項*



![Codes de récupération](assets/fr/12.webp)



*要妥善保存的復原代碼清單*



### 組織與管理



Ente Auth 提供多項實用功能：



**快速複製**：按下代碼即可自動複製到剪貼簿。



**情境感應動作**：長按（或在桌面上按滑鼠右鍵）可編輯、刪除、分享或釘選項目。



**標籤與搜尋**：使用標籤 (個人/專業、服務類別) 整理您的帳戶，並使用搜尋列快速篩選。



![Création d'un tag](assets/fr/17.webp)



*標籤建立程序：上下文功能表和建立對話框*



![Tag appliqué](assets/fr/18.webp)



*標籤「Bitcoin」成功套用於公牛 Bitcoin* 帳戶



**自動圖示**：由於整合了 [Simple Icons] 圖示套件 (https://simpleicons.org/)，每個條目都可以用服務的標誌來說明。



**臨時安全共享**：安全共用是 Ente Auth 的獨特功能，可讓您傳送 2FA 代碼給同事，而不會洩露底層的秘密。generate 加密連結的有效期最長為 2、5 或 10 分鐘 - 收件者可即時看到密碼，但無法匯出或存取帳戶資料。此方法適用於技術協助或臨時協作，提供簡單截圖或文字訊息無法達到的安全層級。



![Partage sécurisé](assets/fr/19.webp)



*Interface 臨時安全共用：選擇時間（5 分鐘）*



**安全匯出/匯入**：Ente Auth 可讓您匯出代碼至其他應用程式，或從 Google Authenticator 及其他解決方案匯入代碼。透過加密檔案或 QR 代碼匯出，可確保資料的可攜性而不影響安全性。



**BIP39 復原密碼**：應用程式會根據 BIP39 (Bitcoin Improvement Proposal) 標準自動產生 24 個字的復原短語，與加密貨幣錢包相同。該短語是您的終極恢復密鑰，即使您忘記主密碼，也能恢復所有密碼。



## 組態與設定



Ente Auth 提供許多可透過應用程式設定存取的自訂選項：



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Ente Auth* 中可用參數的概述



### 帳戶和資料管理



![Paramètres de sécurité](assets/fr/14.webp)



*進階安全選項：電子郵件驗證、PIN 碼、活動會話*。



安全設定可讓您 ：




- 啟用新連線的電子郵件驗證
- 啟動密碼
- 檢視各種裝置上的活動會話
- 設定 PIN 碼或生物辨識技術



### Interface 和使用選項



![Paramètres généraux](assets/fr/15.webp)



*Interface 參數和應用程式自訂*



一般設定包括 ：




- 語言：**Interface 多語言**
- 顯示：大圖示，精簡模式
- 隱私：隱藏代碼、快速搜尋
- **Telemetry**：錯誤報告（可停用）



## 備份與同步



### 加密如何運作



當您新增一個已連線的 Ente 帳戶時，應用程式會立即使用您的主金鑰 (源自您的密碼) 在本機加密這些敏感資料。加密後的資料會傳送到 Ente 伺服器儲存。



得益於此機制，您的密碼可隨時獲得端對端的加密雲端備份。如果您遺失裝置，只需重新安裝 Ente Auth 並重新連線：應用程式會自動下載並解密您所有的密碼。



### 多裝置同步



如果您在智慧型手機和電腦上都使用 Ente Auth，其中一台裝置上的任何新增或變更都會在幾秒鐘內出現在另一台裝置上。此同步會透過 Ente 的雲端進行，但由於資料是端對端加密，伺服器只能看到無法讀取的加密內容。



![Synchronisation mobile](assets/fr/16.webp)



*同步示範：手機和桌上型電腦可存取相同的 Bull Bitcoin 帳戶*。



無縫同步：在您的智慧型手機上安裝 Ente Auth，使用您的憑證登入，您所有的 2FA 代碼 (這裡是 Bull Bitcoin)都會自動出現。上面的範例顯示了桌上型電腦和行動裝置之間的完美同步 - 同樣的 Bull Bitcoin 代碼可在兩部裝置上存取。



在保密性方面，Ente 或任何第三方都無法存取您的 2FA 秘密。即使是元資料 (標籤、備註、服務名稱) 也會在傳送前加密。這種零知識架構確保只有您自己才能破譯您的密碼。



### 離線使用



同步化需要網際網路，但 Ente Auth 可在每部裝置上完美離線運作，因為所有資料都儲存在本機。離線變更會排隊，並在連線恢復後立即同步。



## 安全性與隱私權



### 密碼保證



Ente Auth 基於強大的端對端加密與零知識架構。您的密碼是以您個人持有的金鑰加密的，該金鑰是使用先進的金鑰推導函數從您的主密碼推導出來的。



**零知識架構：Ente 無法實體存取您的資料。即使是元資料（服務名稱、標籤、備註）也會在傳輸前在客戶端加密。此方法可確保在您的伺服器受到攻擊或政府要求時，Ente 只能揭露沒有您的密碼就無法讀取的加密資料。**



**本地加密**：加密過程完全在您的裝置上進行，然後才傳送到雲端。Ente 的伺服器只接收並儲存加密資料，即使服務管理員也無法進行未經授權的存取。



### 透明度與稽核



由於程式碼是 [開放原始碼](https://github.com/ente-io/auth)，社群可以驗證沒有後門。Ente 已進行 [多項外部稽核](https://ente.io/blog/cryptography-audit/) 以驗證其實作的安全性：





- **Cure53** (德國)：應用程式與密碼安全稽核
- **Symbolic Software**（法國）：專業的密碼技術
- **Fallible**（印度）：滲透測試與弱點分析



這些由認可公司執行的獨立稽核，可保證 Ente Auth 的加密實作符合最佳安全實務，且無重大瑕疵。



### 隱私權政策



Ente Auth 採用以最少資料收集為基礎的 [典範隱私權政策](https://ente.io/privacy/)。僅保留服務運作所需的必要資訊：您的電子郵件 Address 用於驗證和帳戶恢復。



**無追蹤或遙測**：與大多數應用程式不同，Ente Auth 不會收集使用指標、識別碰撞資料和行為資訊。本應用程式在運作時，沒有侵入性的廣告或分析追蹤程式。



**GDPR 合規性**：Ente 完全遵守《歐洲一般資料保護條例》。您有權隨時存取、更正或刪除您的資料。資料匯出](https://ente.io/take-control/) 只需點擊一下，永久刪除您的帳戶會從伺服器刪除您的所有資料。



**分散式安全儲存**：您的加密資料會複製到 3 個不同國家的 3 個不同供應商，確保最佳可用性，同時避免依賴單一雲端供應商。



Ente 的商業模式是以付費的 Ente Photos 服務為基礎，使我們能夠提供 Ente Auth ** 免費且無限制**，而不會透過將個人資料貨幣化來損害您的隱私。這種方式保證了服務的持續性，而無需依賴廣告或轉售個人資料。



## 與其他解決方案的比較



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth 是少數結合所有優點的解決方案之一：源代碼透明、加密雲端備份和跨平台同步。



## 建議用例



### 個人使用者



Ente Auth 非常適合有系統啟動 2FA 的安全意識人士。您再也不必擔心更換手機時遺失密碼，或在便利性和安全性之間做出選擇。



### 家庭與多裝置使用



如果您使用多部裝置，此應用程式便會發揮作用。您可以在智慧型手機和平板電腦上儲存代碼，或同步安全地分享特定的家庭代碼 (Netflix、家庭雲端)。



### 專業用途



對於管理敏感帳戶的團隊而言，Ente Auth 可在保護安全性的同時促進協作，這要歸功於其整合於「組織與管理」部分的進階分享功能。



## 最佳實踐





- 儲存您的緊急代碼：將各服務提供的復原代碼與您的手機分開保存。





- 使用強大的主密碼：您的 Ente Auth 主密碼必須是唯一且強大的，因為它會保護您所有的代碼。





- 啟動本機保護：設定 PIN 碼或生物辨識技術，防止未經授權的實體存取。





- 不要過度自訂：避免進階修改，以免影響同步化。





- 保持應用程式更新：更新可修正安全漏洞並改善功能。





- 測試還原：偶爾檢查是否可以在其他裝置上還原您的代碼。



## 總結



Ente Auth 是雙重認證的現代化綜合解決方案。透過結合安全性、透明度和易用性，此開放源碼應用程式在不犧牲便利性的前提下，滿足高要求使用者的需求。



Ente Auth 與專屬解決方案不同，專屬解決方案會將您鎖入不透明的生態系統，而 Ente Auth 則可讓您重新掌控驗證資料，同時透過加密備份保護您的資料，避免意外遺失。



無論您是希望保護個人帳戶安全的個人，或是管理企業存取的團隊，Ente Auth 都是您在不影響隱私權的情況下，將數位安全性現代化的明智選擇。



## 資源與支援



### 官方文件




- 官方網站：[ente.io/auth](https://ente.io/auth)
- 說明中心：[help.ente.io/auth](https://help.ente.io/auth)
- 技術部落格：[ente.io/blog](https://ente.io/blog)



### 原始碼與透明度




- **GitHub**：[github.com/ente-io/auth](https://github.com/ente-io/auth)
- **加密審計**：[ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### 社區




- **Discord**：[discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit**：[r/enteio](https://reddit.com/r/enteio)