---
name: 訊號
description: 自由表達
---
![cover](assets/cover.webp)



Signal 是端對端的加密訊息應用程式，預設提供良好的保密性。每個訊息、通話和檔案都受到 Signal 通訊協定的保護，該通訊協定被公認為最強大的通訊協定之一。它被許多其他應用程式重複使用，包括用於 RCS 通訊的 WathsApp、Facebook Messenger、Skype 和 Google Messages。



Signal 由 Moxie Marlinspike（化名）於 2014 年推出，並自 2018 年起由 Brian Acton（WhatsApp 的共同創辦人）支持下成立的非營利組織 Signal Foundation 開發。



![Image](assets/fr/01.webp)



與 WhatsApp 相比，Signal 以其透明度脫穎而出：應用程式的程式碼 (包括用戶端與伺服器端) 完全開放原始碼。這允許任何人對其進行審核，特別是檢查加密是否如所宣傳的那樣應用。



然而，Signal 依賴於電話號碼的使用，與其他解決方案相比，這是其在匿名性方面的主要弱點。儘管如此，在我看來，該應用程式在安全性和機密性方面是最可靠的，這要歸功於其完全開放的架構和廣泛採用的加密協定，因此經過測試和審核，不像其他較為邊緣化的應用程式。



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




## 安裝 Signal 應用程式



Signal 適用於所有平台。您可以直接從手機的應用程式商店下載應用程式：




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)；
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669)；



在 Android 上，也可以 [透過 APK 安裝](https://github.com/signalapp/Signal-Android/releases)。



在本教程中，我們將專注於手機版本，但請注意 [也提供桌面版本](https://signal.org/fr/download/) (MacOS, Linux and Windows)。不過，您需要先設定行動應用程式，才能將帳戶與桌上型電腦版本同步。



## 在 Signal 上建立帳號



第一次啟動應用程式時，請按一下「*繼續*」按鈕。



![Image](assets/fr/02.webp)



輸入您的電話號碼，然後按一下「*下一步*」。



![Image](assets/fr/03.webp)



驗證碼將會透過 SMS 傳送給您。在 Signal 應用程式中輸入此驗證碼。



![Image](assets/fr/04.webp)



選擇 PIN 碼來保護您的 Signal 帳戶。此密碼可加密您的資料，並可在您的裝置遺失時用來恢復存取您的帳戶。因此，選擇一個穩健的 PIN 碼是很重要的，盡可能長且隨機，並保留可靠的記錄。



![Image](assets/fr/05.webp)



再次確認此 PIN 碼。



![Image](assets/fr/06.webp)



現在您可以個人化您的使用者個人資料。選擇一張照片、輸入您的姓名或暱稱。在此階段，您也可以定義哪些人可以透過您的號碼在 Signal 上找到您。如果您想讓別人看到您，請選擇「*Everyone*」；如果您想讓別人無法透過電話號碼找到您，請選擇「*Nobody*」（這時您只能以「*使用者名稱*」加入）。完成選擇後，按一下「*下一步*」。



![Image](assets/fr/07.webp)



現在您已連線至 Signal，並準備好 Exchange 訊息。



![Image](assets/fr/08.webp)



## 設定您的 Signal 帳戶



按一下左上角的個人檔案照片，即可存取應用程式設定。



![Image](assets/fr/09.webp)



透過「*帳戶*」功能表，您可以管理您的個人資料設定。我建議您保留預設設定。您也可以啟動「*註冊鎖定*」選項，以保護您的帳戶免受某些類型的攻擊。此功能表也包含將帳號轉移至新裝置所需的選項。



![Image](assets/fr/10.webp)



在設定中再次按一下您的個人資料圖片，就會進入個人化個人資料的選項。我建議您設定一個 「*使用者名稱*」：這將使您在不暴露電話號碼的情況下與其他人取得聯繫。



![Image](assets/fr/11.webp)



只要選擇「*QR 代碼或連結*」，您就可以獲得想要將您加到 Signal 的人所需要分享的資訊。



![Image](assets/fr/12.webp)



*Privacy*" 功能表尤其重要。在這裡您可以找到控制您的號碼可見度、與聯絡人的訊息管理，以及在應用程式上賦予的各種授權的選項。



![Image](assets/fr/13.webp)



您也可以自由探索「*外觀*」、「*聊天*」和「*通知*」功能表，依照個人需求調整 Interface 和應用程式的操作。



## 連接桌面應用程式



若要連接桌面應用程式，請先在電腦上安裝軟體 (請參閱本教學的第一部分)。然後在您的手機上，前往「設定」並開啟「*連結的裝置*」部分。



![Image](assets/fr/14.webp)



按一下「*連結新裝置*」按鈕。



![Image](assets/fr/15.webp)



在電腦上啟動軟體，然後用手機掃描螢幕上顯示的 QR 代碼。如果您想要匯入您的對話內容，請選擇「*傳輸訊息記錄*」選項。



![Image](assets/fr/16.webp)



您的裝置現在已完全同步。



![Image](assets/fr/17.webp)



## 使用 Signal 傳送訊息



要在 Signal 上與某人溝通，您首先需要將他們加入為連絡人。有幾種方式可以選擇：您可以透過電話號碼加入（如果對方已啟動透過此方式尋找的選項），或使用其 Signal ID。



按一下 Interface 右下角的鉛筆圖示。



![Image](assets/fr/18.webp)



在我的情況下，我想要依使用者名稱新增該人。因此我按一下「*依使用者名稱*尋找」。



![Image](assets/fr/19.webp)



然後，您可以貼入其登入資訊或掃描 QR 代碼。



![Image](assets/fr/20.webp)



傳送訊息給他建立聯繫。



![Image](assets/fr/21.webp)



對話內容就會出現在首頁上。如果對方接受您的聯絡請求，您會看到對方的姓名和個人檔案照片。



![Image](assets/fr/22.webp)



恭喜您，現在您已經可以快速使用 Signal 訊息，這是 WathsApp 的絕佳替代方案！如果您認為本教學有用，請在下方留下 Green 拇指，我將不勝感激。歡迎在您的社交網路分享本教學。非常感謝您！



我也推薦這篇教學，其中我介紹了 Proton Mail，一個比 Gmail 更能保護隱私的替代品：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2