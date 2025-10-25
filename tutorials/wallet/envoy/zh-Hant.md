---
name: Envoy
description: 使用 Envoy 應用程式設定和使用 Passport
---
![cover](assets/cover.webp)


Envoy 是 Foundation 開發的 Bitcoin Wallet 管理應用程式。它是專為搭配 Passport Hardware Wallet 使用而設計的。


本教學中介紹的 Passport "*Batch 2*「 搭配 Envoy 應用程式，是 」*Founder's Edition*" 的後繼機種。它以優質的設計、高解析度彩色螢幕和符合人體工學的實體鍵盤脫穎而出。它以「*Air-Gap*」模式運作，可確保 Wallet 的私人密碼匙完全隔離，並可透過 MicroSD 卡或 QR 碼進行通訊。本裝置配備可拆卸、可充電的諾基亞 BL-5C 電池，容量為 1200 mAh。由於 BL-5C 型號可在商店中廣泛買到，因此可輕鬆更換此非專屬電池。


連線方面，Passport 配備 MicroSD 連接埠、用於充電的 USB-C 連接埠，以及用於掃描 QR 碼的後置攝影機。


在安全性方面，Passport 加入了安全元件，裝置的原始碼完全開放原始碼。它提供良好的 Bitcoin Hardware Wallet 應有的所有功能。請注意，Passport 尚未支援 miniscript，但已計劃在 2025 年第二季推出此功能。


Passport 定價 199 美元，定位為高階 Hardware Wallet，與 Coldcard Q、Jade Plus、Tezor Safe 5 和 Ledger 的頂級機種競爭。


![Image](assets/fr/01.webp)


若要在 Passport 上管理您的安全 Wallet，您有多種選擇。此 Hardware Wallet 與市面上大多數的 Wallet 管理軟體相容，包括 Sparrow Wallet、Specter Desktop、Nunchuk、Keeper 等。


本教學主要針對初級和中級使用者，我們將探討如何在 Passport 上使用 Envoy 應用程式。這是充分利用 Hardware Wallet 的最簡單方法。


如果您是進階使用者，並想要探索更複雜的功能，我建議您參閱另一篇教學，我們在其中使用 Sparrow Wallet 設定 Passport：


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## 護照開箱


當您收到 Passport 時，請確定包裝盒和紙箱上的 Seal 完好無損，以確認包裝未被打開。裝置設定時，也會進行軟體驗證，確認裝置的真實性和完整性。


![Image](assets/fr/02.webp)


盒內物品包括 ：




- 護照；
- 一張紙板，用來寫下您的 Mnemonic 詞組；
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


## 下載 Envoy 應用程式


前往您的應用程式商店下載 Envoy ：




