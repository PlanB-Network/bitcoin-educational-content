---
name: WireGuard
description: Mise en place de WireGuard VPN sur Debian et Windows
---
![cover](assets/cover.webp)

___

*Ce tutoriel est basé sur le contenu original de Florian BURNEL publié sur [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Des modifications ont pu être apportées au texte original.*

___

## I. Présentation

Dans ce tutoriel, nous allons apprendre à configurer un VPN basé sur WireGuard, une solution VPN gratuite et open source qui permet d'augmenter les performances, sans pour autant négliger la sécurité.

WireGuard est une solution relativement récente puisqu'elle est disponible en version stable depuis mars 2020 et elle a l'honneur d'être intégrée directement au **noyau Linux depuis la version 5.6**. Cela ne l'empêche pas d'être accessible depuis d'anciennes distributions de Linux qui utilisent une autre version du noyau. En comparaison de solutions comme OpenVPN et IPSec, WireGuard se veut plus simple dans son fonctionnement et beaucoup plus rapide, comme nous le verrons en fin d'article.

Quelques points clés de WireGuard :

* Simple, léger et ultra efficace !
* Fonctionne uniquement en UDP (ce qui peut être un inconvénient pour traverser certains firewalls)
* Fonctionne selon le modèle peer-to-peer et non "client-serveur"
* Authentification par un échange de clé, sur le même principe que SSH avec les clés privées/publiques
* Utilisation de plusieurs algorithmes : chiffrement symétrique avec ChaCha20, authentification des messages avec Poly1305, ainsi que d'autres comme Curve25519, BLAKE2 et SipHash24
* Supporte aussi bien IPv4 que IPv6
* Multiplateformes : Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (et implémenté dans ProtonVPN)
* Seulement 4 000 lignes de code, là où les autres solutions en comptent plusieurs centaines de milliers

Pour la partie cryptographique, les différents algorithmes utilisés sont triés sur le volet, audité de plusieurs façons, et examinés par des chercheurs en sécurité spécialisés dans le domaine.

Le site officiel du projet : [wireguard.com](https://www.wireguard.com/)

Alors convaincu par cette solution suite à la lecture de cette introduction ? Il ne reste plus qu'à poursuivre la lecture de cet article !

## II. Schéma du lab WireGuard

Avant de vous présenter mon lab pour la mise en place de WireGuard, sachez que l'on peut imaginer **mettre en place WireGuard pour interconnecter deux infrastructures distantes**, mais aussi pour **connecter un client distant à une infrastructure tel qu'un réseau d'entreprise ou le réseau de son domicile**. Cela dans le même esprit qu'on le ferait avec OpenVPN, comme nous l'avons vu récemment dans le tutoriel "[OpenVPN sur Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".

Si WireGuard n'est pas mis en place directement sur le routeur ou le pare-feu, comme on peut imaginer le faire avec OpenWRT, il faudra mettre en place une redirection de port afin que le flux parvienne jusqu'au paire WireGuard.

![Image](assets/fr/034.webp)

Maintenant, je vais vous parler de mon lab et de ce que nous allons mettre en place aujourd'hui.

Je vais utiliser une machine Debian 11 comme serveur WireGuard et un poste client sous Windows en guise de client VPN WireGuard. Même si cela est un peu trompeur de parler d'une relation client-serveur, car **WireGuard fonctionne selon le modèle "peer-to-peer"**. Un bel abus de langage lorsque l'on cherche à mettre en place une connexion "client-to-site". Disons plutôt que je vais avoir deux paires ou **deux points de connexion WireGuard** si vous préférez : l'un sous Debian 11 et l'autre sous Windows.

Ces deux paires peuvent communiquer ensemble dans les deux sens, cela signifie que depuis ma machine Windows je peux accéder au LAN distant de la machine Debian 11, et que l'inverse est possible aussi : tout dépend de la configuration du tunnel et du pare-feu du pair WireGuard.

Dans cet exemple, je vais me concentrer sur le cas suivant : **depuis mon Peer 1 sous Windows connecté sur le réseau de mon domicile, je souhaite accéder à mon réseau d'entreprise afin d'accéder aux serveurs de l'entreprise via le tunnel VPN WireGuard**. Ce qui donne ce schéma :

![Image](assets/fr/035.webp)

Au niveau des adresses IP, cela donne :

* **Réseau du domicile** : 192.168.1.0/24
* **Réseau d'entreprise** : 192.168.100.0/24
* **Réseau du tunnel WireGuard** : 192.168.110.0/24
  + Adresse IP du Peer 1 (Windows) dans le tunnel : 192.168.110.2/24
  + Adresse IP du Peer 2 (Debian) dans le tunnel : 192.168.110.121/24

Voilà, le décor est planté ! Passons à la configuration !

**Note** : par défaut, WireGuard fonctionne en UDP sur le **port 51820**.

## III. Installation et configuration du serveur WireGuard

Je vais utiliser les termes "client" pour la machine Windows et "serveur" pour la machine Debian dans ce tutoriel, car même si c'est du peer-to-peer, cela me semble plus parlant.

### A. Installer WireGuard sur Debian 11

Le paquet d'installation de WireGuard est disponible dans les dépôts officiels de Debian 11. Nous n'avons qu'à mettre à jour le cache des paquets et à l'installer :

```
sudo apt-get update
```

```
sudo apt-get install wireguard
```

![Image](assets/fr/022.webp)

La partie serveur de WireGuard sera installée, ainsi que différents outils donnant accès à des commandes utiles pour gérer la configuration.

### B. Mettre en place une interface WireGuard

À l'aide de la **commande "wg"** nous devons générer une clé privée et une clé publique : indispensable pour l'authentification entre deux paires, c'est-à-dire le serveur et un client (qui devra aussi disposer d'un couple de clés).

Nous allons créer la clé privée "**/etc/wireguard/wg-private.key**" et la clé publique "**/etc/wireguard/wg-public.key**" grâce à cet enchaînement de commandes :

```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```

![Image](assets/fr/023.webp)

La valeur de la clé publique sera retournée dans la console. Au sein du fichier de configuration de WireGuard, nous devons **ajouter la valeur de notre clé privée**. Pour récupérer cette valeur, saisissez la commande ci-dessous et copiez la valeur :

```
sudo cat /etc/wireguard/wg-private.key
```

Il est temps de créer un fichier de configuration dans "**/etc/wireguard/**". Par exemple, nous pouvons nommer ce fichier "**wg0.conf**", si l'on estime que l'interface réseau associée à WireGuard sera "wg0", sur le même principe que l'on trouve "eth0", par exemple.

```
sudo nano /etc/wireguard/wg0.conf
```

Dans ce fichier, nous devons ajouter le contenu suivant dans un premier temps (nous reviendrons le compléter par la suite) :

```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```

La section `[Interface]` sert à déclarer la partie serveur. Voici quelques informations :

* **Address** : l'adresse IP de l'interface WireGuard au sein du tunnel VPN (sous-réseau différent du LAN distant)
* **SaveConfig** : la configuration est mise en mémoire (et protégée) tout le temps que l'interface est active
* **ListenPort** : le port d'écoute de WireGuard, ici c'est 51820 qui est le port par défaut, mais je vous invite à le personnaliser
* **PrivateKey** : la valeur de la clé privée de notre serveur (*wg-private.key*)

Sauvegardez le fichier et fermez-le. Avec la commande "**wg-quick**", nous pouvons démarrer cette interface en précisant son nom (wg0, car le fichier se nomme wg0.conf) :

```
sudo wg-quick up wg0
```

Si vous listez les adresses IP de votre serveur Debian 11, vous allez voir une nouvelle interface nommée "wg0" avec l'adresse IP définie dans le fichier de config :

```
ip a
```

![Image](assets/fr/027.webp)

Dans le même esprit, nous pouvons afficher la configuration de l'interface "wg0" via la commande "wg show" :

```
sudo wg show wg0
```

![Image](assets/fr/024.webp)

Enfin, il reste à activer le démarrage automatique de notre interface wg0 WireGuard :

```
sudo systemctl enable wg-quick@wg0.service
```

Pour le moment, nous allons laisser de côté la configuration de la partie serveur de WireGuard.

### C. Activer l'IP Forwarding

Pour que notre machine Debian 11 soit en mesure de **router les paquets entre les différents réseaux (tel un routeur)**, c'est-à-dire entre le réseau du VPN et le réseau local, nous devons activer l'[IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Par défaut, cette fonctionnalité est désactivée.

Modifiez ce fichier de configuration :

```
sudo nano /etc/sysctl.conf
```

Ajoutez la directive suivante à la fin du fichier et enregistrez :

```
net.ipv4.ip_forward = 1
```

Voilà, c'est tout.

### D. Activer l'IP Masquerade

Pour que notre serveur puisse router correctement les paquets et que le LAN distant soit accessible à la machine Windows, il faut activer l'IP Masquerade sur notre serveur Debian. C'est en quelque sorte l'activation du NAT. Je vais effectuer cette configuration sur le pare-feu Linux au travers d'UFW que j'ai l'habitude d'utiliser ([tutoriel ufw sur Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).

Si vous n'avez pas encore UFW et que vous souhaitez le mettre en place (vous pouvez aussi passer par Nftables), commencer par l'installer :

```
sudo apt install ufw
```

Tout d'abord, il faut autoriser le SSH pour ne pas perdre la main sur le serveur distant (adaptez le numéro de port) :

```
sudo ufw allow 22/tcp
```

Le port 51820 en UDP doit aussi être autorisé, car nous l'utilisons pour WireGuard (là encore, adaptez le numéro de port) :

```
sudo ufw allow 51820/udp
```

Ensuite, on va poursuivre la configuration afin d'activer l'IP masquerade. Pour cela, il faut récupérer le nom de l'interface qui est connectée au réseau local. Si vous ne connaissez pas le nom, exécutez "ip a" afin de voir le nom de la carte. Dans mon cas, on peut voir que c'est la carte "**ens192**".

![Image](assets/fr/036.webp)

On va se servir de cette information. Éditez le fichier suivant :

```
sudo nano /etc/ufw/before.rules
```

Ajoutez ces lignes à la fin du fichier afin d'**activer l'IP masquerade sur l'interface ens192** (adaptez le nom de l'interface) au sein de la chaîne POSTROUTING de la table NAT de notre pare-feu local :

```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```

Ce qui donne, en image :

![Image](assets/fr/037.webp)

Gardez ce fichier de configuration ouvert et passez à l'étape suivante. 😉

### E. Configuration du pare-feu Linux pour WireGuard

Toujours au sein du même fichier de configuration, on va déclarer le réseau d'entreprise "192.168.100.0/24" afin que l'on puisse le contacter. Voici les deux règles à ajouter (idéalement après la section "*# ok icmp code for FORWARD*" pour regrouper les règles) :

```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```

Si l'on souhaite autoriser seulement un hôte, par exemple "192.168.100.11", c'est simple :

```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```

Désormais, vous pouvez sauvegarder le fichier puis le fermer. Il ne reste plus qu'à activer UFW et à redémarrer le service pour appliquer nos changements :

```
sudo ufw enable
```

```
sudo systemctl restart ufw
```

La première partie de la configuration du serveur Debian est terminée.

## IV. Client WireGuard sous Windows

Le client WireGuard est disponible pour Windows, macOS, Android, etc... C'est une bonne nouvelle. Tous les téléchargements sont accessibles sur cette page : [Client WireGuard](https://www.wireguard.com/install/). Dans cet exemple, je vais configurer le client sous Windows. Pour mettre en place le client WireGuard sous Linux, il faut reprendre le même principe que pour créer le fichier wg0.conf sur la machine Debian (sans toute la partie NAT, etc.).

### A. Installer le client WireGuard Windows

Après avoir téléchargé l'exécutable ou le package MSI, l'installation est simple puisqu'il suffit de lancer l'installeur, et puis...voilà, c'est fait ! 🙂

![Image](assets/fr/038.webp)

### B. Créer un profil WireGuard

Commencez par ouvrir le logiciel afin de créer un nouveau tunnel, pour cela cliquez sur la flèche à droite du bouton "**Ajouter le tunnel**" et cliquez sur le bouton "**Ajouter un tunnel vide**".

![Image](assets/fr/028.webp)

Une fenêtre de configuration va s'ouvrir. À chaque fois que l'on crée une nouvelle configuration de tunnel, WireGuard génère un couple de clés privé/public propre à cette configuration. **Dans cette configuration, nous devons déclarer le "peer", c'est-à-dire le serveur distant.**Pour le moment, nous avons seulement ceci :

```
[Interface]
PrivateKey = <la clé privée du PC>
```

Nous devons compléter cette configuration, notamment pour déclarer l'adresse IP sur cette interface (*Address*), mais aussi pour déclarer le serveur WireGuard distant via un bloc `[Peer]`. L'image ci-dessous doit vous rappeler le fichier de configuration que l'on a créé du côté du serveur Linux.

Commençons par le bloc `[Interface]` en ajoutant l'adresse IP "**192.168.110.2**" ; je vous rappelle que le serveur dispose de l'adresse IP "**192.168.110.121**" sur ce segment réseau. Ce qui donne :

```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```

Ensuite, nous devons déclarer le bloc "Peer" avec trois propriétés, ce qui donne cette configuration :

```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```

En image :

![Image](assets/fr/029.webp)

**Quelques explications au sujet du bloc `[Peer]`** :

* **PublicKey** : il s'agit de la clé publique du serveur WireGuard Debian 11 (vous pouvez obtenir sa valeur via la commande "*sudo wg*")
* **AllowedIPs** : il s'agit des adresses IP / des sous-réseaux accessibles via ce réseau VPN WireGuard, ici il s'agit du sous-réseau propre à mon VPN WireGuard (*192.168.110.0/24*) et de mon LAN distant (*192.168.100.0/24*)
* **Endpoint** : il s'agit de l'adresse IP de l'hôte Debian 11 puisque c'est notre point de liaison WireGuard (il faudra préciser l'adresse IP publique)

Pour finir, donnez un nom en renseignant le champ "**Nom**" (sans espaces) et copiez-collez la clé publique du client, car nous allons devoir la déclarer sur le serveur. Cliquez sur "**Enregistrer**".

### C. Déclarer le client sur le serveur WireGuard

Il est temps de retourner sur le serveur Debian dans le but de déclarer le "**Peer**" c'est-à-dire notre PC Windows dans la configuration de WireGuard. Tout d'abord, il faut **stopper l'interface "wg0"** afin de pouvoir modifier sa configuration :

```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```

Ensuite, modifiez le fichier de configuration précédemment créé :

```
sudo nano /etc/wireguard/wg0.conf
```

Dans ce fichier, à la suite du bloc `[Interface]`, il faut que l'on déclare un bloc `[Peer]` :

```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```

Ce bloc `[Peer]` contient la clé publique du PC Windows 10 (**PublicKey**) ainsi que l'adresse IP de l'interface de ce PC (**AllowedIPs**) : le serveur communiquera dans ce tunnel WireGuard uniquement pour contacter le client Windows, d'où la valeur "**192.168.110.2/32**".

Il ne reste plus qu'à sauvegarder le fichier (*CTRL+O puis Entrée puis CTRL+X via Nano*). Relancez l'interface "wg0" :

```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```

Pour vérifier que la déclaration du "peer" fonctionne, vous pouvez utiliser cette commande :

```
sudo wg show
```

À partir du moment où l'hôte distant aura monté sa connexion WireGuard, son adresse IP va remonter au sein de la valeur "endpoint".

![Image](assets/fr/033.webp)

Pour finir, on va sécuriser les fichiers de configuration pour limiter l'accès à "root" :

```
sudo chmod 600 /etc/wireguard/ -R
```

### D. Première connexion avec WireGuard

La configuration est prête, nous pouvons l'initier depuis le PC Windows. Pour cela, au sein du client "**WireGuard**", cliquez sur le bouton "**Activer**" : la connexion va **passer de "Eteinte" à "Activée"**, mais cela ne veut pas dire que ça fonctionnera. Tout dépend si toute votre configuration est correcte ou non. **Lorsque la connexion est établie, nos deux machines communiquent via l'interface WireGuard configurée de chaque côté !**

![Image](assets/fr/030.webp)

En cas de problème, ce sera visible au sein de l'onglet "**Journal**". Les deux hôtes vont s'échanger des paquets régulièrement pour vérifier l'état de la connexion, d'où les messages "*Receiving keepalive packet from peer 1*".

![Image](assets/fr/031.webp)

Si l'onglet "**Journal**" de WireGuard affiche un message tel que celui ci-dessous, vous devez vérifier que les clés publiques déclarées des deux côtés sont correctes.

```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```

À partir de mon PC distant, je peux pinguer l'adresse IP de mon interface WireGuard côté serveur, ainsi qu'un hôte de mon LAN distant.

![Image](assets/fr/032.webp)

### E. Performances : OpenVPN vs WireGuard

À partir de mon PC distant connecté à mon VPN WireGuard, j'ai pu accéder à un serveur de fichiers et transférer un fichier par [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), pour voir le taux de transfert. **Avec WireGuard, je plafonne à 45 Mo/s environ, ce qui est top, car je suis en WiFi.**

![Image](assets/fr/025.webp)

Dans les mêmes conditions, mais via une connexion OpenVPN (en UDP) cette fois-ci, avec la même opération, le débit est totalement différent : 3 Mo/s environ. La différence est flagrante !

![Image](assets/fr/026.webp)

Au-delà de sa vitesse accrue dans les transferts, c'est également **la connexion qui est beaucoup plus rapide !** Cela est intéressant, car par exemple si l'on bascule d'une connexion WiFi à une connexion 4G/5G, la reconnexion sera tellement rapide que l'interruption ne sera pas visible.

### F. Bonus : full tunnel WireGuard

Avec la configuration actuelle, une partie des flux passent par le VPN, et le reste passe par la connexion Internet du client, et c'est notamment le cas de la navigation Internet. Si l'on veut passer en **mode "full tunnel" WireGuard** pour que tout passe par le tunnel VPN, il y a quelques modifications à apporter à notre configuration....

Tout d'abord, il faut installer le paquet "resolvconf" sur le serveur :

```
sudo apt-get update
sudo apt-get install resolvconf
```

Une fois que c'est fait, il faut modifier le profil "wg0.conf" sur la machine Debian : on stoppe l'interface, on modifie, et on relance.

```
sudo wg-quick down /etc/wireguard/wg0.conf
```

Ensuite, **dans le bloc `[Interface]`, on ajoute le serveur DNS à utiliser**. Dans mon cas, c'est le contrôleur de domaine de mon lab, mais on pourrait aussi installer Bind9 sur la machine Debian pour avoir un résolveur local.

```
DNS = 192.168.100.11
```

On sauvegarde le fichier, puis on relance l'interface :

```
sudo wg-quick up /etc/wireguard/wg0.conf
```

Enfin, au niveau de la configuration du tunnel sur le poste Windows 10, il faut modifier la section "AllowedIPs" pour indiquer que tout doit passer dans le tunnel. Remplacez :

```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```

Par :

```
AllowedIPs = 0.0.0.0/0
```

On peut voir que cela active aussi l'option "**Bloquer tous les trafic hors tunnel (interrupteur)**" (*kill switch*).

![Image](assets/fr/040.webp)

Pour finir, je profite de ce full tunnel pour réaliser un petit test de débit dont voici les résultats :

![Image](assets/fr/039.webp)

La configuration de WireGuard est assez simple et facile à comprendre, et surtout à maintenir. **WireGuard est considéré comme l'avenir des VPN**, alors nous avons tout intérêt à le suivre de près ! Nous pouvons voir également que le bénéfice est important au niveau des performances, ce qui est un énorme avantage pour WireGuard en comparaison d'OpenVPN.

Documentations supplémentaires :

* [Man - Commande wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
* [Man - Commande wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)

**Voilà, votre VPN WireGuard est en place et il est opérationnel ! Félicitations !**
