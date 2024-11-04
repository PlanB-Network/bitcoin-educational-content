---
term: CHANGE
---

In the context of Bitcoin transactions, refers to the UTXO created with the remaining funds after the actual payment has been satisfied. When using UTXOs with an amount of bitcoins greater than the necessary amount for the actual payment and transaction fees, the surplus is a UTXO returned to an internal address of the wallet, called the change address. The change represents this UTXO. For example, if you want to pay for a baguette that costs `4,000 sats` with a UTXO of `10,000 sats`, you will create a change of `6,000 sats` in your transaction (if we disregard the transaction fees).

![](../../dictionnaire/assets/16.webp)

> ► *Even though it's rarely used, we could also refer to it as "currency" (change given) to talk about the change.*