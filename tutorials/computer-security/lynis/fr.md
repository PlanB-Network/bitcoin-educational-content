---
name: Lynis
description: Réaliser un audit de sécurité d'une machine Linux avec Lynis
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Fares CHELLOUG publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

**Dans ce tutoriel, nous allons apprendre à réaliser un audit de sécurité d'une machine Linux avec Lynis !**  Pour ceux qui ne connaissent pas **Lynis,** c'est un petit utilitaire en ligne de commande qui va permettre d'analyser la configuration de votre serveur afin de vous faire des recommandations pour **améliorer la sécurité de votre machine.**

Lynis est un outil open source proposé par l’entreprise CISOFY qui est spécialisée dans **l’audit et le durcissement des systèmes**. Pour progresser dans le durcissement de Linux et des services populaires (SSH, Apache2, etc.), Lynis est votre allié ! En effet, Lynis indique ce qui ne va pas et il fournit également des recommandations pour vous aiguiller dans la bonne direction (et vous faire gagner du temps).

**Lynis** fonctionne avec la plupart des distributions Linux, notamment : **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis s'adresse aux utilisateurs de Linux / UNIX, mais il est aussi compatible **macOS**. Très rapide à installer, il n’y a pas de gestion des dépendances au niveau des packages.

Il est utilisé pour différents usages :

* Les audit de sécurité
* Les tests de conformité (PCI, HIPAA et SOX)
* Le durcissement des configurations système
* La détection de vulnérabilités

Cet outil est très largement utilisé par plusieurs typologies d’utilisateurs, notamment les administrateurs système, les auditeurs informatiques et les pentesters. Pour les analyses, l’outil se base sur des standards tels que le **CIS Benchmark, NIST, NSA, OpenSCAP** et sur des recommandations officielles des guides **Debian, Gentoo, Red Hat**.

Le projet est disponible à cette adresse sur **Github** :

