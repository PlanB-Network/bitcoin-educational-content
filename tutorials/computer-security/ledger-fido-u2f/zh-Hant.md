---
name: "Ledger U2F & FIDO2"
description: 使用 Ledger 加強您的線上安全性
---
![cover](assets/cover.webp)



Ledger 裝置是硬體錢包，原本是設計用來保護 Bitcoin Wallet 的安全，但它們也具有進階選項，可以在網路上進行強大的認證。由於與 **U2F** 和 **FIDO2** 通訊協定相容，它們可讓您透過設定第二個驗證因素，確保線上帳戶的存取安全。



U2F (Universal 2nd Factor) 協定於 2014 年由 Google 和 Yubico 推出，之後由 FIDO Alliance 標準化。它可以在登入時加入第二個實體驗證因素 (2FA)。啟用後，除了傳統的密碼外，使用者每次嘗試連線到其帳戶時，都必須按下 Ledger 上的按鈕，以示同意。在這種情況下，Ledger 的運作方式類似於 Yubikey。U2F 實際上是 FIDO2 標準的子元件，包含 FIDO2 標準，同時帶來顯著的改進，包括對現代瀏覽器的原生支援，以及在驗證金鑰管理方面更大的彈性。



這些方法是以非對稱加密技術為基礎：不傳輸任何秘密資料，使網路釣魚或攔截攻擊無效。目前許多線上服務都支援 U2F 和 FIDO2。



在本教程中，我們將教您如何使用 Ledger 啟用 U2F 和 FIDO2 進行雙重認證。



**註：** 所有配備最新韌體的 Ledger 裝置都支援 U2F 和 FIDO2：Nano X 和 Nano S classic 從版本 2.1.0 開始，Nano S Plus 從版本 1.1.0 開始。Stax 和 Flex 機型原生相容。



## 安裝 Ledger 安全金鑰應用程式



如果您使用的是 Ledger 裝置，您可能知道單靠韌體並不包含管理加密錢包所需的所有功能。例如，若要使用 Bitcoin Wallet，您需要安裝「*Bitcoin*」應用程式。同樣地，若要管理 MFA 金鑰，您需要安裝「*安全金鑰*」應用程式。



開始之前，請確認您已在 Ledger 上設定好 Bitcoin Wallet。正確儲存您的 Mnemonic 是很重要的，因為用於 2FA 的鑰匙是從這個 Mnemonic 中衍生出來的。如果您的 Ledger 遺失或損壞，您可以在另一部 Ledger 裝置上輸入您的 Mnemonic 詞組，以恢復鑰匙的存取權（目前，Ledgers 尚未支援「*無密碼*」模式的 FIDO2 識別碼，因此沒有駐留的識別碼）。



將您的 Ledger 連接到電腦並解鎖。



![Image](assets/fr/01.webp)



若要安裝應用程式，請開啟 [Ledger Live] 軟體 (https://www.Ledger.com/Ledger-live)，然後進入「*我的 Ledger*」標籤。找到「*安全鑰匙*」應用程式，並將其安裝到您的裝置上。



![Image](assets/fr/02.webp)



*Security Key*" 應用程式現在應該會出現在 Ledger 上安裝的其他應用程式旁邊。



![Image](assets/fr/03.webp)



按一下應用程式，使其保持開啟狀態，以便進行教程的下一步。



![Image](assets/fr/04.webp)



## 使用 U2F/FIDO2 與 Ledger 進行 2FA



使用雙因素驗證存取您要保護的帳戶。例如，我要使用 Bitwarden 帳戶。您通常會在服務設定中找到 2FA 選項，在「*驗證*」、「*安全*」、「*登入*」或「*密碼*」標籤下。



![Image](assets/fr/05.webp)



在專門用於雙重認證的部分中，選擇「*密碼*」選項（該詞彙可能因您使用的網站而異）。



![Image](assets/fr/06.webp)



通常會要求您確認目前的密碼。



![Image](assets/fr/07.webp)



為您的安全金鑰命名，以方便辨識，然後按一下「*讀取金鑰*」。



![Image](assets/fr/08.webp)



您的帳戶詳細資訊將顯示在 Ledger 顯示器上。按下「*註冊*」按鈕確認（或同時按下兩個按鈕，視您使用的機型而定）。



![Image](assets/fr/09.webp)



存取權限已成功註冊。



![Image](assets/fr/10.webp)



註冊此安全金鑰。



![Image](assets/fr/11.webp)



從現在開始，當您登入您的帳戶時，除了一般的密碼之外，還會要求您連接您的 Ledger。



![Image](assets/fr/12.webp)



然後您可以按下 Ledger 顯示器上的「*登入*」按鈕確認驗證（或同時按下兩個按鈕，視您使用的機型而定）。



![Image](assets/fr/13.webp)



使用 Hardware Wallet Ledger 進行雙重認證的優點在於，由於有了 Mnemonic 短語，您可以輕鬆地恢復金鑰。除了這個基本備份之外，您也可以使用每個啟動 2FA 的服務所提供的緊急密碼。如果您遺失了安全鑰匙，這個緊急代碼可以讓您連線到您的帳戶。因此，必要時它可以取代 2FA 進行連線。



例如，在 Bitwarden 上，您可以按一下「*檢視復原碼*」來存取此代碼。



![Image](assets/fr/14.webp)



我建議您將這個密碼與您的主密碼存放在不同的地方，以防止它們一起被盜。例如，如果您的密碼儲存在密碼管理器中，請將您的 2FA 緊急代碼分別保存在紙張上。



此方法可在遺失用於 2FA 認證的 Ledger 時為您提供兩層備份：第一層是使用 Mnemonic 短語為所有帳戶進行備份，第二層是使用緊急代碼為特定帳戶進行備份。然而，重要的是 ** 不要混淆 Mnemonic 與緊急代碼的作用** ：




- 12 或 24 個字的 Mnemonic 詞組不僅可以讓您存取所有帳戶中用於 2FA 的金鑰，還可以存取用 Ledger 保護的比特幣；
- 緊急密碼允許您暫時繞過相關帳戶的 2FA 請求（在本例中，僅在 Bitwarden 上）。



恭喜您，現在您已經可以使用 Ledger 進行 MFA 了！如果您覺得本教學有用，請在下方留下 Green 的拇指，我會非常感激。請隨時在您的社交網路分享本教學。非常感謝



我也要推薦這份教學，其中我們瞭解了 U2F 和 FIDO2 驗證的另一種解決方案：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e