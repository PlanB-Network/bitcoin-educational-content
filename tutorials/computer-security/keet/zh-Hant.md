---
name: Keet
description: 點對點聊天
---
![cover](assets/cover.webp)



Keet 是一款無需任何伺服器即可運作的即時通訊應用程式。該應用程式由 Holepunch（由 Tether 和 Bitfinex 資助的公司）於 2022 年推出，完全以點對點網路為基礎，並採用徹底去中心化的方式：使用者之間直接交換訊息、通話和檔案，沒有中介。



Keet 對所有通訊進行端對端加密，並且不要求任何個人資料。註冊是匿名的，不需要電話號碼或電子郵件。除了交換文字訊息外，Keet 還提供高品質的視訊通話，以及無限制的檔案分享。因此，該應用程式可以混合方式使用，同時用於個人和專業用途。



![Image](assets/fr/01.webp)



目前（2025 年 4 月），Keet 並未完全開放原始碼。部分原始碼可以在 [Holepunch 的 GitHub 儲存庫](https://github.com/holepunchto) 取得，尤其是密碼和網路元件，但用戶端 Interface 尚未開放。不過，Holepunch 已經宣佈打算最終將整個應用程式開放原始碼。根據您發現本教學的時間，這可能已經完成了。




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



## 安裝 Keet



Keet 適用於所有平台。您可以直接從手機的應用程式商店下載應用程式：




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1)；
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549)；



在 Android 上，也可以 [透過 APK 安裝](https://github.com/holepunchto/keet-mobile-releases/releases)。



在本教程中，我們將專注於手機版本，但請注意 [電腦版本也可用](https://keet.io/) (MacOS、Linux 和 Windows)。也可以在多台裝置上同步您的帳戶。



## 在 Keet 上建立帳戶



第一次啟動時，您可以忽略簡報畫面。



![Image](assets/fr/02.webp)



按一下「*我是新使用者*」按鈕。



![Image](assets/fr/03.webp)



接受使用條款，然後按一下「*快速設定*」。



![Image](assets/fr/04.webp)



選擇名稱或暱稱，然後按一下「*完成設定*」。



![Image](assets/fr/05.webp)



您的個人資料已建立。再次按一下「*完成設定*」以完成設定。



![Image](assets/fr/06.webp)



您可以隨時從「*個人資料*」標籤自訂個人資料。



## 儲存您的 Keet 帳戶



使用您的新 Keet 帳戶的第一件事是儲存您的恢復詞組。這是一連串的24個單詞，讓您可以在遺失或更換裝置時恢復存取您的帳戶。這個詞組讓任何知道它的人都能完全訪問您的帳戶，所以做一個可靠的備份並永不洩露是很重要的。



若要執行此動作，請按一下 Interface 右下方的「*設定檔」標籤。



![Image](assets/fr/07.webp)



然後存取「*設定*」功能表。



![Image](assets/fr/08.webp)



選擇「*隱私權與安全性*」。



![Image](assets/fr/09.webp)



然後按一下「*恢復詞組*」。



![Image](assets/fr/10.webp)



按下「*檢視詞組*」按鈕以顯示您的復原詞組。仔細複製並妥善保存。



![Image](assets/fr/11.webp)



## 使用 Keet 傳送訊息



要在 Keet 上通訊，您需要建立「*房間*」。要這樣做，請按一下 Interface 右上方的鉛筆圖示。



![Image](assets/fr/12.webp)



選擇「*新增群組聊天*」。



![Image](assets/fr/13.webp)



為您的「*房間*」選擇名稱和說明，然後按一下「*建立群聊*」。



![Image](assets/fr/14.webp)



您的「*房間*」現已建立。按一下右上方的「*+*」圖示，即可邀請參與者。



![Image](assets/fr/15.webp)



定義透過邀請連結授予新會員的權利，以及連結的有效期限。然後按一下「*generate 邀請*」。



![Image](assets/fr/16.webp)



Keet 將 generate 連結加入您的「*Room*」。您可以複製它並分享，或讓您想要邀請的人掃描它的 QR 代碼。



![Image](assets/fr/17.webp)



現在您可以開始交換訊息和多媒體檔案。若要啟動通話，請按一下右上角的電話圖示。



![Image](assets/fr/18.webp)



在這個群組中，您也可以傳送私人訊息給特定的成員。按一下群組的個人資料圖片，然後在「*成員*」區段中選擇想要的成員。



![Image](assets/fr/19.webp)



按一下「*傳送 DM 請求*」按鈕並輸入您的訊息。



![Image](assets/fr/20.webp)



一旦 DM 請求被接受，您就可以在首頁找到此聯絡人，您可以與他私下交談。



![Image](assets/fr/21.webp)



## 在多部裝置上同步您的帳戶



現在您知道如何使用 Keet 並擁有帳號，您也可以在其他裝置上同步化，例如電腦。若要執行此操作，請在手機上開啟應用程式，然後按一下「*檔案*」並進入「*設定*」。



![Image](assets/fr/22.webp)



然後前往「*我的裝置*」功能表。



![Image](assets/fr/23.webp)



按一下「*新增裝置*」。Keet 將 generate 連結同步化新裝置。複製此連結。



![Image](assets/fr/24.webp)



在您的第二台裝置上安裝 Keet。在主畫面上，選擇「*我是目前使用者*」選項。



![Image](assets/fr/25.webp)



然後按一下「*連結裝置*」。



![Image](assets/fr/26.webp)



貼上第一台裝置提供的連結，然後按一下「*開始同步處理*」。



![Image](assets/fr/27.webp)



在您的第一台裝置上，按一下「*確認連結裝置*」以授權連線。



![Image](assets/fr/28.webp)



在第二台裝置上，按一下「*連結裝置*」即可完成程序。



![Image](assets/fr/29.webp)



現在您可以從這個新裝置存取所有「*房間*」和對話。



![Image](assets/fr/30.webp)



恭喜您，現在您已經可以快速使用 Keet 訊息，這是 WathsApp 的絕佳替代方案！如果您覺得本教程有用，請在下方留下 Green 拇指，我將非常感激。歡迎在您的社交網路分享本教學。非常感謝



我也推薦這篇教學，其中我介紹了 Proton Mail，一個比 Gmail 更能保護隱私的替代品：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2