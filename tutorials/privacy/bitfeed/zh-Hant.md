---
name: Bitfeed
description: 探索主要的 Bitcoin 通訊協定鏈。
---

![cover](assets/cover.webp)



Bitfeed 是一個可視化 Bitcoin 協定上鏈層的平台。它是由 Mempool.space 專案的其中一位貢獻者所發起，主要以其簡約的外觀和易用性脫穎而出。



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

在本教程中，我們將介紹此工具，它可讓您探索網絡上的所有交易和區塊。



## 開始使用 Bitfeed



Bitfeed 是一個專注於三個重點的平台：





- Blockchain 諮詢**、
- 交易搜尋**、
- 可視化 mempool**。



### 諮詢區塊鏈



在 Bitfeed 首頁，您主要可以找到 ：





- 搜尋列：此區段是區塊鏈查詢的入口。您可以在此依據區塊號碼或切細值搜尋特定區塊。您也可以搜尋特定交易和 Bitcoin 位址，以驗證網路中的某些交易資訊。



![searchBar](assets/fr/01.webp)



在左上角，您可以看到比特幣的當前價格，以美元 (USD) 估算。



![price](assets/fr/02.webp)



右側側邊欄是平台功能表。從此選單中，您可以依喜好自訂平台介面、新增或移除項目，以及自訂檢視篩選條件。例如，以值或虛擬位元組 (vBytes) 重量檢視每個區塊的大小。



![menu](assets/fr/03.webp)



頁面中央是最後挖出的區塊，可看到該區塊所包含的所有交易。這部分提供了時間戳記、區塊中涉及的比特幣總數、區塊大小（以位元組為單位元組）、交易數量以及區塊中每個虛擬位元組的平均交易成本比率等資訊。



![block](assets/fr/04.webp)



您可以在搜尋列中搜尋特定區塊，回溯頻道的歷史，並根據您的條件檢視。



例如，我們要檢視區塊 `879488` 中的交易。



![bloc](assets/fr/05.webp)



此區塊的第一筆交易代表**coinbase**交易，可讓此區塊的礦工賺取 mining 獎勵，此獎勵必須在挖出 100 個區塊後才能使用，由包含的交易費用和區塊補助金所組成。此交易是使新比特幣能夠在系統上發行的交易。



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

預設情況下，區塊中的交易會根據兩個標準來表示：




- 大小，可以在值和權重 (vBytes) 之間變化；
- 顏色會因年代和每個虛擬位元組的交易費用比例而有所不同。



![options](assets/fr/07.webp)



因此我們可以得出結論，包含在同一區塊中的所有交易在區塊鏈中的確認數量相同。最大的立方體代表包含最高金額比特幣的交易。



**「資訊 」**選單選項進一步證實了這一解釋，它告知我們區塊交易的顏色和大小的翻譯。



![infos](assets/fr/08.webp)



您也可以根據虛擬位元組和收費比率檢視一個區塊的交易。此檢視可能與前一檢視不同，因為交易中包含的 bitcoin 值並不能定義其大小。



![visualisation](assets/fr/09.webp)



### 檢視交易



您可以透過搜尋列使用交易的識別碼搜尋交易。您也可以點選方塊，查看該交易的相關資訊。



在我們的案例中，就以佔用區塊 `879488` 中最大空間的交易為例。



![biggest](assets/fr/10.webp)



您會看到這筆交易有 `42,989` ，代表最後一個被挖出的區塊與我們選擇的區塊之間的差異。這些確認有助於加強 Bitcoin 網路的安全性，因為若要惡意修改此交易，攻擊者需要擁有等同於重寫整個主區塊鏈的計算能力。



此交易的大小為 `57,088 vBytes`，主要是由於其結構中使用了大量的 UTXO (842 個項目)。令人驚訝的是，與整體區塊平均 5.82 sats/vByte 相比，應用的費用比率仍然相對較低（只有 4 sats/vByte）。



因此，佔用空間最多的交易不一定是交易成本比率最高的交易。



![transaction](assets/fr/11.webp)



如果按照**資訊**選單中的比例，交易成本比率最高的交易是紫色的那筆。這是交易 [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35)，交易成本比率為`147.49 sats/vBytes`。



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool 可視化



mempool 是等待納入區塊的 Bitcoin 交易集中在一起的虛擬位置。Bitfeed 允許諮詢多個 Bitcoin 礦工的 [mempool](https://planb.academy/resources/glossary/mempool)，提供廣泛的交易追蹤。



![mempool](assets/fr/13.webp)



在本節中，您可以追蹤 Bitcoin 網路主鏈上所有有效且尚未確認的交易。



![unconfirmed](assets/fr/14.webp)



現在您有了一份使用 Bitfeed 平台分析區塊和交易的指南，以便可視化 Bitcoin 網路主鏈上的可用資訊，同時受益於簡約、易用的介面。如果您喜歡本教學，我們建議您進行下一步：透過 Amboss 專案發現 Lightning Network。



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017
