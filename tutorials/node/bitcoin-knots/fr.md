---
name: Bitcoin Knots
description: Comment lancer un nœud avec le client alternatif Bitcoin Knots ?
---
![cover](assets/cover.webp)

Bitcoin Knots est une implémentation alternative du protocole Bitcoin, dérivée de Bitcoin Core. Conçue et maintenue par Luke Dashjr, elle propose quelques fonctionnalités supplémentaires et des ajustements de règles de mempool, tout en restant compatible avec les autres nœuds du réseau. Bitcoin Knots intègre un portefeuille Bitcoin, mais il peut également être utilisé comme un simple noeud Bitcoin avec à côté d'autres logiciels de portefeuille.

## Pourquoi utiliser Knots plutôt que Core ?

Core est actuellement l'implémentaiton majoritaire du protocole Bitocin sur le réseau Bitcoin. En effet, le protocole Bitcoin n'est qu'un ensemble de règles, mais il faut un logiciel pour appliquer ces règles. Lorsqu'une machine fait tourner un de ces clients qui implémente le protocole Bitcoin, on appelle cela un noeud, et tous les noeuds forment le réseau Bitcoin.

Au cours de l'histoire de Bitcoin, il y a eu de nombreux clients différents dans la lignée du logiciel originial développé par Satoshi Nakamoto. Aujourd'hui (mars 2025), c'est le logiciel Bitcoin Core qui est ultra majoritaire, puisqu'environ 98% du réseau Bitcoin est constitué de noeuds qui font tourner ce logiciel.

Mais il existe également des clients alternatifs. Ces logiciels ne sont pas des noeuds d'Altcoin, comme Bitcoin Cash par exemple, puisqu'ils sont compatibles avec le reste du réseau Bitcoin. Ce sont simplement des logiciels différents qui permettent de faire tourner un noeud Bitcoin. Parmis ces client alternatif, le plus connu est Bitcoin Knots, puisqu'il représente actuellement 1,4% du réseau. Les autres clients alternatifs représentent une part infime.

01

Il peut y avoir principalement 2 raisons qui peuvent vous pousser à faire tourner un de ces clients plutôt que Core :
- Technique : ces clients ont souvent quelques options différentes avec Core, par exemple au niveau des règles de mempool qui régissent quelles transaction sont acceptées et diffusées par votre noeud. Il proposent également des interface graphiques différentes ;
- Politique : certains préfèrent utiliser ces clients alternatifs comme Knots pour des raisons qui ne sont pas techniques, par exemple pour soutenir le développement d'alternatives à Core et combattre le monopole à son échelle. Si un jour Core devient compromis, cela peut être intéressant non seulement d'avoir des clients alternatifs forts et bien maintenus, mais également de savoir comment utiliser ces clients alternatifs. Ou bien, certains font tourner Knots pour participer à un contre mouvement, parce qu'ils n'ont plus confiance en les développeurs de Core ou bien n'apprécient pas la gestion du client majoritaire.

## Installer Bitcoin Knots ?

