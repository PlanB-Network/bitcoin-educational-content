---
name: Firefox
description: Comment configurer Firefox pour protéger sa vie privée
---

![cover](assets/cover.webp)

On passe tous des heures en ligne, souvent sans se rendre compte de ce que notre navigateur révèle sur nous. Bonne nouvelle: avec quelques réglages bien choisis, **Firefox** peut devenir un compagnon discret, efficace et agréable au quotidien. Ce guide, dans l’esprit des autres tutoriels du site, vous accompagne pas à pas avec un ton simple et des conseils concrets. L’objectif n’est pas de « tout bloquer », mais de trouver **votre** équilibre entre confort et confidentialité.

- **Pas de recette universelle**: plus vous modifiez, plus vous risquez de vous démarquer (fingerprinting). Le but est de rester protégé sans sortir de la foule.
- **Allez-y par étapes**: changez un réglage, testez un ou deux sites que vous utilisez souvent, puis continuez.

## Présentation de Firefox

Firefox est un navigateur libre et open‑source (moteur Gecko), développé par Mozilla, une organisation à but non lucratif. Concrètement, cela signifie que son modèle économique n’est pas fondé sur l’exploitation de vos données. Il embarque de solides protections de confidentialité tout en restant simple à utiliser.

- **Enhanced Tracking Protection (ETP)**: bloque par défaut de nombreux traqueurs.
- **Total Cookie Protection** et **State Partitioning**: chaque site est « dans sa boîte », empêchant le suivi croisé.
- **Mode HTTPS‑only** et **DNS over HTTPS (DoH)**: limitent les fuites d’information sur le réseau.
- Code ouvert, audits indépendants, pas de modèle publicitaire.

### Déjà activé par défaut (rassurant)

- **Isolation de site (Fission)**: activée par défaut. Chaque site s’exécute dans un processus séparé, ce qui empêche un onglet malveillant d’accéder aux données d’un autre et améliore la robustesse (mitige certaines fuites inter‑sites). Vérifiez via `about:support` (rechercher « Fission »).
- **Total Cookie Protection (TCP)**: actif par défaut. Les cookies et autres stockages sont confinés au site de première partie (un « bocal » par site), ce qui neutralise le pistage intersites. Des exceptions temporaires existent via la Storage Access API quand c’est nécessaire (boutons de connexion intégrés).
- **Bounce/Redirect Tracking Protection**: Firefox détecte et nettoie automatiquement les cookies laissés par les sites de rebond (liens qui vous redirigent via un traqueur avant la destination), réduisant ce canal de pistage sans action de votre part.

## Installation de Firefox

- **Windows**: téléchargez depuis `https://www.mozilla.org` (ou Microsoft Store), puis lancez l’installeur.
- **macOS**: ouvrez le `.dmg` et glissez l’app dans Applications.
- **Linux**: installez via votre gestionnaire de paquets (apt, dnf, pacman), Flatpak (Flathub) ou Snap. Préférez les sources officielles.

Astuce rapide: après l’installation, ouvrez Aide → À propos de Firefox pour vérifier les mises à jour. Les versions récentes corrigent des failles et améliorent la vie privée.

## Configuration recommandée

On démarre par les réglages simples qui apportent un gros gain sans douleur. Si un site ne fonctionne plus comme prévu, cliquez sur le bouclier 🛡️ à gauche de la barre d’adresse pour faire une exception locale.

### Réglages de base (facile)

1) Protection contre le pistage
- Passez **ETP** en **Strict**. Vous bloquez davantage de traqueurs (cookies inter‑sites, scripts de fingerprinting, cryptomineurs, widgets sociaux…).
- Si un site casse (vidéo qui ne se lance pas, bouton de connexion récalcitrant), désactivez la protection uniquement pour ce site via le bouclier.

Pour information, voici les différents niveau ETP possible :

- **Standard** (équilibré, compatibilité maximale)
  - Bloque: traqueurs de réseaux sociaux, cookies intersites (toutes fenêtres), contenu de pistage en navigation privée, mineurs de cryptomonnaie, détecteurs d’empreinte.
  - Inclut **Total Cookie Protection** (TCP): les cookies sont confinés par site.
