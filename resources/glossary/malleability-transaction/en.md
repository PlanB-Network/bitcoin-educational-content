---
term: Transaction malleability
definition: Possibility of modifying the structure of a transaction without changing its effect, but by altering its TXID.
---

Refers to the ability to slightly modify the structure of a Bitcoin transaction, without altering its effect, but while changing the transaction identifier (*TXID*). This property can be exploited maliciously to mislead stakeholders about the status of a transaction, thus causing issues like double spending. Malleability was made possible by the flexibility of the digital signature used. The SegWit soft fork was notably introduced to prevent this malleability of Bitcoin transactions, making the implementation of the Lightning Network complicated. It achieves this by removing the malleable data from the transaction from the TXID calculation.

> ► *Although rare, the term "mutability" is sometimes used to refer to the same concept.*