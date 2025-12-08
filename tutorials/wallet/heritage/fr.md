---
name: Heritage
description: Un portefeuille Bitcoin avec mécanisme d'héritage intégré via scripts Taproot
---

![cover](assets/cover.webp)

## Introduction

La transmission de bitcoins en cas de décès ou d'incapacité représente un défi majeur pour tout détenteur de crypto-actifs. Sans plan d'héritage adapté, ces actifs deviennent irrécupérables pour vos proches.

Heritage apporte une réponse élégante en implémentant un mécanisme de dead-man switch directement sur la blockchain Bitcoin. Ce portefeuille open-source permet de configurer des conditions de succession on-chain : si le propriétaire n'effectue plus de transactions pendant une période définie, des clés alternatives prédésignées peuvent débloquer les fonds.

## Qu'est-ce que Heritage ?

Heritage est un portefeuille Bitcoin intégrant nativement un mécanisme d'héritage via les scripts Taproot. Développé sous licence MIT par Crypto7, ce logiciel open-source garantit transparence et pérennité.

### Architecture technique

Heritage fonctionne grâce à des scripts Taproot encodés dans les adresses Bitcoin. Chaque UTXO intègre deux types de conditions de dépense :

- **Chemin primaire** : Le propriétaire peut dépenser ses bitcoins à tout moment avec sa clé principale
- **Chemins alternatifs** : Pour chaque héritier désigné, un script combine sa clé publique avec un verrou temporel (timelock)

Chaque transaction du propriétaire repousse automatiquement la date d'activation des clauses d'héritage. En cas d'inactivité prolongée (décès, incapacité), les conditions s'enclenchent automatiquement.

## Modes de fonctionnement

Heritage peut fonctionner selon trois modes de synchronisation avec la blockchain :

- **Service btc-heritage.com** : Mode par défaut, synchronisation automatique via le service en ligne
- **Nœud Bitcoin Core personnel** : Souveraineté maximale avec votre propre nœud
- **Serveur Electrum** : Alternative légère au nœud complet

## Le service Heritage (optionnel)

Heritage propose deux formules :

**Faites-le vous-même (gratuit)** : Le logiciel open-source seul. Vous gérez tout en autonomie avec votre propre nœud. Vous devez créer vos propres alertes (calendrier, rappels) pour ne pas oublier de renouveler vos timelocks.

**Utilisez le service (0,05% par an)** : Le service btc-heritage.com ajoute :
- Rappels automatiques avant l'expiration de vos délais
- Notifications aux héritiers pour les guider dans la récupération
- Support prioritaire

Tarification : 0,05% du montant géré par an, minimum 0,5 mBTC/an. Première année gratuite.

---

# Partie 1 : Heritage CLI

Heritage CLI est le programme en ligne de commande, idéal pour les utilisateurs avancés souhaitant un contrôle granulaire. Il permet une utilisation sur machine air-gapped pour une sécurité maximale.

## Documentation officielle

