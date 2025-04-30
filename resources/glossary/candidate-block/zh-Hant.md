---
term: 候選區
---

候選區塊是參與 Bitcoin 系統 Mining 流程的 Miner 正在建立的區塊。候選區塊是一個臨時資料結構，包含等待確認的交易，但尚未有有效的 Proof-of-Work 加入 Blockchain。Miner 會根據各種因素（例如相關的交易費用和區塊大小限制）來選擇要納入候選區塊的交易。一旦交易被選中，Miner 就會產生區塊標頭，其中包括版本、交易摘要 (Merkle Root)、Timestamp、前一區塊的 Hash、難度目標和 Nonce。然後，Miner 會嘗試找出符合目前難度目標的標頭 Hash。為此，Miner 會修改標頭中的 Nonce。Miner 也可以修改其候選區塊中的其他資訊。這就是 Proof-of-Work 機制。如果 Miner 成功找到有效的 Hash，候選區塊就會成為有效區塊，並廣播到網路加入 Blockchain。