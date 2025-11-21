---
name: Ente Auth
description: Un authentificateur 2FA open source et chiffré de bout en bout
---
![cover](assets/cover.webp)

L'authentification à deux facteurs (2FA) est devenue indispensable pour sécuriser nos comptes en ligne. En plus de votre mot de passe habituel, elle exige un code temporaire généralement généré par une application dédiée. Ce mécanisme, appelé TOTP (Time-Based One-Time Password), garantit que même si votre mot de passe est compromis, un attaquant ne pourra pas accéder à votre compte sans posséder ce second facteur renouvelé toutes les 30 secondes.

Cependant, choisir la bonne application d'authentification n'est pas anodin. Google Authenticator, bien que populaire, présente des limitations importantes : code propriétaire impossible à auditer, synchronisation sans chiffrement de bout en bout, et risque de perte totale des codes en cas de problème avec votre téléphone. D'autres solutions comme Authy exigent un numéro de téléphone et ne garantissent pas une confidentialité totale.

**Ente Auth** se distingue comme une alternative moderne et sécurisée. Cette application gratuite, open source et multiplateforme, développée par l'équipe derrière [Ente Photos](https://ente.io), propose des sauvegardes cloud chiffrées de bout en bout et une synchronisation transparente entre tous vos appareils. Contrairement aux solutions propriétaires, Ente Auth vous permet de garder le contrôle total sur vos codes d'authentification sans compromettre votre vie privée.

Dans ce tutoriel, nous découvrirons comment installer et utiliser Ente Auth pas à pas, et pourquoi cette solution se distingue des authentificateurs traditionnels.

## Présentation d'Ente Auth

Ente Auth a été développé par l'équipe derrière Ente Photos, un service de stockage de photos chiffré de bout en bout et respectueux de la vie privée. Fidèle à la philosophie d'Ente ("Ente" signifie "le mien" en malayalam, symbolisant la maîtrise de vos données), Ente Auth a été conçu pour redonner aux utilisateurs le contrôle total sur leurs codes d'authentification à deux facteurs.

### Fonctionnalités principales

**Codes TOTP standards** : Ente Auth génère des codes temporaires compatibles avec la majorité des services (GitHub, Google, Binance, ProtonMail, etc.). Vous pouvez ajouter autant de comptes 2FA que nécessaire et l'application se charge de calculer les codes à partir des secrets fournis.

**Sauvegarde cloud chiffrée de bout en bout** : Vos codes sont sauvegardés en ligne de manière sécurisée. Vous seul pouvez les déchiffrer – la clé de chiffrement est dérivée de votre mot de passe et n'est connue que de vous. Ente (le serveur) n'a aucune connaissance de vos secrets ni même des intitulés de vos comptes, car tout est chiffré côté client selon une architecture zero-knowledge.

**Synchronisation multi-appareils** : Vous pouvez installer Ente Auth sur plusieurs appareils (smartphone, tablette, ordinateurs) et accéder à vos codes sur chacun d'eux. Toute modification est propagée automatiquement et instantanément sur vos autres appareils via le cloud chiffré, vous apportant une grande flexibilité au quotidien.

**Interface minimaliste et intuitive** : L'application propose une interface épurée, facile à prendre en main même pour des utilisateurs non techniciens. Les comptes 2FA sont affichés avec le nom du service, votre identifiant et le code à 6 chiffres mis à jour en temps réel. Ente Auth affiche également le code suivant quelques secondes à l'avance pour éviter d'être pris de court par l'expiration.

