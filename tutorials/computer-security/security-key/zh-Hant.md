---
name: YubiKey 2FA
description: 如何使用實體安全鑰匙？
---
![cover](assets/cover.webp)


如今，雙因素認證 (2FA) 已經成為提高線上帳戶安全性、防止未經授權存取的必要方式。隨著網路攻擊的增加，單靠密碼來保護您的帳戶有時並不足夠。


2FA 除了傳統的密碼之外，還需要第二種驗證方式，因此引入了額外的 Layer 安全性。這種驗證有多種形式，例如透過 SMS 傳送的代碼、專用應用程式產生的動態代碼，或使用實體安全鑰匙。即使您的密碼被盜，使用 2FA 也能大幅降低您的帳戶被洩露的風險。


在另一篇教學中，我介紹了如何設定和使用 TOTP 2FA 應用程式：


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

在此，我們將介紹如何使用實體安全鑰匙作為所有帳戶的第二認證因素。


## 什麼是實體安全鑰匙？


實體安全鑰匙是一種裝置，用來透過雙重因素驗證 (2FA) 加強線上帳戶的安全性。這些裝置通常類似小型 USB 鑰匙，必須插入電腦的連接埠，以驗證是否確實是合法使用者嘗試連線。

![SECURITY KEY 2FA](assets/notext/01.webp)

當您登入受 2FA 保護且使用實體安全鑰匙的帳戶時，您不僅必須輸入一般密碼，還必須將實體安全鑰匙插入電腦，並按下按鈕以驗證認證。因此，這種方法增加了額外的 Layer 安全性，因為即使有人成功取得您的密碼，如果沒有實際擁有鑰匙，他們也無法存取您的帳戶。


實體安全金鑰特別有效，因為它結合了兩種不同類型的認證因素：知識證明（密碼）和持有證明（實體金鑰）。


但是，這種 2FA 方法也有缺點。首先，如果您要存取帳戶，您必須隨時備有安全金鑰。您可能需要將它添加到您的鑰匙鏈中。其次，與其他 2FA 方法不同，使用實體安全鑰匙需要支付初始成本，因為您必須購買小型裝置。安全鑰匙的價格一般在 30 到 100 歐元之間，視所選功能而定。


## 選擇哪一種實體安全鑰匙？


要選擇您的安全金鑰，必須考慮幾個標準。

首先，您需要檢查裝置支援的通訊協定。我建議至少選擇支援 OTP、FIDO2 和 U2F 的金鑰。製造商通常會在產品描述中強調這些細節。要驗證每個金鑰的相容性，您也可以造訪 [dongleauth.com](https://www.dongleauth.com/dongles/)。

此外，請確保密鑰與您的作業系統相容，儘管像 Yubikey 這樣的知名品牌一般都支援所有廣泛使用的系統。


您也應該根據電腦或智慧型手機上可用的連接埠類型來選擇鑰匙。例如，如果您的電腦只有 USB-C 連接埠，請選擇配備 USB-C 連接埠的按鍵。有些按鍵也提供藍牙或 NFC 連線選項。

![SECURITY KEY 2FA](assets/notext/02.webp)

您也可以根據裝置的附加功能進行比較，例如防水和 Dust 防水功能，以及按鍵的形狀和大小。


關於安全鑰匙品牌，Yubico 的 [YubiKey 裝置](https://www.yubico.com/) 是最知名的，我個人使用並推薦這款裝置。Google 也提供 [Titan Security Key](https://store.google.com/fr/product/titan_security_key) 裝置。至於開放原始碼的替代方案，[SoloKeys](https://solokeys.com/) (non- OTP) 和 [NitroKey](https://www.nitrokey.com/products/nitrokeys) 是有趣的選擇，但我從來沒有機會測試它們。


## 如何使用實體安全鑰匙？


當您收到安全金鑰後，不需要任何特定的設定。金鑰通常在收到後即可使用。您可以立即使用它來保護您支援這種認證方式的線上帳號。例如，我將向您展示如何使用此物理安全金鑰來保護我的 Proton 郵件帳戶。

![SECURITY KEY 2FA](assets/notext/03.webp)

您可以在帳戶設定中找到啟用 2FA 的選項，通常在「*密碼*」或「*安全性*」一節中。按一下允許您使用實體金鑰啟動 2FA 的核取方塊或按鈕。

![SECURITY KEY 2FA](assets/notext/04.webp)

將鑰匙插入電腦。

![SECURITY KEY 2FA](assets/notext/05.webp)

輕觸安全鑰匙上的按鈕進行驗證。

![SECURITY KEY 2FA](assets/notext/06.webp)

輸入名稱以記住您使用的按鍵。

![SECURITY KEY 2FA](assets/notext/07.webp)

就這樣，您的安全金鑰已成功加入帳戶的 2FA 驗證。

![SECURITY KEY 2FA](assets/notext/08.webp)

在我的範例中，如果我嘗試重新連線到我的 Proton 郵件帳號，首先會要求我輸入密碼和使用者名稱。這是認證的第一個因素。

![SECURITY KEY 2FA](assets/notext/09.webp)

接著，我被要求插入我的安全金鑰，以進行第二重驗證。

![SECURITY KEY 2FA](assets/notext/10.webp)

接下來，我需要觸碰實體鑰匙上的按鈕，以驗證認證，然後重新連線到我的 Proton 郵件帳戶。

![SECURITY KEY 2FA](assets/notext/11.webp)

重複此操作以保護所有線上帳戶，尤其是重要帳戶，如電子郵件帳戶、密碼管理員、雲端和線上儲存服務或金融帳戶。