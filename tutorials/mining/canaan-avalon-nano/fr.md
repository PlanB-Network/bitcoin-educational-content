---
name: Canaan Avalon Nano 3S
description: Configurer son ASIC Avalon pour solominer ou miner en pool
---

![cover](assets/cover.webp)

Dans ce tutoriel, nous allons passer en revue la mise en place du Avalon Nano 3S de la marque Canaan, permettant de facilement miner à la maison.

Jusque-là les machines ASIC (*Application Specific Integrated Circuit*) spécifiquement conçues pour effectuer une tâche donnée, en l'occurrence le calcul de hashs (SHA-256) pour miner du bitcoin, étaient particulièrement inadaptées à un usage domestique. Les nuisances en termes de bruit, de chaleur générée à évacuer, voir la nécessité d'adapter son installation électrique pour supporter l'énorme puissance de ces appareils empêchaient la plupart d'entre nous de participer.

Aujourd'hui Canaan, un des principaux fabricants de machines ASIC décide de s'attaquer au marché des particuliers qui veulent miner chez eux, en proposant une gamme de produits relativement silencieux et très simple à installer (plug & play).

Ces appareils sont marketés comme étant pour l'un un chauffage d'appoint en ce qui concerne le **Avalon Nano 3S (140W)**, ou carrément comme un mini radiateur d'une puissance de **800W** pour le **Avalon Mini 3**.

https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Attention, la différence de prix avec des chauffages traditionnels de puissance équivalente ne permet pas, dans la grande majorité des cas, d'être gagnant financièrement. Les satoshis générés par l'activité de mining ne compenseront jamais cet écart de prix, à moins d'avoir accès à de l'électricité gratuite (surplus), ou très bon marché.

Selon moi il faut davantage voir ces appareils comme une manière simple de miner à la maison pour ceux qui le désirent pour des raisons personnelles : *obtenir des sats non KYC / jouer à la "loterie" en solominant / participer à la décentralisation du hashrate etc..*., tout en bénéficiant **en bonus** de la chaleur générée pour chauffer sa pièce en hiver. Mais pas comme un moyen de faire des économies dans la plupart des cas du moins (pays occidentaux).

## Unboxing et Caractéristiques 

Dans un 1er temps voyons voir ce qu'il se cache à l'intérieur de la boite du Avalon Nano 3S.

![image](assets/fr/01.webp)


![image](assets/fr/02.webp)

Une fois la boite ouverte on y trouve une pochette cartonnée contenant un récepteur WIFI qu'il faudra comme on le verra par la suite, brancher sur le port USB de l'appareil pour que celui-ci soit en mesure de se connecter à votre réseau local. On y trouve également le manuel d'instruction ainsi qu'une tige métallique permettant de réinitialiser l'appareil aux paramètres d'usine si nécessaire.

![image](assets/fr/03.webp)


![image](assets/fr/04.webp)

Une fois tout sorti de la boite voilà ce qu'on a sous la main : la machine elle-même bien sûr, le manuel d'utilisation, le récepteur WIFI, la pointe métallique évoquée plus haut, et l'alimentation électrique de l'appareil. La carte bleue fournie n'est pas digne d'intérêt selon nous.

![image](assets/fr/05.webp)

Ci-dessous un tableau récapitulatif des spécifications techniques générales du Nano 3S :

| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Mise sous tension et connexion au réseau local

Une fois déballé, placez votre Avalon Nano 3 S si possible à un endroit relativement dégagé pour permettre une bonne circulation de la chaleur. Ensuite commencez par insérer le petit module de réception WIFI comme montré ci-dessous:

![image](assets/fr/06.webp)
Branchez alors la fiche USB-C de l'alimentation dans le port USB-C de l'appareil pour l'alimenter électriquement.

![image](assets/fr/07.webp)
![image](assets/fr/08.webp)

L'appareil va démarrer et le logo Avalon Nano s'affichera sur l'écran, suivi d'un logo de "téléphone portable" avec les mots "Veuillez configurer le réseau avec l'application Avalon Family", en anglais "Please Configure the Network With Avalon Family App".

![image](assets/fr/09.webp)


![image](assets/fr/10.webp)

Pour ce faire, rendez vous dans votre store d'application mobile, recherchez puis téléchargez l'application **Avalon Family**.

![image](assets/fr/11.webp)
Une fois installée ouvrez-la, cliquez sur "Skip" en haut à droite, puis sur le bouton "Add" et enfin sur "Search". Veillez à avoir le Bluetooth activé sur votre smartphone, afin que la détection de l'appareil se fasse sans problème.

![image](assets/fr/12.webp)
Une fois l'appareil détecté par l'application cliquez sur celui-ci, et choisissez "Connect". Vous arrivez enfin sur l'écran vous permettant de rentrer vos identifiants de connexion WIFI.
![image](assets/fr/13.webp)
Une fois l'appareil connecté à votre réseau local, l'écran de celui-ci ressemblera désormais à ça:

![image](assets/fr/14.webp)

On y voit un hashrate "fictif" car aucune pool n'a encore été configurée, l'heure, la date, la puissance et l'adresse IP de l'appareil, très utile si on veut avoir accès à l'interface de l'appareil via un PC et un navigateur (on verra cela plus loin).

![image](assets/fr/15.webp)


## Connexion  à une pool de minage

**Cette partie est commune aux appareils Nano 3s et Mini 3, car les procédés sont strictement identiques**.

