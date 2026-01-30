---
term: Assume valid
definition: A Bitcoin Core parameter allowing to skip signature verification for blocks prior to a certain point, accelerating the initial synchronization.
---

A configuration parameter in Bitcoin Core that allows a newly initialized node (which has not yet completed the Initial Block Download, or IBD) to skip signatures verification for all transactions included in blocks prior to a specific block. This block is identified by the hash of its header and is updated with each new release of Bitcoin Core. When a node starts up with this parameter enabled, it first verifies the chain of block headers to find the branch with the most accumulated work. If the node detects the hash provided by Core in the branch it has chosen, it will omit signature verification for all blocks before that point. If the hash is not present, the node will fall back to a full traditional synchronization, verifying everything from the beginning.

The goal of Assume Valid is to  speed up the initial sync of a new node without compromising security, under the assumption that the network has already validated those past transactions. The main trade-off is that the node may not detect thefts or invalid signatures that occurred before the Assume Valid block. However, it can still independently verify the total bitcoin supply. From the Assume Valid block onward, all transaction signatures are fully verified. 
This approach relies on the assumption that if a transaction has been accepted by the network for a long time without dispute, it is unlikely to be fraudulent.