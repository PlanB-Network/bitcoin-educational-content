---
name: Satochip
description: 設定和使用 Satochip 智慧卡
---
![cover](assets/cover.webp)


Hardware Wallet 是專門管理和保護 Bitcoin Wallet 私密金鑰的電子裝置。與安裝在經常連接到網際網路的一般用途機器上的軟體錢包（或 Hot 錢包）不同，硬體錢包可以實體隔離私人金鑰，降低駭客入侵和竊取的風險。


Hardware Wallet 的主要目標是將裝置的功能最小化，以減少其攻擊面。較小的攻擊面也意味著較少的潛在攻擊媒介，也就是攻擊者可利用來存取比特幣的系統弱點較少。


建議使用 Hardware Wallet 來保護您的 bitcoins，尤其是當您持有大量的 bitcoins 時，不論是絕對值或是佔您總資產的比例。


硬體錢包與電腦或智慧型手機上的 Wallet 管理軟體結合使用。此軟體可管理交易的建立，但驗證這些交易所需的加密簽章則完全在 Hardware Wallet 中完成。這表示私密金鑰永遠不會暴露在潛在的脆弱環境中。


硬體錢包為使用者提供雙重保護：一方面，硬體錢包透過保持私密金鑰離線來保護您的比特幣免受遠端攻擊；另一方面，硬體錢包通常提供更好的物理保護，防止有人試圖提取金鑰。正是根據這兩個安全標準，我們可以對市場上的不同機型進行判斷和排序。


在本教程中，我建議探索其中一個解決方案：Satochip。


## Satochip 簡介


Satochip 是一種卡片形式的 Hardware Wallet，內含經過 *EAL6+* 認證的晶片，具有極高的安全性標準 (*NXP JCOP*)。它由一家比利時公司生產。


![SATOCHIP](assets/notext/01.webp)


此智慧卡的售價為 25 歐元，相較於市面上其他硬體錢包，價格非常實惠。晶片是一種安全元件，可確保對物理攻擊有很好的抵抗力。此外，它的程式碼是開放源碼 (*AGPLv3*)。

不過，由於其格式的關係，Satochip 並不如其他硬體提供那麼多的選項。很明顯，它沒有電池、沒有攝影機，也沒有 micro SD 讀卡機，因為它是一張卡片。在我看來，它最大的缺點是 Hardware Wallet 沒有螢幕，這使得它更容易受到某些類型的遠端攻擊。事實上，這迫使使用者盲目簽署，並相信他們在電腦螢幕上看到的東西。


儘管有其局限性，Satochip 仍因其低廉的價格而備受關注。這款 Wallet 除了可以用來加強消費型 Wallet 的安全性之外，還可以用來加強儲蓄型 Wallet 的安全性，而儲蓄型 Wallet 則由配備螢幕的 Hardware Wallet 所保護。對於那些持有少量比特幣而又不想投資一百歐元購買更複雜裝置的人來說，它也是一個很好的解決方案。此外，在 Multisig 配置中使用 Satochips，或者將來在帶有時間鎖的 Wallet 系統中使用 Satochips，都能提供有趣的優勢。


Satochip 公司還提供另外 2 種產品。有一種 Satodime，它是一種不記名卡，設計用於離線儲存比特幣，但不允許進行交易。它是一種紙質 Wallet，更加安全，例如可以用來送禮。最後是 Seedkeeper，它是一種 Mnemonic 短語管理器。它可以用來安全地保存我們的 seed，而不會直接記在一張紙上。


## 如何購買 Satochip？


