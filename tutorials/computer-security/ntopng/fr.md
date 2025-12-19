---
name: Ntopng
description: Monitorer son réseau avec ntopng
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian Duchemin publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

**Qu'il s'agisse de vérifier la fluidité du réseau, d'avoir une vision claire de l'utilisation faite ou encore pour des stats de performances, le monitoring des flux réseau est une chose importante dans un réseau d’entreprise.** Il permet d'anticiper les changements au niveau de l'infrastructure et aide à assurer une qualité d'utilisation pour les usagers (qu'on appelle aussi QoE pour *Quality of Experience*, en opposition à la QoS).

Pour faire cela, il existe beaucoup de techniques et de logiciels/protocoles. Netflow par exemple, développé par Cisco, permet de récupérer les statistiques des flux IP d'une interface, mais son utilisation est restreinte aux seuls équipements compatibles.

C'est pourquoi dans ce tutoriel, je vais vous présenter **Ntop** et vous montrer comment l'utiliser dans votre infrastructure pour vous permettre de garder un œil sur votre utilisation du réseau.

Ntop est un logiciel open source installable sur toute machine Linux. Il est libre de constructeur et permet de collecter les données suivantes :

**Utilisation de la bande passante**
**Principaux clients**
**Principales destinations**
**Protocoles utilisés**
**Applications utilisées**
**Ports utilisés**
*Etc.*

Aujourd'hui renommé **Ntopng (New Generation)**, il offre de nombreuses fonctionnalités de base de manière gratuite. À noter qu'une version commerciale est disponible permettant d'exporter les alertes configurées vers un logiciel type SIEM ou encore filtrer le trafic avec des règles définies directement depuis la sonde.

## II. Prérequis

L'installation d'une sonde Ntop diffère selon l'équipement et l'environnement. Je ne vais donc pas vous donner ici de marche à suivre, mais vais vous exposer les différentes possibilités.

### A. Mode embarqué

Si vous avez en production un firewall pfSense, OPNSense, Endian, ou même un poste Linux avec NFTables, bonne nouvelle! Vous pouvez installer Ntopng directement et commencer à monitorer vos interfaces.

L'avantage de cette technique est qu'elle ne nécessite aucun matériel supplémentaire. En revanche, elle augmente l'utilisation des ressources donc assurez-vous d'avoir un matériel adéquat ou une VM suffisamment dimensionnée (minimum 2 cœurs et 2BG de RAM).

### B. Mode TAP / SPAN

Un "**tap**" (littéralement robinet en français) est **un appareil réseau qui va dupliquer le trafic qui le traverse pour l'envoyer sur un autre périphérique.** Ce dispositif présente l’avantage de ne rien modifier à l'infrastructure existante, on peut le placer où on veut pour monitorer des sections réseau précises ou le placer entre le switch cœur de réseau et le routeur de périphérie pour analyser le trafic vers/issu d'Internet.

Le gros inconvénient de ce type de matériel est leur coût. En effet, dans nos réseaux actuels en Gigabit, un tap passif ne peut pas capturer correctement le trafic réseau, il faut forcément un appareil actif qui se trouve aux alentours de 200€ (minimum).

Le mode **SPAN**, appelé aussi **port mirroring**, est utilisé par un commutateur pour renvoyer le trafic issu d'un port vers un autre port. C'est de loin la méthode que je préfère, car elle est simple à mettre en place et permet, à l'instar du tap, de monitorer une portion du réseau ou son entièreté à loisir. Deux inconvénients tout de même : il faut que le commutateur intègre cette fonction et son utilisation peut augmenter la charge processeur de celui-ci.

### C. Mode routeur

Il est tout à fait possible de monter un routeur sous Linux et d'installer dessus ntopng. Seul inconvénient à cette méthode, cela modifiera votre réseau, soit son adressage interne, soit l'adressage entre votre "vrai" routeur et celui que vous ajoutez.

