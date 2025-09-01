---
name: Graylog
description: Centralisez et analysez vos logs facilement
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## Déployer Graylog sur Debian 12

### I. Présentation

Graylog est une solution open source de type "puits de logs" dont l'objectif est de permettre la centralisation, le stockage, et l'analyse en temps réel des journaux de vos machines et vos périphériques réseaux. Dans ce tutoriel, nous allons apprendre à installer Graylog, dans sa version gratuite, sur une machine Debian 12 !

Au sein d'un système d'information, chaque **serveur**, qu'il soit sous **Linux** ou **Windows**, et chaque **équipement réseau** (switch, routeur, firewall, etc...) **génère ses propres journaux**, stockés en local. Les journaux étant stockés sur chaque machine en local, l'analyse et la corrélation des événements est très difficile... C'est là que **Graylog** intervient. Il va assurer la fonction de **puits de logs**, c'est-à-dire que **toutes vos machines vont lui envoyer leurs logs** (via syslog, par exemple). Graylog va ensuite **stocker et indexer ces logs**, tout en vous permettant d'effectuer des recherches globales et de créer des alertes.

Graylog est un outil d'analyse et de surveillance qui va vous permettre d'identifier plus facilement les comportements suspects et les problèmes divers et variés (stabilité, performance, etc...).


![Image](assets/fr/034.webp)

**Remarque**: la version gratuite, **Graylog Open**, ne se présente pas comme un SIEM comme peut l'être Wazuh, notamment, car il manque de vraies fonctions de détection d'intrusion.

### II. Prérequis

La **stack Graylog** s'appuie sur **plusieurs composants** que nous devrons installer et configurer. Ici, nous installerons tous les composants sur le même serveur, mais il est possible de créer des clusters basés sur plusieurs nœuds et de répartir les rôles sur plusieurs serveurs. Dans le cadre de ce tutoriel, nous installerons **Graylog 6.1**, soit la version la plus récente à ce jour.

* **MongoDB 7**, qui est la version actuellement recommandée pour Graylog (minimum 5.0.7, maximum 7.x)
* **OpenSearch**, qui est un fork open source de Elasticsearch créé par Amazon (minimum 1.1.x, maximum 2.15.x)
* **OpenJDK 17**

Le **serveur Graylog** est sous **Debian 12**, mais l'installation est possible sur d'autres distributions, y compris par l'intermédiaire de Docker. La machine virtuelle est équipée de **8 Go de RAM** et **256 Go d'espace disque**, afin d'avoir assez de ressources pour tous les composants (sinon cela peut avoir un impact important sur les performances). Mais, je l'indique à titre indicatif, car **le dimensionnement de l'architecture Graylog dépend de la quantité d'informations à traiter**. Graylog peut tout à fait traiter 30 Mo ou 300 Mo de données par jour, comme 300 Go de données par jour... C'est une **solution scalable** capable de gérer **des téraoctets de logs** (voir [cette page](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).

![Image](assets/fr/032.webp)

Source: Graylog

Avant de commencer la configuration, attribuez une adresse IP statique à la machine Graylog et installez les dernières mises à jour. Veillez aussi à configurer le fuseau horaire de la machine locale et définissez un serveur NTP pour la synchronisation de la date et l'heure. Voici la commande à exécuter:

```
sudo timedatectl set-timezone Europe/Paris
```

**Remarque**: l'installation d'**OpenSearch est facultative** si vous utilisez **Graylog Data Node** à la place.

### III. Installation pas à pas de Graylog

Commençons par une mise à jour du cache des paquets et l'installation d'outils nécessaires pour la suite des événements.

```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```

![Image](assets/fr/030.webp)

#### A. Installation de MongoDB

Une fois que c'est fait, nous allons commencer l'installation de MongoDB. Téléchargez la clé GPG correspondante au dépôt MongoDB:

```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```

Puis, ajoutez le dépôt de MongoDB 6 sur la machine Debian 12:

```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```

Ensuite, nous allons mettre à jour le cache des paquets et tenter d'installer MongoDB:

```
sudo apt-get update
sudo apt-get install -y mongodb-org
```

L'installation de MongoDB ne peut pas être effectuée, car il manque une dépendance: **libssl1.1**. Nous allons devoir installer ce paquet manuellement avant de pouvoir poursuivre parce que Debian 12 ne l'a pas dans ses dépôts.

