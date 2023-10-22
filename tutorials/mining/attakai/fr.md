---
name: Attakaï

description: transformation d'un S9 en chauffage maison
---

![cover](assets/cover.png)

# Attakai - le home-mining rendu possible et accessible !

L'initiative "Attakaï" exploite le minage de Bitcoin en utilisant la chaleur générée. Le guide propose des solutions pour rendre les mineurs adaptés à une utilisation en tant que radiateurs dans les logements, offrant ainsi plus de confort et d'économies d'énergie. Le Bitcoin ajuste automatiquement la difficulté du minage et récompense les mineurs pour leur travail. Cependant, la concentration du hashrate peut poser des risques pour la neutralité du réseau. "Attakaï" offre un guide pratique pour rétrofitter les mineurs de manière économique, permettant aux participants de réduire leur facture d'électricité et d'être récompensés avec des sats sans KYC.

## Introduction

“Attakaï », qui signifie « la température idéale » en japonais, est le nom de l’initiative visant à découvrir le minage de bitcoin à travers la réutilisation de la chaleur lancée par @ajelexBTC et @BlobOnChain avec Découvre Bitcoin. Ce guide de retrofitting d’un ASIC servira de base pour en apprendre plus sur le minage, son fonctionnement, son histoire récente et l’économie sous-jacente.

### Pourquoi réutiliser la chaleur d’un ASIC ?

Il est important de comprendre la relation entre l’énergie et la production de chaleur dans un système électrique.

Pour un investissement de 1 kW d’énergie électrique, un radiateur électrique produit 1 kW de chaleur, ni plus ni moins. Les nouveaux radiateurs ne sont pas plus performants que les radiateurs traditionnels. Leur avantage réside dans leur capacité à diffuser la chaleur de manière continue et homogène dans une pièce, apportant ainsi plus de confort par rapport aux radiateurs traditionnels qui alternent entre une forte puissance de chauffage et une absence de chauffage, générant ainsi des variations de température régulières et de l’inconfort.

Un ordinateur, ou plus largement une carte électronique, ne consomme pas d’énergie pour effectuer des calculs, il a simplement besoin que de l’énergie circule dans ses composants pour fonctionner. La consommation d’énergie est dûe à la résistance électrique des composants qui produit des pertes créant ainsi de la chaleur: c’est ce qu’on appelle l’effet joule.

Certaines entreprises ont eu l’idée de mutualiser les besoins en puissance de calcul et les besoins de chauffage grâce à des radiateurs/serveur. L’idée étant de distribuer les serveurs d’une entreprise en petites unités qui pourraient être placées dans des logements ou des bureaux. Cependant, cette idée rencontre plusieurs problèmes. Le besoin des serveurs n’est pas lié au besoin de chauffage et les entreprises ne peuvent pas utiliser les capacités de calcul de leurs serveurs de façon flexible. Il existe aussi des limites à la bande passante que des particuliers peuvent posséder. Toutes ces contraintes ne permettent pas à l’entreprise de rentabiliser ces installations coûteuses ni de fournir une offre de serveur en ligne stable sans avoir des centres de données capables de prendre le relais quand le besoin de chauffage n’est pas présent.

> “La chaleur de votre ordinateur n’est pas gaspillée si vous devez chauffer chez vous. Si vous utilisez un chauffage électrique là où vous habitez, alors la chaleur de votre ordinateur n’est pas un gâchis. C’est le même prix si vous générez cette chaleur avec votre ordinateur. Si vous avez un autre système de chauffe moins cher que l’électrique alors le gaspillage est seulement dans la différence de coût. Si c’est l’été et que vous utilisez la climatisation alors c’est le double.
> La création de bitcoins devrait avoir lieu là où elle est moins chère. Peut-être que ce sera là où le climat est froid et là où le chauffage est électrique, où miner deviendrait gratuit.”
> Satoshi Nakamoto – 8 août 2010

Le Bitcoin et sa preuve de travail se démarquent car ils ajustent automatiquement la difficulté du minage en fonction de la quantité de calcul effectuée par l’ensemble du réseau, cette quantité s’appelle le hashrate et est exprimée en hash/seconde. Aujourd’hui il est estimé à 280 Exahash/seconde, soit 280 milliards de milliards de hash/seconde. Ce hashrate représente du travail et donc une quantité d’énergie dépensée. Plus le hashrate est élevé, plus la difficulté augmente, et inversement. Ainsi, on peut activer ou désactiver un mineur Bitcoin à n’importe quel moment sans incidence pour le réseau contrairement aux radiateurs/serveurs qui nécessiteraient de rester stables pour offrir leur service. Le mineur est récompensé pour le travail effectué relativement au travail des autres, aussi petite cette participation soit-elle.

En résumé, un radiateur électrique et un mineur Bitcoin produisent tous deux 1 kW de chaleur pour 1 kW d’électricité dépensée. Cependant, le mineur reçoit également des bitcoins en récompense. Indépendamment du prix de l’électricité, du prix du bitcoin ou de la concurrence de l’activité de minage sur le réseau Bitcoin, il est économiquement plus avantageux de se chauffer avec un mineur plutôt qu’avec un radiateur électrique.

