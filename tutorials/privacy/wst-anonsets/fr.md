---
name: Whirlpool Stats Tools - Anonsets
description: Comprendre le concept d'anonset et savoir le calculer avec WST
---
![cover](assets/cover.jpeg)

*"Break the link your coins leave behind"*

Dans ce tutoriel, nous allons étudier le concept d'anonsets, des indicateurs qui permettent d'estimer la qualité d'un processus de coinjoins sur Whirlpool. Nous abordons la méthode de calcul et d'interprétation de ces indicateurs. Suite à la partie théorique, nous passerons à la pratique en apprenant à calculer les anonsets d'une transaction spécifique à l'aide de l'outil Python *Whirlpool Stats Tools* (WST).

## Qu'est-ce qu'un coinjoin sur Bitcoin ?
**Le coinjoin est une technique qui permet de casser le traçage des bitcoins sur la blockchain**. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction coinjoin.

Les transactions coinjoin renforcent la confidentialité des utilisateurs de Bitcoin en complexifiant l'analyse de chaîne pour les observateurs externes. Leur structure permet de fusionner plusieurs pièces de différents utilisateurs en une unique transaction, brouillant ainsi les pistes et rendant difficile la détermination des liens entre les adresses d'entrée et de sortie.

Le principe du coinjoin repose sur une approche collaborative : plusieurs utilisateurs qui souhaitent mélanger leurs bitcoins déposent des montants identiques en entrées d'une même transaction. Ces montants sont ensuite redistribués en sorties de valeur équivalente. À l'issue de la transaction, il devient impossible d'associer un output spécifique à un utilisateur donné. Aucun lien direct n'existe entre les entrées et les sorties, rompant ainsi l'association entre les utilisateurs et leurs UTXO, de même que l'historique de chaque pièce.
![coinjoin](assets/1.webp)

Exemple d'une transaction coinjoin :
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Afin de réaliser un coinjoin tout en garantissant que chaque utilisateur conserve le contrôle sur ses fonds à tout moment, le processus débute par la construction de la transaction par un coordinateur, qui la transmet ensuite à chaque participant. Chaque utilisateur procède alors à la signature de la transaction après avoir vérifié que celle-ci lui convient. Toutes les signatures collectées sont finalement intégrées à la transaction. Si une tentative de détournement des fonds est effectuée par un utilisateur ou le coordinateur, par le biais d'une modification des outputs de la transaction coinjoin, les signatures se révéleront invalides, ce qui conduira au rejet de la transaction par les nœuds.

Il existe plusieurs implémentations de coinjoin, telles que Whirlpool, JoinMarket ou Wabisabi, chacune ayant pour objectif de gérer la coordination entre les participants et d'accroître l'efficacité des transactions coinjoin.

Dans ce tutoriel, nous nous pencherons sur mon implémentation préférée : Whirlpool, qui est disponible sur Samourai Wallet et Sparrow Wallet. C'est selon moi l'implémentation la plus efficace pour les coinjoins sur Bitcoin.

## Quelle est l'utilité du coinjoin sur Bitcoin ?
L'utilité du coinjoin réside dans sa capacité à produire du déni plausible, en noyant votre pièce au sein d'un groupe de pièces indifférenciables. Le but recherché par cette action est de briser les liens de traçabilité, tant du passé vers le présent que du présent vers le passé. 

Autrement dit, un analyste connaissant votre transaction initiale à l'entrée des cycles de coinjoins ne devrait pas être en mesure d'identifier avec certitude votre UTXO à la sortie des cycles de remix (analyse entrée de cycles vers sortie de cycles).
![coinjoin](assets/2.webp)
Inversement, il faut qu'un analyste connaissant votre UTXO à la sortie des cycles de coinjoin se trouve dans l'incapacité de déterminer la transaction originelle à l'entrée des cycles (analyse sortie de cycles vers entrée de cycles).
![coinjoin](assets/3.webp)
Pour évaluer la difficulté pour un analyste de lier le passé au présent et vice-versa, il faut quantifier la taille des groupes au sein desquels votre pièce est dissimulée. Cette mesure nous indique le nombre d'analyses possédant une probabilité identique. Ainsi, si l'analyse correcte est noyée parmi 3 autres analyses de probabilité égale, votre niveau de dissimulation est très faible. En revanche, si l'analyse correcte se trouve au sein d'un ensemble de 20 000 analyses toutes aussi probables les unes que les autres, votre pièce est très bien cachée.

