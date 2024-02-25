---
name: Contribution - Obsidian
description: Comment contribuer à PlanB Network avec GitHub et Obsidian ?
---
La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur Github, offrant ainsi la possibilité à quiconque de participer à l'enrichissement de la plateforme. Les contributions peuvent prendre diverses formes : correction et relecture des textes existants, traduction dans d'autres langues, mise à jour des informations ou encore création de nouveaux tutoriels encore absents de notre site.

Si vous êtes rédacteur et désirez apporter votre pierre à l'édifice PlanB Network, mais que vous ne vous sentez pas à l'aise avec l'utilisation de Github, ce tutoriel est conçu spécialement pour vous. Nous allons voir en détail comment contribuer à PlanB Network via Github, tout en utilisant Obsidian, un outil conçu pour faciliter la rédaction.

## Quel type de contenu rédiger ?
Nous recherchons en priorité des tutoriels sur des outils liés à Bitcoin ou à son écosystème. Ces contenus peuvent s'articuler autour de six catégories principales :
- Portefeuille ;
- Nœud ;
- Minage ;
- Marchand ;
- Échanger ;
- Confidentialité.

Au-delà de ces sujets spécifiquement liés à Bitcoin, PlanB cherche également des contributions sur des thèmes favorisant la souveraineté individuelle, tels que :
- Les outils open sources ;
- L'informatique ;
- La cryptographie ;
- L'énergie ;
- Les mathématiques ;
- L'économie ;
- Les DIY ;
- Le LifeHacking...

Par exemple, nous avons actuellement des tutoriels sur Tails, Nostr ou encore GrapheneOS. Ces outils ne sont pas directement en rapport avec Bitcoin, mais ce sont des systèmes qui peuvent nous intéresser dans une démarche de souveraineté dans le monde du numérique, ou dans l'apprentissage pour y arriver. Ces contenus peuvent être intégrés dans une sous-catégorie de la section « Autres ».

Vous avez le choix entre concevoir un tutoriel de zéro ou reprendre un tutoriel préalablement publié sur votre site web (à condition d'en détenir les droits d'auteur) pour le partager également sur PlanB Network, en y ajoutant un lien vers l'article d'origine.

Quel que soit votre choix, gardez à l'esprit que tous les contenus publiés sur PlanB Network sont sous la licence libre [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Cette licence autorise quiconque à copier et, potentiellement, à modifier votre contenu, à la seule condition que la source originale soit dûment créditée.

## Processus de contribution
Pour ajouter un tutoriel au site de PlanB Network, il faut faire une Pull Request sur le dépôt GitHub actuellement nommé [sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data). Votre contribution doit se conformer à la structure standard et inclure tous les fichiers nécessaires. C'est justement ce que nous allons détailler dans les parties suivantes.

Ensuite, un administrateur examinera votre tutoriel. Si des ajustements sont requis, il vous en informera pour que les modifications soient apportées. Une fois approuvé, le tutoriel sera intégré au dépôt.


## Étape 1 : Création d'un compte GitHub

Si vous n'êtes pas encore inscrit sur GitHub, il vous faudra créer un compte. Pour cela, rendez-vous sur [https://github.com/signup](https://github.com/signup). Saisissez votre adresse email, puis choisissez un mot de passe solide.
![github](assets/fr/1.png)
Ensuite, choisissez votre nom d'utilisateur. Vous avez la possibilité de révéler votre véritable identité ou de préférer l'usage d'un pseudonyme. Cliquez sur `Continue` et complétez le Captcha. Un email contenant un code de confirmation vous sera envoyé ; vous devrez le saisir pour finaliser la création de votre compte.
![github](assets/fr/2.png)
Remplissez les questions si vous souhaitez que GitHub vous oriente vers certains outils, ou bien cliquez sur `skip personalization` pour passer.
![github](assets/fr/3.png)
Choisissez le plan gratuit en cliquant sur le bouton `Continue for free`.
![github](assets/fr/4.png)
Vous serez alors redirigé vers votre tableau de bord. Si vous le souhaitez, il vous est possible de personnaliser votre compte en cliquant sur votre photo de profil située en haut à droite de l'écran, puis en accédant au menu `Settings`.
![github](assets/fr/5.png)
Dans cette section, vous avez la possibilité d'ajouter une nouvelle photo de profil, de sélectionner un nom, de personnaliser votre biographie, ou encore d'ajouter un lien vers votre site web personnel.
![github](assets/fr/6.png)
Je vous conseille également d'aller faire un tour dans le menu `Password and authentication`, afin de mettre en place l'authentification à deux facteurs.
![github](assets/fr/7.png)

## Étape 2 : Installer GitHub Desktop 


Rendez-vous sur https://desktop.github.com/ pour télécharger le logiciel GitHub Desktop. Ce logiciel vous permet d'intéragir facilement avec Github, sans avoir à utiliser un terminal.



Lors du premier lancement du logiciel, il vous sera demandé de connecter votre compte GitHub. Pour ce faire, cliquez sur `Sign in to GitHub.com`.



Une page d'authentification s'ouvre sur votre navigateur. Entrez votre adresse email et votre mot de passe choisis à l'étape précédente, puis cliquez sur le bouton `Sign in`.




Cliquez sur `Authorize desktop` pour confirmer la connexion entre votre compte et le logiciel.