Note : pour les lecteurs de l'article [Créez un routeur Wifi avec Raspberry Pi et RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) il est tout à fait possible d'installer ntopng sur votre Rpi pour avoir des statistiques précises!

### D. Mode Bridge

Une alternative intéressante est l'utilisation d'**une machine sous Linux en mode bridge.** Mise entre deux équipements, cela permet de capturer tout le trafic sans pour autant intervenir sur la configuration de l'infrastructure ou de ses équipements. Comme une vieille machine peut faire l'affaire, le coût peut également être intéressant pour cette méthode. À noter que pour être optimal, l'appareil devrait posséder trois cartes réseaux, deux en mode bridge, une pour accéder à l'interface et en SSH. Il est possible d'utiliser seulement deux cartes, mais à ce moment-là, le trafic lié à l'administration du périphérique sera lui aussi capturé...

C'est donc **ce dernier mode que je vais utiliser**. Pour des raisons pratiques, j’utiliserai des machines virtuelles pour la démonstration, mais la méthode reste la même en cas d'utilisation sur des machines physiques.

## III. Préparation de la sonde avec une interface bridge

Pour la sonde, je choisis une machine en **Debian 11** en installation minimale.

Première étape, toujours la même, mettre à jour les paquets :

```
apt-get update && apt-get upgrade
```

Installer ensuite le paquet **bridge-utils** qui va nous permettre de créer notre bridge :

```
apt-get install bridge-utils
```

Une fois installé, il faut tout d'abord bien noter le nom actuel de nos cartes réseau. En effet sous Debian, ce nom peut prendre plusieurs formes et nous en aurons besoin pour la configuration.

Une simple commande **ip add** va nous renvoyer une sortie avec ces infos :

![Image](assets/fr/016.webp)

Ici, je vois 3 interfaces :

* **Lo** : c'est l'interface de loopback (ou en français interface de bouclage); c'est une interface virtuelle qui "boucle" sur l'équipement. En gros, cette interface, qui a comme adresse 127.0.0.1 (quoique n'importe quelle adresse en 127.0.0.0/8 fera l'affaire, cette plage étant réservée pour cet usage) sert à contacter l'équipement lui-même. Si vous avez installé sur votre poste un site web (avec WAMPP par exemple), vous avez sûrement à un moment ou un autre utilisé l'adresse "*localhost*" pour afficher le site hébergé sur votre propre machine. Ce nom d'hôte est justement associé à l'adresse 127.0.0.1 et donc à l'interface de loopback.
**ens33** : c'est ma première interface qui a ici reçu une adresse de mon DHCP
**ens36** : ma seconde interface

Maintenant que je possède toutes les informations, je vais pouvoir modifier le fichier */etc/network/interfaces* pour créer mon bridge. Voici à quoi il ressemble actuellement (peut varier) :

```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```

La première partie concerne donc mon interface de loopback que je ne toucherais pas, vient ensuite l'interface ens33. Les modifications visent à ajouter ma deuxième interface qui est absente (ens36) et configurer le bridge avec ces deux interfaces :

```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```

Quelques explications sur ces premières modifications :

**auto interface** : va "démarrer" automatiquement l'interface au démarrage du système
* **iface *interface* inet manual** : pour utiliser l'interface sans aucune adresse IP. À l'instar du mot clé "static" pour définir une adresse IP statique ou "dhcp" pour utiliser l'adressage dynamique

On poursuit les modifications :

```
# Bridge interface
auto br0
iface br0 inet static
     address 192.168.1.23
     netmask 255.255.255.0
     gateway 192.168.1.1
     bridge_ports ens33 ens36
     bridge_stp off
```

Là encore, quelques explications :

**iface br0 inet static** : j'ai défini ici mon interface bridge (*br0*) avec une adresse statique.
**address, netmask, gateway** : les informations d'adressage de la carte
**bridge_ports** : les interfaces qui seront incluses dans le pont
* **bridge_stp** : le protocole Spanning Tree est utilisé lors de l'interconnexion de switch pour la détection de liens redondants afin d'éviter les boucles. Un pont pouvant être inséré entre deux chemins réseau, il peut être à l'origine d'une boucle, d'où la possibilité d'activer ce protocole. Ici je n'en ai pas besoin donc je le désactive.