- **Strict** (recommandé pour la confidentialité)
  - Bloque: traqueurs de réseaux sociaux, cookies intersites (toutes fenêtres), contenu de pistage (toutes fenêtres), mineurs de cryptomonnaie, détecteurs d’empreinte connus et suspectés.
  - Peut casser certains sites; utilisez le bouclier 🛡️ pour une exception locale puis actualisez l’onglet.
- **Personnalisée** (utilisateurs avancés)
  - Choix fin de ce qui est bloqué: cookies, contenu de pistage, mineurs, fingerprinting (connu/suspect).

*Note: après tout changement de niveau, **actualisez les onglets** pour appliquer.*

2) Cookies et données de site
- Activez **« Supprimer les cookies et données des sites à la fermeture »** pour repartir proprement à chaque redémarrage.
- Ajoutez des **Exceptions** pour garder la connexion sur 2 ou 3 sites indispensables (messagerie, banque). C’est un bon compromis confort/privé.

3) HTTPS uniquement
- Activez **« Mode HTTPS uniquement dans toutes les fenêtres »**. Vous évitez les connexions non chiffrées par défaut.

4) Télémétrie et mesures publicitaires
- Dans « Collecte de données par Firefox », **décochez toutes les cases** pour ne rien envoyer à Mozilla.
- Désactivez **« Autoriser les sites à effectuer des mesures publicitaires respectueuses de la vie privée »**. L’intention est bonne, mais mieux vaut garder le navigateur neutre.
- **Safe Browsing**: il est raisonnable de **le garder activé** (vérifications locales et requêtes hachées) pour une meilleure sécurité sans coût majeur côté vie privée.

5) Saisie auto, suggestions et page d’accueil
- Désactivez l’**auto‑remplissage** (identifiants, adresses, cartes). Pratique, mais peu nécessaire si vous utilisez un gestionnaire de mots de passe.
- Dans **Recherche**, désactivez **« Afficher des suggestions de recherche »** pour éviter l’envoi de vos frappes au moteur.
- Dans **Barre d’adresse**, décochez **« Suggestions sponsorisées »** et **« Suggestions contextuelles »**.
- Dans **Accueil**, désactivez **Pocket** et le **contenu sponsorisé** pour une page d’accueil plus sobre.

6) Global Privacy Control (optionnel)
- Activez le **GPC** pour signaler votre refus de la vente/partage de données. C’est déclaratif, mais utile en complément.

7) Moteur de recherche
- Passez à **DuckDuckGo**, **Startpage**, **Qwant** ou **Brave Search** (Paramètres → Recherche). Vous gagnez en discrétion sans changer vos habitudes.

8) Navigation privée
- Utilisez les **fenêtres privées** (Ctrl/Cmd+Maj+P) pour compartimenter des sessions ponctuelles (recherche de cadeaux, compte secondaire…). Évitez de rester en « ne jamais garder l’historique » en permanence: des extensions peuvent être inactives en privé et les exceptions cookies perdent de leur intérêt.

Petit rappel bienveillant: ce niveau suffit déjà à la grande majorité des gens. N’allez plus loin que si vous en ressentez le besoin.

### Extensions recommandées (officielles et éprouvées)

- **uBlock Origin**: très léger, très efficace, « installez et oubliez ». Bloque pubs et pistage courant.
- **Privacy Badger**: apprend à bloquer ce qui vous suit d’un site à l’autre, et envoie Do Not Track/GPC.
- **Firefox Multi‑Account Containers**: séparez vos activités en onglets colorés (perso, pro, social…). Installez l’extension officielle: https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/

Rappel : limitez le nombre d’extensions. Chaque module ajoute un peu de surface d’attaque… et de « singularité » à votre navigateur.

## Compartimentage et options avancées

### DNS over HTTPS (DoH)
- Paramètres → Général → Paramètres réseau → **Activer DoH** → **Cloudflare** ou **Quad9** → **Protection maximale**.
- **Protection maximale = TRR‑only** (pas de repli sur le DNS du système). Si un réseau d’entreprise/hôtel bloque, revenez au mode **Standard** ou désactivez DoH.
- Si vous utilisez déjà un **VPN de confiance** ou vos **propres DNS**, DoH peut être redondant.
- Test: `https://www.dnsleaktest.com/` doit n’afficher que le fournisseur DoH choisi.

