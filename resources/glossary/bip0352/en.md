---
term: BIP0352
definition: Silent Payments, a method using static addresses to receive payments without visible address reuse.
---

Proposal for improvement by Josibake and Ruben Somsen that introduces Silent Payments, a method for using static Bitcoin addresses to receive payments without address reuse, interaction, and without a visible on-chain link between different payments. This technique eliminates the need to generate new, unused receiving addresses for each transaction, thereby avoiding the usual interactions in Bitcoin where the recipient must provide a new address to the payer.

In this system, the payer uses the recipient's public key and their own private key to generate a fresh address for each payment. 
Only the recipient, with their private key, can compute the private key corresponding to this address. This mechanism relies on ECDH (*Elliptic‑Curve Diffie‑Hellman*), a cryptographic key exchange algorithm, to establish a shared secret used to derive the receiving address and its private key (only on the recipient’s side).
To identify the Silent Payments intended for them, recipients must scan the blockchain and examine each transaction matching the criteria for Silent Payments. 
Unlike BIP47, which uses a notification transaction to establish the payment channel, Silent Payments eliminate this step, saving one transaction. 
The trade‑off, however, is that recipients must scan all potential transactions and apply ECDH to determine whether they are the intended recipient.