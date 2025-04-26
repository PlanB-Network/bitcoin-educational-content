---
name: Authy 2FA
description: 如何使用 2FA 應用程式？
---
![cover](assets/cover.webp)


如今，雙因素認證 (2FA) 已經成為提高線上帳戶安全性、防止未經授權存取的必要方式。隨著網路攻擊的增加，單靠密碼來保護您的帳戶有時並不足夠。2FA 除了密碼之外，還需要第二種驗證方式，因此多了一重安全防護。這種驗證有幾種形式，例如透過 SMS 傳送的代碼、專用應用程式產生的動態代碼，或使用實體安全鑰匙。使用 2FA 可以大大降低您的帳戶被洩露的風險，即使在您的密碼被盜的情況下也是如此。


## 透過驗證應用程式進行 2FA


我們會在其他教學中探討其他解決方案，例如實體安全鑰匙，但在本教學中，我建議特別討論 2FA 應用程式。這些應用程式的操作相當簡單：當帳戶啟用 2FA 後，每次登入時，除了要求您輸入一般的密碼外，還會要求您輸入一個 6 位數的代碼。此代碼由您的 2FA 應用程式產生。這個 6 位數字代碼的一個重要特點是它不是靜態的；應用程式每 30 秒會產生一個新代碼。

![AUTHY 2FA](assets/notext/01.webp)

代碼每 30 秒更新一次，讓攻擊者很難存取您的帳戶。此系統可防止攻擊者重複使用竊取或攔截的代碼，因為代碼很快就會過期。因此，即使攻擊者成功取得代碼，他們也只能在需要新代碼之前的很短時間內使用。此外，代碼變更如此頻繁，也大幅減少了駭客試圖透過暴力手段猜測代碼的時間。


因此，透過驗證應用程式進行 2FA 是一種易於使用且免費的方法，可大幅提升您線上帳戶的安全性。


有許多應用程式可用來設定 2FA，其中 Google Authenticator 和 Microsoft Authenticator 最為人熟知。然而，在本教程中，我希望向您介紹另一種較不知名的解決方案 Authy。所有這些應用程式都使用相同的 TOTP (*Time based One Time Password*) 通訊協定運作，因此它們的使用方式相當類似。

與其他大型科技公司的解決方案相比，Authy 具備多項優勢。首先，它允許您在多部裝置上同步您的 2FA 令牌，這在遺失或更換電話時非常有用。Authy 還能讓您 generate 加密備份並線上儲存，確保即使遺失主要裝置，也不會遺失存取權杖的權限。從使用者 Interface 的角度來看，我個人認為 Authy 也比其他替代方案提供更愉快、更直覺的體驗。


## 如何安裝 Authy？


在您的智慧型手機上，前往應用程式商店（Google Play 商店或 Apple 商店），搜尋「*Twilio Authy Authenticator*」。



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

首次啟動應用程式時，您需要建立一個帳戶。選擇您所在國家的撥號代碼以及您的電話號碼，然後按一下「*提交*」。

![AUTHY 2FA](assets/notext/03.webp)

輸入您的電子郵件 Address 以恢復代碼。

![AUTHY 2FA](assets/notext/04.webp)

我們將發送一封電子郵件給您確認您的 Address。輸入收到的 6 位數字來確認。

![AUTHY 2FA](assets/notext/05.webp)

選擇兩種可用方法之一來驗證您的電話號碼。如果您選擇接收簡訊，請輸入簡訊收到的 6 位數代碼來確認您的號碼。

![AUTHY 2FA](assets/notext/06.webp)

恭喜，您的 Authy 帳戶已經建立！

![AUTHY 2FA](assets/notext/07.webp)

## 如何設定 Authy？


首先，按一下螢幕右上方的三個小圓點，進入應用程式的設定。

![AUTHY 2FA](assets/notext/08.webp)

然後按一下「*設定*」。

![AUTHY 2FA](assets/notext/09.webp)

在「*我的帳戶*」標籤中，您可以選擇修改您的帳戶。我建議您選擇「*App Protection*」，在應用程式中加入 PIN 碼。這可為存取您的應用程式增加額外的 Layer 安全性。

![AUTHY 2FA](assets/notext/10.webp)

在「*帳戶*」標籤中，您可以為您的代碼設定備份。此備份可在發生問題時恢復您的代碼。它使用您必須定義的密碼進行加密。重要的是，此密碼必須強大並保存在安全的地方。如果您有其他復原方法，例如使用同一個 Authy 帳號的第二台裝置，則不一定必須設定此備份。

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


如果您希望允許新增其他裝置，我建議您啟動選項，在新增新裝置之前，要求您 Authy 帳戶上目前已授權的裝置進行確認。

![AUTHY 2FA](assets/notext/12.webp)

若要新增裝置，只需使用相同的憑證重覆前述的安裝程序即可。接下來會要求您從主裝置確認這項新存取。


## 如何在帳戶上設定 2FA？


要透過 Authy 等應用程式在帳戶上設定 2FA 認證碼，該帳戶必須支援此功能。現在，大多數的線上服務都提供 2FA 選項，但情況並不總是如此。讓我們以我在另一篇教學中介紹的 Proton 郵件帳號為例：


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

您通常可以在帳戶的設定中找到此 2FA 選項，通常位於「*密碼*」或「*安全性*」部分。

![AUTHY 2FA](assets/notext/14.webp)

當您在 Proton 郵件帳戶上啟動此選項時，會出現一個 QR 代碼。您必須使用 Authy 應用程式掃描此 QR 代碼。

![AUTHY 2FA](assets/notext/15.webp)

在 Authy 上，按一下「*+*」按鈕。

![AUTHY 2FA](assets/notext/16.webp)

按一下「*掃描 QR 碼*」。然後掃描網站上的 QR 代碼。

![AUTHY 2FA](assets/notext/17.webp)

如有必要，您也可以選擇調整使用者名稱。進行變更後，按一下「*儲存*」按鈕。

![AUTHY 2FA](assets/notext/18.webp)

Authy 會顯示該帳號專屬的 6 位數動態密碼，每 30 秒刷新一次。

![AUTHY 2FA](assets/notext/19.webp)

在網站上輸入此代碼以完成 2FA 設定。

![AUTHY 2FA](assets/notext/20.webp)

有些網站也會在啟動 2FA 後提供您恢復代碼。如果您失去 Authy 應用程式的存取權，這些代碼可讓您存取您的帳戶。我建議將其保存在安全的地方。

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

每次登入帳戶時，您都需要提供 Authy 所產生的動態密碼。現在您可以使用此 2FA 方法確保所有相容帳號的安全。若要在 Authy 上新增帳號，請按一下應用程式右上方的三個小圓點。

![AUTHY 2FA](assets/notext/23.webp)

然後按一下「*新增帳戶*」。

![AUTHY 2FA](assets/notext/24.webp)

遵循與第一個帳戶相同的步驟。您的各種動態代碼將可以在 Authy 首頁上看到。