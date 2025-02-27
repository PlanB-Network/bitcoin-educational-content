---
name: Contribución - GitHub Web tutorial (principiante)
description: Guía completa para Planificar ₿ Tutoriales en red con GitHub Web
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, necesita haber completado algunos pasos preliminares. Si aún no lo ha hecho, eche un vistazo primero a este tutorial introductorio y luego vuelva aquí :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Ya tienes :


- Elija un tema para su tutorial;
- Póngase en contacto con el equipo de Plan ₿ Network a través de [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network ;
- Elige tus herramientas de contribución.

En este tutorial, veremos cómo añadir tu tutorial al Plan ₿ Network utilizando la versión web de GitHub. Si ya dominas Git, puede que este tutorial tan detallado no sea necesario para ti. En su lugar, te recomiendo que eches un vistazo a alguno de estos otros 2 tutoriales, donde detallo las pautas a seguir y los pasos para realizar cambios desde un archivo :


- Usuarios con experiencia** :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957
## Requisitos previos

Requisitos previos antes de empezar el tutorial :


- Tener una [cuenta GitHub](https://github.com/signup);
- Disponga de un fork del [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Tener [un perfil de profesor en Plan ₿ Network](https://planb.network/professors) (sólo si ofreces una tutoría completa).

Si necesitas ayuda para conseguir estos requisitos previos, mis otros tutoriales te ayudarán:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Una vez que todo esté en su lugar y tengas tu fork del repositorio Plan ₿ Network, puedes empezar a añadir el tutorial.

## 1 - Crear una nueva sucursal

Abre tu navegador y navega hasta la página de tu fork en el repositorio Plan ₿ Network. Esta es la bifurcación que has establecido en GitHub. La URL de su bifurcación debe tener este aspecto: `https://github.com/[tu-nombre-deusuario]/bitcoin-educational-content` :

![GITHUB](assets/fr/01.webp)

Asegúrate de que estás en la rama principal `dev` y haz clic en el botón "*Sync fork*". Si tu bifurcación no está actualizada, GitHub te pedirá que actualices tu rama. Procede con esta actualización:

![GITHUB](assets/fr/02.webp)

Haz clic en la rama `dev` y, a continuación, nombra tu rama de trabajo de forma que su título refleje claramente su objetivo, utilizando guiones para separar las palabras. Por ejemplo, si nuestro objetivo es escribir un tutorial sobre el uso de Green Wallet, la rama podría llamarse `tuto-cartera-verde-loic`. Tras introducir un nombre adecuado, haz clic en "*Crear rama*" para confirmar la creación de tu nueva rama basada en `dev` :

![GITHUB](assets/fr/03.webp)

Ahora deberías estar en tu nueva rama de trabajo:

![GITHUB](assets/fr/04.webp)

Esto significa que cualquier cambio que hagas se guardará sólo en esa rama específica.

Para cada nuevo artículo que vaya a publicar, cree una nueva rama a partir de `dev`.

Una rama en Git representa una versión paralela del proyecto, que te permite trabajar en modificaciones sin afectar a la rama principal, hasta que tu trabajo esté listo para ser integrado.

## 2 - Añadir archivos del tutorial

Ahora que se ha creado la rama de trabajo, es el momento de integrar su nuevo tutorial.

Dentro de sus archivos de rama, tendrá que encontrar la subcarpeta adecuada para la colocación de su tutorial. La organización de las carpetas refleja las diferentes secciones del sitio web de Plan ₿ Network. En nuestro ejemplo, ya que estamos añadiendo un tutorial sobre Green Wallet, dirígete a la siguiente ruta: `bitcoin-educational-content\tutorials\wallet` que corresponde a la sección `WALLET` del sitio web:

![GITHUB](assets/fr/05.webp)

En la carpeta `wallet`, cree un nuevo directorio dedicado específicamente a su tutorial. El nombre de esta carpeta debe indicar claramente el software cubierto en el tutorial, utilizando guiones para conectar las palabras. En mi ejemplo, la carpeta se llamará `green-wallet`. Haga clic en "*Añadir archivo*" y luego en "*Crear nuevo archivo*" :

![GITHUB](assets/fr/06.webp)

Introduzca el nombre de la carpeta seguido de una barra `/` para confirmar su creación como carpeta.

![GITHUB](assets/fr/07.webp)

En esta nueva subcarpeta dedicada a su tutorial, deberá añadir varios elementos:


- Crea una carpeta `assets` para guardar todas las ilustraciones necesarias para tu tutorial;
- Dentro de esta carpeta `assets`, cree una subcarpeta con el nombre del código del idioma original del tutorial. Por ejemplo, si el tutorial está escrito en inglés, esta subcarpeta debería llamarse `en`. Coloca todos los elementos visuales del tutorial (diagramas, imágenes, capturas de pantalla, etc.) en esta carpeta.
- Debe crear un archivo `tutorial.yml` para registrar los detalles de su tutorial;
- Debe crearse un archivo markdown para escribir el contenido real de su tutorial. Este archivo debe nombrarse de acuerdo con el código del idioma en el que está escrito. Por ejemplo, para un tutorial escrito en francés, el archivo debe llamarse `fr.md`.

Para resumir, esta es la jerarquía de archivos (seguiremos creándolos en la próxima sección):

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```

## 3 - Rellene el archivo YAML

Empecemos con el archivo YAML. En la casilla para crear un nuevo archivo, introduzca `tutorial.yml` :

![GITHUB](assets/fr/08.webp)

Rellene el archivo `tutorial.yml` copiando la siguiente plantilla:

```yaml
id:
project_id:
tags:
-
-
-
category:
level:
credits:
professor:
# Proofreading metadata
original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributors_id:
-
reward:
````
Voici le détail des champs obligatoires :
- **id** : Un UUID (_Universally Unique Identifier_) permettant d’identifier de manière unique le tutoriel. Vous pouvez le générer avec [un outil en ligne](https://www.uuidgenerator.net/version4). La seule contrainte est que cet UUID soit aléatoire pour ne pas avoir de conflit avec un autre UUID sur la plateforme ;
- **project_id** : L'UUID de l’entreprise ou de l’organisation derrière l’outil présenté dans le tutoriel [depuis la liste des projets](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Par exemple, si vous réalisez un tutoriel sur le logiciel Green Wallet, vous pouvez trouver ce `project_id` dans le fichier suivant : `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Cette information est ajoutée dans le fichier YAML de votre tutoriel parce que Plan ₿ Network maintient une base de données de toutes les entreprises et organisations opérant sur Bitcoin ou des projets connexes. En ajoutant le `project_id` de l'entité liée à votre tutoriel, vous créez un lien entre les deux éléments ;
- **tags** : 2 ou 3 mots-clés pertinents liés au contenu du tutoriel, choisis exclusivement [dans la liste des tags de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) ;
- **category** : La sous-catégorie correspondant au contenu du tutoriel, selon la structure du site Plan ₿ Network (par exemple pour les wallets : `desktop`, `hardware`, `mobile`, `backup`) ;
- **level** : Le niveau de difficulté du tutoriel, parmi :
- `beginner`
- `intermediate`
- `advanced`
- `expert`
- **professor** : Votre `contributor_id` (mots BIP39) tel qu'affiché sur [votre profil professeur](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) ;
- **original_language** : La langue d’origine du tutoriel (par exemple `fr`, `en`, etc.) ;
- **proofreading** : Informations sur le processus de relecture. Remplissez la première partie, car la relecture de votre propre tutoriel compte comme une première validation :
- **language** : Code de langue de la relecture (par exemple `fr`, `en`, etc.).
- **last_contribution_date** : Date du jour.
- **urgency** : Laissez vide.
- **contributors_id** : Votre ID GitHub.
- **reward** : Laissez vide.
Pour davantage de détails sur votre identifiant de professeur, reportez-vous au tutoriel correspondant :
https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Voici un exemple de fichier `tutorial.yml` complété pour un tutoriel sur le wallet Blockstream Green :
```

id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:


  - carteras
  - software
  - llaves

categoría: móvil

nivel: principiante

créditos:

profesor: pretty-private

# Corrección de metadatos

idioma_original: fr

corrección de pruebas:


  - idioma: fr

last_contribution_date: 2024-11-20

urgencia:

contribuyentes_id:


      - LoicPandul

recompensa:

```
Une fois la modification de votre fichier `tutorial.yml` achevée, enregistrez votre document en cliquant sur le bouton "*Commit changes...*" :
![GITHUB](assets/fr/09.webp)
Ajoutez un titre et une description, et assurez-vous que le commit soit réalisé sur la branche de travail que vous avez créée au début de ce tutoriel. Puis confirmez en cliquant sur "*Commit changes*".
![GITHUB](assets/fr/10.webp)
## 4 - Créer les sous-dossiers pour les images
Cliquez de nouveau sur "*Add File*" puis sur "*Create new file*" :
![GITHUB](assets/fr/11.webp)
Entrez `assets` suivi d'un slash `/` pour créer le dossier :
![GITHUB](assets/fr/12.webp)
Répétez cette étape dans le dossier `/assets` pour créer le sous-dossier de langue, par exemple `fr` si votre tutoriel est en français :
![GITHUB](assets/fr/13.webp)
Dans ce dossier, créez un fichier factice pour obliger GitHub à conserver votre dossier (qui sinon serait vide). Nommez ce fichier `.gitkeep`. Ensuite, cliquez sur "*Commit changes...*".
![GITHUB](assets/fr/14.webp)
Assurez-vous à nouveau que vous êtes sur la branche de travail correcte, puis cliquez sur "*Commit changes*".
![GITHUB](assets/fr/15.webp)
## 5 - Créer le fichier Markdown
Maintenant, nous allons créer le fichier qui accueillera votre tutoriel, nommé selon le code de votre langue, comme par exemple `fr.md` si l'on rédige en français. Accédez au dossier de votre tutoriel :
![GITHUB](assets/fr/16.webp)
Cliquez sur "*Add file*", puis sur "*Create new file*".
![GITHUB](assets/fr/17.webp)
Nommez le fichier en utilisant le code de votre langue. Dans mon cas, le tutoriel étant rédigé en français, je nomme mon fichier `fr.md`. L'extension `.md` indique que le fichier est au format Markdown.
![GITHUB](assets/fr/18.webp)
Nous commençons par remplir la section `Properties` en haut du document. Ajoutez manuellement et remplissez le bloc de code suivant (les clés `name:` et `description:` doivent être conservées en anglais, mais leur valeur doit être rédigée dans la langue utilisée pour votre tutoriel) :
```

---
name: [Título]
description: [Descripción]
---
```
![GITHUB](assets/fr/19.webp)
Remplissez le nom de votre tutoriel ainsi qu'une courte description de celui-ci :
![GITHUB](assets/fr/20.webp)
Ajoutez ensuite le chemin de l'image de couverture au début de votre tutoriel. Pour ce faire, notez :
```

![cover-green](assets/cover.webp)

```
Cette syntaxe vous sera utile chaque fois que l'ajout d'une image dans votre tutoriel sera nécessaire. Le point d'exclamation signale qu'il s'agit d'une image, dont le texte alternatif (alt) est spécifié entre les crochets. Le chemin d'accès à l'image est indiqué entre les parenthèses :
![GITHUB](assets/fr/21.webp)
Cliquez sur le bouton "*Commit changes...*" pour enregistrer ce fichier.
![GITHUB](assets/fr/22.webp)
Vérifiez que vous êtes sur la bonne branche, puis confirmez le commit.
![GITHUB](assets/fr/23.webp)
Votre dossier de tutoriel devrait maintenant se présenter de cette manière, selon le code de votre langue :
![GITHUB](assets/fr/24.webp)
## 6 - Ajouter le logo et la couverture
Au sein du dossier `assets`, vous devez ajouter un fichier nommé `logo.webp`, qui servira de vignette pour votre article. Cette image doit obligatoirement être au format `.webp` et doit respecter une dimension carrée afin de s'harmoniser avec l'interface utilisateur.
Vous avez la liberté de choisir le logo du logiciel traité dans le tutoriel ou toute autre image pertinente, à condition que celle-ci soit libre de droits. En complément, ajoutez également au même endroit une image intitulée `cover.webp`. Celle-ci sera affichée en haut de votre tutoriel. Veillez à ce que cette image, tout comme le logo, respecte les droits d'utilisation et soit adaptée au contexte de votre tutoriel.
Pour ajouter des images dans le dossier `/assets`, vous pouvez les glisser-déposer depuis vos fichiers locaux. Assurez-vous que vous êtes bien dans le dossier `/assets` et sur la bonne branche de travail, puis cliquez sur "*Commit changes*".
![GITHUB](assets/fr/26.webp)
Vous devriez maintenant voir les images apparaître dans le dossier.
![GITHUB](assets/fr/27.webp)
## 7 - Rédiger le tutoriel
Poursuivez la rédaction de votre tutoriel en notant votre contenu dans le fichier Markdown avec le code de langue (dans mon exemple, en français, c'est le fichier `fr.md`). Accédez au fichier et cliquez sur l'icône du crayon :
![GITHUB](assets/fr/28.webp)
Commencez la rédaction de votre tutoriel. Lorsque vous ajoutez un sous-titre, utilisez le formatage Markdown approprié en préfixant le texte avec `##` :
![GITHUB](assets/fr/29.webp)
Alternez entre la vue "*Edit*" et la vue "*Preview*" pour mieux visualiser le rendu.
![GITHUB](assets/fr/30.webp)
Pour enregistrer votre travail, cliquez sur "*Commit Changes...*", assurez-vous d'être sur la bonne branche de travail, puis confirmez en cliquant de nouveau sur "*Commit Changes*".
![GITHUB](assets/fr/31.webp)
## 8 - Ajouter des visuels
Le sous-dossier de langues dans le dossier `/assets` (dans mon exemple : `/assets/fr`) permet de stocker les schémas et les visuels qui accompagneront votre tutoriel. Autant que possible, évitez d'inclure du texte dans vos images pour rendre votre contenu accessible à un public international. Bien sûr, le logiciel présenté contiendra du texte, mais si vous ajoutez des schémas ou des indications supplémentaires sur les captures d'écran du logiciel, faites-le sans texte ou, si cela s'avère indispensable, utilisez l'anglais.
Pour nommer vos images, utilisez simplement des numéros correspondant à leur ordre d'apparition dans le tutoriel, formatés sur deux chiffres (ou trois chiffres si votre tutoriel contient plus de 99 images). Par exemple, nommez votre première image `01.webp`, votre deuxième `02.webp`, et ainsi de suite.
Le format de vos images doit être en `.webp` exclusivement. Si besoin, vous pouvez utiliser [mon logiciel de conversion d'images](https://github.com/LoicPandul/ImagesConverter).
![GITHUB](assets/fr/32.webp)
Maintenant que vous avez ajouté vos images dans le sous-dossier, vous pouvez supprimer le fichier factice `.gitkeep`. Ouvrez ce fichier, cliquez sur les trois petits points en haut à droite, puis sur "*Delete file*".
![GITHUB](assets/fr/33.webp)
Enregistrez vos modifications en cliquant sur "*Commit changes...*".
![GITHUB](assets/fr/34.webp)
Pour insérer un schéma présent dans votre sous-dossier dans votre document de rédaction, utilisez la commande Markdown suivante, en prenant soin de spécifier le texte alternatif approprié ainsi que le chemin correct de l'image en fonction de votre langue :
```

![green](assets/fr/01.webp)

```