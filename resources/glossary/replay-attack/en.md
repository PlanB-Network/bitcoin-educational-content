---
term: REPLAY ATTACK
---

In the context of Bitcoin, a replay attack occurs when a valid transaction on one Blockchain is maliciously reproduced on another Blockchain which has the same transaction history. In other words, a transaction broadcast on one channel can be replicated on another without the consent of the sender of the first transaction.

Let's take the example of a hypothetical Hard Fork from Bitcoin, named "*BitcoinBis*". If you make a payment in bitcoins to buy a baguette from a baker on the real Blockchain Bitcoin, that same baker could replay that legitimate transaction on *BitcoinBis* to get the same amount in cryptocurrencies on this Fork, without any action on your part.

This type of attack can only occur in the case of Blockchain branching with 2 independent chains that persist over time. Typically, this would be the case with Hard Fork. For a replay attack to be possible, the 2 blockchains must have a common history, and the duplicated transaction must consume as inputs UTXOs created from previous transactions that took place before the two chains split, or from previous transactions that have themselves already been replayed in a previous replay attack.

Generally speaking, in computing, a replay attack consists of intercepting and reusing valid data to deceive a system by repeating the original transmission. This can sometimes lead to identity theft on a network.

> ► *In the case of a replay attack on a Bitcoin transaction, this is sometimes referred to simply as a "replay transaction. "*