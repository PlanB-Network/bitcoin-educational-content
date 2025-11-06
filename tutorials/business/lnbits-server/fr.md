---
name: LNbits Server
description: Installation et configuration d'un serveur LNbits auto-hébergé sur VPS Ubuntu avec Phoenixd ou sur Umbrel
---

![cover](assets/cover.webp)

LNbits est une interface web open source qui transforme n'importe quel backend Lightning (LND, Core Lightning, Phoenixd) en plateforme de services complète. Cette solution auto-hébergée permet de gérer plusieurs portefeuilles Lightning isolés, déployer des points de vente, créer des systèmes de dons ou des services de facturation, tout en conservant un contrôle total sur vos fonds.

Ce tutoriel couvre deux approches d'installation : **VPS Ubuntu avec Phoenixd** (solution légère sans nœud Bitcoin complet) et **Umbrel** (intégration avec votre nœud LND existant). Contrairement au tutoriel LNbits général de Plan ₿ Academy qui couvre les concepts et extensions, ce guide se concentre sur les procédures d'installation techniques pas à pas.

## Qu'est-ce que LNbits ?

LNbits est un système de comptabilité Lightning développé en Python (FastAPI) qui se connecte à un backend existant (LND, Core Lightning, Phoenixd). Contrairement aux nœuds Lightning traditionnels, LNbits offre une interface accessible permettant de gérer plusieurs portefeuilles isolés avec leurs propres clés API. Vous pouvez créer des sous-comptes pour votre famille, employés ou projets, sans leur donner accès à l'ensemble de vos fonds.

L'architecture découplée stocke les informations dans SQLite (par défaut) ou PostgreSQL (production), tandis que les fonds restent gérés par votre backend Lightning. Cette séparation garantit la portabilité : vous pouvez migrer de Phoenixd vers LND sans perdre vos données utilisateurs.

## Fonctionnalités clés

LNbits offre un **système d'extensions** polyvalent : TPoS (point de vente), Paywall (monétisation de contenu), Events (billetterie), LndHub (serveur pour BlueWallet), Bolt Cards (paiements NFC), Split Payments (répartition automatique), et User Manager (gestion d'utilisateurs avec authentification).

Le **tableau de bord** affiche en temps réel soldes, historique de transactions, et outils de facturation. Chaque wallet dispose d'une URL unique contenant ses clés API, permettant un accès sans login traditionnel. Le système de **clés API à trois niveaux** (admin, invoice, lecture seule) offre un contrôle granulaire des permissions pour intégrations sécurisées.

LNbits implémente nativement **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) et supporte les **Lightning Address**, garantissant la compatibilité avec les portefeuilles Lightning modernes et facilitant le déploiement de services professionnels.

## Plateformes supportées

**VPS Ubuntu** : Solution légère sans nœud Bitcoin complet. Prérequis : 1 vCPU, 1-2 Go RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nom de domaine requis pour exposition publique (services LNURL).

**Umbrel** : Installation simplifiée depuis l'App Store. Prérequis : nœud Umbrel fonctionnel avec LND synchronisé et canaux ouverts. Configuration automatique.

Vous trouverez ci-dessous les liens vers nos tutoriels Umbrel et Umbrel LND :

https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation sur VPS Ubuntu avec Phoenixd

### Étape 1 : Sécurisation du serveur VPS

**Avant toute installation**, vous devez sécuriser votre serveur VPS Ubuntu selon les règles de l'art. Cette étape est **critique** pour protéger votre infrastructure et vos fonds Lightning.

