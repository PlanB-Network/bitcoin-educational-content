---
term: ASSUME UTXO
---

A configuration parameter in the Bitcoin Core client that allows a newly initialized node (one that hasn’t yet performed Initial Block Download, or IBD) to postpone the verification of transactions and the UTXO set prior to a given snapshot. The concept relies on using a UTXO set (a list of all existing UTXOs at a certain point in time) provided by Core and assumed to be accurate This enables the node to quickly synchronize with the chain that has the most accumulated work. 

Since the node skips the lengthy IBD process, it becomes operational for the user much faster. Assume UTXO splits the synchronization (IBD) into two phases:

* First, the node performs the Header First Sync (verification of headers only) and considers the UTXO set provided by Core as valid;
* Then, once it is up and running, the node begins verifying the full block history in the background, building its own UTXO set. If this new UTXO set does not match the one provided by Core, it will produce an error message.

Therefore, Assume UTXO speeds up the preparation of a new Bitcoin node by postponing the transaction verification process and the UTXO set through an updated snapshot provided in Core.