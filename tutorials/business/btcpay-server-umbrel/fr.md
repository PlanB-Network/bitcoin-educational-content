---
name: BTCPay Server - Umbrel
description: Installation et utilisation de BTCPay Server sur Umbrel pour accepter Bitcoin et Lightning
---

![cover](assets/cover.webp)

Dans l'écosystème Bitcoin, accepter des paiements représente un défi majeur pour commerçants et entreprises. Les solutions traditionnelles, qu'elles soient bancaires (cartes bancaires, Stripe, PayPal) ou même Bitcoin (BitPay, Coinbase Commerce), imposent des intermédiaires qui prélèvent des frais substantiels, collectent vos données commerciales sensibles, et peuvent bloquer ou censurer vos transactions selon leur bon vouloir. Cette dépendance va à l'encontre des principes fondamentaux de Bitcoin : décentralisation, confidentialité et souveraineté financière.

BTCPay Server émerge comme la réponse open-source à cette problématique. Ce processeur de paiement auto-hébergé transforme votre propre nœud Bitcoin en infrastructure professionnelle, sans intermédiaire, sans frais de traitement supplémentaires et sans compromis sur la vie privée. Développé par une communauté mondiale de contributeurs depuis 2017, BTCPay Server vous permet de recevoir des paiements Bitcoin et Lightning directement dans vos portefeuilles, en conservant le contrôle total de vos fonds à tout moment.

Traditionnellement, installer BTCPay Server exige des compétences techniques avancées : configuration de serveur Linux, maîtrise de Docker, gestion de certificats SSL et sécurisation réseau. Umbrel révolutionne cette approche en proposant une installation en un clic directement intégrée avec votre nœud Bitcoin et Lightning. Cette simplification rend accessible à tous ce qui était auparavant réservé aux techniciens expérimentés.

**Point important à comprendre** : BTCPay Server sur Umbrel fonctionne par défaut sur votre réseau local uniquement. Vous pouvez créer des factures, accepter des paiements Lightning et Bitcoin, et gérer votre comptabilité depuis n'importe quel appareil connecté à votre réseau domestique (ordinateur, smartphone, tablette). Cette configuration convient parfaitement pour facturer des services en présentiel, gérer des paiements en face-à-face, ou utiliser BTCPay Server depuis votre réseau local. En revanche, pour intégrer BTCPay Server à une boutique en ligne accessible publiquement sur Internet, une configuration supplémentaire avec exposition publique sera nécessaire (nous aborderons cette problématique en fin de tutoriel).

Ce tutoriel vous accompagne à travers l'installation complète de BTCPay Server sur Umbrel, la configuration de votre portefeuille Bitcoin et de votre nœud Lightning, la création et le paiement de factures, ainsi que la gestion du reporting comptable. Vous découvrirez comment utiliser BTCPay Server efficacement sur votre réseau local, puis nous évoquerons les solutions pour une exposition publique si vous souhaitez l'intégrer à un site e-commerce.

## Prérequis

Pour suivre ce tutoriel, vous devez disposer d'Umbrel correctement installé et configuré. Si ce n'est pas encore le cas, consultez notre tutoriel dédié à l'installation d'Umbrel.

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Votre nœud Bitcoin Core doit être entièrement synchronisé avec la blockchain (100% dans l'application Bitcoin d'Umbrel). Cette synchronisation initiale nécessite généralement entre 3 jours et 2 semaines selon votre matériel et connexion Internet.

Pour accepter des paiements Lightning instantanés, vous devrez également installer LND (Lightning Network Daemon) sur Umbrel. Consultez notre tutoriel dédié à l'installation et la configuration de LND sur Umbrel si vous souhaitez activer cette fonctionnalité.

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Prévoyez au moins 50 Go d'espace disque libre pour BTCPay Server, ses bases de données et les données Lightning. Une connexion Internet stable via câble Ethernet est fortement recommandée pour éviter les déconnexions.

## Installation de BTCPay Server sur Umbrel

Depuis l’interface d’Umbrel (`umbrel.local`), accédez à l'App Store et recherchez "BTCPay Server" dans la catégorie Bitcoin.

![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)

Cliquez sur Install. Umbrel vérifie automatiquement que Bitcoin Core et LND sont installés, puis démarre le déploiement (2-5 minutes).

![Dépendances requises pour BTCPay Server](assets/fr/02.webp)

Une fois installée, ouvrez l'application. Vous devez créer un compte administrateur avec des identifiants robustes.

![Création du compte administrateur BTCPay Server](assets/fr/03.webp)

Après la création du compte, BTCPay Server vous invite immédiatement à créer votre premier magasin (store). Choisissez un nom professionnel et sélectionnez une devise de référence (EUR, USD ou BTC).

![Création du premier magasin BTCPay Server](assets/fr/04.webp)

