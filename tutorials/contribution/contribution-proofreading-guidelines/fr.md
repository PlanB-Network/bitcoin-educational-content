---
name: Lignes directrices pour la relecture
description: Quels sont les facteurs importants à prendre en compte lors de la relecture sur Plan ₿ Network ?
---

![github](assets/cover.webp)


Bienvenue dans ce tutoriel sur les **règles à suivre lors de la relecture de contenu sur Plan ₿ Network**. Nous sommes heureux que vous partagiez notre mission de traduire les documents Bitcoin dans le plus grand nombre de langues possible, afin d'aider les gens à prendre conscience de son fonctionnement et de la façon dont il peut être utilisé dans leur vie quotidienne.


Tout d'abord, contribuer au [dépôt public] (https://github.com/PlanB-Network/Bitcoin-educational-content) de Plan ₿ Network vous donne la possibilité d'écrire des tutoriels, de relire le contenu existant, ou même de proposer l'ajout d'une nouvelle langue à la plateforme. Pour en savoir plus, rejoignez d'abord notre [groupe Telegram](https://t.me/PlanBNetwork_ContentBuilder), et écrivez une brève présentation de vous et des langues que vous pouvez parler.


Ce tutoriel est dédié aux contributeurs qui souhaitent relire du contenu. La plupart d'entre eux ne connaissent pas grand-chose à [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ou au [langage Markdown](https://www.markdownguide.org/basic-syntax/) que nous utilisons dans le dépôt, il est donc important de partager quelques idées sur les facteurs clés impliqués dans cette tâche.


Ci-dessous, j'ai rassemblé les problèmes les plus courants rencontrés par les correcteurs. N'hésitez pas à en suggérer d'autres, car cela peut aider d'autres personnes à s'améliorer.


Avant de plonger dans les détails, la première chose à faire est de lire ce tutoriel sur les actions pratiques à suivre sur Github, en forkant le dépôt Plan ₿ Network, en commettant des changements et en envoyant des PRs :


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## Qu'est-ce que la relecture ?


La relecture est le processus de révision finale d'un texte écrit, qui permet d'identifier et de corriger les erreurs de grammaire, d'orthographe, de ponctuation et de formatage. Elle permet de s'assurer que le texte est clair, cohérent et exempt d'erreurs avant sa publication ou sa soumission.


Lorsque vous effectuez ce type de tâche, il est important de respecter le sens de la langue d'origine (EN ou FR), mais de veiller à ce que le texte dans la langue finale soit aussi fluide que possible pour un locuteur natif.


N'oubliez jamais que la traduction/relecture est une ÉDUCATION !


En fait, notre objectif commun est d'éduquer le plus grand nombre de personnes possible sur le Bitcoin, et il est donc fondamental que les documents qu'elles lisent soient clairs et faciles à comprendre.

En ce sens, tous les contributeurs de Plan ₿ Network sont des éducateurs !


## Les premières étapes de la relecture sur Plan ₿ Network


