---
name: Payjoin
description: Qu'est-ce qu'un Payjoin sur Bitcoin ?
---
![Miniature payjoin - stéganographie](assets/cover.webp)

***ATTENTION :** Suite à l'arrestation des fondateurs de Samourai Wallet et à la saisie de leurs serveurs le 24 avril dernier, les Payjoins Stowaway sur Samourai Wallet ne fonctionnent plus qu'en échangeant manuellement les PSBT entre les parties concernées, à condition que les deux utilisateurs soient connectés à leur propre Dojo. Pour ce qui est de Sparrow, les Payjoins via le BIP78 fonctionnent toujours. Toutefois, il est possible que ces outils soient relancés dans les semaines à venir. En attendant, vous pouvez toujours consulter cet article pour comprendre le fonctionnement théorique des payjoins.*

_Nous suivons de près l'évolution de cette affaire ainsi que les développements concernant les outils associés. Soyez assuré que nous mettrons ce tutoriel à jour au fur et à mesure que de nouvelles informations seront disponibles._

_Ce tutoriel est fourni à des fins éducatives et informatives uniquement. Nous ne cautionnons ni n'encourageons l'utilisation de ces outils à des fins criminelles. Il est de la responsabilité de chaque utilisateur de respecter les lois en vigueur dans sa juridiction._

---
## Comprendre les transactions Payjoin sur Bitcoin

Le Payjoin est une structure spécifique de transaction Bitcoin qui permet d'améliorer la confidentialité des utilisateurs lors d'une dépense en collaborant avec le destinataire du paiement. 

C'est en 2015 que [LaurentMT](https://twitter.com/LaurentMT) évoquait pour la première fois cette méthode sous l'appellation de « *steganographic transactions* », selon un document accessible [ici](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Cette technique fut ensuite adoptée par le portefeuille Samourai Wallet, qui en 2018, fut le premier client à l'implémenter avec l'outil Stowaway. On retrouve également le concept du Payjoin dans le [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) et le [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Plusieurs termes sont ainsi utilisés pour désigner un Payjoin :
- Payjoin ;
- Stowaway ;
- P2EP (*Pay-to-End-Point*) ;
- Transaction stéganographique.

La particularité du Payjoin réside dans sa capacité à générer une transaction qui paraît ordinaire à première vue, mais qui est en réalité un mini Coinjoin entre deux personnes. Pour cela, la structure de la transaction fait intervenir le destinataire du paiement dans les entrées aux côtés de l'expéditeur réel. Le destinataire inclut donc un paiement vers lui-même au milieu de la transaction qui permet elle-même de le payer. 

Prenons un exemple concret : si vous achetez une baguette pour `4000 sats` à l'aide d'un UTXO de `10 000 sats`, et que vous optez pour un Payjoin, votre boulanger ajoutera un UTXO de `15 000 sats` lui appartenant en entrée, qu'il récupèrera en intégralité en sortie, en plus de vos `4000 sats` :
![schéma transaction payjoin](assets/fr/1.webp)

Dans cet exemple, le boulanger introduit `15 000 sats` en entrée et ressort avec `19 000 sats`, la différence est exactement de `4 000 sats`, c'est-à-dire le prix de la baguette. De votre côté, vous entrez avec `10 000 sats` et vous vous retrouvez avec `6 000 sats` à la sortie, ce qui représente bien un solde de `-4 000 sats`, c'est-à-dire le prix de la baguette. Pour simplifier l'exemple, j'ai délibérément omis les frais de minage dans cette transaction.

## Ça sert à quoi une transaction Payjoin ?

La transaction Payjoin remplit deux objectifs qui permettent aux utilisateurs d'améliorer la confidentialité de leur paiement. 

Tout d'abord, le Payjoin vise à induire en erreur un observateur extérieur en créant un leurre dans l'analyse de chaîne. Ceci est rendu possible grâce à l'heuristique de propriété commune des entrées d'une transaction, également connue sous l'acronyme CIOH (*Common Input Ownership Heuristic*). Habituellement, lorsqu'une transaction sur la blockchain présente plusieurs entrées, on suppose que toutes ces entrées appartiennent vraisemblablement à une même entité ou à un même utilisateur. Ainsi, lorsqu'un analyste examine une transaction Payjoin, il est amené à croire que toutes les entrées proviennent d'une même personne. Toutefois, cette perception est erronée, car le destinataire du paiement contribue également aux entrées aux côtés du payeur réel. L'analyse de chaîne est donc déviée vers une interprétation qui se révèle être fausse.

Ensuite, le Payjoin permet également de tromper un observateur extérieur sur le montant réel du paiement qui a été opéré. En examinant la structure de la transaction, l'analyste pourrait croire que le paiement est équivalent au montant d'une des sorties. Or, en réalité, le montant du paiement ne correspond à aucun des outputs. Il est en fait la différence entre l'UTXO du destinataire en sortie et l'UTXO du destinataire en entrée. En ça, la transaction Payjoin rentre dans le domaine de la stéganographie. Elle permet de cacher le montant réel d’une transaction au sein d’une fausse transaction qui agit comme un leurre.

> La stéganographie est une technique de dissimulation d'informations au sein d'autres données ou objets, de manière à ce que la présence de l'information cachée ne soit pas perceptible. Par exemple, un message secret peut être dissimulé à l'intérieur d'un point dans un texte qui n'a rien à voir, le rendant indétectable à l'œil nu (c'est la technique du [micropoint](https://fr.wikipedia.org/wiki/Micropoint)). Contrairement au chiffrement, qui rend les informations incompréhensibles sans la clé de déchiffrement, la stéganographie ne modifie pas l'information. Elle reste affichée en clair. Son objectif est plutôt de cacher l'existence même du message secret, alors que le chiffrement révèle clairement la présence d'informations cachées, bien qu'inaccessibles sans la clé.

Reprenons notre exemple de transaction Payjoin pour le paiement d'une baguette.
![schéma transaction payjoin de l'extérieur](assets/fr/2.webp)
En voyant cette transaction sur la blockchain, un observateur extérieur qui suit les heuristiques habituelles de l'analyse de chaîne en fera l'interprétation suivante : « *Alice a fusionné 2 UTXO en entrée de la transaction afin de payer `19 000 sats` à Bob* ».
![mauvaise interprétation transaction payjoin de l'extérieur](assets/fr/3.webp)
Cette interprétation est évidemment incorrecte, car comme vous le savez déjà, les deux UTXO en entrée n'appartiennent pas à la même personne. De plus, la valeur réelle du paiement n'est pas de `19 000 sats`, mais bien de `4 000 sats`. L'analyse de l'observateur externe est ainsi dirigée vers une conclusion erronée, ce qui garantit la préservation de la confidentialité des parties prenantes.
![schéma transaction payjoin](assets/fr/1.webp)
Si vous souhaitez analyser une véritable transaction Payjoin, en voici une que j'ai réalisée sur le testnet : [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)

[**-> Découvrez notre tutoriel pour faire un Payjoin avec Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)

[**-> Découvrez notre tutoriel pour faire un Payjoin avec Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)


**Ressources externes :** 
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt ;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.
