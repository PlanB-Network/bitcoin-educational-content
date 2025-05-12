---
name: Umbrel LND
description: Tutoriel avancé sur l'installation et la configuration de Lightning Network Daemon (LND) sur Umbrel
---
![cover](assets/cover.webp)


## Introduction

Ce tutoriel avancé vous guidera pas à pas dans l'installation, la configuration et l'utilisation de l'application Lightning Node (LND) sur votre nœud Umbrel. Vous apprendrez à ouvrir des canaux, à gérer votre liquidité et à synchroniser votre nœud avec une application mobile.

## 1. Prérequis : nœud Bitcoin Umbrel fonctionnel

Avant de déployer Lightning, vous devez disposer d'un nœud Bitcoin complet opérationnel sur Umbrel. Cela implique d'installer Umbrel (sur Raspberry Pi, NAS ou autre machine) et de synchroniser entièrement la blockchain Bitcoin.

Pour installer Umbrel et configurer votre nœud Bitcoin, nous vous recommandons de suivre notre tutoriel dédié : 

https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Assurez-vous que votre nœud Bitcoin est à jour et fonctionne correctement, car le Lightning Network s'appuie sur lui pour toutes les transactions hors chaîne.

## 2. Introduction au Lightning Network

Le Lightning Network est un protocole de seconde couche conçu pour accélérer et réduire le coût des transactions Bitcoin en les réalisant hors de la blockchain principale.

Concrètement, Lightning utilise un réseau de canaux de paiement entre nœuds : deux utilisateurs ouvrent un canal en bloquant des BTC on-chain (transaction initiale), puis peuvent échanger instantanément des paiements à l'intérieur de ce canal. Ces transactions off-chain ne sont pas enregistrées sur la blockchain, d'où leur rapidité et leurs frais quasi nuls.

Les paiements peuvent être routés à travers plusieurs canaux (grâce aux nœuds intermédiaires) pour atteindre n'importe quel destinataire sur le réseau, ce qui permet une échelle quasi illimitée de transactions instantanées. Lightning offre ainsi des transactions très rapides et peu coûteuses, idéales pour les paiements du quotidien ou les micro-transactions, tout en allégeant la charge sur la blockchain Bitcoin.

Pour fonctionner, un nœud Lightning doit être connecté en permanence au réseau et interagir avec d'autres nœuds Lightning. Des implémentations logicielles variées existent (LND, Core Lightning, Eclair, etc.), toutes compatibles entre elles. Umbrel utilise LND (Lightning Network Daemon) au sein de son application Lightning Node officielle. Ce tutoriel se concentre sur LND.

Pour une introduction théorique complète au Lightning Network, nous vous recommandons de suivre notre cours dédié :

https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Ce cours vous permettra d'approfondir les concepts fondamentaux du Lightning Network avant de passer à la pratique avec votre nœud LND.

## 3. Pourquoi utiliser LND en auto-hébergement ?

Exploiter son propre nœud Lightning (LND) sur Umbrel procure une souveraineté totale sur vos fonds et vos canaux, comparé aux solutions custodiales ou semi-custodiales.

### Comparaison des solutions Lightning :

**Solutions custodiales (ex: Wallet of Satoshi)** :
- Vos bitcoins Lightning sont gérés par un tiers de confiance
- Simple d'utilisation, pas de complexité technique
- L'opérateur détient vos fonds et peut tracer vos transactions
- Vous sacrifiez le contrôle et la confidentialité

