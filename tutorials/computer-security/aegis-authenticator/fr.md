---
name: Aegis Authenticator
description: Comment utiliser Aegis Authenticator pour sécuriser ses comptes avec la double authentification ?
---

![cover](assets/cover.webp)

L'authentification à deux facteurs (2FA) est aujourd'hui indispensable pour sécuriser ses comptes en ligne. En plus du mot de passe, elle ajoute un second facteur (souvent un code à 6 chiffres) qui expire après 30 secondes, ce qui complique considérablement la tâche des pirates informatiques. Utiliser une application TOTP (*Time-based One-Time Password*) dédiée est plus sûr que les SMS, qui peuvent être détournés par des attaques de SIM swapping.

Cependant, toutes les applications d'authentification ne se valent pas. De nombreuses solutions propriétaires (Google Authenticator, Authy, etc.) posent problème : elles sont propriétaires et à code source fermé (impossible d'auditer leur sécurité), intègrent parfois des trackers publicitaires, n'offrent pas de sauvegarde chiffrée de vos codes, et peuvent même empêcher l'export de vos comptes pour vous enfermer dans leur écosystème.

Aegis Authenticator, au contraire, se présente comme une alternative libre et éthique à ces applications. Aegis est une application gratuite, sécurisée et open source qui permet de gérer vos jetons de vérification en deux étapes sur Android. Son développement met l'accent sur des fonctionnalités essentielles que d'autres apps n'offrent pas, notamment un chiffrement robuste des données locales et la possibilité de sauvegardes sécurisées. En somme, Aegis offre une solution de double authentification locale et auditable, idéale pour qui souhaite garder un contrôle total sur ses codes 2FA.

## Présentation d'Aegis Authenticator

Aegis Authenticator est une application 2FA open source pour Android, publiée sous licence GPL v3. Elle se distingue par sa philosophie "privacy by design" : l'application fonctionne entièrement hors-ligne et ne requiert aucune connexion à un service distant. Ainsi, vos tokens restent stockés localement sur votre appareil, dans un coffre sécurisé dont vous seul détenez la clé.

### Fonctionnalités clés

**Coffre-fort chiffré :** tous vos codes OTP sont stockés dans un vault chiffré en AES-256 (mode GCM) et protégé par un mot de passe maître défini par l'utilisateur. Vous pouvez déverrouiller ce coffre via le mot de passe ou via des données biométriques (empreinte digitale, reconnaissance faciale) pour plus de commodité. En l'absence de mot de passe, les données seraient en clair – il est donc fortement recommandé d'en définir un.

**Organisation avancée :** Aegis permet de garder vos nombreux comptes 2FA bien organisés. Vous pouvez trier vos entrées alphabétiquement ou dans l'ordre de votre choix, les regrouper par catégories (par exemple : Perso, Travail, Social) pour vous y retrouver facilement, et attribuer à chaque entrée une icône personnalisée. Une barre de recherche est incluse pour retrouver instantanément un service ou un compte par son nom.

**Sauvegardes locales chiffrées :** pour ne jamais perdre accès à vos comptes, Aegis propose des sauvegardes automatiques de votre coffre. Celles-ci sont chiffrées (via un mot de passe) et peuvent être enregistrées à l'endroit de votre choix (stockage interne, dossier cloud, etc.). L'application peut également exporter votre base de données de comptes manuellement, au format chiffré ou en clair selon vos besoins. Importer des comptes depuis d'autres applications 2FA est tout aussi facile (Aegis prend en charge l'import depuis Authy, Google Authenticator, FreeOTP, andOTP, etc.).

**Sécurité et vie privée :** l'application est entièrement hors-ligne par défaut. Elle ne requiert aucune permission réseau – ce qui signifie qu'elle n'émet aucune donnée vers l'extérieur et ne comporte aucun traqueur publicitaire ou module d'analyse comportementale. Aegis n'affiche pas de publicité et n'exige pas de compte utilisateur : dès son installation, elle est fonctionnelle sans inscription. Son code source étant public sur GitHub, la communauté peut l'auditer librement, garantissant l'absence de fonctionnalités malveillantes ou cachées.

