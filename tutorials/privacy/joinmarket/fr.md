---
name: JoinMarket

description: Guide et tutoriel sur l'utilisation de JoinMarket pour faire du CoinJoin sur du Bitcoin via la ligne de commande
---

![cover](assets/cover.webp)



---

Si vous avez trouvé cette page en faisant une recherche en ligne sur " JoinTmarket ", je vous remercie sincèrement. Vous êtes cependant tombé sur un guide qui traite d'un sujet complètement différent, mais extrêmement intéressant ! 🚬🍁



L'objectif de ce tutoriel est d'illustrer le fonctionnement théorique et pratique de JoinMarket, à travers la ligne de commande. 🐢 💚



## Définition théorique de JoinMarket



Nous pouvons définir JoinMarket comme un outil, ou un Wallet, qui permet le CoinJoin avec d'autres utilisateurs d'une manière totalement Trustless et sans coordinateur central.



Comme toute la partie théorique de cet outil est extrêmement vaste, j'ai décidé de l'aborder dans un épisode spécifique de mon podcast. Pour ceux qui comprennent l'italien, je recommande vivement de poursuivre la lecture après avoir écouté l'épisode, afin de mieux assimiler les concepts de base pour utiliser correctement ce programme.



Vous pouvez rattraper l'épisode en cliquant sur ces liens directs :




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (vous pouvez l'écouter directement depuis votre navigateur).
- [Antenna pod](https://antennapod.org/) est un gestionnaire de podcast gratuit et opensource qui ne nécessite pas d'enregistrement. Pour trouver l'épisode, téléchargez l'application, ajoutez manuellement mon podcast en collant [ce lien](https://Anchor.fm/s/bd5d5b20/podcast/rss) dans la section _feed rss_, puis recherchez l'épisode consacré à JoinMarket.



## Installation



Systèmes d'exploitation :





- Raspiblitz
- Parapluie
- MonNœud
- Raspibolt



## Fichiers de configuration



JoinMarket est un logiciel personnalisable avec un nombre infini de paramètres ; ces paramètres sont spécifiés dans un fichier de configuration situé dans le répertoire principal du programme appelé `Joinmarket.cfg`.



Dans cette section, nous allons passer en revue certains champs qu'il peut être intéressant d'explorer et/ou de modifier, en fonction de vos besoins. Je tiens à souligner que toutes les modifications énumérées ci-dessous sont utiles à connaître afin d'adapter le fonctionnement du logiciel aux besoins personnels, sans pour autant être obligatoires.



Tout d'abord, allons dans le dossier `joinmarket/scripts` et lançons la commande :



```bash
python wallet-tool.py generate
```


A ce stade, nous devrions obtenir une erreur, mais en faisant cela, le logiciel va generate un fichier de paramètres prédéfinis pour nous. Nous pouvons éditer le fichier de paramètres à partir du terminal avec :



```bash
nano joinmarket.cfg
```



ou :



```bash
vim joinmarket.cfg
```



une fois ouvert, nous remarquerons de nombreuses lignes avec divers paramètres et leur explication en anglais. Plus précisément, nous analyserons ci-dessous les variables les plus intéressantes :





- `merge_algorithm` dans le cas où nous faisons comme un fabricant, ce champ ajuste l'agressivité avec laquelle le logiciel consolidera les sorties non dépensées. Si nous avons beaucoup d'UTXO à consolider, il peut être judicieux de passer de _gradual_ à _greedy_
- `tx_fees` ajuste en tant que preneur les frais avec lesquels payer la transaction, il est très utile de changer ce paramètre dans le cas où vous utilisez souvent le tumbler (nous en parlerons plus tard) car s'il y a un pic dans les frais pendant l'exécution de ce dernier, si nous ne réglons pas ce champ correctement, nous risquons de dépenser beaucoup de Sats pour du CoinJoin. En fixant des valeurs en milliers (comme 2000), cela équivaudra à 2 Sats/vBytes, 3500 à 3,5 Sats/vBytes, et ainsi de suite. Je recommanderais un nombre compris entre 1500 et 6000 en fonction de vos besoins.
- `max_cj_fee_abs` est utilisé pour spécifier combien nous sommes prêts à payer en termes absolus pour les makers que nous choisissons pendant CoinJoin. Par défaut ce champ pour les makers est de 200 Sats, une bonne option pourrait être un nombre allant de 200 à 1000 Sats par contrepartie (ceci est basé sur combien vous voulez dépenser et combien d'anon-set vous recherchez pour vos CoinJoins)
- `max_cj_fee_rel` a la même fonction que le champ ci-dessus mais spécifie les frais relatifs (pourcentages) que nous sommes prêts à payer à chaque contrepartie. Comme il s'agit d'une valeur en "pourcentage", faites attention à ne pas mettre des valeurs élevées pour éviter des coûts élevés dans les CoinJoins avec de gros montants. La valeur par défaut pour les makers est _0.00002_, je recommande une valeur similaire ou légèrement supérieure.
- `minimum_makers` est le champ qui spécifie le nombre d'autres contreparties avec lesquelles nous faisons du CoinJoin, par défaut joinMarket choisit toujours entre 4 et 9 contreparties, si nous le souhaitons, pour plus de confidentialité, nous pouvons augmenter cette valeur à 5 ou 6 (cela rendra les transactions plus chères cependant).
- `cjfee_a` spécifie, dans le cas où nous agissons en tant que maker, combien de Sats en termes absolus nous voulons collecter pour louer notre liquidité. Ce champ est totalement subjectif, la valeur par défaut est déjà très bonne (nous aurons ainsi une meilleure confidentialité en tant que maker), nous pouvons envisager de la mettre à 0 si nous voulons gagner plus de CoinJoin en moins de temps.
- `cjfee_r` même champ que ci-dessus mais en pourcentage et non en valeur absolue. Là encore, je recommande de laisser la valeur par défaut ou de l'abaisser pour attirer plus de preneurs.
- `ordertype` Avec ce champ, nous choisissons de faire payer le fabricant en valeur absolue (absoffer) ou en pourcentage (reloffer). En général, les preneurs préfèrent les offres absolues pour les questions économiques.
- `minsize` si, en tant que créateur, nous ne voulons pas que la UTXO soit trop petite, nous pouvons spécifier la CoinJoin minimale pour participer. Ce champ est exprimé en Satoshi et est totalement subjectif. Nous pouvons laisser ce champ à 0 ou l'augmenter à 500000 (Sats), 1000000 (Sats), et ainsi de suite.



Faites très attention à ne pas modifier les mauvais champs, certaines variables du fichier joinmarket.cfg, si elles sont mal réglées, peuvent compromettre la fonctionnalité du logiciel ou anéantir complètement votre vie privée, gardez les yeux ouverts et soyez prudent au maximum !



## Configuration de l'environnement de travail



Certains nœuds définissent automatiquement les valeurs correctes pour ces champs dans le fichier joinmarket.cfg, mais il est recommandé de les vérifier à nouveau manuellement :





- `rpc_user = yourusername-as-in-Bitcoin.conf` (nom d'utilisateur comme dans Bitcoin.conf)
- `rpc_password = yourpassword-as-in-Bitcoin.conf` (mot de passe de l'utilisateur)
- `rpc_host = localhost #default usually correct`
- `rpc_port = 8332 # défaut pour Mainnet`



A ce stade, nous pouvons procéder à la création de notre Wallet dans JoinMarket :



```bash
python wallet-tool.py generate
```



Cette commande nous permet d'entrer un mot de passe pour crypter la Wallet et le nom que nous voulons lui donner. Lorsqu'elle vous demande si vous voulez ou non soutenir les obligations de fidélité, je vous recommande d'utiliser l'option _yes_, la sortie retournée ressemblera à ceci :



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


si une erreur apparaît, c'est probablement parce que nous avons mal défini les 4 champs RPC spécifiés ci-dessus. Dans ce cas, il peut être utile de suivre [ce guide](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) qui se trouve dans la documentation originale de JoinMarket.



Nous avons terminé la configuration de notre environnement de travail et nous pouvons commencer à explorer les commandes qui nous seront les plus utiles. Tous les scripts dont nous allons parler peuvent être lancés dans la console, suivis de `--help` pour une explication en profondeur.



Nous pouvons maintenant essayer de lancer l'application :



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



cette commande vous montrera tous les différents mélanges wallet avec les différentes adresses catégorisées comme :




- Nouveau (Address jamais utilisé)
- Change-out (reliquat d'une transaction précédente)
- Cj-out (sortie d'un CoinJoin)



voici un exemple pratique du résultat :



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Nous pouvons maintenant déposer nos premiers Satoshis dans une ou plusieurs adresses en nous rappelant que, quel que soit le créateur ou le preneur, le logiciel n'ira jamais consolider directement le UTXO dans différentes profondeurs de mélange, de cette façon nous pouvons garder les Satoshis avec différents niveaux de confidentialité séparés au sein du Wallet.



## Envoi de Bitcoin avec CoinJoin Simple



Nous pouvons maintenant déplacer nos Satoshis. L'une des principales commandes de ce logiciel est le script :



```bash
pyhton sendpayment.py
```


qui nous permettra d'envoyer des transactions à d'autres adresses avec ou sans CoinJoin. Voyons comment cela fonctionne et quelques exemples pratiques. Par défaut, le formatage de la commande est le suivant (n'oubliez pas de remplacer le texte entouré des symboles < et >) :



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



un exemple basique d'utilisation pourrait être :



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


dans ce cas nous allons envoyer à l'adresse 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc soit 5000000 Satoshi de notre mixdepth 0 (celui par défaut) en allant choisir de 4 à 9 contreparties pour CoinJoin (option par défaut).



Pour mieux contrôler comment et quels UTXOs dépenser, nous pouvons passer en revue les options supplémentaires de cette commande :



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


dans cet exemple, nous avons ajouté deux spécifications : -N indique le nombre de contreparties avec lesquelles nous allons mixer, -m la profondeur de mixage à partir de laquelle nous allons retirer des fonds. En fait, nous avons envoyé 100 000 000 Sats (1 btc) à l'adresse 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c avec les fonds dans mixdepth 1 et en mélangeant avec 5 contreparties.



Si nous mettons 0 comme valeur d'envoi en spécifiant un mixdepth, joinMarket effectuera un "balayage", c'est-à-dire qu'il enverra tous les fonds dans ce mixdepth en les consolidant les uns avec les autres :



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



ici, nous avons envoyé tous les fonds de la profondeur de mélange 0 (nous aurions pu ne pas la spécifier car c'est la valeur par défaut) en les mélangeant avec 7 contreparties.



La commande sendpayment est utilisée pour déplacer des fonds de joinMarket vers des Wallet externes ou pour envoyer des Satoshi à une personne en ajoutant une Layer de confidentialité entre nous et elle. Pour obtenir un niveau de confidentialité suffisant sur nos UTXO, il est plus approprié d'utiliser la commande tumbler.py que nous expliquerons plus loin dans ce guide.



## Être un créateur



Le script que nous allons aborder dans cette section est le suivant :



```bash
yg-privacyenhanced.py
```



Ce programme est utilisé pour agir en tant que maker sur le joinMarket. Le logiciel se connectera à notre nœud Bitcoin et à la place de marché interne de la plateforme dans laquelle les makers se présentent en tant qu'offreurs de liquidité et les takers recherchent des contreparties. Si vous souhaitez utiliser une obligation de fidélité, vous pouvez en créer une avec ce formatage :



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



par exemple :



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



la sortie qui nous sera renvoyée sera une adresse Bitcoin (c'est-à-dire celle sur laquelle vous devrez déposer les fonds que vous souhaitez allouer à fidelity).



**Attention** : Il y a deux choses auxquelles il faut faire très attention si vous voulez créer un Bon de Fidélité (alias FB) ;





- une fois que les fonds ont été déposés, ils ne peuvent plus être déplacés jusqu'à leur expiration. Faites attention au nombre de Sats que vous envoyez à l'adresse et au format de la date. Les erreurs ne sont pas permises !
- L'obligation de fidélité est facilement reconnaissable sur la chaîne, il est donc conseillé de déposer des fonds par l'intermédiaire d'un CoinJoin et avec une origine sans rapport avec votre identité. Il est également conseillé de faire la même chose une fois que vous voulez déplacer la caution de fidélité expirée hors de JoinMarket.



Il est important de rappeler qu'il est possible de recharger l'obligation de fidélité avec une seule transaction, en cas de UTXO multiples, seule la plus importante sera considérée comme valide pour l'obligation de fidélité.



Une fois que nous avons créé le lien de fidélité (dont nous nous souvenons qu'il est facultatif), nous sommes prêts à lancer l'exécutable pour agir en tant que maker sur joinMarket. Une fois que les Sats ont été déposés aux différentes adresses et à la mixdepth, nous pouvons exécuter la commande :



```bash
python yg-privacyenhanced.py <wallet name>
```



A partir de ce moment (après quelques minutes de connexion au réseau) et jusqu'à ce que nous arrêtions le script, notre client JoinMarket apparaîtra sur la liste des faiseurs actifs sur le protocole et offrira notre liquidité à diverses contreparties pour faire du CoinJoin. Ne vous attendez pas à des dizaines de CoinJoins par jour (à moins que vous n'ayez une grande fidélité et une grande liquidité déposée sur Wallet), rappelez-vous également que des facteurs tels que les frais requis et les Satoshis déposés affectent la fréquence à laquelle vous serez un maker.



En exécutant la commande ci-dessous, vous pourrez voir l'historique de toutes les transactions effectuées sur la Wallet et tout gain (si vous êtes un créateur) ou toute dépense (si vous êtes un preneur) que vous avez eu au cours de la durée de vie de la wallet.



```bash
python wallet-tool.py <wallet name> history
```



Une fois que vos Satoshis font des CoinJoins, ils se déplacent de mixdepth en mixdepth jusqu'à ce qu'ils atteignent le dernier. Une fois le quatrième passé, ils reviendront au mixdepth 0. C'est à vous de décider combien d'intimité vous souhaitez obtenir avant de les déplacer vers un Cold Wallet, il est conseillé de terminer un cycle Wallet complet.



## Gobelet



Nous voici enfin arrivés à la partie la plus juteuse de JoinMarket, le tumbler ! Si vous avez écouté le podcast, vous savez déjà de quoi il s'agit. Une recommandation avant de commencer : **N'oubliez pas de définir les limites dans le fichier joinmarket.cfg (comme expliqué au début) et envisagez d'exécuter le programme uniquement lorsque les frais onchain sont relativement bas (moins de 10 Sats/vB).



Pour lancer le culbuteur, il est nécessaire d'avoir arrêté le script du fabricant (s'il était actif), après quoi nous pouvons exécuter la commande :



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Il est essentiel d'entrer **au moins** 3 adresses de sortie pour le tumbler : ceci afin d'assurer une bonne confidentialité et de ne pas créer de liens évidents entre les UTXOs tout au long du processus. Comme d'habitude, en ajoutant "--help" à la commande, vous pouvez aller voir tous les détails supplémentaires. Voyons un exemple plus complexe avec des règles avancées :



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Dans ce cas, nous avons lancé un script de tumbling qui n'utilisera pas le nombre de contreparties par défaut (le paramètre -N indique que nous avons besoin de 7 contreparties avec une variance maximale de 2, donc un nombre aléatoire de makers de 5 à 9) et avec un plus grand nombre de CoinJoin par mixdepth (par défaut ce script fait un nombre aléatoire de CoinJoin par section de Wallet allant de 1 à 3, en utilisant la commande -c 3 1 au lieu de cela ce sera de 2 à 4). De cette façon, nous dépenserons plus de Sats en frais mais nous aurons un plus grand ensemble d'anonymat.



Vous pouvez également ajouter autant d'adresses de sortie que vous le souhaitez (minimum 3, il n'y a pas de maximum si ce n'est le bon sens). Cependant, il n'est pas possible, pour des raisons de confidentialité, de décider comment Satoshi sera réparti entre les adresses spécifiées en sortie.



Tumbler est un processus délibérément long, occasionnellement il peut arriver que quelque chose s'arrête de fonctionner, dans la plupart des cas cela se résoudra en quelques heures. Dans le cas d'un crash total, nous pouvons essayer de le redémarrer avec la commande :



```bash
python tumbler.py --restart
```



Il est également possible de relancer une nouvelle commande de culbutage. Cela ne démarrera pas la programmation du culbuteur précédent mais démarrera un nouveau cycle de mélange. Si la fermeture du terminal SSH de votre nœud arrête également le script, vous pouvez utiliser le programme `TMUX` qui peut être installé avec la commande :



```bash
sudo apt install tmux
```



Le lancer depuis le shell en tapant `tmux` ouvrira un terminal pour vous qui restera actif en arrière-plan même si vous fermez la connexion à distance. Lorsque vous vous reconnectez à votre nœud avec la commande : `tmux attach`, vous ouvrirez à nouveau le shell qui est resté actif en arrière-plan.



## Conclusion



JoinMarket est un logiciel illimité et personnalisable. Dans ce guide, nous avons découvert les principales fonctions afin qu'il soit possible pour n'importe qui (ou du moins j'ai essayé, je suis conscient que l'utilisation de ce logiciel n'est pas une promenade dans le parc) de l'utiliser. L'un des plus grands problèmes de JoinMarket est justement le nombre de personnes qui l'utilisent et qui en font un maker. Si peu d'utilisateurs profitent de ce logiciel, la confidentialité globale (anon-set) est réduite. C'est pourquoi j'espère que ce guide vous incitera à l'utiliser et vous convaincra de télécharger et d'installer mon logiciel préféré pour faire CoinJoin. Au cas où vous voudriez approfondir certains aspects, je vous recommande de lire les différentes documentations approfondies sur github, elles sont très bien faites et vous pouvez les trouver ici.



Joyeux mélange de tortues!🐢 💚



[Ici](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) vous pouvez soutenir Turtlecute