---
name: Lignes directrices pour la relecture
description: Quels sont les facteurs importants à prendre en compte lors de la relecture sur Plan ₿ Academy ?
---

![github](assets/cover.webp)


Bienvenue dans ce tutoriel sur les **règles à suivre lors de la relecture de contenu sur Plan ₿ Academy**. Nous sommes heureux que vous partagiez notre mission de traduire les ressources sur Bitcoin dans le plus grand nombre de langues possible, afin d'aider les gens à prendre conscience de son fonctionnement et de la manière dont il peut être utilisé dans leur vie quotidienne.


Tout d'abord, contribuer au [dépôt public](https://github.com/PlanB-Network/Bitcoin-educational-content) de Plan ₿ Academy vous donne la possibilité d'écrire des tutoriels, de relire le contenu existant, ou même de proposer l'ajout d'une nouvelle langue à la plateforme. Pour en savoir plus, rejoignez d'abord notre [groupe Telegram](https://t.me/PlanBNetwork_ContentBuilder), et écrivez une brève présentation de vous et des langues que vous pouvez parler.


Ce tutoriel est dédié aux contributeurs qui souhaitent relire du contenu. La plupart d'entre eux ne connaissent pas grand-chose à [Github](https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ou au [langage Markdown](https://www.markdownguide.org/basic-syntax/) que nous utilisons dans le dépôt, il est donc important de partager quelques idées sur les facteurs clés impliqués dans cette tâche.


Ci-dessous, j'ai rassemblé les problèmes les plus courants rencontrés par les correcteurs. N'hésitez pas à en suggérer d'autres, car cela peut aider d'autres personnes à s'améliorer.


Avant de plonger dans les détails, la première chose à faire est de lire ce tutoriel sur les actions pratiques à suivre sur Github, en forkant le dépôt Plan ₿ Academy, en commettant des changements et en envoyant des PRs :


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Qu'est-ce que la relecture ?


La relecture est le processus de révision finale d'un texte écrit, qui permet d'identifier et de corriger les erreurs de grammaire, d'orthographe, de ponctuation et de formatage. Elle permet de s'assurer que le texte est clair, cohérent et exempt d'erreurs avant sa publication ou sa soumission.


Lorsque vous effectuez ce type de tâche, il est important de respecter le sens de la langue d'origine (EN ou FR), tout en veillant à ce que le texte dans la langue finale soit aussi fluide que possible pour un locuteur natif.


N'oubliez jamais que la traduction/relecture est de l'ÉDUCATION !


En effet, notre objectif commun est d'éduquer le plus grand nombre de personnes possible sur le Bitcoin, et il est donc fondamental que les documents qu'elles lisent soient clairs et faciles à comprendre.

En ce sens, tous les contributeurs de Plan ₿ Academy sont des éducateurs !


## Les premières étapes de la relecture sur Plan ₿ Academy