**Interface moderne :** Aegis adopte un design Material Design soigné, avec support du thème sombre (dont un mode AMOLED) et même une vue en tuiles optionnelle pour afficher vos codes sous forme de grilles. L'interface est épurée, sans fioritures, et empêche la capture d'écran des codes par mesure de sécurité.

## Installation

Aegis Authenticator étant open source, ses développeurs privilégient des canaux de distribution respectueux de la vie privée. Il existe deux manières principales de l'installer :

### Via F-Droid (recommandé)

Le moyen le plus sûr et simple est de passer par F-Droid, le store alternatif libre. Si F-Droid n'est pas encore installé sur votre téléphone, commencez par le télécharger depuis le site officiel [F-Droid.org](https://f-droid.org). Ensuite :

- Ouvrez F-Droid et assurez-vous d'avoir bien actualisé les dépôts pour obtenir la liste à jour des applications
- Recherchez « Aegis Authenticator » dans F-Droid. L'application officielle devrait apparaître (éditeur : Beem Development)
- Lancez l'installation en appuyant sur Installer. Aegis faisant partie des applications vérifiées par F-Droid, vous bénéficiez d'un téléchargement fiable et sécurisé

L'installation via F-Droid présente l'avantage de recevoir des mises à jour automatiques de l'application dès qu'elles sont publiées. De plus, F-Droid garantit que l'application est exempte de tout composant propriétaire indésirable.

### Via GitHub (APK signé)

Si vous préférez installer l'application sans passer par un store, vous pouvez télécharger directement l'APK officiel depuis la page GitHub du projet. Sur le dépôt Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), rendez-vous dans la section Releases où les versions stables sont publiées. 

- Téléchargez la dernière version APK disponible
- Avant d'installer l'APK, assurez-vous d'avoir autorisé l'installation d'applications de sources inconnues sur votre appareil (dans les Paramètres Android)
- L'APK fourni sur GitHub est signé par le développeur avec la même clé que sur F-Droid

Après l'installation manuelle, l'application fonctionnera identiquement. Notez simplement que les mises à jour ne seront pas automatiques : il faudra penser à vérifier périodiquement les nouvelles versions sur GitHub.

### Google Play Store vs F-Droid

Aegis Authenticator est disponible à la fois sur le Google Play Store et sur F-Droid, vous offrant le choix de la méthode d'installation :

**Google Play Store :**
- ✅ Mise à jour automatique intégrée au système Android
- ✅ Installation simple et familière
- ✅ Même APK signé que sur les autres canaux

**F-Droid (recommandé) :**
- ✅ Store libre et open source
- ✅ Construction reproductible et vérifiable
- ✅ Aucun service Google requis
- ✅ Respect de la philosophie du logiciel libre

Le choix entre ces deux options dépend de vos préférences concernant l'écosystème Google. Si vous privilégiez la simplicité, le Play Store convient parfaitement. Si vous souhaitez une approche plus respectueuse de la vie privée et indépendante des services Google, F-Droid est le meilleur choix.

## Première configuration

Lors du premier lancement d'Aegis, une procédure de configuration initiale vous est proposée afin de sécuriser votre coffre-fort de codes 2FA :

![Configuration initiale Aegis](assets/fr/01.webp)

*Processus de configuration initial d'Aegis : écran d'accueil, choix de sécurité, définition du mot de passe maître et finalisation*

### Définir un mot de passe maître

Aegis va d'abord vous demander de choisir un mot de passe principal. Ce mot de passe servira à chiffrer l'ensemble de vos jetons d'authentification stockés dans le coffre. Il est fortement recommandé de définir un mot de passe robuste et unique, que vous seul connaîtrez. 

**⚠️ Attention :** n'oubliez surtout pas ce mot de passe – si vous le perdez, vos codes 2FA chiffrés deviendront inaccessibles (il n'existe pas de backdoor). Aegis vous demandera de saisir deux fois le mot de passe pour confirmation.

