---
name: Session
description: 傳送加密訊息，而非元資料
---
![cover](assets/cover.webp)



Session 是 2020 年創建的加密訊息應用程式，旨在提供比傳統訊息更高的保密性。它最早是由 *Oxen Privacy Tech Foundation* 所開發，後來由 *Session Technology Foundation* 所開發。



Session 擁有一些有趣的技術特性：訊息的端對端加密、分散式網路組織以保證可用性和備援，以及 Tor 啟發的洋蔥路由。此外，與需要電話號碼註冊的 WathsApp 或 Signal 不同，Session 不需要任何個人資訊 (沒有電話號碼、沒有電子郵件，只有一對密碼鑰匙)。



Session 可讓您傳送訊息、檔案、語音訊息、音訊通話，以及最多 100 名成員的群組 (以及超過 100 名成員的社群)，同時減少元資料洩漏。



![Image](assets/fr/01.webp)



Session 首先是針對將保密性放在首位的使用者。這項訊息服務是 WhatsApp 的重要替代方案，其架構設計可抵擋現代監控模式。



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = 端對端加密 *



## 安裝會話應用程式



Session 適用於所有平台。您可以直接從手機的應用程式商店下載應用程式：




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger)；
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868)；
- [F-Droid](https://fdroid.getsession.org/).



在 Android 上，也可以 [透過 APK 安裝](https://github.com/session-foundation/session-android/releases)。



在本教程中，我們將專注於行動版本，但請注意 [電腦版本也可用](https://getsession.org/download) (MacOS、Linux 和 Windows)。稍後，我們將探討如何在多部裝置上同步處理一個帳戶。



## 在 Session 上建立帳戶



首次啟動時，請按一下「*建立帳戶*」。



![Image](assets/fr/02.webp)



為您的個人資料選擇一個顯示名稱。可以是假名或真名。



![Image](assets/fr/03.webp)



接下來，您必須在兩種通知管理模式中做出選擇：





- 快速模式（"**Firebase Cloud Messaging/Apple Push Notification Service**"）：借助 Google 或 Apple（取決於您的系統）提供的通知服務，您可以近乎實時地接收訊息通知。為了讓此模式運作，您的 IP Address 和獨特的通知 ID 會傳送給 Google 或 Apple，而會話帳號 ID 也會在 STF 伺服器上註冊 (透過 Tor)。此模式會暴露元資料（誠然是最低限度的），但不會損害訊息內容或聯絡人，也不會讓您的實際活動被追蹤。因此，此模式的回應效率較高，但依賴於集中式的基礎架構，保密性稍差。





- 慢速模式 (**背景輪詢**)：會話應用程式在背景保持活動，定期輪詢網路是否有新訊息。與第一種方式相比，這種方式保證了更高的保密性，因為資料不會傳送到第三方伺服器；Google、Apple 或 STF 伺服器都不會收到任何資訊。另一方面，這種模式有兩個缺點：通知可能會延遲 (長達幾分鐘)，而且由於應用程式在背景活動，能源消耗通常較高。



![Image](assets/fr/04.webp)



現在您已連接到會話應用程式，可以開始交換訊息。



![Image](assets/fr/05.webp)



## 儲存您的會話帳號



在開始使用會話之前，首先要做的是儲存您的帳戶，以便在遺失裝置時可以還原。若要執行此操作，請按一下「*儲存您的復原密碼*」旁邊的「*繼續*」按鈕。



![Image](assets/fr/06.webp)



接下來會顯示 Mnemonic 詞組。請仔細複製並妥善保管。此短語可讓您完全存取您的 Session 帳戶，因此切勿洩漏。您需要它才能在其他裝置上存取您的帳戶，尤其是當您目前的手機遺失或更換時。



![Image](assets/fr/07.webp)



這個詞組的運作方式與 Bitcoin 組合中使用的 Mnemonic 詞組類似。因此，我建議您參考這份教學，我在其中說明了儲存 Mnemonic 詞組的最佳做法：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**請注意**：與 Bitcoin 作品集上使用的 Mnemonic 短語不同，在 Session 上，**您絕對必須完整保存每個單詞**。前 4 個字母是不夠的！



## 設定會話應用程式



若要存取應用程式設定，請按一下 Interface 左上方的個人檔案照片。在這裡您可以新增個人照片。



![Image](assets/fr/08.webp)



在「*隱私權*」功能表中，您可以啟用或停用各種功能（請注意，有些功能可能會暴露您的 IP Address）。我也建議您啟動「*鎖定應用程式*」選項，它需要驗證才能存取應用程式。



![Image](assets/fr/09.webp)



在 「*通知*」功能表中，您可以選擇 「*快速模式*」和 「*慢速模式*」（請參閱本教程的前幾部分）。您也可以依自己的喜好自訂通知。



![Image](assets/fr/10.webp)



最後，進入「*外觀*」功能表，讓 Interface 適應您的口味。如果您想要重新備份，「*恢復密碼*」功能表可讓您擷取 Mnemonic 的短語。



![Image](assets/fr/11.webp)



## 使用會話傳送訊息



若要聯絡其他人，請按一下首頁上的「*+*」按鈕。



![Image](assets/fr/12.webp)



有多個選項可供選擇。如果您想要建立或加入群組，請選擇「*建立群組*」或「*加入社群*」。



![Image](assets/fr/13.webp)



如果您希望他人將您加為連絡人，您可以讓他們掃描您的會話 ID 作為 QR 代碼。



![Image](assets/fr/14.webp)



若要遠端傳送您的登入資訊，請點選「*邀請朋友*」。然後您可以複製您的會話 ID，並透過其他通訊管道傳送。您也可以從首頁點選您的個人檔案照片來擷取此資訊。



![Image](assets/fr/15.webp)



如果您有其他人的會話 ID 並希望將其加入，請點選「*新訊息*」。



![Image](assets/fr/16.webp)



然後，您可以在文字中貼上它的識別碼，或直接掃描它 (如果您有 QR 代碼)。



![Image](assets/fr/17.webp)



然後向此人傳送初始訊息。



![Image](assets/fr/18.webp)



只要對方接受您的請求，您就會看到他們的使用者名稱出現，您就可以與他們自由聊天。



![Image](assets/fr/19.webp)



## 同步桌面軟體



要在電腦上同步帳戶，您需要安裝軟體。[從官方網站下載](https://getsession.org/download)。我建議您在安裝之前檢查其真實性和完整性。



![Image](assets/fr/20.webp)



首次啟動時，請按一下「*我有帳號*」。



![Image](assets/fr/21.webp)



輸入您的 Mnemonic 詞組，確保每個字之間留有空格。



![Image](assets/fr/22.webp)



現在您可以從電腦存取您的對話。



![Image](assets/fr/23.webp)



恭喜您，現在您已經掌握了使用會話訊息的技巧，這是 WathsApp 的絕佳替代方案！



我也推薦這篇教學，其中我介紹了 Threema，另一個有趣的訊息應用程式替代方案：



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74