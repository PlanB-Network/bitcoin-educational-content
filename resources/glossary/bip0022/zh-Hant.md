---
term: BIP0022
---

BIP 於 2012 年由 Luke Dashjr 提出，為外部 Mining 介面引入標準化的 JSON-RPC 方法，稱為「getblocktemplate」。隨著 Mining 難度的增加，使用專門的外部軟體製作 Proof of Work 的情況也有所發展。本 BIP 提出了完整節點與 Mining 專用軟體之間區塊模板的通用通訊標準。此方法包含傳送整個區塊的結構，而非僅是標頭，以便 Miner 進行客製化。