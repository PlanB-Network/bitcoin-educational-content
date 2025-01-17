---
name: Añadiendo Herramientas Educativas
description: ¿Cómo añadir nuevos materiales educativos en PlanB Network?
---
![event](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos líderes sobre Bitcoin, en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, lo que permite a cualquier persona participar en enriquecer la plataforma.

Más allá de tutoriales y formación, PlanB Network también ofrece una vasta biblioteca de contenido educativo variado sobre Bitcoin, accesible para todos, [en la sección "BET" (_Bitcoin Educational Toolkit_) ](https://planb.network/resources/bet). Esta base de datos incluye pósters educativos, memes, pósters de propaganda humorística, diagramas técnicos, logos y otras herramientas para los usuarios. El objetivo de esta iniciativa es apoyar a individuos y comunidades que enseñan Bitcoin alrededor del mundo proporcionándoles los recursos visuales necesarios.

¿Quieres participar en enriquecer esta base de datos, pero no sabes cómo? ¡Este tutorial es para ti!

*Es imperativo que todo el contenido integrado en el sitio esté libre de derechos o respete la licencia del archivo fuente. Además, todos los visuales publicados en PlanB Network están disponibles bajo la licencia [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*
![event](assets/01.webp)
- Primero, necesitas tener una cuenta en GitHub. Si no sabes cómo crear una cuenta, hemos hecho un tutorial detallado para guiarte.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Ve al [repositorio de GitHub de PlanB dedicado a datos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) en la sección `resources/bet/`:
![event](assets/02.webp)
- Haz clic en la parte superior derecha en el botón `Add file`, luego en `Create new file`:
![event](assets/03.webp)
- Si nunca has contribuido con los contenidos de PlanB Network antes, necesitarás crear tu fork del repositorio original. Hacer un fork de un repositorio significa crear una copia de ese repositorio en tu propia cuenta de GitHub, lo que te permite trabajar en el proyecto sin afectar el repositorio original. Haz clic en el botón `Fork this repository`:
![event](assets/04.webp)
- Entonces llegarás a la página de edición de GitHub:
![event](assets/05.webp)
- Crea una carpeta para tu contenido. Para hacerlo, en el cuadro `Name your file...`, escribe el nombre de tu contenido en minúsculas con guiones en lugar de espacios. En mi ejemplo, digamos que quiero añadir un visual PDF de la lista de palabras BIP39 de 2048 palabras. Entonces, llamaré a mi carpeta `bip39-wordlist`: ![event](assets/06.webp)
- Para confirmar la creación de la carpeta, simplemente añade una barra inclinada después del nombre en el mismo cuadro, por ejemplo: `bip39-wordlist/`. Añadir una barra inclinada crea automáticamente una carpeta en lugar de un archivo:
![event](assets/07.webp)
- En esta carpeta, crearás un primer archivo YAML llamado `bet.yml`:
![event](assets/08.webp)
- Llena este archivo con información relacionada con tu contenido usando esta plantilla:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`builder`**: Indica el identificador de tu organización en la Red PlanB. Si aún no tienes un identificador de "constructor" para tu empresa, puedes crear uno siguiendo este tutorial.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Si no tienes uno, puedes simplemente usar tu nombre, tu pseudónimo o el nombre de tu empresa sin haber creado un perfil de constructor.
- **`type`**: Selecciona la naturaleza de tu contenido entre las siguientes dos opciones:
	- `Educational Content` para contenidos educativos.
	- `Visual Content` para otros tipos de contenidos diversos.

- **`links`**: Proporciona enlaces a tus contenidos. Tienes dos opciones:
	- Si eliges alojar tu contenido directamente en el GitHub de PlanB, necesitarás añadir los enlaces a este archivo durante los siguientes pasos.
	- Si tus contenidos están alojados en otro lugar, como en tu sitio web personal, indica los enlaces correspondientes aquí:
	    - `download`: Un enlace para descargar tu contenido.
	    - `view`: Un enlace para ver tu contenido (puede ser el mismo que el enlace de descarga). Si tu contenido está disponible en varios idiomas, añade un enlace para cada idioma.

- **`tags`**: Añade dos etiquetas asociadas con tu contenido. Ejemplos:
	- bitcoin
	- tecnología
	- economía
	- educación
	- meme...

- **`contributors`**: Menciona tu identificador de colaborador si tienes uno.

Por ejemplo, tu archivo YAML podría verse así:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- En mi ejemplo, dejaré los enlaces vacíos por ahora, ya que añadiré mi PDF directamente en GitHub:
![event](assets/09.webp)
- Una vez que tus modificaciones a este archivo estén completas, guárdalas haciendo clic en el botón `Commit changes...`:
![event](assets/10.webp)
- Añade un título para tus modificaciones, así como una breve description:
![event](assets/11.webp)
- Haz clic en el botón verde `Propose changes`:
![event](assets/12.webp)
- Luego llegarás a una página que resume todos tus cambios:
![event](assets/13.webp)
- Haz clic en tu foto de perfil de GitHub en la parte superior derecha, luego en `Your Repositories`:
![event](assets/14.webp)
- Selecciona tu fork del repositorio de la Red PlanB:
![event](assets/15.webp)
- Deberías ver una notificación en la parte superior de la ventana con tu nueva rama. Probablemente se llame `patch-1`. Haz clic en ella:
![event](assets/16.webp)
- Ahora estás en tu rama de trabajo (**¡asegúrate de estar en la misma rama que tus modificaciones anteriores, esto es importante!**):
![event](assets/17.webp)
- Regresa a la carpeta `resources/bet/` y selecciona la carpeta de tu contenido que acabas de crear en el commit anterior:
![event](assets/18.webp)
- En la carpeta de tu contenido, haz clic en el botón `Add file`, luego en `Create new file`:
![event](assets/19.webp)
- Nombra esta nueva carpeta `assets` y confirma su creación poniendo una barra `/` al final:
![event](assets/20.webp)
- En esta carpeta `assets`, crea un archivo llamado `.gitkeep`: ![event](assets/21.webp)
- Haz clic en el botón `Commit changes...`: ![evento](assets/22.webp)- Deja el título del commit por defecto y asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`: ![evento](assets/23.webp)
- Regresa a la carpeta `assets`: ![evento](assets/24.webp)
- Haz clic en el botón `Add file`, luego en `Upload files`: ![evento](assets/25.webp)
- Se abrirá una nueva página. Arrastra y suelta una miniatura que represente tu contenido en el área. Esta imagen se mostrará en el sitio de PlanB Network: ![evento](assets/26.webp)
- Puede ser una vista previa, un logo o un icono: ![evento](assets/27.webp)
- Una vez que la imagen esté subida, asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`: ![evento](assets/28.webp)
- Ten cuidado, tu imagen debe llamarse `logo` y debe estar en formato `.webp`. Por lo tanto, el nombre completo del archivo debe ser: `logo.webp`: ![evento](assets/29.webp)
- Regresa a tu carpeta `assets` y haz clic en el archivo intermedio `.gitkeep`: ![evento](assets/30.webp)
- Una vez en el archivo, haz clic en los tres pequeños puntos en la parte superior derecha y luego en `Delete file`: ![evento](assets/31.webp)
- Asegúrate de seguir en la misma rama de trabajo, luego haz clic en el botón `Commit changes`: ![evento](assets/32.webp)
- Agrega un título y una descripción a tu commit, luego haz clic en `Commit changes`: ![evento](assets/33.webp)
- Regresa a la carpeta de tu contenido: ![evento](assets/34.webp)
- Haz clic en el botón `Add file`, luego en `Create new file`: ![evento](assets/35.webp)
- Crea un nuevo archivo YAML nombrándolo con el indicador de tu lengua materna. Este archivo se utilizará para la descripción del contenido. Por ejemplo, si quiero escribir mi descripción en inglés, nombraré este archivo `en.yml`: ![evento](assets/36.webp)
- Rellena este archivo YAML usando esta plantilla:

```yaml
name: 
description: |
  
```

- Para la clave `name`, puedes agregar el nombre de tu contenido;
- Para la clave `description`, simplemente necesitas agregar un párrafo corto que describa tu contenido. La descripción debe estar en el mismo idioma que el nombre del archivo. No necesitas traducir esta descripción a todos los idiomas soportados en el sitio, ya que los equipos de PlanB lo harán con su modelo.
Por ejemplo, así es como podría lucir tu archivo:

```yaml
name: BIP39 WORDLIST
description: |
  Lista completa y numerada de las 2048 palabras en inglés del diccionario BIP39 utilizadas para codificar frases mnemotécnicas. El documento se puede imprimir en una sola página.
```

![evento](assets/37.webp)
- Haz clic en el botón `Commit changes...`:
![evento](assets/38.webp)
- Asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, agrega un título, luego haz clic en `Commit changes`:
![evento](assets/39.webp)
- La carpeta de tu contenido ahora debería lucir así:
![evento](assets/40.webp)
*Si prefieres no añadir el contenido en GitHub y ya has anotado los enlaces en el archivo `bet.yml` durante los pasos anteriores, puedes saltarte esta sección e ir directamente a la parte que concierne la creación del Pull Request.*
- Regresa a la carpeta `/assets`:
![evento](assets/41.webp)
- Haz clic en el botón `Add file`, luego en `Upload files`:
![evento](assets/42.webp)
- Se abrirá una nueva página. Arrastra y suelta en el área el contenido que deseas compartir:
![evento](assets/43.webp)
- Por ejemplo, yo añadí el archivo PDF de la lista BIP39:
![evento](assets/44.webp)
- Una vez que el contenido esté subido, asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`:
![evento](assets/45.webp)
- Regresa a tu carpeta `/assets` y haz clic en el archivo que acabas de subir:
![evento](assets/46.webp)
- Recupera la URL intermedia de tu archivo. Por ejemplo, en mi caso, la URL es:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Conserva solo la última parte de la URL desde `/resources` en adelante:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Añade a la base de la URL la siguiente información para tener el enlace correcto:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Lo que estamos haciendo aquí es anticipar el enlace futuro a tu archivo, una vez que tu propuesta haya sido fusionada en el repositorio fuente de la Red PlanB.
- Regresa a tu archivo `bet.yml` y haz clic en el icono de lápiz: ![evento](assets/47.webp)
- Añade tu enlace ahí:
![evento](assets/48.webp)
- Una vez que tus cambios estén completos, haz clic en el botón `Commit changes...`:
![evento](assets/49.webp)
- Añade un título para tus cambios, así como una breve description:
![evento](assets/50.webp)
- Haz clic en el botón verde `Commit changes`:
![evento](assets/51.webp)

---

- Si todo te parece correcto, regresa a la raíz de tu bifurcación:
![evento](assets/52.webp)
- Deberías ver un mensaje indicando que tu rama ha sido modificada. Haz clic en el botón `Compare & pull request`:
![evento](assets/53.webp)
- Añade un título claro y una descripción para tu PR:
![evento](assets/54.webp)
- Haz clic en el botón `Create pull request`:
![evento](assets/55.webp)
¡Felicidades! Tu PR ha sido creado con éxito. Un administrador lo revisará ahora y, si todo está en orden, lo fusionará en el repositorio principal de la Red PlanB. Deberías ver tu BET aparecer en el sitio web unos días después.

Asegúrate de seguir el progreso de tu PR. Un administrador puede dejar un comentario pidiendo información adicional. Mientras tu PR no esté validado, puedes consultarlo en la pestaña de Pull requests en el repositorio de GitHub de la Red PlanB:
![evento](assets/56.webp)
¡Muchas gracias por tu valiosa contribución! :)
