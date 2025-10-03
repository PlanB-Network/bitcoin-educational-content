---
name: Nmap
description: Maîtrisez Nmap pour la cartographie réseau et le scan de vulnérabilités
---

![cover](assets/cover.webp)

*Ce tutoriel est basé sur le contenu original de Mickael Dorigny publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont été apportées au texte original.*

___

Bienvenue dans ce tutoriel d'introduction à Nmap conçu pour toute personne souhaitant maîtriser cet outil puissant de scan de réseau. L’objectif est de vous fournir les connaissances fondamentales nécessaires pour utiliser efficacement Nmap au quotidien.

Nmap est un outil polyvalent, largement utilisé par les professionnels de l’informatique, du réseau et de la cybersécurité pour le diagnostic, la découverte de réseau et l'audit de sécurité. Ce tutoriel s'adresse à ceux qui découvrent ces domaines et souhaitent apprendre les bases de Nmap. Une connaissance élémentaire en administration système et en réseau est recommandée.

Vous découvrirez les bases de Nmap, comment effectuer des balayages de ports, identifier les hôtes actifs sur un réseau, détecter les versions de services et les systèmes d'exploitation, réaliser des scans de vulnérabilités, et bien plus encore. Chaque section comprend des explications détaillées et des exemples pratiques pour vous aider à maîtriser l’utilisation de Nmap dans divers contextes.

À l’issue de ce tutoriel, vous aurez acquis une solide compréhension de Nmap et serez en mesure de l’utiliser efficacement pour améliorer la sécurité et la gestion de vos réseaux. Bonne lecture.

## 1 - Introduction à Nmap : Qu’est-ce que Nmap ?

### I. Présentation

Dans cette première section, nous allons évoquer les grandes lignes de l’outil de scan réseau Nmap. Nous verrons quels sont les éléments clés à connaître sur cet outil et son fonctionnement général. Cela nous permettra de mieux appréhender la suite du tutoriel.

### II. Présentation de l'outil Nmap

Nmap, pour _Network Mapper_, est un outil gratuit et open source utilisé pour la **découverte et la cartographie d’un réseau ainsi que l’audit de sécurité**. Il peut aussi être utilisé pour d’autres tâches comme **l’inventaire réseau, le diagnostic ou la supervision**.

Il permet de déterminer si les hôtes d’un réseau ciblé sont actifs et joignables, quels services réseau sont exposés, quelles versions et technologies sont utilisées, ainsi que d’autres informations utiles à l’analyse. Nmap peut être utilisé pour scanner un seul service sur une machine précise ou bien sur de larges pans de réseau, jusqu’à Internet tout entier.

Les points forts de Nmap sont nombreux :

- **Puissance et flexibilité** : Nmap permet de scanner des réseaux de grande taille et d'utiliser des techniques avancées de détection. Il supporte UDP, TCP, ICMP, IPv4 et IPv6, et peut effectuer des détections de versions, des analyses de vulnérabilités ou des interactions spécifiques selon le protocole. Son architecture est modulable, notamment grâce aux scripts NSE (Nmap Scripting Engine), que nous verrons plus loin dans ce tutoriel.
- **Facilité d’utilisation** : la documentation officielle est abondante et de qualité. De nombreuses ressources communautaires existent également pour accompagner la prise en main.
- **Popularité et longévité** : Nmap est une référence dans son domaine depuis 1998. La version actuelle, à l'heure de cette mise à jour, est la 7.95. Bien que d’autres outils existent pour certaines tâches spécifiques, Nmap reste un incontournable pour la cartographie réseau et l’analyse.

**Nmap au cinéma**

Nmap est l’un des rares outils de sécurité à avoir acquis une certaine notoriété grand public. Il apparaît notamment dans le film _Matrix Reloaded_, dans une scène emblématique où Trinity l’utilise pour pirater un système :

![nmap-image](assets/fr/01.webp)

_Scène de Matrix : Reloaded faisant apparaître Nmap._

On le retrouve également dans d’autres œuvres cinématographiques.

**Retour d’expérience**

En tant qu’administrateur système puis auditeur en cybersécurité et pentester, **j’utilise Nmap presque quotidiennement** et je **le recommande régulièrement** aux administrateurs système souhaitant renforcer leur maîtrise des réseaux et améliorer leur capacité de diagnostic.

### III. Fonctionnement haut niveau

Nmap est disponible sur Linux, Windows et macOS. Il est principalement écrit en C, C++ et Lua (pour les scripts NSE). Il s’utilise principalement en ligne de commande, bien qu’il existe des interfaces graphiques comme Zenmap. Toutefois, il est vivement conseillé de débuter par la ligne de commande afin de mieux comprendre son fonctionnement.

Exemple simple :

```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```

Cette commande sera expliquée en détail plus loin. Dans ce tutoriel, nous utiliserons Nmap sous Linux, mais les usages sont similaires sur les autres systèmes. Sous Windows, Nmap s’appuie sur la bibliothèque **Npcap** (remplaçante de WinPcap, désormais obsolète) pour capturer et injecter les paquets réseau.

Nmap s’utilise comme un binaire classique, tel que `ls` ou `ip`. Certaines fonctionnalités avancées peuvent nécessiter des droits élevés, car l’outil manipule parfois les paquets d'une manière non conventionnelle afin de provoquer des réactions spécifiques sur les systèmes cibles (notamment pour la détection de services ou de failles).

### IV. Impacts de l’utilisation de Nmap

Avant d’utiliser Nmap, il est essentiel d’être conscient de ses impacts potentiels sur les réseaux et systèmes :

- Il peut envoyer **des milliers voire des millions de paquets** en peu de temps, ce qui peut saturer certaines infrastructures réseau.
- Il peut générer **des paquets malformés ou non conformes aux standards**, susceptibles de perturber certains équipements (notamment les systèmes industriels).
- Il peut produire **des comportements similaires à ceux d’une attaque**, ce qui peut déclencher des alertes dans les systèmes de sécurité (pare-feu, IDS/IPS, etc.).

De manière générale, **l’utilisation de Nmap est très bavarde**, car l’outil génère beaucoup de trafic pour extraire un maximum d’informations. Il est donc recommandé de bien comprendre son fonctionnement avant de l’utiliser sur des environnements sensibles ou de production.

### V. Conclusion

Cette section nous a permis d’introduire Nmap et ses principales caractéristiques. Nous avons vu qu’il s’agit d’un outil de cartographie réseau incontournable, puissant et flexible. Nous avons également abordé son mode de fonctionnement et les précautions nécessaires à son utilisation, afin de préparer le terrain pour les parties suivantes du tutoriel.

## 2 - Pourquoi utiliser Nmap ?

### I. Présentation

Dans cette section, nous allons passer en revue les principaux usages qui peuvent être faits de l’outil de scan réseau Nmap. Nous verrons qu’il s’agit d’un outil très utilisé dans de nombreux contextes et métiers, et que l’avoir dans sa boîte à outils en sachant le maîtriser est à coup sûr une compétence utile.

### II. Utiliser Nmap pour le diagnostic et la supervision

