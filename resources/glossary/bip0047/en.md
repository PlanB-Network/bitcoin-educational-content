---
term: BIP0047
---

Proposed by Justus Ranvier in 2015, this protocol addresses the critical issue of Bitcoin address reuse, a practice that severely compromises user privacy. Satoshi Nakamoto, in the Bitcoin White Paper, had already highlighted the importance of using distinct key pairs for each transaction to maintain segregation in the different actions of users. 
BIP47 introduces the concept of reusable payment codes, allowing a user to receive multiple payments without manually generate a new Bitcoin address for each transaction. These codes act as virtual identifiers, derived from the user's wallet seed and located at the account level in the derivation structure of an HD wallet. 
By combining the payment codes of both parties, each participant can derive a large set of unique addresses for the other party, without requiring additional communication after the initial exchange.
The protocol relies on the ECDH algorithm (Elliptic-Curve Diffie-Hellman), a variant of the Diffie-Hellman key exchange adapted to elliptic curves, enabling both parties to establish a shared secret used to generate unique receiving addresses. 
Although BIP47 has not been merged into Bitcoin Core and received mixed feedback from the community, implementations such as PayNym (Samourai Wallet) and Sparrow Wallet have adopted and fully integrated it into their privacy toolsets.