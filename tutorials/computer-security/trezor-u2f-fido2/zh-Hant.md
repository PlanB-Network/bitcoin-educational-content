---
name: Trezor U2F & FIDO2
description: 使用 Trezor 加強您的線上安全
---
![cover](assets/cover.webp)



Trezor 裝置是硬體錢包，原本是設計用來保護 Bitcoin Wallet 的安全，但它們也具有先進的選項，可以在網路上進行強大的身份驗證。由於與**U2F**和**FIDO2**協定相容，因此無需完全依賴密碼即可安全存取您的線上帳戶。



U2F (*Universal 2nd Factor*) 協定於 2014 年由 Google 和 Yubico 推出，之後由 FIDO Alliance 標準化。它能在登入時加入第二個實體驗證因素 (2FA)。一旦啟用，除了傳統的密碼之外，使用者每次嘗試連線到自己的帳戶時，都必須按下 Trezor 上的按鈕，以示同意。在這種情況下，Trezor 的運作方式類似於 Yubikey。



此方法以非對稱加密技術為基礎：不傳輸秘密資料，使網路釣魚或攔截攻擊無效。目前許多線上服務都支援 U2F。



除了可實現雙重認證的 U2F 之外，Trezors 還支援 FIDO2 (*Fast IDentity Online 2.0*)，這是 U2F 的進化版。這是 2018 年起的標準化認證協定，它延伸了 U2F 的邏輯，目的是完全取代密碼。它以兩個元件為基礎： *WebAuthn*（瀏覽器端）和 *CTAP2*（實體密鑰端）。FIDO2 實現了 「無密碼 」認證：用戶只需通過其 Trezor 裝置來識別自己的身份，Trezor 裝置就像一個獨一無二的加密令牌，而無需額外的密碼。此通訊協定現在與許多線上服務相容，特別是那些面向企業的服務。



除了「無密碼*」功能外，FIDO2 還能以類似 U2F 的方式進行雙重認證。



FIDO2 還引入了駐留憑證的概念，即直接存儲在 Trezor 中的識別碼，其中包括允許連接的私密金鑰和用戶的識別資訊。這種機制實現了真正的免密碼認證：只需插入 Trezor 並確認訪問，而無需輸入 ID 或密碼。相反，非駐機認證則較為傳統，只在設備中儲存私密金鑰；使用者 ID 則儲存在伺服器端，因此每次連線時都必須輸入。我們稍後再看看如何用 Trezor 儲存。



在本教程中，我們將發現如何啟動 U2F 或 FIDO2 進行雙重認證，然後如何設定 FIDO2，直接使用 Trezor 無需密碼即可存取您的帳戶。



**註：** U2F 相容於所有 Trezor 機型，但 FIDO2 只支援 Safe 3、Safe 5 和 Model T，不支援 Model One。



## 在 Trezor 上使用 U2F/FIDO2 進行 2FA



開始之前，請確認您已在 Trezor 上設定好 Bitcoin Wallet。正確儲存您的 Mnemonic 非常重要，因為雙重認證中 U2F 和 FIDO2 所使用的金鑰都來自此 Mnemonic。如果您的 Trezor 遺失或損壞，您可以在另一部 Trezor 裝置上輸入您的 Mnemonic 詞組來恢復對金鑰的存取（請注意，對於 「*無密碼*」模式下的 FIDO2 認證，僅 seed 是不夠的，我們會在接下來的章節中看到）。



將 Trezor 連接到電腦並解鎖。



![Image](assets/fr/01.webp)



使用雙因素驗證存取您要保護的帳戶。例如，我要使用 Bitwarden 帳戶。您通常會在服務設定中找到 2FA 選項，在「*驗證*」、「*安全*」、「*登入*」或「*密碼*」標籤下。



![Image](assets/fr/02.webp)



在專門用於雙重認證的部分中，選擇「*密碼*」選項（該詞彙可能因您使用的網站而異）。



![Image](assets/fr/03.webp)



通常會要求您確認目前的密碼。



![Image](assets/fr/04.webp)



為您的安全金鑰命名，以方便辨識，然後按一下「*讀取金鑰*」。



![Image](assets/fr/05.webp)



您的帳戶詳細資訊將會顯示在 Trezor 螢幕上。輕觸螢幕或按下 按鈕確認。您也會被要求確認 PIN 碼。



![Image](assets/fr/06.webp)



註冊此安全金鑰。



![Image](assets/fr/07.webp)



從現在開始，當您想要連線到您的帳號時，除了一般的密碼之外，還會要求您連線您的 Trezor。



![Image](assets/fr/08.webp)



然後您可以按下 Trezor 螢幕來確認認證。



![Image](assets/fr/09.webp)



使用 Hardware Wallet Trezor 進行雙重認證的好處是，由於有 Mnemonic 短語，您可以輕鬆恢復密鑰。除了這個基本備份之外，您也可以使用每個啟動 2FA 的服務所提供的緊急密碼。如果您遺失了安全鑰匙，這個緊急代碼可以讓您連線到您的帳戶。因此，必要時它可以取代 2FA 進行連線。



例如，在 Bitwarden 上，您可以按一下「*檢視復原碼*」來存取此代碼。



![Image](assets/fr/10.webp)



我建議您將這個密碼與您的主密碼存放在不同的地方，以防止它們一起被盜。例如，如果您的密碼儲存在密碼管理器中，請將您的 2FA 緊急代碼分別保存在紙張上。



如果您遺失了用於 2FA 認證的 Trezor，這種方法可為您提供兩級備份：第一級備份使用 Mnemonic 短語，適用於所有帳戶；第二級備份使用緊急代碼，適用於每個特定帳戶。然而，重要的是**不要混淆 Mnemonic 和緊急代碼的作用**：




