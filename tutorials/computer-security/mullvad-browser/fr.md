---
name: Mullvad Browser
description: Comment utiliser le navigateur Mullvad Browser pour la confidentialité
---

![cover](assets/cover.webp)

Dans un monde où la surveillance numérique devient omniprésente, protéger sa vie privée en ligne n'a jamais été aussi crucial. Les entreprises utilisent des techniques sophistiquées pour vous pister: 

- **Cookies tiers**: petits fichiers déposés par des sites externes pour vous suivre d'un site à l'autre
- **Empreintes numériques** (fingerprinting): collecte des caractéristiques uniques de votre navigateur et appareil (résolution d'écran, polices installées, plugins, etc.) pour vous identifier sans cookies
- **Scripts de pistage**: codes JavaScript invisibles qui analysent votre comportement de navigation (clics, défilement, temps passé)
- **Analyse de l'adresse IP**: localisation géographique et identification de votre fournisseur d'accès Internet

Ces données sont ensuite combinées pour créer des profils détaillés de votre comportement en ligne et monétisées, souvent à votre insu. Cette réalité soulève une question fondamentale: comment naviguer sur Internet tout en préservant votre anonymat et votre confidentialité ?

La réponse réside en grande partie dans le choix de votre navigateur web. Cet outil, que nous utilisons quotidiennement pour accéder à l'information, faire nos achats ou communiquer, joue un rôle déterminant dans la protection de nos données personnelles. Malheureusement, les navigateurs les plus populaires comme Google Chrome (qui détient environ 65% du marché mondial) sont conçus selon des modèles économiques basés sur la collecte massive de données utilisateur.

![MULLVAD BROWSER](assets/fr/01.webp)
*Mullvad Browser se distingue par son efficacité exceptionnelle en matière de blocage des traqueurs, surpassant largement les navigateurs grand public.*

Face à cette problématique, de nouveaux acteurs émergent avec une philosophie différente: celle de placer la vie privée au cœur de leur conception. Parmi eux, Mullvad Browser se distingue comme une solution innovante qui combine les meilleures protections de confidentialité avec une expérience de navigation fluide et accessible.

Contrairement aux navigateurs traditionnels qui cherchent à personnaliser votre expérience en collectant vos données, Mullvad Browser adopte l'approche inverse: faire en sorte que tous ses utilisateurs apparaissent identiques aux yeux des sites web, rendant ainsi le pistage individualisé pratiquement impossible.

Dans ce tutoriel, nous découvrirons ensemble comment Mullvad Browser peut transformer votre façon de naviguer sur Internet, en vous offrant une protection robuste contre la surveillance sans sacrifier la facilité d'utilisation.


## Présentation de Mullvad Browser

**Mullvad Browser** est un navigateur web focalisé sur la protection de la vie privée, développé en collaboration avec le projet Tor et distribué gratuitement par la société suédoise Mullvad VPN. Lancé en avril 2023, il se présente comme un **« Tor Browser sans le réseau Tor »**, conçu pour minimiser le pistage en ligne et les empreintes numériques (fingerprinting) tout en permettant à l'utilisateur de naviguer via un VPN de confiance plutôt que par le réseau Tor.

Mullvad Browser est un navigateur libre et open-source basé sur Firefox ESR (la version longue durée de Mozilla Firefox) et durci par les experts du Tor Project. Concrètement, il reprend la plupart des **fonctionnalités de protection de Tor Browser**, mais **ne route pas le trafic via le réseau Tor**. À la place, l'utilisateur peut (et devrait) l'associer à un VPN chiffré de confiance pour anonymiser son adresse IP.

Du point de vue de l'expérience utilisateur, Mullvad Browser ressemble à un navigateur classique et offre une navigation fluide. Il est disponible gratuitement sur Windows, macOS et Linux (pas de version mobile). Il n'est pas nécessaire d'être abonné à Mullvad VPN pour l'utiliser ; toutefois, **utiliser Mullvad Browser sans masquer son IP n'apporte pas d'anonymat complet** – c'est pourquoi il est vivement recommandé de l'utiliser conjointement avec un VPN fiable.

### Objectifs: vie privée et anti-tracking

Le navigateur Mullvad a été conçu dans un but principal: **protéger la vie privée de l'utilisateur** en ligne et contrer les techniques courantes de traçage et de profilage. Ses objectifs principaux incluent:

- **Réduire drastiquement le suivi publicitaire et le pistage** par les sites web et les régies. Mullvad Browser bloque par défaut les traceurs tiers, les cookies de suivi et les scripts de fingerprinting susceptibles de vous identifier.

- **Uniformiser l'empreinte du navigateur** afin de **« se fondre dans la foule »**. L'empreinte numérique (fingerprint) est comme une "carte d'identité" unique créée par la combinaison de toutes les caractéristiques de votre navigateur. Mullvad Browser fait en sorte que tous ses utilisateurs aient exactement la même "carte d'identité", rendant impossible leur distinction individuelle.

- **Offrir une protection immédiate sans extensions additionnelles**. Mullvad Browser vient en configuration *prête-à-l'emploi*: l'utilisateur n'a pas besoin d'installer une panoplie d'extensions ou de modifier des réglages pour être protégé.

- **Ne pas sacrifier la performance ni l'ergonomie** plus que nécessaire. En l'absence du routage Tor, Mullvad Browser offre une navigation beaucoup plus rapide que Tor Browser, se rapprochant des performances d'un navigateur standard couplé à un VPN.

### Fonctionnalités clés de Mullvad Browser

Mullvad Browser embarque une série de **fonctionnalités de sécurité et de confidentialité** inspirées directement de Tor Browser:

- **Navigation privée en permanence:** Le mode Navigation Privée est activé par défaut et impossible à désactiver. **Aucun historique, cookie ou cache n'est conservé d'une session à l'autre**. Dès que vous fermez Mullvad Browser, toutes les données de navigation sont effacées.

- **Protection renforcée contre le fingerprinting:** Le navigateur applique des réglages stricts pour contrecarrer l'empreinte numérique. Cela inclut:
	- **Uniformisation de l'agent utilisateur** et de la version du navigateur
	- **Fuseau horaire fixé à UTC** pour tous les utilisateurs
	- **Letterboxing**: technique qui ajoute automatiquement des marges grises autour des pages web pour standardiser la taille d'affichage et empêcher l'identification par les dimensions de votre écran
	- **Blocage des API de fingerprinting**: les technologies Canvas (dessin 2D), WebGL (graphiques 3D) et AudioContext (traitement audio) sont neutralisées car elles peuvent révéler des détails uniques sur votre matériel
	- **Polices système normalisées** pour éviter l'identification par les polices installées

- **Blocage des traqueurs et publicités:** Mullvad Browser intègre nativement l'extension **uBlock Origin** (préinstallée) avec des listes de protection supplémentaires afin de bloquer les **trackers tiers, scripts publicitaires et autres contenus malveillants**. Cette protection s'accompagne de l'**isolation des cookies tiers** (First-Party Isolation): technique qui range les cookies dans des "pots" séparés pour chaque site web, empêchant ainsi un site de lire les cookies déposés par un autre.

- **Bouton de réinitialisation de session:** Tout comme le bouton "New Identity" de Tor Browser, Mullvad Browser propose un bouton permettant de **redémarrer rapidement le navigateur avec une nouvelle session vierge**.

- **Niveaux de sécurité ajustables:** Vous pouvez ajuster le niveau de sécurité (*Normal*, *Plus sûr*, *Le plus sûr*) dans les paramètres, exactement comme dans Tor Browser.

## Extensions intégrées par défaut

Mullvad Browser inclut **trois extensions préinstallées** qui constituent le cœur de sa protection contre le pistage. **Il est crucial de ne jamais les supprimer ou modifier leurs configurations**, car cela vous rendrait unique parmi les utilisateurs Mullvad Browser:

### **uBlock Origin**
Cette extension de blocage de publicités et de traqueurs vient préconfigurée avec des **listes de filtres optimisées** pour bloquer:
- Les publicités intrusives
- Les traqueurs tiers qui collectent vos données
- Les scripts malveillants
- Les éléments de pistage behavioral

uBlock Origin dans Mullvad Browser utilise des paramètres standardisés pour que tous les utilisateurs bloquent exactement les mêmes éléments, préservant ainsi l'uniformité des empreintes numériques.

### **NoScript**
NoScript fonctionne en arrière-plan pour gérer les **niveaux de sécurité** du navigateur. Cette extension:
- **Contrôle l'exécution de JavaScript** selon le niveau choisi (Normal/Plus sûr/Le plus sûr)
- **Filtre les attaques XSS** (Cross-Site Scripting) automatiquement
- **Bloque les contenus actifs dangereux** sur les sites non-HTTPS
- Son icône est cachée par défaut mais peut être affichée via "Personnaliser la barre d'outils"

### **Extension Mullvad Browser**
Cette extension spécifique à Mullvad offre des fonctionnalités différentes selon que vous soyez client Mullvad VPN ou non:

#### **Sans abonnement Mullvad VPN:**
- **Vérification de connexion basique**: affiche votre IP publique actuelle et quelques informations de connexion
- **Recommandations de confidentialité**: conseils pour améliorer vos paramètres de sécurité (DNS, HTTPS-only, moteur de recherche)
- **Contrôle WebRTC**: activation/désactivation pour éviter les fuites d'adresse IP
- **Peut être supprimée sans impact** sur votre empreinte numérique si vous n'utilisez pas Mullvad VPN

#### **Avec abonnement Mullvad VPN:**
L'extension révèle son plein potentiel avec des fonctionnalités avancées:

- **Proxy SOCKS5 intégré**: connexion directe au proxy du serveur VPN Mullvad avec un clic
	- **Adresse IP fixe**: contrairement au VPN qui peut changer d'IP, le proxy garantit toujours la même adresse de sortie
	- **Kill switch automatique**: si le VPN se déconnecte, le trafic navigateur est immédiatement bloqué
	- **Support IPv6**: connectivité IPv6 même si votre connexion VPN ne l'a pas activée

- **Multihop (double VPN)**: possibilité de changer la localisation du proxy pour créer un tunnel dans le tunnel
	- Votre trafic passe d'abord par votre serveur VPN, puis "saute" vers un autre serveur Mullvad
	- Permet d'utiliser une localisation différente uniquement pour le navigateur

- **Surveillance de connexion avancée**: monitoring en temps réel de votre statut VPN, serveur connecté, et détection des fuites DNS

- **Accès à Mullvad Leta**: moteur de recherche privé réservé aux abonnés (bien que déconseillé par Mullvad pour des raisons de corrélation avec votre compte)

Ces trois extensions travaillent ensemble pour créer un écosystème de protection cohérent, où chaque utilisateur bénéficie exactement des mêmes défenses sans possibilité de personnalisation qui compromettrait l'anonymat collectif.

## Avantages et inconvénients de Mullvad Browser

### Avantages

- **Excellente protection de la vie privée par défaut:** Mullvad Browser applique dès l'installation des réglages très stricts en matière de confidentialité, sans nécessiter de configuration manuelle.

- **Performances supérieures à Tor Browser:** En l'absence du routage onion, Mullvad Browser est **nettement plus rapide et réactif** que Tor Browser pour la navigation web classique.

- **Interface familière et simplicité:** Mullvad Browser reprend l'interface de Firefox. Si vous êtes habitué à Firefox ou même à Tor Browser, vous ne serez pas dépaysé.

- **Collaboration de confiance et code audité:** Mullvad Browser bénéficie de l'expertise du Tor Project et tout le code source est disponible, ce qui permet des audits externes.

### Inconvénients

- **Pas d'anonymat réseau sans VPN:** Le point le plus important est que **Mullvad Browser ne cache pas votre adresse IP par lui-même** (comme tous les autres navigateur, sauf Tor Browser). Votre adresse IP est comme votre "adresse postale" sur Internet: elle révèle votre localisation et votre fournisseur d'accès. Il **dépend donc fortement d'un VPN** (réseau privé virtuel) pour masquer cette information cruciale.

- **Pas de version mobile:** À ce jour, Mullvad Browser n'est disponible que sur PC (Windows, Mac, Linux).

- **Incompatible avec certaines habitudes:** Le **mode privé permanent** signifie qu'on ne peut pas conserver de session d'un usage sur l'autre. Il est impossible de rester connecté à un compte web d'une session à l'autre.

- **Fonctionnalités restreintes:** Pour préserver l'uniformité du fingerprint, Mullvad Browser a **désactivé plusieurs fonctionnalités** présentes dans Firefox et n'est pas destiné à être personnalisé.

## Installation de Mullvad Browser

Mullvad Browser est disponible gratuitement pour Windows, macOS et Linux. Pour l'installer, rendez-vous sur [le site officiel de Mullvad](https://mullvad.net/browser).

![MULLVAD BROWSER](assets/fr/02.webp)

*Page d'accueil officielle de Mullvad Browser avec le bouton de téléchargement mis en évidence.*

![MULLVAD BROWSER](assets/fr/03.webp)

*Sélectionnez votre système d'exploitation sur la page de téléchargement de Mullvad Browser.*

Cliquez sur le bouton **"Télécharger"** correspondant à votre système d'exploitation.

Pour Linux, vous pouvez choisir entre différents formats selon votre distribution. Une fois le téléchargement terminé:

### Sur Windows
Exécutez le fichier `.exe` téléchargé et suivez les instructions d'installation.

### Sur macOS
Ouvrez le fichier `.dmg` téléchargé et glissez l'application Mullvad Browser dans votre dossier Applications.

### Sur Linux
Extrayez l'archive `.tar.xz` dans le répertoire de votre choix et exécutez le fichier `start-mullvad-browser.desktop`.

## Configuration et première utilisation

Lors du premier lancement de Mullvad Browser, vous verrez une interface très similaire à celle de Tor Browser. Le navigateur est préconfiguré pour la confidentialité et ne nécessite aucune modification particulière.

![MULLVAD BROWSER](assets/fr/04.webp)

*Interface d'accueil de Mullvad Browser avec les extensions, l'icône du balai pour générer une nouvelle identité et le menu de l'application en haut à droite.*

**Important:** Mullvad Browser ne masque pas votre adresse IP par défaut. Pour une protection complète, il est fortement recommandé d'utiliser un VPN en parallèle. Vous pouvez utiliser Mullvad VPN ou tout autre service VPN de confiance.

Le navigateur inclut également **DNS-over-HTTPS (DoH)** utilisant le service DNS de Mullvad: cette technologie chiffre vos requêtes DNS (traduction des noms de sites en adresses IP) pour éviter que votre fournisseur d'accès Internet ne puisse surveiller les sites que vous visitez.

### Réglages de sécurité

Vous pouvez ajuster le niveau de sécurité en cliquant sur le **menu de l'application** (trois barres horizontales) en haut à droite, puis **"Paramètres"**, puis l'onglet **"Vie privée et sécurité"**. Descendez jusqu'à la section **"Sécurité"**:

![MULLVAD BROWSER](assets/fr/05.webp)

*Choix des niveaux de sécurité: les flèches montrent le chemin depuis le menu de l'application vers l'onglet "Vie privée et sécurité" jusqu'aux options de sécurité.*

Mullvad Browser propose trois niveaux de sécurité:

- **Normal** (niveau actuel par défaut): Toutes les fonctions du navigateur et des sites Web sont activées

- **Plus sûr**: Désactive les fonctions souvent dangereuses des sites Web, ce qui pourrait entraîner une perte de fonctionnalité de certains sites Web:
	- JavaScript est désactivé pour les sites non HTTPS
	- Certaines polices et certains symboles mathématiques sont désactivés
	- Le son et la vidéo (médias HTML5) ainsi que WebGL sont "cliquer pour lire"

- **Le plus sûr**: Ne permet que les fonctions de sites Web exigées pour les sites statiques et les services de base:
	- JavaScript est désactivé par défaut pour tous les sites
	- Certaines polices, icônes, images et certains symboles mathématiques sont désactivés
	- Le son et la vidéo (médias HTML5) ainsi que WebGL sont "cliquer pour lire"

### Bouton de nouvelle session

Pour redémarrer avec une session vierge sans fermer le navigateur, cliquez sur l'icône du balai ou utilisez le menu de l'application > **"Nouvelle session"**.

![MULLVAD BROWSER](assets/fr/06.webp)

*Fonction "Réinitialiser votre identité" permettant de redémarrer le navigateur avec une session complètement vierge.*

## Utilisation au quotidien

### Navigation normale

Mullvad Browser se comporte comme un navigateur classique pour la navigation quotidienne. Tous les sites web sont accessibles normalement, avec l'avantage d'une protection renforcée contre le pistage.

### Gestion des cookies et connexions

En raison du mode privé permanent, vous devrez vous reconnecter à vos comptes à chaque nouvelle session. C'est le prix à payer pour une confidentialité maximale.

### Extensions

Mullvad Browser vous permet techniquement d'installer des extensions supplémentaires depuis le catalogue Firefox, mais **il est important de comprendre les implications**. Chaque extension ajoutée modifie votre empreinte numérique et vous distingue des autres utilisateurs Mullvad Browser, ce qui va à l'encontre du principe fondamental du navigateur: faire en sorte que tous les utilisateurs apparaissent identiques.

Comme l'explique Mullvad: *"Parfois, n'avoir aucune défense spécifique est mieux qu'en avoir une. En voulant augmenter la confidentialité en ligne, vous installez des extensions qui finalement vous rendent encore plus visible."*

Si vous choisissez d'installer des extensions malgré tout, sachez que vous créez une empreinte unique qui peut être utilisée pour vous traquer d'un site à l'autre. Pour une protection maximale, il est préférable de s'en tenir aux trois extensions préinstallées qui sont identiques pour tous les utilisateurs.

## Bonnes pratiques avec Mullvad Browser

1. **Utilisez toujours un VPN**: Mullvad Browser ne masque pas votre IP. Un VPN est essentiel pour l'anonymat complet.

2. **Ne personnalisez pas le navigateur**: Évitez de modifier les paramètres ou d'ajouter des extensions, cela pourrait vous rendre identifiable.

3. **Utilisez le bouton de nouvelle session**: Entre différentes activités, utilisez la fonction de réinitialisation pour cloisonner vos sessions.

4. **Choisissez le niveau de sécurité adapté à vos besoins**:
   - **Normal (recommandé)**: Pour la navigation quotidienne. Offre déjà une excellente protection tout en gardant les sites web fonctionnels. C'est le meilleur équilibre pour 95% des utilisateurs.
   - **Plus sûr**: Si vous visitez des sites inconnus ou potentiellement dangereux, ou pour une protection accrue sur des réseaux Wi-Fi publics. Certains sites peuvent mal fonctionner.
   - **Le plus sûr**: Réservé aux situations à haut risque (journalisme d'investigation, communication sensible, environnements hostiles). La plupart des sites modernes seront cassés, mais c'est le prix de la sécurité maximale.

5. **Vérifiez régulièrement les mises à jour**: Gardez votre navigateur à jour pour bénéficier des derniers correctifs de sécurité.

6. **Utilisez des moteurs de recherche respectueux de la vie privée**: Privilégiez DuckDuckGo, Startpage ou Searx plutôt que Google.

7. **Activez le mode HTTPS uniquement**: Dans les paramètres, assurez-vous que le mode "HTTPS uniquement" est activé pour forcer les connexions sécurisées.

8. **Ne modifiez AUCUN paramètre avancé**: Contrairement à d'autres navigateurs, Mullvad Browser est conçu pour que TOUS les utilisateurs aient exactement la même configuration. Modifier des paramètres dans `about:config` ou changer les réglages d'uBlock Origin/NoScript vous rendrait unique et défait complètement l'anonymat du navigateur.

## Configuration DNS recommandée

Mullvad Browser intègre automatiquement le DNS-over-HTTPS de Mullvad. Si vous utilisez Mullvad VPN, l'extension vous recommandera de **désactiver Mullvad DoH** car il est plus rapide d'utiliser le serveur DNS de votre serveur VPN. Si vous n'utilisez pas Mullvad VPN, gardez Mullvad DoH activé pour éviter la surveillance DNS par votre fournisseur d'accès.

## Conclusion

Mullvad Browser représente une excellente solution pour ceux qui recherchent une navigation web respectueuse de la vie privée sans les contraintes de performance du réseau Tor. Combiné à un VPN de qualité, il offre une protection robuste contre le pistage et la surveillance en ligne.

Bien qu'il présente certaines limitations (pas de version mobile, sessions non persistantes), Mullvad Browser constitue un outil précieux dans l'arsenal de quiconque souhaite reprendre le contrôle de sa vie privée numérique. Sa facilité d'utilisation et sa configuration par défaut en font un choix judicieux pour les utilisateurs soucieux de confidentialité, qu'ils soient débutants ou expérimentés.

## Ressources

### Documentation officielle
- [Site officiel Mullvad Browser](https://mullvad.net/fr/browser)
- [Page de téléchargement Mullvad Browser](https://mullvad.net/en/download/browser)
- [Spécifications techniques détaillées](https://mullvad.net/en/browser/hard-facts)
- [Extension Mullvad Browser](https://mullvad.net/en/help/mullvad-browser-extension)

### Guides et explications
- [Pourquoi la vie privée est importante](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor sans Tor: concept de Mullvad Browser](https://mullvad.net/en/browser/tor-without-tor)
- [Comment choisir un navigateur respectueux de la vie privée](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Comprendre le fingerprinting des navigateurs](https://mullvad.net/en/browser/browser-fingerprinting)

### Support et aide
- [Centre d'aide Mullvad Browser](https://mullvad.net/en/help/tag/mullvad-browser)
- [Premiers pas vers la confidentialité en ligne](https://mullvad.net/en/help/first-steps-towards-online-privacy)

### Ressources communautaires
- [Guide Mullvad Browser - Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Discussions communautaires](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)
