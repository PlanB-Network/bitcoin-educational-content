---
name: Ashigaru
description: Samourai Wallet 的 fork 保護、管理和混合您的比特幣
---

![cover](assets/cover.webp)



Ashigaru 是一款 Bitcoin 移動 wallet 應用程式，繼 Samourai Wallet 專案之後，以全新的形式推出。此軟體誕生於一個特殊的環境：2024 年 4 月，Samourai Wallet 的創始人被美國當局逮捕，他們的伺服器也被查封。雖然 Samurai 應用程式本身仍可使用，但目前已不再維護。Ashigaru 是 Samurai Wallet 的免費 fork 版本，由匿名團隊維護，以保證 Samurai 功能的延續性，並維護其原始理念：捍衛 Bitcoin 使用者的隱私與主權。



Ashigaru 吸收了 Samourai 的大部分基因：類似的介面、明顯的自我監護方式、開放源碼以及注重隱私。程式碼以 GNU GPLv3 授權釋出，確保任何人都可以審核、修改或重新散佈軟體。



Ashigaru 應用程式整合了一套先進的工具，用於保密和管理您的 UTXO：




- Whirlpool**，一個以 Zerolink 為基礎的 Coinjoin 協定，讓您可以打破交易進出之間的確定連結，而不會失去對您資金的主權。
- PayNym** 實作可重複使用的付款代碼 (BIP47)，現在透過「*Pepehash*」頭像系統來表示。
- Ricochet**，此功能會在交易中加入中間跳轉，使交易更難被追蹤。
- 當然還有***Coin Control***，可以精確地選擇、凍結和標示您的 UTXO。
- 批次支出****，透過將多筆付款組合成單一交易來降低成本。
- 隱藏模式**，可將手機上的應用程式隱藏在假啟動器之後，以便在實體檢查手機時不被發現。
- 先進的支出工具可優化您的保密性（payjoin、stonewall...）。
- 使用密碼 BIP39 的最佳化復原系統。
- 自動優化交易費用選擇的系統。



![Image](assets/fr/01.webp)



因此，Ashigaru 針對的是了解 Bitcoin 上交易可追蹤性問題的使用者。無論您是注重隱私的使用者、致力於自我監控的資深 bitcoiner，或是面臨監控增加風險的個人，這個 wallet 應用程式都能提供您所需的工具，讓您重新掌控自己在 Bitcoin 上的活動。



Ashigaru 可透過應用程式在手機上使用，我們將在本教學中探討。但它也可以在 PC 上使用 ***Ashigaru Terminal***，我們會在未來的教學中介紹。



![Image](assets/fr/02.webp)



在本教程中，我想向您介紹 Ashigaru 的基本使用方法：安裝、連接到 Dojo、備份、接收和發送比特幣。進階工具將在其他專門的教學中介紹。



## 1.Ashigaru 的先決條件



此應用程式需要一些先決條件才能正常運作。首先，它不是 Google Play 商店或 App Store 等經典商店中的應用程式。它只能透過 Tor 網路下載的「.apk」檔案手動安裝到您的手機上。因此，如果您使用 iPhone，此方法將無法運作：您需要使用 Android 裝置。