La documentation complète du CLI est disponible sur [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Cette page couvre toutes les étapes d'utilisation :

![Documentation CLI](assets/fr/010.webp)

1. **Téléchargement** : Instructions pour télécharger le binaire
2. **Connexion au service** : Authentification avec btc-heritage.com
3. **Créer une wallet avec Ledger** : Configuration sécurisée avec hardware wallet
4. **Créer une wallet avec clés locales** : Alternative sans Ledger
5. **Restaurer une wallet** : Récupération depuis une seed existante
6. **Créer une Configuration Heritage** : Définir les héritiers et leurs délais
7. **Enregistrer sur Ledger** : Sauvegarder la configuration sur le device
8. **Sauvegarder/Restaurer l'historique** : Gestion des backups
9. **Recevoir des bitcoins** : Générer des adresses
10. **Dépenser des bitcoins** : Envoyer des transactions
11. **Autres commandes** : Fonctionnalités avancées

Chaque section contient les commandes exactes à exécuter avec leurs explications.

## Aperçu des commandes principales

```bash
# Connexion au service
heritage-cli service login

# Création du wallet (avec Ledger)
heritage-cli wallet create

# Création d'un héritier
heritage-cli heir <nom> create --email <email>

# Configuration des délais (en jours)
heritage-cli wallet heritage-config set --sh backup:360 --sh conjoint:390

# Générer une adresse
heritage-cli wallet new-address

# Envoyer des bitcoins
heritage-cli wallet send-bitcoin -r <adresse>:<montant> --sign --broadcast

# Aide
heritage-cli help
```

Pour le guide complet avec toutes les options, consultez la [documentation CLI officielle](https://btc-heritage.com/heritage-cli).

---

# Partie 2 : Heritage Desktop

Heritage Desktop est l'application graphique offrant une interface intuitive. Elle guide l'utilisateur à travers chaque étape de configuration.

## Installation de l'application

Téléchargez l'application depuis [btc-heritage.com](https://btc-heritage.com) ou [GitHub](https://github.com/crypto7world/heritage-gui/releases).

### Linux (AppImage)

```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```

### Windows et macOS

Exécutez l'installateur téléchargé. Note : les binaires ne sont pas signés, ce qui peut déclencher des avertissements de sécurité.

## Premier lancement

L'assistant d'onboarding propose trois choix :

1. **Créer un nouveau wallet** avec plan d'héritage
2. **Hériter de bitcoins** en tant que bénéficiaire
3. **Explorer manuellement** les fonctionnalités

## Configuration du wallet

![Configuration du wallet](assets/fr/001.webp)

1. **Choix de la synchronisation** : Service Heritage ou votre propre nœud
2. **Clé principale** : Connectez votre Ledger ou générez une clé locale
3. **Création des héritiers** : Ajoutez vos bénéficiaires via l'interface
4. **Configuration des délais** : Définissez les timelocks pour chaque héritier
5. **Sauvegarde** : Notez les phrases mnémotechniques générées

## Interface principale

![Interface principale](assets/fr/002.webp)

L'interface affiche :
- Le solde du wallet
- Le temps restant avant chaque échéance d'héritage
- L'historique des transactions
- Les alertes de renouvellement

## Recevoir des bitcoins

![Recevoir](assets/fr/003.webp)

Cliquez sur "Recevoir" pour générer une nouvelle adresse. Chaque adresse intègre automatiquement vos conditions d'héritage.

## Envoyer des bitcoins

![Envoyer](assets/fr/004.webp)

1. Cliquez sur "Envoyer"
2. Entrez l'adresse de destination et le montant
3. Vérifiez les détails de la transaction
4. Signez avec votre Ledger ou clé locale
5. Diffusez la transaction

Chaque transaction renouvelle automatiquement vos timelocks.

---

# Récupération par un héritier

Lorsque le délai configuré est écoulé, l'héritier peut récupérer les fonds.

## Avec Heritage Desktop

1. Lancez l'application et choisissez "Hériter de bitcoins"
2. Importez la phrase mnémotechnique de 12 mots
3. L'application reconstruit les adresses et détecte les fonds
4. Transférez les bitcoins vers votre wallet personnel

## Avec Heritage CLI

```bash
heritage-cli wallet create --kp local --seed "les 12 mots de la phrase héritier"
heritage-cli wallet sync
heritage-cli wallet send-bitcoin -r <votre_adresse>:<montant> --sign --broadcast
```

Le réseau Bitcoin vérifie automatiquement que le timelock est expiré. Toute tentative prématurée sera rejetée.

---

## Bonnes pratiques

### Sauvegarde des descripteurs

Les descripteurs du wallet sont essentiels pour reconstruire vos adresses Heritage. Selon la documentation officielle, leur sauvegarde est encore plus importante que celle de la seed. Sans les descripteurs, même avec votre phrase mnémotechnique, vous ne pourrez pas retrouver vos fonds.

### Sécurité des clés

Utilisez un Ledger pour la clé principale. Ne stockez jamais les phrases des héritiers au même endroit que la vôtre. Dispersez les informations entre plusieurs supports et localisations.

### Tests préalables

Effectuez un test complet sur testnet ou avec un petit montant. Simulez une récupération par un héritier pour valider l'ensemble du processus.

### Documentation pour vos proches

Rédigez des instructions claires expliquant chaque étape de la récupération. Vos héritiers ne seront peut-être pas familiers avec Bitcoin au moment critique.

## Conclusion

Heritage permet de planifier sa succession Bitcoin de manière souveraine, que ce soit via le CLI pour un contrôle total ou via l'application Desktop pour une expérience guidée. La mise en place requiert une réflexion sur les délais appropriés et la sécurisation des secrets.

## Ressources

- [Site officiel Heritage](https://btc-heritage.com)
- [Documentation](https://btc-heritage.com/docs)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)
