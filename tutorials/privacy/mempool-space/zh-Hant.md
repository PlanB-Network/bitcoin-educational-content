---
name: Mempool
description: 探索整個 Bitcoin 生態系統。
---

![cover](assets/cover.webp)



Bitcoin 協定是一個開放給諮詢者的假名、分散式網路。成員（節點），即擁有 Bitcoin 軟體實例的電腦，可以不受限制地存取在 Bitcoin 上公佈的所有資料。然而，在 Bitcoin 的早期，協定的存取權並不像現在這麼廣泛。


在 Bitcoin 的早期，必須執行 Bitcoin 節點才能存取適當的工具 (bitcoin-cli)，從命令列中查詢網路。



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

因此，為了擴大 Bitcoin 社群而推出了一些專案，讓任何沒有擁有節點和/或不具備所需技術能力的人都能更容易地使用 Bitcoin。



在本教程中，我們將探討 **Mempool.space**專案、其功能以及對 Bitcoin 生態系統的影響。



## 什麼是 Mempool.space？



**Mempool.space**是一個開放原始碼的探索器，提供各種Bitcoin協定網路的交易、交易費用、區塊和礦工等有用資訊。它於 2020 年推出，透過代表性的圖形、流暢的動畫和不雜亂的介面，為使用者帶來顯著的體驗改善。



要了解這個專案，Mempool（記憶池）是一個虛擬空間，Bitcoin 網路上所有等待確認的交易都儲存在這個空間。Mempool 就像是一個「等候室」，Bitcoin 交易就在其中等待確認。網絡上的每台電腦（節點）都有自己的等候室，這也解釋了為什麼不是所有人都能同時看到所有交易。



該平台在 Bitcoin 生態系統中的主要影響是，它允許您存取 Bitcoin 上存在的大部分節點記憶區中的各種資訊，而無需執行一個節點。Mempool.space 是檢視和搜尋 Bitcoin 通訊協定網路的儲存庫。



Mempool.space 在生態系統中的使用越來越廣泛，加上 Mempool.space 是開放原始碼，因此能夠整合到越來越多的個人主機系統中。現在您可以直接在個人節點上擁有自己的 Mempool.space 實例。請參閱以下我們在您的 Umbrel 節點上設定 Mempool.space 的教學。



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Mempool.space 的基本知識