Que l'on veuille "solominer" ou bien miner "en pool" il va nous falloir nous connecter à une pool de minage. En effet notre appareil n'est qu'un vulgaire "hasheur" qui n'a aucune conscience du réseau Bitcoin. Le connecter à une pool lui permet d'avoir accès au réseau bitcoin, et de recevoir des "template de blocs" sur lesquels travailler.

### Utilisation de l'application pour se connecter à une pool de minage

Sur l'application Avalon Family sélectionner l'appareil comme indiqué ci-dessous. Il vous sera alors automatiquement demandé de changer le mot de passe administrateur de la machine, cliquez sur "OK" si vous souhaitez le faire, ou sur cancel pour laisser le mot de passe d'accès par défaut "admin".
![image](assets/fr/16.webp)
Ensuite sélectionnez "Settings", puis "Pool Config" et entrez les paramètres pour les 3 pools demandées.
Les pools #2 et #3 serviront de backup dans le cas où les services de l'une d'elle venaient à faire défaut, pour éviter que votre mineur ne travaille pour rien. Par défaut le hashrate sera pointé vers la pool #1

Dans notre cas nous choisissons:
- 1 - Public Pool,
- 2 - CkPool,
- 3 - Ocean.

![image](assets/fr/17.webp)

Pour plus de détails sur la manière de se connecter à une pool de minage, veuillez vous référer à ces tutoriels :

https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

En synthèse il nous faut:

- l'adresse de la pool choisie généralement **stratum+tcp://xxxxxxxx:port**.

- le nom du "worker" composé de *votre adresse bitcoin* et du *pseudo* que vous choisissez pour votre appareil, les 2 étant séparés par un *point*, par exemple:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**

- la mot de passe qui est généralement toujours "**x**"

Une fois les informations de pool renseignées, cliquez sur "Save".

![image](assets/fr/18.webp)
Redémarrez l'appareil comme demandé, et patientez quelques minutes que votre hashrate soit pointé vers votre pool de prédilection (#1).

### Utilisation du navigateur pour se connecter à une pool de minage

Vous pouvez également réaliser ces opérations de connexion à une pool de minage et plus généralement, accéder à l'interface de gestion de votre appareil via votre navigateur préféré.

Pour ce faire, tapez dans la barre de recherche du navigateur l'adresse IP de l'appareil que l'on peut voir sur l'écran en bas, ici dans notre exemple **192.168.144.6**

![image](assets/fr/15.webp)

S'affichera alors la page suivante, vous demandant d'ouvrir l'application Avalon Family et de scanner le QR code affiché avec l'application.

![image](assets/fr/20.webp)

Ouvrez donc l'application, et cliquez sur les 3 tirets en haut à droite, puis sur scan. Scannez le QR code du navigateur puis tapez le mot de passe administrateur de l'application et cliquez sur OK.

![image](assets/fr/21.webp)

Vous voilà sur la page web vous permettant d'interagir avec votre Avalon. Il s'agit davantage d'un tableau de bord destiné à afficher les métriques de la machine, que d'un moyen de la paramétrer. 

Mais les réglages de pool sont accessibles néanmoins de cette façon en cliquant sur **"Pool Config"** en bas à droite.

![image](assets/fr/22.webp)

De la même manière qu'avec l'application mobile vous pouvez renseigner ici vos paramètres de pools.

![image](assets/fr/23.webp)

## Contrôler son appareil via l'application Avalon Family

Nous avons désormais connecté notre home miner à notre réseau local, puis pointé notre hashrate vers des pools de mining. Allons maintenant découvrir les fonctionnalités essentielles de notre machine à travers l'application Avalon Family.

Dans l'application Avalon family cliquez sur l'icone correspondant au Avalon Nano 3S.
3 menus vous sont ensuite proposés: "Work Mode", "Light control", et "Settings". Cliquez tout d'abord sur "Work Mode". Vous seront alors proposés 3 modes de puissance pour votre machine.

**Low** : vous apporte environ 3 Th/s de hashrate pour 70W de consommation électrique
**Medium**: vous apporte envrion 4.5 Th/s de hashrate pour 100W de consommation électrique
**High**: vous apportera environ 6 Th/s de hashrate à la consommation maximale de 140W

![image](assets/fr/31.webp)
Revenons un cran en arrière pour explorer le menu "Light Control". Il s'agit ici purement de cosmétique. Tout un tas d'options sont proposées pour faire varier la couleur, l'intensité, la chaleur, ou éteindre les leds de l'appareil pendant la nuit etc... Vous découvrirez tout cela par vous-même très facilement.

![image](assets/fr/32.webp)
![image](assets/fr/33.webp)

![image](assets/fr/34.webp)

Enfin le dernier menu mis à notre disposition est le menu "Settings" que nous avons déjà aperçu pour se connecter à nos pools de minage. Il permet donc de gérer ses pools, de changer le mot de passe administrateur de l'appareil, et d'observer différentes métriques telles que la date de fin de garantie, la propreté du filtre, ou la manière de contacter le support en cas de défaillance.

![image](assets/fr/35.webp)
Pour l'entretien et afin d'essayer de garder un filtre aussi propre possible il est recommandé d'utiliser un aspirateur et d'aspirer régulièrement au niveau des entrées et sorties d'air afin d'éviter l'encrassement.

Nous voilà arrivés au bout de ce tuto qui nous aura appris comment connecter notre appareil Avalon Nano 3 S à notre réseau local, comment pointer son hashrate vers des pools de minage, et comment naviguer à travers les options et les réglages grâce à l'application Avalon Family.

Pour aller plus loin, vous pouvez consulter notre tutoriel consacré à la version supérieure des Avalon : le Mini 3.

https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7
