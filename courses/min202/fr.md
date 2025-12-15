---
name: Titre du cours
goal: Comprendre, installer, configurer et utiliser sa première machine de mining
objectives:
  - Quelles solutions pour miner à la maison
  - Comprendre la différence entre solomining et mining en pool
  - Panorama des solutions hardware pour miner facilement chez soit
  - Panorama des solutions software
  - Etre en mesure de miner en totale autonomie, sur sa propre pool de solomining
---

# Le parcours du Bitcoiner souverain: 1- Détenir ses clés privées / 2 - Faire tourner un noeud / 3- Il est temps de miner

Le parcours du bitcoiner souverain se déroule souvent de cette manière. D'abord on cherche à mettre nos précieux satoshis à l'abris en sautant le pas de la garde en prore. On télécharge notre wallet favori et on se fournit en matériel de "stockage froid".

Ensuite on comprend que détenir ses propres clés ne suffit pas à nous garantir un accès autonôme au réseau bitcoin car seuls les opérateurs de noeuds peuvent diffuser des transactions sans demander la permission. Alors on fait tourner son propre noeud.

Pour finir l'étape ultime de tout Bitcoiner souverain c'est d'ajouter sa propre contribution à la sécurité du réseau en déployant de la puissance de calcul supplémentaire, du hashrate, et en minant depuis chez soit.

Dans ce cours MIN202 nous verrons comment miner du bitcoin à la maison, grace à des machines adaptées à cet usage et facilement configurable par tous.
Nous verrons les différentes solutions hardware qui s'offrent à nous pour se faire, les logiciels associés, comment les utiliser. 

Désormais miner à la maison est devenu simple, les solutions "plug & play" sont là et c'est une excellente nouvelle.

# Introduction


## 1.1 Aperçu du cours


Bienvenue dans le cours MIN 202. L'objectif ici sera de permettre à quiconque qui décide de miner du bitcoin de pouvoir le faire facilement chez soit, tout en en comprenant les enjeux et les limitations potentielles. Est-ce utile, est-ce rentable, si oui dans quel contexte etc...

### Partie 1- Introduction

Dans cette partie nous rappellerons rapidement les notions de bases du fontionnement de bitcoin et de  la **preuve de travail**, afin de savoir faire la différence entre un appareil de mining et un noeud bitcoin simple.
Ce sera l'occasion pour nous de rappeler le rôle de la **preuve de travail** au sein du protocole bitcoin, et donc la place des mineurs et des pool de mining dans cet écosystème, leur rôle, leur pouvoir et influence sur le protocole.
Nous verrons également les défis qui se posent au particulier qui souhaiteraient participer et miner depuis chez lui, et les solutions potentielles qui s'offrent à lui

#### Brefs Rappels sur la preuve de travail et le mining(fusionner les 3 )
#### Mineur vs Noeud
#### Qu'est ce qu'une pool de mining et à quoi ça sert ?
#### Miner soit-même "à la maison" défis et solutions




### Partie 2 - Pourquoi  et comment miner soit-même ?

Dans la seconde partie de ce cours nous essaierons de déterminer les raisons qui peuvent pousser un particulier à vouloir miner à la maison, et les différentes manière d'y parvenir en fonction du contexte et du profil de chacun.

Nous détaillerons ainsi le fonctionnement du solo ou en pool en essayant de vous aider à choisir la meilleur manière de vous y prendre en fonction de vos objectifs.

Nous dresserons à cet effet un panorama des solutions logicielles et matérielles adaptées à un usage domestique, et qui ne nécessitent aucune connaissances particulière en que ce soit en informatique ou du matériel à utliser.
#### Pourquoi faire du Solomining
#### Pourquoi miner en Pool 
#### Panorama des solutions hardware
#### Panorama des solutions software (profil de genrs, simple, cypherpunk, medium)



### Partie 3 - Installer et configurer son premier mineur personnel

Dans cette troisème grande partie, nous étudierons le projet Bitaxe en détail. Ce projet 100% Open Source tant du point de vue matériel que logiciel,vise à rendre le minage accessible à tout un chacun, en permettant de construire soit même sa machine ASIC et de l'opérer.

Puis nous verrons en détail comment installer l'appareil et le configurer. On en profitera également pour dresser une cartographie des pools de minages (solo ou mutualisé) que vous pourrez utiliser avec votre Bitaxe, et de leurs caractéristiques et spécificités.

Enfin nous en profiterons pour faire un tour complet d'AXEOS le système d'exploitation de votre Bitaxe, afin de comprenre comment le piloter sur le bout des doigts.

Pour finir on passera en revue les bonnes pratiques visant le bon entretien de votre machine afin que celle-ci soit opérationnelle le plus longtemps possible.


#### Bitaxe le projet 100% Open Source

#### Installation d'un Bitaxe et connexion à une "solopool"
#### Panorama des différentes Pool de mining
#### Découverte d'AxeOS 
#### Entretien de la machine 


### Partie 4 - Miner via sa propre pool de mining et construire ses propres templates de block

Enfin nous aborderons dans une dernière partie les moyens mis à la disposition des particuliers pour miner de manière aussi autonome que possble. En effet les pools de mining sont en fait des intermédaires, c'est à dire des tiers de confiance.

Un mineur souverain doit en effet être en mesure d'ajouter sa propre puissance de calcul au réseau de manière indépendante, sans dépendre de ces tiers. Nous verrons comment cela est possible même pour les débutant du mining.

Ce sera l'occasion de parler de Stratum v2 de Datum, et de l'applicatiopn Public Pool qui permettent un plus grand contrôle à l'utilisateur en lui permettant de s'affranchir en partie ou totalement du bon vouloir des pools de mining.

#### Pourquoi ? (Block Template / intermédiare etc...)
#### Public Pool sur Umbrel & Start 9
#### Stratum V2 & Datum


## 1.2 Rappel rapide sur la preuve de travail et le minage de Bitcoin


Commençons par rappeler succintement à quoi sert la **preuve de travail** et ce qu'on appelle communément le minage de Bitoin.
Pour rappel Bitcoin est un système de cash électronique pair-à-pair. C'est à dire qu'il ne repose sur aucune entité centrale pour fonctionner. Il s'agit en fait d'un réseau d'ordinateur stockant le grand livre de compte et l'historique des transactions et des balances de chacun des utilisateurs du réseau.

![Image](assets/fr/001.webp)

### Le problème de la double dépense

