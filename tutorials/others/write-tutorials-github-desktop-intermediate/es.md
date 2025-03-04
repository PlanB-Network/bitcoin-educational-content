---
name: Contribución - Tutorial con GitHub Desktop (Intermedio)
description: Guía completa para proponer un tutorial sobre Plan ₿ Red usando GitHub Desktop
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, debes haber completado algunos pasos preliminares. Si aún no lo has hecho, te invito a que primero consultes este tutorial introductorio y luego vuelvas aquí:

https://planb.network/tutorials/others/contribution/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Ya lo has hecho:


- Ha elegido el tema de su tutorial;
- Contacta con el equipo de Plan ₿ Network a través de [el grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Elige tus herramientas de contribución.

En este tutorial, veremos cómo añadir tu tutorial en Plan ₿ Network configurando tu entorno local con GitHub Desktop. Si ya dominas Git, puede que este tutorial tan detallado no sea necesario para ti. Más bien te recomendaría consultar este otro tutorial donde sólo presento las pautas principales, sin una guía detallada paso a paso:


- Usuarios con experiencia**:

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Si prefieres no configurar tu entorno local, sigue este otro tutorial diseñado para principiantes, donde realizamos los cambios directamente a través de la interfaz web de GitHub:


- Principiantes (interfaz web)**:

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Requisitos previos

Software necesario para seguir este tutorial:


- [GitHub Desktop](https://desktop.github.com/);
- Un editor de archivos markdown como [Obsidian](https://obsidian.md/);
- Un editor de código ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Requisitos previos antes de empezar el tutorial:


- Tener una [cuenta GitHub](https://github.com/signup);
- Disponga de un fork del [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Tener [un perfil de profesor en Plan ₿ Network](https://planb.network/professors) (sólo si propone una tutoría completa).

Si necesitas ayuda para obtener estos requisitos previos, mis otros tutoriales te ayudarán:

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb
Una vez que todo está en su lugar y su entorno local está configurado correctamente con su propio tenedor del Plan ₿ Red, puede empezar a añadir el tutorial.

## 1 - Crear una nueva sucursal

Abre tu navegador y dirígete a la página de tu fork del repositorio Plan ₿ Network. Esta es la bifurcación que has establecido en GitHub. La URL de tu bifurcación debería parecerse a: `https://github.com/[tu-nombre-deusuario]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Asegúrate de que estás en la rama principal `dev` y haz clic en el botón `Sync fork`. Si tu rama no está actualizada, GitHub te ofrecerá actualizarla. Procede con esta actualización. Si, por el contrario, tu rama ya está actualizada, GitHub te informará:

![TUTO](assets/fr/04.webp)

Abra el software GitHub Desktop y asegúrese de que su bifurcación está correctamente seleccionada en la esquina superior izquierda de la ventana:

![TUTO](assets/fr/05.webp)

Haz clic en el botón `Fetch origin`. Si tu repositorio local ya está actualizado, GitHub Desktop no te sugerirá ninguna acción adicional. En caso contrario, aparecerá la opción `Obtener origen`. Haz clic en este botón para actualizar tu repositorio local:

![TUTO](assets/fr/06.webp)

Compruebe que se encuentra en la rama principal `dev`:

![TUTO](assets/fr/07.webp)

Haga clic en esta rama y, a continuación, en el botón `Nueva rama`:

![TUTO](assets/fr/08.webp)

Asegúrese de que la nueva rama se basa en el repositorio fuente, a saber, `PlanB-Network/bitcoin-educational-content`.

Nombra tu rama de forma que el título deje claro su objetivo, utilizando guiones para separar cada palabra. Por ejemplo, digamos que nuestro objetivo es escribir un tutorial sobre el uso del software Sparrow Wallet. En este caso, la rama de trabajo dedicada a escribir este tutorial podría llamarse: `tuto-sparrow-wallet-loic`. Una vez introducido el nombre apropiado, haga clic en `Crear rama` para confirmar la creación de la rama:

![TUTO](assets/fr/09.webp)

Ahora haz clic en el botón `Publish branch` para guardar tu nueva rama de trabajo en tu fork online en GitHub:

![TUTORIAL](assets/fr/10.webp)

Ahora, en GitHub Desktop, deberías encontrarte en tu nueva rama. Esto significa que todos los cambios realizados localmente en tu ordenador se guardarán exclusivamente en esta rama específica. Además, mientras esta rama permanezca seleccionada en GitHub Desktop, los archivos visibles localmente en tu máquina corresponderán a los de esta rama (`tuto-sparrow-wallet-loic`), y no a los de la rama principal (`dev`).

![TUTORIAL](assets/fr/11.webp)

Para cada nuevo artículo que desee publicar, deberá crear una nueva rama a partir de `dev`. Una rama en Git es una versión paralela del proyecto, que te permite hacer cambios sin afectar a la rama principal, hasta que el trabajo esté listo para ser fusionado.

## 2 - Añadir los archivos del tutorial

Ahora que la rama de trabajo está creada, es hora de integrar tu nuevo tutorial. Tienes dos opciones: utilizar mi script de Python, que automatiza la creación de los documentos necesarios, o crear manualmente cada archivo. Vamos a ver los pasos a seguir para cada opción.

### Con mi script Python

Debe instalar en su máquina:
- Python 3.8 o superior.

Para usar el script, diríjase a la carpeta donde está almacenado. El script se encuentra en el repositorio de datos de Plan ₿ Network en la ruta: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Una vez dentro de la carpeta, instale las dependencias:

```bash
pip install -r requirements.txt
```

Luego, inicie el software con el siguiente comando:

```bash
python3 main.py
```

Se abrirá una interfaz gráfica de usuario (GUI). La primera vez, deberá ingresar toda la información necesaria, pero en usos posteriores, el script recordará su información personal, por lo que no tendrá que ingresarla nuevamente.

![DATA-CREATOR-PY](assets/fr/37.webp)

Comience ingresando la ruta local a la carpeta `/tutorials` en su clon del repositorio (`.../bitcoin-educational-content/tutorials/`). Puede ingresarla manualmente o hacer clic en el botón "Browse" para navegar a través del explorador de archivos.

![DATA-CREATOR-PY](assets/fr/38.webp)

Seleccione el idioma en el que redactará su tutorial.

![DATA-CREATOR-PY](assets/fr/39.webp)

En el campo "Contributor's GitHub ID", ingrese su identificador de GitHub.

![DATA-CREATOR-PY](assets/fr/40.webp)

En el campo "PBN professor's ID", ingrese su identificador utilizando las palabras de la lista BIP39, tal como aparece en [su perfil de profesor](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).

![DATA-CREATOR-PY](assets/fr/41.webp)

Si aún no tiene un perfil de profesor, consulte este tutorial:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Luego, haga clic en el botón "New Tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Elija una categoría principal para su tutorial. Luego, seleccione una subcategoría adecuada en función de la categoría principal elegida.

![DATA-CREATOR-PY](assets/fr/43.webp)

Determine el nivel de dificultad del tutorial.

![DATA-CREATOR-PY](assets/fr/44.webp)

Elija un nombre para el directorio creado específicamente para su tutorial. El nombre de esta carpeta debe reflejar el software abordado en el tutorial y utilizar guiones para separar las palabras. Por ejemplo, la carpeta podría llamarse `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

El `project_id` es el UUID de la empresa u organización detrás de la herramienta presentada en el tutorial, disponible en [la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, para un tutorial sobre Sparrow Wallet, encontrará el `project_id` en el archivo: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Esta información se agrega al archivo YAML de su tutorial porque Plan ₿ Network mantiene una base de datos de empresas y organizaciones activas en Bitcoin o proyectos relacionados. Al agregar el `project_id` asociado a su tutorial, está creando un vínculo entre su contenido y la entidad correspondiente.

***Actualización:*** En la nueva versión del script, ya no es necesario ingresar manualmente el `project_id`. Se ha agregado una función de búsqueda para encontrar el proyecto por su nombre y recuperar automáticamente el `project_id` correspondiente. Escriba el comienzo del nombre del proyecto en el campo "Project Name" para buscarlo y luego seleccione la empresa deseada en el menú desplegable. El `project_id` se completará automáticamente en el campo debajo. También puede ingresarlo manualmente si es necesario.

![DATA-CREATOR-PY](assets/fr/46.webp)

Para las etiquetas, seleccione 2 o 3 palabras clave relevantes en relación con el contenido de su tutorial, eligiéndolas exclusivamente de [la lista de etiquetas de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). También tiene una función de búsqueda de palabras con una lista desplegable en el software.

![DATA-CREATOR-PY](assets/fr/47.webp)

Una vez que haya ingresado y verificado toda la información, haga clic en "Create Tutorial" para confirmar la creación de los archivos de su tutorial. Esto generará localmente la carpeta de su tutorial y todos los archivos necesarios dentro de la categoría seleccionada.

![DATA-CREATOR-PY](assets/fr/48.webp)

Ahora puede omitir la subsección "Sin mi script de Python", así como el paso 3 "Rellenar el archivo YAML", ya que el script ya ha realizado estas acciones automáticamente por usted. Pase directamente al paso 4 y comience a redactar su tutorial.

Para obtener más información sobre este script de Python, también puede consultar el [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Sin mi script de Python

Abra su gestor de archivos y navegue hasta la carpeta `bitcoin-educational-content`, que representa el clon local de su repositorio. Normalmente, debería encontrarla en `Documents\GitHub\bitcoin-educational-content`.

Dentro de este directorio, deberá localizar la subcarpeta adecuada para colocar su tutorial. La organización de las carpetas refleja las diferentes secciones del sitio web de Plan ₿ Network. En nuestro ejemplo, dado que queremos agregar un tutorial sobre Sparrow Wallet, debemos ir a la siguiente ruta: `bitcoin-educational-content\tutorials\wallet`, que corresponde a la sección `WALLET` en el sitio web:

![TUTO](assets/fr/12.webp)

Dentro de la carpeta `wallet`, necesitas crear un nuevo directorio específicamente dedicado a tu tutorial. El nombre de esta carpeta debe evocar el software cubierto en el tutorial, asegurándose de conectar las palabras con guiones. En mi ejemplo, la carpeta se llamará `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

En esta nueva subcarpeta dedicada a su tutorial, hay que añadir varios elementos:


- Cree una carpeta `assets`, destinada a recibir todas las ilustraciones necesarias para su tutorial;
- Dentro de esta carpeta `assets`, debe crear una subcarpeta con el nombre del código del idioma original del tutorial. Por ejemplo, si el tutorial está escrito en inglés, esta subcarpeta debe llamarse `en`. Coloque allí todos los elementos visuales del tutorial (diagramas, imágenes, capturas de pantalla, etc.).
- Debe crearse un archivo `tutorial.yml` para registrar los detalles relacionados con su tutorial;
- Se debe crear un archivo en formato markdown para escribir el contenido real de su tutorial. Este archivo debe titularse según el código del idioma en el que se escriba. Por ejemplo, para un tutorial escrito en francés, el archivo debe llamarse `fr.md`.

![TUTO](assets/fr/14.webp)

En resumen, ésta es la jerarquía de archivos que hay que crear:

```plaintext
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Rellene el archivo YAML

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

A continuación se detallan los campos obligatorios:


- **id**: Un UUID (_Universally Unique Identifier_) para identificar de forma única el tutorial. Puede generarlo con [una herramienta en línea](https://www.uuidgenerator.net/version4). El único requisito es que este UUID sea aleatorio para evitar conflictos con otro UUID de la plataforma;
- **project_id**: El UUID de la empresa u organización detrás de la herramienta presentada en el tutorial [de la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, si está creando un tutorial sobre el software Sparrow Wallet, puede encontrar este `project_id` en el siguiente archivo: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Esta información se añade al archivo YAML de su tutorial porque Plan ₿ Network mantiene una base de datos de todas las empresas y organizaciones que operan en Bitcoin o proyectos relacionados. Al añadir el `project_id` de la entidad relacionada con su tutorial, se crea un vínculo entre los dos elementos;
- **tags**: 2 o 3 palabras clave relevantes relacionadas con el contenido del tutorial, elegidas exclusivamente [de la lista de etiquetas del Plan ₿ Red](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);
- **category**: La subcategoría correspondiente al contenido del tutorial, según la estructura del sitio Plan ₿ Network (por ejemplo para carteras: `desktop`, `hardware`, `mobile`, `backup`);
- **level**: El nivel de dificultad del tutorial, entre:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`
- **professor**: Su `contributor_id` (palabras BIP39) tal y como aparece en [su perfil de profesor](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);
- **idioma_original**: El idioma original del tutorial (por ejemplo `fr`, `en`, etc.);
- **proofreading**: Información sobre el proceso de corrección. Rellene la primera parte, ya que la corrección de su propio tutorial cuenta como primera validación:
    - **original_language**: Código de idioma de la corrección (por ejemplo `fr`, `en`, etc.).
    - **last_contribution_date**: La fecha de hoy.
    - **urgency**: Dejar en blanco.
    - **contributors_id**: Tu ID de GitHub.
    - **reward**: Dejar en blanco.

Para más detalles sobre su identificador de profesor, consulte el tutorial correspondiente:

https://planb.network/tutorials/others/contribution/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
Este es un ejemplo de un archivo `tutorial.yml` completo para un tutorial sobre el monedero Blockstream Green:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143
project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8
tags:
- wallets
- software
- keys
category: mobile
level: beginner
credits:
professor: pretty-private
# Proofreading metadata
original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency:
contributors_id:
- LoicPandul
reward:
Once you have finished modifying your `tutorial.yml` file, save your document by clicking on `File > Save`:
![TUTO](assets/fr/16.webp)
You can now close your code editor.
## 4 - Fill in the Markdown File
Now, you can open your file that will host your tutorial, named with the code of your language, such as `fr.md`. Go to Obsidian, on the left side of the window, scroll through the folder tree until you find the folder of your tutorial and the file you are looking for:
![TUTO](assets/fr/18.webp)
Click on the file to open it:
![TUTO](assets/fr/19.webp)
We will start by filling in the `Properties` section at the top of the document.
![TUTO](assets/fr/20.webp)
Manually add and fill in the following code block:
```

---
name: [Título]
description: [Descripción]
---
```
![TUTO](assets/fr/21.webp)
Fill in the name of your tutorial and a short description of it:
![TUTO](assets/fr/22.webp)
Then, add the path of the cover image at the beginning of your tutorial. To do this, note:
```

![cover-sparrow](assets/cover.webp)

```
This syntax will be useful whenever adding an image to your tutorial is necessary. The exclamation point indicates that it is an image, with the alternative text (alt) specified between the brackets. The path to the image is indicated between the parentheses:
![TUTO](assets/fr/23.webp)
## 5 - Add the Logo and Cover
Within the `assets` folder, you must add a file named `logo.webp`, which will serve as a thumbnail for your article. This image must be in `.webp` format and must respect a square dimension to harmonize with the user interface. You are free to choose the logo of the software covered in the tutorial or any other relevant image, provided that it is free of rights. In addition, also add an image titled `cover.webp` in the same place. This image will be displayed at the top of your tutorial. Ensure that this image, like the logo, respects usage rights and is suitable for the context of your tutorial:
## 6 - Writing the Tutorial and Adding Visuals
Continue writing your tutorial by drafting your content. When you want to integrate a subtitle, apply the appropriate markdown formatting by prefixing the text with `##`:
![TUTO](assets/fr/24.webp)
The language subfolder in the `assets` folder is used to store diagrams and visuals that will accompany your tutorial. As much as possible, avoid including text in your images to make your content accessible to an international audience. Of course, the software being presented will contain text, but if you add diagrams or additional indications on software screenshots, do so without text or, if it proves indispensable, use English.
![TUTO](assets/fr/25.webp)
To name your images, simply use numbers corresponding to their order of appearance in the tutorial, formatted with two digits (or three digits if your tutorial contains more than 99 images). For example, name your first image `01.webp`, your second `02.webp`, and so on.
Your images must be in `.webp` format exclusively. If needed, you can use [my image conversion software](https://github.com/LoicPandul/ImagesConverter).
![TUTO](assets/fr/26.webp)
To insert a diagram into your document, use the following Markdown command, making sure to specify the appropriate alternative text as well as the correct path of the image:
```

![sparrow](assets/fr/01.webp)

```