Satochip 可在 [官方網站](https://satochip.io/product/satochip/) 上銷售。若要在實體商店購買，您也可以在 Satochip 網站上找到 [認證經銷商名單](https://satochip.io/resellers/)。


要與您的 Wallet 管理軟體互動，Satochip 提供兩種可能性：透過 NFC 通訊或透過智慧卡讀卡器。若要使用 NFC 選項，請確定您的機器與此技術相容，或取得外接式 NFC 讀卡機。Satochip 以 13.56 MHz 的標準頻率運作。否則，您也可以購買一個智能卡閱讀器。您可以在 Satochip 網站或其他地方找到。


![SATOCHIP](assets/notext/02.webp)


## 如何使用 Sparrow 設定 Satochip？


當您收到您的Satochip後，第一步是檢查包裝，以確保它未被打開。Satochip的包裝應包括一張密封貼紙。如果這張貼紙丟失或損壞，可能表明智能卡已被破壞，可能不是真卡。

![SATOCHIP](assets/notext/03.webp)

您會在裡面找到 Satochip。


![SATOCHIP](assets/notext/04.webp)


要管理 Wallet，在本教程中，我建議使用 Sparrow。如果您還沒有這個軟體，[請造訪官方網站下載](https://sparrowwallet.com/download/)。您也可以參考我們的 Sparrow Wallet 教學（即將推出）。


![SATOCHIP](assets/notext/05.webp)


將 Satochip 插入智能卡閱讀器或放在 NFC 閱讀器上，然後將閱讀器連接至 Sparrow 已開啟的電腦。


![SATOCHIP](assets/notext/06.webp)


開啟 Sparrow Wallet，確定您已正確連線至 Bitcoin 節點。要做到這一點，請檢查右下方的勾：如果您連線到公共節點，勾應該是黃色的；如果連線到 Bitcoin Core，勾應該是 Green；如果連線到 Electrum，勾應該是藍色的。


![SATOCHIP](assets/notext/07.webp)


在 Sparrow Wallet 上，按一下「*檔案*」標籤。


![SATOCHIP](assets/notext/08.webp)


然後在「*New Wallet*」功能表上。


![SATOCHIP](assets/notext/09.webp)


為您的 Wallet 選擇一個名稱，然後按一下「*建立 Wallet*」。


![SATOCHIP](assets/notext/10.webp)


按一下「*已連線的 Hardware Wallet*」按鈕。


![SATOCHIP](assets/notext/11.webp)


按一下「*掃描...*」按鈕。


![SATOCHIP](assets/notext/12.webp)


您的 Satochip 應該會出現。按一下「*Import Keystore*」。


![SATOCHIP](assets/notext/13.webp)


接下來，您需要設定一個 PIN 碼來解鎖您的 Satochip。選擇一個強大的密碼，介於 4 到 16 個字元之間。備份此密碼。


請注意，此密碼並非 passphrase。這表示即使沒有此密碼，您的 Mnemonic 短語仍可讓您在必要時將 Wallet 重新匯入軟體。此密碼僅用於確保存取 Satochip 本身的安全。它等同於其他硬體錢包上的 PIN 碼。


輸入密碼後，再次按一下「*匯入金鑰儲存庫*」按鈕。


![SATOCHIP](assets/notext/14.webp)


再次記下密碼，然後按一下「*初始化*」按鈕。


![SATOCHIP](assets/notext/15.webp)


然後您就會看到產生 Mnemonic 詞組的視窗。按一下「*generate New*」按鈕。


![SATOCHIP](assets/notext/16.webp)

將恢復短語寫在紙張或金屬媒介上，製作一個或多個實體副本。請注意，這個短語允許在沒有任何額外保護的情況下完全訪問您的比特幣。因此，如果有人發現它，他們可以立即竊取您的比特幣，即使沒有訪問您的 Satochip 或其 PIN 碼。因此，保護這些備份的安全是非常重要的。此外，這個短語允許您在遺失、損壞 Satochip 或忘記 PIN 碼的情況下重新獲得您的比特幣。

![SATOCHIP](assets/notext/17.webp)


您的 Bitcoin Wallet 已成功建立。


![SATOCHIP](assets/notext/18.webp)


再次按一下「*匯入金鑰儲存庫*」按鈕。


![SATOCHIP](assets/notext/19.webp)


您的 Wallet 已經建立。您的私人金鑰現在已儲存在 Satochip 的智慧卡上。按一下「*應用*」按鈕繼續。


![SATOCHIP](assets/notext/20.webp)


除了您的 Satochip 的 PIN 碼之外，建議您另外設定一個密碼，以確保 Sparrow Wallet 所管理的公開資訊的安全。此密碼將確保您存取 Sparrow Wallet 的安全性，有助於保護您的公開金鑰，地址和交易記錄，防止任何未經授權的存取。


![SATOCHIP](assets/notext/21.webp)


在兩個欄位中輸入密碼，然後按一下「*設定密碼*」按鈕。


![SATOCHIP](assets/notext/22.webp)


您的 Satochip 已在 Sparrow Wallet 上設定完成。


![SATOCHIP](assets/notext/23.webp)


現在您的 Wallet 已經建立，您可以中斷您的 Satochip 連線。請將它放在安全的地方！


## 如何使用 Satochip 接收比特幣？


進入 Wallet 之後，按一下「*接收*」標籤。


![SATOCHIP](assets/notext/24.webp)


Sparrow Wallet 會為您的 Wallet 產生一個 Address。通常，對於其他硬體錢包，建議點擊 "*Display Address*"直接在設備屏幕上驗證 Address。不幸的是，Satochip 無法使用此選項，但請確保您的其他錢包能使用此選項。


![SATOCHIP](assets/notext/25.webp)


您可以添加 「*標籤*」來描述將使用此 Address 保護的比特幣的來源。這是一個很好的做法，可以幫助您更好地管理您的 UTXO。


![SATOCHIP](assets/notext/26.webp)


如需更多關於標籤的資訊，我也建議您參考這份教學：


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然後您就可以使用這個 Address 來接收比特幣。


![SATOCHIP](assets/notext/27.webp)

## 如何使用 Satochip 傳送比特幣？

現在您已經用Satochip的安全Wallet收到了您的第一筆Sats，您也可以花掉它們了！將您的 Satochip 連接到您的電腦，啟動 Sparrow Wallet，然後到 「*發送*」標籤構建一個新的交易。


![SATOCHIP](assets/notext/28.webp)


如果您要執行硬幣控制，即具體選擇在交易中消耗哪些 UTXOs，請前往「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 "*Send Selected*"。您將被重新導向到 「*發送*」標籤的相同畫面，但您已經為交易選擇了UTXO。


![SATOCHIP](assets/notext/29.webp)


輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個地址。


![SATOCHIP](assets/notext/30.webp)


註記「*標籤*」以記住此支出的用途。


![SATOCHIP](assets/notext/31.webp)


選擇傳送到此 Address 的金額。


![SATOCHIP](assets/notext/32.webp)


根據當前市場調整交易費率。


![SATOCHIP](assets/notext/33.webp)


確保交易的所有參數正確無誤，然後按一下「*建立交易*」。


![SATOCHIP](assets/notext/34.webp)


如果一切都令您滿意，請按一下「*完成簽署交易*」。


![SATOCHIP](assets/notext/35.webp)


按一下「*簽署*」。


![SATOCHIP](assets/notext/36.webp)


再次按一下您的 Satochip 旁邊的「*簽署*」。


![SATOCHIP](assets/notext/37.webp)


輸入 Satochip 的 PIN 碼，然後再按一下「*簽署*」以簽署交易。


![SATOCHIP](assets/notext/38.webp)


您的交易現在已簽署。點選「*廣播交易*」，將交易廣播到 Bitcoin 網路。


![SATOCHIP](assets/notext/39.webp)


您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。


![SATOCHIP](assets/notext/40.webp)


恭喜您，現在您已經了解 Satochip 的使用方法！如果您覺得這篇教學對您有幫助，請在下方豎起大拇指。歡迎在您的社交網路分享這篇文章。非常感謝