Rendez-vous [sur le site officiel de Bitcoin Knots](https://bitcoinknots.org/#download) et téléchargez le logiciel en fonction de votre système d'exploitation. Téléchargez l'empreinte et les signatures pour pouvoir le vérifier. Vous pouvez également retrouver ces fichiers [sur le dépôt GitHub de Bitcoin Knots](https://github.com/bitcoinknots/bitcoin).

02

Avant d'installer le logiciel sur votre machine, je vous conseille vivement de vérifier son authenticité et son intégrité. Si vous ne savez pas comment le faire, vous pouvez suivre cet autre tutoriel : 

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Une fois le logiciel vérifié, vous pouvez l'installer en suivant les étapes sur le panneaux de configuration.

03

## Lancer l'IBD

Lors du premier démarrage de Bitcoin Knots, vous pourrez choisir le répertoire local dans lequel stocker les données du noeud (notamment la blockchain, l'UTXO set et les paramètres).

04

Vous avez également la possibilité d'élaguer les données de la blockchain, afin de ne conserver que les blocks les plus récents. Cette option vous permet de bien vérifier tous les blocs, mais de ne jamais dépasser la limite de stockgae que vous avez paramétré, en supprimant au fur et à mesure les blocs les plus vieux. Si vous disposez de uffisament de place sur votre disque (environ 650 go actuellement, mais cette valeur ne fait évidemment qu'augmenter), vous pouvez décocher cette case. Si vous êtes limités au niveau de votre espace de stockage, vous pouvez cocher cette option, et paramétrer une valeur maximale à ne pas dépasser.

Attention, si vous noeud est élagué et que vous l'utilisez pour sycnhorniser une récupération de portefeuille, vous ne pourrez pas retrouver les données de transactions antérieure au bloc le plus ancien que vous conservez en local. 

05

Vous avez également la possibilité d'activer l'option "Assume Valid". Cette option permet de sauter la vérification des signatures pour toutes les transactions incluses dans les blocs antérieurs à un certain bloc donné.

L'objectif d'Assume Valid est d'accélérer le processus de synchronisation initiale de votre nœud sans compromettre la sécurité, en supposant que la majorité du réseau ait déjà validé ces transactions dans le passé. Le seul vrai compromis pour le nœud est qu'en cas de vol antérieur de bitcoins, il ne sera pas averti. Cependant, il peut toujours s'assurer de l'exactitude de la quantité de bitcoins émis. Votre nœud poursuivra tout de même la vérification des signatures de transactions postérieures au bloc "Assume Valid". Cette approche repose sur l'hypothèse que si une transaction est acceptée par le réseau depuis assez longtemps sans contestation, il est improbable qu'elle soit frauduleuse.

Par exemple, ici, "Assume Valid" est paramétré avec le bloc n°855 000 `0000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138` publié le 1er août 2024. Cela signifie que lors de l'IBD, mon nœud ne vérifiera les signature qu'à partir de ce bloc.

06

Cliquez ensuite sur le bouton "OK" pour lancer l'*Inital Block Download*. Il faudra ensuite patienter le temps que votre nœud se synchronise. Si vous souhaitez reprendre la synchronisaiton plus tard, vous pouvez fermer le logiciel et éteindre votre ordinateur. La synchronisaiton reprendra sans problème là où vous en étiez.

07

## Paramétrer son nœud Bitcoin Knots

Cliquez sur l'onglet "Settings", puis le menu "Options".

08

Dans l'onglet "Main", vous trouverez les paramètres principaux de votre noeud :
- "Start..." vous permet de démarrer automatiquement votre noeud à chaque démarage de votre oridnateur afin de lancer immédiatement la synchronisation ;
- "Prune..." vous permet d'ajuster la limite de stockage pour les blocks si vous avez un noeud élagué ;
- "Database cash..." vous permet d'ajuster la limite maximale de mémoire vive que peut utiliser votre noeud sur votre ordinateur.
- Et enfin, vous pouvez cocher la case "Enable RPC server" si vous souhaitez vous connecter à votre Bitcoin Knots depuis un autre logiciel de portefeuille comme Sparrow Wallet par exemple.

09

Dans l'onglet "Wallet", vous retrouvez les options du portefeuille que vous pourrez créer par la suite directement sur Knots. Je vous conseille d'activer RBF et le coin control, et vous pouvez également choisir le type de script utilisé.

10

Dans "Network" vous avez les options réseau si vous avez besoin de les ajuster en fonciton de vos besoin.

11

L'onglet "Mempool" vous permet de paramétrer votre *Memory Pool*, notamment la manière dont les transaction non confirmées sont conservées en mémoire, et la taille de stockage que vous allouez à cette foncitonnalité (par défaut 300 MB).

12

L'onglet "Spam filtering" est une fonciotnnalité propre à Bitcoin Knots. Vous y trouverez de nombreux paramètres permettant d'ajuster les transacitons que vous acceptez de diffuser ou non. L'objectif ici est de limiter les conséquences de certaines utilisaitons marginales de Bitcoin, notamment les méta-protocoles, afin d'une part de combattre leur utilisation et d'autre part de ne pas surcharger votre noeud avec cela. C'est une prise de position politique, en fonciton de votre vision de Bitcoin.

Vous trouverez également des paramètres plus classiques comme par exemple le seuil de "Dust".

Dans tous les cas, ces paramètres agissent uniquement sur les règles de standardisation, ce qui signifie que votre noeud acceptera tout de même les trnsactions qui ne respectent pas ces paramètres, mais uniquement si elles sont incluses dans un bloc. Sinon, il ne pourrait pas être compatible avec le reste du réseau Bitcoin. Ces paramètres agissent uniquement sur la manière dont votre noeud traite les transactions non confirmées et les diffuse à ses pairs. Mais puisque Knots est minoritaire, dans les faits, se sont les règles de standardisation par défaut établies sur Bitcoin Core qui font loi.

13

L'onglet "Mining" vous permet de paramétrer la manière dont votre noeud participe au minage (si vous souhaitez qu'il y participe).