Habituellement dans les sytèmes d'échanges électroniques traditionnels, une entité (banque, banque centrale etc....) est chargée de débiter et créditer les comptes des utilisateurs en fonction des transactions effectuées par ces derniers. Ces banques permettent de remédier au problème de la double dépense que posent les systèmes électroniques, au sein desquels les données peuvent être dupliquées facilement. Quand un utilisateur dépense ses sous, la banque s'assure que son compte est bien débité, et que le compte du destinataire est bien crédité et qu'ainsi aucune monnaie supplémentaire n'est créée.

Ca c'est en théorie, puisqu'en pratique on sait que les banques commerciales et centrales ont bel et bien le pouvoir  de créer de la monnaie ex-nihilo, et qu'elles profitent de ce privilège pour s'approprier les ressources des autres indument.

![Image](assets/fr/002.webp)

Le génie de Satoshi Nakamoto est justement d'avoir réussi à trouver un moyen de se passer d'intermédiaire pour "débiter" et "créditer" les comptes des utilisateurs de Bitcoin. Et c'est là que la **preuve de travail** intervient. Personne n'est en mesure de pervertir le registre, car n'importe qui peut participer et controler ce qui y est inscrit. Tout le monde peut très facilement vérifier toutes les transactions qui s'y déroulent, les refuser si elles sont invalides (par exemple si la transaction dépense un bitcoin déjà dépensé précédemment), et même proposer de nouvelles transactions qui viendront mettre à jour le registre.

Dans Bitcoin pour éviter le spam et une croissance  de la base de donnée trop rapide, les transactions sont ajoutées au registre par bloc de taille limitée (max 4MB) toutes les 10 minutes en moyenne (cela représente généralement quelques milliers de transactions toutes les 10 minutes).
Mais alors qui choisit quelles transactions vont être ajoutées puisqu'on a décidé de se passer d'entité centrale ?
Certes tout le monde peut proposer un nouveau bloc de transactions, mais sous réserve qu'une **preuve de travail** suffisante ait été apportée. C'est là que les mineurs entre en jeu.

### La preuve de travail, pierre angulaire de la résolution du problème de la double dépense

Chaque mineur qui veut proposer un nouveau bloc et ainsi recevoir la récompense de bloc associée (contituée de la subvention de bloc  de 3,125 BTC  à l 'heure où est écrit ce cours, et des frais de transactions payés par les utilisateurs) peut le faire à condition d'avoir la preuve qu'un travail a été fournie. En somme il s'agit d'une sorte de compétition entre mineurs, chacun essayant de trouver une solution à un problème cryptographique que l'on ne détaillera pas ici. Ce qu'il faut retenir c'est que c'est par le biais ce concours, que l'on est en mesure de désigner qui est en droit d'ajouter le dernier bloc au "grand livre de compte" qu'on appelle "blockchain". Si quelqu'un cherchait à propager une transaction dépensant des Bitcoin déjà intégré au grand registre, les noeuds du réseau s'en rendraient compte et la considéreraient comme invalide.

Ainsi la **preuve de travail** est l'élément central du protocole Bitcoin permettant de désigner alternativement et en dehors de toute considération autre que l'énergie dépensée pour essayer de résoudre le problème le plus rapidement possible , qui sera en mesure de modifier le registre et de recevoir sa récompense.

![Image](assets/fr/003.webp)

### Noeuds mineurs & Noeuds non mineurs

Pour en terminer avec ces rappels thériques sur la fonctionnement du minage, il convient de savoir distinguer les principaux acteurs du réseau que sont les **noeuds mineurs** et les **noeuds non mineurs.**

Les noeuds **non mineurs**, sont simplement des utilisateurs du réseau, qui stockent le grand livre de compte, vérifient que les blocs ajoutés par les mineurs sont valides, et qui relaient les transactions d'autres noeud du réseau afin que celles-ci aient un chance d'atteindre un noeud mineur pour être ajoutée au registre. Un noeud non mineurs sert en quelque sorte de porte d'accès au réseau Bitcoin. Sans noeud vous ne pouvez pas diffuser de transactions sur le réseau, ni vérifier le solde de vos adresses et de votre wallet. En synthèse un noeud non mineur permet **d'utiliser** le réseau de manière souveraine.

Les **noeuds mineurs** quant à eux possèdent en plus une partie logicielle aditionnelle, leur permettant d'interragir avec des machines de minage qu'on appelle aujourd'hui **ASIC (Application Specific integrated Circuit)**. Ils sélectionnent les transactions qui les intéressent le plus, généralement celles qui payent le plus de frais et constituent des blocs. Puis ils proposent ces blocs candidats à la machine de minage qui essaye de résoudre le fameux problème cryptographique. Puis en cas de succès le noeud mineur propose le bloc et sa **preuve de travail** au réseau. En synthèse en noeud mineur permet de **faire fonctionner** le réseau.



## 1.3 Miner soit-même "à la maison" défis et solutions

### Une industrie du minage ultra compétitive

Une compétition acharnée a lieu depuis plus d'une décénnie désormais, entre des mineurs du monde entier, pour tenter de miner le plus de bitcoin possible, le tout en dépensant le moins d'énergie possible. En effet les machines **ASIC**  cherchent à réaliser le plus de calculs à la seconde, nécessitant une puissance électrique considérable. Le challenge pour un mineur est donc de toujours dépenser moins d'énergie que la valeur des bitcoins qu'il va générer. La chasse à l'énergie peu cher et à la rationnalisation des couts de maintenance et d'entretien des machines, a nécessairement conduit cette industrie à se professionaliser.

Aujourd'hui les mineurs professionnels ont accès à de l'énergie infiniment moins chère que des particuliers, prisonniers des prix parfois articificellement gonflés par les taxes qu'ils ont à payer, et la mauvaise gestion des réseaux de productions et de distributions en situation de monopoles. Les fermes de minage elles, négocient avec les fournisseurs d'électricité des prix extrèmement avantageux en monétisant les extra-capacités, c'est à dire en achetant à très bas prix (parfois négatifs !!!) de l'énergie qui serait autrement gaspillée par l'énergéticien.

![Image](assets/fr/004.webp)


Dans ce cadre, l'efficience atteinte par ces entité géantes est diabolique. C'est à dire que l'énergie nécessaire pour produire un hash cryptographique ne cesse de diminuer au fil du temps. On peut alors légitimement s'interroger sur la possibilité pour un  mineur non professionel, qui ne bénéficie pas de ces prix avantageux de l'énergie, de partciper au fonctionnement du réseau.

### Quelle place pour le minage des particuliers ?

En effet à quoi bon participer et essayer de miner si on dépense plus d'électrité que ce qu'on récupère en Bitcoin ?

Certains avanceront l'argument de l'**altruisme**. En effet si on veut éviter une centralisation des capacités de minages entre les mains de ces grandes entreprises qui peuvent être soumises facilement aux caprices des politiciens corrompus, il faut miner coûte que coûte. Ceci peut en effet être un sérieux vecteur d'attaque sur  Bitcoin, mais n'est ce pas comme essayer de vider un piscine olympique à la petit cuillère ?

D'autres vous dirons que miner est rentable si on se projette suffisamment loin dans le futur. En effet la théorie économique voudrait que la valeur de Bitcoin continue à augmenter pour peu que la croissance de la demande perdure. Mais si on est persuadé que la valeur de Bitcoin a vocation à augmenter, ne vaut-il pas mieux acheter directement du BTC plutôt qu'une machine de minage qu'on ne sera jamais certain d'ammortir ?

Quand bien même on aurait décider de miner coûte que coute est-ce vraiment réalisable à la maison ? Après-tout ces grosses machines sont extrèmement couteuses, bruyantes, difficiles à entretenir. La plupart d'entres-elle demandent en plus une telle puissance électrique que les prises domestiques ne peuvent tout simplement pas suivre. Alors est-ce possible pour un simple individu d'apporter se pierre à l'édifice en dehors de l'altruisme ou de la spéculation à long terme ?

![Image](assets/fr/005.webp)

Dans la partie suivante de ce cours nous verrons qu'il est effectivement possible pour des particuliers de se lancer dans le minage de Bitcoin, et que des solutions hardware et software existent déjà, permettant aux individus quelques soit leurs sources de motivation (altruisme, curiosité, spéculation, et bien d'autres encore) ou leur compétences de participer au fonctionnement du coeur du réseau bitcoin.

