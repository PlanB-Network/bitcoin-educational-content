---
term: UTXO SET

---
Refers to the collection of all existing UTXOs at any given moment. In other words, it's a large list of all the different pieces of bitcoins waiting to be spent. If you add up the amounts of all the UTXOs in the UTXO set, it gives us the total monetary mass of bitcoins in circulation. Each node in the Bitcoin network maintains its own UTXO set in real-time. It updates it as new valid blocks are confirmed, with the transactions they include, which consume some UTXOs from the UTXO set, and create new ones in return.

This UTXO set is kept by each node to quickly verify if the UTXOs spent in transactions are indeed legitimate. This allows them to detect and reject double-spending attempts. The UTXO set is often at the heart of concerns about Bitcoin's decentralization, as its size naturally increases very quickly. Since a portion of it must be kept in RAM to verify transactions in a reasonable time, the UTXO set could gradually make operating a full node too costly. The UTXO set also has a significant impact on the IBD (*Initial Block Download*). The more of the UTXO set that can be placed in RAM, the faster the IBD is. On Bitcoin Core, the UTXO set is stored in the folder named `/chainstate`.

> ► *In English, "UTXO set" could be translated as "UTXO set".*