### Conteneurs et profils
- Avec **Multi‑Account Containers**, créez des espaces: Personnel, Travail, Finance, Réseaux sociaux, Shopping, Jetable. Installez l’extension officielle: https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/. Attribuez automatiquement certains sites à un conteneur (ex: tous les domaines Google dans « Réseaux sociaux/Google »).
- Pour un cloisonnement total, utilisez des **profils Firefox** via `about:profiles` (profil principal, profil « ultra‑sécurisé » minimaliste, profil de test). Pratique pour séparer travail/sensible/expériences sans tout casser.

### Extensions avancées (à réserver à un profil/usage dédié)
- **NoScript**: bloque JavaScript et contenus actifs par défaut. Puissant, mais demande un peu d’huile de coude pour autoriser site par site.
- **Cookie AutoDelete**: supprime les cookies d’un site dès que l’onglet est fermé (utile si Firefox reste ouvert longtemps).
- **LocalCDN**: sert localement des bibliothèques courantes au lieu de CDN externes (réduit les appels vers Google/Microsoft). Compatibilité partielle.
- **Chameleon**: randomise certains éléments de l’empreinte (User‑Agent, fuseau…). Testez avant d’adopter; trop se différencier peut… vous distinguer.

## Réglages experts (about:config) et Arkenfox

Ces réglages sont puissants et parfois « cassants ». Idéal: les tester d’abord dans un **profil séparé** pour ne pas pénaliser votre navigation principale.

### about:config (barre d’adresse → `about:config`)

Résistance au fingerprinting (mode hérité de Tor Browser):
```text
privacy.resistFingerprinting = true
```
Effets attendus: fuseau forcé en UTC, **letterboxing** (marges pour uniformiser la taille), User‑Agent/polices standardisés, restrictions Canvas/WebGL/AudioContext. Résultat: vous ressemblez davantage aux autres… au prix de petites bizarreries (heure décalée, taille des fenêtres standard, parfois un peu d’anglais qui apparaît).

Désactiver WebRTC (utile si vous utilisez un VPN):
```text
media.peerconnection.enabled = false
```
Résultat: pas de fuite d’IP via WebRTC. Inconvénient: casse les visios Web (Meet, Jitsi…).

Referer plus strict (réduit les infos envoyées aux sites tiers):
```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```
Option plus stricte (peut casser des paiements/SSO):
```text
network.http.referer.XOriginPolicy = 2
```

Limiter certaines API peu utiles côté vie privée (à adapter à vos usages):
```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```

Simple règle d’or: si quelque chose casse, revenez en arrière sur le dernier réglage modifié. Pas de panique, vous gardez le contrôle.

### Arkenfox user.js

Le projet **Arkenfox** fournit un fichier `user.js` maintenu par la communauté qui applique automatiquement des centaines de préférences Firefox orientées confidentialité et sécurité. Au redémarrage, Firefox lit ce fichier présent dans votre profil et applique ces réglages.

#### À quoi ça sert concrètement ?
- Éviter de modifier soit même les paramètres et `about:config` en partant d’une base durcie, cohérente et documentée.
- Réduire le risque d’oublier un réglage critique et gagner du temps.

#### Ce que ça change (exemples)
- Coupe la télémétrie et des services annexes de Mozilla.
- Renforce cookies/cache/référer et HTTPS‑only; cloisonne davantage.
- Active la résistance au fingerprinting (RFP) et le letterboxing.
- Désactive WebRTC par défaut (évite les fuites d’IP).
- Ajuste DoH/TLS et limite des API bavardes.
- Réduit votre « unicité » navigateur, avec quelques compromis d’usage.

#### Quand l’utiliser
- Si vous voulez un Firefox durci en 10 minutes sans tout configurer à la main.
- Si vous acceptez d’ajuster ponctuellement des exceptions (DRM/streaming, visio Web, SSO/paiements).

#### Avantages
- Rapide, cohérent, mis à jour (calé sur les versions ESR).
- Très bien documenté (wiki + commentaires dans le fichier).
- Facile à personnaliser via de petits overrides.

