---
name: Bitchat
description: Messagerie décentralisée, sans Internet, pour une communication libre
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Ce tutoriel vidéo de BTC Sessions vous guide dans la mise en place et l'utilisation de Bitchat!*


Bitchat est né d'un effort de prototypage rapide où [@jack](https://primal.net/jack) a développé le concept initial au cours d'une session de codage d'un week-end. [@calle](https://primal.net/calle) a rejoint le projet peu de temps après pour co-développer l'implémentation Android. Jack dirige actuellement le développement de la version iOS, tandis que Calle supervise la version Android avec le soutien de nombreux autres contributeurs.


## Introduction : Discuter librement, sans la grille


Imaginez que vous puissiez envoyer des messages lorsque l'internet tombe en panne, lors d'une catastrophe naturelle ou dans des endroits où la communication est restreinte. Bitchat rend cela possible. Il s'agit d'une application de messagerie décentralisée, de pair à pair, qui évite les serveurs centraux et permet aux appareils de communiquer directement entre eux, entièrement hors ligne, grâce à la technologie Bluetooth et au réseau maillé. Conçue dans un souci de confidentialité et de résilience, Bitchat est idéale pour les zones où la connectivité traditionnelle n'est pas fiable ou disponible, par exemple en cas de catastrophe, dans les endroits isolés ou pour les personnes qui cherchent à éviter la surveillance. Bitchat utilise la cryptographie pour garantir que chaque message est crypté de bout en bout, vérifié et infalsifiable.


Dans ce tutoriel, nous verrons comment fonctionne Bitchat et comment vous pouvez l'utiliser pour une communication vraiment privée, prête à être mise hors ligne.


## 🚀 Caractéristiques principales


Bitchat permet d'envoyer des messages hors ligne grâce à ces [fonctionnalités](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features) :



- Compatible multiplateforme** : Compatibilité totale des protocoles entre iOS et Android.
- Réseau maillé décentralisé** : Découverte automatique des pairs et relais de messages multi-sauts par Bluetooth Low Energy (BLE)
- Chiffrement de bout en bout** : Échange de clés X25519 + AES-256-GCM pour les messages privés
- Chats basés sur les canaux** : Messagerie de groupe basée sur des sujets avec protection optionnelle par mot de passe
- Stockage et transfert** : Les messages sont mis en cache pour les pairs hors ligne et délivrés lorsqu'ils se reconnectent
- Le respect de la vie privée d'abord** : Pas de comptes, pas de numéros de téléphone, pas d'identifiants persistants
- Commandes de type IRC : Interface familière du style `/join, /msg, /who`.
- Conservation des messages** : Sauvegarde facultative des messages à l'échelle du canal, contrôlée par les propriétaires du canal
- Effacement d'urgence** : Appuyez trois fois sur le logo pour effacer instantanément toutes les données
- Interface utilisateur Android moderne** : Jetpack Compose avec Material Design 3
- Thèmes sombres/clairs** : Esthétique inspirée des terminaux correspondant à la version iOS
- Optimisation de la batterie** : Analyse adaptative et gestion de l'énergie


## 1️⃣ Comment fonctionne Bitchat - simplement


Bitchat vous permet d'envoyer des messages à des téléphones proches directement par Bluetooth (`BLE` comme suit), sans avoir besoin d'Internet ou d'un signal cellulaire. Lorsque vous commencez une conversation, les téléphones effectuent un échange sécurisé afin de créer une clé de cryptage unique et temporaire pour votre conversation. Chaque message est protégé par un chiffrement de bout en bout, et une nouvelle clé est utilisée pour chacun d'entre eux afin de garantir la sécurité des messages passés, même si votre téléphone est compromis ultérieurement. Enfin, l'application divise les messages en petits morceaux et les mélange avec des données fictives aléatoires pour dissimuler votre activité de messagerie. Pour les conversations directes d'appareil à appareil, l'application ne fonctionne que dans un rayon d'environ 100 mètres. C'est comme passer des notes chiffrées dans une pièce bondée : les appareils chuchotent directement entre eux, détruisant les clés après chaque message.


