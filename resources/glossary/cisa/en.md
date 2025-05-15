---
term: CISA
---

Acronym for "Cross-Input Signature Aggregation". This is a technical proposal designed to optimize the size of Bitcoin transactions by reducing the number of signatures required to validate them.

Currently, on Bitcoin, each input in a transaction must have an individual signature before it can be consumed. This proves that the owner of the UTXO in question has authorized the transaction. With CISA, the aim is to combine the signatures of all inputs to a single transaction into a single signature covering all inputs. This would make it possible to reduce the size of transactions with many inputs, and thus also reduce their costs. This would be particularly useful for those carrying out coinjoins or consolidations, while enabling more transactions to be confirmed on Bitcoin without altering block sizes or intervals. CISA is based on the Schnorr protocol, which enables linear aggregation of signatures. This means that a single signature can prove the possession of several independent keys.

However, implementing CISA on Bitcoin is very complex, as it requires profound changes in the way scripts work. Currently, script verification on Bitcoin is done input by input. Moving to a model where an entire transaction is checked at once, as proposed by CISA, is far from a trivial change.