---
name: 入口網站
description: 設定和使用 TwentyTwo-Devices Hardware Wallet 入口網站
---
![cover](assets/cover.webp)


Portal是由TwentyTwo Devices設計的Bitcoin Hardware Wallet，TwentyTwo Devices是一家專門為比特幣玩家製作開源硬體錢包的公司。TwentyTwo Devices由Alekos Filini創立，Alekos Filini是Magical Bitcoin專案（[以下命名為BDK](https://github.com/bitcoindevkit)）的創造者，曾在Blockstream和BHB Network工作，TwentyTwo Devices的目標是專注於用戶自主性、簡易性和安全性。


Portal 與市面上其他硬體錢包的不同之處在於其與智慧型手機的原生整合。它無需電纜或電池即可運作。它使用 NFC 技術為自己供電，並與任何相容的行動 Wallet 進行通訊。其引人入勝的設計符合人體工學。圓形部分放置在智慧型手機背面，露出一個螢幕，您可以在使用專用按鈕簽署之前，先檢查交易的詳細資訊。


![Image](assets/fr/01.webp)


Portal 完全開放原始碼，以 Rust 寫成的韌體為基礎，並使用 BDK (Bitcoin Dev Kit) 進行金鑰和交易管理。它的售價為 89 歐元 [在官方網站](https://store.twenty-two.xyz/products/portal-hardware-Wallet)。


在撰寫本文時，Portal 與 Nunchuk 和 Bitcoin Keeper 應用程式相容。在本教程中，我們將以 Nunchuk 來設定。


## 開箱


當您收到您的 Portal 時，請檢查盒子和封口的標籤是否完好。您會發現您的 Portal 是裝在一個密封袋中。


確保 Seal 完好無損，以確認袋子未被打開。包裝袋上以大字顯示的唯一號碼應與藍色 Seal 下方以黑色書寫的號碼、包裝盒標籤上的號碼以及首次啟動時螢幕上顯示的號碼相符。


![Image](assets/fr/02.webp)


## 雙節棍安裝


要管理託管在 Portal 上的 Wallet，我們要使用 Nunchuk 應用程式。從 [Google Play 商店](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App 商店](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) 或直接透過其 [檔案`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) 下載應用程式。


![Image](assets/fr/03.webp)


如果您是第一次使用 Nunchuk，應用程式會提示您建立帳號。在本教程中，您無需建立帳號。選擇 「*以訪客身份繼續*」即可在沒有帳號的情況下繼續使用。


![Image](assets/fr/04.webp)


## 入口網站設定


在 Nunchuk 主螢幕上，按一下螢幕上方的「*NFC*」標誌。


![Image](assets/fr/05.webp)


將 Portal 置於智慧型手機背面以啟用。


![Image](assets/fr/06.webp)


Nunchuk 會識別您的 Portal。然後按一下「*繼續*」。


![Image](assets/fr/07.webp)


若要建立新的 Wallet，請選擇「*generate seed on Portal*」，然後按一下「*繼續*」。


![Image](assets/fr/08.webp)


您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。這兩種選項所提供的安全性相似，因此您可以選擇最容易儲存的選項，也就是 12 個字。


![Image](assets/fr/09.webp)


接著會要求您選擇密碼。密碼將解鎖您的入口網站。因此可防止未經授權的實體存取。此密碼不參與您的 Wallet 密鑰的產生。因此，即使無法取得此密碼，只要擁有 12 或 24 個字的 Mnemonic 詞組，就能重新取得您的 bitcoins。建議您選擇一個盡可能隨機且足夠長的密碼。請確保將此密碼保存在與您的 Portal 不同的地方（如密碼管理器）。


![Image](assets/fr/10.webp)


您的入口網站將會顯示您的 12 個字的 Mnemonic 詞組。這個 Mnemonic 可以讓您完全不受限制地存取您所有的 bitcoins。任何擁有此短語的人都可以竊取您的資金，即使沒有實體存取您的入口網站。


如果您的 Portal 遺失、遭竊或破損，這 12 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。


您可以將它刻在一張紙上，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


如需更多關於儲存和管理 Mnemonic 詞組正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_***當然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。**_


請用力按下 Portal 上的按鈕，以進入下一個單字。請確定您將整隻手指放在按鍵上，並持續按壓幾秒鐘，這樣才能正確偵測到互動。


![Image](assets/fr/11.webp)


然後，您的 Portal 會確認您在 Nunchuk 中輸入的密碼。


![Image](assets/fr/12.webp)


現在您已完成設定您的 Portal 並建立 Mnemonic 詞組！


![Image](assets/fr/13.webp)


## Bitcoin Wallet 配置


在 Nunchuk 上按一下「*繼續*」，仍將您的 Portal 握在手機背面。


![Image](assets/fr/14.webp)


在本教程中，我將設定單一簽章 Wallet，因此選擇此選項。


![Image](assets/fr/15.webp)


使用預設帳號，即 Wallet 中的第一個帳號 (號碼 0)。然後 Nunchuk 會要求您確認 Portal 密碼以解除鎖定。


![Image](assets/fr/16.webp)


在 Portal 上，確認匯出您的 xpub 到 Nunchuk。這可讓您從智慧型手機管理 Wallet，而無需 Portal 即可花費 bitcoins。按下 按鈕確認。


請注意，由於本教程是在 Testnet 上執行，因此您的情況下所指示的衍生路徑會與我的不同。


![Image](assets/fr/17.webp)


命名您的 Wallet，例如「*Portal*」，然後按一下「*Continue*」。


![Image](assets/fr/18.webp)


然後 Nunchuk 會向您展示您的 Descriptor。做個備份是個好主意。雖然 Descriptor 不允許您花費 bitcoins，但它允許您在 Wallet 復原時從 Mnemonic 詞組追蹤金鑰的衍生路徑。請將它存放在安全的地方，因為雖然它的洩漏可能不會造成安全問題，但卻代表保密性的問題。


按一下「*完成*」。


![Image](assets/fr/19.webp)


現在您需要為您的 Bitcoin Wallet 設定 generate 公開金鑰。為此，請按一下「*建立新的 Wallet*」按鈕。


![Image](assets/fr/20.webp)


再次按一下「*建立新的 Wallet*」。然後選擇「*使用現有鑰匙建立新 Wallet*」選項。


![Image](assets/fr/21.webp)


為您的 Wallet 選擇一個名稱，然後按一下「*繼續*」。


![Image](assets/fr/22.webp)


選擇您的 Portal 作為這套新金鑰的簽署裝置，然後按一下「*繼續*」。


![Image](assets/fr/23.webp)


如果一切都令您滿意，請驗證創作。


![Image](assets/fr/24.webp)


然後您就可以儲存您的 Wallet 配置文件。此檔案只包含您的公開金鑰，這意味著即使有人存取此檔案，也無法竊取您的 bitcoins。但是，他們可以追蹤您所有的交易。因此，此檔案只會對您的隱私造成風險。在某些情況下，它對於恢復您的 Wallet 可能是不可或缺的。


![Image](assets/fr/25.webp)


僅此而已！


![Image](assets/fr/26.webp)


## 如何使用 Portal 接收比特幣？


若要接收 bitcoins，請選擇您的 Wallet。


![Image](assets/fr/27.webp)


使用已產生的 Address 之前，請在 Portal 畫面上檢查。若要執行此動作，請按一下「*接收*」。


![Image](assets/fr/28.webp)


按一下三個點，然後選擇「*Verify Address via PORTAL*」。然後輸入密碼。


![Image](assets/fr/29.webp)


將 Portal 放置在手機背面，然後按下按鈕確認。


![Image](assets/fr/30.webp)


請確認入口網站顯示的 Address 與您 Nunchuk 上的 Address 吻合，然後再按一次按鈕確認。如果地址相同，您可以將此 Address 交給付款人。


![Image](assets/fr/31.webp)


一旦付款人的交易被廣播，您就會看到它出現在您的 Wallet 上。


![Image](assets/fr/32.webp)


按一下「*檢視角落*」。


![Image](assets/fr/33.webp)


選擇您的新 UTXO。


![Image](assets/fr/34.webp)


點擊 「*標籤*」旁邊的 "*+*"，為您的 UTXO 添加標籤。這是一個很好的做法，因為它可以幫助您記住您的硬幣來源，並在將來消費時優化您的隱私。


![Image](assets/fr/35.webp)


選擇現有標籤或建立新標籤，然後按一下「*儲存*」。您也可以建立「*收藏*」，以更有條理的方式組織您的零件。


![Image](assets/fr/36.webp)


## 如何使用 Portal 傳送 bitcoins？


現在您的 Wallet 中已有比特幣，您也可以傳送它們。要這樣做，點擊您選擇的 Wallet。


![Image](assets/fr/37.webp)


按一下「*傳送*」按鈕。


![Image](assets/fr/38.webp)


選擇要傳送的金額，然後按一下「*繼續*」。


![Image](assets/fr/39.webp)


在您未來的交易中加入「*備註*」，提醒您交易的目的。


![Image](assets/fr/40.webp)


然後在提供的欄位中輸入收件人的 Address。您也可以按一下螢幕右上方的圖示，掃描編碼為 QR 碼的 Address。然後按一下「*建立交易*」按鈕。


![Image](assets/fr/41.webp)


檢查您的交易詳細資料，然後按一下您 Portal 旁邊的「*Sign*」按鈕，並輸入您的密碼。


![Image](assets/fr/42.webp)


將 Portal 放在手機背面。檢查收款人的 Address 和金額是否正確。如果是，請按下 按鈕繼續。


![Image](assets/fr/43.webp)


檢查交易費用是否正確，然後再按一次按鈕簽署交易。


![Image](assets/fr/44.webp)


您的交易已經簽署。您可以在 Nunchuk 上最後一次檢查其詳細資料，然後按一下「*廣播交易*」按鈕，即可在 Bitcoin 網路上廣播。


![Image](assets/fr/45.webp)


您的交易正在等待確認。


![Image](assets/fr/46.webp)


恭喜您，現在您已經掌握了使用 Portal 的訣竅！如果您覺得這篇教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝


要瞭解更多資訊，請參閱我們關於 HD 錢包如何運作的完整訓練課程：


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f