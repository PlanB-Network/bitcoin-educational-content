---
term: BIP0017
---

由 Luke Dashjr 提出，與 BIP12 和 BIP16 競爭。BIP17 引進了一個新的操作碼 `OP_CHECKHASHVERIFY`，目的是在解鎖資金之前，將 `scriptSig` 中的腳本與 `scriptPubKey` 中的 Hash 進行驗證。經過一段時間的激烈爭論後，BIP16 (P2SH) 最終比 BIP17 (CHV) 更受歡迎。