### Activer le déverrouillage biométrique (optionnel)

Si votre appareil Android dispose d'un lecteur d'empreintes ou d'un autre capteur biométrique, Aegis vous proposera d'activer le déverrouillage par biométrie. Cette option est facultative mais très pratique : elle permet de déverrouiller l'application rapidement avec votre empreinte digitale ou votre visage, plutôt que de taper le mot de passe à chaque fois.

Notez que la biométrie est un confort supplémentaire : votre mot de passe maître reste requis en cas de changement de biométrie ou si l'appareil redémarre.

### Découvrir les paramètres de l'application

Une fois dans l'application (interface principale vide au départ), familiarisez-vous avec les options de configuration disponibles. Accédez aux paramètres via le menu déroulant en haut à droite de l'écran (trois points verticaux), puis sélectionnez "Settings".

![Interface principale et paramètres](assets/fr/02.webp)

*Interface principale d'Aegis vide au départ, accès au menu des paramètres et vue d'ensemble des options disponibles*

Le menu des paramètres d'Aegis regroupe plusieurs sections importantes :

- **Appearance** : Personnalisation du thème (clair, sombre, AMOLED), de la langue et autres réglages visuels
- **Behavior** : Configuration du comportement de l'application lors des interactions avec la liste des entrées
- **Icon packs** : Gestion et import de packs d'icônes pour personnaliser l'apparence de vos comptes
- **Security** : Réglages de chiffrement, déverrouillage biométrique, verrouillage automatique et autres paramètres de sécurité
- **Backups** : Configuration des sauvegardes automatiques vers un emplacement de votre choix
- **Import & Export** : Import de sauvegardes depuis d'autres applications d'authentification et export manuel de votre coffre Aegis
- **Audit log** : Journal détaillé de tous les événements importants survenus dans l'application

Cette organisation claire vous permet de configurer Aegis selon vos préférences et besoins de sécurité.

## Ajouter un compte 2FA

Avec Aegis configuré, passons à l'essentiel : l'ajout de vos comptes à deux facteurs. Le processus est simple et Aegis offre plusieurs méthodes pour intégrer vos codes d'authentification.

### Les trois méthodes d'ajout disponibles

Depuis l'interface principale d'Aegis, appuyez sur le bouton **+** en bas à droite pour accéder aux options d'ajout. Trois méthodes s'offrent à vous :

- **Scan QR code** : Scanner directement le QR code affiché par le service web
- **Scan image** : Scanner un QR code à partir d'une image sauvegardée sur votre appareil
- **Enter manually** : Saisir manuellement les informations du compte 2FA

### Exemple pratique : configurer Bitwarden

Prenons l'exemple concret de l'activation de la 2FA sur Bitwarden pour illustrer le processus :

![Exemple avec Bitwarden](assets/fr/04.webp)

*Exemple d'activation de la 2FA sur Bitwarden : interface web avec options d'authentification et recommandation d'Aegis*

- **Connexion et accès aux paramètres** : Connectez-vous sur votre espace Bitwarden et accédez aux paramètres, onglet "Security"
- **Section fournisseurs** : Dirigez-vous dans la section "Providers" et cliquez sur "Manage" dans la partie "Authenticator app"

![Configuration 2FA avec QR code](assets/fr/05.webp)

*Processus complet d'ajout d'un compte : QR code affiché par le service, clé secrète visible et saisie du code de vérification*

- **Scan du QR code** : Une popup s'ouvre avec le QR code et la clé secrète
- **Dans Aegis** : Utilisez "Scan QR code" pour capturer automatiquement les informations
- **Vérification** : Entrez le code à 6 chiffres généré par Aegis dans le champ "Verification code"
- **Activation** : Cliquez sur "Turn on" pour finaliser l'activation

### Ajout manuel des détails

Si vous préférez ou ne pouvez pas scanner le QR code, utilisez l'option "Enter manually". Le formulaire vous permet de renseigner :

