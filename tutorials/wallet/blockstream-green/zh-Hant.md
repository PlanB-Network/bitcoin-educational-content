---
name: Blockstream Green - 移动电话
description: 設定行動版 Software Wallet
---
![cover](assets/cover.webp)


Software Wallet 是安裝在電腦、智慧型手機或其他連網裝置上的應用程式，可讓您管理並保護 Bitcoin Wallet 金鑰。與隔離私人金鑰的硬體錢包不同，"Hot "錢包因此會在可能遭受網路攻擊的環境中運作，增加盜版和竊取的風險。


軟體錢包應該用來管理合理數量的比特幣，尤其是用於日常交易。對於 Bitcoin 資產有限的人來說，軟體錢包也是一個有趣的選擇，因為對他們來說，投資在 Hardware Wallet 上似乎不相稱。然而，它們經常暴露在網際網路中，對於儲存您的長期儲蓄或大筆資金而言，安全性較低。對於後者，最好選擇更安全的解決方案，例如硬體錢包。


在本教程中，我要向您介紹最佳的行動 Software Wallet 解決方案之一： **Blockstream Green**。


![GREEN](assets/fr/01.webp)


如果您想瞭解如何在電腦上使用 Blockstream Green，請參閱此其他教學：


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

## 介紹 Blockstream Green


Blockstream Green 是可在行動和桌上型電腦上使用的 Software Wallet。前身為 *Green Address*，此 Wallet 在 2016 年被收購後，成為 Blockstream 專案。


Green 是一款特別容易使用的應用程式，因此對初學者來說非常有趣。它提供所有優良 Bitcoin Wallet 的基本功能，包括 RBF (*Replace-by-fee*)、Tor 連線選項、連結您自己的節點、SPV (*簡易付款驗證*)、硬幣標籤和控制。


Blockstream Green 也支援 Liquid Network、Blockstream 為 fast 開發的 Bitcoin Sidechain、Confidential Transactions 以外的主要 Blockchain。本教學專注於 Bitcoin，但稍後的教學會涵蓋 Liquid 的使用。


## 安裝和設定 Blockstream Green 應用程式


第一步當然是下載 Green 應用程式。前往您的應用程式商店：



- [For Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)；
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN](assets/fr/02.webp)


