---
term: BIP0145
definition: Update of the JSON-RPC getblocktemplate call to integrate SegWit support and transaction weight calculation.
---

Updates the JSON-RPC call `getblocktemplate` to include support for SegWit, in accordance with BIP141. This update allows miners to construct blocks by taking into account the new "weight" metric for transactions and blocks introduced by SegWit, as well as other parameters such as the calculation of the sigops limit.