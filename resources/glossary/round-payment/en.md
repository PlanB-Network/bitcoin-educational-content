---
term: ROUND PAYMENT
---

An internal heuristic for chain analysis on Bitcoin that allows for a hypothesis about the nature of the outputs of a transaction based on round amounts. Generally, when faced with a simple payment pattern (1 input and 2 outputs), if one of the outputs spends a round amount, then it represents the payment. By elimination, if one output represents the payment, the other represents the change. It can therefore be interpreted that it is likely that the user inputting the transaction still possesses the output identified as being the change.

It should be noted that this heuristic is not always applicable, since the majority of payments are still made in fiat currency units. Indeed, when a merchant in France accepts bitcoin, generally, they do not display stable prices in sats. They would rather opt for a conversion between the price in euros and the amount in bitcoins to be paid through their POS (like BTCPay Server, for example). Therefore, there should not be a round number in the transaction output. Nevertheless, an analyst could attempt to make this conversion by taking into account the exchange rate in effect when the transaction was broadcast on the network. If one day, bitcoin becomes the preferred unit of account in our exchanges, this heuristic could become even more useful for analyses.

![](../../dictionnaire/assets/11.webp)