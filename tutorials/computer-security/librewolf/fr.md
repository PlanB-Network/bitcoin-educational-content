---
name: LibreWolf
description: Comment utiliser le navigateur LibreWolf pour la confidentialité
---

![cover](assets/cover.webp)

Chaque clic, chaque recherche, chaque site visité : votre navigateur web est devenu un mouchard sophistiqué qui alimente un système de surveillance commerciale planétaire. Google Chrome, utilisé par plus de 3 milliards de personnes, transforme votre navigation quotidienne en données lucratives pour les géants de la publicité. Même Firefox, malgré sa réputation de navigateur "éthique", active par défaut des mécanismes de télémétrie qui transmettent vos habitudes de navigation à Mozilla.

Cette réalité pose une question essentielle : est-il encore possible de naviguer librement sur Internet sans être constamment épié et profilé ? Heureusement, la réponse est oui, grâce à des projets communautaires qui replacent l'utilisateur au centre de leurs préoccupations.

LibreWolf incarne cette philosophie de résistance numérique. Né d'une communauté de développeurs indépendants, ce navigateur transforme Firefox en véritable bouclier contre la surveillance en ligne. Là où les navigateurs commerciaux cherchent à monétiser votre attention, LibreWolf fait le pari inverse : vous rendre invisible aux yeux des traqueurs tout en préservant une expérience de navigation fluide et moderne.

Dans ce tutoriel, nous découvrirons comment LibreWolf peut transformer votre façon de naviguer sur Internet, en vous offrant une protection robuste contre le pistage sans sacrifier la performance ni la compatibilité web.

![LIBREWOLF](assets/fr/01.webp)
*Parts de marché des navigateurs web : Chrome domine avec 65% du marché, suivi de Safari et Edge. Cette domination soulève des questions sur la diversité et la confidentialité du web.*

## Présentation de LibreWolf

**LibreWolf** est un navigateur web open-source dérivé de Mozilla Firefox, développé et maintenu par une communauté indépendante de passionnés de logiciel libre. Son objectif principal est d'offrir une navigation centrée sur la confidentialité, la sécurité et la liberté de l'utilisateur.

Concrètement, LibreWolf reprend le moteur Gecko de Firefox, mais avec une philosophie radicalement différente : là où Firefox doit équilibrer confidentialité et facilité d'utilisation, LibreWolf fait le choix de privilégier la vie privée par défaut. Le projet supprime tout ce qui pourrait porter atteinte à votre vie privée (télémétrie, collecte de données, modules sponsorisés) tout en intégrant des réglages de sécurité renforcés.

### Objectifs : vie privée et liberté

LibreWolf vise à maximiser la protection contre le pistage et le fingerprinting (empreinte numérique) tout en améliorant la sécurité du navigateur. Ses objectifs principaux incluent :

- **Éliminer toute télémétrie et collecte de données** présentes dans Firefox
- **Désactiver les fonctions contraires à la liberté de l'utilisateur**, comme les modules de DRM propriétaires  
- **Appliquer d'emblée des paramètres orientés confidentialité/sécurité** et des correctifs spécifiques
- **Garantir transparence et indépendance** vis-à-vis des intérêts commerciaux grâce à son développement communautaire

En résumé, LibreWolf se présente comme "Firefox, tel qu'il aurait été si la confidentialité était la priorité absolue" – un navigateur qui vous respecte par défaut, sans configuration additionnelle requise.

### Fonctionnalités principales

Dès le premier lancement, LibreWolf offre un ensemble de fonctionnalités orientées vie privée :

**Aucune télémétrie ni collecte de données :** Contrairement à Chrome ou Firefox qui envoient certaines statistiques d'utilisation, LibreWolf ne collecte absolument rien de votre navigation. Pas de rapports de plantage, pas d'études utilisateur, pas de suggestions sponsorisées.

**Blocage intégré des publicités et traqueurs :** LibreWolf intègre nativement l'extension uBlock Origin, l'un des meilleurs bloqueurs de publicités et trackers du marché. Par défaut, LibreWolf filtre de manière agressive tout ce qui pourrait vous pister en ligne (publicités intrusives, scripts de suivi, mining de cryptomonnaie).

**Moteur de recherche privé par défaut :** LibreWolf propose par défaut DuckDuckGo comme moteur de recherche initial, qui ne conserve aucun historique de vos requêtes. D'autres alternatives axées sur la vie privée (Searx, Qwant, Whoogle) sont également disponibles.

