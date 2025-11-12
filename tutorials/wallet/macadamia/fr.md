---
name: Macadamia Wallet
description: Portefeuille mobile Cashu pour paiements en BTC anonymes et instantanés
---

![cover](assets/cover.webp)

Macadamia Wallet est un portefeuille mobile iOS qui implémente le protocole Cashu, un système d'ecash Chaumien permettant des paiements Bitcoin totalement anonymes. Grâce aux signatures aveugles, aucun observateur ne peut relier vos dépôts à vos dépenses, offrant une confidentialité similaire au cash physique.

Dans ce tutoriel, nous verrons comment installer et configurer Macadamia, effectuer vos premières transactions Cashu (Mint, Send, Receive, Melt), et gérer plusieurs mints pour sécuriser vos fonds.

## Qu'est-ce que Macadamia Wallet ?

### Le protocole Cashu

Cashu utilise des signatures aveugles inventées par David Chaum : vous déposez des bitcoins chez un serveur "mint" qui émet des jetons équivalents en satoshis. Le mint signe ces jetons sans voir leur contenu, rendant impossible de relier un jeton à un utilisateur. Les échanges sont hors-chaîne, de pair à pair, et totalement opaques – même le mint ne peut pas suivre qui paie qui.

Macadamia est un wallet iOS open source développé en Swift/SwiftUI. Il fonctionne sans compte ni KYC, vos jetons sont stockés localement et protégés par une seed phrase. Le code est auditable sur GitHub et les jetons sont interopérables avec d'autres wallets Cashu (Minibits, Cashu.me).

### Modèle custodial et compromis

**Important** : Cashu fonctionne selon un modèle custodial. Les jetons sont des promesses de paiement (IOU) adossées aux réserves Bitcoin du mint. Si le mint disparaît, vos jetons perdent leur valeur. C'est le compromis pour obtenir une confidentialité maximale.

Utilisez Macadamia comme un porte-monnaie physique : petits montants uniquement. Répartissez vos fonds entre plusieurs mints pour diluer le risque.

## Fonctionnalités principales

Macadamia implémente les quatre opérations fondamentales du protocole Cashu. **Mint** convertit vos satoshis en jetons via une facture Lightning. **Send** permet d'envoyer des jetons gratuitement via QR code ou lien, entièrement hors-chaîne. **Receive** vous laisse recevoir des jetons ou générer une facture Lightning. **Melt** paye une facture Lightning en détruisant vos jetons.

Le wallet supporte la gestion de plusieurs mints simultanément. Vous pouvez swapper vos jetons entre différents mints via Lightning.

## Plateformes supportées

Macadamia est disponible uniquement sur iOS 17 ou supérieur pour iPhone et iPad. L'application native développée en Swift/SwiftUI offre une intégration optimale à l'écosystème Apple.

Le protocole Cashu garantit l'interopérabilité entre wallets. Vous pouvez restaurer votre seed phrase dans d'autres applications comme Minibits sur Android ou Nutstash sur desktop.

La version actuelle est distribuée via TestFlight. N'utilisez que de petits montants avec cette version beta.

## Installation

Macadamia est actuellement disponible via TestFlight, le programme de test beta d'Apple. Voici les étapes pour l'installer :

### Installation via TestFlight

**Étape 1 : Télécharger TestFlight**

Si vous n'avez pas encore l'application TestFlight sur votre appareil, recherchez "TestFlight" dans l'App Store et installez-la. TestFlight est l'application officielle d'Apple permettant de tester les versions beta des applications iOS.

**Étape 2 : Rejoindre le programme beta de Macadamia**

Une fois TestFlight installé, suivez ce lien d'invitation depuis votre iPhone ou iPad : [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)

Le lien ouvrira automatiquement TestFlight et vous proposera d'installer Macadamia Wallet. Touchez "Accepter" puis "Installer" pour commencer le téléchargement. L'application pèse environ dix mégaoctets et s'installe en quelques secondes.