Avant de commencer une nouvelle tâche de relecture, annoncez-la dans le [groupe Telegram] (https://t.me/PlanBNetwork_ContentBuilder) ou informez votre coordinateur Plan ₿ Network, qui ouvrira un [numéro] dédié (https://github.com/orgs/PlanB-Network/projects/3). Lorsque vous recevrez le lien du numéro, il vous suffira de **commenter que vous commencez** la tâche de relecture de ce contenu.


Ce système aide le coordinateur à suivre l'évolution de la situation dans le répertoire et permet au contenu d'être "revendiqué" par le relecteur, ce qui évite la duplication des efforts par quelqu'un d'autre.

Sur le problème lui-même, vous trouverez les liens qui vous redirigent vers le contenu à vérifier. Vous pouvez simplement cliquer dessus, ou, mieux encore, vous pouvez retourner à votre propre repo forké et travailler directement à partir de là. Voyons comment vous pouvez le faire !


Tout d'abord, **N'oubliez jamais de SYNCER votre repo, sur la branche "dev "**. De cette façon, le contenu sera toujours mis à jour avant que vous ne commenciez n'importe quel type de tâche, et vous ne créerez pas de conflits entre l'ancien et le nouveau matériel. Assurez-vous de cliquer sur "Sync Fork" et "Update branch".



![REVIEW](assets/en/1.webp)



Une fois la synchronisation réussie, vous pouvez accéder directement au contenu qui vous intéresse et effectuer un commit sur une nouvelle branche, comme le montre ce [tutoriel] (https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Sinon, vous pouvez ouvrir une nouvelle branche où travailler, en cliquant sur "Branches", comme indiqué ci-dessous.



![REVIEW](assets/en/2.webp)



Dans cette nouvelle page, vous trouverez toutes les branches que vous avez déjà ouvertes sous le titre "Vos branches". Cette section est très utile car elle vous permet de retrouver facilement l'endroit où vous avez modifié un contenu. Si vous souhaitez ouvrir une nouvelle branche, vous pouvez cliquer sur "Nouvelle branche" dans le coin supérieur droit de la page.



![REVIEW](assets/en/3.webp)



Vous obtiendrez ensuite une fenêtre contextuelle dans laquelle vous devrez insérer le nom de la nouvelle succursale. Dans le cas ci-dessous, j'ai choisi de l'appeler "BTC101-FR". De cette façon, je me souviendrai toujours que cette branche spécifique doit être utilisée pour la relecture du cours BTC101 en français, et **je ne l'utiliserai pour aucune autre tâche**.


Je vous suggère de faire de même : veillez à ouvrir une nouvelle branche chaque fois que vous devez commencer une nouvelle tâche.



![REVIEW](assets/en/4.webp)



Après avoir créé cette nouvelle branche, assurez-vous de cliquer dessus depuis "Vos branches" dans la page précédente et commencez à travailler sur le fichier *.md* lié au contenu spécifique (dans mon cas, je vais cliquer sur "courses" -> "BTC101" -> "fr.md"). Tous les commits liés au fichier spécifique devront être commis (sauvegardés) à l'intérieur de la même branche.



## Langue originale ou traduction ?


Lors de la relecture d'un contenu, il est important de **toujours vérifier la version originale en anglais (ou en français)**. Sachez que nous traduisons à l'aide d'outils linguistiques d'IA, et que le rendu dans la langue cible peut donc ne pas être fluide ou bien compréhensible pour le lecteur final.


N'hésitez donc pas à ajuster le texte et à modifier les phrases, si nécessaire. Notre objectif est d'améliorer la fluidité, mais toujours en respectant le sens original. En cas de doute sur la manière de traiter un mot spécifique, n'hésitez pas à demander au coordinateur de la traduction.


Les outils LLM peuvent traduire littéralement certains mots liés à Bitcoin, comme Lightning Network. C'est notamment le cas lorsqu'il s'agit de mots très techniques. Dans de tels cas, il est conseillé de conserver le mot anglais original dans votre langue cible pour plus de clarté, à moins que vos règles linguistiques ne vous imposent de traduire chaque mot.


Dans ce deuxième cas, **faites toujours des recherches pour voir si quelqu'un d'autre dans votre communauté Bitcoin a déjà traduit ce mot** et s'il est maintenant largement utilisé.



- Une solution pourrait être de **vérifier sur [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** dans votre langue cible pour voir si le mot a été traduit ou non. Si ce n'est pas le cas, vous gardez le mot en anglais.



- Dans tous les cas, mon conseil serait d'**insérer le mot EN néanmoins**, en ajoutant le sens correspondant dans la langue cible à l'intérieur de parenthèses rondes, en suivant le schéma EN (LANG), ou vice-versa. Ex. Address (indirizzo), ou indirizzo (Address).



- Une autre bonne solution consiste à conserver le mot/phrase original EN, puis **créer un lien hypertexte** qui redirige vers le [glossaire](https://planb.network/en/resources/glossary) sur planb.network. Pour ce faire, vous devez insérer le mot/phrase entre crochets, et le lien entre parenthèses rondes, comme vous pouvez le voir dans l'exemple ci-dessous :


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Dans le résultat final (image ci-dessous), vous ne visualiserez pas le lien entier, et le mot deviendra cliquable.



![REVIEW](assets/en/5.webp)



Veuillez noter que le lien vers le glossaire que vous obtiendrez sur le site web contient le code de langue après le mot "réseau" (exemple : `https://planb.network/en/resources/glossary/UTXO`-> ici vous pouvez lire le code de langue "en"). Dans ce cas, **supprimez le code de langue du lien**, comme vous l'avez vu dans l'encadré ci-dessus. De cette façon, le système amènera automatiquement le lecteur à la langue qu'il a choisie.


Le contenu du référentiel est truffé d'hyperliens comme ceux présentés ci-dessus. Maintenant que vous savez ce qu'ils signifient, **veillez à ne pas supprimer les liens** insérés par l'auteur original.



- Une autre chose liée à la restitution des mots est la suivante. Si vous trouvez "Plan ₿ Network" dans le texte, **laissez-le dans sa forme originale**. Ne traduisez pas le mot "plan" ou le mot "réseau". En outre, n'utilisez PAS l'article "The" lorsque vous présentez Plan ₿ Network : **considérez-le comme une marque**.



- Il en va de même pour "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", qui doivent également être conservés sous leur forme originale.


Une dernière remarque à propos de ce paragraphe : comme nous l'avons dit plus haut, nous utilisons des outils d'IA pour traduire le contenu, puis nous demandons l'intervention des contributeurs pour nous assurer que tout est fluide et bien relu.


Si vous utilisez l'IA pour relire la majorité du texte, nous ne manquerons pas de le remarquer, car nous sommes familiarisés avec les structures de phrases typiques générées par l'IA. Si nous constatons que vous vous êtes fié uniquement à l'IA pour la relecture, sans apporter de modifications significatives, la récompense finale en Sats peut être réduite de moitié !



## La structure des en-têtes


Dans le langage markdown, les en-têtes (et les titres de paragraphes) commencent tous par le signe Hash ``#``. Le nombre de signes Hash correspond au niveau de l'en-tête. Par exemple, un titre de niveau trois comporte trois signes numériques avant le texte (par exemple, `### Mon titre`).


Dans les cours, les parties les plus importantes sont introduites par un seul signe Hash, tandis que les sous-parties peuvent comporter de deux à quatre signes Hash. Dans les didacticiels, nous n'utilisons normalement que des en-têtes comportant deux signes Hash.



![REVIEW](assets/en/6.webp)



Veillez à ne JAMAIS supprimer les signes Hash** avant un titre, sinon vous créerez des problèmes avec la structure du texte.


En même temps, **ne changez pas** la partie chapterID que vous pouvez voir dans l'image ci-dessus, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ou les références vidéo comme ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Lorsque nous insérons ``#`` devant un titre, il deviendra automatiquement gras dans l'aperçu du cours, donc **évitez de mettre les titres en gras lors de la correction**.


Par ailleurs, dans la version EN des cours, les **titres introduits par un ou deux ``#`` ont tous les mots commençant par une majuscule**, alors que les titres commençant par trois ou quatre ``#`` ne suivent généralement pas cette règle. Dans la mesure du possible, veillez à ce que les titres dans votre langue cible suivent cette structure.



## La section initiale des cours


Au début de tout contenu, vous trouverez les mots minuscules statiques suivants : "nom", "description", "objectifs". Ils sont utilisés par le site web pour décoder le contenu lui-même et sont **toujours laissés en EN**. Par conséquent, ne les traduisez pas, sinon le contenu créera des problèmes de synchronisation. Veillez à ne relire que la partie située après les deux points, qui est automatiquement traduite par l'IA.



![REVIEW](assets/en/7.webp)



Dans cette même section initiale, conservez le format tel quel. N'ajoutez rien au début du texte. Par exemple, évitez d'ajouter "tt" avant les tirets, comme dans l'image ci-dessous !



![REVIEW](assets/en/8.webp)



## Recommandations sur le format


Vous trouverez ci-dessous quelques exemples de problèmes de format auxquels il convient de prêter attention lors de la relecture d'un contenu dans votre langue cible.



- Faites attention aux ponctuations bizarres comme ``*\*\'', ou ``**`` qui peuvent représenter un mauvais rendu du symbole gras. Dans l'image ci-dessous, vous pouvez voir que les astérisques ne se trouvent qu'à droite du mot, ce qui est bizarre.



![REVIEW](assets/en/9.webp)



Par conséquent, vérifiez toujours le texte original en anglais pour voir si un texte en gras est censé s'y trouver. Dans ce cas, il suffit d'ajouter deux astérisques au début du mot pour qu'il apparaisse correctement sur le site web. En fait, dans le langage markdown, **pour rendre le gras, vous devez insérer deux astérisques ``**`` à la fois avant et après le mot/la phrase** (voir l'exemple ci-dessous).



![REVIEW](assets/en/10.webp)




- Les mêmes problèmes peuvent se produire avec des symboles comme $ et `` ` ``.

Veillez à vérifier le fichier de la langue originale (souvent EN ou FR) pour voir où ces symboles sont censés se trouver. Vous pouvez toujours demander l'aide du coordinateur à ce sujet.



- Si vous trouvez des guillemets, assurez-vous de faire des recherches en ligne pour trouver la bonne traduction dans votre langue. Les guillemets sont généralement insérés après le symbole ``>``.



![REVIEW](assets/en/11.webp)



## Relecture du questionnaire


Saviez-vous que vous pouvez également relire les questions des quiz de chaque cours ? Par exemple, si vous souhaitez relire les quiz du cours BTC101 en informatique, vous pouvez ouvrir une branche dédiée et suivre le chemin suivant : "cours" -> "BTC101" -> "quiz". Vous y trouverez tous les dossiers dédiés à chaque question, ainsi que le fichier linguistique correspondant au format _yml_.


Une fois de plus, assurez-vous que vous vous trouvez dans une agence spécialement ouverte à cet effet et informez-en toujours le coordinateur.


Après avoir examiné la question, assurez-vous de changer le statut "examiné" de "faux" à "vrai", comme le montre l'image ci-dessous.



![REVIEW](assets/en/12.webp)


## Relecture du glossaire


Tout comme les quiz, vous pouvez également relire le glossaire. Le glossaire original a été rédigé en français, vous y trouverez donc des phrases comme : "En français, cette expression peut se traduire par..."


Dans ce cas, veuillez adapter cette phrase à votre langue cible ou à l'anglais.


## Autres bonnes pratiques



- Si vous avez besoin de rechercher des mots spécifiques dans le texte, vous pouvez cliquer sur ``CTRL+F`` et la section rechercher-remplacer apparaîtra. Cette partie est très utile lorsque vous avez besoin de sauter à une partie spécifique du texte, ou que vous avez besoin de remplacer des mots/phrases spécifiques par lots, sans faire défiler le contenu complet.



![REVIEW](assets/en/13.webp)



Lorsque vous utilisez la fonction "remplacer tout", il est important de vérifier les résultats pour s'assurer que les liens n'ont pas été modifiés. Par exemple, si vous souhaitez remplacer le mot "Bitcoin" par "Bitkoin" (ce qui peut être nécessaire dans certaines langues), la fonction "remplacer tout" permet de mettre à jour efficacement toutes les occurrences dans le texte. Cependant, il faut savoir que cet outil modifiera également tous les liens contenant ce mot, ce qui peut entraîner des problèmes de redirection.


Dans l'exemple ci-dessous, le correcteur a utilisé la fonction ci-dessus pour remplacer "Satoshi" par "Satoshi(Sats)", et a également modifié le lien vers un didacticiel contenant le mot lui-même. En conséquence, le lien est devenu invalide.


Vérifiez toujours tous les liens hypertextes dans le texte, afin de vous assurer qu'ils sont corrects.



![REVIEW](assets/en/14.webp)




- Si l'auteur insère un lien renvoyant à un cours ou à un tutoriel Plan ₿ Network (**non** entre parenthèses), le site web créera automatiquement une "carte" affichant la vignette correspondante. Par conséquent, assurez-vous toujours qu'il y a **un espace entre le texte et le lien lui-même**, sinon vous risquez de voir l'erreur suivante sur le site web.



![REVIEW](assets/en/15.webp)





- Enfin, une autre bonne pratique à appliquer lorsque vous avez terminé votre tâche de relecture et envoyé le PR est de retourner au problème original ouvert par le coordinateur et de commenter avec "Relecture effectuée". **N'oubliez pas d'y insérer également le lien de votre PR**.



## Conclusion


En résumé, le fait d'être conscient des erreurs courantes des correcteurs peut vraiment vous aider à améliorer vos compétences en matière de vérification du contenu. Il est facile de négliger des éléments tels que le contexte ou la cohérence, et la détection de ces erreurs peut faire une grande différence.


Gardez toujours à l'esprit qu'un débutant peut lire ces cours et tutoriels, et qu'il est donc de notre responsabilité de veiller à ce qu'il les comprenne parfaitement. En tant que correcteur, vous êtes un éducateur !


Merci d'avoir lu ce tutoriel et bonne lecture !