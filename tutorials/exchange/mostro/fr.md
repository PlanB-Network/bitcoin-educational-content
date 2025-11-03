---
name: Mostro
description: Plateforme d'échange Bitcoin P2P sans KYC via Lightning et Nostr
---

![cover](assets/cover.webp)

Comment acquérir ou vendre des bitcoins sans compromettre sa souveraineté financière ? Les plateformes centralisées imposent des procédures KYC invasives exposant vos données personnelles, avec possibilités de gel arbitraire de comptes ou de surveillance étatique.

**Mostro P2P** propose une alternative décentralisée combinant Lightning Network, protocole Nostr et hold invoices. Son innovation majeure : un système d'escrow automatisé où vos bitcoins restent sous votre contrôle durant tout l'échange, éliminant les risques de vol, faillite d'exchange ou confiscation arbitraire.

## Qu'est-ce que Mostro P2P ?

Mostro P2P est un protocole d'échange Bitcoin open source créé par **grunch**, développeur du populaire bot Telegram **lnp2pbot** lancé en 2021. Si lnp2pbot permettait déjà des échanges P2P sans KYC via Lightning, il présentait une vulnérabilité majeure : **Telegram constitue un point de défaillance centralisé** susceptible d'être censuré par les gouvernements.

Mostro représente l'**évolution décentralisée** de ce concept : en remplaçant Telegram par le protocole **Nostr** (réseau de relais distribués incensurable), Mostro élimine ce risque systémique. Le protocole combine Lightning Network pour les transactions instantanées, Nostr pour la communication résistante à la censure, et les **hold invoices** pour créer un escrow automatisé véritablement non-custodial.

### Architecture technique

Mostro fonctionne via trois composants :
- **Daemon Mostrod** : coordonne les échanges entre utilisateurs et Lightning Network
- **Nœud Lightning** : crée les hold invoices (escrow cryptographique ~24h)
- **Clients Mostro** : interfaces utilisateur (CLI, Mobile, Web)

