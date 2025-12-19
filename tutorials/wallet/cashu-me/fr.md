---
name: Cashu.me
description: Guide Cashu.me pour l'utilisation d'ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Voici un tutoriel vidéo de BTC Sessions, un guide vidéo qui vous explique comment configurer et utiliser le Bitcoin Wallet de Cashu.me, qui vous donne accès à des transactions Bitcoin simples, bon marché et privées - sans avoir besoin d'un magasin d'applications !*


Dans ce tutoriel, nous allons explorer Cashu.me, un Wallet basé sur un navigateur pour les paiements privés Bitcoin en utilisant Chaumian ecash. Avant de nous lancer, nous allons faire une brève présentation d'ecash et de son fonctionnement.


## Introduction à ecash


Imaginez que vous puissiez disposer d'espèces numériques fonctionnant exactement comme des billets de banque dans votre poche - privées, instantanées et utilisables de pair à pair sans intermédiaire. C'est ce que permet ecash : une approche de paiement numérique qui ramène la confidentialité de l'argent physique dans le monde numérique. Contrairement à l'onchain-Bitcoin, qui enregistre chaque transaction sur un Ledger public visible par tous, ecash crée des jetons privés qui représentent une valeur Bitcoin réelle tout en préservant la confidentialité de vos habitudes de consommation.


Pensez à l'ecash comme à des instruments numériques au porteur stockés sur votre appareil - si vous les détenez, vous les possédez, tout comme de l'argent physique. Ces jetons sont émis par des services de confiance appelés " Mints " qui détiennent les réserves Bitcoin sous-jacentes. Lorsque vous utilisez ecash, vous ne diffusez pas vos transactions à l'ensemble du réseau. Au lieu de cela, vous échangez des jetons privés directement avec d'autres personnes, créant ainsi une expérience de paiement qui ressemble plus à la remise d'argent liquide qu'à un paiement numérique traditionnel.


Cashu est un protocole Chaumian ecash libre et open-source conçu pour Bitcoin. La technologie s'appuie sur les recherches cryptographiques pionnières de David Chaum dans les années 1980, en utilisant des "signatures aveugles" pour garantir la confidentialité. Lorsque vous recevez des jetons ecash, la Monnaie les signe sans savoir où ils seront dépensés ensuite - une caractéristique cruciale qui empêche le suivi des transactions. Il est important de noter qu'ecash ne remplace pas Bitcoin ; il le complète en répondant à certains problèmes critiques liés aux exigences de l'architecture Bitcoin. Il offre la confidentialité des espèces physiques (qui fait défaut à la Ledger transparente de la Bitcoin) et permet des microtransactions instantanées sans les frais de la Blockchain ni les délais de confirmation.


Ecash s'intègre parfaitement au Lightning Network. Vous utilisez Lightning pour déposer des Bitcoin dans une Monnaie (convertissant votre valeur en Bitcoin en jetons Ecash) et pour les retirer plus tard (convertissant à nouveau les jetons en solde Lightning dépensable). Ensemble, ils forment une combinaison puissante : Bitcoin fournit le règlement sécurisé Layer, Lightning permet des transactions rapides et l'interopérabilité du réseau, et ecash ajoute la confidentialité Layer qui rend les paiements numériques à nouveau vraiment privés.


## Cashu.me


Cashu.me est une "Application Web Progressive (PWA)" qui implémente le protocole Cashu - une implémentation spécifique de la monnaie Chaumienne conçue pour Bitcoin. En tant que PWA, il fonctionne directement dans votre navigateur sans nécessiter d'installation à partir des magasins d'applications, bien que vous puissiez l'`installer` sur votre appareil pour un accès plus facile. Cette approche basée sur le web assure une large compatibilité entre les systèmes d'exploitation tout en maintenant la sécurité grâce à des protocoles cryptographiques plutôt qu'à des restrictions de plateforme.


## 🎉 Caractéristiques principales


Nous allons nous plonger dans les fonctionnalités et explorer ce que Cashu.me a à offrir :



