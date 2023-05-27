---
name: Mining
goal: Mining
---

# Description

TODO

+++

## Chapitre 1 : Attakaï : le home-mining rendu possible et accessible !

### Résumé du chapitre

L'initiative "Attakaï" explore le minage de Bitcoin en utilisant la chaleur générée. Le guide propose des solutions pour rendre les mineurs adaptés à une utilisation en tant que radiateurs dans les logements, offrant ainsi plus de confort et d'économies d'énergie. Le Bitcoin ajuste automatiquement la difficulté du minage et récompense les mineurs pour leur travail. Cependant, la concentration du hashrate peut poser des risques pour la neutralité du réseau. "Attakaï" offre un guide pratique pour rétrofitter les mineurs de manière économique, permettant aux participants de réduire leur facture d'électricité et d'être récompensés avec des sats sans KYC.

### Introduction

“Attakaï », qui signifie « la température idéal » en japonais, est le nom de l’initiative visant à découvrir le minage de bitcoin à travers la réutilisation de la chaleur lancée par @ajelexBTC et @BlobOnChain avec Découvre Bitcoin. Ce guide de retrofitting d’un ASIC servira de base pour en apprendre plus sur le minage, son fonctionnement, son histoire récente et l’économie sous-jacente.

### Pourquoi réutiliser la chaleur d’un ASIC ?

Il est important de comprendre la relation entre l’énergie et la production de chaleur dans un système électrique.
Pour un investissement de 1 kW d’énergie électrique, un radiateur électrique produit 1 kW de chaleur, ni plus ni moins. Les nouveaux radiateurs ne sont pas plus performants que les radiateurs traditionnels. Leur avantage réside dans leur capacité à diffuser la chaleur de manière continue et homogène dans une pièce, apportant ainsi plus de confort par rapport aux radiateurs traditionnels qui alternent entre une forte puissance de chauffage et une absence de chauffage, générant ainsi des variations de température régulières et de l’inconfort.
Un ordinateur, ou plus largement une carte électronique, ne consomme pas d’énergie pour effectuer des calculs, il a simplement besoin que de l’énergie circule dans ses composants pour fonctionner. La consommation d’énergie est dû à la résistance électrique des composants qui produit des pertes créant ainsi de la chaleur c’est ce qu’on appel l’effet joule.
Certaines entreprises ont eu l’idée de mutualiser les besoins en puissance de calcul et les besoins de chauffage grâce à des radiateurs/serveur. L’idée étant de distribuer les serveurs d’une entreprise en petites unités qui pourraient être placées dans des logements ou des bureaux. Cependant, cette idée rencontre plusieurs problèmes. La besoin des serveurs n’est pas liée au besoin de chauffage et les entreprises ne peuvent pas utiliser les capacités de calcul de leurs serveurs de façon flexible. Il existe aussi des limites à la bande passante que des particuliers peuvent posséder. Toutes ces contraintes ne permettent pas à l’entreprise de rentabiliser ces installations coûteuses ni de fournir une offre de serveur en ligne stable sans avoir des centres de données capables de prendre le relais quand le besoin de chauffage n’est pas présent.
“La chaleur de votre ordinateur n’est pas gaspillée si vous devez chauffer chez vous. Si vous utilisez un chauffage électrique là où vous habitez, alors la chaleur de votre ordinateur n’est pas un gâchis. C’est le même prix si vous générer cette chaleur avec votre ordinateur.
Si vous avez un autre système de chauffe moins cher que l’électrique alors le gaspillage est seulement dans la différence de coût. Si c’est l’été et que vous utilisez la climatisation alors c’est le double.
La création de bitcoins devrait avoir lieu là où elle est moins chère. Peut-être que ce sera là où le climat est froid et là où le chauffage est électrique, où miner deviendrait gratuit.”

- Satoshi Nakamoto – 8 août 2010

