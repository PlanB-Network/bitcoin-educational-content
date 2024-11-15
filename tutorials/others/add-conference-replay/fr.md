---
name: Ajouter un replay de conférence
description: Comment ajouter le replay d'une conférence sur PlanB Network ?
---
![conference](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Vous souhaitez ajouter le replay de votre conférence Bitcoin sur le site de PlanB Network et donner de la visibilité à cet évènement, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !

En revanche, si vous souhaitez ajouter une conférence qui se déroulera dans le futur, je vous conseille de lire cet autre tutoriel dans lequel on vous explique comment ajouter un nouvel évènement sur le site.

https://planb.network/tutorials/others/add-event


![conference](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait un tutoriel détaillé pour vous accompagner.

https://planb.network/tutorials/others/create-github-account


- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) dans la section `resources/conference/` :
![conference](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![conference](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![conference](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![conference](assets/05.webp)
- Créez un dossier pour votre conférence. Pour ce faire, dans la case `Name your file...`, notez le nom de votre conférence en minuscules avec des tirets à la place des espaces. Par exemple, si votre conférence s'appelle "Paris Bitcoin Conférence", vous devez noter `paris-bitcoin-conference`. Ajoutez également l'année de votre conférence, par exemple : `paris-bitcoin-conference-2024` :
![conference](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite de votre nom dans la même case, par exemple : `paris-bitcoin-conference-2024/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![conference](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `conference.yml` :
![conference](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre conférence à l'aide de ce template :

```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Par exemple, votre fichier YAML pourrait ressembler à celui-ci :

```yaml
year: 2024-08
name: Paris Bitcoin Conférence 2024
builder: Paris Bitcoin Conférence
location: Paris, France 
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - International
  - All Public
```

![conference](assets/09.webp)

Si vous n'avez pas encore d'identifiant "*builder*" pour votre organisation, vous pouvez l'ajouter en suivant cet autre tutoriel.

https://planb.network/tutorials/others/add-builder



- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![conference](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![conference](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![conference](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![conference](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![conference](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![conference](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![conference](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail :
![conference](assets/17.webp)
- Retournez dans le dossier `resources/conference/` et sélectionnez le dossier de votre conférence que vous venez de créer dans le commit précédent :
![conference](assets/18.webp)
- Dans le dossier de votre conférence, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![conference](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![conference](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![conference](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![conference](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![conference](assets/23.webp)
- Retournez dans le dossier `assets` :
![conference](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![conference](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone une image qui représente votre conférence et sera affichée sur le site de PlanB Network :
![conference](assets/26.webp)
- Ça peut être le logo, une miniature ou encore une affiche :
![conference](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` : 
![conference](assets/28.webp)
- Attention, votre image doit s'appeler `thumbnail` et doit être au format `.webp`. Le nom complet du fichier devrait donc être : `thumbnail.webp` :
![conference](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![conference](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![conference](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes` :
![conference](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![conference](assets/33.webp)
- Revenez dans votre dossier de conférence :
![conference](assets/34.webp)
- Cliquez sur le bouton `Add file`, puis sur `Create new file` :
![conference](assets/35.webp)
- Créez un nouveau fichier markdown (.md) en le nommant avec l'indicateur de votre langue natale. Ce fichier va être utilisé pour les replays de votre conférence. Par exemple, si je veux rédiger les descriptions des conférences en anglais, je vais nommer ce fichier en.md :
![conference](assets/36.webp)
- Remplissez ce fichier markdown à l'aide de ce modèle que vous pouvez adapter à la configuration de votre conférence :

```markdown
---
name: Paris Bitcoin Conférence 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
--- 

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin ?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```

![conference](assets/37.webp)

---

- Au début de votre document, dans le "front matter", complétez le champ `name:` avec le nom de votre conférence et l'année des replays. Dans le champ `description:`, rédigez une courte description de votre événement dans la langue du fichier. Par exemple, pour un fichier nommé `en.md`, la description doit être en anglais. L'équipe de PlanB Network se chargera de traduire votre description grâce à leur modèle.

- Les titres de premier niveau, marqués par un `#`, servent à organiser la conférence par scènes. Par exemple, `# Main Stage` pour la grande scène principale et `# Workshop Room` pour une scène dédiée aux workshops.

- Les titres de second niveau, marqués par un double `##`, sont utilisés pour séparer les différentes vidéos de replay. Si les conférences ont été filmées en continu sur une demi-journée, indiquez, par exemple, `## Friday morning`. Si les conférences ont été filmées et rediffusées individuellement, nommez directement la conférence avec un titre de second niveau.

- Sous chaque titre de second niveau, insérez un lien vers la vidéo de replay correspondante. La syntaxe doit être : `![video](https://youtu.be/XXXXXXXXXXXX)`, en remplaçant `XXXXXXXXXXXX` par le véritable lien de la vidéo.

- Si le format le permet (conférences individuelles), vous pouvez ajouter le nom des intervenants. Pour cela, ajoutez le champs `Speaker:` suivi du nom ou du pseudonyme de l'intervenant sous le lien de la vidéo. En cas de multiples intervenants, séparez chaque nom par une virgule, comme cela par exemple : `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![conference](assets/38.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![conference](assets/39.webp)
- Cliquez sur `Commit changes` :
![conference](assets/40.webp)
- Le dossier de votre conférence devrait dorénavant ressembler à celui-ci :
![conference](assets/41.webp)
- Si tout vous convient, revenez à la racine de votre fork :
![conference](assets/42.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![conference](assets/43.webp)
- Ajoutez un titre clair et une description sur votre PR :
![conference](assets/44.webp)
- Cliquez sur le bouton `Create pull request` :  
![conference](assets/45.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir les replays de votre conférence apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet `Pull requests` sur le dépôt GitHub de PlanB Network :
![conference](assets/46.webp)
Merci beaucoup pour votre précieuse contribution ! :)

