---
name: Blockstream Green - 2FA
description: 在 Green Wallet 上設定 2/2 Multisig
---
![cover](assets/cover.webp)

___

***注意：** 自2025年5月起，將無法再啟用受雙重驗證（2FA）保護的新帳戶。此功能僅適用於先前已啟用此類帳戶的使用者。*

___

Software Wallet 是安裝在電腦、智慧型手機或其他連網裝置上的應用程式，可讓您管理並保護 Bitcoin Wallet 金鑰。與隔離私人金鑰的硬體錢包不同，"Hot "錢包因此會在可能遭受網路攻擊的環境中運作，增加盜版和竊取的風險。

軟體錢包應該用來管理合理數量的比特幣，尤其是用於日常交易。對於 Bitcoin 資產有限的人來說，軟體錢包也是一個有趣的選擇，因為對他們來說，投資 Hardware Wallet 似乎不相稱。然而，它們經常暴露在網際網路中，對於儲存長期儲蓄或大筆資金而言，安全性較低。對於後者，最好選擇更安全的解決方案，例如硬體錢包。

在本教程中，我將向您介紹如何使用 Blockstream Green 上的 "*2FA*"選項來提高 Hot Wallet 的安全性。


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## 介紹 Blockstream Green


Blockstream Green 是可在行動和桌上型電腦上使用的 Software Wallet。前身為 *Green Address*，此 Wallet 在 2016 年被收購後，成為 Blockstream 專案。


Green 是一款特別容易使用的應用程式，因此對初學者來說非常有趣。它提供所有優良 Bitcoin Wallet 的基本功能，包括 RBF (*Replace-by-fee*)、Tor 連線選項、連結您自己的節點、SPV (*簡易付款驗證*)、硬幣標籤和控制。


Blockstream Green 也支援 Liquid Network，這是 Blockstream 為 fast 開發的 Bitcoin Sidechain，Confidential Transactions 以外主要是 Blockchain。在本教程中，我們專注於 Bitcoin，但我也做了另一個教程，學習如何在 Green 上使用 Liquid ：


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig 選項 (2FA)


在 Green 上，您可以創造經典的 "*singlesig*"Hot Wallet。但您也可以選擇 "*2FA Multisig*"，在不使 Hot Wallet 的日常管理過於複雜的情況下，增強其安全性。


所以您要設定 2/2 Multisig Wallet，也就是每筆交易都需要兩個金鑰的簽章。第一個金鑰來自您的 12 或 24 個字的 Mnemonic 詞組，在本機以您手機上的 PIN 碼保護。您可以完全控制此密鑰。第二個金鑰由 Blockstream 伺服器持有，使用該金鑰進行簽章需要經過認證，認證可透過電子郵件、簡訊、電話收到的代碼來實現，或如本教程所述，透過認證應用程式（Authy、Google Authenticator 等）來實現。


為了確保您在 Blockstream 失敗時的自主性（例如，公司破產或持有第二個金鑰的伺服器被摧毀的情況下），您的 Multisig 應用了時間鎖機制。此機制會在大約一年之後將 2/2 Multisig 轉換成 1/2 Multisig（或精確地說是 51,840 個區塊，但此數值是可以修改的），之後您的 Wallet 就只需要您的本地金鑰就可以花費比特幣了。因此，如果您失去了 Blockstream 伺服器的存取權或 2FA 認證，您最多只需要等待一年，就可以在您的應用程式中自由使用您的比特幣，而不需要仰賴 Blockstream。


![GREEN 2FA MULTISIG](assets/fr/02.webp)


此方法可大幅提高 Hot Wallet 的安全性，同時讓您掌控比特幣，方便日常使用。但是，它需要定期刷新時間鎖來維持 2FA 的安全性。360 天的倒計時，在此期間您的資金受到 2FA 的保護，從您收到比特幣開始。如果在收到比特幣 360 天後，您還沒有使用這些資金進行交易，您的比特幣將只受到您的本地金鑰保護，而不受 2FA 保護。


此限制使得 2FA 選項更適合消費型 Wallet，因為定期交易會自動更新時間鎖。對於長期儲蓄的 Wallet，這可能會有問題，因為您需要考慮每年在時間鎖過期前對自己進行一次掃描交易。