Nmap peut être utilisé dans le cadre du diagnostic réseau et plus largement de la supervision. Au même titre qu’un ping permet de statuer sur la communication entre deux hôtes, Nmap permet très rapidement de savoir si un hôte est actif ou si un service précis est opérationnel. Nous pouvons grâce à [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") obtenir des données précises concernant le temps de réponse d’un hôte, la route empruntée par les paquets, la réponse faite par un service spécifique, etc.

La commande et le résultat suivant permettent, par exemple, de savoir rapidement si un serveur web sur l’hôte **192.168.1.18** est actif et répond correctement :

```
nmap --open -p 80 192.168.1.18
```

![nmap-image](assets/fr/02.webp)

*Utilisation de Nmap pour récupérer l’état du service web sur un serveur distant.*

Ainsi, l’utilisation de Nmap permet d’aller plus loin que le fameux “ping test” lors des phases de débogage ou de diagnostic. Nous verrons plus loin qu’il existe plusieurs méthodes utilisées par Nmap pour identifier quel service est en écoute sur un port donné, et notamment sa version.

### III. Utiliser Nmap pour la cartographie du réseau

En tant que _Network Mapper_, la cartographie du réseau est l’objectif principal de cet outil. Il peut être utilisé au sein d’un réseau local ou de multiples réseaux, sous-réseaux et VLAN afin de dresser une liste des hôtes et des services joignables. Nmap permet de réaliser cette tâche bien plus rapidement et efficacement que n’importe quelle méthode manuelle.

La commande suivante permet, par exemple, d’identifier rapidement les hôtes actifs sur le réseau **192.168.1.0/24** :

```
nmap -sn 192.168.1.0/24
```

*Remarque : l’option `-sP` est obsolète et a été remplacée par `-sn`.*

![nmap-image](assets/fr/03.webp)

*Utilisation de Nmap pour découvrir les hôtes joignables d’un réseau.*

Nous verrons plus loin qu’il existe plusieurs méthodes utilisées par Nmap pour déterminer si un hôte peut être considéré comme “actif”, même s’il n’expose a priori aucun service.

### IV. Utiliser Nmap pour évaluer une politique de filtrage

Nmap présente l’avantage d’être factuel : ses résultats permettent d’établir des constats concrets, contrairement à n’importe quel document d’architecture ou politique de filtrage. C’est un outil clé pour évaluer concrètement l’efficacité du cloisonnement du système d’information, car il permet de **vérifier si la politique de filtrage est effectivement appliquée**.

Dans un réseau d’entreprise, les bonnes pratiques imposent une segmentation des systèmes selon leur rôle, criticité ou localisation. Des règles de filtrage (souvent mises en œuvre via des pare-feu) doivent restreindre les communications entre zones. Mais ces configurations sont souvent complexes et sujettes à erreurs.

Ainsi, pour valider que la politique est bien respectée, rien ne vaut un test concret. Par exemple, on peut vérifier que des services d’administration sensibles (SSH, WinRM, MSSQL, MySQL, etc.) ne sont pas accessibles depuis une zone utilisateur.

L’utilisation de **Nmap pour tester la politique de filtrage** devrait être systématique avant la mise en production d’une telle politique. Malheureusement, cette vérification est souvent négligée.

D’après mon expérience, de nombreuses erreurs de configuration passent inaperçues en l’absence de tests de validation. Une simple erreur dans une plage IP ou un oubli de règle peut rendre vulnérable une zone censée être isolée.

### V. Utiliser Nmap pour l’audit de sécurité et tests d'intrusion

Nmap possède **de nombreuses fonctionnalités utiles à l’évaluation de la sécurité**, aux tests d’intrusion (pentests), et malheureusement aussi aux attaquants.

Les fonctions de découverte réseau sont cruciales pour un attaquant, qui doit comprendre la topologie du réseau après une compromission initiale. Mais Nmap offre bien plus que cela : il intègre un moteur de scripts, dont **beaucoup sont dédiés à la détection de vulnérabilités**.

Par exemple, cette commande permet de vérifier si un service FTP permet une connexion anonyme, sans avoir à se connecter manuellement :

```
nmap --script ftp-anon -p 21 192.168.1.18
```

![nmap-image](assets/fr/04.webp)

*Utilisation d’un script NSE pour vérifier la présence d’une authentification anonyme FTP via Nmap.*

Ainsi, la détection de vulnérabilités via Nmap fait partie des premières étapes dans un audit ou un test d’intrusion. Elle permet d’identifier rapidement certains points faibles et d’optimiser les efforts d’analyse.

Mais attention : **les outils de scan de vulnérabilités ont leurs limites**. Nmap ne couvre qu’une partie des menaces et ne garantit pas qu’un système est sûr si aucun problème n’est détecté. Il est donc essentiel de **comprendre le fonctionnement des scripts utilisés** et de ne pas se reposer uniquement sur leur verdict.

### VI. Conclusion

Nous avons vu que maîtriser Nmap permet de couvrir un large éventail de cas d’usage, du diagnostic à la supervision, en passant par la cartographie, l’évaluation de politiques de sécurité et la recherche de vulnérabilités. Dans la section suivante, nous allons passer à la pratique et installer Nmap.


## 3 - Installation et configuration de Nmap

### I. Présentation

Dans cette section, nous allons apprendre à installer l’outil de scan réseau Nmap sur les OS Linux et Windows. Nous aurons à la fin de cette section tout ce qu’il faut pour commencer à utiliser Nmap pour les prochains modules. Enfin, nous verrons quels privilèges il peut demander lors de son utilisation et pourquoi.

### II. Installation de Nmap sous Linux

Nmap a été initialement créé pour fonctionner sur les systèmes d’exploitation GNU/Linux. Ainsi, et grâce à sa grande longévité et popularité, vous le trouverez dans tous les dépôts officiels des grandes distributions Unix. Dans ce tutoriel, j’utiliserai un système d’exploitation [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"), basé sur Debian. Mais vous pourrez l’utiliser exactement de la même manière depuis une Debian classique, un CentOS, Red Hat, ou autre !

Sous Debian, pour vérifier que Nmap est bien présent dans vos dépôts actuels, vous pouvez utiliser la commande suivante :

```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
  The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```

La réponse ici indique clairement que le paquet “nmap” existe dans les dépôts (ici, ceux de Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Dès lors, vous pourrez installer Nmap via les commandes d’installation habituelles, rien de désarmant pour le moment 🙂 :

```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```

Pour vérifier que Nmap est bien installé, nous allons afficher sa version :

```
nmap --version
```

Voici le résultat attendu :

![nmap-image](assets/fr/05.webp)

_Résultat de l’affichage de la version actuelle de Nmap._

On peut noter la présence dans cet affichage de la librairie “libpcap” (_Packet Capture Library_) et de sa version. Également exploitée par Wireshark, “libpcap” est utilisée par Nmap pour la création, la manipulation des paquets et l’écoute du trafic réseau.

### III. Installation de Nmap sous Windows

Pour une installation sur un système d’exploitation Windows, il faut commencer par télécharger le binaire depuis le site officiel (et aucun autre !) :

- Page de téléchargement de Nmap sur le site officiel : [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)
    

Il faudra alors télécharger le binaire nommé `nmap-<VERSION>-setup.exe` :

![nmap-image](assets/fr/06.webp)

_Page de téléchargement du binaire d’installation Nmap pour Windows._

Une fois ce binaire présent sur votre système, il vous suffit de l’exécuter pour procéder à l’installation de Nmap. Il s’agit d’une installation tout ce qu’il y a de plus classique, vous pouvez laisser l’ensemble des options par défaut.

J’ai pour réflexe de décocher la case “zenmap (GUI Frontend)”, il s’agit d’une interface graphique pour Nmap que je n’utilise pas et qui ne sera pas couverte dans ce tutoriel, mais libre à vous de tenter l’expérience une fois que vous maîtriserez l’outil Nmap en ligne de commande !

![nmap-image](assets/fr/07.webp)

_Désélection optionnelle de Zenmap lors de l’installation de Nmap sous Windows._

À la fin de l’installation de Nmap, vous aurez une seconde installation de proposée : celle de la librairie “Npcap” :

![nmap-image](assets/fr/08.webp)

_Installation de la librairie “Npcap” lors de l’installation de Nmap sous Windows._

Il s’agit de la librairie sur laquelle se repose Nmap pour gérer les communications réseau, c’est-à-dire la construction, l’envoi et la réception de paquet réseau. Vous avez forcément déjà croisé cette librairie si vous utilisez Wireshark sous Windows, puisque lui aussi l’utilise également et requiert son installation.

Même chose que sous Linux, vous pourrez valider que Nmap est bien installé en ouvrant une Invite de commande ou un terminal [Powershell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") et en saisissant la commande suivante :

```
nmap --version
```

Voici le résultat attendu :

![nmap-image](assets/fr/09.webp)

_Résultat de l’affichage de la version actuelle de Nmap._

Nmap est maintenant installé sous Windows. Vous pourrez l’utiliser exactement de la même façon que sur Linux, en suivant ce tutoriel.

### IV. Les privilèges locaux requis pour utiliser Nmap

Mais au fait, lors de l’utilisation de Nmap, **est-il nécessaire d’avoir des privilèges locaux élevés sur le système ?** La réponse est : **cela dépend**.

Dans son utilisation très basique, c’est-à-dire sans aller très loin dans l’usage de ses options, Nmap ne requiert pas forcément de droits privilégiés. Néanmoins, vous vous apercevrez vite qu’il est mieux d’utiliser Nmap dans un contexte privilégié (“root” sous Linux, “administrateur” ou équivalent sous Windows) pour pouvoir l’utiliser avec toutes ses capacités, au risque d’obtenir un message d’erreur comme celui-ci :

![nmap-image](assets/fr/10.webp)

_Message d’erreur sous Linux lorsque les options de Nmap nécessitent les droits “root”._

Que ce soit sous Linux ou sur Windows, il y a de nombreux cas où Nmap vous demandera un accès privilégié. Les principales raisons sont les suivantes (liste non exhaustive) :

- **Construire des paquets réseau “brut”**: Nmap est capable d’utiliser de nombreuses méthodes de scan, incluant la manipulation et construction avancée de paquets. C’est par exemple le cas quand nous voulons effectuer des scans TCP SYN, qui ne respectent pas le _Three-way handshake_ classique des échanges TCP. Pour ce faire, Nmap doit utiliser d’autres fonctions que celles natives aux systèmes d’exploitation, qui ne savent que respecter les bonnes pratiques concernant les communications réseau (il fait ici appel aux librairies “Npcap” et “libcap” vues précédemment). C’est parce que Nmap ne fait pas les choses de façon “standard” qu’il est capable de déduire certaines informations concernant les OS, les services et certaines vulnérabilités.
    
- **Écouter le trafic réseau** : certaines options de Nmap nécessitent qu’il se mette en écoute du réseau afin de récupérer certaines informations. Cette action est considérée comme sensible sur les systèmes d’exploitation puisqu’elle permet d’écouter aussi les communications des autres applications du système. Exactement comme Wireshark, Nmap a besoin de privilèges spécifiques pour réaliser cela, qu’il est plus facile d’obtenir en étant directement dans une session privilégiée.
    
- **Se mettre en écoute sur des ports privilégiés** : sur les systèmes d’exploitation, les ports de 0 à 1024 (TCP comme UDP) sont dits privilégiés, c’est-à-dire qu’ils sont en quelque sorte réservés à des usages bien précis et donc protégés. Bien qu’il s’agisse d’une raison un peu obsolète aujourd’hui, il est toujours nécessaire d’avoir certains privilèges pour écouter sur ces ports, ce que Nmap peut être amené à faire en fonction de la façon dont il sera utilisé.
    
- **Envoyer des paquets en UDP :** de même, la mise en écoute d’une application réseau sur des ports UDP (un protocole sans état) nécessite des droits privilégiés sur les systèmes d’exploitation. Une session privilégiée sera donc nécessaire dès lors que l’on souhaite faire un scan UDP, pour lequel Nmap devra se mettre en écoute d’une réponse pour analyser les réponses à ses scans.
    

Pour être plus précis, il est possible, au moins sous Linux, d’exécuter Nmap avec toutes ses fonctions et options sans pour autant être “root”. Cela en accordant les bonnes _capabilities_ au binaire. Cependant, cela nécessite des manipulations avancées et peut ne pas être aussi pratique que d'exécuter directement Nmap avec des privilèges. Également, cette approche est moins courante et peut poser des problèmes de sécurité si elle est mal configurée.

Néanmoins, cela s’éloigne un peu de notre tutoriel sur Nmap, nous nous en passerons donc pour l'instant.

Pour la suite de ce tutoriel, considérez que Nmap est toujours exécuté en tant que “root” (depuis un shell en tant que ”root” ou via la commande “sudo”), ou dans un terminal administrateur sous Windows, même si cela n’est pas indiqué. Sinon, vous pourrez avoir des différences de résultat (subtiles, mais bien présentes) par rapport au tutoriel.

### V. Conclusion

Voilà ! Nmap est maintenant installé sur notre système d’exploitation et prêt à être utilisé, il ne nécessite pas plus de configuration que cela. Cette section clôture l’introduction et la présentation de Nmap. J’espère qu’elle vous aura mis l’eau à la bouche et que vous avez hâte de commencer la pratique.

Plus sérieusement, nous avons maintenant une meilleure idée de ce qu’est l’outil de cartographie Nmap et quels sont ses cas d’usages les plus courants, mais aussi ses limites. Passons à la suite !


## 4 - Scans des ports TCP et UDP avec Nmap

### I. Présentation

Dans cette section, nous apprendrons à faire nos premiers scans de port grâce à l’outil de scan réseau Nmap. Nous verrons comment l’utiliser pour dresser une liste des services réseau exposés sur un hôte, qu’ils utilisent les protocoles TCP ou UDP.

N’oubliez pas, à partir d’ici, de ne scanner que des hôtes dans un environnement maîtrisé et pour lequel vous disposez d’une autorisation explicite.

- Pour rappel : [Code pénal : Chapitre III : Des atteintes aux systèmes de traitement automatisé de données](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)
    

**Si vous n’en avez pas sous la main**, je vous oriente vers les solutions gratuites suivantes, qui sont faites pour !

- **[Hack The Box](https://app.hackthebox.com/ "Hack The Box")** : Plateforme d’entraînement au hacking, Hack The Box met constamment à disposition des systèmes vulnérables que vous pourrez attaquer comme bon vous semble. Plusieurs centaines de systèmes sont disponibles, mais un pool renouvelé de 20 machines est proposé gratuitement toute l’année, l’accès se fait via un VPN OpenVPN.
    
- **[Vulnhub](https://www.vulnhub.com/ "Vulnhub")** : Cette plateforme propose en téléchargement de nombreux systèmes intentionnellement vulnérables qu’il est possible d’utiliser via VirtualBox (solution gratuite elle aussi) ou autre. Une fois téléchargé, pas besoin de VPN, tout est en local.
    

Également, vous êtes libre de vous **créer une machine virtuelle** sur votre système d’exploitation préféré et d’y installer divers services afin qu’ils vous servent de cibles de test. L’avantage ici sera que vous pourrez également voir ce qu’il se passe côté serveur lors d’un scan, notamment avec Wireshark, et aurez la main sur le pare-feu local quand nous ferons des tests plus avancés.

Place à la pratique !

### II. Scanner les ports TCP d'un hôte via Nmap

#### A. Premier scan de port TCP avec Nmap

Nous allons maintenant effectuer nos premiers scans via Nmap. Notre objectif ici est simple, nous souhaitons découvrir quels sont les services exposés par le serveur web que nous venons de déployer, histoire de voir s’il n’y a rien d’inattendu, à tout hasard un service d’administration qui ne devrait pas être accessible, ou l’exposition d’un port d’une application qui nous pensions décomissionnée.

Dans mon exemple suivant, l’hôte à scanner possède l’adresse IP “192.168.1.18” :

```
nmap 192.168.1.18
```

Voici un résultat possible, nous y voyons un retour tout à fait classique de Nmap avec de nombreuses informations :

![nmap-image](assets/fr/11.webp)

_Résultat d’un scan TCP simple réalisé via Nmap._

En jetant un œil rapide à ce résultat, nous comprenons que les ports TCP/22 et TCP/80 sont accessibles sur cet hôte.

Par défaut et si on ne lui dit rien à ce sujet, Nmap va effectuer uniquement des scans sur les ports TCP.

#### B. Comprendre le résultat d’un scan Nmap simple

Allons néanmoins plus loin sur la compréhension de cette sortie, chaque ligne à son importance, déjà pour savoir ce qui vient d’être fait, et ensuite pour bien interpréter les résultats du scan en lui-même.

La première ligne est essentiellement un rappel de la version et date du scan (utiles pour les traces et l’archivage tout de même !) :

```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```

La seconde ligne nous indique le début des résultats de scan concernant l’hôte “debian.home (192.168.1.19)”. Information qui nous sera utile lorsque l’on commencera à scanner plusieurs hôtes en même temps :

```
Nmap scan report for debian.home (192.168.1.19)
```

La troisième ligne nous indique que l’hôte en question en bien “Up”, c’est-à-dire actif :

```
Host is up (0.00022s latency).
```

Enfin, Nmap nous informe que 998 ports TCP identifiés comme fermés ne sont pas affichés dans la sortie :

```
Not shown: 998 closed tcp ports (conn-refused)
```

Il nous évite ainsi près de 1000 lignes de résultat ressemblant à :

```
1/tcp closed
2/tcp closed
3/tcp closed
…
```

Merci à lui de nous épargner cela !

Pourquoi 998 ports “closed” ? Si l’on ajoute les 2 ports ouverts cela fait 1000, et c’est le nombre de ports que Nmap va scanner dans sa configuration par défaut, il ne scanne pas les 65535 ports TCP existants ! Nous verrons plus tard que cela est entièrement et facilement personnalisable. Mais si l’hôte ciblé possède un service en écoute sur un port un peu exotique, ce scan “par défaut” ne permettra pas de le découvrir.

À la suite de ces différentes informations, nous retrouvons ce qui est le plus intéressant, un tableau organisé selon les trois colonnes “PORT – STATE – SERVICE” :

- La première colonne “PORT” indique simplement le port/protocole ciblé, il est ici important de regarder s’il s’agit d’un port TCP (`<port>/tcp`) ou de l’UDP (`<port>/udp`).
    
- La colonne “STATE” indique le statut du service réseau découvert sur ce port et déterminé par Nmap en fonction de la réponse obtenue. Il peut bien sûr être “open” (ouvert), “closed” (fermé), mais aussi “filtered” (filtré) ou “unknown” (inconnu). Nous verrons notamment plus tard comment Nmap fait pour distinguer ces différents états.
    
- La colonne “SERVICE” indique le service exposé sur le port en question. Attention toutefois, nous n’avons ici pas utilisé d’options relatives à la découverte active des services. Nmap se base alors sur une référence locale entre un port/protocole et le service supposément assigné : le fichier “/etc/services”
    

Si l’on jette un oeil au fichier “/etc/services” sur un système Linux, on retrouve un lien “port/protocole – service” similaire à celui affiché par Nmap :

![nmap-image](assets/fr/12.webp)

_Extrait du contenu du fichier “/etc/services” sous Linux._

Il faut bien comprendre que, pour l’instant, Nmap n’a pas fait de découverte active de service. Ainsi, il aurait été incapable d’identifier le service SSH derrière un port TCP/80 si tel avait été le cas. D’où l’importance de savoir utiliser les bonnes options, cela va venir !

Savoir bien interpréter la sortie de Nmap est très important pour bien maîtriser l’outil. La bonne nouvelle, c’est que cette sortie sera en grande partie la même, quelles que soient les options utilisées.

#### C. Regardons sous le capot : analyse réseau via Wireshark

Si l’on regarde attentivement ce qu’il se passe sur l’interface réseau de l’hôte qui scanne le serveur ou sur celle du serveur lui-même, les actions de Nmap seront beaucoup plus claires. C’est ce que nous allons faire ici.

Ce que je peux vous montrer ici est une partie de ce qui est visible dans Wireshark. Pour aller plus loin, n’hésitez pas à faire vous-même une capture réseau lors d’un scan pour parcourir ensuite ce qui a été capturé.

Dans le cadre de ce test, mon hôte de scan (192.168.1.18) et mon hôte cible (192.168.1.19) sont sur le même réseau local.

Nmap commence par chercher à savoir si l’hôte cible est actif sur le réseau local en émettant une requête ARP. En cas de réponse, il sait alors que l’hôte est actif et commence son scan réseau :

![nmap-image](assets/fr/13.webp)

_ARP request émise par Nmap pour déterminer si un hôte cible est présent sur le réseau local._

Si l’hôte à scanner est sur un réseau distant, Nmap commence par émettre un ping request et tente de joindre quelques ports très fréquemment exposés (TCP/80, TCP/443) :

![nmap-image](assets/fr/14.webp)

_Ping request émis par Nmap pour déterminer si un hôte cible est joignable sur un réseau distant._

S’il obtient une réponse à l’un de ces différents essais, il considère la cible comme active.

Une fois que Nmap a déterminé que sa cible était belle et bien active, il va chercher à résoudre son nom de domaine auprès du serveur DNS configuré sur la carte réseau, c’est vrai que l’on ne lui a pas demandé de ne pas le faire :

![nmap-image](assets/fr/15.webp)

_Résolution DNS sur la cible du scan par Nmap._

Maintenant que Nmap a bien identifié sa cible et qu’il l’a sait active, il commence à faire son scan de port TCP :

![nmap-image](assets/fr/16.webp)

_Émission de paquet TCP SYN et réception de RST/ACK lors d’un scan Nmap._

Il va pour cela, sur chaque port TCP faisant partie de son range par défaut, **envoyer des paquets TCP SYN et attendre une réponse**. Sur la capture ci-dessus, il reçoit de la part du serveur scanné des paquets TCP RST/ACK signifiant “circulez, il n’y a rien à voir”, autrement dit, ces ports sont fermés. Ce sera, nous l’avons vu dans le résultat, le cas de la plupart des ports scannés. Ceci à l’exception de deux :

![nmap-image](assets/fr/17.webp)

_Réponse à l’envoi d’un packet TCP SYN sur le port 22, actif sur la cible du scan._

Sur la capture ci-dessus, nous voyons un **paquet TCP SYN/ACK envoyé par l’hôte ciblé**. Le port est actif et expose bien un service. Nmap acquiesce alors la réception de la réponse, puis met fin à la connexion (TCP RST/ACK). **Voilà comment il a su que le port TCP/22 était actif**.

Nous avons vu ici que Nmap respecte bien le “Three Way Handshake” lors de son scan réseau TCP. Pour des raisons de performance, il est possible de lui demander de ne pas répondre au retour du serveur, faisant alors l’économie de plusieurs milliers de paquets lors du scan d’un large réseau. Mais, nous verrons ces options et optimisations plus tard dans le tutoriel.

Nous avons à présent une meilleure idée de comment faire un scan TCP et de ce qu’il se passe réellement quand il est opéré. Nous avons également vu que par défaut, Nmap effectue un scan de port TCP sur un nombre limité de ports.

### III. Scanner les ports UDP avec Nmap

#### A. Premier scan de port UDP avec Nmap

À présent, nous allons voir comment réaliser un scan sur les ports UDP d’un hôte. Comme nous l’avons vu, Nmap va par défaut toujours effectuer des scans sur des ports TCP. Cela peut nous faire passer à côté de pas mal d’informations si nous ne le savons pas.

Pour rappel, dans le cadre de ce test, mon hôte de scan (192.168.1.18) et mon hôte cible (192.168.1.19) sont sur le même réseau local.

```
nmap -sU 192.168.1.19
```

Ici, le retour obtenu a le même format que pour un scan TCP, les services actifs affichés sont cependant en `<port>/UDP`, comme demandé !

![nmap-image](assets/fr/18.webp)

_Résultat d’un scan UDP simple réalisé via Nmap._

C’est l’option “-sU” qui permet d’indiquer à Nmap que l’on veut travailler sur de l’UDP, et non du TCP comme c’est le cas par défaut.

Au passage, vous remarquerez sûrement que Nmap nécessite les droits “root” pour les scans UDP, comme mentionné précédemment dans le tutoriel.

_Remarque : Depuis les dernières versions de Nmap, il est toujours recommandé d’exécuter les scans UDP avec des privilèges administrateur pour garantir la fiabilité des résultats, car certaines fonctionnalités requièrent l’accès brut aux sockets réseau._

Les scans UDP peuvent être très longs (1100 secondes pour scanner 1000 ports dans mon exemple), cela en raison de l’absence du “Three Way Handshake” en UDP, qui fait que Nmap attendra un retour pour chaque paquet UDP envoyé et qu’il déterminera le port comme “closed” uniquement s’il n’a pas de retour au bout d’un certain temps (timeout). Cette réponse des hôtes scannés n’étant d’ailleurs pas systématique et souvent limitée en termes de nombre de réponses par seconde pour éviter certaines attaques par amplification. Cela au contraire du TCP où il y a une réponse immédiate de l’hôte scanné, que le port soit ouvert ou fermé. Nous verrons plus tard comment optimiser cela.

Une deuxième difficulté en UDP est **que les services ne répondent pas systématiquement à la réception d’un paquet**, tout simplement, car ce n’est pas toujours nécessaire et que c’est le principe de l’UDP. Lorsque c’est le cas et qu’aucun ICMP “port unreachable” n’est reçu, le service est marqué comme “open|filtered” par Nmap, comme présent dans la capture ci-dessus.

#### B. Regardons sous le capot : analyse réseau via Wireshark

Comme lors de notre scan TCP, regardons de plus près ce qu’il se passe au niveau réseau lors d’un scan UDP via une analyse Wireshark. Le comportement de Nmap pour déterminer si un hôte est actif est le même.

La seule vraie différence lors d’un scan UDP est que Nmap n’attendra pas un “Three Way Handshake”, puisque ce mécanisme n’existe pas en UDP (protocole sans état) :

![nmap-image](assets/fr/19.webp)

_Émission de paquet UDP et réception de ICMP (port unreachable) lors d’un scan Nmap._

Nous voyons sur la capture ci-dessus que Nmap va émettre un grand nombre de paquets UDP, et recevoir pour la plupart d’entre eux un paquet ICMP “Destination unreachable (Port unreachable)” en réponse. C’est normal, puisqu’il s’agit de la réponse appropriée et définie par le [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") lorsqu’un port UDP n’est pas joignable :

![nmap-image](assets/fr/20.webp)

_Extrait du RFC 1122._

Regardons de plus près cette capture Wireshark, qui expose **les trois cas de figure possibles** en UDP :

![nmap-image](assets/fr/21.webp)

_Capture réseau lors d’un scan UDP sur différents ports avec Nmap._

Ces trois cas de figure sont les suivants :

- Le premier échange est composé des paquets n°3, 4 et 8, 9. Nmap envoie des paquets UDP sur le port SNMP classique et **construit donc à l’avance des paquets conformes à ce protocole**. Il obtient ensuite une réponse du serveur (paquets n°8 et 9). Résultat : Nmap a eu une réponse, le service est bien actif (“open”).
    
- Le second échange est composé des paquets n°6 et 7. Nmap envoi un paquet UDP “vide” (sans structure relative à un protocole précis) à destination du port UDP/165 et reçoit en réponse un paquet ICMP “Destination unreachable (Port unreachable)”. Résultat : Nmap a eu une réponse (négative), l’hôte est bien up, mais le service qu’il a essayé de joindre n’est pas opérationnel sur ce port, celui-ci sera marqué en fermé (“closed”).
    
- Le dernier échange est composé du paquet n°12 : Nmap envoi un paquet UDP “vide” à destination du port UDP/1235. Il n’a aucune réponse, même pas un refus explicite de la part de l’hôte scanné. Résultat : Nmap marque le port en “open|filtered” car il est incapable de dire s’il s’agit d’une absence de réponse due à la présence d’un pare-feu, configuré pour ne rien répondre, ou à un service UDP actif qui ne renvoie aucune réponse de toute façon (non obligatoire en UDP).
    

Voici donc le résultat affiché par Nmap suite à ces trois cas de figure :

![nmap-image](assets/fr/22.webp)

_Résultats possibles d’un scan UDP réalisé via Nmap._

Nous avons à présent une meilleure idée de comment faire un scan UDP et de ce qu’il se passe réellement quand il est opéré. Pour l’instant nous n’avons fait qu’utiliser Nmap très simplement, sans vraiment d’options et sans vraiment décider des ports à scanner, mais cela va bientôt changer !

### IV. Maitriser finement les ports scannés via Nmap

#### A. Rappel du comportement par défaut de Nmap

Comme nous l’avons vu, Nmap choisit lui-même le nombre et les ports à scanner si l’on ne lui spécifie pas d’options. Il s’agit là d’une configuration “par défaut” utilisée par Nmap lorsque l’on ne lui indique pas exactement quoi faire. Ces options par défaut sont faites pour avoir une idée des principaux ports exposés, ceux-ci étant sélectionnés par fréquence d’exposition (ports les plus communs ou fréquents) plutôt que dans un ordre numérique (port 1, 2, 3, etc.) et également pour éviter de partir sur un scan des 65535 ports possibles si l’on ne spécifie pas les options appropriées, ce qui serait trop long et verbeux pour un cas d’utilisation “par défaut”.

**Comment sont choisis ces ports ?**

Les 1000 ports scannés dans le mode par défaut sont choisis en fonction de leur fréquence d’apparition. Il s’agit de statistiques maintenues par Nmap et mises à jour au même titre que le binaire lui-même et de ses scripts (modules). Vous pouvez vous-même consulter ces statistiques dans le fichier “/usr/shares/nmap/nmap-services” :

![nmap-image](assets/fr/23.webp)

_Extrait du fichier “/usr/shares/nmap/nmap-services”._

Nous voyons ici dans la troisième colonne ce qui s’apparente à des probabilités (entre 0 et 1) ou une répartition en pourcentage. Il s’agit de la fréquence d’apparition de chaque couple port/protocole. Nous voyons alors que les ports les plus connus (FTP, SSH, TELNET et SMTP dans cet extrait) ont une valeur bien supérieure aux autres.

#### B. Spécifier précisément les ports cibles d’un scan Nmap

Néanmoins dans la réalité, nous pouvons avoir besoin de scanner uniquement un port précis, ou plusieurs, ou un range de port bien identifié. Cela tombe bien, Nmap nous permet très facilement de faire cela, de manière uniforme qu’il s’agisse d’un scan UDP ou TCP.

**Scanner un port spécifique via Nmap**

Si nous souhaitons scanner un seul port, et non pas 1000, nous pouvons spécifier ce port via l’option “-p” ou “--port” de Nmap :

```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```

Dès lors, le scan sera naturellement beaucoup plus rapide et Nmap n’émettra que les paquets nécessaires pour détecter si l’hôte est actif, puis si le port spécifié est joignable. Voilà qui nous fera gagner du temps si l’on veut juste réaliser un test rapide, histoire de voir si le service web de notre site vitrine est toujours up.

**Scanner plusieurs ports via Nmap**

De la même manière, nous pouvons spécifier plusieurs ports à Nmap, cela à l’aide de la même option et en enchaînant les ports spécifiés par une virgule :

```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```

Peu importe l’ordre, Nmap vérifiera tous ces ports, et uniquement ceux-ci sur l’hôte ciblé. Vous remarquerez dans le résultat affiché par Nmap que celui-ci **nous indique explicitement tous les ports et leur état**, même s’ils sont “closed”. À l’inverse du comportement par défaut où cette sortie complète aurait pris beaucoup trop de place :

![nmap-image](assets/fr/24.webp)

*Résultat d’un scan Nmap TCP sur les ports indiqués.*

**Scanner un range de ports**

Si le nombre de ports que l’on souhaite scanner est trop grand, il est possible de les spécifier par fourchette, par exemple :

```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```

Il est bien sûr possible de mixer un peu tout cela comme bon vous semble, par exemple :

```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```

**Scanner de ports en TCP et UDP**

Vous pouvez également très bien réaliser des scans en UDP et TCP en même temps, sur des ports bien choisis :

```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```

Vous remarquerez dans ce dernier exemple la présence des “U:” pour indiquer un port UDP et “T:” pour indiquer un port TCP. Voici une sortie possible de ce type de scan :

![nmap-image](assets/fr/25.webp)

*Résultat d’un scan sur des ports TCP et UDP avec Nmap.*

Voilà qui commence à être intéressant en termes de personnalisation des scans !

**Scanner tous les ports**

Pour finir, il est possible d’indiquer à Nmap des ranges beaucoup plus grands, ou au contraire plus petits. Nous avons vu que la liste par défaut sélectionnée par Nmap contient 1000 ports. Nous pouvons très bien lui demander le top 100 des ports les plus fréquents, ou le top 200, cela en utilisant l’option “--top-ports” :

```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```

Et enfin, nous pouvons lui demander de scanner tous les ports possibles (les 65535), cela avec la notation “-p-” :

```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```

Ce dernier cas de figure prendra certes plus de temps, notamment en UDP, mais vous serez alors certains de ne passer à côté d’aucun port ouvert.

*Remarque : L’option “-p-” est bien la méthode recommandée pour scanner tous les ports TCP. Pour les scans UDP, il est conseillé de limiter le nombre de ports pour des raisons de performance, car les scans complets de tous les ports UDP peuvent prendre énormément de temps.*

Plus tard dans le tutoriel, nous verrons comment optimiser la vitesse des scans Nmap en fonction de nos besoins, ce qui sera notamment utile aux scans sur l’intégralité des ports en TCP et UDP.

### V. Conclusion

Dans cette section, nous avons enfin fait un peu de pratique, nous savons à présent **utiliser Nmap de façon basique pour scanner les ports TCP et UDP** d’un hôte. Nous avons également regardé en détail ce qu’il se passe au niveau réseau et **comment Nmap détermine si un port TCP ou UDP est actif ou non**. Enfin, nous savons comment sélectionner finement les ports que nous souhaitons scanner et **ce que font vraiment les options par défaut de Nmap**. Dans la suite, nous réutiliserons ces connaissances et les appliquerons au scan d’un réseau tout entier, notamment pour effectuer une cartographie globale et découverte d’un réseau.


## 5 - Cartographie et découverte de réseau avec Nmap

### I. Présentation

Dans cette section, nous apprendrons à utiliser l’outil de scan réseau Nmap afin de dresser une cartographie du réseau. Nous verrons qu’il peut être très efficace dans cette tâche à travers ses différentes options. Enfin, nous verrons différentes méthodes pour spécifier les cibles de nos scans à Nmap.

Nous utiliserons notamment ce que nous avons appris dans la section précédente concernant la manière dont Nmap détermine si un hôte est actif et joignable.

Comme évoqué dans l’introduction à Nmap, celui-ci est un Network Mapper, littéralement un cartographe du réseau. Il s’agit donc de l’outil parfait pour dresser une liste des hôtes accessibles du réseau, qu’il s’agisse d’un réseau distant ou local.

**Retour de l’auteur :**

Dans les faits en tant qu’auditeur cybersécurité et pentester, j’utilise Nmap systématiquement lors de la réalisation de tests d’intrusion internes afin de savoir où je suis, quels sont mes voisins sur le réseau local et quels sont les autres réseaux accessibles ainsi que les systèmes qui s’y situent. Mon objectif est simple : faire une cartographie du réseau, déterminer la taille du système d’information et notamment esquisser sa surface d’attaque.

Cette cartographie du réseau peut aussi être utile dans des contextes de diagnostic du réseau, de supervision, de recensement des actifs (êtes-vous bien sûr que votre SI est bien composé uniquement de ce qui est dans l’Active Directory ou dans votre GLPI/OCS Inventory ?), etc. Cela peut donc également être intéressant afin de détecter la présence de Shadow IT dans votre système d’information.

### II. Utiliser Nmap pour scanner une plage réseau

#### A. Découverte d’un réseau avec un scan Nmap

Nous souhaitons à présent passer à la vitesse supérieure et analyser tout notre réseau local. Rien de plus simple, il nous suffit pour cela de réutiliser les commandes vues dans la section précédente, mais de spécifier un CIDR à la place d’une simple adresse IP.

Un CIDR (**Classless Inter Domain Routing**) est la notation “classique” pour spécifier une plage réseau et son étendue (à l’aide du masque). Par exemple “192.168.0.0/24”, il s’agit d’une “traduction” de la notation décimale du masque “255.255.255.0”.

Pour utiliser Nmap en spécifiant un CIDR, nous pouvons l’utiliser comme suivant :

```
# Scan a CIDR
nmap 192.168.0.0/24
```

Il est également possible, comme pour les ports dans la section précédente, de spécifier plusieurs hôtes, plusieurs réseaux, ou range :

```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```

Voici un exemple de résultat que nous pourrions avoir lors de l’exécution d’un scan sur un réseau :

![nmap-image](assets/fr/26.webp)

_Résultat d’un scan Nmap pour cartographier plusieurs réseaux._

Nous voyons notamment plusieurs hôtes actifs, chaque section relative à un hôte débute par une ligne telle que celle-ci :

```
Nmap scan report for <name> (<IP>)
```

Cela nous permet de clairement voir à quel hôte se rapportent les résultats qui suivent. La toute dernière ligne a également son importance :

```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```

Nous savons que, sur les réseaux scannés, Nmap a découvert 5 hôtes actifs.

#### B. Regardons sous le capot : analyse réseau via Wireshark

Nous allons à présent regarder un peu plus en détail ce qu’il se passe au niveau réseau lors d’une découverte réseau réalisée via Nmap.

Comme nous l’avons vu dans la section précédente, Nmap va par défaut utiliser le protocole ARP pour détecter la présence d’hôtes sur le réseau local :

![nmap-image](assets/fr/27.webp)

_Paquets ARP capturés lors du scan d’un réseau local via Nmap et avec ses options par défaut._

Il est ainsi en capacité de détecter la quasi-totalité des hôtes du réseau local, puisque la réponse à une requête ARP est généralement fournie par tous les hôtes actifs sur le réseau et ne paraît nullement suspecte.

Pour les réseaux distants, Nmap va utiliser une combinaison de techniques :

![nmap-image](assets/fr/28.webp)

_Paquets ICMP et TCP capturés lors du scan d’un réseau distant via Nmap et avec ses options par défaut._

Pour être plus précis, Nmap utilise un paquet “Echo ICMP” (cas classique du “ping”) ainsi qu’un paquet “ICMP Timestamp”, d’ordinaire utilisé pour calculer le temps de transite d’un paquet. Il espère ainsi avoir une réponse des hôtes situés sur des réseaux distants.

Néanmoins il ne se limite pas à cela. Vous pouvez voir dans la capture Wireshark ci-dessus que des **paquets TCP SYN** sont systématiquement envoyés sur les ports TCP/443 de chaque hôte potentiel des réseaux à scanner, ainsi que des paquets **TCP ACK** sur le port TCP/80.

**Pourquoi envoyer des paquets TCP sur des ports dans le cadre d’une découverte réseau ?**

L'envoi d'un paquet SYN à un port donné permet à Nmap de **déterminer si un service est en cours d'écoute sur ce port**. Si un hôte répond à un paquet SYN avec un paquet SYN/ACK, cela indique qu'il est actif et qu'un service est en cours d'écoute sur ce port. Nmap tente donc sa chance sur ce service, **même si aucune réponse au ping n’a été obtenue**.

L'envoi d'un paquet ACK à un port donné permet à Nmap de **déterminer si un pare-feu est présent sur cet hôte**. Si un hôte répond à un paquet ACK avec un paquet RST (Reset), cela indique qu'un pare-feu est probablement présent sur cet hôte et qu'il bloque le trafic non sollicité. Ainsi l’hôte trahit sa présence sur le réseau, même s’il n’a pas répondu aux autres sollicitations.

Il est cependant important de noter que la détection de pare-feu à l'aide de cette technique peut ne pas être parfaitement fiable dans tous les cas. Certains hôtes peuvent générer des réponses RST pour d'autres raisons que la présence d'un pare-feu, comme la configuration spécifique du service ou du système d'exploitation. De plus, les pare-feu modernes peuvent être configurés pour ne pas répondre aux tentatives de découverte de ce type.

Nous avons bien avancé à présent et savons réaliser une découverte réseau basique. Nous allons à présent voir quelques options supplémentaires nous permettant de mieux maîtriser le comportement de Nmap.

### III. Découverte réseau sans scan de port avec Nmap

Vous l’aurez sûrement remarqué, par défaut Nmap **effectue un scan de port à la suite de sa découverte d’hôte actif**, ce qui rajoute à notre scan une énorme quantité de paquets et d’attente de réponses. Si vous avez 5 hôtes sur votre réseau, Nmap va chercher à vérifier l’état d’environ 5 000 ports, ce qui prendra plus de temps.

Il est cependant possible d’utiliser les options de Nmap afin d’effectuer **uniquement une découverte des hôtes actifs** sur un réseau, sans découverte de leurs services.

Si l’on souhaite uniquement savoir quels sont les hôtes joignables, sans informations sur les services et ports qu’ils exposent, nous pouvons alors utiliser l’option “-sn” pour réaliser **uniquement un scan utilisant des Echo ICMP (ping) et requêtes ARP**. Autrement dit, désactiver totalement le scan de port :

```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```

Voici le résultat d’une découverte réseau Nmap réalisée sans scan de port :

![nmap-image](assets/fr/29.webp)

Résultat d’une découverte réseau sans scan de port avec Nmap.

Nous avons évoqué précédemment les éventuelles limitations de l’utilisation unique de l’ICMP pour la découverte d’hôte (pour les réseaux distants). C’est pourquoi Nmap utilise aussi quelques astuces pouvant trahir la présence d’un pare-feu ou d’un service spécifique sur les hôtes. Nous pouvons, à l’aide des options, réutiliser ces astuces et même les étendre, sans pour autant repartir sur un scan complet des ports de chaque hôte découvert.

Nous allons pour cela utiliser l’option “-PS” (TCP SYN), “-PA” (TCP ACK), qui vont nous permettre d’indiquer les ports que l’on souhaite joindre dans le cadre de notre découverte d’hôte, ainsi que l’option “-PP” :

```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```

Ce scan nous assure déjà d’avoir une découverte des hôtes un peu plus complète que via les options par défaut.

Nous commençons à avoir des commandes assez complètes, utilisant de multiples options. Cela parce que nous savons comment Nmap fonctionne et quelles sont les limites de ses options “par défaut” qui peuvent parfois nous faire perdre du temps ou passer à côté d’éléments importants. C’est tout l’intérêt de prendre le temps d’apprendre à le maîtriser !

Pour détailler un peu les options de notre dernière commande :

- “`-sn`” : désactive le scan de ports pour chaque hôte actif découvert par Nmap.
    
- “`-PP`” : active l’ICMP echo (ping scan) pour la découverte d’hôte.
    
- “`-PS <PORT>`” : envoi d’un paquet TCP SYN sur le ou les ports indiqués afin de détecter un éventuel service actif trahissant la présence d’un hôte n’ayant pas répondu au ping.
    
- “`-PA <PORT>`” : envoi d’un paquet TCP ACK sur le ou les ports indiqués afin de détecter un éventuel pare-feu actif trahissant la présence d’un hôte n’ayant pas répondu au ping.
    

Dans l’exemple ci-dessus, je spécifie les ports que je considère être les plus souvent exposés dans mes contextes d’utilisation de Nmap pour l’option “-PS”. Ces différents ports seront donc testés sur chaque hôte, non pas dans le but de voir si le service qu’ils hébergent est vraiment actif, mais pour voir si cela permet de découvrir un hôte qui n’aurait pas répondu à nos Echo ICMP en étant quand même actif (par l’intermédiaire d’une réponse du service ou du pare-feu de l’hôte).

Voici ce que l’on peut observer dans une capture réseau réalisée au moment d’un tel scan, il s’agit ici d’un extrait sur un seul hôte cible :

![nmap-image](assets/fr/30.webp)

_Paquets envoyés par Nmap lors d’une découverte réseau avancée, sans scan de port._

Nous retrouvons bien nos paquets TCP SYN, notre TCP ACK sur le port TCP/80 et notre Echo ICMP. Nmap réalisera tous ces tests pour chaque hôte ciblé par notre scan de découverte réseau.

### IV. Utiliser un fichier des actifs à cibler avec Nmap

La spécification des cibles peut vite s’avérer complexe dans des systèmes d’information réels qui peuvent parfois être composés de dizaines ou de centaines de réseau, sous-réseau et VLAN. Dès lors, il devient plus simple d’utiliser un fichier comme source pour Nmap que de les spécifier un à un dans la ligne de commande.

Pour commencer, il faut créer un simple fichier contenant une entrée par ligne :

![nmap-image](assets/fr/31.webp)

_Fichier contenant une cible (hôte ou réseau) par ligne._

Ensuite, nous pouvons utiliser toutes les options de Nmap vues jusqu’ici et spécifier l’option “-iL <chemin/fichier>” :

```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```

Nmap va alors inclure dans son scan toutes les cibles contenues dans notre fichier.

Si vous souhaitez être sûr que vos cibles seront toutes prises en compte, vous pouvez utiliser l’option “-sL -n”. Nmap va alors uniquement interpréter les CIDR et hôtes du fichier pour vous les afficher, sans faire partir aucun paquet sur le réseau :

```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```

Cela permet d’être bien sûr de la liste des hôtes qui seront scannés.

Une dernière astuce importante que je souhaite vous partager concerne **l’exclusion d’hôte ou de réseau dans le cadre d’un scan**. Ce besoin d’exclure un hôte peut être nécessaire dans différents cas, notamment si l’on souhaite être sûr et certain qu’**un composant sensible du système d’information ne soit pas dérangé ou perturbé par nos scans**.

Des exemples fréquents de tels besoins sont les cas où une entreprise possède des équipements industriels (automates) ou de santé. Ces équipements sont parfois mal conçus et pas du tout prévus pour recevoir des paquets mal formatés ou en trop grande quantité. Pour des besoins évidents de disponibilité ou risque métier/humain, il est alors préférable de les exclure des tests.

Pour exclure des adresses IP ou réseaux de notre scan, nous pouvons utiliser l’option “--exclude” de Nmap, par exemple :

```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```

Dans cet exemple, je scanne le réseau “192.168.1.0/24” mais exclus l’hôte “192.168.1.140” qui s’y situe. Aucun paquet ne sera émis par Nmap à destination de cet hôte. Autre exemple avec l’exclusion d’un sous-réseau :

```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```

Même chose, je scanne le large réseau “10.0.0.0/16”, mais le réseau “10.0.100.0/24” ne sera pas scanné. À nouveau, je vous invite à utiliser l’option “-sL -n” afin d’avoir une vue très claire des hôtes qui seront scannés et exclus du scan, notamment si vous opérez dans un contexte sensible.

### V. Découverte réseau et scan de port

Nous pouvons à présent combiner ce que nous avons appris dans cette section avec nos apprentissages de la section précédente concernant les options de scan de port. Par défaut, nous avons vu que Nmap procédera au scan des 1000 ports les plus fréquents sur chaque hôte actif découvert. Nous avons vu comment empêcher ce comportement s’il n’est pas souhaité, mais nous pouvons tout à fait le maîtriser, voire l’étendre si cela répond à nos besoins.

Par exemple, la commande suivante va vérifier la présence d’un service en écoute sur le port TCP/22 sur chaque hôte scanné :

```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```

Nmap va dans un premier temps faire une découverte réseau pour lister les hôtes actifs, et pour chacun d’entre eux, vérifier qu’un service est présent sur le port TCP/22.

De la même manière, nous pouvons réaliser un scan complet de tous les ports TCP sur chaque hôte découvert sur le réseau “192.168.0.0/24”, en excluant l’hôte “192.168.0.4” par exemple :

```
# Port scan of a CIDR with exclusion 
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```

Libre à vous de combiner toutes les options que nous avons apprises jusque-là en fonction de vos propres besoins.

### VI. Conclusion

Nous avons vu dans cette section comment utiliser Nmap afin de réaliser une cartographie du réseau à l’aide de différentes options. Nous pouvons à présent maîtriser finement les cibles de nos scans ainsi que le comportement de Nmap concernant le scan de port et la méthode de découverte des hôtes. Et le plus important, nous savons quel est le comportement par défaut de Nmap ainsi que ses limitations, et comment utiliser ses principales options pour aller plus loin.

La section suivante sera dédiée aux mécanismes et options de découverte des versions des services et systèmes d’exploitation scannés par Nmap.


## 6 - Détection des versions de services et systèmes d’exploitation avec Nmap

### I. Présentation

Dans cette section, nous allons apprendre à utiliser Nmap pour découvrir et détecter précisément les versions des services et systèmes d’exploitation utilisés par les hôtes scannés. Nous verrons en détail le fonctionnement de Nmap pour accomplir cette tâche, ainsi que les limites de l’outil pour mieux comprendre et interpréter ses résultats.

Nous l’avons vu dans les précédentes sections de ce tutoriel, par défaut, Nmap ne va pas chercher à savoir quel service est exposé sur les ports qu’il scanne et considère comme ouvert. Ainsi, vous pourriez mettre en écoute un service web sur le port TCP/22, Nmap continuera à le rapporter comme ouvert, certes, mais en tant que service `SSH`. Cela parce qu’il utilise une [base de données](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) locale à votre système pour rechercher une relation entre un port/protocole et le nom d’un service (le fichier `/etc/services/`).

Dans la majorité des cas, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) vous fournira une information correcte, car il est rare dans un environnement de production de trouver de tels cas. Cependant, les cas de figure restants seront des situations où un service classique ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, etc.) sera exposé sur un port non classique (par exemple 2022 pour un service SSH), Nmap ne trouvera alors pas de correspondance dans sa base locale, ou une qui ne correspond pas à la réalité, et vous passerez à côté d’une information importante.

Heureusement, Nmap propose des options et mécanismes très précis pour découvrir quel service exact peut se cacher derrière un port ouvert. Il possède même une base de données de requêtes et signatures permettant d’identifier les technologies et versions exactes. En plus des services, Nmap peut de la même manière identifier la technologie utilisée et sa version.

C’est ce que nous allons voir dans cette section.

### II. Comment détecter une technologie ou une version

#### A. Rappel sur l’identification d’une technologie ou version

L’identification d’une technologie et d’une version consiste à récupérer le nom du service, du CMS, de l’application ou du logiciel qui est en écoute sur le port ciblé. Par exemple, une page web est gérée par un CMS (`WordPress`), exécuté par un service web (`Apache`, IIS, Nginx) et hébergé par un serveur (Linux ou Windows). Mais comment savoir quel service web est en place ?

La méthodologie classique pour connaître cette information est le _banner grabbing_ (récupération de bannière) qui consiste simplement à repérer où le service en question affiche cette information et à lire la donnée. Bien souvent, dans leur configuration ou traitement par défaut, les services affichent leur nom et même leur version en première réponse après une connexion.

![nmap-image](assets/fr/32.webp)

_Affichage d’une version dès l’établissement d’une connexion TCP par un service FTP._

Nous voyons ici qu’une simple connexion TCP à ce service via `telnet` entraîne en réponse un paquet TCP contenant sa technologie et sa version.

Lorsque l’on a une petite idée du type de service qui est en face de nous, il est également possible d’envoyer des commandes ou requêtes spécifiques à ce service pour en extraire des informations. Ces requêtes/commandes peuvent aussi être envoyées à l’aveugle (sans être sûr qu’il s’agit du bon type de service), en espérant que l’une d’entre elles provoque une réponse du service en question.

Dans d’autres cas un peu plus avancés, il est nécessaire d’envoyer des paquets spécifiques pour causer une réaction, comme une erreur, qui fournira des informations détaillées sur la version ou la technologie utilisée.

Vous vous en doutez à présent, Nmap va utiliser toutes ces techniques pour tenter d’identifier précisément le type de service hébergé sur un port, ainsi que le nom de sa technologie et sa version.

#### B. Comprendre les Probes et Match de Nmap

Pour effectuer toutes ces vérifications sur chaque port scanné, Nmap utilise une base de données locale qui est fréquemment mise à jour (au même titre que le binaire ou ses modules). Il s’agit d’un fichier texte de plusieurs milliers de lignes : `/usr/share/nmap/nmap-service-probes`.

Ce fichier est composé de nombreuses entrées, toutes sont organisées autour de deux directives principales :

- Les `Probe` : il s’agit de la définition du paquet qu’enverra Nmap pour tenter de provoquer une réaction du service à identifier. Voyez cela comme des tentatives à l’aveugle du type _Bonjour ? Guten Tag ? Hello ? Hum… Buenos Dias peut-être ?_. Dès que le service ciblé recevra un probe qu’il comprend (c’est-à-dire parlant le bon protocole), il répondra à Nmap, qui aura alors une confirmation du type de service dont il s’agit.
    
- Les `Match` : ce sont des expressions régulières qu’appliquera Nmap sur la réponse obtenue. Si l’envoi d’une requête HTTP GET a provoqué une réponse du service, il appliquera sur cette réponse des dizaines d’expressions régulières afin d’identifier la présence, par exemple, du mot `Apache`, `Nginx`, `Microsoft IIS`, etc.
    

Il existe quelques autres directives pour des cas spécifiques, mais les principales pour comprendre le fonctionnement de Nmap et personnaliser son utilisation sont celles-ci. Pour que cette partie théorie soit plus concrète, voici un exemple :

![nmap-image](assets/fr/33.webp)

_Exemple de Probe présent dans le fichier `/usr/share/nmap/nmap-service-probes` de Nmap._

Nous voyons en première ligne de cet exemple un Probe assez simple à comprendre et nommé `GetRequest`. Il s’agit d’un paquet TCP contenant une requête HTTP GET vide sur la racine du service web en utilisant HTTP/1.0, puis un saut de ligne et une ligne vide.

La ligne `ports` indique à Nmap pour quel port il faut envoyer ce Probe. Cela permet de prioriser les tests et de gagner un certain temps.

Enfin, nous avons deux exemples de `match`. Le premier par exemple catégorisera le service web scanné en `ajp13` si l’expression régulière contenue dans cette ligne match avec la réponse du service reçue.

Pour comprendre à quoi peuvent ressembler les Probes, voici une liste de quelques Probes que vous pourrez trouver dans ce fichier (il y en a 188 en tout en date d’écriture de ce tutoriel).

![nmap-image](assets/fr/34.webp)

_Exemple de plusieurs Probes utilisés par Nmap et présents dans le fichier `/usr/share/nmap/nmap-service-probes`._

Il faut ici notamment s’intéresser aux deux premiers (nommés `NULL` et `GenericLines`), qui consistent juste à envoyer un paquet TCP vide ou contenant un renvoi à la ligne. Bien souvent, les services présents sur les serveurs s’annoncent avec précision dès qu’une connexion est reçue, sans action, commande ou requête spécifique du client.

Voici le cas d'un _match_ un peu plus complexe :

```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```

L'expression régulière exacte est ici contenue entre le `m|` et le `|`, qui délimite toute expression régulière dans ce fichier. Prenez ici le temps de bien lire l'entièreté de cet exemple. Vous remarquerez la présence d'une sélection dans l’expression régulière : `([\d.]+)`, celle-ci permet d'isoler une version. Également, cet exemple défini d'autres éléments comme le nom du produit `p/nginx/`, la version récupérée `v/$1/` et le CPE avec version `cpe:/a:igor_sysoev:nginx:$1/`.

Un CPE (Common Platform Enumeration) est un système de notation standardisé utilisé pour identifier et décrire les logiciels et matériels. Ce format permet une gestion plus efficace des vulnérabilités et des configurations de sécurité, et surtout une manière unifiée de les représenter, quel que soit le produit en question. Voici deux exemples de CPE : `cpe:/o:microsoft:windows_8.1:r1` et `cpe:/a:apache:http_server:2.4.35`

On identifie ici clairement leurs types `o` pour OS, `a` pour application, vendeur, produit, et versions.

Ainsi en cas de _match_ avec l'une de cette expression régulière, nous récupérerons non seulement le nom du service, mais aussi sa version et le CPE exact, ce qui nous facilitera notamment la recherche de CVE impactant cette version. Vous retrouverez notamment ces informations dans la sortie standard de Nmap et verrez qu'elles seront très utiles pour d'autres usages que nous évoquerons dans quelques sections.

La syntaxe exacte des _matchs_ et plus globalement des directives du fichier `/usr/share/nmap/nmap-service-probes` ne s’arrête pas là et peut paraître assez complexe lorsque l’on n’est pas habitué à manipuler Nmap et ses résultats. Cependant, il faut au moins garder en tête son existence et son fonctionnement général, cela sera utile plus tard lorsque vous souhaiterez comprendre ou débugger un résultat, personnaliser un scan ou même contribuer au développement de Nmap.

### III. Utiliser Nmap pour détecter des versions

À présent, nous allons utiliser toute cette mécanique complexe de _Probe_ et _Match_ via une option simple : `-sV`. Celle-ci permet simplement d’indiquer à Nmap : tente de découvrir précisément les services et versions des ports que tu détermines comme ouvert.

```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```

Voici un exemple complet du résultat d’une telle commande :

![nmap-image](assets/fr/35.webp)

_Résultat de la détection de versions des applications exposées sur le réseau par Nmap._

Nous voyons ici que Nmap est parvenu à identifier toutes les versions des services réseau exposés par cette cible et qu’il nous affiche ces informations dans une nouvelle colonne `VERSION`. Il est possible de voir des informations assez précises, allant parfois jusqu’au système d’exploitation, si cette information fait partie de la signature récupérée.

Pour comprendre en détail ce qu’il se passe pendant un scan de vulnérabilité, nous pouvons utiliser l’option `--version-trace`. Elle permettra d’avoir une vue en mode “debug” et affichera notamment le _Probe_ qui a permis la détection :

```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```

En résultat, nous aurons de nombreuses informations et il va falloir trier un peu. Tentez d’identifier les lignes qui commencent par `Service scan hard match`. Vous verrez alors des lignes telles que celles-ci :

```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```

Nous voyons très clairement quels _Probes_ ont permis la détection de technologie et version (ici les _Probes_ `NULL` et `GetRequest`), ainsi que les informations récupérées.

### IV. Maitriser les tests et la précision des détections

Nous allons à présent revenir sur une directive du fichier `/usr/share/nmap/nmap-service-probes` sur laquelle nous ne nous sommes pas attardés tout à l’heure :

![nmap-image](assets/fr/36.webp)

_Directive `rarity` des Probes dans le fichier `/usr/share/nmap/nmap-service-probes`._

Cette directive permet d’indiquer la rareté (comprendre : priorité/probabilité) associée à un _Probe_. Cette notation de 1 à 9 permet d’avoir la main sur le niveau d’exhaustivité de l’analyse faite par Nmap lors de l’envoi des _Probes_. Dans le système de “notation” mis en place par Nmap, une rareté à 1 permet d’avoir en retour une information dans la grande majorité des cas, alors qu’une rareté à 8 ou 9 représente plus un cas très particulier propre à une configuration ou un service rarement présent.

Pour être plus clair, dans un cas par défaut, Nmap va envoyer sur chaque service à identifier les _Probes_ qui ont une rareté de 1 à 7. Pour que vous vous représentiez mieux la répartition des _Probes_ par _rarity_, voici leur décompte :

```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```

Cela peut paraître contre-intuitif, il y a plus de `rarity` 8 et 9 que le reste. C’est justement parce que les Probe à rareté 1 sont génériques et fonctionnent dans la majorité des cas, peu importe le service (rappelez-vous du Probe `NULL` qui envoie simplement un paquet TCP vide). Alors que les Probes plus complexes sont presque uniques par service.

Si l’on souhaite gérer manuellement les Probes que l’on souhaite utiliser dans notre scan de version, nous pouvons utiliser l’option `--version-intensity`. Voici deux exemples :

```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```

Pour finir sur ce sujet, voici un exemple de _Probe_ 9 et 8:

![nmap-image](assets/fr/37.webp)

_Exemples de Probe à rarity 8 et 9 dans le fichier `/usr/share/nmap/nmap-service-probes`._

Ces deux _Probes_ permettent de détecter des serveurs Quake1 et Quake2 (le jeu vidéo). Intéressant pour le côté nostalgique, mais peu probable que ça nous serve au quotidien.

En fonction de vos besoins de précision ou de rapidité, rappelez-vous donc que ce principe de `rarity` existe et peut jouer sur le résultat.

### V. Utiliser Nmap pour détecter des systèmes d'exploitation

Nous allons maintenant voir comment Nmap peut nous aider à détecter les systèmes d’exploitation des hôtes scannés et détectés sur un réseau. Il faut pour cela utiliser l’option `-O` (pour `OS Scan`) de Nmap.

```
# Enable OS Scan
nmap -O 10.10.10.0/24
```

Voici un exemple de résultat, ici Nmap nous indique qu’il s’agit probablement d’un OS Linux, il nous propose différentes statistiques concernant sa version exacte.

![nmap-image](assets/fr/38.webp)

_Détection de la probabilité d’identification d’un système d’exploitation par Nmap._

Pour établir ce résultat, Nmap va utiliser une multitude de techniques qui fonctionnent de manière très similaire aux _Probes_ et _Matches_ pour la détection de technologies et versions. La différence principale étant que Nmap utilisera des paramètres assez “bas niveau” des protocoles ICMP, TCP, UDP, etc. Voici deux exemples de test pour la détection d’un système d’exploitation Microsoft Windows 11 :

![nmap-image](assets/fr/39.webp)

_Exemples de tests réalisés par Nmap pour la détection d’un OS Windows 11._

Nous n’allons pas nous mentir, il est très difficile d’interpréter ces tests et nous n’allons pas chercher à les comprendre en profondeur dans le cadre d’un tutoriel d’introduction à Nmap. Si vous souhaitez creuser le sujet, sachez que le fichier contenant ces informations est `/usr/share/nmap/nmap-os-db`.

Il faut cependant être conscient que la détection d’un OS est plus une probabilité établie par Nmap qu’une certitude.

### VI. Conclusion

Dans cette section, nous avons appris à utiliser les options de Nmap permettant de détecter les technologies, versions et systèmes d’exploitation des services et hôtes scannés. Nous avons maintenant une bonne compréhension de la manière dont procède Nmap pour obtenir ces informations à distance. Nous avons également passé en revue les options pour gérer la verbosité et la précision des tests, ainsi que les limites de l’outil sur ces sujets.

Dans la prochaine section, nous allons apprendre à utiliser les scripts NSE de Nmap afin d’effectuer une analyse de sécurité de notre système d’information. Prenez le temps de relire les dernières sections si nécessaire, et n’hésitez pas à pratiquer et fouillez vous-même dans les entrailles de l’outil pour mieux maîtriser ce que nous avons appris jusqu’ici.


## 7 - Analyse de la sécurité : détection des vulnérabilités

### I. Présentation

Dans cette section, nous allons apprendre à utiliser l’outil de scan réseau Nmap afin de mener une détection ou analyse de vulnérabilités sur les cibles de nos scans. Nous découvrirons notamment les différentes options permettant d’accomplir cette tâche et étudierons les limites des capacités de l’outil afin de mieux comprendre et interpréter ses résultats.

Cette première section sera l’occasion d’introduire la recherche de vulnérabilités par Nmap, nous verrons comment utiliser de manière basique les options de détection de vulnérabilités. Cela nous permettra dans les prochaines sections d’étudier plus en détail le fonctionnement de cette fonctionnalité, ainsi que sa personnalisation.

### II. Utiliser Nmap pour détecter des vulnérabilités

Nous souhaitons à présent utiliser le scanner réseau Nmap afin de détecter des vulnérabilités sur les services et systèmes de notre système d’information. Cela signifie qu’en plus de faire une découverte des hôtes actifs, puis une énumération des services exposés et une détection des versions et technologies, Nmap cherchera détecter des vulnérabilités.

Pour réaliser cette tâche, Nmap se repose sur des scripts NSE (_Nmap Scripting Engine_), que l’on peut voir comme des modules qui permettent une approche granulaire des tests.

Avec les bonnes options, nous demanderons donc à Nmap d’utiliser ses différents scripts NSE sur chaque service découvert, permettant ainsi de découvrir :

- Des défauts de configuration ;
    
- Des découvertes additionnelles et plus avancées de version et OS ;
    
- Des vulnérabilités connues (CVE) ;
    
- Des identifiants faibles ;
    
- Des éléments caractéristiques d’une infection par un malware ;
    
- Des possibilités de déni de service ;
    
- Etc.
    

Vous l’aurez compris, les scripts NSE permettent d’étendre de manière importante les capacités de Nmap concernant les opérations réseau qu’il peut réaliser. Et ce pour faire des tâches bien plus avancées que celles réalisées jusque-là. La bonne nouvelle, c’est que comme d’habitude, ces fonctionnalités peuvent être utilisées simplement via une option et dans un contexte par défaut. C’est ce que nous allons voir par la suite.

### III. Exemple de scan de vulnérabilité

L’utilisation des scripts NSE peut être faite lors de l’utilisation de Nmap pour scanner un seul port sur un hôte, l’ensemble des services de cet hôte ou pour tous les services détectés sur plusieurs réseaux. Nous pouvons donc utiliser les options que nous allons voir dans l’ensemble des contextes d’utilisation étudiés jusque-là.

Pour activer la recherche de vulnérabilité via un scan Nmap, nous devons utiliser l’option `-sC` :

```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```

Attention, rappelez-vous que par défaut si on ne lui spécifie rien, Nmap ne va scanner que les 1000 ports les plus communs. Il ne fera donc pas de détection de vulnérabilité sur les ports plus exotiques que vos cibles pourraient exposer.

Avant d’utiliser cette fonctionnalité sur un système d’information de production, je vous invite à continuer la lecture du tutoriel. Nous verrons notamment dans les prochaines sections comment mieux maîtriser l’impact et les types de tests qui seront exécutés.

En réutilisant ce que nous avons appris précédemment, nous pouvons par exemple être plus complet et scanner la totalité des ports TCP d’une cible :

```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```

Voici le résultat d’un scan Nmap utilisant les scripts NSE :

![nmap-image](assets/fr/40.webp)

_Exemple de résultat d’un scan de vulnérabilités sur un hôte via Nmap._

Nous voyons ici l’affichage d’informations supplémentaires intéressantes dans le cadre d’une analyse de vulnérabilité :

- Le service FTP est accessible en mode anonyme, il n’est pas protégé par une authentification. Le script NSE en charge de cette vérification nous l’indique et nous affiche même une partie de l’arborescence du service FTP, nous voyons ici que nous avons accès au répertoire `C` du système Windows !
    
- Le script NSE en charge de la récupération avancée des services web nous affiche le titre de la page, ce qui permet de se faire une meilleure idée de ce que le service web héberge.
    
- Nous avons également une mini analyse de la configuration du service SMB (scripts `smb2-time`, `smb-security-mode` et `smb2-security-mode`). L’affichage des informations est un peu différent puisqu’elles sont présentes après le résultat du scan réseau pour une meilleure lisibilité. Ces informations nous indiquent notamment l’absence de signature des échanges SMB. Cette faiblesse de configuration permet d’utiliser la cible dans le cadre d’une attaque SMB Relay, un défaut de sécurité notable et souvent exploité dans le cadre de tests d’intrusion/cyberattaque.
    

Il ne s’agit là bien entendu que d’un exemple. Nmap possède des scripts NSE concernant de nombreux services et ciblant un grand nombre de vulnérabilités. Nous étudierons plus en profondeur ces nombreuses possibilités dans la prochaine section.

Pour finir sur cette introduction au scan de vulnérabilité, voici une commande complète de découverte réseau, scan de port TCP, détection de version et de vulnérabilités :

```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```

Voilà une commande qui commence à ressembler à des cas d’utilisation plus réalistes de Nmap !

### IV. Connaître les limites de Nmap dans la recherche de vulnérabilité

Que l’on soit clair, Nmap n’est pas en capacité de réaliser un test d’intrusion complet de votre système d’information ou de simuler une opération Red Team. Il possède plusieurs limites qu’il faut connaître pour ne pas avoir un faux sentiment de sécurité :

- **Couverture limitée** : bien que les scripts NSE de Nmap soient puissants, leur couverture de test peut être limitée par rapport à d'autres outils spécialisés dans la découverte de vulnérabilités. Certaines vulnérabilités peuvent ne pas être couvertes par les scripts NSE disponibles, je pense notamment aux vulnérabilités concernant l’Active Directory, l’exposition de données sensibles ou des cas plus poussés d’application web vulnérables.
    
- **Complexité des vulnérabilités** : certains types de vulnérabilités peuvent être difficiles à détecter à l'aide de scripts NSE en raison de leur complexité. Par exemple, les vulnérabilités nécessitant une interaction complexe avec un service distant peuvent ne pas être détectées efficacement par Nmap (cas de permissions excessives dans un partage de fichier ou d’un défaut de contrôle des permissions dans une application web).
    
- **Détection passive** : Nmap se concentre principalement sur les scans actifs pour détecter les vulnérabilités, ce qui signifie qu'il peut ne pas détecter efficacement les vulnérabilités potentielles sans établir de connexion active avec les hôtes cibles. Les vulnérabilités qui ne se manifestent pas lors d'un scan actif peuvent donc être manquées (cas d’une injection de code dans une application web).
    
- **Dépendance des mises à jour** : la [base de données](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) de scripts NSE de Nmap est en constante évolution, mais il peut y avoir un délai entre la découverte d'une nouvelle vulnérabilité et l'ajout d'un script correspondant à Nmap. Par conséquent, Nmap peut ne pas toujours être à jour avec les dernières vulnérabilités.
    
- **Faux positifs et faux négatifs** : comme avec tout outil de sécurité, les scripts NSE de Nmap peuvent produire des faux positifs (fausses alertes de vulnérabilités) ou des faux négatifs (vulnérabilités réelles non détectées). C’est un élément à garder en tête lors de l'analyse des résultats de Nmap.
    

Il est donc important de comprendre ce que fait Nmap et ce qu’il ne fait pas, et de la même manière de savoir bien interpréter ses résultats. Nous avons notamment vu tout au long de ce tutoriel que les options par défaut peuvent nous faire passer à côté d’éléments importants qu’une utilisation maîtrisée permet de découvrir.

En tant qu’administrateur système réseau, ingénieur sécurité ou même RSSI, l’utilisation de Nmap permet d’avoir un aperçu global, mais assez surfacique, de l’état de sécurité d’un système d’information. Il s’agit là d’une première étape importante de sécurisation qui peut être réalisée régulièrement par l’équipe informatique. Cependant, elle ne doit pas se substituer à l’intervention et l’avis d’experts en [cybersécurité](https://www.it-connect.fr/cours-tutoriels/securite-informatique/) qui sauront découvrir des faiblesses de manière bien plus complète que Nmap.

### V. Conclusion

Cette première section du module 3 nous a permis d’introduire le scan de vulnérabilités via Nmap. Nous savons à présent utiliser l’option principale pour réaliser cette tâche, mais connaissons aussi les limites de l’exercice. Dans la prochaine section, nous allons étudier plus en profondeur cette fonctionnalité en nous intéressant aux scripts NSE, qui permettent de décupler la puissance de Nmap.

## 8 - Utilisation des scripts NSE de Nmap

### I. Présentation

Dans cette section, nous allons étudier en profondeur les scripts NSE (_Nmap Scripting Engine_). Nous verrons notamment en quoi ils constituent l’une des grandes forces de cet outil, comment ils fonctionnent et comment parcourir et utiliser les nombreux scripts existants.

Cette section fait suite aux apprentissages précédents du tutoriel, dans lesquels nous avons appris à utiliser les fonctionnalités de recherche de vulnérabilité de Nmap de façon basique. Nous allons à présent étudier plus en profondeur le fonctionnement de [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) à ce sujet pour, encore une fois, réaliser des analyses plus précises et maîtrisées.

### II. Le concept des scripts NSE de Nmap

Les scripts NSE de Nmap permettent d’étendre ses capacités de manière très flexible. Ils sont écrits en langage LUA, un langage de scripting plus maniable et facile d’accès que le C ou le C# utilisé par Nmap. L’intérêt d’utiliser un script LUA avec Nmap plutôt qu’un outil seul est que cela nous permet de profiter de la rapidité d’exécution et des fonctionnalités standards de Nmap (découverte d’hôte, de ports, de versions, etc.).

Ces scripts sont organisés par catégorie et un seul script peut faire partie de plusieurs catégories :

| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples : `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples : `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples : `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples : `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples : `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples : `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples : `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples : `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples : `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples : `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples : `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples : `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples : `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Techniquement, les catégories auxquelles appartient un script sont indiquées directement dans son code.

![nmap-image](assets/fr/41.webp)

_Indication des catégories du script NSE `ftp-anon`._

Cet exemple montre une partie du code du script NSE `ftp-anon.nse`, dont nous avons vu le résultat d’exécution dans la section précédente.

### III. Lister les scripts NSE existants

Les scripts NSE de Nmap sont par défaut situés dans le répertoire `/usr/share/nmap/scripts/`, sans arborescence ou hiérarchie spécifique. Voici un aperçu du contenu de ce répertoire :

![nmap-image](assets/fr/42.webp)

_Extrait du contenu du répertoire `/usr/share/nmap/scripts/` contenant les scripts NSE._

Ce répertoire contient plus de 5 000 scripts NSE. Dans la majorité des cas, la première partie du nom de script contient le protocole ou la catégorie à laquelle il se rattache. Cela nous permet de faire un tri, par exemple si l’on souhaite lister tous les scripts qui visent le service FTP :

![nmap-image](assets/fr/43.webp)

_Liste des scripts NSE Nmap dont le nom commence par `ftp-`._

Nmap ne propose pas vraiment d’option pour parcourir et lister ses scripts NSE, vous pouvez utiliser la commande `--script-help` suivie du nom d’une catégorie ou d’un mot :

```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```

Cependant, le résultat de sortie sera l’affichage du nom de chaque script et sa description, ce qui n’est pas optimal si la recherche ressort plusieurs dizaines de scripts :

![nmap-image](assets/fr/44.webp)

_Résultat de l’utilisation de la commande `--script-help` de Nmap._

La méthode la plus efficace selon moi reste donc les commandes classiques Linux dans le répertoire `/usr/share/nmap/scripts/` :

```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```

N’hésitez pas à parcourir le code des modules qui vous parlent afin de mieux comprendre comment fonctionne un script NSE.

### IV. Utiliser les scripts NSE de Nmap

À présent, nous allons apprendre à réaliser des scans de vulnérabilités en choisissant finement les scripts NSE qui nous intéressent.

#### A. Sélectionner les scripts par catégories

Pour commencer, nous pouvons choisir d’exécuter tous les scripts appartenant à une catégorie précise. Nous devons indiquer cette ou ces catégories à Nmap avec l’argument `--script <catégorie>` :

```
# Use default NSE scripts
nmap --script default 10.10.10.152
```

Cette première commande est l’équivalent de la commande `nmap -sC`. Par défaut, Nmap va sélectionner les scripts qui sont dans la catégorie `default`, mais c’est pour l’exemple. La commande suivante va par exemple utiliser tous les scripts qui sont présents dans la catégorie `discovery` :

```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```

Comme nous l’avons vu, certaines catégories permettent d’identifier rapidement ce que font les scripts NSE qui s’y rattachent (`discovery`, `vuln`, `exploit`), alors que d’autres définissent le niveau de risque, de détection ou la stabilité du test réalisé. Si l’on est dans un contexte sensible et que l’on ne maîtrise pas bien les différentes actions réalisées par notre sélection de scripts, nous pouvons choisir de combiner les sélections pour ne choisir que les scripts qui sont dans les catégories `discovery` et `safe` :

```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```

Si l’on veut absolument et de manière explicite exclure les scripts des catégories `dos` et `intrusive`, il est possible d’utiliser la notation suivante :

```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```

Attention, le fait de spécifier des conditions d’exclusion comme ci-dessus entraînera l’utilisation de toutes les autres catégories qui ne sont pas explicitement exclues. Pour être plus juste, nous pouvons indiquer par exemple :

```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```

Voilà différents exemples qui vous permettront de manipuler plus précisément les scripts NSE par catégorie, notamment lors de l’utilisation de Nmap dans le cadre d’une analyse de vulnérabilité dans des contextes réels.

#### B. Sélectionner les scripts de façon unitaire

Nous pouvons également choisir de mener un seul test bien précis lors d’une analyse, un test correspondant à un script NSE. Pour cela, nous devons indiquer le nom du script dans le paramètre `--script <nom>`. Si l’on reprend l’exemple du script `ftp-anon.nse` :

```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```

Nous avons alors un résultat très précis :

![nmap-image](assets/fr/45.webp)

_Résultat de l’utilisation du script NSE `ftp-anon` sur un port FTP par Nmap._

Nous voyons le résultat de l’exécution du script `ftp-anon` sur le port 21, et aucun autre port, car nous avons spécifié l’option `-p 21`. Nous aurions aussi pu réaliser un scan de port basique, et l’exécution du script NSE `ftp-anon` seulement les services FTP découverts :

```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```

Ainsi, Nmap aurait également exécuté ce test de connexion anonyme s’il avait trouvé un service FTP sur un autre port.

Pour avoir une petite description de ce que fait un script NSE, vous pouvez utiliser l’option `--script-help` évoquée précédemment :

![nmap-image](assets/fr/46.webp)

_Résultat de l’affichage de l’aide pour le script NSE `sshv1`._

Bref, encore une fois, nous pouvons réutiliser ici toutes les options de découverte réseau, de services, version et technologies utilisées jusqu’ici !

#### C. Gérer les arguments de scripts

Au cours de votre utilisation de Nmap, vous rencontrerez certains scripts NSE qui nécessitent des arguments en entrée pour pouvoir fonctionner correctement. Nous allons à présent voir comment passer des arguments à ces scripts par l’intermédiaire des options de Nmap.

En exemple, nous allons prendre le script `ssh-brute`, qui permet d’effectuer une attaque par brute force sur le service SSH.

Une attaque par brute force classique consiste à tester plusieurs mots de passe (parfois des millions) pour tenter de s’authentifier sur un compte bien précis. À force de tenter des mots de passe, l’attaquant mise sur une probabilité que l’utilisateur ait utilisé un mot de passe faible qui serait dans le dictionnaire de mot de passe utilisé pour l’attaque.

Ce script possède des options “par défaut”, que nous pourrions personnaliser en fonction de notre contexte. Dans le cadre de cette attaque, nous pouvons par exemple fournir à Nmap la liste des utilisateurs et le dictionnaire de mot de passe à utiliser. À ma connaissance, il n’est pas possible de facilement lister les arguments nécessaires pour un script, le moyen le plus fiable reste le site web officiel de Nmap. Un lien direct vers la documentation d’un script NSE peut être obtenu en réponse à l’option `--script-help` :

![nmap-image](assets/fr/47.webp)

_Résultat de l’affichage de l’aide pour le script NSE `ssh-brute` avec un lien vers nmap.org._

En cliquant sur le lien indiqué, nous arrivons sur cette page web du site [https://nmap.org](https://nmap.org/) :

![nmap-image](assets/fr/48.webp)

_Liste des arguments pouvant être passés au script NSE `ssh-brute` de Nmap._

Ici, nous avons une vue claire des arguments pouvant être utilisés, les principaux dans notre contexte d’utilisation sont `passdb` (fichier contenant une liste des mots de passe) et `userdb` (fichier contenant une liste des utilisateurs). La documentation fait ici une référence à des librairies internes à Nmap, car ces mécanismes de brute force et les options associées sont mutualisés pour être utilisés de façon uniforme entre plusieurs scripts (`ssh-brute`, `mysql-brute`, `mssql-brute`, etc.) et auront donc à peu près les mêmes arguments :

```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```

Comme vous pouvez le voir dans cette dernière commande, nous pouvons spécifier les arguments nécessaires à un script Nmap en utilisant l’option `--scripts-args clé=valeur,clé=valeur`. Voici un résultat possible de la sortie Nmap lors de la réalisation d’un brute force SSH via le script NSE `ssh-brute` :

![nmap-image](assets/fr/49.webp)

_Résultat de l'exécution d'un bruteforce SSH via Nmap._

Comme vous le voyez, les informations générées par les scripts NSE sont préfixées par un `NSE : [nom du script]` dans l’interactive output (sortie terminal), ce qui permet de s’y retrouver plus facilement. Au sein de l’affichage habituel des résultats de Nmap, nous avons simplement une synthèse indiquant si oui ou non des identifiants faibles ont été découverts (incluant les mots de passe, il faut s’en souvenir).

Pour aller plus loin et rappeler que tout cela est utilisable en plus de toutes les options précédemment étudiées, voici une commande qui va réaliser une découverte du réseau `10.10.10.0/24`, scanner les 2000 ports TCP les plus fréquents et exécuter sur les services FTP une recherche d’accès en anonyme et sur les services SSH une campagne de brute force :

```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```

Ceci n’est qu’un exemple parmi les nombreux scripts disponibles et leurs options. Mais, nous avons à présent une meilleure idée de comment mieux appréhender les scripts NSE, savoir s’ils nécessitent des arguments et comment passer ces arguments à Nmap.

### V. Conclusion

Cette section nous a permis de manipuler et de comprendre comment concrètement utiliser les scripts NSE de Nmap pour réaliser différentes tâches. Je vous invite ici à prendre le temps de découvrir les différentes catégories de scripts et les scripts eux-mêmes pour vous rendre compte du nombre de tests qu’ils permettent d’automatiser.

Voilà plusieurs sections que nous accumulons les options de découverte, scan et énumération plus ou moins avancées. Vous devriez à présent vous rendre compte que l’affichage de sortie et des résultats Nmap commence à être bien fourni, parfois même trop verbeux pour notre terminal. Dans la prochaine section, nous allons apprendre à maîtriser cette sortie, notamment en la stockant dans des fichiers sous différents formats.




## 9 - Gérer les données de sortie de Nmap


### I. Présentation

Dans cette section, nous allons nous intéresser à la sortie produite par Nmap et notamment aux différentes options de formatage de cette sortie. Nous verrons que Nmap peut produire plusieurs formats de sortie afin de répondre à des besoins différents, et qu’il s’agit là aussi d’une des grandes forces de cet outil.

Nmap offre par défaut une vue détaillée des résultats des scans et tests qu'il effectue. Cela inclut les hôtes et services scannés, ceux qui sont détectés comme accessibles, les spécificités des ports ouverts, leur état et leur version. De plus, les détails des scripts NSE sont également disponibles dans la sortie du terminal. Cependant, cette sortie peut devenir rapidement volumineuse, même avec un formatage clair des informations, ce qui peut rendre difficile la recherche d’informations précises dans les résultats.

### II. Maîtriser les formats de sortie de Nmap

#### A. Enregistrer le résultat d’un scan dans un fichier texte

Pour nous faciliter la tâche, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) nous permet très facilement d’enregistrer sa sortie dans un fichier texte. Cela peut être utile pour de l’archivage, une comparaison avec d’autres tests, mais aussi pour parcourir cette sortie avec des outils de traitement de texte spécialisés ou des langages de scripting, je pense notamment à Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, etc. Pour stocker la sortie standard de Nmap dans un fichier texte, nous pouvons utiliser l’option `-oN <nom du fichier>` (le "N" de "normal") :

```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```

Dès lors, pas de surprise, Nmap affichera une sortie standard comme à son habitude dans notre terminal, mais également dans le fichier indiqué.

#### B. Générer une sortie Nmap dans un format condensé

Il existe également un second format de sortie dans le style “texte” et interprétable facilement par un humain : le format “greppable”.

Ce format a été créé afin de fournir une vue “condensée” de la sortie Nmap, notamment structurée de manière à faciliter son traitement par des outils comme `grep`. Voyons un exemple de ce type de résultat :

![nmap-image](assets/fr/50.webp)

_Scan réseau Nmap et sortie au format "greppable"._

Ici, j’ai réalisé une découverte réseau ainsi qu’un scan de port et une analyse des technologies et versions sur un réseau en /24, puis j’ai stocké la sortie dans un fichier au format “greppable”. Je me retrouve avec un fichier contenant 2 lignes par hôte actif :

- Une première ligne pour m’indiquer que tel hôte est _Up_;
    
- Une seconde ligne pour m’indiquer les ports scannés, leur statut et les informations de technologies et versions récupérées dans un format bien particulier : `<port>/<status/<protocol>//<service>//<version>/,`
    

Ce formatage à l’aide d’un délimiteur fixe permet un traitement rapide par des outils de traitement de texte tels que `grep`, ou des langages de scripting et programmation. La commande suivante me permet par exemple de retrouver facilement les informations de l’hôte `10.10.10.5` dans le cas d’un énorme scan réalisé par Nmap et dont la sortie serait difficile à parcourir :

```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```

À l’inverse, je peux aussi facilement lister tous les hôtes qui ont un port 21 d’ouvert, car ports et IP sont sur la même ligne :

```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```

Pour générer une telle sortie, nous devons utiliser l’option `-oG <nom du fichier>.gnmap` (le "G" de "grep"). Par habitude, j’utilise ici l’extension `.gnmap` pour un tel fichier, mais libre à vous d’utiliser celle que vous souhaitez :

```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```

Ce format peut répondre à plusieurs besoins et est plutôt pratique pour du scripting/tri rapide. Néanmoins, il tend à être délaissé au profit du format que nous allons voir juste après.

_Remarque : le format greppable `-oG` est officiellement déprécié depuis Nmap 7.90. Il reste utilisable pour compatibilité, mais il est conseillé de privilégier le format XML ou normal pour tout développement ou parsing automatisé._

#### C. Le format XML des sorties Nmap

Le dernier format qui mérite d’être mentionné dans ce tutoriel est le format XML. Au contraire des deux formats précédents, celui-ci n’est pas fait pour être lu par des humains, mais par d’autres outils ou des scripts.

Le format XML (_eXtensible Markup Language_) est un langage de balisage utilisé pour stocker et transporter des données, offrant une structure hiérarchique via des balises personnalisées.

Dans le cadre de Nmap, le format XML est utilisé pour générer des rapports détaillés sur les analyses et scans effectués, incluant des informations sur les hôtes, les ports et les vulnérabilités détectées, mais aussi des informations additionnelles qui ne sont pas affichées dans la sortie standard de Nmap.

Pour générer un fichier de sortie au format XML, nous devons utiliser l’option `-oX` ("O" de "XML") :

```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```

Vous trouverez alors en résultat la sortie standard de Nmap dans votre terminal, ainsi qu’un fichier au format XML dans votre répertoire courant.

Le format XML n’est bien sûr pas fait pour être lu et interprété par un humain. Néanmoins, si vous souhaitez faire du scripting ou de l’analyse automatisée sur ce format de la sortie Nmap, il faut quand même avoir une idée des balises et de la structure utilisée. Par exemple, voici une partie du contenu du fichier XML créé par Nmap, il expose les résultats du scan pour 1 hôte :

![nmap-image](assets/fr/51.webp)

_Exemple d’un enregistrement au format XML pour 1 hôte lors d’un scan Nmap._

Nous voyons ici beaucoup d’informations, nous pouvons notamment nous intéresser aux deux ports ouverts :

```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```

Nous comprenons bien que ce format va nous faciliter le parsing automatisé des résultats, chaque information est bien rangée dans une balise ou un attribut dédié et nommé. Nous retrouvons notamment une information que nous n’avons pas croisée jusqu’ici : le CPE.

```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```

Nous avons rapidement mentionné le CPE dans la section 2 du module 2, cette information est notamment déterminée dans les matches lors de la détection de version. Nmap se sert de ses mécanismes de détection de services, de technologies et de versions afin de retrouver le CPE associé.

Cela nous permet par la suite de réutiliser cette information avec les bases de données et applications qui l’utilisent. Je pense notamment à la base NVD qui référence les CVE. Elle contient, pour chaque CVE, les CPE concernés par la vulnérabilité. Voici un exemple de CVE concernant le `a:microsoft:internet_information_services:7.5` venant de la base NVD :

![nmap-image](assets/fr/52.webp)

_Présence d’un CPE dans les détails d’une CVE de la base NVD._

Nous comprenons à présent mieux l’intérêt de ce format, il propose une structure très claire des informations et contient toutes les données récoltées ou traitées par Nmap.

Par réflexe, j’effectue systématiquement un enregistrement de mes scans Nmap dans les trois formats d’un seul coup. Cela est possible grâce à l’option `-oA <nom>` ("A" pour "All"), qui créera un fichier `<nom>.nmap`, un fichier `<nom>.xml` et un fichier `<nom>.gnmap`. Ainsi je suis sûr de ne manquer de rien quand il faudra revenir sur les résultats.

Avec ces trois formats, vous devriez avoir tout ce qu’il faut pour enregistrer, puis éventuellement traiter de façon automatisée les résultats de Nmap. Nous réutiliserons notamment le format XML dans la section suivante, quand nous aborderons l’utilisation de Nmap avec d’autres outils de sécurité.

#### III. Générer un rapport HTML d’un scan Nmap

Le format XML offre de nombreuses possibilités, notamment celle de servir de base à la génération d’un rapport au format HTML, qui sera visuellement plus agréable à parcourir.

Pour transformer un fichier Nmap au format XML en page web, nous allons utiliser l’outil `xsltproc`, qu’il nous faudra au préalable installer :

```
# Install the xsltproc tool
sudo apt install xsltproc
```

Une fois cet outil installé, il suffit de lui fournir en entrée le fichier XML à convertir, ainsi que le nom du rapport HTML à générer :

```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```

En résultat, nous aurons l’intégralité de notre scan joliment structuré, avec même quelques couleurs et des liens cliquables dans le sommaire !

![nmap-image](assets/fr/53.webp)

_Extrait d’un rapport de scan Nmap au format HTML généré par xsltproc._

Dans les grandes lignes, il faut savoir que le fichier XML enregistré par Nmap contient une référence vers un autre fichier, au format XSL :

```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```

La conversion en HTML est donc une fonction prévue et facilitée par Nmap, `xsltproc` étant un outil commun et reconnu pour effectuer cette tâche (qui ne provient pas de la suite d’outil Nmap).

Le langage XSLT (_Extensible Stylesheet Language Transformations_) est un sous-ensemble du langage XSL qui permet d’afficher des données XML sur une page web et de les « transformer », parallèlement aux styles XSL, en informations lisibles et mises en forme au format HTML.

_Source : [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_

Le niveau d’information du rapport est équivalent à celui du format XML de Nmap et supérieur à celui de la sortie standard dans le terminal (_interactive output_).

### IV. Gérer le niveau de verbosité de Nmap

Nous allons à présent passer en revue quelques options qui vous permettront de debugger Nmap ou d’obtenir un suivi précis de son avancement.

La première option que l’on peut mentionner est l’option `-v`, qui permet d’augmenter la verbosité de Nmap, voici un exemple :

![nmap-image](assets/fr/54.webp)

_Sortie verbeuse de Nmap grâce à l’option `-v`._

Sur un scan ciblant de nombreux hôtes et ports, la sortie terminal deviendra difficile à exploiter en raison du nombre d’informations affichées. C’est pourquoi il convient d’utiliser cette option en combinaison avec les options vues précédemment qui permettent de stocker la sortie standard de Nmap dans un fichier. Les informations liées à l’utilisation de la verbosité ne seront pas incluses dans ce fichier de sortie. Comme vous le voyez dans l’exemple ci-dessus, cette verbosité permet d’avoir un suivi assez clair et en direct des actions et découvertes de Nmap. Pour des scans assez longs où l’affichage des données peut tarder à venir, cela évite d’être à l’aveugle sur l’activité actuelle de Nmap et de savoir que les choses avancent et à quel rythme. Pour augmenter la verbosité d’un niveau supplémentaire, il est possible d’utiliser l’option `-vv`.

Pour aller plus loin sur le suivi de l’activité de Nmap pendant son scan, il est possible d’utiliser l’option `--packet-trace`. Avec l’option `-v`, nous obtenons en live les ports ouverts découverts par Nmap alors qu’avec cette option, nous aurons une ligne de log pour chaque paquet envoyé sur un port. Cela produit naturellement une sortie très verbeuse, mais permet un suivi détaillé de l’activité de Nmap, voici un exemple :

![nmap-image](assets/fr/55.webp)

_Suivi détaillé de l’activité de Nmap via `--packet-trace`._

À nouveau, ces informations ne seront pas enregistrées dans le fichier de sortie produit par Nmap si l’on utilise les options `-oN`, `-oG`, `-oX` ou `-oA`.

Enfin, Nmap dispose également de deux options de debug qui sont `-d` et `-dd`. Ces options ont un comportement similaire à l’option de verbosité `-v`, mais ajoutent des informations techniques supplémentaires, comme une synthèse des paramètres techniques en début de scan :

![nmap-image](assets/fr/56.webp)

_Affichage des options de Timing par la vue “debug” de Nmap._

Nous verrons notamment dans les prochaines sections ce que sont les options de “Timing” et pourquoi il est intéressant de les connaître.

Enfin, pour avoir uniquement un suivi basique et synthétique de l’avancée du scan Nmap, nous pouvons utiliser l’option `--stats-every 5s`, le "5s" signifie ici 5 secondes et peut être modifié en fonction de vos besoins. Il s’agit de la fréquence à laquelle nous aurons un retour de Nmap sur son avancement :

![nmap-image](assets/fr/57.webp)

_Informations affichées par l’option `--stats-every` de Nmap._

Nous pouvons notamment avoir un pourcentage d’avancée, ainsi qu’une indication de la phase à laquelle il se trouve : phase de découverte d’hôte via [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), phase de découverte des ports TCP exposés, etc. Ces informations peuvent également être obtenues dans la sortie terminal en appuyant sur "Entrée" pendant un scan.

Cependant, il faut savoir que Nmap n’est pas très bon pour estimer le temps que va lui prendre une tâche, notamment parce qu’il ne sait pas à l’avance le nombre d’hôtes et de services qu’il va avoir à scanner.

### V. Conclusion

Dans cette section, nous avons vu plusieurs options qui nous permettent d’enregistrer les résultats d’un scan Nmap dans différents formats de fichier. Cela vous sera très utile, car dans des contextes réalistes, les résultats de scan peuvent occuper plusieurs centaines, voire milliers de lignes ! Nous avons également vu comment augmenter le niveau de verbosité de Nmap dans le cadre du debug ou pour obtenir un état d’avancement du scan.

D’ailleurs, le format XML nous sera particulièrement utile pour la section suivante dans laquelle nous aborderons quelques outils capables de travailler sur les résultats de Nmap.


## 10 - Utiliser Nmap avec d’autres outils de sécurité

### I. Présentation

Dans cette section, nous allons passer en revue différents cas classiques d’utilisation de Nmap avec d’autres outils de sécurité gratuits et open source. Nous utiliserons notamment ce qui a été appris dans les sections précédentes et cela nous permettra de renforcer encore plus la puissance et l’efficacité de Nmap.

La possibilité d’enregistrer les résultats d’un scan Nmap en XML rend de fait compatible ses données avec un tas d’autres outils. La quasi-totalité des langages de programmation et de scripting possédant des librairies capables de parser du XML aujourd’hui, cela facilite grandement le traitement de ces données. Plusieurs outils, orientés sécurité offensive notamment, possèdent des fonctions de traitement du format XML généré par Nmap. Voyons cela plus en détail.

Je vais évoquer quelques outils offensifs sans vraiment détailler leur usage ou leur fonctionnement, je partirai du principe que le lecteur en connaît l’usage basique et qu’ils sont déjà opérationnels. Cette section intéressera surtout les professionnels de la [cybersécurité](https://www.it-connect.fr/cours-tutoriels/securite-informatique/), les personnes en formation ou ayant décidé d’approfondir le sujet.

### II. Importer les résultats de Nmap dans Metasploit

Le premier outil que nous allons traiter au sujet de la réutilisation des données de Nmap dans le cadre de la sécurité offensive et la recherche de vulnérabilité est Metasploit.

Metasploit est un framework d’exploitation et d’attaque. Il s’agit d’une solution gratuite et d’un outil reconnu qui contient de très nombreux modules écrits en Ruby ou en Python. Ceux-ci permettent d’exploiter des vulnérabilités, d’opérer des attaques, de générer des backdoors, de gérer leur callback (fonction de C&C ou Communication and Control) et d’utiliser le tout de manière uniforme.

Ce framework d’exploitation très connu et très utilisé peut notamment travailler avec une [base de données](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) postgreSQL dans laquelle vont être stockés les hôtes, ports, services, informations d’authentification et autres.

- Documentation officielle de Metasploit : [https://docs.metasploit.com/](https://docs.metasploit.com/)
    

C’est ici que Nmap et sa sortie entrent en jeu, car le format XML de la sortie Nmap peut être importé très facilement dans la base de données de Metasploit afin d’alimenter sa base d’hôtes et de services, qui pourront alors rapidement être désignés comme cibles de telle ou telle attaque.

Une fois dans mon shell interactif Metasploit, je commence par créer un workspace, sorte d’espace propre à mon environnement du jour :

```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```

Une fois mon workspace créé, nous devons valider que la communication avec la base de données est opérationnelle :

```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```

Enfin, nous pouvons utiliser la commande Metasploit `db_import` pour importer notre scan Nmap au format XML :

```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```

Voici le résultat de l’exécution de l’ensemble de ces commandes :

![nmap-image](assets/fr/58.webp)

_Import d’un scan Nmap au format XML dans la base de données Metasploit._

Vous voyez ici que chaque hôte est importé, avec ses services. Ces données peuvent alors être affichées via la commande `services` ou `services -p <port>` pour un service spécifique :

![nmap-image](assets/fr/59.webp)

_Liste des services importés du fichier XML dans la base de données Metasploit._

Enfin, nous pouvons très facilement et rapidement réutiliser ces données dans un module grâce à l’option `-R`, qui va “convertir” la liste des services obtenue en entrée pour la directive `RHOSTS`, qui permet justement de spécifier les cibles de l’attaque à mener. Voici un exemple avec le module `ssh_login` qui permet d’effectuer une attaque par brute force sur les services [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/) :

![nmap-image](assets/fr/60.webp)

_Utilisation de l’option `services -R` pour importer les services spécifiés comme cible de l’attaque._

Ceci n’est qu’un petit exemple de ce qu’il est possible de faire grâce aux données de Nmap dans Metasploit, mais il permet de vous donner une petite idée de comment ces informations peuvent être très rapidement et facilement réutilisées dans le cadre d’un test d’intrusion, recherche de vulnérabilité ou cyberattaque. Il est aussi intéressant de mentionner que Nmap peut être directement exécuté depuis Metasploit pour un import des résultats dans la base de données (commande `db_nmap`), encore un sujet intéressant à traiter !

### III. Utiliser Nmap avec le scanner web Aquatone

Le second outil que je souhaite vous présenter dans cette section sur la réutilisation des résultats de Nmap dans la cadre de la sécurité offensive et l’analyse de vulnérabilité est Aquatone.

Aquatone est un scanner web conçu pour explorer efficacement les applications web d'un réseau. Il propose des fonctionnalités avancées pour la découverte des services web, l'identification des sous-domaines, l'analyse des ports et une prise d’empreinte des applications web. Le tout présenté de manière claire et concise dans des rapports au format HTML, JSON et texte afin de faciliter l'analyse de la sécurité web.

Comme pour Metasploit, Aquatone est capable de traiter directement le format XML de Nmap pour s’en servir de cible à scanner. Il sait notamment extraire uniquement les hôtes et services qui l’intéressent (les services web) parmi toutes les données qu’un rapport Nmap peut contenir.

- Lien de l’outil : [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)
    

Pour utiliser la sortie XML de Nmap avec Aquatone, il suffit d’envoyer le fichier XML dans un pipe qui sera consommé par Aquatone, voici un exemple :

```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```

Là où Aquatone fait normalement une découverte des ports sur les hôtes pour y trouver des services web, il va dans ce contexte uniquement se baser sur les résultats de Nmap qui a déjà fait cette opération, ce qui représente un gain de temps :

![nmap-image](assets/fr/61.webp)

_Utilisation d’un résultat Nmap au format XML avec `aquatone`._

Voici, pour information, un extrait du rapport produit par Aquatone :

![nmap-image](assets/fr/62.webp)

_Exemple de rapport `aquatone`._

À titre personnel, j’utilise souvent Aquatone pour avoir une vue rapide sur les types de sites web présents sur le réseau, notamment grâce à sa fonctionnalité de screenshot.

Là encore, le fait d’avoir un rapport Nmap complet au format XML permet de gagner du temps et de facilement le réutiliser dans un autre outil.

### IV. Conclusion

Nous voyons bien à travers ces deux exemples que le format XML de Nmap facilite l’utilisation de ses résultats par d’autres outils, car il s’agit d’un format de données structuré et utilisable facilement. Il existe bien d’autres outils capables de traiter ces résultats, comme des outils de reporting automatisés, de représentation graphique ou des scanners de vulnérabilité plus complexes et propriétaires.

Il est bien entendu tout à fait possible de développer vos propres scripts et outils en Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) ou autre langage possédant une librairie de parsing XML pour manipuler et réutiliser à votre guise les données des résultats Nmap.

Cette section nous permet de clore le module du tutoriel concernant une utilisation plus avancée de Nmap, notamment pour la recherche de vulnérabilité à travers les scripts NSE.

La prochaine section du tutoriel sera orientée, entre autres, autour de quelques bonnes pratiques et astuces supplémentaires, plus techniques, sur les scans spécifiques que permet de réaliser Nmap. Nous y étudierons aussi les options d’optimisation de la performance des scans, très utiles à connaître pour les scans sur de larges réseaux.


## 11 - Améliorer les performances d’un scan réseau

### I. Présentation

Dans ce chapitre, nous allons apprendre à optimiser la vitesse des scans réseau réalisés avec Nmap en utilisant différentes options spécifiques. Ce chapitre sera notamment l’occasion d’en apprendre plus sur le fonctionnement interne de Nmap, de la gestion des _timeouts_ aux configurations préenregistrées dans l’outil.

Maintenant que nous avons fait un bon tour d’horizon des fonctionnalités de Nmap, nous allons apprendre à maîtriser la bête et sa puissance. Si vous avez déjà utilisé l’outil sur de larges réseaux, vous vous êtes sûrement aperçu que certains scans peuvent être longs, malgré la puissance de l’outil. Et pour cause, une simple commande `nmap` avec quelques options peut générer des millions de paquets ciblant des centaines de milliers de systèmes et services potentiels.

De plus, certaines configurations d’équipement réseau peuvent intentionnellement imposer un ralentissement de la cadence (nombre de paquets par seconde), au risque de rejeter vos paquets ou bannir votre adresse IP pour des raisons de sécurité.

En fonction des contextes, il peut être intéressant de chercher à optimiser tout cela, c’est ce que nous allons voir dans ce chapitre.

Dans tous les cas, sachez que vous pouvez consulter les valeurs par défaut des paramètres que nous allons voir ainsi que la bonne prise en compte des options que vous allez utiliser via le debug de Nmap (option `-d` vue dans un précédent chapitre) :

![nmap-image](assets/fr/63.webp)

_Visualisation des options de Timing via l’option `-d` de Nmap._

### II. Gérer la rapidité des scans Nmap

#### A. Gérer la parallélisation

Par défaut, Nmap utilise la parallélisation dans ses scans pour les optimiser et tous les paramètres qu’il utilise sont modifiables via différentes options. Cependant, les cas où la modification de ces paramètres est réellement nécessaire sont assez rares, nous n’allons donc pas les aborder en détail dans ce tutoriel :

- `--min-hostgroup/max-hostgroup <size>` : taille des groupes de scans d'hôtes en parallèle.
    
- `--min-parallelism/max-parallelism <numprobes>` : parallélisation des Probes.
    
- `--scan-delay/--max-scan-delay <time>` : ajuste le délai entre les Probes.
    

Sachez simplement qu’ils existent et peuvent être utilisés.

#### B. Gérer le nombre de paquets par seconde

Par défaut, Nmap va ajuster lui-même le nombre de paquets par seconde qu’il va envoyer en fonction de la réaction du réseau. Mais il est possible de forcer ce paramétrage en définissant la valeur haute et/ou minimale à suivre en termes de nombre de paquets par seconde. Ce paramétrage se fait à l’aide des options `--min-rate <nombre>` et `--max-rate <nombre>` où `nombre` représente un nombre de paquets par seconde. Exemple :

```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```

Ces options permettent de régler la rapidité des scans en fonction des besoins spécifiques, que ce soit pour accélérer le processus, soit pour limiter la bande passante utilisée. Le second cas de figure (limiter la vitesse des scans) est celui qui vous amènera sûrement en priorité vers ces options, notamment si vous constatez des latences réseau au moment de l’utilisation de Nmap (ce qui reste assez rare).

### III. Gérer les échecs de connexions et timeout

Un autre paramètre sur lequel nous pouvons jouer pour optimiser la vitesse des scans Nmap (ou garantir une meilleure précision) concerne les _timeout_ et les _retry_.

Il s’agit, pour les _timeouts_, du **délai d’attente sans réponse** au-delà duquel Nmap cessera d’attendre une réponse et considérera le service ou l’hôte comme non joignable. Pour les _retry_, il s’agit du **nombre d'essais successifs d’une opération** que Nmap va réaliser avant de passer à autre chose.

Comme pour la parallélisation, la gestion du _timeout_ et du _retry_ peut porter sur les phases de découverte de l’hôte ou des services :

- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <temps>` : spécifie le temps aller-retour d’un échange. À nouveau, ce paramètre est dans les faits calculé et adapté à la volée durant le scan. Il est peu probable que vous ayez à l’utiliser, Nmap calculant à la volée ce temps en fonction de la réaction du réseau.
    
- `--max-retries <nombre>` : limite le nombre de retransmissions d’un paquet lors du scan de port. Par défaut, Nmap peut aller jusqu’à 10 essais pour un même service, notamment s'il constate des latences ou pertes au niveau réseau, mais dans la plupart des cas, un seul est réalisé.
    
- `--host-timeout <temps>` : spécifie le temps maximum que Nmap va passer sur un hôte pour l'ensemble de ses opérations, y compris le scan de ports, la détection de services, et toute autre opération liée à cet hôte. Si cet intervalle de temps est dépassé sans réponse ou **sans achèvement des opérations**, Nmap abandonnera cet hôte sans afficher aucun résultat le concernant, et passera au suivant dans sa liste. Cela permet de contrôler la durée maximale que Nmap consacre à un hôte donné, évitant ainsi de rester bloqué sur des hôtes récalcitrants et permettant d'optimiser le temps de scan global.
    

Dans mes usages courants, j’utilise en priorité les options `--max-retries`, et `--host-timeout` pour optimiser mes scans :

```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```

Ces paramètres offrent une flexibilité supplémentaire pour ajuster les comportements de scan en fonction des besoins spécifiques et des conditions du réseau. Il faut cependant bien être conscient de ce qu’ils impliquent en termes de charge sur les hôtes scannés et en termes de perte potentielle de précision.

### IV. Utilisation des configurations préparamétrées

Les différentes options que nous avons vues dans ce chapitre peuvent être utilisées individuellement ou dans le cadre de configurations préparamétrées proposées par Nmap. L’option qui permet l’utilisation de ces _templates_ (modèles de configuration) est `-T <numéro>` ou `-T <nom>`. Il existe 5 niveaux _templates_ utilisables :

```
-T<0-5>: Set timing template (higher is faster)
```

Par défaut, Nmap utilise le _template_ 3 (_normal_), qui est en général suffisant.

Pour ma part, j’opère généralement dans des contextes où il faut être assez rapide (tout en restant aussi complet que possible) et j’utilise fréquemment l’option `-T4`.

```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```

Voici ce que nous affichent les informations de debug concernant ce scan :

![nmap-image](assets/fr/64.webp)

_Utilisation du préparamétrage `-T4` lors d’un scan Nmap._

### V. Conclusion

Dans ce chapitre, nous avons vu différentes techniques et options utilisables afin de gérer la puissance, l’agressivité et la performance de Nmap. Ces options vous seront utiles notamment lors de scans sur de larges réseaux, et plus rarement pour gagner en discrétion.

Dans le prochain chapitre, nous allons passer en revue quelques bonnes pratiques concernant l’utilisation et la sécurité lors de l’utilisation de Nmap.


## 12 - Sécurité et confidentialité des données lors de l’utilisation de Nmap

### I. Présentation

Dans ce chapitre, nous allons nous rappeler de différentes bonnes pratiques à adopter concernant la sécurité et surtout la confidentialité des données produites, traitées et stockées par Nmap.

L’utilisation de Nmap au sein d’un système d’information peut rapidement être catégorisée comme une action offensive. En conséquence, plusieurs précautions sont à prendre pour agir dans un cadre légal, mais garantir la sécurité des cibles visées, des données récoltées et du système utilisé pour le scan.

### II. Obtention d'autorisations appropriées

Avant de scanner un réseau ou un système, assurez-vous d'avoir obtenu les autorisations appropriées. Scanner des systèmes notamment pour y détecter des vulnérabilités (`scripts NSE`) sans autorisation peut être illégal et entraîner des conséquences juridiques, notamment si la sécurité du système d’information n’est pas dans vos attributions officielles.

- Pour rappel : [Code pénal : Chapitre III : Des atteintes aux systèmes de traitement automatisé de données](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)
    

### III. Protéger les données sensibles

Les résultats produits par Nmap peuvent être considérés comme sensibles, notamment lorsqu’ils contiennent des informations sur les faiblesses du système d’information pouvant être exploitées par un attaquant. Mais aussi lorsqu’ils concernent des systèmes qui ne sont pas accessibles par tous (exemple : SI sensible, industriel, de santé, de [sauvegarde](https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).

Nous avons également vu qu’en fonction des `scripts NSE` utilisés, les résultats de scan NSE de [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) peuvent aussi contenir des identifiants.

Ainsi, un individu malveillant qui parvient à accéder à ces résultats de scan aura sous la main une cartographie du système d’information et des nombreuses informations techniques, sans avoir lui-même effectué ces actions au risque de se faire détecter.

Il est donc important de veiller à ne pas collecter ou stocker de manière inappropriée des informations sensibles lors de l'utilisation de Nmap, cela inclut, entre autres, les points suivants :

- Chiffrement des données de sortie : si vous avez besoin de stocker ou de transmettre les résultats de vos scans Nmap, assurez-vous de les chiffrer pour protéger la confidentialité des données. Cela empêchera toute interception non autorisée des informations sensibles. Dans l’idéal, les données devront être chiffrées dès leur sortie du système utilisé pour la réalisation du scan (une archive ZIP chiffrée avec un mot de passe robuste sera un très bon début).
    
- Mise en place de contrôles d'accès : assurez-vous que seules les personnes autorisées ont accès aux résultats de vos scans Nmap à l’endroit où ils seront stockés. Mettez en place des contrôles d'accès appropriés pour protéger les informations sensibles contre les accès non autorisés.
    
- Vigilance sur la manipulation des données : lors du transit, de la copie, du traitement des données de scan, assurez-vous de maîtriser strictement la sécurité des données. Cela signifie ne pas les laisser traîner dans le répertoire `Téléchargement` d’un poste connecté à Internet, ne pas les faire transiter au travers de votre application interne d’échange de fichier en HTTP, ne pas laisser votre Notepad ouvert sans verrouillage du poste pendant la pause midi, etc.
    

### IV. Maitriser l’agressivité des scans

Nous l’avons vu tout au long du tutoriel, Nmap peut être très verbeux au niveau réseau. Également, il peut être amené à envoyer des paquets qui ne sont pas bien formatés et qui ne respectent pas à la lettre la structure des protocoles dans les trames et paquets réseau qu’il génère. Toutes ces actions peuvent avoir un impact sur certains systèmes et services, parfois jusqu’à causer un dysfonctionnement ou une saturation des ressources système et réseau.

Il convient donc, pour éviter tout incident, de maîtriser le comportement de Nmap et de savoir l’adapter au contexte dans lequel il est utilisé via les différentes options vues dans ce tutoriel. Nous n'utiliserons pas forcément Nmap de la même manière sur un système d’information contenant du [matériel](https://www.it-connect.fr/actualites/actu-materiel/) industriel que dans un réseau utilisateur composé de systèmes Windows protégés par un pare-feu local ou dans un coeur de réseau.

Les différents apprentissages du tutoriel vous ont, je l’espère, appris à maîtriser et analyser le comportement de Nmap, mais le meilleur apprentissage reste la pratique. Assurez-vous donc de correctement maîtriser les options de Nmap que vous utiliserez.

### V. Protéger le système de scan

Le premier chapitre nous a permis de voir que Nmap nécessite dans la majorité des cas une exécution en tant que `root` ou administrateur local. Cela, car il réalise des opérations réseau parfois assez bas niveau au travers des librairies réseau, ce qui nécessite des permissions élevées et risquées du point de vue de la stabilité du système ou de la confidentialité des autres applications.

Ainsi, Nmap peut être vu comme un composant sensible du système sur lequel il est installé. Assurez-vous d'utiliser la dernière version de Nmap, car les versions plus anciennes peuvent contenir des vulnérabilités de sécurité connues. En utilisant une version à jour, vous pouvez minimiser les risques liés à l'utilisation de l'outil.

Si vous avez opté pour une utilisation de Nmap non pas via une session en tant que `root`, mais en accordant des privilèges spécifiques à un utilisateur privilégié pour qu’il ait tout ce dont il a besoin pour utiliser Nmap (`sudo` ou _capabilities_), sachez que Nmap peut être utilisé dans le cadre d’une élévation de privilège complète :

![nmap-image](assets/fr/65.webp)

_Élévation de privilèges Nmap via `sudo`._

Ici, j’utilise la commande Nmap à travers `sudo`, mais cela me permet d’obtenir un shell interactif en tant que `root` sur le système, ce qui n’était pas l’objectif initial.

Également il est vivement déconseillé d’installer Nmap sur des systèmes qui ne sont pas prévus pour réaliser des scans réseau à la base. Je pense notamment aux serveurs ou postes de travail. Cela ajouterait d’une part un vecteur potentiel d’élévation de privilège, mais surtout donnerait à l’attaquant un accès à un outil offensif sans effort.

Enfin, la sécurité du système utilisé pour le scan doit être assurée de façon plus large afin qu’il ne soit pas lui-même vecteur d’une intrusion ou d’une fuite d’informations. En tant qu’administrateur système, préférez utiliser un système dédié, idéalement avec une durée de vie limitée, plutôt que votre propre poste de travail.

### VI. Conclusion

En conclusion, assurez-vous de correctement maîtriser Nmap avant toute utilisation dans des conditions réelles ou de production et soyez vigilant concernant le traitement et la gestion de ses résultats. Il serait dommage de causer des dommages, d’entraîner une fuite de données ou de faciliter une compromission alors que la démarche initiale va dans le sens d’une amélioration de la sécurité de son entreprise.

## 13 - Les scans de port via TCP : SYN, Connect et FIN

### I. Présentation

Dans ce chapitre et le suivant, nous allons étudier plus en profondeur les différents types de scan TCP qui sont disponibles dans Nmap, en commençant par les plus utilisés qui sont les scans SYN, Connect et FIN.

Vous l’aurez peut-être remarqué, mais Nmap propose plusieurs options en ce qui concerne les scans TCP :

![nmap-image](assets/fr/66.webp)

_Techniques de scan disponibles dans Nmap._

L'idée est donc d'expliquer certaines de ces méthodes afin de comprendre leur différence, leur intérêt et leur limite. Ainsi, vous verrez qu’en fonction des contextes ou de ce que l’on souhaite savoir, il vaut mieux opter pour une option ou pour une autre.

### II. Le TCP SYN scan ou "Half Open scan"

Le premier type de scan TCP que nous allons voir est le `TCP SYN Scan`, aussi appelé `Half Open Scan` (signifiant "_à moitié ouvert_"). Si vous vous rappelez des analyses réseau faites à la suite de nos premiers scans de port, il s’agit du type de scan utilisé par défaut par [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) lorsqu’il est exécuté avec les droits `root`.

La traduction aide bien à comprendre le fonctionnement de ce scan. En effet, un TCP SYN scan va envoyer sur chaque port ciblé un paquet `TCP SYN`, qui est donc le premier paquet qu'envoie un client (celui qui demande à établir une connexion) dans le cadre du fameux _Three way handshake_ TCP. En temps normal, si le port est ouvert sur le serveur cible avec un service tournant derrière, celui-ci va renvoyer un paquet `TCP SYN/ACK` permettant de valider la SYN du client et d'initialiser la connexion TCP. Cette réponse prend la forme d’un paquet TCP avec les flags SYN et ACK à 1, on pourra alors affirmer que le port est ouvert et mène à un service.

En revanche, si le port est fermé, le serveur nous renverra un paquet `TCP` avec les flags RST et ACK à 1 pour mettre fin à la demande de connexion, on saura alors qu'aucun service ne semble être actif derrière ce port :

![nmap-image](assets/fr/67.webp)

_Schéma des comportements lors d'un TCP SYN Scan pour un port ouvert et fermé._

Pour avoir une vue plus concrète du `TCP SYN Scan`, j'ai effectué un scan du port TCP/80 vers un hôte qui avait un serveur web actif sur ce port. En effectuant une analyse réseau avec Wireshark, nous pouvons voir le flux suivant (source de scan : `10.10.14.84`) :

![nmap-image](assets/fr/68.webp)

_Capture réseau lors d'un TCP SYN scan pour un port ouvert._

Nous voyons sur la première ligne que la source du scan envoie un paquet TCP à l’hôte `10.10.10.203` sur le port TCP/80. Dans ce paquet TCP, le flag SYN est à 1 pour signifier qu’il s’agit d’une demande d’initialisation de connexion TCP.

Nous voyons ensuite sur la deuxième ligne que la cible répond avec un `TCP SYN/ACK`, ce qui veut dire qu'il accepte d'initialiser une connexion et donc de recevoir des flux sur le port TCP/80. On peut donc en déduire que le port TCP/80 est ouvert et qu'un serveur web est bien présent sur le serveur scanné.

Notre hôte renvoie ensuite un paquet RST pour fermer la connexion, cela permet à l’hôte scanné de ne pas maintenir une connexion TCP ouverte en attente de réponse. Dans le cas d’un scan sur de nombreux ports, ne pas fermer les connexions TCP pourrait mener à un déni de service, saturant le nombre de connexion en attente de réponse que le serveur peut maintenir (voir [Wikipedia – Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))

Vous pourrez voir plus précisément dans Wireshark, pour chaque test que nous allons faire, l’état des flags TCP. Cela afin de savoir s’il s’agit d’un paquet SYN, SYN/ACK, ACK, etc :

![nmap-image](assets/fr/69.webp)

_Visualisation des flags TCP d’un paquet dans Wireshark (TCP SYN ici)._

À l'inverse, j'ai effectué le même test entre les deux machines, mais cette fois-ci en scannant un port TCP/81 sur lequel aucun service n'est actif (source de scan : `10.10.14.84`) :

![nmap-image](assets/fr/70.webp)

_Capture réseau lors d'un TCP SYN scan pour un port fermé._

L’hôte scanné renvoie un `TCP RST/ACK` en réponse à mon `TCP SYN` lorsque le port n'est pas ouvert.

Comme indiqué, lorsque vous exécutez Nmap depuis un terminal privilégié, le TCP SYN Scan est le mode par défaut, il peut être forcé via l’option `-sS` (`scan SYN`) :

```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```


Le `TCP SYN Scan` est le scan le plus couramment utilisé pour des questions de rapidité. En revanche, l’absence de finalisation du _Three Way Handshake_ par un client (pas d’envoi du ACK après le SYN/ACK serveur) peut paraître suspecte si elle est observée trop de fois sur un serveur ou depuis une même source sur le réseau. En effet, le comportement normal d'un client après réception d’un paquet TCP SYN/ACK en réponse à un TCP SYN est d’envoyer un `acknowledgement` (ACK) pour ensuite commencer l'échange.

Néanmoins, cela permet d'avoir un scan un peu plus rapide, car il ne s'encombre pas à envoyer un ACK à chaque réponse positive. L'avantage du SYN Scan est donc sa rapidité, car un seul paquet est envoyé par port à scanner, cela au détriment d’une plus grande chance de détection.

De plus, le TCP SYN scan est capable de détecter si un port est filtré (protégé) par un pare-feu. En effet, un pare-feu devant l'hôte visé peut être détecté via le comportement qu'il a lorsqu'il reçoit un paquet TCP SYN sur un port qu'il est censé protéger. Celui-ci ne va tout simplement pas répondre. Or nous avons vu que dans les deux cas (port ouvert ou port fermé), il y a une réponse de l'hôte. Ce troisième comportement va alors révéler la présence d'un pare-feu entre l'hôte scanné et la machine qui lance le scan. Voici le résultat que Nmap peut nous retourner lorsqu'un port scanné est filtré par un pare-feu :

![nmap-image](assets/fr/71.webp)

_Affichage Nmap lors du scan d'un port filtré._

Lorsque l'on effectue une capture réseau au moment du scan, nous pouvons effectivement voir qu'aucune réponse n'est donnée :

![nmap-image](assets/fr/72.webp)

_Capture réseau lors d'un TCP SYN scan pour un port filtré par un pare-feu._

La différence entre un port fermé et un port filtré est la suivante : un port filtré est un port protégé par un pare-feu alors qu'un port fermé est un port sur lequel aucun service ne tourne et qui est donc incapable de traiter nos paquets TCP. Certains types de scan TCP comme le TCP SYN scan sont capables de détecter si un port est filtré alors que d'autres types de scan ne le peuvent pas.

### III. Le TCP Connect scan ou "Full Open scan"

Le second type de scan TCP est le `TCP Connect scan`, aussi nommé _Full Open Scan_. Il reprend le même fonctionnement que le TCP SYN scan, mais cette fois-ci en renvoyant un `TCP ACK` après une réponse positive du serveur (un SYN/ACK). C'est pourquoi il est nommé `"Full Open"`, car l'on ouvre et initie complètement la connexion sur chaque port ouvert lors du scan, respectant ainsi le _Three Way Handshake_ TCP :

![nmap-image](assets/fr/73.webp)

_Schéma des comportements lors d'un TCP Connect Scan pour un port ouvert et fermé._

Voici ce que l'on peut voir transiter sur le réseau lors d'un `TCP Connect scan` ciblant un port ouvert :

![nmap-image](assets/fr/74.webp)

_Sniff réseau lors d’un TCP Connect scan pour un port ouvert._

Nous voyons que le premier paquet TCP envoyé est un `TCP SYN` envoyé par le client, le serveur va ensuite répondre par un `TCP SYN/ACK` ce qui nous indiquera que le port est ouvert et héberge un service actif. Pour simuler un client légitime jusqu'au bout, Nmap va ensuite renvoyer un `TCP ACK` au serveur. À l'inverse, lors d'un scan sur un port fermé :

![nmap-image](assets/fr/75.webp)

_Capture réseau lors d’un TCP Connect scan pour un port fermé._

On remarque que la réponse du serveur à notre paquet `SYN` est une fois encore un paquet `TCP RST/ACK`, nous pouvons donc en déduire que le port est fermé et qu'aucun service ne tourne sur celui-ci.

En utilisant Nmap, c'est l'option `-sT` (`scan Connect`) qui permet d'effectuer un TCP Connect Scan. Sachez également que lorsque Nmap est utilisé depuis une session non privilégiée, c’est le mode de scan TCP utilisé par défaut :

```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```

Le `TCP Connect Scan` simule une demande de connexion plus légitime avec un comportement qui se rapproche le plus de celui d'un client lambda, il est donc plus difficile de repérer un scan sur un nombre réduit de ports. Il est toutefois plus lent, car il initialise complètement chaque connexion TCP sur les ports ouverts de la machine scannée.

Un scan Nmap sur 10 000 ports sera toujours facilement détectable si des services de protection et de détection des intrusions réseau (IDS, IPS, EDR) sont installés. Quand un attaquant souhaite se faire discret, il va plutôt orienter ses recherches vers des ports choisis stratégiquement et en nombre réduit comme le port 445 (SMB) ou 80 (HTTP) qui sont souvent ouverts sur les serveurs et qui présentent des failles généralement courantes.

Étant donné que dans les deux cas, le TCP Connect Scan attend une réponse, il est lui aussi capable de détecter la présence d'un pare-feu qui pourrait filtrer les ports sur l’hôte visé.

### IV. Le TCP FIN scan ou "Stealth Scan"

Le `TCP FIN Scan`, aussi nommé _Stealth Scan_, utilise quant à lui le comportement d'un client mettant fin à une connexion TCP afin de détecter un port ouvert.

En effet, en TCP, une fin de session se traduit par l'envoi d'un paquet TCP avec le flag FIN à 1. Dans un échange habituel, le serveur cesse donc toute communication avec le client (aucune réponse). Si le serveur n'avait aucune connexion TCP active avec le client, il renverra en revanche un `RST/ACK`. On saura donc différencier un port ouvert d'un port fermé en envoyant des paquets `TCP FIN` à un ensemble de ports :

![nmap-image](assets/fr/76.webp)

_Schéma des comportements lors d'un TCP FIN scan pour un port ouvert et fermé._

J'ai à nouveau effectué une capture du réseau lors d'un _Stealth scan_ et voilà ce que l'on voit lorsque le port scanné est ouvert :

![nmap-image](assets/fr/77.webp)

_Capture réseau lors d’un TCP FIN scan pour un port ouvert._

On voit donc que le client envoie un ou deux paquets pour mettre fin à une connexion TCP et que le serveur ne répond pas. Il accepte tout simplement la fin de connexion et arrête de communiquer.

Voici ce que l'on peut voir maintenant lorsque l'on scanne un port fermé :

![nmap-image](assets/fr/78.webp)

_Capture réseau lors d'un TCP FIN scan pour un port fermé._

Nous voyons que le serveur renvoie un paquet `TCP RST/ACK`, il y a donc bien une différence de comportement entre un port ouvert et un port fermé et nous sommes en mesure de lister les ports ouverts sur un serveur via l'envoi de paquet TCP FIN. En utilisant Nmap, c'est l'option `-sF` (`scan FIN`) qui permet d'effectuer un TCP FIN Scan :

```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```

Le TCP FIN Scan ne fonctionne pas sur les hôtes Windows, cela, car l’OS a tendance à ignorer les paquets TCP FIN lorsqu'ils sont envoyés sur des ports qui ne sont pas ouverts. Nous aurons donc l'impression que tous les ports sont fermés si l'on effectue un TCP FIN Scan sur un hôte Windows.

C'est là l'intérêt de connaître à la fois plusieurs méthodes de scan, mais aussi de comprendre la différence entre chacune d'entre elles.

Étant donné que dans un des deux cas, le TCP FIN n'attendra pas de réponse, celui-ci sera incapable de détecter la présence d'un pare-feu entre l’hôte cible et la source de scan.

Voici donc un exemple de résultat de scan TCP FIN par Nmap :

![nmap-image](assets/fr/79.webp)

_Résultat d’un scan TCP FIN par Nmap._

En effet, une non-réponse de l'hôte sur un port donné pourra à la fois signifier que le port est filtré, mais également qu'il est ouvert et actif.

Ce scan est qualifié de "stealth" (discret), car il ne produit pas beaucoup de trafic et ne provoque généralement pas de journalisation dans les systèmes ciblés. Il peut être utilisé pour découvrir discrètement les ports sur un réseau sans lever d’alerte. Cependant, comme mentionné précédemment, son efficacité peut varier en fonction du système cible, tout comme sa discrétion en fonction de la configuration des équipements de sécurité.

### V. Conclusion

Voilà pour ce premier des deux chapitres concernant les différents types de scan TCP proposés par Nmap ! Nous avons vu ici les plus communs, dans le prochain chapitre, nous nous pencherons sur les types de scan TCP XMAS, Null et ACK qui opèrent de façon différente pour détecter les ports ouverts sur un hôte.



## 14 - Les scans de port via TCP : XMAS, Null et ACK

### I. Présentation

Dans cette section, nous continuerons à étudier les différentes méthodes de scan TCP proposées par Nmap. Nous allons ici étudier les méthodes `XMAS`, `Null` et `ACK` qui permettent, via des spécificités propres à TCP, de récupérer des informations sur les ports et services ouverts sur une cible donnée.

### II. Le TCP XMAS scan

Le `TCP XMAS Scan` est un peu particulier, car il ne simule pas du tout un comportement normal d'utilisateur ou de machine au sein d'un réseau. En effet, le `TCP XMAS Scan` va envoyer des paquets TCP avec les flags `URG` (Urgent), `PSH` (Push), et `FIN` (Finish) à 1 dans le but de déjouer certains pare-feu ou mécanismes de filtrage.

Le nom XMAS vient du fait que voir ces flags allumés est inhabituel. Lorsque ces trois drapeaux sont activés simultanément dans un paquet TCP, il ressemble à un sapin de Noël allumé :

![nmap-image](assets/fr/80.webp)

_Schéma des flags TCP utilisés dans un XMAS scan._

Sans détailler le rôle de ces flags ici, il faut savoir que lors d'un envoi de paquet avec ces trois flags activés, un service actif derrière le port visé ne renverra aucun paquet. En revanche, si le port est fermé, nous recevrons un paquet `TCP RST/ACK`. On saura alors différencier le comportement d'un port ouvert et d'un port fermé pour lister les ports sur une machine :

![nmap-image](assets/fr/81.webp)

_Schéma des comportements lors d’un TCP XMAS Scan pour un port ouvert et fermé._

En suivant toujours la même logique, un scan réseau sur le port TCP/80 d'un hôte avec un serveur web actif montre le comportement suivant lors de la détection d'un port ouvert (source de scan `10.10.14.84`) :

![nmap-image](assets/fr/82.webp)

_Capture réseau lors d’un TCP XMAS scan pour un port ouvert._

On voit donc que la source de scan envoie deux paquets TCP XMAS (avec les flags `FIN`, `PSH` et `URG` à 1) à l’hôte `10.10.10.203` et qu'il n'y a aucun retour de la cible, ce qui indique que le port est ouvert. À l'inverse, lors d'un `TCP XMAS Scan` sur un port fermé, voici le résultat observé :

![nmap-image](assets/fr/83.webp)

_Capture réseau lors d'un TCP XMAS scan pour un port fermé._

La réponse à notre paquet TCP est alors un `TCP RST/ACK`, ce qui indique que le port est fermé. Pour utiliser cette technique avec Nmap, l'option `-sX` (`scan XMAS`) permet d'effectuer un TCP XMAS Scan :

```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```

Il est important de signaler que le TCP XMAS scan n'est pas capable de détecter les pare-feu qui pourraient se trouver entre la cible et la machine de scan, à l'inverse de certains autres types de scans comme le TCP SYN ou Connect. En effet, un pare-feu actif entre les deux hôtes fera en sorte qu'aucun retour TCP ne soit fait si le port visé est filtré (c'est-à-dire protégé par le pare-feu). On est alors dans l'impossibilité, lors d'une non-réponse, de savoir s'il s'agit d'un port protégé par le pare-feu ou d'un port ouvert et actif. Il faut également savoir que, comme le `TCP FIN scan`, certaines applications ou systèmes d'exploitation comme Windows peuvent fausser les résultats de ce type de scan.

_Remarque : le support des scans XMAS/FIN/NULL sur les versions récentes de Windows reste limité, les résultats peuvent être incohérents sur ce type de cible. (Mise à jour 2025)_

### III. Le TCP Null scan

À l'inverse du TCP XMAS scan, le `TCP Null scan` va envoyer des paquets TCP scan avec tous les flags à 0. Il s'agit là aussi d'un comportement que l'on ne trouvera jamais dans un échange normal entre des machines, car l'envoi d'un paquet TCP sans flag n'est pas spécifié dans le RFC décrivant le protocole TCP. C'est pourquoi il peut être détecté plus facilement.

L'utilisation de ce scan peut, comme le TCP XMAS scan, perturber certains firewalls ou modules de filtrage et alors laisser passer les paquets :

![nmap-image](assets/fr/84.webp)

_Schéma des comportements lors d’un TCP Null Scan pour un port ouvert et fermé._

Voici ce que l'on peut observer sur le réseau lors d’un `TCP Null scan` sur un port ouvert :

![nmap-image](assets/fr/85.webp)

_Capture réseau lors d'un TCP Null scan pour un port ouvert._

La machine de scan envoie un paquet sans flag (`[<None>]` dans Wireshark) sans aucune réponse du serveur. À l'inverse, lorsque le port visé est fermé :

![nmap-image](assets/fr/86.webp)

_Capture réseau lors d'un TCP Null scan pour un port fermé._

Pour effectuer un TCP Null scan avec Nmap, il suffit d'utiliser l’option `-sN` (`scan Null`) :

```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```

Étant donné que la réponse quand un port est ouvert et quand un firewall est actif (aucun retour du serveur dans les deux cas) est identique, le TCP Null scan est incapable de détecter la présence d'un pare-feu. De plus, le pare-feu peut même fausser le résultat en laissant croire qu'un port est ouvert, car il ne répond pas aux paquets TCP sans flags alors que celui-ci est filtré. C'est une information à connaître lorsque l'on emploie des scans incapables de différencier un port ouvert d'un port filtré (protégé par un pare-feu), comme les scans `TCP Null`, `XMAS` ou `FIN`, afin de rester cohérent dans l'interprétation des résultats obtenus.

### IV. Le TCP ACK scan

Le `TCP ACK scan` est utilisé pour détecter la présence d'un pare-feu sur l’hôte cible ou entre la cible et la source de scan.

Contrairement aux autres scans, le TCP ACK scan ne va pas chercher à identifier les ports ouverts sur l’hôte, mais plutôt à savoir si un système de filtrage est actif en répondant pour chaque port par `filtered` ou `unfiltered`. Certains scans TCP comme les `TCP SYN` ou `TCP Connect` peuvent faire les deux en même temps, alors que d'autres comme `TCP FIN` ou `TCP XMAS` ne permettent pas du tout de déterminer la présence d'un filtrage. C'est pourquoi le TCP ACK scan peut avoir un intérêt :

![nmap-image](assets/fr/87.webp)

_Schéma des comportements lors d'un TCP ACK Scan pour un port filtré et non filtré._

On utilisera l'option `-sA` de Nmap pour effectuer ce type de scan. Voici le résultat que l’on peut obtenir lors de l'exécution d’un TCP ACK scan dans le cas où le port est filtré, c'est-à-dire bloqué et protégé par un pare-feu :

![nmap-image](assets/fr/88.webp)

_Affichage Nmap lors du TCP ACK Scan._

Exemple de résultat pour un hôte disposant d’un pare-feu et un autre n’en disposant pas. Nmap retourne `filtered` sur les ports TCP/80 et TCP/81 de l’hôte `10.10.10.203`. Sur une analyse réseau via Wireshark, le comportement est le suivant :

![nmap-image](assets/fr/89.webp)

_Capture réseau lors d'un TCP ACK scan pour un port non filtré par un pare-feu._

La machine cible ne renvoie rien dans le cas où un pare-feu est présent.

Pour lancer ce scan avec Nmap, il faut utiliser l’option `-sA` (`scan ACK`) :

```bash
# Execution of a TCP ACK Scan 
nmap -sA 192.168.1.15
```

### V. Conclusion

Nous avons ici vu trois méthodes différentes de scan via TCP en plus de celles déjà présentées. Ces différentes méthodes sont à utiliser dans des conditions et contextes bien précis, notamment dans le cadre de tests d’intrusion ou d’opérations Red Team, durant lesquels des notions de discrétion sont présentes.

## 15 - Nmap CheatSheet – Récapitulatif des commandes du tutoriel

### I. Présentation

Voici un court récapitulatif des nombreuses commandes et cas d’usage de Nmap, afin de retrouver et réutiliser rapidement ces commandes dans un usage quotidien.

### II. Nmap : CheatSheet IT-Connect

Voici donc un pense-bête ou cheatsheet des commandes présentées. Cette page permet de retrouver facilement l’essentiel des usages courants de Nmap.

- Scan de port
    

```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address 
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address 
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```

- Découverte des hôtes actifs
    

```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```

_Remarque : L’option `-sP` est obsolète depuis plusieurs années et doit être remplacée par `-sn`. (Actualisation 2025)_

```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```

- Détection de version
    

```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```

- Les scripts NSE : recherche de vulnérabilité
    

```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```

- Gestion de la sortie Nmap
    

```bash
# Save scan to text file 
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```

- Optimisation des performances
    

```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```

- Les types de scan TCP
    

```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```

J’espère que ces différentes commandes vous seront utiles. N’oubliez pas d’adapter la cible des scans à votre contexte et de vous référer à la documentation officielle pour maîtriser pleinement les tests réalisés.

### III. Conclusion

Le tutoriel sur Nmap est maintenant terminé. Vous disposez des bases nécessaires pour utiliser cet outil complet et puissant. Il est fortement conseillé de s’exercer sur des environnements contrôlés (Hack The Box, VulnHub, machines virtuelles) avant une utilisation en production.

Il reste beaucoup à explorer sur le fonctionnement interne de l’outil et ses fonctionnalités avancées. Toutefois, la maîtrise des commandes et concepts présentés ici vous permettra d’utiliser Nmap avec assurance et pertinence.


