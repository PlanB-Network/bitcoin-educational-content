---
term: HTLC
---

Stands for "*Hashed Timelock Contract*". This is a smart contract mechanism mainly used on Lightning. It is also sometimes found in atomic swaps. Basically, HTLC makes a money transfer conditional on the revelation of a secret, and also includes a time condition to protect the sender's money in the event of a failed transaction.

On Lightning, HTLC allows you to send bitcoins to a node with which you don't have a direct channel, by passing through several channels, with no need for trust along the way. Payment between each node is conditional on the provision of a pre-image (the secret which, when hashed, corresponds to an agreed value). If the final recipient provides this pre-image, it can claim the funds, and necessarily enables each intermediate node to claim the funds in cascade.

For example, if Alice wants to send 1 BTC to David, but doesn't have a direct channel with him, she has to go through Bob and Carol, who have payment channels with each other. Here's how the transaction works:


- David presents Alice with a Invoice Lightning. This contains the hash $h$ of a secret $s$ (the pre-image) that only David knows. So we have: $h = \text{hash}(s)$ ;
- Alice creates a HTLC with Bob, who offers to send her 1 BTC on condition that Bob provides her with a secret $s$ (the pre-image) that corresponds to the hash $h$ ;
- Bob creates a HTLC with Carol, who offers to send him 1 BTC on condition that she provides the same secret $s$ ;
- Carol creates a HTLC with David, who offers another 1 BTC if he reveals the $s$ preimage;
- David reveals $s$ (which only he knew) to Carol to receive 1 BTC. Carol can now use $s$ to get the BTC from Bob. And Bob, who now knows $s$, does the same with Alice.

Finally, Alice sent 1 BTC to David via Bob and Carol (a neutral action for the latter), without anyone having to trust each other, as everything is secured in cascade by the HTLCs' conditions.

HTLCs thus enable so-called "atomic" exchanges: either the transfer is entirely successful, or it fails, and the funds are returned. This guarantees the security of transactions, even between multiple participants with no need for trust.