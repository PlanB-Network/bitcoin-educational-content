---
name: LineageOS
description: 適用於智慧型手機的免費 Android 作業系統
---

![cover](assets/cover.webp)



智慧型手機上預先安裝的傳統 Android 系統有許多眾所皆知的問題：Google 服務的密集整合導致持續的資料追蹤、製造商強加的不需要的贊助應用程式 (bloatware)，以及幾年之後就放棄更新追蹤，使得仍能運作的裝置被程式化淘汰。



LineageOS 為這些問題提供了一個優雅的答案。LineageOS 是開放原始碼社群的產品，也是 CyanogenMod (2016 年底停產) 的直接繼承者，是一個免費的 Android 手機作業系統，讓使用者重新掌控智慧型手機。該專案於 2016 年 12 月正式推出，目前在全球擁有超過 440 萬個活躍安裝，並支援超過 20 個不同品牌的數百種手機機型。



![lineageos-homepage](assets/fr/01.webp)



*介紹專案及其目標的 LineageOS 官方網站*



## 什麼是 LineageOS？



### 理念與目標



LineageOS 是基於 Android 開源專案 (AOSP) 的開放原始碼行動作業系統，由全球龐大的志願貢獻者社群所開發。它的非官方座右銘可能是「您的裝置，您的規則」：該專案旨在延長智慧型手機的使用壽命，同時提供簡化、隱私友好的 Android 體驗。



該專案從史上最流行的另類 Android ROM 之一 CyanogenMod 的灰燼中崛起。當 CyanogenMod Inc. 在 2016 年 12 月關門時，社群動員創造了 LineageOS，保留了前身的創新精神和開源理念。



有別於 OEM Android 發行版本，LineageOS 預設不預先安裝任何 Google 應用程式，並完全消除臃腫的軟體。使用者一開始使用的是極簡的系統，只包含必要的應用程式 (電話、訊息、相機、瀏覽器)，並可自由選擇後續新增的應用程式。



### 影響與社區



官方統計數據顯示了該專案的規模：LineageOS 在 224 個國家/地區擁有超過 440 萬個活躍安裝，是全球最廣泛採用的 Android 替代方案之一。巴西以超過 200 萬的使用者數領先，其次是中國和美國，顯示出免費、可客製化 Android 的普遍吸引力。




## 主要功能



### Interface 和使用者體驗



**Pure Android**：LineageOS 提供接近 AOSP 的真實 Android 體驗，沒有製造商的覆蓋或多餘的應用程式。Interface 保持 Android 使用者熟悉的操作方式，同時因沒有臃腫軟體而提供最佳流暢性。



**預設不含 Google**：基於法律與道德理由，不預先安裝任何 Google 服務。這種「不含 Google」的方式可保證完全控制您的個人資料，並透過避免服務在背景執行來改善效能。



### 客製化與安全性



**進階客製化**：LineageOS 釋放了許多在 Android 上無法使用的選項：導航按鈕重新配置、可自訂的系統主題、適用於不同情境 (工作、個人、遊戲) 的使用設定檔。



**Outil Trust**：整合式功能可監控裝置的安全狀態，並對潛在威脅發出警示，提供系統安全的即時可見性。



**延長更新**：LineageOS 社群承諾每月提供安全修補程式，讓製造商停產的裝置繼續接收最新的 Android 安全修補程式。



## 相容裝置



LineageOS 支援來自 20 多家製造商的數百種裝置：Samsung、Xiaomi、OnePlus、Motorola、Sony、Google Pixel、Fairphone 等等。相較於 GrapheneOS 等僅限於 Pixel 裝置的替代方案，這種廣泛的相容性是該專案的主要優勢之一。



![devices-compatibility](assets/fr/02.webp)



*按製造商篩選的 LineageOS 相容裝置頁面*



![google-devices](assets/fr/03.webp)



*支援 Google 裝置，包括 Pixel 4 (代號「火焰」)*



### 熱門裝置



根據官方統計，使用率最高的機種包括多種不同價格和機齡的裝置，顯示 LineageOS 有能力為舊款智慧型手機注入新生命，同時也能優化新機。



### 安裝前的重要事項



