---
name: Tiankii
description: Suite d'outils Lightning pour commerçants et particuliers
---

![cover](assets/cover.webp)

Dans l'écosystème Bitcoin, accepter des paiements en temps réel reste un défi majeur pour les commerces et les particuliers. Les solutions traditionnelles nécessitent souvent des connaissances techniques avancées, une infrastructure complexe à maintenir, ou imposent la garde des fonds par des intermédiaires. Cette situation freine l'adoption massive de Bitcoin comme monnaie du quotidien, pourtant promise par les avancées technologiques du Lightning Network.

Tiankii, entreprise salvadorienne née en 2021, répond à cette problématique en proposant une infrastructure Bitcoin accessible et modulaire. Plutôt que de forcer l'adoption d'un écosystème fermé, Tiankii offre une suite d'outils interconnectés permettant à chacun d'intégrer Bitcoin Lightning dans ses activités sans sacrifier le contrôle de ses fonds.

## Qu'est-ce que Tiankii ?

### Origine et philosophie

Tiankii – terme nahuatl signifiant "marché à ciel ouvert accessible à tous" – est la première startup 100% Bitcoin du Salvador. Fondée par Darvin Otero après l'adoption du Bitcoin comme monnaie légale dans le pays, l'entreprise vise à transformer Bitcoin d'une réserve de valeur en monnaie transactable pour les achats quotidiens. Contrairement aux plateformes custodiales, Tiankii adopte une approche non-custodial où les utilisateurs conservent le contrôle de leurs fonds, l'infrastructure servant uniquement d'intermédiaire technique.

### Architecture technique

Tiankii se positionne comme un fournisseur d'infrastructure Bitcoin-as-a-Service basée sur le Lightning Network. Cette technologie de seconde couche permet des transactions quasi-instantanées avec des frais négligeables, rendant possible les micropaiements et les achats du quotidien.

L'architecture repose sur trois piliers :

**Lightning-first** : Privilégier systématiquement le réseau Lightning pour sa rapidité et ses coûts réduits, tout en conservant le support des transactions on-chain pour les montants importants.

**Standards ouverts** : Utilisation de LNURL pour automatiser les demandes de paiement, Lightning Address pour des identifiants lisibles de type email, et Bolt Card pour les paiements NFC interopérables.

**Modularité wallet-agnostic** : Possibilité de connecter différents portefeuilles Lightning (LNbits, Blink, BlueWallet) ou son propre nœud, offrant une flexibilité maximale selon le niveau d'expertise et d'autonomie souhaité.

## Les outils de l'écosystème Tiankii

### Bitcoin POS – Terminal de paiement en magasin

L'application transforme smartphone ou tablette en terminal Lightning. Le commerçant entre le montant en monnaie locale, l'application génère un QR code Lightning ou accepte une carte NFC Bolt Card. Les transactions sont créditées instantanément sans commission, avec conversions automatiques dans plus de 150 devises, gestion des pourboires et historique des ventes.

### Merchant Dashboard – Gestion commerciale unifiée

Interface web centralisée pour connecter son wallet Lightning, suivre les transactions en temps réel, émettre des factures et générer des rapports comptables. La plateforme agrège tous les canaux : paiements en magasin (POS), vente en ligne (plugins e-commerce), ou intégrations API. Les paiements convergent vers le portefeuille choisi.

### Bitcoin Contactless Card (Bolt Card)

La carte NFC Bolt Card représente l'innovation majeure de Tiankii pour démocratiser Bitcoin auprès du grand public. Fonctionnant comme une carte bancaire sans contact, elle permet de régler ses achats en Bitcoin Lightning par simple tapotement sur un terminal compatible.

Contrairement aux solutions custodiales classiques, cette carte suit un standard ouvert garantissant l'interopérabilité. L'utilisateur peut la lier à son propre wallet via l'application IBI, conservant ainsi ses clés privées et le contrôle total des fonds associés. Le paiement s'effectue en une seconde environ, sans nécessiter de sortir son smartphone ni d'avoir une connexion internet active au moment du paiement.

Cette solution s'avère particulièrement inclusive pour les personnes non familiarisées avec les smartphones, offrant une porte d'entrée accessible vers l'économie Bitcoin.

### IBI App – Interface individuelle Bitcoin

