---
name: BitBanana
description: Gestionnaire mobile pour votre nœud Lightning
---

![cover](assets/cover.webp)

Dans ce tutoriel, vous apprendrez à installer et configurer BitBanana sur Android pour piloter votre nœud Lightning depuis votre smartphone. Nous verrons comment connecter l'application à votre infrastructure existante (Umbrel, RaspiBlitz, myNode, ou tout nœud LND/Core Lightning), effectuer des paiements Lightning, gérer vos canaux à distance, consulter vos revenus de routage, et sauvegarder vos configurations. Vous découvrirez également les bonnes pratiques de sécurité pour protéger l'accès à votre nœud et la comparaison avec Zeus, une alternative populaire.

## Présentation de BitBanana

BitBanana est une application mobile Android open source qui transforme votre smartphone en tableau de bord complet pour contrôler à distance votre nœud Lightning. Contrairement aux portefeuilles Lightning qui embarquent un nœud local sur le téléphone, BitBanana adopte une philosophie 100% contrôle à distance : l'application ne détient aucun satoshi et se connecte uniquement à votre infrastructure existante.

Développée par Michael Wünsch sous licence MIT, l'application garantit une transparence totale avec zéro collecte de données personnelles et des builds reproductibles vérifiés. BitBanana supporte nativement LND et Core Lightning via les URIs standard (`lndconnect://` et `clngrpc://`), simplifiant drastiquement la configuration initiale. L'application reconnaît également LndHub et Nostr Wallet Connect pour les utilisateurs sans nœud personnel, bien que ces modes fonctionnent en custodial avec des fonctionnalités limitées.

L'interface offre un accès complet à toutes les fonctions critiques de votre nœud : envoi et réception de paiements (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), gestion des canaux Lightning (ouverture, fermeture, ajustement des frais, rebalancing), coin control avancé, et gestion des watchtowers. BitBanana implémente également plusieurs couches de sécurité robustes : verrouillage biométrique, mode furtif, Emergency PIN, et support Tor natif pour anonymiser les connexions.

## Plateformes supportées et installation

### Installation

BitBanana est exclusivement disponible pour Android 8.0 ou supérieur. L'application n'existe pas sur iOS et aucune version n'est prévue. Cette limitation s'explique par l'historique du projet : BitBanana est le successeur direct de Zap Android, développé initialement par Michael Wünsch qui a décidé de continuer son travail sous sa propre marque. Zap était une famille d'applications distinctes (Zap Android, Zap iOS, Zap Desktop) développées par différents contributeurs avec des bases de code séparées. BitBanana ne poursuit que la branche Android.

Par ailleurs, l'écosystème iOS présente des contraintes réglementaires et techniques significatives pour les applications Lightning non-custodial. En 2023, Apple a rejeté une mise à jour de Zeus pour "violations de licence", et en 2024, Phoenix Wallet a quitté l'App Store américain face aux incertitudes réglementaires concernant les fournisseurs de services Lightning. Ces obstacles expliquent pourquoi de nombreux développeurs Lightning privilégient Android, qui offre une politique plus ouverte pour les applications non-custodial.

Trois méthodes d'installation sont disponibles pour Android : Google Play Store (5000+ installations, mises à jour automatiques), F-Droid (builds reproductibles, vérification du code source), ou APK manuel depuis GitHub.

![BitBanana](assets/fr/01.webp)

Le site officiel bitbanana.app (gauche) met en avant "100% Self-Custodial with ZERO data collection". L'écran central présente les trois options de téléchargement : F-Droid (recommandé), Google Play, et APK. L'écran de droite montre la permission notifications pour les alertes de paiements.

L'application demande les permissions : réseau (connexion nœud), caméra (QR codes), NFC (LNURL), services arrière-plan (notifications), biométrie (sécurité), et WireGuard VPN. Aucun tracker, zéro collecte de données. Activez le verrouillage par mot de passe ou biométrie pour sécuriser l'accès.

## Configuration initiale

### Connexion à un nœud LND

Pour connecter BitBanana à votre nœud LND (Umbrel, RaspiBlitz, myNode), obtenez un URI `lndconnect` ou QR code contenant l'adresse, le certificat TLS et le macaroon d'authentification.

Pour ce tutoriel, nous utilisons un noeud LND via umbrel. Pour plus de détail à ce sujet n'hésitez pas à consulter notre tutoriel dédié : 

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)

Sur l'application Lightning Node, accédez au menu en haut à droite et sélectionnez "Connect wallet".

![BitBanana](assets/fr/04.webp)

Choisissez **gRPC (Tor)** pour une connexion via Tor (recommandé). Le QR code et les détails (Host .onion, Port 10009, Macaroon) s'affichent.

![BitBanana](assets/fr/02.webp)

Dans BitBanana, appuyez sur "CONNECT NODE", scannez le QR code ou collez l'URI. Autorisez l'accès caméra, puis vérifiez l'adresse .onion affichée avant de confirmer.