- 12 或 24 個字的 Mnemonic 詞組不僅可以讓您存取所有帳號上用於 2FA 的金鑰，還可以存取用 Trezor 保護的比特幣；
- 緊急密碼允許您暫時繞過相關帳戶的 2FA 請求（在本例中，僅在 Bitwarden 上）。



## 在 Trezor 上使用 FIDO2



除了雙因素認證外，FIDO2 還可以實現 「無密碼 」認證，即在登錄網站時無須輸入密碼。只需將 Trezor 連接到您的電腦，就能以這種方式訪問您的安全帳戶。以下是如何配置此功能。



在您開始之前，請確認您已經在 Trezor 上設定好 Bitcoin Wallet。儲存 Mnemonic 是很重要的，因為 FIDO2「*無密碼*」識別碼是與您的 seed 一起加密的（我們會在下一節了解如何正確儲存這些識別碼）。



將 Trezor 連接到電腦並解鎖。



![Image](assets/fr/01.webp)



以 「*無密碼*」模式存取您要保護的帳戶。我以 Bitwarden 帳戶為例。這個選項通常可以在服務設定中找到，通常是在 「*驗證*」、「*安全*」或 「*密碼*」標籤下。



以 Bitwarden 為例，該選項位於「*主密碼*」標籤下。按一下「*開啟*」以啟動透過 FIDO2 進行驗證。



![Image](assets/fr/11.webp)



通常會要求您確認密碼。



![Image](assets/fr/12.webp)



您的帳戶詳細資訊將會顯示在 Trezor 螢幕上。輕觸螢幕或按下 按鈕確認。您還需要確認 PIN 碼。



![Image](assets/fr/13.webp)



在網站上，新增一個名稱以記住您的安全金鑰，然後按一下「*開啟*」。



![Image](assets/fr/14.webp)



然後您會被要求確認身份，以檢查鑰匙是否正常運作。



![Image](assets/fr/15.webp)



從現在開始，登入您的帳戶時，將不再需要輸入您的電子郵件 Address 或登入。只需點擊按鈕，即可在登錄表單上使用實體鑰匙進行身份驗證。



![Image](assets/fr/16.webp)



輸入 Hardware Wallet PIN 碼，確認與 Trezor 的連線。



![Image](assets/fr/17.webp)



您無需輸入密碼即可連接到您的帳戶。



![Image](assets/fr/18.webp)



**請注意，即使您在 Trezor 上透過 FIDO2 啟用「*無密碼*」驗證，您線上帳戶的主密碼仍可作為登入之用**。



## 儲存您的 FIDO2 認證 (認證居民)



如果您使用 FIDO2 或 U2F 進行雙重認證，也就是透過您的 Trezor 登入除了 2FA 驗證之外還需要密碼的帳號，則單憑 Mnemonic 短語就可以擷取您的密碼鑰匙。但是，如果您在上一節所述的 「*無密碼*」模式下使用 FIDO2，則除了備份加密這些憑證的 Mnemonic 短語外，還需要複製一份 FIDO 憑證。



要做到這一點，您需要一台安裝了 Python 的電腦。打開終端機，執行以下命令來安裝必要的 Trezor 軟體：



```shell
pip3 install --upgrade trezor
```



透過 USB 將 Trezor 連接到電腦，並使用 PIN 碼解鎖。



![Image](assets/fr/01.webp)



若要擷取儲存於 Trezor 上的 FIDO2 識別碼清單，請執行下列指令：



```shell
trezorctl fido credentials list
```



在 Trezor 上確認匯出。



![Image](assets/fr/19.webp)



您的 FIDO2 登錄資訊將顯示在您的終端機上。例如，對於我的 Bitwarden 帳戶，我得到了這些資訊：



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



複製並儲存所有這些資訊到一個文字檔中。此備份除了揭露您是以 FIDO2 使用這些服務之外，並沒有其他重大風險。*Credential ID*" 是使用您的 Wallet 的 seed 加密的，這表示攻擊者取得此備份後，將無法連線到您的帳號，只能注意到您正在使用這些帳號。若要解密這些 ID，您需要 Wallet 中的 seed。



因此，您可以創建多個文本文件的副本，並將它們存儲在不同的地方，例如本機電腦、檔 案託管服務和 USB 隨身碟等外部媒體。但是請記住，這個備份不會自動更新，所以每次與 Trezor 建立新的 「*無密碼*」連接時，您都需要更新它。



現在假設您的 Trezor 壞了。要找回您的 FIDO2 認證，您首先需要在新的 FIDO2 相容 Trezor 裝置上使用 Mnemonic 詞組恢復您的 Wallet。



復原完成後，若要在新裝置上匯入您的 FIDO2 識別碼，請在終端機執行下列指令：



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



只要將 `<CREDENTIAL_ID>` 換成您的一個識別碼即可。例如，在我的情況下，這將提供 ：



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



您的 Trezor 將提示您匯入您的 FIDO2 識別碼。請在螢幕上按鍵確認。



![Image](assets/fr/20.webp)



您的 FIDO2 登錄現在可以在您的 Trezor 上運行了。對每個識別碼重複此步驟。



恭喜您，現在您已經可以使用 U2F 和 FIDO2 快速使用您的 Trezor 了！如果您覺得本教學有用，請在下方留下 Green 拇指。請隨時在您的社交網路分享本教學。非常感謝



我也要推薦這份教學，其中我們瞭解了 U2F 和 FIDO2 驗證的另一種解決方案：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e