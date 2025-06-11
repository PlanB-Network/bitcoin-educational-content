---
name: Canaan Avalon Mini 3
description: Configurer son ASIC Avalon pour solominer ou miner en pool
---

![cover](assets/cover.webp)

Dans ce tutoriel, nous allons passer en revue la mise en place du Avalon Mini 3 de la marque Canaan, permettant de facilement miner à la maison.

Jusque-là les machines ASIC (*Application Specific Integrated Circuit*) spécifiquement conçues pour effectuer une tâche donnée, en l'occurrence le calcul de hashs (SHA-256) pour miner du bitcoin, étaient particulièrement inadaptées à un usage domestique. Les nuisances en termes de bruit, de chaleur générée à évacuer, voir la nécessité d'adapter son installation électrique pour supporter l'énorme puissance de ces appareils empêchaient la plupart d'entre nous de participer.

Aujourd'hui Canaan, un des principaux fabricants de machines ASIC décide de s'attaquer au marché des particuliers qui veulent miner chez eux, en proposant une gamme de produits relativement silencieux et très simple à installer (plug & play).

Ces appareils sont marketés comme étant pour l'un un chauffage d'appoint en ce qui concerne le **Avalon Nano 3S (140W)**, ou carrément comme un mini radiateur d'une puissance de **800W** pour le **Avalon Mini 3**.

https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Attention, la différence de prix avec des chauffages traditionnels de puissance équivalente ne permet pas, dans la grande majorité des cas, d'être gagnant financièrement. Les satoshis générés par l'activité de mining ne compenseront jamais cet écart de prix, à moins d'avoir accès à de l'électricité gratuite (surplus), ou très bon marché.

Selon moi il faut davantage voir ces appareils comme une manière simple de miner à la maison pour ceux qui le désirent pour des raisons personnelles : *obtenir des sats non KYC / jouer à la "loterie" en solominant / participer à la décentralisation du hashrate etc..*., tout en bénéficiant **en bonus** de la chaleur générée pour chauffer sa pièce en hiver. Mais pas comme un moyen de faire des économies dans la plupart des cas du moins (pays occidentaux).

## Unboxing et Caractéristiques 

### Avalon Nano 3S

Dans un 1er temps voyons voir ce qu'il se cache à l'intérieur de la boite du Avalon Mini 3.

![image](assets/fr/24.webp)

En ouvrant la boite le mode d'emploi est directement présenté à votre vue, mais plus important le module de réception WIFI est dissimulé sous l'autocollant blanc et rond situé à gauche du mode d'emploi. Vous en aurez besoin par la suite.

![image](assets/fr/25.webp)

En dessous du bloc de mousse se trouve l'appareil, puis une fois retiré de la boite, le bloc d'alimentation.

![image](assets/fr/26.webp)


![image](assets/fr/27.webp)

## Mise sous tension et connexion au réseau local

Une fois déballé, placez votre Avalon Mini 3 si possible à un endroit relativement dégagé pour permettre une bonne circulation de la chaleur. Ensuite commencez par insérer le petit module de réception WIFI dans le port USB situé en dessous de l'appareil, branchez l'alimentation électrique et veillez à ce que le bouton de mise sous tension soit bien en position "1".

![image](assets/fr/28.webp)

Une fois ces étapes réalisées, l'écran LED de l'appareil s'allume et affiche le symbole "Bluetooth", signe qu'il est prêt à être connecté à votre réseau local grâce à l'application Avalon Family.

![image](assets/fr/29.webp)

![image](assets/fr/30.webp)

Pour ce faire, rendez vous dans votre store d'application mobile, recherchez puis téléchargez l'application **Avalon Family**.

![image](assets/fr/11.webp)
Une fois installée ouvrez-la, cliquez sur "Skip" en haut à droite, puis sur le bouton "Add" et enfin sur "Search". Veillez à avoir le Bluetooth activé sur votre smartphone, afin que la détection de l'appareil se fasse sans problème.

