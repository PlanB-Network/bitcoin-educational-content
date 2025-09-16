---
name: 石墨烯OS

description: 一個基於安卓、專注於安全和隱私的行動作業系統
---

![cover](assets/cover.webp)
> [GrapheneOS](https://grapheneos.org/) 是一個非營利的開源行動作業系統，旨在提供高度的隱私與安全，同時保持與 Android 應用程式的完全相容。

GrapheneOS 創立於 2014 年，原名為「CopperheadOS」，以傳統的 Android Code (AOSP) 為基礎，但做了許多改變和改進，目的在於改善使用者隱私和安全性。GrapheneOS 讓使用者而非大型科技公司掌控手機。


![video](https://youtu.be/VnumtalYLFI)

### Sommaire：



- 介紹
- 準備工作
- 安裝
- 應用程式替代品
- 缺點
- 有用資訊


*本教程改編自 [BitcoinQnA 在 Bitcoiner.Guide 上以 MIT 授權發佈的原始內容](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md)，其最初的撰寫工作應完全歸功於 BitcoinQnA。*


## 為何使用 GrapheneOS？


現代手機是價值 500-1000 美元的追蹤和資料收集裝置。我們生活的每個層面都透過手機進行，不幸的是，這些資料大部分都會以某種形式與第三方分享。

GrapheneOS 是專門為了減少這種資料分享而建立，並從潛在的攻擊媒介改善您裝置的安全性。沒有 GrapheneOS 帳戶這回事。您不需要 GrapheneOS 帳戶來下載應用程式或與作業系統互動。簡單來說，您不是產品。


GrapheneOS 透過一些簡單的核心原則，為您的 Android 體驗提供額外的安全性。


1. **Attack surface reduction** - 移除不必要的程式碼 (或 bloatware)。

2. **Vulnerability exposure prevention** - 讓使用者有足夠的粒度來選擇他們可以接受的危害。

3. **Sandbox containment** - GrapheneOS 強化現有的 Android 沙盒，進一步鎖定每個應用程式與手機其他部分溝通的能力。


進一步瞭解 GrapheneOS 功能集的技術細節 [這裡](https://grapheneos.org/features)。


### 緩和過渡


如果您已在 Google 或 Apple 的生態系統中紮根多年，一想到要在一夜之間失去所有的便利性，您可能會感到害怕。不過，只要謹慎考慮應用程式安裝的決定 (稍後會說明)，就能減少或消除許多預期的困難。


儘管替代方案越來越好，但一想到要做這樣的改變，還是會讓人感到反感。如果您發現自己處於這種情況，我最好的建議是讓您的新 GrapheneOS 裝置與現有手機同時使用一段時間。從那時開始，您可以每週慢慢減少使用 2-3 個應用程式，直到您發現自己只會使用 GrapheneOS 裝置為止。


如果您採取這種方法，請嚴格要求自己，儘快斷絕對受監視替代品的依賴。我們人類很懶惰，通常會選擇阻力最小的路徑。請記住您一開始轉換的原因。


*** 您選擇以時間，有時甚至是 Hard 賺來的金錢（取決於您安裝的替代應用程式）來支付，而不是以個人資料來支付。


## 開始使用


GrapheneOS 目前僅生產_(相當諷刺)_[Google Pixel](https://grapheneos.org/faq#supported-devices) 系列手機。這並不是沒有理由的。Pixel 提供最佳的硬體安全性，以補足強化作業系統的工作。這包括特定元件隔離和驗證開機等功能。


### 選擇裝置


在選擇要安裝 GrapheneOS 的 Pixel 時，請確認勾選裝置持續取得預設 [安全更新](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g) 的時間。


在撰寫本文時，Pixel 6a 是目前最便宜的機型，且擁有良好的長期支援，保證至 2027 年 7 月。如果您選擇這款機型，OEM 解鎖將無法使用出廠的原版作業系統。您需要透過空中下載更新，將系統更新至 2022 年 6 月或之後的版本。更新後，您還需要將裝置出廠重設，以修復 OEM 解鎖功能。所有其他已解鎖電信業者的機型都可以直接使用 GrapheneOS。


選擇裝置時，您也要確保購買的是解鎖版本。某些電信業者 (例如 Verizon) 出貨的裝置已鎖定開機載入程式，完全無法進行下列程序。


### 安裝 GrapheneOS


GrapheneOS [web installer](https://grapheneos.org/install/web)讓整個過程輕而易舉，任何人都能在 10 分鐘內完成。

以下說明是取自上述連結的精簡版。


您需要處理的是



- 像素
- 從手機連接至電腦的 USB 傳輸線
- 可執行網頁瀏覽器的電腦 (任何以 Chromium 為基礎的瀏覽器：Chrome、Edge、Brave 等)


讓我們深入了解：


1.第一步是進入 ** 設定** > ** 關於手機**，重複點選建置編號，直到看到 **「開發人員模式」**已啟用。

2.接下來前往 ** 設定** > ** 系統** > ** 開發者選項**，並啟用 **「OEM解鎖」**。

3.現在重新啟動裝置，並在手機重新開機時按住音量下鍵。

4.將手機連接到筆記型電腦，如果出現授權提示，請允許連接。

5.在 Web 安裝程式頁面上，按一下「解鎖開機載入程式」。

6.接著您會看到手機選項變更。使用音量鍵將選項變更為「解鎖」，並使用電源鍵接受。

7.接下來按一下網頁安裝程式頁面上的下載釋放。

8.下載完成後，進入下一步，按一下「Flash Release」。這需要一兩分鐘的時間，您完全不需要碰觸手機。

9.最後，移至網頁安裝程式的下一步，然後按一下 **Lock Bootloader**。您需要變更選擇，並按下電源按鈕確認，方法與之前的步驟相同。

10.當您看到「Start」（開始）一詞時，請按下電源按鈕確認，裝置便會開機進入全新的免 Google 作業系統。


![image](assets/fr/2.webp)

GrapheneOS 開始畫面



在初始開機和設定之後，最好從「設定」>「系統」>「開發者選項」中停用 OEM 解鎖功能。


您可能還需要採取額外、可選但建議的步驟，即透過 Auditor 應用程式驗證安裝。您需要一部已安裝應用程式的 Android 手機來完成此步驟。您可在 [此處](https://attestation.app/tutorial)_找到相關說明。



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

詳細說明上述簡單步驟的視訊



如果這些簡單的步驟看起來太過分，您可以考慮購買附有 GrapheneOS 軟體 [預先安裝](https://ronindojo.io/en/roninmobile) 的 Pixel。只要注意您對提供者有少許信任即可。


### 預先安裝的應用程式


現在您已經設定好了，您可能會注意到 GrapheneOS 在第一次安裝時顯得非常簡陋。預設您會安裝這些應用程式：


![image](assets/fr/3.webp)


預設應用程式


您可能不熟悉的只有「稽核」和「釩」兩種。



- Auditor 應用程式](https://play.google.com/store/apps/details?id=app.attestation.auditor) 使用以硬體為基礎的安全功能來驗證裝置的身份以及作業系統的真實性和完整性。它會驗證裝置是否在鎖定開機載入程式的情況下執行原廠作業系統，以及作業系統是否被竄改。
- [Vanadium](https://github.com/GrapheneOS/Vanadium) 是 Chromium 網頁瀏覽器的隱私與安全加固變體。


## 客製化


手機設定是個人化的東西，但以下是我在安裝 GrapheneOS 時最先變更的一些項目，讓自己更有家的感覺。


### 設定壁紙和更新主題


前往「設定」>「壁紙與樣式」。從這裡開始：



- 更新首頁和鎖定螢幕背景，以取得從網路上下載的圖片。
- 選擇整個 UI 使用的重點顏色。
- 啟用 Dark 主題。


### 顯示電池百分比


前往 ** 設定** > **電池**，然後在狀態列中啟用 **顯示電池百分比**。


### 匯入聯絡人


**From another Android phone** - Head to Contacts app and look for the Export to VCF option.


**From iOS** - 使用類似 Export Contact 的應用程式，並使用「vCard」匯出選項匯出 VCF 檔案。

取得 VCF 檔案後，您可以使用 microSD 卡或 USB 磁碟機等外接式儲存裝置，將檔案傳輸至您的 GrapheneOS 裝置。如果您手邊沒有這些儲存裝置，您可以選擇透過下列其中一個應用程式來分享。


![image](assets/fr/4.webp)


個人化首頁畫面



## 替代應用程式


為了讓您的手機更有用，您需要安裝一些應用程式！以下的選項之所以包含在內，是因為我個人曾使用過這些選項，或是因為這些選項受到廣大隱私社區的強力推薦。還有許多其他很棒的選項沒有被提及，[Awesome Privacy](https://awesome-privacy.xyz) 提供一個非常廣泛的清單，列出所有類型裝置的隱私保護應用程式。


一個應用程式是自由與開放原始碼軟體 (FOSS)，並不代表它不會有潛在的隱私洩漏。使用 [Exodus](https://reports.exodus-privacy.eu.org/en/) 查看您偏好的應用程式在隱私權審核方面的表現。


### F-Droid


[F-Droid](https://f-droid.org/) 是 Android 上可安裝的 FOSS 應用程式目錄。用戶端可輕鬆地在裝置上瀏覽、安裝和更新應用程式。值得一提的是，透過 F-Droid 更新有時候會比其他應用程式商店慢。這主要取決於應用程式是否透過主 F-Droid 套件庫或自訂套件庫找到。


要安裝 F-Droid，只需透過 GrapheneOS 手機上的瀏覽器前往他們的網站，然後點選下載。這會下載一個 `.apk` 檔案。接著會詢問您是否要安裝應用程式。


除了在 F-Droid 預設儲存庫中找到的應用程式外，許多開放原始碼專案也會主持他們自己的儲存庫，可以在 F-Droid 應用程式設定中加入。如果屬於這種情況，相關專案會在其網站上教您完成所需的簡單步驟。


![image](assets/fr/5.webp)


F-Droid 首頁畫面


https://planb.network/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

### Aurora 商店


[Aurora Store](https://auroraoss.com/) 是 Google Play 商店的 FOSS 版本。Aurora 的外觀和感覺與傳統的 Play 商店非常相似，並允許您下載和更新任何您通常透過 Google 選項找到的應用程式。


Aurora 的殺手功能是匿名登入。這表示您可以下載任何無法透過 F-Droid 或直接 APK 下載的喜愛應用程式，而無需登入 Google 帳戶。


在您急著將其設定為預設安裝選項之前，請記住我們試圖擺脫的許多應用程式都是從 Play 商店安裝的。僅僅因為它們可以從 Aurora 存取，並不能改變某些應用程式可能內嵌追蹤功能的事實。這並不總是可能的，但只要可以，在透過 Aurora 下載之前，請尋找 F-Droid 的替代方案。


要安裝 Aurora，只需在 F-Droid 中搜尋「Aurora Store」即可。


Aurora 也有一些潛在的攻擊媒介，因為「匿名帳號」確實是由 Aurora 所建立和控制。理論上，他們可以提供惡意更新或推送應用程式到您的手機，不過您仍必須接受裝置上的安裝提示。Aurora 有時也會因區域和裝置誤讀而導致應用程式無法顯示。這通常可以透過以下步驟解決。


**Top tip** - Aurora Store 有時候會出現速率限制，限制您搜尋和安裝應用程式的能力。若要解決這個問題，請前往 ** 設定** > ** 應用程式** > ** 極光** > ** 預設開啟**，然後將網域 `play.google.com` 加入。現在，每當瀏覽到產品或服務的網站時，只要有「透過 Play 商店下載」的連結，點選它就會在 Aurora 中開啟該應用程式供您下載。



![image](assets/fr/6.webp)


Aurora 商店首頁畫面


https://planb.network/tutorials/computer-security/data/aurora-store-b3345da7-1ed1-407e-a9ae-a1c7f0ba9967

### APK 下載


Android 上的應用程式也可以透過「.apk」檔案下載和安裝。這是一個很棒的選擇，不需要第三方應用程式商店，只要直接從專案或服務的網站或 GitHub 套件庫下載檔案即可。


這種方法的缺點是您無法獲得自動更新，因此您需要監控該服務的通訊管道，才能得知新版本的資訊。不過有一個很棒的專案叫做 Obtanium，目的就是要解決這個問題。[Obtainium](https://github.com/ImranR98/Obtainium)可讓您直接從其發佈頁面安裝與更新開放原始碼應用程式，並在有新版本時接收通知。


![image](assets/fr/7.webp)


Obtanium 預覽


### 網頁應用程式


如果您不常使用某項服務，但又不想下載原生應用程式，您可以簡單地存取網頁版本。現在許多網站也提供 Progressive Web App (PWA) 支援。您可以將特定網站 (例如 Twitter.com) 加入書籤到您手機的首頁畫面。然後當您點擊圖示時，它就會以全螢幕應用程式的方式開啟，而不會受到一般瀏覽器體驗的干擾。您可以參考以下範例。


要在 Vanadium（GrapheneOS 的原生瀏覽器）中實現這一目標，只需導航到所選的網站，點擊螢幕右上角的三個垂直圓點，然後點擊 **「添加到主螢幕」**。


這種方法唯一的缺點是，由於這只是一個書籤網頁，您不會收到任何形式的通知。雖然有些人可能會認為這是個好處！


![image](assets/fr/8.webp)


Twitter PWA


### 網頁瀏覽器


使用預先打包的選項 Vanadium 真的不會有錯。此應用程式與我試過的任何其他行動瀏覽器表現相同，而且我從未遇到任何相容性問題。


當您需要存取 Tor 原生的 `.onion` 網站時，您可以直接從他們的 [網站](https://www.torproject.org/download/#android) 或透過 F-Droid 下載 Tor 瀏覽器 APK。


### VPN


要保護您的線上活動不受網路服務供應商 (ISP) 的窺探，虛擬私人網路 (VPN) 應用程式是一個不錯的選擇。VPN 透過加密隧道將您的網際網路流量傳送到由 VPN 服務供應商控制的共用 IP Address，以確保您的裝置活動無法與您聯繫。


這裡有兩個公認的選項，可以讓您在不提供任何個人資訊的情況下用比特幣支付服務。兩者都可在 F-Droid 上取得。





https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68

https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### 訊息


近年來，加密訊息的解決方案越來越多。但問題是，您可以在手機上安裝最好、最隱密的選項，但如果您沒有聯絡人使用，那又有什麼意義呢？


大多數對隱私空間毫無興趣的人可能都在使用 WhatsApp 或 iMessage。前者可透過 Aurora Store 下載，但後者無法在 GrapheneOS 上運作 (很明顯！)。



- [Signal](https://signal.org/)是較受歡迎的端對端加密 (E2EE) 聊天工具之一，擁有良好的記錄和豐富的功能。Signal 需要電話號碼才能註冊，因此如果您打算與不知道您電話號碼的人聊天，或許可以考慮其他的替代方案。Signal 必須透過 Aurora 商店下載。
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) 是一個相當新的 E2EE 訊息傳遞工具。它沒有使用者 ID，不需要電話號碼或個人資訊。人們可以透過掃描您的個人 QR 代碼或造訪您的獨特連結找到您。Simplex 也允許進階使用者運行自己的伺服器，以進一步減少對任何中央實體的依賴。Simplex 沒有桌面用戶端，因此如果多裝置是您的優先選項，則可能不太適合。適用於 Android 的 Simplex 可透過 F-Droid 取得。
- [Threema](https://threema.ch/en/faq/libre_installation)提供類似 Simplex 的體驗，但歷史更悠久，因此感覺上更精進一些。Threema 並非免費，終身授權需要 $4.99，可以用 Bitcoin 購買。Threema 提供網頁用戶端和原生桌面應用程式。Android 應用程式可透過 F-Droid 取得。
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) 是 Android 版 Telegram 官方應用程式的非官方 FOSS Fork。Telegram 有 E2EE「秘密聊天」功能，但預設選項並非隱私。Telegram FOSS 可從 F-Droid 下載。


![image](assets/fr/9.webp)

左: Threema, 右：單色


https://planb.network/tutorials/computer-security/communication/signal-8dfb5572-6962-4f1c-bfa5-3192da4e9a4e

https://planb.network/tutorials/computer-security/communication/telegram-09ab3cf3-7625-4267-97a1-24e59a9e5943

https://planb.network/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3

https://planb.network/tutorials/computer-security/communication/simplex-chat-7a1efa11-4d0a-49c4-92aa-e18bf22c22b9

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74

### 媒體



- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/)是一個跨平台的 Spotify 用戶端，不需要 Premium 帳戶。Spotube 可透過 F-Droid 使用。
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/)是一款神奇的應用程式，可免費蒸錄 YouTube 音樂中的任何音樂。ViMusic 可從 F-Droid 購買。
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/)提供沒有惱人廣告和可疑權限的 YouTube 體驗。有了 NewPipe，您可以訂閱頻道、在背景中收聽，甚至下載以供離線觀看。NewPipe 可透過 F-Droid 進行存取。
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/)是一個 Podcast 播放器，可讓您訂閱和管理所有喜愛的節目。AntennaPod 可透過 F-Droid 使用。


![image](assets/fr/11.webp)

左: Spotube, 右：ViMusic


### 地圖


如果您想要在開車時使用語音輔助，並在 GrapheneOS 中使用地圖應用程式，您需要安裝 [RHVoice](https://rhvoice.org/installation/)，並 [configure](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) 它。



- [Magic Earth](https://www.magicearth.com/) 是一款地圖替代軟體，支援轉向導航、3D 和離線地圖。Magic Earth 可從 Aurora 商店下載。
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) 是基於眾包 OpenStreetMap 資料，供旅行者、遊客、遠足者和騎單車者使用的另類地圖。它是 Maps.me 應用程式 (之前稱為 MapsWithMe) 的一個注重隱私的開放原始碼 Fork。它支援 100% 的功能，無需使用中的網際網路連線，並可從 F-Droid 下載。
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) 是另一個很棒的地圖替代方案，支援上述所有功能。


![image](assets/fr/13.webp)

左: Magic Earth, 右：有機地圖


### 電子郵件



- [Proton Mail](https://proton.me/mail) 提供免費的私人電子郵件服務，支援已審核的 E2EE。Proton 也提供付費版本，支援自訂網域和 [aliasing](https://proton.me/support/creating-aliases)。Proton Mail 可直接下載 APK 或透過 Aurora 下載。
- [Tutanota](https://tutanota.com/) 提供與 Proton Mail 相同的功能，包括可選的付費服務，可直接下載 APK 或透過 F-Droid 下載。
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) 是一個開放原始碼的電子郵件用戶端，基本上可以與所有的電子郵件供應商合作。它支援多個帳號、統一收件匣和 OpenPGP 加密標準。


![image](assets/fr/15.webp)

左：Proton Mail，右：Tutanota


### 生產力



- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/)是一款檔案同步程式。它能在兩部或多部裝置之間即時同步檔案，並安全地防止他人窺探。您的資料是您個人的資料，您理應選擇儲存的地點、是否與第三方共用，以及如何透過網際網路傳輸。Syncthing 可透過 F-Droid 使用。
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/)當連接到您的家庭網路時，您所有的裝置都可以輕鬆地互相對話。輕鬆地在您所有的裝置上傳送檔案、相片、剪貼簿資料 (甚至在 iOS 上！)。KDE connect 可以從 F-Droid 下載。
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/)是一款 E2EE 筆記應用程式，可在所有裝置上同步您的想法和待辦事項。他們的免費計劃應可涵蓋大部分的個人使用情況。Notesnook 可在 F-Droid 上使用。
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) 與 Notesnook 非常相似，但需要付費計劃才能匹配功能集。Standard Notes 可透過 F-Droid 使用。
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) 是一款鍵盤應用程式，可讓您自訂任何您能想到的手機打字體驗。可透過 F-Droid 下載。
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) 是預設的 Google 鍵盤應用程式。根據我的經驗，它提供迄今為止最佳的輸入和滑動體驗。如果您下載此應用程式，請確保完全停用所有與網路相關的權限。可透過 Aurora 下載。


![image](assets/fr/17.webp)

左：Notesnook，右：KDE Connect


### 生活方式



- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) 是一款設計精美的開放原始碼天氣應用程式，可透過 F-Droid 使用。它也支援不同尺寸的小工具，讓您可以直接從主螢幕上看到所選地點的天氣。
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) 是一款開放原始碼且保護隱私的翻譯應用程式，支援超過 200 種語言。Translate You 可透過 F-Droid 使用。
- [質子日曆](https://proton.me/calendar/download) 是一款簡單易用的 E2EE，可與您的質子電子郵件帳戶無縫互動。Proton Calendar 可以 APK 或透過 Aurora 商店下載。
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/)是一款用於顯示和儲存登機證、優惠券、電影票和會員卡等的應用程式。只需下載相關的「pkpass」或「espass」檔案，然後用該應用程式開啟即可。PassAndroid 可透過 F-Droid 使用。


![image](assets/fr/19.webp)

左：幾何天氣，右：質子日曆


### 安全性/隱私權



- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) 為您的所有裝置提供免費和 E2EE 跨平台密碼管理解決方案。他們的付費服務可讓您在應用程式中整合 2FA 密碼。Bitwarden 的伺服器端可自行託管，Android 應用程式則可透過 F-Droid 使用。
- [Proton Pass](https://proton.me/pass/download) 提供類似 Bitwarden 的免費服務，但 [Proton Unlimited](https://proton.me/pricing) 客戶能使用額外的進階功能。Proton Pass 可透過 APK 或 Aurora 使用。
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/)是一款雙因素驗證應用程式，適用於使用一次性密碼通訊協定的系統。可透過掃描 QR 碼輕鬆添加令牌。FreeOTP 可透過 F-Droid 使用。
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/)是一款免費、安全且開放原始碼的 Android 應用程式，用來管理您線上服務的 2 步驗證代碼。Aegis 可透過 F-Droid 使用。
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/)是一項付費的跨平台服務，可在本機為您的資料加密，以便您可以安全地將資料上傳到您最喜愛的雲端服務。Cryptomator 可透過 F-Droid 下載。


