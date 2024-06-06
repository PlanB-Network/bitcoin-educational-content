---
name: 
description:
---
![github](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Vous souhaitez ajouter une conférence Bitcoin sur le site de PlanB Network et donner de la visibilité à votre évènement, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !

- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait [un tutoriel détaillé pour vous accompagner](https://planb.network/tutorials/others/create-github-account).
- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/conference) dans la section `resources/conference/` :

- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :

- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :

- Vous arrivez ensuite sur la page d'édition de GitHub :

- Créez un dossier pour votre conférence. Pour ce faire, dans la case `Name your file...`, tapez le nom de votre conférence en minuscules avec des tirets à la place des espaces. Par exemple, si votre conférence s'appelle "Paris Bitcoin Conférence", vous devez noter `paris-bitcoin-conference`. Ajoutez également l'année de votre conférence, par exemple : `paris-bitcoin-conference-2024` :

- Pour valider la création du dossier, il suffit de taper un slash à la suite de votre nom dans la même case, par exemple : `paris-bitcoin-conference-2024/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier :

- Dans ce dossier, vous allez créer un premier fichier YAML nommé `events.yml` :

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

Si vous n'avez pas encore d'identifiant "*builder*" pour votre organisation, vous pouvez l'ajouter [en suivant cet autre tutoriel](https://planb.network/tutorials/others/add-builder).

- Une vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :

- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :

- Cliquez sur le bouton vert `Propose changes` :

- Vous arrivez ensuite sur une page qui résume tous vos changements :

- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :

- Sélectionnez votre fork du dépôt de PlanB Network :

- Vous devriez voir apparaitre sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :

- Vous êtes maintenant sur votre branche de travail :

- Retournez dans le dossier `resources/conference/` et sélectionnez le dossier de votre conférence que vous venez de créer dans le commit précédent :

- Dans le dossier de votre conférence, cliquez sur le bouton `Add file`, puis sur `Create new file` :





