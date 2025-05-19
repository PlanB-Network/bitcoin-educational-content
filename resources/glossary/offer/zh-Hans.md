---
term: 提供
---

在 BOLT12 中，*offers* 是静态二维码，用于在 Lightning Network 上进行多次付款。与传统发票不同，*offers* 可以重复使用。它们可用于 generate 多次 Invoice 请求。用户扫描包含*offer*的二维码时，会向相关的 "闪电 "节点发送一条请求新Invoice的信息。节点会回复一个付款人可以使用的Invoice。因此，*offer*提供了一个唯一的标识符，用于接收来自闪电平台上不同用户的多笔付款。