---
term: BIP0119
---

引入一個新的操作碼，名為 `OP_CHECKTEMPLATEVERIFY` (CTV)。CTV 允許在交易中建立非遞迴契約，以便對特定硬幣的使用方式施加特定條件，包括在未來的交易中。更具體來說，它可以根據輸入 UTXO 的 `scriptPubKey` 定義交易輸出的 `scriptPubKey` 條件。CheckTemplateVerify 被設計為簡單且無動態狀態。它的實作目的在於擴充 Bitcoin 的腳本功能，以方便各種應用程式，例如交易擁塞控制、建立非互動付款通道、DLC、付款池...等。這個新的 opcode 將會被引入來取代 `OP_NOP4`。此變更將意味著 Soft Fork。