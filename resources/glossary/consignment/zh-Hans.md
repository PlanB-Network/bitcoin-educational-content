---
term: Consignment
---

作为 RGB 协议的一部分，受 *Client-side Validation* 约束的各方之间交换的分组数据。托运货物有两大类：




- Contract Consignment：由发行方提供，包括 Schema、Genesis、Interface 和 Interface Implementation 等初始化信息。
- 转账 Consignment：由付款方提供。它包含到 Terminal Consignment（即付款方收到的最终状态）之前的整个状态转换历史。


这些货物不在 Blockchain 中公开记录，而是由有关各方通过自己选择的通信渠道直接交换。