Le Bitcoin et sa preuve de travail se démarquent car ils ajustent automatiquement la difficulté du minage en fonction de la quantité de calcul effectué par l’ensemble du réseau, cette quantité s’appelle le hashrate et est exprimé en hash/seconde. Aujourd’hui il est estimé à 280 Exahash/seconde, soit 280 milliards de milliards de hash/seconde. Ce hashrate représente du travail et donc une quantité d’énergie dépensée. Plus le hashrate est élevée, plus la difficulté augmente, et inversement. Ainsi, on peut activer ou désactiver un mineur Bitcoin à n’importe quel moment sans incidence pour le réseau contrairement aux radiateurs/serveurs qui nécessiterait de rester stables pour offrir leur service. Le mineur est récompensé pour le travail effectué relativement au travail des autres, aussi petite cette participation soit-elle.
En résumé, un radiateur électrique et un mineur Bitcoin produisent tout deux 1 kW de chaleur pour 1 kW d’électricité dépensée. Cependant, le mineur reçoit également des bitcoins en récompense. Indépendamment du prix de l’électricité, du prix du bitcoin ou de la concurrence de l’activité de minage sur le réseau Bitcoin, il est économiquement plus avantageux de se chauffer avec un mineur plutôt qu’avec un radiateur électrique.

La plus-value pour Bitcoin
Nous ne rentrerons pas dans les détails du fonctionnement du minage ici (ressources disponibles sur l’académie si besoin). Ce qu’il est important de comprendre, c’est la manière dont le minage participe à la décentralisation de Bitcoin.
Plusieurs technologies déjà existantes ont été ingénieusement combinées pour donner vie au consensus de Nakamoto. Ce consensus permet de récompenser économiquement les acteurs honnêtes pour leur participation au fonctionnement du réseau Bitcoin, tout en décourageant les acteurs malhonnêtes. C’est l’un des points clés qui permet au réseau d’exister de façon durable.
Les acteurs honnêtes, ceux qui effectuent du minage selon les règles, sont tous en concurrence les uns avec les autres pour obtenir la plus grande part possible de la récompense pour la production de nouveaux blocs. Cette incitation économique conduit naturellement à une forme de centralisation car des entreprises choisissent de se spécialiser dans cette activité lucrative en réduisant leurs coûts grâce aux économies d’échelle. Ces acteurs industriels ont une position avantageuse, pour l’achat, la maintenance de machines mais aussi pour la négociation de tarifs d’électricité de gros.
“Au début, la plupart des utilisateurs exécuteraient des nœuds de réseau, mais à mesure que le réseau se développerait au-delà d’un certain point, il serait de plus en plus laissé aux spécialistes avec des fermes de serveurs de matériel spécialisé. Une batterie de serveurs n’aurait besoin que d’un seul nœud sur le réseau et le reste du LAN se connecte à ce nœud.”

- Satoshi Nakamoto – 2 novembre 2008

  Certaines entités détiennent un pourcentage considérable du hashrate total dans de grandes fermes de minage. On peut observer la récente vague de froid aux États-Unis où une partie importante du hashrate a été mise hors ligne pour permettre à l’énergie d’être redirigée vers les foyers ayant un besoin exceptionnel d’électricité. Pendant plusieurs jours, les mineurs ont été incités économiquement à éteindre leurs fermes et on peut donc voir cette météo exceptionnelle sur la courbe du hashrate de Bitcoin.
  Ce sujet pourrait devenir problématique et apporte un risque important pour la neutralité du réseau. Un acteur possédant plus de 51% du hashrate pourrait plus facilement censurer des transactions s’il le souhaitait. C’est pourquoi il est important de distribuer le hashrate entre de multiples acteurs plutôt que dans des entités centralisées qui pourraient être plus facilement saisies par un gouvernement, par exemple.

Si les mineurs sont répartis dans des milliers, voire des millions de logements à travers le monde, il devient très compliqué pour un État d’en prendre le contrôle.

