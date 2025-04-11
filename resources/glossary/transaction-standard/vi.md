---
term: TRANSACTION STANDARD

---
A Bitcoin transaction that, in addition to adhering to the consensus rules, also falls within the standardization rules set by default on Bitcoin Core nodes. These standardization rules are imposed individually by each Bitcoin node, in addition to the consensus rules, to define the structure of unconfirmed transactions it accepts in its mempool and broadcasts to its peers.

These rules are thus configured and executed locally by each node and can vary from one node to another. They apply exclusively to unconfirmed transactions. Therefore, a node will only accept a transaction it deems non-standard if it is already included in a valid block.

It is noted that the majority of nodes leave the default configurations as established in Bitcoin Core, thereby creating a uniformity of standardization rules across the network. A transaction that, although compliant with the consensus rules, does not respect these standardization rules, will have difficulty propagating through the network. However, it can still be included in a valid block if it reaches a miner. In practice, these transactions, qualified as non-standard, are often transmitted directly to a miner through external means to the Bitcoin peer-to-peer network. This is often the only way to confirm such a transaction. For example, a transaction that allocates no fees is both valid according to the consensus rules and non-standard, because the default policy of Bitcoin Core for the `minRelayTxFee` parameter is `0.00001` (in BTC/kB).