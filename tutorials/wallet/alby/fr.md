---
name: Alby

description: Extension de navigateur pour Bitcoin et Lightning Network
---

![cover](assets/cover.webp)


Rendre les paiements de plus en plus facile avec bitcoin est le challenge de nombreuses entreprises du secteur. Dans ce lot, la solution Alby se démarque particulièrement au travers de l'extension de son portefeuille Alby disponible pour les navigateurs. Cette extension vise à mettre en place un cadre fluide qui détecte automatiquement des adresses et qui vous permet de faire des paiements en bitcoins sans frictions. Dans ce tutoriel, nous partons à la découverte de l'extension Alby et tester comment elle facilite les paiements depuis le navigateur.


![video](https://youtu.be/nd5fX2vHuDw)


## L'extension Alby

L'extension Alby est un outil qui permet à votre navigateur web d'interagir facilement et de façon sécurisée avec le réseau Bitcoin et sa couche Lightning Network. Elle se caractérise par trois aspects :
- Le portefeuille Lightning Network : Il s'agit de relier votre nœud ou votre compte Alby afin d'envoyer de de recevoir du bitcoin rapidement et à faible coût via la couche Lightning Network.
-  Les paiements fluides via le Web : Elle supprime la nécessité de scanner des codes QR ou de basculer entre les applications pour les paiements en bitcoin sur des sites web qui supportent Lightning. Elle permet des transactions fluides en un seul clic ou sans confirmation dans le cas où vous avez configuré un budget.
- Un gestionnaire Nostr : L'extension gère vos clés Nostr et facilite la connexion et l'interaction avec les applications Nostr agissant comme un signataire sécurisé sans exposer votre clé privée à chaque plateforme.

https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Se connecter à l'extension

Dans ce tutoriel, nous utiliserons l'extension Alby dans le navigateur Firefox sous un système d'exploitation Ubuntu. Toutefois, elle est disponible sous Windows et avec des navigateurs comme Chrome.

Vous pouvez ajouter l'extension Alby à votre navigateur en vous rendant sur le magasin d'extensions de [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) ou celui de [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).
 
![firefox](assets/fr/01.webp)

![chrome](assets/fr/02.webp)

ℹ️ Il est important de vérifier que l'auteur de l'extension soit bel et bien le compte officiel de Alby afin d'éviter toute forme de piratage ou de vol de vos bitcoins.

Ajoutez l'extension à votre navigateur en cliquant sur le bouton à droite.
Accordez les permissions nécessaires pour l'installation et l'utilisation de l'extension puis épinglez l'extension à la barre d'outils pour la retrouver plus facilement.

![pin](assets/fr/03.webp)

Définissez également un code de déverrouillage (très important), qui vous permettra de garantir l'accès sécurisé à votre portefeuille Lightning depuis votre navigateur. Nous vous suggérons de définir un mot de passe alphanumérique fort.

ℹ️ Sauvegardez ce mot de passe dans un endroit sûr afin d'y avoir accès en cas d'oubli car il peut être modifié mais pas récupéré.

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)

Alby démontre son adaptabilité en vous proposant deux choix :
- Continuer avec un compte Alby si vous souhaitez profiter des applications tout en gardant le contrôle de vos bitcoins.
- Connecter votre propre portefeuille ou votre nœud Lightning si vous en avez déjà un qui est supporté par l'extension.

https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Dans ce tutoriel, nous choisissons de continuer avec le compte Alby afin de profiter des fonctionnalités de l'écosystème Alby.

https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Connectez votre compte Alby, ou créez-en un si vous n'avez pas encore de compte.

![signup](assets/fr/05.webp)

## Faire ses premiers paiements 

Une fois connecté, vous pouvez cliquer sur l'extension Alby dans la barre d'outils pour accéder à votre portefeuille.

![buzzin](assets/fr/06.webp)

Une fois votre compte Alby créé, vous devez connecter ce compte à un portefeuille afin de dépenser des satoshis. Pour lier le portefeuille bitcoin à votre compte Alby, nous vous suggérons d'utiliser un nœud Alby Hub que vous pouvez configurer soit sur votre ordinateur ou souscrire à un plan proposé par Alby.

![hubplan](assets/fr/13.webp)


Dans ce tutoriel, notre compte Alby est soutenu par une installation locale sur notre machine.
Pour monter votre propre nœud Alby, nous vous recommandons notre tutoriel sur Alby Hub.

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Ce nœud vous permet de créer des portefeuilles Lightning self-custodial et  de gérer efficacement vos canaux Lightning afin d'envoyer et de recevoir des satoshis.

![channels](assets/fr/14.webp)

Ouvrez des canaux de réception qui définissent le total de satoshis que vous êtes aptes à recevoir.

![receivechanal](assets/fr/15.webp)

Ouvrez des canaux d'envoi en bloquant des satoshis sur une adresse bitcoin onchain. Les satoshis que vous avez bloqué définissent le total de satoshis que vous êtes en mesure de dépenser.

![spend](assets/fr/16.webp)

Vous pouvez désormais recevoir et envoyer des satoshis via l'extension Alby.

![exchange](assets/fr/08.webp)

A partir de ce moment, l'extension Alby est capable de détecter les adresses Lightning et les factures disponibles sur les pages web que vous visitez et vous suggérera de les payer en bitcoin ou avec Lightning directement depuis votre extension.

![suggest](assets/fr/09.webp)

![pay](assets/fr/10.webp)


## Sécuriser ses clés de récupération avec la clé mère

La clé mère proposée par l'extension Alby fonctionne comme une surcouche de protection qui vous permet de communiquer de façon sécurisée avec la couche principale du réseau Bitcoin (Onchain), le système Nostr et vous permet d'activer la connexion via Lightning avec les applications Nostr.

![masterKey](assets/fr/11.webp)

Cette clé mère se présente sous forme de 12 mots semblables à votre phrase de récupération. Nous vous recommandons donc de le stocker suivant des méthodes sûres afin de vous garantir son accessibilité à tout moment.

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)

Vous pouvez désormais expérimenter les paiements bitcoin et Lightning sans friction avec l'extension Alby. Si vous avez apprécié ce tutoriel, nous vous recommandons notre tutoriel sur Alby Hub pour monter votre propre nœud Alby et pour contrôler tous les aspects de vos portefeuilles Alby depuis une interface fluide et puissante.

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a
