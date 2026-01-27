---
name: Dana Wallet
description: Portefeuille minimaliste dédié aux Silent Payments (BIP-352)
---

![cover](assets/cover.webp)

La réutilisation d'adresses Bitcoin constitue l'une des menaces les plus directes pour la confidentialité des utilisateurs. Lorsqu'un destinataire partage une adresse unique pour recevoir plusieurs paiements, n'importe quel observateur peut retracer l'ensemble des transactions associées et reconstituer son historique financier. Ce problème affecte particulièrement les créateurs de contenu, les associations caritatives ou les activistes qui souhaitent afficher publiquement une adresse de donation sans compromettre leur vie privée ni celle de leurs donateurs.

Dana Wallet répond à cette problématique en proposant une solution élégante : les Silent Payments. Ce portefeuille minimaliste et open-source, lancé en 2024, permet de générer une adresse statique réutilisable tout en garantissant que chaque paiement reçu aboutit sur une adresse distincte sur la blockchain. L'émetteur n'a besoin d'aucune interaction préalable avec le destinataire, et aucun observateur externe ne peut relier les différentes transactions entre elles. Sur la chaîne, ces paiements ressemblent à des transactions Taproot parfaitement ordinaires.

Dana Wallet est disponible sur Mainnet et Signet, mais les développeurs le considèrent encore comme expérimental et recommandent de ne pas y déposer des fonds que vous n'êtes pas prêt à perdre. Dans ce tutoriel, nous utiliserons la version Signet pour découvrir les Silent Payments sans risquer de fonds réels.

## Qu'est-ce que Dana Wallet ?

### Philosophie et objectifs

Dana Wallet adopte une approche "SP-first" (Silent Payments en priorité) : le portefeuille génère exclusivement des adresses Silent Payments et n'accepte que ce type de paiement. Vous ne pourrez pas créer d'adresse Bitcoin classique (legacy, SegWit ou Taproot standard) avec cette application. Cette restriction volontaire permet de se concentrer pleinement sur l'apprentissage du protocole BIP-352 sans être distrait par d'autres fonctionnalités. L'interface épurée privilégie délibérément la simplicité d'utilisation à la profusion d'options, rendant l'outil accessible même aux utilisateurs découvrant les concepts de confidentialité on-chain.

Le projet est entièrement open-source, développé avec Flutter pour l'interface mobile et Rust pour la logique cryptographique interne. Cette architecture permet d'allier une expérience utilisateur fluide à des performances optimales pour les opérations de scan intensives.

### Comment fonctionnent les Silent Payments ?

Les Silent Payments (BIP-352) reposent sur un mécanisme cryptographique sophistiqué utilisant l'échange de clés de Diffie-Hellman sur courbe elliptique (ECDH). Le destinataire génère une adresse statique (commençant par `sp1...` sur mainnet ou `tsp1...` sur Signet) composée de deux clés publiques distinctes : une clé de scan ($B_{scan}$) pour détecter les paiements entrants, et une clé de dépense ($B_{spend}$) pour dépenser les fonds reçus. Cette séparation permet de conserver la clé de dépense sur un hardware wallet tout en utilisant la clé de scan sur un appareil connecté.

Lorsqu'un expéditeur souhaite effectuer un paiement, son portefeuille combine la somme des clés privées de ses inputs avec la clé publique de scan du destinataire pour calculer un secret partagé ECDH. Ce secret génère un "tweak" cryptographique qui, ajouté à la clé de dépense du destinataire, crée une adresse Taproot unique pour cette transaction.

Le destinataire peut reproduire ce calcul grâce à sa clé privée de scan et les clés publiques visibles dans la transaction (propriété mathématique de Diffie-Hellman). Cela lui permet de détecter et dépenser les fonds sans interaction préalable avec l'expéditeur.

Cette approche offre plusieurs avantages :
- **Confidentialité du destinataire** : chaque paiement aboutit sur une adresse différente
- **Confidentialité de l'expéditeur** : aucun identifiant persistant ne lie les paiements
- **Absence de serveur tiers** : le protocole fonctionne de manière autonome
- **Transactions indiscernables** : les Silent Payments ressemblent à des transactions Taproot ordinaires