Et justement, la taille de ces groupes représente des indicateurs que l'on appelle les "anonsets".

## Comprendre les anonsets
Les anonsets servent d'indicateurs pour évaluer le degré de confidentialité d'un UTXO particulier. Plus spécifiquement, ils mesurent le nombre d'UTXO indistinguables au sein de l'ensemble qui inclut la pièce étudiée. L'exigence d'un ensemble d'UTXO homogènes fait que les anonsets sont habituellement calculés sur des cycles de coinjoins. L'utilisation de ces indicateurs est particulièrement pertinente pour les coinjoins Whirlpool en raison de leur uniformité.

Les anonsets permettent, le cas échéant, de juger de la qualité des coinjoins. Un anonset de grande taille signifie un niveau d'anonymat accru, car il devient difficile de distinguer un UTXO spécifique au sein de l'ensemble. 

Deux types d'anonsets existent :
- **L'ensemble d'anonymat prospectif ;**
- **L'ensemble d'anonymat rétrospectif.** 

Le premier indique la taille du groupe parmi lequel se cache l'UTXO étudié en sortie de cycle, sachant l'UTXO en entrée, c'est-à-dire le nombre de pièces indifférenciables présentes au sein de ce groupe. Cet indicateur permet de mesurer la résistance de la confidentialité de la pièce face à une analyse passé vers présent (entrée vers sortie). En anglais, le nom de cet indicateur est « *forward anonset* », ou « *forward-looking metrics* ». 
![coinjoin](assets/4.webp)
Cette métrique permet d'estimer dans quelle mesure votre UTXO est protégé contre les tentatives de reconstitution de son historique depuis son point d'entrée jusqu'à son point de sortie dans le processus de coinjoin. 

Par exemple, si votre transaction a participé à son premier cycle de coinjoin et que deux autres cycles descendants ont été réalisés, l'anonset prospectif de votre pièce s'élèverait à `13` :
![coinjoin](assets/5.webp)
Le second indique le nombre de sources possibles pour une pièce donnée, sachant l'UTXO en sortie de cycle. Cet indicateur permet de mesurer la résistance de la confidentialité de la pièce face à une analyse présent vers passé (sortie vers entrée), c'est-à-dire à quel point il est difficile pour un analyste de remonter à l'origine de votre pièce, avant les cycles de coinjoins. En anglais, le nom de cet indicateur est « *backward anonset* », ou « *backward-looking metrics* ».
![coinjoin](assets/6.webp)
 En connaissant votre UTXO à la sortie des cycles, l'anonset rétrospectif détermine le nombre de transactions Tx0 potentielles qui auraient pu constituer votre entrée dans les cycles de coinjoins. Sur le schéma ci-dessous, cela correspond à l'addition de toutes les bulles orange.
 ![coinjoin](assets/7.webp)

## Calculer les anonsets avec Whirlpool Stats Tools (WST)
Pour calculer ces indicateurs sur vos propres pièces qui sont passées dans des cycles de coinjoin, vous pouvez utiliser un outil spécialement développé par Samourai Wallet : *Whirlpool Stats Tools*.

Si vous disposez d'un RoninDojo, WST est préinstallé sur votre nœud. Vous pouvez donc passer les étapes d'installation et suivre directement les étapes d'utilisation. Pour ceux qui ne disposent pas d'un nœud RoninDojo, voyons ensemble comment procéder à l'installation de cet outil sur un ordinateur.

Vous aurez besoin de : Tor Browser (ou Tor), Python 3.4.4 ou supérieur, git et pip. Ouvrez un terminal. Afin de vérifier la présence et la version de ces logiciels sur votre système, saisissez les commandes suivantes :
```bash
python --version
git --version
pip --version
```

Si besoin, vous pouvez les télécharger depuis leurs sites web respectifs :
- https://www.python.org/downloads/ (pip vient directement avec Python depuis la version 3.4) ;
- https://www.torproject.org/download/ ;
- https://git-scm.com/downloads.

