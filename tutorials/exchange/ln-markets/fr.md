---
name: LN Markets
description: Plateforme de trading Bitcoin sur le Lightning Network
---

![cover](assets/cover.webp)

LN Markets est la première plateforme de trading Bitcoin véritablement Lightning-native, permettant de trader des dérivés Bitcoin avec effet de levier directement depuis votre wallet Lightning, sans KYC, avec règlements instantanés et custodie minimale. Lancée en 2020, elle élimine les frictions des exchanges traditionnels : pas de vérification d'identité, pas de dépôts bloqués, pas d'attente de confirmations blockchain. Votre wallet Lightning devient votre compte de trading.

## Qu'est-ce que LN Markets ?

LN Markets propose des **Futures** (contrats perpétuels avec levier jusqu'à 100×) et des **Options** (Call/Put avec risque limité à la prime payée). La plateforme fonctionne comme une couche d'agrégation de liquidité consolidant plusieurs venues de trading pour une exécution optimale zero-slippage. Vos fonds ne sont verrouillés que pendant la durée exacte de vos positions actives, pas des jours ou semaines comme sur un compte custodial traditionnel.

### Produits de trading disponibles

**Futures (Contrats Perpétuels)**

Les contrats perpétuels sont des futures sans date d'expiration permettant de spéculer sur l'évolution du prix Bitcoin avec effet de levier. LN Markets propose deux modes de gestion de la marge :

**Mode Isolated (Marge Isolée)** : Chaque position possède sa propre marge dédiée. Seuls les fonds alloués à cette position spécifique sont à risque. Si la position atteint le prix de liquidation, **seule cette position est liquidée**, vos autres positions et votre solde restant ne sont pas affectés. Idéal pour limiter strictement le risque par trade.

**Mode Cross (Marge Croisée)** : La marge est partagée entre toutes vos positions ouvertes. Votre solde compte total sert de garantie pour toutes vos positions. Si une position va mal, le système puise dans tout votre solde disponible pour éviter la liquidation. **Risque** : si votre solde total s'épuise, toutes vos positions peuvent être liquidées simultanément. Recommandé uniquement pour les traders expérimentés cherchant à maximiser l'efficacité du capital.

**Direction des positions** :

- **Position Long** : vous pariez sur la hausse du BTC/USD. Si le prix monte, vous gagnez ; s'il baisse, vous perdez. **Exemple** : Bitcoin à 100,000 $, vous ouvrez un Long avec 10,000 sats et levier 10×. Si Bitcoin monte à 105,000 $ (+5%), votre position gagne 50% (5% × 10), soit ~5,000 sats de profit. Si Bitcoin chute à 95,000 $ (-5%), vous perdez 50%, soit ~5,000 sats de perte.

- **Position Short** : vous pariez sur la baisse du BTC/USD. Si le prix descend, vous gagnez ; s'il monte, vous perdez. **Exemple** : Bitcoin à 100,000 $, vous ouvrez un Short avec 10,000 sats et levier 10×. Si Bitcoin chute à 95,000 $ (-5%), vous gagnez 50%, soit ~5,000 sats. Si Bitcoin monte à 105,000 $ (+5%), vous perdez 50%.

L'effet de levier (jusqu'à 100×) amplifie gains et pertes proportionnellement. Un mécanisme de **funding rate** (frais périodiques toutes les 8 heures) équilibre les positions long et short. Vous pouvez gérer jusqu'à 100 positions futures simultanément.

**Options**

Une option est comme un **ticket de loterie avec date d'expiration**. Vous payez une prime pour parier sur la direction du prix Bitcoin. **Avantage majeur** : vous ne pouvez jamais perdre plus que la prime payée, aucune liquidation possible.

- **Call Option (pari haussier)** : Vous pariez que Bitcoin va monter au-dessus du strike avant expiration. Vous gagnez si le prix monte, perte limitée à la prime si le prix baisse.

- **Put Option (pari baissier)** : Vous pariez que Bitcoin va descendre sous le strike. Vous gagnez si le prix chute, perte limitée à la prime si le prix monte.

- **Straddle (pari sur volatilité)** : Vous achetez un Call ET un Put simultanément. Vous gagnez si Bitcoin fait un gros mouvement dans n'importe quelle direction, vous perdez les deux primes si le prix reste stable.

Limite : 50 positions simultanées. Idéal pour débuter le trading avec levier sans craindre la liquidation.

**Swap sats ↔ sUSD** : Convertissez instantanément vos satoshis en dollars synthétiques (sUSD) pour vous protéger de la volatilité, ou inversement pour retrouver une exposition Bitcoin.

## Accès à la plateforme et création de compte

### Accéder à LN Markets

