---
name: Jade Plus - Sparrow
description: Jade Plus 與 Sparrow Wallet 的進階配置
---
![cover](assets/cover.webp)


Jade Plus 是 Blockstream 設計的 Bitcoin 專用 Hardware Wallet。它是經典 Jade 的繼承者，在軟體上有所提升，提供更多選項，並重新設計人體工學，讓使用更直覺。新版本擁有華麗的 1.9 吋 LCD 螢幕，色域比前一代產品更廣。按鈕和功能表導覽也經過最佳化。


Jade Plus 有多種使用方式：透過 USB-C 有線連接、在「*Air-Gap*」模式下搭配 micro SD 卡（需使用轉接器）、透過藍牙，甚至藉由整合式相機交換 QR 碼。此款 Hardware Wallet 由電池供電。


它的基本黑色版本售價 149.99 美元起，"*Genesis Grey*「 或 」*Lunar Silver*"版本的價格最多可漲 20 美元。因此，Jade Plus 是一個有趣的選擇，其先進功能可媲美 Coldcard Q 或 Passport V2 等高階硬體錢包，但價格卻相當低廉，接近中階機種。


![JADE-PLUS-SPARROW](assets/fr/01.webp)


Jade Plus 與大多數的 Wallet 管理軟體相容。以下是撰寫本文時（2025 年 1 月）的相容性摘要：


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

在本教程中，我們將以 QR 碼模式設定 Jade Plus 與桌上型 Sparrow Wallet 軟體的進階組態。此配置適合中級或有經驗的使用者。如果您正在尋找適合初學者的簡易方法，我建議您參考本教學，我們將透過藍牙連線使用 Jade Plus 與 Green Wallet：


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Jade Plus 安全模式


Jade Plus 使用基於 「虛擬安全元件 」的安全模型，由 「盲甲骨文 」實現。具體而言，此機制結合了使用者選擇的 PIN、Jade 上託管的秘密以及由 Oracle（Blockstream 所維護的伺服器）持有的秘密，以建立一個分佈在兩個實體上的 AES-256 金鑰。在啟動過程中，ECDH Exchange 會保護與 Oracle 的通訊，並在 Hardware Wallet 上加密復原短語。實際上，當您想要存取 seed 簽署交易時，您需要存取 .NET Framework：




- Jade Plus 裝置本身；
- 若要使用 PIN 碼來解除鎖定裝置 ；
- 而對於神諭的秘密。


這種方式的主要優點是在硬體層級上沒有單點故障，因為如果攻擊者取得您的 Jade 的存取權，要擷取金鑰就必須同時攻擊 Jade 和 Oracle。這種模式也意味著 Jade Plus 是完全開放原始碼的，避免了使用真正實體安全 Elements 的限制，例如 Ledger 上使用的限制。


此系統的缺點在於 Jade Plus 的使用取決於 Blockstream 所維護的 Oracle。如果此 Oracle 無法存取，則無法再直接使用 Hardware Wallet 與 PIN。但是，這並不表示您的比特幣就會丟失，因為您仍然可以使用您的恢復短語來恢復它們，您可以在 「*無狀態*」模式下在 Jade Plus 中輸入恢復短語。為了繞過這個依賴性，您也可以配置和管理您自己的 oracle 伺服器。


另一個管理 seed 的方法是不在 Jade Plus 上註冊。在這種情況下，Jade 只會變成一個簽章裝置。在初始化過程中，除了一般將恢復詞組儲存為文字外，您也會將其儲存為手動產生的 QR 代碼。如此一來，每次使用 Wallet 時，您就可以使用 Jade 的相機匯入 seed。對於進階使用者來說，這可能是個有趣的選項，這取決於您的安全策略，但您需要小心既要儲存 seed，又要保護它，因為即使是 QR 代碼，也會讓任何人竊取您的資金。我們將在本教學中介紹此選項，但這並非必要。


## Jade Plus 開箱


當您收到 Jade Plus 時，請檢查包裝盒和 Seal 是否完好，以確保您的包裹沒有被打開。


![JADE-PLUS-SPARROW](assets/fr/02.webp)


在盒子裡，您會發現 ：




- Le Jade Plus；
- USB-C 連接線；
- 卡片，以文字或「*CompactSeedQR*」來記錄您的 Mnemonic 詞組；
- 一些使用說明 ；
- 一條繩子
- 一些貼紙。


