---
name: Trezor Safe 3
description: 設定與使用 Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*圖片來源：[Trezor.io](https://trezor.io/)*



Trezor Safe 3 是由 SatoshiLabs 設計的 Hardware Wallet，創造於 2023 年。它是一款非常小巧輕便的機型（14 克），專為初學者和中級使用者設計。它是著名的 Model One 的繼承者，有重大的新增功能，同時保留了品牌的開放源碼方式，使其有別於主要競爭對手 Ledger。Safe 3 的售價為 79 歐元。因此它被定位在 Hardware Wallet 的中端市場，與 Ledger Nano S Plus 直接競爭。



Safe 3 沒有電池，完全透過 USB-C 連線運作，用於電源和通訊。它有一個 0.96 吋的小型單色 OLED 顯示器和兩個實體按鈕。



![Image](assets/fr/01.webp)



Safe 3 提供優良 Hardware Wallet 應有的所有基本功能，包括 passphrase BIP39 的絕佳整合。不過，它尚未支援 Miniscript。



這款機型特別適合初學者，甚至可能是我會推薦給新使用者的 Hardware Wallet。它也非常適合中級使用者。另一方面，它可能無法滿足尋求更特殊功能的進階使用者的所有期望，這些功能可在 Coldcard 等裝置上找到。儘管如此，如果您不需要這些進階選項，Trezor Safe 3 也許是您的絕佳選擇。



## Trezor Safe 3 安全模式



Trezor Safe 3 現已配備 EAL6+ 認證的 **Secure Element**，與之前的 Model One 和 Model T 等型號相比有了顯著的進步。這是 OPTIGA Trust M V3 晶片，不直接儲存 seed，而是作為加密元件，以確保存取的安全性。安全元件會保留一個秘密，只有在使用者正確輸入 PIN 碼後才能存取。此密碼之後會用來解密 seed，seed 會加密儲存於裝置的主記憶體中。



此混合式安全系統提供更完善的實體保護，特別是針對抽取式攻擊或入侵式分析，這些都是 Model One 容易發生的問題，尤其是在 PIN 碼管理方面。由於使用了 Secure Element，這些弱點現在都已被迴避。此型號也維持開放源碼的軟體架構：管理私密金鑰的產生與使用的程式碼仍可完全存取與驗證。OPTIGA 晶片只管理 PIN 碼，這是 Bitcoin Wallet 金鑰管理的外部元素。它只會釋放可用於解密 seed 的秘密。此外，OPTIGA Trust M V3 晶片受惠於相對自由的授權，授權中本聰實驗室（SatoshiLabs）自由公布潛在的漏洞。



在我看來，這種安全模式是目前市場上最好的折衷方案之一。它結合了安全元件與開放原始碼軟體管理的優點。在此之前，使用者必須在使用晶片的強化實體安全性與開放原始碼的透明度之間做出選擇；有了 Trezor Safe 3，兩者皆可受惠。



在本教程中，我們將教您如何安全地設定和使用 Trezor Safe 3。



## Trezor Safe 3 開箱



當您收到 Safe 3 時，請確定包裝盒和 Seal 完好無損，以確認包裝未被打開。稍後設定時，也會對裝置的真實性和完整性進行軟體驗證。



盒內物品包括 ：




- Trezor Safe 3；
- 小袋內有記錄 Mnemonic 短語的卡片、貼紙和說明書；
- USB-C 至 USB-C 連接線。



![Image](assets/fr/02.webp)



打開時，您的 Trezor Safe 3 應該有保護塑膠保護，USB-C 連接埠應有全息 Seal 保護。確定它在那裡。



![Image](assets/fr/03.webp)



裝置上的導覽方式很簡單：使用右鍵向右捲動，左鍵向左捲動。同時按下兩個按鈕可確認動作。



![Image](assets/fr/04.webp)



## 先決條件



在本教程中，我將教您如何使用 Trezor Safe 3 與 [Sparrow Wallet 投資組合管理軟體](https://sparrowwallet.com/download/)。如果您尚未安裝此軟體，請立即安裝。如果您需要幫助，我們也有一個關於配置 Sparrow Wallet 的詳細教程：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您還需要 Trezor Suite 軟體來設定 Safe 3、檢查其真實性並安裝韌體。我們只會使用這個軟體，之後只需要用它來更新韌體。對於 Wallet 的日常管理，我們將只使用 Sparrow Wallet，因為它針對 Bitcoin 進行了優化，即使是初學者也很容易上手（Sparrow 只支援 Bitcoin，不支援altcoins）。



[從官方網站下載 Trezor Suite](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



對於這兩個程式，我強烈建議您在安裝到您的機器之前，先檢查它們的真實性 (使用 GnuPG) 和完整性 (透過 Hash)。如果您不知道如何執行，可以參考其他教學：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 啟動 Trezor Safe 3



將 Safe 3 連接到已安裝 Trezor Suite 和 Sparrow Wallet 的電腦。



![Image](assets/fr/06.webp)



開啟 Trezor Suite，然後按一下「*設定我的 Trezor*」。



![Image](assets/fr/07.webp)



選取「*Bitcoin-only 韌體*」，然後按一下「*Install Bitcoin-only*」。



![Image](assets/fr/08.webp)



Trezor Suite 將會在 Safe 3 上安裝韌體。安裝期間請稍候。



![Image](assets/fr/09.webp)



按一下「*繼續*」。



![Image](assets/fr/10.webp)



然後進行真實性測試，以確保您的 Hardware Wallet 不是偽造或洩露的。



![Image](assets/fr/11.webp)



在 Safe 3 上，按右鍵確認。



![Image](assets/fr/12.webp)



如果您的 Trezor 是真品，Trezor Suite 中會顯示一則確認訊息。



![Image](assets/fr/13.webp)



然後您可以跳過有基本操作說明的視窗。



![Image](assets/fr/14.webp)



## 建立 Bitcoin 產品組合



在 Trezor Suite 上，按一下「*建立新的 Wallet*」按鈕。



![Image](assets/fr/15.webp)



對於標準組合，您可以選擇預設備份類型。這會創建一個經典的單一密碼組合，其中包含 12 個字的 Mnemonic 詞組。按一下「*建立 Wallet*」。



如果您想進一步瞭解 Trezor 上的其他備份選項，包括 * 多重共用備份*，我建議您也參考本教程：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



接受 Hardware Wallet 上的使用條款。



![Image](assets/fr/17.webp)



再按一次右鍵，建立新的組合。



![Image](assets/fr/18.webp)



在 Trezor Suite 中，按一下「*繼續備份*」。



![Image](assets/fr/19.webp)



軟體提供如何管理 Mnemonic 詞組的說明。



這個 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins。任何持有此短語的人都可以盜取您的資金，即使沒有實體存取您的 Trezor Safe 3。



如果您的 Hardware Wallet 遺失、被盜或破損，這 12 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。



您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。



確認指示，然後按一下「*建立 Wallet 備份*」按鈕。



![Image](assets/fr/20.webp)



Safe 3 會使用隨機數字產生器建立您的 Mnemonic 詞組。請確定在此操作過程中沒有人在看著您。在您選擇的實體媒體上寫下螢幕上提供的詞組。根據您的安全策略，您可以考慮製作幾份完整的短語實體複本 (但最重要的是，不要將它分割)。重要的是要保持字詞的編號和順序。



***顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。



如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



若要移至下一個單字，請按一下滑鼠右鍵。您可以按左鍵倒退。記下所有單字後，按住右鍵進入下一步。



![Image](assets/fr/22.webp)



依照順序選擇 Mnemonic 詞組中的單字，確認您寫下的單字是否正確。使用左右按鈕在提案之間瀏覽，然後同時點選 2 個按鈕，選擇正確的單字。



![Image](assets/fr/23.webp)



完成此驗證程序後，請按一下右側的按鈕。



![Image](assets/fr/24.webp)



## 設定 PIN 碼



接下來是 PIN 碼步驟。PIN 碼可以解鎖您的 Trezor。因此可防止未經授權的實體存取。PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法獲得 PIN 碼，擁有 12 個字的 Mnemonic 短語也能讓您重新獲得比特幣。



在 Trezor Suite 上，點擊 「*繼續 PIN*」，然後點擊 「*設定 PIN*」按鈕。



![Image](assets/fr/25.webp)



與 Safe 3 確認。



![Image](assets/fr/26.webp)



我們建議您選擇一個盡可能隨機的 PIN 碼。請務必將此密碼保存在與您的 Trezor 儲存位置不同的地方（例如密碼管理器）。您可以定義一個 8 到 50 位數的 PIN 碼。我建議您選擇盡可能長的 PIN 碼，以提高安全性。



使用左右按鈕選擇每個數字。若要確認您的選擇並進入下一位數，請同時按下這兩個按鈕。



![Image](assets/fr/27.webp)



完成後，按一下位數開始處的「*ENTER*」核取標記，然後再確認您的 PIN。



![Image](assets/fr/28.webp)



您的 PIN 碼已註冊。



![Image](assets/fr/29.webp)



在 Trezor Suite 上，按一下「*完成設定*」按鈕。



![Image](assets/fr/30.webp)



Safe 3 的設定至此完成。如果您願意，可以變更 Hardware Wallet 的名稱和首頁。



![Image](assets/fr/31.webp)



除了定期對 Hardware Wallet 執行韌體更新，或者如果您想執行恢復測試，我們將不再需要 Trezor Suite 軟體。我們現在要使用 Sparrow 來管理組合，因為這個軟體完全適合 Bitcoin 專用。



## 在 Sparrow Wallet 上設定投資組合



如果您尚未下載 Sparrow Wallet [從官方網站](https://sparrowwallet.com/)，請先將其下載並安裝到您的電腦上。



開啟 Sparrow Wallet 後，請確定軟體已連接到 Bitcoin 節點，Interface 右下角的勾號表示此節點。如果您在連接 Sparrow 時遇到問題，建議您閱讀本教學的開頭部分：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。



![Image](assets/fr/32.webp)



命名您的投資組合，然後按一下「*建立 Wallet*」。



![Image](assets/fr/33.webp)



在 "*Script Type*"下拉菜單中，選擇用來保護比特幣的腳本類型。我推薦 "*Taproot*「，或者如果不行的話，」*Native SegWit*"。



![Image](assets/fr/34.webp)



按一下「*已連接 Hardware Wallet*」按鈕。當然，您的 Safe 3 必須連線至電腦且已解鎖。



![Image](assets/fr/35.webp)



按一下「*掃描*」按鈕。您的 Safe 3 應該會出現。按一下「*匯入金鑰儲存庫*」。



![Image](assets/fr/36.webp)



現在您可以看到 Wallet 的詳細資訊，包括第一個帳號的擴充公開金鑰。點選「*Apply*」按鈕，完成 Wallet 的建立。



![Image](assets/fr/37.webp)



選擇一個強大的密碼以確保存取 Sparrow Wallet 的安全性。此密碼可確保安全存取您的 Sparrow Wallet 資料，保護您的公用金鑰、地址、標籤和交易記錄免於未經授權的存取。



我建議您將此密碼儲存在密碼管理器中，以免忘記。



![Image](assets/fr/38.webp)



現在您的投資組合已匯入 Sparrow Wallet！



![Image](assets/fr/39.webp)



在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行空幣恢復測試**。寫下一些參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重置您的 Trezor Safe 3。然後嘗試使用紙張備份在 Trezor 上還原 Wallet。檢查還原後生成的 xpub 是否與您最初寫下的相符。如果吻合，您就可以放心，您的紙張備份是可靠的。



若要進一步瞭解如何執行復原測試，我建議您參閱此其他教學：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Safe 3 接收比特幣？



在 Sparrow 上，按一下「*接收*」標籤。



![Image](assets/fr/40.webp)



在使用 Sparrow Wallet 建議的 Address 之前，請在您的 Trezor 螢幕上檢查。這種做法可以讓您確認 Sparrow 上顯示的 Address 不是偽造的，而且 Hardware Wallet 確實持有隨後使用此 Address 所保護的比特幣所需的私密金鑰。這可以幫助您避免幾種類型的攻擊。



若要執行此檢查，請按一下「*顯示 Address*」按鈕。



![Image](assets/fr/41.webp)



檢查您 Trezor 上顯示的 Address 是否與 Sparrow Wallet 上的相符。建議您在傳送 Address 給寄件者之前進行這項檢查，以確定其有效性。您可以使用按鈕確認。



![Image](assets/fr/42.webp)



然後，您可以添加一個 「*標籤*」來描述將用此 Address 作保護的比特幣來源。這是一個很好的做法，可以讓您更好地管理您的 UTXO。



![Image](assets/fr/43.webp)



然後您就可以使用這個 Address 來接收比特幣。



![Image](assets/fr/44.webp)



## 如何使用 Trezor Safe 3 傳送比特幣？



現在您已經在 Safe 3 加密的 Wallet 上收到了第一筆 Satss，您也可以花掉它們了！將 Trezor 連接到電腦，使用 PIN 碼解鎖，啟動 Sparrow Wallet，然後到 "*Send*"標籤建立新的交易。



![Image](assets/fr/45.webp)



如果您希望*Coin Control*，即在交易中特別選擇消耗哪些 UTXOs，請前往「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 「*發送所選*」。您將被重新導向至 「*發送*」標籤中的相同畫面，但您已為交易選擇了UTXO。



![Image](assets/fr/46.webp)



輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。



![Image](assets/fr/47.webp)



寫下「*標籤*」以記住此支出的目的。



![Image](assets/fr/48.webp)



選擇要傳送到此 Address 的金額。



![Image](assets/fr/49.webp)



根據當前市場調整您的交易費率。例如，您可以使用 [Mempool.space](https://Mempool.space/) 來選擇合適的費率。



確定所有交易參數都正確，然後按一下「*建立交易*」。



![Image](assets/fr/50.webp)



如果一切都令您滿意，請按一下「*完成簽署交易*」。



![Image](assets/fr/51.webp)



按一下「*簽署*」。



![Image](assets/fr/52.webp)



點選 Trezor Safe 3 旁邊的「*簽署*」。



![Image](assets/fr/53.webp)



檢查 Hardware Wallet 螢幕上的交易參數，包括收款人的收款 Address、發送金額和收費。一旦交易在 Trezor 上完成驗證，請同時點擊兩個按鈕進行簽名。



![Image](assets/fr/54.webp)



您的交易現在已簽署。最後一次檢查是否一切正常，然後按一下「*廣播交易*」，在 Bitcoin 網路上廣播。



![Image](assets/fr/55.webp)



您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。



![Image](assets/fr/56.webp)



恭喜您，現在您已經掌握了 Trezor Safe 3 與 Sparrow Wallet 的基本使用方法！若想更進一步，我推薦您閱讀這篇有關使用 Hardware Wallet Trezor 搭配 passphrase BIP39 以提升安全性的全面教學：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