On enregistre les changements et on redémarre le réseau :

```
systemctl restart networking
```

Pour vérifier les modifications, on affiche à nouveau le résultat de la commande **ip** add :

![Image](assets/fr/021.webp)  
On voit clairement apparaître **ma nouvelle interface "*br0*" avec l'adresse IP que je lui ai assignée.** Au passage, on peut aussi remarquer que mes deux interfaces physiques sont bien "UP", mais ne disposent d'aucune adresse IP.

## IV. Installation de NtopNG

Maintenant que notre sonde est capable de "sniffer" le trafic entre mon réseau et le routeur, il ne reste plus qu'a installer ntopng. Pour cette installation, il faut avant tout modifier le fichier */etc/apt/sources.list* et ajouter **contrib** à la fin de chaque ligne commençant par **deb** ou **deb-src**.

Par défaut, les sources de paquets ne contiennent que les paquets respectant le DFSG (*Debian Free Sotftware Guidelines*), identifiés par le mot-clé **main**. On peut ajouter en plus ces sources :

**contrib** : paquets contenant des logiciels conformes au DFSG, mais utilisant des dépendances ne faisant pas partie de la branche **main**
**non-free** : contiens des paquets ne respectant pas la DFSG

Exemple d'une ligne dans /etc/apt/sources.list :

```
deb http://deb.debian.org/debian/ bullseye main
```

Je vais donc juste rajouter le mot **contrib** aux lignes telles quel celles-ci.

Le reste des manipulations sont listées sur le site de [NtopNG](https://packages.ntop.org/apt/) où pour Debian 11, il faut ajouter les sources de Ntop pour l'installation future, cet ajout est automatisé par l'utilisation d'un package :

```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```

Vient ensuite la phase d'installation proprement parler :

```
apt-get clean all
apt-get update
apt-get install ntopng
```

La première commande va supprimer le cache du gestionnaire de paquets apt. La seconde va mettre à jour la liste des paquets et la troisième va installer NtopNG.

Après l'installation, le logiciel **NtopNG est directement disponible sur le port 3000 de la machine Debian**. Donc pour moi ce sera `http://192.168.1.23:3000`

![Image](assets/fr/022.webp)

Page d'accueil NtopNG

Les identifiants et mot de passe par défaut sont indiqués, donc il ne reste plus qu'a les renseigner!

## V. Utilisation de NtopNG

Lors de la première connexion, la première chose qui va vous être demandée est de changer le mot de passe admin par défaut et la langue, malheureusement, le Français n'en fait pas partie.

Vous arrivez ensuite sur le tableau de bord :

![Image](assets/fr/023.webp)

Tableau de bord NtopNG

Ne vous habituez pas à celui-ci! En effet, si vous remarquez l'encart jaune en haut de l'écran, vous verrez la phrase : "*Licence expire in 04:57*". Par défaut, l'installation lance un essai de la version complète de NtopNG, mais pour une durée (très) limitée. Une fois ce "compte à rebours" atteint, la version *community* est activée et le dashboard change :

![Image](assets/fr/024.webp)

Nouveau dashboard NtopNG en version community

La première chose à faire est de **vérifier que la bonne interface est en écoute**. En haut à gauche, la liste des interfaces disponibles sous forme de liste déroulante vous permet de sélectionner l'interface qui nous intéresse ici : br0

![Image](assets/fr/025.webp)

Sélection de l'interface

La nouvelle fenêtre affiche les "*Top Flaw Talkers*" soit les périphériques qui communiquent le plus. Ici je n'ai que deux postes qui apparaissent :

![Image](assets/fr/026.webp)

**Les hôtes sources apparaissent donc à gauche, les destinations à droite.** Cela permet de visualiser l'utilisation de chacun de la bande passante totale et d'avoir une visualisation d’ensemble sur le trafic réseau. C'est déjà pas mal, mais on peut aller plus loin...

Si je clique sur "*Hosts*" par exemple, j'ai un graphique qui me montre la consommation de chaque hôte de mon réseau en envoi et réception. Ici par exemple, je constate que 192.168.1.37 représente à lui seul 80% de mon trafic :

![Image](assets/fr/027.webp)

Si je clique sur l'adresse IP de l'hôte en question, je suis redirigé vers une page récapitulative :

![Image](assets/fr/028.webp)

Je vois par exemple qu'il s'agit d'une machine VMWare (par reconnaissance du OUI de m'adresse MAC), qu'elle s'appelle DESKTOP-GHEBGV1 (donc sûrement un hôte Windows) ET j'ai **les stats sur les paquets reçus et envoyés ainsi que la quantité de données**.