![Video présentation](https://youtu.be/gKoh44UCSnE)

### La plus-value pour Bitcoin

Nous ne rentrerons pas dans les détails du fonctionnement du minage ici (ressources disponibles sur l’académie si besoin). Ce qu’il est important de comprendre, c’est la manière dont le minage participe à la décentralisation de Bitcoin.
Plusieurs technologies déjà existantes ont été ingénieusement combinées pour donner vie au consensus de Nakamoto. Ce consensus permet de récompenser économiquement les acteurs honnêtes pour leur participation au fonctionnement du réseau Bitcoin, tout en décourageant les acteurs malhonnêtes. C’est l’un des points clés qui permet au réseau d’exister de façon durable.
Les acteurs honnêtes, ceux qui effectuent du minage selon les règles, sont tous en concurrence les uns avec les autres pour obtenir la plus grande part possible de la récompense pour la production de nouveaux blocs. Cette incitation économique conduit naturellement à une forme de centralisation car des entreprises choisissent de se spécialiser dans cette activité lucrative en réduisant leurs coûts grâce aux économies d’échelle. Ces acteurs industriels ont une position avantageuse, pour l’achat, la maintenance de machines mais aussi pour la négociation de tarifs d’électricité de gros.

> “Au début, la plupart des utilisateurs exécuteraient des nœuds de réseau, mais à mesure que le réseau se développerait au-delà d’un certain point, il serait de plus en plus laissé aux spécialistes avec des fermes de serveurs de matériel spécialisé. Une batterie de serveurs n’aurait besoin que d’un seul nœud sur le réseau et le reste du LAN se connecte à ce nœud.” - Satoshi Nakamoto – 2 novembre 2008

Certaines entités détiennent un pourcentage considérable du hashrate total dans de grandes fermes de minage. On peut observer la récente vague de froid aux États-Unis où une partie importante du hashrate a été mise hors ligne pour permettre à l’énergie d’être redirigée vers les foyers ayant un besoin exceptionnel d’électricité. Pendant plusieurs jours, les mineurs ont été incités économiquement à éteindre leurs fermes et on peut donc voir cette météo exceptionnelle sur la courbe du hashrate de Bitcoin.

Ce sujet pourrait devenir problématique et apporte un risque important pour la neutralité du réseau. Un acteur possédant plus de 51% du hashrate pourrait plus facilement censurer des transactions s’il le souhaitait. C’est pourquoi il est important de distribuer le hashrate entre de multiples acteurs plutôt que dans des entités centralisées qui pourraient être plus facilement saisies par un gouvernement, par exemple.

**Si les mineurs sont répartis dans des milliers, voire des millions de logements à travers le monde, il devient très compliqué pour un État d’en prendre le contrôle.**

À sa sortie d’usine, un mineur n’est pas approprié pour servir de radiateur dans un logement, en raison de deux problèmes principaux : un bruit excessif et l’absence de réglages. Cependant, ces problèmes peuvent être facilement résolus grâce à des modifications simples réalisées au hardware et au software, permettant d’obtenir un mineur beaucoup plus silencieux et pouvant être paramétré et automatisé comme les chauffages électriques modernes.

**Attakaï est une initiative éducative qui vous apprend à effectuer un retrofitting de l’Antminer S9 de la manière la plus économique possible.**

C’est une excellente opportunité pour apprendre en pratiquant. En plus de réduire votre facture d’électricité, vous êtes récompensé pour votre participation par des sats KYC free.

## Chapitre 1 : Guide d’achat pour un ASIC d’occasion

Dans cette section nous allons voir les bonnes pratiques afin d’acheter un Bitmain Antminer S9 d’occasion, la machine sur laquelle ce tutoriel de retrofitting en radiateur sera basé. Ce guide fonctionne aussi pour d’autres modèles d’ASIC car il s’agit d’un guide d’achat général pour du matériel de minage d’occasion.

Le Antminer S9 est un appareil proposé par Bitmain depuis mai 2016. Il consomme 1400W d’électricité et produit 14,5 TH/s. Bien qu’il soit considéré comme ancien, il reste une excellente option pour débuter le minage. Étant donné qu’il a été produit en grande quantité, il est facile de trouver des pièces détachées en abondance dans de nombreuses régions du monde. On peut généralement l’acquérir de façon pair à pair sur des sites tels qu’Ebay ou LeBonCoin, car les revendeurs s’adressant aux professionnels ne le proposent plus en raison de sa moindre compétitivité par rapport à des machines plus récentes. Il est moins efficient que des ASIC comme le Antminer S19, proposé depuis mars 2020, mais cela en fait un matériel d’occasion abordable et plus approprié pour les modifications que nous allons effectuer.

Le Antminer S9 existe en plusieurs déclinaisons (i,j) qui apportent des modifications mineures au matériel de première génération. Nous ne pensons pas que cet élément devrait orienter votre décision d’achat et ce guide fonctionnera pour toutes ces déclinaisons.

Le prix des ASIC varie en fonction de nombreux facteurs comme le cours du prix du bitcoin, la difficulté du réseau, l’efficience de la machine et le coût de l’électricité. Il est donc difficile de donner une estimation précise pour l’achat d’une machine d’occasion. En février 2023, le prix attendu en France se situe généralement entre 100€ et 200€ mais ces prix sont susceptibles de changer très rapidement

![image](assets/guide-achat/1.jpeg)

Le Antminer S9 est composé des parties suivantes :

- 3 hashboards où sont les puces qui produisent le hachage

![image](assets/guide-achat/2.jpeg)

- Une carte de contrôle comprenant un emplacement pour une carte SD, un port Ethernet et des connecteurs pour les hashboards et les ventilateurs. C’est le cerveau de votre ASIC.

![image](assets/guide-achat/3.jpeg)

- 3 câbles de data qui connectent les hashboards avec la carte de contrôle

![image](assets/guide-achat/4.jpeg)

- L’alimentation qui fonctionne en 220V et peut donc être branchée comme un appareil ménager classique

![image](assets/guide-achat/5.jpeg)

- 2 ventilateurs de 120mm

![image](assets/guide-achat/6.jpeg)

- Un cable C13 mâle

![image](assets/guide-achat/7.jpeg)

Lorsque vous achetez une machine d’occasion, il est important de vérifier que toutes les pièces sont incluses et fonctionnelles. Lors de l’échange, vous devriez demander au vendeur de mettre en marche la machine pour vérifier son bon fonctionnement. Il est important de vérifier que l’appareil s’allume correctement, puis de vérifier la connectivité à internet en branchant un câble Ethernet et en accédant à l’interface de connexion de Bitmain via un navigateur internet sur le même réseau local. Vous pourrez trouver cette adresse IP en vous connectant à l’interface de votre routeur internet et en cherchant les appareils connectés. Cette adresse devrait avoir le format suivant : 192.168.x.x

![image](assets/guide-achat/8.gif)

Vérifiez également que les identifiants par défaut fonctionnent (identifiant : root, mot de passe : root). Si les identifiants par défaut ne fonctionnent pas il faudra effectuer un reset de la machine.

![image](assets/guide-achat/9.jpeg)

Une fois connecté, vous devriez pouvoir voir l’état de chaque hashboard sur le tableau de bord. Si le mineur est connecté à une pool, vous devriez voir toutes les hashboards fonctionner. Il est important de noter que les mineurs font beaucoup de bruit, c’est normal. Assurez-vous également que les ventilateurs fonctionnent correctement.

Vous pouvez ensuite supprimer la pool de minage de l’ancien propriétaire pour configurer la vôtre par la suite. Si vous le souhaitez, vous pouvez également inspecter les hashboards en démontant la machine. Cependant, cette étape est plus complexe et nécessite plus de temps et certains outils. Si vous souhaitez procéder à ce démontage, vous pouvez vous référer à la partie suivante de ce tutoriel qui détaille comment le faire. Il est important de noter que les mineurs collectent beaucoup de poussière et nécessitent un entretien régulier. C’est cette accumulation de poussière et la qualité de l’entretien que vous pourrez observer en démontant la machine.
Après avoir passé en revue tous ces points, vous pouvez acheter votre machine avec un degré de confiance maximum. En cas de doute, adressez-vous à la communauté et si vous avez besoin de matériel pour réaliser ce tutoriel, n’hésitez pas à nous envoyer un message.

Pour synthétiser ce guide en une phrase : **« Ne faites pas confiance, vérifiez »**.

## Chapitre 2 : Guide d’achat des pièces pour modifications

![image](assets/piece/1.jpeg)

### Comment transformer votre Antminer S9 en un chauffage silencieux et connecté ?

Si vous êtes propriétaire d’un Antminer S9, vous savez probablement à quel point cet équipement peut être bruyant et encombrant. Cependant, il est possible de le transformer en un chauffage silencieux et connecté en suivant quelques étapes simples. Dans cet article nous allons vous présenter les équipements nécessaires pour effectuer les modifications, tandis qu’un article ultérieur expliquera en détail les étapes à suivre pour réaliser ces changements.

### 1. Remplacer les ventilateurs

Les ventilateurs d’origine de l’Antminer S9 sont trop bruyants pour utiliser votre Antminer en chauffage. La solution est de les remplacer par des ventilateurs plus silencieux. Notre équipe a testé plusieurs modèles de la marque Noctua et a sélectionné le Noctua NF-A14 iPPC-2000 PWM comme le meilleur compromis, attention à bien choisir la version 12V des ventilateurs. Ce ventilateur de 140mm peut permettre de produire jusqu’à 1300W de chauffage tout en maintenant un niveau de bruit théorique de 31 dB. Pour pouvoir monter ces ventilateurs de 140mm, il faudra utiliser un adaptateur 140mm vers 120mm que vous pourrez retrouver sur la boutique de DécouvreBitcoin. Et nous ajouterons également des grilles de protection 140mm.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

Le ventilateur de l’alimentation est également assez bruyant et doit être remplacé. Attention!! il existe plusieurs modèles d’alimentation pour Antminer S9 avec des ventilateurs différents. Prenez le temps de mesurer le diamétre de celui-ci. Il devrait être de 60mm ou 40mm. Nous recommandons la marque Noctua NF-A6x25 FLX 12V ou NF-A4X20 FLX 12V. Notez que les connecteurs des ventilateurs Noctua ne sont pas les mêmes que ceux d’origine, donc vous aurez besoin d’un sucre pour les connecter, 2 suffiront. Attention ici aussi à bien choisir la version 12V du ventilateur

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

### 2. Ajouter un bridge WIFI/Ethernet

Au lieu d’utiliser un câble Ethernet, vous pouvez connecter votre Antminer en WIFI en ajoutant un bridge WIFI/Ethernet. Nous avons sélectionné le vonets vap11g-300 car il permet facilement de récupérer le signal WIFI de votre box Internet et de le transmettre à votre Antminer en Ethernet sans créer de sous réseau. Si vous avez des compétences en électricité pouvez l’alimenter directement avec l’alimentation du Antminer sans avoir besoin de rajouter un chargeur USB, pour cela vous aurez besoin d’un jack 5,5mmx2,1mm femelle.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

### 3. Optionnel : ajouter une prise connectée

Si vous souhaitez allumer/éteindre votre Antminer depuis votre smartphone et monitorer sa consommation d’énergie, vous pouvez ajouter une prise connectée. Nous avons testé la prise ANTELA en version 16A compatible avec l’application smartlife. Cette prise connectée permet de consulter la consommation jour par jour et mois par mois et se connecte directement en WIFI à votre box Internet.

![image](assets/piece/8.jpeg)

> Liste du matériel et liens
>
> - 2X pièce 3D adapteur 140mm vers 120mm
> - [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)
> - [2X Grilles de ventilateurs 140mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
> - [Noctua NF-A6x25 FLX](https://www.amazon.fr/Noctua-NF-A6X25-FLX-ventilateur-Marron/dp/B009LEKGGE/ref=sr_1_1?__mk_fr_FR=ÅMÅŽÕÑ&crid=194YUD4V4OR20&keywords=NF-A6x25+FLX&qid=1688562939&sprefix=nf-a6x25+flx%2Caps%2C153&sr=8-1)
> - [Sucre d’électricien 2,5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
> - [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
> - [Optionnel prise connectée ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)



## Chapitre 3 - Modification du software - Réinitialiser un Antminer S9

Pour suivre ce tutoriel vous pouvez brancher votre machine directement avec un câble Ethernet ou alors vous pouvez utiliser le bridge Vonet de ce tutoriel. [Suivez ce lien sur notre chaîne youtube pour voir comment l'installer](https://www.youtube.com/watch?v=y4oYURBaPqg)

### Réinitialiser via le bouton « Reset »

Cette méthode peut être appliquée dans les 10 minutes après le démarrage du mineur.

Après avoir allumé le mineur pendant 2 minutes, veuillez appuyer sur le bouton « Reset » pendant 5 secondes, puis relâchez-le. Le mineur sera restauré aux paramètres d’usine dans les 4 minutes et redémarrera automatiquement (il n’est pas nécessaire de l’éteindre).

![image](assets/software/1.jpeg)

### Réinitialiser via l'interface web

Connectez-vous à l’interface utilisateur de votre mineur, cliquez sur « Upgrade » >> « Effectuer une réinitialisation », puis cliquez sur « OK » dans la fenêtre pop-up.

### Système d’exploitation d’origine

Pour cette partie, nous supposerons que la machine fonctionne, est en marche et que son système d’exploitation d’origine est installé. Nous allons voir brièvement l’interface du système d’exploitation d’origine proposée par Bitmain.

Tout d’abord, connectez-vous à votre machine à travers votre réseau local :

![image](assets/software/2.gif)

Une fois sur la page de connexion, vous devrez vous connecter à l’ASIC en utilisant les identifiants par défaut.

- username: root
- password: root

(Comment reset si mot de passe par défaut ne fonctionne pas ?)

Le système d’exploitation principal est relativement basique. Avec les 4 onglets : System, Miner Configuration, Miner Status, Network. Dans l’onglet Miner Configuration vous pouvez configurer jusqu’à 3 pools de minage.

![image](assets/software/3.jpeg)

Dans l’onglet Miner Status vous pourrez observer différentes informations sur le fonctionnement de l’ASIC en direct. Le hashrate exprimé en GH/s, des informations plus précises sur la pool ainsi qu’un détail sur le statut de chaque hashboard et la vitesse des ventilateurs en rotations/minute.

![image](assets/software/4.jpeg)

### Braiins OS+

Maintenant, nous allons étudier le logiciel pour ASICs Braiins OS+(https://braiins.com/os/plus). Le logiciel est développé par la société Braiins(https://braiins.com/) qui est l’entreprise mère de la pool de minage Braiins Pool'https://braiins.com/pool). Cette pool de minage possède au moment de l’écriture de ces lignes 4.39% du hashrate global( https://mempool.space/fr/mining/pool/slushpool). La société basée à Prague était anciennement nommée Slushpool et est la première pool de minage ayant débuté en novembre 2010. Aujourd’hui la société aux activités variées propose des outils d’étude de profitabilité pour le minage ( https://insights.braiins.com/en), des solutions de gestion de fermes de minage en parallèle de son activité de pool et son logiciel d’optimisation pour ASICs. Elle propose aussi de miner en utilisant le nouveau protocole Stratum V2(https://braiins.com/bitcoin-mining-stack-upgrade).

Nous allons donc étudier plus en détail le fonctionnement des appareils de la marque Bitmain qui sont pour l’instant les seuls modèles compatibles :

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

Le logiciel Braiins OS peut être installé assez simplement sur toutes les machines citées ci-dessus. Il permettra un contrôle plus précis d’une machine en permettant de l’overclocker sur-cadençage ou de l’underclocker sous-cadençage. Il permet également un réglage fin de la fréquence de chaque puce grâce à une fonctionnalité d’optimisation automatique appelée l’autotuning. Comme chaque puce de hachage est légèrement différente du fait de son procédé de fabrication, le logiciel teste la fréquence optimale pour chacune d’entre elles afin d’obtenir une efficience (W/THs) maximum. Le logiciel annonce des performances pouvant être supérieures de 25% à celles d’origine. Selon nos mesures il est possible d’atteindre ces figures.

## Installation de Braiins OS+

Il existe plusieurs façons d’installer Braiins OS+ sur un ASIC. Vous pouvez vous référer à ce guide mais aussi à la documentation officielle de Braiins et aux tutoriels vidéo.
Installation de Braiins OS+ directement sur la mémoire du Antminer

Découvrez comment installer facilement Braiins OS+ directement sur la mémoire de votre Antminer avec BOS toolbox, en remplaçant ainsi le système d’exploitation d’origine, à travers les étapes détaillées ci-dessous. Si vous souhaitez conserver l’OS d’origine en parallèle vous pouvez installer Braiins OS+ sur un carte SD.

1. Alimentez votre Antimner et branchez le à votre Box internet
2. Télécharger BOS toolbox Windows / Linux
3. Décompressez le fichier téléchargé et ouvrez le fichier bos-toolbox.bat choisissez la langue puis après quelque instant vous verrez cette fenêtre:

![image](assets/software/5.jpeg)

4. Bos toolbox va vous permettre de facilement trouver l’adresse IP de votre Antminer et installer Braiins OS+. Si vous connaissez déjà l’adresse IP de cotre machine vous pouvez passer à l’étape 8. Autrement, aller dans l’onglet scan.

![image](assets/software/6.jpeg)

5. Habituellement sur les réseaux domestique la plage d’adresse IP se situe entre 192.168.1.1 et 192.168.1.255, mettez donc dans le champs IP range “192.168.1.0/24. Si votre réseaux est différent veuillez changer ces adresses. Puis cliquez sur “Start”

6. Attention, si le Antminer possède un mot de passe alors la détection ne fonctionnera pas. Si c’est le cas le plus simple est d’effectuer un Reset factory

7. Vous devriez voir apparaître l’ensemble des Antminer sur votre réseau, ici l’adresse IP est 192.168.1.37

![image](assets/software/7.jpeg)

8. Cliquez sur Back puis l’onglet install, rentrez l’adresse IP précédemment trouvée dans le champs Miner(s) et “admin” (ou “root”) dans le champs Password, c’est le mot de passe par défaut puis cliquer sur “Start”.
   Si l’installation ne fonctionne pas, ni avec “admin” ou “root” en Password il peut être nécessaire d’effectuer un reset factory puis essayer de nouveau.

![image](assets/software/8.jpeg)

9. Après quelques instants, votre Antminer va redémarrer et vous pourrez accéder à l’interface de Braiins OS+ à l’adresse IP en question, ici 192.168.1.37 à rentrer directement dans la barre d’adresse de votre navigateur, username par défaut “root” pas de password par défaut.
   Installation de Braiins OS+ sur une carte SD

![image](assets/software/9.jpeg)

![image](assets/software/10.jpeg)

La deuxième méthode utilise l’interface d’origine de votre Antminer. Cette méthode fonctionne pour les machines avec un système d’exploitation datant d’avant 2019.

### Interface Antminer

1. Télécharger le nouveau système d’exploitation à installer ici.
2. Comme dans la section précédente, connectez vous à votre machine à travers votre réseau local.
3. Allez dans l’onglet System puis Upgrade
4. Chargez le fichier que vous avez téléchargé et flashez l’image.

![image](assets/software/11.jpeg)

### Carte micro SD

Une seconde méthode vous permet d’utiliser une carte micro SD. Cette méthode fonctionne uniquement avec les machines avec un système d’exploitation datant d’après 2019.

1. Téléchargez le nouveau système d’exploitation à installer ici.

2. Flashez l’image téléchargée sur une carte Micro SD. pour cela, vous pouvez utiliser Etcher. Simplement copier le fichier dans la carte micro SD ne fonctionnera pas.

3. Si vous possédez un Antminer S9 et ses déclinaisons (S9i, S9j) vous devrez ajuster des “jumper” pour forcer votre ASIC à démarrer à partir du fichier contenu sur la carte micro SD plutôt que la NAND. Si vous avez un autre modèle, vous pouvez passer à la partie 4. Les jumpers se trouvent sur la carte de contrôle sur la partie supérieur de l’ASIC, à proximiter du port Ethernet. Vous devrez la retirer en la faisant glisser en arrière. Une fois la position du jumper modifiée comme sur les images ci-dessous BOOT FROM SD vous pouvez réinsérer la carte de contrôle et connecter le S9 à nouveau.

![image](assets/software/12.jpeg)

![image](assets/software/13.jpeg)

4. Insérez la carte micro SD dans l’ASIC.
5. Démarrez l’ASIC. Si la version d’installation automatique a été utilisée, le nouveau système d’exploitation sera automatiquement installé. L’installation est terminée lorsque les deux LEDs s’allument au même moment. Vous pouvez redémarrer l’ASIC et retirer la carte micro SD. Si l’autre version a été téléchargée, vous devrez laisser la carte Micro SD à l’intérieur de l’ASIC.

Pour plus d’informations sur l’installation, vous pouvez visiter cette section du site de Braiins.

## L’interface

Vous devrez vous connecter à votre ASIC de façon similaire. En utilisant l’adresse IP locale de votre appareil sur votre réseau à travers un navigateur.

Les identifiants par défaut sont les mêmes que le système d’exploitation d’origine.

- username: root
- password: 

Vous serez alors accueilli par le Dashboard de Brains OS+

### Dashboard

![image](assets/software/14.jpeg)

Sur cette première pages vous pourrez observer les performances de votre machine en direct.

- Trois graphiques en temps réel qui vous présente la température, le hashrate ainsi que le statut global de votre machine.
- Sur la droite le hashrate réel, la température moyenne des puces, votre efficience estimée en W/THs ainsi que la consommation électrique.
- Au dessous la vitesse de rotation des ventilateurs en pourcentage de la vitesse maximum ainsi que le nombre de rotations/minute.

![image](assets/software/15.jpeg)

- Plus bas vous trouverez une vue détaillée de chaque hashboard. La température moyenne de la board et des puces qui la compose, la tension et la fréquence.
- Un détail sur les pools de minage active dans Pools.
- Le statut de l’autotuning dans Tuner Status.
- Sur la droite des détails sur les parts transmises à la pool.

### Configuration

![image](assets/software/16.jpeg)

### System

![image](assets/software/17.jpeg)

### Quick actions

![image](assets/software/18.jpeg)

Configuration d’une pool

On peut imaginer une pool de minage comme une coopérative agricole. Les agriculteurs mettent en commun leur production pour réduire la variance de l’offre et de la demande et ainsi obtenir des revenus plus stables pour leur exploitation. Une pool de minage fonctionne de la même manière et la matière première mise en commun sont des hash. En effet, la découverte d’un seul hash valide permet la création d’un bloc et ainsi de remporter la coinbase ou la récompense aujourd’hui de 6,25 BTC plus les frais des transactions inclus dans le bloc. Si vous minez seul, vous ne serez récompensé que lorsque vous trouverez un bloc. Étant en compétition contre tous les autres mineurs de la planète, vous auriez donc très peu de chances de remporter ce grand loto et vous devriez malgré tout payer les frais associés à l’utilisation de votre mineur sans aucune garantie de réussite. Les pools de minage viennent répondre à cette problématique en mutualisant la puissance de calcul de plusieurs (milliers) de mineurs et en partageant la récompense de ces derniers en fonction du pourcentage de participation au hashrate de la pool lorsqu’un bloc a été trouvé. Pour visualiser vos chance de miner un block de miner un block seul vous pouvez utiliser cet outil. En rentrant les informations d’un Antminer S9 on voit que les chances de trouver un hash permettant la création d’un block sont de 1/24 777 849 chaque bloc ou de 1/ 172 068 par jour. Il faudrait en moyenne (avec un hashrate et une difficulté constante) 471 ans pour trouver un bloc.

Malgré tout, comme dans Bitcoin tout est probabilité, il arrive parfois que des “solo miner” soit récompensés pour cette prise de risque : Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Si vous aimez jouer, vous pouvez essayer, mais notre guide ne s’orientera pas dans cette direction. Au lieu de cela, nous allons nous concentrer sur la pool de minage qui convient le mieux à nos besoins pour créer un système de chauffage.

Les considérations à avoir en choisissant une pool de minage sont le fonctionnement des récompenses de la pool, qui peuvent être différentes, ainsi que le montant minimum avant de pouvoir retirer les récompenses sur une adresse. Par exemple, Braiins, qui propose le logiciel dont nous parlons ici, propose également une pool. Cette pool a un système de récompense appelé “Score” qui encourage les mineurs à miner pendant de longues périodes. La participation inclut un facteur de temps d’activité qui est exprimé avec un “scoring hashrate”. Dans notre cas, où nous souhaitons un système de chauffage qui peut être allumé pendant quelques minutes seulement, ce n’est pas le système de récompense idéal. Nous préférons plutôt un système de récompense qui nous donne une récompense égale pour chaque participation. De plus, le montant minimum de retrait pour Braiins Pool est de 100 000 sats et On-Chain. Nous perdons donc quelques sats en frais de transaction et une partie de notre récompense peut être bloquée si nous ne minons pas suffisamment pendant l’hiver.

Le modèle de récompense qui nous intéresse est le PPS, qui signifie « pay-per-share ». Cela signifie que le mineur recevra une récompense pour chaque partage valide. Il existe également une variante de ce système, le FPPS (Full Pay Per Share), qui divise non seulement la récompense de la coinbase, mais aussi les frais de transaction inclus dans le bloc. Les pools de minage que nous vous recommandons pour connecter votre minage/chauffage sont Linecoin Pool (FPPS) et Nicehash (PPS).

- Nicehash : L’avantage de Nicehash est que le retrait peut être effectué en utilisant Lightning avec des frais minimes. De plus, le montant minimum de retrait est de 2000 sats. L’inconvénient est que Nicehash utilise son hashrate pour la blockchain la plus rentable, sans donner vraiment le contrôle à l’utilisateur et elle ne participe donc pas forcément au hashrate de Bitcoin.

- Lincoin : L’avantage de Linecoin est le nombre de fonctionnalités proposées, telles qu’un tableau de bord détaillé, la possibilité de faire des retraits avec un Paynym (BIP 47) pour une meilleure protection de la vie privée, et l’intégration d’un bot Telegram ainsi que des automatisations directement configurables dans l’application mobile. Cette pool ne mine que des blocs Bitcoin mais le montant minimum pour retirer reste élevé à 100 000 sats. Nous examinerons plus en détail l’interface d’une de ces pools dans un prochain article.

Pour configurer une pool dans Braiins 0S+, il faudra créer un compte dans l’une des pool de votre choix. Ici nous allons prendre l’exemple de Lincoin :

![image](assets/software/19.jpeg)

Une fois votre compte créé, cliquez sur Connect To Pool

Ensuite copiez l’adresse Stratum ainsi que votre username :

![image](assets/software/20.jpeg)

Vous pouvez à présent retourner dans l’interface de Braiins OS+ afin de rentrer ces identifiant. Pour le mot de passe, vous pouvez laisser le champ vide.

![image](assets/software/21.jpeg)

### Overclocking et Underclocking

L’overclocking et l’autotuning consiste tous les deux à ajuster les fréquences sur les cartes de hachage pour améliorer les performances de l’ASIC. La différence entre les deux réside dans la complexité de ces réglages de fréquence.

L**overclocking** est un ajustement simple qui consiste à augmenter la fréquence sur les cartes de hachage pour augmenter le taux de hachage de la machine. L’underclocking, quant à lui, consiste à diminuer la fréquence d’horloge d’un circuit intégré en dessous de sa fréquence nominale En réduisant la fréquence d’horloge d’un ASIC par l’underclocking, on réduit également la chaleur générée par le matériel. Cela permet de diminuer la vitesse des ventilateurs nécessaires pour refroidir l’ASIC, car ils n’ont pas à travailler aussi dur pour maintenir une température appropriée. En réduisant la vitesse des ventilateurs, le bruit généré par l’ASIC est également réduit. Cela peut être particulièrement utile pour les utilisateurs qui utilisent des ASIC à la maison et qui cherchent à minimiser les perturbations sonores causées par le matériel de minage.

Il est important de noter que l’underclocking peut entraîner une réduction des performances de l’ASIC, il est donc important de trouver un bon équilibre entre les performances et le bruit.

Braiins OS+ prend en charge l’overclocking, l’underclocking des ASICs et l’autotuning. Il permet aux utilisateurs de régler la fréquence d’horloge de leur matériel de manière flexible pour maximiser les performances ou économiser de l’énergie selon leurs préférences.

### Autotuning

Avant 2018, les mineurs avaient deux moyens de gagner un avantage dans leur activité : trouver de l’électricité à un coût raisonnable et acheter du matériel plus efficace. Cependant, en 2018, une nouvelle avancée a été découverte dans le domaine des logiciels et des micrologiciels miniers, appelée AsicBoost. Cette technique permet aux mineurs de réduire leurs coûts d’environ 13% en modifiant le micrologiciel exécuté sur leurs appareils.

Aujourd’hui, il existe une nouvelle avancée dans le secteur des logiciels et des micrologiciels miniers appelée autoréglage (ou autotuning) qui offre un avantage encore plus important qu’AsicBoost. Les ASIC sont composées de nombreuses petites puces informatiques qui effectuent le hachage. Ces puces sont faites de silicium, le même élément largement utilisé dans les semi-conducteurs et autres composants microélectroniques. La compréhension clé ici est que toutes les puces de silicium ne sont pas identiques – chacune peut varier légèrement dans ses propriétés électriques. Les fabricants de matériel le savent et publient les spécifications de performances de leurs machines minières en fonction de la limite inférieure de leurs tolérances. En d’autres termes, les fabricants connaissent la fréquence qui fonctionne le mieux pour les puces moyennes et ils utilisent cette fréquence de manière uniforme pour toutes les puces de la machine.

Cela met une limite supérieure au taux de hachage qu’une machine peut avoir. L’autoréglage est un processus dans lequel des algorithmes évaluent les fréquences optimales pour le hachage puce par puce, au lieu de traiter l’ensemble de la machine comme une seule unité. Cela signifie qu’une puce de meilleure qualité qui peut effectuer plus de hachages par seconde obtiendra une fréquence plus élevée, et une puce de qualité inférieure qui peut effectuer relativement moins obtiendra une fréquence plus faible. Le réglage automatique par puce est essentiellement un moyen d’optimiser les performances d’un ASIC via le logiciel et le micrologiciel qui y sont exécutés.

Le résultat final est un taux de hachage plus élevé par watt d’électricité, ce qui signifie des marges bénéficiaires plus importantes pour les mineurs. La raison pour laquelle les machines ne sont pas distribuées avec ce type de logiciel est que la variance par machine n’est pas souhaitable, car les clients veulent savoir exactement ce qu’ils obtiennent et il est donc une mauvaise idée pour les fabricants de vendre un produit qui n’a pas des performances constantes et prévisibles d’une machine à l’autre. En outre, le réglage automatique par puce nécessite des ressources de développement considérables, car il est complexe à mettre en place. Les fabricants dépensent déjà beaucoup de ressources pour développer leurs propres firmwares. Il existe des solutions logicielles qui permettent de mettre en place l’autotuning, comme Braiins OS+. En plus d’améliorer les performances de l’ASIC jusqu’à 20%.

## Chapitre 4 - TUTORIEL : Comment transformer un mineur en chauffage ?

![image](assets/hardware/0.jpeg)

Si vous êtes un bricoleur averti et que vous cherchez à transformer un mineur en chauffage, ce tutoriel est fait pour vous. Nous tenons à vous avertir que les modifications apportées à un appareil électronique peuvent présenter des risques électriques et d’incendie. Il est donc essentiel de prendre toutes les précautions nécessaires pour éviter tout dommage ou blessure.
En sortie d’usine, un mineur n’est pas vraiment utilisable comme radiateur dans un logement, car il est beaucoup trop bruyant et qu’il n’est pas réglable. Toutefois, il est possible d’effectuer des modifications simples pour résoudre ces problèmes.

> ATTENTION : Il est essentiel d’avoir préalablement installé Braiins OS+ sur votre mineur, ou tout autre logiciel ayant la capacité de réduire les performances de votre machine. Cette mesure est cruciale, car dans le but de réduire le bruit, nous allons installer des ventilateurs moins puissants, qui pourront dissiper moins de chaleur.

### Matériels nécessaires

- 2 pièces 3D adapteur 140mm vers 120mm avec 8 visses de 16mm
- 2 ventilateurs Noctua NF-A14 iPPC-2000 PWM
- 2 grilles de ventilateurs 140mm
- 1 ventilateur Noctua NF-A6x25 FLX
- Sucre d’électricien 2,5mm2
- Vonets VAP11G-300
- Optionnel : prise connectée ANTELA

### Remplacement des ventilateurs

Nous allons commencer par remplacer le ventilateur de l’alimentation.

> ATTENTION : Tout d’abord, avant de commencer, assurez-vous de bien avoir débranché votre mineur pour éviter tout risque d’électrocution.

![image](assets/hardware/1.jpeg)

Nous allons commencer par remplacer le ventilateur de l’alimentation.

Tout d’abord, retirez les 6 vis sur le côté du boîtier qui le maintiennent fermé. Une fois les vis retirées, ouvrez délicatement le boîtier pour retirer la protection plastique qui recouvre les composants.

![image](assets/hardware/2.jpeg)
![image](assets/hardware/3.jpeg)

Ensuite, il est temps de retirer le ventilateur d’origine en prenant soin de ne pas endommager les autres composants. Pour ce faire, retirez les vis qui le maintiennent en place et décollez délicatement la colle blanche qui entoure le connecteur. Il est important de procéder avec délicatesse pour éviter d’endommager les fils ou les connecteurs.

![image](assets/hardware/4.jpeg)

Une fois le ventilateur d’origine retiré, vous remarquerez que les connecteurs du nouveau ventilateur Noctua ne correspondent pas à ceux du ventilateur d’origine. En effet, le nouveau ventilateur dispose de 3 fils, dont un fil jaune qui permet de contrôler la vitesse. Cependant, ce fil ne sera pas utilisé dans ce cas précis. Pour brancher le nouveau ventilateur, il est donc recommandé d’utiliser un adaptateur spécial. Il est cependant important de noter que cet adaptateur peut parfois être difficile à trouver.

![image](assets/hardware/5.jpeg)

Si vous ne disposez pas de cet adaptateur, vous pouvez tout de même procéder au branchement du nouveau ventilateur en utilisant un sucre d’électricien. Pour cela, vous devrez couper les câbles de l’ancien et du nouveau ventilateur, attention à garder suffisamment de longueur sur chaque câbles.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

Sur le nouveau ventilateur, utilisez un cutter et coupez délicatement les contours de la gaine principale à 1cm sans coupez les gaines des câbles en dessous.

![image](assets/hardware/8.jpeg)

Puis en tirant la gaine principale vers le bas, coupez les gaines des câble rouge et noir de la même manière que précédemment. Et coupez le câble jaune à ras.

![image](assets/hardware/9.jpeg)

Sur l’ancien ventilateur il est plus délicat de découper la gaine principale sans abîmer les gaines des files rouge et noir. Pour cela, nous avons utilisé une aiguille que nous avons glissé entre la gaine principale et les fils rouges et noirs.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Une fois les fils rouges et noirs dégagés, coupez les gaines toujours délicatement pour ne pas abîmer les fils électriques.

![image](assets/hardware/12.jpeg)

Puis relier les câbles avec un sucre, le fil noir avec le noir et le fil rouge avec le rouge. Vous pouvez également rajouter du scotch d’électricien.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)

Une fois le branchement effectué, il est temps de mettre en place le nouveau ventilateur Noctua avec la grille et les anciennes vis, les nouvelles vis qui sont dans la boîte seront réutilisé plus tard. Assurez-vous de le placer avec la bonne orientation. Vous remarquerez une flèche sur l’un des côtés du ventilateur, qui indique le sens du flux d’air. Il est important de placer le ventilateur de manière à ce que cette flèche pointe vers l’intérieur du boîtier. Puis rebranchez le ventilateur.

![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Optionnel : Si vous êtes compétent en électricité, vous pouvez ajouter directement sur la sortie d’alimentation 12V un connecteur jack 5,5 mm femelle qui permettra d’alimenter directement le bridge Wi-Fi Vonet. Cependant, si vous n’êtes pas sûr de vos compétences en électricité, il est préférable d’utiliser le connecteur USB avec un chargeur de type smartphone pour éviter tout risque de court-circuit ou de dommage électrique.

![image](assets/hardware/17.jpeg)

Une fois les branchements effectués, remettez bien le plastique du couvercle par-dessus le plastique du boîtier et pas à l’intérieur.

![image](assets/hardware/18.jpeg)

Enfin, remettez le couvercle du boîtier en place puis revissez les 6 vis sur les côtés pour maintenir le tout bien en place. Et voilà, votre boîtier d’alimentation est désormais équipé d’un nouveau ventilateur

### Remplacement des 2 ventilateurs principaux

1. Tout d’abord, débranchez les ventilateurs et dévissez-les.
   ![image](assets/hardware/19.jpeg)

2. Les connecteurs des nouveaux ventilateurs Noctua ne correspondent pas à ceux d’origine, mais pas de panique ! Sortez votre cutter et coupez délicatement les petites languettes en plastique pour que les connecteurs s’adaptent parfaitement à votre mineur.

![image](assets/hardware/20.jpeg)
![image](assets/hardware/21.jpeg)

3. C’est l’heure de l’installation des pièces 3D !
   Fixez-les des deux côtés du mineur à l’aide des vis que vous avez retirées des ventilateurs. Vissez jusqu’à ce que la tête de vis sous rentrer dans la pièce 3D et que celle-ci soit bien maintenu en place. Attention à ne pas trop serrer, vous pourriez déformer la pièce et une des vis risque de toucher un condensateur ! Puis coupez délicatement les petites languettes en plastique pour que les connecteurs s’adaptent parfaitement à votre mineur.

![image](assets/hardware/22.jpeg)

4. Passons maintenant aux ventilateurs.
   Fixez-les sur les pièces 3D à l’aide des vis fournies la boîte. Attention au sens de circulation de l’air, les flèches sur les côtés des ventilateurs vous indiqueront la direction à suivre. Allez du côté du port Ethernet à l’autre côté. Voir photo ci-dessous

![image](assets/hardware/23.jpeg)
![image](assets/hardware/24.jpeg)
![image](assets/hardware/25.jpeg)

5. Dernière étape : branchez les ventilateurs et fixez les grilles par-dessus avec les vis qui n’ont pas été utilisées dans la boîte du ventilateur de l’alimentation. Vous en avez seulement 4 mais 2 par grille dans des angles opposés suffiront. Vous pouvez également chercher d’autres vis similaires dans un magasin de bricolage si besoin.

![image](assets/hardware/26.jpeg)
![image](assets/hardware/27.jpeg)

En attendant de pouvoir offrir un casing plus sexy à votre nouveau chauffage, vous pouvez attacher le boîtier et l’alimentation ensemble avec des colliers de serrage d’électricien.

![image](assets/hardware/28.jpeg)

Et pour la touche finale, branchez le bridge Vonet sur le port Ethernet à son alimentation. Si ce n’est pas encore fait, vous pouvez suivre ce tutoriel pour paramétrer votre bridge.

![image](assets/hardware/29.jpeg)

Bravo ! Vous venez de remplacer l’ensemble de la partie mécanique de votre mineur. Vous devriez maintenant entendre beaucoup moins de bruit.

Guide crée par DecouvreBitcoin, plus d'info sur MINAGE 201 - crédit Jim et Ajelex
