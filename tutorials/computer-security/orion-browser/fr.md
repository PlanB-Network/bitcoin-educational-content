---
name: Orion Browser
description: Comment utiliser Orion Browser pour protéger sa vie privée sur Mac et iPhone ?
---

![cover](assets/cover.webp)

## Introduction

Dans un contexte où la majorité des navigateurs collectent massivement nos données personnelles, le choix d'un navigateur respectueux de la vie privée devient crucial. Chrome domine avec 65% du marché mondial, mais son modèle économique repose sur l'exploitation de vos données de navigation. Safari, bien qu'intégré à l'écosystème Apple, manque de fonctionnalités avancées de protection et ne supporte pas les extensions tierces de manière flexible.

![Répartition du marché des navigateurs](assets/fr/01.webp)
*Répartition du marché des navigateurs web : Chrome domine largement avec plus de 65% de part de marché, suivi de Safari, Edge et Firefox*

**Orion Browser** se présente comme une alternative innovante pour les utilisateurs Apple. Développé par Kagi, ce navigateur combine la rapidité du moteur WebKit avec une philosophie zéro télémétrie. Contrairement à ses concurrents, Orion n'envoie aucune donnée à des serveurs distants et bloque nativement 99,9% des publicités et traqueurs, y compris sur YouTube.

Sa particularité unique ? Orion est le **seul navigateur WebKit** permettant d'installer nativement les extensions Chrome **et** Firefox, offrant ainsi le meilleur des deux mondes. Cette compatibilité, combinée à une consommation mémoire 2 à 3 fois inférieure aux autres navigateurs et une intégration parfaite à l'écosystème Apple (iCloud, Keychain), en fait un choix idéal pour les utilisateurs Mac et iPhone soucieux de leur confidentialité.

## Pourquoi choisir Orion Browser ?

### Avantages principaux

**Protection maximale dès l'installation** : Orion bloque 99,9% des publicités (YouTube inclus) et tous les traqueurs first-party et third-party par défaut. Sa technologie combine WebKit's Intelligent Tracking Prevention avec les listes EasyPrivacy pour une efficacité maximale. Particularité unique : Orion bloque les scripts de fingerprinting **avant leur exécution**, rendant le tracking littéralement impossible - une approche plus radicale que les autres navigateurs qui tentent seulement de "masquer" les données.

**Zéro télémétrie vérifiable** : Orion adopte une approche radicale en matière de confidentialité avec une architecture "zero telemetry" par conception. Contrairement aux autres navigateurs qui effectuent des centaines de requêtes réseau au démarrage (exposant IP, empreinte navigateur, informations personnelles), Orion ne "phone home" jamais. Cette différence fondamentale élimine complètement les risques de fuite de données involontaires.

**Performance exceptionnelle** : Basé sur une version optimisée de WebKit, Orion égale voire surpasse Safari en rapidité sur Mac. Les tests Speedometer 2.0/2.1 le placent systématiquement en tête sur les processeurs Apple Silicon. Le blocage natif des publicités accélère encore le chargement des pages de 20 à 40%.

**Support universel des extensions** : Innovation majeure, Orion permet d'installer les extensions du Chrome Web Store **et** de Mozilla Add-ons. Le support WebExtensions est actuellement expérimental avec un objectif de 100% de compatibilité à la sortie de bêta. Vous pouvez utiliser de nombreuses extensions populaires comme uBlock Origin, Bitwarden, même sur iPhone - une première mondiale sur iOS, bien que certaines puissent ne pas fonctionner parfaitement.

### Limitations à connaître

- **Disponibilité limitée** : Actuellement réservé à macOS et iOS/iPadOS. Une version Linux atteint des jalons de développement (Milestone 2 en 2025) mais aucun build public n'est disponible. Windows et Android ne sont pas en développement faute de ressources.
- **Code source fermé** : Bien que certains composants soient open-source, Orion reste majoritairement propriétaire, ce qui constitue un point de débat dans la communauté privacy.
- **Extensions expérimentales** : Le support des extensions reste en bêta avec des incompatibilités fréquentes. Les extensions peuvent affecter les performances et certaines ne fonctionnent pas du tout.
- **Sécurité WebKit** : Contrairement à Chromium, WebKit n'offre pas d'isolation de processus par site aussi robuste, ce qui peut poser des risques de sécurité dans certains scénarios.
- **Tests de blocage** : Orion performe volontairement mal aux tests publicitaires en ligne (26-35%) car Kagi considère ces tests comme "fondamentalement défaillants". L'efficacité réelle en usage quotidien est bien supérieure.