![image](assets/fr/12.webp)
Une fois l'appareil détecté par l'application cliquez sur celui-ci, et choisissez "Connect". Vous arrivez enfin sur l'écran vous permettant de rentrer vos identifiants de connexion WIFI.
![image](assets/fr/13.webp)
Une fois l'appareil connecté à votre réseau local, votre Mini 3 fera défiler sur son écran les informations telles que son adresse IP, l'heure, le hashrate et la puissance électrique.

Ci-dessous un tableau récapitulatif des spécifications techniques générales du Mini 3:

| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Connexion  à une pool de minage

**Cette partie est commune aux appareils Nano 3s et Mini 3, car les procédés sont strictement identiques.**

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

Dans le menu principal de l'application Avalon family, cliquez sur l'icone correspondant au Avalon Mini 3. Vous serez directement dirigés vers le menu permettant de gérer les modes de fonctionnement.

3 possibilités s'offrent à vous:  le mode "Heater", le mode "Mining" ou le mode "Night".

- En mode "Heater" vous disposez de 2 niveaux de puissance "Eco" ou "Super".
  Le niveau "Eco" correspond à une puissance de chauffage de 500W pour un hashrate d'environ 25 Th/s et 40 dB en ce qui concerne le niveau sonore. 
  Le niveau "Super" quant à lui, correspond à une puissance de sortie de 650 W pour environ  30Th/s et 45 dB. Ce mode permet de régler une température ambiante maximale au-delà de laquelle l'appareil cessera de fonctionner.

![image](assets/fr/36.webp)
- En mode "Mining", l'appareil fonctionne au régime maximal, sans possibilité de régler une température cible (en dehors de la limite intégrée à l'appareil en cas de surchauffe bien évidemment). Il s'agit de tirer parti au maximum des performances du miner. Ici la puissance de sortie approche les 800 W pour environ 37.5 Th/s et 50-55 dB de niveau sonore.

![image](assets/fr/37.webp)
Enfin en mode "Night", votre Mini 3 fonctionne à son régime minimal avec un minimum de bruit. 400 W,  20 Th/s et 33 dB environ.

Là aussi vous pouvez définir une température cible au-delà de laquelle l'appareil passe en mode inactif et arrête de miner. Si la température baisse, l'appareil redémarre et recommence à chauffer et miner. Dans ce mode, les LED de l'écran sont éteintes par défaut mais vous pouvez décider de les allumer si besoin pour éclairer la pièce dans la pénombre, comme une veilleuse (voir photo ci-dessous).

![image](assets/fr/38.webp)

![image](assets/fr/39.webp)

Pour finir, vous pouvez là encore vous amuser à jouer avec les LED de votre Avalon via le menu "Display". Vous pourrez au choix faire défiler les informations pertinentes utiles au bon fonctionnement, choisir d'afficher l'heure, ou carrément une image custom (pixélisée).

![image](assets/fr/40.webp)

![image](assets/fr/41.webp)

Le menu "Settings", quant à lui, permet comme dans le cas du Avalon Nano 3S de changer le mot de passe administrateur, les paramètres de pool, de consulter l'obstruction du filtre (situé en dessous de l'appareil), de contacter le support, ou les logs de l'appareil.

![image](assets/fr/42.webp)

Là encore le filtre situé en partie basse de l'appareil peut être nettoyé à l'aide d'un aspirateur, le plus régulièrement possible étant le mieux bien évidemment.

Nous voilà arrivés au bout de ce tuto qui nous aura appris comment connecter notre appareil Avalon Mini 3 à notre réseau local, comment pointer son hashrate vers des pools de minage, et comment naviguer à travers les options et les réglages grâce à l'application Avalon Family.

Pour aller plus loin, vous pouvez consulter notre tutoriel consacré à la version plus petite des Avalon : le Nano 3S.

https://planb.network/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6