## Accéder à BTCPay Server sur votre réseau local

BTCPay Server est accessible depuis n'importe quel appareil de votre réseau local (WiFi ou Ethernet). Accédez depuis votre navigateur à : 

```url
http://umbrel.local
```

Ou bien directement à :

```url
http://umbrel.local:3003
```

**Accès à distance avec Tailscale** : Pour accéder à BTCPay Server depuis n'importe où dans le monde, utilisez Tailscale. Ce VPN sécurisé vous permet de vous connecter à votre Umbrel comme si vous étiez sur votre réseau local. Consultez notre tutoriel dédié à Tailscale sur Umbrel.

https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Configurer votre portefeuille Bitcoin

Pour accepter des paiements, vous devez configurer un portefeuille Bitcoin. BTCPay Server affiche les options de configuration dans le tableau de bord.

![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)

Pour configurer le wallet Bitcoin, rendez-vous dans la section "Wallets" > "Bitcoin".

Vous avez deux options : créer un nouveau portefeuille directement dans BTCPay, ou importer un portefeuille existant. Pour l'import, plusieurs méthodes sont proposées :
- **Connect hardware wallet** (recommandé) : Importez vos clés publiques via l'application Vault
- **Import wallet file** (recommandé) : Uploadez un fichier exporté depuis votre portefeuille
- **Enter extended public key** : Saisissez manuellement votre XPub/YPub/ZPub
- **Scan wallet QR code** : Scannez un QR code depuis BlueWallet, Cobo Vault, Passport ou Specter DIY
- **Enter wallet seed** (non recommandé) : Saisissez votre phrase de récupération 12 ou 24 mots

![Options de création de portefeuille](assets/fr/06.webp)

Pour ce tutoriel, nous allons créer un nouveau Hot wallet : la clé privée sera donc stockée sur notre serveur Umbrel. Dans ce cas précis, il est fortement conseillé de déplacer les fonds régulièrement vers un portefeuille froid pour éviter de stocker des gros montants sur le serveur.

![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)

Une fois configuré, BTCPay Server confirme que votre portefeuille est prêt à accepter des paiements on-chain.

![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)

## Activer Lightning Network

Pour accepter des paiements Lightning instantanés, rendez-vous dans la section Wallets > Lightning. Ensuite, comme votre nœud LND est déjà en place sur Umbrel, il vous suffit de cliquer sur le bouton "Save" pour valider la connexion entre votre BTCPay Server et votre nœud Lightning.

![Configuration du nœud Lightning](assets/fr/09.webp)

## Créer et payer des factures

Dans l'interface BTCPay Server, naviguez vers Invoices > Create Invoice. Indiquez le montant, ajoutez une description optionnelle, et cliquez sur Create.

