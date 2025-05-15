---
name: Ledger 軟體
description: 設定和使用 Ledger Flex
---
![cover](assets/cover.webp)


Hardware Wallet 是專門管理和保護 Bitcoin Wallet 私密金鑰的電子裝置。與安裝在經常連接到網際網路的通用機器上的軟體錢包（或 Hot 錢包）不同，硬體錢包可以實體隔離私密金鑰，降低駭客入侵和竊取的風險。


Hardware Wallet 的主要目標是將裝置的功能最小化，以減少其攻擊面。較少的攻擊面也意味著較少的潛在攻擊媒介，也就是攻擊者可利用來存取比特幣的系統弱點較少。


建議使用 Hardware Wallet 來保護您的比特幣，尤其是當您持有大量比特幣時，不論是絕對值還是佔您總資產的比例。


硬體錢包與電腦或智慧型手機上的 Wallet 管理軟體結合使用。此軟體管理交易的建立，但驗證這些交易所需的加密簽章僅在 Hardware Wallet 內完成。這意味著私密金鑰永遠不會暴露在潛在的脆弱環境中。


硬體錢包為使用者提供雙重保護：一方面，硬體錢包透過保持私密金鑰離線來保護您的比特幣免受遠端攻擊；另一方面，硬體錢包通常提供更好的物理保護，防止有人試圖提取金鑰。正是根據這兩個安全標準，我們可以對市場上的不同機型進行判斷和排序。


在本教程中，我建議探索其中一個解決方案：**Ledger Flex**。


![LEDGER FLEX](assets/notext/01.webp)


## Ledger Flex 簡介


Ledger Flex 是法國 Ledger 公司生產的 Hardware Wallet，市售價格為 249 歐元。


![LEDGER FLEX](assets/notext/02.webp)


它採用大型 E Ink 觸控螢幕，這是一種黑白顯示技術。這與電子閱讀器的技術相同。E Ink 螢幕即使在明亮的陽光下，也能提供清晰易讀的顯示效果，而且耗能極低，螢幕靜止時甚至完全不耗能。它的工作原理是使用含有黑色和白色顏料微粒的微膠囊。當施加電荷時，黑色或白色顏料顆粒會移動到螢幕表面，進而形成文字或影像。

Ledger Flex 配備 CC EAL6+ 認證的「安全元件」晶片，提供您進階的保護，防止硬體受到物理攻擊。螢幕直接由此晶片控制。常被批評的一點是，此晶片的程式碼並未開放原始碼，需要對此元件的完整性有一定程度的信任。不過，這個元件是經過獨立專家審核的。


在使用方面，Ledger Flex 提供多種連線選項：藍牙、USB-C 和 NFC。大螢幕可讓您輕鬆驗證交易細節。Ledger 還能快速採用 Bitcoin 的新功能，例如 Miniscript，從競爭對手中脫穎而出。


測試之後，我對產品的品質印象深刻。使用者體驗極佳，裝置也很直覺。它是一款出色的 Hardware Wallet。不過，在我看來它有 2 大缺點：無法驗證晶片的程式碼，當然還有它的價格，明顯高於競爭對手。相比之下，Foundation 最先進的機型售價為 199 美元，Coinkite 的機型售價為 219.99 美元，而同樣配備大型觸控螢幕的最新 Trezor 則售價為 169 歐元。


## 如何購買 Ledger Flex？