- La monnaie électronique chaumienne sur Lightning** : Utilise des signatures aveugles afin que les monnaies ne puissent pas suivre les soldes des utilisateurs ou l'historique des transactions
- Autocontrôle des jetons** : Vous contrôlez les jetons ecash localement avec votre phrase seed
- Sauvegarde de la phrase seed** : phrase de récupération de 12 mots pour la restauration Wallet
- Indépendance de la monnaie** : Fonctionne avec plusieurs monnaies indépendantes - vous n'êtes pas lié à un seul fournisseur
- Des transactions instantanées et gratuites** : Les paiements sont finalisés en quelques secondes, sans frais, au sein de la même Monnaie
- Architecture préservant la vie privée** : Les monnaies ne peuvent pas voir qui effectue des transactions avec qui
- Ecash hors ligne** : Envoyer/recevoir des jetons par le biais d'un protocole de transmission local, tel que NFC, QR code, Bluetooth, etc. sans connexion Internet
- Découvrez les monnaies ecash via Nostr** : Trouver et vérifier des monnaies de confiance grâce au protocole Nostr
- Échanger des ecashs entre les monnaies** : Toutes les monnaies parlent le langage Lightning, ce qui signifie que vous pouvez transférer de la valeur entre elles.
- Contrôlez votre Wallet à distance avec Nostr Wallet Connect (NWC)** : Se connecter à d'autres applications comme Nostr Client et commencer à zapper via NWC


Le compromis essentiel est la "confiance" : alors que vous contrôlez les jetons eux-mêmes, vous devez faire confiance aux monnayeurs pour conserver les réserves Bitcoin sous-jacentes. Comme l'indique la documentation de Cashu :


> ...la Monnaie gère l'infrastructure Lightning et conserve les satoshis pour les utilisateurs d'ecash de la Monnaie. Les utilisateurs doivent faire confiance à la Monnaie pour Redeem leurs écus une fois qu'ils veulent passer à Lightning.

