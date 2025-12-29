---
name: White Noise
description: Una aplicación de mensajería privada y descentralizada basada en los protocolos Nostr y MLS
---

![cover](cover.webp)




## Introducción



"En medio de la dificultad se encuentra la oportunidad". Esta cita de Albert Einstein nos recuerda que los problemas no son definitivos, sino que contienen en su interior las semillas de soluciones nuevas e innovadoras.



Las motivaciones del lanzamiento de la solución que presentamos en este tutorial lo ilustran perfectamente. Es **White Noise**, nacido de la necesidad.



En palabras de su fundador, Max Hillebrand, recogidas por *Bitcoin Magazine*: "Lanzamos este proyecto por falta de alternativas" Explica que "las aplicaciones de cifrado existentes son ineficaces a gran escala: añadir 100 personas a una conversación de grupo ralentiza considerablemente el cifrado. Las plataformas descentralizadas, por su parte, no ofrecen mensajería privada". Por último, la red de retransmisión abierta de Nostr permite a todo el mundo difundir ideas, pero la protección de los mensajes directos sigue siendo dramáticamente inadecuada. Nos dimos cuenta: para proteger la libertad, teníamos que fusionar estos sistemas"



## ¿Qué es la White Noise?



White Noise es una aplicación de mensajería de código abierto desarrollada por un equipo sin ánimo de lucro. La aplicación promueve la seguridad, la privacidad y la descentralización. A diferencia de las aplicaciones convencionales, no requiere ni número de teléfono ni dirección de correo electrónico.


White Noise se distingue por la integración de dos protocolos fundamentales -Nostr y MLS- que constituyen su base técnica.



Nostr (Notes and Other Stuff Transmitted by Relays) es un protocolo descentralizado de código abierto diseñado para resistir la censura.  El protocolo utiliza relés, pares de claves y clientes.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Con White Noise, incluso puedes elegir tu propia configuración de retransmisión para maximizar la privacidad.



MLS (Messaging Layer Security), por su parte, es un protocolo de seguridad que permite cifrar los mensajes de extremo a extremo. En otras palabras, los mensajes sólo son accesibles en los puntos finales, es decir, el remitente y el destinatario del mensaje. Esto significa que los relés que intervienen en el encaminamiento de los mensajes no pueden acceder a su contenido.



He aquí una rápida comparación entre White Noise y algunas de las aplicaciones de mensajería más conocidas.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Primeros pasos con White Noise



### Instalación de White Noise



Acceda al [sitio web de White Noise](https://www.whitenoise.chat/) y, a continuación, haga clic en **Descargar**.



![screen](assets/fr/03.webp)



White Noise sólo está disponible actualmente en dispositivos móviles.


En la nueva interfaz que aparece, pulse :





- el botón **Zapstore** o **Android APK** si quieres descargarlo en Android ;
- en el botón **iOS TestFlight** si utilizas un iPhone.



![screen](assets/fr/04.webp)



Para los fines de este tutorial, vamos a llevar a cabo una descarga de Android.


Si eliges descargar a través de **Zapstore**, serás redirigido a ella. Una vez en Zapstore, escribe **White Noise** en la barra de búsqueda. A continuación, proceda a la descarga haciendo clic en **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Si optas por descargar el archivo APK, se te redirigirá al repositorio GitHub de White Noise para que elijas la versión adecuada para tu smartphone.



Los archivos APK disponibles son :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), adecuado para teléfonos recientes con procesadores de 64 bits;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) adecuado para teléfonos antiguos con procesadores de 32 bits.



También tienes archivos **.sha256**, que son sólo sumas de comprobación para verificar la integridad de la descarga.



![screen](assets/fr/07.webp)



Una vez finalizada la descarga, instala y abre la aplicación.



![screen](assets/fr/08.webp)



### Configuración inicial de la cuenta de usuario



Para su primera conexión a White Noise, pulse el botón **Registrarse**.



![screen](assets/fr/09.webp)



A continuación, configura tu perfil eligiendo una foto de perfil, un nombre y añadiendo una breve descripción de ti mismo. No tienes que rellenar tu identidad real (nombre y foto).


Tenga en cuenta que White Noise elige automáticamente un nombre (seudónimo) para usted, que puede mantener o cambiar. Por último, pulsa el botón **Finalizar**.



![screen](assets/fr/10.webp)



Se te redirigirá a la **pantalla de inicio** de White Noise, donde aparecerán tus conversaciones. Tu cuenta ya está configurada y lista para usar. Puedes compartir tu perfil o buscar amigos para iniciar un chat.



![screen](assets/fr/11.webp)




### Descubrir las interfaces White Noise



En la interfaz principal, en la parte superior de la pantalla verás :