這種安全方法的另一個缺點是，您必須使用少數人的腳本範本。這意味著，從保密性的角度來看，事情會變得更複雜：很少有人會和您使用相同類型的腳本，這使得外部觀察者更容易識別您的 Wallet 指紋。更重要的是，由於這些腳本的規模較大，因此會產生較高的交易成本。


如果您不想使用 2FA 選項，而只想在 Green 上設定一個 "*singlesig*"Green 上的 Wallet，我邀請您參閱此其他教學 ：


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 安裝和設定 Blockstream Green 軟體


第一步當然是下載 Green 應用程式。前往您的應用程式商店：



- [For Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)；
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


對於 Android 使用者，您也可以透過 `.apk` 檔案 [Blockstream 的 GitHub 上提供](https://github.com/Blockstream/green_android/releases) 安裝應用程式。


![GREEN 2FA MULTISIG](assets/fr/04.webp)


啟動應用程式，然後勾選「我接受條件...*」方塊。


![GREEN 2FA MULTISIG](assets/fr/05.webp)


當您第一次打開 Green 時，主螢幕會出現沒有設定的 Wallet。之後，如果您建立或匯入錢包，它們就會出現在這個 Interface 中。在繼續建立 Wallet 之前，我建議您調整應用程式設定以符合您的需求。按一下「應用程式設定」。


![GREEN 2FA MULTISIG](assets/fr/06.webp)


*Enhanced Privacy*" 選項只適用於 Android，可透過停用螢幕截圖和隱藏應用程式預覽來增強隱私。它也會在手機鎖定時自動鎖定應用程式存取權，讓您的資料更難曝光。


![GREEN 2FA MULTISIG](assets/fr/07.webp)


對於希望加強隱私權的人，應用程式提供透過 Tor 將您的流量根植於 Tor 網路的選項，這個網路會加密您所有的連線，讓您的活動難以被追蹤。雖然這個選項可能會稍微拖慢應用程式的運作速度，但為了保護您的隱私，我們強烈建議您使用這個選項，尤其是當您沒有使用自己的完整節點時。


![GREEN 2FA MULTISIG](assets/fr/08.webp)


對於擁有自己完整節點的用戶，Green Wallet 提供了通過 Electrum 伺服器與之連接的可能性，保證了對 Bitcoin 網絡資訊和交易分配的完全控制。


![GREEN 2FA MULTISIG](assets/fr/09.webp)


另一個替代功能是「*SPV Verification*」選項，它允許您直接驗證某些 Blockchain 資料，從而減少信任 Blockstream 預設節點的需要，不過這種方法無法提供 Full node 的所有保證。


![GREEN 2FA MULTISIG](assets/fr/10.webp)


根據您的需要調整這些設定後，按一下「*儲存*」按鈕並重新啟動應用程式。


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## 在 Blockstream Green 上建立 Bitcoin Wallet


現在您已準備好建立 Bitcoin Wallet。按一下「*開始*」按鈕。


![GREEN 2FA MULTISIG](assets/fr/12.webp)


您可以選擇建立本機 Software Wallet 或透過 Hardware Wallet 管理 Cold Wallet。在本教程中，我們將專注於建立 Hot Wallet，因此您需要選擇「*在此裝置*」選項。


![GREEN 2FA MULTISIG](assets/fr/13.webp)


然後，您可以選擇還原現有的 Bitcoin Wallet 或建立新的 Wallet。在本教程中，我們將建立一個新的 Wallet。但是，如果您需要從 Mnemonic 短語重新生成現有的 Bitcoin Wallet，例如在遺失舊手機之後，您需要選擇第二個選項。


![GREEN 2FA MULTISIG](assets/fr/14.webp)


然後您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。當您的手機發生問題時，這個詞組可讓您從任何相容的軟體恢復存取 Wallet。目前，選擇 24 字短語不會比 12 字短語更安全。因此，我建議您選擇 12 個字的 Mnemonic 詞組。


Green 接著會提供您 Mnemonic 的詞組。在繼續之前，請確定您沒有被監視。按一下「*Show recovery phrase*（顯示復原詞組*）」，將其顯示在螢幕上。


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**此 Mnemonic 可讓您完全無限制地存取您所有的 bitcoins**。任何持有此短語的人都可以竊取您的資金，即使沒有實體存取您的手機（在 Green 上的 2/2 Wallet 的情況下，受限於過期的 Timelock 或 2FA）。


它可讓您在手機遺失、遭竊或損壞時恢復本機鑰匙的存取權。因此，小心備份**在實體媒體（非數位）**上，並將其存放在安全的地方是非常重要的。您可以將它寫在一張紙上，或者為了增加安全性，如果是大型的 Wallet，我建議將它刻在不銹鋼支架上，以防止火災、水災或倒塌的風險（對於專門用來保護少量比特幣的 Hot Wallet，簡單的紙張備份可能就足夠了)。


*顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。


![GREEN 2FA MULTISIG](assets/fr/16.webp)


當您正確地將 Mnemonic 詞組記錄在實體媒體上後，請點選「*繼續*」。Green Wallet 接下來會要求您確認 Mnemonic 詞組中的一些單字，以確保您正確記錄了這些單字。請在空白處填入遺漏的單字。


![GREEN 2FA MULTISIG](assets/fr/17.webp)


選擇裝置的 PIN 碼，用於解鎖 Green Wallet。這是用來防止未經授權的實體存取。此 PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要擁有 12 或 24 字元的 Mnemonic 詞組，即可重新取得本機金鑰。


我們建議您選擇一個盡可能隨機的 6 位數 PIN 碼。請務必儲存此密碼，以免忘記，否則您將被迫從 Mnemonic 擷取 Wallet。然後您可以加入生物辨識攔截選項，避免每次使用時都要輸入 PIN 碼。一般而言，生物辨識技術的安全性遠不及 PIN 碼本身。因此，在預設情況下，我建議您不要設定這個解鎖選項。


![GREEN 2FA MULTISIG](assets/fr/18.webp)


再次輸入 PIN 碼以確認。


![GREEN 2FA MULTISIG](assets/fr/19.webp)


等待您的 Wallet 建立，然後按一下「*建立帳號*」按鈕。


![GREEN 2FA MULTISIG](assets/fr/20.webp)


然後，您可以選擇標準的單一簽章 Wallet 或受雙重認證 (2FA) 保護的 Wallet。在本教程中，我們將選擇第二個選項。


![GREEN 2FA MULTISIG](assets/fr/21.webp)


您的 Bitcoin Multisig Wallet 現在已使用 Green 應用程式建立！


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## 設定 2FA


按一下您的帳戶。


![GREEN 2FA MULTISIG](assets/fr/23.webp)


按一下 Green 按鈕「*加入 2FA* 增加您帳戶的安全性」。


![GREEN 2FA MULTISIG](assets/fr/24.webp)


接下來您就可以選擇認證方式來存取 2/2 Multisig 的第二把金鑰。在本教程中，我們會使用驗證應用程式。如果您不熟悉這類應用程式，建議您參考我們的 Authy 教學：


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

選擇「*驗證器應用程式*」。


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green 接著會顯示 QR 碼和復原金鑰。此密鑰可讓您在遺失 Authy 應用程式時恢復 2FA 的存取權。建議您將此金鑰安全備份，雖然如上所述，您仍可在時間鎖過期後恢復比特幣的存取權。


在您的認證應用程式中，新增一個新代碼，然後掃描 Green 提供的 QR 代碼。


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*顯然，您絕對不能在網路上分享此密鑰和 QR 碼，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。


按一下「*繼續*」按鈕。


![GREEN 2FA MULTISIG](assets/fr/27.webp)


輸入認證應用程式上的 6 位數動態代碼。


![GREEN 2FA MULTISIG](assets/fr/28.webp)


現在已啟用 2 因子驗證。


![GREEN 2FA MULTISIG](assets/fr/29.webp)


瀏覽此選單，您也可以設定時間鎖持續時間。收到比特幣後即開始倒數計時，一旦時間鎖過期，您的資金就只能使用本機金鑰使用，不需要 2FA。預設的期限設定為 12 個月，但對於儲蓄 Wallet 來說，選擇 15 個月以減少時間鎖更新的頻率，可能會比較合理。相反，對於消費型 Wallet，6 個月的時間鎖可能會比較好，因為它會隨著您的每日交易頻繁更新，而且較短的時間鎖可以減少 2FA 出現問題時的等待時間。您可以自行決定最適合您的時間鎖期限。