- Documentation Cashu, [Questions générales sur la sécurité et la confidentialité](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Cela fait d'ecash une solution de garde pour le Bitcoin lui-même, bien que vous conserviez le contrôle total des jetons.


## 1️⃣ Configuration initiale


① Commencez par visiter [Wallet.cashu.me](https://Wallet.cashu.me) dans votre navigateur. Comme Cashu.me est un `PWA`, vous n'avez pas besoin de le télécharger à partir des magasins d'applications, il suffit d'ouvrir le site directement dans votre navigateur. Pour un accès plus facile, vous pouvez éventuellement l'installer sur l'écran d'accueil de votre appareil.


② Pour installer la PWA, appuyez sur le bouton de menu ⋮ dans votre navigateur et sélectionnez `Ajouter à l'écran d'accueil`. Une fois l'installation terminée, fermez l'onglet du navigateur et lancez Cashu.me depuis l'écran d'accueil de votre appareil. Sur l'écran d'accueil, appuyez sur "Suivant" pour continuer.


③ La sécurité est essentielle. Conservez votre phrase seed en toute sécurité dans un gestionnaire de mots de passe ou, mieux encore, écrivez-la sur papier. Cette phrase de récupération de 12 mots est votre seul moyen de récupérer des fonds si vous perdez l'accès à cet appareil. Tapez sur l'icône 👁️ pour révéler votre phrase seed, écrivez soigneusement les 12 mots dans l'ordre, puis cochez la case "Je l'ai écrite". Tapez sur `Suivant` pour continuer, et cochez la case pour confirmer que vous acceptez les `termes` sur l'écran suivant.


![image](assets/en/01.webp)


Une fois l'installation terminée, vous devez vous connecter à une Monnaie. Tapez sur `ADD MINT` suivi de `DISCOVER MINTS` pour voir les monnaies recommandées par la communauté Nostr. Pour une vérification supplémentaire, vous pouvez consulter les évaluations des monnaies sur [bitcoinmints.com](bitcoinmints.com).


Ensuite, cliquez sur "Cliquer pour parcourir les menthes" pour voir la liste complète. Sélectionnez une menthe en copiant son URL, en la collant dans le champ URL et en lui donnant un nom reconnaissable. Pour cet exemple, nous utiliserons :


URL : `https://mint.minibits.cash/Bitcoin`

Nom : `Minibits`


![image](assets/en/02.webp)


Tapez sur `ADD MINT` pour terminer le processus. Sur l'écran de confirmation, vérifiez que vous faites confiance à l'opérateur de cette menthe, puis tapez à nouveau sur `ADD MINT`. La Monnaie Minibits apparaît alors sur votre écran d'accueil. Une fois votre Wallet configurée, vous devrez l'approvisionner avant d'effectuer des transactions.


![image](assets/en/03.webp)


## 2️⃣ Financement de votre Wallet


Cashu.me propose deux méthodes distinctes pour financer votre Wallet. Lorsque vous appuyez sur "Recevoir" sur l'écran d'accueil, vous verrez des options pour recevoir des fonds via "ECASH" ou via "LIGHTNING".


![image](assets/en/04.webp)


### Financement via LIGHTNING


La première option est de financer la Wallet via la Invoice Lightning. sélectionnez un hôtel des monnaies si vous avez ajouté plusieurs hôtels des monnaies et définissez le "montant (Sats)" que vous souhaitez recevoir. Vous obtenez alors un QR-Code que vous pouvez scanner avec une autre Wallet lightning ou vous pouvez simplement "copier" la Invoice et la coller dans une autre Wallet pour payer et financer votre cashu.me Wallet.


![image](assets/en/05.webp)


### Recevoir de l'argent liquide


La méthode ecash vous permet de recevoir des tokens directement d'un autre Wallet ecash. Commencez par appuyer sur le bouton `Receive`, et sélectionnez l'option `ECASH`. Vous pourrez alors choisir entre `Coller`, `Scanner` ou utiliser `NFC` pour envoyer un Cashu token depuis une autre Wallet. Si vous choisissez de coller, entrez la chaîne token que vous avez copiée d'une autre Wallet, le "Montant" et la "Monnaie" s'afficheront automatiquement. Tapez sur "RECEVOIR" pour terminer la transaction, et la Sats apparaîtra dans votre Wallet. Remarquez que votre solde est maintenant réparti entre plusieurs monnaies. Par exemple, vous pouvez avoir 1 000 Sats dans votre "Monnaie" Minibits et 1 000 Sats supplémentaires dans une "Monnaie" Coinos. Cette séparation entre les différentes monnaies est un aspect important de l'architecture de Cashu.


![image](assets/en/06.webp)


### Changement de menthe


Si vous ne faites plus confiance à une Monnaie que vous avez ajoutée, cashu.me offre la possibilité d'échanger des fonds d'une Monnaie à l'autre. Allez dans l'onglet des monnaies et faites défiler l'écran jusqu'à ce que vous voyiez " Multimint Swaps " (échange de monnaies multiples). Sélectionnez l'hôtel des monnaies "From" et "To" dans les menus déroulants et entrez le montant que vous souhaitez transférer. Touchez `SWAP` pour déplacer les tokens entre les monnaies. Cette opération sera exécutée via une transaction Lightning, vous devez donc prévoir une marge pour les frais potentiels de Lightning. Dans mon exemple, 1 sat était suffisant.


![image](assets/en/07.webp)


## 3️⃣ Envoi de fonds


Pour envoyer Sats, Cashu.me propose deux options. Envoyer via `ecash` ou via `lightning`. Jetons un coup d'œil aux deux options.


### Envoi via Lightning


Pour envoyer un message via Lightning, procédez comme suit :


1. Tapez sur "ENVOYER" sur l'écran d'accueil et sélectionnez "Éclair"

2. L'application vous demandera d'entrer un `Lightning Invoice` ou un `Address`. Vous pouvez coller le Invoice/Address directement, ou utiliser l'option de scan du code QR pour le capturer visuellement, puis confirmer avec `ENTER`

3. Sélectionnez l'hôtel des monnaies à partir duquel vous voulez payer en utilisant le champ déroulant et appuyez sur `PAY` pour confirmer. **Note** : il y a aussi une option pour utiliser `Multinut` sous `Settings` -> `Experimental` qui vous permet de payer des factures de plusieurs Monnaies en même temps.

4. Une fois le paiement effectué, vous verrez une confirmation de paiement et le montant déduit de votre solde.


![image](assets/en/08.webp)


### Envoi via ecash


L'envoi d'argent liquide est tout aussi simple.


1. Tapez sur `SEND` et sélectionnez cette fois l'option `ECASH`.

2. sélectionnez une monnaie et entrez le montant que vous voulez envoyer en Sats et appuyez sur "ENVOYER" pour confirmer

3. Cela crée un "QR Code animé" que vous pouvez personnaliser en ajustant les paramètres de vitesse et de taille. N'importe qui peut scanner ce code QR pour Redeem le Sats immédiatement, ou vous pouvez appuyer sur COPIER pour envoyer la chaîne token à quelqu'un d'autre par d'autres canaux tels que Bluetooth, NFC, ou la messagerie standard.

4. J'ouvre une autre Wallet. Collez le contenu du presse-papiers et sélectionnez `Receive ecash` dans l'autre Wallet.


![image](assets/en/09.webp)


## 4️⃣ Caractéristiques supplémentaires


Au-delà des fonctionnalités de base d'envoi et de réception, Cashu.me offre des fonctions supplémentaires puissantes qui améliorent votre expérience Bitcoin au sein de l'écosystème Nostr.


### Nostr Wallet Connect


Nostr Wallet Connect (`NWC`) transforme la façon dont vous interagissez avec les applications Nostr en créant une connexion transparente entre votre Wallet et les applications sociales. Ce protocole permet à des applications comme [Damus](https://damus.io/) ou [Primal](https://primal.net/home) de demander des paiements directement via les relais Nostr sans que vous ayez à quitter l'application.


Pour configurer `NWC` dans Cashu.me :


1. Allez dans "Réglages" dans le menu Hamburger en haut à gauche

2. Faites défiler jusqu'à la section `NOSTR Wallet CONNECT` et appuyez sur le bouton `Activer`

3. Vous fixerez ensuite une allocation pour établir le montant maximum que les applications peuvent dépenser à partir de votre Wallet.

4. Une fois configuré, vous pouvez copier la chaîne de connexion et la coller dans n'importe quel client Nostr qui supporte `NWC`, permettant ainsi une fonctionnalité de zapping et de tipping instantanée.


![image](assets/en/10.webp)


### Lightning Address via npub.cash


Cashu.me s'intègre à [npub.cash](https://npub.cash/) pour vous fournir un Lightning Address qui fonctionne parfaitement avec le protocole Nostr. Ici, vous pouvez vous inscrire et réclamer votre nom d'utilisateur en fournissant votre Nostr `nsec`, qui coûte 5,000 Sats et soutient le projet npub.cash, ou vous pouvez utiliser n'importe quelle clé publique Nostr (`npub`) sans enregistrement.


Tout d'abord, allez dans `Settings` et appuyez sur `Enable` Lightning Address with npub.cash. Cela va generate créer un npub.cash Address en utilisant une chaîne `npub` dérivée de votre phrase Wallet seed par défaut.


Vous pouvez également visiter [cette page web](https://npub.cash/username) pour demander un nom d'utilisateur personnalisé en utilisant votre propre Nostr `nsec`, ce qui vous donnera un Lightning Address personnalisé comme username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Conclusion


Cashu.me propose des paiements privés Bitcoin qui fonctionnent comme de l'argent liquide - instantanément et de pair à pair sans exposer l'historique de vos transactions. J'apprécie personnellement son architecture PWA, qui permet de s'affranchir des restrictions imposées par les magasins d'applications. En combinant la sécurité du Bitcoin, la vitesse de Lightning et la confidentialité d'ecash, le Wallet offre des cas d'utilisation qui pourraient améliorer l'adoption quotidienne du Bitcoin.


Bien que vous ayez un contrôle total sur vos jetons ecash grâce à l'autoconservation, n'oubliez pas que les monnayeurs sont des tiers de confiance qui détiennent les réserves Bitcoin sous-jacentes. La possibilité d'utiliser plusieurs monnaies et d'échanger entre elles offre une certaine flexibilité tout en préservant la confidentialité.


Grâce à des fonctionnalités telles que les adresses NWC et npub.cash, Cashu.me est une option Wallet attrayante pour les clients sociaux qui privilégient le respect de la vie privée et la souveraineté par rapport aux restrictions politiques des grandes entreprises technologiques.


## 📚 Ressources


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)