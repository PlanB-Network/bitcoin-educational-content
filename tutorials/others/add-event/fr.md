---
name: Ajouter un évènement sur PlanB Network
description: Comment proposer l'ajout d'un nouvel évènement sur PlanB Network ?
---
![event](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Vous souhaitez ajouter une conférence Bitcoin sur le site de PlanB Network et donner de la visibilité à votre évènement, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !

En revanche, si vous souhaitez ajouter les replays d'un conférence qui s'est déjà déroulée, je vous conseille de lire cet autre tutoriel dans lequel on vous explique comment ajouter une nouvelle ressource sur le site.

https://planb.network/tutorials/others/contribution/add-conference-replay-3282deba-16ab-4dd9-8357-680902bfb527


![event](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait un tutoriel détaillé pour vous accompagner.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) dans la section `resources/conference/` :
![event](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![event](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![event](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![event](assets/05.webp)
- Créez un dossier pour votre conférence. Pour ce faire, dans la case `Name your file...`, notez le nom de votre conférence en minuscules avec des tirets à la place des espaces. Par exemple, si votre conférence s'appelle "Paris Bitcoin Conférence", vous devez noter `paris-bitcoin-conference`. Ajoutez également l'année de votre conférence, par exemple : `paris-bitcoin-conference-2024` :
![event](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite de votre nom dans la même case, par exemple : `paris-bitcoin-conference-2024/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![event](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `events.yml` :
![event](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre conférence à l'aide de ce template :

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website: 
    replay_url:
    live_url :
  tags: 
    - 
```

Par exemple, votre fichier YAML pourrait ressembler à celui-ci : 

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, France
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conférence 2024
  builder: Paris Bitcoin Conférence
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: The largest Bitcoin conference in France with over 8,000 participants each year!
  language: 
    - fr
    - en
    - es
    - it
  links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url :
  tags: 
    - Bitcoiner
    - General
    - International
```
![event](assets/09.webp)
Si vous n'avez pas encore d'identifiant "*builder*" pour votre organisation, vous pouvez l'ajouter en suivant cet autre tutoriel.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d



- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![event](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![event](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![event](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![event](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![event](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![event](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![event](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail :
![event](assets/17.webp)
- Retournez dans le dossier `resources/conference/` et sélectionnez le dossier de votre conférence que vous venez de créer dans le commit précédent :
![event](assets/18.webp)
- Dans le dossier de votre conférence, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![event](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![event](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![event](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![event](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![event](assets/23.webp)
- Retournez dans le dossier `assets` :
![event](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![event](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone une image qui représente votre conférence et sera affichée sur le site de PlanB Network :
![event](assets/26.webp)
- Ça peut être le logo, une miniature ou encore une affiche :
![event](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` : 
![event](assets/28.webp)
- Attention, votre image doit s'appeler `thumbnail` et doit être au format `.webp`. Le nom complet du fichier devrait donc être : `thumbnail.webp` :
![event](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![event](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![event](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes` :
![event](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![event](assets/33.webp)
- Revenez à la racine de votre dépôt :
![event](assets/34.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![event](assets/35.webp)
- Ajoutez un titre clair et une description sur votre PR :
![event](assets/36.webp)
- Cliquez sur le bouton `Create pull request` :
![event](assets/37.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir votre évènement apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet `Pull requests` sur le dépôt GitHub de PlanB Network :
![event](assets/38.webp)
Merci beaucoup pour votre précieuse contribution ! :)



