---
name: Ajouter un livre sur PlanB Network
description: Comment ajouter un nouveau livre sur PlanB Network ?
---
![book](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

**Vous souhaitez ajouter un livre en rapport avec Bitcoin sur le site de PlanB Network et donner de la visibilité à votre ouvrage, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !**
![book](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait un tutoriel détaillé pour vous accompagner.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) dans la section `resources/books/` :
![book](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![book](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![book](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![book](assets/05.webp)
- Créez un dossier pour votre livre. Pour ce faire, dans la case `Name your file...`, notez le nom de votre livre en minuscules avec des tirets à la place des espaces. Par exemple, si votre ouvrage s'appelle "*My Bitcoin Book*", vous devez noter `my-bitcoin-book` :
![book](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite de votre nom de livre dans la même case, par exemple : `my-bitcoin-book/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![book](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `book.yml` :
![book](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre livre à l'aide de ce template :

```yaml
author: 
level: 
tags:
  - 
  - 
```

Voici les informations à remplir pour chaque champ :
- **`author`** : Indiquez le nom de l'auteur du livre.
- **`level`** : Indiquez le niveau requis pour pouvoir lire et bien comprendre le livre. Choisissez un niveau parmi les suivants :
	- `beginner`
	- `intermediate`
	- `advanced`
	- `expert`
- **`tags`** : Ajoutez deux ou trois étiquettes associées à votre livre. Par exemple :
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Par exemple, votre fichier YAML pourrait ressembler à celui-ci : 

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![book](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![book](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![book](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![book](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![book](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![book](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![book](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail :
![book](assets/17.webp)
- Retournez dans le dossier `resources/books/` et sélectionnez le dossier de votre livre que vous venez de créer dans le commit précédent :
![book](assets/18.webp)
- Dans le dossier de votre livre, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![book](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![book](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![book](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![book](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![book](assets/23.webp)
- Retournez dans le dossier `assets` :
![book](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![book](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone l'image de couverture de votre livre. Cette image sera affichée sur le site de PlanB Network :
![book](assets/26.webp)
- Attention, l'image doit être dans le format d'un livre, afin de s'adapter au mieux à notre site web, comme par exemple :
![book](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` : 
![book](assets/28.webp)
- Attention, votre image doit être nommée `cover_en` si la couverture est en anglais et doit être au format `.webp`. Ainsi, le nom complet du fichier devrait être `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. Si vous désirez utiliser une image de couverture différente pour chaque langue, par exemple en cas de traduction de l'ouvrage, vous pouvez les placer au même endroit dans le dossier `assets` :
![book](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![book](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![book](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes...` :
![book](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![book](assets/33.webp)
- Retournez dans le dossier de votre livre :
![book](assets/34.webp)
- Cliquez sur le bouton `Add file`, puis sur `Create new file` :
![book](assets/35.webp)
- Créez un nouveau fichier YAML en le nommant avec l'indicateur de la langue du livre. Ce fichier va être utilisé pour la description de l'ouvrage. Par exemple, si je veux rédiger ma description en anglais, je vais nommer ce fichier `en.yml` :
![book](assets/36.webp)
- Remplissez ce fichier YAML à l'aide de ce modèle :
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Voici les informations à remplir pour chaque champ :
- **`title`** : Indiquez le nom du livre entre guillemets.
- **`publication_year`** : Indiquez l'année de publication du livre.
- **`cover`** : Indiquez le nom du fichier correspondant à l'image de couverture, en accord avec la langue du fichier YAML que vous éditez actuellement. Par exemple, si vous modifiez le fichier `en.yml` et que vous avez préalablement ajouté l'image de couverture anglaise intitulée `cover_en.webp`, indiquez simplement `cover_en.webp` dans ce champ.
- **`description`** : Ajoutez un court paragraphe qui décrit le livre. La description doit être dans la même langue que celle indiquée dans le titre du fichier YAML.
- **`contributors`** : Ajoutez votre identifiant de contributeur si vous en avez un.

Par exemple, votre fichier YAML pourrait ressembler à celui-ci : 

```yaml
title: "My Bitcoin Book"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
 Discover the groundbreaking world of Bitcoin with this comprehensive guide tailored for beginners. My Bitcoin Book demystifies the complexities of Bitcoin, providing a clear and concise introduction to how the protocol works. From its revolutionary technology to its potential impact on the global economy, this book offers invaluable insights and practical knowledge. Perfect for those new to Bitcoin, it covers the basics, security tips, and the future of digital finance. Dive into the future of money and empower yourself with the knowledge to navigate the digital age confidently.
contributors:
  - pretty-private
```

![book](assets/37.webp)
- Cliquez sur le bouton `Commit changes...` :
![book](assets/38.webp)
- Vérifiez que la case `Commit directly to the patch-1 branch` est cochée, ajoutez un titre, puis cliquez sur `Commit changes` :
![book](assets/39.webp)
- Le dossier du livre devrait dorénavant ressembler à celui-ci :
![book](assets/40.webp)
- Si tout vous convient, revenez à la racine de votre fork :
![book](assets/41.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![book](assets/42.webp)
- Ajoutez un titre clair et une description sur votre PR :
![book](assets/43.webp)
- Cliquez sur le bouton `Create pull request` :
![book](assets/44.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir votre livre apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet `Pull requests` sur le dépôt GitHub de PlanB Network :
![book](assets/45.webp)
Merci beaucoup pour votre précieuse contribution ! :)