要透過 Tor 下載 `.apk` 檔案，您需要一個能夠存取 `.onion` 網站的瀏覽器。最簡單的方法是在手機上安裝 Tor 瀏覽器應用程式，可從 [Google Play 商店](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) 或直接 [透過其`.apk`](https://www.torproject.org/download/#android) 下載。



![Image](assets/fr/03.webp)



大多數最新的智慧型手機都會預設阻止安裝來自未知來源的應用程式。您需要在裝置設定中為 Tor 瀏覽器暫時啟動此選項，以允許安裝。應用程式安裝完成後，請記得停用此功能，以加強手機的安全性。



使用 Ashigaru 的另一個必要先決條件是 Bitcoin Dojo 節點。基於安全和主權的考量，Ashigaru 團隊不提供中央伺服器來連接您的應用程式。因此，您需要運行自己的 Dojo 實例，或者連接至可信的實例。



Dojo 可讓您的 Ashigaru 應用程式查詢區塊鏈資訊、檢視您的地址餘額，並在 Bitcoin 網路上廣播您的交易。



若要瞭解更多關於 Dojo 的資訊，並學習如何安裝，我邀請您遵循此專用教學：



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

如果您真的無法負擔運行自己的 Dojo，您可以在 [dojobay.pw](https://www.dojobay.pw/mainnet/) 找到願意免費分享實例的人。這可能是暫時的解決方案，但長遠來說，我建議您使用自己的 Dojo，以保證您的主權和機密性。



## 2.檢查並安裝 Ashigaru 應用程式



### 2.1.下載 Ashigaru 應用程式



在手機上開啟 Tor 瀏覽器，進入 [Ashigaru 官方網站](https://ashigaru.rs/download/)，在 `Download`區段。然後點擊 `Download for Android` 按鈕下載安裝檔案。



![Image](assets/fr/04.webp)



在裝置上安裝應用程式之前，我們會檢查其真實性和完整性。這是非常重要的步驟，尤其是直接從「.apk」檔案安裝應用程式時。



### 2.2.檢查 Ashigaru 應用程式



回到 [Ashigaru 官方網站](https://ashigaru.rs/download/) 的 `Download` 區塊，然後複製標題 `SHA-256 Hash of the APK file` 下顯示的訊息。複製整個區塊，從 `BEGIN PGP SIGNED MESSAGE` 到 `END PGP SIGNATURE`。



![Image](assets/fr/05.webp)



仍然在手機上，在 Tor 瀏覽器中開啟一個新標籤，然後到 [Keybase 驗證工具](https://keybase.io/verify)。將您剛複製的訊息貼到提供的欄位中，然後按下「驗證」按鈕。



![Image](assets/fr/06.webp)



如果簽章是真實的，Keybase 會顯示一則訊息，確認檔案已由 Ashigaru 開發人員簽章。您也可以點選 Keybase 所指示的 `ashigarudev` 設定檔，檢查他們的金鑰指紋是否與 ：`a138 06b1 fa2a 676b`。



但是，如果在此階段出現錯誤，則表示簽章無效。在這種情況下，**請勿安裝 APK**。從頭重新開始，或在繼續之前向社群尋求協助。



![Image](assets/fr/07.webp)



Keybase 已為您提供應用程式的雜湊值。現在我們要檢查您下載的 `.apk` 檔案的雜湊值是否與 Keybase 上驗證的相符。為此，請前往 [HASH FILE ONLINE](https://hash-file.online/)。



![Image](assets/fr/08.webp)



按一下「BROWSE...」按鈕，然後選擇在步驟 2.1 中下載的 `.apk` 檔案。


然後選擇雜湊函數 `SHA-256`，然後按一下 `CALCULATE HASH` 以計算檔案的雜湊值。



![Image](assets/fr/09.webp)



網站會顯示您的 `.apk` 檔案的雜湊值。將其與您在 Keybase.io 上驗證的雜湊值進行比較。如果兩個哈希值相同，則表示真實性和完整性檢查成功。現在您可以繼續安裝應用程式。



![Image](assets/fr/10.webp)



### 2.3. 安裝 Ashigaru 應用程式



若要安裝應用程式，請開啟手機的檔案管理員，並移至下載資料夾。然後點擊您剛剛檢查過的 `.apk` 檔案，並在出現提示時確認安裝。



![Image](assets/fr/11.webp)



Ashigaru 已安裝在您的手機上。



## 3.初始化應用程式並建立 Bitcoin 產品組合



首次啟動應用程式時，請選擇 `MAINNET`。



![Image](assets/fr/12.webp)



然後按一下「開始」。



![Image](assets/fr/13.webp)



現在我們要建立一個新的 Bitcoin 組合。按下「建立新的 wallet」按鈕。



![Image](assets/fr/14.webp)



### 3.1. 建立 Bitcoin 產品組合



Ashigaru 需要 passphrase BIP39。選擇您的 passphrase，並將其輸入適當的欄位。它必須盡可能長且隨機，以抵抗暴力攻擊。



立即為這台 passphrase 做一個實體備份。這是非常重要的一步：如果您遺失了您的手機，**如果您不再擁有這個 passphrase，您將無法再存取您的 Ashigaru wallet 所儲存的比特幣**。這個 passphrase 也用來加密 wallet 復原檔案。



如果您不知道什麼是 passphrase，或不完全瞭解它的運作方式，我強烈建議您閱讀這份額外的教學。這一點非常重要，因為 passphrase 是您安全的關鍵要素：誤解其使用方法可能會導致您的資金永久損失。



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

輸入您的 passphrase 後，按一下 `NEXT`。



![Image](assets/fr/15.webp)



然後選擇 PIN 碼。此代碼將用於解鎖您的 Ashigaru wallet，防止未經授權的實體存取。它不參與 wallet 密鑰的加密推導。這意味著，即使不知道 PIN 碼，任何人只要有您的助記短語和 passphrase 就可以重新獲得您的比特幣。



選擇長而隨機的 PIN 碼。切記在手機以外的地方保留一份備份，以防止它們同時被洩露。



![Image](assets/fr/16.webp)



一旦建立了 PIN 碼，Ashigaru 就會顯示 wallet 的助記短語。警告：這個短語與您的 passphrase 相結合，可以完全存取您的比特幣。任何持有它的人都可以佔有您的資金，即使他們無法存取您的手機。當您的手機遺失、被盜或損壞時，這12個字的序列可以用來恢復您的wallet。因此，請務必小心保存在實體媒介（紙張或金屬）上。



切勿以數位形式儲存此短語，否則您的資金有被盜用的風險。根據您的安全策略，您可以製作數份實體複本，但絕對不要分割。保持字詞的正確順序，並確保它們都有編號。



最後，切勿將記憶體和 passphrase 存放在同一個地方。如果兩者同時遭到攻擊，攻擊者就有可能存取您的 wallet。



![Image](assets/fr/17.webp)



若要進一步瞭解如何保護您的助記詞組，請參閱本補充教學 ：



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

然後 Ashigaru 會要求您重新確認您的 passphrase。利用這個機會檢查您的實體備份是否正確。



![Image](assets/fr/18.webp)



### 3.2. 連接道場



接下來是連線到您的道場的步驟。如簡介中所述，Ashigaru 必須連線至道場才能與 Bitcoin 網路互動。



登入您的 Dojo「維護工具」，並開啟「PAIRING」功能表。



![Image](assets/fr/19.webp)



在 Ashigaru 上，按 `Scan QR` 按鈕，然後掃描 DMT 顯示的連接 QR 代碼。然後按一下 `Continue` 以確認。



![Image](assets/fr/20.webp)



輸入您的 PIN 碼來解鎖 wallet。這將帶您進入同步化頁面。在此階段看到 *PayNym* 錯誤是正常的，因為 wallet 是新的。只需單擊「繼續」即可。



![Image](assets/fr/21.webp)



接下來，您將進入作品集的首頁。



![Image](assets/fr/22.webp)



在繼續之前，我建議您在 wallet 仍未包含 bitcoin 時進行一次測試復原。這將使您能夠檢查您的紙備份是否正常工作。要瞭解如何進行，請遵循此教程：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4.設定 Ashigaru 應用程式



若要存取應用程式設定，請按一下左上角您的 *PayNym* 圖片，然後選擇「設定」。



![Image](assets/fr/23.webp)



在這裡您可以找到多種選項，讓 Ashigaru 的操作符合您的需求。但是，我強烈建議您從一開始就啟動 2 個重要參數。



首先打開「安全性 > 隱藏模式」功能表，然後在需要時啟動此功能。它會將 Ashigaru 應用程式隱藏在您手機上安裝的一般應用程式的名稱、標誌和介面後面。其目的是防止任何人在實際檢查您的手機時識別 Ashigaru。



![Image](assets/fr/24.webp)



提供的每個虛假應用程式都有特定的方法來解鎖真正的 Ashigaru 介面。例如，如果您選擇計算機，Ashigaru 應用程式會從您的主螢幕上消失，取而代之的是一個虛假的計算機。當您打開它時，您會看到經典的計算機工作介面，但要進入 Ashigaru，您只需快速點選 `=` 符號五次即可。



第二個要啟動的重要參數是 [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee) 。如果交易因費用太低而卡在 mempools 中，此選項可讓您增加交易的費用。您可以透過 `Transactions > Spend using RBF` 功能表來啟動它。



![Image](assets/fr/25.webp)



提示：您只需點擊首頁上顯示的總餘額，即可將投資組合的顯示單位從 "BTC 「更換為 」sat"。



## 5.在 Ashigaru 上接收比特幣



現在您的投資組合已開始運作，您可以接收 satss。要這樣做，請按介面右下方的 `+` 按鈕，然後按綠色的 `Receive` 按鈕。



![Image](assets/fr/26.webp)



Ashigaru 會顯示您 wallet 中第一個未使用的接收地址，以防止地址重複使用（地址重複使用對您的隱私而言是非常不好的做法）。然後您就可以將這個地址轉寄給需要寄比特幣給您的人或服務。



![Image](assets/fr/27.webp)



交易一旦在網路上廣播，就會自動出現在應用程式的首頁。



![Image](assets/fr/28.webp)



## 6.使用 Ashigaru 傳送 bitcoins



現在您的 Ashigaru wallet 中已有比特幣，您也可以傳送它們。要這樣做，請按右下方的 `+` 按鈕，然後選擇紅色的 `Send` 按鈕。



![Image](assets/fr/29.webp)



然後，選擇您要支出的帳戶。目前，我們還沒有處理「Postmix」帳戶，它是專門用於硬幣接合的，我們會在稍後的教學中討論。因此，我們將從主存款帳戶發送資金。



![Image](assets/fr/30.webp)



輸入交易詳細資料：要傳送的金額和收件人的 Bitcoin 位址。



![Image](assets/fr/31.webp)



按一下右上角的三個小圓點，然後按一下「顯示未使用的輸出」，您也可以精確選擇您想要使用的 UTXO，以提高您的隱私。



![Image](assets/fr/32.webp)



填寫完所有詳細資料後，按一下介面下方的白色箭頭即可繼續。



然後，您會進入一個摘要頁面，顯示交易的所有詳細資料。會顯示幾個重要元素：




- 在「目的地」區塊中，最後一次檢查收件者地址和傳送的金額是否正確；
- 在「費用」區塊中，您可以檢視 Ashigaru 自動選擇的費用比率，必要時，按一下「管理」即可修改；
- Transaction」區塊指出您要執行的交易類型。在這裡，我們討論的是簡單的交易，但 Ashigaru 也支援其他類型的隱私優化交易，我們將在未來的教學中詳細介紹；
- 紅色的「交易警示」區塊會警告您，如果您的交易顯示可被連鎖分析工具識別的模式，而這些模式可能會危及您的隱私。點擊它，您可以查看詳細資訊。例如，在我的案例中，Ashigaru 告訴我發送的金額是整數 (`3000sats`)，讓我可以推斷出哪個輸出對應於支出，哪個是兌換。要瞭解有關這些鏈分析啟發式方法的更多資訊，我邀請您在 Plan ₿ Academy 上關注我的 BTC 204 培訓 ；
- 最後，您可以為交易加上標籤，以記錄交易的目的。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

檢查完所有資訊後，使用綠色箭頭傳送 bitcoins。按住箭頭，然後向右拖曳，確認上傳。



![Image](assets/fr/33.webp)



您的交易已在 Bitcoin 網路上廣播。



![Image](assets/fr/34.webp)



## 7.復原您的 Ashigaru wallet



Ashigaru wallet 的復原與經典 Bitcoin wallet 的復原略有不同，因為應用程式使用的方法與 Samurai Wallet 相同。如果您失去了對 wallet 的存取權（無論是因為忘記密碼、卸載或遺失手機），有幾種方法可以恢復您的比特幣。



如果您還能使用您的手機，或者您曾經備份過這個檔案，最簡單的方法就是使用備份檔案`ashigaru.txt`。此檔案包含您在 Ashigaru 的新實例（或 Sparrow Wallet）上還原您的組合所需的所有資訊，但它是用您在本教程步驟 3.1 中定義的 passphrase 加密的。因此，您必須同時擁有 `ashigaru.txt` 檔案和您的 passphrase 才能使用此方法。



有了這兩個元素，您就可以，例如，還原 Sparrow Wallet 上的投資組合。



![Image](assets/fr/35.webp)



如果您無法存取 `ashigaru.txt` 檔案，您仍可以使用 passphrase 的助記詞組重新存取您的資金，就像存取其他 Bitcoin 組合一樣。我建議您在新的 Ashigaru 實例上執行還原，或直接在 Sparrow Wallet 上執行還原，以便在使用 Whirlpool 的情況下輕鬆恢復旁路路徑。或者，您也可以透過手動輸入衍生路徑，將此資訊匯入任何其他與 BIP39 相容的軟體。



有關這個過程的詳細資訊，請參閱我所寫的 Wallet Samurai wallet 復原完整教學。由於 Ashigaru 是 fork，因此程序完全相同：



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

如您所見，無論您使用何種還原方法，passphrase 都是不可或缺的。所以一定要小心備份。您也可以依據您的安全策略製作多份副本。



## 8.更新應用程式



若要更新 Ashigaru 應用程式，由於您是透過`.apk`檔安裝，而非像一般應用程式一樣透過 Play Store 安裝，因此您需要下載與更新版本對應的新`.apk`檔，然後再手動安裝。



重複本教學第 2 節所述的步驟，除了當您點擊「.apk」檔啟動安裝時，**您的 Android 手機應該提供「更新」選項，而不是「安裝」**。



![Image](assets/fr/41.webp)



這是非常重要的一點：如果 Android 顯示「安裝」而非「更新」，您很可能正在安裝詐騙版本。在這種情況下，請立即中斷安裝程序。



與第一次安裝一樣，在進行更新之前，請檢查 `.apk` 檔案的真實性和完整性。



若要瞭解新版本何時推出，請不定期瀏覽 Ashigaru 官方網站。請放心，Ashigaru 是繼承自 Samourai Wallet 的穩定成熟應用程式，更新頻率相對較低。



## 9.捐贈 Ashigaru 計劃



Ashigaru 是一個開放源碼專案。如果您想支持其開發，可以透過 PayNym 直接從應用程式捐款。



要進行此操作，請點擊介面右上方的 PayNym，然後選擇以 `PM...` 開頭的付款代碼。



![Image](assets/fr/36.webp)



然後按螢幕右下方的 `+` 按鈕。



![Image](assets/fr/37.webp)



選擇 `Ashigaru Open Source Project` 為收件人。



![Image](assets/fr/38.webp)



按一下 `CONNECT` 按鈕，建立 BIP47 通訊通道（有關此協定的詳細資訊，請參閱下面的教學）。



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



確認通知交易後，您就可以按一下介面右上角的白色小箭頭，將捐款寄給該專案。



![Image](assets/fr/40.webp)



您現在已經知道如何使用 Ashigaru 應用程式的基本功能。在未來的教學中，我們將介紹如何利用進階的消費交易，以及 Whirlpool，即繼承自 Samurai Wallet 的硬幣接合實作。
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
