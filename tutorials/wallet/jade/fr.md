---
name: Jade

description: Comment configurer votre appareil JADE
---

![image](assets/cover.webp)

## Vidéo tutorielle

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Portefeuille matériel Bitcoin mobile TUTORIEL COMPLET par BTCsession

## Guide d'écriture complet

![image](assets/cover2.webp)

### Prérequis

1. Téléchargez la dernière version de Blockstream Green.

2. Installez ce pilote pour vous assurer que Jade est reconnu par votre ordinateur.

### Configuration sur ordinateur de bureau

![guide complet](https://youtu.be/0fPVzsyL360)

Ouvrez Blockstream Green, puis cliquez sur le logo Blockstream sous "Appareils".

![image](assets/1.webp)

Branchez Jade à votre ordinateur de bureau à l'aide du câble USB fourni.

> Remarque : Si Jade n'est pas reconnu par votre ordinateur, assurez-vous de télécharger le pilote trouvé dans le guide ici.

Une fois que votre Jade apparaît dans Green, mettez à jour Jade en cliquant sur "Vérifier les mises à jour" et sélectionnez la dernière version du micrologiciel. Utilisez la molette de défilement ou le bouton bascule sur Jade pour confirmer et continuer avec la mise à jour. Assurez-vous que votre Jade affiche toujours le bouton "Initialiser", sinon vous devrez attendre après avoir configuré Jade pour le mettre à niveau. Utilisez le bouton retour pour revenir à cet écran si nécessaire.

![image](assets/2.webp)

Après avoir mis à jour le micrologiciel de Jade, sélectionnez "Configurer Jade" sur la politique de réseau et de sécurité que vous souhaitez utiliser.

> Astuce : La politique de sécurité est répertoriée sous "Type" à l'écran de connexion affiché ci-dessous. Si vous n'êtes pas sûr de choisir Singlesig ou Multisig Shield, veuillez consulter notre guide ici. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![image](assets/3.webp)

Ensuite, sélectionnez "Créer un nouveau portefeuille" et choisissez 12 mots pour générer votre phrase de récupération. En cliquant sur "Avancé", vous aurez la possibilité d'une phrase de récupération de 12 et 24 mots.

![image](assets/4.webp)

Enregistrez la phrase de récupération hors ligne sur papier (ou en utilisant un appareil de sauvegarde de phrase de récupération dédié pour une sécurité supplémentaire). Ensuite, utilisez la molette de défilement ou le bouton bascule sur le dessus de votre Jade pour vérifier votre phrase de récupération. Cette étape vous assure de l'avoir correctement écrite.

![image](assets/5.webp)

Définissez et confirmez votre code PIN à six chiffres. Il est utilisé pour déverrouiller Blockstream Jade à chaque fois que vous vous connectez à votre portefeuille.

![image](assets/6.webp)

Maintenant, sélectionnez simplement "Aller au portefeuille" dans l'application de bureau Green et vous verrez votre portefeuille s'ouvrir sur Blockstream Green. Blockstream Jade indiquera également qu'il est prêt ! Vous pouvez maintenant utiliser votre Jade pour envoyer et recevoir des transactions Bitcoin.

![image](assets/7.webp)

Après avoir fini d'utiliser votre portefeuille, déconnectez votre Blockstream Jade de votre appareil. La prochaine fois que vous voudrez utiliser le portefeuille sur Blockstream Jade, reconnectez simplement votre appareil et suivez les instructions.

source : https://help.blockstream.com/hc/en-us/articles/17478506300825

### Annexe A - Vérification du fichier de téléchargement du portefeuille Green

Vérifier le téléchargement signifie vérifier que le fichier que vous avez téléchargé n'a pas été modifié depuis sa publication par le développeur.

Nous faisons cela en vérifiant que la signature (produite par la clé privée du développeur) ainsi que le fichier téléchargé et la clé publique du développeur renvoient un résultat VRAI lorsqu'ils passent par la fonction gpg –verify. Je vais vous montrer comment faire cela ensuite. Si vous voulez en savoir plus sur le contexte, j'ai ce guide et celui-ci.
Tout d'abord, nous obtenons la clé de signature :

Pour Linux, ouvrez le terminal et exécutez cette commande (vous devez simplement copier et coller le texte et inclure les guillemets) :

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

Pour Mac, faites la même chose, sauf que vous devrez d'abord télécharger et installer GPG Suite.

Pour Windows, faites la même chose, sauf que vous devrez d'abord télécharger et installer GPG4Win.

Vous obtiendrez une sortie indiquant que la clé publique a été importée.

![image](assets/9.webp)

Cette image a un attribut alt vide ; son nom de fichier est image-3-1024x162.webp

Ensuite, nous devons obtenir le fichier contenant le hachage du logiciel. Il est stocké sur la page GitHub de Blockstream. Allez d'abord sur leur page d'informations ici, puis cliquez sur le lien "desktop". Cela vous amènera à la page de la dernière version sur GitHub, où vous verrez un lien vers le fichier SHA256SUMS.asc, qui est un document texte contenant le hachage publié par Blockstream du programme que nous avons téléchargé.

![image](assets/10.webp)

GitHub :

![image](assets/11.webp)

Ce n'est pas nécessaire, mais après l'avoir enregistré sur le disque, j'ai renommé "SHA256SUMS.asc" en "SHA256.txt" pour pouvoir plus facilement ouvrir le fichier sur Mac à l'aide de l'éditeur de texte. Voici le contenu du fichier :

![image](assets/12.webp)

Le texte qui nous intéresse se trouve en haut. Selon le fichier que nous avons téléchargé, il y a une sortie de hachage correspondante que nous comparerons plus tard.

La partie inférieure du document contient la signature faite sur le message ci-dessus - c'est un fichier deux en un.

L'ordre n'a pas d'importance, mais avant de vérifier le hachage, nous allons vérifier que le message de hachage est authentique (c'est-à-dire qu'il n'a pas été altéré).

