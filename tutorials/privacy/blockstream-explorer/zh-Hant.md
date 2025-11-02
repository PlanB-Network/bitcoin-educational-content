---
name: BLOCKSTREAM 探索者
description: 探索 Bitcoin 和 Liquid Network 的主要 Layer
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer 是一個有助於探索交易和 Bitcoin 協定的 Global State 以及 BLOCKSTREAM 公司開發的 [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid 的專案。



由 Adam Back 創立的 BLOCKSTREAM 公司於 2014 年發起，[BLOCKSTREAM.info](https://BLOCKSTREAM.info) 探索器旨在為 Bitcoin 提供強大的基礎架構，保證各層 (On-Chain 和 Liquid) 之間的互操作性和交易追蹤，同時增強使用者的安全性和隱私權。



在本教程中，我們將介紹其與眾不同之處、服務，以及如何提供 Bitcoin 的 On-Chain 和 Liquid 層運作與狀態的無縫監控。



## 開始使用 BLOCKSTREAM



### 導航主航道



當您進入 BLOCKSTREAM.info explorer，在「**儀表板**」上，預設選取的是 Bitcoin 通訊協定主頻道。從這個 Interface，您可以總覽 ：





- 主鏈大小：最近開採的區塊。



![blocks](assets/fr/01.webp)



本節提供最近開採的區塊資訊、Timestamp、每個 BLOCK 所包含的交易數量、以千位元組 (kB) 為單位的大小，以及每個 BLOCK 以重量單位 (**WU** = *Weight Units*) 進行的測量。最後一項測量是令人感興趣的，因為它使我們能夠評估 BLOCK 的最佳化，因為主鏈的每個 BLOCK 都限制為 `4,000,000WU`，或 `4,000kWU`。





- 最近的交易。



![transactions](assets/fr/02.webp)



交易部分提供交易的唯一識別碼、涉及的 Bitcoin 值、虛擬位元組 (vB) 大小（代表所有資料（輸入和輸出）的總和）和相關費率的資訊。例如，若交易大小為 `153 vB` 且費率為 `2 sat/vB`，則會產生 `306 satoshis` 的費用。



### 流體探勘



從「**區塊**」功能表，您可以追溯整個主鏈的歷史，直到最後開採的 BLOCK。



![blocs](assets/fr/03.webp)



點選特定的 BLOCK，您可以獲得更多關於其中包含的資訊和交易的詳細資訊。例如，對於 BLOCK 919330：您有 BLOCK 的 Hash。您也可以瀏覽到之前的 BLOCK，因為每個已開採的 BLOCK（Genesis 除外）都會連結到之前的 BLOCK，並保留其前身的 Hash。



![metadata](assets/fr/04.webp)



點擊 **「詳細資料 」** 按鈕，您可以獲得更多關於這個 BLOCK 的資訊，例如它的狀態，確認它已被添加到保留和傳播的主鏈中。您還可以獲得此 BLOCK 的開採難度：此難度代表解決 Mining 密碼問題所需的計算能力，每 2016 個區塊（約 2 周）調整一次。



![details](assets/fr/05.webp)



在此詳細資訊部分下方，我們可以找到此 BLOCK 中包含的所有交易。



BLOCK 中的第一筆交易稱為 **交易幣基**。它用於分配 Miner 的 Mining 獎勵（BLOCK 和 BLOCK 授權中包含的交易相關的所有費用）。這項交易所創造的比特幣，只有在再挖出連續 100 個區塊之後才能使用。換句話說，Miner 要能夠使用它們，就必須等待 BLOCK **919430** 的產生。這就是所謂的 [*「成熟期 」*](https://planb.network/fr/resources/glossary/maturity-period)。



Coinbase 是一種特殊的交易：它是唯一沒有實際輸入的交易，因為它不花費之前交易的任何 bitcoins。




![coinbase](assets/fr/06.webp)



所有其他交易分為兩部分：輸入和輸出。



比特幣要在新的交易中作為輸入，交易的啟動者必須提供與特定腳本對應的簽名，以證明他或她擁有比特幣。每枚比特幣 (UTXO) 都包含一個腳本，一般需要特定的簽章，只有持有者的私密金鑰才能提供。這些腳本是用 Bitcoin Script 寫成的 ***scriptSig*** (在 ASM 中)，可以有多種類型。在這個範例中，我們可以看到使用的 UTXO 是 P2SH 類型，輸出到 P2WPKH (*Pay-to-Witness-Public-Key-Hash*) 類型。



您可以使用啟發式方法追蹤特定 UTXO 的歷史。我們邀請您探索不同的 Bitcoin 啟發式方法，以及如何加強 Bitcoin 交易的機密性：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



讓我們以這筆交易的出帳費用為例。按一下交易識別碼，我們就會被轉到交易詳細資料頁面的**交易**部分。



![transaction](assets/fr/08.webp)



從這個頁面，您可以找出該筆交易包含在哪個 BLOCK。根據使用的 Address 類型，交易可以優化其資料 (* 虛擬位元組*)，因此可以支付較少的交易費用。例如，這筆交易使用以 `bc1q` 開頭的原生 SegWit BECH32 Address 格式，節省了 53% 的費用。



![trx_details](assets/fr/09.webp)



## Liquid 塗層



Liquid Network 是 [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) 和 Bitcoin 協定的第 2 級開放原始碼解決方案。特別是，它能使 Bitcoin 交易更快、更機密。



在 BLOCKSTREAM.info 探索器上，按一下 **「Liquid」** 按鈕，切換到 Liquid Network。



![liquid](assets/fr/10.webp)



點選其中一個我們想要跟蹤的交易，我們會看到 Bitcoin 的金額被 "**Confidential**" 的字樣取代。在這個網路中，交易可以是保密的，因此我們無法看到每筆 UTXO 的金額，不論是交易中或交易外的金額。



![liquid_trx](assets/fr/11.webp)



然而，我們注意到 Bitcoin 通訊協定的主要 Layer 上存在的原則和機制是相同的：Bitcoin 鎖定腳本和 UTXO 追蹤性。



![liquid_details](assets/fr/12.webp)



Liquid Network 也提供可供組織使用的非儲存數位資產。在 **「資產」** 功能表中，您可以找到已註冊資產的清單、總數及其相關網域。



![assets](assets/fr/13.webp)



對於每項資產，您可以追蹤發行和燒毀交易的歷史（刪除流通中的總數）。



![assets_trxs](assets/fr/14.webp)




## 更多選項



BLOCKSTREAM.info 探索器還包括 Testnet、Bitcoin、On-Chain 和 Liquid Network 上交易的可視化和追蹤。



![testnet](assets/fr/15.webp)



當您前往 Testnet 網路時，您不會使用真正的 bitcoins，但您擁有上述所有功能。



![liquid_testnet](assets/fr/16.webp)



此網路具有不同的鏈長，您可以連接並測試 Bitcoin 和 Liquid 機構的運作。





- API 部分專門用於任何希望將某些 Explorer 功能整合到自己應用程式中的人。透過這個 API，您可以查詢不同層級 (On-Chain 和 Liquid) 的主鏈、追蹤交易，並找出例如 BLOCK 中交易的平均費用。



![api](assets/fr/17.webp)



現在您已準備好充分發揮 BLOCKSTREAM Explorer 的潛力，以查詢 On-Chain 和 Liquid 層上的區塊鏈。希望本教程能為您提供有用的資訊，並向您推薦我們關於另一個 Bitcoin Explorer 的教程：



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f