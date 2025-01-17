---
term: TRANSACTION (TX)

---
In the context of Bitcoin, a transaction (abbreviated as "TX") is an operation recorded on the blockchain that transfers the ownership of bitcoins from one or more inputs to one or more outputs. Each transaction consumes Unspent Transaction Outputs (UTXOs) as inputs, which are outputs from previous transactions, and creates new UTXOs as outputs, which can be used as inputs in future transactions.

Each input includes a reference to an existing output along with a signature script (`scriptSig`) that fulfills the spending conditions (`scriptPubKey`) established by the output it references. This is what allows bitcoins to be unlocked. The outputs define new spending conditions (`scriptPubKey`) for the transferred bitcoins, often in the form of a public key or an address to which the bitcoins are now associated.