```
Les paquets suivants contiennent des dépendances non satisfaites :
 mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
 mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```

Nous allons télécharger le paquet DEB nommé "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (version la plus récente) avec la commande **wget**, puis procéder à son installation via la commande **dpkg**. Ce qui donne les deux commandes suivantes:

```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```

![Image](assets/fr/028.webp)

Relancez l'installation de MongoDB:

```
sudo apt-get install -y mongodb-org
```

Ensuite, relancez le service MongoDB et activez son démarrage automatique au lancement du serveur Debian.

```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```

MongoDB est installé, nous pouvons passer à l'installation du prochain composant.

#### B. Installation d'OpenSearch

Nous allons passer à l'installation d'OpenSearch sur le serveur. La commande suivante permet d’ajouter la clé de signature pour les paquets OpenSearch:

```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```

Puis, ajoutez le dépôt OpenSearch pour que nous puissions télécharger le paquet avec **apt** par la suite:

```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```

Mettez à jour votre cache de paquets:

```
sudo apt-get update
```

Puis, **installez OpenSearch** en prenant soin de **définir le mot de passe par défaut pour le compte Admin** de votre instance. Ici, le mot de passe est "**IT-Connect2024!**", mais remplacez cette valeur par un mot de passe robuste. **Évitez les mots de passe faibles** du style "**P@ssword123**" et utilisez au moins **8 caractères** avec au moins un caractère de chaque type (minuscule, majuscule, chiffre et caractère spécial), sinon il y aura une erreur à la fin de l'installation. **C'est un prérequis depuis OpenSearch 2.12.**

```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```

Patientez pendant l'installation...

Quand c'est terminé, prenez le temps d'effectuer la configuration minimale. Ouvrez le fichier de configuration au format YAML:

```
sudo nano /etc/opensearch/opensearch.yml
```

Lorsque le fichier est ouvert, configurez les options suivantes:

```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```

Cette configuration OpenSearch est destinée à configurer un nœud unique. Voici des explications sur les différents paramètres que nous utilisons:

* **cluster.name: graylog**: ce paramètre nomme le cluster OpenSearch avec le nom "**graylog**".
* **node.name: ${HOSTNAME}**: le nom du nœud est défini dynamiquement pour correspondre à celui de la machine Linux locale. Même si nous n'avons qu'un seul nœud, il est important de le nommer correctement.
* **path.data: /var/lib/opensearch**: ce chemin spécifie où OpenSearch stocke ses données sur la machine locale, en l'occurrence dans "**/var/lib/opensearch**".
* **path.logs: /var/log/opensearch**: ce chemin définit où les fichiers journaux d'OpenSearch sont stockés, ici dans "**/var/log/opensearch**".
* **discovery.type: single-node**: ce paramètre configure OpenSearch pour fonctionner avec un nœud unique, d'où le choix de l'option "**single-node**".
* **network.host: 127.0.0.1**: cette configuration fait qu'OpenSearch écoute uniquement sur son interface de boucle locale, ce qui est suffisant puisqu'il est sur le même serveur que Graylog.
* **action.auto_create_index: false**: en désactivant la création automatique d'index, OpenSearch ne créera pas d’index automatiquement lorsqu’un document est envoyé sans index existant.
* **plugins.security.disabled: true**: cette option désactive le plugin de sécurité d'OpenSearch, ce qui signifie qu'il n'y aura ni authentification, ni gestion des accès, ni chiffrement des communications. Ce paramétrage permet de gagner du temps pour effectuer la mise en place de Graylog, mais il est à éviter en production (voir [cette page](https://opensearch.org/docs/1.0/security-plugin/index/)).

Certaines options sont déjà présentes, donc vous devez simplement enlever le "#" pour les activer, puis indiquer votre valeur. Si vous ne trouvez pas une option, vous pouvez la déclarer directement à la fin du fichier.

![Image](assets/fr/023.webp)

Enregistrez et fermez ce fichier.

#### C. Configurer Java (JVM)

Vous devez configurer Java Virtual Machine utilisé par OpenSearch afin d'ajuster la quantité de mémoire que peut utiliser ce service. Éditez le fichier de configuration suivant:

```
sudo nano /etc/opensearch/jvm.options
```

