---
term: SIMPLE PAYMENT
---

Transaction pattern (or model) used in chain analysis characterized by the consumption of one or more UTXOs in inputs and the production of 2 UTXOs in outputs. This model will therefore look like this:

![](../../dictionnaire/assets/5.webp)

This simple payment model indicates that we are likely in the presence of a sending or payment transaction. The user has consumed their own UTXO in inputs to satisfy in outputs a payment UTXO and a change UTXO (change returned to the same user). We therefore know that the observed user is likely no longer in possession of one of the two UTXOs in outputs (the payment one), but they are still in possession of the other UTXO (the change one).