**Protection anti-fingerprint renforcée :** L'empreinte numérique permet d'identifier un navigateur de façon unique via sa configuration, même sans cookies. Pour contrer cela, LibreWolf active la technologie RFP (Resist Fingerprinting) issue du projet Tor, afin de rendre votre navigateur le plus générique possible. Des tests montrent qu'un Firefox standard est unique à ~90% sur des outils comme coveryourtracks.eff.org, contre seulement ~10-20% pour LibreWolf (ces chiffres restent indicatifs et peuvent varier selon la configuration logicielle, matérielle et les extensions installées).

![LIBREWOLF](assets/fr/07.webp)
*Page de test [Cover Your Tracks](https://coveryourtracks.eff.org/) de l'EFF avec le bouton TEST YOUR BROWSER. Cette page permet d'évaluer la protection contre les traqueurs et le fingerprinting.*

![LIBREWOLF](assets/fr/08.webp)
*Résultat du test Cover Your Tracks. Le message "you have strong protection against Web tracking" s'affiche, montrant l'efficacité des protections de LibreWolf.*

**Durcissement des réglages de sécurité :** LibreWolf active par défaut des paramètres de sécurité stricts. La Protection Renforcée contre le Pistage de Firefox est poussée au niveau Strict pour bloquer des milliers de traqueurs, cookies tiers et contenus malveillants. Il active également l'isolement des sites et des cookies (*Total Cookie Protection*) pour cloisonner les données de chaque domaine, et restreint WebRTC (limitation des *ICE candidates* et routage via proxy lorsqu’un proxy est présent) afin de réduire les risques de fuite d’adresse IP.

**Mises à jour rapides du moteur :** Le projet suit de très près les évolutions de Firefox : LibreWolf est toujours basé sur la dernière version stable de Firefox, et les mainteneurs s'efforcent de publier une nouvelle version dans les 24 à 72 heures suivant chaque sortie officielle de Firefox.

## Avantages et inconvénients

### Avantages

- **Aucune télémétrie ni connexion indésirable :** LibreWolf ne transmet aucune donnée d'utilisation, assurant un respect total de votre vie privée.

- **Open-source et communautaire :** Le projet est 100% open-source et maintenu par des bénévoles. Cette indépendance garantit qu'aucun modèle publicitaire n'influencera le développement.

- **Pré-configuré pour la vie privée :** LibreWolf vous fait gagner un temps précieux : nul besoin de passer des heures à durcir les réglages de Firefox, tout est déjà fait.

- **Bloqueur de pub/trackers natif :** uBlock Origin est intégré d'office, ce qui vous protège efficacement contre les pubs et mouchards sans rien faire.

- **Excellentes protections anti-fingerprinting :** Grâce à RFP et aux nombreux paramètres de privacy activés, LibreWolf réduit drastiquement votre empreinte numérique unique sur le web.

- **Performance et légèreté améliorées :** En supprimant la télémétrie et certaines fonctionnalités non essentielles, LibreWolf peut s'avérer légèrement plus rapide et moins gourmand que Firefox standard.

### Inconvénients et limites

- **Pas de mise à jour automatique intégrée :** LibreWolf ne se met pas à jour tout seul. C'est à vous de veiller à installer les nouvelles versions dès leur sortie pour rester en sécurité.

- **Compatibilité réduite avec certains services :** En raison de ses réglages très stricts, LibreWolf peut rencontrer des problèmes sur certains sites web. Les plateformes de streaming Netflix, Disney+ ne fonctionneront pas, car LibreWolf désactive les DRM Widevine par défaut.

- **Pas de réseau anonyme intégré :** Contrairement au Tor Browser, LibreWolf ne route pas le trafic via Tor ou un VPN par lui-même. Si vous avez besoin d'anonymat réseau, il faudra configurer manuellement un proxy/VPN.

- **Cookies et sessions non persistants (par défaut) :** Par souci de confidentialité, LibreWolf supprime les cookies, l'historique et les données de site à chaque fermeture de navigateur. Vous devrez vous reconnecter à vos comptes à chaque nouvelle session.

- **Pas de version mobile ni de synchronisation cloud :** LibreWolf n'existe que sur Desktop (Windows, Linux, macOS). Il n'y a pas d'application mobile, et donc pas de synchronisation de comptes ou de favoris via un cloud.

## Installation de LibreWolf

**Site officiel :** [librewolf.net](https://librewolf.net)

LibreWolf est disponible sur les principaux systèmes d'exploitation de bureau : Linux, Windows et macOS. Pour télécharger LibreWolf, rendez-vous sur le site officiel :

![LIBREWOLF](assets/fr/02.webp)
*Page d'accueil de LibreWolf (librewolf.net) montrant le logo du navigateur, un bouton bleu Installation, et les liens Source Code et Documentation. Une grande flèche bleue pointe vers le bouton d'installation.*

Cliquez sur le bouton "Installation" pour accéder aux instructions détaillées selon votre système d'exploitation :

![LIBREWOLF](assets/fr/03.webp)
*Page de choix des systèmes d'exploitation pour le téléchargement de LibreWolf.*

L'installation diffère selon votre OS :

### Sur Linux
LibreWolf propose des builds pour de nombreuses distributions. Sur Debian/Ubuntu et dérivés, un dépôt APT officiel est disponible. Alternativement, LibreWolf est publié en Flatpak sur Flathub :
```
flatpak install flathub io.gitlab.librewolf-community
```

### Sur Windows
Téléchargez l'installeur (.exe) depuis le site officiel ou utilisez les gestionnaires de packages :
- **Chocolatey :** `choco install librewolf`
- **WinGet :** `winget install librewolf`

### Sur macOS
LibreWolf est disponible sous forme de package .dmg pour Mac. Téléchargez l'image disque sur le site officiel et glissez-déposez l'application LibreWolf dans votre dossier Applications. Alternativement, vous pouvez l'installer via Homebrew.


## Configuration et première utilisation

Au premier démarrage, vous remarquerez l'interface familière de Firefox, à ceci près qu'elle est plus dépouillée : la page d'accueil ne contient que la barre de recherche et aucune suggestion sponsorisée. Vous verrez l'icône d'uBlock Origin dans la barre d'outils – signe que le bloqueur est actif.

![LIBREWOLF](assets/fr/04.webp)
*Page d'accueil de LibreWolf avec extensions et menu. Une flèche bleue en haut à droite indique l'icône du menu (trois barres horizontales).*

LibreWolf charge automatiquement vos pages en mode "strict" (anti-pistage), et le moteur de recherche par défaut sera DuckDuckGo. Vous pouvez essayer de visiter un site de test de tracking (par ex. amiunique.org) pour observer l'empreinte exposée – elle devrait être bien plus générique qu'avec un navigateur standard.

### Paramètres de confidentialité

LibreWolf est déjà configuré de manière optimale pour la confidentialité. Dans Menu → Options → Vie privée et Sécurité, vous verrez que LibreWolf est positionné en mode Protection renforcée contre le pistage : Strict. Ce mode bloque :
- Les traceurs inter-sites
- Les cookies tiers  
- Les contenus de pistage connus
- Les cryptomineurs
- Les détecteurs d'empreinte numérique

![LIBREWOLF](assets/fr/05.webp)
*Page onglet sécurité et vie privée montrant les paramètres de sécurité de LibreWolf.*

WebRTC est désactivé (empêchant les fuites d'IP), et Total Cookie Protection est en place. La télémétrie et les études Firefox sont entièrement désactivées.

### Gestion des cookies et de l'historique

Par défaut, LibreWolf supprime cookies et stockage local à chaque fermeture. Si ce comportement vous gêne, vous pouvez l'ajuster dans Vie privée et Sécurité → Cookies et données de sites en décochant "Supprimer les cookies et les données de sites à la fermeture de LibreWolf".

![LIBREWOLF](assets/fr/06.webp)
*Même page un peu plus bas montrant l'option de suppression des cookies à la fermeture du navigateur.*

### Ajout d'extensions utiles

Par principe, LibreWolf déconseille l'ajout d'extensions non nécessaires, car chaque extension peut être un vecteur de suivi. Néanmoins, certaines extensions réputées peuvent améliorer votre expérience :
- **Firefox Multi-Account Containers** (par Mozilla) pour compartimenter vos navigations
- **Decentraleyes** ou **LocalCDN** pour servir en local des librairies courantes

Évitez particulièrement les extensions de "VPN gratuits" ou proxy douteux – uBlock Origin couvre déjà 99% des besoins.

## Utilisation au quotidien

### Navigation web quotidienne
Utilisez LibreWolf pour vos activités courantes sur Internet. La différence majeure avec un autre navigateur, c'est que vous laissez beaucoup moins de traces publicitaires. Les bannières "Accepter les cookies" disparaissent sur de nombreux sites grâce aux listes de filtrage d'uBlock.

### Utiliser les onglets privés pour compartimenter
Même si LibreWolf efface tout en fin de session, il peut être utile d'ouvrir une fenêtre de navigation privée (Ctrl+Maj+P) pour certaines tâches durant la session afin de cloisonner une identité ponctuelle.

### Profiter des conteneurs Multi-comptes
Installer l'extension Multi-Account Containers peut grandement vous aider à segmenter vos activités en silos étanches. Par exemple, vous pouvez définir un conteneur "Banque" pour vos sites bancaires, un conteneur "Réseaux Sociaux" pour Facebook/Twitter, etc. Chaque conteneur a ses propres cookies, sessions et stockage isolés.

### Gestion fine des permissions par site
LibreWolf vous permet de contrôler au cas par cas les autorisations que vous donnez aux sites (Localisation, Caméra, Micro, Notifications). N'accordez ces permissions qu'aux sites en qui vous avez confiance et où c'est nécessaire.

## Bonnes pratiques avec LibreWolf

1. **Maintenez LibreWolf à jour :** Allez régulièrement sur le site pour voir s'il y a une nouvelle version, surtout après une sortie de Firefox stable.

2. **Évitez de mélanger identité personnelle et navigation privée :** L'idéal est de ne pas vous connecter avec vos comptes personnels sur la même session où vous faites des recherches sensibles.

3. **Ne surchargez pas LibreWolf d'extensions superflues :** Chaque extension installée peut introduire des risques de sécurité ou de fingerprinting.

4. **Utilisez un VPN ou proxy Tor en complément :** LibreWolf ne rend pas anonyme vis-à-vis de votre fournisseur d'accès. Pour obtenir l'anonymat réseau, vous pouvez utiliser LibreWolf derrière un VPN de confiance.

5. **Sauvegardez vos données importantes :** Marque-pages, mots de passe si vous en stockez localement. Envisagez un gestionnaire de mots de passe externe (KeePassXC, Bitwarden) plutôt que le gestionnaire de base du navigateur.

## Comparaison avec d'autres navigateurs

LibreWolf fait partie de la "boîte à outils" des navigateurs orientés vie privée :

**LibreWolf vs Firefox :** LibreWolf arrive déjà durci et sans aucune télémétrie. Firefox garde l'avantage de la synchronisation multi-appareils et d'une base utilisateurs très large, mais nécessite une configuration manuelle pour atteindre le niveau de confidentialité de LibreWolf.

**LibreWolf vs Brave :** Brave utilise le code de Chrome/Chromium et intègre un modèle économique via son programme de publicité optionnelle. LibreWolf, en étant un fork communautaire de Firefox, conserve l'écosystème libre de Mozilla et n'a aucun lien avec Google.

**LibreWolf vs Tor Browser :** Tor Browser est irremplaçable pour l'anonymat face à une surveillance puissante, mais il est lent et inconfortable en usage quotidien. LibreWolf, pour la navigation quotidienne sur le web classique, est bien plus pratique et rapide.

**LibreWolf vs Mullvad Browser :** Mullvad Browser va encore plus loin dans l'uniformisation mais au prix d'une utilisabilité réduite (impossible de conserver un cookie de login). LibreWolf vise un équilibre : très privé, mais utilisable au quotidien.

## Conclusion

LibreWolf représente une excellente solution pour ceux qui recherchent un navigateur "quotidien" ultra-privé sans aller jusqu'à l'anonymat extrême de Tor. C'est un choix idéal pour les activistes, journalistes, développeurs ou utilisateurs avertis qui souhaitent une navigation web classique (rapide, compatible sites modernes) tout en échappant au pistage publicitaire et aux Big Tech.

Bien qu'il présente certaines limitations (pas de mise à jour automatique, compatibilité réduite avec certains services), LibreWolf constitue un outil précieux dans l'arsenal de quiconque souhaite reprendre le contrôle de sa vie privée numérique. Sa facilité d'utilisation et sa configuration par défaut en font un choix judicieux pour les utilisateurs soucieux de confidentialité.

## Ressources

### Documentation officielle
- [Site officiel LibreWolf](https://librewolf.net)
- [Code source sur Codeberg](https://codeberg.org/librewolf)
- [FAQ officielle](https://librewolf.net/docs/faq)

### Guides et comparaisons
- [Guide des navigateurs privés - Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Tests de confidentialité comparatifs](https://privacytests.org)

### Support communautaire
- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)