![GREEN 2FA MULTISIG](assets/fr/30.webp)


現在您可以退出此功能表。您的 Multisig Wallet 已準備就緒！


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## 在 Blockstream Green 上設定您的 Wallet


如果您想要個人化您的 Wallet，請按一下右上角的三個小圓點。


![GREEN 2FA MULTISIG](assets/fr/32.webp)


*Rename*" 選項可讓您自訂 Wallet 的名稱，如果您在同一個應用程式上管理多個錢包，這個選項特別有用。


![GREEN 2FA MULTISIG](assets/fr/33.webp)


*Unit*" 功能表可讓您變更 Wallet 的基本單位。例如，您可以選擇以梭希（satoshis）而非比特幣顯示。


![GREEN 2FA MULTISIG](assets/fr/34.webp)


*Settings*" 功能表可讓您存取 Bitcoin Wallet 的各種選項。


![GREEN 2FA MULTISIG](assets/fr/35.webp)


舉例來說，您可以在這裡找到您的擴充公開金鑰及其 *描述符*，如果您打算從這台 Wallet 設定 Wallet 為僅看管模式，這對您很有用。


![GREEN 2FA MULTISIG](assets/fr/36.webp)


您也可以變更 Wallet PIN 碼並啟動生物辨識連線。


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## 使用 Blockstream Green


現在您的 Bitcoin Wallet 已設定完成，您已準備好接收第一台 Sats！只要按一下「*接收*」按鈕即可。


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green 接著會在您的 Wallet 中顯示第一個空白的接收 Address。您可以掃描相關的 QR 代碼，或者直接複製 Address 來發送 bitcoins。這種類型的 Address 並沒有指定付款方要發送的金額。但是，您可以通過點擊右上角的三個小圓點，然後點擊 「*要求金額*」，並輸入所需的金額，就可以在 generate 中要求一個特定金額的 Address。


![GREEN 2FA MULTISIG](assets/fr/39.webp)


當交易在網路上廣播時，就會出現在您的 Wallet 中。


![GREEN 2FA MULTISIG](assets/fr/40.webp)


等到您收到足夠的確認後，才會認為交易是確實的。


![GREEN 2FA MULTISIG](assets/fr/41.webp)


有了 Wallet 中的 bitcoins，您現在還可以發送 bitcoins。點擊 「*發送*」。


![GREEN 2FA MULTISIG](assets/fr/42.webp)


在下一頁，輸入收件人的 Address。您可以手動輸入或掃描 QR 代碼。


![GREEN 2FA MULTISIG](assets/fr/43.webp)


選擇付款金額。


![GREEN 2FA MULTISIG](assets/fr/44.webp)


在畫面底部，您可以選擇此交易的收費率。您可以選擇遵循應用程式的建議或自訂費用。相對於其他待處理的交易，費用越高，您的交易處理速度就越快。有關收費市場資訊，請瀏覽 [Mempool.space](https://Mempool.space/) 中的「*交易費用*」部分。


![GREEN 2FA MULTISIG](assets/fr/45.webp)


點選「*下一步*」，進入交易摘要畫面。檢查 Address、金額和收費是否正確。


![GREEN 2FA MULTISIG](assets/fr/46.webp)


如果一切順利，請將螢幕下方的 Green 按鈕向右滑動，即可在 Bitcoin 網路上簽署和廣播交易。


![GREEN 2FA MULTISIG](assets/fr/47.webp)


這時您需要輸入驗證碼，以解鎖 Blockstream 持有的第二個 Multisig 密鑰。輸入驗證應用程式上顯示的 6 位數驗證碼。


![GREEN 2FA MULTISIG](assets/fr/48.webp)


您的交易現在會出現在您的 Bitcoin Wallet 面板上，等待確認。


![GREEN 2FA MULTISIG](assets/fr/49.webp)


現在您知道如何使用 Blockstream Green 的 2FA 選項輕鬆設定 2/2 Multisig Wallet！


如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您查看 Blockstream Green 手機應用程式設定 Liquid Wallet 的其他綜合教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a