Les ordres sont publiés sur Nostr comme événements publics (type 38383), tandis que les négociations privées transitent par messages chiffrés de bout en bout (NIP-59, NIP-44). Chaque instance Mostro définit ses propres frais (généralement entre 0,3% et 1%) et limites de transaction (variant de quelques milliers à plusieurs centaines de milliers de sats selon l'instance).

### Avantages décisifs

**Résistance à la censure** : Aucun gouvernement ne peut fermer Mostro tant que des relais Nostr existent quelque part dans le monde. Contrairement à lnp2pbot vulnérable via Telegram, Mostro permet des échanges **véritablement incensurables**.

**Escrow non-custodial** : Les hold invoices Lightning verrouillent vos bitcoins sans les transférer définitivement. Vos fonds restent sous votre contrôle et vous sont automatiquement restitués en cas de problème (~24h).

**Confidentialité par design** : Deux modes disponibles selon vos besoins. Le **Reputation Mode** lie votre réputation à votre clé Nostr pour construire une confiance durable. Le **Full Private Mode** privilégie l'anonymat absolu avec des clés éphémères à usage unique.

## Fonctionnalités principales

**Communication décentralisée** : Tous les ordres sont publiés sur Nostr via des événements cryptographiquement signés. Les négociations privées transitent par messages chiffrés de bout en bout, garantissant une confidentialité absolue.

**Système de réputation** : Notation 5 étoiles avec calcul itératif stocké de manière permanente sur Nostr. Permet de construire progressivement une réputation de trader fiable.

**Arbitrage décentralisé** : En cas de litige, un arbitre impartial examine les preuves et tranche selon des critères transparents. Chaque litige génère un token unique pour traçabilité.

**Flexibilité des paiements** : Support de nombreuses devises fiat via le service de taux de change yadio.io. Accepte virements SEPA, PayPal, Revolut, espèces, et toute méthode convenue entre parties.

## Clients Mostro disponibles

Mostro propose deux clients principaux opérationnels pour réaliser vos échanges P2P.

### Mostro CLI - Client en ligne de commande

Le **Mostro CLI** est le client le plus mature et fonctionnel. Écrit en Rust, il offre l'ensemble complet des fonctionnalités Mostro via une interface en ligne de commande. Compatible avec macOS, Linux et Windows.

**Commandes principales** :
- `listorders` : Afficher tous les ordres disponibles
- `neworder` : Créer un nouvel ordre d'achat ou de vente
- `takesell` / `takebuy` : Prendre un ordre de vente ou d'achat
- `fiatsent` : Confirmer l'envoi du paiement fiat
- `release` : Libérer l'escrow et finaliser l'échange
- `getdm` : Consulter les messages directs
- `rate` : Évaluer votre contrepartie après un échange

Idéal pour les utilisateurs techniques, l'automatisation et les environnements nécessitant une sécurité maximale.

### Mostro Mobile - Application smartphone

L'**application mobile** en version alpha permet des échanges P2P directement depuis votre smartphone. Interface graphique intuitive avec navigation par onglets, visualisation des ordres, filtres avancés et chat intégré pour communiquer avec vos contreparties.

Disponible pour **Android** (via APK sur GitHub), elle constitue le choix optimal pour les utilisateurs privilégiant la simplicité et le trading mobile occasionnel.

### Mostro-web - Interface web (en développement)

Interface web JavaScript avancée en cours de développement actif. Conçue pour offrir une expérience utilisateur complète avec fonctionnalités étendues de trading et gestion de portefeuille. Accès via navigateur sans installation requise.

## Installation et configuration

Ce tutoriel vous guidera à travers l'installation et l'utilisation des deux clients Mostro principaux : le CLI et l'application mobile.

### Prérequis essentiels

Avant de commencer, vous devez disposer de :

- **Un portefeuille Lightning Network** fonctionnel avec liquidité suffisante (ou compatible avec Lightning)
	- Recommandés : Phoenix, Breez, Wallet of Satoshi...
	- Minimum 1000 satoshis de liquidité pour tester

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- **Une clé privée Nostr** (format `nsec1...`)
	- Créez une clé dédiée au trading sur [nostrkeygen.com](https://nostrkeygen.com/)
	- **Important** : N'utilisez jamais votre clé Nostr personnelle principale
	- Conservez votre clé privée en lieu sûr (gestionnaire de mots de passe)

- **Optionnel mais recommandé** : VPN ou connexion Tor pour masquer votre adresse IP

https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Installation de Mostro CLI

#### Sur macOS

**Étape 1 : Vérification de Rust**

Vérifiez que Rust est installé (version 1.64+ requise) :

```bash
rustc --version
```

Si Rust n'est pas installé :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

**Étape 2 : Clonage du repository**

```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```

![Vérification Rust et clonage](assets/fr/01.webp)

**Étape 3 : Configuration**

Copiez et éditez le fichier de configuration :

```bash
cp .env-sample .env
```

Ouvrez `.env` et configurez vos paramètres :

```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```

**Important pour la synchronisation CLI/Mobile** : Pour avoir accès aux mêmes ordres sur le CLI et l'application mobile, vous devez utiliser la **même Mostro Pubkey** et les **mêmes relais Nostr** dans les deux clients. Vérifiez ces paramètres dans Settings de l'app mobile.

![Configuration .env](assets/fr/02.webp)

**Étape 4 : Installation**

Compilez et installez le CLI :

```bash
cargo install --path .
```

La compilation prend 1-2 minutes. L'exécutable `mostro-cli` sera installé dans `~/.cargo/bin/`.

![Installation du CLI](assets/fr/03.webp)

**Étape 5 : Vérification**

Vérifiez que tout fonctionne :

```bash
mostro-cli --help
```

Vous devriez voir la liste complète des commandes.

![Vérification avec --help](assets/fr/04.webp)

#### Sur Linux (Ubuntu/Debian)

Installation identique à macOS, avec l'ajout de dépendances :

```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```

Suivez ensuite les étapes 3 et 4 de la section macOS.

#### Sur Windows

Installez d'abord Rust via [rustup.rs](https://rustup.rs/), puis utilisez PowerShell :

```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```

Configuration identique : copiez `.env-sample` vers `.env` et renseignez vos paramètres.

### Installation de Mostro Mobile

#### Sur Android

**Étape 1** : Rendez-vous sur la [page des releases GitHub](https://github.com/MostroP2P/mobile/releases) et téléchargez le fichier **app-release.apk** (environ 65 MB).

![Page GitHub Releases](assets/fr/10.webp)

**Étape 2** : Une fois téléchargé, ouvrez le fichier APK depuis vos téléchargements. Android vous demandera d'autoriser l'installation depuis cette source.

![Téléchargement et installation APK](assets/fr/11.webp)

**Étape 3** : Suivez les écrans d'accueil (onboarding) qui présentent les fonctionnalités :
- **Trade Bitcoin freely - no KYC** : Échangez sans vérification d'identité grâce à Nostr
- **Privacy by default** : Choisissez entre Reputation mode et Full privacy mode
- **Security at every step** : Protection par hold invoices non-custodiales

![Écrans d'accueil Mostro](assets/fr/12.webp)

**Étape 4** : Continuez l'onboarding pour découvrir :
- **Fully encrypted chat** : Communication chiffrée de bout en bout
- **Take an offer** : Parcourez le carnet d'ordres et choisissez une offre
- **Can't find what you need?** : Créez votre propre ordre personnalisé

![Suite onboarding](assets/fr/13.webp)

**Étape 5** : Une fois l'onboarding terminé, l'app génère automatiquement une paire de clés Nostr. Accédez au menu (☰) puis **Account** pour sauvegarder vos **Secret Words** (phrase de récupération). C'est également sur cet écran que vous avez la possibilité de changer de mode de confidentialité précédent évoqué. 

![Menu et sauvegarde des clés](assets/fr/15.webp)

**Important** : Notez votre phrase de récupération dans un endroit sûr (gestionnaire de mots de passe, coffre-fort papier).

### Configuration initiale de sécurité

Quelle que soit la plateforme utilisée :

- **Clé dédiée** : Utilisez une identité Nostr distincte pour le trading
- **Petits montants** : Commencez avec moins de 10 000 sats pour vous familiariser
- **Relais multiples** : Configurez 3-5 relais géographiquement diversifiés
- **Protection réseau** : Activez VPN ou Tor pour masquer votre adresse IP
- **Wallet sécurisé** : Activez le verrouillage automatique de votre wallet Lightning

## Utilisation avec le CLI

Cette section démontre l'achat de bitcoins via Mostro CLI en suivant un cas d'usage réel.

### Étape 1 : Lister les ordres disponibles

La commande `listorders` affiche tous les ordres actifs :

```bash
mostro-cli listorders
```

Vous verrez un tableau avec les détails de chaque ordre : ID, type (buy/sell), montant, devise, méthode de paiement.

![Liste des ordres disponibles](assets/fr/05.webp)

Dans cet exemple, un ordre de vente de 5 EUR via Revolut est visible (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).

### Étape 2 : Prendre l'ordre

Pour acheter ces bitcoins, prenez l'ordre avec `takesell` :

```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```

Mostro vous demandera de fournir une **Lightning invoice** pour recevoir les BTC. Le montant exact en satoshis vous est indiqué (ici : 4715 sats).

![Prise d'ordre de vente](assets/fr/06.webp)

### Étape 3 : Fournir votre facture Lightning

Générez une facture Lightning depuis votre wallet (Phoenix, Breez, etc.) pour le montant exact, puis envoyez-la :

```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```

Le système confirme l'envoi et vous informe d'attendre que le vendeur paie la hold invoice pour activer l'escrow.

![Envoi de la Lightning invoice](assets/fr/07.webp)

### Étape 4 : Communiquer avec le vendeur

Une fois l'escrow activé, utilisez `dmtouser` pour demander les coordonnées de paiement au vendeur :

```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
  --orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
  --message "Hey what's your revtag ?"
```

![Communication avec le vendeur](assets/fr/08.webp)

### Étape 5 : Récupérer la réponse

Consultez les messages directs pour voir la réponse du vendeur :

```bash
mostro-cli getdm
```

Le vendeur vous communique son identifiant de paiement (ici son Revtag : `@satoshi`).

![Réception de la réponse](assets/fr/09.webp)

### Étape 6 : Effectuer le paiement fiat

Envoyez le paiement via la méthode convenue (Revolut dans cet exemple) vers les coordonnées fournies. **Conservez tous les justificatifs** (captures d'écran, références de transaction).

### Étape 7 : Confirmer l'envoi du paiement

Une fois le paiement effectué, signalez-le à Mostro :

```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```

### Étape 8 : Réception des bitcoins

Dès que le vendeur confirme réception du fiat et libère l'escrow avec la commande `release`, vous recevez instantanément vos bitcoins sur la Lightning invoice que vous aviez fournie.

### Étape 9 : Évaluation

Évaluez le vendeur pour contribuer à la réputation décentralisée :

```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```

### Commandes utiles

**Annuler un ordre** (avant qu'il soit pris) :
```bash
mostro-cli cancel -o <order-id>
```

**Créer un nouvel ordre de vente** :
```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```

**Ouvrir un litige** :
```bash
mostro-cli dispute -o <order-id>
```

## Utilisation avec l'application mobile

Cette section démontre la vente de bitcoins via Mostro Mobile en suivant un cas d'usage réel.

### Interface principale

L'application comporte 3 onglets principaux :

- **Order Book** : Parcourez les ordres d'achat (BUY BTC) et de vente (SELL BTC) disponibles
- **My Trades** : Consultez vos ordres actifs et historique
- **Chat** : Communiquez avec vos contreparties de manière chiffrée

![Interface principale](assets/fr/14.webp)

### Configuration recommandée

Avant de trader, configurez quelques paramètres via le menu (☰) > **Settings** :

- **Lightning Address** (optionnel) : Pour recevoir les paiements directement
- **Relays** : Ajoutez plusieurs relais Nostr pour la résilience (ex: `wss://nos.lol`, `wss://relay.damus.io`)
- **Mostro Pubkey** : Vérifiez la clé publique de l'instance Mostro que vous utilisez

![Paramètres de l'application](assets/fr/16.webp)

**Important pour la synchronisation CLI/Mobile** : Si vous utilisez à la fois le CLI et l'application mobile, configurez **exactement les mêmes relais Nostr et la même Mostro Pubkey** dans les deux clients. Sans cette configuration identique, vous ne verrez pas les mêmes ordres disponibles sur les deux interfaces. Les relais et la Mostro Pubkey visibles dans Settings (capture ci-dessus) doivent correspondre à ceux de votre fichier `.env` du CLI.

### Étape 1 : Créer un ordre de vente

Appuyez sur le bouton vert **"+"** en bas à droite, puis sélectionnez **SELL** (bouton rouge).

![Boutons de création d'ordre](assets/fr/17.webp)

Remplissez le formulaire de création :

1. **Currency** : Sélectionnez la devise que vous souhaitez recevoir (EUR, USD, etc.)
2. **Amount** : Entrez le montant en fiat (ex: 1 à 3 EUR)
3. **Payment methods** : Choisissez la méthode (ex: "Revolut")
4. **Price type** : Sélectionnez "Market Price" (prix du marché)
5. **Premium** : Ajustez la prime (slider de -10% à +10%, recommandé : 0% pour vendre rapidement)

Appuyez sur **Submit** pour publier votre ordre.

### Étape 2 : Confirmation de publication

Votre ordre est maintenant publié ! Il sera disponible pendant 24 heures. Vous pouvez l'annuler à tout moment avant qu'un acheteur ne le prenne en exécutant la commande `cancel`.

![Ordre publié](assets/fr/18.webp)

L'ordre apparaît dans l'onglet **My Trades** avec le statut "Pending" et le badge "Created by you".

### Étape 3 : Un acheteur prend votre ordre

Lorsqu'un acheteur prend votre ordre, vous recevez une notification. Consultez les détails dans **My Trades**.

![Ordre pris par un acheteur](assets/fr/19.webp)

**Instruction importante** : Vous devez maintenant **payer la hold invoice** affichée pour verrouiller vos bitcoins (ici 4674 sats pour 1-5 EUR) dans l'escrow. Vous avez **15 minutes maximum** sinon l'échange sera annulé.

Copiez la hold invoice et payez-la depuis votre wallet Lightning (Phoenix, Breez, etc.).

### Étape 4 : Communiquer avec l'acheteur

Une fois l'escrow activé, appuyez sur **CONTACT** pour ouvrir le chat chiffré avec l'acheteur.

L'acheteur (ici "anonymous-gloriaZhao") vous contactera pour demander vos coordonnées de paiement. Répondez avec vos informations (Revtag, IBAN, etc.).

![Chat avec l'acheteur](assets/fr/20.webp)

### Étape 5 : Réception du paiement fiat

Attendez de recevoir le paiement fiat sur votre compte Revolut (ou autre méthode convenue). **Vérifiez scrupuleusement** :
- Le montant exact
- L'expéditeur
- La référence si demandée

L'acheteur vous informera via le chat qu'il a envoyé le paiement. Mostro affichera également un message confirmant que le fiat vous a été envoyé.

![Confirmation d'envoi du paiement](assets/fr/20.webp)

### Étape 6 : Libérer l'escrow

Une fois que vous avez **confirmé la réception** du paiement fiat sur votre compte, appuyez sur le bouton vert **RELEASE** puis confirmer pour envoyer les sats à l'acheteur.

![Libération de l'escrow](assets/fr/20.webp)

Les bitcoins sont instantanément transférés à l'acheteur via sa Lightning invoice.

### Étape 7 : Évaluer la contrepartie

Après la libération, appuyez sur **RATE** pour évaluer l'acheteur. Sélectionnez de 1 à 5 étoiles (ici 5/5) et appuyez sur **Submit Rating**.

![Évaluation de la contrepartie](assets/fr/21.webp)

L'échange est terminé !

### Acheter des bitcoins avec l'app mobile

Le processus pour **acheter** des bitcoins est similaire mais inversé :

1. Parcourez l'onglet **Order Book** > **BUY BTC** pour voir les ordres de vente
2. Appuyez sur un ordre intéressant et consultez les détails
3. Appuyez sur **Take Order**
4. Fournissez votre Lightning invoice (générée depuis votre wallet)
5. Attendez que le vendeur active l'escrow
6. Contactez le vendeur via **CONTACT** pour obtenir ses coordonnées de paiement
7. Envoyez le paiement fiat (conservez les preuves)
8. Le vendeur libère l'escrow après vérification
9. Vous recevez les bitcoins instantanément sur votre Lightning invoice
10. Évaluez le vendeur (1-5 étoiles)

### Gestion des problèmes

**Annuler un ordre** : Dans **My Trades**, appuyez sur votre ordre puis sur le bouton **CANCEL** (disponible uniquement avant qu'il soit pris).

**Ouvrir un litige** : Si un désaccord survient, appuyez sur **DISPUTE** dans les détails de l'ordre. Joignez toutes les preuves (captures d'écran du chat, références de transaction bancaire).

## Avantages et limitations

### Avantages

**Souveraineté financière** : Vos bitcoins ne quittent jamais votre contrôle direct grâce au mécanisme de hold invoice, éliminant les risques de faillite d'exchange ou piratage.

**Résistance à la censure** : Aucune autorité ne peut fermer le réseau ou censurer vos ordres. Le système fonctionne tant qu'il existe des relais Nostr opérationnels.

**Anonymat par défaut** : Seule une clé Nostr pseudonyme vous identifie, sans KYC ni données personnelles. Communications chiffrées bout-à-bout.

**Flexibilité des paiements** : Tout mode de paiement mutuellement accepté est possible (virements, applications mobiles, espèces, troc).

### Limitations

**Développement précoce** : Interfaces rudimentaires et courbe d'apprentissage technique requise.

**Liquidité limitée** : Nombre d'ordres restreint, particulièrement pour gros montants ou devises rares.

**Exigences techniques** : Compréhension basique de Lightning et Nostr nécessaire.

**Responsabilité individuelle** : Aucun support centralisé en cas de problème, prudence requise.

## Conclusion

Mostro P2P représente une alternative prometteuse aux exchanges centralisés, combinant Lightning Network, Nostr et escrow automatisé pour des échanges véritablement décentralisés. Malgré son développement précoce et sa liquidité limitée, la plateforme offre déjà souveraineté financière, résistance à la censure et anonymat par défaut.

Pour les bitcoiners privilégiant autonomie et confidentialité, Mostro constitue une option viable méritant exploration progressive. Son architecture décentralisée garantit une évolution communautaire plutôt que commerciale, ouvrant la voie à un futur d'échanges Bitcoin véritablement libres.

## Ressources

### Documentation officielle
- [Site officiel Mostro](https://mostro.network)
- [Documentation technique](https://mostro.network/docs-english/index.html)
- [Fondation Mostro](https://mostro.foundation)

### Code source et développement
- [Dépôt GitHub principal](https://github.com/MostroP2P/mostro)
- [Client web](https://github.com/MostroP2P/mostro-web)
- [Client CLI](https://github.com/MostroP2P/mostro-cli)

### Communauté
- [Protocole Nostr](https://nostr.com)
- [Guides Lightning Network](https://lightning.network)