À sa sortie d’usine, un mineur n’est pas approprié pour servir de radiateur dans un logement, en raison de deux problèmes principaux : un bruit excessif et l’absence de réglage. Cependant, ces problèmes peuvent être facilement résolus grâce à des modifications simples réalisées au hardware et au software, permettant d’obtenir un mineur beaucoup plus silencieux et pouvant être paramétré et automatisé comme les chauffages électriques modernes.
Attakaï est une initiative éducative qui vous apprend à effectuer un retrofitting de l’Antminer S9 de la manière la plus économique possible. C’est une excellente opportunité pour apprendre en pratiquant. En plus de réduire votre facture d’électricité, vous êtes récompensé pour votre participation par des sats KYC free.

## Chapitre 2 : Guide d’achat pour un ASIC d’occasion

Dans cet article nous allons voir les bonnes pratiques afin d’acheter un Bitmain Antminer S9 d’occasion, la machine sur laquelle ce tutoriel de retrofitting en radiateur sera basé. Ce guide fonctionne aussi pour d’autres modèles d’ASIC car il s’agit d’un guide d’achat général pour du matériel de minage d’occasion.
Le Antminer S9 est un appareil proposé par Bitmain depuis mai 2016. Il consomme 1323W d’électricité et produit 13,5 TH/s. Bien qu’il soit considéré comme ancien, il reste une excellente option pour débuter le minage. Étant donné qu’il a été produit en grande quantité, il est facile de trouver des pièces détachées en abondance dans de nombreuses régions du monde. On peut généralement l’acquérir de façon pair à pair sur des sites tels qu’Ebay ou LeBonCoin, car les revendeurs s’adressant aux professionnels ne le proposent plus en raison de sa moindre compétitivité par rapport à des machines plus récentes. Il est moins efficient que des ASIC comme le Antminer S19, proposé depuis mars 2020, mais cela en fait un matériel d’occasion abordable et plus approprié pour les modifications que nous allons effectuer.
Le Antminer S9 existe en plusieurs déclinaisons (i,j) qui apportent des modifications mineures au matériel de première génération. Nous ne pensons pas que cet élément devrait orienter votre décision d’achat et ce guide fonctionnera pour toutes ces déclinaisons.
Le prix des ASIC varie en fonction de nombreux facteurs comme le cours du prix du bitcoin, la difficulté du réseau, l’efficience de la machine et le coût de l’électricité. Il est donc difficile de donner une estimation précise pour l’achat d’une machine d’occasion. En février 2023, le prix attendu en France se situe généralement entre 100€ et 200€ mais ces prix sont susceptible de changer très rapidement
Le Antminer S9 est composé des parties suivantes :

- 3 hashboards où sont les puces qui produisent le hachage
- Une carte de contrôle comprenant un emplacement pour une carte SD, un port Ethernet et des connecteurs pour les hashboards et les ventilateurs. C’est le cerveau de votre ASIC.
- 3 câbles de data qui connectent les hashboards avec la carte de contrôle
- L’alimentation qui fonctionne en 220V et peut donc être branchée comme un appareil ménager classique
- 2 ventilateurs de 120mm
- Un cable C13 mâle
  Lorsque vous achetez une machine d’occasion, il est important de vérifier que toutes les pièces sont incluses et fonctionnelles. Lors de l’échange, vous devriez demander au vendeur de mettre en marche la machine pour vérifier son bon fonctionnement. Il est important de vérifier que l’appareil s’allume correctement, puis de vérifier la connectivité à internet en branchant un câble Ethernet et en accédant à l’interface de connection de Bitmain via un navigateur internet sur le même réseau local. Vous pourrez trouver cette adresse IP en vous connectant à l’interface de votre routeur internet et en cherchant les appareils connectés. Cette adresse devrait avoir le format suivant : 192.168.x.x
  Vérifiez également que les identifiants par défaut fonctionnent (identifiant : root, mot de passe : root). Si les identifiants par défaut ne fonctionne pas il faudra effectuer un reset de la machine.
  Une fois connecté, vous devriez pouvoir voir l’état de chaque hashboard sur le tableau de bord. Si le mineur est connecté à une pool, vous devriez voir toutes les hashboards fonctionner. Il est important de noter que les mineurs font beaucoup de bruit, c’est normal. Assurez-vous également que les ventilateurs fonctionnent correctement.
  Vous pouvez ensuite supprimer la pool de minage de l’ancien propriétaire pour configurer la vôtre par la suite. Si vous le souhaitez, vous pouvez également inspecter les hashboards en démontant la machine. Cependant, cette étape est plus complexe et nécessite plus de temps et certains outils. Si vous souhaitez procéder à ce démontage, vous pouvez vous référer à la partie suivante de ce tutoriel qui détaille comment le faire. Il est important de noter que les mineurs collectent beaucoup de poussière et nécessitent un entretien régulier. C’est cette accumulation de poussière et la qualité de l’entretien que vous pourrez observer en démontant la machine.
  Après avoir passé en revue tous ces points, vous pouvez acheter votre machine avec un degré de confiance maximum. En cas de doute, adressez-vous à la communauté et si vous avez besoin de matériel pour réaliser ce tutoriel, n’hésitez pas à nous envoyer un message.
  Pour synthétiser ce guide en une phrase : « Ne faites pas confiance, vérifiez ».