![Ajout d'un compte 2FA](assets/fr/03.webp)

*Processus d'ajout d'un nouveau compte 2FA : interface vide, options d'ajout, formulaire de saisie manuel et compte ajouté avec succès*

- **Name** : Le nom du service (ex: Bitwarden, GitHub...)
- **Issuer** : L'émetteur (souvent identique au nom)
- **Group** : Optionnel, pour organiser vos comptes par catégories
- **Note** : Remarques personnelles sur ce compte
- **Secret** : La clé secrète fournie par le service (masquée par défaut)
- **Advanced** : Paramètres avancés (algorithme, période, nombre de chiffres)

Une fois le compte ajouté, il apparaît dans votre liste avec son code actuel et un indicateur temporel montrant le temps restant avant renouvellement.

### Compatibilité universelle

Aegis est compatible avec tous les services utilisant les standards TOTP et HOTP, ce qui inclut la quasi-totalité des sites proposant la 2FA : réseaux sociaux, banques, gestionnaires de mots de passe, plateformes crypto, etc.

### Organisation des entrées

Après avoir ajouté plusieurs comptes, vous apprécierez les outils d'organisation d'Aegis :

- **Tri personnalisé :** Par défaut, les comptes sont listés par ordre alphabétique, mais vous pouvez modifier l'ordre manuellement
- **Groupes et catégories :** Créez des groupes pour séparer vos comptes personnels de vos comptes professionnels, ou regrouper par type de service (banque, mail, réseaux sociaux…)
- **Icônes personnalisées :** Aegis tente d'assigner automatiquement une icône appropriée si disponible, sinon vous pouvez choisir parmi de nombreuses icônes génériques ou importer une image
- **Recherche rapide :** La barre de recherche en haut vous permet de taper quelques lettres pour filtrer instantanément les entrées correspondantes

En touchant une entrée, le code OTP s'affiche en grand (s'il était masqué) et vous pouvez le copier dans le presse-papiers en un appui long – pratique pour le coller dans l'application que vous voulez connecter.

## Sécurité et sauvegardes

La sécurité étant le cœur d'Aegis, il convient de comprendre comment sont protégés vos codes 2FA et comment assurer leur persistance en cas de problème.

### Architecture de sécurité

**Chiffrement robuste** : Tous vos codes sont stockés dans un coffre chiffré utilisant l'algorithme **AES-256 en mode GCM**, combiné à votre mot de passe maître. La dérivation de clé s'appuie sur **scrypt**, offrant une protection renforcée contre les attaques par force brute.

**Déverrouillage sécurisé** : Le mot de passe maître est requis pour déchiffrer vos données. La biométrie (optionnelle) utilise le **Keystore sécurisé d'Android** et le TEE (Trusted Execution Environment) pour protéger la clé de chiffrement.

**Permissions minimales** : Aegis fonctionne hors-ligne par défaut et ne requiert que l'accès à la caméra (scan QR), à la biométrie et au vibreur. Aucune donnée n'est collectée ni partagée.

### Options de sauvegarde

Aegis propose plusieurs stratégies de sauvegarde adaptées à différents besoins de sécurité et de commodité :

![Configuration des sauvegardes](assets/fr/06.webp)

*Interface complète avec compte ajouté, alerte de sauvegarde, paramètres de sauvegarde automatique et stratégies de backup*

**1. Sauvegardes locales automatiques**
- Configuration d'un dossier de destination au choix
- Fréquence personnalisable (après chaque modification, quotidienne, etc.)
- Fichiers chiffrés (.aesvault) protégés par mot de passe
- Compatible avec dossiers synchronisés (Nextcloud, Dropbox, etc.)

![Sélection du dossier de sauvegarde](assets/fr/07.webp)

*Processus de sélection du dossier de sauvegarde : explorateur de fichiers, dossier de destination et autorisation d'accès*

**2. Sauvegardes cloud Android**
- Intégration optionnelle avec le système de sauvegarde d'Android
- Disponible uniquement pour les coffres chiffrés (sécurité préservée)
- Sauvegarde transparente avec les autres données Android
- Restauration automatique lors de changement d'appareil