Ledger Flex 可在 [官方網站](https://shop.Ledger.com/pages/Ledger-flex) 購買。若要在實體商店購買，您也可以在 Ledger 網站上找到 [認證經銷商名單](https://www.Ledger.com/reseller)。


## 先決條件


收到 Ledger Flex 後，第一步是檢查包裝，確保包裝未被打開。


![LEDGER FLEX](assets/notext/03.webp)


Ledger 的包裝應包括 2 條密封條。如果這些封條遺失或損壞，可能表示 Hardware Wallet 已經損壞，可能不是真品。


![LEDGER FLEX](assets/notext/04.webp)


打開之後，您應該會發現盒子裡有以下物品：


- Ledger Flex；
- USB-C 連接線；
- 使用者手冊；
- 寫下您的 Mnemonic 詞組的卡片。


![LEDGER FLEX](assets/notext/05.webp)


在本教程中，您將需要 2 個軟體：Ledger Live 用來初始化 Ledger Flex，Sparrow Wallet 用來管理您的 Bitcoin Wallet。請至其官方網站下載 [Ledger Live](https://www.Ledger.com/Ledger-live) 及 [Sparrow Wallet](https://sparrowwallet.com/download/) 。


![LEDGER FLEX](assets/notext/06.webp)

我們即將提供教程，說明如何驗證您所下載軟體的真實性和完整性。我強烈建議您在此針對 Ledger Live 和 Sparrow 進行驗證。

## 如何使用 Ledger Live 初始化 Ledger Flex？


按下右側按鈕幾秒鐘，即可開啟 Ledger Flex。


![LEDGER FLEX](assets/notext/07.webp)


捲動不同的介紹頁面。


![LEDGER FLEX](assets/notext/08.webp)


選擇「*設定不使用 Ledger Live*」選項，然後按一下「*跳過 Ledger Live*」按鈕。


![LEDGER FLEX](assets/notext/09.webp)


接下來會要求您為 Ledger 選擇一個名稱。按一下「*設定名稱*」，然後輸入您選擇的名稱。


![LEDGER FLEX](assets/notext/10.webp)


選擇裝置的 PIN 碼，用於解鎖 Ledger。因此，這是用來防止未經授權的實體存取。此 PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法存取此 PIN 碼，擁有您的 24 字 Mnemonic 詞組也可讓您重新存取您的比特幣。


建議選擇 8 位數的 PIN 碼，盡可能隨機。此外，請確保將此密碼保存在與 Ledger Flex 不同的地方（例如，密碼管理器）。


![LEDGER FLEX](assets/notext/11.webp)


再次輸入 PIN 碼以確認。


![LEDGER FLEX](assets/notext/12.webp)


接著會提示您選擇復原現有的 Wallet 或建立新的 Wallet。在本教程中，我們將介紹從頭建立新的 Wallet，因此請選擇「*設定為新的 Ledger*」選項，以 generate 建立新的 Mnemonic 樂句。


![LEDGER FLEX](assets/notext/13.webp)


您的 Flex 會提供如何管理恢復用語的指示。


**這個 Mnemonic 詞組可以完全且不受限制地存取您所有的 bitcoins**。任何擁有此短語的人都可以盜取您的資金，即使沒有實體存取您的 Ledger。如果您的 Ledger Flex 遺失、遭竊或損壞，24 字短語可讓您恢復存取比特幣的權利。因此，小心保存並將其存放在安全的地方是非常重要的。


您可以將它寫在 Ledger 隨附的硬紙板紙上，或者為了增加安全性，我建議您將它刻在不銹鋼介質上，以防止火災、水災或倒塌的風險。


您可以輕觸螢幕瀏覽這些說明並跳頁。


![LEDGER FLEX](assets/notext/14.webp)

Ledger 會使用隨機數字產生器建立您的 Mnemonic 詞組。請確定在此操作過程中沒有人觀察您。將 Ledger 提供的短語寫在您選擇的實體媒體上。根據您的安全策略，您可以考慮製作幾份完整的詞組實體複本 (但最重要的是，請勿分割)。重要的是，要保持單字的編號和順序。

****顯然，您絕對不應該在網路上分享這些文字，這與我在本教學中所做的相反。此範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。***


![LEDGER FLEX](assets/notext/15.webp)


若要移至下一組單字，請按一下「*下一步*」按鈕。記下所有單字後，按一下「*Done*」按鈕進入下一步。


![LEDGER FLEX](assets/notext/16.webp)


按一下「*開始確認*」按鈕，然後按順序選擇 Mnemonic 詞組中的單字，確認您已正確記下這些單字。繼續此程序，直到第 24 個單字為止。


![LEDGER FLEX](assets/notext/17.webp)


如果您要確認的詞組與 Flex 在上一步提供給您的完全相同，您就可以繼續。如果不是，這表示您的 Mnemonic 詞組的實體備份不正確，您需要重新啟動程序。


![LEDGER FLEX](assets/notext/18.webp)


您的 seed 已在 Ledger Flex 上正確建立。在繼續從這個 seed 建立新的 Bitcoin Wallet 之前，讓我們一起探索裝置設定。


## 如何修改 Ledger 的設定？


若要鎖定或解除鎖定 Ledger，請按側邊按鈕。接著會要求您輸入上一步設定的 PIN 碼。


![LEDGER FLEX](assets/notext/19.webp)


若要存取設定，請按一下裝置左下方的齒輪符號。


![LEDGER FLEX](assets/notext/20.webp)


*Name*" 功能表可讓您變更 Ledger 的名稱。


![LEDGER FLEX](assets/notext/21.webp)


在「*關於本 Ledger*」中，您可以找到有關您的 Flex 的資訊。


![LEDGER FLEX](assets/notext/22.webp)


在「*鎖定畫面*」功能表中，您可以選擇「*自訂鎖定畫面圖片*」來變更鎖定畫面上顯示的圖片。由於裝置採用 E Ink 螢幕技術，因此可以讓螢幕持續開啟而不消耗電池。E Ink 螢幕不會消耗能源來維持靜態影像。不過，在顯示變化時，它們會消耗能源。

子功能表「*自動鎖定*」可讓您設定並啟動 Ledger 在一段確定的非活動時間後自動鎖定。

![LEDGER FLEX](assets/notext/23.webp)


在「*聲音*」功能表中，您可以開啟或關閉 Flex 的聲音。在「語言」功能表中，您可以變更顯示語言。


![LEDGER FLEX](assets/notext/24.webp)


按一下右箭頭，即可存取其他設定。「*變更 PIN*」可讓您變更 PIN 碼。


![LEDGER FLEX](assets/notext/25.webp)


*藍牙*「和 」*NFC*"功能表可讓您管理這些通訊。


![LEDGER FLEX](assets/notext/26.webp)


在「*電池*」中，您可以設定 Ledger 自動關機。


![LEDGER FLEX](assets/notext/27.webp)


在「*進階*」部分，您可以存取更複雜的安全設定。建議保持啟動「*PIN 洗碼*」選項，以加強安全性。您也可以在此功能表中設定 BIP39 passphrase。


![LEDGER FLEX](assets/notext/28.webp)


passphrase 是可選的密碼，結合復原短語，可為您的 Wallet 提供額外的 Layer 安全性。


目前，您的 Wallet 是由 24 個字組成的 Mnemonic 詞組所產生。此恢復詞組非常重要，可讓您在遺失時恢復 Wallet 的所有鑰匙。但是，它構成單一點故障 (SPOF)。如果它受到損害，比特幣就會有危險。這就是 passphrase 的用處。這是一個可選的密碼，您可以任意選擇，它可以添加到 Mnemonic 短語中，以加強 Wallet 的安全性。


passphrase 不應該與 PIN 碼混淆。它在密碼鑰匙的產生過程中扮演一個角色。它與 Mnemonic 詞組配合使用，修改生成密碼匙的 seed。因此，即使有人取得您的 24 字短語，如果沒有 passphrase，他們也無法存取您的資金。使用 passphrase 基本上會產生一個新的 Wallet，並具有不同的金鑰。修改（即使是輕微修改）passphrase 會產生不同的 Wallet generate。


passphrase 是一個非常強大的工具，可以增強您比特幣的安全性。但是，在實施之前，了解它的工作原理是非常重要的，以避免丟失您的 Wallet 的訪問權限。我會在另一個專門的教學中解說如何使用 passphrase。


![LEDGER FLEX](assets/notext/29.webp)


passphrase 是一個非常強大的工具，可以加強您比特幣的安全性。但是，在實施之前，了解它的工作原理是至關重要的，以避免丟失 Wallet 的訪問權限。這就是為什麼我要在專門的教學中解釋一切的原因：


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

最後，最後一個設定頁面允許您重設 Ledger。只有在您確定 Ledger 不含任何保護比特幣的鑰匙時，才可進行此重設，因為您可能會永久失去存取資金的權利。

![LEDGER FLEX](assets/notext/30.webp)


## 如何安裝 Bitcoin 應用程式？


首先在電腦上啟動 Ledger Live 軟體，然後連接並解鎖您的 Ledger Flex。


![LEDGER FLEX](assets/notext/31.webp)


在 Ledger Live 中，進入「*我的 Ledger*」功能表。您會被要求授權存取您的 Flex。


![LEDGER FLEX](assets/notext/32.webp)


按一下「*允許*」按鈕，驗證 Ledger 的存取權限。


![LEDGER FLEX](assets/notext/33.webp)


首先，如果您 Ledger Flex 的韌體不是最新版本，Ledger Live 會自動提供更新。如果適用，請點選「*更新韌體*」，然後點選「*安裝更新*」開始安裝。


![LEDGER FLEX](assets/notext/34.webp)


在 Ledger 上按一下「*安裝*」按鈕，然後在安裝過程中等待。


![LEDGER FLEX](assets/notext/35.webp)


您的 Ledger Flex 韌體已更新。


![LEDGER FLEX](assets/notext/36.webp)


如果您願意，可以變更 Ledger Flex 的鎖定螢幕桌布。若要執行此操作，請按一下「*新增 >*」。


![LEDGER FLEX](assets/notext/37.webp)


按一下「*從電腦上載*」按鈕，然後從相片中選擇您的壁紙。


![LEDGER FLEX](assets/notext/38.webp)


您可以裁剪圖片。


![LEDGER FLEX](assets/notext/39.webp)


從不同選項中選擇對比度，然後按一下「*確認對比度*」。


![LEDGER FLEX](assets/notext/40.webp)


在您的 Flex 上，按一下「*載入圖片*」按鈕。


![LEDGER FLEX](assets/notext/41.webp)


如果您對圖片感到滿意，請按一下「*保留*」，將其設定為您的鎖定螢幕桌布。


![LEDGER FLEX](assets/notext/42.webp)


最後，我們要新增 Bitcoin 應用程式。在 Ledger Live 上，點選「*Bitcoin (BTC)*」旁邊的「*Install*」按鈕即可。


![LEDGER FLEX](assets/notext/43.webp)


應用程式會安裝在您的 Flex 上。


![LEDGER FLEX](assets/notext/44.webp)


從現在開始，您不再需要 Ledger Live 軟體來定期管理您的 Wallet。當有新版本推出時，您可以偶爾回到這裡更新韌體。至於其他的事情，我們會使用 Sparrow Wallet，它是一個更全面的工具，可以有效率地管理 Bitcoin Wallet。


## 如何使用 Sparrow 設定新的 Bitcoin Wallet？

開啟 Sparrow Wallet，跳過介紹頁面進入主畫面。觀察位於螢幕右下方的開關，檢查您是否已正確連線至節點。

![LEDGER FLEX](assets/notext/45.webp)


我強烈建議您使用自己的 Bitcoin 節點。在本教程中，我使用的是公共節點（黃色），因為我使用的是 Testnet，但如果要正常使用，最好選擇本地的 Bitcoin 核心（Green）或連接到遠端節點（藍色）的 Electrum 伺服器。


按一下「*檔案*」功能表，然後按一下「*新增 Wallet*」。


![LEDGER FLEX](assets/notext/46.webp)


選擇此 Wallet 的名稱，然後按一下「*建立 Wallet*」。


![LEDGER FLEX](assets/notext/47.webp)


在 "*Script Type*"下拉菜單中，選擇用來保護比特幣的腳本類型。我建議選擇 "*Taproot*「，如果沒有，則選擇 」*Native SegWit*"。


![LEDGER FLEX](assets/notext/48.webp)


按一下「*已連線的 Hardware Wallet*」按鈕。


![LEDGER FLEX](assets/notext/49.webp)


將 Ledger Flex 連接到電腦，使用 PIN 碼解除鎖定，然後開啟「*Bitcoin*」應用程式。在本教程中，我使用的是 "*Bitcoin Testnet*"應用程式，但 Mainnet 的步驟仍相同。


![LEDGER FLEX](assets/notext/50.webp)


在 Sparrow 上，按一下「*掃描*」按鈕。


![LEDGER FLEX](assets/notext/51.webp)


然後按一下「*匯入金鑰儲存庫*」。


![LEDGER FLEX](assets/notext/52.webp)


現在您可以看到 Wallet 的詳細資訊，包括第一個帳號的擴充公開金鑰。點選「*Apply*」按鈕，完成 Wallet 的建立。


![LEDGER FLEX](assets/notext/53.webp)


選擇一個強大的密碼以確保存取 Sparrow Wallet 的安全性。此密碼將確保您在 Sparrow 上存取 Wallet 資料的安全性，有助於保護您的公開金鑰，地址，標籤和交易記錄，防止任何未經授權的存取。


我建議您將此密碼儲存在密碼管理器中，以免忘記。


![LEDGER FLEX](assets/notext/54.webp)


這樣，您的 Wallet 就完成了！


![LEDGER FLEX](assets/notext/55.webp)

在您的 Wallet 收到您的第一枚比特幣之前，我強烈建議您執行一次乾式恢復測試。記下一個參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重設您的 Ledger Flex。之後，嘗試使用您的紙張備份在 Ledger 上還原您的 Wallet。檢查還原後生成的 xpub 是否與您最初記下的相符。如果是這樣，您就可以放心您的紙本備份是可靠的。


## 如何使用 Ledger Flex 接收比特幣？


按一下「*接收*」標籤。


![LEDGER FLEX](assets/notext/56.webp)


將 Ledger Flex 連接到電腦，使用 PIN 碼解除鎖定，然後開啟「*Bitcoin*」應用程式。


![LEDGER FLEX](assets/notext/57.webp)


在使用 Sparrow Wallet 提供的 Address 之前，請在 Ledger Flex 的螢幕上進行驗證。此做法可讓您確認 Sparrow 上顯示的 Address 並非偽造，且 Ledger 確實持有必要的私人密碼匙，以便稍後花費使用此 Address 保證的比特幣。


若要執行此驗證，請按一下「*顯示 Address*」按鈕。


![LEDGER FLEX](assets/notext/58.webp)


確保 Ledger Flex 上顯示的 Address 與 Sparrow Wallet 上顯示的相符。此外，我們也建議您在將 Address 交給寄件者之前進行這項驗證，以確保其有效性。


![LEDGER FLEX](assets/notext/59.webp)


您可以添加 「*標籤*」來描述將被此 Address 保護的比特幣的來源。這是一個很好的做法，可以幫助您更好地管理您的 UTXO。


![LEDGER FLEX](assets/notext/60.webp)


如需更多關於標籤的資訊，我也建議您查看此其他教學：


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然後您就可以使用這個 Address 來接收比特幣。


![LEDGER FLEX](assets/notext/61.webp)


## 如何使用 Ledger Flex 傳送比特幣？


現在，您已經在用 Flex 加密的 Wallet 中收到了第一筆 Sats，您也可以花掉它們了！將您的 Ledger 連接到您的電腦，解除鎖定，啟動 Sparrow Wallet，然後到 "*Send*"頁籤建立新的交易。


![LEDGER FLEX](assets/notext/62.webp)


如果您要進行「*coin control*」，也就是具體選擇在交易中消耗哪些 UTXOs，請移至「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 「*發送所選*」。您將被重新導向到 「*發送*」標籤的相同畫面，但您已為交易選擇了UTXO。

![LEDGER FLEX](assets/notext/63.webp)

輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。


![LEDGER FLEX](assets/notext/64.webp)


註記「*標籤*」以記住此支出的目的。


![LEDGER FLEX](assets/notext/65.webp)


選擇傳送到此 Address 的金額。


![LEDGER FLEX](assets/notext/66.webp)


根據當前市場調整交易費率。


![LEDGER FLEX](assets/notext/67.webp)


確保交易的所有設定都正確無誤，然後按一下「*建立交易*」。


![LEDGER FLEX](assets/notext/68.webp)


如果一切都令您滿意，請按一下「*完成簽署交易*」。


![LEDGER FLEX](assets/notext/69.webp)


按一下「*簽署*」。


![LEDGER FLEX](assets/notext/70.webp)


按一下您的 Ledger Flex 旁邊的「*簽署*」。


![LEDGER FLEX](assets/notext/71.webp)


確認您的 Flex 螢幕上的交易設定，包括收件者的接收 Address、發送金額和費用金額。


![LEDGER FLEX](assets/notext/72.webp)


若要簽名，請將手指按住「*按住簽名*」按鈕。


![LEDGER FLEX](assets/notext/73.webp)


您的交易現在已簽署。按一下「*廣播交易*」，即可在 Bitcoin 網路上廣播。


![LEDGER FLEX](assets/notext/74.webp)


您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。


![LEDGER FLEX](assets/notext/75.webp)


恭喜您，現在您已經掌握了 Ledger Flex 與 Sparrow Wallet 的基本使用方法！在未來的教學中，我們將介紹如何使用 Ledger Flex 搭配 Liana 來利用 Miniscript。


如果您覺得本教學對您有幫助，請在下方豎起大拇指。歡迎在您的社交網路分享這篇文章。非常感謝您！