---
term: Lightning 发票
definition: 包含完成交易所需的所有信息的 Lightning 支付请求。
---

收款人生成的闪电付款请求，包含完成交易所需的所有信息。


Invoice Lightning 包含收款节点公钥形式的付款目的地、"LN "前缀、金额、过期时间、HTLC 中使用的密文的 Hash 以及其他元数据（其中一些是可选的，如路由选项）。这些发票由 BOLT11 标准定义。一旦支付，Invoice "闪电 "就不能重复使用。


