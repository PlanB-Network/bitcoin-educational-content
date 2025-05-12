---
name: Tapsigner
description: 使用 Nunchuk 設定和使用 Tapsigner
---
![cover](assets/cover.webp)


Hardware Wallet 是專門管理 Bitcoin Wallet 私密金鑰並保障其安全性的電子裝置。與安裝在經常連接到網際網路的通用機器上的軟體錢包（或 Hot 錢包）不同，硬體錢包可以實體隔離私人金鑰，降低黑客入侵和竊取的風險。


Hardware Wallet 的主要目標是將裝置的功能最小化，以減少其攻擊面。較小的攻擊面也意味著較少的潛在攻擊媒介，也就是攻擊者可利用來存取比特幣的系統弱點較少。


建議使用 Hardware Wallet 來保護您的 bitcoins，尤其是當您持有大量的 bitcoins 時，不論是絕對值或是佔您總資產的比例。


硬體錢包與電腦或智慧型手機上的 Wallet 管理軟體結合使用。此軟體可管理交易的建立，但驗證這些交易所需的加密簽章則完全在 Hardware Wallet 中完成。這意味著私密金鑰永遠不會暴露在潛在的脆弱環境中。


硬體錢包為使用者提供雙重保護：一方面，硬體錢包透過保持私密金鑰離線來保護您的比特幣免受遠端攻擊；另一方面，硬體錢包通常提供更好的物理保護，防止有人試圖提取金鑰。正是根據這兩個安全標準，我們可以對市場上的不同機型進行判斷和排序。


在本教程中，我建議探索其中一個解決方案：Coinkite 的 Tapsigner。


## Tapsigner 簡介


Tapsigner 是 Coinkite 公司以 NFC 卡形式設計的 Hardware Wallet，該公司也以生產 Coldcards 而聞名。


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsigner 可根據 BIP32 儲存由主私人密碼匙和鏈碼組成的一對密碼匙，從而衍生出一棵加密密碼匙樹。將 Tapsigner 對準手機或 NFC 讀卡機，即可使用這些金鑰簽署交易。

這款 NFC 卡的售價為 19.99 美元，相較於市面上其他硬體錢包，價格非常實惠。不過，由於其格式的關係，Tapsigner 並不如其他裝置提供那麼多的選項。很明顯，它沒有電池、沒有攝影機，也沒有 micro SD 讀卡機，因為它是一張卡片。在我看來，它最大的缺點是 Hardware Wallet 上沒有螢幕，這使得它更容易受到某些類型的遠端攻擊。事實上，這迫使使用者盲目簽署，並相信他們在電腦螢幕上看到的東西。


儘管有其限制，但 Tapsigner 因其低廉的價格而令人感興趣。這款 Wallet 除了可以用來加強消費型 Wallet 的安全性之外，還可以用來加強由配備螢幕的 Hardware Wallet 所保護的儲蓄型 Wallet 的安全性。對於那些持有少量比特幣而又不想投資一百歐元購買更複雜裝置的人來說，它也是一個很好的解決方案。此外，在 Multisig 配置中使用 Tapsigner，或者將來在帶有時間鎖的 Wallet 系統中使用 Tapsigner，都可以帶來有趣的好處。


## 如何購買 Tapsigner？