![JADE-PLUS-SPARROW](assets/fr/03.webp)


本裝置有 4 個導覽按鈕：




- 右下方的按鈕可以開啟 Jade；
- 裝置正面的大按鈕可用來選擇項目；
- 頂端的兩個小按鈕可讓您向左和向右瀏覽；
- 您也可以同時按一下裝置上方的兩個按鈕，來選擇項目。


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## 設定新的 Bitcoin Wallet


按一下開始按鈕。


![JADE-PLUS-SPARROW](assets/fr/05.webp)


按一下「*設定 Jade*」。


![JADE-PLUS-SPARROW](assets/fr/06.webp)


選擇「進階設定」。


![Image](assets/fr/07.webp)


然後按一下「*建立新的 Wallet*」來 generate 一個新的 seed。您可以選擇 12 個字或 24 個字的 Mnemonic 詞組。兩種選項的 Wallet 安全性仍然相同，因此選擇最簡單的選項儲存（即 12 個字）可能會比較方便。


![Image](assets/fr/08.webp)


按一下「*繼續*」按鈕以顯示新的復原短語。


![Image](assets/fr/09.webp)


您的 Jade Plus 會顯示 12 個字的 Mnemonic 詞組。 **這個Mnemonic讓您可以完全不受限制地存取您所有的比特幣。任何擁有這個短語的人都可以盜取您的資金，即使沒有實體存取您的 Jade Plus。如果您的 Jade 遺失、被盜或破損，這 12 個字的短語可以恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。**


您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


![Image](assets/fr/10.webp)


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

當然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。


按一下螢幕右邊的箭頭，會顯示下列字元。


![Image](assets/fr/11.webp)


儲存詞組後，Jade Plus 會要求您確認。使用裝置上方的按鈕依順序選取正確的單字，然後按一下中央按鈕進入下一個單字。


![Image](assets/fr/12.webp)


接下來您有 2 個選擇。如介紹中所述，您可以選擇直接將 seed 儲存在裝置上，並使用 Blockstream 的「*虛擬安全元件*」保護系統存取您的 Wallet（選項 1），或是將 seed 儲存在 QR 代碼中，每次使用時掃瞄一下（選項 2）。


對於選項 1，請選擇「*否*」；對於選項 2，請選擇「*是*」。


![Image](assets/fr/13.webp)


### 選項 1：QR PIN 解鎖


如果您選擇了選項 1 (CompactSeedQR："*No*")，則會直接進入連線方式選擇。在本教程中，我們希望透過 QR 碼交換在 Air-Gap 模式下使用裝置，因此請選擇「*QR*」。


![Image](assets/fr/27.webp)


按一下「*繼續*」。


![Image](assets/fr/28.webp)


PIN 碼用於解鎖您的 Jade，並可防止未經授權的實體存取。此 PIN 碼並不參與您的 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要擁有 12 個字的 Mnemonic 詞組，就可以重新取得您的 bitcoins。我們建議您選擇一個盡可能隨機的 PIN 碼。此外，請確保您將此代碼保存在與您的 Jade 儲存位置不同的地方，例如密碼管理器中。


在 Jade 上選擇 6 位數的 PIN 碼，使用左右按鈕捲動數位，並使用中間按鈕確認每一位數。


![Image](assets/fr/29.webp)


再次確認您的 PIN 碼。


![Image](assets/fr/30.webp)


如簡介所述，您的 seed 會加密儲存於 Jade Plus。若要解密，您必須提供 ：




- 有效的 PIN 碼（我們剛剛設定的） ；
- Blockstream 所維護的 Oracle 的秘密。


在本進階教學中，我們將使用 Sparrow Wallet 來管理我們的 Bitcoin Wallet。然而，與 Blockstream 的 Green Wallet 軟體不同，Sparrow 無法存取 Blockstream 伺服器上的 Oracle。因此，每次解鎖 Jade Plus 時，我們都會使用 Blockstream 的網站來擷取甲骨文秘密。


請造訪 https://jadefw.blockstream.com/pinqr/index.html


按一下「*開始 QR 解鎖*」。


![Image](assets/fr/31.webp)


按一下「*完成*」，因為您已經在 Jade Plus 上選擇了 PIN 碼。


![Image](assets/fr/32.webp)


使用電腦的相機掃描 Jade 螢幕上顯示的 QR 代碼。


