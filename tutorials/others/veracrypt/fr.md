---
name: VeraCrypt
description: Comment chiffrer facilement un support de stockage ?
---
![cover](assets/cover.webp)

De nos jours, il est important de mettre en place une stratégie pour garantir l'accessibilité, la sécurité et la sauvegarde de vos fichiers, tels que vos documents personnels, vos photos ou vos projets importants. La perte de ces données peut être catastrophique.

Pour prévenir ces problèmes, je vous conseille de maintenir plusieurs sauvegardes de vos fichiers sur des supports différents. Une méthode généralement utilisée en informatique est la stratégie de sauvegarde du "_3-2-1_", qui assure la protection de vos fichiers :
- **3** copies de vos fichiers ;
- Sauvegardées sur au moins **2** types de supports différents ;
- Avec au moins **1** copie conservée hors site.

Autrement dit, il est conseillé d'enregistrer vos fichiers à 3 endroits différents, en utilisant des supports de nature différente, tels que votre ordinateur, un disque dur externe, une clé USB ou un service de stockage en ligne. Et enfin, avoir une copie hors site signifie que vous devriez avoir une sauvegarde stockée en dehors de votre maison ou de votre entreprise. Ce dernier point permet d'éviter la perte totale de vos fichiers en cas de sinistres locaux tels que des incendies ou des inondations. Une copie externe, éloignée de votre domicile ou de votre entreprise, assure que vos données survivront indépendamment des risques locaux.

Pour mettre en place facilement cette stratégie de sauvegarde 3-2-1, vous pouvez opter pour une solution de stockage en ligne, en synchronisant automatiquement ou périodiquement les fichiers de votre ordinateur avec ceux de votre cloud. Parmi ces solutions de sauvegarde en ligne, il y évidemment celles des grandes entreprises du numérique que vous connaissez : Google Drive, Microsoft OneDrive ou encore Apple iCloud. Cependant, ce ne sont pas les meilleures solutions pour protéger votre vié privée. Dans un tutoriel précédent, je vous ai présenté une alternative qui chiffre vos documents pour une meilleure confidentialité : Proton Drive.

https://planb.network/tutorials/others/proton-drive

En adoptant cette stratégie de sauvegarde locale et sur le cloud, vous bénéficiez déjà de deux types de supports différents pour vos données, dont un qui est hors site. Pour compléter la stratégie du 3-2-1, il vous suffit d'ajouter une copie supplémentaire. Ce que je vous conseille de faire, c'est tout simplement de réaliser périodiquement des exports de vos données présentes en local et sur votre cloud vers un support physique, comme une clé USB ou un disque dur. De cette manière, même si les serveurs de votre solution de stockage en ligne sont détruits et que votre ordinateur tombe en panne simultanément, vous disposez toujours de cette troisième copie sur un support externe pour ne pas perdre vos données.

01

Mais il est également important de penser a la sécurité de vos supports de données pour garantir que personne d'autre que vous ou vos proches ne puisse y accéder. Les données locales et en ligne sont normalement sécurisées. Sur votre ordinateur, vous avez probablement mis en place un mot de passe, et les disques durs des ordinateurs modernes sont souvent chiffrés par défaut. Concernant votre stockage en ligne (cloud), je vous ai montré dans un tutoriel précédent comment sécuriser votre compte avec un mot de passe robuste et une authentification à deux facteurs. Cependant, pour votre troisième copie stockée sur un support physique, la seule sécurité est sa possession physique. Si un cambrioleur parvient à voler votre clé USB ou votre disque dur externe, il pourra accéder facilement à toutes vos données.

02

Pour prévenir ce risque, il est conseillé de chiffrer votre support physique. Ainsi, toute tentative d'accès aux données nécessitera la saisie d'un mot de passe pour déchiffrer le contenu. Sans ce mot de passe, il sera impossible d'accéder aux données, ce qui sécurise vos fichiers personnels même en cas de vol de votre clé USB ou de votre disque dur externe.

03

Dans ce tutoriel, je vous montre comment chiffrer facilement un support de stockage externe à l'aide de VeraCrypt, un outil open source.

## Présentation de VeraCrypt

VeraCrypt est un logiciel open source disponible sur Windows, macOS et Linux, qui vous permet de chiffrer vos données de différentes manières et sur différents supports.

04

Ce logiciel permet de créer et de maintenir des volumes chiffrés à la volée, c'est-à-dire que vos données sont automatiquement chiffrées avant d'être sauvegardées et déchiffrées avant d'être lues. Cette méthode vous garantit que vos données restent protégées même en cas de vol de votre support de stockage. Aussi VeraCrypt chiffre non seulement les fichiers, mais également les noms de fichiers, les métadonnées, les dossiers, et même l'espace libre sur votre support de stockage.

