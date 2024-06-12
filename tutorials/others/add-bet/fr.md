---
name: Ajouter des outils pédagogiques
description: Comment ajouter des nouveaux supports éducatifs sur PlanB Network ?
---
![event](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme.

Au-delà des tutoriels et des formations, PlanB Network publie également une grande base de données de contenus éducatifs divers sur Bitcoin que n'importe qui peut télécharger et utiliser [dans le section "BET" (*Bitcoin Educational Toolkit*)](https://planb.network/resources/bet). Ces contenus visuels comprennent des posters éducatifs, des mèmes, des affiches de propagande humoristiques, des schémas techniques, des logos ou encore des outils pour les utilisateurs. L'idée derrière cette initiative est d'aider les personnes et les communautés qui enseignent Bitcoin à travers le monde, en leur fournissant les supports visuels dont ils peuvent avoir besoin.

Vous souhaitez participer à l'enrichissement de cette base de données, mais vous ne savez pas comment faire ? Ce tutoriel est fait pour vous !

*Il est impératif que tous les visuels intégrés au site soient libres de droit ou respectent la licence du fichier source. Aussi, l'intégralité des visuels publiés sur PlanB Network sont mis à disposition sous licence [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Tout d'abord, il vous faut avoir un compte sur GitHub. Si vous ne savez pas comment créer un compte, nous avons fait [un tutoriel détaillé pour vous accompagner](https://planb.network/tutorials/others/create-github-account).
- Rendez-vous sur [le dépôt GitHub de PlanB dédié à la data](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/resources/bet) dans la section `resources/bet/` :
![event](assets/02.webp)
- Cliquez en haut à droite sur le bouton `Add file`, puis sur `Create new file` :
![event](assets/03.webp)
- Si vous n'avez encore jamais contribué sur les contenus de PlanB Network, vous allez devoir créer votre fork du dépôt original. Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Cliquez sur le bouton `Fork this repository` :
![event](assets/04.webp)
- Vous arrivez ensuite sur la page d'édition de GitHub :
![event](assets/05.webp)
- Créez un dossier pour votre contenu. Pour ce faire, dans la case `Name your file...`, notez le nom de votre contenu en minuscules avec des tirets à la place des espaces. Dans mon exemple, disons que je souhaite ajouter un visuel en PDF de la liste de 2048 mots du BIP39. Je vais donc appeler mon dossier `bip39-wordlist` :
![event](assets/06.webp)
- Pour valider la création du dossier, il suffit de noter un slash à la suite du nom dans la même case, par exemple : `bip39-wordlist/`. Le fait d'ajouter un slash permet de créer automatiquement un dossier plutôt qu'un fichier :
![event](assets/07.webp)
- Dans ce dossier, vous allez créer un premier fichier YAML nommé `bet.yml` :
![event](assets/08.webp)
- Remplissez ce fichier avec les informations relatives à votre contenu à l'aide de ce template :

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```

Voici ce qu'il faut remplir dans chaque champs :
- `builder` : Votre identifiant d'organisation sur PlanB Network. Si vous n'avez pas encore d'identifiant "*builder*" pour votre entreprise, vous pouvez l'ajouter [en suivant cet autre tutoriel](https://planb.network/tutorials/others/add-builder). Sinon, vous pouvez simplement noter votre nom, votre pseudo, ou bien le nom de votre entreprise sans avoir créé de profil builder ;
- `type`: La nature de votre contenu entre ces 2 choix :
	- `Educational Content` pour les contenus éducatifs ;
	- `Visual Content` pour les autre contenus divers.
- `links` : Les liens vers vos contenus. Pour ces champs, vous 2 choix. Vous pouvez soit héberger votre contenu directement le GitHub de PlanB, et dans ce cas il faudra compléter les liens de ce fichier durant les étapes suivantes. Ou bien, si vos contenus sont déjà hébergés ailleurs, comme sur votre site web personnel par exemple, vous pouvez renseigner les liens vers ce site dans ces champs :
	- `download` : Un lien pour télécharger votre contenu,
	- `view` : Un lien pour consulter votre contenu (peut être le même lien que celui pour télécharger). Si votre contenu est disponible dans plusieurs langues, vous pouvez ajouter un lien individuel par langue.
- `tags` : Les 2 étiquettes associées à votre contenu comme par exemple :
	- bitcoin,
	- technology,
	- economy,
	- education,
	- meme...
- `contributors` : Votre identifiant de contributeur si vous en avez déjà un.

Par exemple, votre fichier YAML pourrait ressembler à celui-ci : 

```yaml
builder: DecouvreBitcoin
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view: 
    - en: https://penpot.planb.network/#/view/c157057b-fd28-8042-8004-5004d6068cdd?page-id=7d7b7e64-d4bb-807c-8004-50116435dca5&section=interactions&index=0&share-id=7154756b-3ebd-8040-8004-64753689c627&zoom=fill
    - fr: https://penpot.planb.network/#/view/c157057b-fd28-8042-8004-5004d6068cdd?page-id=c2967cf3-0fc9-806b-8004-64732b2071d2&section=interactions&index=0&share-id=7154756b-3ebd-8040-8004-647396aa3682&zoom=fill
    - es: https://penpot.planb.network/#/view/c157057b-fd28-8042-8004-5004d6068cdd?page-id=c2967cf3-0fc9-806b-8004-647329f4f5af&section=interactions&index=0&share-id=7154756b-3ebd-8040-8004-6474b451a565&zoom=fill
tags:
  - bitcoin
  - technology
contributors:
  - rabbit-hole
```

- Dans mon exemple, je vais laisser les liens vides pour le moment, car je vais ajouter mon PDF directement sur GitHub :
![event](assets/09.webp)
- Une fois vos modifications sur ce fichier terminées, enregistrez-les en cliquant sur le bouton `Commit changes...` :
![event](assets/10.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![event](assets/11.webp)
- Cliquez sur le bouton vert `Propose changes` :
![event](assets/12.webp)
- Vous arrivez ensuite sur une page qui résume tous vos changements :
![event](assets/13.webp)
- Cliquez sur votre image de profil GitHub en haut à droite, puis sur `Your Repositories` :
![event](assets/14.webp)
- Sélectionnez votre fork du dépôt de PlanB Network :
![event](assets/15.webp)
- Vous devriez voir apparaître sur le haut de la fenêtre une notification avec votre nouvelle branche. Elle s'appelle sûrement `patch-1`. Cliquez dessus :
![event](assets/16.webp)
- Vous êtes maintenant sur votre branche de travail (**vérifiez que vous êtes bien sur la même branche que vos modifications précédentes, c'est important !**) :
![event](assets/17.webp)
- Retournez dans le dossier `resources/bet/` et sélectionnez le dossier de votre entreprise que vous venez de créer dans le commit précédent :
![event](assets/18.webp)
- Dans le dossier de votre contenu, cliquez sur le bouton `Add file`, puis sur `Create new file` :
![event](assets/19.webp)
- Nommez ce nouveau dossier `assets` et confirmez sa création en mettant un slash `/` à la fin :
![event](assets/20.webp)
- Dans ce dossier `assets`, créez un fichier nommé `.gitkeep` :
![event](assets/21.webp)
- Cliquez sur le bouton `Commit changes...` :
![event](assets/22.webp)
- Laissez le titre du commit par défaut, et vérifiez bien que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![event](assets/23.webp)
- Retournez dans le dossier `assets` :
![event](assets/24.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![event](assets/25.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone une miniature qui représente votre contenu. C'est cette image qui sera affichée sur le site de PlanB Network :
![event](assets/26.webp)
- Ça peut être un aperçu, un logo ou une icône :
![event](assets/27.webp)
- Une fois l'image chargée, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![event](assets/28.webp)
- Attention, votre image doit s'appeler `logo` et doit être au format `.webp`. Le nom complet du fichier devrait donc être : `logo.webp` :
![event](assets/29.webp)
- Retournez dans votre dossier `assets` et cliquez sur le fichier intermédiaire `.gitkeep` :
![event](assets/30.webp)
- Une fois sur le fichier, cliquez sur les 3 petits points en haut à droite puis sur `Delete file` :
![event](assets/31.webp)
- Vérifiez que vous êtes toujours sur la même branche de travail, puis cliquez sur le bouton `Commit changes` :
![event](assets/32.webp)
- Ajoutez un titre et une description à votre commit, puis cliquez sur `Commit changes` :
![event](assets/33.webp)
- Retournez dans le dossier de votre contenu :
![event](assets/34.webp)
- Cliquez sur le bouton `Add file`, puis sur `Create new file` :
![event](assets/35.webp)
- Créez un nouveau fichier YAML en le nommant avec l'indicateur de votre langue natale. Ce fichier va être utilisé pour la description du contenu. Par exemple, si je veux rédiger ma description en anglais, je vais nommer ce fichier `en.yml` :
![event](assets/36.webp)
- Remplissez ce fichier YAML à l'aide de ce modèle :

```yaml
name: 
description: |
  
```

- Pour la clé `name`, vous pouvez ajouter le nom de votre contenu ;
- Pour la clé `description`, vous devez simplement ajouter un court paragraphe qui décrit votre contenu. La description doit être dans la même langue que le nom du fichier. Vous n'avez pas besoin de traduire cette description dans toutes les langues prises en charge sur le site, car les équipes de PlanB le feront avec leur modèle. 

Par exemple, voici à quoi pourrait ressembler votre fichier :

```yaml
name: BIP39 WORDLIST
description: |
  Complete and numbered list of the 2048 English words from the BIP39 dictionary used to encode mnemonic phrases. The document can be printed on a single page.
```

![event](assets/37.webp)
- Cliquez sur le bouton `Commit changes...` :
![event](assets/38.webp)
- Vérifiez que la case `Commit directly to the patch-1 branch` est cochée, ajoutez un titre, puis cliquez sur `Commit changes` :
![event](assets/39.webp)
- Le dossier de votre contenu devrait dorénavant ressembler à celui-ci :
![event](assets/40.webp)

---

*Si vous ne souhaitez pas ajouter de contenu sur GitHub et avez déjà ajouté les liens des contenus dans les étapes précédentes, vous pouvez sauter cette partie et passer directement à la partie sur la Pull Request.*

- Retournez dans le dossier `/assets` :
![event](assets/41.webp)
- Cliquez sur le bouton `Add file`, puis sur `Upload files` :
![event](assets/42.webp)
- Une nouvelle page va s'ouvrir. Glissez et déposez dans la zone le contenu que vous souhaitez partager :
![event](assets/43.webp)
- Par exemple, j'ai ajouté le fichier PDF de la liste BIP39 :
![event](assets/44.webp)
- Une fois le contenu chargé, vérifiez que la case `Commit directly to the patch-1 branch` est cochée, puis cliquez sur `Commit changes` :
![event](assets/45.webp)
- Retournez dans votre dossier `/assets` et cliquez sur le fichier que vous venez de charger :
![event](assets/46.webp)
- Récupérez l'URL intermédiaire de votre fichier. Par exemple, dans mon cas, l'URL est :

```url
https://github.com/tutoriel-pandul/sovereign-university-data/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Conservez uniquement la dernière partie de l'URL à partir de `/ressources` :

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Ajoutez à la base de l'URL les informations suivantes pour avoir le bon lien :

```url
https://github.com/DecouvreBitcoin/sovereign-university-data/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Ce que l'on fait ici, c'est que l'on anticipe le futur lien vers votre fichier, une fois que votre proposition sera fusionnée sur le dépôt source de PlanB Network.

- Retournez sur votre fichier `bet.yml` et cliquez sur l'icône du crayon :
![event](assets/47.webp)
- Ajoutez-y votre lien :
![event](assets/48.webp)
- Une fois vos modifications terminées, cliquez sur le bouton `Commit changes...` :
![event](assets/49.webp)
- Ajoutez un titre pour vos modifications, ainsi qu'une courte description :
![event](assets/50.webp)
- Cliquez sur le bouton vert `Commit changes` :
![event](assets/51.webp)

---

- Si tout vous convient, revenez à la racine de votre fork :
![event](assets/52.webp)
- Vous devriez voir apparaître un message vous indiquant que votre branche a subi des modifications. Cliquez sur le bouton `Compare & pull request` :
![event](assets/53.webp)
- Ajoutez un titre clair et une description sur votre PR :
![event](assets/54.webp)
- Cliquez sur le bouton `Create pull request` :
![event](assets/55.webp)
Félicitations ! Votre PR a bien été créée. Un administrateur va maintenant la vérifier et, si tout est conforme, l'intégrer au dépôt principal de PlanB Network. Vous devriez voir votre BET apparaître sur le site web quelques jours plus tard.

Pensez bien à suivre le progrès de votre PR. Il est possible qu'un administrateur y laisse un commentaire pour demander des informations supplémentaires. Tant que votre PR n'est pas validée, vous pouvez la consulter dans l'onglet Pull requests sur le dépôt GitHub de PlanB Network :
![event](assets/56.webp)
Merci beaucoup pour votre précieuse contribution ! :)