14

Et enfin, dans l'onglet "Display", vous trouverez des paramètres sur l'interface graphique, notamment la langue du logiciel.

15

## Créer un portefeuille Bitcoin

Une fois la synchronisation initiale terminée, votre noeud Bitcoin Knots est opérationnel. Vous pouvez maintenant soit le connecter à un autre logiciel de portefeuille, oubien utiliser le portefeuille chaud directement intégré au logiciel. Pour ce faire, cliquez sur le bouton "Create a new wallet".

16

Choisissez un nom pour votre portefeuille. Vous pouvez également le protéger avec une Passphrase BIP39 en cliquant sur "Encrypt Wallet". Puis, cliquez sur le bouton "Create".

17

Une passphrase BIP39 est un mot de passe optionnel que vous pouvez choisir librement, et qui vient s'ajouter à votre phrase mnémonique pour renforcer la sécurité du portefeuille. Avant de configurer cette option sur votre portefeuille, il est fortement recommandé de lire cet article pour bien comprendre le fonctionnement théorique de la passphrase et éviter les erreurs qui pourraient entraîner la perte de vos bitcoins :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si vous avez coché l'option pour la passphrase, choisissez maintenant une passphrase forte, et faites en une ou plusieurs sauvegarde sur un support physique.

18

Votre portefeuille Bitcoin est maintenant créé.

19

## Sauvegarder son portefeuille Bitcoin

Avant de recevoir vos premiers bitocins, il est important de réaliser une sauvegarde de votre portefeuille Bitcoin pour pouvoir récuéprer vos fonds en cas de perte ou de casse de votre ordinateur. Pour ce faire, cliquez sur l'onglet "File" puis "Backup wallet".

20

Cela va vous permettre de générer un fichier qui a lui seul, permet de restaurer tous vos bitcoins. Faites y donc très attention et sauvegardez-le sur un support externe à votre ordinateur.

## Recevoir des bitcoins

Cliquez sur le bouton "Receive".

21

Renseignez un "Label" sur votre adresse pour vous souvenir de son objectif et pouvoir faire du *Coin Control* par la suite. Vous pouvez également paramétrer à l'avance un montant spécifique à recevoir avec cette adresse, ou bien ajouter un message au payeur. Une fois l'adresse paramétrée, cliquez sur "Request payment".

22

Bitcoin Knots vous affiche une adresse de réception que vous pouvez copier ou scanner pour la transmettre au payeur.

23

Une fois la transaction diffusée, vous pouvez la voir dans le menu "Transactions".

24

## Envoyer des bitcoins





## Connecter son nœud à un autre logiciel

L'interface de Bitocin Knots pour le portefeuille Bitcoin n'est pas forcément la plus simple à utiliser, et reste limitée en options. Mais vous pouvez également utiliser votre noeud Bitcoin Knots avec un logiciel de gestion de portefeuille spécialisé afin d'avoir accès aux informations de la blockchain Bitcoin et diffuser vos transactions.

La procédure va être différente en fonction du logiciel de portefeuille que vous utilisez, mais il existe généralement 2 options : 
