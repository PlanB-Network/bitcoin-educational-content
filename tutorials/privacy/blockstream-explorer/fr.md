---
name: Blockstream Explorer
description: Explorez la couche principale de Bitcoin et le Liquid Network
---

![cover](assets/cover.webp)

L'explorateur Blockstream est un projet qui facilite l'exploration des transactions et l'état global du protocole Bitcoin, ainsi que de la [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid développée par la société Blockstream.

Initié en 2014 par Blockstream, entreprise fondée par Adam Back, l'explorateur [blockstream.info](https://blockstream.info) vise à fournir une infrastructure robuste pour Bitcoin, garantissant l'interopérabilité et le suivi des transactions entre les couches (on-chain et Liquid), tout en renforçant la sécurité et la confidentialité des utilisateurs.

Dans ce tutoriel, nous présentons ce qui le distingue, ses services, et comment il offre un suivi fluide des opérations et de l'état des couches on-chain et Liquid de Bitcoin.

## Débuter avec l'explorateur Blockstream

### Naviguer sur la chaîne principale

Lorsque vous vous rendez sur l'explorateur Blockstream.info, sur le "**Tableau de bord**", la chaîne principale du protocole Bitcoin est sélectionnée par défaut. À partir de cette interface, vous avez une vue d'ensemble de : 

- La taille de la chaîne principale : Les blocs récemment minés.

![blocks](assets/fr/01.webp)

Cette section renseigne sur les récents blocs minés, l'horodatage, le nombre de transactions incluses dans chaque bloc, la taille en kilo-octets (kB) et la mesure de chaque bloc en unités de poids (**WU** = *Weight Units*). Cette dernière mesure est intéressante, car elle permet d'évaluer l'optimisation du bloc, sachant que chaque bloc de la chaîne principale est limité à `4 000 000 WU`, soit `4 000 kWU`.

- Les récentes transactions effectuées.

![transactions](assets/fr/02.webp)

La section des transactions renseigne sur l'identifiant unique de la transaction, la valeur de bitcoin impliquée, la taille en virtual bytes (vB) — qui représente la somme de toutes les données (entrées et sorties) —, ainsi que le taux de frais associé. Par exemple, une transaction d'une taille de `153 vB` avec un taux de `2 sat/vB` entraîne des frais de `306 satoshis`.

### Une exploration fluide

À partir du menu "**Blocs**", vous pouvez remonter l'historique de toute la chaîne principale en partant du dernier bloc miné.

![blocs](assets/fr/03.webp)

En cliquant sur un bloc précis, vous pouvez obtenir plus de détails concernant les informations et transactions inclus dans ce dernier. Par exemple, pour le bloc 919330 : vous avez le hash du bloc. Vous avez également la possibilité de naviguer vers le bloc précédent car chaque bloc miné (en dehors du bloc Genesis) est lié au bloc précédent en gardant le hash de son prédécesseur. 

![metadata](assets/fr/04.webp)

En cliquant sur le bouton **"Détails"**, vous pouvez obtenir plus de renseignements sur ce bloc comme le statut qui confirme l'ajout de ce bloc à chaîne principale retenue et propagée. Vous avez aussi la difficulté à laquelle ce bloc est miné : cette difficulté représente la puissance de calcul nécessaire à la résolution du problème cryptographique du minage et est ajustée tous les 2016 blocs (environ 2 semaines).

![details](assets/fr/05.webp)

En dessous de cette section de détails, nous retrouvons l'ensemble des transactions incluses dans ce bloc. 

