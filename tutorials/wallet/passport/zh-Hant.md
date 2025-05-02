---
name: 護照 - 基金會
description: 在手动模式下配置和使用 Passport Hardware Wallet
---
![cover](assets/cover.webp)


Passport 是僅限 Bitcoin 的 Hardware Wallet，由 2020 年 4 月在波士頓成立的美國公司 Foundation Devices 設計。


本教學中介紹的 Passport "*Batch 2*「 是 」*Founder's Edition*" 的後繼機種。它以其優質的設計、高解析度彩色螢幕和符合人體工學的實體鍵盤脫穎而出。它以 "*Air-Gap*"模式運作，可確保 Wallet 的私密金鑰完全隔離，並可透過 MicroSD 卡或 QR 代碼進行通訊。本裝置配備可拆卸、可充電的諾基亞 BL-5C 電池，容量為 1200 mAh。由於 BL-5C 型號可在商店中廣泛買到，因此可輕鬆更換此非專屬電池。


連線方面，Passport 配備 MicroSD 連接埠、用於充電的 USB-C 連接埠，以及用於掃描 QR 碼的後置攝影機。


在安全性方面，Passport 加入了安全元件，裝置的原始碼完全開放原始碼。它提供良好的 Bitcoin Hardware Wallet 應有的所有功能。請注意，Passport 尚未支援 miniscript，但已計劃在 2025 年第二季推出此功能。


Passport 定價 199 美元，定位為高階 Hardware Wallet，與 Coldcard Q、Jade Plus、Tezor Safe 5 和 Ledger 的頂級機種競爭。


![Image](assets/fr/01.webp)


若要在 Passport 上管理您的安全 Wallet，您有多種選擇。此 Hardware Wallet 可與市面上大多數的 Wallet 管理軟體相容，包括 Sparrow Wallet、Specter Desktop、Nunchuk、Keeper 等。在本教程中，我們將學習如何將它與 Sparrow Wallet 搭配使用。


如果您是初學者，最簡單的方法是使用由 Foundation 開發的原生 Envoy 應用程式來使用 Passport。若要瞭解如何在 Passport 上使用 Envoy，請參閱其他教學：


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## 護照開箱


當您收到 Passport 時，請確定包裝盒和紙箱上的 Seal 完好無損，以確認包裝未被打開。裝置設定時，也會進行軟體驗證，確認裝置的真實性和完整性。


![Image](assets/fr/02.webp)


盒內物品包括 ：




- 護照；
- 一張紙板，用來寫下您的 Mnemonic 詞句；
- 用於充電的 USB-C 連接線 ；
- MicroSD 卡 ；
- 兩個 MicroSD 至 Lightning 或 USB-C 轉接器 ；
- 貼紙。


在裝置上，您會發現 ：




- 鍵盤 (1) ；
- USB-C 連接埠 (2)；
- 刪除按鈕 (3)；
- 返回按鈕 (4) ；
- 確認按鈕 (5)；
- 方向墊 (6)；
- 開關按鈕 (7)；
- 狀態指示燈 (8)；
- MicroSD 連接埠 (9) ；
- A 按鈕可變更模式 aA1 (10) ；
- 後置攝影機。


![Image](assets/fr/03.webp)


## 起始護照


按機器側邊的開關按鈕啟動。


![Image](assets/fr/04.webp)


按確認按鈕進入下一個功能表。


![Image](assets/fr/05.webp)


在本教程中，我們將使用 Sparrow Wallet 來管理 Passport 加密的 Wallet。選擇「*手動設定*」。


![Image](assets/fr/06.webp)


然後接受使用條款。


![Image](assets/fr/07.webp)


下一步是檢查您的裝置。這將確認您護照的真實性，並確保它在運送途中未被篡改。您會被要求掃描一個 QR 代碼。


![Image](assets/fr/08.webp)


