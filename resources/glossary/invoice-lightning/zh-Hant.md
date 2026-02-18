---
term: Lightning 發票
definition: 包含完成交易所需的所有資訊的 Lightning 支付請求。
---

收款人產生的閃光付款請求，包含完成交易所需的所有資訊。


Invoice Lightning 包含收款節點公開金鑰形式的付款目的地，也包含 `LN` 前綴、金額、到期時間、HTLC 中使用的秘密的 Hash 以及其他元資料，其中有些是可選的，例如路由選項。這些發票由 BOLT11 標準定義。一旦付費，Invoice Lightning 就無法再使用。


