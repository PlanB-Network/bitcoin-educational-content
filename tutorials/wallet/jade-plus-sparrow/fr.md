---
name: Jade Plus - Sparrow
description: Configuration avancée du Jade Plus avec Sparrow Wallet
---
![cover](assets/cover.webp)

Le Jade Plus est un hardware wallet Bitcoin-only conçu par Blockstream. C'est le successeur du Jade classique avec des améliorations logicielles, des options en plus et une ergonomie repensée pour une utilisation plus intuitive. Cette nouvelle version se distingue notamment par son magnifique écran LCD de 1,9 pouce offrant une gamme de couleurs étendue comparée à son prédécesseur. Les boutons et la navigation dans les menus ont aussi été optimisés.

Le Jade Plus peut être utilisé de plusieurs manières : via une connexion filaire USB-C, en mode "*Air-Gap*" avec une carte micro SD (adaptateur nécessaire), en Bluetooth ou encore par échange de QR codes grâce à la caméra intégrée. Ce hardware wallet fonctionne sur batterie.

Il est disponible à partir de $149,99 en version noire de base, et le prix peut augmenter de jusqu'à $20 pour les versions "*Genesis Grey*" ou "*Lunar Silver*". Le Jade Plus se positionne donc comme un choix intéressant, avec des fonctionnalités avancées comparables à celles des hardware wallets haut de gamme tels que le Coldcard Q ou le Passport V2, mais à un tarif assez bas, proche des modèles de milieu de gamme.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

Le Jade Plus est compatible avec la majorité des logiciels de gestion de portefeuille. Voici un récapitulatif des compatibilités au moment de la rédaction de ce tutoriel (janvier 2025) :

| Logiciel de gestion | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green   | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana               | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow             | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk             | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter             | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet          | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum            | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper              | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

Dans ce tutoriel, nous allons réaliser une configuration avancée du Jade Plus avec le logiciel desktop Sparrow Wallet en mode QR codes. Cette configuration est idéale pour les utilisateur intermédiaires ou expérimentés. Si vous recherchez une approche plus simple pour les débutants, je vous recommande de consulter ce tutoriel où nous utilisons le Jade Plus avec Green Wallet avec une connexion Bluetooth :

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Le modèle de sécurité du Jade Plus

Le Jade Plus utilise un modèle de sécurité reposant sur un "*secure element virtuel*", matérialisé par un "*blind oracle*". Concrètement, ce mécanisme combine le PIN choisi par l’utilisateur, un secret hébergé sur le Jade et un secret détenu par l’oracle (un serveur maintenu par Blockstream), afin de créer une clé AES-256 répartie sur deux entités. Lors de l’initiation, un échange ECDH sécurise la communication avec l’oracle, et permet de chiffrer la phrase de récupération sur le hardware wallet. Concrètement, lorsque l'on souhaite accéder à la seed pour signer des transactions, il faut avoir accès :
- À l'appareil Jade Plus en lui-même ;
- Au PIN pour déverrouiller l'appareil ;
- Et au secret de l'oracle.

L’avantage majeur de cette approche est l’absence de point de défaillance unique au niveau du hardware, puisque si jamais un attaquant a accès à votre Jade, l’extraction des clés exige de compromettre simultanément le Jade et l’oracle. Aussi, ce modèle permet au Jade Plus d'être entièrement open-source, puisqu'il permet d'éviter les contraintes liées à l'utilisation de véritables secure elements physiques, tels que ceux utilisés sur les Ledger par exemple.

L'inconvénient de ce système est que l'utilisation du Jade Plus dépend de l'oracle maintenu par Blockstream. Si cet oracle devient inaccessible, il n'est plus possible d'utiliser directement le hardware wallet avec le PIN. Cependant, cela ne signifie pas que vos bitcoins sont perdus, car ils peuvent toujours être récupérés grâce à votre phrase de récupération, que vous pouvez d'ailleurs entrer dans le Jade Plus en mode "*stateless*". Pour contourner cette dépendance, il est aussi possible de configurer et de gérer son propre serveur d'oracle.

## Unboxing du Jade Plus

Lors de la réception de votre Jade Plus, vérifiez que la boite et le sceau sont en bon état afin d'être sûr que votre paquet n'a pas été ouvert.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Dans la boite, vous trouverez :
- Le Jade Plus ;
- Un cable USB-C ;
- Des cartons pour noter votre phrase mnémonique sous forme de mots ou bien sous forme "*CompactSeedQR*" ;
- Quelques notices d'utilisation ;
- Un cordon ;
- Quelques autocollants.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

L'appareil dispose de 4 boutons de navigation :
- Le bouton en bas à droite permet d'allumer le Jade ;
- Le gros bouton sur la face de l'appareil permet de sélectionner un élément ;
- Les deux petits boutons sur le haut permettent de naviguer à droite ou à gauche ;
- Vous pouvez également sélectionner un élément en cliquant simultanément sur les deux boutons en haut de l'appareil.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Configuration d'un nouveau portefeuille Bitcoin

Cliquez sur le bouton de démarrage.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Cliquez sur "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)