### Chapitre 3 : Guide d’achat des pièces pour modifications

Comment transformer votre Antminer S9 en un chauffage silencieux et connecté ?
Si vous êtes propriétaire d’un Antminer S9, vous savez probablement à quel point cet équipement peut être bruyant et encombrant. Cependant, il est possible de le transformer en un chauffage silencieux et connecté en suivant quelques étapes simples. Dans cet article nous allons vous présenter les équipements nécessaires pour effectuer les modifications, tandis qu’un article ultérieur expliquera en détail les étapes à suivre pour réaliser ces changements.

1. Remplacer les ventilateurs
   Les ventilateurs d’origine de l’Antminer S9 sont trop bruyants pour utiliser votre Antminer en chauffage. La solution est de les remplacer par des ventilateurs plus silencieux. Notre équipe a testé plusieurs modèles de la marque Noctua et à sélectionné le Noctua NF-A14 iPPC-2000 PWM comme le meilleur compromis, attention à bien choisir la version 12V des ventilateurs. Ce ventilateur de 140mm peut permettre de produire jusqu’à 1300W de chauffage tout en maintenant un niveau de bruit théorique de 31 dB. Pour pouvoir monter ces ventilateurs de 140mm, il faudra utiliser un adaptateur 140mm vers 120mm que vous pourrez retrouver sur la boutique de DécouvreBitcoin. Et nous ajouterons également des grilles de protection 140mm.
   Le ventilateur de l’alimentation est également assez bruyant et doit être remplacé. Nous recommandons le Noctua NF-A6x25 PWM. Notez que les connecteurs des ventilateurs Noctua ne sont pas les mêmes que ceux d’origine, donc vous aurez besoin d’un sucre pour les connecter, 2 suffirons. Attention ici aussi à bien choisir la version 12V du ventilateur.

2. Ajouter un bridge WIFI/Ethernet
   Au lieu d’utiliser un câble Ethernet, vous pouvez connecter votre Antminer en WIFI en ajoutant un bridge WIFI/Ethernet. Nous avons sélectionné le vonets vap11g-300 car il permet facilement de récupérer le signal WIFI de votre box Internet et de le transmettre à votre Antminer en Ethernet sans créer de sous réseau. Si vous avez des compétences en électricité pouvez l’alimenter directement avec l’alimentation du Antminer sans avoir besoin de rajouter un chargeur USB, pour cela vous aurez besoin d’un jack 5,5mmx2,1mm femelle.

3. Optionnel : ajouter une prise connectée
   Si vous souhaitez allumer/éteindre votre Antminer depuis votre smartphone et monitorer sa consommation d’énergie, vous pouvez ajouter une prise connectée. Nous avons testé la prise ANTELA en version 16A compatible avec l’application smartlife. Cette prise connectée permet de consulter la consommation jour par jour et mois par mois et se connecte directement en WIFI à votre box Internet.

