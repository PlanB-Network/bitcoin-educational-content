---
name: Proton Authenticator
description: Comment utiliser Proton Authenticator pour sécuriser ses comptes avec la 2FA ?
---
![cover](assets/cover.webp)

L'authentification à deux facteurs (2FA) ajoute une barrière de sécurité supplémentaire à vos comptes en exigeant, en plus de votre mot de passe, une preuve supplémentaire que vous seul possédez. Activer la 2FA réduit drastiquement les risques de piratage, même si votre mot de passe est compromis suite à du phishing ou une fuite de données. Sans 2FA, un attaquant n'a besoin que de votre mot de passe pour accéder à vos comptes ; avec 2FA, il lui faudrait aussi votre deuxième facteur, ce qui déjoue la plupart des tentatives de vol de compte.

Différents types de 2FA existent. Les codes par SMS sont mieux que rien, mais restent vulnérables aux attaques de SIM swapping et à l'interception. Nous ne recommandons pas le SMS comme 2FA principal. Les applications d'authentification (TOTP) génèrent des codes temporaires localement sur votre appareil, ce qui les rend bien plus difficiles à intercepter. Les clés de sécurité physiques offrent la meilleure sécurité mais nécessitent du matériel dédié.

Proton Authenticator s'inscrit dans la catégorie des authentificateurs TOTP. C'est une réponse de Proton aux limites des applications existantes : beaucoup sont propriétaires, contiennent des trackers publicitaires et n'offrent pas de sauvegarde chiffrée. Proton Authenticator se distingue en fournissant une application open source, sans pubs ni trackers, avec sauvegarde chiffrée de bout en bout.

## Présentation de Proton Authenticator

Proton Authenticator est une application mobile et desktop d'authentification TOTP développée par Proton, réputé pour ses services axés sur la confidentialité. Comme tous les produits Proton, l'application est open source et a fait l'objet d'audits de sécurité indépendants. Elle est disponible gratuitement sur toutes les plateformes (Android, iOS, Windows, macOS, Linux).

Proton Authenticator apporte les fonctionnalités principales suivantes :

- **Génération de codes TOTP** pour vos comptes 2FA, compatibles avec la majorité des sites utilisant Google Authenticator, Authy, etc.

- **Sauvegarde cloud chiffrée optionnelle** : vous pouvez lier l'application à votre compte Proton pour sauvegarder et synchroniser vos codes de manière chiffrée de bout en bout. Si vous perdez votre appareil, il suffit de reconnecter un nouvel appareil pour restaurer tous vos codes.

- **Synchronisation multi-appareils** : en vous connectant à Proton dans l'application, vos codes 2FA se synchronisent automatiquement entre plusieurs appareils via le chiffrement de bout en bout. Sur iOS, une alternative est la synchronisation via iCloud.

- **Verrouillage local par mot de passe ou biométrie** : l'application propose un verrouillage par code PIN et/ou par empreinte digitale/Face ID. Ainsi, même si quelqu'un accède physiquement à votre téléphone déverrouillé, il ne pourra pas ouvrir Proton Authenticator.

- **Aucune collecte de données ni trackers** : Proton s'engage à ne récolter aucune donnée personnelle via l'application. Il n'y a pas de publicité ni d'analyse comportementale cachée.

- **Import/Export faciles** : un point fort de Proton Authenticator est la présence d'un assistant d'import des comptes existants, compatible avec d'autres applications (Google Authenticator, Authy, Aegis, etc.). De même, vous pouvez exporter vos codes vers un fichier si besoin.

En résumé, Proton Authenticator vise à être une solution 2FA sans compromis : sécurisée, privée, flexible.

## Installation

Proton Authenticator est disponible gratuitement sur toutes les plateformes. Pour télécharger l'application, rendez-vous sur la page officielle : [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)

![PROTON AUTHENTICATOR](assets/fr/01.webp)

*Page officielle de Proton Authenticator montrant les fonctionnalités principales et l'interface de l'application*

