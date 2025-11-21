---
name: Weblate - Traducir elementos estáticos
description: ¿Cómo puedes participar en la traducción de los elementos estáticos de planb.network?
---
![cover](assets/cover.webp)

La misión de Plan ₿ Academy es proporcionar recursos educativos de primera clase sobre Bitcoin y traducirlos al mayor número de idiomas posible. Gran parte del contenido publicado en el sitio es de código abierto y está alojado en GitHub, lo que permite a cualquiera participar en el enriquecimiento de la plataforma. Las contribuciones pueden adoptar diversas formas: corregir y corregir el contenido existente, actualizar la información o crear nuevos tutoriales para añadir a la plataforma.

En este tutorial, te mostraremos cómo contribuir fácilmente a la traducción de los elementos estáticos de nuestro sitio web. Los datos de la plataforma se dividen en dos categorías principales:

- Los datos/elementos estáticos del frontend (páginas, botones, etc.);
- El contenido educativo (tutoriales, cursos, recursos...).

Para traducir los contenidos educativos, utilizamos [inteligencia artificial](https://github.com/Asi0Flammeus/LLM-Translator). Luego, para corregir los eventuales errores de estos archivos, invitamos a los correctores a contribuir. Si deseas corregir algún contenido, consulta el siguiente tutorial:

https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017
Por otro lado, si estás interesado en traducir los elementos estáticos del sitio web (excluidos los contenidos educativos), ¡Estás en el lugar adecuado! Para traducir eficazmente el frontend, utilizamos la herramienta Weblate, que es muy sencilla de utilizar y facilita el planteamiento de la traducción.

Si deseas añadir un idioma completamente nuevo a Plan ₿ Academy, asegúrate de ponerte en contacto con el equipo de Plan ₿ Academy a través de nuestro [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder). Si no tienes telegram, puedes enviar un correo electrónico a mari@planb.network. Asegúrate de escribir una pequeña presentación sobre quién eres y los idiomas que hablas.

Los miembros de nuestro equipo te darán instrucciones específicas y abrirán los "issues" correspondientes en Github para coordinar tu trabajo.

Antes de seguir, checa este tutorial específico para añadir un nuevo idioma al Weblate.

https://planb.academy/tutorials/contribution/content/weblate-add-new-language-eef2f5c0-1aba-48a3-b8f0-a57feb761d86
Cuando estés listo para empezar a traducir, vuelve a este tutorial y repasa los siguientes puntos.

## Registrarse en Weblate

- Ve a [el Weblate autoalojado de Plan ₿ Academy](https://weblate.planb.network/):

![weblate](assets/01.webp)

- Si ya tienes una cuenta Weblate, haz clic en `Iniciar sesión`:

![weblate](assets/02.webp)

- Si no tienes una cuenta, haz clic en `Registrarse`:

![weblate](assets/03.webp)

- Introduce tu dirección de correo electrónico, así como un nombre de usuario y un nombre completo (puedes utilizar un seudónimo) y, a continuación, haz clic en `Registrarse`:

![weblate](assets/04.webp)

- En la bandeja de entrada de tu correo electrónico, deberías haber recibido un mensaje de confirmación de Weblate. Haz clic en el enlace para confirmar tu inscripción:

![weblate](assets/05.webp)

- Elige una contraseña segura y haz clic en "Cambiar mi contraseña":

![weblate](assets/06.webp)

- Ahora puedes volver al panel de Plan ₿ Academy:

![weblate](assets/07.webp)

## Empezar a traducir

- Haz clic en el proyecto "Elementos del sitio web" (no en el glosario):

![weblate](assets/08.webp)

- Accederás a una interfaz en la que podrás ver los idiomas en curso:

![weblate](assets/09.webp)

- Elige tu idioma. Por ejemplo, el francés:

![weblate](assets/10.webp)

- Para empezar a traducir, basta con hacer clic en el botón `Traducir`:

![weblate](assets/11.webp)

- Se te redirigirá a la interfaz de trabajo:

![weblate](assets/12.webp)

- A continuación, Weblate te sugerirá automáticamente frases, párrafos o incluso palabras para traducir en la casilla `idioma`. En tu caso, probablemente verás la cadena principal en inglés, y otro cuadro de texto para tu idioma:

![weblate](assets/13.webp)

- Tu tarea consiste en traducir las cadenas indicadas. Debes introducir tu texto en la casilla correspondiente al idioma que hayas elegido. Por ejemplo, si estás trabajando en la versión francesa, escribe tu traducción en la casilla `Francés`:

![weblate](assets/14.webp)

- Haz clic en la pestaña `Sugerencia automática`:

![weblate](assets/15.webp)

- Aquí, Weblate te muestra una traducción realizada por inteligencia artificial:

![weblate](assets/16.webp)

- Si la traducción sugerida te parece relevante, puedes hacer clic en el botón `Clonar en traducción`:

![weblate](assets/17.webp)

- La sugerencia se coloca ahora en tu buzón de trabajo:

![weblate](assets/18.webp)

- A continuación, puedes modificar manualmente la sugerencia:

![weblate](assets/19.webp)

- Cuando la traducción te parezca satisfactoria, pulsa el botón `Guardar y continuar`. Asegúrate de desmarcar la casilla "Necesita edición" cuando estés seguro de tu traducción:

![weblate](assets/20.webp)

- Ya está, tu traducción se ha guardado correctamente. Weblate te redirigirá automáticamente al siguiente elemento a traducir. Si vuelves al panel correspondiente a tu idioma, podrás ver que cada tipo de cadena tiene un estado de traducción diferente. Por ejemplo, si necesitas centrarte sólo en las "cadenas sin traducir", puedes hacer clic en la pestaña específica:

![weblate](assets/21.webp)

- Si necesitas buscar una palabra concreta, ya sea en tu idioma o en el original, haz clic en "buscar" e introdúcela allí:

![weblate](assets/22.webp)

## Pautas de traducción

- Cuando encuentres palabras insertadas dentro de llaves "{", no es necesario que las traduzcas. Por ejemplo, en "Your account has been created, {{userName}}!", traducirás toda la frase, pero mantendrás "userName" en inglés.
- Cuando encuentres "Plan ₿ Academy" en una cadena, asegúrate de NO traducir la palabra "network" (considera Plan ₿ Academy como una marca registrada). Además, ¡utiliza siempre la ₿ de Bitcoin!
- Si en su lugar, encuentras la palabra "network" sola, puedes traducirla.
- No traduzcas "B-CERT", ya que es otra palabra fija.
- Si encuentras cadenas que terminan con un espacio, puedes dejarlo.
- Algunas cadenas pueden contener un espacio entre la última palabra y un signo de puntuación: no lo dejes en la lengua de destino a menos que la gramática lo implique. Por ejemplo, "Información de contacto :" debe corregirse en "Información de contacto:". En este caso, tradúcelo utilizando la forma correcta. También puedes añadir un comentario para informar a los administradores sobre este problema en la versión original en inglés.

## Novedades

- Estamos trabajando para añadir una sección de "explicación" para cualquier cadena, junto con una captura de pantalla, para ayudarte a encontrar dónde aparece una frase/palabra específica en el sitio web. Por ahora, si tienes alguna duda sobre algunas palabras y necesitas encontrar su ubicación específica en el sitio web, puedes hacer una pregunta en la sección "comentarios" o preguntar al coordinador de traducción en el grupo de Telegram mencionado al principio de este tutorial.

![weblate](assets/23.webp)

¡Gracias de antemano por tu contribución a la traducción de Plan ₿ Academy! Si tienes alguna pregunta o comentario específico para nosotros, no dudes en ponerte en contacto con nosotros a través del [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder).