Liste du matériel et liens

- 2X pièce 3D adapteur 140mm vers 120mm
- 2X NF-A14 iPPC-2000 PWM https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2
- 2X Grilles de ventilateurs 140mm https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details
- Noctua NF-A6x25 PWM https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ
- Sucre d’électricien 2,5mm2 https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1
- Vonets vap11g-300 https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
- Optionnel prise connectée ANTELA https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1

---

### TUTORIEL : Comment transformer un mineur en chauffage ?

Si vous êtes un bricoleur averti et que vous cherchez à transformer un mineur en chauffage, ce tutoriel est fait pour vous. Nous tenons à vous avertir que les modifications apportées à un appareil électronique peuvent présenter des risques électriques et d’incendie. Il est donc essentiel de prendre toutes les précautions nécessaires pour éviter tout dommage ou blessure.
En sortie d’usine, un mineur n’est pas vraiment utilisable comme radiateur dans un logement, car il est beaucoup trop bruyant et qu’il n’est pas réglable. Toutefois, il est possible d’effectuer des modifications simples pour résoudre ces problèmes.

ATTENTION : Il est essentiel d’avoir préalablement installé Braiins OS+ sur votre mineur, ou tout autre logiciel ayant la capacité de réduire les performances de votre machine. Cette mesure est cruciale, car dans le but de réduire le bruit, nous allons installer des ventilateurs moins puissants, qui pourront dissiper moins de chaleur.

Matériels nécessaires

- 2 pièces 3D adapteur 140mm vers 120mm
- 2 ventilateurs Noctua NF-A14 iPPC-2000 PWM
- 2 grilles de ventilateurs 140mm
- 1 ventilateur Noctua NF-A6x25 PWM
- Sucre d’électricien 2,5mm2
- Vonets VAP11G-300
- Optionnel : prise connectée ANTELA

Remplacement des ventilateurs
Nous allons commencer par remplacer le ventilateur de l’alimentation.

ATTENTION : Tout d’abord, avant de commencer, assurez-vous de bien avoir débranché votre mineur pour éviter tout risque d’électrocution.

Tout d’abord, retirez les 6 vis sur le côté du boîtier qui le maintiennent fermé. Une fois les vis retirées, ouvrez délicatement le boîtier pour retirer la protection plastique qui recouvre les composants.
Ensuite, il est temps de retirer le ventilateur d’origine en prenant soin de ne pas endommager les autres composants. Pour ce faire, retirez les vis qui le maintiennent en place et décollez délicatement la colle blanche qui entoure le connecteur. Il est important de procéder avec délicatesse pour éviter d’endommager les fils ou les connecteurs.
Une fois le ventilateur d’origine retiré, vous remarquerez que les connecteurs du nouveau ventilateur Noctua ne correspondent pas à ceux du ventilateur d’origine. En effet, le nouveau ventilateur dispose de 3 fils, dont un fil jaune qui permet de contrôler la vitesse. Cependant, ce fil ne sera pas utilisé dans ce cas précis. Pour brancher le nouveau ventilateur, il est donc recommandé d’utiliser un adaptateur spécial. Il est cependant important de noter que cet adaptateur peut parfois être difficile à trouver.
Si vous ne disposez pas de cet adaptateur, vous pouvez tout de même procéder au branchement du nouveau ventilateur en utilisant un sucre d’électricien. Pour cela, vous devrez couper les câbles de l’ancien et du nouveau ventilateur.
Sur le nouveau ventilateur, utilisez un cutter et coupez délicatement les contours de la gaine principale à 1cm sans coupez les gaines des câbles en dessous. Puis en tirant la gaine principale vers le bas, coupez les gaines des câble rouge et noir de la même manière que précédemment. Et coupez le câble jaune à ras.
Sur l’ancien ventilateur il est plus délicat de découper la gaine principale sans abîmer les gaines des files rouge et noir. Pour cela, nous avons utilisé une aiguille que nous avons glissé entre la gaine principale et les fils rouges et noirs.
Une fois les fils rouges et noirs dégagés, coupez les gaines toujours délicatement pour ne pas abîmer les fils électriques. Puis relier les câbles avec un sucre, le fil noir avec le noir et le fil rouge avec le rouge. Vous pouvez également rajouter du scotch d’électricien.