**Open source et auditée** : Le code source d'Ente Auth est [public sur GitHub](https://github.com/ente-io/auth) sous licence AGPL v3.0. N'importe quel développeur peut l'auditer pour vérifier l'absence de failles ou de comportements indésirables. La cryptographie implémentée a fait l'objet d'un [audit externe indépendant](https://ente.io/blog/cryptography-audit/), gage de sérieux dans la sécurité de l'application.

### Avantages et limites

**Avantages :**
- Protection de la vie privée par design avec chiffrement de bout en bout
- Synchronisation sécurisée entre tous vos appareils
- Code open source auditable
- Interface utilisateur claire et intuitive
- Sauvegarde automatique pour éviter la perte des codes
- Disponible sur toutes les plateformes (mobile et desktop)

**Limites :**
- Nécessite une connexion internet pour la synchronisation
- Les utilisateurs avancés peuvent préférer des solutions 100% hors-ligne comme Aegis (Android uniquement)
- Relativement récent comparé à des solutions établies

## Installation

Ente Auth est disponible sur la plupart des plateformes courantes. Vous pouvez télécharger l'application depuis [le site officiel](https://ente.io/auth) ou depuis les stores officiels.

![Installation d'Ente Auth](assets/fr/01.webp)

*Page de téléchargement d'Ente Auth avec toutes les plateformes disponibles*

### Android
Plusieurs options s'offrent à vous :
- **Google Play Store** : Recherchez "Ente Auth" pour une installation classique
- **F-Droid** : Disponible sur le catalogue d'applications open source Android, avec une garantie de construction vérifiée sans contenu propriétaire
- **Installation manuelle** : Les fichiers APK sont téléchargeables depuis la [page GitHub du projet](https://github.com/ente-io/auth/releases) avec notification intégrée pour les nouvelles versions

### iOS (iPhone/iPad)
Installez Ente Auth directement depuis l'App Store d'Apple en recherchant le nom de l'application. L'app iOS peut également fonctionner sur les Mac équipés de puces Apple Silicon (M1/M2) via le Mac App Store.

### Ordinateurs (Windows, macOS, Linux)
Ente Auth propose des applications de bureau natives. Rendez-vous sur [ente.io/download](https://ente.io/download) ou sur la section [Releases du GitHub](https://github.com/ente-io/auth/releases) :

- **Windows** : Un installeur EXE est fourni
- **macOS** : Une image disque DMG à glisser-déposer dans Applications
- **Linux** : Plusieurs formats disponibles (AppImage portable, .deb pour Debian/Ubuntu, .rpm pour Fedora/Red Hat)

**Note :** Ce tutoriel est basé sur Ente Auth v4.4.4 et versions ultérieures. Les versions antérieures peuvent présenter des différences d'interface mineures.

### Interface Web
Sans installation, vous pouvez accéder à vos codes via [auth.ente.io](https://auth.ente.io) depuis un navigateur. L'interface web est limitée à la consultation des codes (utile pour le dépannage), car l'ajout de comptes nécessite l'application mobile ou desktop pour des raisons de sécurité.

## Première configuration

### Création du compte

Au premier lancement d'Ente Auth, vous avez deux options :

![Premier lancement d'Ente Auth](assets/fr/02.webp)

*Écran d'accueil d'Ente Auth avec les options de création de compte*

**Avec compte (recommandé)** : Choisissez "Create Account" et saisissez votre adresse e-mail et un mot de passe. **Important** : ce mot de passe sert de master password pour chiffrer vos données. Choisissez-le robuste et unique car il n'existe pas de procédure de réinitialisation classique sans perte de données. Si vous l'égarez, vos données chiffrées seront irrécupérables.

**Mode hors-ligne** : Sélectionnez "Use without backups" pour utiliser l'application localement sans cloud. Dans ce mode, vos codes restent sur l'appareil mais vous devrez les exporter manuellement pour éviter leur perte.

![Vérification email et récupération de clé](assets/fr/03.webp)

*Processus de vérification email et génération de la clé de récupération de 24 mots*

Une vérification par e-mail peut être demandée pour valider la création du compte et permettre la restauration sur un nouvel appareil. Ente Auth vous fournira également une clé de récupération de 24 mots (basée sur la méthode BIP39). **Sauvegardez impérativement cette clé** dans un endroit sûr : c'est votre seul moyen de récupérer vos données si vous oubliez votre mot de passe.

### Sécurité locale

Je recommande fortement d'activer la protection locale par code ou biométrie. Rendez-vous dans **Settings → Security → Lockscreen** et configurez :

- **Déverrouillage biométrique** : Face ID, empreinte digitale selon les capacités de votre appareil
- **Code PIN/mot de passe** spécifique à l'application
- **Délai d'Auto-Lock** : par exemple "Immédiatement" ou après 30 secondes d'inactivité

Cette protection empêche un accès non autorisé à vos codes si quelqu'un accède à votre téléphone déverrouillé. Notez que ce verrouillage est une barrière supplémentaire : vos données restent chiffrées de bout en bout même sans cette protection.

## Ajouter des comptes 2FA

### Procédure standard

Pour ajouter un nouveau compte 2FA, nous allons prendre l'exemple concret d'activation de la 2FA sur Bull Bitcoin :

![Configuration du premier compte](assets/fr/04.webp)

*Interface principale d'Ente Auth prête pour ajouter le premier compte 2FA*

**Côté service (Bull Bitcoin)** : Connectez-vous à votre compte Bull Bitcoin, allez dans les paramètres de sécurité, et activez l'authentification à deux facteurs.

![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)

*Menu des paramètres de sécurité dans l'interface Bull Bitcoin*

![Activation 2FA Bull Bitcoin](assets/fr/06.webp)

*Option d'activation de l'authentification à deux facteurs sur Bull Bitcoin*

Le service affichera alors un QR code à scanner avec votre application d'authentification :

![QR code 2FA Bull Bitcoin](assets/fr/07.webp)

*QR code généré par Bull Bitcoin à scanner avec votre authentificateur*

**Dans Ente Auth** : Cliquez sur "Enter a setup key" puis scannez le QR code affiché par Bull Bitcoin. Ente Auth reconnaîtra automatiquement le compte et remplira les champs.

![Ajout du compte dans Ente Auth](assets/fr/08.webp)

*Configuration des détails du compte Bull Bitcoin dans Ente Auth*

Vous pouvez personnaliser le nom du service et votre identifiant pour un meilleur repérage. Les paramètres avancés (algorithme SHA1, période 30s, 6 chiffres) sont généralement corrects par défaut.

**Validation côté service** : Retournez sur Bull Bitcoin et saisissez le code à 6 chiffres généré par Ente Auth pour finaliser l'activation.

![Saisie du code 2FA](assets/fr/09.webp)

*Saisie du code généré par Ente Auth pour valider l'activation 2FA*

![2FA activée](assets/fr/10.webp)

*Confirmation de l'activation réussie de la 2FA sur Bull Bitcoin*

**Codes de sauvegarde** : Bull Bitcoin vous proposera des codes de récupération. **Sauvegardez-les impérativement** dans un endroit sûr, séparé de votre authentificateur.

![Gestion des codes de sauvegarde](assets/fr/11.webp)

*Option pour générer des codes de sauvegarde d'urgence sur Bull Bitcoin*

![Codes de récupération](assets/fr/12.webp)

*Liste des codes de récupération à conserver en lieu sûr*

### Organisation et gestion

Ente Auth propose plusieurs fonctionnalités pratiques :

**Copie rapide** : Appuyez sur le code pour le copier automatiquement dans le presse-papiers.

**Actions contextuelles** : Un appui long (ou clic droit sur desktop) permet d'éditer, supprimer, partager ou épingler une entrée.

**Tags et recherche** : Organisez vos comptes avec des étiquettes (personnel/professionnel, par catégorie de service) et utilisez la barre de recherche pour filtrer rapidement.

![Création d'un tag](assets/fr/17.webp)

*Processus de création d'un tag : menu contextuel et dialogue de création*

![Tag appliqué](assets/fr/18.webp)

*Tag "bitcoin" appliqué avec succès sur le compte Bull Bitcoin*

**Icônes automatiques** : Chaque entrée peut être illustrée par le logo du service grâce à l'intégration du pack d'icônes [Simple Icons](https://simpleicons.org/).

**Partage sécurisé temporaire** : Fonctionnalité unique d'Ente Auth, le partage sécurisé permet de transmettre un code 2FA à un collègue sans révéler le secret sous-jacent. Générez un lien chiffré valable 2, 5 ou 10 minutes maximum - le destinataire voit le code en temps réel mais ne peut ni l'exporter ni accéder aux données du compte. Cette méthode est idéale pour l'assistance technique ou la collaboration temporaire, offrant un niveau de sécurité impossible avec une simple capture d'écran ou message texte.

![Partage sécurisé](assets/fr/19.webp)

*Interface de partage sécurisé temporaire : choix de la durée (5 min)*

**Export/Import sécurisé** : Ente Auth permet d'exporter vos codes vers d'autres applications ou d'importer depuis Google Authenticator et d'autres solutions. L'export se fait via un fichier chiffré ou un QR code, garantissant la portabilité de vos données sans compromettre leur sécurité.

**Clé de récupération BIP39** : L'application génère automatiquement une phrase de récupération de 24 mots selon le standard BIP39 (Bitcoin Improvement Proposal), identique aux portefeuilles de cryptomonnaies. Cette phrase constitue votre clé de récupération ultime, permettant de restaurer tous vos codes même en cas d'oubli du mot de passe principal.

## Configuration et paramètres

Ente Auth offre de nombreuses options de personnalisation accessibles via les paramètres de l'application :

![Paramètres principaux d'Ente Auth](assets/fr/13.webp)

*Vue d'ensemble des paramètres disponibles dans Ente Auth*

### Gestion du compte et des données

![Paramètres de sécurité](assets/fr/14.webp)

*Options de sécurité avancées : vérification email, code PIN, sessions actives*

Les paramètres de sécurité permettent de :
- Activer la vérification par e-mail pour les nouvelles connexions
- Activer Passkey
- Consulter les sessions actives sur vos différents appareils
- Configurer un code PIN ou la biométrie

### Options d'interface et d'usage

![Paramètres généraux](assets/fr/15.webp)

*Paramètres d'interface et de personnalisation de l'application*

Les paramètres généraux incluent :
- **Langue** : Interface multilingue
- **Affichage** : Icônes larges, mode compact
- **Confidentialité** : Masquer les codes, recherche rapide
- **Télémétrie** : Reporting d'erreurs (désactivable)

## Sauvegarde et synchronisation

### Fonctionnement du chiffrement

Lorsque vous ajoutez un compte avec un compte Ente connecté, l'application chiffre immédiatement cette donnée sensible localement en utilisant votre master key (dérivée de votre mot de passe). Les données chiffrées sont ensuite envoyées vers le serveur d'Ente pour stockage.

Grâce à ce mécanisme, une sauvegarde cloud chiffrée de bout en bout de vos codes est toujours disponible. Si vous perdez votre appareil, réinstallez Ente Auth et reconnectez-vous : l'application téléchargera et déchiffrera automatiquement tous vos codes.

### Synchronisation multi-appareils

Si vous utilisez Ente Auth sur smartphone et ordinateur, tout ajout ou modification sur un appareil apparaît en quelques secondes sur l'autre. Cette synchronisation passe par le cloud d'Ente, mais comme les données sont chiffrées de bout en bout, le serveur ne voit que du contenu crypté illisible.

![Synchronisation mobile](assets/fr/16.webp)

*Démonstration de la synchronisation : même compte Bull Bitcoin accessible sur mobile et desktop*

La synchronisation est transparente : installez Ente Auth sur votre smartphone, connectez-vous avec vos identifiants, et tous vos codes 2FA (ici Bull Bitcoin) apparaissent automatiquement. L'exemple ci-dessus montre la synchronisation parfaite entre desktop et mobile - le même code Bull Bitcoin est accessible sur les deux appareils.

Du point de vue confidentialité, ni Ente ni aucun tiers n'a accès à vos secrets 2FA. Même les métadonnées (tags, notes, noms de services) sont chiffrées avant envoi. Cette architecture zero-knowledge assure que vous êtes le seul à pouvoir déchiffrer vos codes.

### Utilisation hors-ligne

La synchronisation nécessite Internet, mais Ente Auth fonctionne parfaitement hors-ligne sur chaque appareil puisque toutes les données sont stockées localement. Les modifications hors-ligne sont mises en file d'attente et synchronisées dès le retour de connexion.

## Sécurité et vie privée

### Garanties cryptographiques

Ente Auth s'appuie sur un chiffrement de bout en bout robuste avec architecture zero-knowledge. Vos codes sont chiffrés avec une clé que vous seul détenez, dérivée de votre mot de passe maître à l'aide de fonctions de dérivation avancées (key derivation functions). 

**Architecture zero-knowledge** : Ente ne peut matériellement pas accéder à vos données. Même les métadonnées (noms des services, tags, notes) sont chiffrées côté client avant transmission. Cette approche garantit qu'en cas d'attaque sur les serveurs ou de demande gouvernementale, Ente ne pourrait divulguer que des données cryptées illisibles sans votre mot de passe.

**Chiffrement en local** : Le processus de chiffrement s'effectue entièrement sur votre appareil avant l'envoi vers le cloud. Les serveurs d'Ente ne reçoivent et ne stockent que des données préalablement chiffrées, rendant impossible tout accès non autorisé même par les administrateurs du service.

### Transparence et audits

Le code étant [open source](https://github.com/ente-io/auth), la communauté peut vérifier l'absence de portes dérobées. Ente a fait réaliser des [audits externes multiples](https://ente.io/blog/cryptography-audit/) pour valider la sécurité de son implémentation :

- **Cure53** (Allemagne) : Audit de sécurité applicative et cryptographique
- **Symbolic Software** (France) : Expertise cryptographique spécialisée  
- **Fallible** (Inde) : Tests de pénétration et analyse des vulnérabilités

Ces audits indépendants, menés par des firmes reconnues, garantissent que l'implémentation cryptographique d'Ente Auth respecte les meilleures pratiques de sécurité et ne présente pas de failles critiques.

### Respect de la vie privée

Ente Auth applique une [politique de confidentialité exemplaire](https://ente.io/privacy/) fondée sur la collecte minimale de données. Seules les informations strictement nécessaires au fonctionnement du service sont conservées : votre adresse e-mail pour l'authentification et la récupération de compte.

**Aucun tracking ni télémétrie** : Contrairement à la plupart des applications, Ente Auth ne collecte aucune métrique d'usage, aucune donnée de crash identifiante, ni aucune information comportementale. L'application fonctionne sans trackers publicitaires ou analytics intrusifs.

**Conformité GDPR** : Ente respecte intégralement le Règlement Général sur la Protection des Données européen. Vous disposez du droit d'accéder, corriger, ou supprimer vos données à tout moment. L'[export de données](https://ente.io/take-control/) s'effectue en un clic, et la suppression définitive de votre compte efface toutes vos données des serveurs.

**Stockage décentralisé et sécurisé** : Vos données chiffrées sont répliquées sur 3 prestataires différents, dans 3 pays distincts, garantissant une disponibilité optimale tout en évitant la dépendance à un unique fournisseur cloud.

Le modèle économique d'Ente repose sur le service payant Ente Photos, permettant d'offrir Ente Auth **gratuitement et sans limitations** sans compromettre votre confidentialité par la monétisation de vos données. Cette approche garantit la pérennité du service sans dépendre de la publicité ou de la revente de données personnelles.

## Comparaison avec d'autres solutions

| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth se distingue comme l'une des rares solutions à cumuler tous les avantages : transparence du code source, sauvegarde cloud chiffrée, et synchronisation multiplateforme.

## Cas d'usage recommandés

### Utilisateurs particuliers

Ente Auth convient parfaitement aux particuliers soucieux de sécurité qui activent systématiquement la 2FA. Vous n'aurez plus à craindre de perdre vos codes en changeant de téléphone, ni à choisir entre praticité et sécurité.

### Utilisation familiale et multi-appareils

L'application prend tout son sens si vous utilisez plusieurs appareils. Vous pouvez enregistrer vos codes sur smartphone et tablette, ou partager certains codes familiaux (Netflix, cloud familial) de manière synchronisée et sûre.

### Usage professionnel

Pour les équipes gérant des comptes sensibles, Ente Auth facilite la collaboration tout en préservant la sécurité grâce à ses fonctionnalités de partage avancées intégrées dans la section "Organisation et gestion".

## Bonnes pratiques

- **Sauvegardez vos codes de secours** : Conservez précieusement les codes de récupération fournis par chaque service, hors de votre téléphone.

- **Utilisez un mot de passe maître fort** : Votre master password Ente Auth doit être unique et robuste car il protège tous vos codes.

- **Activez la protection locale** : Configurez PIN ou biométrie pour empêcher un accès physique non autorisé.

- **Ne personnalisez pas à l'excès** : Évitez les modifications avancées qui pourraient compromettre la synchronisation.

- **Gardez l'application à jour** : Les mises à jour corrigent les failles de sécurité et améliorent les fonctionnalités.

- **Testez la restauration** : Vérifiez occasionnellement que vous pouvez restaurer vos codes sur un autre appareil.

## Conclusion

Ente Auth représente une solution moderne et complète pour l'authentification à deux facteurs. En combinant sécurité, transparence et facilité d'usage, cette application open source répond aux besoins des utilisateurs exigeants sans sacrifier la commodité.

Contrairement aux solutions propriétaires qui vous enferment dans un écosystème opaque, Ente Auth vous redonne le contrôle de vos données d'authentification tout en vous protégeant contre la perte accidentelle grâce à ses sauvegardes chiffrées.

Que vous soyez un particulier souhaitant sécuriser vos comptes personnels ou une équipe gérant des accès professionnels, Ente Auth constitue un choix judicieux pour moderniser votre approche de la sécurité numérique sans compromis sur la vie privée.

## Ressources et support

### Documentation officielle
- **Site officiel** : [ente.io/auth](https://ente.io/auth)
- **Centre d'aide** : [help.ente.io/auth](https://help.ente.io/auth)
- **Blog technique** : [ente.io/blog](https://ente.io/blog)

### Code source et transparence
- **GitHub** : [github.com/ente-io/auth](https://github.com/ente-io/auth)
- **Audit cryptographique** : [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)

### Communauté
- **Discord** : [discord.gg/z2YVKkycX3](https://discord.gg/z2YVKkycX3)
- **Reddit** : [r/enteio](https://reddit.com/r/enteio)
