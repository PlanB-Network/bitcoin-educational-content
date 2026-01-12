---
name: Bitchat
description: 分散式、無網際網路的訊息傳輸，讓您自由溝通
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*BTC Sessions 的這段視訊教學將帶您了解設定和使用 Bitchat 的過程！* * BTC Sessions 的這段視訊教學將帶您了解設定和使用 Bitchat 的過程


Bitchat 源自快速原型開發工作，[@jack](https://primal.net/jack) 在週末的一次編碼會議中開發了最初的概念。不久之後，[@calle](https://primal.net/calle) 加入該專案，共同開發 Android 實作。Jack 目前領導 iOS 版本的開發，而 calle 則在許多其他貢獻者的支持下監督 Android 版本。


## 簡介：自由聊天，沒有網格


想像一下，當網際網路癱瘓、發生自然災害時，或是在通訊受到限制的地方傳送訊息。Bitchat 讓這一切成為可能。Bitchat 是一款分散式的點對點通訊應用程式，可跳過中央伺服器，讓裝置之間直接對話，完全離線使用藍牙和網狀網路。Bitchat 的設計充分考量隱私與彈性，非常適合在傳統連線不可靠或無法連線的地方使用，例如災難現場、偏遠地區，或是想要避開監控的人。Bitchat 的核心技術是使用加密技術，確保每個訊息都經過端對端加密、驗證和防竄改。


在本教程中，我們將介紹 Bitchat 如何運作，以及如何使用它進行真正私密的離線通訊。


## 主要功能


Bitchat 可透過這些 [功能](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features)，實現離線訊息傳送：



- 跨平台相容**：iOS 與 Android 之間的完整通訊協定相容。
- 分散式網狀網路**：透過藍牙低功耗 (BLE) 自動發現對等體及多跳訊息中繼
- 端對端加密**：X25519 金鑰交換 + 私人訊息的 AES-256-GCM
- 基於頻道的聊天**：以主題為基礎的群組訊息，可選擇密碼保護
- 儲存與轉寄**：緩存離線對等人的訊息，並在他們重新連線時傳送
- 隱私第一**：無帳號、無電話號碼、無永久性識別碼
- IRC 式指令：熟悉的 `/join、/msg、/who` 風格介面。
- 訊息保留**：可選擇由頻道擁有者控制全頻道的訊息儲存
- 緊急清除**：輕按三下標誌即可立即清除所有資料
- 現代 Android UI**：使用 Material Design 3 的 Jetpack Compose
- 深色/淺色主題**：終端機風格的美學與 iOS 版本相匹配
- 電池最佳化**：適應性掃描及電源管理


## 1️⃣Bitchat如何運作 - 簡單而言


Bitchat 可讓您直接透過藍牙 (`BLE`如下所示) 向附近的手機傳送訊息，無需網際網路或手機信號。當您開始聊天時，手機會進行安全握手，為您的對話建立獨特的臨時加密金鑰。每封訊息都會受到端對端加密的保護，而且每封訊息都會使用新的金鑰，以確保過去的訊息仍然安全，即使您的手機稍後受到攻擊。最後，應用程式會將訊息分割成小塊，並與隨機的假資料混合，以隱藏您的訊息活動。對於裝置對裝置的直接聊天，它只能在 ~100 公尺的範圍內運作。這就像在擁擠的房間裡傳送加密的紙條一樣，裝置之間直接耳語，在每次訊息之後將金鑰撕碎。


Bitchat 也允許您使用 Nostr 協定和 `#geohashes` 加入基於位置的聊天室。geohash 是一個簡短的代碼，如 `#u33d`，代表一個特定的地理區域，從一個鄰里到整個城市或地區。只需輸入 geohash 聊天室的標籤，您就可以「電傳」到世界各地的任何 geohash 聊天室。您的訊息會透過分散的中繼網路傳送，以保護您的確切位置。此外，每次加入 geohash 聊天室時，您都會被賦予一個新的臨時身份，為您基於位置的對話增加了一層隱私。


如需更精確的技術細節，請參閱 [官方白皮書](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)。


## 2️⃣安裝與設定


### 從何處取得 Bitchat


您可以透過下列方式安裝 Bitchat：



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (適用於 iOS 裝置)
- [Google Play 商店](https://play.google.com/store/apps/details?id=com.bitchat.droid) (適用於 Android 裝置)


Android 使用者也有其他選擇：



- 直接從 [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) 頁面下載 APK 或
- 透過與 Nostr 相容的 [Zapstore] 安裝(https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**注意**：本教學主要針對 Android 實作。iOS 版本可能有所不同。


### 設定流程


安裝完成後，開啟 Bitchat，即可看到這個初始權限畫面。以下是您需要做的：


1. **授予這些必要的權限：**


   - 藍牙存取** (搜尋附近的 Bitchat 使用者)
   - 精確位置** (Android 需要此功能才能使用藍牙)
   - 通知** (接收私人訊息提醒)

2. **停用電池最佳化**：


   - 這可讓 Bitchat 在背景中執行
   - 持續維持網狀網路連線


點選 `Grant Permissions` ，依照 `prompts` 和 `Disable Battery Optimization` 移至下一個畫面。


![image](assets/en/02.webp)


歡迎來到 Bitchat 的主畫面。讓我們開始定位：


### 設定


先做第一件事。點選`Bitchat 標誌`即可開啟設定選單。  下列選項可供使用：



- 設定「外觀」（系統/淺色/深色）。
- 啟用 geohash 的「工作證明」以阻嚇垃圾郵件 (選用)
- 開啟 `Tor` 以加強隱私。


![image](assets/en/16.webp)


### 設定您的身分


點選上方的`bitchat/anonXXXX`欄位，選擇您的使用者名稱。這是其他人在藍牙和網際網路模式下看到您的方式。例如，您可以將 "anon2022 "變更為您選擇的使用者名稱。


![image](assets/en/03.webp)


### 選擇網路頻道


使用 `#location channels` 功能表 (使用者名稱右側) 切換連線類型：



- BLE Mesh****：預設藍牙模式（無網路，距離 10 至 50 公尺）
- #geohashes**：使用 [Nostr 通訊協定] 的網際網路地理群體(https://nostr.com/)


當您選擇「#geohashes」模式時，Bitchat 會與 Nostr 通訊協定整合，以啟用地理社群。您的訊息會發佈到「分散式 Nostr 中繼」，而非 Bitchat 的點對點網路，因此可以進行更廣泛但經過位置過濾的對話。最重要的是，您的 Bitchat 身份金鑰會以加密方式簽署所有 Nostr 事件，以維持身份驗證，而 geohash 標籤 (如鄰里的「#u4pruyd」) 會根據您選擇的精確度過濾訊息。這表示您可以參與當地討論，而無需透露確切的座標，不過需要網際網路連線。


![image](assets/en/04.webp)


### 監控同儕

許可證：CC-BY-SA-V4

對等計數器顯示使用者：



- 附近 (BLE 網格) 或
- 在您的 geohash 區域 (#geohashes)


![image](assets/en/05.webp)


## 3️⃣全球聊天與私人訊息


Bitchat 提供兩種不同的通訊模式，以滿足不同的需求：



- 公開頻道：** 用於與他人公開對話。您可以透過本地 BLE 網狀網路與附近的使用者連線，或透過全球 #geohash 與啟用網際網路、以位置為基礎的社群連線。
- 私人訊息：** 用於安全的一對一對話。這些訊息會建立直接的加密連線，以確保您的交談內容保密。


瞭解這兩種模式將有助於您在對話中游刃有餘。


### 公共管道：社區中心


位置頻道」功能表 (右上方) 控制您的公開能見度。選擇「mesh」可透過 BLE mesh 將您連結到附近的所有使用者，通常是 10-50 公尺範圍內的裝置。這會創造一個開放式論壇，向範圍內的所有人廣播訊息，非常適合活動公告或當地警示。


若要達到更廣泛的地理範圍，請選擇任何 `#geohash` 標籤，加入依地點篩選的網際網路驅動社群。這些頻道使用 Nostr 通訊協定中繼，允許跨城市或地區溝通，同時保持基於位置的相關性。您的訊息會即時顯示給同一頻道中的其他人，新的參與者加入時會自動看到最近的訊息記錄。


![image](assets/en/06.webp)


### 私人對話：安全加密


若要開始私人對話，請直接點選任何顯示在「對手總覽」中的「使用者名稱」。您也可以點選「星星圖示」將該使用者標記為我的最愛，如此一來，即使該使用者離線，您的連絡人清單中仍會顯示該使用者。


![image](assets/en/07.webp)


當您開始私人聊天時，Bitchat 會自動啟動「安全握手」。裝置會交換短暫金鑰，以建立專為您的對話而設的加密隧道。透過持續的端對端加密，這個過程可確保您所有的訊息和共用檔案都能保持機密。私人訊息支援文字和檔案共用。


![image](assets/en/08.webp)


## 4️⃣附加功能


您可以在 Bitchat 的任何地方輸入 `/`，立即存取動作面板。這會顯示快速動作的指令選單。



- 管理連線**：封鎖使用者」或「解除封鎖對等方
- 頻道控制**：顯示頻道」或「加入/建立頻道
- 社會互動**：送上熱情擁抱」或「用鱒魚拍打」 🎣
- 聊天維護**：清除聊天訊息
- 隱私權工具**：查看誰在線上」或「傳送私人訊息


指令會立即執行 - 例如 `/block Satoshi` 讓批評者噤聲，或 `/hug Hal` 散播正面訊息🫂。


![image](assets/en/09.webp)


## 5️⃣建立頻道


Bitchat 中的頻道可讓您圍繞主題、位置或社群進行有組織的溝通。要建立您自己的頻道，請遵循以下工作流程：


### 步驟 1：建立頻道


要建立頻道，請在任何聊天中輸入 `/j` 或 `/join`，然後輸入頻道名稱（例如 `/j <channelname>`）。建立後會出現一個新的 `icon ⧉`，表示新的頻道。其他使用者可以輸入相同的指令加入 (例如 `/j bitchat_tutorial`)。


![image](assets/en/10.webp)


### 步驟 2：組態設定


除了預設命令外，下列設定在頻道內也是可用的：



- `/save` 將訊息儲存到本機
- `/transfer` 來轉移通道所有權和
- `/pass`變更頻道密碼。


對於私人社群，此指令會啟用密碼保護，要求核准的成員在加入前輸入自訂密碼。


## 6️⃣緊急模式


現在，讓我們來談談「憂鬱模式」：點按三下「Bitchat 標誌」，應用程式內的所有本機訊息和資料就會被完全清除。這是您的終極隱私保障，最適合需要立即謹慎處理的情況。


**重要提醒：** _恐慌模式是永久性的。一旦啟動，資料將無法復原。請謹慎使用。


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash 頻道可根據「地理位置」而非傳統的網路連線，進行有針對性的對話。此功能可將 bitchat 轉變為位置感知的溝通工具，非常適合當地協調、社群建構和特定位置的討論。


### #geohashes` 如何運作


該系統使用 [Geohash system](https://en.wikipedia.org/wiki/Geohash) 將世界分割成一個個方格，哈希值中的每個字元都代表更高的精確度：



- 4** 級 (例如：`u33d`)：覆蓋範圍約 25km × 25km - 適合全城討論
- 等級 6** (例如 `u33d8z`)：覆蓋約 1.2 km × 1.2 km - 鄰近精確度
- 8** 級 (例如：`u33d8z1k`)：涵蓋約 150 公尺 × 150 公尺 - 街道區段精確度


精確選擇可在隱私與實用性之間取得平衡：更高的層級可創建更多專屬區域，但也能更精確地顯示您的位置。


### 加入 `#geohash` 頻道


1.存取 `#location channels` 功能表。

2.選擇您所需的精確度等級，並輸入 `#geohash` (例如：#u33d)

3.點選 `Teleport` 按鈕加入 `#location channel`。


![image](assets/en/12.webp)


或者，您也可以點選 `地圖圖示`，使用地圖檢視來決定精確度等級，然後點選 `選擇`加入 `#定位頻道`。


![image](assets/en/13.webp)


**重要提醒**：_#geohash 功能需要使用中的網際網路連線 - 不像 BLE mesh 可透過藍牙離線操作。


## 8️⃣熱圖


熱圖是發現全球 Bitchat 活動和頻道的酷炫方式。[Bitmap](https://bitmap.lat/)可視化並追蹤 Nostr 網路上匿名、基於地點的訊息，顯示短暫的 Nostr 事件。看看並加入特定位置的頻道和聊天。


![image](assets/en/15.webp)


## 🎯 結論


Bitchat 可在傳統訊息傳輸失敗的情況下，進行安全的分散式通訊。它能夠使用 BLE 網狀網路，在沒有網際網路基礎建設的情況下運作，因此適用於抗議活動、災害地區，以及連線能力有限或受到審查的偏遠地區。此應用程式可透過短暫金鑰加密、基於 geohash 的位置頻道，以及恐慌模式資料刪除功能來確保隱私。


該應用程式仍處於早期開發階段，但已展現出良好的前景。使用者應預期偶爾會出現 bug，並透過 [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) 回報問題。改進計劃包括使用 Cashu 通訊協定進行應用程式內私人交易的「ecash」整合。


![image](assets/en/14.webp)


## 📚 Bitchat 資源


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)