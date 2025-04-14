---
name: Sparrow Wallet - Multisig
description: Créer un portefeuille multisignature sur Sparrow
---
![cover](assets/cover.webp)

Un portefeuille multisignature (souvent appelé "multisig") est une structure de portefeuille Bitcoin qui exige plusieurs signatures cryptographiques, issues de clés différentes, pour autoriser une dépense. Contrairement à un portefeuille classique ("singlesig"), où une seule clé privée suffit à déverrouiller un UTXO, le multisig repose sur un modèle **m-de-n** : parmi les _n_ clés associées au portefeuille, _m_ doivent impérativement co-signer chaque transaction.

Ce mécanisme permet de répartir le contrôle d’un portefeuille entre plusieurs entités ou dispositifs. Par exemple, dans une configuration 2-de-3, trois ensembles de clés indépendants sont générés, mais deux suffisent pour débloquer les fonds. Cette architecture réduit drastiquement les risques liés à la compromission ou à la perte d’une clé : un voleur ayant accès à une seule clé ne peut pas vider le portefeuille, et un utilisateur qui en perd une peut encore accéder à ses fonds avec les deux restantes.

01

Cependant, cette meilleure sécurité s’accompagne d’une complexité plus élevée. La configuration d’un portefeuille multisig nécessite la sécurisation de plusieurs phrases mnémoniques (une par facteur de signature) et des clés publiques étendues ("xpub"). En effet, si vous utilisez un portefeuille multisig 2-de-3, pour récupérer le portefeuille, vous devez soit posséder les trois phrases mnémoniques, soit disposer d'au moins deux des trois phrases. Mais si vous n'avez que deux phrases sur les trois, il faut également avoir accès aux trois *xpubs*, sans lesquelles il sera impossible de retrouver les clés publiques nécessaires pour accéder aux bitcoins qu'elles protègent.

Pour résumer, pour récupérer un portefeuille multisig, vous devez :
- Soit avoir accès à toutes les phrases mnémoniques associées à chaque facteur de signature ;
- Soit disposer du nombre minimum de phrases mnémoniques requis par le seuil pour pouvoir signer, et également avoir accès aux xpubs de tous les facteurs afin de pouvoir récupérer les clés publiques nécessaires.

02

Cette gestion des sauvegardes des portefeuilles multisig est facilitée par les *Output Script Descriptors*, qui regroupent toutes les données publiques nécessaires pour accéder aux fonds. Cependant, cette fonctionnalité n'est pas encore implémentée dans tous les logiciels de gestion de portefeuille.

Le multisig est particulièrement adapté aux bitcoiners qui recherchent une sécurité renforcée ou une gestion collective des fonds : entreprises, associations, familles, ou utilisateurs individuels détenant un montant significatif de bitcoins. Il permet de créer des schémas de gouvernance décentralisés, par exemple pour répartir le pouvoir de signature entre plusieurs dirigeants ou membres d’une équipe.

Dans ce tutoriel, nous allons apprendre à créer et utiliser un portefeuille multisignature classique avec **Sparrow Wallet**. Si vous souhaitez créer un portefeuille multisignature personnalisé avec des timelocks, je vous recommande plutôt d'utiliser le logiciel Liana :

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prérequis




## Créer un portefeuille multisig




## Recevoir des bitcoins sur son multisig




## Envoyer des bitcoins avec son multisig















Félicitations, vous savez dorénavant comment configurer et utiliser un portefeuille multisignature sur Sparrow. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous recommande de consulter ce tutoriel sur une autre méthode pour augmenter la sécurité de votre portefeuille Bitcoin, la Passphrase BIP39 :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7