**Connexion à Core Lightning**

Si vous utilisez Core Lightning (CLN) au lieu de LND, le processus reste identique avec l'URI `clngrpc://` contenant les certificats TLS mutuels. Core Lightning supporte nativement BOLT12 (offers), permettant des factures réutilisables et des paiements récurrents non disponibles sur LND.

**Connexion sans nœud personnel (LNbits/hébergé)**

Si vous n'avez pas de nœud Lightning, BitBanana peut se connecter à des services hébergés via LndHub (protocole utilisé par BlueWallet et LNbits) ou Nostr Wallet Connect (NWC). Attention : ces modes fonctionnent en custodial (le service héberge vos fonds) avec des fonctionnalités limitées. Vous ne pourrez pas gérer de canaux ni configurer les frais de routage, uniquement envoyer et recevoir des paiements Lightning.

Pour plus de détails sur LNbits ou bien Nostr Wallet Connect, vous pouvez consulter nos différents tutoriels :

https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Utilisation quotidienne

### Interface principale

L'écran d'accueil affiche votre solde Lightning avec le menu en haut en gauche donnant accès aux sections : Channels, Routing, Sign/Verify, Nodes, Contacts, Settings, Backup. L'icône horloge (haut droite) ouvre l'historique des transactions. Les boutons "Send" et "Receive" en bas permettent de recevoir ou envoyer vos satoshis. 

![BitBanana](assets/fr/05.webp)

### Paiements Lightning et on-chain

![BitBanana](assets/fr/10.webp)

**Envoyer un paiement :** Appuyez sur le bouton "Send" depuis l'écran d'accueil. L'écran de paiement (gauche) vous propose de coller une adresse ou des données de paiement dans le champ "Address or payment data", avec un scanner QR en haut à droite pour scanner des codes. Vous pouvez également sélectionner un contact enregistré dans la section Contacts pour éviter de scanner à chaque fois.

BitBanana reconnaît intelligemment tous les formats de paiement : factures Lightning classiques (chaînes de caractères commençant par `lnbc`), Lightning Address (format email comme `utilisateur@domaine.com`), codes LNURL-pay pour les paiements dynamiques, LNURL-withdraw pour retirer des fonds, et même les paiements Keysend directement vers une clé publique Lightning sans facture préalable. L'application effectue automatiquement les résolutions LNURL nécessaires en arrière-plan.

Une fois la facture chargée, BitBanana affiche les détails complets : montant exact, frais estimés de routage, description du paiement (si fournie par le destinataire), et délai d'expiration de la facture. Après confirmation, le paiement est routé via vos canaux Lightning. Vous pouvez ensuite consulter la route empruntée hop par hop et les frais réellement payés dans les détails de la transaction.

**Recevoir un paiement :** Appuyez sur le bouton "Receive". Un sélecteur (écran droite) vous permet de choisir entre Lightning (paiement instantané via vos canaux) et On-Chain. Pour une réception Lightning, indiquez le montant souhaité en satoshis (ou laissez à 0 pour créer une facture sans montant fixe que le payeur pourra compléter), et ajoutez une description optionnelle qui apparaîtra sur la facture. BitBanana génère instantanément une facture Lightning avec QR code à scanner. Vous pouvez également copier la facture en texte pour l'envoyer via messagerie. Dès réception du paiement, une notification push vous alerte et la transaction apparaît immédiatement dans l'historique avec tous les détails.

### Canaux et routage

![BitBanana](assets/fr/06.webp)

La section "Channels" affiche vos capacités d'envoi/réception et liste vos canaux avec avatars uniques. Chaque canal montre sa répartition de liquidité entre balance locale et distante. Touchez un canal pour les détails complets et actions (fermeture, modification des frais de routage). Les trois points en haut à droite donnent accès à l'option "Rebalance" pour rééquilibrer la liquidité de vos canaux. Le bouton "+" ouvre un nouveau canal.

La section Routing (écran central) affiche les revenus de forwarding par période (1D, 1W, 1M, 3M, 6M, 1Y) avec l'historique détaillé des forwards pour optimiser votre stratégie.

Sign/Verify (écran droite) permet de signer/vérifier des messages cryptographiquement pour prouver le contrôle du nœud.

### Multi-nœuds et paramètres

![BitBanana](assets/fr/07.webp)

**Manage Nodes** : liste vos nœuds avec boutons pour ajouter manuellement, scanner QR, ou basculer entre nœuds. Vous pouvez notamment paramétrer plusieurs type de connexion pointant sur le même noeud : connexion via réseau local, via VPN ou encore via Tor. 

**Manage Contacts** : stocke vos contacts Lightning pour paiements rapides.

**Settings** : personnalisation devises, langue, avatars. Section Security & Privacy : App Lock (PIN/biométrie), Hide balance (mode furtif), Tor (anonymisation IP). Configuration oracles prix, explorateurs blocs, estimateurs frais personnalisés.

## Avantages et limitations

