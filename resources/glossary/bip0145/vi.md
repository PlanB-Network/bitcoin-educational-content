---
term: BIP0145

definition: Cập nhật lệnh gọi JSON-RPC getblocktemplate để tích hợp hỗ trợ SegWit và tính toán trọng lượng giao dịch.
---
Updates the JSON-RPC call `getblocktemplate` to include support for SegWit, in accordance with BIP141. This update allows miners to construct blocks by taking into account the new "weight" measurement of transactions and blocks introduced by SegWit, and other parameters such as the calculation of the sigops limit.