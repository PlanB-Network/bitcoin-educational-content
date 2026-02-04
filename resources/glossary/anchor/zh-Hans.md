---
term: Anchor
definition: 在RGB协议中，一组数据证明了承诺包含在比特币交易中，而不会公开其内容。
---

在 RGB 协议中，Anchor 代表一组客户端数据，用于证明交易中包含单个 Commitment。在 RGB 协议中，Anchor 由以下 Elements 组成：




- transaction ID Bitcoin (txid) from Witness Transaction ；
- Multi Protocol Commitment（MPC）；
- Deterministic Bitcoin Commitment（DBC）；
- 如果使用 Tapret Commitment 机制，则需要额外交易证明 (ETP)。


因此，Anchor 的作用是在特定的 Bitcoin 交易和经 RGB 协议验证的私人数据之间建立可验证的联系。它保证这些数据确实包含在 Blockchain 中，但其确切内容不会公开。