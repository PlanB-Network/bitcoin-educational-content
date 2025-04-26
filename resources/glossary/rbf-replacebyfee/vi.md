---
term: RBF (REPLACE-BY-FEE)

---
A transactional mechanism that allows the sender to replace one transaction with another by paying higher fees, in order to speed up its confirmation. If a transaction with too low fees gets stuck, the sender can use *Replace-By-Fee* to increase the fees and prioritize their replacement transaction in the mempools.

RBF is applicable as long as the transaction is in the mempools; once in a block, it can no longer be replaced. At the initial sending, the transaction must specify its availability to be replaced by adjusting the `nSequence` value to a number less than `0xfffffffe`. This is known as an RBF "flag". This setting signals the possibility of updating the transaction after it has been broadcast, which subsequently allows for an RBF. However, it is sometimes possible to replace a transaction that has not signaled RBF. Nodes using the configuration parameter `mempoolfullrbf=1` accept this replacement even if RBF was not initially signaled.

Unlike CPFP (*Child Pays For Parent*), where the recipient can act to speed up the transaction, RBF (*Replace-By-Fee*) allows the sender to take the initiative to speed up their own transaction by increasing the fees.