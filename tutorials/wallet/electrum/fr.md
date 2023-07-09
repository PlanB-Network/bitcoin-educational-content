---
name: Electrum

description: Guide complet d'Electrum, de 0 à héros
---

![cover](assets/cover.png)

Description pour Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

# Portefeuille Bitcoin Electrum

> "Je dois dire que lorsque j'ai découvert ce guide, j'ai été choqué. Félicitations à Arman the Parman pour cela. Ce serait dommage de ne pas l'héberger ici et de le traduire dans autant de langues que possible. Honnêtement, des conseils de ce gars." Rogzy

Publication originale : https://armantheparman.com/electrum/

![Portefeuille de bureau Electrum (Mac / Linux) - téléchargement, vérification, connexion à votre nœud.](https://youtu.be/wHmQNcRWdHM)

![Effectuer une transaction Bitcoin avec Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Pourquoi Electrum ?

Il s'agit d'un guide détaillé sur l'utilisation du portefeuille Bitcoin Electrum, avec des solutions à tous ses pièges et particularités - quelque chose que j'ai développé après plusieurs années d'utilisation et d'enseignement de la sécurité/confidentialité du Bitcoin aux étudiants. Electrum n'est pas le meilleur portefeuille Bitcoin pour les personnes qui veulent tout garder aussi simple que possible et préfèrent rester au niveau débutant. Au contraire, il est destiné à la personne qui est, ou aspire à être, un utilisateur "avancé".

Pour le nouveau détenteur de Bitcoin, il est excellent à condition d'être supervisé par un utilisateur expérimenté pour lui montrer la voie. S'ils apprennent à l'utiliser seuls, cela serait sûr à condition qu'ils prennent leur temps et l'utilisent dans un environnement de test avec seulement un petit nombre de sats au départ. Ce guide soutient cette entreprise, mais il est également une bonne référence pour les autres.

> Avertissement : Ce guide est volumineux. N'essayez pas de tout faire en une journée. Il est préférable de sauvegarder le guide et de le consulter petit à petit.

## Téléchargement d'Electrum

Idéalement, utilisez un ordinateur dédié au Bitcoin pour vos transactions Bitcoin (Mon guide à ce sujet https://armantheparman.com/mint/) _(ÉGALEMENT disponible dans la section confidentialité)_. Il est possible de s'entraîner avec de petites sommes sur un ordinateur "sale" lorsque vous apprenez pour la première fois (qui sait combien de logiciels malveillants cachés votre ordinateur habituel a accumulés au fil des ans - vous ne voulez pas exposer vos portefeuilles Bitcoin à ceux-ci).

Obtenez Electrum depuis https://electrum.org/.

Cliquez sur l'onglet Télécharger en haut.

Cliquez sur le lien de téléchargement correspondant à votre ordinateur. Tout ordinateur Linux ou Mac peut utiliser le lien Python (cercle rouge). Un ordinateur Linux avec une puce Intel ou AMD peut utiliser l'Appimage (cercle vert ; c'est comme un fichier exécutable Windows). Un appareil Raspberry Pi a un microprocesseur ARM et ne peut utiliser que la version Python (cercle rouge), pas Appimage, même si les Pi fonctionnent sous Linux. Le cercle bleu est pour Windows et le cercle noir est pour Mac.

![image](assets/1.png)

## Vérification d'Electrum

Le but de "vérifier" le téléchargement est de s'assurer qu'aucun bit de données n'a été altéré. Cela vous empêche d'utiliser une version malveillante "piratée" du logiciel. Il est possible de sauter cette étape à condition d'utiliser uniquement la copie téléchargée pour s'entraîner, c'est-à-dire de ne pas utiliser de portefeuilles contenant de l'argent sérieux. Ensuite, lorsque vous êtes prêt à utiliser Electrum pour vos fonds réels, vous devez supprimer votre copie et recommencer, cette fois en vérifiant votre téléchargement.

Pour ce faire, nous utilisons des outils de cryptographie à clé publique / privée - gpg, dont nous avons écrit un guide ici (https://armantheparman.com/gpg/). L'outil gpg est inclus dans tous les systèmes d'exploitation Linux. Pour Mac et Windows, consultez le lien gpg pour obtenir les instructions de téléchargement.

En plus de télécharger le logiciel Electrum, pour des raisons de sécurité, vous avez également besoin de la SIGNATURE numérique du logiciel. Il s'agit d'une chaîne de texte (en réalité, un nombre encodé en texte) que le développeur a produit avec sa clé gpg PRIVÉE. En utilisant le programme gpg, nous pouvons ensuite "tester" la SIGNATURE par rapport à sa clé PUBLIQUE (créée à partir de la clé privée du développeur) à laquelle tout le monde a accès, par rapport au fichier de téléchargement.

En d'autres termes, avec les trois entrées (signature, clé publique et fichier de données), nous obtenons une sortie vraie ou fausse pour confirmer que le fichier n'a pas été altéré.

Pour obtenir la signature, cliquez sur le lien correspondant au fichier que vous avez téléchargé (voir les flèches colorées):

![image](assets/2.png)

En cliquant sur le lien, le fichier peut être automatiquement téléchargé dans votre dossier de téléchargements, ou il peut s'ouvrir dans le navigateur. S'il s'ouvre dans le navigateur, vous devez enregistrer le fichier. Vous pouvez faire un clic droit et sélectionner "enregistrer sous". Selon le système d'exploitation ou le navigateur, vous devrez peut-être faire un clic droit sur la zone d'espace blanc, pas sur le texte.

Voici à quoi ressemble le texte téléchargé. Vous pouvez voir qu'il y a plusieurs signatures - ce sont des signatures de différentes personnes. Vous pouvez vérifier chacune d'entre elles. Je vais vous montrer comment vérifier celle du développeur.

![image](assets/3.png)

Ensuite, vous devez obtenir la clé publique de ThomasV - c'est le principal développeur. Vous pouvez l'obtenir directement de lui, de son compte Keybase, de Github, ou de quelqu'un d'autre, d'un serveur de clés, ou du site Web Electrum.

Obtenir la clé publique à partir du site Web Electrum est en réalité la méthode la moins sécurisée, car si ce site Web est malveillant (la chose même que nous vérifions), pourquoi obtenir une clé publique à partir de celui-ci (la clé publique pourrait être fausse) ?

Pour simplifier les choses pour l'instant, je vais vous montrer comment l'obtenir à partir du site Web quand même, mais gardez cela à l'esprit. Voici la copie (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) sur GitHub avec laquelle vous pouvez la comparer.

Faites défiler un peu la page pour trouver le lien vers la clé publique de ThomasV (cercle rouge ci-dessous). Cliquez dessus et téléchargez-la, ou si cela ouvre un texte dans un navigateur, faites un clic droit pour enregistrer.

![image](assets/4.png)

Vous avez maintenant 3 nouveaux fichiers, probablement tous dans le dossier de téléchargements. Peu importe où ils se trouvent, mais le processus est plus facile si vous les mettez tous dans le même dossier.

Les trois fichiers :

1. Le téléchargement d'Electrum
2. Le fichier de signature (généralement, il a le même nom de fichier que le téléchargement d'Electrum avec une extension ".asc")
3. La clé publique de ThomasV.

Ouvrez un terminal sur Mac ou Linux, ou une invite de commande (CMD) sur Windows.

Accédez au répertoire des téléchargements (ou à l'endroit où vous avez mis les trois fichiers). Si vous n'avez aucune idée de ce que cela signifie, apprenez à partir de cette courte vidéo pour Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) et celle-ci pour Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). N'oubliez pas que sur les ordinateurs Linux, les noms de répertoire sont sensibles à la casse.

Dans le terminal, tapez ceci pour importer la clé publique de ThomasV dans le "trousseau" de votre ordinateur (le trousseau est un concept abstrait - en réalité, il s'agit simplement d'un fichier sur votre ordinateur) :

```
gpg --import ThomasV.asc
```

Assurez-vous que le nom du fichier correspond à ce que vous avez téléchargé. Remarquez également qu'il s'agit d'un double tiret, pas d'un simple tiret. Notez également qu'il y a un espace avant et après "--import". Ensuite, appuyez sur <enter>.

Le fichier devrait être importé. Si vous obtenez une erreur, vérifiez que vous êtes dans le répertoire où le fichier se trouve réellement. Pour vérifier dans quel répertoire vous vous trouvez (sur Mac ou Linux), tapez pwd. Pour voir quels fichiers se trouvent dans le répertoire où vous vous trouvez (sur Mac ou Linux), tapez ls. Vous devriez voir le fichier texte "ThomasV.asc" répertorié, éventuellement parmi d'autres fichiers.

Ensuite, nous exécutons la commande pour vérifier la signature.

```
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Remarquez qu'il y a 4 "éléments" ici, séparés chacun par un espace. J'ai mis en gras le texte alternativement pour vous aider à voir. Les quatre éléments sont :

1. le programme gpg
2. l'option --verify
3. le nom du fichier de la signature
4. le nom du programme

Il est intéressant de noter que parfois vous pouvez omettre le 4e élément et l'ordinateur devine ce que vous voulez dire. Je ne suis pas sûr, mais je crois que cela ne fonctionne que si les noms de fichiers ne diffèrent que par le "asc" à la fin.

Ne copiez pas simplement les noms de fichiers que j'ai indiqués ici - assurez-vous qu'ils correspondent au nom du fichier que vous avez sur votre système.

Appuyez sur <enter> pour exécuter la commande. Vous devriez voir une "bonne signature de ThomasV" pour indiquer le succès. Il y aura quelques erreurs car nous n'avons pas les clés publiques des autres signatures qui sont contenues dans le fichier de signature (ce système de combinaison des signatures dans un seul fichier peut changer dans les versions ultérieures). De plus, il y a un avertissement en bas que nous pouvons ignorer (cela nous alerte que nous n'avons pas explicitement indiqué à l'ordinateur que nous faisons confiance à la clé publique de ThomasV).

Maintenant, nous avons une copie vérifiée d'Electrum qui est sûre à utiliser.

## Exécution d'Electrum

### Exécution d'Electrum si vous utilisez Python

Si vous avez téléchargé la version Python, voici comment la faire fonctionner. Vous verrez sur la page de téléchargement ceci :

![image](assets/5.png)

Pour Linux, il est conseillé de d'abord mettre à jour votre système :

```
sudo apt-get update
sudo apt-get upgrade
```

Copiez le texte jaune surligné, collez-le dans le terminal et appuyez sur <enter>. On vous demandera votre mot de passe, éventuellement une confirmation pour continuer, puis il installera ces fichiers ("dépendances").

Vous devrez également extraire le fichier compressé dans un répertoire de votre choix. Vous pouvez le faire avec l'interface utilisateur graphique ou en ligne de commande (commande surlignée en rose) - rappelez-vous que vos noms de fichiers peuvent être différents. (Notez que lorsque nous avons vérifié le téléchargement dans la section précédente, c'était le fichier zip que nous avons vérifié, pas le répertoire extrait.)

Il y a une option pour "installer" en utilisant le programme PIP, mais cela est inutile et ajoute des étapes supplémentaires et l'installation de fichiers. Exécutez simplement le programme en utilisant le terminal pour contourner tout cela.

Les étapes (Linux) sont les suivantes :

1. accédez au répertoire où les fichiers sont extraits
2. tapez : ./run_electrum

Sur un Mac, les étapes sont les mêmes, mais vous devrez peut-être d'abord installer Python3 et utiliser cette commande pour l'exécuter :

```
python3 ./run_electrum
```

Une fois que Electrum est en cours d'exécution, la fenêtre du terminal restera ouverte. Si vous la fermez, le programme Electrum se terminera. Il suffit de la réduire pendant que vous utilisez Electrum.

### Exécution d'Electrum avec l'Appimage

C'est un peu plus facile, mais pas aussi facile qu'un fichier exécutable Windows. Selon la version de Linux que vous utilisez, par défaut, les fichiers Appimage peuvent avoir des attributs définis de manière à ce que l'exécution soit interdite par le système. Nous devons changer cela. Si votre Appimage fonctionne, vous pouvez passer cette étape. Accédez à l'endroit où se trouve le fichier, en utilisant le terminal, puis exécutez cette commande :

```
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

"sudo" donne des privilèges de superutilisateur ; "chmod" est une commande pour changer le mode, en modifiant qui peut lire, écrire ou exécuter ; "ug+x" signifie que nous modifions l'utilisateur et le groupe pour autoriser l'exécution.

Ajustez le nom du fichier en fonction de votre version.

Ensuite, Electrum s'exécutera en double-cliquant sur l'icône de l'Appimage.

### Exécution d'Electrum avec Mac

Double-cliquez simplement sur le fichier téléchargé (c'est un "lecteur"). Une fenêtre s'ouvrira. Faites glisser l'icône d'Electrum dans la fenêtre sur votre bureau, ou où vous souhaitez conserver le programme. Vous pouvez ensuite "éjecter" le lecteur et supprimer le lecteur (fichier téléchargé).

Pour exécuter le programme, double-cliquez simplement dessus. Vous pouvez rencontrer des erreurs "nanny" spécifiques à Mac qu'il faut contourner.

### Exécution d'Electrum avec Windows

Malgré le fait que je déteste Windows par-dessus tout, c'est la méthode la plus simple. Double-cliquez simplement sur le fichier exécutable pour l'exécuter.

## Commencez avec un portefeuille fictif

Lorsque vous chargez Electrum pour la première fois, une fenêtre s'ouvrira comme ceci :

![image](assets/6.png)

Nous sélectionnerons votre serveur manuellement plus tard, mais pour l'instant, laissez les paramètres par défaut et connectez-vous automatiquement.

Ensuite, créez un portefeuille fictif - ne mettez jamais de fonds dans ce portefeuille. Le but de ce portefeuille fictif est de progresser dans le logiciel et de s'assurer que tout fonctionne bien avant de charger votre vrai portefeuille. Nous essayons d'éviter de divulguer accidentellement la confidentialité avec un vrai portefeuille. Si vous vous entraînez simplement, le portefeuille que vous créez peut être considéré comme un portefeuille fictif de toute façon.

Vous pouvez laisser le nom par défaut "default_wallet" ou le changer selon vos préférences, puis cliquez sur suivant. Plus tard, si vous avez plusieurs portefeuilles, vous pouvez les trouver et les ouvrir à cette étape en cliquant d'abord sur "Choisir..."

![image](assets/7.png)

Choisissez "Portefeuille standard" et <Suivant> :

![image](assets/8.png)

Ensuite, sélectionnez "J'ai déjà une graine". Je ne veux pas que vous preniez l'habitude de créer une graine Electrum, car elle utilise son propre protocole qui n'est pas compatible avec d'autres portefeuilles - c'est pourquoi nous ne cliquons pas sur "nouvelle graine".

![image](assets/9.png)

Rendez-vous sur https://iancoleman.io/bip39/ et créez une graine fictive. Tout d'abord, changez le nombre de mots à 12 (ce qui est une pratique courante), puis cliquez sur "générer" et copiez les mots dans la boîte dans votre presse-papiers.

![image](assets/10.png)

Ensuite, collez les mots dans Electrum. Voici un exemple :

![image](assets/11.png)

Electrum recherchera des mots correspondant à son propre protocole. Nous devons contourner cela. Cliquez sur options, et sélectionnez BIP39 Seed :

![image](assets/12.png)'

La graine devient alors valide. (Avant cela, Electrum s'attendait à une graine Electrum, donc cette graine était considérée comme invalide). Avant de cliquer sur suivant, remarquez le texte qui dit "Checksum OK". Il est important (pour le vrai portefeuille que vous pourriez utiliser ultérieurement) que vous le voyiez avant de continuer, car cela confirme la validité de la graine que vous avez entrée. L'avertissement en bas peut être ignoré, c'est la plainte du développeur d'Electrum à propos de BIP39 et de leurs revendications "FUD"ey" selon lesquelles leur version (qui n'est pas compatible avec d'autres portefeuilles) est supérieure.

> Un petit détour pour un avertissement important. Le but de la somme de contrôle est de s'assurer que vous avez entré votre graine sans erreur de frappe. La somme de contrôle est la dernière partie de la graine (le 12e mot est la somme de contrôle) qui est mathématiquement déterminée par la première partie de la graine (11 mots). Si vous faisiez une erreur de frappe au début, le mot de somme de contrôle ne correspondra pas mathématiquement, et le logiciel de portefeuille vous alertera avec un avertissement. Cela ne signifie pas que la graine ne peut pas être utilisée pour créer un portefeuille Bitcoin fonctionnel. Imaginez créer un portefeuille avec une erreur de frappe, charger le portefeuille avec des bitcoins, puis un jour vous pourriez avoir besoin de restaurer le portefeuille, mais lorsque vous le faites, vous ne recréez pas l'erreur de frappe - vous restaurerez le mauvais portefeuille ! Il est assez dangereux qu'Electrum vous permette de continuer à créer un portefeuille si votre somme de contrôle est invalide, alors soyez averti, c'est votre responsabilité de vous en assurer. D'autres portefeuilles ne vous permettront pas de continuer, ce qui est beaucoup plus sûr. C'est l'une des choses que je veux dire quand je dis qu'Electrum est bon à utiliser, une fois que vous avez appris à l'utiliser correctement (les développeurs d'Electrum devraient corriger cela).

Remarquez que si vous souhaitez ajouter une phrase secrète, la possibilité de la sélectionner se trouve dans cette fenêtre d'options, juste en haut.

Après avoir cliqué sur OK, vous serez ramené à l'endroit où vous avez saisi la phrase de la graine. Si vous avez sélectionné une option de phrase secrète, vous NE LA SAISISSEZ PAS avec les mots de la graine (la demande à cet effet viendra ensuite).

Si vous n'avez pas demandé de phrase secrète, vous verrez ensuite cet écran - plus d'options pour le type de script de votre portefeuille et le chemin de dérivation que vous pouvez apprendre ici (https://armantheparman.com/public-and-private-keys/), mais laissez simplement les valeurs par défaut et continuez.

![image](assets/13.png)

> Pour des informations supplémentaires : La première option vous permet de choisir entre l'héritage (adresses commençant par "1"), le pay-to-script-hash (adresses commençant par "3") ou bech32/native segwit (adresses commençant par "bc1q"). Au moment de la rédaction, Electrum ne prend pas encore en charge taproot (adresses commençant par "bc1p"). La deuxième option dans cette fenêtre vous permet de modifier le chemin de dérivation. Je vous suggère de ne jamais le modifier, surtout avant de comprendre ce que cela signifie. Les gens insisteront sur l'importance d'écrire le chemin de dérivation afin de pouvoir récupérer votre portefeuille si nécessaire, mais si vous le laissez par défaut, vous devriez probablement vous en sortir, donc ne paniquez pas - mais il est toujours bon de prendre l'habitude d'écrire le chemin de dérivation.

Ensuite, vous aurez la possibilité d'ajouter un MOT DE PASSE. Ne confondez pas cela avec "PHRASE SECRÈTE". Un mot de passe verrouille le fichier sur votre ordinateur. Une phrase secrète fait partie de la composition de la clé privée. Comme il s'agit d'un portefeuille fictif, vous pouvez laisser le mot de passe vide et continuer.

![image](assets/14.png)

Vous recevrez une fenêtre contextuelle concernant les notifications de nouvelle version (je vous suggère de sélectionner non). Le portefeuille se générera alors et sera prêt à être utilisé (mais n'oubliez pas, ce portefeuille est destiné à être supprimé, c'est juste un portefeuille fictif).

![image](assets/15.png)

Il y a quelques choses que je vous suggère de faire pour configurer l'environnement logiciel (nécessaire une seule fois) :

### Changer les unités en BTC

Allez dans le menu supérieur, outils -> préférences d'Electrum, et là, sous l'onglet général, vous trouverez l'option pour changer l'"unité de base" en BTC.
Activer l'onglet Adresses et Coins

Allez dans le menu supérieur, affichage, et sélectionnez "afficher les adresses". Ensuite, revenez à affichage et sélectionnez "afficher les coins".

### Activer Oneserver

Par défaut, Electrum se connecte à un nœud aléatoire. Il se connecte également à de nombreux autres nœuds secondaires. Je ne suis pas sûr des données échangées avec ces nœuds secondaires, mais nous ne voulons pas que cela se produise, pour des raisons de confidentialité. Même si vous spécifiez un nœud, par exemple votre propre nœud, ces multiples autres nœuds seront également connectés, et je ne suis pas sûr des informations partagées. Quoi qu'il en soit, il est facile de l'empêcher. Avant de vous montrer comment spécifier votre propre nœud, nous allons forcer Electrum à se connecter à un seul serveur à la fois.

> Il y a un moyen de le faire en spécifiant "oneserver" depuis la ligne de commande, mais je ne recommande pas cette méthode. Je vais montrer une alternative que je pense plus facile à long terme, et moins susceptible de vous connecter accidentellement à d'autres nœuds.

La raison pour laquelle nous utilisons un portefeuille fictif est que si nous avions chargé notre vrai portefeuille, avec nos vrais bitcoins, nous nous serions connectés involontairement à un nœud aléatoire à présent même si nous avons sélectionné "définir le serveur manuellement" au départ, il se connecte toujours à ces autres nœuds secondaires pour une raison quelconque (hé les développeurs d'Electrum, vous devriez corriger cela). Si notre portefeuille était privé, ce serait une catastrophe.

Nous ne pouvons pas non plus effectuer les étapes que je vais vous montrer ci-dessous sans charger au préalable un certain type de portefeuille. (Nous allons modifier un fichier de configuration qui ne se remplit et ne se prépare à l'édition que lorsqu'un portefeuille est chargé).

**Fermez Electrum (IMPORTANT, si vous ne le faites pas, les modifications que vous apportez seront effacées).**

### Fichier de configuration LINUX/MAC

Ouvrez le terminal sous Linux ou Mac (instructions pour Windows plus tard) :

Vous devriez automatiquement être dans le dossier home. À partir de là, accédez au dossier de configuration caché d'Electrum (cela diffère de l'emplacement de l'application).

```
cd .electrum
```

Remarquez le point avant "electrum" qui indique qu'il s'agit d'un dossier caché.

Une autre façon d'y accéder est de taper :

```
cd ~/.electrum
```

où "~" représente le chemin de votre répertoire home. Vous pouvez voir le chemin complet de votre répertoire actuel avec la commande "pwd".

Une fois dans le répertoire ".electrum", tapez "nano config" et appuyez sur <enter>.

Un éditeur de texte s'ouvrira (appelé nano) avec le fichier de configuration ouvert. La souris ne fonctionne pas beaucoup ici. Utilisez les touches fléchées pour accéder à la ligne qui dit :

```
"oneserver": false,
```

Changez "false" en "true" ; et ne perturbez pas la syntaxe (ne supprimez pas la virgule ou le point-virgule).

Appuyez sur <ctrl> x pour quitter, puis sur "y" pour enregistrer, puis <enter> pour confirmer le changement sans modifier le nom du fichier.
Maintenant, exécutez à nouveau Electrum. Ensuite, cliquez sur le cercle en bas à droite, ce qui ouvre les paramètres réseau. Ensuite, près du haut dans l'onglet aperçu, vous verrez "connecté à 1 nœud" - cela indique le succès.
Juste en dessous, vous verrez un champ de texte et l'adresse du serveur est là. Vous êtes actuellement connecté à ce nœud aléatoire. Plus d'informations sur la connexion à un nœud dans la prochaine section.

### Fichier de configuration Windows

Le fichier de configuration Windows est un peu plus difficile à trouver. Le répertoire est :

```
C:/Users/Parman/AppData/Roaming/Electrum
```

Évidemment, vous devez changer "Parman" par votre propre nom d'utilisateur pour l'ordinateur.

Dans ce dossier, vous trouverez le fichier de configuration. Ouvrez-le avec un éditeur de texte et modifiez la ligne :

```
"oneserver": false,
```

Changez "false" en "true" ; ne perturbez pas la syntaxe (ne supprimez pas la virgule ou le point-virgule).

Ensuite, enregistrez le fichier et quittez.

## Connecter Electrum à un nœud

Ensuite, nous voulons connecter notre portefeuille fictif à un nœud de notre choix. Si vous n'êtes pas prêt à exécuter un nœud, vous pouvez faire l'une des choses suivantes :

1. Se connecter au nœud personnel d'un ami (nécessite Tor)
2. Se connecter au nœud d'une entreprise de confiance
3. Se connecter à un nœud aléatoire (non recommandé).

Au fait, voici les instructions pour exécuter votre propre nœud, et voici les raisons pour lesquelles vous devriez le faire (tous les tutoriels dans la section Node ou dans nos cours gratuits).

### Se connecter au nœud d'un ami via Tor (Guide à venir.)

### Se connecter au nœud d'une entreprise de confiance

La seule raison de le faire serait si vous devez accéder à la blockchain et que vous n'avez pas votre propre nœud disponible (ou celui d'un ami).

Connectons-nous au nœud de Bitaroo - On nous dit qu'ils ne collectent pas de données. Ils sont une bourse Bitcoin uniquement, gérée par un passionné de Bitcoin. Se connecter à eux implique un peu de confiance, mais c'est mieux que de se connecter à un nœud aléatoire, qui pourrait être une entreprise de surveillance.

Accédez aux paramètres réseau en cliquant sur le cercle dans la partie inférieure droite de la fenêtre du portefeuille (le rouge indique une absence de connexion, le vert indique une connexion, et le bleu indique une connexion via Tor).

![image](assets/16.png)

Une fois que vous avez cliqué sur l'icône du cercle, une fenêtre contextuelle apparaîtra : Votre portefeuille affichera "connecté à 1 nœud" car nous l'avons forcé plus tôt.

Décochez la case "sélectionner le serveur automatiquement", puis dans le champ Serveur, saisissez les détails de Bitaroo comme indiqué :

![image](assets/17.png)

Fermez la fenêtre, et maintenant nous devrions être connectés au nœud de Bitaroo. Pour confirmer, le cercle devrait être vert. Cliquez dessus à nouveau et vérifiez que les détails du serveur ne sont pas revenus à un nœud aléatoire.

### Se connecter à votre propre nœud

Si vous avez votre propre nœud, c'est génial. Si vous avez seulement Bitcoin Core et pas un serveur Electrum en plus, vous ne pourrez pas encore connecter un portefeuille Electrum à votre nœud.

> Note : Le serveur Electrum et le portefeuille Electrum sont des choses différentes. Le serveur est un logiciel requis pour que le portefeuille Electrum puisse communiquer avec la blockchain Bitcoin - Je ne sais pas pourquoi cela a été conçu de cette façon - peut-être pour la vitesse, mais je pourrais me tromper.
> Si vous utilisez un logiciel de nœud comme MyNode (celui que je recommande aux débutants), Raspiblitz (recommandé pour les utilisateurs plus avancés) ou Umbrel (que je ne recommande pas encore personnellement car j'ai rencontré trop de problèmes), vous pourrez connecter votre portefeuille simplement en entrant l'adresse IP de l'ordinateur (Raspberry Pi) sur lequel le nœud est exécuté, suivie de deux points et de 50002, comme indiqué sur l'image de la section précédente. (Plus bas, je vous montrerai comment trouver l'adresse IP de votre nœud).
> Ouvrez les paramètres réseau (cliquez sur le cercle vert ou rouge en bas à droite). Décochez la case "sélectionner le serveur automatiquement", puis saisissez votre adresse IP comme je l'ai fait (la vôtre sera différente, mais les deux points et "50002" doivent être identiques).

![image](assets/18.png)

Fermez la fenêtre, et maintenant nous devrions être connectés à votre nœud. Pour vérifier, cliquez à nouveau sur le cercle et vérifiez que les détails du serveur n'ont pas été modifiés pour revenir à un nœud aléatoire.

Parfois, malgré avoir tout fait correctement, la connexion peut être refusée. Voici quelques choses à essayer...

- Mettez à jour vers une version plus récente d'Electrum et de votre logiciel de nœud.
- Essayez de supprimer le dossier de cache dans le répertoire ".electrum".
- Essayez de changer le port de 50002 à 50001 dans les paramètres réseau.
- Utilisez ce guide pour vous connecter en utilisant Tor comme alternative (https://armantheparman.com/tor/).
- Réinstallez le serveur Electrum sur le nœud.

## TROUVER L'ADRESSE IP DE VOTRE NŒUD

Une adresse IP n'est pas quelque chose que l'utilisateur moyen sait généralement comment rechercher et utiliser. J'ai aidé de nombreuses personnes à exécuter un nœud et à connecter leurs portefeuilles au nœud, et un obstacle fréquent semble être la recherche de son adresse IP.

Pour MyNode, vous pouvez taper dans une fenêtre de navigateur :

```
mynode.local
```

Parfois, "mynode.local" ne fonctionne pas (assurez-vous de ne pas le taper dans la barre de recherche Google). Pour forcer la barre de navigation à reconnaître votre texte comme une adresse et non une recherche, précédez le texte de http://

comme ceci :

```
http://mynode.local
```

Si cela ne fonctionne pas, essayez avec un "s", comme ceci :

```
https://mynode.local
```

Cela accédera à l'appareil, et vous pouvez cliquer sur le lien des paramètres (voir mon "cercle" bleu ci-dessous) pour afficher cette page où se trouve l'adresse IP :

![image](assets/19.png)

Cette page se chargera et vous verrez l'adresse IP du nœud (cercle bleu).

![image](assets/20.png)

Ensuite, à l'avenir, vous pourrez taper 192.168.0.150 ou http://192.168.0.150 dans votre navigateur.

Pour le Raspiblitz (lorsqu'il n'est pas connecté à un écran), vous avez besoin d'une méthode différente (qui fonctionne également pour MyNode) :

Connectez-vous à la page web de votre routeur - ici, vous trouverez l'adresse IP de tous vos appareils connectés. La page web du routeur sera une adresse IP que vous entrez dans un navigateur web. La mienne est :

    http://192.168.0.1

Pour obtenir les identifiants de connexion au routeur, vous pouvez les trouver dans le manuel d'utilisation ou parfois même sur une étiquette apposée sur le routeur lui-même. Recherchez le nom d'utilisateur et le mot de passe. Si vous ne pouvez pas les trouver, essayez Utilisateur : "admin" Mot de passe : "password".
Si vous parvenez à vous connecter, vous verrez vos appareils connectés et à partir de leurs noms, il peut être clair lequel est votre nœud. L'adresse IP sera là.

### Si les deux premières méthodes échouent, la dernière fonctionnera mais elle est fastidieuse :

Tout d'abord, trouvez l'adresse IP de n'importe quel appareil de votre réseau (l'ordinateur actuel fera l'affaire).

Sur un Mac, vous le trouverez dans les préférences réseau :

![image](assets/21.png)

Nous nous intéressons aux 4 premiers éléments (192.168.0), pas au 4e élément, le "166" que vous voyez sur l'image (le vôtre sera différent).

Pour Linux, utilisez la ligne de commande :

```
ifconfig | grep inet
```

Cette ligne verticale est le symbole "pipe" et vous le trouverez en dessous de la touche <delete>. Vous verrez une sortie et une adresse IP. (Ignorez 127.0.0.1, ce n'est pas ça, et ignorez le masque réseau)

Pour Windows, ouvrez l'invite de commandes (cmd) et tapez :

```
ipconfig/all
```

et appuyez sur Entrée. L'adresse IP se trouve dans la sortie.

C'était la partie facile. La partie difficile consiste maintenant à trouver l'adresse IP de votre nœud - nous devons deviner par force brute. Disons par exemple que l'adresse IP de votre ordinateur commence par 192.168.0.xxx, alors pour votre nœud, dans un navigateur, essayez :

```
https://192.168.0.2
```

Le nombre le plus petit possible est 2 (0 signifie n'importe quel appareil, et 1 appartient au routeur) et le plus élevé, je crois, est 255 (cela se trouve être 11111111 en binaire, le plus grand nombre contenu dans 1 octet).

Un par un, progressez jusqu'à 255. Finalement, vous vous arrêterez au bon numéro qui chargera votre page MyNode (ou la page RaspiBlitz). Ensuite, vous saurez quel numéro entrer dans les paramètres réseau d'Electrum pour vous connecter à votre nœud.

Cela ressemblera à quelque chose comme ça (assurez-vous d'inclure les deux-points et le numéro qui suit) :

![image](assets/22.png)

> Il est utile de savoir que ces adresses IP sont INTERNES à votre réseau domestique. Personne à l'extérieur ne peut les voir et elles ne sont pas sensibles. Elles sont un peu comme des extensions téléphoniques dans une grande organisation qui vous dirigent vers différents téléphones.

## Supprimer le portefeuille factice

Maintenant, nous nous sommes connectés avec succès à un seul et unique nœud. C'est ainsi qu'Electrum se chargera par défaut à partir de maintenant. Vous devriez maintenant supprimer le portefeuille factice (Menu : fichier -> supprimer), au cas où vous enverriez accidentellement des fonds à ce portefeuille non sécurisé (il est non sécurisé car nous ne l'avons pas créé de manière sûre).

## Créer un portefeuille de pratique

Après avoir supprimé le portefeuille factice, recommencez et créez-en un nouveau, de la même manière, mais cette fois, notez les mots de la graine et gardez-les assez en sécurité.

Il est bon d'apprendre comment Electrum fonctionne avec ce portefeuille de pratique, sans le matériel encombrant (nécessaire pour une sécurité élevée). Ne mettez qu'une petite quantité de bitcoin dans ce portefeuille - supposez que vous perdrez cet argent. Une fois compétent, apprenez ensuite à utiliser Electrum avec un portefeuille matériel.

Dans le nouveau portefeuille que vous avez créé, vous verrez une liste d'adresses. Les adresses vertes sont appelées "adresses de réception". Elles sont le produit de 3 choses :

- La phrase de la graine
- La phrase secrète
- Le chemin de dérivation

Votre nouveau portefeuille dispose d'un ensemble d'adresses de réception qui peuvent être créées mathématiquement et de manière reproductible par n'importe quel portefeuille logiciel disposant de la graine, de la phrase de passe et du chemin de dérivation. Il y en a 4,3 milliards ! Plus que ce dont vous aurez besoin. Electrum ne vous montre que les 20 premières, puis davantage au fur et à mesure de leur utilisation.

Plus d'informations sur les clés privées Bitcoin peuvent être trouvées dans ce guide.

![image](assets/23.png)

C'est très différent de certains autres portefeuilles qui ne présentent qu'une seule adresse à la fois.

Parce que vous avez saisi la phrase de la graine pour créer ce portefeuille, Electrum dispose de la clé privée pour chacune des adresses, et il est possible de dépenser à partir de ces adresses.

Notez également qu'il existe des adresses jaunes, appelées "adresses de changement" - Il s'agit simplement d'un autre ensemble d'adresses provenant d'une branche mathématique différente (4,3 milliards de celles-ci existent également). Elles sont utilisées par le portefeuille pour renvoyer automatiquement les fonds excédentaires dans le portefeuille en tant que monnaie de rendu. Par exemple, si vous prenez 1,5 bitcoin et en dépensez 0,5 chez un commerçant, les 1,0 restants doivent aller quelque part. Votre portefeuille les dépensera sur la prochaine adresse de changement jaune vide - sinon, cela ira au mineur ! Pour plus d'informations à ce sujet (UTXOs), consultez ce guide. (https://armantheparman.com/utxo/)

Ensuite, retournez sur le site de clé privée d'Ian Colman et saisissez la graine (au lieu d'en générer une). Vous verrez que les informations de clé privée et de clé publique ci-dessous changent ; tout ce qui se trouve en dessous dépend des éléments ci-dessus sur la page.

> N'oubliez pas que vous ne devez "jamais" saisir la graine sur un ordinateur pour votre véritable portefeuille Bitcoin - les logiciels malveillants peuvent la voler. Nous utilisons simplement un portefeuille d'entraînement, à des fins d'apprentissage, donc c'est bien pour le moment.

Faites défiler vers le bas et modifiez le chemin de dérivation en BIP84 (segwit) pour correspondre à votre portefeuille Electrum en cliquant sur l'onglet BIP84.

![image](assets/24.png)

En dessous, vous verrez la clé privée étendue du compte et la clé publique étendue du compte :

![image](assets/25.png)

Allez dans Electrum et comparez-les. Il y a un menu en haut, portefeuille -> informations :

![image](assets/26.png)

Cela apparaît :

![image](assets/27.png)

Remarquez que les deux clés publiques correspondent.

Ensuite, comparez les adresses. Retournez sur le site d'Ian Coleman et faites défiler vers le bas :

![image](assets/28.png)

Remarquez qu'elles correspondent aux adresses dans Electrum.

Maintenant, nous allons vérifier les adresses de changement. Remontez un peu vers le chemin de dérivation et changez le dernier 0 en 1 :

![image](assets/29.png)

Maintenant, faites défiler vers le bas et comparez les adresses avec les adresses jaunes dans Electrum.

Pourquoi avons-nous fait tout cela ?

Nous avons pris les mots de la graine et les avons passés à deux programmes logiciels indépendants différents pour nous assurer qu'ils nous donnaient les mêmes informations. Cela réduit considérablement le risque que du code malveillant se cache à l'intérieur et nous donne de fausses clés privées ou publiques, ou adresses.

La prochaine étape consiste à recevoir un petit test et à le dépenser dans le portefeuille d'une adresse à une autre.

## Test du portefeuille (Apprenez à l'utiliser)

Ici, je vais vous montrer comment recevoir un UTXO dans votre portefeuille, puis le déplacer (le dépenser) vers une autre adresse dans le portefeuille. Il s'agit d'un montant très faible que nous ne nous soucierons pas de perdre.

Cela a plusieurs objectifs.

- Cela prouvera que vous avez le pouvoir de dépenser des pièces dans le nouveau portefeuille.
- Il démontrera comment utiliser le logiciel Electrum pour effectuer une dépense (et certaines fonctionnalités), avant d'ajouter une complexité supplémentaire pour des raisons de sécurité (en utilisant un portefeuille matériel ou un ordinateur déconnecté de l'internet).
- Il renforcera l'idée que vous avez plusieurs adresses parmi lesquelles choisir pour recevoir et dépenser, dans le même portefeuille.

Ouvrez votre portefeuille de test Electrum et cliquez sur l'onglet "Adresses", puis faites un clic droit sur la première adresse et sélectionnez "Copier" -> "Adresse":

![image](assets/30.png)

L'adresse est maintenant dans la mémoire de votre ordinateur.

Maintenant, allez sur une plateforme d'échange où vous avez des bitcoins, et retirons une petite somme vers cette adresse, disons 50 000 sats. Je vais utiliser Coinbase comme exemple car c'est la plateforme d'échange la plus couramment utilisée, même si elle est ennemie de Bitcoin, et je suis dégoûté de me connecter à un ancien compte abandonné à cette fin.

Connectez-vous et cliquez sur le bouton "Envoyer/Recevoir", qui se trouve actuellement en haut à droite de la page web.

![image](assets/31.png)

Évidemment, je n'ai pas de fonds sur Coinbase, mais imaginez simplement qu'il y en a et suivez les étapes : Collez l'adresse d'Electrum dans le champ "À" comme je l'ai fait. Vous devrez également sélectionner un montant (je suggère environ 50 000 sats). Ne mettez pas de "message facultatif" - Coinbase collecte suffisamment de vos données (et les vend), il n'est donc pas nécessaire de les aider. Enfin, cliquez sur "Continuer". Après cela, je ne sais pas quels autres pop-ups vous obtiendrez, vous êtes seul, mais la méthode est similaire pour toutes les plateformes d'échange.

![image](assets/32.png)

Selon la plateforme d'échange, vous verrez peut-être les sats dans votre portefeuille immédiatement, ou il peut y avoir un délai de quelques heures/jours.

Notez qu'Electrum vous montrera les coins reçus même s'ils n'ont pas été confirmés sur la blockchain. Les coins que vous avez sont lus à partir de la liste d'attente d'un nœud Bitcoin, ou "mempool". Lorsqu'ils sont inclus dans un bloc, vous verrez les fonds confirmés.

Maintenant que nous avons un UTXO dans notre portefeuille, nous devrions le labéliser. Seul nous pouvons voir ce label, cela n'a rien à voir avec le registre public. Tous nos labels Electrum ne sont visibles que sur l'ordinateur que nous utilisons. Nous pouvons en fait enregistrer un fichier et l'utiliser pour restaurer tous nos labels sur un autre ordinateur exécutant le même portefeuille.

### Créer un label pour un UTXO

J'avais besoin d'un don pour ce portefeuille de test, merci à @Sathoarder de m'avoir fourni un UTXO en direct (10 000 sats), et une autre personne (anonyme) a fait un don à la même adresse (5 000 sats). Remarquez qu'il y a 15 000 sats dans le solde de la première adresse, et un total de 2 transactions (colonne de droite). En bas, le solde est de 10 000 sats confirmés, et 5 000 sats sont non confirmés (encore dans le mempool).

![image](assets/33.png)

Maintenant, si nous allons à l'onglet "Coins", nous pouvons voir deux "coins reçus" ou UTXOs. Ils sont tous les deux dans la même adresse.

![image](assets/34.png)

En revenant à l'onglet "Adresses", si vous double-cliquez sur la zone "labels" à côté de l'adresse, vous pourrez entrer du texte, puis appuyez sur <enter> pour enregistrer :

![image](assets/35.png)

Ceci est une bonne pratique pour que vous puissiez suivre d'où viennent vos pièces, si elles sont sans KYC ou non, et combien chaque UTXO vous a coûté (au cas où vous auriez besoin de vendre et de calculer les impôts qui vous seront volés par votre gouvernement).

Idéalement, vous devriez éviter d'accumuler plusieurs pièces dans la même adresse. Si vous décidez de le faire (ne le faites pas), vous pouvez étiqueter chaque pièce au lieu de toutes avec la même étiquette en utilisant la méthode de l'adresse. Vous ne pouvez pas réellement aller à l'onglet "pièces" et modifier les étiquettes là-bas (non, ce serait trop intuitif !). Vous devez aller à l'onglet Historique, trouver la transaction, étiqueter celle-ci, et ensuite vous verrez les étiquettes dans la section des pièces. Toutes les étiquettes que vous voyez dans la section des pièces proviennent des étiquettes d'adresse OU des étiquettes d'historique, mais toute étiquette d'historique remplace toute étiquette d'adresse. Pour sauvegarder vos étiquettes dans un fichier, vous pouvez les exporter depuis le menu en haut, portefeuille -> étiquettes -> exporter.

Ensuite, dépensons les pièces de la première adresse vers la deuxième adresse. Cliquez avec le bouton droit de la souris sur la première adresse et sélectionnez "dépenser à partir de" ce n'est pas vraiment nécessaire dans ce scénario, mais imaginez que nous avons de nombreuses pièces dans de nombreuses adresses ; en utilisant cette fonctionnalité, nous pouvons forcer le portefeuille à ne dépenser que les pièces que nous voulons. Si nous voulons sélectionner plusieurs pièces dans plusieurs adresses, nous pouvons sélectionner les adresses avec un clic gauche tout en maintenant la touche de commande enfoncée, puis cliquer avec le bouton droit de la souris et sélectionner "dépenser à partir de" :

![image](assets/36.png)

Une fois que vous avez fait cela, une barre verte apparaîtra en bas de la fenêtre du portefeuille indiquant le nombre de pièces que vous avez sélectionnées et le total disponible à dépenser.

Vous pouvez également dépenser des pièces individuelles dans une adresse et exclure les autres dans la même adresse, mais cela est déconseillé car vous laissez des pièces dans une adresse qui a été affaiblie cryptographiquement en raison de la dépense d'une des pièces (une autre raison de ne pas mettre plusieurs pièces dans une seule adresse, en plus des raisons de confidentialité, est que, étant donné que vous devriez toutes les dépenser si vous en dépensez une, cela devient inutilement coûteux). Voici comment sélectionner une seule pièce à partir d'une adresse partagée, mais ne le faites pas :

![image](assets/37.png)

Maintenant, nous avons sélectionné les deux pièces à dépenser. Ensuite, nous avons décidé où les dépenser. Envoyons-les à la deuxième adresse. Nous devrons copier l'adresse comme ceci :

![image](assets/38.png)

Ensuite, allez à l'onglet "Envoyer" et collez la deuxième adresse dans le champ "payer à". Pas besoin d'ajouter une description ; vous pourriez le faire, mais vous pouvez le faire plus tard en modifiant les étiquettes. Pour le montant, sélectionnez "Max" pour dépenser toutes les pièces que nous avons sélectionnées. Ensuite, cliquez sur "Payer", puis cliquez sur le bouton "avancé" sur la fenêtre contextuelle qui apparaît.

![image](assets/39.png)

Cliquez toujours sur "avancé" à cette étape pour pouvoir avoir un contrôle précis et vérifier exactement ce qui se trouve dans la transaction. Voici la transaction :

![image](assets/40.png)

Nous voyons deux fenêtres internes blanches. La première en haut est la fenêtre des entrées (quelles pièces sont dépensées), et la seconde en bas est celle des sorties (où vont les pièces).

Note, le statut (en haut à gauche) est "non signé" pour le moment. Le "Montant envoyé" est de 0 car les pièces sont en train d'être transférées dans le portefeuille. Les frais sont de 481 sats. Notez que s'ils étaient de 480 sats, le zéro final serait supprimé, comme ceci, 0.0000048 et pour l'œil fatigué, cela peut ressembler à 48 sats - soyez prudent (quelque chose que les développeurs d'Electrum devraient corriger).

La taille de la transaction fait référence à la taille des données en octets, pas au montant de bitcoin. Le "remplacement par frais" est activé par défaut et vous permet de renvoyer la transaction avec des frais plus élevés si nécessaire. Le LockTime vous permet d'ajuster quand la transaction est valide - je n'ai pas encore joué avec cela, mais je déconseille de l'utiliser à moins de comprendre parfaitement ce que vous faites et d'avoir pratiqué avec de petites sommes.

En bas, nous avons quelques outils sophistiqués d'ajustement des frais miniers. Tout ce que vous avez à faire pour les transferts internes est de le régler sur les frais minimums de 1 sat/byte. Tapez simplement manuellement le nombre dans le champ Frais cible. Pour vérifier les frais appropriés pour un paiement externe, vous pouvez consulter https://mempool.space pour voir à quel point le mempool est occupé, et certains frais suggérés sont affichés.

![image](assets/41.png)

J'ai sélectionné 1 sat/byte.

Dans la fenêtre d'entrée, nous voyons deux entrées. La première est le don de 5000 sats. Nous voyons à gauche son hachage de transaction (que nous pouvons rechercher sur la blockchain). À côté, il y a un "21" - cela indique qu'il s'agit de la sortie étiquetée 21 dans cette transaction (c'est en réalité la 22e sortie car la première est étiquetée zéro).

Quelque chose à noter ici : les UTXO n'existent que dans une transaction. Pour dépenser un UTXO, nous devons le référencer et mettre cette référence dans l'entrée d'une nouvelle transaction. Les sorties deviennent alors de nouveaux UTXO et l'ancien UTXO devient un STXO (sortie de transaction dépensée).

La deuxième ligne est le don de 10 000 sats. Il y a un "0" à côté du hachage de transaction dont il provient car c'est la première (et peut-être la seule) sortie de cette transaction.

Dans la fenêtre inférieure, nous voyons notre adresse. Remarquez que le total des bitcoins des entrées ne correspond pas tout à fait au total des sorties. La différence revient au mineur. Le mineur examine l'écart dans toutes les transactions du bloc qu'il essaie de miner et ajoute ce nombre à sa récompense. (Les frais de minage de cette manière sont totalement déconnectés de la chaîne de transactions et commencent une nouvelle vie).

Si nous ajustons les frais de minage, la valeur de sortie changera automatiquement.

> Il est intéressant de souligner ici : notez la couleur des adresses dans la fenêtre de transaction. Rappelez-vous que les adresses vertes sont répertoriées dans votre onglet d'adresses. Si une adresse est mise en surbrillance en vert (ou en jaune) dans une fenêtre de transaction, alors Electrum a reconnu l'adresse comme l'une des siennes. Si l'adresse n'a pas de surbrillance, alors c'est une adresse externe (externe au portefeuille actuellement ouvert), et vous devez la vérifier avec une attention particulière.

Une fois que vous avez vérifié tout dans la transaction et que vous êtes sûr de laquelle de vos pièces vous dépensez et où vont les pièces, vous pouvez cliquer sur "finaliser".

![image](assets/42.png)

Après avoir cliqué sur "finaliser", vous ne pouvez plus apporter de modifications - Si vous en avez besoin, vous devez fermer cela et recommencer. Remarquez que le bouton "finaliser" a changé en "exporter" et de nouveaux boutons sont apparus : "enregistrer", "combiner", "signer" et "diffuser". Le bouton "diffuser" est grisé car la transaction est non signée et donc invalide à ce stade.
Une fois que vous avez cliqué sur "signer", si vous avez un mot de passe pour le portefeuille, vous serez invité à le saisir, puis le statut (en haut à droite) passera de "non signé" à "signé". Ensuite, le bouton "Diffuser" sera disponible.

Après avoir diffusé, vous pouvez fermer la fenêtre de transaction. Si vous allez à l'onglet d'adresse, vous verrez maintenant que la première adresse est vide et que la deuxième adresse a 1 UTXO.

Note : Vous verrez tous ces changements même avant que la transaction ne soit ajoutée à un bloc ou "confirmée". Cela est dû au fait qu'Electrum met à jour les soldes/transactions en se basant non seulement sur les données de la blockchain, mais aussi sur les données de la mempool. Tous les portefeuilles ne font pas cela.

Il convient de souligner qu'au lieu de diffuser, nous pouvons enregistrer la transaction pour plus tard. Elle peut être enregistrée soit dans les états non signés, soit signés.

Cliquez sur le bouton "exporter" (paradoxalement, NE CLIQUEZ PAS sur le bouton "enregistrer"), et vous verrez plusieurs options. La transaction est encodée avec du texte et peut donc être enregistrée de plusieurs manières.

![image](assets/43.png)

L'enregistrement sous forme de code QR est très intéressant. Si vous choisissez cette option, un QR code apparaîtra :

![image](assets/44.png)

Vous pouvez ensuite prendre une photo du code QR. Il y a plusieurs choses que vous pouvez faire avec cela, mais pour l'instant, disons simplement que vous le chargez à nouveau dans le portefeuille plus tard. Vous pouvez fermer Electrum, charger à nouveau le portefeuille et aller dans le menu Outils :

![image](assets/45.png)

Cela chargera la caméra de votre ordinateur. Vous montrez ensuite à la caméra la photo du code QR sur votre téléphone, et cela chargera la transaction à nouveau, exactement comme vous l'avez laissée.

Il n'est pas intuitif de charger une transaction enregistrée, alors prenez note spéciale. Charger une transaction n'est pas un "outil", mais l'option est cachée dans le menu Outils (une autre chose que les développeurs d'Electrum devraient corriger).

Un processus similaire est possible avec une transaction enregistrée sous forme de fichier. Essayez de vous entraîner avec l'une ou l'autre méthode, dans le même portefeuille. Je ne vais pas le détailler ici, mais vous pouvez utiliser cette fonctionnalité pour transmettre une transaction entre le même portefeuille sur différents ordinateurs, entre des portefeuilles multi-signatures et vers et depuis des portefeuilles matériels. Voici quelques instructions.

Maintenant, en revenant au bouton "enregistrer" - ce n'est pas ainsi que vous enregistrez le texte de la transaction. Ce que cela fait réellement, c'est indiquer au portefeuille Electrum de reconnaître cette transaction sur l'ordinateur local comme étant soumise en tant que paiement. Si vous le faites par accident, vous verrez la transaction avec une petite icône d'ordinateur. Vous pouvez faire un clic droit et supprimer la transaction - ne vous inquiétez pas, vous ne pouvez pas supprimer des bitcoins de cette manière. Electrum oubliera alors que cette transaction a jamais eu lieu et "remboursera" les sats et affichera les sats à l'endroit correct où ils se trouvent réellement.

### Adresses de changement

Les adresses de changement sont intéressantes. Vous devez comprendre les UTXO pour comprendre cette explication. Si vous dépensez vers une adresse un montant inférieur à l'UTXO, alors les bitcoins restants iront au mineur à moins qu'une sortie de changement ne soit spécifiée.
Vous pourriez avoir une UTXO de 6,15 bitcoins et vouloir dépenser 0,15 bitcoin pour faire un don à des manifestants opprimés par le gouvernement "démocratique" tyrannique quelque part dans le monde. Vous prendriez alors les 6,15 bitcoins (en utilisant la fonction "dépenser depuis" dans Electrum) et les mettriez dans une transaction.

Vous colleriez l'adresse des manifestants dans le champ "payer à", peut-être que vous mettriez "EndTheFed & WEF" dans le champ "description", et pour le montant, vous mettriez 0,15 bitcoin et cliqueriez sur "payer", puis "avancé".

Dans l'écran de transaction, dans la fenêtre d'entrée, vous verrez la UTXO de 6,15 bitcoins. Dans la fenêtre de sortie, vous verrez une adresse qui n'est pas mise en évidence (c'est l'adresse des manifestants) avec 0,15 bitcoin à côté. Vous verrez également une adresse jaune avec légèrement moins de 6,0 bitcoins. Il s'agit de l'adresse de changement automatiquement sélectionnée par le portefeuille parmi ses propres adresses de changement jaunes. Le but de l'adresse de changement est que le portefeuille puisse y mettre des pièces de monnaie de changement sans perturber la disponibilité des adresses de réception que vous pouvez avoir prévues, ou pour lesquelles vous avez envoyé des factures. Si elles doivent être utilisées ultérieurement par des clients, par exemple, vous ne voulez pas que votre portefeuille les utilise automatiquement et les remplisse. C'est désordonné et mauvais pour la confidentialité.

Notez que lorsque vous ajustez les frais de minage, le montant de la sortie de changement s'ajustera automatiquement, pas le montant du paiement.

### Changement manuel ou paiement à plusieurs

Il s'agit d'une fonctionnalité très intéressante d'Electrum. Vous y accédez comme ceci.

![image](assets/46.png)

Vous pouvez ensuite entrer plusieurs destinations pour le solde de la UTXO que vous dépensez, comme ceci :

![image](assets/47.png)

Collez l'adresse, tapez une virgule, puis un espace, puis le montant, puis <entrée>, puis recommencez. NE SAISISSEZ PAS LES MONTANTS DANS LES FENÊTRES "MONTANT" - Electrum remplira le total ici au fur et à mesure que vous tapez les montants individuels dans la fenêtre "Payer à".

Cela vous permet de déterminer manuellement où va le changement (par exemple, une adresse spécifique dans votre portefeuille ou un autre portefeuille), ou vous pouvez payer plusieurs personnes à la fois. Si votre total n'est pas suffisamment élevé pour correspondre à la taille de la UTXO, Electrum créera quand même une sortie de changement supplémentaire pour vous.

La fonctionnalité "Payer à plusieurs" permet également la possibilité de créer vos propres "PayJoins" ou "CoinJoins" - en dehors du cadre de cet article, mais j'ai un guide ici. (https://armantheparman.com/cj/)

## Portefeuilles

Je veux vous montrer un portefeuille en mode "Observation seulement" utilisant Electrum. Pour cela, je dois d'abord définir "portefeuille". Le mot "portefeuille" est utilisé de deux manières différentes dans Bitcoin :

- Type A, "portefeuille" - fait référence au logiciel qui affiche vos adresses et soldes, par exemple Electrum, Blue Wallet, Sparrow Wallet, etc.

- Type B, "portefeuille" - fait référence à la collection unique d'adresses associées à la combinaison de notre phrase de récupération/phrase secrète/chemin de dérivation. Il y a 8,6 milliards d'adresses dans n'importe quel portefeuille (4,3 milliards d'adresses de réception et 4,3 milliards d'adresses de changement). Si vous modifiez quelque chose dans la phrase de récupération, la phrase secrète ou le chemin de dérivation, vous obtenez un nouveau portefeuille inutilisé avec 8,6 milliards d'adresses vides, toutes uniques.

Le type auquel on fait référence lorsqu'on utilise le mot "portefeuille" est évident dans le contexte.

## Portefeuille en mode "Observation seulement" - un exercice

Il n'est pas complètement évident à quoi sert un portefeuille de surveillance, mais je vais commencer par expliquer ce que c'est, comment en créer un à titre d'exemple, puis nous reviendrons plus tard sur son objectif lorsque j'expliquerai davantage sur les portefeuilles matériels. (Pour une revue approfondie sur l'utilisation d'un portefeuille matériel et les différentes marques spécifiques, voir ici.)

Nous allons créer un faux portefeuille ordinaire (cette fois-ci en ajoutant un peu plus de complexité avec une phrase secrète), puis son portefeuille de surveillance correspondant. Si vous le souhaitez, vous pouvez copier exactement celui que j'ai créé, ou créer le vôtre - ce portefeuille doit être jeté ; ne l'utilisez pas réellement. Commencez par générer une graine de 12 mots en utilisant le site Ian Coleman.

Remarquez les 12 mots aléatoires dans la capture d'écran ci-dessous, et que j'ai saisi une phrase secrète dans le champ de la phrase secrète :

PHRASE SECRÈTE : "Craig Wright est un menteur et un escroc et mérite d'être en prison. De plus, Ross Ulbricht devrait être libéré de prison immédiatement."

La phrase secrète peut comporter jusqu'à 100 caractères et idéalement ne devrait pas être ambiguë ni trop courte - celle que j'ai utilisée est juste pour le plaisir - je suggère généralement d'éviter les lettres majuscules et les symboles pour réduire votre stress lorsque vous essayez des combinaisons si vous avez déjà eu des problèmes pour vous souvenir de votre phrase secrète.

![image](assets/48.png)

Ensuite, dans Electrum, allez dans le menu fichier -> nouveau/restaurer. Tapez un nom unique pour créer un nouveau portefeuille et cliquez sur "suivant".

![image](assets/49.png)

Les étapes suivantes devraient vous être familières maintenant, donc je vais les énumérer sans images :

- Portefeuille standard
- J'ai déjà une graine
- Copiez et collez les 12 mots dans la boîte, ou tapez-les manuellement.
- Cliquez sur options et sélectionnez BIP39, et cochez également la case de la phrase secrète ("étendre cette graine avec des mots personnalisés")
- Saisissez votre phrase secrète exactement comme vous l'avez fait sur la page Ian Coleman
- Laissez les paramètres de script et de chemin de dérivation par défaut
- Pas besoin d'ajouter un mot de passe (verrouille le portefeuille)

Maintenant, retournez sur le site Ian Coleman, descendez jusqu'à la section "chemin de dérivation" et cliquez sur l'onglet "BIP 84" pour sélectionner les mêmes paramètres de script que les valeurs par défaut dans Electrum (Native Segwit).

![image](assets/50.png)

Les clés privées et publiques étendues sont juste en dessous, et elles changent lorsque vous apportez des modifications au chemin de dérivation (ou à toute autre chose plus haut sur la page).

![image](assets/51.png)

Vous verrez également les clés privées/publiques étendues "BIP32" - elles doivent être ignorées pour le moment.

La clé privée étendue du compte peut être utilisée pour régénérer entièrement votre portefeuille. Cependant, la clé publique étendue du compte ne peut produire qu'une version limitée du même portefeuille (portefeuille de surveillance) - si vous mettez cette clé dans Electrum, elle produira toujours les 8,6 milliards d'adresses que la graine ou la clé privée étendue auraient, mais il n'y aura pas de clés privées disponibles pour Electrum, donc aucune dépense n'est possible. Faisons-le maintenant pour illustrer le point :

Copiez la "clé publique étendue du compte" dans le presse-papiers.

Ensuite, allez dans Electrum, laissez le portefeuille que nous avons créé ouvert, et allez dans fichier -> nouveau/restaurer. Le processus de création du portefeuille est un peu différent qu'auparavant :

- Portefeuille standard
- Utiliser une clé maîtresse
- Collez la clé publique étendue dans la boîte et continuez
- Pas besoin de saisir une phrase secrète ; elle fait déjà partie de la clé publique étendue
- Pas besoin de saisir les paramètres de script et de chemin de dérivation
- Pas besoin d'ajouter un mot de passe (verrouille le portefeuille)

Lorsque le portefeuille se charge, vous devriez remarquer que les mêmes adresses sont chargées que précédemment lorsque la graine a été saisie. Vous devriez également remarquer en haut de la barre de titre qu'il est indiqué "watching wallet". Ce portefeuille peut vous montrer vos adresses et soldes (en vérifiant les soldes via un nœud), mais vous ne pouvez pas SIGNER de transactions (car le portefeuille de surveillance n'a pas de clés privées).
Alors, quel est l'intérêt ?

Une raison, et pas la principale, est que vous pouvez potentiellement observer votre portefeuille et son solde sur un ordinateur sans exposer vos clés privées à des logiciels malveillants sur l'ordinateur.

Une autre raison est que cela est REQUIS pour effectuer des paiements si vous choisissez de garder vos clés privées hors de l'ordinateur ; je vais expliquer :

> Les portefeuilles matériels (HWW) ont été créés pour qu'un appareil puisse stocker vos clés privées en toute sécurité (verrouillées avec un code PIN), ne jamais exposer les clés à un ordinateur (même lorsqu'il est connecté à un ordinateur via un câble) et ne peuvent pas se connecter à Internet eux-mêmes. Un tel appareil ne peut pas effectuer de transactions par lui-même car toutes les transactions Bitcoin commencent par la référence à une UTXO(s) sur la blockchain (qui se trouve sur un nœud). Un portefeuille doit spécifier l'ID de transaction dans lequel se trouve l'UTXO, ainsi que la sortie de la transaction à dépenser. Ce n'est qu'après avoir spécifié l'entrée qu'une nouvelle transaction peut être créée en premier lieu, sans parler de la signer. Les portefeuilles matériels ne peuvent pas créer de transactions car ils n'ont pas accès à des UTXOs - ils ne sont connectés à rien ! Une clé publique étendue est généralement extraite du HWW, et les adresses sont ensuite affichées sur un ordinateur - beaucoup de personnes sont familières avec le logiciel Ledger ou Trezor Suite qui affiche les adresses et les soldes sur leur ordinateur - c'est un portefeuille de surveillance. Ces programmes peuvent créer des transactions, mais ils ne peuvent pas les signer. Ils peuvent seulement faire signer des transactions par des HWW qui y sont connectés. Le HWW prend la transaction nouvellement générée à partir du portefeuille de surveillance, la signe, puis la renvoie à l'ordinateur pour la diffuser à un nœud. Le HWW ne peut pas diffuser par lui-même, c'est le portefeuille de surveillance associé qui le fait. De cette manière, les deux portefeuilles (portefeuille de clé publique sur l'ordinateur et portefeuille de clé privée dans le HWW) coopèrent pour générer, signer et diffuser, tout en veillant à ce que les clés privées restent isolées et éloignées d'un appareil connecté à Internet.

## Transactions Bitcoin partiellement signées (PSBTs)

Il est possible de créer une transaction, de l'enregistrer dans un fichier, de la recharger ultérieurement, de la signer, de l'enregistrer à nouveau, puis de la diffuser enfin - je ne dis pas que quelqu'un aurait besoin de le faire ; c'est juste quelque chose de possible.

Maintenant, considérez un portefeuille multisignature 3 sur 5 - 5 clés privées créent un portefeuille et 3 sont nécessaires pour signer complètement une transaction (voir ici pour en savoir plus sur les clés de portefeuille multisignature). Il est possible d'avoir 5 ordinateurs différents, chacun avec l'une des cinq clés privées.

L'ordinateur un peut générer une transaction et la signer. Il peut ensuite l'enregistrer dans un fichier et l'envoyer par e-mail à l'ordinateur 2. L'ordinateur 2 peut ensuite la signer et potentiellement enregistrer le fichier dans un code QR, puis transmettre le QR via un appel Zoom à l'ordinateur 3 de l'autre côté du monde. L'ordinateur 3 peut capturer le QR, charger la transaction dans Electrum et la signer. Après les deux premières signatures, la transaction était une PSBT (transaction Bitcoin partiellement signée). Après la troisième signature, la transaction est devenue entièrement signée et valide, prête à être diffusée.
Pour en savoir plus sur PSBTS, consultez ce guide. (https://armantheparman.com/psbt/)

## Utilisation de portefeuilles matériels avec Electrum

J'ai un guide sur l'utilisation des portefeuilles matériels en général, que je pense être important pour les personnes qui découvrent les HWW, à lire. (https://armantheparman.com/using-hwws/)

Il existe également des guides sur différentes marques de HWW se connectant à Sparrow Bitcoin Wallet que vous pouvez trouver ici. (https://armantheparman.com/hwws/)

Ce sera mon premier guide montrant comment utiliser un portefeuille matériel avec Electrum - je vais utiliser le portefeuille matériel ColdCard pour le démontrer. Ce n'est pas censé être un guide détaillé sur le ColdCard en particulier, ce guide se trouve ici. Je montre simplement des points spécifiques à Electrum. (https://armantheparman.com/cc/)

### Connexion via la carte micro SD (hors ligne)

Avant de connecter votre vrai portefeuille via le ColdCard, j'espère que vous avez suivi les étapes précédentes pour charger un portefeuille fictif Electrum et configurer les paramètres réseau.

Ensuite, sur le ColdCard, insérez la carte SD. Je suppose que vous avez déjà créé votre graine. Si vous accédez au portefeuille avec une phrase de passe, appliquez-la maintenant. Faites défiler vers le bas et sélectionnez le menu Avancé/Outils -> Exporter le portefeuille -> Portefeuille Electrum.

Vous pouvez faire défiler vers le bas et lire le message. Il vous propose toujours de sélectionner "1" pour entrer un numéro de compte non nul (une partie du chemin de dérivation), mais si vous avez suivi mon conseil, vous n'avez pas modifié les chemins de dérivation par défaut, vous ne voudrez donc pas de numéro de compte non nul ; appuyez simplement sur la coche pour continuer.

Ensuite, sélectionnez la sémantique du script. La plupart des gens sélectionneront "Native Segwit".

Il affichera "Fichier de portefeuille Electrum écrit" et affichera le nom du fichier. Prenez-en note mentalement.

Ensuite, retirez la carte micro SD et insérez-la dans l'ordinateur avec Electrum.

Certains systèmes d'exploitation ouvriront automatiquement l'explorateur de fichiers lorsque vous insérez la microSD. Beaucoup de gens verront le nouveau fichier de portefeuille et le double-cliqueront, se demandant pourquoi cela ne fonctionne pas. Ce n'est pas une conception géniale. Vous devez en fait ignorer l'explorateur de fichiers (le fermer) et ouvrir le fichier de portefeuille à l'aide d'Electrum :

Ouvrez Electrum. S'il est déjà ouvert avec un autre portefeuille, sélectionnez fichier -> nouveau. Nous recherchons cette fenêtre :

![image](assets/52.png)

Voici le truc, ce n'est pas intuitif. Cliquez sur "choisir". Ensuite, parcourez le système de fichiers sur la carte microSD et trouvez le fichier de portefeuille et ouvrez-le.

Maintenant, vous avez ouvert le portefeuille de surveillance correspondant à votre portefeuille matériel. Bien.

### Connexion via le câble USB.

Cette méthode devrait être plus facile, mais pour les ordinateurs Linux, c'est beaucoup plus difficile. Quelque chose appelé "règles Udev" doit être mis à jour. Voici comment faire (guide détaillé https://armantheparman.com/gpg-articles/ ), et brièvement :

Il est bon de s'assurer que le système est à jour. Ensuite :

```
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

puis...

```
python3 -m pip install ckcc-protocol
```

Si vous obtenez une erreur, assurez-vous que pip est installé. Vous pouvez vérifier avec (pip --version), et vous pouvez l'installer avec (sudo apt install pythron3-pip)

Créez ou modifiez le fichier existant, /etc/udev/rules.d/

Comme ceci :

```
sudo nano /etc/udev/rules.d
```

Un éditeur de texte s'ouvrira. Copiez le texte d'ici et collez-le dans le fichier rules.d, enregistrez et quittez.

![image](assets/53.png)

Ensuite, exécutez ces commandes les unes après les autres :

```
sudo groupadd plugdev

sudo usermod -aG plugdev $(whoami)

sudo udevadm control –reload-rules && sudo udevadm trigger
```

Si vous obtenez un message indiquant que le groupe "plugdev" existe déjà, c'est normal, continuez. Après la deuxième commande, vous n'aurez aucun retour, passez simplement à la troisième commande.

Vous devrez peut-être déconnecter puis reconnecter le ColdCard à l'ordinateur.

Si malgré tout cela vous ne parvenez toujours pas à connecter le ColdCard, je vous recommande de mettre à jour le firmware (un guide sera bientôt disponible, mais pour l'instant, vous pouvez trouver des instructions sur le site du fabricant).

Ensuite, créez un nouveau portefeuille :

- Portefeuille standard
- Utilisez un périphérique matériel
- Il détectera et reconnaîtra votre ColdCard. Poursuivez.
- Sélectionnez les paramètres de script et le chemin de dérivation
- Décidez si le fichier du portefeuille doit être chiffré (recommandé)

### Transactions avec le ColdCard

Avec le câble connecté, les transactions sont faciles. La signature des transactions se fera sans problème.

Si vous utilisez l'appareil de manière déconnectée, vous devrez manuellement transférer la transaction enregistrée entre les appareils à l'aide de la carte microSD. Il y a quelques astuces.

Après avoir créé une transaction et l'avoir finalisée, vous devez cliquer sur le bouton d'exportation en bas à gauche. Vous verrez "enregistrer dans un fichier", ce qui n'est pas ce que nous voulons en réalité. Vous devez en fait aller d'abord dans la dernière option de menu qui dit "pour les portefeuilles matériels", puis, à partir de cette sélection, trouver l'autre "enregistrer dans un fichier" et le sélectionner. Ensuite, enregistrez le fichier sur la microSD, retirez la carte et insérez-la dans le ColdCard. N'oubliez pas que vous devrez peut-être appliquer une phrase de passe pour sélectionner le bon portefeuille. L'écran affichera "prêt à signer". Cliquez sur la coche, vérifiez la transaction, puis confirmez en cliquant à nouveau sur la coche. Une fois terminé, retirez la carte et remettez-la dans l'ordinateur.

Ensuite, nous devons ouvrir la transaction avec Electrum. La fonction est cachée dans le menu Outils -> Charger une transaction. Parcourez le système de fichiers et trouvez le fichier. Il y aura trois fichiers à chaque fois que vous signez. Le fichier enregistré d'origine créé par le portefeuille de surveillance, et deux fichiers créés par le ColdCard (je ne sais pas pourquoi il fait cela). L'un dira "signé" et l'autre dira "final". Ce n'est pas intuitif, mais celui qui est "signé" n'est pas utile, nous devons ouvrir la transaction "finale".

Une fois que vous avez chargé cela, vous pouvez cliquer sur "diffuser" et le paiement sera effectué.

## Mise à jour d'Electrum et du répertoire caché ".electrum"

Electrum se trouve sur votre ordinateur à deux endroits. Il y a l'application elle-même, et il y a un dossier de configuration caché. Ce dossier se trouve à différents endroits selon votre système d'exploitation :

Windows :

> C:/Utilisateurs/votre_nom_d'utilisateur/AppData/Roaming/Electrum

Mac :

> /Utilisateurs/votre_nom_d'utilisateur/.electrum

Linux :

> /home/votre_nom_d'utilisateur/.electrum

Notez le "." avant "electrum" dans Linux et Mac - cela indique que le répertoire est caché. Notez également que ce répertoire n'est créé (automatiquement) qu'une fois que vous avez exécuté Electrum pour la première fois. Le répertoire contient le fichier de configuration d'Electrum ainsi que le répertoire qui contient tous les portefeuilles que vous avez enregistrés.

Si vous supprimez le programme Electrum de votre ordinateur, le répertoire caché restera, à moins que vous ne le supprimiez également activement.

Pour mettre à niveau Electrum, vous suivez la même procédure que celle que j'ai décrite au début pour le téléchargement et la vérification. Vous aurez alors deux copies du programme sur votre ordinateur, et vous pourrez exécuter l'une ou l'autre - chaque programme accédera au même dossier caché d'Electrum pour sa configuration et l'accès à votre portefeuille. Tout ce que nous avons enregistré, comme l'unité de base, le nœud par défaut auquel se connecter, les autres préférences et l'accès aux portefeuilles, restera car tout cela est enregistré dans ce dossier.

### Déplacer votre Electrum et vos portefeuilles vers un autre ordinateur

Pour ce faire, vous pouvez copier les fichiers du programme sur une clé USB, ainsi que le répertoire .electrum. Ensuite, copiez ou déplacez-les vers le nouvel ordinateur. Vous n'avez pas besoin de vérifier le programme à nouveau. Assurez-vous de copier le répertoire .electrum à l'emplacement par défaut (n'oubliez pas de le copier AVANT d'exécuter Electrum pour la première fois sur cet ordinateur, sinon un dossier .electrum par défaut vide sera créé et vous pourriez vous y perdre).

## Étiquettes

Comme je l'ai expliqué précédemment, dans l'onglet des adresses, il y a une colonne d'étiquettes. Vous pouvez double-cliquer dessus et saisir des notes pour vous-même (elles ne sont présentes que sur votre ordinateur, pas publiques et pas sur la blockchain).

![image](assets/54.png)

Lorsque vous déplacez votre portefeuille Electrum vers un autre ordinateur, vous ne souhaitez peut-être pas perdre toutes ces notes. Vous pouvez les sauvegarder dans un fichier en utilisant le menu, portefeuille -> étiquettes -> exporter, puis sur le nouvel ordinateur, utilisez portefeuille -> étiquettes -> importer.

## Conseils :

Si vous trouvez cette ressource utile et que vous souhaitez soutenir ce que je fais pour Bitcoin, vous pouvez faire un don de quelques sats ici :

Adresse Lightning statique : dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/