Une fois tous ces logiciels installés, depuis un terminal, clonez le dépôt de WST :
```bash
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```
![WST](assets/8.webp)
Naviguez dans le répertoire de WST :
```bash
cd whirlpool_stats
```

Installez les dépendances :
```bash
pip3 install -r ./requirements.txt
```
![WST](assets/9.webp)
Vous pouvez éventuellement les installer manuellement (facultatif) :
```bash
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Naviguez dans le sous-dossier `/whirlpool_stats` :
```bash
cd whirlpool_stats
```

Démarrez WST :
```bash
python3 wst.py
```
![WST](assets/10.webp)
Lancez Tor ou Tor Browser en fond.

**-> Pour les utilisateurs RoninDojo, vous pouvez reprendre le tutoriel directement ici.**

Définissez le proxy sur Tor (RoninDojo),
```bash
socks5 127.0.0.1:9050
```

ou bien sur Tor Browser en fonction de ce que vous utilisez :
```bash
socks5 127.0.0.1:9150
```

Cette manipulation vous permettra de télécharger les données sur OXT via Tor, afin de ne pas faire fuiter des informations sur vos transactions. Si vous êtes novice et que cette étape vous semble complexe, sachez qu'il s'agit simplement de diriger votre trafic internet à travers Tor. La méthode la plus simple consiste à lancer le navigateur Tor Browser en arrière-plan sur votre ordinateur, puis à exécuter uniquement la seconde commande pour vous connecter via ce navigateur (`socks5 127.0.0.1:9150`).
![WST](assets/11.webp)
Ensuite, dirigez-vous sur le répertoire de travail depuis lequel vous avez l'intention de télécharger les données de WST à l'aide de la commande `workdir`. Ce dossier servira à stocker les données transactionnelles que vous allez récupérer depuis OXT sous forme de fichiers `.csv`. Ces informations sont essentielles au calcul des indicateurs que vous cherchez à obtenir. Vous êtes libre de choisir l'emplacement de ce répertoire. Il pourrait être judicieux de créer un dossier spécifiquement destiné aux données de WST. À titre d'exemple, optons pour le dossier de téléchargements. Si vous utilisez RoninDojo, cette étape n'est pas nécessaire :
```bash
workdir chemin/vers/votre/répertoire
```

L'invite de commande devrait alors avoir changé pour indiquer votre répertoire de travail.
![WST](assets/12.webp)
Téléchargez ensuite les données de la pool qui contient votre transaction. Par exemple, si je suis dans la pool de `100 000 sats`, la commande est :
```bash
download 0001
```
![WST](assets/13.webp)
Les codes de dénominations sont les suivants sur WST :
- Pool 0,5 bitcoins : `05`
- Pool 0,05 bitcoins : `005`
- Pool 0,01 bitcoins : `001`
- Pool 0,001 bitcoins : `0001`

Une fois les données téléchargées, chargez-les. Par exemple, si je suis dans la pool de `100 000 sats`, la commande est :
```bash
load 0001
```

Cette étape prend quelques minutes en fonction de votre ordinateur. C'est le moment de vous faire un café ! :)
![WST](assets/14.webp)
Après avoir chargé les données, tapez la commande `score` suivie de votre TXID (identifiant de transaction) pour obtenir ses anonsets :
```bash
score TXID
```

**Attention**, le choix du TXID à utiliser varie en fonction de l'anonset que vous désirez calculer. Pour évaluer l'anonset prospectif d'une pièce, il est nécessaire d'entrer, via la commande `score`, le TXID correspondant à son premier coinjoin, soit le mix initial effectué avec cet UTXO. En revanche, pour déterminer l'anonset rétrospectif, vous devrez saisir le TXID du dernier coinjoin réalisé. Pour résumer, l'anonset prospectif est calculé à partir du TXID du premier mix, tandis que l'anonset rétrospectif est calculé à partir du TXID du dernier mix.

WST vous affiche alors le score rétrospectif (*Backward-looking metrics*) puis le score prospectif (*Forward-looking metrics*). Pour l'exemple, j'ai pris le TXID d'une pièce au hasard sur Whirlpool qui ne m'appartient pas.
![WST](assets/15.webp)
La transaction en question : [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)

Si l'on considère cette transaction comme le premier coinjoin effectué pour la pièce concernée, alors elle bénéficie d'un anonset prospectif de `86 871`. Cela signifie qu'elle se dissimule parmi `86 871` pièces indiscernables. Pour un observateur externe connaissant cette pièce au début des cycles de coinjoin et tentant de retracer sa sortie, il sera confronté à `86 871` UTXO possibles, chacun ayant une probabilité identique d'être la pièce recherchée.

Si l'on considère cette transaction comme le dernier coinjoin de la pièce, elle dispose alors d'un anonset rétrospectif de `42 185`. Cela signifie qu'il existe `42 185` sources potentielles pour cet UTXO. Si un observateur externe identifie cette pièce à la fin des cycles et cherche à en retrouver l'origine, il se trouvera face à `42 185` sources possibles, toutes avec une probabilité égale d'être l'origine recherchée.

Outre les scores des anonsets, WST vous donne également le taux de diffusion de votre output dans la pool en fonction de l'anonset. Cet autre indicateur vous permet simplement de juger du potentiel d'amélioration de votre pièce. Ce taux est particulièrement utile pour l'anonset prospectif. En effet, si votre pièce a un taux de diffusion de 15 %, cela signifie qu'elle peut être confondue avec 15 % des pièces de la pool. C'est bien, mais vous avez encore une très large marge d'amélioration en continuant de remixer. En revanche, si votre pièce dispose d'un taux de diffusion de 95 %, alors vous êtes en train d'approcher des limites de la pool. Vous pouvez continuer de remixer, mais votre anonset ne va pas beaucoup augmenter.

Il est important de noter que les anonsets calculés par WST ne sont pas d'une exactitude parfaite. Le volume de données à traiter étant énorme, WST utilise l'algorithme *HyperLogLogPlusPlus* pour réduire considérablement la charge liée au traitement des données en local et la mémoire nécessaire. C'est un algorithme qui permet d'estimer le nombre de valeurs distinctes dans de très grands ensembles de données tout en conservant une grande précision dans le résultat. Les scores fournis en résultat sont donc suffisamment bons pour être utilisés dans vos analyses, car ce sont des estimations très proches de la réalité, mais ils ne doivent pas être interprétés comme des valeurs exactes à l'unité près.

Pour conclure, gardez à l'esprit qu'il n'est pas impératif de calculer systématiquement les anonsets pour chacune de vos pièces en coinjoins. La conception même de Whirlpool vous apporte déjà des garanties. En effet, l'anonset rétrospectif constitue rarement un sujet de préoccupation. Dès votre mix initial, vous obtenez un score rétrospectif particulièrement élevé grâce à l'héritage des mix précédents depuis le coinjoin Genesis. Concernant l'anonset prospectif, il suffit de conserver votre pièce dans le compte post-mix pendant une durée suffisamment importante.

C'est la raison pour laquelle je considère l'utilisation de Whirlpool comme particulièrement pertinente dans une stratégie *Hodl -> Mix -> Spend -> Replace*. À mon avis, la démarche la plus logique consiste à conserver l'essentiel de son épargne en bitcoins dans un cold wallet, tout en maintenant en permanence un certain nombre de pièces en coinjoins sur Samourai pour pouvoir couvrir les dépenses quotidiennes. Une fois les bitcoins issus des coinjoins dépensés, ils sont remplacés par de nouveaux, afin de revenir au seuil de pièces en mix que l'on a défini. Cette méthode permet de se libérer de la préoccupation des anonsets de nos UTXO, tout en rendant le délai nécessaire à l'efficacité des coinjoins bien moins contraignant.

**Ressources externes :** 

- [Podcast en Francąis sur l'analyse de chaîne](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Article wikipedia sur HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- [Repo de Samourai pour Whirlpool Stats](https://code.samourai.io/whirlpool/whirlpool_stats)
- [Website de Whirlpool par Samourai](https://samouraiwallet.com/whirlpool)
- [Article Medium en Anglais sur la vie privée et Bitcoin par Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Article Medium en Anglais sur le concept d'anonymity set par Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)
