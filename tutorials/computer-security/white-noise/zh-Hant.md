---
name: White Noise
description: 基於 Nostr 和 MLS 協定的私有、分散式訊息傳輸應用程式
---

![cover](assets/cover.webp)




## 簡介



「難中有機」。這句來自愛因斯坦的名言提醒我們，問題並非一成不變，而是在問題中蘊藏著新穎、創新解決方案的種子。



我們在本教程中介紹的解決方案的推出動機完美地說明了這一點。它是 **White Noise**，因需要而生。



用其創辦人 Max Hillebrand 的話來說，*Bitcoin Magazine* 報導：「我們推出這個專案是因為缺乏替代方案」。他解釋說：「現有的加密應用程式在大規模使用時效率很低：在一個群組對話中加入 100 個人會大大減慢加密速度。同時，分散式平台不提供私人訊息。最後，Nostr 的開放中繼網路允許每個人傳播想法，但對直接訊息的保護仍然嚴重不足。我們意識到：為了保護自由，我們必須合併這些系統」。



## 什麼是 White Noise？



White Noise 是一個由非營利團隊開發的開放原始碼訊息應用程式。該應用程式提倡安全性、隱私性和分散性。與傳統的應用程式不同，它既不需要電話號碼，也不需要電子郵件地址。


White Noise 的特點在於整合了兩個基本通訊協定 - Nostr 和 MLS - 這兩個協定構成了其技術基礎。



Nostr (Notes and Other Stuff Transmitted by Relays) 是一個分散式、開放源碼的協定，旨在抵抗審查。  此協定使用中繼器、金鑰對和用戶端。



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

使用 white Noise，您甚至可以選擇自己的中繼設定，將隱私最大化。



另一方面，MLS（Messaging Layer Security）是一種可對訊息進行端對端加密的安全通訊協定。換句話說，訊息只能在端點（即訊息的發送者和接收者）存取。這表示參與訊息路由的中繼站無法存取訊息內容。



以下是 White Noise 與多個知名訊息應用程式的快速比較。



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## 開始使用 White Noise



### White Noise 安裝