![Création d'une nouvelle facture](assets/fr/10.webp)

Ensuite vous pouvez cliquer sur le bouton "Checkout" pour afficher la facture. BTCPay génère alors une facture avec QR code unifié (BIP21) contenant l'adresse Bitcoin et la facture Lightning.

![Détails de la facture générée](assets/fr/11.webp)

Votre client peut scanner le QR code avec n'importe quel portefeuille compatible.

![Page de paiement avec QR code](assets/fr/12.webp)

Une fois payée, la facture passe au statut "Settled" (réglée) en quelques secondes pour Lightning.

![Confirmation de paiement réussi](assets/fr/13.webp)

## Gestion et suivi des paiements

Dans la section "Reporting", onglet "Invoices", vous trouverez l'historique complet de vos factures avec date, montant, statut et méthode de paiement. Vous pouvez l'exporter si besoin.

![Section reporting avec l'historique des factures](assets/fr/14.webp)

## Configuration du magasin

BTCPay Server permet de gérer plusieurs magasins (stores) avec des paramètres distincts. Chaque magasin représente une entité commerciale séparée : boutique e-commerce, point de vente physique, ou facturation de services.

Dans les paramètres du magasin, vous trouverez plusieurs sections importantes :

![Paramètres du magasin](assets/fr/15.webp)

- **General Settings** : Nom du magasin, devise de référence (BTC, EUR, USD), durée d'expiration des factures (15 minutes par défaut), nombre de confirmations blockchain requis
- **Rates** : Configuration des sources de taux de change et des conversions fiat/Bitcoin
- **Checkout Appearance** : Personnalisation de l'apparence de vos pages de paiement (logo, couleurs, messages personnalisés)
- **Email Settings** : Configuration des notifications par e-mail pour les paiements reçus
- **Access Tokens** : Gestion des tokens API pour intégrations e-commerce (WooCommerce, Shopify, etc.)
- **Users** : Gestion des accès utilisateurs au magasin avec différents niveaux de permissions (Owner, Guest)
- **Webhooks** : Configuration des webhooks pour synchronisation temps réel avec votre système comptable ou ERP

BTCPay Server propose également une section Plugins pour étendre les fonctionnalités avec des intégrations e-commerce, systèmes de point de vente, et outils additionnels.

![Gestion des plugins](assets/fr/16.webp)

## Avantages et limitations de l'usage local

**Avantages de BTCPay Server sur Umbrel** :
- Souveraineté totale : contrôle exclusif des clés privées et fonds, aucun tiers ne peut geler ou censurer vos paiements
- Économies substantielles : seulement frais réseau Bitcoin (quelques centimes en Lightning) vs 2-3% des processeurs traditionnels
- Confidentialité maximale : aucune inscription, vérification d'identité ou partage de données avec des entreprises tierces
- Architecture open-source garantissant transparence, auditabilité et pérennité via une large communauté de développeurs
- Installation simplifiée via Umbrel, sans compétences techniques avancées requises

**Limitations importantes** :
- **Réseau local uniquement** : BTCPay Server sur Umbrel n'est accessible que depuis votre réseau domestique. Parfait pour facturation en présentiel, services freelance ou petits commerces physiques, mais inadapté pour boutiques en ligne accessibles publiquement sur Internet.
- Responsabilité technique complète : maintenance du nœud, sauvegardes régulières, monitoring de la connectivité
- Gestion de la liquidité Lightning nécessaire : ouverture et gestion de canaux avec capacité entrante suffisante
- Support limité à la documentation communautaire et forums, requérant plus d'autonomie qu'un service client commercial

Cette limitation réseau local constitue le principal frein pour intégrer BTCPay Server à une boutique e-commerce où les clients doivent pouvoir accéder aux pages de paiement depuis n'importe où sur Internet.

## Bonnes pratiques et sécurité

Activez les sauvegardes automatiques Umbrel et stockez une copie sur support externe (clé USB, disque dur, cloud chiffré). Conservez vos seeds Bitcoin (phrases de récupération) en lieu sûr, physiquement séparé. Sauvegardez le fichier channel.backup de LND pour la récupération Lightning.

Surveillez régulièrement la synchronisation de Bitcoin Core, les canaux Lightning et la réponse de BTCPay Server. Un test hebdomadaire simple : générer et payer une facture de quelques satoshis. Maintenez Umbrel à jour (correctifs sécurité, améliorations). Effectuez une sauvegarde avant les mises à jour majeures. Pour un usage professionnel, envisagez un monitoring externe (UptimeRobot) alertant par e-mail/SMS.

## Exposer BTCPay Server publiquement pour une boutique en ligne

Pour intégrer BTCPay Server à une boutique e-commerce accessible sur Internet (WooCommerce, Shopify, etc.), vos clients doivent pouvoir accéder aux pages de paiement depuis n'importe où, pas seulement depuis votre réseau local.

**Solution : Nginx Proxy Manager**

Vous pouvez exposer BTCPay Server publiquement en utilisant Nginx Proxy Manager (disponible dans l'App Store Umbrel). Cette solution nécessite :
- Un nom de domaine (classique ou gratuit via DuckDNS, No-IP, Afraid.org)
- La configuration du port forwarding (ports 80 et 443) sur votre routeur
- L'installation de Nginx Proxy Manager qui gère automatiquement les certificats SSL

Cette configuration expose votre serveur sur Internet et nécessite une vigilance accrue (mots de passe robustes, 2FA, mises à jour régulières). Nous préparerons un tutoriel dédié détaillant cette procédure complète.

## Conclusion

BTCPay Server sur Umbrel combine la puissance du nœud Bitcoin et la simplicité d'Umbrel pour créer une infrastructure de paiement professionnelle auto-hébergée accessible à tous. Cette souveraineté financière implique une responsabilité de maintenance, mais Umbrel simplifie considérablement la charge opérationnelle comparée aux bénéfices : élimination des frais de traitement, protection de votre vie privée, résistance à la censure et contrôle total de vos fonds.

L'usage en réseau local couvre déjà de nombreux cas d'usage : facturation de services freelance, paiements en présentiel, petits commerces physiques, ou simplement apprentissage et expérimentation de Bitcoin et Lightning dans un environnement maîtrisé. Pour les besoins e-commerce nécessitant une exposition publique, la solution Nginx Proxy Manager existe mais requiert une configuration technique supplémentaire que nous détaillerons dans un tutoriel dédié.

Que vous gériez un commerce, un projet naissant ou expérimentiez simplement, BTCPay Server sur Umbrel offre une autonomie financière complète. Le chemin commence par un premier magasin, une première facture, un premier paiement reçu directement dans votre infrastructure souveraine.

## Ressources

### Documentation officielle
- [Site officiel BTCPay Server](https://btcpayserver.org)
- [Documentation complète BTCPay Server](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Documentation Tailscale](https://tailscale.com/kb)
### Communauté et support
- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)
