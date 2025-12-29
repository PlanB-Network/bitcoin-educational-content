---
name: Blockstream Explorer
description: 探索 Bitcoin 和 Liquid Network 的主層
---

![cover](assets/cover.webp)



Blockstream Explorer 是一個專案，有助於探索交易和 Bitcoin 協定的全球狀態，以及 Blockstream 公司開發的 [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid。



由 Adam Back 創立的 Blockstream 公司於 2014 年發起，[blockstream.info](https://blockstream.info) 探索器旨在為 Bitcoin 提供強大的基礎架構，保證各層 (on-chain 和 Liquid) 之間的互操作性和交易追蹤，同時增強使用者的安全性和隱私權。



在本教程中，我們將探討它的與眾不同之處、它的服務，以及它如何對 Bitcoin 的 on-chain 和 Liquid 層的運作和狀態提供無縫監控。



## 開始使用 Blockstream explorer



### 導航主航道



當您進入 Blockstream.info 瀏覽器，在「**儀表板**」上，預設選取 Bitcoin 通訊協定主鏈。從這個介面，您可以總覽.NET、.NET Framework、.NET Framework 3.0、.NET Framework 4.0 和.NET Framework 5.0：





- 主鏈大小：最近開採的區塊。



![blocks](assets/fr/01.webp)



本節提供最近挖出的區塊資訊、時間戳記、每個區塊包含的交易數量、大小（千位元組 (kB) ）以及每個區塊的重量單位測量 (**WU** = *重量單位*)。最後一項測量是我們感興趣的，因為考慮到主鏈的每個區塊限制為 `4,000,000WU`，或 `4,000kWU`，它使我們能夠評估區塊的優化。





- 最近的交易。



![transactions](assets/fr/02.webp)



交易部分提供交易的唯一識別碼、涉及的比特幣值、虛擬位元組 (vB) 大小（代表所有數據（輸入和輸出）的總和）和相關費率的資訊。例如，一筆大小為 `153 vB` 且費率為 `2 sat/vB` 的交易將產生 `306 satoshis` 的費用。



### 流體探勘



從「**區塊**」功能表，您可以追溯整個主鏈的歷史，直到最後開採的區塊。



![blocs](assets/fr/03.webp)



點擊特定區塊，您可以獲得其中包含的資訊和交易的更多詳細資訊。例如，區塊 919330：您會看到該區塊的哈希值。您也可以導航到前一個區塊，因為每個已挖掘的區塊 (Genesis 除外) 都會連結到前一個區塊，並保留前一個區塊的哈希值。



![metadata](assets/fr/04.webp)



點擊 **「詳細資料 」** 按鈕，您可以獲得更多關於此區塊的資訊，例如其狀態，這證實了它已被添加到保留和傳播的主鏈中。您還可以獲得該區塊的開採難度：該難度代表解決 mining 密碼問題所需的計算能力，每 2016 個區塊（約 2 周）調整一次。



![details](assets/fr/05.webp)



在此詳細資訊部分下方，我們可以找到此區塊中包含的所有交易。



區塊中的第一筆交易稱為**交易代幣基礎**。它是用來分配礦工的 mining 獎勵 (所有與區塊中包含的交易相關的費用以及區塊補助金)。這項交易所創造的比特幣，只有在再挖出連續 100 個區塊之後才能使用。換句話說，為了能夠使用它們，礦工必須等待區塊 **919430** 的產生。這就是所謂的 [*「成熟期 」*](https://planb.academy/fr/resources/glossary/maturity-period)。



Coinbase 是一種特殊的交易：它是唯一沒有實際輸入的交易，因為它不花費之前交易的任何 bitcoins。




![coinbase](assets/fr/06.webp)



所有其他交易分為兩部分：輸入和輸出。



比特幣要在新的交易中作為輸入，交易的啟動者必須提供與特定腳本對應的簽名，以證明他或她擁有比特幣。每枚比特幣 (UTXO) 都包含一個腳本，一般需要特定的簽章，只有持有者的私密金鑰才能提供。這些腳本是用 Bitcoin Script 寫成的 ***scriptSig*** (在 ASM 中)，可以有多種類型。在這個範例中，我們可以看到使用的 UTXO 是 P2SH 類型，輸出至 P2WPKH 類型 (*Pay-to-Witness-Public-Key-Hash*) 的輸出。



您可以使用啟發式方法追蹤特定 UTXO 的歷史。我們誠摯地邀請您探索不同的 Bitcoin 啟發式方法和途徑，以加強您在 Bitcoin 上交易的機密性：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



讓我們以這筆交易的出帳費用為例。按一下交易識別碼，我們就會被轉到交易詳細資料頁面的**交易**部分。



![transaction](assets/fr/08.webp)



從這個頁面，您可以找出交易包含在哪個區塊中。根據所使用的地址類型，交易可以優化其資料 (* 虛擬位元組*)，因此可以支付較少的交易費用。例如，這筆交易使用以 `bc1q` 開頭的原生 SegWit Bech32 位址格式，節省了 53% 的費用。



![trx_details](assets/fr/09.webp)



## Liquid 層



Liquid Network 是 Bitcoin 協定的 [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) 和開放原始碼第 2 級解決方案。特別是，它能讓比特幣交易更快、更保密。



在 Blockstream.info 瀏覽器上，按一下 **"Liquid"**按鈕，切換到 Liquid 網路。



![liquid](assets/fr/10.webp)



點擊其中一個我們想要追蹤的交易，我們會看到比特幣的大塊金額被 「**保密**」的字樣所取代。在這個網路中，交易可以是保密的，所以我們無法看到每個 UTXO 的金額，無論是在交易中或交易外。



![liquid_trx](assets/fr/11.webp)



然而，我們注意到 Bitcoin 協定的主要層上存在的原則和機制是相同的：比特幣鎖定腳本和 UTXO 可追蹤性。



![liquid_details](assets/fr/12.webp)



Liquid Network 也提供可供組織使用的非儲存數位資產。在 **「資產」** 功能表中，您可以找到已註冊資產的清單、總數及其相關網域。



![assets](assets/fr/13.webp)



對於每項資產，您可以追蹤發行和燒毀交易的歷史（刪除流通中的總數）。



![assets_trxs](assets/fr/14.webp)




## 更多選項



Blockstream.info 探索器還包括 Testnet、Bitcoin、on-chain 和 Liquid Network 上交易的可視化和追蹤。



![testnet](assets/fr/15.webp)



當您進入 Testnet 網路時，您不會使用真正的 bitcoins，但您擁有上述所有功能。



![liquid_testnet](assets/fr/16.webp)



此網路具有不同的鏈條長度，您可以連接並測試 Bitcoin 和 Liquid 機構的運作。





- API 部分專門提供給任何希望將某些 Explorer 功能整合到自己應用程式中的人。透過這個 API，您可以查詢不同層級的主鏈（on-chain 和 Liquid）、追蹤交易以及找出區塊中交易的平均費用等。



![api](assets/fr/17.webp)



現在您已準備好發揮 Blockstream Explorer 的全部潛力，以查詢 on-chain 和 Liquid 層上的區塊鏈。我們希望您能發現本教程內容豐富，並推薦我們關於另一個 Bitcoin 探索器的教程：



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f