**Points forts :**
- Mobilité totale : pilotez votre nœud Lightning depuis n'importe où
- Fonctionnalités complètes : paiements (LNURL, Lightning Address, BOLT 12), gestion canaux, coin control, watchtowers, multi-nœuds
- Sécurité : PIN/biométrie, mode furtif, Emergency PIN, Tor natif, blocage captures d'écran
- Gratuit, open source (MIT), zéro commission, zéro collecte de données

**Limitations :**
- Nécessite un nœud Lightning actif (ou LNbits en custodial)
- Pas de version iOS prévue
- Sécuriser l'accès au téléphone est critique (macaroon admin = accès total au nœud)

## Bonnes pratiques

**Sécurité :**
- Activez le verrouillage PIN/biométrie (empêche accès non autorisé au nœud)
- Configurez un Emergency PIN (efface données sensibles en cas de contrainte)
- Ne partagez jamais votre URI de connexion ou macaroon
- Mode furtif dans environnements hostiles

**Connexion :**
- VPN mesh (Tailscale, ZeroTier) : meilleur compromis rapidité/sécurité
- Tor : confidentialité maximale, latence plus élevée
- Clearnet : éviter sauf nécessité (expose IP, ports ouverts)

### Sauvegarde et restauration

Enfin vous avez le menu "Backup" qui vous permet de sauvegarder vos configurations pour migration téléphonique ou réinstallation.

![BitBanana](assets/fr/08.webp)

**Important :** Le backup ne contient PAS la seed ni les backups de canaux (à faire sur le nœud). Il contient : configurations nœuds (adresses, certificats, macaroons), labels, contacts, paramètres. Le bouton Restore permet d'importer un backup existant. Confirmation obligatoire avant sauvegarde.

![BitBanana](assets/fr/09.webp)

Saisissez un mot de passe de chiffrement (écran droite). Le système ouvre le sélecteur de fichiers (écran gauche) pour enregistrer `BitBananaBackup_2025-XX-XX.dat`. Confirmation "Backup created".

**Sécurité :** Stockez le backup chiffré (cloud personnel, USB, NAS). Ne partagez jamais le fichier ni le mot de passe. Testez la restauration régulièrement. Le backup récupère les connexions, pas les fonds.

## BitBanana vs Zeus : Quelle différence ?

Si vous explorez les applications mobiles pour gérer un nœud Lightning, vous rencontrerez probablement Zeus, une alternative populaire à BitBanana. Contrairement à BitBanana qui se concentre exclusivement sur le contrôle à distance d'un nœud existant, Zeus adopte une approche plus complète en offrant deux modes de fonctionnement : un nœud Lightning embarqué directement dans l'application (mode embedded avec LND intégré) et la connexion à distance à un nœud externe, exactement comme BitBanana.

Cette double fonctionnalité rend Zeus particulièrement attractif pour les débutants qui souhaitent expérimenter Lightning sans infrastructure préalable. Le mode embedded permet de démarrer immédiatement avec un nœud mobile complet, tandis que les utilisateurs avancés peuvent basculer vers la connexion à distance une fois leur nœud personnel configuré. Zeus supporte également LND et Core Lightning pour la connexion distante, comme BitBanana.

Autre avantage majeur de Zeus : la disponibilité multiplateforme (iOS et Android), alors que BitBanana reste exclusivement Android. Zeus intègre également l'infrastructure LSP Olympus pour faciliter la réception de paiements Lightning via des canaux "just-in-time", un système de Point of Sale pour les commerçants, et des fonctionnalités de swap intégrées pour gérer la liquidité.

BitBanana conserve toutefois des atouts spécifiques : une interface plus simple et épurée, une meilleure expérience utilisateur (UX) grâce à son focus exclusif sur le contrôle à distance, et une approche pédagogique avec des explications contextuelles. Zeus offre davantage de fonctionnalités mais au prix d'une interface plus complexe. L'application reste particulièrement adaptée aux utilisateurs souhaitant contrôler exclusivement un nœud à distance sans fonctionnalités custodiales.

Pour découvrir Zeus en détail, vous pouvez consulter les tutoriels suivants : 

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusion

BitBanana transforme votre smartphone Android en tableau de bord Lightning complet, offrant une mobilité inédite aux opérateurs de nœuds. L'application couvre l'ensemble des fonctionnalités : paiements (tous formats), gestion canaux, coin control, watchtowers, multi-nœuds, avec une sécurité renforcée (PIN/biométrie, Tor, Emergency PIN).

Entièrement souveraine, BitBanana ne collecte aucune donnée et ne compromet ni la confidentialité ni le contrôle de vos fonds. Le code source ouvert (MIT) garantit la transparence.

## Ressources

### Documentation officielle
- [Site web BitBanana](https://bitbanana.app)
- [Documentation complète](https://docs.bitbanana.app)
- [Code source GitHub](https://github.com/michaelWuensch/BitBanana)

### Installation
- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Droid](https://f-droid.org/packages/app.michaelwuensch.bitbanana)
