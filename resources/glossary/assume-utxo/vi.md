---
term: ASSUME UTXO

---
A configuration parameter in the leading Bitcoin Core client that allows a node that has just been initialized (but has not yet undergone the IBD) to defer the verification of transactions and the UTXO set until a given snapshot. The concept relies on the use of a UTXO set (a list of all existing UTXOs at a given time) provided by Core and presumed accurate, which allows the node to be very quickly synchronized with the chain with the most accumulated work. Since the node skips the lengthy IBD step, it becomes operational for its user very quickly. Assume UTXO divides the synchronization (IBD) into two parts:


- First, the node performs the Header First Sync (verification of headers only) and considers the UTXO set provided by Core as valid;
- Then, once it is operational, the node will verify the complete block history in the background, updating a new UTXO set that it has verified itself. If this new UTXO set does not match the one provided by Core, it will produce an error message.

Therefore, Assume UTXO speeds up the preparation of a new Bitcoin node by postponing the transaction verification process and the UTXO set through an updated snapshot provided in Core.