---
name: Start9

description: Tutoriel sur la mise en place d'un serveur privé Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Voici un tutoriel vidéo de Southern Bitcoiner, un guide vidéo qui vous montre comment configurer et utiliser un serveur personnel Start9 / StartOS, et comment faire fonctionner un nœud bitcoin


## 1️⃣ Introduction


### Qu'est-ce que Start9 ?


Start9 est une société fondée en 2020, surtout connue pour avoir développé [**StartOS**,](https://github.com/Start9Labs/start-os) un système d'exploitation basé sur Linux conçu pour les serveurs personnels. Il permet aux utilisateurs d'auto-héberger facilement une large gamme de services logiciels, tels que les nœuds Bitcoin et Lightning, les applications de messagerie ou les gestionnaires de mots de passe, tout en conservant un contrôle total sur leurs données et en éliminant la dépendance à l'égard des plates-formes technologiques centralisées. StartOS dispose d'une interface conviviale basée sur un navigateur, d'une place de marché pour l'installation de services et d'outils de protection de la vie privée intégrés tels que l'intégration de Tor et le cryptage HTTPS à l'échelle du système. Start9 fournit également des appareils matériels préchargés avec le système d'exploitation, bien que le logiciel puisse être installé sur du matériel compatible ou des machines virtuelles (VM).


### Quelles sont les options disponibles ?


Start9 propose à la fois des options de déploiement préconstruites et DIY. Le [**Server One**](https://store.start9.com/collections/servers/products/server-one) et le [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) sont des dispositifs matériels officiels dotés de composants performants : le Server One utilise un **processeur AMD Ryzen 7 5825U** avec de la RAM configurable (16GB-64GB) et du stockage (2TB-4TB NVMe SSD), tandis que le Server Pure est équipé d'un **Intel i7-10710U**, offrant également des options de RAM et de stockage configurables. Les deux comprennent **un support technique à vie** lorsqu'ils sont achetés directement auprès de Start9. Pour les utilisateurs qui préfèrent la flexibilité, StartOS peut être installé gratuitement sur une large gamme de matériel existant, y compris les ordinateurs portables, les ordinateurs de bureau, les mini-PC et les ordinateurs monocartes, ou dans des VM.


![image](assets/en/01.webp)


### Quelles sont les différences avec Umbrel ?


StartOS et Umbrel simplifient tous deux l'installation de services auto-hébergés, mais diffèrent en termes d'architecture et de fonctionnalités. Umbrel fonctionne comme une couche d'application sur les systèmes Debian/Ubuntu ou les machines virtuelles, tandis que Start9 est un système d'exploitation dédié qui nécessite une installation directe sur le matériel ou la machine virtuelle. Umbrel présente une interface soignée, inspirée de macOS, tandis que Start9 privilégie un design fonctionnel et minimal. Umbrel offre une plus grande [sélection d'applications](https://apps.umbrel.com/), tandis que le [Start9 Marketplace](https://marketplace.start9.com/) compense avec des capacités techniques avancées. Start9 simplifie l'accès aux paramètres avancés grâce à des formulaires d'interface utilisateur validés, réduisant ainsi le besoin d'interaction avec la ligne de commande. Il excelle également dans la gestion des sauvegardes avec des sauvegardes cryptées du système en un clic, une fonctionnalité qui fait défaut à Umbrel. StartOS fournit des outils de surveillance intégrés et applique le chiffrement HTTPS pour l'accès au réseau local, ce qui renforce la sécurité. Umbrel utilise HTTP non chiffré localement, bien que les deux plateformes supportent l'accès à distance sécurisé via Tor. Umbrel convient aux utilisateurs qui privilégient un riche écosystème d'applications et une interface utilisateur soignée. Start9 est un choix solide pour ceux qui apprécient la sécurité, la configurabilité, la fiabilité des sauvegardes et la gestion avancée des services sans avoir besoin d'une expertise en ligne de commande. Pour en savoir plus sur Umbrel et les différences avec Start9, visitez ce cours :


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Conditions préalables au bricolage : Spécifications minimales et recommandées


Pour une utilisation de base avec des services minimaux, les **spécifications minimales** sont : **1 cœur vCPU (2.0GHz+ boost), 4GB RAM, 64GB de stockage**, et un port Ethernet. Cela dit, je recommande d'aller bien au-delà, surtout si vous utilisez un nœud Bitcoin. Personnellement, j'ai commencé avec 1TB et j'ai rapidement manqué d'espace. Il vaut mieux viser **au moins 2 To de stockage**, ainsi qu'un **processeur quadricœur (2,5 GHz+)** et **8 Go+ de RAM**. Cela fait une énorme différence en termes de performances et de longévité. Si vous voulez aller plus loin, voici un fil de discussion communautaire à jour sur le [Matériel capable d'exécuter StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Téléchargement et flashage du micrologiciel


Pour commencer l'installation, utilisez un autre ordinateur pour visiter le [site web Start9](https://start9.com/), et naviguez jusqu'à la section documentation en cliquant sur `DOCS`. De là, accédez aux `Flashing Guides` pour trouver la version appropriée de StartOS. Deux options sont disponibles :



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Ce tutoriel couvre l'option `x86/ARM`.


La dernière version du système d'exploitation peut être téléchargée à partir de la [page de publication Github](https://github.com/Start9Labs/start-os/releases/latest). des versions [Pre-release](https://github.com/Start9Labs/start-os/releases) sont également disponibles pour les utilisateurs qui souhaitent tester les nouvelles fonctionnalités. En bas de la page, sous `Assets`, téléchargez le `x86_64` ou le `x86_64-nonfree.iso`.  L'image `x86_64-nonfree.iso` contient des logiciels non-libres (à source fermée) requis pour le Server One et la plupart des matériels DIY, en particulier pour le support des graphiques et des périphériques réseau.


Il est recommandé de vérifier l'intégrité du fichier en comparant son hash SHA256 à celui listé sur GitHub. Pour Linux, la commande `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` peut être utilisée, les autres systèmes d'exploitation étant couverts dans la documentation.


Après avoir téléchargé et vérifié l'image StartOS, il faut la flasher sur une clé USB. le logiciel `BalenaEtcher` est recommandé pour cette tâche. Il s'agit d'un outil libre et gratuit pour écrire des fichiers image de système d'exploitation sur des lecteurs USB et des cartes SD, disponible pour Windows, macOS et Linux. Téléchargez la version appropriée sur le site officiel [Balena Etcher website](https://www.balena.io/etcher/) et exécutez le programme d'installation. Connectez la clé USB ou la carte SD cible, ouvrez Balena Etcher et cliquez sur "Flash from file" pour sélectionner l'image du système d'exploitation téléchargée. Etcher détectera automatiquement les lecteurs connectés ; sélectionnez la cible correcte s'il y en a plusieurs. Cliquez sur "Flash!`" pour commencer à écrire l'image. Etcher valide automatiquement le processus d'écriture à la fin. Une fois l'écriture terminée, retirez le lecteur en toute sécurité et utilisez-le pour démarrer l'appareil.


![image](assets/en/19.webp)


## 4️⃣ Configuration initiale


Pour la configuration initiale, reportez-vous à la page Start9 [documentation](https://docs.start9.com/0.3.5.x/) sous la rubrique "MANUEL DE L'UTILISATEUR" suivie de "Prise en main - Configuration initiale".  Ce guide officiel doit être consulté pour obtenir les informations les plus récentes.


Deux options sont présentées :



- Un nouveau départ
- Options de récupération


Pour une nouvelle installation de serveur, sélectionnez "Start Fresh". Commencez par brancher le serveur à l'alimentation électrique et à un câble Ethernet. Assurez-vous que l'ordinateur utilisé pour l'installation se trouve sur le même réseau local. Retirez la clé USB récemment mise à jour de l'ordinateur et insérez-la dans le serveur.


Vous pouvez contrôler le serveur à distance à partir de n'importe quel ordinateur du même réseau. Ouvrez un navigateur web et accédez à `http://start.local`.


**Note** : Si des problèmes de connexion surviennent avec cette adresse, cela est souvent dû au fait que les réseaux domestiques ne résolvent pas les noms de domaine `.local`. Le problème peut être résolu en accédant directement au serveur via son adresse IP. L'adresse IP peut être trouvée en se connectant à l'interface d'administration du routeur (généralement à l'adresse `192.168.1.1` ou à une adresse similaire), et en localisant l'appareil dans la liste des clients DHCP ou des cartes de réseau. Ensuite, entrez l'adresse IP complète (par exemple `http://192.168.1.105`) dans le navigateur. Cela permet de contourner la résolution DNS. Si le problème persiste, consultez la [page des problèmes courants](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) ou [contactez le service d'assistance](https://start9.com/contact/)


L'écran de configuration de StartOS devrait apparaître. Cliquez sur `Start Fresh` pour commencer l'installation du nouveau serveur.


![image](assets/en/03.webp)


L'étape suivante consiste à sélectionner le lecteur de stockage où les données StartOS seront stockées.


![image](assets/en/04.webp)


Définissez un `Password` fort pour le serveur. Enregistrez-le comme le conseille Start9, puis cliquez sur `FINISH`.


![image](assets/en/05.webp)


Un écran montrera que StartOS est en train d'initialiser et de configurer le serveur. L'étape suivante est de `Télécharger l'adresse` car l'adresse `start.local` n'est utilisée que pour l'installation et ne fonctionnera plus par la suite.


![image](assets/en/06.webp)


Le fichier de configuration contient deux adresses d'accès critiques : une pour le "réseau local (LAN)" et une autre pour l'accès sécurisé via "Tor". Ces deux adresses doivent être sauvegardées dans un gestionnaire de mots de passe sécurisé. L'étape suivante consiste à "faire confiance à votre autorité de certification racine". Ouvrez un nouvel onglet de navigateur et suivez les instructions pour faire confiance à l'autorité de certification racine et vous connecter. Le certificat de l'autorité de certification racine peut également être téléchargé en cliquant sur "Télécharger le certificat" dans le fichier téléchargé.


## 5️⃣ Faites confiance à votre autorité de certification racine


Après avoir téléchargé le certificat, le système d'exploitation doit faire confiance à l'autorité de certification racine du serveur. Cliquez sur "Voir les instructions" et trouvez les directives pour le système d'exploitation spécifique.


![image](assets/en/07.webp)


Pour un système Linux, les commandes suivantes sont utilisées. Ouvrez d'abord un terminal et installez les paquets nécessaires :


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Naviguez jusqu'au répertoire où le certificat a été téléchargé, typiquement `~/Downloads` . Exécutez les commandes suivantes pour ajouter le certificat à la liste de confiance du système d'exploitation. Allez dans le répertoire des téléchargements avec `cd ~/Downloads`. Créez le répertoire requis avec `sudo mkdir -p /usr/share/ca-certificates/start9`. Copiez le fichier de certificat, en remplaçant `votre-nom-de-filtre.crt` par le nom réel du fichier, en utilisant `sudo cp "votre-nom-de-filtre.crt" /usr/share/ca-certificates/start9/`. Enregistrez le certificat de manière permanente en ajoutant son chemin à la configuration du système avec `sudo bash -c "echo 'start9/votre-nom-de-fil.crt' >> /etc/ca-certificates.conf"`. Enfin, reconstruisez le magasin de confiance avec `sudo update-ca-certificates`. Il est essentiel d'utiliser le nom de fichier réel du certificat et de vérifier tous les chemins d'accès avant d'exécuter ces commandes. Ce processus établit une confiance permanente pour les connexions HTTPS du serveur Start9.


Une installation réussie sera indiquée par une sortie indiquant `1 added`. La plupart des applications pourront alors se connecter de manière sécurisée via `https`. Si vous utilisez Firefox, une [étape finale] supplémentaire (https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff) est nécessaire. Pour Chrome ou Brave, une autre [étape finale](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) est nécessaire pour configurer le navigateur afin qu'il respecte l'autorité de certification racine. Testez la connexion en actualisant la page. Si le problème persiste, quittez et rouvrez le navigateur avant de revisiter la page.


![image](assets/en/08.webp)


## 6️⃣ Démarrer avec StartOS


Il devrait maintenant être possible de se connecter en utilisant une connexion HTTPS sécurisée. Saisissez le "mot de passe" pour accéder à l'"écran d'accueil".


![image](assets/en/09.webp)


Cet écran propose des raccourcis utiles pour commencer. La barre latérale gauche contient les principaux éléments du menu de navigation.


## 7️⃣ Système


L'onglet Systèmes de StartOS permet d'accéder aux fonctions principales du système pour gérer le serveur personnel. Il offre des outils de maintenance, de sécurité, de diagnostic et de configuration du système sans nécessiter d'expertise en ligne de commande.


La section `Sauvegardes` permet de créer des sauvegardes complètes du système, y compris les services, les configurations et les données, qui peuvent être restaurées ultérieurement. Cette fonction est essentielle pour la reprise après sinistre ou la migration vers un nouveau matériel. Les sauvegardes peuvent être stockées sur des disques externes et sont cryptées à l'aide du mot de passe principal.


La section "Gestion" de l'onglet Systèmes permet de contrôler les fonctions clés du système. Les utilisateurs peuvent vérifier et appliquer manuellement les mises à jour de StartOS, en gardant le contrôle sur le processus de mise à jour du système. Il est possible de charger des services personnalisés ou tiers non disponibles sur le marché officiel. Si le serveur n'est pas connecté via Ethernet, les paramètres Wi-Fi peuvent être configurés à partir de cette section. Les utilisateurs avancés peuvent activer l'accès SSH pour la gestion du système au niveau du terminal.


![image](assets/en/10.webp)


La section `Insights` permet de surveiller en temps réel les performances et la santé du serveur, en affichant l'utilisation du CPU, de la RAM et du disque sous forme de graphiques. Elle indique également la température du système, ce qui est utile pour les appareils comme le Raspberry Pi qui n'ont pas de système de refroidissement actif. Les mesures de temps de disponibilité et de charge moyenne aident à évaluer la stabilité du système, et des journaux en direct sont disponibles pour dépanner les problèmes de service ou de système.


La section `Support` offre un accès aux FAQs intégrées, à la documentation officielle, et aux canaux de support de la communauté. Les logs de débogage peuvent être téléchargés depuis cette section pour être partagés avec le support de Start9 pour une résolution plus rapide des problèmes.


![image](assets/en/11.webp)


## 8️⃣ Place de marché


Le `Marketplace` est utilisé pour découvrir, installer et gérer des services sur le serveur personnel. Elle donne accès à des logiciels tels que Bitcoin Core, BTCPay Server, et electrs. StartOS supporte plusieurs places de marché, y compris le registre officiel de Start9 et les registres gérés par la communauté. Ces derniers peuvent être ajoutés en cliquant sur `CHANGE` et en passant au `Community Registry`, qui donne accès à une plus large gamme de services.


![image](assets/en/12.webp)


## 9️⃣ Installation d'un nœud Bitcoin complet


L'installation d'un Bitcoin full node sur StartOS offre une souveraineté totale sur l'expérience Bitcoin. Il permet la validation des transactions et renforce la confidentialité et la sécurité en supprimant la dépendance à l'égard de services externes susceptibles d'enregistrer l'activité. Le contrôle total des transactions est acquis, ce qui permet de les diffuser directement sur le réseau. L'option par défaut est `Bitcoin Core`, qui s'intègre nativement avec StartOS et permet la connexion avec des portefeuilles comme Specter, Sparrow, ou Electrum pour une configuration d'auto-détention. Une alternative, `Bitcoin Knots`, est également disponible via le Community Registry.


Pour installer Bitcoin Core, accédez au Marché. Dans le registre par défaut, recherchez et installez le service Bitcoin Core. Après l'installation, une invite "Needs Config" apparaîtra, exigeant que les paramètres soient complétés avant que le service puisse fonctionner. Cela se produit généralement après des mises à jour ou de nouvelles installations et invite à revoir les "paramètres RPC". Procédez à la configuration par défaut et cliquez sur "Save".


![image](assets/en/13.webp)


Une fois entièrement synchronisé, votre nœud peut servir de backend privé pour des portefeuilles tels que Sparrow, ce qui permet d'améliorer la confidentialité et la validation des transactions. Cependant, pour les utilisateurs qui stockent des montants importants, il est essentiel de comprendre les compromis de sécurité de cette connexion directe. Lorsqu'un wallet se connecte directement au Bitcoin Core, il peut exposer des données sensibles, car le Bitcoin Core stocke les clés publiques (xpubs) et les soldes wallet en clair sur la machine hôte. Un système compromis pourrait permettre à un attaquant de découvrir vos avoirs et de vous cibler.


Pour atténuer ce risque et obtenir un modèle de sécurité plus robuste, vous pouvez mettre en place un Electrum Server privé. Ce serveur agit comme un intermédiaire, indexant la blockchain sans stocker d'informations spécifiques à la wallet. En connectant votre wallet à votre propre serveur Electrum au lieu de le connecter directement au Bitcoin Core, vous empêchez le wallet d'accéder aux données sensibles du nœud.


![image](assets/en/14.webp)


## 🔟 Mise en place des électeurs


`electrs` (Electrum Rust Server) est un indexeur rapide et efficace qui se connecte à votre nœud Bitcoin Core et permet aux portefeuilles compatibles Electrum d'interroger l'historique des transactions et les soldes en temps réel. En exécutant electrs sur StartOS, vous ne dépendez plus de serveurs Electrum tiers, ce qui améliore considérablement la confidentialité et la sécurité - vos requêtes wallet vont directement à votre nœud auto-hébergé.


Pour le mettre en place, installez d'abord le service electrs depuis le StartOS Marketplace. Le système aura besoin que Bitcoin Core soit complètement synchronisé avant de procéder. Après l'installation, confirmez les paramètres `Needs Config` avec les valeurs par défaut recommandées et electrs commence à indexer la blockchain, ce qui peut prendre jusqu'à un jour en fonction de votre matériel.


![image](assets/en/15.webp)


Une fois terminé, vous pouvez connecter des portefeuilles comme Sparrow ou Specter. Une connexion réussie permet à votre wallet de se synchroniser directement avec votre nœud, offrant une expérience Bitcoin sécurisée, privée et auto-hébergée.


## 1️⃣1️⃣ Connect Sparrow Wallet


Pour connecter `Sparrow Wallet` à votre nœud StartOS en utilisant l'implémentation electrs, assurez-vous d'abord que Bitcoin Core est complètement synchronisé et qu'electrs est installé et fonctionne. Ouvrez Sparrow Wallet sur votre appareil et naviguez vers `File` -> `Settings` -> `Server`. Choisissez ensuite `Privé Electrum Server`. Dans le champ URL, entrez le `Tor hostname` et le `Port` pour electrs, que vous pouvez trouver dans StartOS sous `Services` -> `electrs` -> `Properties` (se terminant typiquement par `.onion:50001`).


![image](assets/en/16.webp)


Ensuite, activez Tor en cochant `Use Proxy`, en réglant l'adresse du proxy sur `127.0.0.1` et le port sur `9050`. Cliquez sur `Test Connection` et attendez quelques instants. Une connexion réussie affichera un message de confirmation tel que "Connecté à electrs". Une fois la vérification effectuée, fermez les paramètres et procédez à la création ou à la restauration de votre wallet. Cette configuration garantit que votre wallet interroge votre propre nœud par l'intermédiaire d'electrs, ce qui assure une confidentialité totale et un fonctionnement sans confiance.


![image](assets/en/17.webp)


## 🎯 Conclusion


StartOS de Start9 est une plateforme conviviale, axée sur la protection de la vie privée, conçue pour l'auto-hébergement de services essentiels tels que les nœuds Bitcoin et Lightning, les portefeuilles et les applications personnelles. Elle élimine le besoin de compétences en ligne de commande en offrant une interface graphique propre, des sauvegardes automatisées, une surveillance de la santé et un accès Tor sécurisé, ce qui la rend idéale pour les utilisateurs non techniques. Son architecture modulaire permet une intégration transparente avec des outils comme electrs ou Sparrow, ce qui vous donne un contrôle total sur votre souveraineté financière et numérique. En mettant l'accent sur la transparence, le contrôle local et l'extensibilité, StartOS permet aux utilisateurs de se réapproprier les plateformes centralisées et de gérer leur propre infrastructure privée et résiliente.