Vous serez automatiquement redirigé sur le logiciel GitHub Desktop. Cliquez sur `Finish`.




Si vous venez de créer votre compte GitHub, vous serez redirigé vers une page indiquant que vous n'avez encore créé aucun dépôt. À ce stade, mettez de côté le logiciel GitHub Desktop ; nous y reviendrons ultérieurement.




## Étape 3 : Installer Obsidian 

Passons à l'installation du logiciel de rédaction. Ici, vous disposez de plusieurs options. Il existe une multitude de logiciels spécialisés dans l'édition de fichiers Markdown, tels que Typora, conçus spécifiquement pour la rédaction. Bien que cela ne soit pas idéal, il est aussi possible de choisir un éditeur de code, comme Visual Studio Code (VSC) ou Sublime Text. Cependant, en tant que rédacteur, je préfère utiliser le logiciel Obsidian. Voyons ensemble comment l'installer et le prendre en main.




Rendez-vous sur https://obsidian.md/download et téléchargez le logiciel. Installez-le, choisissez votre langue, puis cliquez sur `Quick Start`.



Vous arriverez sur le logiciel Obsidian. Pour le moment, vous n'avez aucun fichier ouvert.











## Étape 4 : Fork le dépôt de PlanB Network


Rendez-vous sur le dépôt des données de PlanB Network à l'adresse suivante : [https://github.com/DecouvreBitcoin/sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data). Si vous n'êtes pas connecté à votre compte GitHub, veuillez vous reconnecter.







Depuis cette page, cliquez sur le bouton `Fork` en haut à droite de la page.




Dans le menu de création, vous pouvez laisser les paramètres par défaut. Vérifiez que la case `Copy the dev branch only` soit bien cochée, puis cliquez sur le bouton `Create fork`.





Vous arriverez ensuite sur votre propre fork du dépôt de PlanB Network. 




Ce fork constitue donc un dépôt distinct de l'original, bien qu'il contienne pour le moment les mêmes données. C'est sur ce nouveau dépôt que vous allez désormais travailler.


## Étape 5 : Cloner votre dépôt 

Revenez sur le logiciel GitHub Desktop. À présent, votre fork devrait figurer dans la section `Your repositories`. Si vous ne le voyez pas immédiatement, utilisez le bouton des doubles flèches pour rafraîchir la liste. Lorsque votre fork apparaît, cliquez dessus pour le sélectionner.





Cliquez ensuite sur le bouton bleu : `Clone [votre nom]/sovereign-university-data`.




Par la suite, vous avez la possibilité de modifier le chemin d'accès local sur votre ordinateur où le clone de votre dépôt sera stocké. Vous pouvez conserver le chemin par défaut. Pour confirmer, cliquez sur le bouton bleu `Clone`.





Patientez le temps que GitHub Desktop clone votre fork en local.



Après le clonage du dépôt, le logiciel vous propose deux options. Vous devez sélectionner la première : `To contribute to the parent project`. Ce choix vous permettra présenter votre futur travail comme une contribution au projet parent (`DecouvreBitcoin/sovereign-university-data`), et non exclusivement comme une modification de votre fork personnel (`[username]/sovereign-university-data`). Une fois l'option choisie, cliquez sur `Continue`.



Votre GitHub Desktop est désormais correctement configuré. À présent, vous pouvez laisser le logiciel ouvert en arrière-plan pour suivre les modifications que nous effectuerons sur Obsidian.


## Étape 6 : Créer un nouveau coffre Obsidian

Ouvrez le logiciel Obsidian et cliquez sur la petite icône de coffre fort en bas à gauche de la fenêtre.



Cliquez sur le bouton `Open` afin de d'ouvrir un dossier existant comme un coffre.



Votre explorateur de fichier va s'ouvrir. Vous devez localiser et sélectionner le dossier intitulé `GitHub`, qui devrait se situer dans votre répertoire `Documents` parmi vos fichiers. Ce chemin correspond à celui que vous avez établi durant l'étape 5. Après avoir choisi le dossier, confirmez sa sélection. La création de votre coffre sur Obsidian se lancera alors sur une nouvelle page du logiciel. 

-> Attention, il ne faut surtout pas sélectionner le dossier `sovereign-university-data` lors de l'ouverture d'un nouveau coffre Obsidian. C'est bien le dossier parent `GitHub` qu'il faut sélectionner. Sinon, votre dossier de configuration `.obsidian` va être automatiquement placé à l'intérieur du dépôt. Nous ne voulons pas cela, car votre fichier de configuration `.obsidian` contient vos paramètres Obsidian. Cela ne sert à rien de les pousser sur le dépôt de PlanB Network. Une autre solution pour ignore le fichier de configuration est d'ajouter le dossier `.obsidian` dans le dossier `.gitignore`. Mais cette seconde solution viendra également modifier le fichier `.gitignore` du dépôt source.


Sur la gauche de la fenêtre, vous pouvez voir l'arborescence des fichiers avec vos différents dépôt GitHub qui ont été clonés en local. En cliquant sur les flèches situées à côté des noms de dossier, vous pouvez les dérouler pour accéder aux sous-dossiers des dépôts et à leurs documents.








## Étape 7



















LOIC : penses à parler des metadonnées des images et schémas