**3. Exports manuels**
- Export à la demande via **Paramètres > Import & Export**
- Choix entre format chiffré (recommandé) ou clair
- Utile pour migrations ou sauvegardes ponctuelles

### Bonnes pratiques de sécurité

- **Conservez plusieurs versions** de sauvegarde pour éviter les corruptions
- **Testez régulièrement** vos sauvegardes en tentant une restauration
- **Stockez séparément** vos codes de récupération fournis par les services
- **Votre mot de passe maître** reste nécessaire même avec les sauvegardes cloud
- **Sécurisez votre mot de passe maître** : utilisez un mot de passe unique et robuste, stocké dans un gestionnaire de mots de passe
- **Gardez l'application à jour** pour bénéficier des derniers correctifs de sécurité
- **Activez le verrouillage automatique** dans les paramètres pour sécuriser l'accès à l'application
- **Désactivez les captures d'écran** (option par défaut) pour empêcher l'interception de vos codes
- **Utilisez la biométrie avec parcimonie** : préférez le mot de passe pour les accès critiques

## Comparaison avec d'autres applications

Comment Aegis se positionne-t-il face aux autres applications d'authentification populaires ?

### Aegis vs Google Authenticator

**Aegis :**
- ✅ Open source et auditable
- ✅ Sauvegarde chiffrée locale
- ✅ Organisation avancée (groupes, icônes, recherche)
- ✅ Aucune collecte de données
- ❌ Android uniquement

**Google Authenticator :**
- ✅ Disponible sur Android et iOS
- ✅ Synchronisation cloud (depuis 2023)
- ❌ Code source fermé
- ❌ Fonctionnalités limitées
- ❌ Potentielle collecte de données Google

### Aegis vs Authy

**Aegis :**
- ✅ Open source
- ✅ Pas de compte requis
- ✅ Export des codes possible
- ✅ Contrôle total des données
- ❌ Pas de sync multi-appareils natif

**Authy :**
- ✅ Synchronisation multi-appareils
- ✅ Disponible sur Android et iOS
- ❌ Code source fermé
- ❌ Requiert un numéro de téléphone
- ❌ Impossible d'exporter les codes
- ❌ Applications desktop supprimées en mars 2024

Aegis excelle pour les utilisateurs d'Android qui valorisent la transparence, la sécurité locale et le contrôle complet de leurs données. Les alternatives comme Authy conviennent mieux si vous avez absolument besoin de synchronisation automatique multi-appareils.


## Conclusion

Aegis Authenticator représente une excellente solution pour ceux qui recherchent une application 2FA respectueuse de la vie privée, sécurisée et transparente. Son approche open source, combinée à un chiffrement robuste et à une interface soignée, en fait un choix de premier ordre pour sécuriser vos comptes en ligne.

Bien qu'elle soit limitée à Android et ne propose pas de synchronisation cloud native, Aegis compense largement ces limitations par sa philosophie "privacy by design" et son contrôle total des données. Pour les utilisateurs soucieux de leur vie privée numérique, Aegis offre une alternative crédible et puissante aux solutions propriétaires dominantes du marché.

La sécurité de vos comptes en ligne ne doit pas dépendre de la bonne volonté d'entreprises commerciales. Avec Aegis, vous gardez la main sur vos codes d'authentification, dans un coffre-fort numérique dont vous seul détenez la clé.

## Ressources

### Sites officiels
- **Site officiel** : [getaegis.app](https://getaegis.app/) - Présentation de l'application et téléchargement
- **Code source** : [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Dépôt GitHub officiel
- **F-Droid** : [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installation via le store libre

### Documentation technique
- **Documentation du coffre-fort** : [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Description technique du chiffrement et de l'architecture sécurisée
- **FAQ officielle** : [getaegis.app/#faq](https://getaegis.app/#faq) - Réponses aux questions fréquentes
- **Wiki du projet** : [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Documentation utilisateur complète