L'application IBI (Individual Bitcoin Interface) s'adresse aux particuliers souhaitant utiliser Bitcoin Lightning au quotidien. Son atout principal réside dans la génération d'une Lightning Address personnalisée, identifiant de paiement lisible au format email (exemple : alice@ibi.me).

Cet identifiant simplifie drastiquement la réception de paiements : plus besoin de générer une nouvelle facture pour chaque transaction, l'envoyeur peut simplement saisir l'adresse Lightning. L'interface permet également de gérer ses cartes Bolt Card (activation, désactivation, limites de dépenses), de connecter divers wallets Lightning, et d'effectuer des paiements en scannant des QR codes.

### Plugins e-commerce

Intégrations prêtes à l'emploi pour WooCommerce, Shopify et Cloudbeds. Installation en quelques minutes pour ajouter Bitcoin Lightning au checkout. Avantages : zéro commission (versus 2-3% cartes bancaires), règlement instantané, accès mondial, élimination des rétrofacturations. Les paiements arrivent directement sur le wallet connecté du marchand.

### Bitcoin API et outils développeurs

Le SDK Tiankii permet d'intégrer Bitcoin Lightning dans des applications existantes sans maintenir son propre nœud. L'API gère la création de factures, la vérification de paiements et les envois groupés via une infrastructure robuste hébergée sur Google Cloud. Le Command Center complète l'offre pour les organisations avec des Lightning Address sur domaine personnalisé, des paiements de masse, et la gestion centralisée des terminaux et cartes NFC.

## Installation et premiers pas

### Prérequis essentiels

L'utilisation de Tiankii ne nécessite aucun prérequis technique complexe. Les applications fonctionnent via navigateur web sur smartphone, tablette ou ordinateur. Aucune installation d'application native n'est requise : un simple accès à internet et un navigateur récent suffisent pour accéder à IBI ou au Merchant Dashboard.

**Pour les particuliers (IBI App)** : Aucun wallet Lightning préalable n'est nécessaire. Lors de la création de votre compte, Tiankii configure automatiquement une Lightning Address fonctionnelle via le [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), une implémentation sans nœud (nodeless) utilisant le réseau Liquid en arrière-plan. Vous pouvez immédiatement recevoir et envoyer des paiements sans configuration technique. Cette solution simplifie drastiquement l'accès pour les débutants tout en restant auto-custodiale.

**Pour les commerçants (Merchant Dashboard)** : La connexion d'un wallet Lightning existant est obligatoire pour utiliser les terminaux Point of Sale et recevoir des paiements. Tiankii supporte de nombreuses solutions : wallets mobiles (Blink, Strike), solutions auto-hébergées (LNbits, nœud LND/CLN), ou wallets web (Alby). Les guides de connexion détaillés sont disponibles dans la section Ressources de ce tutoriel.

### Pour les particuliers : IBI App

**Création du compte**

Rendez-vous sur accounts.ibi.me pour créer votre compte. Cette page vous propose de choisir entre deux types de comptes : "Personal Use" pour un usage individuel, ou "Business Use" pour un usage commercial. Sélectionnez "Personal Use" pour accéder aux outils permettant de recevoir et envoyer des paiements en Bitcoin.

![Choix du type de compte](assets/fr/01.webp)

Après avoir sélectionné "Personal Use", vous serez automatiquement redirigé vers go.ibi.me pour finaliser votre inscription. Celle-ci s'effectue via email, numéro de téléphone, ou en utilisant votre compte Google, Microsoft ou Twitter. Une fois créé, vous accédez immédiatement à votre interface IBI avec votre Lightning Address déjà opérationnelle.

![Création du compte](assets/fr/02.webp)

**Interface principale**

L'interface IBI affiche votre solde en satoshis et en devise locale (USD). Trois boutons permettent d'interagir : "Receive" pour recevoir des paiements, "Scan" pour scanner un QR code, et "Send" pour envoyer des satoshis.

![Interface IBI](assets/fr/03.webp)

**Recevoir un paiement**

Pour recevoir des satoshis, appuyez sur "Receive". L'application génère automatiquement un QR code et affiche votre Lightning Address personnalisée (format nom@ibi.me). Partagez cette adresse ou le QR code avec l'expéditeur : les fonds arrivent instantanément sur votre compte IBI.

![Réception avec Lightning Address](assets/fr/04.webp)

Une fois votre solde crédité, vous pouvez utiliser ces satoshis pour effectuer des paiements.