- 在 [Google Play 商店](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy)；
- 在 [App Store](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818) 上；
- 關於 [F-Cold](https://foundation.xyz/fdroid/)。


![Image](assets/fr/50.webp)


您也可以直接 [從 Foundation 的 GitHub 套件庫] 下載 APK 檔案(https://github.com/Foundation-Devices/envoy/releases)。


![Image](assets/fr/51.webp)


開啟應用程式後，選擇「*管理護照*」。


![Image](assets/fr/52.webp)


選擇是否要啟動 Tor 連線以強化保密性，然後按「*繼續*」。


![Image](assets/fr/53.webp)


如果您的 Passport 已經設定好，請選擇「*連線現有的 Passport*」；如果您是第一次初始化 Hardware Wallet，請選擇「*設定新的 Passport*」。


![Image](assets/fr/54.webp)


接受使用條款。


![Image](assets/fr/55.webp)


然後，您會被要求驗證護照的真偽。按一下「*下一步*」。


![Image](assets/fr/56.webp)


## 起始護照


按機器側邊的開關按鈕啟動。


![Image](assets/fr/04.webp)


按確認按鈕進入下一個功能表。


![Image](assets/fr/05.webp)


在本教程中，我們將使用 Envoy 來管理 Passport 加密的 Wallet。選擇「*Envoy App*」。


![Image](assets/fr/57.webp)


按一下「*繼續在 Envoy* 上」。


![Image](assets/fr/58.webp)


下一步是檢查您的裝置。這將確認您護照的真實性，並確保它在運送途中未被篡改。您會被要求掃描一個 QR 代碼。


![Image](assets/fr/08.webp)


使用您的護照掃描應用程式中顯示的動態 QR 碼。掃描完成後，請按一下「*下一步*」。


![Image](assets/fr/59.webp)


然後用手機掃描您護照上顯示的 QR 代碼。


![Image](assets/fr/60.webp)


如果出現 「*Your Passport is secure*（您的護照安全）」訊息，即證明您的 Hardware Wallet 是真品。現在您可以用它來保護 Bitcoin Wallet。


![Image](assets/fr/61.webp)


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


### 沒有 Envoy 應用程式


若要執行此動作，請使用 Passport 盒子中隨附的 MicroSD 卡 (或另一張)，並將其插入電腦中。從 [基金會文件網站](https://docs.foundation.xyz/firmware-updates/passport/) 或 [他們的 GitHub 套件庫](https://github.com/Foundation-Devices/passport2/releases) 下載最新的韌體版本。


![Image](assets/fr/21.webp)


在您的裝置上安裝之前，我們強烈建議您檢查下載韌體的真實性和完整性。如果您在這方面需要幫助，請參閱本教程 ：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 使用 Envoy 應用程式


另一個更簡單的方法是直接使用 Envoy 應用程式。按一下「*下載韌體*」。


![Image](assets/fr/62.webp)


使用 Passport 隨附的轉接卡將 MicroSD 卡連接到您的手機。


![Image](assets/fr/63.webp)


在檔案總管中選擇要儲存韌體的 MicroSD 卡。


![Image](assets/fr/64.webp)


韌體已儲存。從智慧型手機中取出 MicroSD 並將其插入 Passport。


![Image](assets/fr/65.webp)


Passport 檔案總管將會開啟。選擇檔案 `vN.N.N-passport.bin`。


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


您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。這兩種選項所提供的安全性相似，因此您可以選擇最容易儲存的選項，即 12 個字。


![Image](assets/fr/29.webp)


按一下「*繼續*」。


![Image](assets/fr/30.webp)


您的 Passport 現在會 generate 您的「*備份碼*」。這是一串數字，可用於解密儲存在 MicroSD 上的 Wallet 備份。此備份系統是 Foundation 裝置特有的，構成您 Mnemonic 樂句的額外備份，但與其他 Bitcoin 軟體不相容。


如果您決定使用此「*備份碼*」，請務必將此「*備份碼*」保存在與包含 Wallet 加密備份的 MicroSD 不同的位置。但是，如果您認為 Mnemonic 短語的良好備份已經足夠，則可以選擇不使用此系統。


![Image](assets/fr/31.webp)


輸入您的「*備份碼*」，確認您已正確儲存。


![Image](assets/fr/32.webp)


如果已插入 MicroSD，則 Wallet 的加密備份已儲存於此。


![Image](assets/fr/33.webp)


您的 Passport 將顯示 12 個字的 Mnemonic 詞組。這個 Mnemonic 可以讓您完全不受限制地存取您所有的 bitcoins。任何擁有這個短語的人都可以盜取您的資金，即使沒有實體存取您的護照。


如果您的護照遺失、被盜或破損，這 12 個字的短語可以恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方非常重要。


您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


按一下確認按鈕，即可看到您的 Mnemonic 詞組。


![Image](assets/fr/34.webp)


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

當然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。


為這句話做一份實體備份。


![Image](assets/fr/35.webp)


您的 Passport 已成功設定。按一下確認按鈕以繼續。


![Image](assets/fr/36.webp)


## 在 Envoy 上設定 Wallet


在本教程中，我將教您如何將 Passport 與 Envoy 應用程式搭配使用。不過，這個 Hardware Wallet 也相容於 Sparrow Wallet、Keeper、BlueWallet、Nunchuk、Specter 等...


![Image](assets/fr/66.webp)


使用 Envoy 應用程式掃描您護照上顯示的 QR 代碼。


![Image](assets/fr/67.webp)


您的公開金鑰現在已匯入應用程式。按一下「*驗證接收 Address*」。


![Image](assets/fr/68.webp)


使用您的護照掃描 Envoy 上顯示的 Address。


![Image](assets/fr/69.webp)


您的護照將確認在 Envoy 匯入的 Wallet 是否有效。請在申請時確認。


![Image](assets/fr/70.webp)


您現在可以在 Envoy 上存取 Wallet 的公開資訊，但若要花費 bitcoins，您需要使用您的 Passport。


![Image](assets/fr/71.webp)


## 發現護照菜單


您的 Passport Interface 有三個主要功能表：




- "*Account*"；
- 「*更多*」；
- "*Settings*".


若要在這些功能表之間導覽，請使用方向鍵上的左右箭頭。


### *帳戶*」功能表


在「*帳戶*」功能表中，您可以找到 Bitcoin Wallet 的主要功能。您可以透過攝影機或 MicroSD 連接埠簽署交易。


![Image](assets/fr/37.webp)


*Account Tools*」子功能表提供驗證 Address、簽署訊息或查詢 Wallet 中的位址等選項。


![Image](assets/fr/38.webp)


在「*管理帳號*」子功能表中，您可以將 Bitcoin Wallet 連接到 Wallet 管理軟體（我們將在本教學的下一個步驟中介紹），或者檢視和重新命名您的帳號。


![Image](assets/fr/39.webp)


### 更多」功能表


在「*更多*」功能表中，您可以在 Wallet 中建立新帳號，並連結至相同的 Mnemonic 詞組。


![Image](assets/fr/40.webp)


您也可以輸入 BIP39 passphrase 或使用臨時 seed。


![Image](assets/fr/41.webp)


### 設定」功能表


在「*設定*」功能表中，您可以找到所有的 Wallet 和裝置設定。


![Image](assets/fr/42.webp)


裝置」子功能表提供您自訂螢幕亮度、設定自動鎖定前的延遲、變更 PIN 碼或重新命名裝置等選項。


![Image](assets/fr/43.webp)


透過「*備份*」子功能表，您可以匯出加密的 Wallet 備份、檢查現有備份的有效性，或再次查詢「*備份碼*」。


![Image](assets/fr/44.webp)


韌體*」子功能表用於更新 Passport 的韌體。我們建議您定期執行這些更新，以受惠於最新的修正和功能。


![Image](assets/fr/45.webp)


*Bitcoin*「子功能表可讓您變更顯示的單位（BTC 或 Satoshis）、管理可能的 Multisig Wallet，或切換至 」*Testnet*"模式。


![Image](assets/fr/46.webp)


在「*進階*」中，您可以檢視 Mnemonic 詞組的字句、對插入的 MicroSD 執行動作、將 Passport 重設為出廠設定，或執行先前執行的真實性檢查。


![Image](assets/fr/47.webp)


您可以啟動 "*Security Words*"，此功能可在輸入 PIN 碼的前四位數後解除鎖定裝置時顯示兩個特定字詞，以增加 Layer 的安全性。這些字詞會在設定時儲存，以確保 Passport 未被更換或竄改。如果日後發現任何不符，我們建議您不要使用裝置。我建議您啟動此選項，以防止裝置受到實體損害的大部分風險。


![Image](assets/fr/48.webp)


最後，「*擴充功能*」子功能表可讓您啟動裝置特定用途的功能，例如 Whirlpool CoinJoin 通訊協定。


![Image](assets/fr/49.webp)


## 接收比特幣


現在您的 Passport 已經設定完成，您可以在新的 Bitcoin Wallet 上接收第一個 Sats。為此，請在 Envoy 上點選您的「*Primary 0*」帳戶。


![Image](assets/fr/72.webp)


按一下「*接收*」按鈕。


![Image](assets/fr/73.webp)


您的 Envoy 應用程式會在 Wallet 上顯示第一個可用的空白 Address。在使用之前，讓我們先檢查 Passport 螢幕上的 Address，確定它真的屬於我們的 Bitcoin Wallet。在 Passport 的「*帳戶*」功能表中，選擇「*帳戶工具*」。


![Image](assets/fr/74.webp)


點選「*Verify Address*」，然後掃描 Envoy 上顯示的 QR 代碼。


![Image](assets/fr/75.webp)


確定 Passport 上顯示的 Address 與 Sparrow 上顯示的 Address 完全符合，並顯示「*Verified*」。


![Image](assets/fr/76.webp)


現在您可以用它來接收 bitcoins。當交易在網路中廣播時，就會出現在 Envoy 上。等到您收到足夠的確認，才會認為交易是確實的。


![Image](assets/fr/77.webp)


## 發送比特幣


現在您的 Wallet 中已有一些 Sats，您也可以傳送一些。要這樣做，請按一下「*傳送*」按鈕。


![Image](assets/fr/78.webp)


輸入收件人的 Address，可以直接貼入，或使用智慧型手機的相機掃描 QR 代碼。


![Image](assets/fr/79.webp)


確定您要傳送的金額，然後按一下「*確認*」。


![Image](assets/fr/80.webp)


根據當前市場情況選擇交易費用，然後檢查交易資訊。如果一切無誤，點擊 「*使用護照簽名*」。


![Image](assets/fr/81.webp)


在交易上加上標籤，以便清楚記錄交易目的。


![Image](assets/fr/82.webp)


Envoy 會顯示 PSBT (*Partially Signed Bitcoin Transaction*)。應用程式已建立交易，但仍缺少簽章來解鎖輸入中使用的比特幣。這些簽章只能由 Passport 執行，Passport 擁有您的 seed，可以存取簽章交易所需的私人金鑰。


![Image](assets/fr/83.webp)


在您的 Passport 上，存取「*帳戶*」功能表，然後按一下「*使用 QR 碼*簽名」。


![Image](assets/fr/84.webp)


掃描 Envoy 上顯示的 PSBT (*Partially Signed Bitcoin Transaction*)。


![Image](assets/fr/85.webp)


確認接收的 Address 和傳送的金額是否正確，然後按下確認鍵。


![Image](assets/fr/86.webp)


檢查 Exchange Address。在我的範例中，沒有，因為交易包含單一輸出。


![Image](assets/fr/87.webp)


請確定費用是您所選擇的。


![Image](assets/fr/88.webp)


如果所有資訊都正確無誤，請按一下確認按鈕簽署交易。


![Image](assets/fr/89.webp)


您的 Passport 會以 QR 代碼的形式顯示您已簽署的交易。


![Image](assets/fr/90.webp)


在 Envoy 應用程式上，按一下 QR 碼圖示，然後掃描 Passport 螢幕上顯示的 PSBT。


![Image](assets/fr/91.webp)


最後一次檢查您的交易詳細資料。如果一切正確無誤，請按 "**Send Transaction**"（傳送交易）在 Bitcoin 網路上廣播。


![Image](assets/fr/92.webp)


您的交易正在等待確認。您可以直接從您的帳戶追蹤交易狀態。


![Image](assets/fr/93.webp)


恭喜您，現在您已經知道如何在 Envoy 應用程式中設定和使用 Passport。如果您覺得本教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。感謝您的分享！


如需詳細資訊，請參閱我們的 Liana 軟體教學：


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04