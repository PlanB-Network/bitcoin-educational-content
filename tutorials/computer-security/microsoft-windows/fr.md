---
name: Windows 11
description: Installation automatique de Microsoft Windows 11 via le fichier de configuration
---
![cover](assets/cover.webp)


Dans ce tutoriel, nous allons apprendre à installer Windows 11 automatiquement en utilisant une méthode différente du processus d'installation standard de Windows.


## Télécharger !


La première chose dont vous aurez besoin est un fichier d'installation. L'endroit le plus sûr et le plus fiable pour le télécharger est le site officiel de Microsoft.


Il suffit de visiter le lien fourni ci-dessous et de suivre les instructions pour télécharger le [fichier ISO Windows 11] (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Une fois que vous êtes sur la page de téléchargement, faites défiler vers le bas jusqu'à la section de téléchargement du fichier ISO.


![Image](assets/en/01.webp)


َAnd choisir la bonne version.


![Image](assets/en/03.webp)


Après avoir sélectionné Windows 11, cliquez sur le bouton Confirmer.


A ce stade, le traitement de la demande peut prendre quelques secondes, puis la page suivante s'affichera :


![Image](assets/en/04.webp)


Après avoir confirmé la demande, vous devez choisir la langue de votre choix.


![Image](assets/en/05.webp)


Après avoir sélectionné la langue et cliqué sur le bouton Confirmer, la demande sera traitée. Cette étape peut prendre quelques secondes.


Une fois la demande traitée avec succès, une page s'affiche avec le lien de téléchargement du fichier .iso. Cliquez sur le bouton de téléchargement 64 bits pour lancer le téléchargement.


La taille du fichier est d'environ 5,5 Go, et le lien généré sera valide pendant 24 heures.


## Automatisation !


À ce stade, nous devons apporter des modifications à l'installation standard de Windows. À ce stade, en utilisant l'installation sans surveillance, nous déterminons quels éléments vont être installés, sans que l'utilisateur ait à intervenir par la suite. En fait, dans cette méthode, un fichier XML est utilisé pour configurer les étapes de l'installation et les services installés dans Windows. En d'autres termes, l'utilisation du fichier Unattended.xml crée un processus d'automatisation pendant l'installation, évitant ainsi la nécessité de sélectionner plusieurs options et les étapes fastidieuses habituellement requises pendant l'installation. Cette méthode est une méthode inhabituelle mais standard qui a été introduite par Microsoft. De plus amples informations sont disponibles sur le [site officiel de Microsoft] (https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Il existe plusieurs outils disponibles sur l'internet pour générer des fichiers Unattended. Certains sont en ligne, d'autres hors ligne. L'un des outils en ligne permettant de créer ce fichier est [ce site web] (https://schneegans.de/windows/unattend-generator). Après l'avoir ouvert, la page suivante s'affiche :


![Image](assets/en/06.webp)


Comme indiqué en haut de la page, cette méthode peut être utilisée pour l'installation de Windows 10 et 11. Dans la première étape, nous sélectionnons la langue de Windows. Si nous avons besoin d'ajouter une deuxième ou même une troisième langue à la liste des langues d'affichage et de clavier de Windows, nous pouvons utiliser la boîte ci-dessous :


![Image](assets/en/07.webp)


L'étape suivante consiste à sélectionner l'emplacement souhaité.


![Image](assets/en/08.webp)


À ce stade, nous pouvons également spécifier l'architecture du processeur de l'ordinateur. Au cours de cette étape, nous pouvons

1. Décider d'ignorer ou non les fonctions de sécurité de Windows, telles que TPM et Secure Boot. La fonction de démarrage sécurisé garantit que si des fichiers centraux de Windows sont altérés au cours du processus de démarrage, le problème est détecté et leur exécution est empêchée. Cette fonction permet également de protéger le système contre l'installation de mises à jour malveillantes sur Windows. L'activation de l'option permettant de contourner ces fonctions est parfois inévitable sur certains ordinateurs, en particulier les anciens modèles. Toutefois, il est généralement recommandé de laisser les fonctions telles que Secure Boot activées.

2. Ignorez la nécessité d'une connexion internet pour terminer le processus. Cette option est utile dans les situations où une connexion LAN filaire n'est pas disponible, car dans la plupart des cas, la carte sans fil n'est pas encore reconnue lors de l'installation de Windows, et l'accès à l'internet par câble est nécessaire. L'activation de cette option résout les problèmes liés à cette étape.


Dans l'étape suivante, nous pouvons choisir un nom pour l'ordinateur.


![Image](assets/en/09.webp)


Nous pouvons également permettre à Windows de choisir un nom pour le système. Au cours de cette étape, nous pouvons sélectionner le type de Windows, compressé ou non, ou laisser Windows déterminer la version appropriée en fonction des spécifications de l'ordinateur. Le fuseau horaire peut également être défini à ce stade.


L'étape suivante consiste à paramétrer la partition :


![Image](assets/en/10.webp)


À ce stade, nous pouvons spécifier le type de partition pour l'installation de Windows, ainsi que les paramètres requis pour l'installation de l'environnement de récupération Windows. En sélectionnant la première option, la sélection de la partition et le partitionnement sont reportés au moment de l'installation de Windows, et pendant l'installation, ces questions seront posées comme dans la méthode d'installation normale.


Dans cette étape, nous sélectionnons la version de Windows à installer :


![Image](assets/en/11.webp)


Si une clé de produit est disponible, elle peut également être saisie à ce stade.


L'étape suivante consiste à configurer le compte de connexion Windows :


![Image](assets/en/12.webp)


## Ouverture de compte


A ce stade :


1. Nous pouvons définir un nom et un mot de passe pour le compte administrateur. Il est également possible de créer plusieurs comptes utilisateurs ou administrateurs.

2. Cette section permet de spécifier le compte auquel il faut se connecter la première fois après l'installation de Windows. Les différentes options de cette section sont présentées dans l'image.

3. Si vous ne souhaitez pas qu'un compte soit créé, nettoyez tous les comptes et sélectionnez cette option. Dans ce cas, après l'installation de Windows, vous serez automatiquement connecté au compte de l'administrateur de Windows.


L'étape suivante consiste à configurer le mot de passe et les paramètres du fichier hôte :


![Image](assets/en/13.webp)


À ce stade, nous déterminons si les mots de passe doivent avoir un délai d'expiration. En outre, cette section comprend les paramètres de sécurité relatifs aux tentatives de connexion infructueuses, qui peuvent être activés ou désactivés en fonction de vos besoins.


Au bas de cette section, il y a des paramètres pour l'affichage des fichiers. Aucune de ces options n'est disponible lors d'une installation standard de Windows et doit être configurée après l'installation. En revanche, avec la méthode d'installation sans surveillance, ces paramètres sont facilement accessibles.


L'étape suivante consiste à configurer les paramètres de sécurité de Windows :


![Image](assets/en/14.webp)


## Paramètres de sécurité


A ce stade :


1. Windows Defender peut être activé ou désactivé. Cette fonction agit comme un logiciel de sécurité dans Windows et aide à empêcher l'exécution de fichiers malveillants, certaines attaques de réseau, etc.

2. Les mises à jour automatiques de Windows peuvent être désactivées. C'est l'un des problèmes les plus courants auxquels sont confrontés les utilisateurs de Windows !

3. Cette section permet d'activer ou de désactiver l'UAC (User Account Control). Cette fonction empêche les applications suspectes de s'exécuter avec des autorisations élevées de lecture et d'écriture.

4. Cette fonction est utilisée par Windows pour détecter les logiciels potentiellement dangereux.

5. Activer ou désactiver la prise en charge des longs chemins d'accès dans les applications Windows, telles que PowerShell et autres.

6. Activer ou désactiver le bureau à distance pour accéder au système à distance.


Selon la version de Windows utilisée, certaines de ces fonctionnalités peuvent être prises en charge ou non.


L'étape suivante consiste à configurer les icônes :


![Image](assets/en/15.webp)


Dans cette section :


1. Les icônes du bureau sont répertoriées et peuvent être ajoutées ou supprimées selon les besoins.

2. Les icônes du menu Démarrer sont répertoriées et peuvent être ajoutées ou supprimées en fonction des besoins.

3. Cette section permet de configurer l'installation ou non des outils liés à la virtualisation. Cette option est spécifique à Windows 11 et ne s'applique pas à Windows 10.


L'étape suivante consiste à configurer les paramètres Wi-Fi :


![Image](assets/en/16.webp)


Cette section permet de configurer les paramètres du réseau Wi-Fi. Comme indiqué précédemment, dans la plupart des cas, la carte Wi-Fi n'est pas reconnue lors de l'installation de Windows, de sorte qu'il n'est généralement pas possible de se connecter pendant l'installation. Cependant, en configurant cette section, si la carte sans fil est détectée, le système peut se connecter à Internet.


L'étape suivante implique un réglage important :


![Image](assets/en/17.webp)


Dans cette section, nous indiquons si les informations relatives aux problèmes du système doivent être envoyées à Microsoft ou non.


L'étape suivante consiste à configurer les applications par défaut :


![Image](assets/en/18.webp)


## Activation/désactivation du logiciel par défaut


Dans cette section, nous pouvons choisir les applications que nous ne voulons pas voir installées par défaut. Par exemple, nous pouvons choisir de ne pas installer Cortana ou Copilot.


L'étape suivante concerne les paramètres de sécurité liés à l'exécution de l'application :


![Image](assets/en/19.webp)


L'application des paramètres WDAC permet d'empêcher l'exécution de certaines applications.


Enfin, après avoir appliqué les paramètres souhaités, le fichier XML généré peut être téléchargé :


![Image](assets/en/20.webp)


En cliquant sur Télécharger le fichier XML, le fichier autounattend.xml est téléchargé. Pour utiliser ce fichier, il suffit de monter l'ISO téléchargé sur une clé USB, de placer le fichier autounattend.xml dans le répertoire racine, puis de procéder à l'installation de Windows.


L'un des outils disponibles pour créer une clé USB amorçable est Rufus. Rufus peut créer une clé USB amorçable pour l'installation de Windows, à partir d'un fichier ISO d'installation de Windows donné. C'est rapide et simple, vous pouvez le télécharger [ici](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


Dans ce logiciel, après avoir sélectionné la clé USB désirée et le fichier ISO approprié, nous cliquons sur Démarrer.


![Image](assets/en/22.webp)


À ce stade, nous désactivons toutes les options, car leur activation peut entraîner des conflits lors de l'utilisation du fichier Unattend généré. Une fois les fichiers copiés sur la clé USB, nous plaçons le fichier autounattend.xml dans le répertoire racine :


![Image](assets/en/23.webp)


À ce stade, la clé USB est prête à être utilisée pour l'installation automatique de Windows, et l'installation peut être lancée à partir de cette clé.


## Montage ISO


Si vous devez installer Windows sur une machine virtuelle, vous pouvez utiliser un logiciel pour créer et modifier des fichiers ISO. L'un de ces logiciels est AnyBurn. Après avoir extrait le contenu du fichier ISO téléchargé sur le site web de Microsoft, placez le fichier autounattend.xml dans le répertoire racine. Ensuite, à l'aide d'AnyBurn, créez un nouveau fichier ISO avec le contenu mis à jour.


AnyBurn est un logiciel multifonctionnel pour travailler avec des fichiers ISO. Il offre diverses fonctionnalités pour gérer les fichiers ISO, dont la création d'images ISO amorçables ; [ici](https://www.anyburn.com/download.php) est le site web original.


Sur la page principale du logiciel, sélectionnez "Créer une image à partir d'un fichier/dossier" :


![Image](assets/en/24.webp)


Sur la page suivante, sélectionnez tous les fichiers extraits de l'ISO ainsi que le fichier autounattend.xml.


![Image](assets/en/25.webp)


Dans cette étape, nous configurons les paramètres pour rendre le fichier ISO amorçable :


![Image](assets/en/26.webp)


À ce stade, le chemin d'accès au fichier bootfix.bin doit être défini pour rendre l'ISO amorçable. Ce fichier est situé à la racine de l'ISO, dans le dossier de démarrage. Il est également recommandé d'activer les options ISO9660 et UDF dans la section Propriétés.


![Image](assets/en/27.webp)


Après cette étape, cliquer sur Suivant créera le fichier ISO. Ce fichier peut être utilisé dans un logiciel de virtualisation tel que Oracle VirtualBox. Vous trouverez ci-dessous un tutoriel sur VirtualBox :


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65