---
term: Batched spending
definition: Technique grouping several payments to different recipients into a single Bitcoin transaction to reduce fees.
---

Batched spending is a technique primarily used by entities with a high volume of transactions, such as exchange platforms, to optimize and reduce transaction costs. By combining multiple payments to different recipients into a single Bitcoin transaction, batched spending uses less block space, thereby lowering associated fees. Batched spending can be easily recognized during chain analysis. The batched spending pattern is characterized by a small number of input UTXOs (often just one) and multiple output UTXOs. Observing this pattern during analysis indicates that the input UTXO likely belongs to an entity with significant economic activity, and that the output UTXOs will disperse accordingly. Some outputs will belong to the company's clients, others may go to partner companies, and typically at least one output will represent change returning to the originating entity.