Le principal inconvénient réside dans le coût du scan : le destinataire doit analyser chaque nouvelle transaction Taproot pour détecter celles qui lui sont destinées.

Si vous souhaitez approfondir le fonctionnement technique des Silent Payments, nous vous recommandons le cours BTC204 sur la confidentialité dans Bitcoin, qui comprend un chapitre dédié aux Silent Payments :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plateformes supportées

Dana Wallet est disponible sous forme d'application Android. L'APK peut être téléchargé via le dépôt F-Droid dédié fourni par les développeurs, via Obtainium, ou directement depuis GitHub. Pour les utilisateurs Linux, il est techniquement possible de compiler l'application Flutter pour desktop.

L'application n'est pas disponible sur iOS ni via les stores officiels (Google Play, App Store), ce qui reflète son statut expérimental et son orientation vers un public technique.

## Installation

### Prérequis essentiels

Pour installer Dana Wallet sur Android, vous aurez besoin d'un appareil Android avec l'option "Sources inconnues" activée dans les paramètres de sécurité. Aucun compte ni inscription n'est requis.

### Ajouter le dépôt F-Droid

La méthode recommandée consiste à ajouter le dépôt F-Droid dédié de Dana Wallet. Rendez-vous sur `fdroid.silentpayments.dev` où vous trouverez le lien du dépôt ainsi qu'un QR code à scanner. Le dépôt propose actuellement 3 applications : la version Mainnet, Development et Signet.

![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)

### Installation via F-Droid

Ouvrez l'application F-Droid sur votre appareil Android, puis accédez aux paramètres via l'icône en bas à droite. Sélectionnez "Repositories" pour gérer les sources d'applications. Appuyez sur le bouton "+" pour ajouter un nouveau dépôt, puis scannez le QR code ou collez le lien `https://fdroid.silentpayments.dev/fdroid/repo`. Une fois le dépôt ajouté, vous verrez les trois versions de Dana Wallet disponibles. Sélectionnez "Dana Wallet - Signet" et appuyez sur "Install".

![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)

## Configuration initiale

### Création du portefeuille

Au premier lancement, Dana Wallet affiche un écran d'accueil présentant sa mission : "Send and receive donations without middlemen". Appuyez sur "Begin" pour continuer. L'écran suivant présente les trois avantages clés de l'application :
- **Effortless donations** : commencez à recevoir des dons en quelques secondes
- **Privacy by default** : plus besoin de serveurs ni d'infrastructure complexe
- **Email-like experience** : envoyez et recevez des bitcoins aussi simplement qu'un email

Vous avez le choix entre "Restore" pour restaurer un portefeuille existant ou "Create new wallet" pour en créer un nouveau. Appuyez sur "Create new wallet".

![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)

L'application génère alors une phrase de récupération que vous devez noter soigneusement sur un support physique. Même pour des fonds de test sans valeur réelle, adoptez les bonnes pratiques de sauvegarde.

### Interface et paramètres

Une fois le portefeuille créé, vous accédez à l'interface principale divisée en deux onglets : "Transact" et "Settings".

L'onglet **Transact** affiche votre solde en bitcoins (et sa conversion en dollars), la liste des transactions récentes, ainsi que deux boutons d'action : "Pay" pour envoyer des fonds et un bouton de réception (icône de téléchargement).

L'onglet **Settings** propose quatre options :
- **Show seed phrase** : affiche votre phrase de récupération pour la sauvegarder
- **Change fiat currency** : modifie la devise d'affichage (USD par défaut)
- **Set backend url** : configure l'URL du serveur Blindbit (voir section suivante)
- **Wipe wallet** : efface complètement le portefeuille de l'appareil

![Interface principale Transact et menu Settings](assets/fr/04.webp)

### Le serveur Blindbit

Dana Wallet utilise un serveur d'indexation appelé **Blindbit** pour détecter vos paiements Silent Payments. Comprendre son fonctionnement est important pour évaluer le modèle de confiance de l'application.