Sur cette page, vous trouverez les liens de téléchargement pour tous les systèmes d'exploitation : Android, iOS, Windows, macOS et Linux. Il vous suffit de cliquer sur le système d'exploitation de votre choix et de suivre les étapes d'installation standard.

Dans ce tutoriel, nous allons vous montrer l'installation et la configuration sur macOS, puis nous verrons comment installer l'application sur iOS et synchroniser vos codes entre les deux appareils.

### Installation sur macOS

Une fois l'application téléchargée et installée, lancez Proton Authenticator. Au premier lancement, l'application vous guide à travers quelques écrans de configuration initiale :

![PROTON AUTHENTICATOR](assets/fr/02.webp)

*Écran de bienvenue de Proton Authenticator avec le message "La sécurité dans chaque code" et le bouton "Commencez"*

### Importation initiale

Si Proton Authenticator détecte que vous utilisiez auparavant une autre application 2FA, un assistant d'import peut apparaître. Il prend en charge l'import direct depuis certaines applications (Google Authenticator, 2FAS, Authy, Aegis, etc.). Vous pouvez sinon passer cette étape et ajouter vos comptes manuellement plus tard.

![PROTON AUTHENTICATOR](assets/fr/03.webp)

*Assistant d'importation proposant de transférer vos codes depuis d'autres applications d'authentification*

![PROTON AUTHENTICATOR](assets/fr/04.webp)

*Liste des applications compatibles pour l'import : 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth et Google Authenticator*

### Protection locale de l'application

Définissez un code PIN de déverrouillage, ou activez le déverrouillage par biométrie (Touch ID) si proposé. Cette étape est cruciale pour empêcher quiconque utilisant votre Mac d'accéder librement à vos codes 2FA.

![PROTON AUTHENTICATOR](assets/fr/05.webp)

*Écran de configuration de Touch ID avec le message "Protégez vos données" et le bouton "Activer Touch ID"*

### Options de synchronisation

L'application vous propose également d'activer la synchronisation iCloud pour sauvegarder vos données de manière sécurisée entre vos appareils Apple.

![PROTON AUTHENTICATOR](assets/fr/06.webp)

*Option de synchronisation iCloud avec le message "Sauvegardez vos données en toute sécurité grâce à la synchronisation iCloud chiffrée"*

Une fois ces étapes franchies, Proton Authenticator est prêt à l'emploi.

![PROTON AUTHENTICATOR](assets/fr/07.webp)

*Interface principale vide de Proton Authenticator avec les options "Créer un nouveau code" et "Importer des codes"*

## Ajouter un compte 2FA avec ProtonMail

Nous allons maintenant voir comment ajouter votre premier code 2FA en utilisant l'exemple de ProtonMail. Cette méthode fonctionne de manière identique pour tous les services qui supportent l'authentification à deux facteurs.

### Activer la 2FA sur ProtonMail

Tout d'abord vous pouvez consulter notre guide sur ProtonMail pour plus d'informations : 

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Connectez-vous à votre compte ProtonMail et rendez-vous dans les paramètres de sécurité. Recherchez l'option "Two-factor authentication" et activez-la. 

![PROTON AUTHENTICATOR](assets/fr/08.webp)

*Page des paramètres ProtonMail avec l'option "Authenticator app" dans la section "Two-factor authentication"*

Cliquez sur le bouton pour activer l'authentificateur et ProtonMail vous proposera de choisir une application d'authentification.

![PROTON AUTHENTICATOR](assets/fr/09.webp)

*Fenêtre de configuration 2FA de ProtonMail avec les boutons "Cancel" et "Next"*

ProtonMail affichera alors un QR code à scanner avec votre application d'authentification.

![PROTON AUTHENTICATOR](assets/fr/10.webp)

*QR code ProtonMail à scanner avec votre application d'authentification, avec l'option "Enter key manually instead" disponible*

Si vous préférez saisir la clé manuellement, cliquez sur "Enter key manually instead" pour voir la clé secrète.

![PROTON AUTHENTICATOR](assets/fr/11.webp)

