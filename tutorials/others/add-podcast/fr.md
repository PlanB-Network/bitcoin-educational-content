---
name: Ajouter un podcast sur PlanB Network
description: Comment ajouter un nouveau podcast sur PlanB Network ?
---
![podcast](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Vous souhaitez ajouter un podcast Bitcoin sur le site de PlanB Network et donner de la visibilité à votre émission, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !
![podcast](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait un tutoriel détaillé pour vous accompagner.

https://planb.network/tutorials/others/create-github-account


- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) dans la section `resources/podcasts/` :
![podcast](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![podcast](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![podcast](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![podcast](assets/05.webp)
- Créez un dossier pour votre podcast. Pour ce faire, dans la case `Name your file...`, notez le nom de votre podcast en minuscules avec des tirets à la place des espaces. Par exemple, si votre émission s'appelle "Super Podcast Bitcoin", vous devez noter `super-podcast-bitcoin` :
![podcast](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite de votre nom de podcast dans la même case, par exemple : `super-podcast-bitcoin/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![podcast](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `podcast.yml` :
![podcast](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre podcast à l'aide de ce template :

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Voici les informations à remplir pour chaque champ :

- **`name`** : Indiquez le nom de votre podcast.

- **`host`** : Indiquez les noms ou pseudos des intervenants ou de l'hôte du podcast. Chaque nom doit être séparé par une virgule.

- **`language`** : Indiquez le code de la langue parlée dans votre podcast. Par exemple, pour l'anglais, notez `en`, pour l'italien `it`...

- **`links`** : Fournissez les liens vers vos contenus. Vous avez deux options :
	- `podcast` : le lien vers votre podcast,
	- `twitter` : le lien vers le profil Twitter du podcast ou de l'organisation qui le produit,
	- `website` : le lien vers le site web du podcast ou de l'organisation qui le produit.

- **`description`** : Ajoutez un court paragraphe qui décrit votre podcast. La description doit être dans la même langue que celle indiquée dans le champ `language:`.

- **`tags`** : Ajoutez deux étiquettes associées à votre podcast. Exemples :
    - `bitcoin`
    - `technology`
    - `economy`
    - `education`...

- **`contributors`** : Mentionnez votre identifiant de contributeur si vous en avez un.

Par exemple, votre fichier YAML pourrait ressembler à celui-ci : 

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
  - bitcoin
  - technology
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![podcast](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![podcast](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![podcast](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![podcast](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![podcast](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![podcast](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![podcast](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail :
![podcast](assets/17.webp)
- Retournez dans le dossier `resources/podcast/` et sélectionnez le dossier de votre podcast que vous venez de créer dans le commit précédent :
![podcast](assets/18.webp)
- Dans le dossier de votre podcast, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![podcast](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![podcast](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![podcast](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![podcast](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![podcast](assets/23.webp)
- Retournez dans le dossier `assets` :
![podcast](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![podcast](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone le logo de votre podcast. Cette image sera affichée sur le site de PlanB Network :
![podcast](assets/26.webp)
- Attention, l'image doit être carrée, afin de s'adapter au mieux à notre site web :
![podcast](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` : 
![podcast](assets/28.webp)
- Attention, votre image doit s'appeler `logo` et doit être au format `.webp`. Le nom complet du fichier devrait donc être : `logo.webp` :
![podcast](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![podcast](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![podcast](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes` :
![podcast](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![podcast](assets/33.webp)
- Revenez à la racine de votre dépôt :
![podcast](assets/34.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![podcast](assets/35.webp)
- Ajoutez un titre clair et une description sur votre PR :
![podcast](assets/36.webp)
- Cliquez sur le bouton `Create pull request` :
![podcast](assets/37.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir votre podcast apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet `Pull requests` sur le dépôt GitHub de PlanB Network :
![podcast](assets/38.webp)
Merci beaucoup pour votre précieuse contribution ! :)