![Image](assets/fr/33.webp)


在您的 Jade 上確認，進入下一個畫面。


![Image](assets/fr/34.webp)


掃描網站上可見的 QR 代碼，即可取得神諭的秘密。


![Image](assets/fr/35.webp)


現在您的 Wallet 已經建立，您可以進行下一步，並跳過「*選項 2：CompactSeedQR*」小節。


![Image](assets/fr/36.webp)


每次啟動時，按一下「*QR 模式*」。


![Image](assets/fr/37.webp)


選擇「*QR PIN 解鎖*」。


![Image](assets/fr/38.webp)


輸入您的 PIN 碼。


![Image](assets/fr/39.webp)


然後前往 [Blockstream 網站](https://jadefw.blockstream.com/pinqr/qrpin.html)，使用 Oracle 掃描 Exchange QR 碼。


![Image](assets/fr/40.webp)


您的 Jade 現在已解鎖。


![Image](assets/fr/41.webp)


### 選項 2：CompactSeedQR


如果您選擇了選項 2 (CompactSeedQR：「*Yes*」)，請再次按一下「*Yes*」。


![Image](assets/fr/14.webp)


按一下「*開始*」。


![Image](assets/fr/15.webp)


您可以使用 Jade Plus 方塊中提供的 QR 碼底座。根據您選擇的是 12 個字還是 24 個字的句子，選擇適當的方塊。您也可以 [從 Blockstream 網站列印範本](https://help.blockstream.com/hc/article_attachments/41928319071769)。


您的 Jade Plus 將顯示 QR 代碼的每個區域。


![Image](assets/fr/16.webp)


用筆在方格內塗色，將您的 seed 複製成 QR 代碼。請務必精確，以確保 Jade Plus 攝影機稍後能夠掃描。使用箭頭移至下一個區域。


![Image](assets/fr/17.webp)


完成後，按一下「*完成*」。


![Image](assets/fr/18.webp)


使用 Jade Plus 掃描您手工製作的 QR 代碼，以檢查其有效性。


![Image](assets/fr/19.webp)


如果您的紙張備份正確，請按一下「*繼續*」。


![Image](assets/fr/20.webp)


在本教程中，我們將使用完全基於 QR 掃描的連接模式，因此請選擇「*QR*」。


![Image](assets/fr/21.webp)


您也可以選擇在 CompactSeedQR 備份之外增加 PIN 碼，如選項 1。這提供了兩種存取 Wallet 的方式：透過 PIN 和 Blockstream 的「虛擬安全元件」系統，或透過 CompactSeedQR。


如果您選擇雙重 PIN 碼選項，請選擇「*PIN*」，並依照選項 1 的相同步驟設定 PIN 碼。


如果您只想繼續使用 CompactSeedQR，請選擇「*SeedQR*」。


![Image](assets/fr/22.webp)


現在您的 Wallet 已經建立，您可以進入下一個步驟。


![Image](assets/fr/23.webp)


每次啟動時，按一下「*QR Mode*」按鈕，然後按一下「*Scan SeedQR*」。


![Image](assets/fr/24.webp)


使用裝置的相機掃描您儲存的 seed 作為 QR 代碼。


![Image](assets/fr/25.webp)


您的 Jade 現在已解鎖。


![Image](assets/fr/26.webp)


## 新增 BIP39 passphrase


BIP39 passphrase 是您可以自由選擇的密碼，它會被加入您的 Mnemonic 詞組，以加強 Wallet 的安全性。啟用此功能後，存取您的 Bitcoin Wallet 需要同時輸入 Mnemonic 和 passphrase。如果沒有這兩個密碼，就無法恢復 Wallet。


在您的 Jade Plus 上配置此選項之前，強烈建議您閱讀這篇文章，以充分理解 passphrase 的理論操作，避免錯誤導致您的比特幣丟失 ：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在您的 Jade 仍鎖定的情況下（passphrase 只能在裝置未解鎖時輸入），進入「*選項*」功能表。


![Image](assets/fr/42.webp)


選擇「*BIP39 passphrase*」。


![Image](assets/fr/43.webp)


在「*頻率*」選項中，您可以選擇 Jade Plus 是否會在每次啟動時要求您輸入 passphrase：




- "*Disabled*" 停用 passphrase 的使用；
- 「*僅限下次登入*」將要求您在下次啟動時返回此功能表，以啟動對您的 passphrase 的請求。此選項可讓您不透露其用途；
- "*Always Ask*" 會讓 Jade 在每次啟動時，有系統地詢問您的 passphrase，從而揭露您的 Wallet 受到 passphrase 的保護。


根據您的安全策略選擇選項。我個人選擇「*Always Ask*」為範例。


![Image](assets/fr/44.webp)


然後，您可以選擇兩種方法輸入您的 passphrase：




- 「*手動*」：虛擬鍵盤可讓您逐字輸入字母（大寫和小寫）、數字和符號。這是所有硬體錢包的標準方法；
- "*WordList*"：Blockstream 為 Jade 設計的特定方法，可加快 passphrase 的輸入速度並增加其熵。在輸入時，系統會建議使用 BIP39 清單中的字詞，讓解鎖變得更容易。此方法會自動將選取的字詞連結成句子，並以空格分隔（例如：`abandon ability able`）。


就個人而言，我建議您使用第一種方法，因為這是所有其他 Wallet 支援的標準。


![Image](assets/fr/45.webp)


然後，您可以返回主畫面，使用您的 PIN 碼或 CompactSeedQR（如上所示）照常解鎖您的 Wallet。接著會要求您輸入 passphrase。


![Image](assets/fr/46.webp)


在 Jade 鍵盤上輸入，並確保在實體媒體 (紙張或金屬) 上做一個或多個備份。在範例中，我使用的是非常弱的 passphrase，但您需要選擇一個強大、隨機的 passphrase，包含所有類型的字元，而且要夠長 (就像強密碼一樣)。


![Image](assets/fr/47.webp)


如果您的 passphrase 有效，請確認。


![Image](assets/fr/48.webp)


請注意 BIP39 密鑰是區分大小寫的。如果您輸入的 passphrase 與最初設定的略有不同，Jade 不會報錯，但會衍生出另一套密碼金鑰，而這些密碼金鑰與您最初設定的 Wallet 並不相同。


因此，在設定時，記下您的主密鑰指紋是很重要的，您可以在螢幕右下角找到主密鑰指紋。例如，我的 passphrase `PBN`，我的主密鑰指紋是 `3AD1AE65`。


![Image](assets/fr/49.webp)


每次使用 passphrase 解鎖 Jade 時，請檢查指紋是否與您在設定時輸入的指紋相同。如果是的話，表示您的 passphrase 是正確的，而且您正在存取正確的 Bitcoin Wallet。如果不一致，則表示您進入了錯誤的 Wallet，需要重新嘗試，注意不要輸入錯誤。


在您的 Wallet 收到您的第一個 bitcoins 之前，**我強烈建議您執行一個空的恢復測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Jade Plus 上刪除您的 Wallet，而它還是空的（`選項 -> 裝置 -> Factory Reset`）。然後嘗試使用 Mnemonic 短語和任何 passphrase 的紙本備份來還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果相符，您就可以放心，您的紙本備份是可靠的。若要瞭解有關如何進行測試還原的更多資訊，請參閱此其他教學：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 在 Sparrow Wallet 上設定 Wallet


在本教程中，我將介紹使用 Sparrow Wallet 的 Jade Plus 的進階用法。不過，這個 Hardware Wallet 與許多其他程式相容，例如 Liana、Nunchuk、Specter、Green 和 Keeper。這些相容性在連線方面各有不同：USB、藍牙或 QR code（詳情請參閱介紹中的表格）。


如果您還沒有下載 Sparrow Wallet [從官方網站](https://sparrowwallet.com/) 並安裝到您的電腦上，請從此開始。


![Image](assets/fr/50.webp)


安裝前請務必檢查軟體的真實性和完整性。如果您不知道如何操作，請參閱本教程：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

開啟 Sparrow Wallet 後，按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。


![Image](assets/fr/51.webp)


命名您的 Wallet，然後按一下「*建立 Wallet*」。


![Image](assets/fr/52.webp)


選擇 "*Airgapped Hardware Wallet*"。


![Image](assets/fr/53.webp)


按一下「*Jade*」選項旁邊的「*Scan...*」。


![Image](assets/fr/54.webp)


解鎖您的 Jade Plus，如果您正在使用，請輸入您的 passphrase。然後前往「*選項*」功能表，選擇「*Wallet*」，然後按一下「*匯出 Xpub*」。


![Image](assets/fr/55.webp)


您的 Jade 會透過幾個 QR 代碼顯示您的 Keystore。使用 Sparrow 在您的電腦上掃描它們。


![Image](assets/fr/56.webp)


現在您應該可以看到您的 xpub 和主密鑰指紋，它們應該與 Jade Plus 上的指紋相符。按一下「*應用*」。


![Image](assets/fr/57.webp)


設定一個強大的密碼，以確保存取 Sparrow Wallet 的安全性。這個密碼可以保護您的公開金鑰，地址，標籤和交易歷史，防止未經授權的存取。最好將這個密碼儲存在密碼管理器中，以免忘記。


![Image](assets/fr/58.webp)


您的 Wallet 已在 Sparrow 上正確設定。


![Image](assets/fr/59.webp)


## 接收比特幣


現在您的 Jade Plus 已經設定完成，您可以在新的 Bitcoin Wallet 上接收第一個 Sats。要這麼做，請在 Sparrow 上點選「*接收*」功能表。


![Image](assets/fr/60.webp)


Sparrow 會在您的 Wallet 中顯示第一個空白的接收 Address。


![Image](assets/fr/61.webp)


在使用之前，讓我們先在 Jade Plus 螢幕上確認一下，確定它是否屬於我們的 Bitcoin Wallet。在 Jade 上點選 "*Scan QR*"，然後掃瞄 Sparrow 上顯示的 Address 的 QR 碼。


![Image](assets/fr/62.webp)


檢查您 Jade 螢幕上顯示的 Address 是否與 Sparrow Wallet 上顯示的相符。如果對應，請按一下核取標記以繼續。


![Image](assets/fr/63.webp)


然後，您的 Hardware Wallet 將確認此 Address 是您的 Wallet 的一部分，並且持有相關的私密金鑰。


![Image](assets/fr/64.webp)


如果 Address 被您的 Jade 驗證通過，您就可以用它來接收比特幣了。當交易在網路中廣播時，就會出現在 Sparrow 上。等到您收到足夠的確認後，交易才算確實完成。


![Image](assets/fr/65.webp)


## 發送比特幣


現在您的 Wallet 中已有一些 Sats，您也可以傳送一些。要這樣做，請按一下「*UTXOs*」功能表。


![Image](assets/fr/66.webp)


選擇您希望用作此交易輸入的 UTXO，然後按一下「*送出所選*」。


![Image](assets/fr/67.webp)


輸入收款人的 Address、提醒您交易目的的標籤，以及您希望寄往此 Address 的金額。


![Image](assets/fr/68.webp)


根據目前的市場狀況調整收費率，然後按一下「*建立交易*」。


![Image](assets/fr/69.webp)


檢查所有交易參數是否正確，然後按一下「*完成簽署交易*」。


![Image](assets/fr/70.webp)


點擊 "*Show QR*"顯示 PSBT (*Partially Signed Bitcoin Transaction*)。Sparrow 已經建立了交易，但仍缺乏簽章來解鎖輸入中使用的 bitcoins。這些簽章只能由 Jade Plus 執行，它託管您的 seed，提供簽章交易所需的私人金鑰。


![Image](assets/fr/71.webp)


在您的 Jade Plus 上，按一下「*掃描 QR*」以掃描 Sparrow 上顯示的 PSBT。


![Image](assets/fr/72.webp)


確認寄送 Address 和寄送金額是否正確，然後按一下箭頭進行驗證。


![Image](assets/fr/73.webp)


確定費用金額是您所選擇的金額，然後按一下 Interface 左上角的「勾」圖示以簽署交易。


![Image](assets/fr/74.webp)


在 Sparrow Wallet 上，點選「*Scan QR*」，掃描 Jade 上顯示的 QR 代碼。


![Image](assets/fr/75.webp)


您已簽署的交易現在可以在 Bitcoin 網路上廣播，並由 Miner 包含在區塊中。如果一切正常，請按一下「*廣播交易*」。


![Image](assets/fr/76.webp)


您的交易已被廣播，正在等待確認。


![Image](assets/fr/77.webp)


恭喜您，現在您知道如何在 QR 模式下設定和使用 Jade Plus 了。如果您覺得這篇教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。感謝您的分享！


若要更進一步，我推薦您參考另一篇有關 Jade Plus 的教學，我們透過藍牙與 Green 行動應用程式進行設定：


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0