**Pourquoi un serveur est-il nécessaire ?**

Pour détecter un Silent Payment, votre wallet doit théoriquement scanner toutes les transactions Taproot de chaque bloc et effectuer un calcul cryptographique (ECDH) pour chacune. Sur un téléphone mobile, cette opération serait trop lourde en termes de calcul et de bande passante.

Le serveur Blindbit résout ce problème en pré-calculant les données intermédiaires (appelées "tweaks") pour toutes les transactions Taproot. Votre wallet télécharge ensuite ces tweaks (33 octets par transaction) et effectue le calcul final **localement** pour vérifier si un paiement vous appartient.

**Confidentialité préservée**

Contrairement à un serveur Electrum classique où vous révélez vos adresses, le serveur Blindbit ne sait pas quels paiements vous appartiennent. Il fournit les mêmes données à tous les utilisateurs, et c'est votre téléphone qui effectue la vérification finale. Votre confidentialité est donc préservée vis-à-vis du serveur.

**Serveur par défaut**

Dana Wallet utilise le serveur public `silentpayments.dev/blindbit/signet` (pour Signet) ou `silentpayments.dev/blindbit/mainnet` (pour Mainnet). Vous pouvez modifier cette URL dans les paramètres si vous hébergez votre propre serveur.

**Héberger son propre serveur Blindbit**

Pour les utilisateurs souhaitant une souveraineté totale, il est possible d'héberger son propre serveur Blindbit Oracle. Cela nécessite :
- Un nœud Bitcoin Core complet **non-élagué** (non-pruned)
- L'installation de Blindbit Oracle (disponible sur GitHub : `setavenger/blindbit-oracle`)
- Environ 10 Go d'espace disque supplémentaire
- Des compétences techniques (compilation Go, configuration serveur)

À noter qu'il n'existe pas encore d'application packagée pour Umbrel ou Start9. L'installation reste manuelle pour le moment. C'est un domaine en évolution active, et des solutions plus accessibles pourraient émerger à l'avenir.

## Utilisation quotidienne

### Recevoir des fonds

Pour recevoir des bitcoins, appuyez sur le bouton de réception (icône de téléchargement) depuis l'écran principal. Dana Wallet affiche alors votre adresse Silent Payment complète au format `tsp1q...` sur Signet. L'interface propose plusieurs options :
- **Show QR code** : affiche le QR code de votre adresse pour un scan facile
- **Share** : partage l'adresse via les applications de votre téléphone
- **Copy** : copie l'adresse dans le presse-papiers

Comme indiqué à l'écran, vous pouvez partager cette adresse publiquement sur vos réseaux sociaux sans compromettre votre confidentialité.

![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)

Pour obtenir vos premiers fonds de test sur Signet, utilisez le faucet Silent Payments dédié accessible sur `silentpayments.dev/faucet/signet`. Copiez votre adresse `tsp1...`, collez-la dans le champ prévu sur le faucet, puis validez la demande. Patientez qu'un bloc soit miné (environ 10 minutes sur Signet).

### Envoyer un paiement

Pour envoyer des fonds, appuyez sur le bouton "Pay" depuis l'écran principal. L'écran "Choose recipient(s)" s'affiche avec trois options pour spécifier le destinataire :
- Saisir manuellement les informations de paiement
- **Paste from clipboard** : coller une adresse depuis le presse-papiers
- **Scan QR Code** : scanner un QR code contenant l'adresse

Une fois l'adresse du destinataire validée, l'écran "Enter amount" vous permet de saisir le montant à envoyer en satoshis. Votre solde disponible est affiché pour référence. Appuyez sur "Proceed to fee selection" pour continuer.

![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)

L'écran suivant vous propose trois niveaux de frais selon l'urgence souhaitée :
- **Fast** (10-30 minutes) : frais plus élevés pour une confirmation rapide
- **Normal** (30-60 minutes) : frais modérés
- **Slow** (1+ heure) : frais minimaux pour les transactions non urgentes