![image](assets/fr/21.webp)

左：質子通道
右：Bitwarden


https://planb.network/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

https://planb.network/tutorials/computer-security/data/cryptomator-84e52c76-2253-49fe-81da-e05e90c28d0d

### 雲端解決方案



- [Proton Drive](https://proton.me/drive/download) 是一個付費的 E2EE 雲端解決方案，用來備份和儲存您所有的檔案。在撰寫本文時，他們剛宣佈推出 Windows 桌面用戶端，但 Mac 和 Linux 使用者必須繼續使用網頁版從電腦進行同步 (目前)。Android 用戶端可透過 APK 或 Aurora 取得。
- [Skiff](https://skiff.com/download) 也提供付費的 E2EE 雲端儲存和檔案協作工具。他們提供 Mac 和 Windows 桌面用戶端（以及 Web 應用程式），其 Android 用戶端則必須從 Aurora 下載。
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/)為協作、跨裝置同步和檔案儲存提供功能齊全的雲端解決方案。更進階的使用者可以選擇在任何喜歡的硬體上自行託管他們的免費開放原始碼軟體。Android 用戶端可透過 F-Droid 下載。
- [Cryptpad](https://cryptpad.fr/)提供了一個免費的、基於網絡的、E2EE 的 Google Docs 替代方案。


![image](assets/fr/23.webp)

寶騰驅動器


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

## 缺點


開放原始碼與隱私權保護的替代方案比您習慣使用的科技集團應用程式多不勝數，而且其中有些往往比封閉式原始碼、充滿間諜軟體的替代方案更好。


然而，當轉換到 GrapheneOS 時，由於沒有其他選擇，您必須放棄一些生物上的舒適。這些包括



- Apple CarPlay/Android Auto** - 您需要堅持使用傳統的藍牙、USB 或 Aux。
- Apple/Google Pay** - 無論如何，幾乎每個人都會隨身攜帶 Wallet！
- 銀行應用程式** - 這些應用程式並非完全無法運作。有些可以，事實上非常好用。其他應用程式只能在啟用 Google Play 服務 (請參閱下文) 的情況下運作，其他應用程式則完全無法運作。請閱讀有關您銀行的報告 [這裡](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) 以瞭解目前的情況。如果您的銀行在無法運作的名單上，請不要害怕，記得您可以將 URL 儲存為網頁應用程式放在主畫面上。
- 推播通知** - 大部分應用程式在不使用特定應用程式時，都會透過 Google Play 服務來傳送更新訊息給您。GrapheneOS 預設並未安裝這些服務，因此如果您發現朋友傳送電子郵件給您時，您沒有立即收到通知，很可能就是這個原因。好消息是，上面提到的一些應用程式已執行自己的背景連線，定期檢查更新，然後在需要時給您通知。


### 沙盒的 Google Play


**請注意：** GrapheneOS 有一個相容性 Layer，提供在標準應用程式沙盒中安裝和使用 Google Play 正式版本的選項。Google Play 在 GrapheneOS 上絕對沒有任何特殊存取權限或特權，相對於繞過應用程式沙箱並獲得大量高特權存取權限。


如果您發現自己最喜歡的應用程式不能沒有推送通知，或是某個「必備」應用程式沒有 Play Services 就沒有用，GrapheneOS 可讓您在完全沙盒化的環境中 [安裝](https://grapheneos.org/usage#sandboxed-google-play-installation) 這些服務。安裝之後，這些服務不需要 Google 帳戶就能運作，而且每個服務的權限都可以嚴格控制。


在您急著在第一天安裝這些應用程式之前，我建議您先看看沒有這些應用程式的情況。您可能會驚訝於有多少應用程式在沒有安裝的情況下仍能正常運作。


如果您真的要安裝，只要點選預先安裝的「Apps」應用程式，然後點選「Google Play Services」即可。您可以考慮將它們與那些較不隱私的應用程式一起安裝，並安裝在完全獨立的使用者個人資料中，以提供額外的 Layer 與手機其他部分的隔離。


![image](assets/fr/24.webp)

播放服務安裝畫面


### 簡介


GrapheneOS 可讓您在手機內擁有獨立的手機體驗。額外的設定檔可安裝自己的應用程式和服務，但無法存取機主帳戶的任何檔案或資料。

如果您只有一、兩個必須使用 Play 服務的應用程式，但又不常使用，將這些應用程式與 Play 服務一起安裝在獨立的設定檔中，可能是個好主意，可進一步保護因在所有者設定檔中執行而留下的任何微小隱私影響。


您可以在 [這裡](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2) 閱讀更多關於此使用個案的資訊。


如果您決定新增一個獨立的設定檔，以符合您的使用情況，應用程式 [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) 可能會對您有用。Insular 可讓您輕鬆地將任何現有的應用程式複製到新的設定檔，而無需透過本指南前文所述的任何傳統安裝途徑。Insular 還可讓您快速「凍結」任何應用程式，以完全停用該應用程式的所有背景服務。


![image](assets/fr/24.webp)

使用者設定檔管理畫面


### e-Sims


如果您想讓您的手機隱私更上一層樓，並擁有一個與您現實世界身份分離的手機服務，eSIM 可能會適合您。eSIM 是一種虛擬 SIM 卡，您可以線上購買，然後透過 QR 碼將其加到您的手機上。提供這種可以用 Bitcoin 匿名支付的服務的公司包括 [Silent.Link](https://silent.link/) 和 [Bitrefill](https://www.bitrefill.com/gb/en/esims/)。


eSIM 不應該被視為完全解決電話隱私問題的靈丹妙藥。如果使用得當，eSIM 可能是個有用的工具，但如果您想完全「離網」，請務必研究使用任何類型行動服務的 [取捨](https://grapheneos.org/faq#cellular-tracking)。


必須安裝 Sandboxed Play Services 才能在 GrapheneOS 中供應 eSIM。


## 備份


在完成新的 de-Google'd Pixel 手機設定後，最好先為自己建立備份。此備份可讓您在遺失手機或手機遺失/遭竊時，將手機還原至相同的狀態。


您可以選擇將備份檔案儲存至任何外部儲存媒體，或儲存至自行託管的雲端解決方案 (如 Nextcloud)，不過有些使用者表示後者的成功率不一。


若要建立您的第一個備份：


1.移至 ** 設定** > ** 系統** > **備份**，然後寫下 12 個字的復原碼。日後需要使用此代碼來解密備份檔案。遺失代碼即無法存取手機備份。

2.接下來選擇您的儲存位置。我建議使用外接式 USB 磁碟機或工業級 microSD 卡。

3.選擇要備份的資料。如果您指定的儲存媒體有足夠的空間，我建議選擇所有內容。

4.點選右上方的三個圓點，然後選擇 ** 立即備份**。


![image](assets/fr/26.webp)


備份畫面


請記住，如果您正在離線備份至外部儲存媒體，定期完成此步驟會很有意義，以確保如果發生最壞的情況，手機最近的任何重要更新都不會遺失。


![video](https://www.youtube.com/embed/eyWmcItzisk)


詳細介紹備份過程的視訊


## 總結


近年來，GrapheneOS 軟體已顯著成熟。它比以往更穩定、更相容。再加上蓬勃發展的開放原始碼與隱私權保護應用程式生態系統，讓 GrapheneOS 成為 Android 或 iOS 的真正可行替代方案，即使是像您一樣的「普通人」也能使用！


資料外洩和拉網式監控在現今世界已經司空見慣，幾乎不再成為頭條新聞。保護自己是您的責任。一路上會有許多調整和犧牲，但降低您遭受這些侵害的風險遠遠沒有您想像中那麼困難。


我希望這份指南能對您的旅程有所幫助。如果您認為本指南有用，並願意支持我的工作，請考慮寄送 [捐款](/tips)。


如果您是現有的 GrapheneOS 使用者，或是因為本指南而成為 GrapheneOS 使用者，請考慮 [捐款](https://grapheneos.org/donate) 來支持他們的重要工作。


### 瞭解更多


GrapheneOS 是一個任何人都可以輕鬆花上好幾個星期去探索的兔子洞。您可以學習和修補許多東西，以根據您的需求和威脅模型量身打造體驗。以下是一些連結，您可以繼續您的旅程：



- [GrapheneOS 官方使用指南](https://grapheneos.org/usage) - 官方網站
- [GrapheneOS論壇](https://discuss.grapheneos.org/) - 官方網站
- [GrapheneOS 設定大師班](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - 由「隱私權路人」提供的影片
- [GrapheneOS General Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast by 'Watchman Privacy'


*本教程改編自 [BitcoinQnA 在 Bitcoiner.Guide 上以 MIT 授權發佈的原始內容](https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md)，其最初的撰寫工作應完全歸功於 BitcoinQnA。*