On verra même que dans certains cas, miner à la maison peut présenter un certains nombre d'avantages ou d'oppotunité, voir être profitable  en fonction de sa situation personnelle, du climat et prix de l'électricité de la zone géographique sur laquelle on vit, par exemple:

- en hiver dans les pays où il est nécessaire de se chauffer, des machines ASIC ultra performantes mais modifiées pour être silencieuses et utilisables en intérieures en mode "plug & play" sont d'ores et déjà produites par certains constructeurs.
- utilisation des minis machines "ticket de loterie" consommant à peine 20W permettent de "jouer à la loterie bitcoin" en "solominant"avec des probabilité de jackpot bien supérieure aux loteries nationales.


# Pourquoi  et comment miner soit-même ?

## 2.1 Pourquoi miner en Pool (supprimer tout les ##)

### Qu'est ce qu'une pool de mining ?

Une **pool de minage** est un regroupement de mineurs qui mettent en commun leur puissance de calcul (hashrate) pour **travailler collectivement** à la recherche de blocs. En effet en tant que mineur  individuel, il est presque impossible de trouver un bloc par soi-même tant notre puissance de calcul est dérisoire comparée à celle de l'ensemble du réseau.

Ici, lorsqu'un des mineurs de la pool trouve un bloc, cette dernière reçoit la **récompense complète (3.125 25 BTC + les frais )**, puis la répartit entre ses membres, proportionnellement à leur contribution.

Cela **lisse les revenus** et **réduit la variance**, ce qui est vital pour les petits mineurs. 

![Image](assets/fr/007.webp)

### Pour des revenus réguliers et prévisibles

Sans cette association entre mineurs qui partagent la récompense lorsque l'un d'entre eux trouve un bloc, un mineur isolé pourrait miner des années sans rien trouver. En rejoignant une pool, les paiements sont réguliers , et prévisibles. La pool demande à chaque mineur du groupe de soumettre des preuvent de travail partielles appelées "shares" , puis attribut

Cela **réduit la variance** : au lieu de tout miser sur une "loterie" où les chances de miner un bloc seul sont infimes , on obtient  des fractions de BTC régulièrement, quotidiennement ou hebdomadairement, en fonction de son hashrate. 

## 2.2 Pourquoi faire du solo mining

Le **solo mining** (ou minage en solo) consiste à miner  **sans passer par un pool**. 

Aujourd'hui les solominer sont clairement extrèmement minoritaires, et sont majoritairement des particuliers qui le font par passion. On se rapporche là de la manière originelle de miner, à l'époque ou Satoshi Nakamoto, Hall Finey, et tous les 1ers Bitcoiners légendaires encaissaient 50 bitcoins toutes les 10 minutes par le seul travail de leur processeur de laptop.

Les professionnels ayant eux besoin de revenus réguliers pour palier à leurs obligations. Cependant comme on le verra ci-dessous, il y a de vraies raisons (techniques, idéologiques et stratégiques) qui peuvent motiver ce choix.

![Image](assets/fr/006.webp)

### Qu'est-ce que le solomining ?

On vient de voir que dans le minage en **pool**, on contribue à un effort collectif pour trouver le prochain bloc. On soumet  des “shares” et si le pool trouve un bloc, la récompense (3,125 BTC actuellement + les frais de transaction) est **répartie**  au pro-rata la puissance de chacun.

En **solo mining**, il est soit possible de faire tourner son propre noeud et son propre logiciel de minage afin de miner de manière totalement souveraine.
Ou bien de passer par un service tiers, une sorte de proxy qu'on appellera "solo pool", et qui nous apportera la couche logicielle nécessaire à la construction des blocs et le noeud Bitcoin.