Veracrypt peut être utilisé pour chiffrer des fichiers en local ou bien des partitions entières, y compris le disque système. Il peut également être utilisé pour chiffrer entièrement un support externe tel qu'une clé USB ou un disque comme nous allons le voir dans ce tutoriel.

Le gros avantage de VeraCrypt par rapport aux solutions propriétaires est qu'il est entièrement open source, ce qui signifie que son code peut être vérifié par n'importe qui.

## Comment installer VeraCrypt ?

Rendez-vous sur [le site officiel de VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) dans l'onglet "Downloads".

05

Téléchargez la version adaptée à votre système d'exploitation. Si vous êtes sous Windows, choisissez "EXE Installer".

06

Choisissez la langue de votre interface.

07

Acceptez les termes de la licence.

08

Sélectionnez "Install".

09

Enfin, choisissez le dossier où sera installé le logiciel puis cliquez sur le bouton "Install".

10

Patientez le temps de l'installation.

11

L'installation est terminée.

12

Si vous le souhaitez, vous pouvez faire un don en bitcoins pour soutenir le développement de cet outil.

13

## Comment chiffrer un support de stockage avec VeraCrypt ?

Lors du premier lancement, vous arriverez sur cette interface :

14

Pour chiffrer le support de votre choix, commencez par le brancher à votre machine. Comme vous allez le découvrir plus loin, la création d'un nouveau volume chiffré sur la clé USB ou le disque va mettre beaucoup plus de temps s'il y a déjà des données sur sur ce support qu'il ne faut pas supprimer. Je vous conseille donc soit d'utiliser une clé USB vierge, soit de prendre soin de vider le support avant la création du volume afin de ne pas perdre trop de temps.

Sur VeraCrypt, cliquez sur l'onglet "Volumes".

15

Puis sur le menu "Create New Volume...".

16

Sur la nouvelle fenêtre qui vient de s'ouvrir, sélectionnez l'option "Encrypt a non-system partition/drive", puis cliquez sur le bouton "Next".

17

Vous avez ensuite le choix entre l'option "Standard VeraCrypt volume" et l'option "Hidden VeraCrypt Volume". La première option permet simplement de créer un volume chiffré sur votre support. L'option "Hidden VeraCrypt Volume" permet de créer un volume caché à l'intérieur d'un volume VeraCrypt standard. Cette méthode vous permet de nier l'existence de ce volume caché en cas de contrainte. Par exemple, si quelqu'un vous force physiquement à déchiffrer votre support, vous pouvez déchiffrer seulement la partie standard pour satisfaire l'agresseur, mais ne pas révéler la partie cachée. Dans mon exemple, je vais rester sur un volume standard.

18

Sur la page suivante, cliquez sur le bouton "Select Device...".

19

Une nouvelle page s'ouvre. Vous pouvez sélectionner la partition de votre support de stockage parmi la liste des disques de votre machine. Normalement, cette partition devrait se trouver en dessous d'une ligne avec la mention "Removable Disk N". Une la partition à chiffrer sélectionnée, cliquez sur le bouton "OK".

20

Le support sélectionné apparait dans la case. Vous pouvez maintenant cliquer sur le bouton "Next".

21

Ensuite, vous allez devoir choisir entre l'option "Create encrypted volume and format it" ou bien "Encrypt partition in place". C'est ce que je vous expliquait au début de cette partie. La première option va supprimer définitivement toutes les données présentes sur votre clé USB ou votre disque. Il faut donc sélectionner cette option seulement si votre support est vide, sinon, vous allez perdre tout ce qui se trouve dessus. Au contraire, si vous avez des données que vous souhaitez conserver, vous pouvez soit les copier ailleurs le temps de l'opération et les remettre après, dans ce cas vous pouvez choisir l'option "Create encrypted volume and format it" qui va tout effacer, mais qui est bien plus rapide. Ou bien, vous pouvez choisir l'option "Encrypt partition in place" qui vous permet de chiffrer le volume sans effacer les données qui y sont déjà présentes, mais cela prend beaucoup plus de temps. Dans mon exemple, ma clé USB est vide, je vais donc choisir la première option qui efface tout.

22

Vous pouvez ensuite choisir l'algorithme de chiffrement et la fonction de hachage utilisés. Je vous conseille de laisser les options par défaut à moins que vous ayez des besoins spécifiques. Cliquez sur le bouton "Next".

23

Vérifiez que la taille de votre volume est correcte pour vous assurer que vous chiffrez bien l'intégralité de l'espace disponible sur la clé USB et non une partie seulement, puis cliquez sur "Next".

