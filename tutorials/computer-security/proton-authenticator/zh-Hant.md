---
name: Proton Authenticator
description: 如何使用 Proton Authenticator 以 2FA 保護我的帳戶？
---
![cover](assets/cover.webp)



雙因素驗證 (2FA) 為您的帳戶增加了一道額外的安全屏障，除了您的密碼之外，還需要額外證明只有您才擁有密碼。即使您的密碼因網路釣魚或資料洩漏而外洩，啟用 2FA 也能大幅降低駭客入侵的風險。如果沒有 2FA，攻擊者只需要您的密碼就可以存取您的帳戶；如果有了 2FA，攻擊者還需要您的第二因素，這樣就挫敗了大部分盜用帳戶的企圖。



2FA 有多種類型。SMS 代碼聊勝於無，但仍然容易受到 SIM 卡交換攻擊和攔截。我們不建議使用 SMS 作為主要的 2FA。驗證應用程式 (TOTP) 可在您的裝置上本機 generate 臨時代碼，使其更難被攔截。實體安全金鑰提供最佳的安全性，但需要專用硬體。



Proton Authenticator 是一款 TOTP 身份驗證器。它是 Proton 對現有應用程式的限制所作出的回應：許多應用程式都是專屬的、包含廣告追蹤程式，而且不提供加密備份。Proton Authenticator 提供開放原始碼應用程式，不含廣告和追蹤程式，並提供端對端加密備份，因此與眾不同。



## 介紹 Proton Authenticator



Proton Authenticator 是 Proton 開發的行動和桌上型 TOTP 驗證應用程式，該公司以注重隱私的服務聞名。與所有 Proton 產品一樣，此應用程式為開放原始碼，並已通過獨立的安全稽核。它可在所有平台（Android、iOS、Windows、macOS、Linux）上免費使用。



Proton Authenticator 提供下列主要功能：





- 為您的 2FA 帳戶產生 **TOTP** 代碼，與使用 Google Authenticator、Authy 等的大多數網站相容。





- 可選加密雲端備份：您可以將應用程式連結至您的 Proton 帳戶，以端對端加密方式備份和同步您的密碼。如果您遺失裝置，只需重新連線新的裝置，即可還原您所有的密碼。





- 多裝置同步：只要在應用程式中登入 Proton，您的 2FA 密碼就會透過端對端加密在多個裝置之間自動同步。在 iOS 上，可選擇透過 iCloud 進行同步。





- 本地密碼或生物識別鎖定：應用程式提供密碼和/或指紋/臉部識別鎖定。因此，即使有人實際進入您未鎖定的手機，也無法開啟 Proton Authenticator。





- **無資料收集或追蹤器**：Proton 承諾不透過應用程式收集任何個人資料。沒有隱藏的廣告或行為分析。





- 輕鬆匯入/匯出：Proton Authenticator 的強項之一是其現有帳號的匯入精靈，與其他應用程式 (Google Authenticator、Authy、Aegis 等) 相容。如有需要，您也可以將密碼匯出至檔案。



簡而言之，Proton Authenticator 的目標是成為不折不扣的 2FA 解決方案：安全、隱私、靈活。



## 安裝