Voici un guide détaillé qui vous accompagnera dans cette configuration : **[Configuration initiale serveur Ubuntu - Guide pas à pas](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** par Daniel P. Costas.

Ce guide couvre la configuration utilisateur, SSH sécurisé, pare-feu (UFW), fail2ban, mises à jour automatiques, et bonnes pratiques de sécurité système.

### Étape 2 : Installation de Phoenixd

Une fois votre serveur sécurisé, vous devez installer et configurer Phoenixd. Plan ₿ Academy propose un tutoriel dédié complet couvrant l'installation, la génération de la seed et la configuration du service systemd :

https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Une fois Phoenixd installé et fonctionnel (vérifiez avec `./phoenix-cli getinfo`), notez le **mot de passe HTTP** dans `~/.phoenix/phoenix.conf` - vous en aurez besoin pour connecter LNbits à Phoenixd.

### Déploiement de LNbits

Installez UV et clonez LNbits :
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```

Configurez le backend Phoenixd :
```bash
cp .env.example .env && nano .env
```

Ajoutez dans `.env` :
```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```

Testez avec `uv run lnbits --host 0.0.0.0 --port 5000` puis créez un service systemd avec `Wants=phoenixd.service`.

## Configuration initiale et premier usage

### Activation du SuperUser

Activez l'interface administrateur dans `.env` :
```
LNBITS_ADMIN_UI=true
```

Redémarrez LNbits (`sudo systemctl restart lnbits`) et récupérez l'identifiant SuperUser :
```bash
cat ~/lnbits/data/.super_user
```

Accédez à `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` pour le panneau d'administration. Le menu "Server" permet de configurer les sources de financement, extensions, et comptes utilisateurs.

### Sécurisation de la création de comptes

**Important pour exposition publique** : Si vous exposez votre instance LNbits sur un nom de domaine public accessible depuis Internet, il est **critique** de désactiver la création libre de comptes utilisateurs.

Depuis l'interface d'administration SuperUser, accédez à "Settings" puis à la section "User Management". Vous y trouverez l'option "Allow creation of new users".

![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)

**Pour une exposition publique avec nom de domaine** :
- **Désactivez impérativement** l'option "Allow creation of new users"
- Sans cette protection, n'importe qui sur Internet peut créer un compte sur votre instance
- Un attaquant pourrait créer des comptes et utiliser la liquidité de votre nœud Lightning à votre insu
- Vous devrez créer manuellement les comptes utilisateurs depuis l'interface SuperUser

**Pour une utilisation locale uniquement** :
- Cette option est moins critique si votre instance n'est accessible que localement (http://localhost:5000)
- Cependant, désactiver cette option reste une bonne pratique de sécurité générale

Une fois cette configuration effectuée, seul l'administrateur SuperUser peut créer de nouveaux comptes utilisateurs via l'interface "Users". Cette approche garantit un contrôle total sur qui peut accéder à votre infrastructure Lightning et utiliser vos fonds.

### Ouverture du premier canal

Phoenixd gère automatiquement les canaux via auto-liquidity. Générez une facture Lightning de ~30 000 sats depuis LNbits et payez-la depuis un autre portefeuille. Phoenixd ouvre automatiquement un canal vers ACINQ. Les frais d'ouverture (~20-23k sats) sont déduits, le solde restant (~7-10k sats) apparaît après confirmation on-chain.

Vérifiez l'état avec `./phoenix-cli getinfo`. Considérez ensuite la désactivation de l'auto-liquidity (`auto-liquidity=off` dans `phoenix.conf`) pour contrôler les ouvertures de canaux.

### Exposition publique et HTTPS

**Important** : HTTPS obligatoire pour exposition publique (sécurité clés API + compatibilité LNURL). Ignorez cette étape pour usage local uniquement.

**Caddy (recommandé)** : SSL automatique. `sudo apt install -y caddy`, éditez `/etc/caddy/Caddyfile` :
```
votre-domaine.com {
    reverse_proxy 127.0.0.1:5000
}
```
Redémarrez : `sudo systemctl restart caddy`.

**Nginx** : Plus de contrôle. Installez `nginx certbot python3-certbot-nginx`, créez `/etc/nginx/sites-available/lnbits` :
```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Activez : `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d votre-domaine.com`

Ajoutez dans `.env` : `FORWARDED_ALLOW_IPS=*`

## Installation sur Umbrel

### Déploiement depuis l'App Store

Accédez à l'App Store Umbrel, recherchez "LNbits", et cliquez sur "Install".

![Installation LNbits Umbrel](assets/fr/01.webp)

Umbrel vérifie automatiquement les dépendances requises. LNbits nécessite Lightning Node (LND) pour fonctionner. Si votre nœud Lightning est déjà opérationnel, cliquez sur "Install LNbits" pour confirmer.

![Dépendances LNbits](assets/fr/02.webp)

Umbrel télécharge l'image Docker, configure automatiquement les connexions avec LND, et démarre le conteneur (2-5 minutes). L'installation se fait entièrement en arrière-plan.

### Configuration initiale du SuperUser

Au premier lancement, LNbits vous invite à créer le compte SuperUser administrateur. Saisissez un nom d'utilisateur et définissez un mot de passe sécurisé pour protéger l'accès à l'interface d'administration.

![Configuration SuperUser](assets/fr/03.webp)

**Important** : Ce compte SuperUser dispose de tous les privilèges sur votre instance LNbits. Choisissez un mot de passe fort et conservez-le en sécurité.

Une fois le compte créé, vous accédez automatiquement à l'interface d'administration principale. Umbrel a déjà configuré LND comme source de financement - tous les paiements Lightning transiteront par vos canaux existants.

### Accès à l'interface administrateur

Dans le menu latéral gauche, cliquez sur "Settings" pour accéder au panneau d'administration complet.

![Interface Settings](assets/fr/04.webp)

La section "Wallets Management" affiche les informations clés de votre configuration :
- **Funding Source** : LndBtcRestWallet (connexion directe à votre nœud LND Umbrel)
- **Node Balance** : Liquidité totale disponible dans vos canaux Lightning
- **LNbits Balance** : Fonds alloués au système LNbits (0 sats initialement)

Vous exploitez désormais directement la liquidité de votre nœud Umbrel pour tous les wallets LNbits que vous créerez. Aucune configuration supplémentaire n'est nécessaire - LNbits est opérationnel.

### Gestion des utilisateurs

L'une des fonctionnalités les plus puissantes de LNbits réside dans sa capacité à créer plusieurs utilisateurs indépendants, chacun avec authentification par mot de passe et wallets isolés. Cette architecture permet de profiter de la liquidité de votre nœud Umbrel tout en offrant des sous-comptes totalement isolés pour différents usages : commerce, famille, employés, projets, etc.

Dans le menu latéral, cliquez sur "Users" pour accéder à la gestion des utilisateurs. Cliquez sur "CREATE ACCOUNT" pour ajouter un nouvel utilisateur.

![Gestion des utilisateurs](assets/fr/05.webp)

Remplissez le formulaire de création d'utilisateur :
- **Username** : Nom d'utilisateur pour la connexion (exemple : "satoshi")
- **Set Password** : Activez cette option pour définir un mot de passe d'authentification
- **Password** et **Password repeat** : Définissez le mot de passe pour cet utilisateur

![Création utilisateur satoshi](assets/fr/06.webp)

Les champs optionnels (Nostr Public Key, Email, First Name, Last Name) peuvent être laissés vides pour une configuration minimale. Cliquez sur "CREATE ACCOUNT" pour valider.

![Confirmation utilisateur créé](assets/fr/07.webp)

Votre nouvel utilisateur apparaît désormais dans la liste des utilisateurs avec son identifiant unique et son nom d'utilisateur.

![Liste des utilisateurs](assets/fr/08.webp)

**Point important** : Chaque utilisateur peut se connecter de manière totalement indépendante avec son propre mot de passe. L'administrateur SuperUser conserve un contrôle total via l'interface d'administration.

### Gestion des wallets utilisateur

Maintenant que l'utilisateur "satoshi" est créé, vous devez lui attribuer un wallet Lightning. Cliquez sur l'icône des wallets (deuxième icône) pour l'utilisateur concerné, puis sur "CREATE NEW WALLET".

![Gestion des wallets](assets/fr/09.webp)

Une boîte de dialogue vous invite à nommer le wallet. Saisissez un nom descriptif (exemple : "Wallet Of Satoshi") et sélectionnez la devise d'affichage (CUC, USD, EUR, etc.).

![Création wallet](assets/fr/10.webp)

Cliquez sur "CREATE". LNbits génère instantanément un wallet Lightning fonctionnel pour cet utilisateur.

![Confirmation wallet créé](assets/fr/11.webp)

Vous voyez désormais les deux wallets existants : le wallet par défaut "LNbits wallet" créé automatiquement, et le nouveau "Wallet Of Satoshi". Pour simplifier l'expérience utilisateur, vous pouvez supprimer le wallet par défaut en cliquant sur l'icône de suppression (poubelle rouge).

![Wallet final unique](assets/fr/12.webp)

L'utilisateur "satoshi" dispose désormais d'un seul wallet clairement identifié. Chaque wallet utilisateur fonctionne de manière totalement autonome tout en utilisant la liquidité de votre nœud LND sous-jacent.

**Concept clé** : Tous ces wallets partagent la liquidité globale de votre nœud Umbrel. Vous ne créez pas de nouveaux canaux Lightning pour chaque wallet - LNbits agit comme une couche de comptabilité intelligente qui gère l'allocation des fonds au sein de votre infrastructure Lightning existante. C'est la puissance du système multi-wallet de LNbits.

### Connexion en tant qu'utilisateur

Déconnectez-vous du compte SuperUser (icône en haut à droite) et retournez sur la page de connexion LNbits. Vous pouvez désormais vous connecter avec les identifiants du nouvel utilisateur.

![Connexion utilisateur satoshi](assets/fr/13.webp)

Saisissez le nom d'utilisateur ("satoshi") et le mot de passe défini précédemment, puis cliquez sur "LOGIN". L'utilisateur accède directement à son wallet personnel, totalement isolé de l'interface d'administration.

### Interface du wallet utilisateur

Une fois connecté, l'utilisateur accède à son interface de wallet Lightning complète.

![Interface wallet utilisateur](assets/fr/14.webp)

L'interface présente :
- **Solde actuel** : Affiché en sats et dans la devise choisie (CUC dans cet exemple)
- **Actions principales** : "PASTE REQUEST" (coller une facture à payer), "CREATE INVOICE" (générer une facture de réception), icône QR (scan rapide)
- **Historique des transactions** : Liste complète de tous les paiements et réceptions
- **Panneau latéral droit** : Options de configuration et d'accès

### Accès mobile au wallet

Le panneau latéral droit offre une fonctionnalité particulièrement pratique : l'accès mobile au wallet. Dépliez la section "Mobile Access" pour découvrir les options disponibles.

![Mobile Access](assets/fr/15.webp)

LNbits propose plusieurs méthodes pour utiliser ce wallet sur smartphone :

**Option 1 : Applications mobiles compatibles**
- Téléchargez **Zeus** ou **BlueWallet** depuis App Store ou Google Play
- Activez l'extension **LndHub** dans LNbits pour ce wallet
- Scannez le QR code LndHub avec l'application mobile pour connecter le wallet

**Option 2 : Accès direct par navigateur mobile**
- Le QR code affiché dans "Export to Phone with QR Code" contient l'URL complète du wallet avec authentification intégrée
- Scannez ce QR code depuis votre smartphone pour ouvrir le wallet directement dans votre navigateur mobile
- Ajoutez la page à l'écran d'accueil pour un accès rapide

**Sécurité importante** : Cette URL contient les clés API d'accès complet au wallet. Ne la partagez jamais publiquement. Traitez ce QR code comme vous traiteriez vos clés privées Bitcoin - toute personne scannant ce QR code obtient un accès complet au wallet.

Cette fonctionnalité mobile transforme votre instance LNbits Umbrel en véritable serveur de wallets Lightning pour vous et votre entourage, tout en conservant la souveraineté complète sur vos fonds grâce à votre nœud auto-hébergé.

### Partage des accès utilisateur

Le cas d'usage principal de cette configuration multi-utilisateurs est le **partage des wallets avec votre famille ou entourage proche**. Une fois que vous avez créé un utilisateur avec son wallet dédié (comme "satoshi" dans notre exemple), vous pouvez partager ces identifiants de connexion avec les personnes de confiance de votre foyer.

**Sécurité d'accès sur Umbrel** : L'accès à votre instance LNbits sur Umbrel est naturellement protégé, car elle n'est accessible que :
- **Sur votre réseau local** : Les membres de votre foyer connectés au même réseau WiFi/Ethernet peuvent accéder à l'instance
- **Via VPN** : Si vous utilisez un VPN comme Tailscale configuré sur votre serveur Umbrel, les utilisateurs autorisés peuvent accéder à distance de manière sécurisée

Cette double couche de protection (accès réseau + authentification utilisateur) rend l'option "Allow creation of new users" moins critique sur Umbrel. Seules les personnes ayant déjà accès à votre réseau ou VPN peuvent atteindre l'interface de connexion.

**Scénario typique** : Vous créez un compte "papa", un compte "maman", un compte "commerce", etc. Chaque membre de la famille dispose de son propre wallet Lightning isolé, tout en profitant de la liquidité commune de votre nœud Umbrel. Partagez simplement le nom d'utilisateur et le mot de passe - l'utilisateur peut alors se connecter depuis n'importe quel appareil sur votre réseau local ou via votre VPN Tailscale. N'hésitez pas à consulter notre tutoriel dédié à Tailscale si besoin :

https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Explorer les extensions disponibles

Retournez sur l'interface SuperUser et accédez au menu "Extensions" dans le panneau latéral gauche pour découvrir l'écosystème complet d'extensions LNbits.

![Extensions disponibles](assets/fr/16.webp)

LNbits propose un catalogue riche d'extensions qui transforment votre instance en véritable plateforme de services Lightning :

- **Jukebox** : Système de jukebox alimenté par des sats (paiements Spotify)
- **Support Tickets** : Système de support payant (recevez des sats pour répondre aux questions)
- **TPoS** : Terminal de point de vente sécurisé et mobile pour commerçants
- **User Manager** : Gestion avancée d'utilisateurs et wallets (que nous venons d'utiliser)
- **Events** : Vente et validation de billets d'événements
- **LNURLDevices** : Gestion de points de vente, ATMs, switches connectés
- **SMTP** : Permettre aux utilisateurs d'envoyer des emails et gagner des sats
- **Boltcards** : Programmation de cartes NFC pour paiements Lightning tap-to-pay
- **NostrNip5** : Création d'adresses NIP5 pour vos domaines
- **Splitpayments** : Répartition automatique de paiements entre plusieurs wallets

