---
name: Añadir un Podcast a la Red PlanB
description: ¿Cómo añadir un nuevo podcast a la Red PlanB?
---
![podcast](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos de primera categoría sobre Bitcoin en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, permitiendo a cualquiera participar en enriquecer la plataforma.

¿Estás buscando añadir un podcast sobre Bitcoin al sitio de la Red PlanB y aumentar la visibilidad de tu programa, pero no sabes cómo? ¡Este tutorial es para ti!
![podcast](assets/01.webp)
- Primero, necesitas tener una cuenta de GitHub. Si no sabes cómo crear una, hemos hecho un tutorial detallado para guiarte.

https://planb.network/tutorials/others/create-github-account


- Ve al [repositorio de GitHub de PlanB dedicado a datos](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) en la sección `resources/podcasts/`:
![podcast](assets/02.webp)
- Haz clic en la parte superior derecha en el botón `Add file`, luego en `Create new file`:
![podcast](assets/03.webp)
- Si nunca has contribuido al contenido de la Red PlanB antes, necesitarás crear tu fork del repositorio original. Hacer un fork de un repositorio significa crear una copia de ese repositorio en tu propia cuenta de GitHub, lo que te permite trabajar en el proyecto sin afectar el repositorio original. Haz clic en el botón `Fork this repository`:
![podcast](assets/04.webp)
- Luego llegarás a la página de edición de GitHub:
![podcast](assets/05.webp)
- Crea una carpeta para tu podcast. Para hacerlo, en el cuadro `Name your file...`, escribe el nombre de tu podcast en minúsculas con guiones en lugar de espacios. Por ejemplo, si tu programa se llama "Super Podcast Bitcoin", deberías escribir `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Para validar la creación de la carpeta, simplemente añade una barra inclinada después del nombre de tu podcast en el mismo cuadro, por ejemplo: `super-podcast-bitcoin/`. Añadir una barra inclinada crea automáticamente una carpeta en lugar de un archivo:
![podcast](assets/07.webp)
- En esta carpeta, crearás un primer archivo YAML llamado `podcast.yml`:
![podcast](assets/08.webp)
- Llena este archivo con información sobre tu podcast usando esta plantilla:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Aquí están los detalles a completar para cada campo:

- **`name`**: Indica el nombre de tu podcast.
- **`host`**: Lista los nombres o pseudónimos de los locutores o el anfitrión del podcast. Cada nombre debe estar separado por una coma.
- **`language`**: Indica el código de idioma del idioma hablado en tu podcast. Por ejemplo, para inglés, anota `en`, para italiano `it`...

- **`links`**: Proporciona enlaces a tu contenido. Tienes dos opciones:
	- `podcast`: el enlace a tu podcast,
	- `twitter`: el enlace al perfil de Twitter del podcast o la organización que lo produce,
	- `website`: el enlace al sitio web del podcast o la organización que lo produce.
- **`description`**: Añade un breve párrafo que describa tu podcast. La descripción debe estar en el mismo idioma indicado en el campo `language:`.
- **`tags`**: Añade dos etiquetas asociadas con tu podcast. Ejemplos:
    - `bitcoin`
    - `tecnología`
    - `economía`
    - `educación`...

- **`contributors`**: Menciona tu ID de colaborador si tienes uno.

Por ejemplo, tu archivo YAML podría lucir así:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin es una sesión técnica EN VIVO realizada una vez a la semana en Twitter para profundizar en el protocolo de Bitcoin, soluciones de segunda capa y todo lo que asombre. Nuestros anfitriones Lounes, Pantamis, Loïc y Sosthene responderán tus preguntas y ofrecerán el show más técnico sobre Bitcoin en el mundo.

tags:
  - bitcoin
  - tecnología
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Una vez que hayas terminado de hacer cambios en este archivo, guárdalos haciendo clic en el botón `Commit changes...`:
![podcast](assets/10.webp)
- Añade un título para tus cambios, así como una breve description:
![podcast](assets/11.webp)
- Haz clic en el botón verde `Propose changes`:
![podcast](assets/12.webp)
- Luego llegarás a una página que resume todos tus cambios:
![podcast](assets/13.webp)
- Haz clic en tu foto de perfil de GitHub en la parte superior derecha, luego en `Your Repositories`:
![podcast](assets/14.webp)
- Selecciona tu fork del repositorio de PlanB Network:
![podcast](assets/15.webp)
- Deberías ver una notificación en la parte superior de la ventana con tu nueva rama. Probablemente se llame `patch-1`. Haz clic en ella:
![podcast](assets/16.webp)
- Ahora estás en tu rama de trabajo:
![podcast](assets/17.webp)
- Regresa a la carpeta `resources/podcast/` y selecciona la carpeta del podcast que acabas de crear en el commit anterior: ![podcast](assets/18.webp)
- En tu carpeta del podcast, haz clic en el botón `Add file`, luego en `Create new file`:
![podcast](assets/19.webp)
- Nombra esta nueva carpeta `assets` y confirma su creación añadiendo una barra `/` al final:
![podcast](assets/20.webp)
- En esta carpeta `assets`, crea un archivo llamado `.gitkeep`:
![podcast](assets/21.webp)
- Haz clic en el botón `Commit changes...`:
![podcast](assets/22.webp)
- Deja el título del commit como predeterminado, y asegúrate de que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`:
![podcast](assets/23.webp)
- Regresa a la carpeta `assets`:
![podcast](assets/24.webp)
- Haz clic en el botón `Add file`, luego en `Upload files`:
![podcast](assets/25.webp)
- Se abrirá una nueva página. Arrastra y suelta el logo de tu podcast en el área. Esta imagen se mostrará en el sitio de PlanB Network: ![podcast](assets/26.webp)
- Ten cuidado, la imagen debe ser cuadrada, para ajustarse mejor a nuestro sitio web:
![podcast](assets/27.webp)
- Una vez que la imagen esté cargada, verifica que la casilla `Commit directly to the patch-1 branch` esté marcada, luego haz clic en `Commit changes`:
![podcast](assets/28.webp)
- Ten cuidado, tu imagen debe llamarse `logo` y debe estar en formato `.webp`. Por lo tanto, el nombre completo del archivo debe ser: `logo.webp`:
![podcast](assets/29.webp)
- Regresa a tu carpeta `assets` y haz clic en el archivo intermedio `.gitkeep`:
![podcast](assets/30.webp)
- Una vez en el archivo, haz clic en los tres pequeños puntos en la parte superior derecha y luego en `Delete file`:
![podcast](assets/31.webp)
- Verifica que todavía estés en la misma rama de trabajo, luego haz clic en el botón `Commit changes`:
![podcast](assets/32.webp)
- Agrega un título y descripción a tu commit, luego haz clic en `Commit changes`:
![podcast](assets/33.webp)
- Regresa a la raíz de tu repositorio:
![podcast](assets/34.webp)
- Deberías ver un mensaje indicando que tu rama ha sufrido cambios. Haz clic en el botón `Compare & pull request`:
![podcast](assets/35.webp)
- Agrega un título claro y descripción a tu PR:
![podcast](assets/36.webp)
- Haz clic en el botón `Create pull request`:
![podcast](assets/37.webp)
¡Felicidades! Tu PR ha sido creado exitosamente. Un administrador lo revisará ahora y, si todo está en orden, lo fusionará en el repositorio principal de PlanB Network. Deberías ver tu podcast aparecer en el sitio web unos días después.

Por favor, asegúrate de seguir el progreso de tu PR. Un administrador puede dejar un comentario solicitando información adicional. Mientras tu PR no esté validado, puedes verlo en la pestaña `Pull requests` en el repositorio de GitHub de PlanB Network:
![podcast](assets/38.webp)
¡Muchas gracias por tu valiosa contribución! :)