La toute première transaction du bloc est appelée **transaction coinbase**. Elle sert à attribuer au mineur la récompense de minage (totalité des frais associés aux transactions incluses dans le bloc et subvention de bloc). Les bitcoins créés par cette transaction ne deviennent dépensables qu’après le minage de 100 autres blocs consécutifs. Autrement dit, pour pouvoir les utiliser, le mineur devra attendre la production du bloc **919430**. C'est ce que l'on appelle la [*"période de maturité"*](https://planb.academy/fr/resources/glossary/maturity-period).

La coinbase est une transaction particulière : c’est la seule qui ne possède aucune vraie entrée, car elle ne dépense pas de bitcoins issus d’une transaction précédente.


![coinbase](assets/fr/06.webp)

Toutes les autres transactions se constituent en deux sections : les entrées et les sorties. 

Pour que des bitcoins soient utilisés comme entrées dans une nouvelle transaction, l'initiateur de la transaction devra prouver sa possession en apportant une signature qui correspond à un script bien précis. Chaque morceau de bitcoins (UTXO) contient un script requérant généralement une signature bien précise que seule la clé privée du détenteur est capable d'apporter. Ces scripts sont des ***scriptSig*** (en ASM), écrits en Bitcoin Script, et peuvent être de différents types. Dans cet exemple, nous pouvons remarquer que les UTXO utilisés étaient de type P2SH vers une sortie de type P2WPKH (*Pay-to-Witness-Public-Key-Hash*). 

Vous pouvez retracer l'historique d'un UTXO spécifique en utilisant des heuristiques. Nous vous invitons à découvrir les différentes heuristiques Bitcoin et les moyens de renforcer la confidentialité de vos transactions sur Bitcoin :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)

Prenons l'exemple de la dépense de la sortie de cette transaction. En cliquant sur l'identifiant de la transaction, nous sommes redirigés vers la section **Transactions** sur la page de détails de cette transaction.

![transaction](assets/fr/08.webp)

À partir de cette page, vous pouvez connaître le bloc dans lequel la transaction a été incluse. En fonction du type d'adresse utilisé, la transaction peut optimiser ses données (*virtual bytes*) et donc payer moins de frais de transaction. Cette transaction, par exemple, a pu s’alléger de 53 % des frais en utilisant un format d'adresse SegWit Bech32 natif commençant par `bc1q`.

![trx_details](assets/fr/09.webp)

## La couche Liquid

Le Liquid Network est une [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) et une solution open source de niveau 2 pour le protocole Bitcoin. Il permet notamment de réaliser des transactions en bitcoins plus rapides et plus confidentielles.

Sur l'explorateur Blockstream.info, cliquez sur le bouton **"Liquid"** pour passer sur le réseau Liquid.

![liquid](assets/fr/10.webp)

En cliquant sur l'une des transactions que nous désirons suivre, nous constatons que les montants des morceaux de bitcoin sont remplacés par la mention "**Confidentiel**". Sur ce réseau, les transactions peuvent être confidentielles, donc nous ne pouvons pas consulter les montants de chaque UTXO, qu'ils soient en entrées comme en sorties de la transaction.

![liquid_trx](assets/fr/11.webp)

Toutefois, nous remarquons que les principes et les mécanismes présents sur la couche principale du protocole Bitcoin sont les mêmes : scripts de verrouillage des bitcoins et traçabilité des UTXO.

![liquid_details](assets/fr/12.webp)

Le Liquid Network permet aussi d'avoir des actifs numériques non-dépositaires qui peuvent être utilisés par des organisations. Dans le menu **"Assets"**, vous retrouverez la liste des actifs enregistrés, le total de ces actifs et le domaine auquel ils sont reliés.

![assets](assets/fr/13.webp)

Pour chaque actif, vous pouvez retracer l'historique des transactions d'émission et des transactions de brûlage (suppression du total en circulation).

![assets_trxs](assets/fr/14.webp)


## Plus d'options

L'explorateur Blockstream.info comprend aussi des visualisations et des suivis de transactions sur Testnet, aussi bien sur Bitcoin on-chain que sur Liquid Network.

![testnet](assets/fr/15.webp)

En allant sur le réseau Testnet, vous n'utilisez pas des bitcoins réels, mais vous disposez de toutes les fonctionnalités présentées un peu plus haut.

![liquid_testnet](assets/fr/16.webp)

Ce réseau se caractérise par une longueur de chaîne différente, auquel vous pourrez vous connecter et tester les fonctionnements des mécanismes Bitcoin et Liquid.

- La section API est dédiée à toute personne qui souhaiterait intégrer certaines fonctionnalités de l'explorateur dans sa propre application. Au travers de cette API vous pourrez interroger la chaîne principale des différentes couches (on-chain et Liquid), traquer des transactions et connaître la moyenne des frais pour les transactions d'un bloc par exemple.

![api](assets/fr/17.webp)

Vous êtes désormais prêts à exploiter tout le potentiel de Blockstream Explorer pour interroger les blockchains sur les couches on-chain et Liquid. Nous espérons que ce tutoriel vous a été instructif et nous vous recommandons notre tutoriel sur un autre explorateur Bitcoin :

https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f
