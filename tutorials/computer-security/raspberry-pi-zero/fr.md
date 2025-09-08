---
name: Raspberry Pi Zero
description: Comment construire un ordinateur minimal, isolé et peu coûteux en utilisant un Raspberry Pi Zero et un kit d’accessoires.
---
![cover](assets/cover.webp)



Si vous êtes sur les pages de Plan ₿ Network depuis un certain temps, vous avez déjà appris que l'un des paramètres de sécurité les plus préconisés, presque un must, **est la gestion des fonds par le stockage hors ligne de vos clés privées**.



Si vous ne l'avez pas encore découvert, vous trouverez tout au long de ce tutoriel des liens vers des ressources open source qui vous permettront d'en savoir plus.



Pour gérer les clés privées hors ligne, il faut donc un appareil en permanence déconnecté du réseau, qu’il s’agisse d’un [portefeuille matériel](https://planb.network/resources/glossary/hardware-wallet) ou d’un ordinateur en airgap, dédié à cette fonction spécifique.



Comment faire si, par exemple, vous n'avez pas la possibilité d'acheter du matériel qui n'exécute que cette tâche, mais que vous ne voulez pas renoncer à cette mesure de sécurité ?



## La solution


Et si je vous disais qu'il est possible de fabriquer un appareil hors ligne sous la forme d'un ordinateur airgap qui a la taille et le poids d'une clé USB et qui coûte 35 euros ? Vous n'y croiriez pas ?



Poursuivre la lecture.



Je vais vous en dire plus : lisez jusqu'au bout. La solution proposée est bon marché, mais elle n'est pas vraiment la plus facile. Il faut d'abord se faire une idée générale, puis décider d'investir un peu de son temps dans des recherches personnelles et choisir, avec le plus de sérénité possible, si l'on veut poursuivre ou non et comment.



## Exigences


**1** Un [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): le PI Zero (sans aucun suffixe) constitue la base pour réaliser un ordinateur aux performances minimales, mais il est surtout dépourvu de cartes Wi-Fi et Bluetooth, exigences indispensables pour l’objectif de cet exercice.





- Coût** : environ 15,00 au moment de la rédaction de ce tutoriel (août 2025).
- Continuité de la production** : Raspberry garantit la production jusqu'en janvier 2030.



Les PI Zero sans Wi-Fi ni Bluetooth sont malheureusement devenues pratiquement indisponibles. Vous pourrez peut-être trouver plus facilement des alternatives aux PI Zero W et PI Zero 2W. Dans ce cas, vous pouvez désactiver les fonctions de connexion en modifiant le fichier de configuration. Après avoir installé le système d'exploitation, vous devrez ajouter ces éléments au fichier de configuration :



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



une section de ce guide vous montrera comment et où procéder. Toutefois, si vous voulez vraiment être sûr, vous pouvez trouver sur le web plusieurs tutoriels pour retirer la puce Wi-Fi à l'aide d'un petit cutter, le genre qui convient pour travailler sur les cartes électroniques.



**2** Un _starter kit_ pour Raspberry PI Zero : comme c'est la pratique pour le monde Raspberry, bare bones, sans boîtier externe. De plus, les ressources limitées d'une si petite carte conditionnent les possibilités de connexion avec le monde extérieur.



Lorsque j'ai décidé de me lancer, j'ai trouvé [ce kit](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) plein d'accessoires, pour profiter pleinement du potentiel de la PI Zero. En effet, le kit contient une alimentation USB A -> micro USB Supply, un petit hub USB, un adaptateur mini-HDMI -> HDMI, un dissipateur thermique en cuivre, et un boîtier extérieur en aluminium. Le kit contient également les vis et la clé Allen nécessaires à l'installation de la PI Zero dans le nouveau boîtier.





- Coût** : 19.99 euros.



**3** Ce tutoriel n'exige pas que vous consacriez de gros budgets à l'ordinateur airgap. Sachez cependant que vous aurez besoin d'un clavier et d'une souris USB (strictement filaires, évitez le Bluetooth) et d'un moniteur. Selon l'entrée de votre moniteur, vous aurez peut-être besoin d'un adaptateur mini-HDMI, la seule sortie disponible sur la PI Zero. Enfin, regardez le Hard pour le fait que nous avons tous un clavier et une souris non filaires à la maison quelque part - il est temps de les retirer du Dust.



## Budget supplémentaire



**4** Vous pouvez obtenir la puissance originale Supply auprès de Raspberry, qui coûte environ 15,00 euros.



**5** J'ai personnellement opté pour l'alimentation Supply fournie dans le _starter kit_, en la combinant toutefois avec un câble USBA → miniUSB dit `no data`, coûtant 3,70 euros.



**6** Une carte micro SD, pour avoir un minimum d'au moins 32 Go de mémoire de masse ; si la qualité/le niveau industriel est meilleur.



**7** Vous aurez besoin d'un système, d'un adaptateur USB vers micro SD, comme celui que vous voyez sur la photo. Le système d'exploitation et la mémoire de votre PI Zero fonctionneront sur ce support.



![img](assets/it/06.webp)



## Installation du système d'exploitation


Avant de ranger votre PI Zero dans sa mallette, je vous recommande d'installer le système d'exploitation. Vous pourrez ainsi vérifier la LED qui indique le fonctionnement, dès le départ.



Pour choisir et graver le système d'exploitation, j'ai opté pour la méthode la plus simple : utiliser l'outil `PI Imager` du Raspberry.



![img](assets/it/01.webp)



Rendez-vous donc sur le [Github de Raspberry](https://github.com/raspberrypi/rpi-imager/releases) pour télécharger la dernière version de l’Imager, en choisissant celle la plus adaptée à votre système d’exploitation (v. 1.9.6 au moment de la rédaction). Vous remarquerez qu’à côté de chaque élément se trouve également le hachage du fichier correspondant. Cela nous sera utile pour la vérification.



![img](assets/it/02.webp)



Je vous recommande de vérifier le système d'exploitation que vous utiliserez sur votre ordinateur airgap, pour votre propre tranquillité d'esprit. Vous aurez ainsi la certitude d'utiliser une version légitime (et non malveillante) de l'imageur et, par conséquent, du système d'exploitation Raspi.



Effectuez la vérification immédiatement après le téléchargement, avec votre machine habituelle connectée à l'internet



Ouvrez ensuite le terminal Linux et préparez le téléchargement, en créant un répertoire `raspios` utile pour travailler avec.



![img](assets/it/19.webp)



Téléchargez l'imageur pour votre distribution Linux avec `wget`.



![img](assets/it/20.webp)



Enfin, lancez la commande `sha256sum` et comparez le Hash avec celui fourni par Raspberry dans son Github.



![img](assets/it/21.webp)



Ou, si vous avez Windows, ouvrez le Power Shell et tapez la commande suivante :



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Vous obtiendrez le Hash qui doit correspondre à celui publié sur Raspberry Github.



Une fois que vous avez vérifié le téléchargement, vous pouvez installer Imager sur votre ordinateur quotidien et l'ouvrir. Imager est l'outil dont vous avez besoin pour graver le système d'exploitation sur la micro SD, qui sera le "disque système" de PI Zero.



Le processus est extrêmement simple : choisissez d'abord le Raspberry que vous allez utiliser (faites donc attention à **votre modèle** de Raspi Zero), puis la version du système d'exploitation, et enfin le point de montage de la carte micro SD sur laquelle vous souhaitez flasher le système d'exploitation.



### Première étape



![img](assets/it/03.webp)



### Deuxième étape



![img](assets/it/07.webp)



**Notez bien** : choisissez `PI OS 32-bit`, le seul qui fonctionne avec PI Zero.



### Troisième étape



![img](assets/it/08.webp)



(Veillez à ne pas sélectionner _Exclure le lecteur système_ pour éviter d'être invité à installer le système d'exploitation de Raspi sur votre ordinateur)



Lorsque tout est configuré, l'imageur vous demande si vous souhaitez utiliser des paramètres personnalisés. Choisissez ce que vous voulez ou cliquez sur _No_ pour continuer avec les options par défaut.



![img](assets/it/09.webp)



Confirmez que vous souhaitez supprimer le contenu de la micro SD



![img](assets/it/10.webp)



L'imageur commence à transférer le système d'exploitation sur le micro SD, une barre de défilement vous informe de la progression.



![img](assets/it/11.webp)



A la fin, il y a une vérification automatique, je vous conseille de ne pas l'arrêter.



![img](assets/it/12.webp)



Enfin, un message apparaît à l'écran et, si tout s'est déroulé correctement, il ressemble à ce que vous voyez sur l'image.



![img](assets/it/13.webp)



Vous pouvez désormais retirer réellement la micro SD du lecteur et la placer dans le logement de la PI Zero. Allumez la petite Raspberry et observez la LED : nous nous attendons à ce qu’elle soit verte et qu’elle clignote, indiquant le chargement normal du système d’exploitation, puis qu’elle reste allumée de manière continue. Si vous avez d’autres indications, par exemple si la LED clignote à fréquence régulière ou est rouge, consultez la FAQ ou [les pages du forum de support](https://forums.raspberrypi.com/).



## Première configuration


Le premier démarrage de Raspi OS est un peu plus lent que d'habitude car il doit effectuer un certain nombre de tâches d'installation. Mais si tout s'est bien passé, vous verrez apparaître un écran de bienvenue.



![img](assets/it/14.webp)



Cliquez sur _Suivant_ pour définir la région géographique, notamment pour charger le bon clavier. Faites particulièrement attention à ce dernier point.



![img](assets/it/15.webp)



Cliquez sur _Suivant_ et vous serez invité à créer votre utilisateur, notez vos informations d'identification et conservez-les précieusement.



![img](assets/it/16.webp)



L'assistant vous demande de choisir un navigateur web par défaut, entre Chromium et Firefox ; il peut également vous demander les paramètres du réseau Wi-Fi si vous travaillez avec un PI Zero W ou 2W. Allez-y et cliquez sur _Skip_.



À un moment donné, vous serez invité à mettre à jour le logiciel embarqué et le système d'exploitation. Choisissez _Skip_ : pour les besoins de cet exercice, nous construisons en fait une machine hors ligne, qui doit rester hors ligne à partir de ce moment.



Enfin, il peut vous demander d'activer `ssh`, mais déclinez cette étape également, puisqu'il s'agit d'une IP à espace aérien zéro.



![img](assets/it/17.webp)



Il n'y a pas grand-chose d'autre à configurer. Lorsque vous avez terminé, redémarrez le Raspberry pour que les modifications soient prises en compte.



![img](assets/it/18.webp)



## Un nouveau trou d'air informatique


Après le redémarrage, votre nouvel ordinateur airgap est prêt. PI Zero vous montre le nouveau bureau, avec lequel vous pouvez travailler soit via l'interface graphique, soit à partir de la ligne de commande.



![img](assets/it/22.webp)



### Premiers pas vers l'IP zéro W ou 2W


Si vous travaillez avec un Raspberry PI Zero de la série W ou 2W, votre carte est équipée de puces Wi-Fi et Bluetooth. Lors de la première installation, vous avez sauté la configuration de la connexion, de sorte que le PI Zero n'est pas connecté à Internet. Vous pouvez maintenant désactiver ces deux puces de manière permanente via le logiciel.



En fait, Raspi OS fournit un fichier `config.txt` que vous pouvez éditer à votre guise. Le `config` est situé dans la partition `boot`, dans le répertoire `firmware`, et vous pouvez l'éditer et le sauvegarder avec les privilèges `root`.



Ouvrez le terminal à partir de l'icône en haut à gauche et il devient `root`.(1)



![img](assets/it/23.webp)



(1) Si Raspi OS ne vous a pas demandé de créer le mot de passe `root` lors des étapes précédentes, je vous recommande de le faire maintenant, avec la commande `passwd`. Avoir l'utilisateur `root` indépendant de votre utilisateur personnel peut s'avérer très pratique dans les situations de récupération.



Avec le terminal, vérifiez la présence du fichier `config.txt` et préparez-vous à l'éditer avec l'éditeur `nano`.



![img](assets/it/24.webp)



L'édition doit être faite en bas de l'ensemble de `config`, après les mots `[All]`. C'est à ce moment que vous ajouterez les commandes `dtoverlay` présentées au début du tutoriel.



![img](assets/it/25.webp)



Sauvegardez, fermez et redémarrez. Dans l'étape suivante, nous allons passer à l'exploration du petit Raspberry.



## Que peut-on attendre de ce dispositif ?


En consultant les [caractéristiques techniques](https://www.raspberrypi.com/products/raspberry-pi-zero/) sur le site de Raspberry, la PI Zero est dotée d’un processeur monocœur BCM2835 et de 512 Mo de RAM, et ne semble donc pas très puissante.



Le terminal étant plus léger, nous utiliserons la ligne de commande pour explorer les configurations du système.



Lors de la mise sous tension, vous verrez un bref écran aux couleurs de l'arc-en-ciel, suivi d'un message de bienvenue de Raspberry et, dans le coin inférieur gauche, des messages du noyau relatifs à l'amorçage.



Lorsque le bureau de PI OS apparaît, ouvrez le terminal et tapez :



```bash
uname -a
```


Cette commande vous indiquera la version du noyau actuellement utilisée à l'écran, ainsi que d'autres informations.



![img](assets/it/26.webp)



Vous pouvez également obtenir des informations sur le processeur et le matériel en tapant :



```bash
lscpu
```



![img](assets/it/27.webp)



Voir aussi `proc/mem/info`.



![img](assets/it/28.webp)



Pour connaître la version de Debian et le nom de code de la version :



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Utilisation


Bien que les performances semblent limitées (sur le papier et par rapport à la puissance des machines d'aujourd'hui), la PI Zero est performante, surtout en tant que terminal.





- Tout d'abord, vous pouvez aller dans les menus principaux et vous inspirer du panneau _Add/Remove software_, où vous trouverez un certain nombre d'utilitaires à programmer et à pratiquer. Rappelez-vous que vous pouvez aussi le faire à partir du terminal, mais toujours avec les privilèges `root`.



![img](assets/it/33.webp)





- Vous pouvez "adopter" ce dispositif hors ligne pour stocker divers documents confidentiels, qui resteront accessibles en cas de besoin, sans jamais être exposés à l'internet.
- Vous pouvez utiliser cette configuration pour sécuriser vos clés GPG en generate.
- Tu pourrais même exploiter ce nouveau « petit jouet » comme dispositif de signature airgap, [en suivant les conseils d’Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Parmi les portefeuilles que je connais, le seul qui propose une version 32 bits est Electrum. Eh bien : le Zero IP tel que nous l'avons préparé dans ce tutoriel vous permettrait de conserver les clés privées en dehors de la configuration du Wallet airgap que nous avons couverte dans ce tutoriel :



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Conclusions


La configuration a probablement une grande faiblesse : le micro SD est un support qui peut poser des problèmes. Il est vulnérable à une utilisation intensive ; vous en avez peut-être déjà fait l'expérience en l'utilisant avec votre téléphone. Après avoir installé tous les logiciels que vous voudrez utiliser sur le Zero airgap IP, faites une bonne sauvegarde du précieux micro SD, en utilisant l'outil Raspi OS dont vous disposez.



![img](assets/it/34.webp)



Au fur et à mesure de l'évolution de vos besoins, et donc de vos possibilités budgétaires, vous pourrez explorer d'autres Raspberry ou des solutions similaires. En parlant de mémoire, par exemple, le PI 5 offre la possibilité d'assembler un disque NVME M2, qui est certainement plus robuste que le microSD.



N'oubliez pas de prendre des notes et de documenter chaque étape de l'installation du logiciel utilitaire que vous êtes sur le point d'utiliser hors ligne. **Tôt ou tard, une mise à jour du système d'exploitation Raspi sortira** et vous voudrez certainement en profiter. À ce moment-là, vous devrez tout effacer et tout recommencer (peut-être avec une nouvelle micro SD 😂).



L'exercice que nous venons de faire, en supposant qu'il s'agisse de votre première expérience, vous en garderez un souvenir impérissable. Il n'est pas toujours possible de consacrer du matériel à des opérations "intégrées" hors ligne, sans pour autant négliger l'attention à porter à une machine en mode "airgapped" à allumer et à vérifier de temps à autre.



Mais vous y êtes arrivé, félicitations ! Et vous pourrez proposer cette solution à tous ceux qui ont besoin de limiter leur budget.