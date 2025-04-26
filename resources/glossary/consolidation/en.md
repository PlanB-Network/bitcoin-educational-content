---
term: CONSOLIDATION
---

A specific transaction in which multiple small UTXOs are merged into one input to form a single, larger UTXO as output. This operation is a transaction made to one's own wallet. The goal of consolidation is to take advantage of periods when fees on the Bitcoin network are low to merge several small UTXOs into one larger in value. Thus, it anticipates mandatory expenses in case of fee increases, allowing for savings on future transaction fees.

Indeed, transactions with many inputs are heavier and, consequently, more expensive. Beyond the savings achievable on transaction fees, consolidation is also a form of long-term planning. If your wallet contains very small UTXOs, these can become unusable if the Bitcoin network enters a prolonged period of high fees. For example, if you need to spend a UTXO of 10,000 sats but the minimum mining fees amount to 15,000 sats, the expense would exceed the value of the UTXO itself. These small UTXOs then become economically irrational to use and remain unusable as long as the fees do not decrease. These UTXOs are commonly referred to as "dust." By regularly consolidating your small UTXOs, you reduce this risk associated with fee increases.

However, it is important to note that consolidation transactions are recognizable during a chain analysis. Such a transaction indicates a Common Input Ownership Heuristic (CIOH), meaning that the inputs of the consolidation transaction are owned by a single entity. This can have implications in terms of privacy for the user.

![](../../dictionnaire/assets/7.webp)