**Unlockable bootloader**：檢查您的製造商/營運商是否允許解鎖。有些品牌 (例如華為) 已經在最近的機型上取消這種可能性，而其他品牌則強制規定特定程序。



**確切的機型**：下載精確對應您裝置的 ROM 是非常重要的。兩個商品名稱相似的型號可能在技術上有所不同 (例如 Galaxy S10 vs S10 5G)，因此需要不同的映像檔。



**可擴充的支援**：較新的裝置可能無法立即獲得支援，因為移植需要志願開發人員的照顧。相反地，如果裝置的維護者退出專案，支援也可能會停止。



## 安裝



### 必要的先決條件



⚠️ **開始前請先完整閱讀本說明書**，以免發生任何問題！



**Return to stock firmware (if necessary) :**




- Android Flash 工具**：使用 Google 官方工具 [flash.android.com](https://flash.android.com)，可從網頁瀏覽器 (需使用 Chrome/Edge) 輕鬆將 Pixel 裝置還原為 Android 原廠版本
- 替代**：從 [developers.google.com/android/images](https://developers.google.com/android/images) 手動製作工廠影像。



**強制性先決條件測試：**




- 使用原始系統啟動裝置至少一次**。
- 測試所有功能**：簡訊、通話、Wi-Fi、行動資料
- 重要**：檢查您是否可以發送/接收簡訊和撥打/接聽電話（包括透過 WiFi 和 4G/5G）。如果在原生系統上無法運作，在 LineageOS 上也無法運作！
- 最近的裝置**：有些裝置需要在原廠系統上至少使用一次 VoLTE/VoWiFi 才能提供 IMS



**系統準備：**




- 移除裝置上的所有 Google** 帳戶，以避免「出廠重設保護」（Factory Reset Protection）可能會阻止啟動。
- 完整備份** ：此過程會完全刪除您的手機。備份相片、聯絡人、應用程式和重要檔案



**ADB 和 Fastboot 工具：** 按照 [LineageOS 官方指南](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) 安裝 Android SDK 平台工具。使用 `adb version` 和 `fastboot --version` 驗證安裝。



**電話配置：**




- 啟動 **開發者選項**：設定 > 關於 > 點選「版本編號」7 次



![android-version](assets/fr/06.webp)



*導覽至「設定」>「關於手機」以啟動開發者模式*。





- 在「開發者」選項中啟用 **USB 除錯**。
- 啟動 **OEM 解鎖** (解鎖開機載入程式的必要條件)



![developer-options](assets/fr/07.webp)



*啟用「開發者選項」、USB 除錯和「OEM 解鎖*」功能



### 詳細安裝



⚠️ **這些說明是 LineageOS 22.2 所特有的。請準確遵循每個步驟。若有任何失敗，請勿繼續前進！



#### 步驟 1：韌體檢查



** 需要韌體**：您的裝置必須已安裝 Android 13 才能繼續（針對 Pixel 4）。韌體是指股票系統中包含的特定裝置影像。



![pixel4-info](assets/fr/04.webp)



*官方 Pixel 4 頁面提供下載連結與安裝指南*。



![downloads-page](assets/fr/05.webp)



*LineageOS build 下載頁面與檔案*



**Pixel 4 特定下載：**




- 建立 LineageOS**：[download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- 所需的檔案**：從本頁下載 3 個所需的檔案 (這些檔案會在下列步驟中使用)：
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (main ROM)
  - dtbo.img` (磁碟分割裝置樹 blob)
  - `boot.img` (復原 LineageOS)



⚠️ **重要**：檢查 Android 版本，而非製造商的作業系統版本。使用自訂 ROM（即使是 LineageOS）並不保證符合此要求。



💡 **提示**：如果對您的韌體有疑問，請先回到原廠系統再繼續！



#### 步驟 2：解鎖開機載入程式



⚠️ **此步驟會刪除您的所有資料！





- 測試 ADB 連線**：透過 USB 連接您的裝置，並從電腦終端機使用 `adb devices` 指令進行測試



![adb-devices](assets/fr/08.webp)



*使用 `adb devices`* 指令檢查 ADB 連線





- 在手機上授權連線**



![usb-debugging-auth](assets/fr/09.webp)



*使用電腦的 RSA 指紋啟用 USB 除錯功能*





- 開機進入開機載入模式** ：


```
adb -d reboot bootloader
```


或按住 ** 音量下降 + 電源** 裝置關閉





- 檢查 fastboot** 連線：


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*在終端機執行 Fastboot 指令以檢查連線*



![bootloader-screen](assets/fr/11.webp)



*Pixel 4 的 fastboot 顯示系統資訊*。





- 解鎖開機載入程式** ：


```
fastboot flashing unlock
```


在裝置上，使用音量鍵瀏覽，然後按下 **Power** 按鈕，選擇「解除開機載入程式」並確認操作



![unlock-bootloader](assets/fr/12.webp)



*確認裝置上的開機載入解鎖*



⚠️ **確認解鎖後，手機會自動重新啟動**。





- 自動重新啟動**後，在開發者選項中重新啟用 USB 除錯功能




#### 步驟 3：快閃其他磁碟分割



⚠️ **復原正常運作所需**





- 重新啟動開機載入程式**：按下音量 + 電源
- Flash** (將 `/path/to/` 改為您下載檔案的資料夾) ：


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*透過 fastboot* 更新 dtbo 和 boot.img 磁碟分割



#### 步驟 4：安裝 LineageOS recovery





- Flash recovery** (將 `/path/to/` 改為下載檔案的資料夾) ：


```
fastboot flash boot /chemin/vers/boot.img
```




- 在復原中重新啟動**以檢查



#### 步驟 5：安裝 LineageOS





- 以恢復模式重新啟動**：音量下 + 電源 → 復原模式



![recovery-mode](assets/fr/14.webp)



*從 LineageOS 復原的 Interface 與主功能表*。





- 出廠重設** ：輸入 「工廠重設」→「格式化資料/工廠重設」



![factory-reset](assets/fr/15.webp)



*在 LineageOS* 復原中重設工廠的過程





- 返回主選單**
- 側載 LineageOS** ：
   - 在裝置上：「套用更新」→「從 ADB 套用」
   - 在電腦上： `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*在 recovery* 中選擇「套用更新」，然後選擇「從 ADB 套用」。



![sideload-process](assets/fr/17.webp)



*透過 sideload* 進行 LineageOS 安裝中



![sideload-terminal](assets/fr/18.webp)



*在終端機中執行側載指令，並顯示安裝進度*



💡 **正常**：程序可能會在 47% 時停止或顯示「成功」錯誤 - 這是正常現象！



#### 步驟 6：首次啟動





- 重新啟動**：「立即重新啟動系統」
- 第一次開機**：可能需要 15 分鐘



🎉 **安裝完成！**



### 注意事項



⚠️ **警告**：LineageOS 以「現狀」提供，不提供保固。雖然我們已盡力確保一切運作正常，但您仍需自行承擔安裝風險！



**關鍵檢查：**




- 韌體相容性**：請務必在您機型的下載頁面上檢查所需的韌體版本
- 安裝 LineageOS 之後，切勿重新上鎖**開機載入程式
- 請遵循您裝置的特定指示**



## 設定與應用



### 首次啟動


簡化的 Interface，接近 Android 原版，不需要 Google。設定簡單：語言、Wi-Fi，不需要帳號。



### 替代應用



**安全應用程式來源：**



**F-Droid** ：基準開源應用程式商店，預先安裝於 LineageOS for microG 或可直接下載。F-Droid 只提供經過驗證與透明編譯的開放原始碼軟體，保證沒有追蹤程式或惡意元件。



**Aurora Store**：無需 Google 帳戶即可存取 Google Play 商店的匿名用戶端。Aurora 借用共用的匿名帳號，讓您在下載主流應用程式的同時，也能保護您的隱私。



**Essential alternative applications:**





- 導航**：有機地圖（基於 OpenStreetMap 的離線地圖）
- 通訊**：Signal (端對端加密訊息)、K-9 Mail (免費電子郵件用戶端)
- 媒體**：NewPipe (無廣告、無追蹤的 YouTube)、VLC (通用媒體播放器)
- 生產力**：Nextcloud (自託管雲端)、Simple Calendar (CalDAV 同步)
- 安全性**：Bitwarden (密碼管理器)、Aegis Authenticator (2FA 代碼)



這些應用程式 (大部分可透過 F-Droid 取得) 形成一個連貫的生態系統，可完全取代 Google 服務，同時提供現代化、功能性的使用者體驗。



## 使用與保養



### 每日體驗



LineageOS 改變了 Android 體驗，將流暢性和反應速度放在首位。精簡的 Interface 在舊裝置上尤其有效，讓舊裝置煥然一新，由於沒有厚重的覆蓋層和多餘的程序，效能普遍優於製造商的 ROM。



基本功能 (通話、簡訊、相片、瀏覽) 可順暢運作，而客製化工具則可讓系統在不影響穩定性的情況下，依個人喜好進行微調。



### OTA 更新系統



LineageOS 具備特別易用的 Over-The-Air 更新系統。新版本會透過通知自動提出，安裝時只需點擊幾下，無需複雜的技術干預。此過程會完全保留您已安裝的資料與應用程式。



這些定期更新是一項重要資產，尤其是對製造商已停產的裝置而言，他們可以繼續受惠於最新的 Android 安全修補程式。



### 建議的最佳做法



**安裝後的安全性：**




- 設定強大的 PIN 或密碼以進行解鎖
- 檢查是否已啟用儲存加密 (通常為預設值)
- 透過 F-Droid 安裝類似 Bitwarden 的密碼管理器



**預防性維護：**




- 定期 OTA 安全更新
- 限制應用程式安裝至可信來源 (F-Droid、Aurora Store)
- 定期檢閱授予應用程式的權限
- 偶爾重新啟動可優化效能並釋放記憶體



## 優點與限制



✅**福利：**




- 預設隱私 (無 Google 追蹤)
- 廣泛的相容性 (300+ 機型)
- 優異的效能（無臃腫軟體）
- 舊裝置的延伸更新



❌ **限制：**




- 技術安裝
- 無 Android Auto/Google Pay
- 銀行應用程式可能有問題



## GrapheneOS vs LineageOS：有什麼區別？



### 不同的方法



**GrapheneOS** 專注於最高安全性，並僅在 Google Pixels 上運行，以利用其專用的安全晶片。該系統結合了許多先進的漏洞緩解措施，並大幅強化應用程式沙箱功能。



**LineageOS** 在儘可能多的裝置上平衡安全性、隱私和便利性。這個方法比較實用，目標是擴充相容性，而非絕對的安全性。



### 管理 Google 服務



**GrapheneOS**：提供可選的沙盒 Google Play 系統。Google Play 可以安裝，但會在嚴格的沙箱中執行，沒有特殊的系統權限。這種獨特的方式讓您可以使用 Google 生態系統，同時維持嚴格的安全控制。



**LineageOS**：讓使用者選擇安裝 Google 服務 (GApps)、microG (免費替代方案)，或完全不使用 Google。最大彈性滿足您的需求。



### 技術比較




| **方面** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **相容性** | 僅限Pixels | 數百台設備 |
| **安全性** | 高級緩解措施 | 標準AOSP安全性 |
| **Google Play** | 可選沙箱 | 可能經典安裝 |
| **安裝** | Web介面 + USB | 技術手動程序 |
| **理念** | 安全第一 | 平衡與選擇自由 |

### 使用建議



**如果您擁有 Pixel，如果最高安全性是您的首要考量，如果您接受強化保護的限制，請選擇 GrapheneOS**。



**如果您擁有非 Pixel 裝置、正在尋找良好的隱私/實用性平衡，或是想要自由選擇與 Google 生態系統妥協的程度，請選擇 LineageOS**。



## 總結



LineageOS 提供一個成熟的選擇，讓您重新掌控 Android 智慧型手機。流暢的體驗、最佳的效能、廣泛的相容性：結合隱私與日常實用性的理想選擇。



## 資源



### 官方文件




- [LineageOS 官方網站](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - 各機型安裝指南
- [LineageOS for microG](https://lineage.microg.org) - 整合 microG 的版本



### 社區




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon帳號@LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1