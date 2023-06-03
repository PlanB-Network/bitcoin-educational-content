---
name: Introduction théorique au Lightning Network
goal: Découvrir le Lightning Network sous l’angle technique. Comprendre comment sont créés les canaux de paiement, leurs mécanismes de sécurité ainsi que leurs fonctionnements en réseau.
objectives:
  - Le fonctionnement technique du réseau via l'ouverture et la fermeture de canaux
  - La gestion de la liquidité et les frais LNN
  - Comprendre les termes tels que HTLC, LNURL et UTXO
  - Comprendre que le lightniong Network est un réseau
  - L'utilisation théorique du Lightning Network
---

# Un voyage vers la deuxième couche de Bitcoin

Cette formation est un cours théorique sur le fonctionnement technique du Lightning Network.

Ici, je vous invite à découvrir la couche n°2 de Bitcoin. C’est une technologie innovante et très complexe, mais pleine de promesses. Ça sera une formation plus tech, il n’y aura pas de tutoriel ou de cas d’usage. Afin de comprendre au mieux cette formation, une bonne compréhension de Bitcoin est nécessaire. Ce cours peut s’accompagner de LN 102 qui est plus pratique.

Cette formation a été crée par Fanis Michalakis, merci à lui

+++

# Un voyage vers la deuxième couche de Bitcoin

## 1. Comprendre le Lightning Network

