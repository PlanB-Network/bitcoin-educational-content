---
name: Threema
description: 安全、匿名的即時通訊
---
![cover](assets/cover.webp)



Threema 於 2012 年在瑞士成立，是一款即時通訊應用程式，旨在保證隱私與安全。與 WhatsApp、Telegram 或 Signal 不同，Threema 不需要電話號碼或電子郵件 Address 來建立帳號。每位使用者都有獨一無二的識別碼，可以完全匿名註冊。



在技術方面，透過 Threema 進行的通訊是端對端加密的。行動應用程式程式碼自 2020 年起即為開放原始碼，但伺服器基礎架構仍為專屬與集中式。伺服器完全託管在瑞士（瑞士以其資料保護的法律架構而聞名）。



![Image](assets/fr/01.webp)



Threema 有 Android 和 iOS 的基本用戶端。此外，還有網頁應用程式，以及適用於 Windows、Linux 和 macOS 的軟體。不過，要使用這些軟體，您必須先在行動裝置上註冊。



Threema 應用程式並非免費。它採用一次性購買模式：5.99 歐元可終生使用該應用程式（若直接購買，則為 4.99 歐元）。要真正匿名使用 Threema，付款也需要匿名。這就是為什麼您可以在「*Threema 商店*」以比特幣或現金購買啟用金鑰來啟用 Android 版本。另一方面，在 iOS 上，由於 Apple 對應用程式盈利的限制，因此必須透過 App Store 購買。



還有一個專用的商業版本，叫做「*Threema Work*」。在本教程中，我們將專注於家庭版。



| 應用程式             | E2EE 1:1       | E2EE 群組      | 匿名註冊            | 開源客戶端許可證             | 開源伺服器許可證             | 去中心化伺服器       | 創建年份          |
| -------------------- | -------------- | -------------- | ------------------- | ---------------------------- | ---------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (可選)      | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Telegram             | 🟡 (可選)      | ❌              | 🟡                  | ✅                            | ❌                            | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                            | ❌                            | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                            | ✅                            | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                            | ❌                            | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (聯邦式)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                            | N/A                          | 🟡 (透過電郵)        | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                            | ✅                            | 🟡 (聯邦式)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                            | ✅                            | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                            | ❌                            | 🟡(無目錄)          | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                            | N/A                          | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                            | N/A                          | ✅                    | 2013              |

*E2EE = 端對端加密 *



## 安裝 Threema 應用程式



Threema 適用於所有平台。您可以直接從手機的應用程式商店下載應用程式：




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app)；
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/)；
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829)；
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