![Installation TestFlight](assets/fr/01.webp)

### Important concernant les versions beta

Macadamia est encore en phase de développement actif. Les versions TestFlight sont mises à jour fréquemment et peuvent introduire de nouvelles fonctionnalités ou corriger des bugs. Cependant, comme pour toute version beta, des dysfonctionnements peuvent survenir. **Il est fortement recommandé de n'utiliser que de petits montants** que vous acceptez de potentiellement perdre en cas de problème technique.

Macadamia ne collecte aucune donnée utilisateur selon la politique de confidentialité affichée. Assurez-vous de vérifier que le développeur est bien cypherbase UG lors de l'installation.

## Configuration initiale

Au premier lancement, Macadamia génère une phrase BIP-39 de 12 mots. Notez-les sur papier dans un endroit sûr – jamais en capture d'écran. Ces mots permettent de recréer votre wallet et dépenser vos jetons.

![Configuration initiale](assets/fr/02.webp)

Suivez les quatre étapes : bienvenue, acceptation des termes, sauvegarde de la seed phrase, et confirmation finale.

![Interface principale](assets/fr/03.webp)

Une fois la configuration terminée, Macadamia présente trois onglets principaux. **Wallet** affiche votre solde et l'historique des transactions. **Mints** permet de gérer vos serveurs Cashu. **Settings** donne accès aux paramètres et à votre seed phrase.