Avant de commencer une nouvelle tâche de relecture, annoncez-la dans le [groupe Telegram](https://t.me/PlanBNetwork_ContentBuilder) ou informez votre coordinateur Plan ₿ Academy, qui ouvrira une "[issue](https://github.com/orgs/PlanB-Network/projects/3)" dédiée. Lorsque vous recevrez le lien de l'issue, il vous suffira de **commenter que vous commencez** la tâche de relecture de ce contenu.


Ce système aide le coordinateur à suivre l'évolution de la situation dans le répertoire et permet au contenu d'être "revendiqué" par le relecteur, ce qui évite la duplication des efforts par quelqu'un d'autre.

Dans l'issue elle-même, vous trouverez les liens qui vous redirigent vers le contenu à vérifier. Vous pouvez simplement cliquer dessus ou, mieux encore, vous pouvez retourner à votre propre dépôt forké et travailler directement à partir de là. Voyons comment vous pouvez le faire !


Tout d'abord, **n'oubliez JAMIAS de SYNCHRONISER votre dépôt, sur la branche `dev`**. De cette façon, le contenu sera toujours mis à jour avant que vous ne commenciez n'importe quel type de tâche, et vous ne créerez pas de conflits entre les anciens et les nouveaux éléments. Assurez-vous de cliquer sur `Sync Fork` puis sur `Update branch`.



![REVIEW](assets/en/1.webp)



Une fois la synchronisation réussie, vous pouvez accéder directement au contenu qui vous intéresse et effectuer un "commit" sur une nouvelle branche, comme le montre ce [tutoriel](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Sinon, vous pouvez ouvrir une nouvelle branche où travailler, en cliquant sur `Branches`, comme indiqué ci-dessous.



![REVIEW](assets/en/2.webp)



Dans cette nouvelle page, vous trouverez toutes les branches que vous avez déjà ouvertes sous le titre `Your branches`. Cette section est très utile car elle vous permet de retrouver facilement l'endroit où vous avez modifié un contenu. Si vous souhaitez ouvrir une nouvelle branche, vous pouvez cliquer sur `New branch` dans le coin supérieur droit de la page.



![REVIEW](assets/en/3.webp)



Vous obtiendrez ensuite une fenêtre dans laquelle vous devrez indiquer le nom de la nouvelle branche. Dans le cas ci-dessous, j'ai choisi de l'appeler "BTC101-FR". De cette façon, je me souviendrai toujours que cette branche spécifique doit être utilisée pour la relecture du cours BTC101 en français, et **je ne l'utiliserai pour aucune autre tâche**.


Je vous suggère de faire de même : veillez à ouvrir une nouvelle branche chaque fois que vous devez commencer une nouvelle tâche.



![REVIEW](assets/en/4.webp)



Après avoir créé cette nouvelle branche, assurez-vous de cliquer dessus depuis `Your branches` dans la page précédente et commencez à travailler sur le fichier `.md` lié au contenu spécifique (dans mon cas, je vais cliquer sur `courses` -> `BTC101` -> `fr.md`). Tous les commits liés au fichier spécifique devront être commis (sauvegardés) à l'intérieur de la même branche.



## Langue originale ou traduction ?


Lors de la relecture d'un contenu, il est important de **toujours vérifier la version originale en anglais (ou en français)**. Sachez que nous traduisons à l'aide d'outils linguistiques d'IA, et que le rendu dans la langue cible peut donc ne pas être fluide ou bien compréhensible pour le lecteur final.


N'hésitez donc pas à ajuster le texte et à modifier les phrases, si nécessaire. Notre objectif est d'améliorer la fluidité, mais toujours en respectant le sens original. En cas de doute sur la manière de traiter un mot spécifique, n'hésitez pas à demander au coordinateur de la traduction.


Les outils LLM peuvent traduire littéralement certains mots liés à Bitcoin, comme Lightning Network. C'est notamment le cas lorsqu'il s'agit de mots très techniques. Dans de tels cas, il est conseillé de conserver le mot anglais original dans votre langue cible pour plus de clarté, à moins que vos règles linguistiques ne vous imposent de traduire chaque mot.


Dans ce deuxième cas, **faites toujours des recherches pour vérifier si quelqu'un d'autre dans votre communauté Bitcoin a déjà traduit ce mot** et s'il est désormais largement utilisé.



- Une solution pourrait être de **vérifier sur [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** dans votre langue cible pour voir si le mot a été traduit ou non. Si ce n'est pas le cas, vous conservez le mot en anglais.



- Dans tous les cas, mon conseil serait d'**insérer le mot en anglais, tout en ajoutant** le sens correspondant dans la langue cible entre parenthèses, en suivant le schéma EN (LANG), ou inversement. Exemple : Address (indirizzo), ou indirizzo (Address).



- Une autre bonne solution consiste à conserver le mot/phrase original en anglais, puis **créer un lien hypertexte** qui redirige vers le [glossaire](https://planb.academy/resources/glossary) sur planb.academy. Pour ce faire, vous devez insérer le mot/phrase entre crochets, et le lien entre parenthèses, comme vous pouvez le voir dans l'exemple ci-dessous :


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


Dans le résultat final (image ci-dessous), vous ne visualiserez pas le lien entier, et le mot deviendra cliquable.



![REVIEW](assets/en/5.webp)



Veuillez noter que le lien vers le glossaire que vous obtiendrez sur le site web contient le code de langue après le mot "academy" (exemple : `https://planb.academy/en/resources/glossary/utxo`-> ici vous pouvez lire le code de langue "en"). Dans ce cas, **supprimez le code de langue du lien**, comme vous l'avez vu dans l'encadré ci-dessus. De cette façon, le système amènera automatiquement le lecteur à la langue qu'il a choisie.


Le contenu du dépôt est rempli d'hyperliens comme ceux présentés ci-dessus. Maintenant que vous savez ce qu'ils signifient, **veillez à ne pas supprimer les liens** insérés par l'auteur original.



- Une autre chose liée à la restitution des mots est la suivante. Si vous trouvez "Plan ₿ Academy" dans le texte, **laissez-le dans sa forme originale**. Ne traduisez pas le mot "plan" ou le mot "academy ". En outre, n'utilisez PAS l'article "Le" lorsque vous présentez Plan ₿ Academy : **considérez-le comme une marque**.



- Il en va de même pour "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", qui doivent également être conservés sous leur forme originale.


Une dernière remarque à propos de ce paragraphe : comme nous l'avons dit plus haut, nous utilisons des outils d'IA pour traduire le contenu, puis nous demandons l'intervention des contributeurs pour nous assurer que tout est fluide et bien relu.


Si vous utilisez l'IA pour relire la majorité du texte, nous ne manquerons pas de le remarquer, car nous sommes familiarisés avec les structures de phrases typiques générées par l'IA. Si nous constatons que vous vous êtes fié uniquement à l'IA pour la relecture, sans apporter de modifications significatives, la récompense finale en sats peut être réduite de moitié !



## La structure des en-têtes


Dans le langage markdown, les en-têtes (et les titres de paragraphes) commencent tous par le signe hash ``#``. Le nombre de signes hash correspond au niveau de l'en-tête. Par exemple, un titre de niveau 3 comporte trois signes avant le texte (exemple, `### Mon titre`).


Dans les cours, les parties les plus importantes sont introduites par un seul signe hash, tandis que les sous-parties peuvent comporter de deux à quatre signes hash. Dans les tutoriels, nous n'utilisons normalement que des en-têtes comportant deux signes hash.



![REVIEW](assets/en/6.webp)



Veillez à **ne JAMAIS supprimer les signes hash** avant un titre, sinon vous créerez des problèmes avec la structure du texte.


En même temps, **ne changez pas** la partie chapterID que vous pouvez voir dans l'image ci-dessus, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ou les références vidéo comme ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Lorsque nous insérons ``#`` devant un titre, il deviendra automatiquement gras dans l'aperçu du cours, donc **évitez de mettre les titres en gras lors de la correction**.


Par ailleurs, dans la version anglaise des cours, les **titres introduits par un ou deux ``#`` ont tous les mots commençant par une majuscule**, alors que les titres commençant par trois ou quatre ``#`` ne suivent généralement pas cette règle. Dans la mesure du possible, veillez à ce que les titres dans votre langue cible suivent cette structure.



## La section initiale des cours


Au début de tout contenu, vous trouverez les mots minuscules statiques suivants : `name`, `goal`, `objectives`. Ils sont utilisés par le site web pour décoder le contenu lui-même et sont **toujours laissés en anglais**. Par conséquent, ne les traduisez pas, sinon le contenu créera des problèmes de synchronisation. Veillez à ne relire que la partie située après les deux-points, qui est automatiquement traduite par l'IA.



![REVIEW](assets/en/7.webp)



Dans cette même section initiale, conservez le format tel quel. N'ajoutez rien au début du texte. Par exemple, évitez d'ajouter "tt" avant les tirets, comme dans l'image ci-dessous !



![REVIEW](assets/en/8.webp)

## Comment gérer les images des cours

Notre site web propose désormais des images traduites pour presque tous les cours !

Lorsque vous relisez, vérifiez toujours que toutes les images sont présentes et affichées correctement. Dans la `vue code`, si vous trouvez ce type de ligne `![IMAGE](assets/en/001.webp)`, cela signifie qu'une image sera affichée à cet endroit.

Assurez-vous de toujours ajouter une nouvelle ligne entre le code de l'image et le texte. Un exemple ci-dessous :

```
CONFIGURATION INCORRECTE :
- pour commencer à traduire, cliquez sur le bouton `Translate` : ![language](assets/08.webp)
Pour enregistrer, cliquez sur `save` !
  
CONFIGURATION CORRECTE :

- pour commencer à traduire, cliquez sur le bouton `Translate` : 

![language](assets/08.webp)

Pour enregistrer, cliquez sur `save` !
```

Par ailleurs, pensez à lire le contenu de chaque image. Si vous remarquez des problèmes avec la traduction du texte à l'intérieur des images, informez votre coordinateur et vous aurez l'occasion de les relire également !

Vous pouvez visualiser l'image dans la section `Preview` de Github (ou sur notre site web, ouvert dans un autre onglet). Ensuite, revenez à la section `code` à côté pour la relecture.

![REVIEW](assets/en/9.webp)

## Recommandations sur le format


Vous trouverez ci-dessous quelques exemples de problèmes de format auxquels il convient de prêter attention lors de la relecture d'un contenu dans votre langue cible.



- Faites attention aux ponctuations étranges comme ``*\*\'', ou ``**`` qui peuvent représenter un mauvais rendu du symbole gras. Dans l'image ci-dessous, vous pouvez voir que les astérisques ne se trouvent qu'à droite du mot, ce qui donne un rendu étrange.



![REVIEW](assets/en/10.webp)



Par conséquent, vérifiez toujours le texte original en anglais pour voir si un texte en gras est censé s'y trouver. Dans ce cas, il suffit d'ajouter deux astérisques au début du mot pour qu'il apparaisse correctement sur le site web. En fait, dans le langage Markdown, **pour afficher un texte en gras, vous devez insérer deux astérisques ``**`` à la fois avant et après le mot/la phrase** (voir l'exemple ci-dessous).



![REVIEW](assets/en/11.webp)




- Les mêmes problèmes peuvent se produire avec des symboles comme ``$`` et `` ` ``. Veillez à vérifier le fichier de la langue originale (souvent EN ou FR) pour voir où ces symboles sont censés se trouver. Vous pouvez toujours demander l'aide du coordinateur à ce sujet.



- Si vous trouvez des guillemets, assurez-vous de faire des recherches en ligne pour trouver la bonne traduction dans votre langue. Les guillemets sont généralement insérés après le symbole ``>``.



![REVIEW](assets/en/12.webp)

## Relecture du questionnaire


Saviez-vous que vous pouvez également relire les questions des quiz de chaque cours ? Par exemple, si vous souhaitez relire les quiz du cours BTC101, vous pouvez ouvrir une branche dédiée et suivre le chemin suivant : `courses` -> `BTC101` -> `quiz`. Vous y trouverez tous les dossiers dédiés à chaque question, ainsi que le fichier linguistique correspondant au format _yml_.


Une fois de plus, assurez-vous que vous vous trouvez dans une branche spécialement ouverte à cet effet et informez-en toujours le coordinateur.


Une chose importante à garder à l'esprit lors de la relecture de ce type de fichier _yml_ est d'éviter d'ajouter des deux-points ``:`` à l'intérieur du texte. En fait, le deux-points est **uniquement** utilisé pour séparer les paires clé-valeur comme `wrong_answers` du reste. Vous pouvez voir un exemple dans l'image ci-dessous :


![REVIEW](assets/en/13.webp)


Après avoir relu la question, assurez-vous de changer le statut `reviewed` de `false` à `true`, comme le montre l'image ci-dessous. Veillez à ce que ces mots d'état restent en anglais, quelle que soit la langue dans laquelle vous travaillez !



![REVIEW](assets/en/14.webp)


Si la ligne de statut `reviewed:true` est manquante, assurez-vous de **l'ajouter à la fin du quiz**.

## Relecture de tutoriel

Si vous décidez de relire des tutoriels, le coordinateur ouvrira une issue dédiée pour **toute la section du tutoriel**. Lorsque vous terminez votre tâche, vous pouvez documenter votre progression en commentant dans l'issue avec une liste des tutoriels révisés : de cette façon, vous créez un système de suivi clair pour référence future, ce qui est important car du nouveau contenu est ajouté chaque mois. Vous pouvez voir un exemple de cette approche [ici](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).

![REVIEW](assets/en/15.webp)

Étant donné que de nouveaux tutoriels sont ajoutés mensuellement, votre branche peut devenir obsolète pendant le processus de relecture. Certains relecteurs ont abordé ce problème en synchronisant la branche exacte sur laquelle ils travaillent : **s'il vous plaît, ne faites JAMAIS cela ! Si vous le faites, vous risquez de perdre toute la progression que vous avez réalisée jusqu'à ce moment !**

Au lieu de cela, vous devez d'abord finir de relire les tutoriels dans votre fork actuel. Ensuite, **synchronisez `dev`**, et créez une nouvelle branche où vous vous concentrez sur la relecture des tutoriels nouvellement ajoutés (uniquement ceux qui manquent dans votre branche précédente).

Dans les tutoriels, il y a une chance que **les images ne soient pas traduites**. Étant donné que la plupart des tutoriels sont **rédigés à l'origine en français ou en anglais**, vous trouverez probablement des images qui contiennent des commandes ou des instructions dans leur langue d'origine. Prenons un exemple du tutoriel sur Sparrow en néerlandais, en présentant à la fois le texte et l'image associée.

```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```

![REVIEW](assets/en/16.webp)

Comme vous pouvez le voir, l'image indique clairement `Public Server`, en anglais, tandis que le texte mentionne l'expression `_Publieke server_`. Dans ce cas, il y a un problème de cohérence, car le lecteur trouve des informations contradictoires en confrontant l'image avec le texte.

Pour résoudre ce problème, vous pouvez insérer la commande telle qu'elle apparaît dans l'image (anglais ou français), suivie de la traduction dans votre langue entre parenthèses, comme indiqué ci-dessous :

```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```


## Relecture du glossaire


Tout comme les quiz, vous pouvez également relire le glossaire. Le glossaire original a été rédigé en français, vous y trouverez donc des phrases comme : "En français, cette expression peut se traduire par..."


Dans ce cas, veuillez adapter la phrase à votre langue cible ou à l'anglais. Par exemple, vous pouvez écrire "En anglais, cette expression...".

Si le titre est laissé en anglais, vous pouvez adapter la phrase à votre langue : "En swahili, cette expression..."


En outre, veillez à écrire les titres en LETTRES MAJUSCULES.


![REVIEW](assets/en/17.webp)


## Le titre et la description de votre PR


Lorsque vous envoyez votre PR (*Pull Request*), il serait souhaitable que vous le nommiez en utilisant ce format : [RELECTURE] NOM DU CONTENU - LANGUE :


```
[PROOFREADING] BTC101 - ENGLISH
```


En outre, dans le **commentaire de la PR**, vous pouvez écrire "closes" + le numéro de l'issue que le coordinateur vous a envoyé lorsque vous avez commencé la relecture, précédé par ``#``.

Par exemple, si vous venez d'envoyer une PR avec la relecture de CYP201 + quiz, vous pouvez écrire "closes [#2934](https://github.com/PlanB-Network/Bitcoin-educational-content/issues/2934)".


De cette manière, la PR et l'issue seront liées, et quiconque consulte le dépôt public Github peut facilement trouver des informations.



## Autres bonnes pratiques



- Si vous avez besoin de rechercher des mots spécifiques dans le texte, vous pouvez cliquer sur ``CTRL+F`` et la section rechercher-remplacer apparaîtra. Cette partie est très utile lorsque vous avez besoin de sauter à une partie spécifique du texte, ou que vous avez besoin de remplacer des mots/phrases spécifiques par lots, sans faire défiler le contenu complet.



![REVIEW](assets/en/18.webp)



Lorsque vous utilisez la fonction "remplacer tout", il est important de vérifier les résultats pour s'assurer que les liens n'ont pas été modifiés. Par exemple, si vous souhaitez remplacer le mot "Bitcoin" par "Bitkoin" (ce qui peut être nécessaire dans certaines langues), la fonction "remplacer tout" permet de mettre à jour efficacement toutes les occurrences dans le texte. Toutefois, il faut savoir que cet outil modifiera également tous les liens contenant ce mot, ce qui peut entraîner des problèmes de redirection.


Dans l'exemple ci-dessous, le correcteur a utilisé la fonction ci-dessus pour remplacer "Satoshi" par "Satoshi(Sats)", et a également modifié le lien vers un didacticiel contenant le mot lui-même. En conséquence, le lien est devenu invalide.


Vérifiez toujours tous les liens hypertextes dans le texte, afin de vous assurer qu'ils sont corrects.



![REVIEW](assets/en/19.webp)




- Si l'auteur insère un lien renvoyant à un cours ou à un tutoriel Plan ₿ Academy (**non** entre parenthèses), le site web créera automatiquement une "carte" affichant la vignette correspondante. Par conséquent, veillez toujours à **ajouter une nouvelle ligne entre le texte et le lien lui-même**, sinon vous risquez de voir apparaître l'erreur suivante sur le site web.



![REVIEW](assets/en/20.webp)


Il en va de même pour les "codes d'image" comme celui-ci ``[IMAGE](asset/fr/001.webp)`` : veillez à toujours ajouter une nouvelle ligne entre le code d'image et le texte. Un exemple ci-dessous :


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```


## Conclusion

Pour résumer, être conscient des erreurs courantes des relecteurs peut vraiment vous aider à améliorer vos compétences lors de la vérification du contenu. Il est facile de négliger des éléments comme le contexte ou la cohérence, et détecter ces erreurs peut faire une grande différence.

Gardez toujours à l'esprit qu'un débutant peut lire ces cours et tutoriels, il est donc de notre responsabilité de nous assurer qu'ils comprennent pleinement. **En tant que relecteur, vous êtes un éducateur !**

Vous êtes maintenant prêt à commencer à relire les cours, tutoriels, quiz et mots du glossaire. Restez à l'écoute pour commencer à vérifier également les transcriptions vidéo !

Merci d'avoir lu ce tutoriel et profitez de votre parcours de relecture !