#### Limites / effets de bord
- Compatibilité: certains sites/applications web peuvent casser (WebRTC, RFP, referer strict…).
- Confort: fuseau en UTC, tailles de fenêtre standardisées (letterboxing), parfois un peu d’anglais.
- Ce n’est pas Tor: pas d’anonymat réseau (pensez VPN/Tor selon vos besoins).

#### Installation (idéalement sur un **profil dédié**)
1. Sauvegardez profil/favoris et listez vos sites en exception cookies.
2. Téléchargez `user.js` depuis le dépôt GitHub « arkenfox/user.js » (version ESR/stable).
3. Repérez votre dossier de profil via `about:profiles`:
   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`
4. Fermez Firefox et placez `user.js` à la racine du dossier de profil.
5. Relancez; personnalisez au besoin via `about:config` ou un fichier d’overrides.

#### Mises à jour
- Suivez les releases Arkenfox (alignées ESR), remplacez le `user.js`, puis relancez Firefox.
- Lisez les notes de version: certaines préférences peuvent évoluer.

#### Overrides utiles (exemples)
```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio Web nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```

#### Bonnes pratiques
- Utilisez un **profil séparé** « Arkenfox » et gardez un profil « normal » pour le confort.
- Minimisez les extensions (uBlock Origin OK) pour limiter la surface d’attaque et l’unicité.

## Bonnes pratiques au quotidien

- **Mises à jour**: Firefox et extensions à jour = moins de failles.
- **Extensions raisonnables**: privilégiez des modules connus; méfiez‑vous des rachats « douteux ».
- **Mots de passe**: privilégiez un gestionnaire dédié (Bitwarden, KeePassXC); évitez de stocker vos mots de passe dans le navigateur; **activez la 2FA**.
- **Hygiène de navigation**: isolez réseaux sociaux/Google dans des conteneurs, faites des pauses (fermez/reouvrez) pour « réinitialiser » le contexte.
- **Mobile**: sur **Android**, Firefox + uBlock Origin offre une protection similaire en mobilité.

## Limites et alternatives

- Un navigateur durci ne veut pas dire anonymat réseau: sans **VPN**, votre IP reste visible. Même avec, la **corrélation** reste possible.
- Trop modifier peut vous rendre **unique**. RFP standardise; Chameleon randomise. Testez, comparez, tranchez selon vos besoins.
- Plus c’est strict, plus certains sites cassent. Utilisez des **exceptions ciblées** ou un **profil séparé** pour les usages sensibles.

Compléments utiles:
- **Tor Browser**: anonymat réseau via Tor; empreinte uniformisée; plus lent et parfois bloqué.
- **Mullvad Browser**: « Tor sans Tor », à combiner avec un VPN; empreinte standardisée; performances proches d’un navigateur classique.
- Combinaison simple: Firefox (niveau modéré) + VPN au quotidien; Tor/Mullvad pour le sensible; profils séparés pour compartimenter.

## Conclusion

Si vous avez lu jusqu’ici, bravo: vous avez déjà accompli 80% du chemin. Avec quelques bascules et bonnes habitudes, **Firefox devient un allié discret**: pistage publicitaire largement freiné, cookies compartimentés, fuites WebRTC/DNS évitées, télémétrie coupée, surface d’attaque réduite… sans sacrifier le confort. Continuez à ajuster par petites touches, testez de temps en temps, et souvenez‑vous: la confidentialité est un **processus**, pas un interrupteur.

## Ressources

Documentation Mozilla
- Enhanced Tracking Protection: `https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop`
- State Partitioning: `https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning`
- MDN Web Security: `https://developer.mozilla.org/docs/Web/Security`

Arkenfox
- Wiki et guide d’installation: `https://github.com/arkenfox/user.js/wiki`
- Dépôt et releases: `https://github.com/arkenfox/user.js`

Guides et communautés
- PrivacyGuides (navigateurs desktop): `https://www.privacyguides.org/en/desktop-browsers/`
- r/firefox, r/privacy, forum PrivacyGuides

Outils de test
- Cover Your Tracks (EFF): `https://coveryourtracks.eff.org/`
- DNS Leak Test: `https://www.dnsleaktest.com/`
- BrowserLeaks: `https://browserleaks.com/`
- BadSSL: `https://badssl.com/`
- CreepJS: `https://abrahamjuliot.github.io/creepjs/`
- 1.1.1.1/help: `https://1.1.1.1/help`
