---
name: OPNsense
description: Comment installer et configurer un firewall OPNsense ?
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

Dans ce tutoriel, nous allons découvrir le firewall open source OPNsense. Nous verrons quelles sont ses fonctionnalités principales, quels sont les prérequis, et comment effectuer l'installation de cette solution basée sur FreeBSD.

Avant de commencer, sachez qu'**OPNsense et pfSense sont tous deux des pare-feux open source** basés sur FreeBSD. Nous pouvons dire que pfSense est en quelque sorte le grand-frère d'OPNsense, car ce dernier en est un fork créé en 2015. Enfin, il est important de préciser que depuis 2017, **OPNsense est passé sur HardenedBSD à la place de FreeBSD**. HardenedBSD est une version renforcée de FreeBSD, qui intègre des fonctionnalités de sécurité avancées

OPNsense se distingue par son interface utilisateur plus moderne et **sa cadence de mise à jour plus fréquente**. En effet, le calendrier de mise à jour d'OPNsense comprend deux versions majeures par an, qui sont mises à jour toutes les deux semaines environ (ce qui donne lieu à des versions mineures). Ce suivi est très intéressant en comparaison de pfSense, si l'on s'intéresse aux versions communautaires de ces solutions.

![Image](assets/fr/050.webp)

## II. Les fonctionnalités d'OPNsense

OPNsense est un système d'exploitation conçu pour servir de pare-feu et de routeur, bien que ses fonctionnalités soient nombreuses et extensibles par l'installation de paquets additionnels. Adapté pour la production, il est utilisé principalement pour la sécurité des réseaux et la gestion des flux.

### A. Les fonctionnalités principales

Voici quelques-unes des principales fonctionnalités d'OPNsense :

- **Pare-feu et NAT** : OPNsense fournit des fonctionnalités avancées de pare-feu stateful avec filtrage par état, ainsi que des capacités de translation d'adresses réseau (NAT).

- **DNS/DHCP** : OPNsense peut être configuré pour gérer les services DNS et DHCP sur le réseau. Il peut assurer le rôle de serveur DHCP, mais aussi être utilisé comme résolveur DNS pour les machines du réseau local. Dnsmasq est aussi intégré par défaut.

- **VPN** : OPNsense supporte plusieurs protocoles VPN, y compris IPsec, OpenVPN, et WireGuard, permettant des connexions sécurisées pour l'accès distant des postes nomades ou l'interconnexion de sites.

- **Proxy Web** : OPNsense inclut un proxy web pour contrôler et filtrer l'accès à Internet. Il peut aussi être utilisé pour filtrer les contenus et gérer les accès au réseau.

- **Gestion de la bande passante (QoS)** : OPNsense offre des fonctionnalités de gestion de la qualité de service (QoS) pour prioriser le trafic réseau et ainsi mieux gérer la bande-passante du réseau.

- **Portail captif** : cette fonctionnalité permet de gérer l'accès des utilisateurs au réseau via une page d'authentification (base locale, vouchers, etc.). C'est une fonction couramment déployée pour les réseaux Wi-Fi publics.

- **IDS/IPS** : OPNsense intègre Suricata pour proposer des fonctions de détection et de prévention d'intrusions (IDS/IPS) afin de protéger le réseau contre les attaques.

- **Haute disponibilité (CARP)** : OPNsense supporte le protocole CARP (*Common Address Redundancy Protocol*) pour la mise en place de la haute disponibilité entre plusieurs firewalls OPNsense, garantissant que le service reste actif même en cas de panne matérielle.

- **Reporting et Monitoring** : OPNsense fournit des outils de reporting et de surveillance en temps réel pour suivre les performances du réseau (avec NetFlow) et détecter les problèmes potentiels, grâce à la création de logs. Cela inclut des graphiques. L'outil Monit est intégré à OPNsense et permet la supervision du firewall en lui-même.

### B. Les paquets additionnels

