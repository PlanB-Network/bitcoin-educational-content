---
term: BIP0030
definition: Soft fork prohibiting duplicate transaction identifiers (TXID), resolving a flaw where two transactions could have the same ID.
---

Proposal that introduced a soft fork implemented on March 15, 2012, to resolve the issue of duplicate transaction identifiers. Before BIP30, it was technically possible to have two different transactions with the same transaction identifier (TXID) within the blockchain. 
This occured twice for coinbase transactions: 
- The transaction in block 91,880 had the same TXID as the coinbase transaction in block 91,722.
- The transaction in block 91,842 had the same TXID as the coinbase transaction in block 91,812. 
BIP30 fixed this flaw by enforcing a new simple rule: no new transaction can have the same TXID as a previously recorded transaction unless the original transaction had been completely spent (i.e., all its outputs had been used). 
This soft fork was activated using the flag day method, making it one of the earliest user-activated soft forks (UASFs) in Bitcoin's history.