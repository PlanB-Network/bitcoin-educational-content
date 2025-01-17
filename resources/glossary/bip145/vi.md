---
term: BIP145

---
Updates the JSON-RPC call `getblocktemplate` to include support for SegWit, in accordance with BIP141. This update allows miners to construct blocks by taking into account the new "weight" measurement of transactions and blocks introduced by SegWit, and other parameters such as the calculation of the sigops limit.