如上所述，[Mempool.space](https://Mempool.space) 是一個 Bitcoin 協定探索器，可讓您從圖形化的 Interface 即時監控您的交易及其在所選 Bitcoin 網路上的傳播。



Mempool.space 支援許多 Bitcoin 通訊協定網路。


在功能表列中，您可以找到下列網路：




- **Mainnet**：真正進行 Bitcoin 交易的主要 Bitcoin 網路。
- **Signet**：測試網路使用數位簽章來驗證區塊，而不需要主網路所需的資源。
- Testnet 3：Bitcoin 通訊協定上的無風險測試與開發網路。
- **Testnet 4**：Testnet 3 的新版本為測試環境帶來了更高的穩定性和新的共識規則。



![reseaux](assets/fr/01.webp)



在首頁左側的 Green 中，您會看到未來可能出現的區塊（交易群組），這些區塊已準備好進行驗證，並整合（開採）到 Bitcoin 網路中。平均而言，每十分鐘就會挖出一個區塊：請保留此資訊，因為它在我們稍後的開發過程中會派上大用場。


在右側的紫色區塊中，您會發現最近在 Bitcoin 上挖出的區塊，最後挖出的區塊數字代表目前的網路高度。



![blocs](assets/fr/02.webp)



**交易費用**部分是一個交易費用估算器。分配給交易的費用越高，您的交易就越有可能被加入到下一個準備挖掘的區塊中。


交易費用代表 Miner 將您的交易插入 Mining 的候選區塊所需的費用。其定義為 sat/vB（Satoshi/虛擬位元組）的比率，代表您為交易在候選區塊中佔用的空間所支付的 Satoshis 數量。



⚠️ 重要事項：在 Mempool 飽和的情況下，礦工會優先處理提供最佳 Satoshi/vByte 比率的交易。您的交易越重（越大），就需要越多的 Satoshis 來快速包含。



![fees-visualizer](assets/fr/03.webp)



**Mempool Goggles** 區段可讓您直覺化交易佔用的空間。



![mempool](assets/fr/04.webp)



由於礦工必須提供 Proof of Work 的難度，以將其候選區塊加入已挖出區塊的鏈中，因此大約每十分鐘就會挖出一個區塊。此難度每 **2016 個區塊**，相當於約 **2 個星期**。您可以在此查看此難度的演變。



![difficulty](assets/fr/05.webp)



將新區塊加入主鏈後，驗證區塊的 Miner 就有權獲得由固定部分（每 210,000 個區塊**減半，相當於約 4 年**的減半期間）和交易費用組成的獎勵。



![halving](assets/fr/06.webp)



## 存取您的交易詳細資料



在 Mempool.space 搜尋列中，您可以輸入您的 Bitcoin Address 或您的 transaction ID 來尋找更多關於您的歷史。



![search](assets/fr/07.webp)



在交易詳細資訊頁面，您可以找到有關交易的一般資訊：




- 狀態：加入區塊時已確認，在 Mempool 中等待時未確認。
- 交易費用。
- **預計到達時間 (ETA)**：您的交易加入區塊所需的大約時間。它是根據與此交易相關的費用構成比率計算出來的。



![general-txinfo](assets/fr/08.webp)



**Flow** 區段顯示您的交易元件圖表。



輸入 (先前的 UTXO)，用於您的交易，而輸出則賦予收款人使用每個輸出的 bitcoins 的權利，只要出示支出所需的簽名即可。



![flow](assets/fr/09.webp)



有關所用位址的詳細資訊，請參閱 **輸入與輸出** 一節。



![address](assets/fr/10.webp)



探索不同的 Bitcoin 交易方案，以提高您的機密性。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 加快交易速度



在 Bitcoin 生態系統中，礦工驗證交易的方面與該交易相關的交易費用有內在關聯。礦工會優先處理費用比率 (satoshis/vBytes) 較高的交易，如果您不支付礦工接受的合理費用，可能會影響您交易的有效性。您的交易會卡在 Mempool 中，等待接受其費用比率的區塊。



幸運的是，Bitcoin 網路上有兩種方法可以加速您的交易確認。





- **RBF** - Replacement By Fee：此方法允許您使用與低費用交易相同的項目，但這次是透過增加交易費用來加速驗證。您的新交易將更快被驗證，並納入區塊中，使低費用交易失效。



您可以使用接受此機制的投資組合執行費用替代動作。例如，請參閱我們關於 Blue Wallet 投資組合的文章。



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent：受 RBF 啟發的方法，但在接收方。當您作為收款人的交易在 Mempool 中被凍結時，您可以選擇花費這筆交易的輸出 (UTXOs)，儘管事實上這筆交易尚未被確認，方法是分配更多的費用給這筆新的交易，讓您作為收款人的交易和啟動的交易的平均費用，鼓勵礦工將這兩筆交易都包含在一個區塊中。



⚠️ 第一筆交易必須包含在區塊中，才能確認第二筆交易。



如果所有這些詞彙看起來有點太專業，我建議您 [參考我們的詞彙表](https://planb.academy/resources/glossary)，其中包含所有與 Bitcoin 及其生態系統相關的技術詞彙定義。



除了這些方法之外，Mempool.space 由於與 Bitcoin 網路上 80% 以上的礦工都有連線，因此也允許您加速您的任何**未確認**交易，甚至是未啟動 RBF 的交易，方法是向 Exchange 的礦工支付代價，讓他們將您的低成本交易插入下一個準備開採的區塊中。



在交易詳細資訊頁面中，按一下 **Accelerate** 按鈕，然後繼續向礦工支付您的交易對手。



![accelerate-section](assets/fr/11.webp)


## 未成年人



Miner 指管理礦場的人，即參與 Mining 流程的電腦，該流程由參與 Proof-of-Work 組成。Miner 將其 Mempool 中的待處理交易組合起來，形成一個候選區塊。然後，它會透過修改各種 nonces，為此區塊的標頭搜尋一個小於或等於目標值的有效 Hash。如果他找到一個有效的 Hash，他就會將他的區塊廣播到 Bitcoin 網路，並將相關的金錢報酬（由區塊補助（新比特幣的無償創造）和交易費用組成）收入囊中。



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗管理員就像是「驗證員」，負責驗證交易並將交易歸類到區塊中。要在 Bitcoin 網路中加入新區塊，他們必須解決一個複雜的數學謎題 (Proof-of-Work)。最先解開謎題的 Miner 贏得 Bitcoin 獎勵（區塊授權 + 區塊中包含的交易費用）。



此 Proof of Work 的難度受到監控，可讓您直觀看到礦工所需計算能力的演變。您可以在以下部分找到 ：





- 估計礦工在上一次難度調整時所獲得的總獎金，以及每 210,000 個區塊（約 04 年）一次的下一次 Halving 區塊獎金的估計。



![rewards](assets/fr/12.webp)



此難度每 2016 個區塊（約兩週）調整一次。它與礦工每 2016 個區塊 Miner 所花的平均時間成反比。


當礦工平均花費的時間少於 10 分鐘時，難度就會增加，證明礦工驗證 Miner 區塊比較容易。相反，當平均耗時大於 10 分鐘時，難度就會降低。



![mining-pool](assets/fr/13.webp)





- 一群礦工：鑑於所涉及的難度，一群礦工合作協助尋找 Bitcoin 上的 Proof of Work，我們稱之為**池**。當一個區塊被團體挖出時，所獲得的報酬會根據每個 Miner 的部分解決方案搜尋的成功百分比來分配，也就是在搜尋 Proof-of-Work 時在計算力上的貢獻，或是根據合作協定的報酬方式來分配。





![mining](assets/fr/14.webp)



## Lightning Network 基礎設施



Mempool 不僅提供 Bitcoin 的網路基礎架構（主鏈）資訊。它還為 Bitcoin 的 Lightning overlay 整合了可視化和探索工具。



在**Lightning**部分，您可以檢視 Lightning 節點之間的所有現有連接。



![network-stats](assets/fr/15.webp)



本 Interface 提供以下資訊 ：





- Lightning Network 統計資料。



![distribution](assets/fr/16.webp)




⚠️ **重要**：支付通道的容量指定了一個節點在 Lightning 交易中可以發送給另一個節點的最大金額。





- Lightning 節點是根據網際網路服務供應商 (主機服務) 來分配，也可選擇根據付款通道容量來分配。



![distribution](assets/fr/17.webp)





- Lightning Network 總容量的歷史。


您還可以根據這些節點的支付通道容量找到它們的排名。



![ranking](assets/fr/18.webp)



## 更多圖形



Mempool.space 是享受與 Bitcoin 協定網路互動的理想平台。這些圖表不僅提供可視化的資料，幫助您決定何時進行交易，還提供精確的參數，讓您能夠即時可視化 Bitcoin 網路和相關 Lightning 基礎設施的強度和健康狀況。



在 **圖形**部分，您可以檢視 Bitcoin 網路的基本資料：




- Mempool 大小演變：您可以觀察 Mempool 的大小如何波動，這可以顯示網路活動量高或低的時期。



![graphs](assets/fr/19.webp)






- 所選網路的交易和交易費用的演變：透過追蹤每秒交易量的變化，您可以預測擁擠或低交易量的時期，並優化您的交易費用。此圖可讓您透視網路處理交易量的能力。



![graphs](assets/fr/20.webp)



現在您已經到達 Mempool.space 的終點，成為您自己的探索者並即時追蹤您的交易。請在下方找到我們關於 Bitcoin **公共池**探索者的文章。



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1