*Saisie manuelle des informations 2FA : Key, Interval (30) et Digits (6)*

### Scanner le QR code avec Proton Authenticator

Dans Proton Authenticator sur macOS, cliquez sur "Créer un nouveau code". L'application vous propose plusieurs options : **Scanner un QR code** ou **Entrer la clé manuellement**.

Utilisez la caméra de votre Mac pour scanner le QR code affiché sur l'écran de ProtonMail. Une fois le QR code scanné, vous arriverez sur l'écran de configuration du nouveau code.

![PROTON AUTHENTICATOR](assets/fr/12.webp)

*Fenêtre de création d'une nouvelle entrée avec les champs Titre (ProtonMail), Secret, Émetteur (Proton), paramètres de chiffres et intervalle*

Proton Authenticator aura automatiquement rempli les informations. Vous pouvez personnaliser le nom si nécessaire, puis cliquez sur "Sauvegarder".

![PROTON AUTHENTICATOR](assets/fr/13.webp)

*Code TOTP généré pour ProtonMail (848 812) avec le compte-temps restant affiché*

### Valider la configuration

ProtonMail vous demandera de saisir un code à 6 chiffres généré par Proton Authenticator pour confirmer que la 2FA fonctionne correctement. 

![PROTON AUTHENTICATOR](assets/fr/14.webp)

*Écran de validation ProtonMail demandant de saisir le code à 6 chiffres (848812)*

Copiez le code depuis l'application (en cliquant dessus) et collez-le dans ProtonMail pour finaliser l'activation.

Une fois validé, ProtonMail vous proposera de télécharger vos codes de récupération. Il est crucial de les sauvegarder précieusement.

![PROTON AUTHENTICATOR](assets/fr/15.webp)

*Écran des codes de récupération ProtonMail avec la liste des codes de secours et le bouton "Download"*

### Codes de secours

Lors de l'ajout d'un compte, conservez les codes de secours fournis par le service. La plupart des sites proposent des codes de récupération statiques à usage unique à stocker en lieu sûr. Gardez ces codes de secours en dehors de Proton Authenticator pour pouvoir accéder à votre compte si vous perdiez l'accès à l'application 2FA.

## Installation sur iOS et import de codes

Maintenant que vous avez configuré Proton Authenticator sur macOS, vous souhaiterez peut-être également l'utiliser sur votre iPhone ou iPad. Voici comment procéder pour avoir vos codes 2FA sur plusieurs appareils.

### Télécharger l'application sur iOS

Rendez-vous sur l'App Store et recherchez "Proton Authenticator". Téléchargez et installez l'application sur votre appareil iOS.

![PROTON AUTHENTICATOR](assets/fr/16.webp)

*Processus d'installation sur iOS : écran de bienvenue, assistant d'import, sélection des applications compatibles, et écran final "Importer des codes depuis Proton Authenticator"*

### Méthode 1 : Export/Import via fichier JSON

Si vous n'utilisez pas de synchronisation automatique (iCloud ou compte Proton), vous devrez transférer manuellement vos codes depuis votre Mac vers votre iPhone :

**Étape 1 - Export depuis macOS** :

Sur votre Mac, ouvrez Proton Authenticator et accédez aux paramètres (icône engrenage). Dans le menu, cliquez sur "Exporter".

![PROTON AUTHENTICATOR](assets/fr/17.webp)

*Menu des paramètres de Proton Authenticator sur macOS avec l'option "Exporter" visible*

![PROTON AUTHENTICATOR](assets/fr/18.webp)

*Fenêtre d'export avec le nom du fichier "Proton_Authenticator_backup_2025" et le bouton "Enregistrer"*

Sauvegardez le fichier JSON sur votre Mac. Vous pouvez l'envoyer par email sécurisé ou l'enregistrer dans iCloud Drive pour y accéder depuis votre iPhone.

**Étape 2 - Import sur iOS** :

Sur votre iPhone, installez Proton Authenticator et lors de la configuration, choisissez d'importer des codes. Sélectionnez "Proton Authenticator" dans la liste et importez le fichier JSON.