Quoi qu'il en soit cette fois-ci quand un mineur trouve un bloc, ce dernier garde **100 % de la récompense**. On peut également préciser que même lorsqu'on choisit le solomining, 2 approches sont possibles:

 **La première** consiste à déléguer à un tiers la responsabilité de connecter notre machine de minage au réseau Bitcoin en mettant à notre disposition un noeud Bitcoin, et le logiciel qui sert à contruire le block template sur lequel va travailler notre machine. Ce tiers prélèvera la plupart du temps des frais pour le service rendu, et est un source de confiance avec des risques de censure ou pourquoi pas de malhonnêteté (le manager de la "solopool" peut théoriquement tenter de tricher et s'auto attribuer la récompense de block si le miner n'est pas attentif.
 

![Image](assets/fr/007.webp)

**La seconde** consiste pour chaque solominer à auto héberer sur un serveur qui lui appartient le noeud bitcoin et le logiciel de minage qui lui permet de sélectionner lui même les transactions qu'il veut inclure dans sont bloc, et de construire soit-même le block template. C'est la manière la plus souveraine de faire du solomining et aujourd'hui les miniserveurs personnels comme Umbrel ou Start9 bien connus des bitoiners, permettent de facilement choisir cette option si on le désire.

![Image](assets/fr/008.webp)



Mais évidemment, quelque soit notre manière de procéder, les chances de succès sont **extrêmement faibles** pour un solominer à la maison avec une puissance de calcul modeste.

Pouquoi diable choisir le solomining alors ?

### Pour la souveraineté et l’indépendance

Si tu le souhaites, tu **n’as besoin de faire confiance à personne** : ni à un pool, ni à un intermédiaire.
Tes blocs (potentiels) et les transactions qui le constituent sont directement soumis à ton propre nœud et ne  sont pas filtrées. En effet une grande pool de mining (solo ou pas) soumise à la régulation pourrait être contrainte de censurer les transactions "non conformes" c'est à dire qui ne plaisent pas au pouvoir politique local.
En solominant, et dans l'hypothèse ou suffisamment de mineurs autour du monde font de même, on pourrait s'assurer qu'aucune censure n'est possible sur bitcoin puisqu'au moins un bloc par jour par exemple, pourrait être miné par un individus souverain.

On participe ainsi à la **décentralisation du  hasrate**, et chaque mineur indépendant renforce la résilience face à la censure ou à la centralisation des pools. En solo mining, **on devient totalement souverain.**

### Pour la confidentialité 

Vous n'avez pas à partager vos données de minage (comme votre hashrate ou vos adresses bitcoin ou même votre adresse IP) avec un opérateur de pool tiers, ce qui préserve votre vie privée. De plus, vous avez un contrôle absolu sur votre configuration, sans risque de censure ou de manipulation par un pool (par exemple, en cas de fork ou de politique interne).

### Pour l’expérimentation et l’apprentissage

C’est une excellente manière de **comprendre Bitcoin techniquement**, notamment :comment fonctionne la propagation des blocs. la communication avec un nœud complet . la logique du Proof-of-Work.Les petits mineurs (avec un Bitaxe, un Antminer, etc.) utilisent souvent le solo mining **à titre pédagogique**.

### Pour la loterie 

Trouver un bloc, même avec du matériel modeste, c’est **comme gagner au loto**. La récompense actuelle est de 3,125 BTC + frais, mais comme on le verra plus tard, même avec une machine peu puissante et accessible financièrement, qui tourne en permanance dans notre salon , les chances de gagner sont tout de même supérieures à celles d'une loterie traditionelle.

Probabilité faible, mais gain énorme — surtout quand on fait tourner la machine pour le plaisir et non pour le profit.
Par exemple si 1 millions de Bitaxes (petites machines de mining) dont on estime qu'aujourd'hui déjà des centaines de milliers sont en service) minaient en solo, cela représenterait au jour ou ce paragraphe est écrit, environ 1 Eh/s soit 1/1000 du hashrate total. De quoi miner un bloc par semaine. Un ticket de loto par semaine gagné par un individu quelque part dans le monde, de quoi changer une vie.

En synthèse et quelque soit la raison qui pousse un individu à solominer, il s'agit là de se reconnecter à la vision originelle de Satoshi où n'importe quel utilisateur du réseau participait à renforcer la sécurité et la décentralisation de celui-ci via un système d'incitations bien alignées. Même un mineur uniquement interessé par l'aspect loterie du minage de bitcoin devient un maillon important du réseau. En effet les petits ruisseaux faisant les grandes rivières, une généralisaiton de ce type de comportement pourrait aider de manière substancielles au retour d'une partie significative du hashrate entre les mains des particuliers.

| Feature          | Solomining                                                                         | Pool Mining                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Rewards          | Whole Block Reward                                                                 | Shared reward based on hashrate contribution among the pool                        |
| Payment term     | Extremely rare, you  may never be rewarded at all especially as a small home miner | Regular payments are received, ideal for those who have access to cheap electricty |
| Sovereignty      | Can be total                                                                       | A third party decides which txs to include and can censor                          |
| Fees             | Can be zero                                                                        | A % of the block reward is take by the pool                                        |
| Setup Complexity | A bit harder for those who seek total sovereignty                                  | Easy                                                                               |


## 2.3 Panorama des solutions hardware

Nous allons dans ce paragraphe détailler une partie (nonexhaustive) des solutions matérielles qui s'offrent à vous pour miner à la maison. Les machines que nous présenterons sont "plug & play" et adaptée à un usage domestique, et peuve même tourner dans votre salon.

En effet les machines ASIC "professionelles" qui sont destinées à être installées sur rack dans des conteneurs ou datacenter, sont beaucoup trop bruyants et puissantes pour être utilisée en intérieur.
Ici certaines des machines présentées sont même marketées par leur fabriquant comme des radiateurs, à installer dans les pièces de votre maison en hiver pour vous chauffer.



### Bitaxe - Le projet 100% Open Source

![Image](assets/fr/010.webp)

Le projet Bitaxe est né du constat que la centralisation du minage tant au niveau des pool de minage que de fabricants de machines pouvait à terme causer un problème pour Bitcoin. Il était temps de tenter de reprendre un peu de contrôle sur cet aspect fondamental du projet qu'est le mining.

Le problème c'est que les puces ASIC qui sont ensuite assemblées par centaines au sein des grosses machines que nous connaissons bien et qu'on retrouve dans les ferme de mining) ne sont pas vendues au détail par leurs fabricants pour être utilisée par qui le veut. Par exemple Bitmain, le plus gros constructeur de machine ASIC du monde, réserve précieusement ses propres puces ASIC à ses propres machines (les fameux Antminer). Et c'est également le cas pour tous les autres fabricants.

Comment faire pour proposer une solution Open Source dans ces conditions. Tout simplement en achetant des machines Antminer complètes, en les désossant, et un déssoudant les puces ASIC, pour les réhabiliter et leur donner une seconde vie au sein du projet de mining open source le plus célèbre de l'écosystème Bitcoin: **[Bitaxe](https://github.com/bitaxeorg)**