En la esquina superior izquierda, el icono de perfil es una miniatura de tu foto de perfil, o la primera letra de tu nombre de perfil. Haz clic en él para acceder a la configuración de tu cuenta.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



En la esquina superior derecha encontrarás el icono para iniciar una nueva conversación.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Configuración de la cuenta de usuario



Pulsa el icono del perfil en la esquina superior izquierda para acceder a los ajustes.



![screen](assets/fr/16.webp)



En la parte superior de la interfaz **Configuración**, encontrarás tu foto y tu nombre de perfil, seguidos de tu clave pública, que puedes compartir utilizando el código QR que aparece al lado.



![screen](assets/fr/17.webp)



Justo debajo, encontrarás el botón **Cambiar cuenta**, que te permite conectarte a otro perfil dentro de la aplicación.



![screen](assets/fr/18.webp)



Luego tiene una primera sección con cuatro (4) submenús como :





- Modificar perfil**



En este submenú, puede modificar el nombre del perfil, la dirección Nostr (NIP-05)... No olvide hacer clic en **Guardar** para guardar los cambios.



![screen](assets/fr/19.webp)





- Claves de perfil**



Aquí tienes acceso a tus claves pública y privada (secreta). Como te recuerda White Noise, tu clave privada no debe ser divulgada bajo ninguna circunstancia.



![screen](assets/fr/20.webp)





- Relé de red



En este submenú puede añadir o eliminar **relés generales** (relés definidos para su uso en todas sus aplicaciones Nostr), **relés de caja** y **relés de paquete de llaves**.



Para ello, pulse sobre el icono **basura** situado delante de un relé para eliminarlo, o pulse sobre el icono **+** (más) para añadir uno nuevo.



![screen](assets/fr/21.webp)





- Desconexión**



Haz clic en este submenú para desconectar tu cuenta de la aplicación. Pero asegúrate de haber guardado tus claves privadas sin conexión, de lo contrario no podrás volver a conectarte más tarde.



![screen](assets/fr/22.webp)




Una segunda sección ofrece submenús:





- Configuración de la aplicación



Aquí puedes definir la apariencia (tema e idioma de visualización) de la aplicación, e incluso borrar datos si crees que han sido comprometidos, o si tú mismo te sientes en peligro.



![screen](assets/fr/23.webp)





- Donaciones a White Noise



Puede apoyar al equipo detrás de White Noise (una organización sin ánimo de lucro) con donaciones a través de su dirección Lightning o su dirección de pago silencioso Bitcoin.



![screen](assets/fr/24.webp)



Por último, en la parte inferior se encuentra la **configuración del desarrollador**.



![screen](assets/fr/25.webp)




## Iniciar una conversación



Veamos ahora cómo iniciar una conversación. En el momento de escribir estas líneas, White Noise ofrece tres opciones de comunicación. A continuación, exploraremos las **Conversaciones Privadas** (**Chat 1:1**), es decir, entre tú y otra persona, las **Conversaciones en Grupo** y el **Envío de Archivos Multimedia**.




### Cat 1:1



Desde la interfaz principal, para añadir un nuevo corresponsal, haz clic en el icono para iniciar una nueva conversación.


A continuación, escanea el código QR de la clave pública (1) o pega la clave pública (2) de tu nuevo corresponsal en la barra de búsqueda para encontrarlo.



![screen](assets/fr/26.webp)



A continuación, pulsa el botón **Iniciar conversación** para iniciar una conversación con tu interlocutor. También puedes **Seguir** a tu interlocutor o invitarle a una conversación de grupo pulsando el botón **Añadir a grupo**.



![screen](assets/fr/27.webp)



El primer mensaje que envías a un nuevo corresponsal es similar a una solicitud de invitación. Esta solicitud debe ser aceptada por tu corresponsal antes de que puedas comunicarte con él/ella. Si se niega, no hay conversación posible.



![screen](assets/fr/28.webp)



Además, mientras no acepten tu invitación, no podrán leer el contenido de tu mensaje inicial.



Una vez que acepte tu invitación, podrá responderte y ambos podréis comunicaros sin problemas y de forma segura.



![screen](assets/fr/29.webp)



Además, en una discusión, dispones de funcionalidades adicionales.



Puedes hacer una pulsación larga en un mensaje concreto para que aparezcan opciones como :




- reaccionar al mensaje con un emoji (1) ;
- haga una **cita directa** para responder al mensaje pulsando **Repuesta** (2) ;
- copie el mensaje pulsando **Copiar** (3).



![screen](assets/fr/30.webp)





- borra un mensaje con el botón **Borrar** sólo si procede de ti.



![screen](assets/fr/31.webp)



Puedes buscar dentro de una conversación.



