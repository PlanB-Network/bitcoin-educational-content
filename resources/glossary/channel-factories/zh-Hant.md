---
term: 通路工廠
---

目前正在 Lightning 上開發的先進機制，允許從單一 UTXO 建立和管理多個付款通道。通道工廠利用`n-of-n` Multisig 位址，讓一組使用者可以共同持有單一 UTXO。從那裡，他們可以在彼此之間開啟和關閉付款通道，而無需額外的 On-Chain 交易，除非他們希望從工廠提取資金。這種方法可以顯著降低成本，並減少 Lightning 交易在 Bitcoin 上所佔的空間。在實踐中，這意味著通常每次打開或關閉通道都需要 On-Chain 交易的操作可以用 off-chain 來執行，必要時還可以發佈未發佈的交易，從而保證安全性。用 David A. Harding 的話來說，通道工廠可以描述為用於 generate 其他 Lightning 通道的 Lightning 通道。