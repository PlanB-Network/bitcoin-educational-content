---
name: Bitwarden
description: 如何設定密碼管理器？
---
![cover](assets/cover.webp)


在數位時代，我們需要管理眾多線上帳戶，涵蓋日常生活的各個層面，包括銀行、金融平台、電子郵件、檔案儲存、健康、行政管理、社交網路、電子遊戲等。


為了在每個帳戶上驗證自己的身份，我們使用一個識別碼，通常是電子郵件 Address，再加上一個密碼。面對無法記住大量獨特密碼的問題，我們可能會重覆使用相同的密碼，或稍微修改常用的基礎密碼，以方便記憶。但是，這些做法會嚴重影響您帳戶的安全性。


密碼要遵循的第一個原則是不要重複使用。每個線上帳號都應該使用完全不同於其他帳號的唯一密碼來保護。這一點很重要，因為如果攻擊者成功破解了您的一個密碼，您不希望他們有權存取您的所有帳戶。為每個帳戶設定獨一無二的密碼可以隔離潛在的攻擊，並限制其範圍。例如，如果您在電子遊戲平台和電子郵件中使用相同的密碼，而該密碼透過與遊戲平台相關的網路釣魚網站被洩露，攻擊者就可以輕易存取您的電子郵件，並控制您所有其他的線上帳戶。


第二個基本原則是密碼的強度。如果密碼很難被暴力破解，也就是說很難通過嘗試和錯誤來猜測，那麼這個密碼就被認為是強大的。這意味著您的密碼必須盡可能隨機、長且包含多種字符（小寫、大寫、數字和符號）。


在日常生活中應用這兩項密碼安全原則（唯一性和穩健性）可能會很困難，因為幾乎不可能為我們的所有帳戶記憶一個唯一、隨機和強大的密碼。這就是密碼管理器發揮作用的地方。


密碼管理器可生成並安全地儲存強大的密碼，讓您無需個別記憶即可訪問所有線上帳戶。您只需要記住一個密碼，即主密碼，就可以存取管理器中儲存的所有密碼。使用密碼管理器可以提高您的線上安全性，因為它可以防止重複使用密碼，並系統地生成隨機密碼。但它也能集中存取您的敏感資訊，簡化您日常使用帳戶的方式。

在本教程中，我們將探討如何設置和使用密碼管理器來增強您的在線安全性。我將向您介紹 Bitwarden，而在另一個教學中，我們將探討另一種稱為 KeePass 的解決方案。

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

警告：密碼管理器是儲存密碼的好幫手，但 ** 您絕對不可以將 Bitcoin Wallet 的 Mnemonic 短語儲存其中！** 請記住，Mnemonic 短語應該專門以實體格式儲存，例如紙張或金屬。


## Bitwarden 簡介


Bitwarden 是一款同時適合初學者和進階使用者的密碼管理器。它具有許多優點。首先，Bitwarden 是一個多平台的解決方案，這表示您可以將它當作行動應用程式、網頁應用程式、瀏覽器延伸功能和桌面軟體來使用。

![BITWARDEN](assets/notext/01.webp)

Bitwarden 可讓您線上儲存密碼，並同步處理所有裝置上的密碼，同時確保主密碼的端對端加密。舉例來說，這可讓您同時在電腦和智慧型手機上存取密碼，並在兩者之間進行同步。由於您的密碼是經過加密的，因此任何人，包括 Bitwarden 在內，如果沒有您主密碼的解密鑰匙，都無法存取這些密碼。


此外，Bitwarden 是開放原始碼的，這表示軟體可以由獨立專家審核。至於定價，Bitwarden 提供三種方案：


- 本教程將探討的免費版本。雖然它是免費的，但它提供的安全等級等同於付費版本。您可以儲存無限數量的密碼，並隨心所欲地同步處理多台裝置；
- 每年 10 美元的高級版本，包含額外功能，例如檔案儲存、銀行卡備份、使用實體安全金鑰設定 2FA 的功能，以及直接透過 Bitwarden 存取 TOTP 2FA 認證；
- 還有每年 40 美元的家庭方案，可將高級版的優點擴展至六個不同的使用者。

![BITWARDEN](assets/notext/02.webp)