對於 Android 使用者，您也可以透過 `.apk` 檔案 [Blockstream 的 GitHub 上提供](https://github.com/Blockstream/green_android/releases) 安裝應用程式。


![GREEN](assets/fr/03.webp)


啟動應用程式，然後勾選「我接受條件...*」方塊。


![GREEN](assets/fr/04.webp)


當您第一次打開 Green 時，主螢幕會出現沒有設定的 Wallet。之後，如果您建立或匯入錢包，它們就會出現在這個 Interface 中。在繼續建立 Wallet 之前，我建議您調整應用程式設定以符合您的需求。按一下「應用程式設定」。


![GREEN](assets/fr/05.webp)


*Enhanced Privacy*" 選項只適用於 Android，可透過停用螢幕截圖和隱藏應用程式預覽來增強隱私。它也會在手機鎖定時自動鎖定應用程式存取權，讓您的資料更難曝光。


![GREEN](assets/fr/06.webp)


對於希望加強隱私權的人，應用程式提供透過 Tor 將您的流量根植於 Tor 網路的選項，這個網路會加密您所有的連線，讓您的活動難以被追蹤。雖然這個選項可能會稍微拖慢應用程式的運作速度，但為了保護您的隱私，我們強烈建議您使用這個選項，尤其是當您沒有使用自己的完整節點時。


![GREEN](assets/fr/07.webp)


對於擁有自己完整節點的用戶，Green Wallet 提供了通過 Electrum 伺服器與之連接的可能性，保證了對 Bitcoin 網絡資訊和交易分配的完全控制。


![GREEN](assets/fr/08.webp)


另一個替代功能是「*SPV Verification*」選項，它允許您直接驗證某些 Blockchain 資料，從而減少信任 Blockstream 預設節點的需要，不過這種方法無法提供 Full node 的所有保證。


![GREEN](assets/fr/09.webp)


根據您的需要調整這些設定後，按一下「*儲存*」按鈕並重新啟動應用程式。


![GREEN](assets/fr/10.webp)


## 在 Blockstream Green 上建立 Bitcoin Wallet


現在您已準備好建立 Bitcoin Wallet。按一下「*開始*」按鈕。


![GREEN](assets/fr/11.webp)


您可以選擇建立本機 Software Wallet 或透過 Hardware Wallet 管理 Cold Wallet。在本教程中，我們將專注於建立 Hot Wallet，因此您需要選擇「*在此裝置*」選項。在未來的教學中，我會告訴您如何使用其他選項。


與此同時，「*僅供觀看*」選項可讓您匯入一個擴展的公開金鑰 (`xpub`)，以檢視 Wallet 的交易，但卻無法花費相關的資金，例如，這對於追蹤 Hardware Wallet 上的 Wallet 非常方便。


![GREEN](assets/fr/12.webp)


然後您可以選擇還原現有的 Bitcoin Wallet 或建立新的 Wallet。在本教程中，我們將建立一個新的 Wallet。但是，如果您需要從 Mnemonic 詞組重新生成現有的 Bitcoin Wallet，例如在遺失 Hardware Wallet 之後，您需要選擇第二個選項。


![GREEN](assets/fr/13.webp)


然後您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。當您的手機發生問題時，這個詞組可讓您從任何相容的軟體恢復存取 Wallet。目前，選擇 24 個字的短語不會比 12 個字的短語更安全。因此，我建議您選擇 12 個字的 Mnemonic 詞組。


Green 接著會提供您 Mnemonic 的詞組。在繼續之前，請確定您沒有被監視。按一下「*Show recovery phrase*（顯示復原詞組*）」，將其顯示在螢幕上。


![GREEN](assets/fr/14.webp)


**此 Mnemonic 可讓您完全不受限制地存取您所有的 bitcoins ** 任何持有此 Mnemonic 的人都可以竊取您的資金，即使沒有實體存取您手機的權限。


它可以在您的手機遺失、被盜或損壞時恢復對比特幣的存取。因此，仔細地**備份在實體媒體（而非數位媒體）**上，並將其存放在安全的地方是非常重要的。您可以把它寫在一張紙上，或者為了增加安全性，如果這是一個大型的 Wallet，我建議把它刻在一個不鏽鋼支架上，以保護它免受火災、水災或倒塌的風險（對於一個專為保護少量比特幣而設計的 Hot Wallet，簡單的紙張備份可能就足夠了）。


*顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會在 Testnet 上使用，並會在本教程結束時刪除。


![GREEN](assets/fr/15.webp)


當您正確地將 Mnemonic 詞組錄製在實物媒介上後，請點選 「*繼續*」。Green Wallet 接下來會要求您確認 Mnemonic 詞組中的一些單字，以確保您正確記錄了這些單字。在空白處填入缺失的單字。


![GREEN](assets/fr/16.webp)


選擇您裝置的 PIN 碼，用於解鎖您的 Green Wallet。這是用來防止未經授權的實體存取。此 PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要擁有 12 或 24 個字的 Mnemonic 詞組，就能重新取得您的 bitcoins。


我們建議您選擇一個盡可能隨機的 6 位數 PIN 碼。請務必儲存此密碼，以免忘記，否則您將被迫從 Mnemonic 取出您的 Wallet。然後您可以加入生物辨識攔截選項，避免每次使用時都要輸入 PIN 碼。一般而言，生物辨識技術的安全性遠不及 PIN 碼本身。因此，在預設情況下，我建議您不要設定這個解鎖選項。


![GREEN](assets/fr/17.webp)


再次輸入 PIN 碼以確認。


![GREEN](assets/fr/18.webp)


等待您的 Wallet 建立，然後按一下「*建立帳號*」按鈕。


![GREEN](assets/fr/19.webp)


然後，您可以選擇標準的單一簽章 Wallet（我們將在本教學中使用），或是受雙因素認證 (2FA) 保護的 Wallet。


![GREEN](assets/fr/20.webp)


Green 上的 2FA 選項創建了一個 2/2 多重簽章 Wallet，其中一個密鑰由 Blockstream 持有。這意味著要進行交易，需要兩把鑰：一個本地鑰，由您手機上的 PIN 碼保護；另一個遠端鑰，由 Blockstream 伺服器上的 2FA 保護。如果無法存取 2FA 或 Blockstream 的服務無法使用，基於時間鎖腳本的恢復機制可確保您的資金自主恢復。雖然此配置可大幅降低您的比特幣被盜的風險，但其管理較為複雜，且部分依賴 Blockstream。在本教程中，我們將選擇經典的單一簽章 Wallet，金鑰本機儲存在手機上。


您的 Bitcoin Wallet 現已使用 Green 應用程式建立！


![GREEN](assets/fr/21.webp)


在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行一次空的恢復測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Green 應用程式上刪除您的 Wallet，而它還是空的。然後嘗試使用您的紙張備份在 Green 上還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果相符，您就可以放心，您的紙本備份是可靠的。若要瞭解有關如何進行測試復原的更多資訊，請參閱此其他教學：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 在 Blockstream Green 上設定您的 Wallet


如果您想要個人化您的 Wallet，請按一下右上角的三個小圓點。


![GREEN](assets/fr/22.webp)


*Rename*" 選項可讓您自訂 Wallet 的名稱，如果您在同一個應用程式上管理多個錢包，這個選項尤其有用。


![GREEN](assets/fr/23.webp)


*Unit*" 功能表可讓您變更 Wallet 的基本單位。例如，您可以選擇以梭希（satoshis）而非比特幣顯示。


![GREEN](assets/fr/24.webp)


*Settings*" 功能表可讓您存取 Bitcoin Wallet 的各種選項。


![GREEN](assets/fr/25.webp)


舉例來說，您可以在這裡找到您的擴充公開金鑰及其 *描述符*，如果您打算從這台 Wallet 設定 Wallet 為僅看管模式，這對您很有用。


![GREEN](assets/fr/26.webp)


您也可以變更 Wallet PIN 碼並啟動生物辨識連線。


![GREEN](assets/fr/27.webp)


## 使用 Blockstream Green


現在您的 Bitcoin Wallet 已經設定完成，您已準備好接收第一台 Sats！只要按一下「*接收*」按鈕即可。


![GREEN](assets/fr/28.webp)


Green 接著會在您的 Wallet 中顯示第一個空白的接收 Address。您可以掃描相關的 QR 代碼，或直接複製 Address 來傳送 bitcoins。這種類型的 Address 沒有指定付款人要發送的金額。但是，您可以通過點擊右上角的三個小圓點，然後點擊 "*Request amount*"，並輸入所需的金額，來發送要求特定金額的 generate Address。


由於您使用的是 SegWit v0 帳號 (BIP84)，所以您的 Address 會以 `bc1q...` 開頭。在我的例子中，我使用的是 Testnet Wallet，所以前綴略有不同。


![GREEN](assets/fr/29.webp)


當交易在網路上廣播時，就會出現在您的 Wallet 中。


![GREEN](assets/fr/30.webp)


等到您收到足夠的確認後，才會認為交易是確實的。


![GREEN](assets/fr/31.webp)


在您的 Wallet 中存有比特幣，您現在還可以發送比特幣。點擊 「*發送*」。


![GREEN](assets/fr/32.webp)


在下一頁，輸入收件人的 Address。您可以手動輸入或掃描 QR 代碼。


![GREEN](assets/fr/33.webp)


選擇付款金額。


![GREEN](assets/fr/34.webp)


在畫面底部，您可以選擇此交易的收費率。您可以選擇遵循應用程式的建議或自訂費用。相對於其他待處理的交易，費用越高，您的交易處理速度就越快。有關收費市場資訊，請瀏覽 [Mempool.space](https://Mempool.space/) 中的「*交易費用*」部分。


![GREEN](assets/fr/35.webp)


按一下「*下一步*」，進入交易摘要畫面。檢查 Address、金額和收費是否正確。


![GREEN](assets/fr/36.webp)


如果一切順利，請將螢幕下方的 Green 按鈕向右滑動，即可在 Bitcoin 網路上簽署和廣播交易。


![GREEN](assets/fr/37.webp)


您的交易現在會出現在您的 Bitcoin Wallet 面板上，等待確認。


![GREEN](assets/fr/38.webp)


*本教學是基於 Loïc Morel 所寫的 [屬於 Bitstack 的原始版本](https://www.bitstack-app.com/blog/installer-portefeuille-Bitcoin-Green-Wallet)。Bitstack 是法國的 Bitcoin 新式銀行，提供以 DCA（美元成本平均法）儲存比特幣的可能性，或透過自動四捨五入系統儲存日常支出。* Bitstack 是法國的 Bitcoin 新式銀行，提供以 DCA（美元成本平均法）儲存比特幣的可能性，或透過自動四捨五入系統儲存日常支出。