![Comprendre le lightning Network](https://youtu.be/PszWk046x-I)

### Le Réseau Lightning et les Canaux de Paiement

Le réseau Lightning est une infrastructure de paiement de deuxième couche, construite sur le réseau Bitcoin, qui permet des transactions rapides et peu coûteuses. Pour comprendre pleinement comment fonctionne le réseau Lightning, il est essentiel de comprendre ce que sont les canaux de paiement et comment ils fonctionnent.
Les Canaux de Paiement sur Lightning

Un canal de paiement sur Lightning est une sorte de "voie privée" entre deux utilisateurs, qui permet des transactions Bitcoin rapides et répétitives. Lorsqu'un canal est ouvert, il est doté d'une capacité fixe, qui est définie à l'avance par les utilisateurs. Cette capacité représente le montant maximum de Bitcoin qui peut être transmis dans le canal à un moment donné.

Les canaux de paiement sont bidirectionnels, ce qui signifie qu'ils ont deux "côtés". Par exemple, si Alice et Bob ouvrent un canal de paiement, Alice peut envoyer du Bitcoin à Bob et Bob peut envoyer du Bitcoin à Alice. Les transactions à l'intérieur du canal ne modifient pas la capacité totale du canal, mais elles modifient la répartition de cette capacité entre Alice et Bob.

Pour qu'une transaction soit possible dans un canal de paiement Lightning, l'utilisateur qui envoie les fonds doit disposer de suffisamment de Bitcoin de son côté du canal. Si Alice souhaite envoyer 1 Bitcoin à Bob par le biais de leur canal, elle doit avoir au moins 1 Bitcoin de son côté du canal.
Limites et Fonctionnement des Canaux de Paiement sur Lightning

Bien que la capacité d'un canal de paiement Lightning soit fixe, cela ne limite pas le nombre total de transactions ni le volume total de Bitcoin qui peut être transmis à travers le canal. Par exemple, si Alice et Bob ont un canal avec une capacité de 1 Bitcoin, ils peuvent effectuer des centaines de transactions de 0,01 Bitcoin ou des milliers de transactions de 0,001 Bitcoin, tant que la capacité totale du canal n'est pas dépassée à un moment donné.

En dépit de ces limites, les canaux de paiement Lightning sont un moyen efficace d'effectuer des transactions Bitcoin rapides et peu coûteuses. Ils permettent aux utilisateurs d'envoyer et de recevoir des Bitcoin sans avoir à payer des frais de transaction élevés ou à attendre de longues périodes de confirmation sur le réseau Bitcoin.

En résumé, les canaux de paiement sur Lightning offrent une solution puissante pour ceux qui souhaitent effectuer des transactions Bitcoin rapides et peu coûteuses. Cependant, il est essentiel de comprendre leur fonctionnement et leurs limites pour pouvoir en tirer pleinement parti.

        Exemple : – Alice a 100 000 SAT – Bob a 30 000 SAT C’est donc l’état actuel du canal. Lors d’une transaction, Alice décide d’envoyer 40 000 SAT à Bob. Elle peut car 40 000<100 000. Le nouvel état du canal est donc : – Alice 60 000 SAT – Bob 70 000 SAT Désormais, Bob souhaite envoyer 80 000 SAT à Alice. N’ayant pas la liquidité, il ne peut pas. La capacité maximum du canal est de 130 000 SAT, avec une possible dépense d’Alice de 60 000 et 70 000 pour Bob.

## 2. Bitcoin, adresses, UTXO et transactions

![bitcoin, adresses, utxo et transactions](https://youtu.be/cadCJ2V7zTg)

Dans ce second épisode, un peu hors série, nous prenons le temps d’étudier comment fonctionnent réellement les transactions Bitcoin, ce qui nous sera bien utile pour comprendre Lightning. Nous nous attardons aussi un instant sur la notion d’adresse multi-signature, qui est capitale pour comprendre le prochain épisode, qui sera consacré à l’ouverture de canaux sur le Lightning Network. – Clé privée > Clé publique > Adresse Lors d’une transaction, Alice envoie de l’argent à Bob. Ce dernier fournit une adresse donnée par sa clé publique. Alice qui a elle-même reçu l’argent sur une adresse via sa clé publique utilise désormais sa clé privée pour signer la transaction et ainsi débloquer les bitcoins de l’adresse. – Lors d’une transaction, dans Bitcoin tous les bitcoins doivent bouger. Nommé UTXO (Unspend Transaction Output), les bouts de bitcoin vont tous partir quitte à retourner après chez le propriétaire même :

        Alice a 0.002 BTC, Bob a 0 BTC Alice décide d’envoyer 0.0015 BTC à Bob. Elle va signer une transaction de 0.002 BTC où 0.0015 iront à Bob et 0.0005 retourneront dans son portefeuille.

Ici de une UTXO (Alice a 0.0002 BTC sur une adresse) nous avons donc créée 2 UTXO (Bob a 0.0015 et Alice a récupéré un nouvelle UTXO (indépendent du précedent) de 0.0005 BTC). – Dans Lightning Network, on utilise des multi-signatures. Il faut donc 2 signatures pour débloquer les fonds, à savoir deux clé privées pour déplacer l’argent. Cela peut donc être Alice et Bob qui, ensemble, doivent accepter de débloquer l’argent (l’UTXO). Dans LN précisément, ce sont des transactions 2/2 donc il faut absolument les 2 signatures contrairement au multi-signatures 2/3 ou 3/5 où il faut seulement une combinaison du nombre complet de clés.

## 3. Ouvrir un canal

![ouvrir un canal](https://youtu.be/B2caBC0Rxko)

Dans ce troisième épisode, nous nous penchons plus en détail sur l’ouverture de canal, et comment cette-dernière est effectuée au travers d’une transaction Bitcoin.

Le Lightning Network a différents niveaux de communication :

    Communication p2p (protocole Lightning Network )
    Canal de paiement (protocole Lightning Network
    Transaction Bitcoin (protocole Bitcoin)

Pour ouvrir un canal, les deux pairs parlent de communication :

    – Alice : “Salut je veux ouvrir un canal !
    – Bob : Ok, voici mon adresse publique.”

Alice a désormais 2 adresses publiques pour créer une adresse multi-sig 2/2. Elle peut maintenant faire une transaction bitcoin pour y envoyer de l’argent.

Alice va donc créer deux transactions :

– Envoi de ses 0.002 BTC vers 0.0013 de l’adresse multi sig et 0.0007 vers chez elle (retour des UTXO). Cette transaction n’est pas encore publique car si elle l’est à ce stade, elle fait confiance à Bob pour pouvoir débloquer l’argent du multi-sig.

Mais alors comment faire ?

Alice va créer une deuxième transaction dite « transaction de retrait » avant de publier le dépôt des fonds dans le multi-sig.

– La transaction de retrait va dépenser les fonds de l’adresse multi-sig vers une adresse à elle (ceci avant que tout soit publié).

Une fois les deux transactions construites, elle annonce à Bob que c’est fait et lui demande une signature avec sa clé publique en lui expliquant qu’ainsi, elle pourra récupérer ses fonds si quelque chose venait à mal se passer. Bob accepte car il n’est pas malhonnête.

Alice peut donc récupérer les fonds seule, elle a déjà la signature de Bob. Elle publie donc les transactions. Le canal est donc ouvert avec désormais 0.0013 BTC (130 000 SAT) du côté d’Alice.

## 4. Transaction Lightning & d’engagement

![trasanction lightning & transaction d'engagement](https://youtu.be/aPqI34tpypM)

Dans ce quatrième épisode, nous analysons ce qui se passe réellement en coulisse lorsqu’on transfert des fonds d’un côté à l’autre d’un canal sur le Lightning Network, avec notamment la notion de transaction d’engagement. La transaction de retrait/fermeture on-chain représente l’état du canal, ceci garantit à qui appartient les fonds après chaque transfert. Donc après un transfert Lightning Network, il y a une mise à jour de cette transaction/contact non réalisé entre les deux pairs, Alice et Bob créent donc une même transaction avec l’état du canal actuel au cas où il a une fermeture :

    Alice crée un canal avec Bob – 130 000 de son côté. La transaction de retrait acceptée par les deux en cas de fermeture dit que 130 000 iront chez Alice à la fermeture, Bob est d’accord car c’est juste.
    Alice envoie 30 000 à Bob. Il y a donc une nouvelle transaction de retrait qui dit qu’en cas de fermeture, Alice touchera 100 000 et Bob 30 000. Les deux sont d’accord car c’est juste.
    Alice envoie 10 000 SAT à Bob, une nouvelle transaction de retrait est à nouveau créée pour dire qu’Alice récupère 90 000 et Bob 40 000. Les deux sont d’accord car c’est juste.

L’argent ne bouge donc jamais mais la balance finale s’actualise via une transaction signée mais non publiée on-chain. La transaction de retrait est donc une transaction d’engagement. Les transferts de satoshis sont une autre transaction d’engagement plus récente qui actualise la balance.

## 5. Transactions, deuxième partie

![transactions partie 2](https://youtu.be/RRvoVTLRJ84)

Si les transactions d’engagement dictent un état du canal avec la liquidité au moment X, peut-on tricher en publiant une ancienne et donc un ancien état ? La réponse est oui car on a déjà la pré signature des deux participants dans la transaction non publiée.

Pour résoudre ce problème on va rajouter de la complexité :

    Timelock = fonds bloqués jusqu’au bloc N
    Clé de révocation = secret Alice et secret Bob

C’est deux éléments sont rajoutés à la transaction d’engagement. Du coup, Alice doit forcément attendre la fin du Timelock, et toute personne qui détient la clé de révocation peut déplacer les fonds sans attendre la fin du Timelock. Si Alice essaie de tricher, Bob utilise la clé de révocation pour voler et punir Alice.

Désormais (et en réalité) la transaction d’engagement n’est pas la même pour Alice et Bob, ils sont symétriques mais chacun avec des contraintes différentes, ils se donnent mutuellement leur secret afin de créer la clé de révocation de la transaction d’engagement précédente. Donc à la création :

    Alice crée le canal avec Bob, 130 000 de son coté, elle a un Timelock qui l’empêche de recouper immédiatement son argent, elle doit attendre un peu. La clé de révocation peut débloquer l’argent mais seul Alice l’a (transaction d’engagement d’Alice)

    Une fois qu’il y a un transfert, Alice va fournir son ancien secret à Bob et donc ce dernier pourra en cas de triche vider le canal à l’état précédent au cas ou Alice essaie de tricher (Alice est donc punie). De la même façon, Bob va fournir son secret à Alice. Pour que s’il essaie de tricher Alice puisse le punir.

L’opération se répète à chaque nouvelle transaction d’engagement. Un nouveau secret est décidé et une nouvelle clé de révocation. Donc pour chaque nouvelle transaction, il faut détruire la transaction d’engagement précédente en donnant le secret de révocation. Ainsi si Alice ou Bob essaie de tricher, l’autre peut agir avant (grâce du Timelock) et donc éviter une triche.

Lors de la transaction n°3, on donne donc le secret de la transaction n°2 pour permettre à Alice et Bob de pouvoir se défendre face à Alice ou Bob.

La personne qui crée la transaction avec le Timelock (celui qui envoie l’argent) peut utiliser la clé de révocation uniquement après le Timelock. Cependant la personne qui reçoit l’argent, peut l’utiliser avant le Timelock en cas de triche d‘un côté à l’autre d’un canal sur le Lightning Network. En particulier, nous passons en détail les mécanismes qui permettent de se prémunir d’une éventuelle tricherie de la part de son pair au sein du canal.

## 6. Fermer un canal

![fermer un canal](https://youtu.be/FVmQvNpVW8Y)

Dans ce sixième épisode, nous nous intéressons à la fermeture de canal au travers d’une transaction Bitcoin, pouvant prendre différentes formes suivant les cas. Il existe 3 types de fermeture de canal :

    Le bon : fermeture coopérative
    La brute : fermeture forcée (non coopérative)
    Le truand : fermeture par un tricheur

Le bon : Les deux pairs se parlent et acceptent de fermer le canal. Ils arrêtent donc toutes les transactions et valident un état final du canal. Ils se mettent d’accord sur les frais de réseaux (la personne qui ouvre le canal paie les frais de fermeture). Ils créent désormais la transaction de fermeture. Il y a donc une transaction de fermeture, différente des transactions d’engagement car il n’y a pas de Timelock et de clé de révocation. La transaction est donc publiée et Alice et Bob touchent leurs soldes respectifs. Ce type de fermeture est rapide (car pas de Timelock) et peu coûteuse en général. La brute : Alice veut fermer le canal, elle communique mais Bob ne répond car il est hors ligne (coupure internet ou électricité). Alice va donc publier la transaction d’engagement la plus récente (la dernière). La transaction est donc publiée et le Timelock s’active. Alors, les frais ont été décidé lors de la création de cette transaction il y a X temps dans le passé ! La MemPool est le réseau ayant changés depuis, le protocole utilise par défaut des frais 5 fois supérieurs à ceux actuels lors de la création de la transaction. Création frais à 10 SAT donc la transaction a considéré 50. Au moment de publier de façon forcée, la transaction de clôture le réseau est à :

    1 SAT = surpayé par 50*
    100 SAT = sous payé par 2*

Ceci rend donc la fermeture forcée plus longue (Timelock) et surtout plus hasardeuse ne terme de frais et donc possible validation par les mineurs. Le truand : Alice essaie de tricher en publiant une ancienne transaction d‘engagement. Mais Bob surveille la MemPool et guette s’il y a des transactions qui essaient d’en publier des anciennes. S’il en trouve, il utilise la clé de révocation pour punir Alice et prendre tous les SAT du canal.

## 7. Lightning le Réseau

![lighting le réseau](https://youtu.be/RAZAa3v41DM)

Dans ce septième épisode, nous étudions le fonctionnement de Lightning en tant que réseau de canaux et comment des paiements sont acheminés de leur source vers leur destination.

Le Lightning est un réseau de canaux de paiement. Ce sont donc des milliers de pairs avec leurs canaux de liquidité qui sont connectés entre eux, et ainsi s’auto-utilisent pour réaliser des transactions entre pairs non-connecté.

La liquidité des canaux ne peut pas se déplacer dans d’autres canaux de liquidité.

Alice -> Eden – > Bob. Les satoshis n’ont pas bougé d’Alice -> Bob, mais d’Alice -> Eden et d’Eden -> Bob.

Chaque personne et canaux a donc de la liquidé différente. Afin de réaliser des paiements, il faut donc trouver une route dans le réseau avec assez de liquidité. S’il en manque, le paiement n’aboutira pas :
Alice 130 – Susie 0 ; Susie 90 – Eden 200 ; Eden 150 – Bob 100

Si Alice envoie 40 à Bob :
Alice 90 – Susie 40 ; Susie 50 – Eden 240 ; Eden 110 – Bob 140

Un autre exemple :
Alice 130 – Susie 0 ; Susie 90 – Eden 200 ; Eden 150 – Bob 100
Bob envoie 40 SAT à Alice :

Ce n’est pas possible car Susie n’a pas de liquidité avec Alice pour lui envoyer 40, donc le paiement n’est pas possible via cette route. Il faut donc une autre route où la transaction est impossible.

Dans l’exemple 1, on remarque bien que Susie et Eden n’ont rien perdu et rien gagné. Pour accepter d’être utilisés pour router la transaction, les nœuds Lightning Network demandent des frais !

Il y a des frais différents en fonction d’où se trouve la liquidité

Alice – Bob

- Frais d’Alice = Alice -> Bob
- Frais de Bob = Bob -> Alice

Il y a deux types de frais :

- Les frais fixes quel que soit le montant : 1 SAT (par défaut mais modifiable)
- Les frais variable (0.01% par défaut)

Exemple de frais :

    Alice – Susie ; 1/1 (1 en frais fixes et 1 en frais variable)
    Susie – Eden ; 0/200
    Eden – Bob ; 1/1

Donc :
Frais 1 : (payé par Alice a elle-même) 1 + (40 000*0.000001)
Frais 2 : 0 + 40 000 * 0.0002 = 8 SAT
Frais 3 : 1 + 40 000\* 0.000001 = 0.4 SAT

Envoi :
1 – Envoi de 40 009.04 Alice -> Susie ; Alice paye a elle-même ses frais donc cela ne compte pas
2 – Susie rend le service d’envoyer 40 001.04 à Eden, elle prend ça comme de 8 SAT
3 – Eden rend le service d’envoyer 40 000 à Bob, il prend son 1.04 SAT de frais.

Alice a payé 9.04 SAT de frais et Bob a reçu 40 000.

Dans le LN, c’est donc le nœud d’Alice qui va décider de la route avant l’envoi. Il y a donc une recherche de la meilleure route et Alice est la seule qui connait la route et le prix. Le paiement est envoyé mais Susie n’a pas d’information.

Pour Susie ou Eden : ils ne savent pas qui est le destinataire final, ni celui qui envoie.

Ceci est un routage en oignon. Le nœud doit donc garder un plan du réseau pour trouver sa route, mais aucun des intermédiaires n’a d’information.

## 8. HTLC

![HTLC](https://youtu.be/-JC4mkq7H48)

Dans un système de routage classique, Alice 100 000 -> 30 000 Susie 250 000 -> Bob 0, comment s’assurer qu’Eden ne triche pas et respecte bien sa part du contrat ?

HTLC – Hashed Time Locked Contract

HTLC est donc un contact de paiement où l’on peut déverrouiller uniquement avec un secret. S’il n’est pas dévoilé, alors le contrat expire. C’est donc un paiement conditionnel. Comment sont-ils utilisés ?

    Bob génère un secret S (la préimage) et en calcule le hash r= hash(s)
    Bob envoie une invoice à Alice avec notamment « r »
    Alice envoie un HTLC de 40 000 satoshis à Susie avec pour condition de révéler « s’ » tel que hash(s’)=r
    Susie envoie un HTLC similaire à Bob
    Bob déverrouille le HTLC de Susie en lui montrant « s »
    Susie déverrouille le HTCL d’Alice en lui montrant « S »

Si Bob est offline et ne relève jamais le secret qui lui donne la légitimité pour recevoir l’argent, dans ce cas le HTLC va expirer après un certain nombre de bloc.

Les HTLC expirent dans l’ordre du dernier au premier : donc expiration Susie – Bob puis Alice – Susie.
Comme ça, si Bob revient, ça ne change rien. Dans le cas contraire, si Alice annule alors que Bob revient, ce sera le bordel et des gens peuvent avoir travaillé pour rien.

Bon et alors, la question c’est : en cas de clôture, il se passe quoi ? En fait, nos transactions d’engagement sont encore plus complexes. Il faut représenter la balance intermédiaire si jamais le canal se fait fermer.

Il y a donc un HTLC-out de 40 000 satoshis (avec les limitations vues avant) dans la transaction d’engagement via un output n°3

    Alice a donc dans la transaction d’engagement :

    Out-put n°1 : 60 000 SAT pour Alice via un Timelock et clé de révocation (ce qui lui reste)
    Out_put n°2 : 30 000 qui appartienne déjà à Susie
    Out-put n°3 : 40 000 en HTLC

La transaction d’engagement d’Alice est avec un HTCL-out car elle envoie et Susie un HTLC-in car elle reçoit.

Donc si l’on publie cette transaction d’engagement, Susie peut récupérer l’argent du HTCL avec l’imagine « s ». Si elle n’a pas la préimage, Alice récupère l’argent une fois que le HTCL expire.

Pensez les out-put comme différents paiements avec différentes conditions.

Une fois le paiement passé (expiration ou exécution), l’état du canal change et la transaction avec HTCL n’existe plus. On retourne avec quelque chose de classique.

En cas de fermeture coopérative : on arrête les paiements et donc on attend l’exécution des transferts/HTCL, la transaction est légère donc moins chère car il y a maximum 1 ou 2 outputs.

Si fermeture forcée : on publie avec tous les HTLC en cours, ça devient donc très lourd et très coûteux. Et c’est le bordel.

## 9. Trouver sa voie

![trouver sa voie](https://youtu.be/wnUGJjOxd9Q)

La seule donnée publique est la capacité totale du canal (Alice + Bob) mais on ne sait pas où se trouve la liquidité.
Pour avoir plus d’infos, notre nœud écoute le canal de communication du LN pour des annonces de nouveaux canaux et les mises à jour des frais des canaux. Votre nœud regarde aussi la blockchain pour la fermeture de canaux.

Comme nous n’avons pas toutes les informations, on doit faire une recherche de graph/route avec les informations qu’on a (capacité maximum des canaux et non où est la liquidité).

Critères :

    Probabilité de réussite
    Frais
    Délai d’expiration des HTLC
    Nombre de nœuds intermédiaires
    Aléatoire
    Etc

Donc s’il y a 3 routes possibles :

    Alice > 2 > 2 > 5 > Bob
    Alice > 1 > 2 > 4 > 5 > Bob
    Alice 1 > 2 > 3 > Bob

On cherche donc la meilleure en théorie avec le moins de frais et le plus de chance de réussir : un maximum de liquidité et le moins de hop possible.

2-3 aillant que 130 000 SAT de capacité, envoyer 100 000 est très peu probable donc choix n°3.

Désormais l’algorithme a fait ses 3 choix et va donc essayer le premier :

Choix 1 :

    Alice envoie un HTCL à 1 de 100 000 SAT ;
    Le 2 fait un HTLC de 100 000 SAT pour le 2
    Le 2 fait un HTLC de 100 000 SAT au 5 sauf que le 5 ne peut pas, donc l’annonce.

L’information est renvoyée donc Alice décide d’essayer la deuxième route :

    Alice envoie un HTLC de 100 000 à 1
    1 fait un HTLC de 100 000 à 2
    2 fait un HTLC de 100 000 vers 4
    4 fait un HTLC de 100 000 vers Bob. Bob a la liquidité donc c’est ok.
    Bob utilise la préimage (hash) du HTLC et donc utilise le secret pour récupérer les 100 000 SAT
    5 a donc désormais le secret du HTLC pour récupérer le HTLC bloqué de 4
    4 a donc désormais le secret du HTLC pour récupérer le HTLC bloqué de 2
    2 a donc désormais le secret du HTLC pour récupérer le HTLC bloqué de 1
    1 a donc désormais le secret du HTLC pour récupérer le HTLC bloqué d’Alice

Alice n’a pas vu l’échec de la route 1, elle a juste attendu 1 seconde de plus. Un échec de paiement se déroule lorsqu’il n’y a pas de route possible. Pour faciliter la recherche de route, Bob peut fournir des infos à Alice pour aider dans son invoice :

    Le montant
    Son adresse
    Le hash de la préimage pour qu’Alice puisse créer le HTLC
    Des indications sur les canaux de Bob

Bob connait la liquidé des canaux 5 et 3 car il est directement connecté avec, il peut indiquer ça à Alice. Il prévient Alice que le nœud 3 est inutile, ça évite à Alice de potentiellement faire sa route.

Un autre élément serait les canaux privé (donc non publiés au réseaux) que Bob peut avoir. Si Bob a un canal privé avec 1, il peut dire à Alice de l’utiliser et ça donnerait Alice > 1 > Bob

## 10. Invoice, LNURL, Keysend

![invoice, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

Un invoice c’est long et chiant, mais ça fait une demande de paiement.

Exemple :
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

    lnbc1m = partie lisible
    1 = séparation avec le reste
    Puis le reste

Bc1 = Encodage Bech32 (base 32), on utilise donc 32 caractères.

    10 = 1.2.3.4.5.6.7.8.9.0
    26 = abcdefghijklmnopqrstuvwxyz
    32 = pas le « b- i- o » et pas le « 1 »

lnbc1m ->

ln = Lightning
Bc = bitcoin (mainnet)
1 = montant
M = milli (10*-3 / u = micro 10*-6 / n = nano 10*-9 / p = pico 10*-12
Ici 1m = 1 \* 0.0001btc = 100 000 BTC

« Prié de payer 100 000 SAT sur le réseau Lightning du mainnet bitcoin

« pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3 »

    Timestamp (quand il a été créé)
    0 ou plusieurs parties supplémentaires :
        Hash de la préimage
        Secret de paiement (routage en oignon)
        Données arbitraires
        Clé publique LN du destinataire
        Durée d’expiration (1h)
        Indications de routage
        Etc
    Signature de l’ensemble

Il existe d’autres types d’invoice. Le meta-protocole LNURL permet de fournir un montant de satoshis direct au lieu de faire une demande. C’est très flexible et permet beaucoup d’améliorations en termes d’expérience utilisateur.

Un Keysend permet à Alice d’envoyer de l’argent à Bob sans avoir la demande de Bob. Alice récupère l’ID de Bob, crée une préimage sans demander à Bob et l’inclus dans son envoi. Donc, Bob va recevoir une demande surprise où il peut débloquer l’argent car Alice a déjà effectué le travail.

## note la formation

## 11. Gérer sa liquidité

![gerer sa liquidité](https://youtu.be/YuPrbhEJXbg)

Dans ce onzième épisode, nous donnons quelques repères généraux pour répondre à la sempiternelle question de la gestion de la liquidité sur Lightning.

Dans LN, il y a 3 types de personnes :

    Les acheteurs : ils ont de la liquidé sortante, c’est le plus simple car il suffit d’ouvrir des canaux
    Les vendeurs : c’est plus compliqué car ils ont besoin de liquidité entrante via d’autres nœuds et d’autre acteurs. Ils doivent avoir des gens connectés à eux
    Les nœuds de routage : ils veulent être équilibre avec de la liquidité des deux côtes et une bonne connexion à de nombreux nœuds pour être utilisés le plus possible

Donc si vous avez besoin de liquidité entrante, vous pouvez en acheter à des services.

Alice achète un canal avec Susie pour 1 million donc elle ouvre un canal avec directement 1 000 000 SAT du coté entrant. Elle peut alors accepter jusqu’à 1 million de SAT de paiement par les clients qui seraient connectés avec Susie (qui est très connectée).

Une autre solution serait de faire des paiements : donc vous payez 100 000 pour X raison, vous pouvez désormais recevoir 100 000.

Solution Loop Out : Atomic swap LN – BTC

Alice 2 millions – Susie 0
Alice veut envoyer la liquidité vers Susie, donc elle fait un Loop out (un nœud spécial qui offre un service pro de rééquilibre).
Alice envoie 1 million à loop via le nœud de Susie, donc Susie a la liquidité et Loop renvoie la balance on-chain au nœud d’Alice :

Donc les 1 million partent chez Susie, cette dernière envoie 1 million à Loop, Loop envoie 1 million à Alice. Alice a donc déplacé la liquidité vers Susie au prix de quelques frais payés à Loop pour le service.

Le plus compliqué dans LN est de garder la liquidité :

    Loop out
    Fermer et ouvrir des canaux
    Attendre que les nœuds de routage réorganisent leur liquidité

## conclusion

![conclusion](https://youtu.be/MaWpD0rbkVo)

Ceci est la fin de la formation Lightning Network Technique de Fanis. Un immense merci à lui pour son temps et pour avoir partager ses connaissances. Si vous souhaitez lui faire une donation en LN ou bitcoin, les adresses sont en bas de la page !

    Et maintenant ? Voici quelques pistes :

        La salle des interview est ouverte, tu peux retrouver une discussion entre Fanis et moi !
        L’aventure Lightning Network continue avec la formation sur Umbrel et la mise en place d’un nœud Lightning Network
        Approfondis tes connaissances dans la bibliothèque avec les ressources Lightning Network
        Viens discuter sur notre serveur discord de Lightning Network

Il y a beaucoup à voir donc n’hésites pas à nous follow pour ne rien louper !

Si tu veux nous laisser un mot d’encouragement ou si tu as des questions sur la formation, laisse les nous ci-dessous ! On se fera un plaisir d’y répondre !

Merci à vous et merci Fanis !
Bisous et à très bientôt !

Rogzy

## allez plus loins ressource

Félicitations ! Vous avez terminé la formation LN 201 – Introduction au Lightning Network 😀 Vous pouvez être fier de vous car ce n’est pas facile : sachez que peu sont les personnes qui descendent aussi bas dans le terrier du Bitcoin.

Tout d’abord, un grand merci à Fanis Makalakis pour nous avoir offert ce super cours gratuit sur un aspect plus ethnique du Lightning. N’hésitez pas à le suivre sur Twitter, sur son blog ou via son travail chez LN market. Si vous souhaitez lui faire une donation en LN directement, c’est par ici.

Ensuite, si vous souhaitez aider le projet, n’hésitez pas à nous sponsoriser sur Patreon. Vos dons serviront à produire du contenus pour de nouvelles formations et bien évidemment, vous serez les premiers à être tenus au courant (y compris pour la prochaine de Fanis qui est dans les tuyaux !).

Fini la théorie et place à la pratique avec la formation LN 202 désormais !

## Soutiens nous

Ce cours, ainsi que l'intégralité du contenu présent sur cette université, vous a été offert gratuitement par notre communauté. Pour nous soutenir, vous pouvez le partager autour de vous, devenir membre de l'université et même contribuer à son développement via GitHub. Au nom de toute l'équipe, merci !

## Note la formation

Un système de notation pour la formation sera bientôt intégré à cette nouvelle plateforme de E-learning ! En attendant, merci beaucoup d'avoir suivi le cours et si vous l'avez apprécié, pensez à le partager autour de

## Interview avec Fanis sur la vie privée dans Lightning

![interview avec Fanis](https://youtu.be/VeJ4oJIXo9k)