Une fois le branchement effectué, il est temps de mettre en place le nouveau ventilateur Noctua avec la grille et les anciennes vis, les nouvelles vis qui sont dans la boîte seront réutilisé plus tard. Assurez-vous de le placer avec la bonne orientation. Vous remarquerez une flèche sur l’un des côtés du ventilateur, qui indique le sens du flux d’air. Il est important de placer le ventilateur de manière à ce que cette flèche pointe vers l’intérieur du boîtier. Puis rebranchez le ventilateur.

Optionnel : Si vous êtes compétent en électricité, vous pouvez ajouter directement sur la sortie d’alimentation 12V un connecteur jack 5,5 mm femelle qui permettra d’alimenter directement le bridge Wi-Fi Vonet. Cependant, si vous n’êtes pas sûr de vos compétences en électricité, il est préférable d’utiliser le connecteur USB avec un chargeur de type smartphone pour éviter tout risque de court-circuit ou de dommage électrique.

Une fois les branchements effectués, remettez bien le plastique du couvercle par-dessus le plastique du boîtier et pas à l’intérieur. Enfin, remettez le couvercle du boîtier en place puis revissez les 6 vis sur les côtés pour maintenir le tout bien en place. Et voilà, votre boîtier d’alimentation est désormais équipé d’un nouveau ventilateur

Remplacement des 2 ventilateurs principaux

1. Tout d’abord, débranchez les ventilateurs et dévissez-les.
2. Les connecteurs des nouveaux ventilateurs Noctua ne correspondent pas à ceux d’origine, mais pas de panique ! Sortez votre cutter et coupez délicatement les petites languettes en plastique pour que les connecteurs s’adaptent parfaitement à votre mineur.
3. C’est l’heure de l’installation des pièces 3D !
   Fixez-les des deux côtés du mineur à l’aide des vis que vous avez retirées des ventilateurs. Vissez jusqu’à ce que la tête de vis sous rentrer dans la pièce 3D et que celle-ci soit bien maintenu en place. Attention à ne pas trop serrer, vous pourriez déformer la pièce et une des vis risque de toucher un condensateur ! Puis coupez délicatement les petites languettes en plastique pour que les connecteurs s’adaptent parfaitement à votre mineur.
4. Passons maintenant aux ventilateurs.
   Fixez-les sur les pièces 3D à l’aide des vis fournies la boîte. Attention au sens de circulation de l’air, les flèches sur les côtés des ventilateurs vous indiqueront la direction à suivre. Allez du côté du port Ethernet à l’autre côté. Voir photo ci-dessous
5. Dernière étape : branchez les ventilateurs et fixez les grilles par-dessus avec les vis qui n’ont pas été utilisées dans la boîte du ventilateur de l’alimentation. Vous en avez seulement 4 mais 2 par grille dans des angles opposés suffiront. Vous pouvez également chercher d’autres vis similaires dans un magasin de bricolage si besoin.

En attendant de pouvoir offrir un casing plus sexy à votre nouveau chauffage, vous pouvez attacher le boîtier et l’alimentation ensemble avec des colliers de serrage d’électricien. Et pour la touche finale, branchez le bridge Vonet sur le port Ethernet à son alimentation. Si ce n’est pas encore fait, vous pouvez suivre ce tutoriel pour paramétrer votre bridge.
Et voilà, bravo ! Vous venez de remplacer l’ensemble de la partie mécanique de votre mineur. Vous devriez maintenant entendre beaucoup moins de bruit.

Section software

Section utilisation
