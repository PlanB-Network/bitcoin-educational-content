---
name: Contribución - GitHub Web tutorial (principiante)
description: Guía completa para publicar tutoriales en Plan ₿ Academy con GitHub Web
---
![cover](assets/cover.webp)

Antes de seguir este tutorial sobre cómo añadir un nuevo tutorial, necesitas haber completado algunos pasos preliminares. Si aún no lo has hecho, echa un vistazo primero a este tutorial introductorio y luego vuelve aquí:

https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Ya deberías haber:

- Elegido un tema para tu tutorial;
- Puesto en contacto con el equipo de Plan ₿ Academy a través de [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o paolo@planb.network;
- Elegido tus herramientas de contribución.

En este tutorial, veremos cómo añadir tu tutorial a Plan ₿ Academy utilizando la versión web de GitHub. Si ya dominas Git, puede que este tutorial tan detallado no sea necesario para ti. En su lugar, te recomendamos que eches un vistazo a alguno de estos otros 2 tutoriales, donde se detallan las pautas a seguir y los pasos para realizar cambios desde un archivo:


- **Usuarios con experiencia**:

https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- **Intermedio (GitHub Desktop)**:

https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Requisitos previos

Requisitos previos antes de empezar el tutorial:

- Tener una [cuenta GitHub](https://github.com/signup);
- Disponer de un fork del [Plan ₿ Academy source repository](https://github.com/PlanB-Network/bitcoin-educational-content);
- Tener [un perfil de profesor en Plan ₿ Academy](https://planb.academy/professors) (sólo si ofreces una tutoría completa).

Si necesitas ayuda para conseguir estos requisitos previos, estos otros tutoriales te ayudarán:

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.academy/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Una vez que todo esté en su lugar y tengas tu fork del repositorio Plan ₿ Academy, puedes empezar a añadir el tutorial.

## 1 - Crear una nueva rama

Abre tu navegador y navega a tu página de bifurcación en el repositorio Plan ₿ Academy. Esta es la bifurcación que has establecido en GitHub. La URL de tu bifurcación debe tener este aspecto: `https://github.com/[tu-nombre-deusuario]/bitcoin-educational-content`:

![GITHUB](assets/fr/01.webp)

Asegúrate de que estás en la rama principal `dev` y haz clic en el botón "*Sync fork*". Si tu bifurcación no está actualizada, GitHub te pedirá que actualices tu rama. Procede con esta actualización:

![GITHUB](assets/fr/02.webp)

Haz clic en la rama `dev` y, a continuación, nombra tu rama de trabajo de forma que su título refleje claramente tu objetivo, utilizando guiones para separar las palabras. Por ejemplo, si nuestro objetivo es escribir un tutorial sobre el uso de Green Wallet, la rama podría llamarse `tuto-green-wallet-loic`. Tras introducir un nombre adecuado, haz clic en "*Crear rama*" para confirmar la creación de tu nueva rama basada en `dev`:

![GITHUB](assets/fr/03.webp)

Ahora deberías estar en tu nueva rama de trabajo:

![GITHUB](assets/fr/04.webp)

Esto significa que cualquier cambio que hagas se guardará sólo en esa rama específica.

Para cada nuevo artículo que vayas a publicar, crea una nueva rama a partir de `dev`.

Una rama en Git representa una versión paralela del proyecto, que te permite trabajar en modificaciones sin afectar a la rama principal, hasta que tu trabajo esté listo para ser integrado.

## 2 - Añadir los archivos del tutorial

Ahora que se ha creado la rama de trabajo, es el momento de integrar tu nuevo tutorial.

Dentro de tus archivos de rama, tendrás que encontrar la subcarpeta adecuada para la colocación del tutorial. La organización de las carpetas refleja las diferentes secciones del sitio web de Plan ₿ Academy. En nuestro ejemplo, ya que estamos añadiendo un tutorial sobre Green Wallet, dirígete a la siguiente ruta: `bitcoin-educational-content\tutorials\wallet` que corresponde a la sección `WALLET` del sitio web:

![GITHUB](assets/fr/05.webp)

En la carpeta `wallet`, crea un nuevo directorio dedicado específicamente a tu tutorial. El nombre de esta carpeta debe indicar claramente el software cubierto en el tutorial, utilizando guiones para conectar las palabras. En este ejemplo, la carpeta se llamará `green-wallet`. Haz clic en "*Añadir archivo*" y luego en "*Crear nuevo archivo*":

![GITHUB](assets/fr/06.webp)

Introduce el nombre de la carpeta seguido de una barra `/` para confirmar su creación como carpeta.

![GITHUB](assets/fr/07.webp)

En esta nueva subcarpeta dedicada a tu tutorial, deberás añadir varios elementos:

- Crea una carpeta `assets` para guardar todas las ilustraciones necesarias para tu tutorial;
- Dentro de esta carpeta `assets`, crea una subcarpeta con el nombre del código del idioma original del tutorial. Por ejemplo, si el tutorial está escrito en inglés, esta subcarpeta debería llamarse `en`. Coloca todos los elementos visuales del tutorial (diagramas, imágenes, capturas de pantalla, etc.) en esta carpeta.
- Deberás crear un archivo `tutorial.yml` para registrar los detalles de tu tutorial;
- Debe crearse un archivo markdown para escribir el contenido real del tutorial. Este archivo debe nombrarse de acuerdo con el código del idioma en el que está escrito. Por ejemplo, para un tutorial escrito en francés, el archivo debe llamarse `fr.md`.

Para resumir, esta es la jerarquía de archivos (seguiremos creándolos en la próxima sección):

```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```

## 3 - Llena el archivo YAML

Empecemos con el archivo YAML. En la casilla para crear un nuevo archivo, introduce `tutorial.yml` :

![GITHUB](assets/fr/08.webp)

Llena el archivo `tutorial.yml` copiando la siguiente plantilla:

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

- **project_id**: El UUID de la empresa u organización detrás de la herramienta presentada en el tutorial [desde la lista de proyectos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects). Por ejemplo, si estás creando un tutorial sobre el software Green Wallet, puedes encontrar el `project_id` en el siguiente archivo: `bitcoin-educational-content/resources/projects/blockstream/project.yml`. Esta información se agrega al archivo YAML de su tutorial porque Plan ₿ Academy mantiene una base de datos de todas las empresas y organizaciones que operan en Bitcoin o proyectos relacionados. Al agregar el `project_id` de la entidad relacionada con su tutorial, se crea un vínculo entre ambos elementos;

- **tags**: 2 o 3 palabras clave relevantes relacionadas con el contenido del tutorial, elegidas exclusivamente [de la lista de etiquetas de Plan ₿ Academy](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);

- **category**: La subcategoría correspondiente al contenido del tutorial, según la estructura del sitio web de Plan ₿ Academy (por ejemplo, para monederos: `desktop`, `hardware`, `mobile`, `backup`);

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

https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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

Una vez que hayas terminado de modificar el archivo `tutorial.yml`, guarda tu documento haciendo clic en el botón "*Commit changes...*":

![GITHUB](assets/fr/09.webp)

Añade un título y una descripción, y asegúrate de que el commit se haga en la rama que creaste al principio de este tutorial. A continuación, confirma haciendo clic en "*Commit changes*".

![GITHUB](assets/fr/10.webp)

## 4 - Crear subcarpetas para las imágenes

Vuelve a hacer clic en "*Añadir archivo*" y, a continuación, en "*Crear nuevo archivo*":

![GITHUB](assets/fr/11.webp)

Introduce `assets` seguido de una barra `/` para crear la carpeta:

![GITHUB](assets/fr/12.webp)

Repite este paso en la carpeta `/assets` para crear la subcarpeta del idioma, por ejemplo `fr` si el tutorial está en francés:

![GITHUB](assets/fr/13.webp)

En esta carpeta, crea un archivo ficticio para forzar a GitHub a mantener tu carpeta (que de otro modo estaría vacía). Nombra este archivo `.gitkeep`. A continuación, haz clic en "*Commit changes...*".

![GITHUB](assets/fr/14.webp)

Comprueba de nuevo que te encuentras en la rama correcta y, a continuación, haz clic en "*Commit changes*".

![GITHUB](assets/fr/15.webp)

## 5 - Creación del archivo Markdown

Ahora vamos a crear el archivo que alojará tu tutorial, llamado según el código de tu idioma, por ejemplo `fr.md` si estamos escribiendo en francés. Ve a la carpeta de tu tutorial:

![GITHUB](assets/fr/16.webp)

Haz clic en "*Añadir archivo*" y, a continuación, en "*Crear nuevo archivo*".

![GITHUB](assets/fr/17.webp)

Nombra el archivo utilizando el código de tu idioma. En este caso, como el tutorial está escrito en francés, llamamos al archivo `fr.md`. La extensión `.md` indica que el archivo está en formato Markdown.

![GITHUB](assets/fr/18.webp)

Empezaremos rellenando la sección `Properties` en la parte superior del documento. Añade y rellena manualmente el siguiente bloque de código (las claves `name:` y `description:` deben mantenerse en inglés, pero sus valores deben escribirse en el idioma utilizado en tu tutorial):

```
---
name: [Titre]
description: [Description]
---
```

![GITHUB](assets/fr/19.webp)

Escribe el nombre de tu tutorial y una breve descripción:

![GITHUB](assets/fr/20.webp)

A continuación, añade la ruta a la imagen de portada al principio del tutorial. Para ello, anota:

```
![cover-green](assets/cover.webp)
```

Esta sintaxis te resultará útil siempre que necesites añadir una imagen a tu tutorial. El signo de exclamación indica una imagen, cuyo texto alternativo (alt) se especifica entre los corchetes. La ruta a la imagen se indica entre los paréntesis:

![GITHUB](assets/fr/21.webp)

Haz clic en el botón "*Commit changes...*" para guardar este archivo.

![GITHUB](assets/fr/22.webp)

Comprueba que estás en la rama correcta y confirma la confirmación.

![GITHUB](assets/fr/23.webp)

Tu carpeta de tutoriales debería tener ahora este aspecto, según tu código de idioma:

![GITHUB](assets/fr/24.webp)

## 6 - Añadir logotipo y portada

Dentro de la carpeta `assets`, necesitarás añadir un archivo llamado `logo.webp`, que servirá como miniatura de tu tutorial. Esta imagen debe estar en formato `.webp`, y debe ser de tamaño cuadrado para que coincida con la interfaz de usuario.

Puedes elegir el logotipo del software utilizado en el tutorial, o cualquier otra imagen relevante, siempre que esté libre de derechos de autor. Además, añade una imagen titulada `cover.webp` en el mismo lugar. Se mostrará en la parte superior del tutorial. Asegúrate de que esta imagen, al igual que el logotipo, respeta los derechos de uso y es adecuada al contexto de tu tutorial.

Para añadir imágenes a la carpeta `/assets`, puedes arrastrarlas y soltarlas desde tus archivos locales. Asegúrate de que estás en la carpeta `/assets` y en la rama correcta, luego haz clic en "*Commit changes*".

![GITHUB](assets/fr/26.webp)

Ahora deberías ver aparecer las imágenes en la carpeta.

![GITHUB](assets/fr/27.webp)

## 7 - Escribir el tutorial

Continúa escribiendo tu tutorial anotando tu contenido en el archivo Markdown con el código del idioma (en nuestro ejemplo, en francés, es el archivo `fr.md`). Ve al archivo y haz clic en el icono del lápiz:

![GITHUB](assets/fr/28.webp)

Empieza a escribir tu tutorial. Cuando añadas un subtítulo, utiliza el formato Markdown adecuado anteponiendo al texto el prefijo `##`:

![GITHUB](assets/fr/29.webp)

Alterna entre las vistas "*Edición*" y "*Vista previa*" para visualizar mejor el renderizado.

![GITHUB](assets/fr/30.webp)

Para guardar tu trabajo, haz clic en "*Commit Changes...*", asegúrate de que estás en la rama correcta y, a continuación, confirma haciendo clic de nuevo en "*Commit Changes*".

![GITHUB](assets/fr/31.webp)

## 8 - Añade elementos visuales

La subcarpeta de idioma de la carpeta `/assets` (en nuestro ejemplo: `/assets/en`) se utiliza para almacenar los diagramas y elementos visuales que acompañarán al tutorial. En la medida de lo posible, evita incluir texto en las imágenes para que el contenido sea accesible a un público internacional. Por supuesto, el software presentado contendrá texto, pero si añades esquemas o indicaciones adicionales en las capturas de pantalla del software, hazlo sin texto o, si es imprescindible, utiliza el inglés.

Para nombrar tus imágenes, utiliza simplemente los números correspondientes al orden de aparición en el tutorial, formateados con dos dígitos (o tres dígitos si el tutorial contiene más de 99 imágenes). Por ejemplo, nombra la primera imagen `01.webp`, a la segunda `02.webp`, y así sucesivamente.

Tus imágenes deben estar únicamente en formato `.webp`. Si es necesario, puedes utilizar [este software de conversión de imágenes](https://github.com/LoicPandul/ImagesConverter).

![GITHUB](assets/fr/32.webp)

Ahora que has añadido tus imágenes a la subcarpeta, puedes eliminar el archivo ficticio `.gitkeep`. Abre este archivo, haz clic en los tres puntitos de la esquina superior derecha y luego en "*Borrar archivo*".

![GITHUB](assets/fr/33.webp)

Guarda los cambios haciendo clic en "*Commit changes...*".

![GITHUB](assets/fr/34.webp)

Para insertar un diagrama de tu subcarpeta en el tutorial, utiliza el siguiente comando Markdown, teniendo cuidado de especificar el texto alternativo apropiado y la ruta de la imagen correcta para tu idioma:

```
![green](assets/fr/01.webp)
```

El signo de exclamación al principio indica una imagen. El texto alternativo, que ayuda a la accesibilidad y a la referenciación, se coloca entre corchetes. Por último, la ruta a la imagen se indica entre paréntesis.

![GITHUB](assets/fr/35.webp)

Si deseas crear tus propios esquemas, asegúrate de seguir las directrices gráficas de Plan ₿ Academy para garantizar la coherencia visual:

- **Fuente**: Utiliza [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Colores**:
 - Naranja: #FF5C00
 - Negro : #000000
 - Blanco: #FFFFFF

**Es imprescindible que todos los elementos visuales integrados en tus tutoriales estén libres de derechos de autor o respeten la licencia del archivo fuente**. Por lo tanto, todos los diagramas publicados en Plan ₿ Academy están disponibles bajo una licencia CC-BY-SA, del mismo modo que el texto.

**-> Consejo:** Al compartir archivos en público, como imágenes, es importante eliminar los metadatos. Estos pueden contener información sensible, como datos de ubicación, fechas de creación y detalles del autor. Para proteger tu privacidad, es una buena idea eliminar estos metadatos. Para simplificar esta operación, puedes utilizar herramientas especializadas como [Exif Cleaner](https://exifcleaner.com/), que te permite limpiar los metadatos de un documento con un simple arrastrar y soltar.

## 9 - Proponer el tutorial

Una vez que hayas terminado de escribir tu tutorial en el idioma de tu elección, el siguiente paso es enviar una **Pull Request**. El administrador añadirá las traducciones que faltan a tu tutorial, utilizando nuestro método de traducción automática con revisión humana.

Para proceder con el Pull Request, después de guardar todos tus cambios, haz clic en el botón "*Contribuir*", luego en "*Open pull request*" :

![GITHUB](assets/fr/36.webp)

Una Pull Request es una solicitud realizada para integrar cambios de tu rama en la rama principal del repositorio Plan ₿ Academy, lo que permite revisar y discutir los cambios antes de fusionarlos.

Antes de continuar, comprueba detenidamente en la parte inferior de la interfaz que estos cambios son los esperados:

![GITHUB](assets/fr/37.webp)

Asegúrate, en la parte superior de la interfaz, de que tu rama de trabajo está fusionada en la rama `dev` del repositorio Plan ₿ Academy (que es la rama principal).

Introduce un título que resuma brevemente los cambios que deseas fusionar con el repositorio fuente. Añade un breve comentario que describa estos cambios (si tienes un número de "issue" asociado a la creación de tu tutorial, recuerda anotar `Closes #{issue number}` como comentario) y, a continuación, haz clic en el botón verde "*Create pull request*" para confirmar la solicitud de fusión:

![GITHUB](assets/fr/38.webp)

Tu PR estará visible en la pestaña "*Pull Request*" del repositorio principal de Plan ₿ Academy. Todo lo que tienes que hacer ahora es esperar a que un administrador se ponga en contacto contigo para confirmar que tu contribución ha sido fusionada, o para solicitar cualquier otra modificación.

![GITHUB](assets/fr/39.webp)

Después de fusionar tu PR con la rama principal, te recomendamos borrar tu rama de trabajo (en nuestro ejemplo: `tuto-green-wallet`) para mantener un historial limpio de tu bifurcación. GitHub te ofrecerá automáticamente esta opción en la página de tu PR:

![GITHUB](assets/fr/40.webp)

Si deseas realizar cambios en tu contribución después de haber presentado tu PR, los pasos a seguir dependen del estado actual de tu PR:

- Si tu PR sigue abierto y aún no se ha fusionado, realiza los cambios en la misma rama de trabajo. Los cambios confirmados se añadirán a tu PR aún abierto;
- En el caso de que el PR ya se haya fusionado con la rama principal, tendrás que rehacer el proceso desde el principio creando una nueva rama y enviando un nuevo PR. Asegúrate de que tu bifurcación está sincronizada con el repositorio fuente de Plan ₿ Academy en la rama `dev` antes de continuar.

Si tienes dificultades técnicas para enviar tu tutorial, no dudes en pedir ayuda en [nuestro grupo de Telegram dedicado a las contribuciones](https://t.me/PlanBNetwork_ContentBuilder). Muchas gracias
