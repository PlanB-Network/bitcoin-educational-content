---
name: Contribution - Tutoriels
description: Comment proposer un nouveau tutoriel sur PlanB Network ?
---
![cover](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme. Les contributions peuvent prendre diverses formes : correction et relecture des textes existants, traduction dans d'autres langues, mise à jour des informations ou encore création de nouveaux tutoriels encore absents de notre site.

Dans ce tutoriel, je vous explique comment modifier la section "Tutoriels" de PlanB Network. Si vous souhaitez ajouter un nouveau tuto ou améliorer un déjà existant existant, cet article est fait pour vous ! Nous allons voir en détail comment contribuer à PlanB Network via GitHub, tout en utilisant Obsidian, un outil de rédaction.

## Prérequis

Pour contribuer à PlanB Network, vous avez 3 options selon votre niveau d'expérience avec GitHub :
1. **Utilisateurs expérimentés** : Continuez avec vos méthodes habituelles et consultez ce tutoriel pour vous familiariser avec la structure des fichiers du dépôt de PlanB, les exigences spécifiques et la méthode de travail.
2. **Débutants prêts à apprendre** : Je vous recommande de configurer votre propre environnement de travail. Suivez ce tutoriel ainsi que nos autres articles présentés ci-dessous pour vous guider étape par étape.
3. **Débutants pour contributions mineures** : Pour des tâches qui demandent moins de modifications comme la relecture ou des corrections, utilisez directement l'interface web de GitHub sans configurer un environnement local complet.

**Logiciels requis pour suivre mon tutoriel :**
- [GitHub Desktop](https://desktop.github.com/)
- [Obsidian](https://obsidian.md/)
- Un éditeur de code ([VSC](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/1.webp)
**Prérequis avant de commencer le tutoriel :**
- Avoir un [compte GitHub](https://github.com/signup).
- Avoir un fork du [dépôt source de PlanB Network](https://github.com/PlanB-Network/bitcoin-educational-content).
- Avoir [un profil de professeur sur PlanB Network](https://planb.network/professors) (uniquement si vous proposez un tutoriel complet).

**Si vous avez besoin d'aide pour obtenir ces prérequis, mes autres tutoriels vous guideront :**
**[Comprendre Git et GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Créer un compte GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Configurer votre environnement de travail](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
**[Créer un profil de professeur](https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4)**

## Quel type de contenu rédiger sur PlanB Network ?

Nous recherchons en priorité des tutoriels sur des outils liés à Bitcoin ou à son écosystème. Ces contenus peuvent s'articuler autour de six catégories principales :
- Portefeuille ;
- Nœud ;
- Minage ;
- Marchand ;
- Échange ;
- Confidentialité.
![tutorial](assets/2.webp)
Au-delà de ces sujets spécifiquement liés à Bitcoin, PlanB cherche également des contributions sur des thèmes qui mettent en avant la souveraineté individuelle, tels que :
- Les outils open sources ;
- L'informatique ;
- La cryptographie ;
- L'énergie ;
- Les mathématiques ;
- L'économie ;
- Les DIY ;
- Le LifeHacking...

Par exemple, nous avons actuellement des tutoriels sur Tails, Nostr ou encore GrapheneOS. Ces outils ne sont pas directement en rapport avec Bitcoin, mais ce sont des systèmes qui peuvent nous intéresser dans une démarche de souveraineté dans le monde du numérique. Ces contenus peuvent être intégrés dans une sous-catégorie de la section « Autres ».

Vous avez le choix entre concevoir un tutoriel de zéro ou reprendre un tutoriel préalablement publié sur votre site web (à condition d'en détenir les droits d'auteur) pour le partager également sur PlanB Network, en y ajoutant un lien vers l'article d'origine.

Quel que soit votre choix, gardez à l'esprit que tous les contenus publiés sur PlanB Network sont sous la licence libre [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Cette licence autorise quiconque à copier et, potentiellement, à modifier votre contenu, à la seule condition que la source originale soit dûment créditée.

## Comment proposer un tutoriel sur PlanB Network ?

Une fois que tout est en place, que votre environnement local est bien paramétré avec votre propre fork de PlanB Network, vous allez pouvoir commencer l'ajout du tutoriel.

### Créer une nouvelle branche

- Ouvrez votre navigateur et dirigez-vous vers la page de votre fork du dépôt de PlanB. Il s'agit du fork que vous avez établi sur GitHub. L'URL de votre fork devrait ressembler à : `https://github.com/[votre-nom-d'utilisateur]/bitcoin-educational-content` :
![tutorial](assets/3.webp)
- Assurez-vous d'être sur la branche principale `dev` puis cliquez sur le bouton `Sync fork`. Si votre fork n'est pas à jour, GitHub vous proposera de mettre à jour votre branche. Procédez à cette mise à jour. Si, au contraire, votre branche est déjà à jour, GitHub vous en informera :
![tutorial](assets/4.webp)
- Ouvrez le logiciel GitHub Desktop et assurez-vous que votre fork est correctement sélectionné dans le coin supérieur gauche de la fenêtre :
![tutorial](assets/5.webp)
- Cliquez sur le bouton `Fetch origin`. Si votre dépôt local est déjà à jour, GitHub Desktop ne suggérera aucune action supplémentaire. Dans le cas contraire, l'option `Pull origin` apparaîtra. Cliquez sur ce bouton afin de mettre à jour votre dépôt local :
![tutorial](assets/6.webp)
- Vérifiez que vous êtes bien sur la branche principale `dev` :
![tutorial](assets/7.webp)
- Cliquez sur cette branche, puis cliquez sur le bouton `New Branch` :
![tutorial](assets/8.webp)
- Assurez-vous que la nouvelle branche soit basée sur le dépôt source, à savoir `PlanB-Network/bitcoin-educational-content`.
- Nommez votre branche de manière à ce que le titre soit clair quant à son objectif, en utilisant des tirets pour séparer chaque mot. À titre d'exemple, admettons que notre objectif soit de rédiger un tutoriel sur l'utilisation du logiciel Sparrow Wallet. Dans ce cas, la branche de travail dédiée à la rédaction de ce tutoriel pourrait être nommée : `tuto-sparrow-wallet-loic`. Une fois le nom approprié saisi, cliquez sur `Create branch` pour confirmer la création de la branche :
![tutorial](assets/9.webp)
- Cliquez maintenant sur le bouton `Publish branch` afin d'enregistrer votre nouvelle branche de travail sur votre fork en ligne sur GitHub :
![tutorial](assets/10.webp)
À présent, sur GitHub Desktop, vous devriez vous trouver sur votre nouvelle branche. Cela signifie que toutes les modifications apportées localement sur votre ordinateur seront exclusivement enregistrées sur cette branche spécifique. Aussi, tant que cette branche reste sélectionnée sur GitHub Desktop, les fichiers visibles localement sur votre machine correspondent à ceux de cette branche (`tuto-sparrow-wallet-loic`), et non à ceux de la branche principale (`dev`).
![tutorial](assets/11.webp)
Pour chaque nouvel article que vous souhaitez publier, il vous faudra créer une nouvelle branche à partir de `dev`. Une branche dans Git est une version parallèle du projet, qui vous permet de faire des modifications sans affecter la branche principale, jusqu'à ce que le travail soit prêt à être fusionné.

### Ajouter le tutoriel

Maintenant que la branche de travail est créée, il est temps de faire l'intégration de votre nouveau tutoriel.

- Ouvrez votre gestionnaire de fichiers et dirigez-vous vers le dossier `bitcoin-educational-content`, qui représente le clone local de votre dépôt. Vous devriez normalement le trouver sous `Documents\GitHub\bitcoin-educational-content`. Au sein de ce répertoire, il sera nécessaire de localiser le sous-dossier adéquat pour le placement de votre tutoriel. L'organisation des dossiers reflète les différentes sections du site web PlanB Network. Dans notre exemple, puisque nous souhaitons ajouter un tutoriel sur Sparrow Wallet, il convient de se rendre dans le chemin suivant : `bitcoin-educational-content\tutorials\wallet` qui correspond à la section `WALLET` sur le site web :
![tutorial](assets/12.webp)
- Au sein du dossier `wallet`, il faut créer un nouveau répertoire spécifiquement dédié à votre tutoriel. Le nom de ce dossier doit évoquer le logiciel traité dans le tutoriel, en veillant à relier les mots par des tirets. Pour mon exemple, le dossier sera intitulé `sparrow-wallet` :
![tutorial](assets/13.webp)
- Dans ce nouveau sous-dossier dédié à votre tutoriel, il faut ajouter plusieurs éléments :
	- Créez un dossier `assets`, destiné à recevoir toutes les illustrations nécessaires à votre tutoriel ;
    - Au sein de ce dossier `assets`, il faut créer 8 sous-dossiers portant les noms `fr`, `de`, `en`, `it`, `es`, `ja`, `vi` et `pt`, afin de classer les visuels selon les langues correspondantes. Vous devez également ajouter un sous-dossier `notext` pour les visuels qui n'ont pas besoin de traduction, comme pour les captures d'écran par exemple ;
	- Un fichier `tutorial.yml` doit être créé pour y consigner les détails relatifs à votre tutoriel ;
	- Un fichier en format markdown est à créer pour y rédiger le contenu effectif de votre tutoriel. Ce fichier doit être intitulé selon le code de la langue de rédaction. Par exemple, pour un tutoriel rédigé en français, le fichier devra s'appeler `fr.md`.
![tutorial](assets/14.webp)
- Pour résumer, voici la hiérarchie des fichiers à créer :
```plaintext
bitcoin-educational-content/
└── tutorials/
    └── wallet/ (à modifier avec la bonne catégorie)
        └── sparrow-wallet/ (à modifier avec le nom du tuto)
            ├── assets/
            │   ├── fr/
            │   ├── de/
            │   ├── en/
            │   ├── it/
            │   ├── es/
            │   ├── pt/
            |   ├── ja/
            |   ├── vi/
            │   └── notext/
            ├── tutorial.yml
            └── fr.md (à modifier selon le code de langue approprié)
```

- Pour commencer, ouvrez votre fichier `tutorial.yml` à l'aide de votre éditeur de code.
- Remplissez chaque champs avec les informations spécifiées ci-dessous :
	- **builder** : Saisissez le nom de l'entreprise qui produit le logiciel sur lequel vous faites un tuto ;
	- **tags** : Déterminez une série de mots-clés en lien étroit avec le sujet de votre article, afin de faciliter sa recherche et son référencement ;
	- **category** : Sélectionnez une sous-catégorie adaptée parmi celles disponibles sur le site de PlanB, en vous basant sur le contenu de votre tutoriel. Par exemple, pour un tutoriel relevant de la section `WALLET`, les options disponibles sont `Desktop`, `Hardware`, et `Mobile` ;
	- **level** : Indiquez le niveau de difficulté de votre tutoriel en optant pour l'une des quatre catégories suivantes :
	    - Débutant (`beginner`),
	    - Intermédiaire (`intermediary`),
	    - Avancé (`advanced`),
	    - Expert (`expert`).
	- **professor** : Renseignez votre identifiant de contributeur tel qu'il apparaît sur votre profil de professeur. Pour davantage de détails, reportez-vous [au tutoriel correspondant](https://planb.network/fr/tutorials/others/create-teacher-profile) ;
	- **link** (optionnel) : Dans le cas où vous désireriez créditer un site web source pour le tutoriel que vous élaborez, tel que votre propre site personnel, c'est ici que vous pouvez ajouter le lien concerné.
![tutorial](assets/15.webp)
- Une fois la modification de votre fichier `tutorial.yml` terminée, enregistrez votre document en cliquant sur `File > Save` :
![tutorial](assets/16.webp)
- Vous pouvez désormais fermer votre éditeur de code.
- Au sein du dossier `assets`, vous devez ajouter un fichier nommé `logo.webp`, qui servira de vignette pour votre article. Cette image doit obligatoirement être au format `.webp` et doit respecter une dimension carrée afin de s'harmoniser avec l'interface utilisateur. Vous avez la liberté de choisir le logo du logiciel traité dans le tutoriel ou toute autre image pertinente, à condition que celle-ci soit libre de droits. En complément, ajoutez également au même endroit une image intitulée `cover.webp`. Celle-ci sera affichée en haut de votre tutoriel. Veillez à ce que cette image, tout comme le logo, respecte les droits d'utilisation et soit adaptée au contexte de votre tutoriel :
![tutorial](assets/17.webp)
- Maintenant, vous pouvez ouvrir votre fichier qui accueillera votre tutoriel, nommé avec le code de votre langue, comme par exemple `fr.md`. Rendez-vous sur Obsidian, sur la gauche de la fenêtre, faites dérouler l'arborescence de dossiers jusqu'au dossier de votre tutoriel et au fichier recherché :
![tutorial](assets/18.webp)
- Cliquez sur le fichier pour l'ouvrir :
![tutorial](assets/19.webp)
- Nous allons commencer par remplir la partie `Properties` tout en haut du document. Dans l'éventualité où cette section est absente de votre fichier (si le document est complètement vierge), il vous est possible de la reproduire en la copiant depuis un autre tutoriel existant :
![tutorial](assets/20.webp)
- Vous pouvez aussi l'ajouter manuellement de cette manière à l'aide de votre éditeur de code :
```markdown
---
name: [Titre]
description: [Description]
---
```
![tutorial](assets/21.webp)
- Remplissez le nom de votre tutoriel ainsi qu'une courte description de celui-ci :
![tutorial](assets/22.webp)
- Ajoutez ensuite votre image de couverture au début de votre tutoriel. Pour ce faire, tapez :
```markdown
![cover-sparrow](assets/cover.webp)
```
- Cette syntaxe vous sera utile chaque fois que l'ajout d'une image dans votre tutoriel sera nécessaire. Le point d'exclamation signale qu'il s'agit d'une image, dont le texte alternatif (alt) est spécifié entre les crochets. Le chemin d'accès à l'image est indiqué entre les parenthèses :
![tutorial](assets/23.webp)
- Poursuivez la rédaction de votre tutoriel en écrivant votre contenu. Lorsque vous souhaitez intégrer un sous-titre, appliquez le formatage markdown adéquat en préfixant le texte avec `##` :
![tutorial](assets/24.webp)

### Comment ajouter des schémas sur le tutoriel ?

Les sous-dossiers de langues dans le dossier `assets` sont destinés à organiser les schémas et les visuels qui accompagneront votre tutoriel. Si vos images incluent du texte, assurez-vous de les traduire pour chaque langue concernée afin de rendre votre contenu accessible à un public international. Pour les schémas sans texte à traduire ou les captures d'écran, placez-les directement dans le sous-dossier `notext`.
![tutorial](assets/25.webp)
Pour nommer vos images, il faut simplement mettre des numéros dans l'ordre d'apparition dans le tuto. Par exemple, nommez votre première image `1.webp`, votre deuxième `2.webp`, et ainsi de suite. 

Si le même schéma est traduit dans plusieurs langues, conservez le même nom de fichier pour les différentes traductions dans les sous-dossiers de langue, tel que `en/1.webp`, `fr/1.webp`, `pt/1.webp`, etc. 

Vous avez la possibilité d'utiliser différents formats d'images tels que `jpeg`, `png`, ou `webp`. Il est recommandé d'opter pour le format `webp` pour que les images soient moins lourdes.
![tutorial](assets/26.webp)
Pour insérer un schéma dans votre document, utilisez la commande suivante en Markdown, en veillant à spécifier le texte alternatif approprié ainsi que le chemin correct de l'image :
```markdown
![sparrow](assets/notext/1.webp)
```
Le point d'exclamation au début indique qu'il s'agit d'une image. Le texte alternatif, qui aide à l'accessibilité et au référencement, est placé entre les crochets. Enfin, le chemin d'accès à l'image est indiqué entre les parenthèses :
![tutorial](assets/27.webp)
Si vous souhaitez créer vos propres schémas, veillez à respecter la charte graphique de PlanB Network pour assurer la cohérence visuelle :
- **Police** : Utilisez [Rubik](https://fonts.google.com/specimen/Rubik) ;
- **Couleurs** :
	- Orange : #FF5C00
	- Noir : #000000
	- Blanc : #FFFFFF

**Il est impératif que tous les visuels intégrés à vos tutoriels soient libres de droit ou respectent la licence du fichier source**. Aussi, l'intégralité des schémas publiés sur PlanB Network sont mis à disposition sous licence CC-BY-SA, de la même manière que le texte.

**-> Astuce :** Lors du partage de fichiers en public, tels que des images, il est important de supprimer les métadonnées superflues. Celles-ci peuvent contenir des informations sensibles, comme des données de localisation, des dates de création, ou encore des détails concernant l'auteur. Afin de protéger votre vie privée, il est conseillé de supprimer ces métadonnées. Pour simplifier cette opération, vous pouvez recourir à des outils spécialisés comme [Exif Cleaner](https://exifcleaner.com/), qui offre la possibilité de nettoyer les métadonnées d'un document grâce à un simple drag-and-drop.

### Comment enregistrer et pousser le tutoriel ?

Une fois que vous avez terminé la rédaction de votre tutoriel dans la langue de votre choix, l'étape suivante consiste à soumettre une **Pull Request**. L'administrateur se chargera ensuite d'ajouter les traductions manquantes de votre tutoriel, grâce à notre méthode de traduction automatisée. 

- Pour procéder à la Pull Request, ouvrez le logiciel GitHub Desktop. 
- Le logiciel devrait automatiquement détecter les modifications que vous avez effectuées localement par rapport au dépôt d'origine. Avant de continuer, vérifiez soigneusement sur la partie gauche de l'interface que ces modifications correspondent bien à ce que vous attendiez :
![tutorial](assets/28.webp)
- Ajoutez un titre pour votre commit, puis cliquez sur le bouton bleu `Commit to [your branch]` pour valider ces modifications :
![tutorial](assets/29.webp)
Un commit est une sauvegarde des modifications apportées à la branche, accompagnée d'un message descriptif, permettant de suivre l'évolution d'un projet dans le temps. C'est donc une sorte de checkpoint intermédiaire.

- Cliquez ensuite sur le bouton `Push origin`. Cela va envoyer votre commit sur votre fork :
![tutorial](assets/30.webp)
- Si vous n'avez pas terminé votre tutoriel, vous pouvez y revenir plus tard et faire de nouveaux commits.
- Si vous avez terminé vos modifications pour cette branche, cliquez maintenant sur le bouton `Preview Pull Request` :
![tutorial](assets/31.webp)
- Vous pouvez vérifier une dernière fois que vos modifications sont bien justes, puis cliquez sur le bouton `Create pull request` :
![tutorial](assets/32.webp)
Une Pull Request est une demande faite pour intégrer les modifications de votre branche vers la branche de principale du dépôt de PlanB Network, qui permet la revue et la discussion des changements avant leur fusion.

- Vous allez être automatiquement renvoyé sur votre navigateur sur GitHub dans la page de préparation de votre Pull Request :
![tutorial](assets/33.webp)
- Indiquez un titre qui résume brièvement les modifications que vous souhaitez fusionner avec le dépôt source. 
- Ajoutez un bref commentaire décrivant ces changements.
- Cliquez sur le bouton vert `Create pull request` pour confirmer la demande de fusion :
![tutorial](assets/34.webp)
Votre PR sera alors visible dans l'onglet `Pull Request` du dépôt principal de PlanB Network. Il ne vous reste plus qu'à patienter jusqu'à ce qu'un administrateur vous contacte pour confirmer la fusion de votre contribution ou pour solliciter d'éventuelles modifications complémentaires.
![tutorial](assets/35.webp)
Après la fusion de votre PR avec la branche principale, il est recommandé de supprimer votre branche de travail (`tuto-sparrow-wallet`) pour maintenir un historique propre sur votre fork. GitHub vous proposera cette option automatiquement sur la page de votre PR :
![tutorial](assets/36.webp)
Sur le logiciel GitHub Desktop, vous pouvez vous replacer sur la branche principale de votre fork (`dev`).
![tutorial](assets/7.webp)
Si vous désirez apporter des modifications à votre contribution après avoir déjà soumis votre PR, la démarche à suivre dépend de l'état actuel de votre PR :
- Si votre PR est toujours ouverte et n'a pas encore été fusionnée, effectuez les modifications localement en restant sur la même branche. Une fois les modifications finalisées, utilisez le bouton `Push origin` pour ajouter un nouveau commit à votre PR encore ouverte ;
- Dans le cas où votre PR a déjà été fusionnée avec la branche principale, vous devrez refaire le processus depuis le début en créant une nouvelle branche, puis en soumettant une nouvelle PR. Assurez-vous que votre dépôt local soit synchronisé avec le dépôt source de PlanB Network avant de procéder.