![Ajout d'un mint](assets/fr/04.webp)

Vous devez maintenant configurer un mint, c'est-à-dire un serveur Cashu qui émettra vos jetons. Accédez à l'onglet "Mints", touchez "Add new Mint URL", et entrez l'adresse du mint choisi (ex: mint.cubabitcoin.org). Consultez bitcoinmints.com ou cashu.space pour découvrir les mints publics réputés. Validez uniquement les mints dont vous avez vérifié la réputation, car ils auront la garde de vos satoshis.

## Utilisation quotidienne

### Création de nouveaux jetons (Mint)

Pour alimenter votre wallet Macadamia avec des ecash, vous devez effectuer une opération de "Mint" (création de jetons). Touchez "Receive", puis choisissez l'option "Lightning". Indiquez le montant souhaité (par exemple 1000 sats), sélectionnez le mint à utiliser, puis générez la facture Lightning.

![Opération Mint](assets/fr/05.webp)

Payez la facture Lightning générée avec votre wallet habituel (Phoenix, Zeus, BlueWallet).

![Confirmation Mint](assets/fr/06.webp)

Les jetons Cashu apparaissent instantanément dans votre solde après paiement.

### Envoi de jetons (Send)

Pour envoyer des jetons Cashu à un autre utilisateur, touchez le bouton "Send" sur l'écran principal, puis sélectionnez "Ecash". Indiquez le montant à envoyer (par exemple 50 sats) et ajoutez éventuellement un mémo descriptif.

![Envoi Ecash](assets/fr/07.webp)

Partagez le QR code ou le texte généré via iMessage, Signal ou Telegram. Le destinataire réclame les fonds instantanément et gratuitement.

### Réception de jetons (Receive)

Pour recevoir des jetons Cashu envoyés par un autre utilisateur, touchez "Receive" puis sélectionnez "Ecash". Scannez le QR code du token ou collez le lien token que vous avez reçu.

![Réception Ecash](assets/fr/08.webp)

Touchez "Redeem" pour réclamer le token.

### Paiements Lightning (Melt)

Pour payer une facture Lightning avec vos jetons Cashu, touchez "Send" puis sélectionnez "Lightning". Collez une facture BOLT11 que vous souhaitez payer.

![Paiement Lightning](assets/fr/11.webp)

Le mint détruit vos jetons et exécute le paiement Lightning. Vous pouvez ainsi payer n'importe quel service Lightning tout en préservant votre anonymat.

### Swap entre mints

Lorsque vous recevez des jetons provenant d'un mint que vous n'avez pas configuré, Macadamia vous offre plusieurs options pour gérer ces tokens.

![Swap inter-mints](assets/fr/09.webp)

Ajoutez le nouveau mint ou swappez les tokens vers un mint existant. Le swap utilise Lightning comme pont pour transférer vos fonds anonymement.

### Gestion avancée multi-mints

Macadamia offre des outils sophistiqués pour gérer plusieurs mints simultanément et répartir vos fonds de manière stratégique.

![Gestion multi-mints](assets/fr/10.webp)

"Distribute Funds" répartit automatiquement votre balance selon des pourcentages (ex: 50/50). "Transfer" permet des transferts manuels entre mints pour diversifier vos risques.

## Avantages et limitations

**Points forts** :

- **Confidentialité maximale** : Transactions intraçables, même par le mint. Aucune métadonnée blockchain, échanges pair-à-pair sans trace.
- **Rapidité et gratuité** : Transferts instantanés gratuits au sein d'un mint, idéal pour micropaiements.
- **Interopérabilité** : Jetons Cashu standardisés utilisables avec d'autres wallets compatibles (Minibits, Nutstash).
- **Simplicité** : Interface iOS native accessible aux débutants tout en restant auditable (open source).

**Contraintes** :

- **Modèle custodial** : Confiance requise envers les mints. Si un mint disparaît, vos jetons perdent leur valeur.
- **iOS uniquement** : Pas de version Android/desktop. L'interopérabilité Cashu permet l'accès via d'autres wallets mais l'expérience optimale reste iOS.
- **Dépendance mint** : Mint hors ligne = impossibilité d'effectuer des transactions nécessitant son intervention (Mint, Melt).
- **Technologie émergente** : Développement actif, bugs possibles, standards évolutifs.

## Bonnes pratiques

- **Diversifiez vos mints** : Répartissez vos jetons entre plusieurs mints réputés pour diluer le risque.
- **Limitez les montants** : Utilisez Macadamia comme un porte-monnaie physique pour paiements quotidiens, pas comme coffre-fort.
- **Sécurisez votre seed** : Conservez votre phrase de 12 mots sur papier dans un endroit sûr. Testez occasionnellement la restauration.
- **Vérifiez les mints** : Consultez cashu.space et forums communautaires avant d'ajouter un mint. Privilégiez ceux avec bon uptime et réputation solide.
- **VPN ou Tor** : Masquez votre IP avec VPN/Tor pour maximiser la confidentialité réseau.
- **Rejoignez la communauté** : Groupes Telegram/Discord Cashu pour mises à jour, recommandations mints et bonnes pratiques.

## Conclusion

Macadamia Wallet apporte les propriétés du cash physique au Bitcoin numérique. En combinant signatures aveugles de Chaum et Lightning, il offre une solution élégante pour la confidentialité transactionnelle. Son interface iOS native rend accessible une technologie cryptographique sophistiquée tout en restant open source et interopérable avec l'écosystème Cashu.

Le modèle custodial impose vigilance et bonnes pratiques de sécurité. Utilisé correctement, Macadamia devient un outil précieux pour les paiements quotidiens nécessitant anonymat, en complément de wallets non-custodiales pour l'épargne.

## Ressources

### Documentation officielle
- Site officiel : [macadamia.cash](https://macadamia.cash)
- FAQ Macadamia : [macadamia.cash/faq](https://macadamia.cash/faq)
- Code source GitHub : [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)

### Documentation Cashu
- Documentation technique : [docs.cashu.space](https://docs.cashu.space)
- Liste des mints publics : [bitcoinmints.com](https://bitcoinmints.com)
- Site officiel du protocole : [cashu.space](https://cashu.space)

### Communauté
- Groupe Telegram Cashu : [t.me/cashu_ecash](https://t.me/cashu_ecash)
