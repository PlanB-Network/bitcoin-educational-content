---
name: Ledger Nano S Plus
description: 設定與使用 Ledger Nano S Plus
---
![cover](assets/cover.webp)


Hardware Wallet 是專門管理和保護 Bitcoin Wallet 私密金鑰的電子裝置。與安裝在經常連接到網際網路的通用機器上的軟體錢包（或 Hot 錢包）不同，硬體錢包可以實體隔離私密金鑰，降低駭客入侵和竊取的風險。


Hardware Wallet 的主要目標是盡可能減少裝置的功能，以降低其攻擊面。較小的攻擊面也意味著較少的潛在攻擊媒介，也就是攻擊者可利用來存取比特幣的系統弱點較少。


建議使用 Hardware Wallet 來保護您的比特幣，尤其是當您持有大量比特幣時，不論是絕對值還是佔您總資產的比例。


硬體錢包與電腦或智慧型手機上的 Wallet 管理軟體結合使用。此軟體管理交易的建立，但驗證這些交易所需的加密簽章僅在 Hardware Wallet 內完成。這意味著私密金鑰永遠不會暴露在潛在的脆弱環境中。


硬體錢包為使用者提供雙重保護：一方面，硬體錢包透過保持私密金鑰離線來保護您的比特幣免受遠端攻擊；另一方面，硬體錢包通常提供更好的物理保護，防止有人試圖提取金鑰。正是根據這兩個安全標準，我們可以對市場上的不同機型進行判斷和排序。


在本教程中，我建議探索其中一個解決方案：**Ledger Nano S Plus**。


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Ledger Nano S Plus 簡介


Ledger Nano S Plus 是法國 Ledger 公司生產的 Hardware Wallet，市售價格為 79 歐元。


![NANO S PLUS LEDGER](assets/notext/02.webp)


Nano S Plus 配備 CC EAL6+ 認證晶片 (「*安全元件*」)，可為您提供先進的保護，防止硬體受到物理攻擊。螢幕和按鈕直接由此晶片控制。經常被批評的一點是，此晶片的程式碼並非開放原始碼，這需要對此元件的完整性有一定的信任。儘管如此，此元件仍由獨立專家審核。


在使用方面，Ledger Nano S Plus 僅透過有線 USB-C 連線操作。


Ledger 在競爭對手中脫穎而出，因為它總是非常快速地採用 Bitcoin 的新功能，例如 Taproot 或 Miniscript 等，這一點非常值得讚賞。

經過測試後，我發現 Ledger Nano S Plus 是一款出色的入門級 Hardware Wallet。它以合理的價格提供高度的安全性。與同價位的其他裝置相比，它的主要缺點是韌體程式碼並非開放原始碼。此外，與 Ledger Flex 或 Coldcard Q1 等更昂貴的機型相比，Nano S Plus 的螢幕相對較小。儘管如此，它的 Interface 設計得非常好：雖然有兩個按鈕且螢幕較小，但仍很容易使用，包括 BIP39 passphrase 等進階功能。Ledger Nano S Plus 沒有電池、Air-gap 連線、攝影機或 micro SD 連接埠，但這對於這個價位的產品來說是相當正常的。


在我看來，Ledger Nano S Plus 是保護 Bitcoin Wallet 的好選擇，適合初級和中級使用者。不過，在這個價格範圍內，我個人比較喜歡 Trezor Safe 3，它提供了大致相同的選擇。在我看來，Trezor 的優勢在於其安全元件的管理：Mnemonic 的詞組和金鑰完全由開放原始碼管理，但仍受惠於晶片的保護。Trezor 的缺點在於他們有時在實作新功能時會非常緩慢，不像 Ledger。


## 如何購買 Ledger Nano S Plus？