Avec la configuration déployée ici, **OpenSearch démarrera avec une mémoire allouée de 4 Go et pourra atteindre jusqu'à 4 Go**, il n'y aura donc pas de variation de mémoire pendant le fonctionnement. Ici, la configuration tient compte du fait que la machine virtuelle dispose d'un total de **8 Go de RAM**. Les deux paramètres doivent avoir la même valeur. Ceci implique de remplacer ces lignes:

```
-Xms1g
-Xmx1g
```

Par ces lignes:

```
-Xms4g
-Xmx4g
```

Voici la modification à apporter en image:

![Image](assets/fr/022.webp)

Fermez ce fichier après l'avoir enregistré.

En complément, nous devons vérifier la configuration du paramètre "**max_map_count**" au niveau du noyau Linux. Il définit la limite des zones de mémoire mappées par processus, afin de répondre aux besoins de notre application. **OpenSearch**, au même titre que **Elasticsearch**, recommande de **fixer cette valeur à "262144" pour éviter des erreurs liées à la gestion de la mémoire**.

En principe, sur une machine Debian 12 fraîchement installée, la valeur est déjà correcte. Mais, nous allons le vérifier. Exécutez cette commande:

```
cat /proc/sys/vm/max_map_count
```

Si vous obtenez une valeur différente de "**262144**", exécutez la commande suivante, sinon ce n'est pas nécessaire.

```
sudo sysctl -w vm.max_map_count=262144
```

Enfin, activez le démarrage automatique d'OpenSearch et lancez le service associé.

```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```

Si vous affichez l'état de votre système, vous devriez voir un processus Java avec 4 Go de RAM.

```
top
```

![Image](assets/fr/029.webp)

Passons à la prochaine étape: l'installation tant attendue, celle de Graylog !

#### D. Installation de Graylog

Pour effectuer l'**installation de Graylog 6.1** dans sa dernière version, exécutez les 4 commandes suivantes afin de **télécharger et d'installer Graylog Server**:

```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```

Quand c'est fait, nous devons apporter des modifications à la configuration de Graylog avant de chercher à le lancer.

Commençons par configurer ces deux options:

* **password_secret**: ce paramètre sert à définir une clé utilisée par Graylog pour sécuriser le stockage des mots de passe utilisateurs (dans l'esprit d'une clé de salage). Cette clé doit être **unique** et **aléatoire**.
* **root_password_sha2**: ce paramètre correspond au mot de passe de l’administrateur par défaut dans Graylog. Il est stocké sous forme d'un hash SHA-256.

Nous allons commencer par générer une clé de 96 caractères pour le paramètre **password_secret**:

```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```

Copiez la valeur retournée, puis ouvrez le fichier de configuration de Graylog:

```
sudo nano /etc/graylog/server/server.conf
```

Collez la clé au niveau du paramètre **password_secret**, comme ceci:

![Image](assets/fr/027.webp)

Enregistrez et fermez le fichier.

Ensuite, vous devez définir le mot de passe du compte "**admin**" créé par défaut. Dans le fichier de configuration, c'est le hash du mot de passe qui doit être stocké, ce qui implique de le calculer. L'exemple ci-dessous permet d'obtenir le hash du mot de passe "**PuitsDeLogs@**": adaptez la valeur avec votre mot de passe.

```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```

Copiez la valeur obtenue en sortie (sans le tiret en bout de ligne).

Ouvrez de nouveau le fichier de configuration de Graylog:

```
sudo nano /etc/graylog/server/server.conf
```

Collez la valeur au niveau de l'option **root_password_sha2** comme ceci:

![Image](assets/fr/026.webp)

Profitez d'être dans le fichier de configuration pour configurer l'option nommée "**http_bind_address**". Indiquez "**0.0.0.0:9000**" pour que l'interface web de Graylog soit accessible sur le port **9000**, via n'importe quelle adresse IP du serveur.

![Image](assets/fr/024.webp)

Puis, configurez l'option "**elasticsearch_hosts**" avec la valeur `http://127.0.0.1:9200` pour déclarer notre instance locale OpenSearch. Ceci est nécessaire, car nous n'utilisons pas de **Graylog Data Node**. Et sans cette option, il ne sera pas possible d'aller plus loin...

![Image](assets/fr/025.webp)

Enregistrez et fermez le fichier.

Cette commande active Graylog pour qu'il démarre automatiquement au prochain démarrage et elle lance immédiatement le serveur Graylog.