Bitchat vous permet également de rejoindre des salons de discussion géolocalisés à l'aide du protocole Nostr et de `#geohash`. Un geohash est un code court, comme `#u33d`, qui représente une zone géographique spécifique, allant d'un simple quartier à une ville ou une région entière. Vous pouvez vous téléporter dans n'importe quel salon de discussion geohash dans le monde en entrant simplement son tag. Vos messages sont envoyés par l'intermédiaire d'un réseau décentralisé de relais, qui protège votre position exacte. De plus, chaque fois que vous rejoignez un salon geohash, vous recevez une nouvelle identité temporaire, ce qui ajoute une couche supplémentaire de confidentialité à vos conversations basées sur la localisation.


Pour plus de détails techniques, veuillez consulter le [livre blanc officiel](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Installation et configuration


### Où se procurer Bitchat


Vous pouvez installer Bitchat via :



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (pour les appareils iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (pour les appareils Android)


Les utilisateurs d'Android disposent également d'autres options :



- Télécharger l'APK directement depuis la page [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) ou
- Installation via le [Zapstore] compatible Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Note** : ce tutoriel se concentre principalement sur l'implémentation Android. La version iOS peut être différente


### Processus d'installation


Après l'installation, ouvrez Bitchat pour voir cet écran de permissions initiales. Voici ce que vous devez faire :


1. **Grant these required permissions:**


   - Accès Bluetooth** (pour découvrir les utilisateurs de Bitchat à proximité)
   - Localisation précise** (Android l'exige pour la fonctionnalité Bluetooth)
   - Notifications** (pour recevoir des messages privés)

2. **Désactiver l'optimisation de la batterie** :


   - Cela permet à Bitchat de fonctionner en arrière-plan
   - Maintient en permanence les connexions du réseau maillé


Tapez sur `Grant Permissions`, suivez les `prompts` et `Disable Battery Optimization` pour passer à l'écran suivant.


![image](assets/en/02.webp)


Bienvenue sur l'écran principal de Bitchat. Orientons-nous un peu :


### Paramètres


Tout d'abord, il faut savoir que le menu des paramètres s'ouvre en tapant sur le logo Bitchat. Le menu des paramètres peut être ouvert en appuyant sur le logo Bitchat.  Les options suivantes sont disponibles :



- Définir l'"apparence" (système/lumière/obscurité).
- activer `Proof of work` pour geohash pour la dissuasion du spam (optionnel)
- Activez `Tor` pour améliorer la confidentialité.


![image](assets/en/16.webp)


### Définir son identité


Touchez le champ `bitchat/anonXXXX` en haut pour choisir votre nom d'utilisateur. C'est ainsi que les autres vous verront en mode Bluetooth et en mode Internet. Par exemple, vous pouvez remplacer "anon2022" par un nom d'utilisateur de votre choix.


![image](assets/en/03.webp)


### Sélectionner les chaînes du réseau


Utilisez le menu `#location channels` (à droite du nom d'utilisateur) pour passer d'un type de connexion à l'autre :



- BLE Mesh*** : Mode Bluetooth par défaut (pas d'internet, portée de 10 à 50 mètres)
- #geohashes** : Communautés géographiques basées sur l'Internet utilisant le [protocole Nostr](https://nostr.com/)


Lorsque vous sélectionnez le mode `#geohashes`, Bitchat s'intègre au protocole Nostr pour permettre la création de communautés géographiques. Vos messages sont publiés sur des "relais Nostr décentralisés" plutôt que sur le réseau peer-to-peer de Bitchat, ce qui permet des conversations plus larges mais filtrées en fonction de la localisation. Les clés d'identité Bitchat signent cryptographiquement tous les événements Nostr pour maintenir l'authentification, tandis que les balises geohash (comme `#u4pruyd` pour un quartier) filtrent les messages selon le niveau de précision que vous avez choisi. Cela signifie que vous pouvez participer à des discussions locales sans révéler vos coordonnées exactes, bien qu'un accès à Internet soit nécessaire.


![image](assets/en/04.webp)


### Surveiller les pairs

licence : CC-BY-SA-V4

Le compteur de pairs indique les utilisateurs :



- À proximité (BLE Mesh) ou
- Dans votre zone geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Global Chat & Private Messages


Bitchat propose deux modes de communication distincts pour répondre à des besoins différents :



- Canaux publics:** Pour des conversations ouvertes avec d'autres personnes. Vous pouvez vous connecter soit via le réseau local BLE pour les utilisateurs proches, soit via un #geohash global pour les communautés géolocalisées et connectées à Internet.
- Messages privés:** Pour des conversations sécurisées en tête-à-tête. Ils établissent une connexion directe et cryptée pour préserver la confidentialité de vos échanges.


La compréhension de ces deux modes vous aidera à vous orienter dans vos conversations.


### Canaux publics : Le centre communautaire


Le menu `#location channels` (en haut à droite) contrôle votre visibilité publique. En sélectionnant `mesh`, vous vous connectez à tous les utilisateurs proches via le réseau BLE, généralement des appareils situés dans un rayon de 10 à 50 mètres. Cela crée un forum ouvert où les messages sont diffusés à tous ceux qui sont à portée, ce qui est idéal pour les annonces d'événements ou les alertes locales.


Pour une plus grande portée géographique, choisissez n'importe quelle balise `#geohash` pour rejoindre des communautés Internet filtrées par emplacement. Ces canaux utilisent les relais du protocole Nostr, ce qui permet de communiquer d'une ville ou d'une région à l'autre tout en conservant la pertinence de la localisation. Vos messages apparaissent en direct aux autres membres du même canal, et les nouveaux participants voient automatiquement l'historique des messages récents lorsqu'ils rejoignent le canal.


![image](assets/en/06.webp)


### Conversations privées : Sécurisées et cryptées


Pour démarrer une conversation privée, tapez directement sur n'importe quel "nom d'utilisateur" affiché dans "Vue d'ensemble des pairs". Vous pouvez également taper sur l'"icône d'étoile" pour marquer cet utilisateur comme favori, ce qui le gardera visible dans votre liste de contacts même s'il n'est pas en ligne.


![image](assets/en/07.webp)


Bitchat initie automatiquement sa "poignée de main de sécurité" lorsque vous commencez une conversation privée. Les appareils échangent des clés éphémères pour créer un tunnel crypté spécifique à votre conversation. Ce processus garantit que tous vos messages et fichiers partagés restent confidentiels grâce à un cryptage continu de bout en bout. Les messages privés permettent le partage de textes et de fichiers.


![image](assets/en/08.webp)


## 4️⃣ Caractéristiques supplémentaires


Vous pouvez accéder au panneau d'actions instantanément en tapant `/` n'importe où dans Bitchat. Ceci révèle un menu de commandes pour des actions rapides.



- Gérer les connexions** : `Bloquer les utilisateurs` ou `Débloquer les pairs`
- Contrôles des canaux** : `Afficher les canaux` ou `Joindre/créer un canal`
- Interactions sociales** : `Envoyer une accolade chaleureuse` ou `gifler avec une truite` 🎣
- Maintenance du chat** : `Effacer les messages du chat`
- Outils de confidentialité** : `Voir qui est en ligne` ou `Envoyer un message privé`


Les commandes s'exécutent immédiatement - comme `/block Satoshi` pour faire taire les critiques ou `/hug Hal` pour répandre la positivité 🫂.


![image](assets/en/09.webp)


## 5️⃣ Créer un canal


Les canaux dans Bitchat permettent une communication organisée autour de sujets, de lieux ou de communautés. Pour créer votre propre canal, suivez ce processus :


### Étape 1 : Créer un canal


Pour créer un canal, tapez `/j` ou `/join` suivi du `nom du canal` dans n'importe quel chat (par exemple `/j <nom du canal>`). Après la création, une nouvelle `icône ⧉` apparaît pour indiquer le nouveau canal. D'autres utilisateurs peuvent le rejoindre en tapant la même commande (par exemple `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Étape 2 : Configuration des paramètres


Outre les commandes par défaut, les paramètres suivants sont disponibles au sein d'un canal :



- `/save` pour sauvegarder les messages localement
- `/transfer` pour transférer la propriété d'un canal et
- `/pass` pour changer le mot de passe de la chaîne.


Pour les communautés privées, cette commande active la protection par mot de passe, obligeant les membres approuvés à saisir un mot de passe personnalisé avant d'adhérer à la communauté.


## 6️⃣ Mode panique


Parlons maintenant du "mode panique" : en tapant trois fois sur le logo "Bitchat", vous effacez tous les messages et toutes les données de l'application. Il s'agit de la protection ultime de votre vie privée, parfaite pour les situations nécessitant une discrétion immédiate.


**Rappel important:** _Le mode panique est permanent. Une fois activé, les données ne peuvent pas être récupérées. A utiliser avec précaution


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Les canaux Geohash permettent des conversations ciblées basées sur des "lieux géographiques" plutôt que sur des connexions réseau traditionnelles. Cette fonctionnalité transforme bitchat en un outil de communication sensible à la localisation, idéal pour la coordination locale, la création de communautés et les discussions spécifiques à un lieu.


### Comment fonctionnent les `#geohashes` ?


Le système divise le monde en carrés de grille en utilisant le [système Geohash](https://en.wikipedia.org/wiki/Geohash), où chaque caractère dans le hachage représente une plus grande précision :



- Niveau 4** (par exemple, `u33d`) : Couvre environ 25 km × 25 km - idéal pour les discussions à l'échelle d'une ville
- Niveau 6** (par exemple, `u33d8z`) : Couvre environ 1,2 km × 1,2 km - précision de voisinage
- Niveau 8** (par exemple, `u33d8z1k`) : Couvre environ 150 m × 150 m - précision du segment de rue


La sélection de précision permet de concilier confidentialité et utilité : des niveaux plus élevés créent des zones plus exclusives mais révèlent votre position avec plus de précision.


### Rejoindre les canaux `#geohash


1. Accédez au menu `#chaînes de localisation`.

2. Sélectionnez le niveau de précision souhaité et entrez le `#geohash` (par exemple #u33d)

3. Touchez le bouton `Teleport` pour rejoindre le canal `#location`.


![image](assets/en/12.webp)


Vous pouvez également appuyer sur l'"icône de carte" pour utiliser la vue cartographique afin de déterminer le niveau de précision et appuyer sur "sélectionner" pour rejoindre le "canal de localisation".


![image](assets/en/13.webp)


**Rappel important** : la fonctionnalité _#geohash nécessite une connexion internet active - contrairement à BLE mesh qui fonctionne hors ligne via Bluetooth


## 8️⃣ Cartes thermiques


Les cartes thermiques sont un moyen intéressant de découvrir les événements et les canaux Bitchat dans le monde entier. [Bitmap](https://bitmap.lat/) visualise et suit les messages anonymes et géolocalisés sur le réseau Nostr, en affichant les événements Nostr éphémères. Jetez-y un coup d'œil et rejoignez les canaux et chats spécifiques à votre localisation.


![image](assets/en/15.webp)


## 🎯 Conclusion


Bitchat permet une communication sécurisée et décentralisée pour les scénarios où la messagerie traditionnelle échoue. Elle peut fonctionner sans infrastructure internet grâce à un réseau maillé BLE, ce qui la rend adaptée aux manifestations, aux zones sinistrées et aux régions éloignées où la connectivité est limitée ou censurée. L'application garantit la confidentialité grâce au cryptage par clé éphémère, aux canaux de localisation basés sur la géohash et à l'effacement des données en mode panique.


L'application en est encore à ses premiers stades de développement, mais elle est déjà prometteuse. Les utilisateurs doivent s'attendre à des bugs occasionnels et signaler les problèmes via [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Des améliorations sont prévues, notamment l'intégration de `ecash` pour les transactions privées in-app utilisant le protocole Cashu.


![image](assets/en/14.webp)


## 📚 Bitchat Resources


[Github](https://github.com/permissionlesstech) | [Site web ](https://bitchat.free/)| [Livre blanc](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)