前往 [White Noise 網站](https://www.whitenoise.chat/)，然後點選 **下載**。



![screen](assets/fr/03.webp)



White Noise 目前僅適用於行動裝置。


在出現的新介面上，按下 ：





- 如果您想在 Android 上下載，請按 **Zapstore** 或 **Android APK** 按鈕；
- 如果您使用 iPhone，請按下 **iOS TestFlight** 按鈕。



![screen](assets/fr/04.webp)



在本教程中，我們將進行 Android 下載。


如果您選擇透過**Zapstore**下載，您將會被重新導向至 Zapstore。進入 Zapstore 後，在搜尋列中輸入 **White Noise**。然後按一下 ** 安裝** 進行下載。



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



如果您選擇下載 APK 檔案，您會被重定向至 White Noise GitHub 套件庫，以選擇適合您智慧型手機的版本。



可用的 APK 檔案有 ：





- whitenoise-0.2.1-arm64-v8a.apk** (57.7 MB)，適合使用 64 位元處理器的最新手機；
- whitenoise-0.2.1-armeabi-v7a.apk** (47.5 MB) 適合使用 32 位元處理器的舊款手機。



您也有**.sha256**檔案，它們只是驗證下載完整性的校驗和。



![screen](assets/fr/07.webp)



下載完成後，安裝並開啟應用程式。



![screen](assets/fr/08.webp)



### 初始使用者帳戶設定



第一次連線到 White Noise，請按「**註冊**」按鈕。



![screen](assets/fr/09.webp)



接下來，請設定您的個人資料，選擇個人照片、姓名並加入簡短的自我描述。您不必填寫您的真實身份（姓名和照片）。


請注意，White Noise 會自動為您選擇一個名字（假名），您可以保留或變更該名字。最後，按下 **End** 按鈕。



![screen](assets/fr/10.webp)



您將被重定向至 White Noise 的 ** 首頁畫面**，您的對話內容將在此列出。您的帳戶現在已設定完成，可以開始使用。您可以分享您的個人資料或搜尋好友開始聊天。



![screen](assets/fr/11.webp)




### 發現 White Noise 介面



在主介面的螢幕頂端，您會看到 ：



在左上角，個人資料圖示是您個人資料照片的縮圖，或是您個人資料名稱的首字母。按一下即可存取您的帳戶設定。



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



在右上角，您可以找到開始新對話的圖示。



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## 使用者帳號設定



按左上角的設定檔圖示存取設定。



![screen](assets/fr/16.webp)



在 ** 設定** 介面的頂端，您會看到您的照片和個人資料名稱，接著是您的公開金鑰，您可以使用旁邊的 QR 代碼分享您的公開金鑰。



![screen](assets/fr/17.webp)



在下方，您會看到 ** 變更帳戶** 按鈕，可讓您連線到應用程式內的另一個設定檔。



![screen](assets/fr/18.webp)



然後，您會看到第一部分有四（4）個子功能表，例如 ：





- 修改檔案**



在此子功能表中，您可以修改設定檔名稱、Nostr 位址 (NIP-05)...別忘了按一下 **Save** 以儲存您的變更。



![screen](assets/fr/19.webp)





- 設定檔按鍵**



在這裡您可以存取您的公開和私人（秘密）金鑰。正如 White Noise 提醒您的，您的私人金鑰在任何情況下都不能外洩。



![screen](assets/fr/20.webp)





- 主電源繼電器



在此子功能表中，您可以新增或移除**一般繼電器**（定義用於所有 Nostr 應用程式的繼電器）、**盒內繼電器**和**鍵組繼電器**。



若要這樣做，請點選中繼前面的 ** 垃圾** 圖示來刪除中繼，或點選 **+** (plus) 圖示來新增中繼。



![screen](assets/fr/21.webp)





- 斷開**



按一下此子功能表可將您的帳戶從應用程式中斷開。但請確定您已離線儲存私人密碼匙，否則稍後您將無法再次登入。



![screen](assets/fr/22.webp)




第二部分提供子功能表：





- 應用程式設定



您可以在此定義應用程式的外觀（主題和顯示語言），甚至可以在您覺得資料已被洩露或您自己覺得有風險時刪除資料。



![screen](assets/fr/23.webp)





- 捐款給 White Noise



您可以透過 White Noise (非營利組織) 背後的團隊，透過他們的 Lightning 位址或 Bitcoin 無聲付款位址捐款支持。



![screen](assets/fr/24.webp)



最後，最下方是 ** 開發者設定**。



![screen](assets/fr/25.webp)




## 開始對話



現在讓我們來看看如何開始對話。在撰寫本文時，White Noise 提供三種通訊選項。我們會依次探討**私人對話** (** 聊天 1:1**)，也就是只有您和另一個人之間的對話、**群組對話**和**傳送多媒體檔案**。




### 貓 1:1



在主介面中，若要新增通訊員，請按一下開始新對話的圖示。


然後，掃描公開金鑰的 QR 碼 (1) 或將新通訊人的公開金鑰 (2) 貼到搜尋列中，即可找到他或她。



![screen](assets/fr/26.webp)



然後點選 ** 開始對話** 按鈕，與您的通訊對象開始對話。您也可以按下 ** 加入群組** 按鈕，**跟蹤**您的通訊人或邀請他/她加入群組對話。



![screen](assets/fr/27.webp)



您發給新通訊對象的第一封訊息就像是邀請請求。在您與他/她溝通之前，您的通訊對象必須接受這個請求。如果他們拒絕，那麼就無法進行對話。



![screen](assets/fr/28.webp)



更重要的是，只要他們不接受您的邀請，他們就無法閱讀您最初的訊息內容。



一旦他接受您的邀請，他現在就可以回覆您，而您們兩人就可以無縫且安全地溝通。



![screen](assets/fr/29.webp)



更重要的是，在討論中，您還可以使用額外的功能。



您可以長按特定訊息以顯示選項，例如 ：




- 以表情符號回應訊息 (1) ；
- 按 **Reply** (2) 進行 ** 直接引用** 來回覆訊息；
- 按 **Copy** (3) 複製訊息。



![screen](assets/fr/30.webp)





- 只有在訊息是來自您的情況下，才能使用 ** 刪除** 按鈕刪除訊息。



![screen](assets/fr/31.webp)



您可以在對話中搜尋。



按一下螢幕上方的通信者頭像以存取「會談資訊」，然後按一下 ** 在會談中搜尋** 按鈕。



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



在出現的搜尋列中，輸入您要搜尋的字詞，然後啟動搜尋。然後您會看到搜尋的字詞以**粗體**突出顯示。



![screen](assets/fr/34.webp)




### 團體對話



可在 White Noise 上建立對話群組。



若要執行此動作，請輕觸新會話啟動介面中的圖示，然後點選 ** 新增群組會話**。然後，在搜尋列中輸入您想要加入群組的第一位成員的公開金鑰。



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



最後，如果此選項不起作用，請從 ** 開始新對話** 介面，在搜尋列中輸入您想要加入群組的第一位成員的公開金鑰。您也可以掃描與其公開金鑰相關的 QR 碼。



這次不要點選 ** 開始對話** 按鈕，而是點選 ** 加入群組** 按鈕。



![screen](assets/fr/37.webp)



在出現的彈出式功能表中，點選 ** 新增群組對話**。



![screen](assets/fr/38.webp)



然後按下 **繼續** (您不需要再次輸入其公開金鑰)。



![screen](assets/fr/39.webp)



身為群組的建立者，您自動成為其管理員。填入群組詳細資料，例如 ** 群組名稱和說明**，然後按一下 ** 建立群組** 按鈕。



![screen](assets/fr/40.webp)



您新增為第一位成員的使用者，以及您之後新增的其他使用者，都會收到邀請他們加入群組的通知。他們必須按一下 ** 接受** 以加入群組。



![screen](assets/fr/41.webp)



您也可以將與您聊天的新成員加入現有的群組。若要這樣做，請點選畫面上方對話者的頭像，以存取「對話資訊」，然後點選 ** 加入群組** 按鈕。



![screen](assets/fr/42.webp)



在出現的新介面上，**勾選**您要將它加入的群組，然後點選**加入群組**。剩下要做的就是等待它同意加入群組。



![screen](assets/fr/43.webp)



請注意，只有群組管理員才能修改群組資訊、新增或驅逐成員。此外，金鑰輪換可防止被禁止的成員解密未來的訊息。



若要移除成員，請從群組主介面，點選上方的群組圖示，進入群組資訊介面。



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



然後按一下該成員的名字，**從群組移除**。從這個介面，您也可以傳送訊息給他，跟蹤他或將他加入其他群組。



![screen](assets/fr/46.webp)



### 傳送多媒體檔案



目前，White Noise 上的使用者之間只能分享相片。無論您是在私人對話或群組聊天中，要這樣做，您需要：





- 按下文字訊息輸入欄位左側的 ** 加 (+)** 符號。



![screen](assets/fr/47.webp)





- 然後按一下底部標示 **Photos** 的方塊，以存取您的圖庫。



![screen](assets/fr/48.webp)





- 選擇要傳送的照片。



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## 需要記住的重點



White Noise 提供良好的保密性和卓越的安全性。另一方面，它是最近才出現的應用程式，並非非常廣泛，而且仍在起步階段。因此，現在下任何積極的結論還太早。在使用過程中有可能會遇到一些故障。



目前，與流行的訊息應用程式相比，它缺乏某些功能 (無法進行音訊或視訊通話、無法傳送音訊或視訊多媒體檔案)。



儘管如此，White Noise 對於保密性要求極高的對話（例如與家人、好友或共同事業的積極份子）來說仍是一個有趣的選擇，儘管它需要花點心思來安裝（透過其他應用程式商店或 APK 檔案）和學習（利用 Nostr 通訊協定掌握一點關於金鑰對、用戶端和中繼的概念）。



現在您知道如何使用 White Noise 與您的朋友和家人安全溝通了。如果您覺得本教學有用，請對我們豎起大拇指。



我們推薦您參考我們的 Tox Chat 教學，這個應用程式可以讓您透過分散式的 Tox 通訊協定，在沒有中介的情況下聊天。



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3