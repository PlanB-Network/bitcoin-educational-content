---
term: SWEEP TRANSACTION
---

Pattern or transaction model used in chain analysis to determine the nature of the transaction. This model is characterized by the consumption of a single UTXO as input and the production of a single UTXO as output. The interpretation of this model is that we are in the presence of a self-transfer. The user has transferred their bitcoins to themselves, to another address they own. Since there is no change in the transaction, it is very unlikely that we are dealing with a payment. Indeed, when a payment is made, it is almost impossible for the payer to have a UTXO that exactly matches the amount required by the seller, in addition to the transaction fees. Generally, the payer is therefore forced to produce a change output. We then know that the observed user is likely still in possession of this UTXO. In the context of a chain analysis, if we know that the UTXO used as input in the transaction belongs to Alice, we can assume that the UTXO in output also belongs to her.

![](../../dictionnaire/assets/6.webp)

> ► *In French, "sweep transaction" could be translated as "transaction de balayage".*