在 Android 上，也可以 [透過 APK 安裝](https://shop.threema.ch/en/download)。



此外，還有 [電腦版本](https://threema.ch/download) (MacOS、Linux 和 Windows)。本教學將教您如何同步它們。



## 購買 Threema 授權



安裝應用程式後，如果您是直接透過應用程式商店安裝，您已經支付了授權費用，應該可以立即使用。如果您是透過 F-Droid 或 APK 安裝，現在則需要在官方網站購買授權。



[前往「*Threema 商店*」(https://shop.threema.ch/)，點選「*購買 Threema Android 版*」按鈕。



![Image](assets/fr/02.webp)



選擇您要購買的授權數量 (如果只是為了您自己，則只需一個)、選擇貨幣，並選擇授權交付方式。您可以選擇透過電子郵件接收授權，如果您希望保持匿名，也可以直接在網站上接收授權。然後按一下「*進行付款*」。



![Image](assets/fr/03.webp)



選擇您的付款方式。在我的情況下，我打算用比特幣支付，我也建議您這樣做，因為它可以讓您保持匿名（前提是您適當地使用 Bitcoin），而且比遠程現金支付方便得多。然後點擊 「*下一步*」。



![Image](assets/fr/04.webp)



如果您不需要 Invoice，請再次按一下「*下一步*」，無需輸入任何個人資訊。



然後點擊「*確認付款*」確認購買。



![Image](assets/fr/05.webp)



然後，您需要將指定的金額傳送到所提供的 Bitcoin Address（不幸的是，目前還不支援 Lightning）。在 Blockchain 上確認交易後，點擊 Invoice 旁邊的 "*Close*"。



然後您就可以取得您的授權金鑰。請注意：如果您沒有輸入電子郵件 Address，這個金鑰只會顯示在這裡。請記住儲存該頁面的 URL，以便日後有需要時可以存取。



![Image](assets/fr/06.webp)



## 在 Threema 上建立帳號



現在您有了授權金鑰，就可以啟動應用程式了。第一次啟動時，如果您尚未透過應用程式商店購買 Threema，系統會要求您輸入在網站上購買的授權金鑰。



![Image](assets/fr/07.webp)



然後按一下「*立即設定*」按鈕。



![Image](assets/fr/08.webp)



將您的手指移動到螢幕上的 generate 熵源，以建立您的「*Threema ID*」。



![Image](assets/fr/09.webp)



您的 "*Threema ID*"將會顯示。這將使您能夠聯絡其他使用者。按一下「*下一步*」。



![Image](assets/fr/10.webp)



選擇一個密碼。如果有需要，它可以讓您恢復帳戶的存取權限。密碼要盡可能長且隨機，並保存一份安全的副本，例如在密碼管理器中。



![Image](assets/fr/11.webp)



然後選擇一個使用者名稱，可以是您的真名或假名。



![Image](assets/fr/12.webp)



這樣您就可以將 Threema ID 和您的電話號碼連結起來。這樣可以讓您更容易搜尋聯絡人，但如果您使用 Threema，也是為了保持您的匿名性：所以最好不要連結。點選「*下一步*」。



![Image](assets/fr/13.webp)



完成此步驟後，請按一下「*完成*」。



![Image](assets/fr/14.webp)



您現在已經與 Threema 連線，可以開始通訊。



![Image](assets/fr/15.webp)



## 設定 Threema



首先，按一下右上角的三個小圓點進入設定，然後選擇「*設定*」。



![Image](assets/fr/16.webp)



在「*隱私權*」標籤中，您會發現多個選項，可依您的需求調整：




- 同步處理手機上的聯絡人 ；
- 接受來自不明人士的訊息；
- 在資料輸入時寫入指標 ；
- 收到訊息的通知...



![Image](assets/fr/17.webp)



在「*安全性*」標籤中，我建議啟動「*鎖定機制*」選項，以保護對應用程式的存取。此外，建議您也啟動 passphrase，以保障本機備份的安全。



![Image](assets/fr/18.webp)



請隨意探索設定的其他部分，依您的喜好自訂應用程式。



![Image](assets/fr/19.webp)



## 備份您的 Threema 帳戶



在您開始交換訊息之前，請務必先計劃好恢復帳號的方法，尤其是在手機變更或遺失的情況下。為此，請按一下 Interface 右上方的三個點，然後進入「*備份*」功能表。



![Image](assets/fr/20.webp)



您可以在此找到備份資料的兩個選項：




- 「*Threema安全*」；
- 「*資料備份*」。



"Threema Safe* 將您所有的帳號資料，除了您的對話之外，都儲存在 Threema 的伺服器上。這些資料會以您建立帳號時所選擇的密碼進行加密，確保 Threema 無法存取這些資料。我們會定期自動備份。



使用 "*Threema Safe*「，要在新的設備上恢復您的帳戶，您只需要輸入您的 」*Threema ID*"和您的密碼。如果缺少這兩項資訊中的任何一項，將無法恢復您的帳戶。



此選項只允許您擷取您的 ID、個人資料、連絡人、群組和特定設定，但 ** 不允許您擷取對話記錄**。



若要啟動「*Threema Safe*」，只要勾選「*備份*」功能表中的選項即可。



![Image](assets/fr/21.webp)



如果您還要備份和還原您的對話記錄，您需要使用「*資料備份*」選項。這會產生一個完整的帳戶備份，儲存在您的手機上。您需要將此備份傳輸到您的新裝置，並使用您的密碼 (可能還有您的 passphrase) 來還原整個帳號。



由於此備份只是本機的，因此需要定期複製到外部媒體。否則，如果您的裝置遺失，將無法復原。因此，此方法最適合有計劃地從一台裝置傳輸至另一台裝置，而非緊急情況。



請注意：「*資料備份*」僅在您使用相同作業系統時有效。例如，您無法使用它從 Samsung 遷移到 iPhone。



## 自訂您的 Threema 個人資料



在 Interface 的左上角，按一下您的個人檔案圖片，然後選擇「*我的個人檔案*」。



![Image](assets/fr/22.webp)



在這裡您可以自訂您的個人資料：新增照片、選擇誰可以看到、或檢視您的 Threema 登入。



![Image](assets/fr/23.webp)



## 同步 PC 軟體



如果您想在個人電腦上存取您的對話，您可以使用專用軟體同步您的 Threema 帳號。請 [從官方網站](https://threema.ch/en/download) 下載適用於您作業系統的軟體。



![Image](assets/fr/24.webp)



在手機上，按一下右上方的三個點，然後開啟「*Threema 2.0 for Desktop*」功能表。



![Image](assets/fr/25.webp)



按一下「*新增裝置*」，然後用手機掃瞄電腦上軟體顯示的 QR 代碼。



![Image](assets/fr/26.webp)



若要確認同步化，請按一下軟體中顯示的表情符號群組。



![Image](assets/fr/27.webp)



在電腦上，使用您的密碼登入。



![Image](assets/fr/28.webp)



除了手機應用程式外，您現在還可以直接從電腦存取 Threema 帳戶。



![Image](assets/fr/29.webp)



## 使用 Threema 傳送訊息



現在一切都已設定妥當，您可以開始溝通了。按一下「*開始聊天*」按鈕。



![Image](assets/fr/30.webp)



選擇「*新增連絡人」。



![Image](assets/fr/31.webp)



輸入或掃描您的通信員的「*Threema ID*」。



![Image](assets/fr/32.webp)



按一下訊息圖示。



![Image](assets/fr/33.webp)



傳送第一封訊息給您的通訊員。



![Image](assets/fr/34.webp)



當您的對方接聽時，連線就會建立，您就可以看到他或她的姓名和個人檔案照片。接著您就可以傳送 Exchange 訊息、多媒體檔案，甚至撥打電話。



![Image](assets/fr/35.webp)



恭喜您，現在您已經可以快速使用 Threema 訊息，這是 WathsApp 的絕佳替代方案！如果您覺得本教程有用，請在下方留下 Green 拇指，我將不勝感激。歡迎在您的社交網路分享本教學。非常感謝



我也推薦這篇教學，其中我介紹了 Proton Mail，一個比 Gmail 更能保護隱私的替代品：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2