Ouvrez le terminal. Vous devez vous trouver dans le répertoire correct où le fichier SHA256SUMS.asc a été téléchargé. En supposant que vous l'ayez téléchargé dans le répertoire "Téléchargements", pour Linux et Mac, accédez au répertoire de cette manière (sensible à la casse) :

```bash
cd Téléchargements
```

Bien sûr, vous devez appuyer sur <entrée> après ces commandes. Pour Windows, ouvrez CMD (invite de commandes) et tapez la même chose (bien que cela ne soit pas sensible à la casse).

Pour Windows et Mac, vous devez déjà avoir téléchargé GPG4Win et GPG Suite, respectivement, comme indiqué précédemment. Pour Linux, gpg est inclus dans le système d'exploitation. À partir du terminal (ou de CMD pour Windows), tapez cette commande :

```bash
gpg --verify SHA256SUMS.asc
```

L'orthographe exacte du nom de fichier (en rouge) peut être différente le jour où vous récupérez le fichier, alors assurez-vous que la commande correspond au nom de fichier tel que téléchargé. Vous devriez obtenir cette sortie et ignorer l'avertissement concernant la signature de confiance - cela signifie simplement que vous n'avez pas indiqué manuellement à l'ordinateur que vous faites confiance à la clé publique que nous avons importée précédemment.

![image](assets/13.webp)

Cet ouput confirme que la signature est bonne, et nous sommes confiants que la clé privée de "info@greenaddress.it" a signé les données (le rapport de hachage).

Maintenant, nous devons hacher notre fichier zip téléchargé et comparer la sortie telle que publiée. Notez que dans le fichier SHA256SUMS.asc, il y a un peu de texte qui dit "Hash: SHA512", ce qui me confond, car le fichier contient clairement des sorties SHA256, donc je vais ignorer cela.

Pour Mac et Linux, ouvrez le terminal, accédez à l'endroit où le fichier zip a été téléchargé (vous devrez probablement taper "cd Téléchargements" à nouveau, à moins que vous n'ayez pas fermé le terminal depuis). Au fait, vous pouvez toujours vérifier dans quel répertoire vous vous trouvez en tapant PWD ("print working directory"), et si tout cela est étranger, il est utile de regarder une courte vidéo YouTube en recherchant "comment naviguer dans le système de fichiers Linux/Mac/Windows".

Pour hacher le fichier, tapez ceci :

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Vous devriez vérifier comment votre fichier est exactement appelé et modifier le texte en bleu ci-dessus si nécessaire.

Vous obtiendrez une sortie comme ceci (la vôtre sera différente si le fichier est différent du mien) :

![image](assets/14.webp)

Ensuite, comparez visuellement la sortie de hachage avec ce qui se trouve dans le fichier SHA256SUMS.asc. S'ils correspondent, alors -> SUCCÈS ! Félicitations.

source: https://armantheparman.com/jade/

### Utilisation sur Sparrow

Si vous savez déjà comment utiliser Sparrow, alors c'est comme d'habitude :

> Note : c'est le même processus avec Specter par exemple

Téléchargez Sparrow en utilisant le lien fourni ici.

![image](assets/14.5.webp)

Cliquez sur Suivant pour suivre le guide de configuration et en apprendre davantage sur les différentes options de connexion.

![image](assets/15.webp)

Choisissez le serveur souhaité, puis sélectionnez Créer un nouveau portefeuille.

![image](assets/16.webp)

Entrez un nom pour votre portefeuille et cliquez sur Créer un portefeuille.

![image](assets/17.webp)

Choisissez les types de politique et de script souhaités, puis sélectionnez Portefeuille matériel connecté.

> Note : Si vous avez déjà utilisé Blockstream Jade en tant que portefeuille Singlesig avec Blockstream Green et que vous souhaitez afficher vos transactions dans Sparrow, assurez-vous que le type de script correspond au type de compte qui contient vos fonds dans Green. Vous devrez également vous assurer que le chemin de dérivation correspond également.

![image](assets/18.webp)

Branchez votre Blockstream Jade et cliquez sur Scanner. Vous serez alors invité à entrer votre NIP sur Jade.

> Astuce : Avant de connecter votre Jade, assurez-vous que l'application Blockstream Green n'est pas ouverte. Si Green est ouvert, cela peut causer des problèmes de détection de votre Jade dans Sparrow.

![image](assets/19.webp)

Sélectionnez Importer Keystore pour importer la clé publique du compte par défaut, ou sélectionnez la flèche pour sélectionner manuellement le chemin de dérivation que vous souhaitez utiliser.

![image](assets/20.webp)

Une fois la clé souhaitée importée, cliquez sur Appliquer.

![image](assets/21.webp)

Vous avez maintenant configuré votre portefeuille avec succès et vous pouvez commencer à recevoir, stocker et dépenser vos bitcoins en utilisant Sparrow et Blockstream Jade.

> Note : Si vous utilisiez précédemment Jade avec Blockstream Green en tant que portefeuille Multisig Shield, ne vous attendez pas à ce que votre nouveau portefeuille Sparrow affiche le même solde - ce sont des portefeuilles différents. Pour accéder à nouveau à votre portefeuille Multisig Shield, il vous suffit de reconnecter votre Jade à Blockstream Green.

![image](assets/22.webp)
'source: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### application green

if you're more a mobile guide, you can use it with blockstream green

- How to set up Blockstream Jade with Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- How to receive bitcoin to a Jade wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA'