Ledger Nano S Plus 已於 [官方網站](https://shop.Ledger.com/products/Ledger-nano-s-plus) 開售。若要在實體商店購買，您也可以在 Ledger 網站上找到 [認證經銷商名單](https://www.Ledger.com/reseller)。


## 先決條件


當您收到 Ledger Nano 後，第一步是檢查包裝，確保它沒有被打開。如果包裝破損，這可能表示 Hardware Wallet 已經損壞，可能不是正品。


打開之後，您應該會發現盒子裡有以下物品：


- Ledger Nano S Plus；
- USB-C 至 USB-A 連接線；
- 使用者手冊；
- 卡片，寫下您的 Mnemonic 詞組。


在本教程中，您將需要 2 個軟體應用程式：Ledger Live 用於初始化 Ledger，Sparrow Wallet 用於管理您的 Bitcoin Wallet。請從它們的官方網站下載 [Ledger Live](https://www.Ledger.com/Ledger-live) 和 [Sparrow Wallet](https://sparrowwallet.com/download/)。


![NANO S PLUS LEDGER](assets/notext/03.webp)

對於這兩個軟體程式，我強烈建議在您的機器上安裝之前，先檢查它們的真實性 (使用 GnuPG) 和完整性 (透過 Hash)。如果您不確定如何執行，可以參考這份教學：

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 如何初始化 Ledger Nano？


將您的 Nano 連接到已安裝 Ledger Live 和 Sparrow Wallet 的電腦。若要在 Ledger 上瀏覽，請使用左側按鈕向左，右側按鈕向右。若要選擇或確認選項，請同時按下這兩個按鈕。


![NANO S PLUS LEDGER](assets/notext/04.webp)


捲動不同的介紹頁面，然後按一下 2 個按鈕開始。


![NANO S PLUS LEDGER](assets/notext/05.webp)


選擇選項「*設定為新裝置*」。


![NANO S PLUS LEDGER](assets/notext/06.webp)


選擇用於解鎖 Ledger 的 PIN 碼。因此，這是用來防止未經授權的實體存取。此 PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要有您的 Mnemonic 24 字短語，就可以重新取得您的比特幣。


![NANO S PLUS LEDGER](assets/notext/07.webp)


建議選擇 8 位數的 PIN 碼，盡可能隨機。此外，請務必將此密碼保存在與 Ledger Nano S Plus 不同的地方（例如密碼管理器）。


使用按鈕移動數字，然後同時按一下兩個按鈕，選取每個數字。


![NANO S PLUS LEDGER](assets/notext/08.webp)


再次輸入 PIN 碼以確認。


![NANO S PLUS LEDGER](assets/notext/09.webp)


您的 Nano 提供了如何管理復原短語的說明。


**這個 Mnemonic 詞組可以完全且不受限制地存取您所有的 bitcoins**。任何擁有此短語的人都可以盜取您的資金，即使沒有實體存取您的 Ledger。當您的 Ledger Nano 遺失、被竊或損壞時，這 24 個字的短語可以讓您恢復比特幣的存取權。因此，小心保存並將其存放在安全的地方是非常重要的。


您可以將它寫在 Ledger 隨附的硬紙板紙上，或者為了更安全起見，我建議您將它刻在不銹鋼介質上，以防止火災、水災或倒塌的風險。


您可以瀏覽這些說明並按一下右側按鈕跳頁。


![NANO S PLUS LEDGER](assets/notext/10.webp)

Ledger 會使用隨機數字產生器建立您的 Mnemonic 詞組。請確定在此操作過程中沒有人觀察您。將 Ledger 提供的短語寫在您選擇的實體媒體上。根據您的安全策略，您可以考慮製作幾份完整的短語實體複本 (但重要的是，請勿分割)。保持字詞的編號和順序是很重要的。

*** 很明顯，您絕對不應該在網路上分享這些文字，這與我在本教學中所做的相反。本範例 Wallet 只會在 Testnet 上使用，並會在教學結束後刪除。


![NANO S PLUS LEDGER](assets/notext/11.webp)


若要移至下一個字，請按一下右鍵。


![NANO S PLUS LEDGER](assets/notext/12.webp)


記下所有單字後，按一下 2 按鈕進入下一步。


![NANO S PLUS LEDGER](assets/notext/13.webp)


按一下「*確認您的恢復詞組*」這兩個按鈕，然後按順序選擇 Mnemonic 詞組中的單字，確認您所記下的單字是否正確。使用左右鍵在選項之間瀏覽，然後點選 2 個按鈕，選擇正確的單字。繼續此步驟，直到第 24 個單字為止。


![NANO S PLUS LEDGER](assets/notext/14.webp)


如果您要確認的詞組與 Ledger 在上一步提供給您的完全相同，您就可以繼續。如果不是，則表示您的 Mnemonic 詞組實體備份不正確，您需要重新啟動程序。


![NANO S PLUS LEDGER](assets/notext/15.webp)


就這樣，您的 seed 已在 Ledger Nano S Plus 上正確建立。在繼續從這個 seed 建立新的 Bitcoin Wallet 之前，讓我們一起探索裝置設定。


## 如何修改 Ledger 的設定？


若要存取設定，請按住 2 個按鈕幾秒鐘。


![NANO S PLUS LEDGER](assets/notext/16.webp)


按一下「*設定*」功能表。


![NANO S PLUS LEDGER](assets/notext/17.webp)


然後選擇「*一般*」。


![NANO S PLUS LEDGER](assets/notext/18.webp)


在「*語言*」功能表中，您可以變更顯示語言。


![NANO S PLUS LEDGER](assets/notext/19.webp)


在「*亮度*」功能表中，您可以調整螢幕亮度。我們暫時對其他的一般設定不感興趣。


![NANO S PLUS LEDGER](assets/notext/20.webp)


現在，前往「*安全性*」設定區。


![NANO S PLUS LEDGER](assets/notext/21.webp)


「*變更 PIN*」可讓您變更 PIN 碼。

![NANO S PLUS LEDGER](assets/notext/22.webp)

「*passphrase*」可讓您設定 BIP39 passphrase。passphrase 是一個可選的密碼，結合您的復原短語，可為您的 Wallet 提供額外 Layer 的安全性。


![NANO S PLUS LEDGER](assets/notext/23.webp)


目前，您的 Wallet 是由 24 個字組成的 Mnemonic 詞組所產生。此恢復詞組非常重要，因為它可讓您在遺失時恢復 Wallet 的所有鑰匙。但是，它構成單一點故障 (SPOF)。如果它受到損害，您的比特幣就會有危險。這就是 passphrase 的用處。這是一個可選的密碼，您可以任意選擇，它可以添加到 Mnemonic 短語中，以增強 Wallet 的安全性。


passphrase 不應該與 PIN 碼混淆。它在密碼金鑰的產生過程中扮演一個角色。它與 Mnemonic 詞組配合使用，改變生成密碼匙的 seed。因此，即使有人取得您的 24 字短語，如果沒有 passphrase，他們也無法存取您的資金。使用 passphrase 基本上會產生一個新的 Wallet，並具有不同的金鑰。修改（即使是輕微修改）passphrase 會產生不同的 Wallet。


passphrase 是一個非常強大的工具，可以增強您比特幣的安全性。但是，在使用之前了解它的工作原理是非常重要的，以避免失去 Wallet 的訪問權限。因此，如果您想在 Ledger 上安裝 passphrase，我建議您參考其他專用教學：


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

*PIN 鎖定*"功能表可讓您設定並啟動 Ledger 在一段確定的非活動時間後自動鎖定。


![NANO S PLUS LEDGER](assets/notext/24.webp)


螢幕保護程式*"功能表可讓您調整 Ledger Nano 的睡眠模式。請注意，除非啟動 「*PIN 鎖定*」選項以對應睡眠模式，否則螢幕保護程式在喚醒時不需要輸入 PIN 碼。此功能對於配備電池的 Ledger Nano X 裝置特別有用，可降低其能源消耗。


![NANO S PLUS LEDGER](assets/notext/25.webp)


最後，「*重設裝置*」功能表可讓您重設 Ledger。只有當您確定 Ledger 並未包含任何保護 bitcoins 的金鑰時，才能進行重設，因為您可能會永久失去存取資金的權利。這個選項對於執行空機恢復測試很有用，但我稍後會再談。


![NANO S PLUS LEDGER](assets/notext/26.webp)

## 如何安裝 Bitcoin 應用程式？


首先在您的電腦上啟動Ledger Live軟體，然後連接並解鎖您的Ledger Nano。在Ledger Live中，進入 "*My Ledger*"選單。您會被要求授權存取您的Nano。


![NANO S PLUS LEDGER](assets/notext/27.webp)


按一下兩個按鈕，驗證 Ledger 的存取權限。


![NANO S PLUS LEDGER](assets/notext/28.webp)


首先，在 Ledger Live 上，確定出現「*正版檢查*」。這可確認您的裝置是正版。


![NANO S PLUS LEDGER](assets/notext/29.webp)


如果您的 Ledger Nano 韌體不是最新的，Ledger Live 會自動提供更新。如有必要，請點選「*更新韌體*」，然後點選「*安裝更新*」開始安裝。在您的 Ledger 上，點選兩個按鈕確認，然後在安裝過程中等待。


最後，我們要新增 Bitcoin 應用程式。在 Ledger Live 上，點選「*Bitcoin (BTC)*」旁邊的「*Install*」按鈕即可。


![NANO S PLUS LEDGER](assets/notext/30.webp)


應用程式會安裝在您的 Nano 上。


![NANO S PLUS LEDGER](assets/notext/31.webp)


從現在開始，您不再需要 Ledger Live 軟體來定期管理您的 Wallet。當有新版本推出時，您可以偶爾回到 Ledger 更新韌體。至於其他方面，我們會使用 Sparrow Wallet，它是更全面的工具，能有效管理 Bitcoin Wallet。


![NANO S PLUS LEDGER](assets/notext/32.webp)


## 如何使用 Sparrow 設定新的 Bitcoin Wallet？


開啟 Sparrow Wallet，跳過介紹頁面進入主畫面。觀察位於畫面右下方的開關，檢查是否已正確連線至節點。


![NANO S PLUS LEDGER](assets/notext/33.webp)


我強烈建議您使用自己的 Bitcoin 節點。在本教程中，我使用的是公共節點（黃色），因為我使用的是 Testnet，但對於一般的使用，最好選擇本地的 Bitcoin 核心（Green）或連接到遠端節點（藍色）的 Electrum 伺服器。


按一下「*檔案*」功能表，然後按一下「*新增 Wallet*」。


![NANO S PLUS LEDGER](assets/notext/34.webp)


選擇此 Wallet 的名稱，然後按一下「*建立 Wallet*」。


![NANO S PLUS LEDGER](assets/notext/35.webp)


在 "*Script Type*"下拉菜單中，選擇用來保護比特幣的腳本類型。我建議選擇 "*Taproot*「，如果沒有，則選擇 」*Native SegWit*"。


![NANO S PLUS LEDGER](assets/notext/36.webp)

按一下「*已連線的 Hardware Wallet*」按鈕。

![NANO S PLUS LEDGER](assets/notext/37.webp)


如果您還沒有這麼做，請將 Ledger Nano S Plus 連接到電腦，使用 PIN 碼解鎖，然後在 Bitcoin 標誌上按一次 2 個按鈕，開啟「*Bitcoin*」應用程式。


*在本教程中，我使用的是 Bitcoin Testnet 應用程式，但 Mainnet.* 的程序仍然相同。


![NANO S PLUS LEDGER](assets/notext/38.webp)


在 Sparrow 上，按一下「*掃描*」按鈕。


![NANO S PLUS LEDGER](assets/notext/39.webp)


然後按一下「*匯入金鑰儲存庫*」。


![NANO S PLUS LEDGER](assets/notext/40.webp)


現在您可以看到 Wallet 的詳細資訊，包括第一個帳號的擴充公開金鑰。點選「*Apply*」按鈕，完成 Wallet 的建立。


![NANO S PLUS LEDGER](assets/notext/41.webp)


選擇一個強大的密碼以確保存取 Sparrow Wallet 的安全性。此密碼將確保您在 Sparrow 上存取 Wallet 資料的安全性，有助於保護您的公開金鑰，地址，標籤和交易歷史，防止任何未經授權的存取。


我建議您將此密碼儲存在密碼管理器中，以免忘記。


![NANO S PLUS LEDGER](assets/notext/42.webp)


這樣，您的 Wallet 就完成了！


![NANO S PLUS LEDGER](assets/notext/43.webp)


在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您執行一次乾式恢復測試**。記下參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重設您的 Ledger Nano。之後，嘗試使用您的紙本備份在 Ledger 上還原您的 Wallet。檢查還原後產生的 xpub 是否與您最初記下的相符。如果是的話，您可以放心您的紙本備份是可靠的。


若要進一步瞭解如何執行復原測試，我建議您參閱此其他教學：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Ledger Nano 接收比特幣？


按一下「*接收*」標籤。


![NANO S PLUS LEDGER](assets/notext/44.webp)


將您的 Ledger Nano S Plus 連接到電腦，使用 PIN 碼解鎖，然後開啟「*Bitcoin*」應用程式。


![NANO S PLUS LEDGER](assets/notext/45.webp)

在使用 Sparrow Wallet 提供的 Address 之前，請在您的 Ledger 的螢幕上進行驗證。這種做法可以讓您確認 Sparrow 上顯示的 Address 並非偽造，而且 Hardware Wallet 確實持有必要的私人密碼匙，以便稍後花費使用此 Address 保證的比特幣。這可以幫助您避免幾種類型的攻擊。

若要執行此驗證，請按一下「*顯示 Address*」按鈕。


![NANO S PLUS LEDGER](assets/notext/46.webp)


確保您 Ledger 上顯示的 Address 與 Sparrow Wallet 上顯示的相符。我們也建議您在將 Address 交給寄件者之前進行這項確認，以確定其有效性。您可以使用按鈕檢視完整的 Address。


![NANO S PLUS LEDGER](assets/notext/47.webp)


如果地址確實相同，請點選「*Approve*」。


![NANO S PLUS LEDGER](assets/notext/48.webp)


您可以添加 「*標籤*」來描述將使用此 Address 保護的比特幣的來源。這是一個很好的做法，可以幫助您更好地管理您的 UTXOs。


![NANO S PLUS LEDGER](assets/notext/49.webp)


如需更多關於標籤的資訊，我也建議您查看此其他教學：


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然後您就可以使用這個 Address 來接收比特幣。


![NANO S PLUS LEDGER](assets/notext/50.webp)


## 如何使用 Ledger Nano 傳送比特幣？


現在您已經在用 Nano S Plus 加密的 Wallet 中收到了第一筆 Sats，您也可以花掉它們了！將您的 Ledger 連接到您的電腦，解除鎖定，啟動 Sparrow Wallet，然後到 「*發送*」標籤建立新的交易。


![NANO S PLUS LEDGER](assets/notext/51.webp)


如果您想要進行「*coin control*」，也就是特別選擇要在交易中消耗哪些 UTXOs，請移至「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 「*發送所選*」。您將被重新導向至 「*發送*」標籤的相同畫面，但您已為交易選擇了UTXO。


![NANO S PLUS LEDGER](assets/notext/52.webp)


輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。


![NANO S PLUS LEDGER](assets/notext/53.webp)


註記「*標籤*」以記住此支出的用途。


![NANO S PLUS LEDGER](assets/notext/54.webp)


選擇傳送到此 Address 的金額。


![NANO S PLUS LEDGER](assets/notext/55.webp)


根據當前市場調整交易費率。


![NANO S PLUS LEDGER](assets/notext/56.webp)

確保交易的所有設定都正確無誤，然後按一下「*建立交易*」。

![NANO S PLUS LEDGER](assets/notext/57.webp)


如果您覺得一切順利，請按一下「*完成簽名交易*」。


![NANO S PLUS LEDGER](assets/notext/58.webp)


按一下「*簽署*」。


![NANO S PLUS LEDGER](assets/notext/59.webp)


按一下您的 Ledger Nano S Plus 旁邊的「*Sign*」。


![NANO S PLUS LEDGER](assets/notext/60.webp)


確認 Ledger 畫面上的交易設定，包括收件者的收件 Address、發送金額及費用金額。


![NANO S PLUS LEDGER](assets/notext/61.webp)


如果您覺得一切順利，請按「*簽署交易*」上的兩個按鈕簽署。


![NANO S PLUS LEDGER](assets/notext/62.webp)


您的交易已經簽署。請再次確認一切正常，然後按一下「*廣播交易*」以在 Bitcoin 網路上廣播。


![NANO S PLUS LEDGER](assets/notext/63.webp)


您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。


![NANO S PLUS LEDGER](assets/notext/64.webp)


恭喜您，現在您已經掌握了 Ledger Nano S Plus 搭配 Sparrow Wallet 的基本使用方法！在未來的教學中，我們將介紹如何使用 Ledger 搭配 Liana 來利用 Miniscript。


如果您覺得本教學對您有幫助，請在下方留下大拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。非常感謝您！


我也建議您看看這篇 Ledger Flex 的完整教學：


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a