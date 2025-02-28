---
name: Contribución - Tutorial de Git (avanzado)
description: Guía para usuarios avanzados para ofrecer un tutorial sobre Plan ₿ Red con Git
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, necesita haber completado algunos pasos preliminares. Si aún no lo ha hecho, eche un vistazo primero a este tutorial introductorio y luego vuelva aquí :

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Ya tienes :


- Elija un tema para su tutorial;
- Póngase en contacto con el equipo de Plan ₿ Network a través de [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network ;
- Elige tus herramientas de contribución.

En este tutorial para usuarios experimentados de Git, resumiremos brevemente los pasos clave y las pautas esenciales para ofrecer un nuevo Plan ₿ Tutorial en red. Si no estás familiarizado con Git y GitHub, te recomiendo que sigas uno de estos otros 2 tutoriales más detallados que te llevarán paso a paso..:


- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Principiantes (interfaz web)** :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Herramientas recomendadas

Para editar archivos Markdown :


- Obsidian** (gratuito, no de código abierto)
- Mark Text** (gratuito, de código abierto)
- Zettlr** (gratuito, de código abierto)
- Typora** (software de pago, ~15 euros, no es de código abierto)

Para Git :


- Git** (gratuito, de código abierto)
- GitHub Desktop** (gratuito, de código abierto)
- Sourcetree** (gratuito, no de código abierto)

Para editar archivos YAML :


- Visual Studio Code** (gratuito, de código abierto)
- Sublime Text** (gratuito con limitaciones, no es de código abierto)

Para crear diagramas y elementos visuales :


- Canva** (gratuito con opciones de pago, no es de código abierto)
- Inkscape** (gratuito, código abierto)
- Penpot** (gratuito, de código abierto)

## Flujos de trabajo

### 1 - Configure su entorno local


- Debes tener tu propio fork del repositorio [Plan ₿ Network en GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sincronice la rama principal (`dev`) de su bifurcación con el repositorio fuente.
- Actualiza tu clon local.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<votre-nom-utilisateur>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Crear una nueva sucursal


- Asegúrate de que estás en la rama `dev`.
- Cree una nueva rama con un nombre descriptivo (p. ej., `tuto-verdes-wallet-loic`).
- Publique esta rama en su bifurcación en línea.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b tuto-green-wallet-loic
# Publiez cette branche sur votre fork en ligne
git push -u origin tuto-green-wallet-loic
```

### 3 - Añadir los documentos del tutorial

***Nota:*** Puedes automatizar los pasos 3 y 4 usando [mi script Python GUI](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Ejecútalo directamente desde su carpeta en tu clon local, luego rellena los campos requeridos en la GUI. Para más información sobre cómo instalarlo y utilizarlo, consulte el [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

Si prefieres hacerlo manualmente, sigue estos pasos:


- Localice la carpeta apropiada en el repositorio local (por ejemplo, `tutorials/wallet`).
- Cree un directorio dedicado al tutorial con un nombre claro (por ejemplo, `green-wallet`). Este nombre de carpeta también determinará la ruta URL del tutorial. Debe estar en minúsculas, sin caracteres especiales (excepto guiones) y sin espacios.
- Añade los siguientes elementos a este directorio:
    - Una subcarpeta llamada `assets` que contiene archivos :
        - Dos imágenes `.webp`:
            - `logo.webp`: El logotipo del tutorial (formato cuadrado con fondo). Este logotipo debe representar el software o la herramienta presentada. Si el tutorial no es específico de una herramienta (por ejemplo: una guía general para generar una frase mnemotécnica), puede elegir un elemento visual adecuado (por ejemplo: un icono genérico).
            - `cover.webp`: Una imagen de portada que se muestra al principio del tutorial.
        - Una subcarpeta con el código del idioma original del tutorial. Por ejemplo, si el tutorial está escrito en inglés, esta subcarpeta debe llamarse `en'. Coloca todos los elementos visuales del tutorial (diagramas, imágenes, capturas de pantalla, etc.) en esta carpeta.
    - Un archivo `tutorial.yml` que contiene metadatos (autor, etiquetas, categoría, nivel de dificultad, etc.).
    - Un archivo Markdown que contiene el tutorial, nombrado según el código del idioma (por ejemplo, `fr.md`, `en.md`, etc.).

```bash
# Positionnez-vous dans le dossier approprié
cd tutorials/wallet
# Créez le répertoire dédié au tutoriel
mkdir green-wallet
cd green-wallet
# Créez le sous-dossier 'assets'
mkdir -p assets
# Créez le sous-dossier pour le code de la langue d’origine (exemple : 'en' pour l’anglais)
mkdir -p assets/en
# Créez les fichiers de métadonnées et le tutoriel Markdown (exemple : 'en.md' pour l’anglais)
touch tutorial.yml en.md
```

### 4 - Rellene el archivo YAML


- Complete el archivo `tutorial.yml` de la siguiente manera:

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
### 5 - Rédigez le contenu
- Complétez les propriétés du fichier Markdown avec :
- Le titre (`name`).
- Une courte description (`description`).
- Ajoutez l’image de couverture en haut du tutoriel avec la syntaxe Markdown (remplacez "green" par le nom de l’outil présenté) :
```

![cover-green](assets/cover.webp)

```
- Rédigez le contenu du tutoriel en Markdown :
- Utilisez des titres bien structurés (`##`), des listes et des paragraphes.
- Insérez des visuels avec la syntaxe Markdown :
```

![nom-image](assets/en/001.webp)

```
- Placez les schémas et images dans le sous-dossier de langue correspondant, dans `/assets`.
### 6 - Enregistrez et soumettez le tutoriel
- Enregistrez vos modifications localement en créant un commit avec un message descriptif.
- Poussez les changements sur votre fork GitHub.
```

# Crear una confirmación con un mensaje descriptivo

git commit -m "Añadir tutorial sobre monedero verde"

# Empuje sus modificaciones en su tenedor

git push origin tuto-verde-wallet-loic

```
- Une fois terminé, créez une Pull Request (PR) sur GitHub pour proposer l’intégration de vos modifications.
- Ajoutez un titre et une brève description à la PR. Mentionnez le numéro d’issue correspondant dans le commentaire.
### 7 - Relecture et fusion
- Attendez la validation ou les retours d’un administrateur.
- Si nécessaire, effectuez des corrections et poussez de nouveaux commits.
```

# Crear un commit describiendo las correcciones realizadas

git commit -m "Correcciones tras la revisión del tutorial de green-wallet"

# Correcciones de empuje en la horquilla

git push origin tuto-verde-wallet-loic

```
- Une fois la PR fusionnée, vous pouvez supprimer votre branche de travail.
## Normes de création de contenu
- **Formatage supporté sur la plateforme** :
- Markdown classique : listes, liens, images, citations, gras, italique, etc.
- LaTeX (en bloc uniquement, pas inline) : délimité par `$$`.
- Code inline : Syntaxe avec un seul backtick.
- Blocs de code : Syntaxe avec trois backtick, par exemple :
```

print("¡Hola, Bitcoin!")

```