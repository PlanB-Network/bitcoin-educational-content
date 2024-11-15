---
name: GitHub Desktop
description: Cómo configurar tu entorno de trabajo local?
---
![github](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos de primer nivel sobre Bitcoin en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, lo que permite a cualquier persona participar en enriquecer la plataforma. Las contribuciones pueden tomar varias formas: corregir y revisar textos existentes, traducir a otros idiomas, actualizar información o crear nuevos tutoriales aún no disponibles en nuestro sitio.

Si deseas contribuir a la Red PlanB, necesitarás usar GitHub para proponer cambios. Para hacer esto, tienes dos opciones:
- **Contribuir directamente a través de la interfaz web de GitHub**: Este es el método más simple. Si eres principiante o si planeas hacer solo unas pocas contribuciones menores, esta opción es probablemente la mejor para ti;
- **Contribuir localmente usando Git**: Este método es más adecuado si planeas hacer contribuciones regulares o significativas a la Red PlanB. Aunque configurar tu entorno local de Git en tu computadora puede parecer complejo al principio, este enfoque es más eficiente a largo plazo. Permite una gestión más flexible de los cambios. Si eres nuevo en esto, no te preocupes, **explicamos todo el proceso de configuración de tu entorno en este tutorial** (prometemos que no necesitarás escribir ninguna línea de comando ^^).

Si no tienes idea de qué es GitHub, o si quieres aprender más sobre los términos técnicos relacionados con Git y GitHub, te recomiendo leer nuestro artículo introductorio para familiarizarte con estos conceptos.

https://planb.network/tutorials/others/basics-of-github



- Para comenzar, obviamente necesitarás una cuenta de GitHub. Si ya tienes una, puedes iniciar sesión, de lo contrario, puedes usar nuestro tutorial para crear una nueva.

https://planb.network/tutorials/others/create-github-account



## Paso 1: Instalar GitHub Desktop

- Ve a https://desktop.github.com/ para descargar el software GitHub Desktop. Este software te permite interactuar fácilmente con GitHub, sin tener que usar un terminal:
![github-desktop](assets/1.webp)
- Cuando inicies el software por primera vez, se te pedirá que conectes tu cuenta de GitHub. Para hacerlo, haz clic en `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- Se abrirá una página de autenticación en tu navegador. Ingresa tu dirección de correo electrónico y la contraseña elegida al crear tu cuenta, luego haz clic en el botón `Sign in`:
![github-desktop](assets/3.webp)
- Haz clic en `Authorize desktop` para confirmar la conexión entre tu cuenta y el software:
![github-desktop](assets/4.webp)
- Serás redirigido automáticamente al software GitHub Desktop. Haz clic en `Finish`: ![github-desktop](assets/5.webp)
- Si acabas de crear tu cuenta de GitHub, serás redirigido a una página que indica que aún no has creado ningún repositorio. En este punto, deja de lado el software GitHub Desktop; volveremos a él más tarde: ![github-desktop](assets/6.webp)

## Paso 2: Instalar Obsidian

Pasemos a instalar el software de escritura. Aquí, tienes varias opciones. Necesitarás software que admita la edición de archivos Markdown, ya que la Red PlanB utiliza este formato para los archivos de texto en su repositorio.
Hay una multitud de software especializado en editar archivos Markdown, como Typora, diseñado específicamente para escribir. Aunque no es ideal, también es posible elegir un editor de código, como Visual Studio Code (VSC) o Sublime Text. Sin embargo, como escritor, prefiero usar el software Obsidian. Veamos juntos cómo instalarlo y comenzar a usarlo.
- Ve a https://obsidian.md/download y descarga el software: ![github-desktop](assets/7.webp)
- Instala Obsidian, lanza el software, elige tu idioma y luego haz clic en `Quick Start`: ![github-desktop](assets/8.webp)
- Llegarás al software Obsidian. Por ahora, no tienes archivos abiertos: ![github-desktop](assets/9.webp)

## Paso 3: Haz un Fork del repositorio de PlanB Network

- Ve al repositorio de datos de PlanB Network en la siguiente dirección: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Desde esta página, haz clic en el botón `Fork` en la parte superior derecha de la ventana: ![github-desktop](assets/11.webp)
- En el menú de creación, puedes dejar la configuración predeterminada. Asegúrate de que la casilla `Copy the dev branch only` esté marcada, luego haz clic en el botón `Create fork`: ![github-desktop](assets/12.webp)
- Luego llegarás a tu propio fork del repositorio de PlanB Network: ![github-desktop](assets/13.webp)
Este fork constituye un repositorio separado del original, aunque actualmente contiene los mismos datos. Ahora trabajarás en este nuevo repositorio.

De cierta manera, hemos hecho una copia del repositorio fuente de PlanB Network. Tu fork (la copia) y el repositorio original ahora evolucionarán independientemente uno del otro. En el repositorio original, otros colaboradores pueden agregar nuevos datos, mientras que tú, en tu fork, procederás con tus propias modificaciones.
Para mantener la consistencia entre estos dos repositorios, será necesario sincronizarlos periódicamente para que recuperen la misma información. Para enviar tus cambios al repositorio fuente, usarás lo que se llama una **Pull Request**. Y para integrar cambios del repositorio fuente en tu fork, usarás el comando **Sync fork** disponible en la interfaz web de GitHub.
![github-desktop](assets/14.webp)

## Paso 4: Clona el fork

- Regresa al software GitHub Desktop. Para este momento, tu fork debería aparecer en la sección `Your repositories`. Si no lo ves inmediatamente, usa el botón de doble flecha para actualizar la lista. Cuando tu fork aparezca, haz clic en él para seleccionarlo:
![github-desktop](assets/15.webp)
- Luego haz clic en el botón azul: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Mantén la ruta predeterminada. Para confirmar, haz clic en el botón azul `Clone`:
![github-desktop](assets/17.webp)
- Espera mientras GitHub Desktop clona tu fork localmente:
![github-desktop](assets/18.webp)
- Después de clonar el repositorio, el software te ofrece dos opciones. Debes seleccionar la primera: `To contribute to the parent project`. Esta elección te permitirá presentar tu trabajo futuro como una contribución al proyecto padre (`PlanB-Network/bitcoin-educational-content`), y no exclusivamente como una modificación de tu bifurcación personal (`[username]/bitcoin-educational-content`). Una vez elegida la opción, haz clic en `Continue`: ![github-desktop](assets/19.webp)
- Tu GitHub Desktop ahora está correctamente configurado. Ahora, puedes dejar el software abierto en segundo plano para seguir las modificaciones que haremos.
![github-desktop](assets/20.webp)
Lo que hemos logrado en esta etapa es la creación de una copia local de tu repositorio, que está alojado en GitHub. Como recordatorio, este repositorio es una bifurcación del repositorio fuente de PlanB Network. Podrás hacer modificaciones a esta copia local, como agregar tutoriales, traducciones o correcciones. Una vez hechas estas modificaciones, utilizarás el comando **Push origin** para enviar tus modificaciones locales a tu bifurcación alojada en GitHub.

También puedes recuperar modificaciones de la bifurcación, por ejemplo, durante una sincronización con el repositorio de PlanB Network. Para esto, utilizarás el comando **Fetch origin** para descargar las modificaciones a tu copia local (tu clon), y luego el comando **Pull origin** para fusionarlas con tu trabajo. Esto te permite mantenerte al día con los últimos desarrollos del proyecto mientras contribuyes de manera efectiva.

![github-desktop](assets/21.webp)
## Paso 5: Crear una nueva bóveda en Obsidian

- Abre el software Obsidian y haz clic en el pequeño icono de bóveda en la parte inferior izquierda de la ventana:
![github-desktop](assets/22.webp)
- Haz clic en el botón `Open` para abrir una carpeta existente como una bóveda: ![github-desktop](assets/23.webp)
- Tu explorador de archivos se abrirá. Necesitas localizar y seleccionar la carpeta titulada `GitHub`, que debería estar en tu directorio `Documents` entre tus archivos. Esta ruta corresponde a la que estableciste durante el paso 4. Después de elegir la carpeta, confirma su selección. La creación de tu bóveda en Obsidian se lanzará entonces en una nueva página del software:

![github-desktop](assets/24.webp)
-> **Atención**, es importante no elegir la carpeta `bitcoin-educational-content` al crear una nueva bóveda en Obsidian. En su lugar, selecciona la carpeta padre, `GitHub`. Si seleccionas la carpeta `bitcoin-educational-content`, la carpeta de configuración `.obsidian`, que contiene tus configuraciones locales de Obsidian, se integrará automáticamente en el repositorio. Queremos evitar esto, ya que no es necesario transferir tus configuraciones de Obsidian al repositorio de PlanB Network. Una alternativa es agregar la carpeta `.obsidian` al archivo `.gitignore`, pero este método también modificaría el archivo `.gitignore` del repositorio fuente, lo cual no es deseable.

- En el lado izquierdo de la ventana, puedes ver el árbol de archivos con tus diferentes repositorios de GitHub que han sido clonados localmente.
- Al hacer clic en las flechas junto a los nombres de las carpetas, puedes expandirlas para acceder a las subcarpetas de los repositorios y sus documentos:
![github-desktop](assets/25.webp)
- No olvides configurar Obsidian en modo oscuro: "La luz atrae a los insectos" ;)

## Paso 6: Instalar un Editor de Código
La mayoría de tus modificaciones serán en archivos en formato Markdown (`.md`). Para editar estos documentos, puedes usar Obsidian, el software del que hablamos anteriormente. Sin embargo, PlanB Network utiliza otros formatos de archivo, y necesitarás modificar algunos de ellos.
Por ejemplo, al crear un nuevo tutorial, necesitarás crear un archivo YAML (`.yml`) para ingresar las etiquetas de tu tutorial, su título y tu ID de profesor. Obsidian no ofrece la posibilidad de modificar este tipo de archivos, por lo que necesitarás un editor de código.

Para esto, tienes varias opciones disponibles. Aunque el bloc de notas estándar de tu computadora puede ser utilizado para estas modificaciones, esta solución no es ideal para un trabajo pulcro. Recomiendo elegir un software específicamente diseñado para este propósito, como [VS Code](https://code.visualstudio.com/download) o [Sublime Text](https://www.sublimetext.com/download). Sublime Text, al ser particularmente ligero, será más que suficiente para nuestras necesidades.
- Instala uno de estos programas de software, y mantenlo a un lado para tus futuras modificaciones. ![github-desktop](assets/26.webp)
¡Felicidades! Tu entorno de trabajo ahora está configurado para contribuir a PlanB Network. Ahora puedes explorar nuestros otros tutoriales específicos para cada tipo de contribución (traducción, corrección de pruebas, escritura.

https://planb.network/tutorials/others

..).