Chaque extension s'active en un clic depuis cette interface. Les extensions marquées "FREE" sont gratuites, tandis que certaines peuvent être en version "PAID". Explorez le catalogue pour identifier celles qui correspondent à vos besoins - qu'il s'agisse de commerce, de gestion familiale, ou d'expérimentation avec les possibilités du Lightning Network.

## Avantages et limitations

**Avantages** : Souveraineté financière (contrôle total fonds/clés/données), flexibilité architecturale (migration VPS→nœud complet sans perte), système d'extensions professionnel, interface intuitive.

**Limitations** : Logiciel en beta (prudence sur montants), sécurité sous responsabilité de l'administrateur, URLs contenant clés API sensibles (HTTPS obligatoire), gestion multi-utilisateurs implique responsabilité custodiale.

## Bonnes pratiques

**Sauvegardes** : Seed Phoenixd/credentials LND, base de données LNbits, fichiers `.env`. Automatisez quotidiennement, conservez-les hors du serveur de production, chiffrées. Testez les restaurations régulièrement.

**Maintenance** : Surveillez régulièrement les mises à jour (LNbits, backend Lightning, système d'exploitation). Consultez toujours les release notes avant mise à jour majeure.

- **Sur Umbrel** : App Store notifie automatiquement les nouvelles versions. Synchronisez les extensions via "Manage Extensions" > "Update All". Vérifiez inclusion base SQLite dans sauvegardes automatiques Umbrel.
- **Sur VPS** : Mise à jour manuelle avec `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Surveillez logs système : `sudo journalctl -u lnbits -f`.

## Conclusion

L'auto-hébergement de LNbits offre une voie concrète vers la souveraineté financière Lightning. VPS+Phoenixd propose une solution légère pour services rapides, Umbrel une intégration complète avec nœud Bitcoin existant. L'architecture extensible permet d'évoluer du simple wallet multi-utilisateurs vers des cas d'usage professionnels sophistiqués.

L'auto-hébergement implique responsabilités : sauvegardez seeds, protégez accès, démarrez avec montants modestes. Avec ces précautions, LNbits devient une solution robuste pour l'économie Lightning tout en préservant décentralisation et autonomie.

## Ressources

### Documentation officielle
- [LNbits Documentation](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Guide d'installation officiel](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)

### Guides communautaires
- [Configuration initiale serveur Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) par Daniel P. Costas (sécurisation VPS pas à pas)
- [Installation LNbits + Phoenixd sur VPS Ubuntu](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) par Daniel P. Costas (guide complet)
- [LNbits Server sur Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) par Axel
- [LNbits sur VPS](https://github.com/TrezorHannes/vps-lnbits) par Hannes
