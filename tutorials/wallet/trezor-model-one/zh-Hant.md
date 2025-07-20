---
name: Trezor Model One
description: 設定與使用 Hardware Wallet Model One
---
![cover](assets/cover.webp)



*圖片來源：[Trezor.io](https://trezor.io/)*



Trezor Model One 是 SatoshiLabs 於 2014 年推出的第一款 Hardware Wallet。經過十多年的發展，它仍然是一個有趣的選擇，特別是對於尋找在技術和預算方面都可以接受的 Hardware Wallet 的用戶而言。事實上，Trezor 官網的售價為 49 歐元。它是這個價格範圍內僅有的硬體錢包之一。它介乎於 20 歐元左右的入門級裝置（例如 Tapsigner）與 80 歐元左右的中階裝置（例如 Ledger Nano S Plus 或 Trezor Safe 3）之間。



Model One 配備 0.96 吋單色 OLED 顯示器和兩個實體按鈕。它的運作不需電池，僅使用 micro-USB 連線供電和資料 Exchange。



![Image](assets/fr/01.webp)



Model One 的主要缺點是缺乏安全元件 (Secure Element)，因此容易受到各種物理攻擊，其中有些攻擊的執行相對較為簡單。這些攻擊可包括分析輔助通道以確定裝置 PIN，或使用更先進技術來擷取加密的 seed，以便稍後暴力破解。請注意，這些攻擊需要實體存取裝置。不過，使用堅固的 passphrase BIP39 可以大幅降低此漏洞。如果您選擇這種 Hardware Wallet，我強烈建議您配置 passphrase。



Model One 具有兩個重要優勢：




- 它以完全開放原始碼的架構為基礎。與較新的 Secure Element 機型不同，Model One 的所有硬體與軟體元件都是可稽核的；
- 它配備了螢幕。據我所知，這是市面上這個價位唯一配備顯示器的 Hardware Wallet。這是一項非常重要的功能，因為它可以驗證已簽署的資訊和接收位址，從而防止許多數位攻擊。



因此，對於預算有限的初級和中級使用者而言，Trezor Model One 可能是一個明智的選擇。然而，由於沒有 Secure Element（安全元件），因此在實體保護方面仍需注意其限制。如果您的預算有限，這是一個不錯的選擇，但如果您有能力選擇更優質的機型，例如售價 79 歐元的 Trezor Safe 3，則更為可取，因為它包含安全元件。



## Trezor Model One 開箱



當您收到 Model One 時，請確定包裝盒和 Seal 完好無損，以確認包裝未被打開。稍後設定時，也會以軟體驗證裝置的真實性和完整性。



盒內物品包括 ：




- Trezor Model One；
- 用於記錄 Mnemonic 短語、貼紙和說明的卡片；
- USB-A 至 micro-USB 連接線。



![Image](assets/fr/02.webp)



導覽裝置非常簡單：




- 按一下滑鼠右鍵以確認，並進入下一步；
- 使用左鍵返回。



## 先決條件



在本教程中，我將向您介紹如何使用 Trezor Model One 與 [Sparrow Wallet 投資組合管理軟體](https://sparrowwallet.com/download/)。如果您尚未安裝此軟體，請立即安裝。如果您需要幫助，我們也有一個關於配置 Sparrow Wallet 的詳細教程：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

您也需要 Trezor Suite 軟體來設定 Model One、檢查真實性和安裝韌體。我們只會在這方面使用這個軟體，之後只需要在韌體更新時使用。對於 Wallet 的日常管理，我們將只使用 Sparrow Wallet，因為它針對 Bitcoin 進行了優化，即使是初學者也很容易上手（Sparrow 只支援 Bitcoin，不支援altcoins）。



[從官方網站下載 Trezor Suite](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



對於這兩個程式，我強烈建議您在安裝到您的機器之前，先檢查它們的真實性 (使用 GnuPG) 和完整性 (透過 Hash)。如果您不知道怎麼做，可以參考其他教學：



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## 啟動 Trezor Model One



將您的 Model One 連接到已安裝 Trezor Suite 和 Sparrow Wallet 的電腦。



![Image](assets/fr/04.webp)



開啟 Trezor Suite，然後按一下「*設定我的 Trezor*」。



![Image](assets/fr/05.webp)



選取「*Bitcoin-only 韌體*」，然後按一下「*Install Bitcoin-only*」。



![Image](assets/fr/06.webp)



Trezor Suite 會在您的 Model One 上安裝韌體。安裝期間請稍候。



![Image](assets/fr/07.webp)



按一下「*繼續*」。



![Image](assets/fr/08.webp)



## 建立 Bitcoin 產品組合



在 Trezor Suite 上，按一下「*建立新的 Wallet*」按鈕。



![Image](assets/fr/09.webp)



接受 Hardware Wallet 上的使用條款。



![Image](assets/fr/10.webp)



在 Trezor Suite 中，按一下「*繼續備份*」。



![Image](assets/fr/11.webp)



軟體提供如何管理 Mnemonic 詞組的說明。



這個 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins。任何持有此短語的人都可以盜取您的資金，即使沒有實體存取您的 Trezor Model One。



如果您的 Hardware Wallet 遺失、被盜或破損，這 24 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。



您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。



確認指示，然後按一下「*建立 Wallet 備份*」按鈕。



![Image](assets/fr/12.webp)



Model One 會使用隨機數字產生器建立您的 Mnemonic 詞組。請確定在此操作過程中沒有人在看著您。在您選擇的實體媒體上寫下螢幕上提供的詞組。根據您的安全策略，您可以考慮製作幾份完整的短語實體複本 (但最重要的是，不要將它分割)。重要的是要保持字詞的編號和順序。



***顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會在 Testnet 上使用，並會在教學結束時刪除。



如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

若要進入下一個單字，請按一下滑鼠右鍵。記下所有單字後，再次按一下滑鼠右鍵進入下一步。



![Image](assets/fr/13.webp)



您的 Hardware Wallet 再次顯示您所有的單字。檢查您是否都寫下來了。



![Image](assets/fr/14.webp)



## 設定 PIN 碼



接下來是 PIN 碼步驟。PIN 碼可以解鎖您的 Trezor。因此可防止未經授權的實體存取。PIN 碼並不參與 Wallet 密鑰的產生。因此，即使無法獲得 PIN 碼，擁有 12 個字的 Mnemonic 短語也能讓您重新獲得比特幣。



在 Trezor Suite 上，點擊 「*繼續 PIN*」，然後點擊 「*設定 PIN*」按鈕。



![Image](assets/fr/15.webp)



在 Model One 上確認。



![Image](assets/fr/16.webp)



我們建議您選擇一個盡可能隨機的 PIN 碼。請務必將此密碼保存在與您的 Trezor 儲存位置不同的地方（例如密碼管理器）。您可以定義一個 8 到 50 位數的 PIN 碼。我建議您選擇盡可能長的 PIN 碼，以提高安全性。



PIN 碼必須在電腦上的 Trezor Suite 中根據 Trezor Model One 上顯示的鍵盤配置，點擊相應數字的點來輸入。



無論是透過 Trezor Suite 或 Sparrow Wallet 解鎖，每次解鎖 Trezor Model One 時都需要輸入特定的 PIN 碼。



![Image](assets/fr/17.webp)



完成後，按一下「*Enter PIN*」按鈕。



![Image](assets/fr/18.webp)



再次寫下您的 PIN 碼以確認。



![Image](assets/fr/19.webp)



在 Trezor Suite 上，按一下「*完成設定*」按鈕。



![Image](assets/fr/20.webp)



您的 Model One 設定至此完成。如果您願意，可以變更 Hardware Wallet 的名稱和首頁。



![Image](assets/fr/21.webp)



我們不再需要 Trezor Suite 軟體了，除了定期對 Hardware Wallet 進行韌體更新，或者如果您想進行恢復測試。我們現在要使用 Sparrow 來管理組合，因為這個軟體非常適合 Bitcoin 專用。



## 在 Sparrow Wallet 上設定投資組合



如果您還沒有下載 Sparrow Wallet [從官方網站](https://sparrowwallet.com/) 並安裝到您的電腦上，請從此開始。



開啟 Sparrow Wallet 後，請確定軟體已連接到 Bitcoin 節點，Interface 右下角的勾號表示該節點。如果您在連接 Sparrow 時遇到問題，建議您參考本教學的開頭部分：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。



![Image](assets/fr/22.webp)



命名您的投資組合，然後按一下「*建立 Wallet*」。



![Image](assets/fr/23.webp)



在 "*Script Type*"下拉菜單中，選擇用來保護比特幣的腳本類型。我推薦 "*Taproot*「，或者如果不行的話，」*Native SegWit*"。



![Image](assets/fr/24.webp)



按一下「*已連線的 Hardware Wallet*」按鈕。當然，您的 Model One 必須已連接到電腦。



![Image](assets/fr/25.webp)



按一下「*掃描*」按鈕。您的 Model One 應該會出現。



當您將 Model One 連接到開啟 Sparrow Wallet 的電腦時，系統會提示您在 Sparrow 上輸入 passphrase BIP39。這個進階選項將會在未來的教學中介紹。目前，您只需選擇 "*Toggle passphrase Off*"，即可避免 Trezor 每次啟動時都提示您輸入 passphrase。



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



按一下「*匯入金鑰儲存庫*」。



![Image](assets/fr/27.webp)



現在您可以看到 Wallet 的詳細資訊，包括第一個帳號的擴充公開金鑰。點選「*Apply*」按鈕，完成 Wallet 的建立。



![Image](assets/fr/28.webp)



選擇一個強大的密碼，以確保對 Sparrow Wallet 的安全存取。此密碼將確保安全存取您的 Sparrow Wallet 資料，保護您的公開金鑰，地址，標籤和交易歷史，防止未經授權的存取。



我建議您將此密碼儲存在密碼管理器中，以免忘記。



![Image](assets/fr/29.webp)



現在您的投資組合已匯入 Sparrow Wallet！



![Image](assets/fr/30.webp)



在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行空幣恢復測試**。寫下一些參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重設您的 Trezor Model One。然後嘗試使用您的紙張備份在 Trezor 上還原您的 Wallet。檢查還原後生成的 xpub 是否與您最初寫下的相符。如果吻合，您就可以放心，您的紙張備份是可靠的。



若要進一步瞭解如何執行復原測試，我建議您參閱此其他教學：



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 如何使用 Trezor Model One 接收比特幣？



在 Sparrow 上，按一下「*接收*」標籤。



![Image](assets/fr/31.webp)



在使用 Sparrow Wallet 提出的 Address 之前，請在您的 Trezor 螢幕上檢查。這種做法可以讓您確認 Sparrow 上顯示的 Address 不是偽造的，而且 Hardware Wallet 確實持有隨後使用此 Address 所保護的比特幣所需的私密金鑰。這可以幫助您避免幾種類型的攻擊。



若要執行此檢查，請按一下「*顯示 Address*」按鈕。



![Image](assets/fr/32.webp)



檢查您 Trezor 上顯示的 Address 是否與 Sparrow Wallet 上的相符。建議您在傳送 Address 給寄件者之前進行這項檢查，以確定其有效性。您可以按右鍵來確認。



![Image](assets/fr/33.webp)



您也可以加入一個 "*Label*" 來描述這個 Address 將要保護的 bitcoins 來源。這是一個很好的做法，可以讓您更好地管理您的 UTXO。



![Image](assets/fr/34.webp)



然後您就可以使用這個 Address 來接收比特幣。



![Image](assets/fr/35.webp)



## 如何使用 Trezor Model One 傳送 bitcoins？



現在您已經在您的第一型加密 Wallet 中收到了第一筆 Satss，您也可以花掉它們了！將您的 Trezor 連接到電腦，啟動 Sparrow Wallet，然後到「*Send*」標籤建立新的交易。



![Image](assets/fr/36.webp)



如果您希望*Coin Control*，即在交易中特別選擇消耗哪些 UTXOs，請前往「*UTXOs*」標籤。選擇您要消耗的 UTXOs，然後點擊 「*發送所選*」。您將被重新導向至 「*發送*」標籤中的相同畫面，但您已為交易選擇了UTXO。



![Image](assets/fr/37.webp)



輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。



![Image](assets/fr/38.webp)



寫下「*標籤*」以記住此支出的目的。



![Image](assets/fr/39.webp)



選擇要傳送到此 Address 的金額。



![Image](assets/fr/40.webp)



根據當前市場調整您的交易費率。例如，您可以使用 [Mempool.space](https://Mempool.space/) 來選擇合適的費率。



確定所有交易參數都正確，然後按一下「*建立交易*」。



![Image](assets/fr/41.webp)



如果一切都令您滿意，請按一下「*完成簽署交易*」。



![Image](assets/fr/42.webp)



按一下「*簽署*」。



![Image](assets/fr/43.webp)



點選您的 Trezor Model One 旁邊的「*簽署*」。



![Image](assets/fr/44.webp)



檢查 Hardware Wallet 畫面上的交易參數，包括收件人的接收 Address、發送金額和費用。交易在 Trezor 上驗證完成後，按滑鼠右鍵簽名。



![Image](assets/fr/45.webp)



您的交易現在已經簽章。最後一次檢查是否一切正常，然後按一下「*廣播交易*」，在 Bitcoin 網路上廣播。



![Image](assets/fr/46.webp)



您可以在 Sparrow Wallet 的「*交易*」標籤中找到它。



![Image](assets/fr/47.webp)



恭喜您，現在您已經掌握了 Trezor Model One 與 Sparrow Wallet 的基本使用方法！為了讓您更進一步，我向您推薦這份關於使用 Hardware Wallet Trezor 與 passphrase BIP39 的全面教學，以加強您的安全 ：



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。非常感謝