Vous remarquerez aussi qu'un nouveau menu en haut de ce récapitulatif est disponible, je vous propose de cliquer sur "**Apps**" pour voir qu'est-ce qui provoque tant de trafic :

![Image](assets/fr/017.webp)  
Ha, il semble qu'on ait une réponse! Sur le graphique de gauche, **on voit que 76,6% de son trafic est du ... Windows Update**, cet hôte est donc en train de télécharger des mises à jour!

NtopNG utilise une technologie appelée DPI pour *Deep Packet Inspection*, lui permettant de catégoriser chaque flux réseau et de définir l'application (ou la famille d'application) qui en est à l'origine.

Petite démonstration, je lance une vidéo YouTube sur mon hôte :

![Image](assets/fr/018.webp)

**Le trafic a immédiatement été reconnu et catégorisé!**

Note : pour des raisons évidentes, ce genre de logiciel peut poser des problèmes de respect de la vie privée, attention donc à l'utiliser dans les bonnes conditions. À noter également qu'il est possible d'**anonymiser les résultats**, l'option se trouve dans **Settings  > Preferences > Misc** et elle se nomme "**Mask Host IP Address**".

## VI. Détections & alertes

NtopNG est également capable d'émettre des alertes de sécurité sur certains flux. Celles-ci se trouvent dans le menu **Alerts**, sur le bandeau de gauche. Ici par exemple, j'ai en tout 2851 alertes, réparties en différentes sévérités : Notice, Warning et Error.

![Image](assets/fr/019.webp)

Intéressons-nous aux alertes de criticité élevées, j'en ai 17!

En cliquant sur ce chiffre, j'ai le détail des alertes. Ici rien d'alarmant, il s'agit d'un faux positif, le téléchargement des mises à jour étant catégorisées comme un transfert de fichier binaire dans un flux HTTP, ce qui peut en effet signifier une attaque.

![Image](assets/fr/020.webp)

Mais là pas de quoi s'inquiéter, toutefois, utilisant la version gratuite, je ne peux pas exclure des domaines ou des hôtes source des alertes, il faudra donc surveiller celles-ci pour éviter de passer à côté de certaines choses beaucoup plus inquiétantes. NtopNG va générer des alertes en cas de :

**Téléchargement de fichier binaire sur HTTP**
**Trafic DNS suspect**
**Utilisation d'un port non standard**
**Détection d'injection SQL**
**Cross-Site Scripting (XSS)**
*Etc.*

## VII. Conclusion

Dans ce tutoriel, nous avons vu **comment mettre en place une sonde avec NtopNG** nous permettant d'**analyser notre trafic réseau** pour visualiser l'utilisation des protocoles et l'occupation de chaque hôte, mais également détecter du trafic suspicieux.

Les fonctionnalités et possibilités sont nombreuses, je ne peux malheureusement tout vous présenter dans cet article, mais n'hésitez pas à explorer!

Cette solution peut tout à fait être mise en place de manière pérenne dans une infrastructure d'entreprise. À noter que NtopNG permet aussi un export des résultats vers une base InfluxDB, ce qui permet par exemple de se créer ses propres tableaux de bord avec un outil tiers comme Graphana.