---
name: Añadiendo un Constructor
description: ¿Cómo proponer la adición de un nuevo constructor en la Red PlanB?
---
![constructor](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos de primera categoría sobre Bitcoin, en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, lo que permite a cualquier persona participar en enriquecer la plataforma.

¿Quieres añadir un nuevo "constructor" de Bitcoin al sitio de la Red PlanB y dar visibilidad a tu empresa o software, pero no sabes cómo? ¡Este tutorial es para ti!
![constructor](assets/01.webp)
- Primero, necesitas tener una cuenta de GitHub. Si no sabes cómo crear una cuenta, hemos hecho un tutorial detallado para guiarte.

https://planb.network/tutorials/others/create-github-account


- Ve al [repositorio de GitHub de PlanB dedicado a datos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) en la sección `resources/builder/`:
![constructor](assets/02.webp)
- Haz clic en la parte superior derecha en el botón `Add file`, luego en `Create new file`:
![constructor](assets/03.webp)
- Si nunca has contribuido al contenido de la Red PlanB antes, necesitarás crear tu fork del repositorio original. Hacer un fork de un repositorio significa crear una copia de ese repositorio en tu propia cuenta de GitHub, lo que te permite trabajar en el proyecto sin afectar el repositorio original. Haz clic en el botón `Fork this repository`:
![constructor](assets/04.webp)
- Luego llegarás a la página de edición de GitHub:
![constructor](assets/05.webp)
- Crea una carpeta para tu empresa. Para hacerlo, en el cuadro `Name your file...`, escribe el nombre de tu empresa en minúsculas con guiones en lugar de espacios. Por ejemplo, si tu empresa se llama "Bitcoin Baguette", deberías escribir `bitcoin-baguette`:
![constructor](assets/06.webp)
- Para validar la creación de la carpeta, simplemente añade una barra inclinada después de tu nombre en el mismo cuadro, por ejemplo: `bitcoin-baguette/`. Añadir una barra inclinada crea automáticamente una carpeta en lugar de un archivo:
![constructor](assets/07.webp)
- En esta carpeta, crearás un primer archivo YAML llamado `builder.yml`:
![constructor](assets/08.webp)
- Llena este archivo con información sobre tu empresa usando esta plantilla:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Aquí está lo que debes llenar para cada clave:
- `name`: El nombre de tu empresa (obligatorio);
- `address` : La ubicación de tu negocio (opcional);
- `language` : Los países en los que opera tu negocio o los idiomas que soporta (opcional);
- `links` : Los diversos enlaces oficiales de tu negocio (opcional);
- `tags` : 2 términos que califiquen tu negocio (obligatorio);
- `category` : La categoría que mejor describe el campo en el que opera tu negocio entre las siguientes opciones:
	- `wallet` (cartera),
	- `infrastructure` (infraestructura),
	- `exchange` (intercambio),
	- `education` (educación),
	- `service` (servicio),
	- `communities` (comunidades),
	- `conference` (conferencia),
	- `privacy` (privacidad),
	- `investment` (inversión),
	- `node` (nodo),
	- `mining` (minería),
	- `news` (noticias),
	- `manufacturer` (fabricante).
Por ejemplo, tu archivo YAML podría lucir así:
```yaml
name: Bitcoin Baguette

address_line_1: París, Francia
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - educación

category: educación
```

![constructor](assets/09.webp)
- Una vez que hayas terminado de hacer cambios en este archivo, guárdalos haciendo clic en el botón `Commit changes...`:
![constructor](assets/10.webp)
- Agrega un título para tus cambios, junto con una breve description:
![constructor](assets/11.webp)
- Haz clic en el botón verde `Propose changes`:
![constructor](assets/12.webp)
- Luego llegarás a una página que resume todos tus cambios:
![constructor](assets/13.webp)
- Haz clic en la foto de tu perfil de GitHub en la parte superior derecha, luego en `Your Repositories`:
![constructor](assets/14.webp)
- Selecciona tu fork del repositorio de PlanB Network:
![constructor](assets/15.webp)
- Deberías ver una notificación en la parte superior de la ventana con tu nueva rama. Probablemente se llame `patch-1`. Haz clic en ella:
![constructor](assets/16.webp)
- Ahora estás en tu rama de trabajo (**¡asegúrate de estar en la misma rama que tus modificaciones anteriores, esto es importante!**):
![constructor](assets/17.webp)
- Regresa a la carpeta `resources/builders/` y selecciona la carpeta de tu negocio que acabas de crear en el commit anterior:
![constructor](assets/18.webp)
- En la carpeta de tu negocio, haz clic en el botón `Add file`, luego en `Create new file`:
![constructor](assets/19.webp)
- Nombra esta nueva carpeta `assets` y confirma su creación colocando una barra `/` al final:
![constructor](assets/20.webp)
- En esta carpeta `assets`, crea un archivo llamado `.gitkeep`:
![constructor](assets/21.webp)
- Haz clic en el botón `Commit changes...`:
![constructor](assets/22.webp)
- Deja el título del commit como predeterminado, y asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`: ![constructor](assets/23.webp)
- Regresa a la carpeta `assets`:
![constructor](assets/24.webp)
- Haz clic en el botón `Add file`, luego en `Upload files`:
![constructor](assets/25.webp)
- Se abrirá una nueva página. Arrastra y suelta una imagen de tu empresa o tu software en el área. Esta imagen se mostrará en el sitio de PlanB Network:
![constructor](assets/26.webp)
- Puede ser el logo o un ícono:
![constructor](assets/27.webp)
- Una vez que la imagen esté cargada, verifica que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`:
![constructor](assets/28.webp)
- Ten cuidado, tu imagen debe ser cuadrada, debe llamarse `logo`, y debe estar en formato `.webp`. Por lo tanto, el nombre completo del archivo debería ser: `logo.webp`:
![constructor](assets/29.webp)
- Regresa a tu carpeta `assets` y haz clic en el archivo intermedio `.gitkeep`:
![builder](assets/30.webp)- Una vez en el archivo, haz clic en los tres puntos pequeños en la parte superior derecha y luego en `Delete file` (Eliminar archivo):
![builder](assets/31.webp)
- Verifica que todavía estés en la misma rama de trabajo, luego haz clic en el botón `Commit changes` (Confirmar cambios):
![builder](assets/32.webp)
- Agrega un título y una descripción a tu confirmación, luego haz clic en `Commit changes` (Confirmar cambios):
![builder](assets/33.webp)
- Regresa a la carpeta de tu empresa:
![builder](assets/34.webp)
- Haz clic en el botón `Add file` (Agregar archivo), luego en `Create new file` (Crear nuevo archivo):
![builder](assets/35.webp)
- Crea un nuevo archivo YAML nombrándolo con el indicador de tu idioma nativo. Este archivo se utilizará para la descripción del constructor. Por ejemplo, si quiero escribir mi descripción en inglés, nombraré este archivo `en.yml`:
![builder](assets/36.webp)
- Llena este archivo YAML usando esta plantilla:
```yaml
description: |
 
contributors:
 - 
```

- Para la clave `contributors`, puedes agregar tu identificador de colaborador en PlanB Network si tienes uno. Si no lo tienes, deja este campo vacío.
- Para la clave `description`, simplemente necesitas agregar un párrafo corto que describa tu empresa o tu software. La descripción debe estar en el mismo idioma que el nombre del archivo. No es necesario traducir esta descripción a todos los idiomas soportados en el sitio, ya que los equipos de PlanB lo harán utilizando su modelo. Por ejemplo, así es como podría lucir tu archivo:
```yaml
description: |
Fundada en 2017, Bitcoin Baguette es una asociación con sede en París dedicada a organizar encuentros de Bitcoin y talleres técnicos. Reunimos a entusiastas, expertos y mentes curiosas para explorar y discutir las complejidades de la tecnología Bitcoin. Nuestros eventos proporcionan una plataforma para compartir conocimientos, hacer networking y fomentar una comprensión más profunda de los mecanismos internos de Bitcoin. Únete a nosotros en Bitcoin Baguette para ser parte de la comunidad Bitcoin de París y mantenerte actualizado con los últimos avances en el campo.

contributors:
- 
```
![builder](assets/37.webp)
- Haz clic en el botón `Commit changes` (Confirmar cambios):
![builder](assets/38.webp)
- Asegúrate de que la casilla `Commit directly to the patch-1 branch` (Confirmar directamente en la rama patch-1) esté marcada, agrega un título, luego haz clic en `Commit changes` (Confirmar cambios):
![builder](assets/39.webp)
- La carpeta de tu empresa debería verse ahora así:
![builder](assets/40.webp)
- Si todo es de tu satisfacción, regresa a la raíz de tu bifurcación:
![builder](assets/41.webp)
- Deberías ver un mensaje indicando que tu rama ha sufrido cambios. Haz clic en el botón `Compare & pull request` (Comparar y crear solicitud de extracción):
![builder](assets/42.webp)
- Agrega un título claro y una descripción a tu PR:
![builder](assets/43.webp)
- Haz clic en el botón `Create pull request` (Crear solicitud de extracción):
![builder](assets/44.webp)
¡Felicidades! Tu PR ha sido creado con éxito. Un administrador lo revisará ahora y, si todo está en orden, lo integrará al repositorio principal de PlanB Network. Deberías ver tu perfil de constructor aparecer en el sitio web unos días después.

Asegúrate de seguir el progreso de tu PR. Un administrador puede dejar un comentario solicitando información adicional. Mientras tu PR no esté validado, puedes consultarlo en la pestaña `Pull requests` en el repositorio de GitHub de PlanB Network:
![builder](assets/45.webp)
¡Muchas gracias por tu valiosa contribución! :)
