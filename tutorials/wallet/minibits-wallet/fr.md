---
name: Minibits Wallet
description: Guide pour Minibits Wallet
---

![cover](assets/cover.webp)


Dans ce tutoriel, je vais vous aider à configurer le Minibits Wallet pour qu'il utilise ecash. Une puissante technologie de paiement axée sur la protection de la vie privée qui fonctionne avec Bitcoin. Minibits est un Wallet ecash et Lightning qui permet des transferts de valeur instantanés, bon marché et privés, ce qui le rend idéal pour les transactions quotidiennes où la vie privée est importante.


Avant de nous plonger dans les Minibits, il convient de bien comprendre ce qu'est et ce que n'est pas l'ecash. Beaucoup de gens confondent ecash avec la technologie Bitcoin ou Blockchain, mais il s'agit de concepts fondamentalement différents.


Ecash n'est PAS une Bitcoin. Il ne remplace pas votre Bitcoin Wallet, mais le complète. Ecash n'est pas une Blockchain et ne vit pas sur une Ledger publique. Il est intéressant de noter que l'ecash n'est PAS une nouvelle technologie - elle est en fait antérieure au web mondial, dont les concepts ont été développés dans les années 1980 et 1990.


Ce que l'ecash EST : incroyablement privé (les transactions ne laissent aucune trace), peer-to-peer (transferts directs sans intermédiaires), et fonctionne comme un instrument numérique au porteur (si vous le possédez, vous le contrôlez). L'un des principaux avantages de l'ecash est qu'il peut être utilisé hors ligne - l'expéditeur et le destinataire peuvent être déconnectés d'Internet pendant les transactions. Ecash peut être frappé par une seule partie ou par une fédération d'entités de confiance, et c'est une technologie parfaitement complémentaire de Bitcoin, qui traite les petites transactions fréquentes tandis que Bitcoin sert de règlement Layer.


Veuillez noter que cette configuration de Minibits représente une "solution de garde", ce qui signifie que vous faites confiance à l'opérateur Mint pour gérer vos fonds. Cela introduit des risques spécifiques que vous devez comprendre avant de continuer.


Le projet affiche cette importante clause de non-responsabilité :


- Cette Wallet ne doit être utilisée qu'à des fins de recherche.
- La Wallet est une version bêta dont les fonctionnalités sont incomplètes et qui comporte des bogues connus et inconnus.
- Ne l'utilisez pas avec de grandes quantités d'ecash.
- Les espèces stockées dans la Wallet sont émises par la Monnaie
- vous faites confiance à la Monnaie pour le soutenir avec Bitcoin jusqu'à ce que vous transfériez vos avoirs vers un autre Bitcoin éclairant Wallet.
- Le protocole Cashu mis en œuvre par le Wallet n'a pas encore fait l'objet d'un examen ou d'un test approfondi.


Traitez les Minibits comme un Wallet de tous les jours, et non comme un compte d'épargne, et n'y stockez jamais de valeur significative.


## 1️⃣ Configuration de votre Wallet


