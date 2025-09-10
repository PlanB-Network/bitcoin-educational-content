---
name: Coin Control
description: Initiez-vous au Coin Control, un outil clé pour protéger votre vie privée sur Bitcoin
---
![cover](assets/cover.webp)


*Ce tutoriel est importé d’[une leçon d’Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Introduction



La solidité du protocole Bitcoin est garantie par des concepts fondamentaux simples. Parmi eux, la transparence se distingue : toutes les transactions Bitcoin sont publiques et facilement vérifiables par quiconque. Bien que cette caractéristique constitue une pierre angulaire du protocole, puisqu’elle empêche la fraude et garantit l’authenticité des fonds, elle peut aussi représenter un défi pour la confidentialité. **Vous êtes-vous déjà demandé si une telle transparence pouvait nuire à votre vie privée ?**



Vous devriez. S'il est assez facile d'accumuler des Satoshi non-kyc, c'est au stade des dépenses que votre vie privée est la plus menacée.



### Que se passe-t-il lorsque vous dépensez une UTXO ?



Dépenser le Bitcoin n'est pas simplement transférer une valeur à quelqu'un d'autre.



En consommant un de vos UTXO, vous devez en effet remplir les conditions imposées pour la transparence du protocole, car vous avez l'obligation de prouver que vous possédez ces fonds. Vous vous rendez donc responsable de :




- exposer votre clé publique ;
- produire une signature numérique.



Le moment de la dépense est donc le plus critique : **dépenser Bitcoin est un acte qui doit être fait consciemment et avec le plus de contrôle possible**.



## Coin Contrôle



Dans le protocole Bitcoin, des éléments tels que _compte_ ou _unités monétaires_ n'existent pas. Le concept de UTXO est expliqué de manière excellente dans le cours suivant, que je recommande vivement :



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Avec Bitcoin, ce que vous accumulez et dépensez plus tard sont de petites ou grandes unités de compte mesurées en Satoshi, représentées par les "sorties de transaction non dépensées", les **UTXO**, également appelées "pièces". Lorsque vous utilisez des UTXO pour créer une transaction, ils sont complètement détruits et d'autres UTXO sont créés à leur place.



Les portefeuilles logiciels sont développés pour faire ce choix automatiquement, en utilisant des pièces sélectionnées "au hasard", en adoptant certains algorithmes fournis par le protocole. Le seul critère auquel ces algorithmes doivent répondre est de couvrir le montant nécessaire à la dépense.



Ils peuvent mélanger des UTXO d'âges différents, ou privilégier les dépenses les plus récentes ou les plus "anciennes", selon l'algorithme choisi par les développeurs. Les meilleurs portefeuilles logiciels prévoient également de laisser un choix important à l'utilisateur.



Le manuel `Coin Control`, également appelé `Coin Selection`, est une fonction de certains portefeuilles logiciels qui vous permet de **sélectionner manuellement les UTXOs à dépenser lorsque vous créez votre transaction**.



Supposons que nous ayons un Wallet avec 3 UTXO de 21 000, 42 000 et 63 000 Satoshi, respectivement.



![img](assets/en/01.webp)



Si vous devez dépenser 24 000 Sats et laisser un algorithme faire la sélection automatique, une bonne Software Wallet pourrait choisir de combiner UTXO 1 + UTXO 2 pour payer les frais de 24 000 Sats et Miner, créant ainsi un reste qui sera reversé à une Address interne de la Wallet de départ.



![img](assets/en/02.webp)



Après l'opération, la nouvelle situation dans Wallet, en ne tenant compte que des UTXO, peut être résumée comme suit.



![img](assets/en/03.webp)



Cependant, avec le bon logiciel et en connaissance de cause, vous auriez pu faire un choix différent et, à certains égards, plus correct. Par exemple, en ne sélectionnant que l'UTXO2 (parmi 42 000 Sats).



![img](assets/en/04.webp)



Avec une situation finale dans votre Wallet, au niveau de la UTXO, cela semble différent d'avant.



![img](assets/en/05.webp)



## Pourquoi le coin control manuel ?



![img](assets/en/06.webp)



Dans les deux exemples ci-dessus, le solde est en fait le même `108,280 Sats`. Après avoir dépensé 24 000 Sats, sans sélection manuelle, nous aurions 2 UTXO dans la Wallet ; avec le contrôle manuel de la Coin, nous en avons 3 au total.



La question que nous pourrions nous poser est la suivante : **pourquoi faire tout cela ?** Il y a, ou pourrait y avoir, plusieurs raisons pour lesquelles nous n’avons pas utilisé `UTXO1` **et toutes constituent la base du pourquoi — lors de la dépense — activer le coin control manuel est l’une des bonnes pratiques à suivre**.



La sélection des UTXO vous permet de privilégier certains aspects par rapport à d'autres. Le choix dépend en fait des objectifs que vous souhaitez atteindre.



### Vie privée



L'un des principaux avantages du contrôle manuel de la Coin est une **plus grande confidentialité pour le dépensier**. Reprenons toujours notre exemple : la dépense de 24 000 Satoshi _sans sélection manuelle de Coin_. Comme la Blockchain de la Bitcoin est publique, un observateur extérieur peut déclarer, sans l'ombre d'un doute, que les entrées `UTXO1 de 21.000 Sats` et `UTXO2 de 42.000 Sats`, ainsi que le reste, le `UTXO5 de 38.280 Sats` **appartiennent tous les trois au même utilisateur**.



En sélectionnant manuellement `UTXO2`, par contre, `UTXO1` reste complètement réservé, dans l'ensemble UTXO en attendant d'être dépensé à un moment plus approprié.



L'"UTXO1" pourrait provenir d'une source KYC, telle qu'un paiement reçu dans la Exchange pour des biens et des services, alors que les autres UTXO ne le sont pas. Mélanger un UTXO-kyc avec d'autres qui sont plus confidentiels compromet l'ensemble d'anonymat des fonds non-kyc.



**Les fonds KYC mèneraient inévitablement à retrouver l’identité du payeur. Si c’était ton wallet, voudrais-tu qu’un observateur externe puisse remonter à ton identité avec une certitude aussi absolue ?**



Essayez donc de considérer que les portefeuilles qui mettent en œuvre la sélection manuelle des UTXO, par exemple, permettent la **ségrégation d'une ou plusieurs UTXO**, une fonction à utiliser lorsque de telles situations se présentent.



Bien que je sois convaincu que les fonds KYC devraient être conservés dans une Wallet distincte de la Bitcoin achetée sans KYC, si c'est votre cas, la séparation de certaines de vos adresses est une aide précieuse, dont vous pourriez tirer parti en apprenant à sélectionner manuellement vos entrées de dépenses.



### Économiser sur les frais



La sélection de la bonne UTXO pour effectuer une dépense **permet d'optimiser les frais**. Toujours à partir de notre exemple initial, la Software Wallet a sélectionné deux UTXO pour couvrir la dépense à effectuer. Deux UTXO impliquent deux signatures à présenter au réseau. Il s'ensuit que la transaction a un plus grand "poids" en termes de vBytes.



En revanche, le contrôle manuel Coin vous permet de ne sélectionner qu'une seule opération suffisante pour couvrir le montant, ce qui vous permet d'économiser des frais en diminuant le "poids" de la transaction.



Lorsque les frais sont élevés, mais que vous êtes obligé de dépenser Bitcoin On-Chain (par exemple, pour ouvrir un canal Lightning Network), c'est alors que le contrôle Coin s'avère être la bonne incitation économique vers laquelle se tourner.



### Agrégation des restes



Lorsque vous effectuez un paiement et que vous utilisez Bitcoin On-Chain, la possibilité de recevoir de la monnaie devient presque toujours une certitude. Chaque reste est en soi une petite perte de vie privée, car il révèle au réseau (et surtout au destinataire du paiement) une de vos Address qui peut être associée à votre source d'entrée.



Etant donné que les meilleurs Wallet HDs generate ont des adresses spéciales pour les restes, vous pouvez facilement les reconnaître et "isoler" tous les restes des différentes transactions effectuées ; lorsqu'ils ont atteint un certain montant, vous pouvez les sélectionner manuellement et les consolider, ou passer à Lightning Network (ma méthode préférée) et les traiter de manière à retrouver la confidentialité perdue dans les dépenses.



### Dépenses d'une Cold Wallet



Le Cold Wallet est un instrument avec lequel on peut raisonnablement obtenir un bon degré de sécurité, pour stocker n'importe quel montant de fonds à mettre de côté pour une longue période. Cependant, des événements imprévus peuvent survenir, et il est alors nécessaire de mettre la main à la poche pour faire face à des dépenses inattendues.



Je ne sais pas combien de personnes peuvent partager mon approche, mais mon conseil est de **ne jamais effectuer la dépense directement à partir d'une Cold Wallet, afin d'éviter de recevoir le changement entre les adresses de la même**. Apprenez à sélectionner manuellement les UTXO nécessaires pour couvrir la dépense, transférez-les dans une Wallet Hot et préparez votre transaction à partir de cette dernière. Toute monnaie, alors, vous pouvez la renvoyer vers une Cold Wallet Address (si le montant est suffisant), l'utiliser pour d'autres dépenses, ou encore la ségréguer comme nous venons de le voir.



## Présentation pratique


Après l'introduction technique du "pourquoi", voyons comment mettre en pratique le contrôle manuel Coin avec différents logiciels, de bureau et mobiles. Nous utiliserons toujours le même Wallet BIP39, importé dans chacun des outils choisis, afin de vous montrer les petites différences entre eux.



## Bureau Wallet



### Sparrow



Si vous utilisez Sparrow, ouvrez votre Wallet et sélectionnez _UTXOs_ dans le menu de gauche. Vous verrez une liste de tous les UTXOs associés à votre Wallet.



Il suffit de cliquer avec la souris sur l'un d'entre eux et de choisir _Send Selected_. Sparrow vous montre aussi le total disponible pour la dépense après la sélection, juste à côté de la commande. Graphiquement, Sparrow vous montre le UTXO sélectionné en le surlignant en bleu.



![img](assets/en/07.webp)



Vous pouvez également en sélectionner plusieurs. Aidez-vous de la touche _CTRL_ pour sélectionner des UTXO non adjacents dans la liste.



![img](assets/en/08.webp)



Après avoir sélectionné manuellement UTXO, vous pouvez commencer à construire la transaction, et Sparrow vous montrera bien, graphiquement, comment elle est constituée.



![img](assets/en/09.webp)



#### Ségrégation de UTXO



La ségrégation des fonds consiste à les "verrouiller" dans la Wallet de façon à ce qu'ils ne puissent pas être utilisés comme données d'entrée dans une transaction. La Sparrow permet cette fonctionnalité, qui est toujours accessible à partir du menu _UTXOs_ : vous placez la souris sur la UTXO à "verrouiller" et cliquez sur le bouton droit de la souris. Parmi les fonctionnalités de cette procédure apparaîtra _Geler UTXO_. C'est ainsi que vous pourrez séparer les pièces avec les portefeuilles Sparrow.



![img](assets/en/29.webp)



### Electrum



Si votre bureau Wallet est Electrum, vous devez savoir que vous pouvez sélectionner manuellement des UTXOs soit dans le menu _Adresses_, soit dans le menu _Monnaies_. Dans les deux menus, la sélection se fait en pointant la souris sur le UTXO désiré et en choisissant _Ajouter au contrôle Coin_ après un clic droit.



![img](assets/en/10.webp)



Même avec ce logiciel, vous pouvez sélectionner plus d'un UTXO, en vous aidant de la touche _CTRL_ de votre clavier s'ils ne sont pas adjacents l'un à l'autre.



![img](assets/en/11.webp)



Graphiquement, Electrum vous montrera la sélection en mettant en évidence les UTXO sélectionnés en Green, tandis qu'une barre apparaît en bas, mise en évidence dans la même couleur, montrant le solde disponible après le contrôle Coin.



![img](assets/en/12.webp)



Une fois que vous avez sélectionné la ou les sorties, vous pouvez construire votre transaction comme vous le faites habituellement à partir du menu _Envoyer_.



#### Ségrégation du UTXO



Electrum fournit cette fonctionnalité en allant dans le menu _Coins_, où vous allez sélectionner une UTXO particulière et ensuite choisir _Freeze_ avec un clic droit. Vous pouvez "geler" la Address même sans fonds à partir du menu _Adresses_, ou la "Coin" pour ne pas la dépenser.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk vous permet de sélectionner manuellement des UTXOs à partir du menu principal une fois qu'il est ouvert. Lancez Nunchuk et cliquez sur _Voir les pièces_.



![img](assets/en/13.webp)



Cela ouvre la fenêtre qui contient tous les UTXO de votre Wallet, où vous pouvez en sélectionner un ou plusieurs en activant la coche à côté de chaque montant. Après avoir fait votre sélection, continuez avec _Créer une transaction_.



![img](assets/en/14.webp)



Vous pouvez ensuite saisir la destination Address et définir le montant et les frais.



![img](assets/en/15.webp)



#### Séparation de UTXO



Pour être complet, le Nunchuk permet également, parmi ses fonctionnalités, de séparer un (ou plusieurs) UTXO et ce de deux manières différentes. Accédez au menu _Voir les pièces_ et choisissez manuellement dans la liste des pièces. Cliquez ensuite sur le menu _Plus_ en bas à droite : une liste d'options apparaîtra, parmi lesquelles vous pouvez choisir _Verrouiller les pièces_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Vous pouvez également cliquer dans l'espace réservé à la UTXO, pour accéder à la fenêtre _Détails de la pièce_. La commande pour verrouiller/déverrouiller la UTXO en question apparaît alors dans le coin supérieur droit.



![img](assets/en/41.webp)



### Application Blockstream



Blockstream App desktop, anciennement connu sous le nom de Green, vous permet d'effectuer une sélection Coin lorsque vous avez déjà commencé à construire la transaction. Ouvrez donc votre Wallet et cliquez sur _Send_.



![img](assets/en/16.webp)



Collez la destination Address dans le champ approprié, puis sélectionnez _Sélection manuelle Coin_.



![img](assets/en/17.webp)



Cela ouvre la fenêtre dans laquelle vous pouvez sélectionner une ou plusieurs pièces UTXO. Dans l'exemple ci-dessous, nous avons sélectionné deux pièces. Confirmez ensuite votre choix en cliquant sur _Confirmation de la sélection Coin_.



![img](assets/en/18.webp)



Fixez le montant et les frais, puis procédez normalement à votre transaction.



![img](assets/en/19.webp)



⚠️ N.B. Dans le menu _Coins_ de Green, il y a des éléments _Lock_/_Unlock_ qui laissent entrevoir la possibilité de séparer UTXO. Cette fonction n'est activée que dans les comptes dits Multisig ; elle n'est également activée qu'en sélectionnant des UTXO d'un montant très faible, proche du seuil de `Dust`.



## Wallet mobile



Les portefeuilles peuvent également être choisis à partir d'un téléphone portable, ce qui permet de sélectionner manuellement les UTXO. Prenons le Blue Wallet comme premier exemple.



### Bleu Wallet



Si vous êtes utilisateur de ce Wallet, ouvrez-le et cliquez pour accéder aux écrans de contrôle relatifs à l'un de vos portefeuilles. Pour accéder au manuel de contrôle de la Coin, vous devez entrer dans la phase de dépense, puis cliquer sur _Envoyer_.



![img](assets/en/21.webp)



Sur l'écran suivant, choisissez les menus indiqués par les trois points dans le coin supérieur droit. Une fenêtre déroulante s'ouvre avec une série de commandes. Choisissez la dernière : _Coin Control_.



![img](assets/en/22.webp)



A ce stade, la Wallet bleue affiche toutes vos UTXO. En plus des quantités, ils sont différenciés graphiquement par des couleurs différentes.



![img](assets/en/27.webp)



Choisissez le UTXO à sélectionner, puis sélectionnez _Use Coin_.



![img](assets/en/23.webp)



Blue Wallet vous ramène à la fenêtre _Envoyer_ pour continuer à construire la transaction. Ajustez le montant et les frais, puis choisissez _Suivant_.



![img](assets/en/24.webp)



À ce stade, vous pouvez mettre fin à la transaction, comme vous le faites habituellement.



#### Ségrégation d'une UTXO



La Wallet bleue vous permet également de séparer les UTXO, les rendant indisponibles pour la dépense, ce qui n'est pas une mauvaise fonction pour une Wallet à partir d'un appareil mobile. Vous accédez à la commande Coin en suivant la procédure expliquée ci-dessus et, après avoir sélectionné la UTXO, choisissez _Freeze_ au lieu de _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



La version mobile du Nunchuk permet également à l'utilisateur de contrôler le Coin. Si vous utilisez cette application à partir d'un téléphone portable, ouvrez-la et allez dans le menu _Portefeuille_. De là, choisissez _Voir les pièces_.



![img](assets/en/30.webp)



Dans la fenêtre où apparaît la liste des UTXO, cliquez sur _Select_.



![img](assets/en/38.webp)



Une fonction de sélection apparaît à côté de chaque UTXO. Comme dans la version de bureau, la sélection manuelle sur le Nunchuk mobile se fait en cochant le petit carré à côté du montant. L'écran affiche le nombre d'UTXOs sélectionnés et le montant total disponible. Lorsque vous avez terminé, cliquez sur le symbole ₿ dans le coin inférieur gauche, qui est la commande pour commencer à construire la transaction.



![img](assets/en/31.webp)



Vous pouvez maintenant terminer la transaction en choisissant le montant et en cliquant sur _Continue_.



![img](assets/en/32.webp)



Continuez comme vous le faites toujours, en collant une destination Address, une description et en personnalisant les paramètres des frais.



#### Ségrégation de UTXO



Vous pouvez également séparer les UTXO avec le Nunchuk mobile. Accédez à la fenêtre de la liste des pièces dédiées et sélectionnez la flèche à côté du UTXO que vous voulez séparer.



![img](assets/en/42.webp)



Vous verrez l'espace réservé aux _Détails de la pièce_, où vous pouvez sélectionner _Bloquer cette pièce_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper est le dernier Wallet que nous verrons dans ce guide. Ses fonctionnalités sont appliquées au contrôle des Coin avec une Wallet à signature unique, bien qu'une telle utilisation ne soit pas le but de cette application très particulière. Après avoir installé Keeper sur votre téléphone, lancez-le et ouvrez un Wallet contenant des fonds. Au centre de l'écran principal, cliquez sur _Voir toutes les pièces_.



![img](assets/en/34.webp)



Le Keeper présente une vue d'ensemble des UTXO. Pour accéder à l'écran de sélection, cliquez sur _Select To Send_.



![img](assets/en/35.webp)



Vous pouvez sélectionner des pièces en les cochant en cliquant sur la commande appropriée. Lorsque vous avez terminé, cliquez sur _Envoyer_.



![img](assets/en/36.webp)



Bitcoin Keeper vous amène directement au menu _Envoyer_, où vous pouvez effectuer la transaction avec les UTXO sélectionnées.



![img](assets/en/37.webp)



## Hardware Wallet



Chacun des portefeuilles logiciels présentés dans ce guide peut être le Interface de surveillance de l'un de vos portefeuilles matériels. Cela signifie que le contrôle du Coin pour le dispositif de signature hors ligne est effectué avec les étapes vues jusqu'à présent.



### Recommandations générales



Le contrôle Coin est une pratique très efficace pour sélectionner les entrées de vos transactions. La sélection manuelle est encore plus efficace si, lors de l'achat/réception de vos fonds, vous avez bien étiqueté la source de vos Satoshis. Si vous souhaitez apprendre cette technique, je vous recommande le tutoriel suivant :



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Nous avons parlé précédemment de la "ségrégation des restes". Si vous voulez verrouiller les restes pour un traitement ultérieur et retrouver la confidentialité (swap sur Layer 2), vous devez prendre soin de les `étiqueter` chaque fois que vous en recevez un. Parmi les portefeuilles logiciels vus jusqu'à présent, seul Electrum colore graphiquement les restes de UTXO pour les rendre visibles d'un coup d'œil. D'autres, comme le Sparrow, vous montrent la chaîne dans le chemin de dérivation du UTXO individuel (`m/84'/0'/0'/1/11`).



Pour appliquer efficacement cette technique, pensez à toujours ajouter une description sur la monnaie que vous recevez : la personne à qui vous avez envoyé vos fonds (un paiement, un tutoriel, ou autre), connaît la Address associée à la monnaie et sait qu'elle vous appartient, puisqu'elle provient de la transaction que vous avez effectuée ensemble !