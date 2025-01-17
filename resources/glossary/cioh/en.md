---
term: CIOH
---

Abbreviation for "*Common Input Ownership Heuristic*". It is a heuristic used in the field of Bitcoin chain analysis which assumes that all inputs of a transaction belong to the same entity or user. When observing the public data of a Bitcoin transaction, and multiple inputs are spotted, then, if there are no patterns or other information to refute this, it can be estimated that all the inputs of this transaction belonged to a single person (or entity).

This analysis heuristic was discovered by Satoshi Nakamoto himself, who discusses it in part 10 of the White Paper:

> "However, the connection is unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, the connections can reveal other transactions that belonged to the same owner." - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Consulted at https://bitcoin.org/bitcoin.pdf.

Even today, CIOH remains the main heuristic used by chain analysis companies, along with address reuse.

![](../../dictionnaire/assets/13.webp)

> ► *In English, "CIOH" could be translated as "Common Input Ownership Heuristic".*