Cerise sur le gateau l'ensemble du projet est 100% open source, tant au niveau du hardware que du software. N'importe qui peut donc s'approvisionner en composants et construire sont propre appareil rendant le projet quasiment inarétable. Dans la pratique les particuliers se fournissent auprès de constructeurs (autrement dit des geeks bricoleurs) spécialisés répartis autour du monde, plutôt que de se munir des pièces et de son faire à souder pour le fabriquer soit-même.

Au moment où ces lignes sont écrites, la version la plus performante du projet Bitaxe est le Bitaxe Gamma, propulsée par une puce Bitmain BM1370, et délivrant environ 1,2 Th/s de hashrate, pour moins de 20W de consommation.

Vous pouvez par exemple vous procurer le votre si vous êtes en europe chez [Bitcoin Bazar](https://bitcoinbazar.fr/en/collections/home-mining), Silexperience, ou encore PlebStyle. 

![Image](assets/fr/011.webp)

### NerdQAxe++

Le projet Bitaxe a très rapidement fait des émules et de nombreuses évolutions de celui-ci on vu le jour.
Les QAxe sont une sous famille de Bitaxe qui présentent sur un seule carte PCB non pas une puce ASIC mais 4 d'où le "Q".

![Image](assets/fr/012.webp)

Les NerdQAxe sont un sous-ensemble de la famille QAxe présentant un écran écran plus grand qu'un Bitaxe traditionnel (ESP32 Lilygo display), pour une meilleure expérience utilisateur.
Les "++" siginfient que les 4 puces ASIC installées sont les dernières et plus performantes disponibles sur le marché à date (4 x BM1370). Ainsi et sans grande surprise on obtient environs 5Th/s de hashrate pour moins de 80W de consommation électrique.

![Image](assets/fr/013.webp)

Mais le firmware (le logiciel qui tourne sur l'appareil) utilisé est fondalement celui du projet racine Bitaxe. Il est il me semble utile de mentionner cette variante pour porter à la connaissance de  ceux qui auraient envie de plus de puissance, tout en gardant l'esprit totalement open source et transparent. Mais bien d'autre dérivés sont disponibles qu'on ne pourra pas détailler ici.

### Braiins BMM101

![Image](assets/fr/014.webp)

https://www.youtube.com/watch?v=QXonFfguymw

Cet appareil proposé par la société Braiins est un "Home Miner" vendu sans équivoque comme un ticket de loterie. Le but est placer la machine dans votre pièce à vivre, de profiter de son silence remarcable et de l'oublier. Il ne s'agit pas vraiment d'obtenir une quelconque rentabilité, mais de tenter sa chance en essayant d'être le prochain mineur qui fournira la preuve de travail nécessaire pour miner un bloc.  Braiins la société qui le fabrique est une référence dans l'écosystème bitcoin, connue pour fournir des solutions de mining en pool depuis 2010 et toujours en activité aujourd'hui et que l'on présentera plus tard dans notre panorama des pool de mining.

![Image](assets/fr/015.webp)

En synthèse cet appareil au design soigné vous permettra de déployer un hasrate de 1 Th/s pour 35/40 W de consommation électrique, le tout avec un bruit réduit de 40 dB.  Le design est soigné, le grand écran permettant d'afficher les informations importantes concernant l'appareil mais aussi le réseau Bitcoin  et même plus.

![Image](assets/fr/016.webp)

![Image](assets/fr/017.webp)

### La Gamma Avalon Home de Cannan

![Image](assets/fr/018.webp)

Canaan est une entreprise Singapourienne et un des 3 plus grands constructeurs de machines de minages et de puces ASIC au monde, au côté de l'indétronable Bitmain et de MicroBT.
Ils développent une gamme de produits s'adressant aux particuliers qui voudraient miner à la maison tout en utilisant l'énergie dissipée par l'équipement pour chauffer son logement, plutôt que d'évacuer cette chaleur comme le font habituellement les mineurs professionnels.

Le défit est donc de faire entrer dans les foyers des machines suffisament puissantes pour chauffer une potentiellement une pièce entière, tout en garantissant un niveau de bruit minimal des ventilateurs pour ne par perturber la vie quotidienne de l'utilisateur. La gamme de produits "Avalon Home" de Canaan que nous présenterons ci-après relève ce défit avec brio. 

#### Avalon Nano 3S

L'Avalon Nano 3S est l'équipement le moins puissant mais le plus compact de cette gamme de produits, présenté comme un chauffage d'appoint. Il vous sera utile posé sur un bureau pour vous réchauffer les doigts en hiver dans votre pièce mal isolée et non chauffée. Mais en aucun cas suffisant pour chauffer ne serait-ce qu'une petite pièce.

![Image](assets/fr/019.webp)


Cette petite boite d'envrion 20 cm par 11 cm et de seulement 1kg  (L205mm x W115mm x H58.5mm exactement )  délivre  un impressionnant 6Th/s de Hashrate (grace à 12 puces ASIC maison) pour seulement 140W de consommation. Il fonctionne en WIFI même si il existe des moyen de le connecter au LAN via un adaptateur USB-RJ45. Plutôt silencieux également puisque fonctionnant sur une plage de bruit entre 30 et 40dB.

![Image](assets/fr/021.webp)

Tous les appareils de la gamme sont pilotables et configurables  de manière plutôt ludique via l'application "Avalon Family" disponible via votre store d'application favori. Vous pourrez le régler selon 3 mode de puissance.


![Image](assets/fr/020.webp)

Un tutoriel détaillé pour apprendre comment le configurer est disponible ic: https://planb.academy/fr/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

S'il s'agit de vous en procurer une unité, Bitcoin Bazar petite boutique physique située à Paris entièrement dédiée à Bitcoin, en vend au côté de tout l'attirail du Bitcoiner souverain: https://bitcoinbazar.fr/en/products/avalon-nano-3s

### Avalon Mini 3

Le Avalon Mini 3 quant à lui nous fait passer à la vitresse supérieure en nous proposant jusqu'à 40Th/S pour 800 W de consommation électriquen (66 puces maison Canaan). Le format de l'appareil fait vraiment penser à celui d'un radiateur, et le silence est là encore au rendez-vous. Suffisant pour chauffer une petite pièce d'environ 20/30m2.


![Image](assets/fr/022.webp)

Les dimensions sont un peu plus supérieures à ce que le Nano 3S vu au dessus propose évidemment, mais restent raisonnables avec 75 cm de longueur pour en encombrement réduit (L760mm x W104mm x H214.5mm (Net)) et un poid d'environ 8 kg. Celles d'un radiateur classique en somme. 
La connectivité est assurée par le WIFI (possibilité optionnelle d'utiliser du RJ45 via adaptateur). Le bruit est là encore extrèmement bien géré pour un appareil de cette puissance (entre 35dB et 55dB suivant les modes de fonctionnement).

![Image](assets/fr/023.webp)
L'application Avalon Family vous permet ici aussi de configurer et piloter l'appareil. 2 mode de fonctionnement sont proposés:
- Chauffage (bruit réduit mais perfrmance un peu en deça du maximum)
- Mining (on pousse l'appareil au maximum mais les ventilateur poussent un peu plus pour refroidir les puces générant plus de bruit)

Un tutoriel pour vous aider à paramétrer l'appareil est également disponible sur le site de l'academy: https://planb.academy/fr/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://bitcoinbazar.fr/en/products/avalon-mini-3

### Avalon Q

Le Avalon Q est l'appareil le plus puissant de la gamme. Il équivaut en terme de hashrate et de puissance à 2 Avalon Mini 3 très exactement 90 Th/s pour 1700W (grace à 160 puce ASIC Canaan) , le tout avec l'allure d'une unité centrale de vieux PC des années 2000.

![Image](assets/fr/025.webp)
Cette impressionante machine se rapproche en terme performance de ce que proposent certaines machines professionelles, mais l'encombrement  (L455mm x W130.5mm x H440mm) et le niveau sonore (45 ~ 65 dB) sont de nouveau si bien gérés que l'appareil trouvera une place de choix dans votre salon et sera en mesure de chauffer une grande pièce de 40 m2.


![Image](assets/fr/026.webp)

De nouveau, l'application Avalon Family permet le pilotage, et la connectivité s'effectue en WIFI avec possibilité de connexion au LAN en RJ45 avec un adaptateur. 

https://bitcoinbazar.fr/en/products/avalon-q

## 2.4 Panorama des solutions software

Lorsqu'il s'agit de matériel de minage, le logiciel installé sur l'appareil  est appelé "firmware". Ce logiciel se compose en synthèse de l'OS (Operating System) de l'appareil, du logiciel de minage, et de l'interface web / application mobile, qui vous permettra d'interagir facilement avec votre miner depuis un navigateur d'ordinateur classique, ou votre smartphone.

Nous présenterons ici un aperçu non exhaustif de certains de ces logiciels en s'attardant davantage sur les machines qui font l'objet de cette formation, c'est à dire celles que nous instrallerons à la maison.

Aujourd'hui les machines de minage sont livrées avec un firmware préinstallé par le fabricant, vous épargnant de devoir choisir quoi installer que ce soit pour les machines traditionnelles de Bitmain, MicroBT, et Canaan mais également dans notre cas de machine de Home Mining à l'attention de particuliers.

Sachez cependant qu'il est  possible dans certains cas de remplacer le firmware du  constructeur par un autre si on le souhaite, pour bénéficier des certaines fonctionnalitées par exemple.

C'est le cas de Braiins OS qui peut se subtituer au firmware de base des appareils Antminer de Bitmain par exemple. On présentera rapidement l'OS dans le paragraphe suivant puisque que c'est l'OS qui équipe notre appareil Braiins BMM101 présenté plus haut, et qu'elle présente des caractéristiques et fonctionnalitées interessantes.

### Braiins OS


### AxeOS & Esp-Miner


### Avalon Family App





# Installer et configurer son premier mineur personnel

## 3.1 Mise en perspective et ordres de grandeurs

Dans ce paragraphe  nous entrons dans la pratique. Nous verrons comment paramétrer un Bitaxe Gamma 601 et le connecter à une pool de mining.

Pour ceux qui auraient opté pour des appareils de la gamme Avalon de Canaan, vous trouverez des tutoriels disponibles ci-dessous:

https://planb.academy/fr/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/fr/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/fr/tutorials/mining/hardware/braiins-mini-miner-f5aec001-fb05-4e89-b3b2-a31abec1253c

Pour rappel un Bitaxe Gamma fournit un hashrate d'environ 1,2 Th/s. C'est à la fois énorme et minuscule. Enorme car une seule de ces petites machines est désormais plus puissante et immensément plus efficiente que les machines les plus performates d'il y 10 ans. Minuscule car en branchant un Bitaxe, vous ne représentez qu'un milliardième du hashrate mondial atuel (évalué à environ 1 Zetahash par seconde au moment où ces lignes sont écrites).

Cela étant dit il va nous falloir décider comment allouer notre hasrate de la manière la plus "smart" possible. En simple est-il plus malin de miner en pool, ou de solominer avec un Bitaxe ?

**Bitaxe en pool**: avec 1,2 Th/s un Bitaxe vous permettrait au moment où sont écrites ces lignes de générer 4 centimes de dollars par jours de bitcoin, sans compter la dépense énergétique qui dépendra de chacun et qui pour la majorité d'entre nous sera supérieure à la récompense. En dehors du fait d'obtenir quelques sats non KYC, l'intérêt est très limité. C'est pour quoi les Bitaxes sont utilisés dans leur écrasante majorité comme des tickets de lotterie.

![Image](assets/fr/027.webp)

**Bitaxe en solomining:

Mais alors s'il s'agit de jouer à la lotterie Bitcoin, quelles sont nos chances de tirer le gros et de gagner les 3,125 bitcoins + frais de la récompense de block allouée à chaque mineur chanceux ?

Comme on vient de le voir un peu plus haut un Bitaxe seul, c'est 1 / 1000 000 000 de la puissance de calcul globale déployée sur terre. Est-ce à dire que notre chance de trouver un block est de 1 sur 1 milliard ? Ce serait le cas si on essayait une seule fois de miner un block, c'est à dire qu'on allumerait notre appareil pendant les 10 prochaines minutes en croisant les doigts, jusqu'au prochian bloc miné. Là effectivement nos chances seraient de 1 sur 1 milliard.

Mais la beauté de Bitcoin, c'est qu'un nouveau bloc est miné toutes les 10 minutes environ, ce qui nous permet de jouer à la lotterie Bitcoin environ 144 fois par jour. Et ça ça change beaucoup de choses en terme de statistiques, car ça n'étonnera personne: plus on jour, plus on a de chance de gagner.

Alors quelles sont nos chances exactement ? Des sites existent ([solochance.com](https://solochance.com/) ou [sololuck.com](https://www.sololuck.com/)) nous permettant de calculer cela (même si le calcul n'est aps très compliqué en soit), qui varient légèrement en fonction de leur appréciation du hashrate global et autres paramètres.

![Image](assets/fr/028.webp)

![Image](assets/fr/029.webp)


Cela permet quand même de se rendre compte des ordres de grandeurs dont nous parlons.

| Bitaxe Gamma (1.2 Th/s) 15th of December 2025 | Duration of mining activity | Number of tries | Chance of hitting a block |
| --------------------------------------------- | --------------------------- | --------------- | ------------------------- |
|                                               | 1 block                     | 1               | 1/1000 000 000            |
|                                               | 1 day                       | 144             | 1 / 6000 000              |
|                                               | 1 year                      | 53560           | 1/ 18 000                 |

Ainsi pour résumer, laisser son Bitaxe Gamma touner toute l'année, revient à effectuer  une fois par an, un tirage au sort avec 1 chance sur 18000 de gagner le jackpot.

Mais dans les faits, est-ce que nous avons des exemples de solominers ayant trouvé un blocs et empocher la récompense ?
Eh bien oui, il suffit pour se faire une idée de suivre l'actualité du solomining sur les réseaux sociaux (X principalement), pour s'en convaincre. Régulièrement, une ou deux fois par moins en 2025, des heureux gagnants sont repérés.

![Image](assets/fr/042.webp)

![Image](assets/fr/043.webp)

Si l'on veut un  moyen non exhaustif mais assez fiable d'avoir une idée du nombre de "solo blocs" trouvés, alors il nous faut tout simplement observer les blocs minés par la pus grande solo pool du monde "Solo CkPool": https://mempool.space/mining/pool/solock

On remarque alors qu'environ 1 bloc par mois est trouvé par un miner solo via cette pool. Cependant il est à noté qu'un mineur solo peut tout aussi bien être un Bitaxe dans un salon, qu'un mineur  professionel possédant des dizaines de machines dernier cri.

![Image](assets/fr/044.webp)

Dernière remarque, mais il est à noter que certain chanceux ont eux déjà réussi à miner des blocs sur des pool [auto hébergées sur leur propre serveur Umbrel](https://mempool.space/mining/pool/publicpool). Le meilleur moyen de miner selon moi, comme le faisaient les mineurs des origines, sans dépendre de personne. Et aujourd'hui, c'est à la portée de n'importe qui. On reviendra dans le dernier paragraphe de cette formation sur les applications permettant de miner en tout autonomie et en quelques clics.

![Image](assets/fr/045.webp)

## 3.2 Installation d'un Bitaxe et connexion à une "solopool"

Entrons dans le dur du sujet désormais et installons notre 1er Bitaxe.

Après l'avoir mis sous tention, des indications apparaissent sur son petit écran. Il vous faudra vous munir de votre smartphone ou de votre ordinateur pour aller rechercher dans les paramètres WI-FI l'appareil répondant au nom de **Bitaxe_E25D**. Bien sur ce nom sera différent dans votre cas.

![Image](assets/fr/030.webp)

Une fois que vous aurez cliquez sur le nom de l'appareil , une oage web s'ouvrira automatiquement en vous demandant de renseigner:

- le nom de l'appareil tel qu'il appaitra sur votre réseau local (livre à vous de chosir celui qui vous convient)
- votre Wi-Fi SSID, c'est à dire le nom du réseau Wi-Fi de votre routeur, ici Livebox-43A0.
- Le mot de passe Wi-Fi permettant de se connecter à votre réseau local en Wi-Fi


![Image](assets/fr/031.webp)

Une fois les champs complétés, cliquez sur "Save", puis "Restart".

![Image](assets/fr/032.webp)


L'appareil redémarre, et est désormais connecté à votre réseau local. Une adresse IP lui a donc été attribuée qu'il nous conviendra de déterminer car c'est grace à cet identifiant que l'on pourra interagir avec l'appareil.

![Image](assets/fr/033.webp)

Avec les Bitaxes l'adresse IP est très facile à trouver puisqu'elle s'affiche sur l'écran de l'appareil tout simplement, comme indiqué ci_dessous:

![Image](assets/fr/034.webp)

![Image](assets/fr/035.webp)

Ainsi l'adresse IP attribuée à notre Bitaxe 601 est "192.168.1.21".
En tapant cette adresse dans notre navigateur favori, on arrive sur l'interface d'AxeOS qui pilote l'appareil et qui va nous permettre de le connecter à une la pool de minage de notre choix, entre autre.


![Image](assets/fr/036.webp)

Allons configurer maintenant la solopool de minage vers laquelle nous allons pointer notre hashrate. 
Pour rappel cette pool est chargée de nous donner un accès au réseau Bitcoin, de sélectionner les transactions à inclure dans le bloc sur lequel nous travaillons, et de diffuser notre bloc valide sur le réseau Bitcoin, dans le cas où nous serions chanceux.

**NB: Lorsque vous initialisez pour la première fois votre Bitaxe, des pools et adresses bitcoins sont déjà renseignées par défaut, mais il faut les remplacer autrement vous minerez pour quelqu'un d'autre si vous ne faites rien.

**La pool renseignée par défaut est Public Pool (Public Pool est un pool au code open source et ouvert, sans frai et conçu pour les petits mineurs comme le Bitaxe.  L'adresse par défaut est celle de l'OSMU l'oraganisation responsable du développement du projet Bitaxe****

Ce tutoriel est réalisé sous la version v 2.11.0 d'Axe OS. Il est  possible que les menus soient sensiblement différents suivant la version de l'OS qui flashé sur votre appareil au moment où vous le configurerez. 

Cliquons via le menu de gauche sur "Pool".

Il nous est donné la possibilité de renseigner 2 pool différentes ici, une principale et une pool de backup au cas où la première ait des problèmes, notre Bitaxe basculera alors automatiquement sur la pool de secours garantissant une continuité du service, maximisant ainsi vos chances de miner un bloc.

Pour chaque Pool les champs à renseigner sont:

- Stratum Host
- Stratum Port
- User
- Password

![Image](assets/fr/037.webp)

Nous choisissons en  pool principale Public Pool, une solo Pool très populaire chez les solominers, toujour en quête de son premier bloc miné malgré les quelques  40 Ph/s que des solominer du monde entier pointent vers elle.

On verra au pragraphe suivant qu'il existe de multiples services de solopool similaires à celui-ci, et qu'il convient de faire attention car ces fournisseurs de services restent des intermédiares  qui peuvent très bien être malhonnêtes.

En allant sur https://web.public-pool.io/#/ on nous indique les informations à renseigner dans les champs qui nous intéressent:

![Image](assets/fr/038.webp)

- Stratum Host: **stratum+tcp://public-pool.io** (ou simplement public-pool.io)
- Stratum Port: **3333**
- User: **"votre adresse bitcoin"."nom de votre appareil"** soit pour nous bc1qpqqf9f9xjfpnen2e4u3hs09sn6rvj386xk7zhgtuwm5pmlxwcuzq0v4fzm.bitaxePlanB
- Password: x (dans le protocole de minage stratum le mot de passe n'a pas d'importance dans la plupart des cas ce sera "x")

En solopool secondaire de backup, nous optons pour Ckpool, la plus grosse pool de solomining qui elle pour le coup a déjà miné de multiples blocs. Sur https://solo.ckpool.org/ on nous indique là aussi les champs à remplir dans l'interface de notre Bitaxe. Comme nous sommes située en Europe, nous choisissons le serveur européen pour bénéficier de meilleures performances.

![Image](assets/fr/039.webp)

- Stratum Host: **stratum+tcp://eusolo.ckpool.org** (ou simplement eusolo.ckpool.org)
- Stratum Port: **3333**
- User: **"votre adresse bitcoin"."nom de votre appareil"** soit pour nous bc1qpqqf9f9xjfpnen2e4u3hs09sn6rvj386xk7zhgtuwm5pmlxwcuzq0v4fzm.bitaxePlanB
- Password: "x" là encore.

Lorsque tout cela est fait, il suffit de cliquer sur "Save" puis "Restart" en bas de l'écran dans AxeOS pour que notre hasrate pointe effectivement vers les pools que nous venons de choisir et que le solomining commence !

Allons maintenant vérifier que Public Pool détecte bien notre hashrate et que tous fonctionne correctement.

Pour ce faire rensignez simplement votre adresse dans le champ prévu à cette effet sur https://web.public-pool.io/#/. Votre adresse Bitcoin vous sert non seulement à recevoir les éventuelles récompense mais également à vous identifier en tant qu'entité minière. Il s'agit en quelque sort de votre identité du point de vue de la pool.

Cliquez ensuite sur le bouton "My Workers" pour visualiser l'ensemble des appareils liés à votre adresse que Public Pool détecte.


![Image](assets/fr/040.webp)

On voit bien ici notre Bitaxe, dénommé par le nom qu'on lui a attribué "bitaxePlanB".

Les informations affichées sont en synthèse:

- la difficulté totale du réseau, c'est à dire un nombre déterminé par le protocole et dont l'ajustement permet  l'émission régulière environ toute les 10 minutes, de nouveaux Bitcoin. Plus ce nombre est élevé, plus il sera difficile pour un mineur de "trouver un bloc". Ce nombre est ajusté tous les 2016 blocs soit environ toutes les 2 semaines pour faire varier la difficulté du minage à la hausse ou à la baisse. Ici la difficulté affichée est de 148,2 Téra.
- Notre meilleure difficulté personnelle sur la période d'activité du mineur: pour nous 92,77 M (millions). Autrement dit il nous faudra faire environ 1,5 millions de fois mieux pour trouver un bloc...
- Le hashrate global de 984 Eh/s
- La hauteur de bloc
- Les information en temps réel sur le hashrate de notre appareil tel que détecté par la pool

![Image](assets/fr/041.webp)

Nous sommes désormais parés, nous minons et participons à l'effort global et la décentralisation du hashrate tout en ayant une maigre chance d'être récompensé. Mission accomplie.

## 3.3 Panorama des différentes Pool de mining

Nous venons de voir dans le rapide tutoriel du paragraphe précédent, 2 solo pool que l'on peut choisir afin de connecter notre "hasheur" au réseau Bitcoin et lui permettre de miner.
Public Pool et CkPool sont en effet les 2 solutions les plus populaires du marché auprès des solominer mais elles sont loin d'être les seules.

Nous verrons dans ce paragraphe un panorama assez complet mais comme souvent non exhaustif des solutions qui s'offrent à nous, et des caractéristiques de chacune des solutions.

### Les solopools

#### [La plus grande et réputée: CkPool](https://solo.ckpool.org/)

CkPool est la solution de référence pour les solominer, fondée par une figure bien connue et presque légendaire de l'écosystème open source du mining Bitcoin: Con Kolivas alias [Dr-Ck (@ckpooldev) ](https://x.com/ckpooldev) sur les réseaux sociaux.
C'est la solopool qui a permis de miner le plus de solo blocs et de loin, notamment du à son ancienneté et à la réputation de son développeur.

Elle cumule aujourd'hui un hashrate total de 215 PH/s.

![Image](assets/fr/046.webp)

Elle prélève 2% de frais à chaque bloc trouvé en échange d'une confiance, d'une fiabilité et d'un "uptime" qui n'est plus à démontrer.

Ainsi si vous trouvez un bloc par l'intermédiaire de CkPool, la transaction coinbase créditera votre adresse, moins les 2% de frais comme on peut le constater ci-dessous pour le dernier bloc trouvé par CkPool.

![Image](assets/fr/047.webp)

#### [Le petit nouveau "Public Pool"](https://web.public-pool.io/#/)



| Type de Pool | Open Source | Frais |
| ------------ | ----------- | ----- |
|              |             |       |


## 3.4 Découverte d'AxeOS


# Miner via sa propre pool de mining 
## 4.1 Pourquoi ? (Block Template / intermédiare etc...)
## 4.2 Public Pool sur Umbrel & Start 9
## 4.3 Datum et Stratum V2



# Partie finale

PARTIE AUTOMATIQUE. NE RIEN NOTER ICI

## Avis & Notes


<isCourseReview>true</isCourseReview>

PARTIE AUTOMATIQUE. NE RIEN NOTER ICI


## Examen final


<isCourseExam>true</isCourseExam>

PARTIE AUTOMATIQUE. NE RIEN NOTER ICI



## Conclusion


<isCourseConclusion>true</isCourseConclusion>

PARTIE AUTOMATIQUE. NE RIEN NOTER ICI

