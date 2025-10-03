---
name: Nunchuk
description: Wallet 移動式適用於所有
---
![cover](assets/cover.webp)



## 功能強大的 Wallet


Nunchuk 於 2020 年末問世，它有一個明確的理念：讓多重簽章成為標準。因此，它的設計可執行非常先進的功能，並選擇直接在 Bitcoin 生態系統的參考軟體 Bitcoin Core 上建立設計。



經過 4 年多的開發和使用，它已經可以進行規模化的嘗試。如果您是初學者且不熟悉 Nunchuk，本指南將協助您踏出第一步並發掘此軟體，在您克服第一個衝擊後，您將能夠瞭解其進階功能。本教學本身是專門提供給擁有必要技能的中級使用者，讓他們能跟上所有的步驟，但對每個人來說，本教學也能成為一種啟發，讓他們找出如何增加技能的方法。我們將從行動版開始，這點指出是必要的，因為 Nunchuk 也有在電腦上執行的軟體。



## 下載


第一步肯定是決定在哪裡下載應用程式。請前往 [官方網站](https://nunchuk.io/)，您可以找到一些說明文件 (雖然不多，但也算是個開始)、功能介紹以及頁尾的所有下載連結。



📌在本教程中，我決定向您展示如何從 Github 套件庫下載 Software Wallet，以及在手機上安裝之前如何驗證版本。 **以下步驟只能在電腦上進行**，因此我建議您在桌上型電腦或筆記型電腦上執行所有這些步驟，並在所有驗證完成後，將 `.apk` 檔案傳輸到您的手機上。



![image](assets/en/01.webp)



如果您的技術不是很進階，您可以決定從官方商店下載`.apk`，並直接跳到本教學的設定部分。另一方面，如果您想要躍進，請繼續按步就班。



因此，從您的桌上型電腦按一下 _Visit our open source repository_ (瀏覽我們的開放原始碼資料庫)



該連結將帶您到 Nunchuk 的 Github 頁面，在那裡您可以找到許多 repos。我們將專注於 _nunchuk-android_ 套件庫。



![image](assets/en/02.webp)



在下一個畫面中，找到右邊的 _Releases_ 部分，然後選擇 _Latest_ 。



![image](assets/en/03.webp)



在 _Assets_ 下，下載版本 (本範例中為 1.67.apk)，以及 SHA256SUMS 檔案和 SHA256SUMS.asc。



![image](assets/en/04.webp)



若要尋找開發者的 GPG 金鑰，請回到套件庫的 _Releases_ 區段，尋找 1.9.53 (或更早版本)，其中有取得並下載 _GPG 金鑰的連結。



![image](assets/en/05.webp)



我們將透過 Sparrow wallet 提供的便利工具進行驗證，該工具具有專用視窗，並支援 PGP 簽署和 SHA256 Manifests。



然後啟動 Sparrow，並從 _Tools_ 功能表中選擇 _Verify Download_。



![image](assets/en/06.webp)



在彈出的視窗中，您會發現需要「填寫」的欄位：選擇右側的 _Browse_ 按鈕，並為每個欄位選擇您剛從 Github 下載的對應檔案。完成所有步驟後，視窗會如下所示，其中 Green 為核取標記，Hash 為確認清單。



![image](assets/en/07.webp)


**N.B. 螢幕截圖來自 Windows 電腦，同樣的做法可以用於電腦上的任何作業系統，只要安裝 Sparrow wallet即可。並已驗證！**



您可以找到 Sparrow wallet 的指南，下載此 Software Wallet


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

然後，您可以將 `.apk` 檔案從電腦傳輸至手機



![image](assets/en/08.webp)



並安裝 Nunchuk



![image](assets/en/09.webp)



在手機上啟動 Nunchuk 之前，請開啟 Orbot，並將新加入者放入 Tor 下的路由應用程式清單中。



![image](assets/en/11.webp)



現在執行 Nunchuk。對於專案功能--這不是本教學的主題--Nunchuk，一旦打開，將邀請您通過電子郵件或Google個人資料登錄。在您打算使用 Nunchuk 公司的進階計劃之前，**避免登入**，並選擇_以訪客身份繼續_選項。



![image](assets/en/12.webp)



## 設定


Nunchuk 以_Home_視窗的方式呈現，讓您輕鬆了解其操作哲學，我們稍後會詳細說明。



在底部您可以找到功能表，第一步，選擇 _Profile_ 存取設定。



![image](assets/en/10.webp)



然後選擇 _Display settings_，繼續忽略建立帳號的邀請。



![image](assets/en/14.webp)



在下面的畫面中，您可以檢查 Wallet 是否線上，並且可以連線您的伺服器，請密切注意點選_本指南_所提供連結的指示。



![image](assets/en/15.webp)



使用 _Save network settings_ 指令儲存設定，回到 _Profile_ 功能表並選擇 _Security settings_。



![image](assets/en/16.webp)



在此功能表中，您可以設定如何保護應用程式的開啟。為了防止不必要的存取，您可以使用手機的生物特徵保護 Nunchuk，和/或加入安全密碼。



![image](assets/en/17.webp)



您也可以看看 _About_ 功能表，您總是可以在 _Profile_ 視窗中找到該功能表。



![image](assets/en/18.webp)



這將允許您檢查應用程式的版本，或在需要時聯絡開發人員。



![image](assets/en/19.webp)



## 鑰匙產生與 Wallet


從 Nunchuk 的理念不難猜測，該軟件旨在作為管理多簽名錢包的有用工具。為了執行此功能，Nunchuk 允許透過將其與安排數位簽章所需的金鑰分離，來建立 Wallet。



事實上，Nunchuk 最理想的操作方式是依賴可 "Cold "的按鍵，建立可只看不動的錢包。



在之前的畫面中，您可能已經注意到底部有一個名為 _Keys_ 的選單。如果您剛下載 Nunchuk，在 _Home_ 和 _Keys_ 兩個選單中，您會看到一個大按鈕邀請您新增一個按鍵，_Add Key_。



![image](assets/en/20.webp)


![image](assets/en/21.webp)



** 這只是 Nunchuk 的運作方式：** 首先您 generate/ 匯入金鑰，然後再建立 Wallet，設定它選擇哪些金鑰會授權解鎖儲存在上面的資金。



即使在 Wallet singlesig 的情況下，您也是先建立鑰匙，然後才建立 Wallet。這正是我們現在要做的，從 Wallet singlesig 開始，打破僵局並發掘 Nunchuk 的功能。



按一下_新增鑰匙_



![image](assets/en/22.webp)



Nunchuk 會顯示許多支援的簽章裝置，但若要開始，請選擇 _Software_。



![image](assets/en/23.webp)



Nunchuk 將 generate 儲存在裝置上的 Mnemonic。接下來您需要寫下備份的字詞順序，創造最佳的環境條件，並確保您有時間好好地、安安靜靜地進行備份。軟體只會顯示一次 Mnemonic，無論您選擇現在或稍後顯示，請選擇 _Create and backup now_。



![image](assets/en/24.webp)



Nunchuk 會產生 24 個字的 Mnemonic 句子，這些句子會立即出現在下一個螢幕上



![image](assets/en/25.webp)



然後進行快速檢查，要求您從 3 個選項中選擇與 Mnemonic 序列中的數字相對應的正確單詞。


如果您已正確寫入 Mnemonic，_Continue_（繼續）按鈕就會開始運作。按下該按鈕即可繼續。



![image](assets/en/26.webp)



命名您的按鍵，然後按 _Continue_。



![image](assets/en/27.webp)



在這些步驟的最後，您會被詢問是否要在您的 Mnemonic 通訊短語中加入 [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39)。如果您對如何使用 passphrase、安排它的備份或它的運作方式沒有必要的認知，我建議您選擇 _我不需要密碼_。



![image](assets/en/28.webp)



最後會建立金鑰，並在功能表中顯示出來：




- 使用 _Key Spec_ 會顯示主指紋
- 您有設定，右上方的三個圓點，可以刪除鑰匙或簽署訊息
- 在鑰匙名稱旁邊，您會發現一個筆尖圖示，按一下它就可以編輯鑰匙的名稱，例如，將來可以讓您的鑰匙井然有序。
- 最後，您可以檢查鑰匙的健康狀態：按下 _Run health check_，應用程式就會檢查鑰匙是否受到損害。



完成後，請按一下_Done_。



![image](assets/en/29.webp)



在 _Keys_ 功能表中，您會看到您的第一個按鍵出現。



![image](assets/en/30.webp)



進入 _Home_ 功能表，會出現建立 Wallet 的選項。按一下 _Create new wallet_（建立新的錢夾）。



![image](assets/en/31.webp)



Nunchuk 向您展示了許多可能性，這些可能性大多與該公司提供的服務有關，而這些服務並非本教程的主題。



在本指南中，我們將透過詳細說明，建立 _Hot Wallet 和 _Custom wallet_。


讓我們從_自訂錢包_開始。



![image](assets/en/32.webp)



簡單來說，應用程式會要求您命名這個新的 Wallet，並選擇位址的腳本。在教學中，我選擇保留預設值 _Native segwit_。完成後，選擇_繼續_。



![image](assets/en/33.webp)



Wallet 的設定會繼續要求您設定使用哪一條鑰匙來解除 Wallet 的資金鎖定。如果有多個金鑰，您可以從清單中選擇。目前我們只建立了一個，因此我們選擇在該金鑰上打勾。在右下角，您可以看到 Nunchuk 將如何要求您設定未來的 Wallet 多重簽章，以增加 _Required keys_ 的數量。



![image](assets/en/34.webp)



由於我們要建立的是 singlesig，所以離開 `1`，然後按一下 _Continue_。



最後，會出現驗證畫面，您可以在此檢查 Wallet 的功能：




- 名稱
- 1/1 Multisig" tage，Nunchuk 也是這樣命名 Wallet 的。
- 腳本類型，`原生 SegWit
- Keys "金鑰及其指紋和衍生路徑



滿意後，按下_建立錢包_。



![image](assets/en/35.webp)



Wallet 已建立，您可以下載 [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) 檔案作為備份。若要返回主功能表，請按一下左上角的箭頭。



![image](assets/en/36.webp)



您在 _Home_ 中，顯示新建立的 Wallet 報告連線的餘額和狀態。按一下藍色空間，即可存取 Wallet 的主要功能。



![image](assets/en/37.webp)





- 右上角的鏡頭圖示可讓您進行交易搜尋；
- `View Wallet config` 允許存取設定功能表，您可以在此編輯 Wallet 的名稱，並啟用右上方的進階選項（您無法取得其螢幕截圖）。在這裡您可以匯出 Wallet 設定、標籤、取代按鍵、變更 [gap limit](https://planb.network/en/resources/glossary/gap-limit) 等。



## 與 Nunchuk 進行交易



獎項_獲得_



![image](assets/en/38.webp)



此應用程式可顯示 Address 的 QR Code 或複製/分享 scriptPubKey 以接收上鏈資金。



![image](assets/en/39.webp)



在這第一架 Address 上，我們有一架 UTXO 到達、



![image](assets/en/40.webp)



但我們仍會按一下 _Receive_ 來接收另一個。



![image](assets/en/41.webp)



目的是讓您發現 Nunchuk 將這個新的 Address 報告為_未使用的位址_，但同時也顯示您有_已使用的位址_及其數量。



### 使用硬幣控制消費交易



當第二個 UTXO 也到達後，回到 Wallet 主畫面查看這兩筆交易的狀態，最重要的是點選 _View coins_ 選項。



![image](assets/en/42.webp)



在這裡您會看到個別的 UTXO。在此，您可以按一下金額旁邊的小箭頭，選擇檢視其中一個特別的金額。



![image](assets/en/43.webp)



並檢查到貨時間、說明、攔截 UTXO，以免花掉等等。



![image](assets/en/44.webp)



但如果您按一下右上角的箭頭，回到 _Coins_ 功能表，就可以開啟「Coin Control」，以更有控制的方式花費您的 UTXO。



在下面的範例中，我選擇 21,000 Sats 中的 UTXO，然後按一下左下角的符號。



![image](assets/en/45.webp)



Nunchuk 會自動打開 _New transaction_ 視窗來花掉這個 UTXO。在消費交易中，首先，您必須手動設定金額，或選擇 _Send all selected_ 來傳送所有硬幣控制餘額，而不產生剩餘金額。設定好金額後，選擇_繼續_。



![image](assets/en/46.webp)



現在 Nunchuk 會顯示貼上 Address 的位置，以便將這些資金轉帳、詳細說明並完成交易。



![image](assets/en/47.webp)



選擇 _Create transaction_（建立交易）會將自動費用和交易管理委託給應用程式。我建議您選擇 _Custom transaction_，以獲得更多控制權。



在這個新畫面中，選擇




- _Subtract fee from send amount_，防止費用被 Wallet 中存在的另一個 UTXO 支付、花掉並產生餘額 (這是可避免的隱私權損失)；
- 然後在探索器上檢查後手動設定費用。



完成所有這些步驟後，按一下_繼續_。



![image](assets/en/48.webp)



下一個畫面是完整的交易摘要。如果一切正常，請選擇 _Confirm and create transaction_（確認並建立交易）。



![image](assets/en/49.webp)



有了_Pending signatures_ Nunchuk 提醒您交易p正在等待您的簽名來核准支出，您可以按一下_Sign_來簽名。



![image](assets/en/50.webp)



_Broadcast_ 指令會出現在底部，用來傳播最終完成並已簽署的交易。



![image](assets/en/51.webp)



### 從功能表 _Send_ 支出交易



當我們在 Wallet 主頁面上看到交易出去並等待確認時，我們使用 _Send_ 功能表來模擬每天的支出。



![image](assets/en/52.webp)



事實上，按一下 _Send_ 即會出現傳送交易的畫面，與剛才看到的畫面相同，但不需透過硬幣控制。



在第二個範例中，我決定選擇 _Custom transaction_ 並傳送全部金額，但我也可以手動設定。一旦您決定了要傳送的金額，請按_Continue_。



![image](assets/en/53.webp)



然後一定要做出是否從有關的 UTXO 中扣除費用的情況（在本範例中，選擇是被強制的，因為只有一個），根據 Mempool 中當時的情況手動調整費用，然後按 _Continue_ （繼續）。



![image](assets/en/54.webp)



如果摘要畫面令人滿意，請選擇 _確認並建立交易_。



![image](assets/en/55.webp)



使用 _Sign_ 簽署交易



![image](assets/en/56.webp)



並將其傳播至網路。



![image](assets/en/57.webp)



Wallet 此时余额为零，历史记录正在更新。



![image](assets/en/58.webp)



## 建立 "Hot Wallet"



最後，也不要遺漏任何 Nunchuk mobile 初期階段的東西，讓我們看看這如何創造出該應用程式所稱的 "Hot Wallet"。



在 Nunchuk 的 _Home_ 功能表中，出現錢包清單的地方，按一下右上角的 `+`。



![image](assets/en/59.webp)



從選項中選擇 _Hot wallet_（熱錢包



![image](assets/en/60.webp)



Nunchuk 在介紹頁面中提供了一些有關處理 Hot 皮夾的建議，您將選擇 _Continue_ 繼續。



![image](assets/en/61.webp)



片刻之後，Wallet 即會建立，並在清單中呈現棕色。這是 Nunchuk 提醒您尚未備份 Wallet 的顏色。



![image](assets/en/62.webp)



按一下 Wallet 的名稱，以存取其設定，您可能會發現邀請您立即備份 Mnemonic 的短語。



![image](assets/en/63.webp)



這個步驟和我們之前見過的一樣，所以我們不再重複。完成後，Nunchuk 會帶您到相關的按鍵頁面，您可以編輯為您使用 _Custom_ 程序所建立的按鍵。



![image](assets/en/64.webp)



也可嘗試 _執行健康檢查_



![image](assets/en/65.webp)



或查看如何在應用程式的 _Home_ 中顯示所有錢包。



![image](assets/en/66.webp)



## 要牢記繼續獨立


就像有一個建立的順序，也就是先產生金鑰，然後再產生 Wallet，您也需要維持相反的順序，才能從應用程式中刪除這些項目。



如果您需要刪除其中一個金鑰，您應該先有先見之明刪除 Wallet 或錢包，因為錢包使用其中一個簽章金鑰進行交易：先刪除錢包，然後才刪除金鑰。如果您不遵循這個順序，您會發現自己無法刪除金鑰。



現在您已經知道如何開始使用 Nunchuk，您可以繼續研究這個應用程式並發掘它的秘密。在本教程中，我們只進行了第一步，但還有更多複雜的應用程式和進階需求，這款 Software Wallet 可以幫助您滿足。