---
term: STANDARDIZATION RULES

---
Standardization rules are individually adopted by each Bitcoin node, in addition to the consensus rules, to define the structure of unconfirmed transactions it accepts into its mempool and broadcasts to its peers. These rules are thus configured and executed locally by each node and can vary from one node to another. They apply exclusively to unconfirmed transactions. Therefore, a node will only accept a transaction it deems non-standard if it is already included in a valid block.

It is noted that the majority of nodes leave the default configurations as established in Bitcoin Core, thereby creating a uniformity of standardization rules across the network. A transaction that, although compliant with the consensus rules, does not adhere to these standardization rules, will have difficulty being broadcast across the network. However, it can still be included in a valid block if it reaches a miner. In practice, these transactions, referred to as "non-standard," are often transmitted directly to a miner through external means outside the Bitcoin peer-to-peer network. This is often the only way to confirm this type of transaction.

For example, a transaction that allocates no fees is both valid according to the consensus rules and non-standard because the default policy of Bitcoin Core for the `minRelayTxFee` parameter is `0.00001` (in BTC/kB).

> ► *The term "mempool rules" is also sometimes used to refer to the standardization rules.*