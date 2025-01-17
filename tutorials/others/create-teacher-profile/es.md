---
name: PlanB Professor
description: Cómo agregar tu perfil de profesor en la Red PlanB?
---
![cover](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos de primera categoría sobre Bitcoin, en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, lo que permite a cualquier persona participar en enriquecer la plataforma. Las contribuciones pueden tomar diversas formas: corregir y revisar textos existentes, producir cursos de formación, traducir a otros idiomas, actualizar información o crear nuevos tutoriales aún no disponibles en nuestro sitio.

Si deseas agregar un nuevo tutorial completo o un curso en la Red PlanB, necesitarás crear tu perfil de profesor. Esto te permitirá ser debidamente acreditado por el contenido que produces en el sitio web.
![tutorial](assets/1.webp)
Si previamente has contribuido a la Red PlanB, es probable que ya tengas un ID de colaborador. Puedes encontrarlo en tu carpeta de profesor accesible [a través de esta página](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors). Si este es el caso, puedes saltarte este tutorial y comenzar a contribuir directamente.
![tutorial](assets/2.webp)

¡Descubramos juntos cómo agregar un nuevo profesor en este tutorial!

## Prerrequisitos

**Software requerido para seguir mi tutorial:**
- [GitHub Desktop](https://desktop.github.com/)
- Un editor de código ([VSC](https://code.visualstudio.com/) o [Sublime Text](https://www.sublimetext.com/))
![tutorial](assets/3.webp)
**Prerrequisitos antes de comenzar el tutorial:**
- Tener una [cuenta de GitHub](https://github.com/signup).
- Tener un fork del [repositorio fuente de la Red PlanB](https://github.com/PlanB-Network/bitcoin-educational-content).

**Si necesitas ayuda para obtener estos prerrequisitos, mis otros tutoriales te guiarán:**
**[Entendiendo Git y GitHub](https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb)**
**[Creando una Cuenta de GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Configurando Tu Entorno de Trabajo](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**

## ¿Cómo crear un nuevo perfil de profesor?

- Abre tu navegador y navega a la página de tu fork del repositorio PlanB. La URL de tu fork debería verse así: `https://github.com/[nombredeusuario]/bitcoin-educational-content`
![tutorial](assets/4.webp)
- Asegúrate de estar en la rama principal `dev` y luego haz clic en el botón `Sync fork`. Si tu fork no está actualizado, GitHub te ofrecerá actualizar tu rama. Procede con esta sincronización.

- Si, por otro lado, tu rama ya está actualizada, GitHub te informará:
![tutorial](assets/5.webp)- Abre GitHub Desktop y asegúrate de que tu fork esté correctamente seleccionado en la esquina superior izquierda de la ventana:
![tutorial](assets/6.webp)
- Haz clic en el botón `Fetch origin`.

- Si tu repositorio local ya está actualizado, GitHub Desktop no sugerirá ninguna acción adicional. De lo contrario, aparecerá la opción `Pull origin`. Haz clic en este botón para actualizar tu repositorio local:
![tutorial](assets/7.webp)
- Asegúrate de estar en la rama principal `dev`:
![tutorial](assets/8.webp)
- Haz clic en esta rama, luego haz clic en el botón `New Branch`:
![tutorial](assets/9.webp)
- Asegúrate de que la nueva rama esté basada en el repositorio fuente, a saber, `PlanB-Network/bitcoin-educational-content`.
- Nombra tu rama de una manera que el título sea claro sobre su propósito, utilizando guiones para separar cada palabra. Dado que esta rama está destinada a agregar un perfil de profesor, un nombre de ejemplo podría ser: `add-professor-[tu-nombre]`. Después de ingresar el nombre, haz clic en `Create branch` para confirmar su creación:
![tutorial](assets/10.webp)
- Ahora haz clic en el botón `Publish branch` para guardar tu nueva rama de trabajo en tu fork en línea en GitHub:
![tutorial](assets/11.webp)
- En este punto, en GitHub Desktop, deberías estar en tu nueva rama. Esto significa que todas las modificaciones realizadas localmente en tu computadora se registrarán exclusivamente en esta rama específica. Además, mientras esta rama permanezca seleccionada en GitHub Desktop, los archivos visibles localmente en tu máquina corresponden a los de esta rama (`add-professor-tu-nombre`), y no a los de la rama principal (`dev`):
![tutorial](assets/12.webp)
- Para agregar tu perfil de profesor, abre tu explorador de archivos y navega a tu repositorio local, en la carpeta `professors`. La encontrarás bajo la ruta: `\GitHub\bitcoin-educational-content\professors`.

- Dentro de esta carpeta, crea una nueva carpeta nombrada con tu nombre o pseudónimo. Asegúrate de que no haya espacios en el nombre de la carpeta. Así, si tu nombre es "Loic Pandul" y ningún otro profesor tiene este nombre, la carpeta a crear será nombrada `loic-pandul`:
![tutorial](assets/13.webp)
- Para facilitar las cosas, ya puedes copiar y pegar todos los documentos de otro profesor en tu propia carpeta. Luego procederemos a modificar estos documentos para personalizarlos según tu perfil:
![tutorial](assets/14.webp)
- Comienza navegando a la carpeta `assets`. Elimina la foto de perfil del profesor que previamente copiaste y reemplázala con tu propia imagen de perfil. Es imperativo que esta imagen esté en formato `.webp` y que se nombre `profile`, dando así el nombre completo del archivo `profile.webp`. Ten en cuenta, esta imagen será publicada en Internet y accesible para todos: ![tutorial](assets/15.webp)
- A continuación, abre el archivo `professor.yml` con tu editor de código (VSC o Sublime Text, por ejemplo). Llegarás al archivo copiado de un profesor existente:
![tutorial](assets/16.webp)
- Debes actualizar la información existente con la tuya propia:
	- **name:** escribe tu nombre o pseudónimo;
	- **links:** indica tus cuentas en redes sociales como Twitter y Nostr, así como la URL de tu sitio web personal (opcional);
	- **affiliation:** menciona el nombre de la empresa que te emplea (opcional);
	- **tags:** especifica tus áreas de especialización de la siguiente lista, sabiendo que puedes agregar tus propios temas. Sin embargo, asegúrate de limitar el número de etiquetas a 4 como máximo para garantizar una buena UI:
	    - privacy,
	    - cryptography,
	    - bitcoin,
	    - mining,
	    - lightning-network,
	    - economy,
	    - history,
	    - merchants,
	    - security,
	    - ...
	- **tips:** proporciona tu dirección Lightning para donaciones para permitir que los lectores de tus futuros tutoriales te envíen algunos sats (opcional);
	- **company:** si posees una, indica el nombre de tu empresa (opcional). Debes actualizar la información existente con la tuya propia:
![tutorial](assets/17.webp)- También debes modificar el `contributor-id`. Este identificador se utiliza para reconocerte en el sitio web, pero no se hace público fuera de GitHub. Eres libre de elegir cualquier combinación de dos palabras, refiriéndote a [la lista en inglés de 2048 palabras de BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). No olvides insertar un guion entre las dos palabras elegidas. Por ejemplo, aquí, elegí `crazy-cactus`:
![tutorial](assets/18.webp)
- Una vez que hayas terminado de modificar el documento `professor.yml`, haz clic en `File > Save` para guardar tu archivo. Luego puedes salir de tu editor de código:
![tutorial](assets/19.webp)
- Dentro de tu carpeta de profesor, puedes eliminar documentos escritos en idiomas que no te conciernen, los cuales fueron inicialmente copiados de otro profesor. Conserva únicamente el archivo correspondiente a tu lengua materna. Por ejemplo, en mi caso, solo conservé el archivo `fr.yml`, ya que mi idioma es el francés: ![tutorial](assets/20.webp)
- Haz doble clic en este archivo para abrirlo con tu editor de código.

- En este archivo, tienes la oportunidad de escribir tu biografía completa bajo la sección `bio` y un resumen o un título sucinto bajo `short_bio`:
![tutorial](assets/21.webp)
- Después de guardar tu documento `fr.yml`, necesitas crear una copia de este archivo para cada uno de los siguientes ocho idiomas:
    - Alemán (DE);
    - Inglés (EN);
    - Francés (FR);
    - Español (ES);
    - Italiano (IT);
    - Portugués (PT);
    - Japonés (JA);
    - Vietnamita (VI).

- Procede a copiar y pegar tu archivo original, luego traduce cada documento al idioma correspondiente. Si dominas el idioma, puedes realizar la traducción manualmente. De lo contrario, siéntete libre de usar una herramienta de traducción automática o un chatbot:
![tutorial](assets/22.webp)
- Si lo prefieres, también es posible conservar únicamente la biografía en tu idioma nativo; nosotros nos encargaremos de la traducción después de la presentación de tu Pull Request.

- Tu carpeta de profesor debería lucir así:
![tutorial](assets/23.webp)
```plaintext
first-name-last-name/
├── fr.yml
├── it.yml
├── es.yml
├── en.yml
├── de.yml
├── pt.yml
├── ja.yml
├── vi.yml
├── professor.yml
└── assets/
    └── profile.webp
```
- Ahora regresa a GitHub Desktop.
- En el lado izquierdo de tu ventana, deberías observar todas las modificaciones realizadas a los documentos, específicas de tu rama. Asegúrate de que estas modificaciones sean correctas:
![tutorial](assets/24.webp)
- Si las modificaciones te parecen correctas, agrega un título para tu commit. Un commit es un guardado de las modificaciones realizadas a la rama, acompañado por un mensaje descriptivo, que permite seguir la evolución de un proyecto a lo largo del tiempo.
- Una vez ingresado el título, presiona el botón azul `Commit to [your branch]` para validar estas modificaciones:
![tutorial](assets/25.webp)
- Luego haz clic en el botón `Push origin`. Esto enviará tu commit a tu fork:
![tutorial](assets/26.webp)
- Si has terminado tus modificaciones para esta rama, haz clic ahora en el botón `Preview Pull Request`:
![tutorial](assets/27.webp)
- Puedes verificar una última vez que tus modificaciones son correctas, luego haz clic en el botón `Create pull request`: ![tutorial](assets/28.webp) - Serás redirigido automáticamente a tu navegador en GitHub a la página de preparación de Pull Request. Un Pull Request es una solicitud para integrar los cambios de tu rama a la rama principal del repositorio de PlanB Network, lo que permite la revisión y discusión de los cambios antes de su fusión: ![tutorial](assets/29.webp)
- En esta página de preparación, indica un título que resuma brevemente las modificaciones que deseas fusionar con el repositorio fuente.
- Agrega un breve comentario describiendo estos cambios.
- Después de completar estos pasos, haz clic en el botón verde `Create pull request` para confirmar la solicitud de fusión: ![tutorial](assets/30.webp)
- Tu PR será entonces visible en la pestaña `Pull Request` del repositorio principal de PlanB Network. Todo lo que tienes que hacer ahora es esperar hasta que un administrador te contacte para confirmar la fusión de tu contribución o para solicitar cualquier modificación adicional: ![tutorial](assets/31.webp)
- Después de la fusión de tu PR con la rama principal, se recomienda eliminar tu rama de trabajo (`add-professor-your-name`) para mantener un historial limpio en tu bifurcación. GitHub te ofrecerá automáticamente esta opción en tu página de PR: ![tutorial](assets/32.webp)
- En el software GitHub Desktop, puedes volver a la rama principal de tu bifurcación (`dev`): ![tutorial](assets/8.webp)
- Si deseas hacer modificaciones a tu perfil después de haber enviado ya tu PR, el procedimiento depende del estado actual de tu PR:
	- Si tu PR todavía está abierto y no ha sido fusionado, realiza las modificaciones localmente mientras permaneces en la misma rama. Una vez finalizadas las modificaciones, utiliza el botón `Push origin` para añadir un nuevo commit a tu PR aún abierto;
	- En el caso de que tu PR ya haya sido fusionado con la rama principal, necesitarás comenzar el proceso de nuevo creando una nueva rama, luego enviando un nuevo PR. Asegúrate de que tu repositorio local esté sincronizado con el repositorio fuente de PlanB Network antes de proceder.