**Portefeuilles non-custodiaux grand public (ex: Phoenix, Breez)** :
- L'utilisateur conserve ses clés privées et donc la propriété de ses BTC
- Pas de gestion d'un nœud complet – l'application gère les canaux en arrière-plan
- Compromis entre simplicité et souveraineté
- Dépendance vis-à-vis de l'infrastructure du fournisseur pour la liquidité
- Limites techniques (un smartphone ne peut pas router des paiements pour d'autres)

**Nœud LND auto-hébergé (Umbrel)** :
- Souveraineté maximale : vos BTC on-chain et off-chain sont entièrement sous votre contrôle
- Aucune tierce partie n'intervient pour ouvrir des canaux ou gérer vos paiements
- Confidentialité accrue (vos canaux et transactions ne sont connus que de vous et de vos pairs directs)
- Liberté d'utilisation : connexion avec vos propres services et wallets
- Possibilité de router des transactions pour d'autres (rémunération en micro-frais)
- Responsabilités techniques accrues (maintenance, gestion de la liquidité, sauvegardes)

En résumé, opérer LND en auto-hébergement vous donne le maximum de contrôle mais exige plus de compétences techniques. Il s'agit d'un arbitrage entre commodité et souveraineté.

## 4. Tutoriel pas à pas

### 4.1 Installation et configuration de l'application Lightning Node sur Umbrel

Une fois votre nœud Umbrel (Bitcoin) synchronisé, suivez ces étapes :

![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)

Installez l'application Lightning Node depuis la section "App Store" de l'interface Umbrel.

![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)

LND (Lightning Network Daemon) sera déployé sur votre Umbrel en tant qu'application. À la première ouverture, vous verrez un message d'avertissement vous informant que Lightning est une technologie expérimentale.

![Création ou restauration d'un nœud LND](assets/fr/03.webp)

Vous aurez le choix entre créer un nouveau nœud ou en restaurer un depuis une sauvegarde/seed. Pour une première installation, choisissez de créer un nouveau nœud. L'app Lightning Node va générer une phrase mnémonique de 24 mots (votre seed Lightning) : notez-la très précieusement (idéalement hors-ligne, sur papier) car elle servira à restaurer vos fonds Lightning en cas de besoin.

**Remarque** : Sur les versions récentes d'Umbrel, c'est l'installation de l'app Lightning qui fournit cette seed de 24 mots (le nœud Bitcoin Umbrel en lui-même n'en donne pas).

![Interface principale de Lightning Node](assets/fr/04.webp)

Après l'initialisation, vous accéderez à l'interface principale de Lightning Node.

![Paramètres de l'application](assets/fr/05.webp)

Dans les paramètres de l'application, vous trouverez différentes options importantes :
   - Consulter votre Node ID (identifiant unique de votre nœud)
   - Connecter un portefeuille externe (Connect wallet)
   - Voir vos mots secrets (View secret words)
   - Accéder aux paramètres avancés (Advanced Settings)
   - Récupérer des canaux (Recover channels)
   - Télécharger le fichier de sauvegarde des canaux (Download channel backup file)
   - Activer les sauvegardes automatiques (Automatic backups)
   - Configurer la sauvegarde via Tor (Backup over Tor)

Ces options sont essentielles pour la sécurité et la gestion de votre nœud Lightning. Assurez-vous particulièrement d'activer les sauvegardes automatiques et de conserver précieusement vos mots secrets.

**Ressources utiles :**
- [Umbrel Community](https://community.umbrel.com) – Forum de discussion permettant aux utilisateurs de partager leurs problèmes et solutions concernant Umbrel et son écosystème
> - [Umbrel App Store – Lightning Node (LND)](https://apps.umbrel.com/app/lightning) – Description des fonctionnalités de l'app Lightning Node sur Umbrel
> - [LND Docs – Quickstart](https://docs.lightning.engineering/lightning-network-tools/lnd/run-lnd) – Documentation officielle de LND

### 4.2 Ouverture d'un canal Lightning

Une fois LND opérationnel, vous pouvez ouvrir votre premier canal Lightning. Pour trouver des nœuds de qualité avec lesquels se connecter :

![Page d'accueil Amboss.space](assets/fr/06.webp)

[Amboss.space](https://amboss.space/) est un explorateur qui permet de trouver des nœuds fiables pour ouvrir des canaux.

![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)

Par exemple, le [nœud d'ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) est un nœud reconnu avec d'excellentes statistiques de disponibilité et de liquidité.

![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)

Pour ce tutoriel, nous allons ouvrir un canal avec [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Les informations nécessaires pour la connexion (pubkey@ip:port) sont indiquées sur leur page Amboss.

Pour ouvrir le canal :

![Bouton d'ouverture de canal](assets/fr/09.webp)

Sur la page d'accueil de Lightning Node, cliquez sur le bouton "+ OPEN CHANNEL"

![Configuration du canal](assets/fr/10.webp)

Dans la page de configuration du canal :
   - Collez l'identifiant du nœud (Node ID) copié depuis Amboss (format : pubkey@ip:port)
   - Définissez le montant de la capacité du canal (certains nœuds comme ACINQ ont des minimums, par exemple 400k sats)
   - Ajustez les frais de transaction d'ouverture si nécessaire

![Canal en cours d'ouverture](assets/fr/11.webp)

Une fois la transaction envoyée, le canal apparaîtra comme "en cours d'ouverture" sur la page d'accueil. Il faut attendre la confirmation de la transaction on-chain.

![Détails du canal](assets/fr/12.webp)

En cliquant sur le canal, vous pouvez voir ses détails :
   - Statut actuel
   - Capacité totale
   - Répartition de la liquidité (entrante/sortante)
   - Clé publique du nœud distant
   - Et d'autres informations techniques

### Utilisation de Lightning Network+ pour obtenir de la liquidité entrante

![Lightning Network+ dans l'App Store](assets/fr/13.webp)

Lightning Network+ est disponible dans l'App Store d'Umbrel pour faciliter l'obtention de liquidité entrante.

![Interface principale de LN+](assets/fr/14.webp)

L'interface principale propose trois options importantes :
- "Liquidity Swaps" : explorer les offres de swap disponibles
- "Open For Me" : filtrer les swaps auxquels vous êtes éligible
- "To Docs" : accéder à la documentation

![Message d'erreur LN+](assets/fr/15.webp)

Note : Si vous n'avez pas encore de canal ouvert, vous verrez ce message d'erreur en cliquant sur "Open For Me".

![Liste des swaps disponibles](assets/fr/16.webp)

La page "Liquidity Swaps" montre toutes les offres de swap disponibles sur le réseau.

![Swaps éligibles](assets/fr/17.webp)

"Open For Me" filtre uniquement les swaps pour lesquels votre nœud remplit les conditions requises.

![Détails d'un swap](assets/fr/18.webp)

Exemple de détails d'un swap :
- Configuration pentagon (5 participants)
- Capacité de 300k sats par canal
- Prérequis : minimum 10 canaux ouverts avec 1M sats de capacité totale
- Places disponibles : 4/5

### 4.3 Synchronisation avec une application mobile (Zeus)

Pour piloter votre nœud Lightning à distance (smartphone), vous pouvez utiliser Zeus (application open-source disponible sur iOS/Android).

**Configuration de Zeus avec Umbrel :**

![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)

Assurez-vous que votre nœud Umbrel est accessible (par défaut via Tor).
Dans l'interface Umbrel, ouvrez l'app Lightning Node, puis cliquez sur le bouton "Connect Wallet" comme indiqué par la flèche.

![Page de connexion avec QR code](assets/fr/20.webp)

Un QR code s'affiche, contenant vos identifiants d'accès LND en format lndconnect. Ce QR code est particulièrement dense en informations, n'hésitez pas à l'agrandir pour faciliter sa lecture.

![Configuration initiale de Zeus](assets/fr/21.webp)

Sur votre téléphone :
   - Ouvrez Zeus
   - Sur la page d'accueil, appuyez sur "Advanced setup" pour connecter votre propre nœud Lightning
   - Dans les paramètres, sélectionnez "Create or connect a wallet"

![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)

Dans Zeus :
   - Choisissez "LND (REST)" comme type de connexion
   - Vous pouvez soit scanner le QR code (méthode recommandée) soit entrer manuellement les informations. (N'hésitez pas à fortement zoomer le QR code d'Umbrel car celui-ci est très dense)
   - Important : activez l'option "Use Tor" si votre Umbrel n'est accessible que via Tor (cas par défaut)
   - Enregistrez la configuration

Votre Zeus est maintenant connecté à votre nœud Umbrel et vous permet d'effectuer des paiements Lightning, de voir vos canaux, soldes, etc., tout en restant en autogestion complète.

**Options avancées de connexion :**

Par défaut, la connexion Zeus ↔ Umbrel s'effectue via Tor. Pour une connexion plus rapide, deux alternatives existent :

**Lightning Node Connect (LNC)** :
   - Mécanisme de connexion chiffrée proposé par Lightning Labs
   - Installez l'app Lightning Terminal sur Umbrel (inclut l'accès LNC)
   - Générez un QR code de connexion dans Lightning Terminal (Connect → Connect Zeus via LNC)
   - Scannez-le dans Zeus (choisissez "LNC" comme type de connexion)

**VPN Tailscale** :
   - VPN maillé facile à configurer
   - Installez Tailscale sur Umbrel (App Store) et sur votre mobile
   - Connectez Zeus via l'IP privée Tailscale au lieu de l'adresse Tor

Ces options ne sont pas obligatoires, la solution Tor + Zeus fonctionne bien dans la plupart des cas.

> **Ressources utiles :**
> - [Zeus Documentation – Umbrel Connection](https://community.umbrel.com/t/zeus-ln-mobile/7619) – Guide officiel pour connecter Zeus à Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) – Projet open-source Zeus
> - [Umbrel Community - Connecter Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guide pour connecter Zeus à Umbrel en utilisant Tailscale

## 5. Sécurité et bonnes pratiques

La gestion d'un nœud Lightning auto-hébergé requiert une attention particulière à la sécurité.

### Sauvegarde et sécurité de votre nœud

**Types de sauvegardes essentielles**

Votre nœud Lightning Umbrel nécessite deux types de sauvegardes :

**La seed phrase (24 mots)**
- Permet de récupérer les fonds on-chain
- Nécessaire pour recréer votre wallet Lightning
- À conserver de manière ultra-sécurisée (hors-ligne, sur papier)

**Le fichier de backup des canaux (SCB - Static Channel Backup)**
- Contient les informations des canaux Lightning
- Permet la fermeture forcée des canaux en cas de crash
- **Important :** Ne jamais sauvegarder manuellement le fichier `channel.db` (risque de pénalités)

**Procédure de sauvegarde manuelle**

Pour sauvegarder manuellement vos canaux :
1. Accédez au menu de Lightning Node (trois points "⋮" à côté de "+ Open Channel")
2. Téléchargez le fichier de backup des canaux
3. Exportez un nouveau SCB après chaque modification de vos canaux
4. Stockez le SCB de manière sécurisée (support chiffré, copie hors-site)

**Système de sauvegarde automatique Umbrel**

Umbrel intègre un système de sauvegarde automatique sophistiqué qui assure :

*Protection des données :*
- Chiffrement côté client avant transmission
- Envoi via le réseau Tor
- Données complétées par du remplissage aléatoire
- Clé de chiffrement unique à votre appareil

*Sécurité renforcée :*
- Sauvegardes instantanées lors des changements d'état
- Sauvegardes "leurres" à intervalles aléatoires
- Masquage des modifications de taille des sauvegardes
- Protection contre l'analyse temporelle

*Processus de restauration :*
- Identifiant et clé dérivés de votre seed Umbrel
- Restauration complète possible avec uniquement la phrase mnémonique
- Récupération automatique des dernières sauvegardes
- Restauration des paramètres et données des canaux

### Restauration en cas de crash

Si votre nœud est perdu (panne hardware, carte SD corrompue) :
- Réinstallez Umbrel
- Renseignez votre seed de 24 mots dans l'app Lightning
- Importez le fichier SCB lors de la restauration

LND contactera chaque partenaire de vos anciens canaux pour les fermer et récupérer votre part des fonds on-chain. Les canaux seront définitivement fermés (à rouvrir si nécessaire).

### Disponibilité et protection contre les fraudes

Idéalement, laissez votre nœud en ligne le plus souvent possible. En cas d'absence prolongée :
- Un pair malveillant pourrait tenter de diffuser un ancien état de canal
- Lightning prévoit un "délai de contestation" (environ 2 semaines sur LND)
- Si vous prévoyez une absence prolongée, configurez un watchtower

**Configuration d'un watchtower :**
- Dans les paramètres avancés de LND, ajoutez l'URL d'un serveur watchtower de confiance
- Vous pouvez utiliser un service public ou installer votre propre watchtower


Pour approfondir la configuration et l'utilisation des watchtowers, nous vous recommandons de consulter notre tutoriel dédié :

https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Autres bonnes pratiques

- **Mises à jour logicielles :** Maintenez Umbrel et LND à jour (corrections de sécurité)
- **Protection matérielle :** Utilisez un système stable (Raspberry Pi avec SSD, mini-PC) et un onduleur (UPS)
- **Sécurité réseau :** Conservez la configuration Tor par défaut, changez le mot de passe admin d'Umbrel (défaut : "moneyprintergobrrr")
- **Chiffrement :** Activez le chiffrement du disque si possible

## 6. Outils complémentaires

L'app Lightning Node d'Umbrel fournit l'essentiel pour gérer vos canaux, mais des outils tiers offrent des fonctionnalités avancées.

### ThunderHub

Interface web moderne de gestion de nœud Lightning installable via l'App Store Umbrel.

**Fonctionnalités :**
- Visualisation en temps réel des canaux (capacités, soldes)
- Outils de rééquilibrage intégrés
- Support des factures multi-chemins (MPP)
- Génération de QR codes LNURL
- Gestion des transactions on-chain

ThunderHub est idéal pour superviser un nœud de routage actif et effectuer des rééquilibrages simplement.

### Ride The Lightning (RTL)

Interface web compatible avec plusieurs implémentations Lightning (LND, Core Lightning, Eclair).

**Points forts :**
- Gestion multi-nœuds
- Tableaux de bord contextuels
- Support des submarine swaps (Lightning Loop)
- Authentification à 2 facteurs
- Export/import des backups de canaux

RTL est un "couteau suisse" complet pour administrer un nœud Lightning avec une approche plus orientée expert.

### Autres outils utiles

- **Lightning Shell** : Ligne de commande (lncli) via navigateur
- **BTC RPC Explorer & Mempool** : Surveillance blockchain
- **LNmetrics & Torq** : Analyse des performances de routage
- **Amboss & 1ML** : Gestion "sociale" de votre nœud (alias, contacts, analyse réseau)

L'installation de ces outils se fait en quelques clics via l'App Store d'Umbrel, sans configuration complexe.

**Ressources outils complémentaires :**
- [ThunderHub.io – Features](https://thunderhub.io) – Présentation des fonctionnalités de ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) – Documentation de RTL
- [David Kaspar – Rebalance via ThunderHub](https://blog.davidkaspar.com) – Guide pratique pour les rééquilibrages
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) – Documentation avancée pour les power-users

## Conclusion

Faire fonctionner votre propre nœud LND sur Umbrel est une étape importante vers la souveraineté financière. Bien que cela demande plus d'implication technique qu'une solution custodiale, les bénéfices en termes de contrôle, de confidentialité et de participation active au réseau Lightning sont considérables.

En suivant ce guide, vous devriez maintenant pouvoir installer LND, ouvrir des canaux, gérer votre liquidité et accéder à votre nœud à distance. N'hésitez pas à explorer progressivement les fonctionnalités avancées et les outils complémentaires à mesure que vous vous familiarisez avec l'écosystème.

Rappelez-vous que la sécurité de vos fonds dépend de vos sauvegardes et de vos pratiques. Prenez le temps de comprendre chaque aspect avant d'engager des montants importants.