Tapsigner 可 [在 Coinkite 官方網站](https://store.coinkite.com/store/category/tapsigner) 購買。若要在實體商店購買，您也可以在網站上找到 [認證經銷商名單](https://coinkite.com/resellers)。


您還需要一部與 NFC 通訊相容的手機，或一個 USB 裝置，以 13.56 MHz 的標準頻率讀取 NFC 卡。


## 如何使用 Nunchuk 初始化 Tapsigner？


收到 Tapsigner 後，第一步是檢查包裝，確保沒有被打開。如果包裝破損，可能表明卡片已被盜用，可能不是真卡。CoinKite 在交付您的 Tapsigner 時會附上一個可以阻擋無線電波的盒子。請確保包裝內有此保護套。


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


為了管理 Wallet，我們將使用 **Nunchuk Wallet** 行動應用程式。請確保您的智慧型手機與 NFC 相容，然後從 [Google Play 商店](https://play.google.com/store/apps/details?id=io.nunchuk.android)、[App 商店](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) 或直接透過 [`.apk`檔](https://github.com/nunchuk-io/nunchuk-android/releases) 下載 Nunchuk。


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

如果您是第一次使用 Nunchuk，應用程式會提示您建立帳號。在本教程中，您無需建立帳號。因此，請選擇 「*以訪客身份繼續*」，即可在沒有帳號的情況下繼續使用。

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


然後按一下「*無輔助 Wallet*」。


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


接下來，按一下「*我自己來探索*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


進入 Nunchuk 後，按一下「*Keys*」標籤旁邊的「*+*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


選擇「*新增 NFC 鑰匙*」。


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


然後按一下「*新增 TAPSIGNER*」。


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


按一下「*繼續*」，然後將您的 Tapsigner NFC 卡放在智慧型手機上。


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


如果您的 Tapsigner 是新的，Nunchuk 會提供初始化。點擊 「*是*」。


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


現在您需要選擇 generate 主鏈代碼的方式。


Tapsigner 使用 BIP32 標準。這意味著確保您比特幣安全的加密金鑰的推導不像 BIP39 錢包那樣依賴 Mnemonic 詞組，而是直接依賴主私密金鑰和主鏈代碼。這 2 個 Elements 會經由 HMAC 函式，以確定性且有層次地推導出您的其他 Wallet。


主私密金鑰由集成到 Tapsigner 中的 TRNG（*真實隨機數生成器*）直接生成。另一方面，主鏈碼必須從外部提供。在此步驟，您可以選擇：按一下「*自動*」讓 Nunchuk 自動 generate 或選擇「*進階*」並在提供的欄位中輸入您自己的 generate。


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


接下來，您需要選擇一個 PIN 碼。在 "*Starting PIN*"區域中，輸入寫在 Tapsigner 背面的 PIN 碼。


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


選擇一個 PIN 碼，以確保對 Tapsigner 的實體存取。此 PIN 碼在 Wallet 復原過程中不起任何作用。它的唯一功能是解鎖您的 Tapsigner 以簽署交易。請務必保存此 PIN 碼，以免忘記。點擊 「*繼續*」繼續。


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

現在將您的 Tapsigner 卡放在手機背面以進行初始化。

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


然後 Nunchuk 會為您的 Wallet 提供 generate 復原檔案，讓您在遺失 NFC 卡時重新取得比特幣。這個檔案是用寫在 Tapsigner 背面的備份碼加密的。要恢復您的比特幣，您絕對需要這個文件以及解密碼。因此，將這個代碼複製成紙質文件是很重要的，因為如果您丟失了您的 NFC 卡，這個代碼的存取權也會丟失，因為它目前只寫在卡上。請務必同時為您的加密復原檔案建立多份備份。


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


為您的 Wallet 選擇一個名稱。


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


您的 Wallet 的基礎現在已經建立好了。若要隨時驗證 Tapsigner 的真實性，您可以按一下「*執行健康檢查*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


輸入您的 PIN 碼。


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


然後將您的卡片放在手機背面。


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## 如何在 Tapsigner 上建立 Wallet？


回到 Nunchuk 首頁，您可以看到您的 Tapsigner 已註冊在可用的簽章裝置中。


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


現在您需要為您的 Bitcoin Wallet 設定 generate 鑰匙。為此，請按一下「*錢包*」標籤右邊的「*+*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


按一下「*建立新的 Wallet*」。


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


然後選擇「*使用現有鑰匙建立新的 Wallet*」選項。


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


為您的 Wallet 選擇一個名稱，然後按一下「*繼續*」。


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


選擇您的 Tapsigner 作為這套新金鑰的簽署裝置，然後按一下「*繼續*」。


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


如果一切都令您滿意，請確認建立。


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

然後您就可以儲存 Wallet 的設定檔。此檔案只包含您的公開金鑰，這意味著即使有人存取此檔案，也無法竊取您的比特幣。但是，他們可以跟蹤您的所有交易。因此，此檔案只會對您的隱私造成風險。在某些情況下，它對於恢復您的 Wallet 可能是必不可少的。

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


您的 Wallet 已成功建立！


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


不使用 Tapsigner 時，請記得將它存放在 Coinkite 提供的保護套中，它可以阻擋無線電波，防止未經授權的讀取。


## 如何在 Tapsigner 上接收比特幣？


若要接收 bitcoins，請點選您的 Wallet。


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


然後用生成的 Address 接收比特幣。如果您之前已經在這個 Wallet 上接收過 bitcoins，您需要點擊「*接收*」按鈕來 generate 一個新的空白接收 Address。


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


一旦發送人的交易被廣播，您就會看到它出現在您的 Wallet 上。


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


按一下「*檢視硬幣*」。


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


選擇您的新 UTXO。


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


點擊 「*標籤*」旁邊的 "*+*"，為您的 UTXO 添加標籤。這是一個很好的做法，因為它可以幫助您記住硬幣的來源，並優化您的隱私，方便日後的消費。


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


選擇現有標籤或建立新標籤，然後按一下「*儲存*」。您也可以選擇建立「*收藏*」，以更有條理的方式整理您的錢幣。


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## 如何使用 Tapsigner 傳送 bitcoins？


現在您的 Wallet 中已有比特幣，您也可以傳送它們。要做到這一點，點擊您選擇的 Wallet。


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


按一下「*傳送*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


選擇要傳送的金額，然後按一下「*繼續*」。


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


在您未來的交易中加入「*註*」，以記住其目的。


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

接下來，在指定欄位手動輸入收件人的 Address。

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


您也可以按一下位於螢幕右上方的圖示，掃描編碼 Address 的 QR 代碼。


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


按一下「*建立交易*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


驗證交易的詳細資訊，然後點擊您的 Tapsigner 旁邊的 "*Sign*"按鈕。


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


輸入您的 PIN 碼以解除鎖定。


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


然後將 Tapsigner 放在智慧型手機背面。


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


您的交易現在已簽署。最後一次檢查是否一切正確，然後按一下「*廣播交易*」，在 Bitcoin 網路上廣播。


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


您的交易正在等待確認。


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## 如果遺失了 Tapsigner，該如何恢復 Wallet？


如果您遺失了 Tapsigner，您可以使用卡片背面的代碼找回您的 Wallet。因此，請務必將此密碼與 Tapsigner 分開保存，因為如果卡片遺失，此密碼的存取權也會遺失。您也需要 Wallet 的加密備份。


在復原時，我們會使用 Nunchuk 應用程式，但請記住，這意味著暫時將您的資金固定在 Hot Wallet 中。如果您的 Tapsigner 保證的金額很大，請考慮改用新的 Coldcard 來遵循相同的復原程序。


開啟 Nunchuk 應用程式，然後按一下「*Keys*」標籤旁邊的「*+*」按鈕。


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


選擇「*新增 NFC 鑰匙*」。


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


選擇選項 "*Recover TAPSIGNER key from backup*"。


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


然後您會被重新導向至裝置的檔案總管。找到並選擇 Wallet 的加密備份檔案。通常，此檔案的名稱是以「backup...」開頭。


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


輸入用於解密備份檔案的密碼。此密碼與 Tapsigner 背面最初註明的密碼相符。


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

然後為您的復原 Wallet 選擇一個名稱。

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


您現在已經可以重新使用您的 bitcoins。您的 Wallet 現在是以 Hot Wallet 的方式管理，可在 Nunchuk 應用程式的「*金鑰*」標籤中看到。接下來，您需要在 "*Wallets*"區段中建立一組新的加密金鑰，方法是將此金鑰與之相關聯。要做到這一點，您可以按照本教學的 "*如何在 Tapsigner 上創建 Wallet？


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


如果您丟失了您的 Tapsigner，我強烈建議您立即將您的比特幣轉移到您擁有的另一個 Wallet，最好有一個 Hardware Wallet 保護。事實上，您丟失的 Tapsigner 有可能落入歹徒手中。因此，重要的是清空您剛剛找回的 Wallet，並停止使用它。


恭喜您，現在您已經可以快速使用 Tapsigner 了！如果您覺得這篇教學對您有幫助，請在下方留下大拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。非常感謝