Pulse sobre el avatar del interlocutor en la parte superior de la pantalla para acceder a la "información de la conversación" y pulse sobre el botón **Buscar en conversación**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



En la barra de búsqueda que aparece, escriba la palabra que desea buscar y lance la búsqueda. A continuación, verás las palabras buscadas resaltadas en **negrita**.



![screen](assets/fr/34.webp)




### Conversaciones en grupo



En White Noise pueden crearse grupos de conversación.



Para ello, toca el icono en la interfaz de inicio de nueva conversación y, a continuación, haz clic en **Nueva conversación de grupo**. A continuación, en la barra de búsqueda, introduce la clave pública del primer miembro que desees añadir a tu grupo.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Eventualmente, si esta opción no funciona, desde la interfaz **Iniciar una nueva conversación**, introduce en la barra de búsqueda la clave pública del primer miembro que desees añadir al grupo. También puedes escanear el código QR asociado a su clave pública.



Esta vez, en lugar de pulsar el botón **Iniciar conversación**, pulsa el botón **Añadir a grupo**.



![screen](assets/fr/37.webp)



En el menú emergente que aparece, pulse sobre **Nueva conversación de grupo**.



![screen](assets/fr/38.webp)



A continuación, pulse **Continuar** (no es necesario que vuelva a introducir su clave pública).



![screen](assets/fr/39.webp)



Como creador del grupo, serás automáticamente su administrador. Rellene los datos del grupo, como **nombre del grupo y descripción**, y haga clic en el botón **Crear grupo**.



![screen](assets/fr/40.webp)



El usuario que añadas como primer miembro, y cualquier otro que añadas posteriormente, recibirán una notificación invitándoles a unirse al grupo. Deben aceptar haciendo clic en **Aceptar** para unirse al grupo.



![screen](assets/fr/41.webp)



También es posible añadir a un nuevo miembro con el que ya estás chateando a un grupo existente. Para ello, haz clic en el avatar del interlocutor en la parte superior de la pantalla para acceder a la "información de la conversación" y toca el botón **Añadir al grupo**.



![screen](assets/fr/42.webp)



En la nueva interfaz que aparece, **marca** el grupo al que deseas añadirlo y pulsa sobre **Añadir al grupo**. Sólo queda esperar a que acepte unirse al grupo.



![screen](assets/fr/43.webp)



Ten en cuenta que sólo un administrador de grupo puede modificar la información del grupo y añadir o expulsar miembros. Además, la rotación de claves impide que los miembros vetados descifren futuros mensajes.



Para eliminar a un miembro, desde la interfaz principal del grupo, pulse sobre el icono del grupo en la parte superior para acceder a la interfaz de información del grupo.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



A continuación, haz clic en el nombre del miembro y **Quitar del grupo**. Desde esta interfaz, también puedes enviarle un mensaje, seguirle o añadirle a otro grupo.



![screen](assets/fr/46.webp)



### Envío de archivos multimedia



Por el momento, en White Noise sólo se pueden compartir fotos entre usuarios. Tanto si estás en una conversación privada como en un chat de grupo, para hacerlo necesitas..:





- pulse el símbolo **más (+)** situado a la izquierda del campo de introducción de mensajes de texto.



![screen](assets/fr/47.webp)





- a continuación, haz clic en la casilla **Fotos** de la parte inferior para acceder a tu galería.



![screen](assets/fr/48.webp)





- elija las fotos que desea enviar.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Puntos clave



White Noise ofrece un buen nivel de confidencialidad y una seguridad superior. Por otro lado, se trata de una aplicación muy reciente, poco extendida y aún en pañales. Por consiguiente, aún es pronto para sacar conclusiones activas. Es posible que se produzcan algunos fallos de funcionamiento durante su uso.



En la actualidad, carece de ciertas funcionalidades (no permite realizar llamadas de audio o vídeo, ni enviar archivos multimedia de audio o vídeo) en comparación con las aplicaciones de mensajería más populares.



No obstante, White Noise sigue siendo una opción interesante para conversaciones en las que la confidencialidad es primordial (por ejemplo, con la familia, amigos cercanos o activistas de una causa común), aunque requiera un poco de esfuerzo para instalarlo (a través de tiendas de aplicaciones alternativas o archivos APK) y aprenderlo (dominando un poco el concepto de pares de claves, clientes y relés con el protocolo Nostr).



Ahora ya sabes cómo utilizar White Noise para comunicarte de forma segura con tus amigos y familiares. Por favor, danos un pulgar hacia arriba si encuentras útil este tutorial.



Le recomendamos nuestro tutorial sobre Tox Chat, una aplicación que le permite chatear sin intermediarios a través del protocolo descentralizado Tox.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3