---
term: REPLAY ATTACK
---

Dans le contexte de Bitcoin, une replay attack se produit lorsqu'une transaction valide sur une blockchain est malicieusement reproduite sur une autre blockchain qui dispose du même historique de transactions. Autrement dit, une transaction diffusée sur une chaîne peut être répliquée sur une autre sans le consentement de l'émetteur de la première transaction.
Prenons l'exemple d'un hard fork hypothétique de Bitcoin, nommé « *BitcoinBis* ». Si vous réalisez un paiement en bitcoins pour acheter une baguette chez un boulanger sur la vraie blockchain Bitcoin, ce même boulanger pourrait rejouer cette transaction légitime sur *BitcoinBis* pour obtenir le même montant en cryptomonnaies sur ce fork, sans aucune action de votre part.
Ce type d'attaque peut uniquement survenir en cas d'embranchement de la blockchain avec 2 chaînes indépendantes qui persistent dans le temps. Typiquement, cela peut survenir en cas de hard fork. Pour qu'une attaque par rejeu soit possible, il faut obligatoirement que les 2 blockchains aient un historique commun et que la transaction dupliquée consomme en inputs des UTXOs créés à partir de transactions précédentes qui ont eu lieu avant la scission des deux chaînes, ou à partir de transactions précédentes qui ont elle-même déjà été rejouées lors d'une précédente attaque par rejeu.
De manière générale, dans l'informatique, une replay attack consiste à intercepter et à réutiliser des données valides pour tromper un système en répétant la transmission originale. Cela peut parfois mener à des usurpations d'identité sur un réseau.
> ► *Dans le cas d'une replay attack sur une transaction Bitcoin, on parle parfois simplement d'une « transaction replay ».*