24

C'est à cette étape que vous allez devoir définir le mot de passe permettant de chiffrer et de déchiffrer votre support. Il est important de choisir un mot de passe fort, car sinon, un attaquant en possession du support physique pourrait déchiffrer votre contenu en devinant le mot de passe par brute force. Le mot de passe doit être aléatoire, le plus long possible, et avec une diversité de caractères. Je vous conseille au minimum de choisir un mot de passe aléatoire de 20 caractères avec des lettre minuscules, des lettres majuscules, des chiffres et des symboles.

Je vous conseille également d'enregistrer votre mot de passe dans un gestionnaire de mot de passe pour pouvoir y accéder facilement et ne pas l'oublier. Dans notre cas spécifique, il vaut mieux enregistrer le mot de passe sur un gestionnaire plutôt que sur un support en papier. En effet, si vous vous faites cambrioler, on pourra vous voler votre support USB, mais le mot de passe étant sur le gestionnaire, l'attaquant ne pourra pas accéder aux données. Et inversement, si votre gestionnaire de mots de passe se fait pirater, l'attaquant ne pourra pas accéder à vos données car le mot de passe seul, sans le support physique, ne sert à rien.

Pour plus d'informations sur la gestion des mots de passe, je vous conseille de découvrir cet autre tutoriel complet :

https://planb.network/tutorials/others/bitwarden

Renseignez votre mot de passe dans les 2 cases prévues à cet effet, puis cliquez sur "Next".

25

VeraCrypt vous demande ensuite si vous pensez stocker des fichiers plus gros que 4 GiB dans le volume qui va être chiffré. S'il vous demande ça, c'est pour présélectionner un système de fichiers adapté. Ce que l'on utilise la plupart du temps est le système FAT qui est compatible avec la majorité des système d'exploitation, mais celui-ci limite la taille des fichiers à 4 GiB au maximum. Sinon, vous pouvez également utiliser exFAT qui prend en charge les fichiers d'une taille supérieure en fonction de vos besoins.

26

Ensuite, vous allez arriver sur une page permettant de générer une clé aléatoire. En réalité, c'est cette clé aléatoire qui va permettre de déchiffrer vos données. Et cette clé sera conservée dans une partie spécifique de votre support, elle-même protégée par le mot de passe que vous avez précédemment renseigné. Pour générer une bonne clé de chiffrement, il faut produire de l'entropie, et c'est justement ce que vous demande de faire VeraCrypt. En bougeant aléatoirement votre souris par dessus la fenêtre, le logiciel utiliser ces mouvement pour générer la clé aléatoire. Faites le jusqu'à ce que la jauge soit entièrement remplie. Puis cliquez sur le bouton "Format" pour lancer la création du volume chiffré.

27

Patientez le temps que le formatage se fasse. Cela peut prendre longtemps pour de gros volumes.

28

Vous aurez ensuite une confirmation.

29

## Comment utiliser un support chiffré avec VeraCrypt ?

Pour le moment, votre support est chiffré et vous ne pouvez donc pas l'ouvrir. Pour le déchiffrer, rendez-vous sur VeraCrypt.

30

Sélectionnez une lettre de lecteur dans la liste. Par exemple, j'ai choisi "L:".

31

Cliquez sur le bouton "Select Device...".

32

Dans la liste de tous les disques de votre machine, sélectionnez le volume chiffré sur votre support puis cliquez sur le bouton "OK".

33

Vous pouvez voir que votre volume est bien sélectionné.

34

Cliquez sur le bouton "Mount".

35

Renseigner le mot de passe choisi lors de la création du volume, puis cliquez sur "OK".

36

Vous pouvez voir que votre volume est maintenant déchiffré et accessible sur la lettre de lecteur "L:".

37

Pour y accéder, ouvrez votre explorateur de fichier et rendez-vous sur le disque "L:" (ou une autre lettre en fonction de celle que vous avez choisie dans les étapes précédentes).

38

Après avoir ajouté vos fichiers personnels, pour chiffrer de nouveau le volume, il suffit de cliquer sur le bouton "Dismount".

39

Votre volume n'apparait plus sur la lettre "L:", il est donc de nouveau chiffré.

40

Vous pouvez maintenant retirer votre support de stockage.

Félicitations, vous disposez dorénavant d'un support chiffré pour stocker en sécurité vos données personnelles, et ainsi avoir une stratégie du 3-2-1 complète en plus de la copie sur votre ordinateur et sur votre solution de stockage en ligne.

Si vous souhaitez soutenir le développement de VeraCrypt, vous pouvez également faire un don en bitcoins [sur cette page](https://www.veracrypt.fr/en/Donation.html).