```
sudo systemctl enable --now graylog-server
```

Une fois que c'est fait, tentez une connexion à Graylog à partir d'un navigateur. Indiquez l'adresse IP du serveur (ou son nom) et le port 9000.

**À titre d'information:**

Il n'y a pas si longtemps que cela, une fenêtre d'authentification similaire à celle ci-dessous apparaissait lors de la première connexion à Graylog. Il fallait indiquer l'identifiant "**admin**" et votre mot de passe. Et, là, on pouvait avoir la mauvaise surprise de constater que la connexion ne fonctionnait pas.

![Image](assets/fr/031.webp)

Il était nécessaire de retourner en ligne de commande sur le serveur Graylog et de consulter les journaux. On pouvait alors que **pour la première connexion**, il est nécessaire d'**utiliser un mot de passe temporaire**, spécifié dans les logs.

```
tail -f /var/log/graylog-server/server.log
```

![Image](assets/fr/021.webp)

Il fallait ensuite retenter une connexion avec l'utilisateur "**admin**" et le mot de passe temporaire, et cela permettait de se connecter !

**Désormais, ce n'est plus le cas. Il suffit de se connecter avec son compte admin et le mot de passe configuré en ligne de commande.**

![Image](assets/fr/033.webp)

**Bienvenue sur l'interface de Graylog !**

![Image](assets/fr/019.webp)

#### E. Graylog: créer un nouveau compte administrateur

Plutôt que d'utiliser le compte admin créé nativement par Graylog, vous pouvez créer votre compte administrateur personnel. Cliquez sur le menu "**System**" puis sur "**Users and Teams**" afin de cliquer sur le bouton "**Create user**". Ensuite, remplissez le formulaire et assignez le rôle administrateur à votre compte.

![Image](assets/fr/020.webp)

Un compte personnalisé peut contenir des informations complémentaires, comme le nom, le prénom et l'adresse e-mail, contrairement au compte admin natif. De plus, ceci vous assure une meilleure traçabilité lorsque chaque personne travaille avec un compte nominatif.

## Envoyer les logs vers Graylog avec rsyslog

### I. Présentation

Dans cette seconde partie, nous allons apprendre à configurer une machine Linux pour qu'elle envoie ses journaux (logs) vers un serveur Graylog. Pour cela, on va procéder à l'installation et à la configuration de Rsyslog sur le système.

### II. Configurer Graylog pour recevoir les logs Linux

Nous allons commencer par la configuration de Graylog. Il y a trois étapes à accomplir:

* La création d'un **Input** pour créer un point d'entrée permettant aux machines Linux d'**envoyer les journaux Syslog via UDP**.
* La création d'un nouvel **Index** pour stocker et **indexer tous les journaux Linux**.
* La création d'un **Stream** pour **router** les journaux reçus par Graylog vers le nouvel Index Linux.

#### A. Créer un Input pour Syslog

Connectez-vous à l'interface de Graylog, cliquez sur "**System**" dans le menu puis sur "**Inputs**". Dans la liste déroulante, sélectionnez "**Syslog UDP**" puis cliquez sur le bouton intitulé "**Launch new input**". Il est également possible de créer un Input Syslog en TCP, mais cela implique d'utiliser un certificat TLS: c'est un plus pour la sécurité, mais ce point ne sera pas abordé dans cet article.

![Image](assets/fr/001.webp)

Un assistant va s'afficher à l'écran. Commencez par donner un nom à cet Input, par exemple "**Graylog_UDP_Rsyslog_Linux**" et choisissez un port. Par défaut, le port est "**514**"mais vous pouvez le personnaliser. Ici, le port "**12514**" est retenu.

![Image](assets/fr/016.webp)

Vous pouvez aussi cocher l'option "**Store full message**" pour que le message de log complet soit stocké dans Graylog. Cliquez sur "**Launch Input**".

![Image](assets/fr/017.webp)

Le nouvel Input a été créé et il est désormais actif. Désormais, Graylog peut recevoir les logs Syslog sur le port 12514/UDP, mais nous n'en avons pas fini avec la configuration de l'application.

![Image](assets/fr/018.webp)
**Remarque**: un seul Input peut être utilisé pour stocker les journaux de plusieurs machines Linux.

#### B. Créer un nouvel Index Linux

