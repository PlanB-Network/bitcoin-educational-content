---
name: Sentinel Watch-Only
description: Qu'est-ce qu'un wallet Watch-Only et comment l'utiliser ?
---
![cover](assets/cover.jpeg)

*"Keep your private keys, private."*

Dans cet article, nous explorons tout ce qu'il faut savoir sur les portefeuilles watch-only. Nous abordons leur fonctionnement et étudions les différentes applications disponibles sur le marché. Enfin, nous vous proposons un tutoriel détaillé sur l'une des applications de portefeuille watch-only les plus populaires : Sentinel.

## C'est quoi un Watch-Only Wallet ?
Un portefeuille en lecture seule, ou watch-only wallet, est un type de logiciel conçu pour permettre à l'utilisateur d'observer les transactions associées à une ou plusieurs clés Bitcoin spécifiques, sans pour autant avoir accès aux clés privées correspondantes.

Ce type d'application conserve uniquement les données nécessaires à la surveillance d'un portefeuille Bitcoin, notamment pour voir son solde et son historique des transactions, mais elle n'a pas accès aux clés privées. Ainsi, il est impossible de dépenser les bitcoins détenus par le portefeuille sur l'application watch-only.

On utilise généralement le watch-only en conjonction avec un portefeuille matériel, ou hardware wallet. Celui-ci va permettre de stocker les clés privées du portefeuille « à froid », sur un matériel non connecté à internet, qui dispose d'une infime surface d'attaque, ce qui isole les clés privées des environnements potentiellement vulnérables. L'application watch-only, elle, stocke exclusivement la clé publique étendue (`xpub`, `zpub`, etc.) du portefeuille Bitcoin. Cette clé parent ne permet pas de trouver les clés privées associées et, par conséquent, ne permet pas de dépenser les bitcoins. Toutefois, elle permet la dérivation des clés publiques enfant et des adresses de réception. Grâce à la connaissance des adresses du portefeuille sécurisé par le hardware wallet, l'application watch-only peut suivre ses transactions sur le réseau Bitcoin, ce qui offre à l'utilisateur la possibilité de surveiller son solde et de générer de nouvelles adresses de réception, sans avoir à connecter à chaque fois son hardware wallet.

## Quel Watch-Only Wallet utiliser ?
À l'heure actuelle, l'application de watch-only la plus complète est [Sentinel](https://sentinel.watch/), développée par les équipes de Samourai Wallet. Elle regroupe l'ensemble des fonctionnalités essentielles pour un bon portefeuille watch-only :
- Support des clés étendues, des clés publiques et des adresses ;
- Possibilité de classer plusieurs comptes ou portefeuilles dans des collections ;
- Génération d'adresses pour recevoir des bitcoins sur son hardware wallet sans nécessiter son emploi direct ;
- Possibilité de construire et de diffuser des transactions hors-ligne ;
- Option de connexion à son propre nœud Bitcoin ;
- Intégration de Tor pour une confidentialité accrue.

Les uniques inconvénients de Sentinel résident dans le fait que l'application est exclusivement disponible pour Android et qu'elle ne supporte pas les portefeuilles multisignatures. Par conséquent, si vous possédez un appareil Android et que votre portefeuille est un single sig classique, je vous recommande Sentinel.

Pour ceux qui désirent tracer un portefeuille multisignatures, Blue Wallet est la seule application que je connaisse offrant un mode watch-only pour ces types de portefeuilles, et elle est accessible tant sur Android qu'iOS.

Pour les utilisateurs d'iOS à la recherche d'une alternative à Sentinel, [Green Wallet](https://blockstream.com/green/) ou [Blue Wallet](https://bluewallet.io/watch-only/) peuvent être des options, bien que leur fonctionnalité de watch-only ne soit pas aussi complète que celle de Sentinel.

## Comment utiliser le Watch-Only Wallet Sentinel ?

Commencez par installer l'application Sentinel. Vous pouvez le faire soit depuis le Google Play Store, soit à l'aide de l'[APK disponible au téléchargement sur le site web officiel](https://sentinel.watch/download/).




Lors de la première ouverture de l'application, on vous propose de choisir entre :
- `Connect to Dojo` ;
- `Connect to Samourai's server`.

[Dojo](https://samouraiwallet.com/dojo) est une implémentation de nœud complet Bitcoin maintenue par les équipes de Samourai. Ce logiciel peut être installé directement de manière indépendante, mais il est également possible de l'ajouter en un clic sur les node-in-box [Umbrel](https://umbrel.com/) et [RoninDojo](https://ronindojo.io/).

[**-> Découvrir comment installer RoninDojo v2 sur un Raspberry Pi.**](https://planb.network/fr/tutorials/node/ronin-dojo-v2)

Si vous disposez de votre propre Dojo, vous pouvez le connecter à cette étape. De cette manière, vous bénéficierez du plus haut niveau de confidentialité lorsque vous irez chercher les informations de vos transactions sur le réseau Bitcoin.




Sinon, vous pouvez sélectionner le serveur de Samourai par défaut. Vous pouvez également choisir de vous connecter via Tor ou non.





Vous arriverez ensuite sur la page principale de Sentinel.





Pour commencer, vous pouvez paramétrer l'application. Pour ce faire, cliquez sur les trois petits points en haut à droite, puis sur `Settings`.




En cliquant sur `User PIN code`, vous pouvez définir un mot de passe pour protéger l'accès à votre watch-only wallet. Vous pouvez choisir de changer la devise de change pour la conversion de vos soldes en fiat, ou bien de cacher les conversions en fiat en cliquant sur `Hide fiat values`. Vous pouvez également cliquer sur `Disable Screenshots` pour désactiver la possibilité de faire des captures d'écran ou de faire fuiter votre Sentinel sur un écran externe.