* [GitHub - Lynis](https://github.com/CISOfy/lynis)
* [Télécharger Lynis depuis le site CISOFY](https://cisofy.com/lynis/#download)

Dans le cadre de ce tutoriel pas à pas, je vais **utiliser un VPS sous Debian 12** et je vais me concentrer sur la partie SSH car j’aimerais vérifier sa configuration et l’améliorer.

## II. Téléchargement et installation

Il y a plusieurs façon de télécharger et d'installer Lynis. Choisissez celle que vous préférez parmi celles présentées ci-dessous.

### A. Installation depuis les repository Debian

Ce mode d’installation permet d’utiliser la commande **lynis** depuis n’importe quel endroit du système, contrairement à l’installation depuis les sources, où il vous faudra vous positionner dans le répertoire.

Connectez-vous en SSH à votre serveur et saisissez les commandes suivantes pour installer Lynis :

```
sudo apt-get update 
sudo apt-get install lynis -y
```

Vous obtenez ceci :

![Image](assets/fr/024.webp)

### B. Téléchargement depuis le site officiel

Vous pouvez également le télécharger depuis le site Cisofy :

```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```

Vous obtenez ceci :

![Image](assets/fr/032.webp)

Ensuite, nous allons décompresser l’archive à l’aide de la commande suivante :

```
sudo tar -zxf lynis-3.0.9.tar.gz 
```

Vous obtenez ceci :

![Image](assets/fr/020.webp)

Nous allons nous placer dans le dossier **lynis** :

```
cd lynis
```

Nous pouvons vérifier les mises à jour, avec la commande suivante :

```
./lynis update info
```

Vous obtenez ceci :

![Image](assets/fr/023.webp)

### C. Téléchargement depuis GitHub

Nous allons télécharger **Lynis** depuis le repository officiel GitHub, à l’aide la commande suivante (*git* doit être présent sur votre machine) :

```
git clone https://github.com/CISOfy/lynis.git
```

Vous obtenez ceci :

![Image](assets/fr/060.webp)

## III. Utilisation de Lynis

Lynis est présent sur notre machine, alors nous allons apprendre à l'utiliser !

### A. Les commandes et options principales

Pour afficher les commandes disponibles, il suffit de saisir la commande suivante :

```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```

Vous obtenez ceci :

![Image](assets/fr/039.webp)

Et, vous obtenez également les options suivantes :

![Image](assets/fr/040.webp)

Pour afficher toutes les commandes disponibles, saisissez la commande suivante :

```
sudo lynis show
```

Vous obtenez ceci :

![Image](assets/fr/022.webp)

Si vous souhaitez afficher toutes les options, vous devez saisir :

```
sudo lynis show options
```

Vous obtenez ceci :

![Image](assets/fr/021.webp)

Dans la suite de cet article, nous allons apprendre à utiliser certaines options.

### B. Exécution de l’audit système

Nous allons demander à **Lynis** d’auditer notre système, il va vous mettre en évidence ce qui est correctement configuré et ce qui pourrait être amélioré. Pour cela, il faut saisir la commande suivante :

```
sudo lynis audit system
# ou 
./lynis audit system
```

Par défaut, si vous n’êtes pas connecté en tant que "root" au moment de l’exécution de cette commande, l’outil s’exécutera avec les privilèges de l'utilisateur actuellement connecté. Certains tests ne seront pas effectués dans ce contexte :

![Image](assets/fr/052.webp)

Voici le détail des tests qui ne seront pas effectués dans ce mode :

![Image](assets/fr/051.webp)

Une fois la commande exécutée, l’analyse démarre. Il suffit de patienter un instant.

A la fin de l'audit, vous obtenez ceci (nous pouvons constater que **Lynis** a correctement identifié le système **Debian 12** et qu’il utilisera pour l’analyse **le plugin Debian**) :

![Image](assets/fr/017.webp)

Ensuite, Lynis va lister un ensemble de points correspondants à tout ce qu'il a vérifié sur notre système. Ceci est organisé par catégories, comme nous allons le voir. Il faut savoir également qu'un code couleur est utilisé pour mettre en évidence les recommandations :

* **Rouge** pour les éléments critiques ou les bonnes pratiques non respectées (un paquet manquant, par exemple), c'est-à-dire que votre serveur ne respecte pas ce point
* **Jaune** pour les suggestions ou le respect partiel de la recommandation (disons que c'est un plus de respecter un point mis en évidence avec cette couleur (non prioritaire)
* **Vert** pour les points où la configuration de votre serveur est conforme
* **Blanc**, lorsque c'est neutre

Ici, nous pouvons constater que Lynis nous recommande d’installer **fail2ban**:

![Image](assets/fr/057.webp)

Sur la partie "**Boot and services**", nous voyons que la protection des services via *systemd* pourrait être amélioré. Ce qui est positif, c'est que Grub2 est présent et qu’il n’y a pas de problème avec les permissions sur les fichiers :

![Image](assets/fr/029.webp)

Ensuite, vous avez les parties "**Kernel**" et "**Memory and Processes**" :

![Image](assets/fr/037.webp)

Puis, la partie "**Users, Groups and Authentification**". L’outil nous informe d’un warning sur les permissions du répertoire "**/etc/sudoers.d**". Pour le moment, nous n’en savons pas plus, mais nous pourrons voir quelle est la recommandation à la fin de l’analyse.

![Image](assets/fr/049.webp)

Voici ce que vous pouvez obtenir sur les sections "**Shells", "Files Systems", et "USB Devices"**. Nous pouvons entre autres observer qu’il y a des suggestions sur les points de montage et que les périphériques USB sont actuellement autorisés sur cette machine.

![Image](assets/fr/048.webp)

Ensuite, les sections : "**Name services", "Ports and packages", "Networking".**  Il indique ici que des packages qui ne sont plus utilisés pourraient être purgés et qu’il n’y a pas d’utilitaire capable de gérer les mises à jour en automatique.

![Image](assets/fr/058.webp)

Nous constatons qu’un firewall est activé (et oui il y a iptables !). En complément, nous pouvons voir qu’il a trouvé des règles inutilisées et qu’un serveur web Apache est installé.

![Image](assets/fr/055.webp)

S'en suit l’analyse du serveur web en lui-même puisque le service a été identifié.

Nous pouvons observer qu’il a trouvé des fichiers de configuration **Nginx**, et que pour la partie SSL/TLS, les **ciphers** sont configurés avec l’utilisation d’un protocole qui serait non sécurisé. En revanche, nous constatons que la gestion des logs est correcte d'après Lynis.

![Image](assets/fr/038.webp)

Le service SSH est présent sur mon serveur VPS. Sa configuration est analysée par Lynis. Il faut avouer que la sécurité sur la partie SSH est facilement améliorable ! Cela tombe bien, nous reviendrons sur cette partie en détail, une fois que nous aurons obtenu les recommandations.

![Image](assets/fr/026.webp)

Voici les sections **"SNMP Support", "Databases", "PHP", "Squid Support", "LDAP Services", "Logging and files"**.

Il y a une suggestion vraiment importante sur la gestion des logs, il est fortement recommandé de ne pas stocker uniquement les logs localement sur votre machine. Si la machine était corrompue par un attaquant, il est probable qu’il chercherait à effacer ses traces... Donc nous devons externaliser les journaux.

![Image](assets/fr/050.webp)

Ici, nous avons l’audit des services vulnérables, de la gestion des comptes, des tâches planifiées et de la synchronisation NTP.Il est indiqué que le niveau est faible sur la partie bannière et identification : c'est compréhensible, si vous affichez la version du système, cela donne une indication à un attaquant potentiel. C'est le cas par défaut.

Il serait intéressant d’activer **auditd** pour avoir des logs en cas d’analyse **forensic**. Le **NTP** est aussi vérifié, car pour rechercher dans les logs efficacement, il est préférable d’avoir des systèmes à l’heure, ce qui simplifie la recherche.

![Image](assets/fr/036.webp)

Ensuite, Lynis s'intéresse aux éléments cryptographiques, à la virtualisation, aux containers, et aux frameworks de sécurité. Certaines sections sont vides car il n'y a aucune correspondance avec la machine analysée. Toutefois, nous pouvons constater que j’ai deux certificats SSL expirés et je n’ai pas activé **SELinux**.

![Image](assets/fr/027.webp)

Là aussi il y a des choses qui peuvent être améliorées , il n’y pas d’antivirus ni de scanner anti-malware et nous avons des suggestions sur les permissions des fichiers.

![Image](assets/fr/028.webp)

Ensuite, Lynis s'intéresse au durcissement de la configuration du noyau Linux (avec notamment des règles sur la stack IPv4) ainsi que la gestion des répertoires "Home" de la machine Linux.

![Image](assets/fr/035.webp)

Nous arrivons à la fin de l'analyse... Ce dernier point montre que nous aurions tout à gagner d'avoir ClamAV sur cette machine.

![Image](assets/fr/030.webp)

## IV. Les Recommandations

Après l'audit, place à la lecture et l'analyse des recommandations. C’est à ce moment-là que nous allons obtenir les recommandations et les explications pour chacun des tests effectués par Lynis.

Prenons par exemple, les recommandations sur la partie SSH. **Pour chaque suggestion, vous avez le paramètre recommandé ainsi qu’un lien qui va vous donner des explications sur ce point de sécurité.** C’est à vous de décider en fonction de votre contexte et de vos usages.

Voyons ensemble quelques exemples de recommandations qui font directement échos aux points mis en évidence tout au long de l'audit...

### A. Quelques exemples de recommandations

* Comme nous l’avons vu précédemment, le NTP est important pour l’horodatage des logs :

![Image](assets/fr/043.webp)

* Par ailleurs, Lynis nous suggère d'installer le paquet **apt-listbugs** pour avoir des informations sur les bugs critiques lors des installations de package via **apt.**

![Image](assets/fr/041.webp)

* L’outil nous propose d’installer **needrestart pour être en capacité** de voir quels sont les processus qui utilisent une vielle version de librairie et qui ont besoin d’être redémarré.

![Image](assets/fr/054.webp)

* Cette suggestion, nous propose d’installer **fail2ban** pour bloquer automatiquement les hôtes qui commettent des échecs d’authentification (notamment du brute force).

![Image](assets/fr/044.webp)

* Pour le durcissement des services système, il nous recommande d’exécuter la commande bleue pour chaque service de notre machine.

![Image](assets/fr/056.webp)

* Il propose de mettre en place des dates d’expirations pour tout les mots de passe des comptes protégés.

![Image](assets/fr/031.webp)

* Cette suggestion nous propose de mettre en place des valeurs minimales et maximales concernant l’âge d'un mot de passe. Cela va permettre entre autre d’assurer un changement régulier pour les passwords.

![Image](assets/fr/042.webp)

* Il est recommandé d’utiliser des partitions séparées, ce qui limite l'impact en cas de problématique d’espace disque sur une partition.

![Image](assets/fr/047.webp)

* Cette recommandation nous propose de désactiver le stockage USB et le firewire pour éviter les fuites de données

![Image](assets/fr/033.webp)

* Pour répondre à cette recommandation, il vous suffit d’installer et de configurer **unnatended-upgrade** par exemple.

![Image](assets/fr/053.webp)

### B. Installation de paquets recommandés

Pour améliorer la configuration du système, nous allons installer certains paquets sur la machine : certains recommandés par Lynis, certains que je vous recommande personnellement.

Vous obtiendrez une bonne base de travail à condition de passer un peu de temps sur leurs configurations. Pour cela, référez-vous au site IT-Connect, à d'autres articles sur le Web ainsi qu'aux documentations des outils.

```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```

Quelques informations sur les paquets installés :

* **Clamav** est un antivirus.
* **unattend-upgrades** va vous permettre de gérer vos mises à jour en automatique et même de reboot la machine ou de purger automatiquement les anciens packages , il est entièrement configurable.
* **rkhunter** est un anti-rootkit qui va analyser votre système de fichier.
* **Fail2ban**, lui va se baser sur vos fichiers de logs en fonction de ce que vous lui donner à lire et il va travailler avec **iptables**, par exemple pour bannir les adresses IP qui tentent de "brute forcer" votre serveur en SSH.

### C. Recommandations pour SSH

Intéressons-nous aux recommandations sur la partie SSH. Elles sont listées ci-dessous. Rassurez-vous, nous allons immédiatement expliquer comment améliorer la configuration.

![Image](assets/fr/034.webp)

Regardons de plus près ma configuration **SSH** actuelle qui se trouve dans :**/etc/ssh/sshd_config**

![Image](assets/fr/018.webp)

La configuration proposée ci-dessous reste encore optimisable, mais vous permet d’avoir une bonne base. *Attention, j’ai retiré pas mal de commentaires pour plus de lisibilité*.

Nous allons :

* Changer le port pour la connexion SSH (on oublie le port par défaut, 22)
* Augmenter le niveau de verbosité des logs, de **INFO à VERBOSE**
* Définir le **LoginGraceTime** à **2 minutes**

Si au-delà de deux minutes les informations de connexions ne sont pas saisies, la connexion est coupée.

* Activer le **strictModes**

Indique si "sshd" doit contrôler les modes et le propriétaire des fichiers de l'utilisateur ainsi que du répertoire de base de l'utilisateur avant de valider une connexion. C'est normalement souhaitable, parce que quelque fois, les novices laissent accidentellement leur répertoire ou leurs fichiers en accès complet à tout le monde. Par défaut, "yes".

* Définir **MaxAuthtries** à 3

Cela représente le nombre d’échecs de tentative d’authentification, avant que la communication soit fermée.

* Définir **MaxSessions** à 2

Cela représente le nombre maximale de sessions simultanées.

* Autoriser l’authentification par clef publique

```
PubkeyAuthentication yes
```

* Conserver l’authentification par mot de passe :

```
PasswordAuthentication yes
```

Interdire les mots de passe vide et l’authentification **Kerberos** ainsi que **l’authentification directe en root**

```
PermitEmptyPasswords no
PermitRootLogin no
```

Attention à bien avoir "**PermitRootLogin no", si c'est égal à "yes", c'est le "mal absolu"**.

* Interdire la redirection des connexions TCP

```
AllowTcpForwarding no
```

Indique si les redirections TCP sont permises, avec "oui" comme réglage par défaut. À noter : désactiver les redirections TCP ne renforce pas la sécurité si les utilisateurs ont accès à un interpréteur de commandes (shell), car ils peuvent toujours mettre en place leurs propres outils de redirection.

* Interdire la redirection de X11

```
X11Forwarding no
```

Indique si les redirections X11 sont acceptées, avec "non" comme réglage par défaut. À noter : même si les redirections X11 sont désactivées, cela n'augmente pas la sécurité car les utilisateurs peuvent toujours mettre en place leurs propres redirecteurs. La redirection X11 est automatiquement désactivée si l'option **UseLogin** est sélectionnée.

* Régler la temporisation de la communication entre le client et sshd

```
ClientAliveInterval  300
```

Définit un délai en secondes, après lequel, en l'absence de réception de données de la part du client, le service sshd envoie un message pour solliciter une réponse du client. Par défaut, cette option a la valeur "0", ce qui signifie que ces messages ne sont pas envoyés au client. Seule la version 2 du protocole SSH prend en charge cette option.

```
ClientAliveCountMax 0
```

D'après la [documentation (*man page*) de sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), voici la signification de cette option : "Règle le nombre de messages de maintien de la connexion (voir ci-dessus) à envoyer sans réponse de la part du client pour **sshd**. Si ce seuil est atteint tandis que les messages de maintien de la connexion ont été envoyés, **sshd** déconnecte le client et termine la session. Il est important de noter que ces messages de maintien de la connexion sont très différents de l'option **KeepAlive** (ci-dessous). Les messages de maintien de la connexion sont envoyés par le tunnel chiffré, et par conséquent ne sont pas falsifiables. Le maintien de la connexion au niveau TCP activé par l'option **KeepAlive** est falsifiable. Le mécanisme de maintien de la connexion est intéressant quand le client ou le serveur ont besoin de savoir si la connexion est inactive."

* Empêcher de divulguer des informations en désactivant le **motd, la bannière, le lastlog**

```
PrintMotd no
```

Indique si sshd doit montrer le contenu du fichier "/etc/motd" lorsqu'un utilisateur se connecte en mode interactif. Sur certains systèmes, ce contenu peut également être affiché par l'interpréteur de commandes (shell), via le fichier /etc/profile ou un fichier similaire. La valeur par défaut est "oui".

```
Banner none
```

Il est utile de préciser que pour certaines juridictions, l'envoi d'un message préalable à l'authentification peut être un prérequis dans le but d'assurer une protection légale. Le contenu du fichier indiqué est transmis à l'utilisateur distant avant de donner l'autorisation pour la connexion. Ceci implique de configurer cette option, car par défaut, aucun message ne sera affiché.

En image, cela donne :

![Image](assets/fr/019.webp)

### D. Le score de l’audit

Enfin, n'oublions pas de consulter le **score de l'audit Lynis** ! Nous voyons que **mon score d’Hardening est de 63** et que le fichier de rapport est consultable dans « **/var/log/lynis-report.dat** ». Il y a également le fichier "**/var/log/lynis.log**".

**Plus le score est élevé, plus votre système respecte les bonnes pratiques de sécurité.** Autrement dit, plus le score est élevé, mieux c'est ! Vous devez donc travailler sur votre configuration pour avoir un score le plus élevé possible, tout en permettant à votre machine et aux services hébergés de fonctionner normalement (ce qui implique de réaliser des tests de bon fonctionnement).

![Image](assets/fr/046.webp)

Voyons maintenant les résultats sur mon deuxième serveur où j’ai passé un peu plus de temps à faire du hardening ! Il est donc normal que le score soit plus élevé (**76**).

![Image](assets/fr/045.webp)

## V. Planification automatisée de Lynis

**Lynis** prévoit également la possibilité de faire exécuter ses vérifications par une tâche planifiée. Il existe en effet l'option **"--cronjob"** qui va exécuter l'intégralité des tests de Lynis sans besoin de validation ou d'action utilisateur. On peut alors très simplement créer un script qui va lancer **Lynis** et mettre la sortie dans un fichier horodaté et avec le nom du serveur en question. Voici un fichier de ce type que vous pourrez mettre dans le dossier */etc/cron.daily* :

```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```

La variable **"NOM_AUDITEUR"** est simplement une variable que l'on va mettre en l'option **"--auditor"** de **Lynis** afin que ce nom soit affiché dans le rapport :

![Image](assets/fr/059.webp)

On va également créer quelques variable contextuelles qui vont permettre de mieux nous organiser comme le nom de l'hôte et la date pour nommer le rapport et l'horodater ainsi que le chemin vers le dossier dans lequel nous souhaitons mettre nos rapports.

## VI. Conclusion

Lynis est un outil très pratique qui va permettre de gagner du temps et être plus efficace lorsque vous souhaitez en savoir plus sur l'état de la configuration d'un serveur Linux, notamment en termes de sécurité. Toutefois, n'oubliez pas que chaque modification doit être testée avant application en production en tenant compte de vos usages et de votre contexte.

Vous n’allez probablement pas appliquer la même configuration pour un VPS exposé sur le Net, où vous n'avez besoin que d’une seule connexion SSH (car vous êtes la seule personne à vous connecter), contrairement à un **bastion** ou un **ordonnanceur** qui va devoir multiplier les connexions **SSH.**

Une fois que vous avez obtenu une configuration qui vous convient au niveau du durcissement, il est conseillé d’adopter un outil d’automation pour ne pas avoir à refaire les tâches manuellement, car cela serait chronophage et source d’erreur. Par exemple, vous pouvez utiliser **: Puppet, Chef, Ansible, etc…**

N’oubliez pas de communiquer avec vos équipes pour la mise en place : il est nécessaire de leur faire comprendre pourquoi vous faites ces modifications et non pas simplement de leur dire que vous faites des modifications. L’objectif sera au final de transmettre les bonnes pratiques et cela augmentera vos chances de réussite.

Enfin, vous pouvez également confronter **Lynis** avec d’autres outils, il en existe plusieurs. Si vous souhaitez aller vers une gestion centralisée tout en restant dans l’open source, je vous recommande l’outil [Wazuh](https://wazuh.com/).

**Ce tutoriel est terminé, amusez-vous bien avec Lynis** !
