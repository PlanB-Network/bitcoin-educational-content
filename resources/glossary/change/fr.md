---
term: CHANGE
---

Dans le cadre des transactions Bitcoin, fait référence à l'UTXO créé avec les fonds restants après que le paiement effectif a été satisfait. Lorsque l'on utilise en entrées des UTXOs avec une quantité de bitcoins supérieure au montant nécessaire pour le paiement effectif et les frais de transaction, le surplus est un UTXO renvoyé à une adresse interne du portefeuille, appelée adresse de change. Le change représente cet UTXO. Par exemple, si vous souhaitez payer une baguette qui coute `4 000 sats` avec un UTXO de `10 000 sats`, vous allez créer dans votre transaction un change de `6 000 sats` (si l'on néglige les frais de transaction).

![](../../dictionnaire/assets/16.webp)

> ► *Même si c'est très peu utilisé, on pourrait également parler de « monnaie » (rendu de monnaie) pour évoquer le change.*

