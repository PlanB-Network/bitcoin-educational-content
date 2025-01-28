---
term: CPFP (CHILD PAYS FOR PARENT)

---
A transactional mechanism aimed at accelerating the confirmation of a Bitcoin transaction, similar to what Replace-by-Fee (RBF) does, but from the recipient's side. When a transaction with fees too low compared to the market remains stuck in the mempools of nodes and does not confirm quickly enough, the recipient can make a new transaction, spending the bitcoins received in the blocked transaction, although it is not yet confirmed. This second transaction necessarily requires the first to be mined to be confirmed. Miners are thus forced to include both transactions together. The second transaction will allocate much more in transaction fees than the first, in such a way that the average fee encourages miners to include both transactions. The child transaction (the second) pays for the parent transaction that is stuck (the first). This is why it is referred to as a "CPFP."

Thus, CPFP allows the recipient to obtain their funds more quickly despite the low initial fees incurred by the sender, unlike RBF (*Replace-By-Fee*), which allows the sender to take the initiative to speed up their own transaction by increasing the fees.