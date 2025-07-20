---
name: Trezor Safe 5
description: 設定與使用 Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*圖片來源：[Trezor.io](https://trezor.io/)*



Trezor Safe 5 是由 SatoshiLabs 設計的最新一代 Hardware Wallet，於 2024 年推出。它定位為 Safe 3 的高階版本，著重於人體工學與耐用性。相較於 Model One 和 Model T，它受惠於與前代 Safe 3 相同的安全進步。



Safe 5 定價 169 歐元，屬於高階 Hardware Wallet 類別，競爭對手包括 Coldcard、Ledger Nano X 和 Flex、Jade Plus、Passport 和 Bitbox。



Safe 5 的與眾不同之處在於其 1.54 吋彩色觸控螢幕，受 *Gorilla Glass 3* 保護，可防止震動與刮傷。它也配備了 *Trezor Touch* 觸覺引擎，當觸碰時會發出輕微的震動。與 Safe 3 一樣，它也結合了 Secure Element，並透過 USB-C 連線操作，還增加了 Micro SD 連接埠。



Safe 3 與 Safe 5 的主要差異除了安全方面之外，還在於裝置的品質。它顯著改善了使用者體驗，操作更順暢，螢幕也更舒適。在安全性方面，兩者旗鼓相當。



![Image](assets/fr/01.webp)



Safe 5 擁有您所期望的優良 Hardware Wallet 的所有基本功能，包括 passphrase BIP39 的絕佳整合。然而，它尚未支援 Miniscript。



此機型特別適合初級和中級使用者。另一方面，它可能無法滿足尋求 Coldcard 等裝置上更多特定功能的進階使用者的所有期望。儘管如此，如果您不需要這些進階選項，Trezor Safe 5 可能是您的絕佳選擇。



## Trezor Safe 5 安全機型



和 Safe 3 一樣，Trezor Safe 5 也配備了 EAL6+ 認證的 **Secure Element**，這是在早期機型（如 Model One 和 Model T）上的重大進步。這是 OPTIGA Trust M V3 晶片，它不會直接儲存 seed，而是作為加密元件，確保存取的安全性。安全元件會保留一個秘密，只有在使用者正確輸入 PIN 碼後才能存取。此密碼之後會用來解密 seed，seed 會加密儲存於裝置的主記憶體中。



此混合式安全系統提供更完善的實體保護，特別是針對抽取式攻擊或入侵式分析，這些都是 Model One 容易發生的問題，尤其是在 PIN 碼管理方面。由於使用了 Secure Element，這些弱點現在都已被迴避。此型號也維持開放源碼的軟體架構：管理私密金鑰的產生與使用的程式碼仍可完全存取與驗證。OPTIGA 晶片僅管理 PIN 碼，這是 Bitcoin Wallet 金鑰管理的外部元素。它只限於釋放可用於解密 seed 的秘密。此外，OPTIGA Trust M V3 晶片受惠於相對自由的授權，授權 SatoshiLabs 自由發佈潛在的漏洞 (NDA-Free)。



在我看來，這種安全模式是目前市場上最好的折衷方案之一。它結合了安全元件與開放原始碼軟體管理的優點。在此之前，使用者必須在強化晶片的實體安全性與開放原始碼的透明度之間做出選擇；有了 Trezor Safe，兩者皆可受惠。



在本教程中，您將學習如何安全地設定和使用 Trezor Safe 5。



## 開箱體驗 Trezor Safe 5



當您收到 Safe 5 時，請確定包裝盒和 Seal 完好無損，以確認包裝未被打開。稍後設定時，也會對裝置的真實性和完整性進行軟體檢查。



盒內物品包括 ：




- Trezor Safe 5；
- 小袋內有記錄 Mnemonic 短語的卡片、貼紙和說明書；
- USB-C 至 USB-C 連接線。



打開時，您的 Trezor Safe 5 應該有保護塑膠保護，USB-C 連接埠應有全息 Seal 保護。確定它在那裡。



![Image](assets/fr/02.webp)



裝置上的導覽相當直覺：




- 點選畫面的下半部可向前移動；
- 向下滑動可返回 ；
- 按住螢幕以確認操作。



## 先決條件



在本教程中，我將向您介紹如何使用 Trezor Safe 5 搭配 [Sparrow Wallet 投資組合管理軟體](https://sparrowwallet.com/download/)。如果您尚未安裝此軟體，請立即安裝。如果您需要幫助，我們也有一個關於配置 Sparrow Wallet 的詳細教程：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您還需要 Trezor Suite 軟體來設定 Safe 5、檢查其真實性並安裝韌體。我們只會使用這個軟體，之後只需要用它來更新韌體。對於 Wallet 的日常管理，我們將只使用 Sparrow Wallet，因為它針對 Bitcoin 進行了優化，即使是初學者也很容易上手（Sparrow 只支援 Bitcoin，不支援altcoins）。



[從官方網站下載 Trezor Suite](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



對於這兩個程式，我強烈建議您在安裝到您的機器之前，先檢查它們的真實性 (使用 GnuPG) 和完整性 (透過 Hash)。如果您不知道如何執行，可以參考其他教學：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 啟動 Trezor Safe 5



將 Safe 5 連接到已安裝 Trezor Suite 和 Sparrow Wallet 的電腦。



![Image](assets/fr/04.webp)



開啟 Trezor Suite，然後按一下「*設定我的 Trezor*」。



![Image](assets/fr/05.webp)



選取「*Bitcoin-only 韌體*」，然後按一下「*Install Bitcoin-only*」。



![Image](assets/fr/06.webp)



Trezor Suite 接著會在 Safe 5 上安裝韌體。安裝期間請稍候。



![Image](assets/fr/07.webp)



按一下「*繼續*」。



![Image](assets/fr/08.webp)



然後進行真實性測試，以確保您的 Hardware Wallet 不是偽造或洩露的。



![Image](assets/fr/09.webp)



在 Safe 5 上，按螢幕確認。



![Image](assets/fr/10.webp)



如果您的 Trezor 是真品，Trezor Suite 中會顯示一則確認訊息。



![Image](assets/fr/11.webp)



然後您可以跳過有基本操作說明的視窗。



![Image](assets/fr/12.webp)



## 建立 Bitcoin 產品組合



在 Trezor Suite 上，按一下「*建立新的 Wallet*」按鈕。



![Image](assets/fr/13.webp)



若要建立標準的 BIP39 Wallet，請先從下拉式功能表中選擇「*傳統 Wallet 備份類型*」，然後選擇 12 或 24 個字的 Mnemonic 詞組 (目前建議使用 12 個字)。這樣您就可以建立經典的單一簽名組合。我建議您在此選擇符合 BIP39 的參數，以方便檢索，並避免受限於特定環境。點選「*建立 Wallet*」即可完成。



如果您想進一步瞭解 Trezor 上的其他備份選項，包括 * 多重共用備份*，我建議您也參考本教程：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



接受 Hardware Wallet 上的使用條款。



![Image](assets/fr/15.webp)



按住螢幕不放可建立新的組合。



![Image](assets/fr/16.webp)



在 Trezor Suite 中，按一下「*繼續備份*」。



![Image](assets/fr/17.webp)



軟體提供如何管理 Mnemonic 詞組的說明。



這個 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins。任何持有此短語的人都可以盜取您的資金，即使沒有實體存取您的 Trezor Safe 5。



如果您的 Hardware Wallet 遺失、被盜或破損，這 12 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。



您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。



確認指示，然後按一下「*建立 Wallet 備份*」按鈕。



![Image](assets/fr/18.webp)



Safe 5 會使用隨機數字產生器建立您的 Mnemonic 詞組。請確定在此操作過程中沒有人在看著您。在您選擇的實體媒體上寫下螢幕上提供的詞組。根據您的安全策略，您可以考慮製作幾份完整的短語實體複本 (但最重要的是，不要將它分割)。重要的是要保持字詞的編號和順序。



***顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。



如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



若要移至下一個單字，請按一下螢幕底部。您可以向下滑動來倒退。記下所有單字後，請將手指放在螢幕上，即可進入下一步。



![Image](assets/fr/20.webp)



按照順序選擇 Mnemonic 詞組中的詞彙，確認您寫下的詞彙是否正確。



![Image](assets/fr/21.webp)



完成此驗證程序後，請按一下螢幕以繼續。



![Image](assets/fr/22.webp)



## 設定 PIN 碼



接下來是 PIN 碼步驟。PIN 碼可以解鎖您的 Trezor。因此可防止未經授權的實體存取。PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法獲得 PIN 碼，擁有 12 個字的 Mnemonic 短語也能讓您重新獲得比特幣。



在 Trezor Suite 上，點擊 「*繼續 PIN*」，然後點擊 「*設定 PIN*」按鈕。



![Image](assets/fr/23.webp)



與 Safe 5 確認。



![Image](assets/fr/24.webp)



我們建議您選擇一個盡可能隨機的 PIN 碼。請務必將此密碼保存在與您的 Trezor 儲存位置不同的地方（例如密碼管理器）。您可以定義一個 8 到 50 位數的 PIN 碼。我建議您選擇盡可能長的 PIN 碼，以提高安全性。



使用觸控板輸入 PIN 碼。



![Image](assets/fr/25.webp)



完成後，按一下右下方的 Green 剔號，然後再確認您的 PIN。



![Image](assets/fr/26.webp)



您的 PIN 碼已註冊。



![Image](assets/fr/27.webp)



在 Trezor Suite 上，按一下「*完成設定*」按鈕。



![Image](assets/fr/28.webp)



Safe 5 的設定現已完成。如果您願意，可以變更 Hardware Wallet 的名稱和首頁。



![Image](assets/fr/29.webp)



除了定期對 Hardware Wallet 執行韌體更新，或者如果您想執行復原測試，我們將不再需要 Trezor Suite 軟體。我們現在要使用 Sparrow 來管理組合，因為這個軟體完全適合 Bitcoin 專用。



## 在 Sparrow Wallet 上設定投資組合



如果您還沒有下載 Sparrow Wallet [從官方網站](https://sparrowwallet.com/) 並安裝到您的電腦上，請從此開始。



開啟 Sparrow Wallet 後，請確定軟體已連接到 Bitcoin 節點，Interface 右下角的勾號表示該節點。如果您在連接 Sparrow 時遇到問題，我建議您參考本教學的開頭部分：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。



![Image](assets/fr/30.webp)



命名您的投資組合，然後按一下「*建立 Wallet*」。



![Image](assets/fr/31.webp)



在 "*Script Type*"下拉菜單中，選擇用來保護比特幣的腳本類型。我推薦 "*Taproot*「，或者如果不行的話，」*Native SegWit*"。



![Image](assets/fr/32.webp)



按一下「*已連接 Hardware Wallet*」按鈕。當然，您的 Safe 5 必須已連接到電腦且已解鎖。



當您將 Safe 5 連接到開啟 Sparrow Wallet 的電腦時，Hardware Wallet 螢幕會提示您輸入 passphrase BIP39。這個進階選項將會在未來的教學中介紹。目前，您只需點選右上角的 Green 剔號，確認您希望使用空的 passphrase（即沒有 passphrase）。為了防止您的 Trezor 在每次啟動時都要求您輸入 passphrase，請進入 Trezor Suite，進入設定，更改 "*Device*" > "*Wallet default "中的選項。> "*Wallet default*「中的選項改為 」*Standard*「，而不是 」*passphrase*"。



![Image](assets/fr/33.webp)



按一下「*掃描*」按鈕。您的 Safe 5 應該會出現。按一下「*匯入金鑰儲存庫*」。



![Image](assets/fr/34.webp)



現在您可以看到 Wallet 的詳細資訊，包括第一個帳號的擴充公開金鑰。點選「*Apply*」按鈕，完成 Wallet 的建立。



![Image](assets/fr/35.webp)



選擇一個強大的密碼，以確保對 Sparrow Wallet 的安全存取。此密碼可確保安全存取您的 Sparrow Wallet 資料，保護您的公用金鑰、地址、標籤和交易歷史記錄免於未經授權的存取。



我建議您將此密碼儲存在密碼管理器中，以免忘記。



![Image](assets/fr/36.webp)



現在您的投資組合已匯入 Sparrow Wallet！



![Image](assets/fr/37.webp)



在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行一次空幣恢復測試**。寫下一些參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重設您的 Trezor Safe 5。然後嘗試使用您的紙張備份在 Trezor 上還原 Wallet。檢查還原後生成的 xpub 是否與您最初寫下的相符。如果吻合，您就可以放心，您的紙張備份是可靠的。



若要進一步瞭解如何執行復原測試，我建議您參閱此其他教學：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Safe 5 接收比特幣？



在 Sparrow 上，按一下「*接收*」標籤。



![Image](assets/fr/38.webp)



在使用 Sparrow Wallet 建議的 Address 之前，請在您的 Trezor 螢幕上檢查。這種做法可讓您確認 Sparrow 上顯示的 Address 不是偽造的，而且 Hardware Wallet 確實持有隨後使用此 Address 所保護的比特幣所需的私密金鑰。這可以幫助您避免幾種類型的攻擊。



若要執行此檢查，請按一下「*顯示 Address*」按鈕。



![Image](assets/fr/39.webp)



檢查您 Trezor 上顯示的 Address 是否與 Sparrow Wallet 上的相符。建議您在傳送 Address 給寄件者之前進行這項檢查，以確保其有效性。您可以按螢幕確認。



![Image](assets/fr/40.webp)



然後，您可以新增一個 "*Label*" 來描述將使用此 Address 作保護的 bitcoins 來源。這是一個很好的做法，可以讓您更好地管理您的 UTXO。



![Image](assets/fr/41.webp)



然後您就可以使用這個 Address 來接收比特幣。



![Image](assets/fr/42.webp)



## 如何使用 Trezor Safe 5 傳送比特幣？



現在您已經在 Safe 5 加密的 Wallet 上收到了第一筆 Satss，您也可以花掉它們了！將 Trezor 連接到電腦，使用 PIN 碼解鎖，啟動 Sparrow Wallet，然後到 "*Send*"標籤建立新的交易。



![Image](assets/fr/43.webp)



如果您希望*Coin Control*，即在交易中特別選擇消耗哪些 UTXOs，請前往「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 「*發送所選*」。您將被重新導向至 「*發送*」標籤中的相同畫面，但您已為交易選擇了UTXO。



![Image](assets/fr/44.webp)



輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。



![Image](assets/fr/45.webp)



寫下「*標籤*」以記住此支出的目的。



![Image](assets/fr/46.webp)



選擇要傳送到此 Address 的金額。



![Image](assets/fr/47.webp)



根據當前市場調整您的交易費率。例如，您可以使用 [Mempool.space](https://Mempool.space/) 來選擇合適的費率。



確定所有交易參數都正確，然後按一下「*建立交易*」。



![Image](assets/fr/48.webp)



如果一切都令您滿意，請按一下「*完成簽署交易*」。



![Image](assets/fr/49.webp)



按一下「*簽署*」。



![Image](assets/fr/50.webp)



點選 Trezor Safe 5 旁邊的「*簽署*」。



![Image](assets/fr/51.webp)



檢查 Hardware Wallet 螢幕上的交易參數，包括收款人的接收 Address、發送金額和收費。在 Trezor 上確認交易後，長按螢幕進行簽名。



![Image](assets/fr/52.webp)



您的交易現在已簽署。最後一次檢查是否一切正常，然後按一下「*廣播交易*」，在 Bitcoin 網路上廣播。



![Image](assets/fr/53.webp)



您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。



![Image](assets/fr/54.webp)



恭喜您，現在您已經掌握了 Trezor Safe 5 搭配 Sparrow Wallet 的基本使用方法！若想更進一步，我向您推薦這份全面的教學，教您如何使用 Trezor Hardware Wallet 搭配 passphrase BIP39 來加強您的安全：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