Après avoir sélectionné le niveau de frais, l'écran de confirmation "Ready to send?" récapitule tous les détails : adresse de destination, montant, délai estimé et frais de transaction. Vérifiez attentivement ces informations puis appuyez sur "Send" pour diffuser la transaction.

Une fois envoyée, la transaction apparaît dans votre historique avec le statut "Unconfirmed" jusqu'à son inclusion dans un bloc. Votre solde est mis à jour en conséquence.

![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)

## Avantages et limitations

### Points forts

- **Pédagogique** : interface simplifiée concentrée sur l'apprentissage des Silent Payments
- **Bidirectionnel** : supporte l'envoi et la réception, contrairement à d'autres portefeuilles
- **Open-source** : code entièrement auditable sur GitHub
- **Faucet dédié** : facilite l'obtention de fonds de test
- **Sans compte** : aucune inscription ni donnée personnelle requise

### Contraintes à considérer

- **Expérimental** : logiciel non audité, à utiliser avec prudence sur Mainnet
- **Plateforme limitée** : principalement Android, pas de version iOS
- **Fonctionnalités réduites** : pas de coin control, pas de sous-comptes, pas de Lightning
- **Scan intensif** : la détection des paiements consomme des ressources significatives

## Bonnes pratiques

### Sécurité de la seed

Même pour des tests sur Signet avec des fonds sans valeur, traitez votre phrase de récupération avec sérieux. Utilisez l'option "Show seed phrase" dans les paramètres pour la noter soigneusement. Par bonne pratique, maintenez des wallets complètement séparés pour Signet et Mainnet : n'utilisez jamais une seed créée pour des tests sur un wallet destiné à recevoir de vrais fonds.

### Avertissement sur le statut expérimental

Dana Wallet est encore considéré comme expérimental par ses développeurs. Comme ils l'indiquent clairement : "Don't use funds you aren't willing to lose" (n'utilisez pas des fonds que vous n'êtes pas prêt à perdre). Pour l'apprentissage, privilégiez la version Signet. Si vous utilisez la version Mainnet, limitez-vous à des montants symboliques.

### Sauvegarde et restauration

La récupération de fonds Silent Payments nécessite un portefeuille compatible avec le protocole BIP-352. Un wallet standard ne peut pas scanner la blockchain pour retrouver vos UTXO Silent Payments. Conservez Dana Wallet installé ou utilisez l'option "Restore" au premier lancement pour récupérer un portefeuille existant.

## Comparaison avec BIP-47 et PayJoin

| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Les Silent Payments éliminent la transaction de notification de BIP-47 au prix d'un scan plus coûteux. PayJoin résout un problème différent (corrélation des entrées) et peut se combiner avec les Silent Payments.

## Conclusion

Dana Wallet représente un outil pédagogique précieux pour découvrir les Silent Payments dans un environnement sans risque financier. Son approche minimaliste permet de comprendre les mécanismes fondamentaux du protocole BIP-352 sans être distrait par des fonctionnalités secondaires. En expérimentant sur Signet, vous développez une compréhension pratique de cette technologie prometteuse pour la confidentialité des transactions Bitcoin.

Les Silent Payments constituent une avancée significative pour concilier facilité d'usage et respect de la vie privée. L'enthousiasme de la communauté et les premières intégrations dans divers portefeuilles (Cake Wallet, BitBox02, BlueWallet pour l'envoi) laissent présager un avenir où publier une adresse de donation ne compromettra plus la confidentialité financière de son propriétaire.

## Ressources

### Documentation officielle
- Dépôt GitHub Dana Wallet : https://github.com/cygnet3/danawallet
- Dépôt F-Droid : https://fdroid.silentpayments.dev
- Site communautaire Silent Payments : https://silentpayments.xyz
- Spécification BIP-352 : https://bips.dev/352

### Outils de test Signet
- Faucet Silent Payments : https://silentpayments.dev/faucet/signet
- Explorateur Signet Mempool : https://mempool.space/signet

### Serveur Blindbit (auto-hébergement)
- Blindbit Oracle (GitHub) : https://github.com/setavenger/blindbit-oracle