在我看來，這些價格都很公道。免費版對於初學者來說是一個很好的選擇，而高級版相較於市面上其他的密碼管理器，則提供了非常好的性價比，同時也提供了更多的功能。此外，Bitwarden 是開放原始碼的這一點也是一大優勢。因此，它是一個有趣的折衷方案，尤其適合初學者。

Bitwarden 的另一項功能是，如果您家中有 NAS 等設備，您可以自行託管您的密碼管理器。透過此設定，您的密碼不會儲存在 Bitwarden 的伺服器上，而是儲存在您自己的伺服器上。這樣您就可以完全控制密碼的可用性。但是，這個選項需要嚴格的備份管理，以避免任何訪問權限的丟失。因此，Bitwarden 的自我託管更適合進階使用者，我們會在另一個教學中討論。

## 如何建立 Bitwarden 帳戶？


造訪 [Bitwarden 網站](https://bitwarden.com/)，點選「*開始*」。

![BITWARDEN](assets/notext/03.webp)

首先輸入您的電子郵件 Address 以及您的姓名或暱稱。

![BITWARDEN](assets/notext/04.webp)

接下來，您需要設定主密碼。正如我們在介紹中所看到的，這個密碼非常重要，因為它讓您可以存取管理器中所有其他儲存的密碼。因此，它存在兩個主要風險：遺失和洩密。如果您遺失了此密碼的存取權，您將無法再存取所有憑證。如果您的密碼被竊，攻擊者將能夠存取您的所有帳戶。


為了將遺失的風險降到最低，我建議將主密碼實體備份到紙張上，並將其存放在安全的地方。如果可能的話，請將此備份放在一個安全的信封中，以定期確保沒有其他人存取過。


為了防止您的主密碼被洩露，它必須非常堅固。它應該盡可能長，使用多種字符，並隨機選擇。在 2024 年，安全密碼的最低建議為 13 個字元，包括數字、小寫和大寫字母以及符號，前提是密碼是真正隨機的。但是，我建議選擇至少 20 個字元的密碼，包括所有可能的字元類型，以確保其安全性更長久。


在專用方塊中輸入您的主密碼，並在下面的方塊中確認。

![BITWARDEN](assets/notext/05.webp)

如果您願意，可以為您的主密碼添加提示。但是，我建議您不要這樣做，因為提示無法在您遺失密碼時提供可靠的復原方法，甚至可能對嘗試猜測或強制執行您密碼的攻擊者有用。一般而言，請避免建立可能危害您主密碼安全性的公開提示。

![BITWARDEN](assets/notext/06.webp)

然後按一下「*建立帳戶*」按鈕。

![BITWARDEN](assets/notext/07.webp)

現在您可以登入新的 Bitwarden 帳戶。輸入您的電子郵件 Address。

![BITWARDEN](assets/notext/08.webp)

然後輸入您的主密碼。

![BITWARDEN](assets/notext/09.webp)

現在您已進入密碼管理器的網頁 Interface。

![BITWARDEN](assets/notext/10.webp)

## 如何設定 Bitwarden？


首先，我們將確認電子郵件 Address。按一下「*寄送電子郵件*」。

![BITWARDEN](assets/notext/11.webp)

然後按一下透過電子郵件收到的按鈕。

![BITWARDEN](assets/notext/12.webp)

最後，再次登入。

![BITWARDEN](assets/notext/13.webp)

首先，我強烈建議您設定雙重認證 (2FA)，以確保密碼管理員的安全。您可以選擇使用 TOTP 應用程式或實體安全鑰匙。啟動 2FA後，您每次登入 Bitwarden 帳戶時，系統不僅會要求您輸入主密碼，還會要求您提供第二因素認證的證明。這是額外的 Layer 安全機制，在您的主密碼紙本備份被洩露時尤其有用。


如果您不確定如何設定和使用這些 2FA 裝置，我建議您參考這 2 個其他教學：


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

若要執行此操作，請移至「*設定*」功能表中的「*安全性*」標籤。

![BITWARDEN](assets/notext/14.webp)

然後按一下「*兩步登入*」標籤。

![BITWARDEN](assets/notext/15.webp)

在此，您可以選擇自己喜歡的 2FA 方法。例如，我會按一下「*管理*」按鈕，選擇使用 TOTP 應用程式的 2FA。

![BITWARDEN](assets/notext/16.webp)

確認您的主密碼。

![BITWARDEN](assets/notext/17.webp)

然後用您的 2FA 應用程式掃描 QR 代碼。

![BITWARDEN](assets/notext/18.webp)

輸入 2FA 應用程式上註明的 6 位數密碼，然後按一下「*開啟*」按鈕。![BITWARDEN](assets/notext/19.webp)

您的帳戶已成功設定雙重認證。

![BITWARDEN](assets/notext/20.webp)

現在，如果您嘗試重新登入管理員，首先需要輸入您的主密碼，然後輸入由 2FA 應用程式產生的 6 位數動態代碼。請確保您隨時都可以使用此動態代碼；沒有它，您將無法恢復密碼。

![BITWARDEN](assets/notext/21.webp)

在設定中，您也可以選擇在「*偏好設定*」標籤中自訂管理器。在這裡，您可以變更管理員自動鎖定前的持續時間，以及 Interface 的語言和主題。

![BITWARDEN](assets/notext/22.webp)

我強烈建議調整 Bitwarden 所產生的密碼長度。預設的長度是 14 個字元，這可能不足以達到最佳的安全性。既然您有一個管理器可以記住所有的密碼，您不妨利用它來使用非常強大的密碼。


為此，請移至「*產生器*」功能表。

![BITWARDEN](assets/notext/23.webp)

在這裡，您可以將密碼的長度增加到 40，並勾選包含符號的方塊。

![BITWARDEN](assets/notext/24.webp)

## 如何保障 Bitwarden 帳戶的安全？


現在您的密碼管理器已經設定完成，您可以開始儲存線上帳號的憑證。若要新增項目，請直接點選「*新增項目*」按鈕，或點選位於畫面右上方的「*新增*」按鈕，然後點選「*項目*」。

![BITWARDEN](assets/notext/25.webp)

在開啟的表單中，首先確定要儲存的項目的性質。若要儲存登入憑證，請從下拉式功能表中選擇「*登入*」選項。

![BITWARDEN](assets/notext/26.webp)

在「*名稱*」欄位中，為您的憑證輸入一個描述性的名稱。這將使您更容易搜尋和組織您的密碼，尤其是當您有大量密碼時。例如，如果您要儲存 PlanB Network 網站的憑證，您可以為此項目命名，使其在您未來搜尋時可立即辨認。

![BITWARDEN](assets/notext/27.webp)

*資料夾*」選項可讓您將憑證分類到資料夾中。目前，我們還沒有建立任何資料夾，但稍後我會告訴您如何建立。

![BITWARDEN](assets/notext/28.webp)

在「*使用者名稱*」欄位中，輸入您的使用者名稱，通常是您的電子郵件 Address。![BITWARDEN](assets/notext/29.webp)

接下來，在「*密碼*」欄位中，您可以輸入您的密碼。但是，我強烈建議您讓 Bitwarden generate 為您設定一個長的、隨機的、獨特的密碼。這樣可以確保您有一個強大的密碼。要使用此功能，請按一下要填寫欄位上方的雙箭頭圖示。

![BITWARDEN](assets/notext/30.webp)

您可以看到密碼已經產生。

![BITWARDEN](assets/notext/31.webp)

在「*URI 1*」欄位中，您可以輸入網站的網域名稱。

![BITWARDEN](assets/notext/32.webp)

最後，在「*註釋*」欄位中，如有必要，您可以新增其他詳細資訊。

![BITWARDEN](assets/notext/33.webp)

完成所有欄位的填寫後，按一下「*儲存*」按鈕。

![BITWARDEN](assets/notext/34.webp)

您的標識符現在會出現在您的 Bitwarden 管理員中。

![BITWARDEN](assets/notext/35.webp)

按一下它，即可存取其詳細資料並進行修改。

![BITWARDEN](assets/notext/36.webp)

按一下右邊的三個小圓點，您就可以快速複製密碼或識別符。

![BITWARDEN](assets/notext/37.webp)

恭喜您，您已成功在管理器中儲存了第一個密碼！如果您想更好地組織您的識別碼，您可以建立特定的資料夾。要做到這一點，請點擊螢幕右上方的 「*新建*」按鈕，然後選擇 「*資料夾*」。

![BITWARDEN](assets/notext/38.webp)

輸入資料夾名稱。

![BITWARDEN](assets/notext/39.webp)

然後按一下「*儲存*」。

![BITWARDEN](assets/notext/40.webp)

您的資料夾現在會出現在管理員中。

![BITWARDEN](assets/notext/41.webp)

您可以在建立識別碼時為其指定資料夾，就像我們之前所做的一樣，或是修改現有的識別碼。例如，按一下 PlanB Network 的識別碼，我就可以選擇將它分類到 "*Bitcoin*" 資料夾。

![BITWARDEN](assets/notext/42.webp)

如此一來，您就可以組織密碼管理器，讓您更容易找到您的識別碼。您可以使用個人、專業、銀行、電子郵件、社交網路、訂閱、購物、管理、串流、儲存、旅行、健康等資料夾來組織它們。

如果您只想使用網頁版的 Bitwarden，完全可以堅持使用。我建議您將密碼管理器加入瀏覽器的收藏夾，以方便存取並避免網路釣魚的風險。不過，Bitwarden 也提供完整的用戶端，讓您可以在各種裝置上使用管理員，並簡化日常使用。他們主要提供行動應用程式、瀏覽器擴充套件和桌面軟體。讓我們來看看如何一起設定它們。


![BITWARDEN](assets/notext/43.webp)


## 如何使用 Bitwarden 瀏覽器擴充套件？


首先，如果您願意，可以設定瀏覽器擴充套件。此擴充套件可作為管理員的縮小版，為您提供自動儲存新密碼、generate 安全密碼建議，以及在網站登入頁面自動填入憑證的可能性。


日常使用此擴充套件非常方便，但也可能開啟新的攻擊媒介。因此，一些網路安全專家建議不要使用密碼管理器的瀏覽器擴充套件。不過，如果您選擇使用 Bitwarden 擴充套件，以下是操作方法：


首先前往 [Bitwarden 官方下載頁面](https://bitwarden.com/download/#downloads-web-browser)。


![BITWARDEN](assets/notext/44.webp)


從提供的清單中選擇您的瀏覽器。在這個範例中，我使用的是 Firefox，所以我被重定向到 Firefox 附加元件商店中的官方 Bitwarden 擴充套件。其他瀏覽器的步驟也相當類似。


![BITWARDEN](assets/notext/45.webp)


按一下「*新增至 Firefox*」按鈕。


![BITWARDEN](assets/notext/46.webp)


之後您就可以將 Bitwarden 附加到您的擴充欄上，以方便存取。按一下擴充欄即可登入。


![BITWARDEN](assets/notext/47.webp)


輸入您的電子郵件 Address。


![BITWARDEN](assets/notext/48.webp)


然後是您的主密碼。


![BITWARDEN](assets/notext/49.webp)


最後，輸入認證應用程式中的 6 位數密碼。


![BITWARDEN](assets/notext/50.webp)


現在您已透過瀏覽器擴充套件連線至 Bitwarden 管理員。


![BITWARDEN](assets/notext/51.webp)


例如，如果我回到 PlanB Network 網站並嘗試登入我的帳戶，您可以看到整合到瀏覽器的 Bitwarden 延伸程式會識別登入欄位，並自動提供我選擇之前儲存的識別碼。


![BITWARDEN](assets/notext/52.webp)

如果我選擇此識別碼，Bitwarden 會為我填入登入欄位。擴充套件的這項功能可讓您快速連線到網站，而不需要從 Bitwarden 網路應用程式或軟體複製貼上認證資料。

![BITWARDEN](assets/notext/53.webp)

該擴充套件還可偵測新帳戶的建立。例如，在 PlanB Network 上建立新帳號時，Bitwarden 會自動建議儲存新的識別碼。

![BITWARDEN](assets/notext/54.webp)

按一下這個出現的建議，就會開啟擴充套件。它允許我輸入新識別碼的詳細資訊，以及 generate 強大且唯一的密碼。

![BITWARDEN](assets/notext/55.webp)

完成資訊填寫並點選「*儲存*」後，擴充套件會儲存認證。

![BITWARDEN](assets/notext/56.webp)

然後，擴充程式會自動將我們的憑證填入網站的適當欄位。

![BITWARDEN](assets/notext/57.webp)

## 如何使用 Bitwarden 軟體？


若要安裝 Bitwarden 桌面軟體，請先前往 [下載頁面](https://bitwarden.com/download/#downloads-desktop)。選擇並下載與您的作業系統相對應的版本。

![BITWARDEN](assets/notext/58.webp)

下載完成後，請在您的電腦上進行軟體安裝。首次啟動 Bitwarden 軟體時，您需要輸入您的憑證，以解鎖密碼管理器。

![BITWARDEN](assets/notext/59.webp)

然後，您就會到達管理員的首頁。Interface 與網頁應用程式幾乎相同。

![BITWARDEN](assets/notext/60.webp)

## 如何使用 Bitwarden 應用程式？


要從您的手機存取密碼，您可以安裝 Bitwarden 手機應用程式。首先前往 [下載頁面](https://bitwarden.com/download/#downloads-mobile)，使用您的智慧型手機掃描與您作業系統相對應的 QR 代碼。

![BITWARDEN](assets/notext/61.webp)

下載並安裝 Bitwarden 官方手機應用程式。首次開啟應用程式時，請輸入您的憑證，以解鎖存取您的密碼管理器。

![BITWARDEN](assets/notext/62.webp)

連線後，您就可以直接從應用程式中查詢和管理所有密碼。

![BITWARDEN](assets/notext/63.webp)

為了加強應用程式的安全性，我建議您進入設定並啟動 PIN 保護。這將增加額外的 Layer 安全性，以防手機遺失或遭竊。

![BITWARDEN](assets/notext/64.webp)

## 如何備份 Bitwarden？

為了確保您永遠不會失去密碼的存取權，即使您遺失了主密碼或 Bitwarden 伺服器受到災難影響，我建議您定期將您的管理員加密備份到外部媒體上。


我們的想法是使用不同於主密碼的密碼來加密您所有的 Bitwarden 認證，並將此加密備份保存在 USB 隨身碟或 Hard 磁碟機上，例如您放在家中的 USB 隨身碟或 Hard 磁碟機上。然後，您可以將解密密碼的實體複本保存在與備份媒體儲存位置不同的地方。例如，您可以將 USB 隨身碟放在家中，並將加密密碼的實體複本委託給信任的朋友。


此方法可確保即使您的備份媒體被盜，如果沒有解密密碼，您的資料仍然無法存取。同樣地，如果您的朋友沒有實體媒體，也無法存取您的資料。


但是，在發生問題時，您可以使用密碼和外部媒介來重新獲得您的憑證，與Bitwarden無關。因此，即使Bitwarden的伺服器被摧毀，您仍有可能取回您的密碼。


因此，我建議您定期執行這些備份，使它們始終包含您的最新憑證。為了避免每次新備份都要麻煩您的朋友，您可以將這個密碼儲存在密碼管理器中。這並非作為備份，因為您的朋友已經有一份實體副本，而是為了簡化您未來的匯出程序。


要繼續匯出，非常簡單：到 Bitwarden 管理員的「*工具*」區，然後選擇「*匯出儲存庫*」。

![BITWARDEN](assets/notext/65.webp)

格式請選擇「*.json (加密)*」。

![BITWARDEN](assets/notext/66.webp)

然後選擇「*密碼保護*」選項。

![BITWARDEN](assets/notext/67.webp)

在此，選擇一個強大、唯一且隨機產生的密碼來加密備份非常重要。這可確保即使您的加密備份遭竊，攻擊者也無法以暴力手段解密。

![BITWARDEN](assets/notext/68.webp)

按一下「*確認格式*」，然後輸入您的主密碼以繼續匯出。

![BITWARDEN](assets/notext/69.webp)

匯出完成後，您會在下載中找到加密的備份檔案。將檔案傳輸至安全的外部儲存裝置，例如 USB 隨身碟或 Hard 磁碟機。根據您的使用情況，定期重複此操作。例如，您可以根據需要每週或每月更新備份。