Nous devons créer un Index dans Graylog pour stocker les journaux des machines Linux. Un **index** dans Graylog est une structure de stockage qui contient les logs reçus, c'est-à-dire les messages reçus. Graylog utilise OpenSearch comme moteur de stockage et les messages sont indexés pour permettre des recherches rapides et efficaces.

À partir de Graylog, cliquez sur "**System**" dans le menu puis sur "**Indices**". Au sein de la nouvelle page qui s'affiche, cliquez sur "**Create index set**".

![Image](assets/fr/005.webp)

Nommez cet index, par exemple "**Linux Index**", ajoutez une description et un préfixe, avant de valider. Ici, nous allons **stocker tous les journaux Linux dans cet index**. Il est également possible de créer des index spécifiques pour stocker uniquement certains logs (uniquement les logs [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), du service Web, etc...).

![Image](assets/fr/006.webp)

Désormais, nous devons créer un nouveau stream pour router les messages vers cet index.

#### C. Créer un Stream

Pour créer un nouveau Stream, cliquez sur "**Streams**" dans le menu principal de Graylog. Ensuite, cliquez sur le bouton "**Create stream**" situé sur la droite. Dans la fenêtre qui apparaît, nommez le stream, par exemple "**Linux Stream**" et choisissez l'index "**Linux Index**" pour le champ nommé "**Index Set**". Validez.

**Remarque**: les messages correspondants à ce stream seront aussi inclus dans le "**Default Stream**", sauf si vous cochez l'option "**Remove matches from 'Default Stream'**".

![Image](assets/fr/002.webp)

Ensuite, dans les paramètres de votre steam, cliquez sur le bouton "**Add stream rule**" pour ajouter une nouvelle règle de routage des messages. Si vous ne trouvez pas cette fenêtre, cliquez sur "**Streams**" dans le menu, puis sur la ligne correspondante à votre stream, cliquez sur "**More**" puis "**Manage Rules**".

Choisissez le type "**match input**" et sélectionnez l'**Input Rsyslog en UDP** créée précédemment. Validez avec le bouton "**Create Rule**". Ainsi, tous les messages à destination de notre nouvel Input seront envoyés dans l'Index pour Linux.

![Image](assets/fr/003.webp)

Votre nouveau Stream doit s'afficher dans la liste et il doit être sur l'état "**Running**". La bande passante de message indique "**0 msg/s**" car pour le moment, nous n'envoyons aucun journal vers l'Input Rsyslog UDP. Pour voir les journaux d'un stream, cliquez simplement sur son nom.

![Image](assets/fr/004.webp)

**Tout est prêt du côté de Graylog**. Passons à la suite, à savoir la configuration de la machine Linux.

### III. Installer et configurer Rsyslog sur Linux

Connectez-vous à la machine Linux, en local ou à distance, et utilisez un compte utilisateur disposant des permissions pour élever ses privilèges (via sudo). Sinon, utilisez directement le compte "root".

#### A. Installer le paquet Rsyslog

Commencez par mettre à jour le cache des paquets et installer le paquet nommé "**rsyslog**".

```
sudo apt-get update
sudo apt-get install rsyslog
```

Puis, vérifiez le statut du service. En principal, il est déjà en cours d'exécution.

```
sudo systemctl status rsyslog
```

#### B. Configurer Rsyslog

Rsyslog dispose d'un fichier de configuration principal situé à cet emplacement:

```
/etc/rsyslog.conf
```

En complément, le répertoire "**/etc/rsyslog.d/**" est utilisé pour stocker des fichiers de configuration supplémentaires pour Rsyslog. Dans le fichier de configuration principal, il y a une directive Include permettant d'importer tous les fichiers "**.conf**" situé ce répertoire. Ceci permet d'avoir des fichiers complémentaires pour configurer Rsyslog sans modifier le fichier principal.

Dans ce répertoire, vous devez utiliser des numéros pour définir l'ordre de chargement, parce que le chargement des fichiers se fait dans l'ordre alphabétique. Ainsi, le fait d'ajouter un préfixe numérique permet de gérer la priorité entre plusieurs fichiers de configuration. Ici, nous n'aurons qu'un seul fichier complémentaire, donc ce n'est pas gênant.

Dans ce répertoire, nous allons créer le fichier intitulé "**10-graylog.conf**":

```
sudo nano /etc/rsyslog.d/10-graylog.conf
```

Dans ce fichier, insérez cette ligne:

```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```

