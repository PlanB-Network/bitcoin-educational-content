---
name: Blockstream Green - Liquid
description: 在 Liquid Network Sidechain 上設定 Wallet
---
![cover](assets/cover.webp)


Bitcoin 通訊協定有其刻意的技術限制，這些限制有助於維持網路的分散性，並確保安全性分佈於所有使用者。然而，這些限制有時會讓使用者感到挫折，尤其是在同時進行大量交易造成擁塞時。有關 Bitcoin 可擴展性的爭論在社群中長期存在分歧，尤其是在區塊大小戰爭期間。自從這次事件之後，Bitcoin 社群廣泛認同可擴展性必須透過 off-chain 解決方案，在第二個 Layer 系統上來確保。這些解決方案包括側鏈 (sidechains)，相較於其他系統 (例如 Lightning Network)，側鏈仍然相對陌生且很少使用。


Sidechain 是獨立的 Blockchain，與主 Bitcoin Blockchain 平行運作。它使用 Bitcoin 作為記帳單位，這要歸功於一種稱為 「*雙向掛鉤*」的機制。此系統可將比特幣鎖定在主鏈上，以便在 Sidechain 上複製其價值，在 Sidechain 上，比特幣以原始比特幣支持的代幣形式流通。這些代幣通常會與鎖定在主鏈上的比特幣保持同等價值，這個過程可以逆轉，以收回 Bitcoin 上的資金。


側鏈的目的是提供額外的功能或技術改進，例如更快的交易速度、更低的費用或支援智慧合約。在不影響 Bitcoin Blockchain 的去中心化或安全性的情況下，這些創新往往無法直接在 Bitcoin Blockchain 上實現。因此，側鏈使測試和探索新解決方案成為可能，同時保留 Bitcoin 的完整性。然而，這些協定通常需要妥協，特別是在分散性和安全性方面，這取決於所選擇的治理模式和共識機制。


如今，最知名的 Sidechain 應該是 Liquid。在本教程中，我會先告訴您什麼是 Liquid，然後引導您如何透過 Blockstream Green 應用程式開始輕鬆使用 Liquid，讓您享受它的所有優點。


![LIQUID GREEN](assets/fr/01.webp)


## 什麼是 Liquid Network？


Liquid 是 Bitcoin 的聯邦 Sidechain 疊加，由 Blockstream 開發，以提高交易速度、保密性和功能性。它使用在聯盟上建立的雙邊錨定機制，將比特幣鎖定在主鏈上，並創造 Liquid 比特幣 (L-BTC) 作為回報，代幣在 Liquid 上流通，同時仍由原始比特幣支持。


![LIQUID GREEN](assets/fr/02.webp)


Liquid Network 依賴參與者聯盟，由 Bitcoin 生態系統中的認可實體組成，負責驗證區塊和管理雙邊掛鉤。除了 L-BTC，Liquid 還能發行其他數位資產，例如穩定幣和其他加密貨幣。


![LIQUID GREEN](assets/fr/03.webp)


## 介紹 Blockstream Green


Blockstream Green 是可在手機和桌面上使用的 Software Wallet。前身為 *Green Address*，此 Wallet 在 2016 年被收購後，成為 Blockstream 專案。


Green 是一款特別容易使用的應用程式，因此對初學者來說非常有趣。它提供所有優良 Bitcoin Wallet 的基本功能，包括 RBF (*Replace-by-fee*)、Tor 連線選項、連線您自己的節點、SPV (*簡易付款驗證*)、硬幣標籤和控制。


Blockstream Green 也支援 Liquid Network，這就是我們要在本教學中了解的。如果您想在其他應用程式中使用 Green，我建議您也看看其他這些教學：


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## 安裝和設定 Blockstream Green 應用程式


第一步當然是下載 Green 應用程式。前往您的應用程式商店：



- [For Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet)；
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![LIQUID GREEN](assets/fr/04.webp)