**Envoyer un paiement**

Pour envoyer des satoshis, appuyez sur "Send". Vous pouvez soit scanner un QR code Lightning, soit saisir directement une Lightning Address de destination.

![Solde et boutons IBI](assets/fr/05.webp)

![Interface d'envoi](assets/fr/06.webp)

Entrez le montant souhaité en satoshis, vérifiez le montant équivalent en devise locale, puis confirmez le paiement.

![Confirmation du montant](assets/fr/07.webp)

Une notification de succès confirme l'envoi avec les détails : montant envoyé, frais de transaction, et destinataire.

![Paiement réussi](assets/fr/08.webp)

**Gestion du compte**

Dans les paramètres (Settings), vous pouvez gérer vos cartes Bitcoin NFC (Bolt Cards). L'interface permet d'activer, désactiver ou configurer les limites de dépenses de vos cartes.

![Historique des transactions](assets/fr/09.webp)

![Paramètres IBI](assets/fr/10.webp)

### Pour les commerçants : Merchant Dashboard et POS

**Création du compte Business**

Rendez-vous sur accounts.ibi.me pour créer votre compte. Sélectionnez "Business Use" pour accéder aux outils commerçants. Ce type de compte débloque l'accès au Merchant Dashboard et aux terminaux point de vente.

Après avoir sélectionné "Business Use", vous serez automatiquement redirigé vers le Merchant Dashboard (pay.tiankii.com). Vous accédez alors à l'interface de gestion commerciale avec le suivi des revenus, les transactions et les outils de paiement. Pour commencer à accepter des paiements, vous devez d'abord connecter votre wallet Lightning en cliquant sur le lien en haut de page (voir la flèche sur l'image).

![Dashboard marchand](assets/fr/11.webp)

**Connexion du wallet Lightning**

Étape cruciale pour activer votre point de vente : connectez votre wallet Lightning pour recevoir les paiements. L'interface propose plusieurs options de connexion. À noter que certaines options (Bitcoin Onchain et Lightning Network) sont encore en développement et apparaissent grisées sur l'interface.

![Options de connexion wallet](assets/fr/12.webp)

Pour ce tutoriel, nous utilisons la connexion via Lightning Address, compatible avec Chivo, Blink Wallet et Strike. Saisissez votre Lightning Address (format nom@domaine.com), par exemple depuis LN Markets, Alby, ou tout autre fournisseur compatible.

![Saisie de la Lightning Address](assets/fr/13.webp)

Une fois la connexion validée, votre compte est opérationnel. Vous pouvez maintenant accéder au terminal de vente (POS) ou retourner au dashboard pour configurer d'autres paramètres.

![Connexion réussie](assets/fr/14.webp)

**Liens de paiement (Payment Links)**

Le menu "Payment Tools" donne accès à "Payment Request" permettant de créer et gérer des liens de paiement. Cette fonctionnalité est utile pour générer des liens de paiement personnalisés à envoyer par email ou message : donations, paiements uniques, paiements multiples, ou même des paywalls pour protéger du contenu. Vous pouvez créer différents types de liens selon vos besoins commerciaux.

![Liens de paiement](assets/fr/15.webp)

**Configuration du terminal de vente**

Pour accepter des paiements en magasin, accédez au menu "Sales Terminal" depuis "Payment Tools". Cette section permet de créer et gérer vos terminaux de point de vente (le nombre de terminaux dépend de votre plan, voir section Plans Freemium vs Business ci-dessous). Cliquez sur "Open" pour ouvrir l'interface du POS dans votre navigateur.

![Gestion des terminaux](assets/fr/16.webp)


**Génération d'une vente**

Le terminal POS affiche un clavier numérique pour saisir le montant de la vente. Entrez le montant dans votre devise locale (par exemple 500 sats correspondant à 630.74 ARS), puis validez avec "OK".

![Saisie du montant](assets/fr/17.webp)

L'application génère instantanément un QR code Lightning ainsi qu'une Lightning Address pour le paiement. Le client peut scanner le QR code avec son wallet ou utiliser sa carte Bolt Card sur un terminal NFC.

![QR code de paiement](assets/fr/18.webp)

Dès réception du paiement, un écran de confirmation s'affiche avec le montant reçu en devise locale et en satoshis. Vous pouvez envoyer un reçu par email, imprimer le ticket, ou démarrer une nouvelle vente immédiatement.

![Paiement encaissé](assets/fr/19.webp)

**Suivi et gestion**

Toutes les transactions sont enregistrées dans votre Merchant Dashboard. Vous disposez d'un suivi complet des revenus par période, du nombre total de ventes, et de l'historique détaillé pour votre comptabilité.

L'interface de paramètres (Settings) offre plusieurs onglets de configuration. L'onglet "General Settings" permet de gérer votre profil marchand et les notifications. L'onglet "Users" permet d'ajouter et gérer les accès au Merchant Dashboard pour votre équipe (gestion multi-utilisateurs selon votre plan). L'onglet "Development Workspace" donne accès aux clés API pour les intégrations avancées, tandis que "Subscription" permet de gérer votre abonnement.

![Paramètres du compte marchand](assets/fr/20.webp)

**Plans Freemium vs Business**

Tiankii propose deux formules pour le Merchant Dashboard. Le plan **Freemium** (gratuit) convient pour démarrer avec des limitations : un seul point de vente, un seul utilisateur, volume mensuel limité à 1 000 USD, et pas d'accès aux connecteurs e-commerce. Le plan **Business** (0,5% de frais par transaction) offre des terminaux illimités, utilisateurs illimités, volume illimité, accès aux plugins WooCommerce/Shopify/Cloudbeds, et notifications WhatsApp exclusives.

![Comparaison plans Freemium et Business](assets/fr/21.webp)

## Avantages et contraintes

### Points forts

**Auto-custodial** : Vous conservez vos clés privées et le contrôle total de vos fonds. Aucun risque de gel de compte ou de faillite d'une plateforme tierce.

**Simplicité** : Lightning Address comme une adresse email, paiements NFC par simple tapotement, interface intuitive sans expertise technique requise.

**Écosystème complet** : Outils pour tous les profils (particuliers, commerçants, développeurs) avec intégrations modulaires selon vos besoins.

**Conformité professionnelle** : Hébergement cloud sécurisé, conformité PCI-DSS, conforme à la réglementation salvadorienne.

### Limitations

**Contraintes Lightning** : Nécessite une connexion permanente du wallet, gestion de liquidité pour les gros volumes, risque d'échec si le destinataire est hors-ligne. Tiankii atténue ces aspects via des LSP intégrés.

**Dépendance SaaS** : En cas d'indisponibilité de Tiankii, génération de factures temporairement impossible (vos fonds restent sécurisés).

**Vie privée** : Tiankii peut observer les métadonnées des transactions (montants, dates). Moins privé qu'une solution auto-hébergée comme BTCPay Server par exemple.

## Conclusion

Tiankii illustre comment une infrastructure bien conçue peut lever les barrières techniques empêchant l'adoption massive de Bitcoin comme monnaie du quotidien. En combinant la puissance du Lightning Network avec une approche non-custodial et des outils accessibles, l'écosystème propose une voie équilibrée entre souveraineté financière et facilité d'usage.

Pour les commerçants, Tiankii représente une opportunité de réduire drastiquement les frais de transaction tout en accédant à une nouvelle clientèle. Pour les particuliers, les Lightning Address et cartes NFC transforment Bitcoin en monnaie praticable, sans complexité technique.

Bien que l'adoption généralisée de Bitcoin reste un défi nécessitant éducation et temps, des infrastructures comme Tiankii démontrent que les outils techniques existent déjà. La mission de simplifier les paiements Bitcoin n'est plus une vision lointaine, mais une réalité accessible à quiconque souhaite franchir le pas.

## Ressources

### Documentation officielle
- [Site officiel Tiankii](https://tiankii.com)
- [Centre d'aide Tiankii](https://help.tiankii.com)
- [Application IBI](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Command Center](https://cc.ibi.me)

### Guides de connexion de wallets
- [Connecter LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connecter BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connecter Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connecter Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)

### Communauté
- [Lightning Network Plus](https://lightningnetwork.plus) - Ressource éducative sur Lightning
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Initiative salvadorienne d'économie circulaire Bitcoin

### Outils connexes
- [Blink Wallet](https://blink.sv) - Wallet Lightning compatible recommandé
- [LNbits](https://lnbits.com) - Solution de wallet auto-hébergée
- [Standard Bolt Card](https://github.com/boltcard) - Spécifications techniques des cartes NFC