Voici comment interpréter cette ligne:

* `*.*`: signifie qu’on doit envoyer tous les logs Syslog de la machine Linux vers Graylog.
* `@`: indique que le transport est effectué en UDP. Il convient de préciser "**@@**" pour basculer en TCP.
* `192.168.10.220:12514`: indique l’adresse du serveur Graylog, ainsi que le port sur lequel on envoie les logs (correspondant à l'Input).
* `RSYSLOG_SyslogProtocol23Format`: correspond au format des messages que l’on veut envoyer à Graylog.

Quand c'est fait, enregistrez le fichier et redémarrez Rsyslog.

```
sudo systemctl restart rsyslog.service
```

Suite à cette action, les premiers messages devraient arriver sur votre serveur Graylog !

### IV. Afficher les journaux Linux dans Graylog

À partir de Graylog, vous pouvez cliquer sur "**Streams**" et sélectionner votre nouveau stream pour afficher les messages associés. Sinon, cliquez sur "**Search**" et effectuez la sélection de votre Steam et lancez une recherche.

Voici quelques éléments clés dans l'interface:

**1** - Sélectionnez la période pour laquelle afficher les messages. Par défaut, ce sont les messages des 5 dernières minutes qui s'affichent.

**2** - Sélectionnez le(s) stream(s) à afficher.

**3** - Activer le refresh automatique de la liste des messages (toutes les 5 secondes, par exemple). Sinon, c'est statique et c'est à vous de faire un refresh manuel.

**4** - Cliquez sur la loupe pour lancer la recherche après avoir modifié la période, le stream, ou le filtre.

**5** - Barre de saisie pour indiquer vos filtres de recherche. Ici, je précise "**source:srv\-docker**" pour afficher uniquement les journaux de la nouvelle machine sur laquelle je viens de configurer Rsyslog.

Des journaux sont bien envoyés par la machine Linux:

![Image](assets/fr/015.webp)

### V. Identifier un échec de connexion SSH

La force de Graylog, c'est d'indexer les journaux et de permettre de faire une recherche selon différents critères: machine source, horodatage, contenu du message, etc... Nous pourrions chercher à identifier les échecs de connexion effectués en SSH.

À partir d'une machine distante (le serveur Graylog, par exemple), tentez de vous connecter à votre serveur Linux sur lequel vous venez de configurer Rsyslog. Par exemple:

```
ssh [email protected]
```

Puis indiquez volontairement un **nom d'utilisateur** et un **mot de passe incorrect**, afin de **générer des erreurs de connexion**. Dans le fichier "**/var/log/auth.log**", ceci va générer des messages de logs similaires à celui-ci:

```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```

Vous devriez retrouver ces messages sur Graylog.

Sur Graylog, utilisez le filtre de recherche suivant pour afficher uniquement les messages correspondants:

```
message:Failed password AND application_name:sshd
```

Si vous avez plusieurs serveurs et que vous souhaitez analyser les logs d'un serveur spécifique, précisez son nom en supplément:

```
message:Failed password AND application_name:sshd AND source:srv\-docker
```

Voici un aperçu du résultat sur une machine où j'ai généré plusieurs erreurs de connexion, à différents moments de la journée:

![Image](assets/fr/009.webp)

Les tentatives de connexion infructueuses sont effectuées à partir de la machine avec l'adresse IP "**192.168.10.199**". Si vous souhaitez en savoir plus sur l'activité de cet hôte, vous pouvez **effectuer une recherche sur cette adresse IP**. Graylog vous sortira tous les logs où cette adresse IP est référencée, sur tous les hôtes (pour lesquels l'envoi de logs est configuré).

Dans ce cas, le filtre à utiliser pourra être:

```
message:"192.168.10.199"
```

Nous obtenons des résultats supplémentaires (ce qui n'est pas étonnant, car nous ne filtrons pas sur l'application SSH):

![Image](assets/fr/008.webp)

### VI. Conclusion

En suivant ce tutoriel, vous devriez être en mesure de configurer une machine Linux pour qu'elle envoie ses logs sur un serveur Graylog. Ainsi, vous serez en mesure de centraliser les journaux de vos hôtes Linux dans votre puits de logs !

Pour aller plus loin, envisager de créer des tableaux de bords et des alertes pour recevoir une notification lorsqu'une anomalie est détectée.

![Image](assets/fr/007.webp)
