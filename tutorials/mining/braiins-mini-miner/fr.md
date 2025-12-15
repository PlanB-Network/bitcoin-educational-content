---
name: Braiins Mini Miner
description: Rendre le minage facile depuis chez soi.
---
![cover](assets/cover.webp)

## Introduction

Le Mini Miner braiins BMM 100 est un produit créé par le pool de minage Braiins. Cet appareil possède un design attrayant et est extrêmement silencieux. Il produit 1,1 Th/s de puissance de calcul et consomme environ 40 watts. Contrairement à d’autres appareils, il n’est pas open source, et son installation est vraiment simple, elle ne nécessite que quelques clics ! Le Mini Miner BMM 100 est la première version sortie. La version 2, appelée BMM 101, est maintenant en production, qui se distingue de la première par un écran plus grand et une connectivité Wi-Fi, mais les procédures d’installation restent les mêmes que la première version.

Vous pouvez également trouver beaucoup plus d’informations importantes en consultant le guide complet directement sur le [site du fabricant](https://braiins.com/hardware/mini-Miner-bmm-100).

## Vue d’ensemble du BMM 100

L’appareil ressemble à un parallélépipède avec un écran en façade.

![image](assets/en/01.webp)

Un ventilateur se trouve sur la face avant supérieure.

![image](assets/en/02.webp)

À l’arrière, on trouve : l’entrée d’alimentation, un emplacement pour carte SD (qui peut être nécessaire pour certaines mises à jour), un petit bouton marqué `IP REPORT` qui permet d’afficher l’adresse IP du Mini Miner, laquelle est indispensable pour accéder au tableau de bord de l’appareil. Une fois le bouton pressé, l’adresse IP s’affiche pendant environ 5 secondes, puis disparaît et l’écran par défaut réapparaît. Toutefois, si vous devez modifier certains paramètres, il suffit d’appuyer de nouveau sur ce bouton et l’adresse IP réapparaîtra à l’écran. En poursuivant la liste, on trouve un port Ethernet et un accès pour réinitialiser l’appareil. Pour cela, il faut utiliser une épingle et maintenir le bouton enfoncé pendant 10 secondes afin de réinitialiser tous les paramètres du Mini Miner. Enfin, il y a deux voyants lumineux, un vert et un rouge, qui indiquent l’état du mineur.

![image](assets/en/03.webp)

## Connexion du Mini Miner

Vous devrez connecter l’appareil à Internet via un câble Ethernet, notez que dans la nouvelle version (BMM 101) cela n’est plus nécessaire. Pour ce Mini Miner, une fois son emplacement choisi, il faut d’abord le relier à la ligne Internet puis à l’alimentation : l’appareil s’allume automatiquement et affiche son adresse IP à l’écran.

## Configuration

Nous devons ouvrir un navigateur et entrer l’adresse IP affichée par le Mini Miner dans la barre de recherche. Je vous rappelle que, pour trouver l’appareil sur le réseau, vous devrez être à proximité, c'est-à-dire que l'ordinateur que vous utilisez devra être connecté au même réseau que le mini Miner. Une fois l’adresse IP saisie et validée par Entrée, la page de connexion au système d’exploitation du Mini Miner, Braiins OS, apparaît à l’écran.

![image](assets/en/06.webp)

Pour vous connecter, vous devez entrer `root` comme nom d’utilisateur, tandis que le mot de passe peut rester vide. Cliquez sur login et le tableau de bord de votre Mini Miner apparaîtra.

![image](assets/en/07.webp)

## Paramètres généraux

Allons dans System.

![image](assets/en/24.webp)

Dans les paramètres, on trouve des options générales comme le thème (clair ou sombre), la langue, le fuseau horaire et le changement de mot de passe.

![image](assets/en/25.webp)

Si nous allons dans "Mini Miner Screen", nous trouvons les paramètres de notre Mini Miner, tels que l’affichage de l’écran. Nous pouvons choisir d’afficher l’heure, le prix du Bitcoin ou l’écran avec les informations d’état de la machine comme le hashrate, la température, la consommation en watts, etc. C’est à vous de choisir ce que vous souhaitez voir à l’écran. Nous pouvons également modifier la luminosité de l’écran, activer le mode nuit et afficher l’heure au format 12 heures ou 24 heures.

![image](assets/en/26.webp)

Une fois les modifications effectuées, cliquez sur `Save Changes` et vous verrez les changements sur l’écran de votre appareil.

![image](assets/en/27.webp)

## Connexion à un pool de minage

Nous ne sommes pas encore opérationnels, car il faut connecter l’appareil à un pool pour commencer à miner. Rendez-vous donc dans "Configuration".

![image](assets/en/08.webp)

La première entrée est `Pools`.

![image](assets/en/09.webp)

Ici, il faudra décider quel pool utiliser. Dans ce tutoriel, je vais vous en montrer deux options. La première est de se connecter au pool Braiins, utilisé également par des mineurs professionnels, comme vous pouvez le voir dans ce tutoriel :

https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

La deuxième option est de se connecter à un pool en solo, comme Public Pool. Suivez ce guide pour le faire :

https://planb.academy/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins pool

Pour se connecter à ce pool, nous devons créer un compte. Ce pool effectue également des paiements via Lightning Network, ce qui nous permettra de recevoir quelques sats par jour. Pour cela, nous devons configurer une adresse Lightning sur laquelle recevoir les récompenses. Si vous ne savez pas comment créer un compte sur Braiins Pool ou configurer votre adresse Lightning, vous pouvez suivre ce guide :

https://planb.academy/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Une fois cela fait, nous sommes dans le tableau de bord du pool Braiins. Ce que nous devons faire, c’est indiquer au pool que nous voulons connecter l’un de nos mineurs. Sur le côté gauche de l’écran, vous trouverez plusieurs entrées. Nous devons aller dans "workers".

![image](assets/en/04.webp)

Puis nous devons cliquer sur le bouton violet à droite qui dit "Connect workers".

![image](assets/en/05.webp)

Une fenêtre apparaît avec les informations nécessaires pour connecter notre Mini Miner au pool. Ici, le seul changement que nous pouvons effectuer est de choisir Stratum V2. Pour savoir ce qu’est Stratum v2, consultez cette entrée dans le [glossaire](https://planb.academy/en/resources/glossary/stratum-v2).

![image](assets/en/10.webp)

Nous devons maintenant copier cette chaîne qui commence par stratumv2. Cliquez sur le petit symbole "copier", puis retournez sur le tableau de bord de notre Mini Miner dans la section configuration et pools. Cliquez sur "add new pool".

![image](assets/en/11.webp)

Collez la chaîne copiée dans le champ Pool URL.

![image](assets/en/12.webp)

Nous devons maintenant ajouter un nom d’utilisateur et un mot de passe. Retournons sur le tableau de bord du pool. En dessous, nous avons également un userID et un mot de passe. Le userID correspond à notre nom d’utilisateur, celui que nous avons donné lors de la création du compte, plus le nom du mineur que nous voulons ajouter. Vous pouvez décider de donner ou non un nom à l’appareil que vous connectez au pool, c’est optionnel, mais conseillé : si vous connectez plusieurs appareils, il sera plus facile de les identifier. Si vous ne voulez rien indiquer, vous pouvez laisser `workerName`.

![image](assets/en/13.webp)

Nous allons ensuite sur notre Mini Miner et entrons le nom d’utilisateur. Ici, je vais entrer dans mon cas "finalstepbitcoin", qui est mon userID, suivi d’un point et du nom miniminer. C’est le nom que j’ai décidé de donner à l’appareil. Si vous ne voulez pas le nommer, écrivez simplement userid.workername. Dans mon cas, ce serait finalstepbitcoin.workername. Une fois le nom d’utilisateur saisi, vous pouvez choisir un mot de passe et l’écrire dans le champ vide. Vous pouvez aussi mettre `anithing123`, qui est celui affiché à l’écran du pool, mais cela signifie simplement que vous pouvez choisir n’importe quel mot de passe.

Une fois toutes les données saisies, il faut cliquer sur le bouton de sauvegarde à droite (en forme de disquette). Ainsi, les données du pool sont configurées dans le Mini Miner.

![image](assets/en/14.webp)

Ensuite, vous devez retourner sur le tableau de bord du pool et cliquer sur "Connected! Go back."

![image](assets/en/15.webp)

Nous avons connecté notre Mini Miner au pool Braiins ! Vous pouvez maintenant le voir dans la liste des workers. S’il n’apparaît pas, actualisez la page et attendez quelques instants. Une fois affiché, vérifiez que son statut est "OK" avec une coche verte.

![image](assets/en/17.webp)

Si vous retournez sur le tableau de bord, vous devriez commencer à voir du mouvement sur le graphique et voir le hashrate de notre appareil. Cela signifie que le pool reçoit notre travail et que nous sommes bel et bien en train de miner.

![image](assets/en/16.webp)

### Public Pool

Avec ce pool, on peut tenter sa chance et miner en solo, en s’appuyant sur un pool. Dans ce cas, nous ne recevrons pas de récompenses régulières, mais nous recevrons la récompense complète si nous réussissons à miner un bloc. Nous allons donc nous connecter à Public Pool, un pool de minage entièrement open source. Ouvrons une nouvelle fenêtre dans le navigateur et allons sur [web.public-pool.io](https://web.public-pool.io/#/).

![image](assets/en/18.webp)

On trouve ensuite une page contenant toutes les informations nécessaires. On y copie ensuite l’adresse stratum.
![image](assets/en/19.webp)

Ensuite, nous retournons sur le tableau de bord de notre Mini Miner, allons dans configuration → pools, cliquons sur "add new pool" (même processus que vu précédemment) et collons l’adresse stratum dans le champ Pool URL.

![image](assets/en/20.webp)

Revenons maintenant à la page du pool et remarquons que, comme nom d’utilisateur, nous devons entrer une adresse Bitcoin, qui sera celle sur laquelle nous recevrons la récompense au cas où nous parvenons à miner un bloc, puis un point et ensuite le nom de notre appareil, comme nous l’avons fait précédemment avec le pool Braiins. Le mot de passe peut être choisi librement.

![image](assets/en/21.webp)

Nous retournons sur le Mini Miner et dans le champ nom d’utilisateur nous collons une adresse Bitcoin suivie d’un point et du nom ; je vais mettre `miniminer`. Dans le champ mot de passe, je vais mettre test, vous pouvez entrer ce que vous voulez.

![image](assets/en/22.webp)

Nous enregistrons maintenant les paramètres et désactivons le pool Braiins.

![image](assets/en/23.webp)

Parfait ! Nous minons maintenant sur Public Pool !

![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)