Proton Authenticator 可免費在所有平台上使用。要下載應用程式，請前往官方網頁：[https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Proton Authenticator 官方頁面顯示應用程式的主要功能和 Interface*



在此頁面，您可以找到所有作業系統的下載連結：Android、iOS、Windows、macOS 和 Linux。只需點選您所選擇的作業系統，並依照標準安裝步驟即可。



在本教程中，我們將教您如何在 macOS 上安裝和設定，然後再看看如何在 iOS 上安裝應用程式，並在兩台裝置之間同步您的代碼。



### 在 macOS 上安裝



下載並安裝應用程式後，啟動 Proton Authenticator。首次啟動時，應用程式會引導您完成幾個初始設定畫面：



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticator 歡迎畫面，包含「每個驗證碼都是安全的」訊息和「開始使用」* 按鈕



### 初始輸入



如果 Proton Authenticator 偵測到您之前使用其他 2FA 應用程式，可能會出現匯入精靈。它支援從某些應用程式（Google Authenticator、2FAS、Authy、Aegis 等）直接匯入。或者，您也可以跳過此步驟，稍後再手動新增您的帳號。



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*匯入精靈可從其他認證應用程式傳輸代碼*。



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*相容的匯入應用程式：2FAS、Aegis Authenticator、Authy、Bitwarden Authenticator、Ente Auth 和 Google Authenticator*



### 本機應用程式保護



設定解鎖密碼，或啟用生物辨識解鎖 (Touch ID)（如可用）。此步驟非常重要，可防止任何人使用您的 Mac 免費存取您的 2FA 代碼。



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Touch ID 設定畫面，顯示「保護您的資料」訊息和「啟動 Touch ID」* 按鈕



### 同步化選項



應用程式還可讓您啟動 iCloud 同步處理功能，在 Apple 裝置之間安全備份資料。



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*帶有訊息「使用加密的 iCloud 同步處理安全備份您的資料」*的 ICloud 同步處理選項



完成這些步驟後，Proton Authenticator 即可使用。



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface 主空質子驗證器，具有「建立新代碼」和「匯入代碼」*選項



## 使用 ProtonMail 新增 2FA 帳戶



現在我們以 ProtonMail 為例，看看如何新增您的第一個 2FA 代碼。此方法適用於所有支援雙因素認證的服務。



### 在 ProtonMail 上啟用 2FA



首先，您可以參考我們的 ProtonMail 指南以獲得更多資訊：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

登入您的 ProtonMail 帳戶並進入安全設定。尋找「雙因素認證」選項並啟動它。



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail 設定頁面的 「雙因素認證 」*部分中的 "Authenticator app "選項



按一下按鈕啟動驗證器，ProtonMail 會提示您選擇驗證應用程式。



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMail 2FA 設定視窗，有「取消」和「下一步」* 按鈕



ProtonMail 會顯示一個 QR 代碼，讓您使用驗證應用程式掃描。



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR 代碼，可用您的認證應用程式掃描，並提供「手動輸入密鑰」選項*。



如果您希望手動輸入金鑰，請按一下「改為手動輸入金鑰」以查看秘鑰。



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*手動輸入 2FA 資訊：鑰匙、間隔 (30) 和位數 (6)*



### 使用 Proton Authenticator 掃描 QR 代碼



在 MacOS 上的 Proton Authenticator 中，點選「建立新密碼」。應用程式會提供您幾個選項： **掃描 QR 碼** 或 **手動輸入鑰匙**。



使用 Mac 的相機掃描 ProtonMail 螢幕上顯示的 QR 碼。掃描 QR 代碼後，您將會進入新代碼設定畫面。



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*新條目建立視窗，包含標題 (ProtonMail)、密碼、寄件者 (Proton)、數位參數和間隔欄位*



Proton Authenticator 會自動填寫資訊。如果您願意，可以自訂名稱，然後按一下「儲存」。



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*為 ProtonMail (848 812) 產生 TOTP 代碼，並顯示剩餘時間*



### 驗證組態



ProtonMail 會要求您輸入由 Proton Authenticator 產生的 6 位數密碼，以確認 2FA 是否正常運作。



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*ProtonMail 驗證畫面要求您輸入 6 位數碼 (848812)*



複製應用程式的程式碼（點選程式碼）並貼入 ProtonMail 以完成啟動。



一經驗證，ProtonMail 會要求您下載復原碼。請務必小心保存。



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail 恢復代碼畫面，包含救援代碼清單和 「下載 」* 按鈕



### 緊急代碼



新增帳戶時，請保留服務提供的復原碼。大多數網站提供靜態、單次使用的恢復代碼，可儲存在安全的地方。將這些備份代碼保存在 Proton Authenticator 外，以便在您失去 2FA 應用程式的存取權時，可以存取您的帳戶。



## IOS 安裝與程式碼匯入



既然您已在 macOS 上設定 Proton Authenticator，您可能也想在 iPhone 或 iPad 上使用它。以下是如何在多台裝置上取得您的 2FA 碼。



### 在 iOS 上下載應用程式



前往 App Store 並搜尋「Proton Authenticator」。在您的 iOS 裝置上下載並安裝應用程式。



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*iOS 上的安裝程序：歡迎畫面、匯入精靈、選擇相容的應用程式，以及最後的「從 Proton Authenticator 匯入程式碼」*畫面



### 方法 1：透過 JSON 檔案匯出/匯入



如果您不使用自動同步處理 (iCloud 或 Proton 帳戶)，您需要手動將您的代碼從 Mac 傳輸到 iPhone：



**步驟 1 - 從 macOS 匯出** ：



在您的 Mac 上，開啟 Proton Authenticator 並前往「設定」（齒輪圖示）。在功能表中，按一下「匯出」。



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*MacOS 上 Proton Authenticator 的設定選單，「匯出」選項顯示*。



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*匯出視窗的檔案名稱為 "Proton_Authenticator_backup_2025「，並按下 」儲存 "*按鈕



在 Mac 上儲存 JSON 檔案。您可以透過安全的電子郵件傳送，或儲存於 iCloud Drive，以便從 iPhone 存取。



**步驟 2 - 在 iOS 上匯入** ：



在 iPhone 上安裝 Proton Authenticator，並在設定過程中選擇匯入代碼。從清單中選擇「Proton Authenticator」並匯入 JSON 檔案。



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*iOS 上的匯入程序：JSON 檔案本地化、匯入確認，以及包含 Face ID 和 iCloud 選項的配置畫面*



### 方法 2：自動同步化



**Via Proton account (for multi-platform synchronization)** ：



如果您尚未設定 Proton 帳戶，並希望在不同作業系統之間進行同步處理，應用程式會提示您建立或連接 Proton 帳戶。



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*裝置同步畫面要求您建立免費的 Proton 帳戶或連線到現有帳戶*。



**透過 iCloud（僅適用於 Apple 生態系統）** ：


如果您只使用 Apple 裝置，您可以在應用程式設定中選擇 iCloud 同步。此方法可在所有 Apple 裝置之間自動安全地同步您的代碼，而無需 Proton 帳戶。



## 加密備份與還原



Proton Authenticator 的主要功能之一是端對端備份 2FA 代碼，確保遺失或更換裝置時，您不必重新開始。



### 端對端加密



使用 Proton Authenticator 進行加密雲端備份時，您的 TOTP 密碼會先在您的裝置上進行本機加密，然後再傳送至 Proton 伺服器。解密只能由您在與您的 Proton 帳戶連接的裝置上進行。Proton AG 並沒有讀取您所登記密碼的鑰匙。



在 iOS 上，如果您選擇 iCloud 而非 Proton 帳戶，您的資料會以 Apple 標準加密。Android 上的本機備份可讓您使用自選的密碼加密備份檔案。



### 遺失時的修復



如果您的手機遺失、遭竊或更換手機 ：



**啟用 Proton 備份**：在新裝置上安裝 Proton Authenticator。在初始設定時，登入相同的 Proton 帳戶。應用程式會立即從加密備份同步下載您所有的 2FA 碼。



**使用 iCloud 備份 (iOS)**：使用相同的 Apple ID 連接新的 iPhone/iPad，並確認已啟動 iCloud Keychain。安裝 Proton Authenticator 後，連線至 iCloud。您的驗證碼應該會透過 iCloud 同步顯示。



**無雲端備份**：您需要手動匯入您的帳號。如果您有匯出備份檔案，請使用 Proton Authenticator 的匯入功能。在最壞的情況下，如果您沒有備份，您需要使用各服務的備份碼，或聯絡支援人員。



Proton Authenticator 可讓您隨時以加密檔案或多帳戶 QR 代碼的方式匯出帳戶。這些選項讓您更有保障。



## 最佳實踐



使用 2FA 驗證器可大幅提升安全性，但必須遵守某些最佳作法：



### 儲存您的緊急代碼



當您在服務上啟動 2FA 時，通常會給您一張恢復密碼清單。請將它們放在手機以外的地方 (紙張、加密密碼管理器等)。萬一您的驗證器完全遺失，這些靜態代碼可以救您一命。



### 不要混淆您的密碼和 2FA 代碼



使用同時儲存 TOTPs 的密碼管理器很有誘惑性。但是，將密碼和 2FA 代碼放在同一個地方會造成單點失敗，並削弱雙重認證。為了達到最高的安全性，許多專家建議將兩個因素分開：密碼放在安全的管理器中，而 2FA 代碼則放在 Proton Authenticator 等單獨的應用程式中。不過，使用整合式管理程式還是比沒有 2FA 好。



### 啟動多種 2FA 方法



理想情況下，在關鍵帳戶上使用一個以上的第二因數。如果服務允許，請不要猶豫添加實體安全鑰匙。如需詳細資訊，請參閱我們的 Yubikey 實體金鑰教學：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

同樣地，請隨身攜帶列印好的緊急密碼。



### 保持低調，保護您的裝置



不要讓任何人搜查您的解鎖手機。使用 Proton Authenticator，您的密碼受到 PIN/生物辨識技術的保護 - 請勿洩露此 PIN。同樣地，也要提防網路釣魚：即使使用 2FA，如果您即時將密碼提供給詐騙網站，也可能被攻擊者使用。



### 更新與稽核



保持 Proton Authenticator 的更新（更新可修正可能的缺陷）。由於程式碼是開放的，社群會進行非正式的稽核，而 Proton 會公佈正式稽核的結果。



## 與其他應用程式的比較



Proton Authenticator 與其他認證應用程式相比如何？以下是比較摘要：



**Proton Authenticator**：開放原始碼、可選的 E2EE 加密雲端備份、多裝置同步、本機鎖定、無追蹤、可在行動和桌上型電腦上使用。



**Google Authenticator**：專有，自 2023 年起透過 Google 帳戶進行備份，但沒有端對端加密（Google 可以看到金鑰），2023 年新增多裝置同步功能，預設沒有應用程式鎖，包含 Google 追蹤器。



**Aegis Authenticator**：開放原始碼、僅本端備份、無雲端同步、密碼/生物鎖、無追蹤、僅 Android。



**Authy**：專屬、密碼加密雲端備份但封閉程式碼、多裝置同步、PIN 鎖/指紋、收集電話號碼、桌面應用程式於 2024 年 3 月停用。



您可以在下面找到我們的 Authy 指南：



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator 是目前最全面、最安全的解決方案之一：開放原始碼、多裝置加密同步、無商業後續。



## 資源與支援



### 官方文件




- 官方網站：[proton.me/authenticator](https://proton.me/authenticator) - 產品介紹與下載
- 下載頁面：[proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - 所有作業系統的連結
- Proton 支援：[proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - 官方 2FA 啟用指南
- 質子部落格：[proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - 公告和詳細功能



### 原始碼與透明度




- **GitHub Proton Authenticator**：[github.com/ProtonMail/protonauthenticator](https://github.com/ProtonMail/proton-authenticator) - 開放原始碼
- 安全稽核：[proton.me/community/security-audits](https://proton.me/community/security-audits) - 獨立稽核報告



### 建議的安全測試


設定完成後，測試您的設定：




- [Have I Been Pwned](https://haveibeenpwned.com/) - 檢查您的帳戶是否已被入侵
- [2FA 目錄](https://2fa.directory/) - 支援 2FA 的服務清單



### 社群與討論




- Reddit r/Proton：[reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - 質子官方社群
- **隱私權指南論壇**：[discuss.privacyguides.net](https://discuss.privacyguides.net) - 有關隱私權問題的技術討論
- Reddit r/privacy：[reddit.com/r/privacy](https://reddit.com/r/privacy) - 一般隱私提示



### 其他




- [Have I Been Pwned](https://haveibeenpwned.com/) - 檢查您的帳戶是否已被入侵
- [2FA 目錄](https://2fa.directory/) - 支援 2FA 的服務清單