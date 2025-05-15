---
term: Anchor
---

在 RGB 協定中，Anchor 代表用於證明交易中包含單一 Commitment 的客戶端資料集。在 RGB 協定中，一個 Anchor 由以下 Elements 組成：




- transaction ID Bitcoin (txid) 來自 Witness Transaction ；
- Multi Protocol Commitment (MPC)；
- Deterministic Bitcoin Commitment（DBC）；
- 如果使用 Tapret Commitment 機制，額外交易證明 (ETP)。


因此，Anchor 的作用是在特定的 Bitcoin 交易和經 RGB 協定驗證的私人資料之間建立可驗證的連結。它保證這些資料確實包含在 Blockchain 中，但其確切內容不會公開。