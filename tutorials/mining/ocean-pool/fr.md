---
name: Ocean Mining

description: Présentation de Ocean Mining
---

![signup](assets/cover.webp)

**Mai 2024**

Ocean Mining est une pool de minage un peu particulière. Ici, pas de compte, pas d'adresse e-mail, pas de mot de passe. A l'image de Bitcoin tout est transparent, pseudonyme et les contributeurs peuvent choisir parmi quatre blocs templates différents.

### Système de rémunération

Le système de rémunération d'Ocean s'appelle TIDES, "Transparent Index of Distinct Extended Shares". Ce système enregistre le travail fourni par les mineurs, ce que l'on appelle les "shares". La pool calcule le pourcentage de "shares" de chaque contributeur, puis ajoute leur adresse Bitcoin dans le bloc template de la pool comme bénéficiaire de ce pourcentage de la récompense de bloc. 

Le bloc template est actualisé environ toutes les 10 secondes pour prendre en compte les nouvelles transactions les plus rémunératrices et pour changer la répartition de la récompense de bloc si nécessaire.

![signup](assets/rem.webp)

Que vos machines soient connectées ou non au moment ou la pool mine un nouveau bloc n'a pas d'importance. Le travail déjà envoyé est conservé pendant les huit prochains blocs trouvés par la pool.

Le fait de conserver le travail pendant huit blocs au lieu de remettre les compteurs à zéro à chaque nouveau bloc miné implique que votre rémunération sera à 100 % seulement une fois que la pool aura trouvé huit blocs après que vous ayez commencé à contribuer. Cela veut aussi dire que vous continuerez à être rémunéré pendant huit blocs si vous arrêtez de contribuer à la pool. 

Ce mécanisme permet à la fois de lisser la rémunération et de décourager le « pool hopping », qui consiste à changer de pool régulièrement en fonction de celle qui a le plus de probabilité de trouver le prochain bloc.

### Retraits

Le fonctionnement d'Ocean Mining permet à ses contributeurs de récupérer des bitcoins "blancs", c'est-à-dire des bitcoins qui sont directement émis par la récompence de bloc. 

Contrairement à la majorité des autres pools, Ocean ne reçoit pas les bitcoins nouvellement minés, les adresses des contributeurs sont directement intégrées dans le bloc template.

Pour le moment, le montant minimum pour réellement profiter des bitcoins blancs est de 1 048 576 sats. Il faut qu’à chaque bloc miné par la pool, votre part de « shares » vous donne droit à plus de 1 048 576 sats pour qu'ils vous soient directement payés par la récompense de bloc. 
Autrement, vos sats seront conservés par Ocean le temps que vos récompenses totales dépassent ce montant. 

Tous les bitcoins provisoirement conservés par Ocean sont sur cette adresse :  [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, tous est vérifiable sur la TimeChain.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Il est également possible de retirer ses sats en Lightning via BOLT12. Nous verrons comment le paramétrer.

### Frais de pool

Les frais sont de 0 % à 2 % selon le bloc template choisi.

## La transparence d’Ocean

### Données contributeurs

![signup](assets/1.webp)

Toutes les informations de la pool sont transparentes, y compris toutes les données utilisateurs. Pour comprendre ce point, nous allons prendre un exemple:

[Sur le dashboard d'Ocean](https://ocean.xyz/dashboard), vous avez de nombreuses informations comme le hashrate des six derniers mois, le nombre de participants à la pool, le nombre total de bitcoins minés, etc.

Nous allons nous intéresser à la partie "Contributors". Vous pouvez voir la liste de tous les contributeurs avec leur hashrate moyen sur les trois dernières heures ainsi que le pourcentage de **"shares"** et de **"hash"** par rapport au reste de la pool.

**« Shares % »** est le pourcentage de travail fourni par le contributeur dans la fenêtre des huit derniers blocs par rapport au reste de la pool.

**« Hash % »** est le pourcentage du hashrate moyen fourni par le contributeur sur les trois dernières heures par rapport au reste de la pool.

![signup](assets/2.webp)

Vous constaterez que les "Contributors" sont identifiés par une adresse Bitcoin. Vous pouvez cliquer sur l’une de ces adresses pour avoir plus de détails. 

Si nous prenons la première, celle qui a le hashrate le plus élevé 
[1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), vous pourrez voir tous les détails concernant cet utilisateur : hashrate, nombre de bitcoins minés, avec quel bloc, et même le détail de chacune de ses machines (ASICs). Cependant, il reste pseudonyme, comme sur Bitcoin.

### Bloc template

En haut à gauche sur le dashboard, vous avez « Next block ». Sur cette page, vous avez quatre blocs templates différents. Ocean permet à chaque contributeur de choisir le bloc template qu’il souhaite soutenir. Cela n’a pas d’impact direct sur votre rémunération. Quand la pool mine un bloc, tous les contributeurs sont rémunérés indépendamment du template qu’ils ont choisi. Cela permet simplement à chacun de « voter » pour le bloc template qui lui correspond.

![signup](assets/3.webp)

**CORE:** Frais 2 %, il s’agit du template classique Bitcoin Core sans filtre, comme écrit sur leur page « Inclut les transactions et la majorité du spam »

**CORE+ANTISPAM:** Frais 0 %, Bitcoin Core avec un filtre contre certaines transactions comme les Ordinals « Inclut les transactions et limite le spam »

**OCEAN:** Frais 0 %, Bitcoin Knot « Inclut seulement les transactions et les données raisonnablement petites »

**DATA-FREE:** Frais 0 %, Bitcoin Knot « Inclut seulement les transactions sans aucune donnée arbitraire »

### Distinction entre Bitcoin Core et Bitcoin Knot

Bitcoin Core est le logiciel qui permet de faire fonctionner environ 99 % des nœuds Bitcoin à travers le monde. Bitcoin est un protocole, ce qui signifie que, comme pour Internet, où il existe plusieurs navigateurs, il peut y avoir plusieurs logiciels différents qui cohabitent sur la même TimeChain. Cependant, par souci de compatibilité et pour limiter le risque de bugs qui laisseraient des traces indélébiles sur la TimeChain, la quasi-totalité des développeurs Bitcoin travaillent sur Bitcoin Core. Bitcoin Knot est un fork de Bitcoin Core, ce qui signifie qu’il partage la majorité de leur code, limitant grandement le risque de bugs. Ce fork a été créé par Luke Dashjr, qui souhaitait appliquer des règles plus restrictives que Bitcoin Core sans créer de hard fork. Désormais, Bitcoin Core et Bitcoin Knot cohabitent grâce au consensus de Nakamoto.

## Ajouter un "worker"


![signup](assets/4.webp)

![signup](assets/5.webp)

![signup](assets/6.webp)

![signup](assets/7.webp)

![signup](assets/8.webp)

![signup](assets/9.webp)

![signup](assets/10.webp)

![signup](assets/11.webp)

![signup](assets/12.webp)

![signup](assets/13.webp)

![signup](assets/14.webp)

![signup](assets/15.webp)

![signup](assets/16.webp)