Rendez-vous sur [lnmarkets.com](https://lnmarkets.com) et cliquez sur "Open App".

![Page d'accueil LN Markets](assets/fr/01.webp)

### Créer votre compte

L'écran de bienvenue propose plusieurs méthodes de connexion :

![Méthodes de connexion](assets/fr/02.webp)

**Options disponibles** :
1. **Register with a Lightning wallet** (recommandé) : LNURL-auth avec Phoenix, Breez, Zeus ou BlueWallet
2. **Register with email** : compte classique (limite l'expérience Lightning)
3. **Alby** ou **Ledger** : extensions navigateur

### Connexion via Lightning (LNURL-auth)

Cliquez sur "Register with a Lightning wallet". Scannez le QR code avec votre wallet Lightning :

![QR code LNURL-auth](assets/fr/03.webp)

Votre wallet signe automatiquement une requête cryptographique et votre compte est créé instantanément, sans email ni mot de passe. Sécurité forte et anonymat total.

### Configuration initiale

![Configuration post-connexion](assets/fr/04.webp)

**Paramètres disponibles** :
- **Username** : personnalisez votre nom d'utilisateur
- **Automatic withdrawals** : activez les retraits automatiques vers votre wallet après clôture des trades
- **Two-Factor Authentication** : renforcez la sécurité avec 2FA
- **Documentation** : accédez aux ressources officielles

## Tour de l'interface

L'interface LN Markets est organisée en plusieurs sections accessibles depuis le menu latéral : 

### Dashboard

![Dashboard](assets/fr/06.webp)

Affiche vos performances par type de produit (Futures Cross, Futures Isolated, Options) avec P&L, volumes tradés et votre Lightning Address personnelle (ex: `pivi@lnmarkets.com`).

### Profile

![Profil trader](assets/fr/07.webp)

Statistiques détaillées : nombre de trades, type de trader (SCALPER, etc.), durée médiane des positions, répartition Long/Short, win rate, moyennes (quantity, margin, leverage), et structure de frais progressive selon volume.

### Trades

![Historique des trades](assets/fr/08.webp)

L'onglet Trades affiche l'historique complet de vos positions avec toutes les métriques importantes : date de création, direction (Long/Short), taille de la position (quantity), marge engagée, prix d'entrée et de sortie, profit/perte réalisé (P&L) et frais de trading. Vous pouvez filtrer par type de produit (Futures/Options) et exporter vos données pour analyse externe ou comptabilité.

### Settings

![Paramètres de la plateforme](assets/fr/05.webp)

L'onglet Settings propose deux onglets : **Account** et **Interface**.

**Onglet Account** :

Gestion du compte avec champs modifiables :
- **Username** : changez votre nom d'utilisateur (ex: "pivi") avec bouton "Update"
- **Email** : ajoutez/modifiez votre adresse email
- **Adresse bitcoin de dépôt** : l'adresse bitcoin que vous pouvez utiliser pour déposer des fonds on-chain.

**Trois toggles de configuration** :
- **Appear in leaderboards** : choisir d'apparaître ou non dans les tableaux de classements publics
- **Use Taproot addresses** : utiliser les adresses Bitcoin Taproot pour dépôts/retraits on-chain
- **Enable automatic withdrawals** : activer les retraits automatiques vers votre wallet Lightning après clôture de trades

**Migration de compte** : Section permettant de migrer votre compte Lightning vers une authentification classique email/mot de passe.

**Gestion des sessions** : Bouton "Clear session and local data" pour déconnecter et nettoyer les données locales du navigateur.

**Onglet Interface** :

Personnalisation de l'expérience utilisateur avec sept toggles :
- **Skip order confirmation** : désactiver les modales de confirmation avant exécution des trades (trading rapide)
- **Show tooltips** : afficher les infobulles d'aide au survol des éléments
- **Private Mode (masks sensitive data)** : masquer les montants et données sensibles dans l'interface (mode confidentialité)
- **Show net PL in profile** : afficher le profit/perte net dans votre profil public
- **Use unit icons** : afficher des icônes pour les unités monétaires (sats, $)
- **Enable sound notifications** : activer les notifications sonores pour les événements de trading
- **Enable desktop notifications** : activer les notifications bureau du système d'exploitation

### Wallet

![Wallet](assets/fr/09.webp)

Soldes Bitcoin et Synthetic USD avec historique des dépôts, retraits, cross transfers, swaps, funding et gestion des adresses on chain.

### API

![API V3](assets/fr/10.webp)

LN Markets propose une API REST complète (V2 et V3) permettant d'automatiser entièrement votre trading via des scripts ou bots. Vous pouvez créer des clés API avec permissions personnalisables (lecture seule, trading, retraits) directement depuis l'interface. Des SDKs officiels TypeScript et Python sont disponibles pour faciliter l'intégration. La documentation complète de l'API V3 est accessible sur [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).

## Premier dépôt de fonds

Cliquez sur "Deposit". Trois méthodes disponibles :

![Modal de dépôt](assets/fr/11.webp)

1. **LNURL** : scannez le QR code avec votre wallet Lightning
2. **Invoice** : saisissez un montant puis scannez la facture Lightning
3. **On-Chain** : dépôt Bitcoin on chain

## Trading en pratique

### Trade Futures Long : parier sur la hausse

Depuis le Dashboard, cliquez sur "Futures" puis "Isolated". Cliquez sur **"Buy"** pour ouvrir une position Long.

![Interface Futures Long](assets/fr/12.webp)

Cliquez sur l'icône **calculatrice** à côté du bouton "Buy" pour afficher le calculateur de position :

![Calculateur de position Long](assets/fr/13.webp)

**Exemple concret** :
- **Quantity** : 100 $ (taille de la position)
- **Trade Margin** : 12,336 sats (marge engagée)
- **Leverage** : 7.73× (chaque 1% de variation BTC = 7.73% sur votre capital)
- **Entry price** : 104,863.5 $
- **Liquidation** : 92,852 $ (prix critique de liquidation automatique)
- **Exit price** : 110,000 $ (pour calcul de profit)
- **PL** : 4,492 sats (profit si sortie à 110,000 $)

**Scénarios** :
- **Hausse +4.9%** (110,000 $) : +4,492 sats profit (+36.4%)
- **Neutre** (104,863 $) : -185 sats (frais uniquement)
- **Baisse -11.5%** (92,852 $) : liquidation totale (-100%)

Cliquez sur le bouton "Buy" pour confirmer le trade. **Deux cas possibles** :

- **Si vous avez assez de liquidité** sur votre compte : une modal de confirmation s'affiche directement (image ci-dessous). Cliquez sur "Yes" pour exécuter le trade instantanément.

![Confirmation trade Long](assets/fr/14.webp)

- **Si vous n'avez pas assez de liquidité** : un QR code Lightning s'affiche à la place. Scannez-le avec votre wallet Lightning pour payer la marge requise. Le trade s'ouvre automatiquement après réception du paiement

### Trade Futures Short : parier sur la baisse

Cliquez sur **"Sell"** pour ouvrir une position Short (vous gagnez si le prix baisse). Ouvrez le calculateur avec l'icône calculatrice pour configurer votre position :

![Calculateur de position Short](assets/fr/15.webp)

Cliquez sur "Sell" pour confirmer. Comme pour le Long, **deux cas possibles** :

- **Si vous avez assez de liquidité** : modal de confirmation directe, cliquez sur "Yes"
- **Si vous n'avez pas assez de liquidité** : un QR code Lightning s'affiche (image ci-dessous). Scannez-le avec votre wallet Lightning pour payer la marge requise :

![Paiement Lightning pour Short](assets/fr/16.webp)

Une fois le paiement Lightning reçu, votre position Short s'ouvre automatiquement. Vous pouvez ensuite la gérer depuis l'interface de trading.

#### Clôturer une position

Pour clôturer votre position (Long ou Short), cliquez sur la **petite croix en bas à droite** de l'interface de gestion :

![Interface de clôture](assets/fr/17.webp)

Une modal de confirmation s'affiche pour valider la fermeture du trade :

![Confirmation clôture](assets/fr/18.webp)

La modal affiche votre P&L actuel (profit ou perte). Cliquez sur "Yes" pour clôturer. Le solde est instantanément ajouté (profit) ou déduit (perte) de votre Wallet via Lightning.

### Trade Options Call : droit d'achat conditionnel

Les options offrent un **risque limité** à la prime payée, sans liquidation possible. Un Call vous donne le droit (pas l'obligation) d'acheter Bitcoin au strike price avant expiration. Contrairement aux Futures, vous ne pouvez jamais perdre plus que la prime investie.

Depuis le Dashboard, cliquez sur "Options" puis sélectionnez l'onglet "Call".

![Interface Options Call](assets/fr/19.webp)

Configurez votre trade avec les paramètres suivants :
- **Quantity** : 100 $ (taille de votre contrat)
- **Expiry** : 2025-11-15 (date d'expiration)
- **Strike** : 96,000 $ (prix cible)

Les autres champs sont calculés automatiquement :
- **Margin** : 1,045 sats (prime à payer, votre investissement)
- **Breakeven** : 96,923 $ (prix pour récupérer votre mise)
- **Delta** : 40 (sensibilité au prix Bitcoin)

**Comment calculer votre gain ?**

Votre profit dépend du prix Bitcoin à l'expiration. Formule : **(Prix BTC - Strike) × Taille du contrat - Prime payée**.

**Exemples concrets** :

- **Bitcoin à 96,000 $** (prix actuel) : Valeur intrinsèque = 0 $. **Perte : -1,045 sats** (vous perdez la prime)

- **Bitcoin à 97,000 $** : Valeur intrinsèque = (97,000 - 96,000) × 0.00105 BTC = 1.05 $. Converti en sats ≈ 2,175 sats. **Profit : 2,175 - 1,045 = +1,130 sats** (+108% de gain)

- **Bitcoin à 98,000 $** : Valeur intrinsèque = 2,000 $ ≈ 3,224 sats. **Profit : +2,179 sats** (+208% de gain)

- **Bitcoin à 100,000 $** : Valeur intrinsèque = 4,000 $ ≈ 5,263 sats. **Profit : +4,218 sats** (+403% de gain)

- **Bitcoin sous 96,000 $** : Option expire sans valeur. **Perte limitée : -1,045 sats**, aucune liquidation possible

Cliquez sur "Buy Call". Une modal de confirmation s'affiche :

![Confirmation Call option](assets/fr/20.webp)

Cliquez à nouveau sur "Buy Call" pour confirmer. L'option apparaît dans "Running Options". À expiration, LN Markets calcule automatiquement la valeur intrinsèque et règle votre profit/perte.

**Note sur les Put Options** : Le fonctionnement est identique au Call, mais inversé. Avec un Put, vous pariez sur la **baisse** du prix Bitcoin. Si Bitcoin descend sous votre strike, vous gagnez ; s'il reste au-dessus, vous perdez uniquement la prime payée. Le calcul des gains suit la même logique : **(Strike - Prix BTC) × Taille du contrat - Prime payée**.

### Retrait de fonds Lightning

Cliquez sur "Withdraw" :

![Modal de retrait](assets/fr/21.webp)

**Méthodes** : LNURL, Invoice, Lightning Address, On-Chain.

**Procédure Invoice** :
1. Générez une facture Lightning depuis votre wallet
2. Copiez la facture (commence par `lnbc...`)
3. Collez-la dans le champ LN Markets
4. Confirmez le retrait
5. Votre wallet est crédité en 1-3 secondes

Aucun frais de retrait Lightning, seulement minimes coûts de routage (<0.1% en pratique).

## Risques et bonnes pratiques

**Risques principaux** :
- **Liquidation totale** : levier élevé peut anéantir 100% de la marge en minutes
- **Service expérimental** : phase alpha, incertitudes technologiques
- **Risque de contrepartie** : plateforme reste contrepartie unique

**Bonnes pratiques** :

1. **Gestion du capital** : adoptez une stratégie de gestion du risque adaptée à votre profil. Par exemple : allouer 5% de votre patrimoine total au trading avec levier, puis risquer maximum 1% de ce capital par trade (ex: 1 BTC de patrimoine → 5M sats pour trader → 50k sats de risque max par position)

2. **Stop-Loss systématiques** : configurez des stop-loss pour limiter vos pertes par trade. Avec une règle de 1% de risque par exemple, même 10 trades perdants consécutifs ne représentent que 10% de votre capital de trading

3. **Commencez petit** : testez d'abord avec quelques milliers de sats pour comprendre les mécanismes avant d'appliquer votre stratégie de gestion de capital

4. **Retirez régulièrement vos profits** : sécurisez vos gains vers votre wallet principal, ne laissez que le capital de trading actif sur la plateforme

5. **Surveillez l'effet de levier** : évitez les leviers >20× sauf si vous maîtrisez parfaitement les risques de liquidation

**Coûts** : aucun frais de dépôt/retrait Lightning, spread ~0.1% par trade (descendant jusqu'à 0.06% selon volume).

## Avantages et limitations

**Avantages** :
- Non-custodial (contrôle total hors périodes de trading)
- Sans KYC (anonymat via Lightning/Nostr)
- Règlements instantanés (dépôts/retraits en secondes)
- Exécution zero-slippage avec agrégation de liquidité
- API publique et support Nostr

**Limitations** :
- Service alpha (évolutions possibles)
- Liquidités moindres que Binance/Deribit
- Interdit aux résidents US

## Conclusion

LN Markets incarne une évolution majeure du trading Bitcoin en intégrant nativement le Lightning Network pour redonner le contrôle aux utilisateurs. Pour les bitcoiners avertis cherchant à spéculer sans compromettre leur souveraineté, c'est une alternative unique aux exchanges centralisés traditionnels.

La plateforme continue d'évoluer avec futures linéaires USDT et trading non-custodial via Discreet Log Contracts (DLC) en développement. En appliquant les bonnes pratiques de gestion du risque (petites sommes, stop-loss, retraits réguliers), LN Markets devient un outil puissant pour explorer le levier Bitcoin de manière responsable.

Démarrez petit, testez avec quelques milliers de sats, et explorez progressivement cette nouvelle frontière du Lightning Network. Bon trading souverain ⚡️!

## Ressources

- [Site officiel LN Markets](https://lnmarkets.com)
- [Documentation](https://docs.lnmarkets.com)
