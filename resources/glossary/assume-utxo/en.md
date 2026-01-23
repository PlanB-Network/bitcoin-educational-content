---
term: Assume utxo
definition: A Bitcoin Core parameter allowing quick synchronization of a new node by using a snapshot of the UTXO set presumed valid, before verifying the history in the background.
---
Configuration parameter in the majority Bitcoin Core client that allows a node that has just been initialized (but has not yet done the IBD) to postpone the verification of transactions and the UTXO set before a given snapshot. The concept is based on the use of a UTXO set (list of all existing UTXOs at a given time) provided by Core and presumed accurate, which allows the node to be synchronized very quickly on the chain with the most accumulated work. Since the node skips the long IBD step, it is very quickly functional for its user.

Assume UTXO divides the synchronization (IBD) into two parts: First, the node performs Header First Sync (headers verification only) and considers the UTXO set provided by Core as valid; Then, once it is functional, the node will verify the full block history in the background, updating a new UTXO set that it will have verified itself. If the latter does not match the UTXO set provided by Core, it will provide an error message.

Assume UTXO therefore allows for accelerating the preparation of a new Bitcoin node by postponing the transaction and UTXO set verification process thanks to an updated snapshot provided in Core.






