---
name: Contribución - Tutorial de Git (avanzado)
description: Guía para usuarios avanzados para ofrecer un tutorial sobre Plan ₿ Red con Git
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, necesita haber completado algunos pasos preliminares. Si aún no lo ha hecho, eche un vistazo primero a este tutorial introductorio y luego vuelva aquí :

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Ya tienes :


- Elija un tema para su tutorial;
- Póngase en contacto con el equipo de Plan ₿ Network a través de [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network ;
- Elige tus herramientas de contribución.

En este tutorial para usuarios experimentados de Git, resumiremos brevemente los pasos clave y las pautas esenciales para ofrecer un nuevo Plan ₿ Tutorial en red. Si no estás familiarizado con Git y GitHub, te recomiendo que en su lugar sigas uno de estos otros 2 tutoriales más detallados que te llevarán paso a paso..:


- Intermedio (GitHub Desktop)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- Principiantes (interfaz web)** :

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

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

```
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

```
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

```
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

```
id: 

project_id: 

tags:
  - 
  - 
  - 

category: 

level: 

professor_id:

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributor_names:
      - 
    reward:
```

Aquí están los campos obligatorios:

- **id** : Un UUID (_Identificador Universalmente Único_) que permite identificar de manera única el tutorial. Puede generarlo con [una herramienta en línea](https://www.uuidgenerator.net/version4). El único requisito es que este UUID sea aleatorio para evitar conflictos con otro UUID en la plataforma;

- **project_id** : El UUID de la empresa u organización detrás de la herramienta presentada en el tutorial [desde la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, si está creando un tutorial sobre el software Green Wallet, puede encontrar el `project_id` en el siguiente archivo: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Esta información se agrega al archivo YAML de su tutorial porque Plan ₿ Network mantiene una base de datos de todas las empresas y organizaciones que operan en Bitcoin o proyectos relacionados. Al agregar el `project_id` de la entidad relacionada con su tutorial, crea un vínculo entre ambos elementos;

- **tags** : 2 o 3 palabras clave relevantes relacionadas con el contenido del tutorial, elegidas exclusivamente [de la lista de etiquetas de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category** : La subcategoría correspondiente al contenido del tutorial, según la estructura del sitio web de Plan ₿ Network (por ejemplo, para monederos: `desktop`, `hardware`, `mobile`, `backup`);

- **level** : El nivel de dificultad del tutorial, elegido entre:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id** : Su `professor_id` (UUID) tal como aparece en [su perfil de profesor](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language** : El idioma original del tutorial (por ejemplo, `fr`, `en`, etc.);

- **proofreading** : Información sobre el proceso de revisión. Complete la primera parte, ya que la revisión de su propio tutorial cuenta como una primera validación:
    - **language** : Código de idioma de la revisión (por ejemplo, `fr`, `en`, etc.).
    - **last_contribution_date** : Fecha del día.
    - **urgency** : 1
    - **contributor_names** : Su ID de GitHub.
    - **reward** : 0

Para más detalles sobre su ID de profesor, consulte el tutorial correspondiente :

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency: 1
    contributor_names:
      - LoicPandul
    reward: 0
```

### 5 - Redactar el contenido


- Complete las propiedades del archivo Markdown con :
    - El título (`nombre`).
    - Una breve descripción (`description`).
- Añade la imagen de portada en la parte superior del tutorial utilizando la sintaxis Markdown (sustituye "verde" por el nombre de la herramienta mostrada):

```
![cover-green](assets/cover.webp)
```


- Escriba el contenido del tutorial en Markdown :
    - Utilice títulos bien estructurados (`##`), listas y párrafos.
    - Insertar elementos visuales utilizando la sintaxis Markdown :

```
![nom-image](assets/en/001.webp)
```


- Coloque los diagramas y las imágenes en la subcarpeta del idioma correspondiente, en `/assets`.

### 6 - Guardar y enviar el tutorial


- Guarde sus cambios localmente creando un commit con un mensaje descriptivo.
- Empuje los cambios a su bifurcación de GitHub.

```
# Créez un commit avec un message descriptif
git commit -m "Ajout du tutoriel green-wallet"
# Poussez vos modifications sur votre fork
git push origin tuto-green-wallet-loic
```


- Una vez terminado, crea una Pull Request (PR) en GitHub para proponer la integración de tus modificaciones.
- Añada un título y una breve descripción al RP. Mencione el número de incidencia correspondiente en el comentario.

### 7 - Corrección y fusión


- Espere la validación o la respuesta de un administrador.
- Si es necesario, haga correcciones y envíe nuevos commits.

```
# Créez un commit décrivant les corrections apportées
git commit -m "Corrections suite à la revue du tutoriel green-wallet"
# Poussez les corrections sur votre fork
git push origin tuto-green-wallet-loic
```


- Una vez fusionado el PR, puede eliminar su rama de trabajo.

## Normas de creación de contenidos


- Formatos compatibles con la plataforma** :
    - Markdown clásico: listas, enlaces, imágenes, citas, negrita, cursiva, etc.
    - LaTeX (sólo bloque, no en línea): delimitado por `$$`.
    - Código en línea: Sintaxis con una sola marca.
    - Bloques de código: Sintaxis con tres barras invertidas, por ejemplo :

```
print("Hello, Bitcoin!")
```


- Ilustraciones y diagramas** :
    - Todas las imágenes deben estar en formato WebP. Utilice esta herramienta gratuita para convertirlas si es necesario: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Nombra los visuales con 2 o 3 dígitos (por ejemplo, `001.webp`, `002.webp`).
    - Para los tutoriales sobre carteras móviles o de hardware, utiliza maquetas.
    - Utilice únicamente imágenes de creación propia o libres de derechos.
    - Asegúrese de que sean pertinentes y de calidad.
- Carta gráfica** :
    - Fuente: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Plan Colores ₿ Red :
        - Naranja: `#FF5C00`
        - Negro: `#000000`
        - Blanco: `#FFFFFF`

Si tienes dificultades técnicas para enviar tu tutorial, no dudes en pedir ayuda en [nuestro grupo de Telegram dedicado a las contribuciones](https://t.me/PlanBNetwork_ContentBuilder). Muchas gracias