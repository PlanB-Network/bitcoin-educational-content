---
term: BIP0047
---

此協定由 Justus Ranvier 於 2015 年提出，旨在解決 Bitcoin Address 重複使用的關鍵問題，這種做法嚴重損害系統上的使用者隱私。Satoshi 中本在 Bitcoin 白皮書中已經強調每筆交易使用不同金鑰對的重要性，以維持使用者不同動作的隔離。BIP47 引進了可重複使用的付款代碼的概念，允許使用者接收多筆付款，而無需為每筆交易手動 generate 一個新的 Bitcoin Address。這些代碼作為虛擬識別碼，從用戶的 Wallet seed 派生，並位於 HD Wallet 派生結構中的帳戶層級。從雙方支付代碼的組合中，雙方都可以推導出大量屬於對方的唯一地址，而無需與對方再次通訊。此協定的核心依賴 ECDH 演算法 (*Elliptic-Curve Diffie-Hellman*)，這是建立在橢圓曲線上的 Diffie-Hellman 金鑰 Exchange 的變體，可讓雙方建立共用的秘密，以產生唯一的接收位址。雖然 BIP47 並未加入 Bitcoin Core，且社群對其反應不一，但 Samourai Wallet 和 Sparrow Wallet 上的 PayNym 等實作已採用 BIP47，並將其完全整合至其隱私工具生態系統中。