Pour commencer, visitez le [Site web Minibits] (https://www.minibits.cash/) où vous trouverez des options de téléchargement pour toutes les principales plateformes. Les utilisateurs iOS peuvent télécharger à partir de l'[App Store] (https://testflight.apple.com/join/defJQgTD), tandis que les utilisateurs iOS de l'UE ont l'option supplémentaire d'installer à partir de l'[Freedom Store] (https://freedomstore.io/). Les utilisateurs d'Android peuvent obtenir l'application depuis [Google Play Store] (https://play.google.com/store/apps/details?id=com.minibits_wallet) ou télécharger le fichier APK directement depuis la page [GitHub Releases] (https://github.com/minibits-cash/minibits_wallet/releases).


Lors de l'installation des Minibits, des écrans d'introduction vous expliquent les concepts de base. Vous pouvez les lire ou les ignorer si vous êtes déjà familiarisé avec la technologie. Une fois ces étapes initiales terminées, vous serez invité à choisir entre :


- je l'ai trouvé, emmenez-moi au Wallet` pour les nouveaux utilisateurs ou
- `Recover lost Wallet` si vous restaurez à partir d'une sauvegarde.


![image](assets/en/01.webp)

Une fois la configuration initiale terminée, vous arrivez sur l'écran d'accueil, qui comporte plusieurs Elements éléments importants à noter. ① L'icône de profil dans le coin supérieur vous permet d'accéder à votre page de profil où vous pouvez accéder à vos Minibits Wallet Address et sélectionner les options de réception par lots. ② Au milieu de l'écran, vous verrez les menthes que vous pouvez utiliser, la menthe Minibits étant sélectionnée par défaut. ③ La ligne d'action en dessous propose des options pour envoyer des paiements ecash ou lightning, scanner un code QR et recevoir des paiements. ④ Enfin, la barre de navigation inférieure contient des raccourcis vers l'écran d'accueil, l'historique des transactions, les contacts et les paramètres.


![image](assets/en/02.webp)


## 2️⃣ Gérer les menthes


Par défaut, la Monnaie Minibits est activée au démarrage de l'application. Cependant, l'un des points forts d'ecash est la possibilité d'utiliser plusieurs monnaies pour une décentralisation et une sécurité accrues. Pour ajouter une autre Monnaie, allez dans " Paramètres ", puis sélectionnez " Gestion des Monnaies ", et enfin appuyez sur " Ajouter une Monnaie ".


[Bitcoinmints.com](Bitcoinmints.com) fournit une liste complète des monnaies disponibles avec les évaluations des utilisateurs pour vous aider à choisir des options fiables. L'utilisation de plusieurs monnaies réduit les risques. Si l'une des monnaies rencontre des problèmes, vos fonds sur les autres monnaies restent accessibles.


![image](assets/en/04.webp)


## 3️⃣ Création d'une sauvegarde


La sauvegarde est sans doute l'étape la plus critique de tout le processus d'installation. Pour accéder aux options de sauvegarde, naviguez vers `Settings`-> `Backup` Ici vous trouverez deux options essentielles :

1. votre phrase seed, qui contient 12 mots, vous permet de récupérer votre solde d'argent en cas de perte de votre appareil. Cette phrase seed est votre clé principale pour tous les ecashs de toutes les monnaies que vous avez ajoutées. Notez-la sur un support physique (papier ou métal) et conservez-la en lieu sûr à plusieurs endroits. Ne stockez jamais votre phrase seed sur un support numérique où elle pourrait être compromise. Consultez ce [tutoriel] (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) pour connaître les meilleures pratiques en matière de protection de votre Wallet.

2. `Wallet backup` qui contient une longue chaîne de sauvegarde.


**Attention** : Vous aurez toujours besoin de votre phrase seed lorsque vous utiliserez cette sauvegarde pour récupérer votre Wallet.


![image](assets/en/05.webp)


## 4️⃣ Créer des Minibits Wallet Address


Ensuite, naviguez vers `Contacts` en bas et personnalisez votre `Minibits Wallet Address` en appuyant sur `Change` -> `Change Wallet Address`. Entrez votre Address préféré et vérifiez la disponibilité.


![image](assets/en/07.webp)


Après avoir défini votre Address, vous serez invité à faire une petite "donation" pour soutenir le projet. Bien que cela soit optionnel, je vous recommande fortement de l'envisager si vous avez l'intention d'utiliser le service régulièrement. Les projets open-source comme Minibits s'appuient sur le soutien de la communauté pour poursuivre le développement et la maintenance. Même une petite contribution permet d'assurer la longévité du projet.


![image](assets/en/08.webp)


## 5️⃣ Nostr Setup


Si vous souhaitez donner un pourboire aux personnes que vous suivez sur Nostr, vous pouvez " Ajouter votre clé npub " en sélectionnant " Contacts " puis " Public ". Cela permet de connecter votre Minibits Wallet au réseau social Nostr, ce qui permet de donner des pourboires en toute transparence.


Vous avez également la possibilité d'"Utiliser votre propre profil" en allant dans "Paramètres" puis dans "Confidentialité" pour importer votre propre Address et votre clé Nostr. Cependant, sachez que cela empêchera votre Wallet de communiquer avec les serveurs Address de minibits.cash Nostr et LNURL, ce qui désactivera les fonctionnalités de la Address pour recevoir des zaps et des paiements.


![image](assets/en/09.webp)


## 6️⃣ Recevoir des fonds


Pour recevoir des fonds, vous devez recharger votre Wallet avec une Invoice lumineuse. Le processus est simple : tapez sur " Topup ", entrez le " Montant " que vous souhaitez ajouter, ajoutez éventuellement un " Memo ", puis tapez sur " Créer une Invoice ". Vous devrez ensuite payer cette Invoice en utilisant une autre Wallet Lightning, ce qui convertira les paiements Lightning Bitcoin en jetons ecash dans votre Wallet Minibits.


![image](assets/en/10.webp)


## 7️⃣ Envoyer des fonds


Maintenant que vous avez financé votre Wallet, vous pouvez envoyer des fonds de deux manières différentes.


### Envoyer de l'argent


La première option consiste à envoyer de l'argent directement. Tapez sur "Envoyer", puis sélectionnez "Envoyer de l'ecash", entrez le "Montant" et tapez sur "Créer token", ce qui créera un code QR que vous pourrez partager avec le destinataire ou qu'il pourra scanner directement avec son appareil. Le destinataire verra les jetons apparaître dans son Wallet compte presque instantanément, sans Blockchain frais ni délai de confirmation.


![image](assets/en/11.webp)


### Payer avec Lightning


La deuxième option consiste à payer via Lightning. Tapez sur `Envoyer`, puis sélectionnez `Payer avec Lightning`. Vous pouvez choisir parmi vos `contacts` Nostr (si vous avez connecté votre npub), ou entrer/coller un code de paiement Lightning Address, Invoice, ou LNURL en utilisant l'option `Coller` ou `Scanner`. Après avoir "confirmé" le destinataire, vous serez invité à saisir le "montant à payer", à ajouter éventuellement un mémo, puis à toucher "Confirmer" suivi de "Payer maintenant" pour terminer la transaction Lightning.


![image](assets/en/12.webp)


## 8️⃣ Créer une connexion NWC


Une autre caractéristique puissante des Minibits est la possibilité de créer des connexions "Nostr Wallet Connect (NWC)", qui permettent à d'autres applications de demander des paiements à votre Wallet sans exposer vos clés privées.


Pour configurer cela, allez dans `Settings`, puis sélectionnez `Nostr Wallet Connect`, et appuyez sur `Add connection`. Donnez à votre connexion un nom descriptif pour identifier à la fois l'application et le compte utilisateur associé. Fixez une limite quotidienne raisonnable pour contrôler le montant qui peut être dépensé par le biais de cette connexion, puis appuyez sur "Sauvegarder" pour terminer la configuration.


Cette fonction est particulièrement utile pour des services tels que Nostr Clients, où vous souhaitez activer le pourboire automatique sans avoir à approuver manuellement chaque transaction.


![image](assets/en/12.webp)


## 🎯 Conclusion


Les Minibits constituent un point d'entrée accessible dans le monde de l'ecash, offrant des paiements axés sur la protection de la vie privée qui complètent vos avoirs en Bitcoin. N'oubliez pas de toujours effectuer des sauvegardes appropriées, d'envisager l'utilisation de plusieurs monnaies pour la redondance et de ne stocker que les quantités appropriées dans cette solution de garde.


Pour des ressources supplémentaires, consultez le dépôt GitHub de Minibits, le site officiel et leur canal Telegram où la communauté discute activement des développements et résout les problèmes


- [Github] (https://github.com/minibits-cash/minibits_wallet)
- [Site web](https://www.minibits.cash/)
- [Télégramme] (https://t.me/MinibitsWallet)


L'écosystème ecash est encore en pleine évolution, mais des outils comme Minibits rendent cette puissante technologie de protection de la vie privée de plus en plus accessible aux utilisateurs quotidiens.