對於 Android 使用者，您也可以透過 `.apk` 檔案 [Blockstream 的 GitHub 上提供](https://github.com/Blockstream/green_android/releases) 安裝應用程式。


![LIQUID GREEN](assets/fr/05.webp)


啟動應用程式，然後勾選「我接受條件...*」方塊。


![LIQUID GREEN](assets/fr/06.webp)


當您第一次打開 Green 時，主螢幕會出現沒有設定的 Wallet。之後，如果您建立或匯入錢包，它們就會出現在這個 Interface 中。在繼續建立 Wallet 之前，我建議您調整應用程式設定以符合您的需求。點擊「應用程式設定」。


![LIQUID GREEN](assets/fr/07.webp)


*Enhanced Privacy*" 選項只適用於 Android，可透過停用螢幕截圖和隱藏應用程式預覽來增強隱私。它也會在手機鎖定時自動鎖定應用程式存取權，讓您的資料更難曝光。


![LIQUID GREEN](assets/fr/08.webp)


對於希望加強隱私權的人，應用程式提供透過 Tor 將您的流量根植於 Tor 網路的選項，這個網路會加密您所有的連線，讓您的活動難以被追蹤。雖然這個選項可能會稍微拖慢應用程式的運作速度，但為了保護您的隱私，我們強烈建議您使用這個選項，尤其是當您沒有使用自己的完整節點時。


![LIQUID GREEN](assets/fr/09.webp)


對於擁有自己完整節點的用戶，Green Wallet提供了通過Electrum服務器與之連接的選項，保證了對Bitcoin網絡信息和交易發佈的完全控制。但是這個功能是針對經典的 Bitcoin 錢包，所以如果您使用的是 Liquid 就不需要了。


![LIQUID GREEN](assets/fr/10.webp)


另一個替代功能是 "*SPV Verification*"選項，它允許您直接驗證某些 Blockchain 資料，從而減少信任 Blockstream 預設節點的需要，雖然這種方法無法提供 Full node 的所有保證。同樣地，這只會影響您的在線 Bitcoin 錢包，不會影響 Liquid。


![LIQUID GREEN](assets/fr/11.webp)


根據您的需要調整這些設定後，按一下「*儲存*」按鈕並重新啟動應用程式。


![LIQUID GREEN](assets/fr/12.webp)


## 在 Blockstream Green 上建立 Liquid Wallet


現在您可以建立 Liquid Wallet。按一下「*開始*」按鈕。


![LIQUID GREEN](assets/fr/13.webp)


您可以選擇建立本機 Software Wallet 或透過 Hardware Wallet 管理 Cold Wallet。在本教程中，我們著重於在 Liquid 上建立 Hot Wallet，因此您需要選擇「*在此裝置*」選項。您也可以使用相容的 Hardware Wallet，例如 Blockstream Jade，來保護您的 Liquid Wallet。


![LIQUID GREEN](assets/fr/14.webp)


然後，您可以選擇還原現有的 Bitcoin Wallet 或建立新的 Bitcoin。在本教程中，我們將建立一個新的 Wallet。但是，如果您需要從 Mnemonic 短語重新生成現有的 Liquid Wallet，例如在遺失 Hardware Wallet 之後，您需要選擇第二個選項。


![LIQUID GREEN](assets/fr/15.webp)


然後您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。當您的手機發生問題時，這個短語可讓您從任何相容的軟體恢復存取 Wallet。目前，選擇 24 字短語不會比 12 字短語更安全。因此，我建議您選擇 12 個字的 Mnemonic 詞組。


Green 接著會提供您 Mnemonic 的詞組。在繼續之前，請確定您沒有被監視。按一下「*Show recovery phrase*（顯示復原詞組*）」，將其顯示在螢幕上。


![LIQUID GREEN](assets/fr/16.webp)


**這台 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins ** 任何持有這台 Mnemonic 的人都可以竊取您的資金，即使沒有實體存取您的手機。


它可以在您的手機遺失、被盜或損壞時恢復對比特幣的存取。因此，仔細地**備份在實體媒體（而非數位媒體）**上，並將其存放在安全的地方是非常重要的。您可以把它寫在一張紙上，或者為了增加安全性，如果這是一個大型的 Wallet，我建議把它刻在一個不鏽鋼支架上，以保護它免受火災、水災或倒塌的風險（對於一個專為保護少量比特幣而設計的 Hot Wallet，簡單的紙張備份可能就足夠了）。


*顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Liquid 的 Testnet 上，並會在教學結束時刪除。*


![LIQUID GREEN](assets/fr/17.webp)


當您正確地將 Mnemonic 詞組記錄在實體媒體上後，請點選「*繼續*」。Green Wallet 接下來會要求您確認 Mnemonic 詞組中的一些單字，以確保您正確記錄了這些單字。請在空白處填入遺漏的單字。


![LIQUID GREEN](assets/fr/18.webp)


選擇裝置的 PIN 碼，用於解鎖 Green Wallet。這是用來防止未經授權的實體存取。此 PIN 碼不涉及 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要擁有 12 或 24 個字的 Mnemonic 詞組，就能重新取得您的比特幣。


我們建議您選擇一個盡可能隨機的 6 位數 PIN 碼。請務必儲存此密碼，以免忘記，否則您將被迫從 Mnemonic 取出您的 Wallet。然後您可以加入生物辨識攔截選項，避免每次使用時都要輸入 PIN 碼。一般而言，生物辨識技術的安全性遠低於 PIN 碼本身。因此，在預設情況下，我建議您不要設定這個解鎖選項。


![LIQUID GREEN](assets/fr/19.webp)


再次輸入 PIN 碼以確認。


![LIQUID GREEN](assets/fr/20.webp)


等待您的 Wallet 建立，然後按一下「*建立帳號*」按鈕。


![LIQUID GREEN](assets/fr/21.webp)


在「*Active*」方塊中，選擇「*Liquid Bitcoin*」。接著您可以選擇標準的單一簽章 Wallet（本教程中將會使用），或是受雙因素認證 (2FA) 保護的 Wallet。


![LIQUID GREEN](assets/fr/22.webp)


就這樣，您的 Liquid Wallet 已經使用 Green 應用程式建立！


![LIQUID GREEN](assets/fr/23.webp)


在您的 Liquid Wallet 收到您的第一個比特幣之前，**我強烈建議您進行一個空的恢復測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Green 應用程式上刪除您的 Wallet，而它還是空的。然後嘗試使用您的紙張備份在 Green 上還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果相符，您就可以放心，您的紙本備份是可靠的。要瞭解有關如何進行測試復原的更多資訊，請參閱此其他教程：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 設定您的 Liquid Wallet


如果您想要個人化您的 Wallet，請按一下右上角的三個小圓點。


![LIQUID GREEN](assets/fr/24.webp)


*Rename*" 選項可讓您自訂 Wallet 的名稱，如果您在同一個應用程式上管理多個錢包，這個選項特別有用。


![LIQUID GREEN](assets/fr/25.webp)


*Unit*" 功能表可讓您變更 Wallet 的基本單位。例如，您可以選擇以 Satoshis 而非 bitcoins 顯示。


![LIQUID GREEN](assets/fr/26.webp)


設定*」功能表可讓您存取 Bitcoin Wallet 的各種選項。


![LIQUID GREEN](assets/fr/27.webp)


例如，您可以在這裡找到您的 *描述符*，如果您打算從這個 Liquid Wallet 設定 Watch-only wallet，這可能會很方便。


![LIQUID GREEN](assets/fr/28.webp)


您也可以變更 Wallet PIN 碼並啟動生物辨識連線。


![LIQUID GREEN](assets/fr/29.webp)


## 使用您的 Liquid Wallet


現在您的 Liquid Wallet 已設定完成，您已準備好接收第一台 L-Sats！


如果您還沒有 L-BTC，您有幾個選擇。第一種是直接寄一些給您。如果有人想在 Liquid 上用比特幣支付您，只需給他們一個接收的 Address。另一個選擇是 Exchange 您的 bitcoins onchain 或在 Lightning Network 上的 L-BTC。要做到這一點，您可以使用 [一個橋樑，如 Boltz](https://boltz.Exchange/)。只要在網站上輸入您的 Liquid Address，然後透過 Lightning Network 或 onchain 付款即可。


![LIQUID GREEN](assets/fr/30.webp)


若要 generate Liquid Address，請按一下「*接收*」按鈕。


![LIQUID GREEN](assets/fr/31.webp)


Green 將會在您的 Wallet 中顯示第一個空白的接收 Address。您可以掃描相關的 QR 代碼，或直接複製 Address 來傳送 L-BTC。


![LIQUID GREEN](assets/fr/32.webp)


當交易在網路上廣播時，就會出現在您的 Wallet 中。


![LIQUID GREEN](assets/fr/33.webp)


等到您收到足夠的確認後，交易才算完成。在 Liquid 上，確認應該很快，因為每分鐘會發布一個區塊。


![LIQUID GREEN](assets/fr/34.webp)


使用 Liquid Wallet 中的 L-Sats，現在也可以傳送。按一下「*傳送*」。


![LIQUID GREEN](assets/fr/35.webp)


在下一頁，輸入收件人的 Liquid Address。您可以手動輸入或掃描 QR 代碼。


![LIQUID GREEN](assets/fr/36.webp)


選擇付款金額。


![LIQUID GREEN](assets/fr/37.webp)


點選「*下一步*」，進入交易摘要畫面。檢查 Address、金額和收費是否正確。


![LIQUID GREEN](assets/fr/38.webp)


如果一切順利，請將螢幕下方的 Green 按鈕向右滑動，即可在 Bitcoin 網路上簽署和廣播交易。


![LIQUID GREEN](assets/fr/39.webp)


您的交易現在會出現在您的 Bitcoin Wallet 面板上，等待確認。


![LIQUID GREEN](assets/fr/40.webp)


現在您知道如何透過 Blockstream Green 應用程式輕鬆使用 Liquid Sidechain！


如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您看看這篇有關 Blockstream Green 手機應用程式設定 onchain Bitcoin Hot Wallet 的其他全面教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143