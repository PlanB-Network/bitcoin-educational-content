---
term: BIP0118
---

改進 Bitcoin 的提案旨在引入兩個新的 SigHash Flag 修改器：`SIGHASH_ANYPREVOUT` 和`SIGHASH_ANYPREVOUTANYSCRIPT`。這些功能擴展了 Bitcoin 交易的功能，特別是在智慧契約和 Lightning Network 等覆蓋解決方案方面。BIP118 將明顯啟用 Eltoo。`SIGHASH_ANYPREVOUT` 的主要優點是允許在多個交易中重複使用簽章，這提供了更大的靈活性。具體來說，這些 SigHashes 允許簽章不涵蓋任何一個交易的輸入。