## Installation d'Orion Browser

### Sur macOS

![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)
*Page d'accueil de Kagi présentant Orion Browser comme "un navigateur sans publicité, avec une protection totale de la vie privée et un support d'extensions universel"*

- Rendez-vous sur [kagi.com/orion](https://kagi.com/orion/)
- Cliquez sur "**Download Orion for macOS**"

![Page de téléchargement d'Orion Browser](assets/fr/03.webp)
*Page de téléchargement d'Orion Browser montrant la disponibilité pour macOS et iOS, avec les liens vers l'App Store*

- Ouvrez le fichier `.dmg` téléchargé
- Glissez l'application Orion dans le dossier Applications
- Au premier lancement, macOS vous demandera de confirmer l'ouverture

**Alternative Homebrew** :
```bash
brew install --cask orion
```

### Sur iPhone/iPad

- Ouvrez l'**App Store**
- Recherchez "**Orion Browser by Kagi**"
- Installez l'application gratuite (compatible iOS 15+)

### Configuration initiale

Au premier lancement, Orion vous guide à travers plusieurs étapes :

**1. Écran de bienvenue**
![Écran de bienvenue d'Orion](assets/fr/04.webp)
*Écran de bienvenue d'Orion Browser mettant en avant ses fonctionnalités clés : navigation plus rapide, zéro télémétrie, blocage des publicités et support des extensions*

**2. Personnalisation de l'interface**
![Options de personnalisation](assets/fr/05.webp)
*Écran de personnalisation permettant de configurer l'apparence des onglets et l'interface selon vos préférences*

- **Import des données** : Transférez facilement vos favoris et mots de passe depuis Safari, Chrome ou Firefox
- **Synchronisation iCloud** : Activez pour retrouver vos favoris et onglets sur tous vos appareils Apple

**3. Installation sur appareils mobiles**
![Installation sur iOS](assets/fr/06.webp)
*Écran d'installation sur iOS montrant le QR code pour télécharger rapidement Orion Browser depuis l'App Store*

**4. Interface d'accueil et outils essentiels**

![Page d'accueil Orion](assets/fr/07.webp)
*Interface d'accueil d'Orion Browser : la flèche indique les trois outils clés accessibles directement depuis la barre d'adresse*

Une fois la configuration terminée, vous découvrez l'interface épurée d'Orion avec ses **trois outils essentiels** (indiqués par la flèche) :

- **Bouclier 🛡️** : Affiche le Privacy Report avec le nombre d'éléments bloqués sur la page courante
- **Pinceau 🖌️** : Personnalise l'affichage de la page (thème, police, suppression d'éléments gênants)
- **Engrenage ⚙️** : Configure les paramètres spécifiques au site web (permissions, blocage, etc.)

Ces outils sont toujours accessibles et vous permettent de contrôler votre expérience de navigation site par site.

**Important** : Orion est gratuit et ne nécessite aucune inscription ou création de compte pour fonctionner.

![Orion+ dans les préférences](assets/fr/08.webp)
*Écran de souscription Orion+ dans les préférences, proposant un abonnement optionnel pour soutenir le développement*

**Orion+ (optionnel)** : Pour soutenir le développement du projet, Kagi propose Orion+ (5 $ /mois, 50 $ /an, ou 150 $ à vie). Cette souscription volontaire permet de :
- Communiquer directement avec l'équipe de développement
- Influencer l'évolution du navigateur selon vos besoins
- Accéder aux versions Nightly avec les dernières fonctionnalités expérimentales
- Bénéficier du moteur WebKit le plus récent
- Obtenir un badge distinctif sur le forum de feedback

Orion+ garantit l'indépendance du projet : "Votre contribution financière nous aide à rester indépendants et à tenir notre promesse de devenir le meilleur navigateur pour nos utilisateurs". C'est ce modèle de financement utilisateur qui permet à Orion de rester sans publicité et sans télémétrie.

## Configuration pour une confidentialité maximale

### Paramètres essentiels

Accédez aux préférences via **Orion → Preferences** (ou ⌘,) :

**1. Search - Moteur de recherche privé**

![Configuration du moteur de recherche](assets/fr/09.webp)
*Configuration du moteur de recherche par défaut : DuckDuckGo est sélectionné pour une confidentialité maximale*

- **Moteur par défaut** : Sélectionnez **DuckDuckGo**, **Startpage** ou **Kagi** pour une confidentialité optimale (évitez Google/Bing)
- **Suggestions de recherche** : Désactivez-les pour éviter les fuites de frappe vers les serveurs du moteur de recherche

**2. Privacy - Protection générale**

![Content Blocker dans les préférences](assets/fr/12.webp)
*Paramètres de confidentialité d'Orion montrant le Content Blocker avec 119 156 règles actives, les options de suppression des trackers et l'agent utilisateur personnalisé*

**Content Blocker actif par défaut** :
- **EasyList** : 119k+ règles bloquant les publicités
- **EasyPrivacy** : Protection contre le tracking
- **Manage Filter Lists** : Ajoutez des listes supplémentaires (Hagezi recommandée)

**Options de confidentialité** :
- **Remove trackers from URLs** : "For Private Browsing only" nettoie les liens copiés
- **Share crash reports** : "After asking for approval" respecte votre consentement
- **Custom user agent** : Modifiable pour contourner certains blocages

![YouTube avec Privacy Report](assets/fr/10.webp)
*Exemple de YouTube visionné avec Orion : aucune publicité visible et Privacy Report montrant les nombreux éléments bloqués*

**3. Website Settings - Contrôle par site**

![Website Settings pour YouTube](assets/fr/11.webp)
*Website Settings pour YouTube montrant les options de compatibilité, blocage de contenu et permissions spécifiques au site*

**Accès rapide** : Cliquez sur l'engrenage ⚙️ dans la barre d'adresse pour ajuster :
- **Compatibility Mode** : Résout les problèmes d'affichage en suspendant les extensions
- **Content Blockers** : Désactive le blocage pour un site spécifique si nécessaire
- **JavaScript/Cookies** : Contrôle granulaire par site
- **Permissions** : Caméra, micro, localisation configurés individuellement

**4. Filtres personnalisés avancés**

**Création de filtres sur mesure** (Privacy → Manage Filter Lists → Custom Filters) :

**Syntaxe simplifiée** (compatible Adblock Plus) :
- `reddit.com##.promotedlink` : Cache les posts sponsorisés Reddit
- `||ads.example.com^` : Bloque complètement un domaine publicitaire
- `@@||site-utile.com^` : Crée une exception pour un site

**Astuce** : Visitez [FilterLists.com](https://filterlists.com) pour des milliers de listes spécialisées prêtes à l'emploi.

### Extensions recommandées

Orion supporte nativement les extensions Chrome et Firefox. Installez-les directement depuis les stores officiels :

**Essentielles** :
- **uBlock Origin** : Complément au bloqueur natif pour un contrôle granulaire
- **Bitwarden** : Gestionnaire de mots de passe open-source
- **ClearURLs** : Supprime les paramètres de tracking des URLs

**Optionnelles** :
- **LocalCDN** : Sert localement les bibliothèques communes
- **Cookie AutoDelete** : Supprime automatiquement les cookies après fermeture des onglets
- **NoScript** : Contrôle total sur l'exécution JavaScript (utilisateurs avancés)

Pour installer une extension :
- Visitez [chrome.google.com/webstore](https://chrome.google.com/webstore) ou [addons.mozilla.org](https://addons.mozilla.org)
- Cliquez sur "Ajouter à Chrome/Firefox"
- Orion interceptera et installera l'extension automatiquement

**Attention** : Le support d'extensions étant expérimental, de nombreuses extensions peuvent ne pas fonctionner correctement ou affecter les performances. En cas de problème (site qui ne fonctionne plus, lenteurs), désactivez les extensions une par une pour identifier la source.

## Utilisation quotidienne

### Interface et fonctionnalités uniques


![Outil de personnalisation pinceau](assets/fr/13.webp)
*Menu pinceau d'Orion permettant de personnaliser l'affichage : taille de police, thème (clair/sombre), désactivation des en-têtes collants et suppression d'éléments gênants*

**Outil pinceau : personnalisation avancée**

L'outil **pinceau** d'Orion est une fonctionnalité unique permettant de personnaliser l'affichage de chaque site web :

**Options de thème** :
- Basculer entre thème clair et sombre pour chaque site
- Adaptation automatique selon vos préférences système

**Contrôle typographique** :
- **Taille de police** : Ajustez la lisibilité avec les boutons A- et A+
- **Style de police** : Changez la famille de polices (par défaut ou personnalisée)

**Nettoyage d'interface** :
- **Disable sticky headers** : Supprime les en-têtes qui restent collés en haut lors du défilement
- **Erase elements** : Supprimez définitivement les éléments gênants (publicités, pop-ups, bandeaux cookies)
  - Cliquez sur "+ Erase" puis sélectionnez l'élément à masquer
  - Très utile pour les sites avec des publicités persistantes ou des éléments de tracking visuels

**Persistance** : Tous ces réglages sont sauvés par domaine et réappliqués automatiquement lors de vos prochaines visites.

**Gestion avancée des onglets** :
- **Onglets verticaux** : Activez via la barre de menus (fonction Tabs on the Side)
- **Onglets compacts** : Dans Préférences → Tabs → Layout "Compact" pour économiser l'espace
- **Groupes d'onglets** : Organisez vos sessions par thème
- **Profils multiples** : Créez des identités séparées via la barre de menus (fonction Profiles) avec données complètement isolées

**Mode Low Power** : Inspiré de l'iPhone, ce mode suspend automatiquement les onglets inactifs après 5 minutes et peut réduire la consommation d'énergie jusqu'à 90%. Activez-le via la barre de menus d'Orion sur Mac, ou dans les réglages sur iOS.

**Outils intégrés** (menu Edit et autres) :
- **Edit Text on Page** : Modifiez temporairement n'importe quel texte (menu Edit)
- **Allow Copy & Paste** : Contourne les restrictions de copie (menu Edit)
- **Copy Clean Link** : Clic droit sur un lien pour supprimer les paramètres de tracking
- **Focus Mode** : Navigation plein écran sans distractions
- **Picture-in-Picture** : Regardez des vidéos en fenêtre flottante
- **Open in Internet Archive** : Accès direct aux versions archivées
- **Privacy Report** : Cliquez sur le bouclier 🛡️ pour voir les éléments bloqués par page

### Gestion de la navigation privée

La navigation privée d'Orion (⌘⇧N) offre :
- Isolation complète des cookies et sessions
- Effacement automatique à la fermeture
- Désactivation de l'historique et du cache
- Protection renforcée contre le fingerprinting

**Astuce** : Pour un compartimentage avancé, créez des **profils séparés** via la barre de menus (fonction Profiles). Chaque profil apparaît comme une app distincte dans le Dock avec ses propres paramètres, extensions et données complètement isolés.

### Optimisation des performances et privacy

Pour maintenir Orion rapide et privé :
- **Extensions** : Limitez au strict nécessaire (peuvent réduire les performances)
- **Low Power Mode** : Activez pour les longues sessions (90% d'économie possible)
- **Privacy Report** : Cliquez sur le bouclier 🛡️ pour voir les blocages en temps réel
- **Personnalisation visuelle** : Utilisez le pinceau 🖌️ pour adapter l'affichage et supprimer les éléments gênants
- **Copy Clean Link** : Clic droit pour copier les liens sans trackers
- **Profils séparés** : Utilisez des profils dédiés pour compartimenter vos activités
- **Website Settings** : Cliquez sur l'engrenage ⚙️ pour adapter les permissions par site
- **Nettoyage régulier** : Videz le cache via Orion → Clear Browsing Data

## Comparaison avec les alternatives

| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Versus Safari** : Orion offre une protection supérieure avec son bloqueur avancé et le support des extensions, tout en conservant les performances WebKit.

**Versus Chrome** : Protection incomparable de la vie privée, sans compromis sur la compatibilité grâce au support des extensions Chrome.

**Versus Firefox** : Plus rapide sur Mac, interface plus intuitive, mais moins de contrôle granulaire et pas open-source.

**Versus Brave** : Philosophie similaire mais Orion évite les controverses crypto/BAT et offre une meilleure intégration Apple.

## Cas d'usage recommandés

**Idéal pour** :
- Utilisateurs Apple cherchant plus de confidentialité que Safari
- Personnes voulant bloquer toutes les publicités (YouTube inclus) sans extensions
- Développeurs nécessitant les devtools WebKit avec protection privacy intégrée
- Utilisateurs d'iPhone voulant des extensions desktop sur mobile (innovation unique)
- Professionnels ayant besoin de compartimenter leurs activités (profils multiples)
- Utilisateurs mobiles cherchant une meilleure gestion de batterie (Low Power Mode)

**À éviter si** :
- Vous utilisez principalement Windows/Linux (pas de version disponible)
- L'open-source complet est indispensable pour votre threat model
- Vous dépendez d'extensions spécifiques qui pourraient ne pas fonctionner
- Vous nécessitez une synchronisation multi-plateforme au-delà de l'écosystème Apple
- Vous préférez une solution éprouvée et stable (statut bêta permanent depuis 2021)

## Points d'attention et sécurité

### Spécificités de sécurité uniques

**Protection anti-fingerprinting révolutionnaire** : Orion est le seul navigateur bloquant complètement l'exécution des scripts de fingerprinting avant qu'ils ne puissent analyser votre système. Cette approche "pas de script qui tourne = pas de fingerprinting possible" surpasse les méthodes traditionnelles de masquage utilisées par d'autres navigateurs.

**Whitelist transparente** : Orion maintient une petite liste publique de sites (browserbench.org, wizzair.com) où le blocage est automatiquement désactivé pour éviter les dysfonctionnements. Cette transparence permet aux utilisateurs de comprendre exactement quand et pourquoi le blocage est allégé.

**Extensions non auditées** : Le support d'extensions Chrome/Firefox introduit des risques supplémentaires car ces extensions n'étaient pas conçues pour WebKit et ne sont pas spécifiquement auditées pour cet environnement.

### Maintenance et mise à jour

- **Mises à jour automatiques** : Orion se met à jour automatiquement sur macOS via Sparkle
- **Suivi des vulnérabilités** : Consultez régulièrement les notes de version pour les correctifs de sécurité
- **Rapport de bugs** : Utilisez [orionfeedback.org](https://orionfeedback.org) pour signaler les problèmes


## Conclusion

Orion Browser représente une avancée significative pour la confidentialité sur macOS et iOS. Son approche zéro télémétrie, combinée à un bloqueur natif ultra-efficace et au support unique des extensions universelles, en fait un choix excellent pour les utilisateurs Apple soucieux de leur vie privée.

**Important** : Orion reste en bêta permanente depuis 2021, avec des limitations de compatibilité d'extensions et des risques inhérents à WebKit. Évaluez ces compromis selon votre modèle de menace.

Pour une utilisation quotidienne sur Mac ou iPhone, c'est probablement le meilleur compromis entre confidentialité, performance et facilité d'utilisation disponible dans l'écosystème Apple, à condition d'accepter ses limitations.

N'oubliez pas : la protection de votre vie privée ne dépend pas uniquement de votre navigateur. Combinez Orion avec de bonnes pratiques (mots de passe forts, 2FA, VPN si nécessaire) pour une sécurité optimale en ligne.

## Ressources et support

### Documentation officielle
- **Site officiel** : [kagi.com/orion](https://kagi.com/orion/)
- **FAQ complète** : [browser.kagi.com/faq](https://browser.kagi.com/faq)
- **Forum communautaire** : [community.kagi.com](https://community.kagi.com)
- **Suivi des bugs** : [orionfeedback.org](https://orionfeedback.org)
- **GitHub Orion** : [github.com/OrionBrowser](https://github.com/OrionBrowser) - Composants open-source
- **Blog Kagi** : [blog.kagi.com](https://blog.kagi.com) - Actualités et mises à jour

### Tests de vérification recommandés

Après configuration, testez votre setup :
- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Test d'empreinte digitale
- [DNS Leak Test](https://www.dnsleaktest.com/) - Vérification des fuites DNS
- [BrowserLeaks](https://browserleaks.com/) - Suite complète de tests privacy

### Alternatives sur Plan ₿ Network
Pour une protection maximale, consultez nos autres guides :
- [Firefox durci](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Configuration avancée multi-plateforme
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Anonymat réseau complet
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Protection fingerprinting maximale

Si vous souhaitez approfondir vos connaissances sur l’histoire et le fonctionnement des navigateurs, ainsi que sur les principaux objets numériques de votre quotidien, je vous invite à découvrir notre nouvelle formation gratuite SCU 202, disponible sur Plan ₿ Network :

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
