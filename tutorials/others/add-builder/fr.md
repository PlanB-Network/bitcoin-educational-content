---
name: Ajouter un builder
description: Comment proposer l'ajout d'un nouveau builder sur PlanB Network ?
---
![builder](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Vous souhaitez ajouter un nouveau "builder" Bitcoin sur le site de PlanB Network et donner de la visibilité à votre entreprise ou à votre logiciel, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !
![builder](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait un tutoriel détaillé pour vous accompagner.

https://planb.network/tutorials/others/create-github-account


- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) dans la section `resources/builder/` :
![builder](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![builder](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![builder](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![builder](assets/05.webp)
- Créez un dossier pour votre entreprise. Pour ce faire, dans la case `Name your file...`, notez le nom de votre entreprise en minuscules avec des tirets à la place des espaces. Par exemple, si votre entreprise s'appelle "Bitcoin Baguette", vous devez noter `bitcoin-baguette` :
![builder](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite de votre nom dans la même case, par exemple : `bitcoin-baguette/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![builder](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `builder.yml` :
![builder](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre entreprise à l'aide de ce template :

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Voici ce qu'il faut remplir dans chaque clé :
- `name` : Le nom de votre entreprise (obligatoire) ;
- `address` : Le lieu de votre entreprise (facultatif) ;
- `language` : Les pays dans lesquels votre entreprise se trouve ou les langues prises en charge (facultatif) ;
- `links` : Les différents liens officiels de votre entreprise (facultatif) ;
- `tags` : 2 termes qui qualifient votre entreprise (obligatoire) ;
- `category` : La catégorie qui qualifie le mieux le domaine dans lequel votre entreprise opère parmi les choix suivants :
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.

Par exemple, votre fichier YAML pourrait ressembler à celui-ci :

```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - education

category: education
```

![builder](assets/09.webp)
- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![builder](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![builder](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![builder](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![builder](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![builder](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![builder](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![builder](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail (**vérifiez que vous êtes bien sur la même branche que vos modifications précédentes, c'est important !**) :
![builder](assets/17.webp)
- Retournez dans le dossier `resources/builders/` et sélectionnez le dossier de votre entreprise que vous venez de créer dans le commit précédent :
![builder](assets/18.webp)
- Dans le dossier de votre entreprise, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![builder](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![builder](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![builder](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![builder](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![builder](assets/23.webp)
- Retournez dans le dossier `assets` :
![builder](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![builder](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone une image de votre entreprise ou de votre logiciel. C'est cette image qui sera affichée sur le site de PlanB Network :
![builder](assets/26.webp)
- Ça peut être le logo ou une icône :
![builder](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` : 
![builder](assets/28.webp)
- Attention, votre image doit être carrée, doit s'appeler `logo` et doit être au format `.webp`. Le nom complet du fichier devrait donc être : `logo.webp` :
![builder](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![builder](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![builder](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes` :
![builder](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![builder](assets/33.webp)
- Retournez dans le dossier de votre entreprise :
![builder](assets/34.webp)
- Cliquez sur le bouton `Add file`, puis sur `Create new file` :
![builder](assets/35.webp)
- Créez un nouveau fichier YAML en le nommant avec l'indicateur de votre langue natale. Ce fichier va être utilisé pour la description du builder. Par exemple, si je veux rédiger ma description en anglais, je vais nommer ce fichier `en.yml` :
![builder](assets/36.webp)
- Remplissez ce fichier YAML à l'aide de ce modèle :
```yaml
description: |
 
contributors:
 - 
```

- Pour la clé `contributors`, vous pouvez ajouter votre identifiant de contributeur à PlanB Network si vous en avez un. Si vous n'en avez pas, laissez ce champ vide.
- Pour la clé `description`, vous devez simplement ajouter un court paragraphe qui décrit votre entreprise ou votre logiciel. La description doit être dans la même langue que le nom du fichier. Vous n'avez pas besoin de traduire cette description dans toutes les langues prises en charge sur le site, car les équipes de PlanB le feront avec leur modèle. Par exemple, voici à quoi pourrait ressembler votre fichier :
```yaml
description: |
 Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.
contributors:
 - 
```

![builder](assets/37.webp)
- Cliquez sur le bouton `Commit changes` :
![builder](assets/38.webp)
- Vérifiez que la case `Commit directly to the patch-1 branch` est cochée, ajoutez un titre, puis cliquez sur `Commit changes` :
![builder](assets/39.webp)
- Le dossier de votre entreprise devrait dorénavant ressembler à celui-ci :
![builder](assets/40.webp)
- Si tout vous convient, revenez à la racine de votre fork :
![builder](assets/41.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![builder](assets/42.webp)
- Ajoutez un titre clair et une description sur votre PR :
![builder](assets/43.webp)
- Cliquez sur le bouton `Create pull request` :
![builder](assets/44.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir votre profil de builder apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet `Pull requests` sur le dépôt GitHub de PlanB Network :
![builder](assets/45.webp)
Merci beaucoup pour votre précieuse contribution ! :)