![PROTON AUTHENTICATOR](assets/fr/19.webp)

*Processus d'import sur iOS : localisation du fichier JSON, confirmation d'import, et écrans de configuration avec les options Face ID et iCloud*

### Méthode 2 : Synchronisation automatique

**Via compte Proton (pour synchronisation multi-plateformes)** :

Si vous n'avez pas encore configuré de compte Proton et souhaitez synchroniser entre différents systèmes d'exploitation, l'application vous proposera de créer ou connecter un compte Proton.

![PROTON AUTHENTICATOR](assets/fr/20.webp)

*Écran de synchronisation des appareils demandant de créer un compte Proton gratuit ou de se connecter à un compte existant*

**Via iCloud (pour l'écosystème Apple uniquement)** :
Si vous utilisez uniquement des appareils Apple, vous pouvez choisir la synchronisation iCloud dans les paramètres de l'application. Cette méthode synchronisera automatiquement vos codes entre tous vos appareils Apple de manière sécurisée, sans nécessiter de compte Proton.

## Sauvegarde chiffrée et restauration

L'une des fonctionnalités phares de Proton Authenticator est sa sauvegarde de bout en bout des codes 2FA, qui garantit qu'une perte ou un changement d'appareil ne vous fera pas tout recommencer à zéro.

### Chiffrement de bout en bout

Quand on parle de sauvegarde cloud chiffrée avec Proton Authenticator, vos secrets TOTP sont chiffrés localement sur votre appareil avant d'être envoyés sur le serveur Proton. Le déchiffrement n'est possible que par vous, sur vos appareils connectés à votre compte Proton. Proton AG n'a pas la clé pour lire vos codes enregistrés.

Sur iOS, si vous optez pour iCloud plutôt que le compte Proton, vos données sont chiffrées selon les standards Apple. La sauvegarde locale sur Android vous permet de chiffrer le fichier de sauvegarde par un mot de passe de votre choix.

### Restauration en cas de perte

Si votre téléphone est perdu, volé ou que vous changez d'appareil :

**Avec sauvegarde Proton activée** : Installez Proton Authenticator sur le nouvel appareil. Lors de la configuration initiale, connectez-vous au même compte Proton. Immédiatement, l'application va synchroniser et télécharger tous vos codes 2FA depuis la sauvegarde chiffrée.

**Avec sauvegarde iCloud (iOS)** : Connectez le nouvel iPhone/iPad avec le même identifiant Apple et assurez-vous d'activer iCloud Keychain. Après avoir installé Proton Authenticator, connectez-vous à iCloud. Vos codes devraient se synchroniser via iCloud et apparaître.

**Sans aucune sauvegarde cloud** : Vous devrez importer manuellement vos comptes. Si vous aviez exporté un fichier de sauvegarde, utilisez la fonction Import dans Proton Authenticator. Dans le pire des cas où vous n'aviez aucune sauvegarde : il faudra recourir aux codes de secours de chaque service ou contacter les supports.

Proton Authenticator permet à tout moment d'exporter vos comptes, soit en un fichier chiffré, soit en QR code multi-comptes. Ces options vous offrent une assurance supplémentaire.

## Bonnes pratiques

L'utilisation d'un authentificateur 2FA améliore grandement votre sécurité, mais il faut respecter certaines bonnes pratiques :

### Sauvegardez vos codes de secours

Lorsque vous activez la 2FA sur un service, on vous remet souvent une liste de codes de récupération. Conservez-les hors de votre téléphone (sur papier, dans un gestionnaire de mots de passe chiffré, etc.). En cas de perte totale de votre authentificateur, ces codes statiques vous sauveront.

### Ne mélangez pas vos mots de passe et vos codes 2FA

Il est tentant d'utiliser un gestionnaire de mots de passe qui stocke aussi les TOTP. Toutefois, garder le mot de passe et le code 2FA au même endroit revient à créer un point de défaillance unique et affaiblir la double authentification. Pour une sécurité maximale, beaucoup d'experts préconisent de séparer les deux facteurs : mots de passe dans un gestionnaire sécurisé, et codes 2FA dans une application distincte comme Proton Authenticator. Cependant, utiliser un gestionnaire intégré reste mieux que de ne pas avoir de 2FA du tout.

### Activez plusieurs méthodes 2FA

Idéalement, utilisez plus d'un second facteur sur vos comptes critiques. N'hésitez pas à ajouter une clé de sécurité physique si le service le permet. N'hésitez pas à consulter notre tutoriel sur les clés physiques Yubikey si vous souhaitez plus d'informations : 

https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

De même, conservez des codes de secours imprimés.

### Restez discret et protégez votre appareil

Ne laissez personne fouiller votre téléphone déverrouillé. Avec Proton Authenticator, vos codes sont protégés par PIN/biométrie – ne divulguez pas ce PIN. De même, méfiez-vous du phishing : même avec 2FA, si vous donnez un code à un site frauduleux en temps réel, il pourrait être utilisé par un attaquant.

### Mises à jour et audits

Gardez Proton Authenticator à jour (les mises à jour corrigent d'éventuelles failles). Le code étant ouvert, la communauté effectue des audits informels, et Proton publie les résultats d'audits formels.

## Comparaison avec d'autres applications

Comment Proton Authenticator se positionne-t-il face aux autres applications d'authentification ? Voici un résumé comparatif :

**Proton Authenticator** : Open source, sauvegarde cloud chiffrée E2EE optionnelle, synchronisation multi-appareils, verrouillage local, aucun tracking, disponible sur mobile et desktop.

**Google Authenticator** : Propriétaire, sauvegarde via compte Google depuis 2023 mais sans chiffrement de bout en bout (les clés peuvent être vues par Google), synchronisation multi-appareils ajoutée en 2023, pas de verrouillage d'application par défaut, contient des trackers Google.

**Aegis Authenticator** : Open source, sauvegarde locale seulement, pas de synchronisation cloud, verrouillage par code/biométrie, aucun tracking, Android uniquement.

**Authy** : Propriétaire, sauvegarde cloud chiffrée par mot de passe mais code fermé, synchronisation multi-appareils, verrouillage PIN/empreinte, collecte le numéro de téléphone, application desktop discontinuée en mars 2024.

Vous trouverez notre guide pour Authy ci-dessous : 

https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator apparaît comme l'une des solutions les plus complètes et sécurisées : open source, synchronisation chiffrée multi-device, sans suivi commercial.

## Ressources et support

### Documentation officielle
- **Site officiel** : [proton.me/authenticator](https://proton.me/authenticator) - Présentation du produit et téléchargements
- **Page de téléchargement** : [proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download) - Liens pour tous les OS
- **Support Proton** : [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Guide officiel d'activation 2FA
- **Blog Proton** : [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Annonce et fonctionnalités détaillées

### Code source et transparence
- **GitHub Proton Authenticator** : [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Code source open source
- **Audits de sécurité** : [proton.me/community/security-audits](https://proton.me/community/security-audits) - Rapports d'audit indépendants

### Tests de sécurité recommandés
Après configuration, testez votre setup :
- [Have I Been Pwned](https://haveibeenpwned.com/) - Vérifiez si vos comptes ont été compromis
- [2FA Directory](https://2fa.directory/) - Liste des services supportant la 2FA

### Communautés et discussions
- **Reddit r/Proton** : [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Communauté officielle Proton
- **Privacy Guides Forum** : [discuss.privacyguides.net](https://discuss.privacyguides.net) - Discussions techniques sur la confidentialité
- **Reddit r/privacy** : [reddit.com/r/privacy](https://reddit.com/r/privacy) - Conseils généraux sur la protection de la vie privée

### Autres
- [Have I Been Pwned](https://haveibeenpwned.com/) - Vérifiez si vos comptes ont été compromis
- [2FA Directory](https://2fa.directory/) - Liste des services supportant la 2FA