Ceci n'est qu'un aperçu des fonctionnalités proposées par OPNsense. De plus, le **catalogue de paquets** accessibles depuis l'interface d'administration d'OPNsense permet d'**enrichir le firewall de fonctionnalités additionnelles**. Par exemple, nous retrouvons : un client ACME, un agent Wazuh, le service de NTP Chrony, ou encore Caddy en tant que reverse proxy.

![Image](assets/fr/051.webp)

## III. Les prérequis d'OPNsense

Tout d'abord, vous devez déterminer où est-ce que vous allez installer OPNsense. Il y a plusieurs solutions envisageables, notamment l'installation sur :

* Un hyperviseur en tant que machine virtuelle, que ce soit Hyper-V, Proxmox, VMware ESXi, etc.
* Une machine en tant que système *bare-metal*. Il peut s'agir d'un mini PC qui assumera le rôle de firewall.

Vous avez aussi la possibilité d'acquérir **une appliance OPNsense rackable** par l'intermédiaire de la boutique en ligne.

Vous devez tenir compte des ressources matérielles nécessaires pour exécuter OPNsense. Ceci est détaillé sur [cette page de la documentation](https://docs.opnsense.org/manual/hardware.html).

**Voici les ressources minimales et recommandées pour la production :**

| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Finalement, **vos besoins en ressources dépendent surtout du nombre de connexions à gérer**, et donc de **votre besoin en bande-passante**. De plus, il faut aussi **tenir compte des services qui seront activés et utilisés** (proxy, détection d'intrusion, etc...) car ils peuvent être gourmands en CPU et/ou RAM.

Vous aurez aussi besoin de l'image ISO d'installation d'OPNsense à télécharger depuis [le site officiel](https://opnsense.org/download/). Pour une installation sur une VM, sélectionnez "**dvd**" comme type d'image pour obtenir une image ISO (et en faire ce que vous voulez...). Pour une installation via une clé USB bootable, sélectionnez l'option "**vga**" et vous obtiendrez un fichier "**.img**".

![Image](assets/fr/048.webp)

De plus, prévoyez un ordinateur pour effectuer l'administration d'OPNsense ainsi que des tests de bon fonctionnement.

## IV. Configuration cible

Notre objectif va être le suivant :

**Créer un réseau virtuel interne (192.168.10.0/24 - LAN)**, qui pourra accéder à internet, par l'intermédiaire du pare-feu OPNsense. Pour de la production, il pourra s'agir de votre réseau local, câble et/ou Wi-Fi.
**Activer et configurer le NAT** pour que les VM du réseau virtuel interne soient en mesure d'accéder à Internet
**Activer et configurer le serveur DHCP sur OPNsense** pour distribuer une configuration IP aux futures machines connectées au réseau virtuel interne
**Configurer le pare-feu** pour autoriser uniquement les flux sortants du LAN vers WAN en HTTP (80) et HTTPS (443).
* **Configurer le pare-feu** pour autoriser le LAN virtuel à utiliser OPNsense comme résolveur DNS (53).

Si vous utilisez la plateforme Hyper-V, ceci vous donnera la représentation suivante :

![Image](assets/fr/033.webp)

## V. Installation du firewall OPNsense

### A. Préparer la clé USB bootable

La première étape consiste à préparer le support d'installation : **la clé USB bootable avec OPNsense**. Ceci est bien sûr facultatif si vous travaillez sur un environnement virtuel, mais dans tous les cas, vous devez télécharger l'image ISO d'installation d'OPNsense.

Suite au téléchargement, vous obtenez **une archive comprenant une image au format ".img"**. Vous pouvez **créer une clé USB bootable** avec diverses applications, notamment **balenaEtcher** : ultra-simple à utiliser. De plus, l'application va reconnaître l'image dans l'archive, ce qui vous êtes de le décompresser en amont.

* [Télécharger balenaEtcher](https://etcher.balena.io/)

Une fois l'application installée, sélectionnez votre image, votre clé USB puis cliquez sur le bouton "**Flash!**". Patientez un instant.

![Image](assets/fr/049.webp)

Voilà, vous êtes prêts à effectuer l'installation.

### B. Installer le système OPNsense

Démarrez la machine destinée à accueillir OPNsense. Vous devriez avoir une page d'accueil similaire à celle ci-dessous. Pendant quelques secondes, l'écran présenté sera visible dans la fenêtre. Laissez le processus se dérouler...

![Image](assets/fr/019.webp)

L'image OPNsense va être chargée sur la machine, afin que le système soit accessible en "**live**", c'est-à-dire qu'il est mis en mémoire de façon temporaire.

![Image](assets/fr/025.webp)

Puis, vous arrivez sur une interface similaire à celle ci-dessous. Connectez-vous à l'aide du login "**installer**" et du mot de passe "**opnsense**". Attention, le clavier est en **QWERTY** pour le moment. À ce moment-là, nous allons **commencer le processus d'installation d'OPNsense**.

![Image](assets/fr/026.webp)

Un nouvel assistant s'affiche à l'écran. La première étape consiste à sélectionner la disposition du clavier correspondante à votre configuration. Pour un clavier AZERTY, sélectionnez l'option "**French (accent keys)**" dans la liste puis **validez par deux fois**.

![Image](assets/fr/027.webp)

La seconde étape consiste à choisir la tâche à effectuer. Ici, nous allons effectuer une installation en utilisant le **système de fichiers ZFS**. Positionnez-vous sur la ligne "**Install (ZFS)**" et validez avec **Entrée**.

![Image](assets/fr/028.webp)

À la troisième étape, sélectionnez "**stripe**" puisque notre machine est équipée d'**un seul disque** : il n'y a pas de redondance possible pour sécuriser le stockage du firewall et ses données. Ceci est surtout pertinent lors de l'installation sur une machine physique pour se prémunir contre une panne matérielle d'un disque, via le principe du RAID.

![Image](assets/fr/029.webp)

À la quatrième étape, appuyez simplement sur **Entrée** pour valider.

![Image](assets/fr/030.webp)

Enfin, validez en sélectionnant "**YES**" puis avec la touche **Entrée**.

![Image](assets/fr/031.webp)

Désormais, vous devez patienter pendant l'installation d'OPNsense... Ce processus nécessite environ 5 minutes.

![Image](assets/fr/032.webp)

Une fois l'installation terminée, nous pouvons de changer le mot de passe "**root**" avant de redémarrer. Sélectionnez "**Root Password**", appuyez sur **Entrée** et indiquez un mot de passe "**root**" par deux fois.

![Image](assets/fr/020.webp)

Enfin, sélectionnez "**Complete Install**" et appuyez sur **Entrée**. Profitez-en pour **éjecter le disque du lecteur DVD de la VM**. Dans les paramètres de la VM, vous pouvez aussi positionner en premier le démarrage sur le disque.

![Image](assets/fr/021.webp)

La machine virtuelle va redémarrer et charger le système OPNsense à partir du disque puisque nous venons de procéder à l'installation. Connectez-vous avec le compte "root" dans la console, et votre nouveau mot de passe (sinon le mot de passe par défaut est "**opnsense**").

### D. Associer les interfaces réseau

Vous allez arriver sur l'écran présenté ci-dessous. Faites le choix "**1**" et appuyez sur **Entrée** pour associer les cartes réseaux de la machine aux interfaces d'OPNsense.

![Image](assets/fr/022.webp)

D'abord, l'assistant propose de configurer une agrégation de liens et des VLANs, indiquez "**n**" pour refuser, et à chaque fois, validez votre réponse avec **Entrée**. Ensuite, vous devez affecter les deux interfaces : "**hn0**" et "**hn1**" au **WAN** et au **LAN**. En principe, "**hn0**" correspond au WAN et l'autre interface au LAN.

Voici la marche à suivre :

![Image](assets/fr/023.webp)

Désormais, nous avons :

* L'interface **LAN** associée à la carte réseau "**hn1**" et avec l'adresse IP par défaut d'OPNsense, à savoir **192.168.1.1/24**.
* L'interface **WAN** associée à la carte réseau "**hn0**" et avec une adresse IP récupérée via **DHCP** sur le réseau local (grâce à notre commutateur virtuel externe).

Par défaut, l'interface d'administration d'OPNsense est accessible uniquement depuis l'interface LAN, pour des raisons évidentes de sécurité. Vous devez donc vous connecter sur l'interface LAN du firewall pour effectuer l'administration. Si c'est impossible, sachez que vous pouvez administrer temporairement OPNsense depuis le WAN. Ceci implique de désactiver la fonction de firewall.

Pour cela, basculez en mode shell via l'option "**8**" et exécutez la commande suivante :

```
pfctl -d
```

![Image](assets/fr/024.webp)

### E. Accès à l'interface de gestion d'OPNsense

L**'interface d'administration d'OPNsense est accessible en HTTPS, via l'adresse IP de l'interface LAN** (ou éventuellement celle de la WAN). À partir de votre navigateur, vous arrivez sur une page de connexion. Connectez-vous avec le compte "root" et le mot de passe sélectionné précédemment.

![Image](assets/fr/034.webp)

Patientez quelques secondes... Vous serez invité à suivre un assistant pour effectuer la configuration de base. Cliquez sur "**Next**" pour continuer.

![Image](assets/fr/036.webp)

La première étape consiste à définir le nom d'hôte, le nom de domaine, à choisir la langue et à définir aussi le(s) serveur(s) DNS à utiliser pour la résolution de noms. Le fait de conserver l'option "**Enable Resolver**" permettra d'utiliser le firewall en tant que résolveur DNS, ce qui sera utile pour les machines de notre LAN virtuel.

![Image](assets/fr/037.webp)

Passez à l'étape suivante. L'assistant vous offre la possibilité de **définir un serveur NTP pour la synchronisation de la date et l'heure**, bien qu'il y ait déjà des serveurs configurés par défaut. De plus, il est essentiel de choisir le fuseau horaire correspondant à votre emplacement géographique (sauf besoin particulier).

![Image](assets/fr/038.webp)

Ensuite, vient une étape importante : **la configuration de l'interface WAN**. Actuellement, elle est configurée en DHCP et elle va rester dans ce mode de configuration, sauf si vous souhaitez définir une adresse IP statique.

![Image](assets/fr/039.webp)

Toujours sur la page de configuration de l'interface WAN, vous devez décocher l'option "**Bloquer l'accès à des réseaux privés via le WAN**" si le réseau côté WAN utilise un adressage privé. Ce sera probablement le cas si vous faites un Lab, et donc cela peut vous empêcher d'accéder à Internet.

![Image](assets/fr/040.webp)

Ensuite, vous pouvez **définir un mot de passe "root"**, mais c'est facultatif parce que nous l'avons déjà fait.

![Image](assets/fr/041.webp)

Poursuivez jusqu'à la fin afin d'enclencher le rechargement de la configuration. Si vous avez besoin de continuer à prendre la main via le WAN, relancez la commande évoquée précédemment une fois ce processus terminé.

![Image](assets/fr/042.webp)

Voilà, la configuration initiale est terminée !

![Image](assets/fr/035.webp)

### E. Configuration du DHCP

Nous avons pour objectif d'utiliser le serveur DHCP d'OPNsense pour distribuer des adresses IP sur le LAN virtuel. Pour cela, nous devons accéder à cet emplacement du menu : 

```
Services > ISC DHCPv4 > [LAN]
```

**Nous pouvons constater que le DHCP est déjà activé par défaut sur le LAN !** Si ce service ne vous intéresse pas, il conviendra de le désactiver. Bien qu'il soit déjà activé et que nous voulons l'utiliser, il est important de réviser sa configuration.

Vous pouvez éventuellement modifier la plage d'adresses IP à distribuer : **192.168.10.10** à **192.168.10.245**, selon les paramètres actuels.

![Image](assets/fr/046.webp)

Nous pouvons constater aussi que les champs "**Serveurs DNS**", "**Passerelle**", "**Nom de domaine**", etc... sont vides par défaut. En fait, il y a un héritage automatique de certaines options et des valeurs par défaut pour ces différents champs. Par exemple, pour le serveur DNS, l'adresse IP de l'interface LAN sera distribuée ce qui permettra d'utiliser le firewall OPNsense en tant que résolveur DNS.

Sauvegardez la configuration après avoir apporté des modifications, si nécessaire.

![Image](assets/fr/047.webp)

Pour tester le bon fonctionnement du serveur DHCP, vous devez connecter une machine sur le réseau LAN de votre firewall.

Cette machine doit récupérer une adresse IP à partir du serveur DHCP d'OPNsense et notre machine doit avoir accès au réseau. L'accès à Internet doit fonctionner. Attention, si vous avez désactivé la fonction de firewall pour accéder à OPNsense depuis le WAN, ceci désactive le NAT, et vous empêche donc d'accéder au Web.

**Remarque** : les baux DHCP actuellement délivrés sont visibles à partir de l'interface d'administration d'OPNsense. Pour cela, accédez à l'emplacement suivant : **Services > ISC DHCPv4 > Baux**.

![Image](assets/fr/045.webp)

### F. Configuration du NAT et des règles de firewall

La bonne nouvelle, c'est que désormais, nous pouvons accéder à l'interface d'administration d'OPNsense à partir du LAN.

```
https://192.168.1.10
```

Après s'être connecté à OPNsense, partons à la découverte de la configuration du NAT. Accédez à cet endroit : **Pare-feu > NAT > Sortant**. Ici, vous avez le choix entre la création de règles de NAT sortantes automatiques (mode par défaut) ou la création manuelle.

Choisissez le mode automatique via l'option "**Génération automatique des règles NAT sortantes**" et cliquez sur "**Sauvegarder**" (en principe, cette configuration est déjà celle active). En mode automatique, OPNsense crée lui-même une règle de NAT pour chacun de vos réseaux.

![Image](assets/fr/043.webp)

Pour le moment, tous les ordinateurs connectés au LAN virtuel "**192.168.10.0/24**" peuvent accéder à Internet sans restriction. Toutefois, notre objectif est de limiter l'accès vers le WAN aux seuls protocoles HTTP et HTTPS, ainsi que le DNS sur l'interface LAN du firewall.

Ainsi, nous devons créer des règles de pare-feu... Parcourez le menu de cette façon : **Pare-feu > Règles > LAN**.

**Par défaut, il y a deux règles pour autoriser tous les flux sortants du réseau LAN, en IPv4 et en IPv6**. Désactivez ces deux règles en cliquant sur la flèche verte tout à gauche, au début de chaque ligne.

Puis, créez trois nouvelles règles pour autoriser le **réseau LAN** (soit "**LAN net**") à :

*accéder à toutes les destinations en* **HTTP**.
*accéder à toutes les destinations en **HTTPS**.*
* solliciter **OPNsense** sur son **interface LAN** (soit "**LAN adresse**"), via le **protocole DNS** (ceci implique d'utiliser le firewall comme DNS), sinon autoriser votre résolveur DNS via son adresse IP.

Ce qui donne le résultat suivant :

![Image](assets/fr/044.webp)

Il ne reste plus qu'à cliquer sur "**Appliquer les changements**" pour basculer en production les nouvelles règles de pare-feu. **Sachez que tous les flux qui ne sont explicitement autorisés seront bloqués par défaut.**

La machine du LAN peut accéder à Internet, en naviguant en HTTP et HTTPS. Tous les autres protocoles seront bloqués.

![Image](assets/fr/018.webp)

## IV. Conclusion

En suivant ce guide, vous êtes désormais capable d'installer OPNsense et d'effectuer une première prise en main. OPNsense offre une large gamme de fonctionnalités pour sécuriser et gérer efficacement le trafic de votre réseau, et il est adapté pour une utilisation en environnement professionnel.

Cette installation n'est que le début : n'hésitez pas à explorer les menus et à configurer d'autres fonctionnalités pour adapter OPNsense à vos besoins.