前往 [官方驗證網站](https://validate.foundationdevices.com/)，選擇「*護照*」。


![Image](assets/fr/09.webp)


使用 Passport 的相機掃描網站上顯示的 QR 代碼。


![Image](assets/fr/10.webp)


接著您的裝置會顯示 4 個字。


![Image](assets/fr/11.webp)


在網站上輸入這些字詞以確認您護照的真實性，然後按一下「*驗證*」。


![Image](assets/fr/12.webp)


如果出現「*Passed*」訊息，表示您的 Hardware Wallet 是真品。現在您可以用它來保護 Bitcoin Wallet。


![Image](assets/fr/13.webp)


確認護照上的測試結果。


![Image](assets/fr/14.webp)


## 設定 PIN 碼


接下來是 PIN 碼步驟。PIN 碼可以解鎖您的護照。因此，它可防止未經授權的實體存取。PIN 碼不涉及 Wallet 密鑰的產生。因此，即使無法取得 PIN 碼，只要擁有 12 或 24 個字的 Mnemonic 詞組，就能重新取得您的 bitcoins。


![Image](assets/fr/15.webp)


我們建議您選擇一個盡可能隨機的 PIN 碼。此外，請務必將此密碼保存在與您的 Passport 儲存位置不同的地方（例如密碼管理器）。


您可以選擇 6 到 12 位數的 PIN 碼。我建議您盡可能將其設長。


使用鍵盤輸入 PIN 碼。完成後，按一下確認按鈕。


![Image](assets/fr/16.webp)


再次確認您的 PIN 碼。


![Image](assets/fr/17.webp)


您的 PIN 碼已註冊。


![Image](assets/fr/18.webp)


## 更新 Passport 韌體


您的 Hardware Wallet 建議您更新韌體。我建議您立即更新，以受益於最新版本帶來的改進和修正。若要繼續，請按一下右側的確認按鈕。


![Image](assets/fr/19.webp)


您的 Passport 已準備好透過 MicroSD 卡接收新的韌體。


![Image](assets/fr/20.webp)


若要執行此動作，請使用 Passport 盒子中隨附的 MicroSD 卡 (或另一張)，並將其插入電腦中。從 [基金會文件網站](https://docs.foundation.xyz/firmware-updates/passport/) 或 [他們的 GitHub 套件庫](https://github.com/Foundation-Devices/passport2/releases) 下載最新的韌體版本。


![Image](assets/fr/21.webp)


在您的裝置上安裝之前，我們強烈建議您檢查下載韌體的真實性和完整性。如果您在這方面需要幫助，請參閱本教程 ：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

檢查`.bin`檔案後，將它放在您的 MicroSD 上，然後將它插入 Passport。Passport 檔案總管將會開啟。選取檔案 `vN.N.N-passport.bin`。


![Image](assets/fr/22.webp)


按一下「*選擇*」。


![Image](assets/fr/23.webp)


然後確認韌體安裝。


![Image](assets/fr/24.webp)


請等待更新完成。


![Image](assets/fr/25.webp)


更新完成後，請輸入 PIN 碼以解除鎖定裝置，並繼續設定。


![Image](assets/fr/26.webp)


## 建立新的 Bitcoin Wallet


現在要建立新的 Bitcoin Wallet。按一下確認按鈕。


![Image](assets/fr/27.webp)


若要建立新的 Wallet，請按一下「*建立新的 seed*」。


![Image](assets/fr/28.webp)


您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。兩種選項所提供的安全性都差不多，因此您可以選擇最容易儲存的選項，也就是 12 個字。


![Image](assets/fr/29.webp)


按一下「*繼續*」。


![Image](assets/fr/30.webp)


您的 Passport 現在會 generate 您的「*備份碼*」。這是一串數字，可用於解密儲存在 MicroSD 上的 Wallet 備份。此備份系統為 Foundation 裝置所特有，構成您 Mnemonic 詞組的額外備份，但與其他 Bitcoin 軟體不相容。


如果您決定使用此 「*備份碼*」，請務必將此 「*備份碼*」保存在與包含 Wallet 加密備份的 MicroSD 不同的位置。但是，如果您認為 Mnemonic 短語的良好備份已經足夠，您可以選擇不使用此系統。


![Image](assets/fr/31.webp)


輸入您的「*備份碼*」，確認您已正確儲存。


![Image](assets/fr/32.webp)


如果已插入 MicroSD，則 Wallet 的加密備份已儲存於此。


![Image](assets/fr/33.webp)


您的 Passport 將顯示您的 12 個字的 Mnemonic 詞組。這個 Mnemonic 可以讓您完全不受限制地存取您所有的 bitcoins。任何擁有此短語的人都可以盜取您的資金，即使沒有實體存取您的護照。


如果您的護照遺失、被盜或破損，這 12 個字的短語可以恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方非常重要。


您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


按一下確認按鈕，即可看到您的 Mnemonic 詞組。


![Image](assets/fr/34.webp)


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

當然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。**_


為這句話做一份實體備份。


![Image](assets/fr/35.webp)


您的 Passport 已成功設定。按一下確認按鈕以繼續。


![Image](assets/fr/36.webp)


## 菜單發現


您的 Passport Interface 有三個主要功能表：




- "*Account*"；
- 「*更多*」；
- "*Settings*".


若要在這些功能表之間導覽，請使用方向鍵上的左右箭頭。


### *帳戶*」功能表


在「*帳戶*」功能表中，您可以找到 Bitcoin Wallet 的主要功能。您可以透過攝影機或 MicroSD 連接埠簽署交易。


![Image](assets/fr/37.webp)


*Account Tools*」子功能表提供多種選項，例如驗證 Address、簽署訊息或查詢 Wallet 中的位址。


![Image](assets/fr/38.webp)


在「*管理帳號*」子功能表中，您可以將 Bitcoin Wallet 連接到 Wallet 管理軟體（我們將在本教學的下一個步驟中介紹），或者檢視和重新命名您的帳號。


![Image](assets/fr/39.webp)


### 更多」功能表


在「*更多*」功能表中，您可以在 Wallet 中建立新帳號，並連結到相同的 Mnemonic 詞組。


![Image](assets/fr/40.webp)


您也可以輸入 BIP39 passphrase（請參閱下一節）或使用臨時 seed。


![Image](assets/fr/41.webp)


### 設定」功能表


在「*設定*」功能表中，您可以找到所有的 Wallet 和裝置設定。


![Image](assets/fr/42.webp)


裝置*」子功能表提供您自訂螢幕亮度、設定自動鎖定前的延遲、變更 PIN 碼或重新命名裝置等選項。


![Image](assets/fr/43.webp)


透過「*備份*」子功能表，您可以匯出加密的 Wallet 備份、檢查現有備份的有效性，或再次查詢「*備份碼*」。


![Image](assets/fr/44.webp)


韌體*」子功能表用於更新 Passport 的韌體。我們建議您定期執行這些更新，以受惠於最新的修正和功能。


![Image](assets/fr/45.webp)


*Bitcoin*「子功能表可讓您變更顯示的單位（BTC 或 Satoshis）、管理可能的 Multisig Wallet，或切換至 」*Testnet*"模式。


![Image](assets/fr/46.webp)


在「*進階*」中，您可以檢視 Mnemonic 詞組的字句、對插入的 MicroSD 執行動作、將 Passport 重設為出廠設定，或執行先前執行的真實性檢查。


![Image](assets/fr/47.webp)


您可以啟動「*Security Words*」，此功能可在輸入 PIN 碼的前四位數後解除鎖定裝置時，顯示兩個特定的詞彙，以增加 Layer 的安全性。這些字詞會在設定時儲存，以確保 Passport 未被更換或竄改。如果日後發現任何不符，我們建議您不要使用裝置。我建議您啟動此選項，以防止裝置受到實體損害的大部分風險。


![Image](assets/fr/48.webp)


最後，「*擴充功能*」子功能表可讓您啟動裝置特定用途的功能，例如 Whirlpool CoinJoin 通訊協定。


![Image](assets/fr/49.webp)


## 新增 BIP39 passphrase


在繼續之前，如果您願意的話，可以加入 BIP39 passphrase。BIP39 passphrase 是您可以自由選擇的密碼，它會加入您的 Mnemonic 詞組，以加強 Wallet 的安全性。啟用此功能後，存取您的 Bitcoin Wallet 需要同時使用 Mnemonic 和 passphrase。如果沒有這兩個密碼，就無法恢復 Wallet。


在您的 Passport 上設定此選項之前，強烈建議您閱讀這篇文章，以充分瞭解 passphrase 的理論操作，並避免可能導致您遺失比特幣的錯誤：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

若要啟動它，請移至「*更多*」功能表，然後按一下「*進入 passphrase*」。


![Image](assets/fr/50.webp)


使用 aA1 鍵盤輸入您的 passphrase，並確保在實體媒體 (紙張或金屬) 上儲存一次或多次。在範例中，我使用的是非常弱的 passphrase，但您應該選擇一個強大、隨機的 passphrase，包括所有字元類型，而且要夠長 (就像強密碼一樣)。


![Image](assets/fr/51.webp)


請注意，BIP39 密碼對大小寫和錯字都很敏感。如果您輸入的 passphrase 與最初設定的略有不同，Passport 將不會報錯，但會衍生出另一套密碼金鑰，而這些密碼金鑰與您最初 Wallet 中的密碼金鑰不同。


因此，在設定時，記下下一步會給您的主密鑰指紋是很重要的。例如，在我的 passphrase `Plan B Network` 中，我的主密鑰指紋是 `745D526B`。


![Image](assets/fr/52.webp)


每次解鎖 Passport 時，您都需要返回此功能表輸入您的 passphrase，並將其套用至 Wallet。Passport 不會儲存 passphrase。


每次解鎖時，在寫下 passphrase 之後，請在此確認畫面上檢查所提供的指紋是否與您在設定時寫下的指紋相同。如果是，則表示您的 passphrase 是正確的，而且您正在存取正確的 Bitcoin Wallet。如果不一致，則表示您進入了錯誤的 Wallet，需要重新嘗試，注意不要有任何輸入錯誤。


在您的 Wallet 上收到您的第一個 bitcoins 之前，**我強烈建議您執行一個空的恢復測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Passport 上刪除您的 Wallet，而它仍然是空的（`設置 -> 進階 -> 刪除 Passport`）。然後嘗試使用您的 Mnemonic 短語和任何 passphrase 的紙張備份還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果相符，您就可以放心，您的紙本備份是可靠的。要瞭解有關如何進行測試復原的更多資訊，請參閱此其他教程 ：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## 在 Sparrow Wallet 上設定 Wallet


在本教程中，我將為您展示 Passport 與 Sparrow Wallet 的進階用法。不過，這款 Hardware Wallet 也相容於 Envoy (基礎應用程式)、Keeper、BlueWallet、Nunchuk、Specter 等...


如果您尚未下載 Sparrow Wallet [從官方網站](https://sparrowwallet.com/)，請先將其下載並安裝到您的電腦上。


![Image](assets/fr/54.webp)


安裝前請務必檢查軟體的真實性和完整性。如果您不知道如何操作，請參閱本教程：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

開啟 Sparrow Wallet 後，按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。


![Image](assets/fr/55.webp)


命名您的 Wallet，然後按一下「*建立 Wallet*」。


![Image](assets/fr/56.webp)


選擇 "*Airgapped Hardware Wallet*"。


![Image](assets/fr/57.webp)


按一下「*Passport*」選項旁邊的「*Scan...*」。這將會開啟您的網路攝影機。


![Image](assets/fr/58.webp)


在 Hardware Wallet 上，移至「*Account*」功能表，選擇「*Manage Account*」子功能表，然後按一下「*Connect Wallet*」。


![Image](assets/fr/59.webp)


在出現的下拉清單中，選擇「*Sparrow*」。


![Image](assets/fr/60.webp)


然後選擇「*Single-sig*」，以獲得不含 Multisig 的一般設定。


![Image](assets/fr/61.webp)


選擇「*QR Code*」選項。


![Image](assets/fr/62.webp)


然後，您的 Passport 將會出現 generate 動態 QR 代碼。使用電腦的網路攝影機，將它們掃描到 Sparrow 軟體中。


![Image](assets/fr/63.webp)


現在您應該可以看到您的 xpub 和您的主密碼指紋，這些指紋應該與您輸入 passphrase 時在護照上顯示的指紋相符。按一下「*應用*」按鈕。


![Image](assets/fr/64.webp)


設定一個強大的密碼，以確保存取 Sparrow Wallet 的安全性。此密碼將保護您的公開金鑰，地址，標籤和交易歷史，防止未經授權的訪問。最好將此密碼儲存在密碼管理器中，以免忘記。


![Image](assets/fr/65.webp)


然後，您的 Passport 會提示您掃描第一次接收的 Address，以確認匯入成功。


![Image](assets/fr/66.webp)


在 Sparrow 中，移至「*接收*」標籤，掃描第一個 Address 的 QR 代碼。


![Image](assets/fr/67.webp)


如果操作成功，您的 Passport 將顯示「*已驗證*」。


![Image](assets/fr/68.webp)


這證明匯入成功。


![Image](assets/fr/69.webp)


## 接收比特幣


現在您的 Passport 已經設定好了，您可以在新的 Bitcoin Wallet 上接收第一個 Sats。要這樣做，在 Sparrow 上按一下「*接收*」功能表。


![Image](assets/fr/70.webp)


Sparrow 會在您的 Wallet 中顯示第一張空白收據 Address。您可以新增一個標籤。


![Image](assets/fr/71.webp)


在使用之前，我們先在 Passport 畫面上確認 Address 是否屬於我們的 Bitcoin Wallet。在 Sparrow 上，如有必要，您可以點選 Address 的 QR 碼來放大它。在 Passport 的「*帳號*」功能表中，選擇「*帳號工具*」。


![Image](assets/fr/72.webp)


按一下「*Verify Address*」，然後掃瞄 Sparrow Wallet 上顯示的 QR 代碼。


![Image](assets/fr/73.webp)


確定 Passport 上顯示的 Address 與 Sparrow 上顯示的 Address 完全符合，並顯示「*Verified*」。


![Image](assets/fr/74.webp)


現在您可以用它來接收 bitcoins。當交易在網路中廣播時，就會出現在 Sparrow 上。等到您收到足夠的確認後，交易才算確定。


![Image](assets/fr/75.webp)


## 發送比特幣


現在您的 Wallet 中已有一些 Sats，您也可以傳送一些。要這樣做，請按一下「*UTXOs*」功能表。


![Image](assets/fr/76.webp)


選擇您希望用作此交易輸入的 UTXO，然後按一下「*送出所選*」。


![Image](assets/fr/77.webp)


輸入收款人的 Address、提醒您交易目的的標籤，以及您希望寄往此 Address 的金額。


![Image](assets/fr/78.webp)


根據目前的市場狀況調整收費率，然後按一下「*建立交易*」。


![Image](assets/fr/79.webp)


檢查所有交易參數是否正確，然後按一下「*完成簽署交易*」。


![Image](assets/fr/80.webp)


點擊 "*Show QR*"顯示 PSBT (*Partially Signed Bitcoin Transaction*)。Sparrow 已經建立了交易，但仍缺乏簽章來解鎖輸入中使用的 bitcoins。這些簽章只能由 Passport 執行，Passport 擁有您的 seed，可以存取簽章交易所需的私密金鑰。


![Image](assets/fr/81.webp)


在您的 Passport 上，存取「*帳戶*」功能表，然後按一下「*使用 QR 碼*簽名」。


![Image](assets/fr/82.webp)


掃描 Sparrow Wallet 上顯示的 PSBT (*Partially Signed Bitcoin Transaction*)。


![Image](assets/fr/83.webp)


確認接收的 Address 和傳送的金額是否正確，然後按下確認鍵。


![Image](assets/fr/84.webp)


檢查 Exchange Address。在我的範例中，沒有，因為交易包括單一輸出。


![Image](assets/fr/85.webp)


請確定費用是您所選擇的。


![Image](assets/fr/86.webp)


如果所有資訊都正確無誤，請按一下確認按鈕簽署交易。


![Image](assets/fr/87.webp)


在 Sparrow Wallet 上，按一下「*掃描 QR*」，然後掃描您護照上顯示的 QR 代碼。


![Image](assets/fr/88.webp)


您已簽署的交易現在可以在 Bitcoin 網路上廣播，並由 Miner 包含在區塊中。如果一切正常，請按一下「*廣播交易*」。


![Image](assets/fr/89.webp)


您的交易已被廣播，正在等待確認。


![Image](assets/fr/90.webp)


恭喜您，現在您已經知道如何設定及使用 Passport。如果您覺得這篇教學有用，請在下方留下 Green 的拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。感謝您的分享！


如需詳細資訊，請參閱我們的 Liana 軟體教學：


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04