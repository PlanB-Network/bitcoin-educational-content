---
name: Contribución - Tutorial con GitHub Desktop (Intermedio)
description: Guía completa para proponer un tutorial en Plan ₿ Network usando GitHub Desktop
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, debes haber completado algunos pasos preliminares. Si aún no lo has hecho, te invitamos a que primero consultes este tutorial introductorio y luego vuelvas aquí:

https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2
Ya deberías haber:

- Elegido el tema de tu tutorial;
- Contactado con el equipo de Plan ₿ Network a través de [el grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Elegido tus herramientas de contribución.

En este tutorial, veremos cómo añadir tu tutorial en Plan ₿ Network configurando tu entorno local con GitHub Desktop. Si ya dominas Git, puede que este tutorial tan detallado no sea necesario para ti. Más bien te recomendaríamos consultar este otro tutorial donde sólo presentamos las pautas principales, sin una guía detallada paso a paso:

- **Usuarios con experiencia**:

https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410
Si prefieres no configurar tu entorno local, sigue este otro tutorial diseñado para principiantes, donde realizamos los cambios directamente a través de la interfaz web de GitHub:

- **Principiantes (interfaz web)**:

https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79
## Requisitos previos

Software necesario para seguir este tutorial:

- [GitHub Desktop](https://desktop.github.com/);
- Un editor de archivos markdown como [Obsidian](https://obsidian.md/);
- Un editor de código ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/)).

![TUTO](assets/fr/01.webp)

Requisitos previos antes de empezar el tutorial:

- Tener una [cuenta GitHub](https://github.com/signup);
- Disponer de un fork del [Plan ₿ Network source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Tener [un perfil de profesor en Plan ₿ Network](https://planb.network/professors) (sólo si propones un tutorial completo).

Si necesitas ayuda para obtener estos requisitos previos, estos otros tutoriales te ayudarán:

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Una vez que todo está en su lugar y tu entorno local está configurado correctamente con tu propio fork de Plan ₿ Network, puedes empezar a añadir el tutorial.

## 1 - Crear una nueva rama

Abre tu navegador y dirígete a la página de tu fork del repositorio Plan ₿ Network. Esta es la bifurcación que has establecido en GitHub. La URL de tu bifurcación debería parecerse a: `https://github.com/[tu-nombre-deusuario]/bitcoin-educational-content`:

![TUTO](assets/fr/03.webp)

Asegúrate de que estás en la rama principal `dev` y haz clic en el botón `Sync fork`. Si tu rama no está actualizada, GitHub te ofrecerá actualizarla. Procede con esta actualización. Si, por el contrario, tu rama ya está actualizada, GitHub te informará:

![TUTO](assets/fr/04.webp)

Abre el software GitHub Desktop y asegúrate de que tu bifurcación está correctamente seleccionada en la esquina superior izquierda de la ventana:

![TUTO](assets/fr/05.webp)

Haz clic en el botón `Fetch origin`. Si tu repositorio local ya está actualizado, GitHub Desktop no te sugerirá ninguna acción adicional. En caso contrario, aparecerá la opción `Obtener origen`. Haz clic en este botón para actualizar tu repositorio local:

![TUTO](assets/fr/06.webp)

Comprueba que te encuentras en la rama principal `dev`:

![TUTO](assets/fr/07.webp)

Haz clic en esta rama y, a continuación, en el botón `Nueva rama`:

![TUTO](assets/fr/08.webp)

Asegúrate de que la nueva rama se basa en el repositorio fuente, es decir, `PlanB-Network/bitcoin-educational-content`.

Nombra tu rama de forma que el título deje claro su objetivo, utilizando guiones para separar cada palabra. Por ejemplo, digamos que nuestro objetivo es escribir un tutorial sobre el uso del software Sparrow Wallet. En este caso, la rama de trabajo dedicada a escribir este tutorial podría llamarse: `tuto-sparrow-wallet-loic`. Una vez introducido el nombre apropiado, hazs clic en `Crear rama` para confirmar la creación de la rama:

![TUTO](assets/fr/09.webp)

Ahora haz clic en el botón `Publish branch` para guardar tu nueva rama de trabajo en tu fork online en GitHub:

![TUTORIAL](assets/fr/10.webp)

Ahora, en GitHub Desktop, deberías encontrarte en tu nueva rama. Esto significa que todos los cambios realizados localmente en tu ordenador se guardarán exclusivamente en esta rama específica. Además, mientras esta rama permanezca seleccionada en GitHub Desktop, los archivos visibles localmente en tu máquina corresponderán a los de esta rama (`tuto-sparrow-wallet-loic`), y no a los de la rama principal (`dev`).

![TUTORIAL](assets/fr/11.webp)

Para cada nuevo artículo que desees publicar, deberás crear una nueva rama a partir de `dev`. Una rama en Git es una versión paralela del proyecto, que te permite hacer cambios sin afectar a la rama principal, hasta que el trabajo esté listo para ser fusionado.

## 2 - Añadir los archivos del tutorial

Ahora que la rama de trabajo está creada, es hora de integrar tu nuevo tutorial. Tienes dos opciones: utilizar mi script de Python, que automatiza la creación de los documentos necesarios, o crear manualmente cada archivo. Vamos a ver los pasos a seguir para cada opción.

### Con el script Python

Es necesario instalar en tu máquina:

- Python 3.8 o superior.

Para utilizar el script, navega hasta la carpeta donde está almacenado. El script se encuentra en el repositorio de datos Plan ₿ Network en la ruta: `bitcoin-educational-content/scripts/tutorial-related/data-creator`.

Una vez en la carpeta, instala las dependencias:

```
pip install -r requirements.txt
```

A continuación, inicia el software con el comando

```
python3 main.py
```

Se abrirá una interfaz gráfica de usuario (GUI). La primera vez, tendrás que introducir toda la información necesaria, pero en usos posteriores, el script recordará tu información personal, por lo que no tendrás que volver a introducirla.

![DATA-CREATOR-PY](assets/fr/37.webp)

Comienza introduciendo la ruta local a la carpeta `/tutorials` de tu repositorio clonado (`.../bitcoin-educational-content/tutorials/`). Puedes introducirla manualmente o hacer clic en el botón "Examinar" para navegar utilizando tu explorador de archivos.

![DATA-CREATOR-PY](assets/fr/38.webp)

Selecciona el idioma en el que escribirás tu tutorial.

![DATA-CREATOR-PY](assets/fr/39.webp)

En el campo "ID de GitHub del colaborador", introduce tu nombre de usuario de GitHub.

![DATA-CREATOR-PY](assets/fr/40.webp)

A continuación, deberás completar tu perfil de profesor. Hay varias opciones disponibles:
- Ingresa las primeras letras de tu nombre en el campo "Professor Name". Tu nombre aparecerá en la lista desplegable "Prof. Suggestions" que se encuentra debajo. Selecciónalo haciendo clic en él;
- Alternativamente, puedes hacer clic directamente en la lista desplegable "Prof. Suggestions" y elegir tu nombre de profesor.

Esta acción completará automáticamente tu UUID de profesor en el campo correspondiente.

![DATA-CREATOR-PY](assets/fr/41.webp)

Si aún no tienes un perfil de profesor, consulta este tutorial:

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4
A continuación, haz clic en el botón "Nuevo tutorial".

![DATA-CREATOR-PY](assets/fr/42.webp)

Elige una categoría principal para tu tutorial. A continuación, selecciona una subcategoría relevante basada en la categoría principal elegida.

![DATA-CREATOR-PY](assets/fr/43.webp)

Determina el nivel de dificultad del tutorial.

![DATA-CREATOR-PY](assets/fr/44.webp)

Elige un nombre para el directorio creado específicamente para tu tutorial. El nombre de esta carpeta debe reflejar el software cubierto en el tutorial, utilizando guiones para separar las palabras. Por ejemplo, la carpeta podría llamarse `red-wallet`:

![DATA-CREATOR-PY](assets/fr/45.webp)

El `project_id` es el UUID de la empresa u organización que está detrás de la herramienta tratada en el tutorial, disponible [en la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, para un tutorial sobre Sparrow Wallet, puedes encontrar su `project_id` en el archivo: `bitcoin-educational-content/resources/projects/sparrow/project.yml`. Esta información se añade al archivo YAML de tu tutorial porque Plan ₿ Network mantiene una base de datos de empresas y organizaciones activas en Bitcoin o proyectos relacionados. Añadiendo el `project_id` asociado, vinculas tu contenido a la entidad relevante.

***Actualización:*** En la nueva versión del script, ya no es necesario introducir manualmente el `project_id`. Se ha añadido una función de búsqueda para encontrar el proyecto por su nombre y recuperar automáticamente el `project_id` correspondiente. Escribe el principio del nombre del proyecto en el campo "Nombre del proyecto" para buscarlo y, a continuación, selecciona la empresa deseada en el menú desplegable. El `project_id` se rellenará automáticamente en el campo inferior. También puedes introducirlo manualmente si lo necesitas.

![DATA-CREATOR-PY](assets/fr/46.webp)

Para las etiquetas, selecciona 2 o 3 palabras clave relevantes relacionadas con el contenido de tu tutorial, eligiendo exclusivamente de [la lista de etiquetas Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). El software también ofrece una función de búsqueda de palabras clave con una lista desplegable.

![DATA-CREATOR-PY](assets/fr/47.webp)

Una vez introducida y verificada toda la información, haz clic en "Crear tutorial" para confirmar la creación de los archivos de su tutorial. Esto generará localmente su carpeta tutorial y todos los archivos necesarios en la categoría seleccionada.

![DATA-CREATOR-PY](assets/fr/48.webp)

Ahora puedes saltarte la subsección "Sin mi script Python" así como el paso 3, "Rellenar el archivo YAML", ya que el script ya ha completado estas acciones por ti. Procede directamente al paso 4 y comienza a escribir tu tutorial.

Para más información sobre este script de Python, consulta el [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md).

### Sin el script Python

Abre tu gestor de archivos y navega hasta la carpeta `bitcoin-educational-content`, que representa el clon local de tu repositorio. Normalmente la encontrarás en `Documents\GitHub\bitcoin-educational-content`.

Dentro de este directorio, deberás localizar la subcarpeta adecuada para colocar tu tutorial. La organización de la carpeta refleja las diferentes secciones del sitio web de Plan ₿ Network. En nuestro ejemplo, ya que queremos añadir un tutorial sobre Sparrow Wallet, debemos navegar a la siguiente ruta: `bitcoin-educational-content\tutorials\wallet`, que corresponde a la sección `WALLET` del sitio web:

![TUTO](assets/fr/12.webp)

Dentro de la carpeta `wallet`, necesitas crear un nuevo directorio específicamente dedicado a tu tutorial. El nombre de esta carpeta debe evocar el software cubierto en el tutorial, asegurándose de conectar las palabras con guiones. En mi ejemplo, la carpeta se llamará `sparrow-wallet`:

![TUTO](assets/fr/13.webp)

En esta nueva subcarpeta dedicada a tu tutorial, hay que añadir varios elementos:

- Crea una carpeta `assets`, destinada a recibir todas las ilustraciones necesarias para el tutorial;
- Dentro de esta carpeta `assets`, deberás crear una subcarpeta con el nombre del código del idioma original del tutorial. Por ejemplo, si el tutorial está escrito en inglés, esta subcarpeta debe llamarse `en`. Coloca allí todos los elementos visuales del tutorial (diagramas, imágenes, capturas de pantalla, etc.).
- Debe crearse un archivo `tutorial.yml` para registrar los detalles relacionados con tu tutorial;
- Se debe crear un archivo en formato markdown para escribir el contenido real del tutorial. Este archivo debe titularse según el código del idioma en el que se escriba. Por ejemplo, para un tutorial escrito en francés, el archivo debe llamarse `fr.md`.

![TUTO](assets/fr/14.webp)

En resumen, ésta es la jerarquía de archivos que hay que crear:

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```

## 3 - Rellena el archivo YAML

Rellena el archivo `tutorial.yml` copiando la siguiente plantilla:

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

- **id**: Un UUID (_Identificador Universalmente Único_) que permite identificar de manera única el tutorial. Puedes generarlo con [una herramienta en línea](https://www.uuidgenerator.net/version4). El único requisito es que este UUID sea aleatorio para evitar conflictos con otro UUID en la plataforma;

- **project_id**: El UUID de la empresa u organización detrás de la herramienta presentada en el tutorial [desde la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, si estás creando un tutorial sobre el software Green Wallet, puedes encontrar el `project_id` en el siguiente archivo: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Esta información se agrega al archivo YAML de su tutorial porque Plan ₿ Network mantiene una base de datos de todas las empresas y organizaciones que operan en Bitcoin o proyectos relacionados. Al agregar el `project_id` de la entidad relacionada con su tutorial, se crea un vínculo entre ambos elementos;

- **tags**: 2 o 3 palabras clave relevantes relacionadas con el contenido del tutorial, elegidas exclusivamente [de la lista de etiquetas de Plan ₿ Network](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: La subcategoría correspondiente al contenido del tutorial, según la estructura del sitio web de Plan ₿ Network (por ejemplo, para monederos: `desktop`, `hardware`, `mobile`, `backup`);

- **level**: El nivel de dificultad del tutorial, elegido entre:
    - `beginner`
    - `intermediate`
    - `advanced`
    - `expert`

- **professor_id**: Tu `professor_id` (UUID) tal como aparece en [tu perfil de profesor](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors);

- **original_language**: El idioma original del tutorial (por ejemplo, `fr`, `en`, etc.);

- **proofreading**: Información sobre el proceso de revisión. Completa la primera parte, ya que la revisión de tu propio tutorial cuenta como una primera validación:
    - **language**: Código de idioma de la revisión (por ejemplo, `fr`, `en`, etc.).
    - **last_contribution_date**: Fecha del día.
    - **urgency**: 1
    - **contributor_names**: Tu ID de GitHub.
    - **reward**: 0

Para más detalles sobre tu ID de profesor, consulta el tutorial correspondiente:

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

Una vez que hayas terminado de modificar el archivo `tutorial.yml`, guarda el documento haciendo clic en `Archivo > Guardar`:

![TUTO](assets/fr/16.webp)

Ahora puedes cerrar el editor de código.

## 4 - Rellenar el archivo Markdown

Ahora, puedes abrir el archivo que alojará tu tutorial, nombrado con el código de tu idioma, como `fr.md`. Ve a Obsidian, en la parte izquierda de la ventana, desplázate por el árbol de carpetas hasta que encuentres la carpeta de tu tutorial y el archivo que estás buscando:

![TUTO](assets/fr/18.webp)

Haz clic en el archivo para abrirlo:

![TUTO](assets/fr/19.webp)

Empezaremos rellenando la sección `Propiedades` de la parte superior del documento.

![TUTO](assets/fr/20.webp)

Añade y rellena manualmente el siguiente bloque de código:

```
---
name: [Title]
description: [Description]
---
```

![TUTO](assets/fr/21.webp)

Escribe el nombre de tu tutorial y una breve descripción del mismo:

![TUTO](assets/fr/22.webp)

A continuación, añade la ruta de la imagen de portada al principio de tu tutorial. Para ello, ten en cuenta:

```
![cover-sparrow](assets/cover.webp)
```

Esta sintaxis te será útil siempre que sea necesario añadir una imagen a tu tutorial. El signo de exclamación indica que se trata de una imagen, con el texto alternativo (alt) especificado entre los corchetes. La ruta a la imagen se indica entre los paréntesis:

![TUTO](assets/fr/23.webp)

## 5 - Añadir el logotipo y la portada

Dentro de la carpeta `assets`, deberás añadir un archivo llamado `logo.webp`, que servirá como miniatura de tu tutorial. Esta imagen debe estar en formato `.webp` y debe respetar una dimensión cuadrada para armonizar con la interfaz de usuario. Puedes elegir libremente el logotipo del software tratado en el tutorial o cualquier otra imagen pertinente, siempre que esté libre de derechos. Además, añade también una imagen titulada `cover.webp` en el mismo lugar. Esta imagen se mostrará en la parte superior del tutorial. Asegúrate de que esta imagen, al igual que el logotipo, respeta los derechos de uso y es adecuada para el contexto de tu tutorial:

## 6 - Escribir el tutorial y añadir elementos visuales

Continúa escribiendo tu tutorial redactando el contenido. Cuando desees integrar un subtítulo, aplica el formato markdown adecuado anteponiendo al texto el prefijo `##`:

![TUTO](assets/fr/24.webp)

La subcarpeta de idiomas de la carpeta `assets` se utiliza para almacenar los diagramas y elementos visuales que acompañarán a tu tutorial. En la medida de lo posible, evita incluir texto en tus imágenes para que el contenido sea accesible a un público internacional. Por supuesto, el software que se presenta contendrá texto, pero si añades diagramas o indicaciones adicionales en las capturas de pantalla del software, hazlo sin texto o, si resulta imprescindible, utilízalo en inglés.

![TUTO](assets/fr/25.webp)

Para nombrar tus imágenes, utiliza simplemente los números correspondientes al orden de aparición en el tutorial, formateados con dos dígitos (o tres dígitos si su tutorial contiene más de 99 imágenes). Por ejemplo, llama a tu primera imagen `01.webp`, a la segunda `02.webp`, y así sucesivamente.

Tus imágenes deben estar exclusivamente en formato `.webp`. Si es necesario, puedes utilizar [este software de conversión de imágenes](https://github.com/LoicPandul/ImagesConverter).

![TUTO](assets/fr/26.webp)

Para insertar un diagrama en tu documento, utiliza el siguiente comando Markdown, asegurándote de especificar el texto alternativo apropiado, así como la ruta correcta de la imagen:

```
![sparrow](assets/fr/01.webp)
```

El signo de exclamación al principio indica que se trata de una imagen. El texto alternativo, que ayuda a la accesibilidad y al SEO, se coloca entre paréntesis. Por último, la ruta a la imagen se indica entre los paréntesis.

Si deseas crear tus propios diagramas, asegúrate de respetar la carta gráfica del Plan ₿ Network para garantizar la coherencia visual:


- **Fuente**: Utiliza [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Colores**:
 - Naranja: #FF5C00
 - Negro #000000
 - Blanco: #FFFFFF

**Es imprescindible que todos los elementos visuales integrados en tus tutoriales estén libres de derechos o respeten la licencia del archivo fuente**. Asimismo, todos los diagramas publicados en Plan ₿ Network están disponibles bajo licencia CC-BY-SA, del mismo modo que el texto.

**-> Consejo:** Al compartir archivos públicamente, como imágenes, es importante eliminar cualquier metadato innecesario. Estos pueden contener información sensible, como datos de localización, fechas de creación o detalles sobre el autor. Para proteger tu privacidad, es aconsejable eliminar estos metadatos. Para simplificar este proceso, puedes utilizar herramientas especializadas como [Exif Cleaner](https://exifcleaner.com/), que permite limpiar los metadatos de un documento con un simple arrastrar y soltar.

## 7 - Guardar y enviar el tutorial.

Una vez que hayas terminado de escribir tu tutorial en el idioma de tu elección, el siguiente paso es enviar una **Pull Requestn**. El administrador se encargará entonces de añadir las traducciones que falten de tu tutorial, gracias a nuestro método de traducción automática con revisión humana.

Para proceder con la Pull Request, abre el software GitHub Desktop. El software debería detectar automáticamente los cambios que has realizado localmente en tu rama en comparación con el repositorio original. Antes de continuar, comprueba cuidadosamente en la parte izquierda de la interfaz que estos cambios coinciden con lo que esperabas:

![TUTO](assets/fr/28.webp)

Añade un título a tu confirmación y haz clic en el botón azul `Commit to [your branch]` para validar los cambios:

![TUTO](assets/fr/29.webp)

Un commit es un almacenamiento de los cambios realizados en la rama, acompañados de un mensaje descriptivo, que permite seguir la evolución de un proyecto a lo largo del tiempo. Es una especie de punto de control intermedio.

A continuación, haz clic en el botón `Push origin`. Esto enviará tu commit a tu fork:

![TUTO](assets/fr/30.webp)

Si no has terminado tu tutorial, puedes volver a él más tarde y hacer nuevos commits. Si has completado tus cambios para esta rama, haz clic ahora en el botón `Preview Pull Request`:

![TUTO](assets/fr/31.webp)

Puedes comprobar una última vez que tus modificaciones son correctas y, a continuación, hacer clic en el botón `Create pull request`:

![TUTO](assets/fr/32.webp)

Una Pull Request es una solicitud realizada para integrar los cambios de tu rama a la rama principal del repositorio Plan ₿ Network, lo que permite la revisión y discusión de los cambios antes de su fusión.

Se te redirigirá automáticamente a tu navegador en GitHub a la página de preparación de tu Pull Request:

![TUTO](assets/fr/33.webp)

Indica un título que resuma brevemente los cambios que deseas fusionar con el repositorio fuente. Añade un breve comentario que describa estos cambios (si tienes un número de "issue" asociado a la creación de tu tutorial, recuerda anotarlo en el comentario `Closes #{issue number}`) y, a continuación, haz clic en el botón verde `Create pull request` para confirmar la Pull Request:

![TUTO](assets/fr/34.webp)

A continuación, tu PR estará visible en la pestaña `Pull Request` del repositorio principal Plan ₿ Network. Todo lo que tienes que hacer es esperar a que un administrador se ponga en contacto contigo para confirmar la fusión de tu contribución o para solicitar cualquier modificación adicional.

![TUTO](assets/fr/35.webp)

Después de que tu PR se haya fusionada con la rama principal, se recomienda eliminar tu rama de trabajo (`tuto-sparrow-wallet`) para mantener un historial limpio en tu bifurcación. GitHub te ofrecerá automáticamente esta opción en la página de su PR:

![TUTO](assets/fr/36.webp)

En el software de escritorio de GitHub, puedes volver a la rama principal de tu bifurcación (`dev`).

![TUTO](assets/fr/07.webp)

Si deseas realizar cambios en tu contribución después de haber presentado su PR, el procedimiento dependerá del estado actual del PR:

- Si tu PR sigue abierto y aún no se ha fusionado, realiza los cambios localmente permaneciendo en la misma rama. Una vez finalizadas las modificaciones, utiliza el botón `Push origin` para añadir un nuevo commit a tu PR aún abierto;
- Si tu PR ya ha sido fusionado con la rama principal, necesitarás comenzar el proceso de nuevo creando una nueva rama y enviando un nuevo PR. Asegúrate de que tu repositorio local está sincronizado con el repositorio fuente de Plan ₿ Network antes de continuar.

Si encuentras dificultades técnicas para enviar tu tutorial, no dudes en pedir ayuda en [nuestro grupo de Telegram dedicado a las contribuciones](https://t.me/PlanBNetwork_ContentBuilder). Muchas gracias


