---
name: Chat Delta
description: Guía práctica de una herramienta de mensajería descentralizada
---

![image](assets/cover.webp)




## Introducción - Control y privacidad del chat



En los últimos años se ha hablado cada vez más de Chat Control, una propuesta normativa que pretende introducir el escaneo automático de los mensajes privados en las principales plataformas de comunicación. El objetivo declarado es combatir los contenidos ilegales, el problema es que este mecanismo supondría de hecho una vigilancia masiva, que iría en detrimento del cifrado de extremo a extremo y, por tanto, de la privacidad de todos los usuarios, no sólo de los infractores.



El riesgo real es que los chats se conviertan en entornos controlados, en los que cada mensaje, imagen o archivo adjunto podría ser examinado antes incluso de llegar al destinatario. Y aquí es donde entra en juego una posible solución: alejarse de las plataformas centralizadas y optar por sistemas de mensajería descentralizados, que no dependen de un único proveedor y no pueden someterse fácilmente a este tipo de escrutinio.



En este tutorial se presenta una de estas soluciones: Delta Chat. Una herramienta madura y ya utilizable.




## Por qué Delta Chat y cómo funciona



Delta Chat es una solución de mensajería ya muy buena para el uso diario: muy útil para hablar con amigos, familiares y otras personas, como un verdadero equivalente de WhatsApp.



Se trata de un sistema de mensajería descentralizado basado íntegramente en el correo electrónico. Básicamente, aprovecha la infraestructura del correo electrónico tradicional, pero construyendo sobre ella una interfaz y una experiencia de mensajería instantánea modernas. A primera vista puede parecer un poco improvisado, pero en realidad funciona muy bien y es sorprendentemente robusto. Puedes utilizar servidores de correo dedicados llamados ChatMail, pero también puede funcionar perfectamente con servidores de correo electrónico normales. Esto significa que puedes conectarte con una cuenta existente si quieres, sin tener que crear nada nuevo.



Otro aspecto destacado es la compatibilidad con WebXDC, que son pequeñas aplicaciones web que pueden utilizarse directamente dentro de los chats, de forma similar a las miniaplicaciones de Telegram. La diferencia importante es que estas aplicaciones no tienen acceso a Internet, por lo que no pueden seguir al usuario ni enviar datos al exterior. La diferencia importante es que estas apps no tienen acceso a Internet, por lo que no pueden rastrear al usuario ni enviar datos al exterior.



Desde el punto de vista de la seguridad, Delta Chat utiliza un cifrado verificado de extremo a extremo, basado en PGP pero con modernas extensiones que lo hacen comparable en nivel de protección a Signal. La única carencia actual es Perfect Forward Secrecy, pero se trata de un aspecto en evolución.



Al basarse únicamente en el correo electrónico, Delta Chat lo evita por completo:




- números de teléfono obligatorios
- Identificaciones centralizadas
- inscripciones vinculadas a un único servicio



Y eso es lo que hace que esta herramienta sea muy resistente a regulaciones invasivas como Chat Control.




## Instalación



Desde la web oficial de [Delta Chat](https://delta.chat/download) puedes ir a la sección de descargas. En Linux está convenientemente disponible a través de Flathub, pero también hay paquetes para Arch, NixOS, Snap y versiones independientes.



![image](assets/it/01.webp)



También está disponible para:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play Store](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- y otras tiendas...



Si buscas una guía para instalar F-Droid, este tutorial puede ayudarte:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Una cosa muy importante: las versiones de escritorio no requieren teléfono. A diferencia de WhatsApp o SimpleX Chat, no es necesario registrarse primero desde el móvil. Puedes crear tu perfil directamente en el PC o transferirlo desde otro dispositivo.




## Creación de perfiles



Una vez abierta la aplicación, Delta Chat pregunta si se desea crear un nuevo perfil o utilizar uno ya existente.



![image](assets/it/02.webp)



Creando un nuevo perfil puedes entrar:




- un nombre
- una imagen (opcional)



Se propone un servidor ChatMail por defecto, pero es posible:




- elegir otro servidor ChatMail
- utilizar una cuenta de correo electrónico clásica
- configurar manualmente IMAP y SMTP
- registrarse utilizando el código de invitación de otro usuario



Tras unos segundos, el perfil estará listo y podrás empezar a utilizar la aplicación.



![image](assets/it/03.webp)




## Interface y chat



La interfaz es muy sencilla y directa:




- Mensajes de dispositivo, que son comunicaciones locales
- Mensajes guardados, similares a los de Telegram y sincronizables entre dispositivos



![image](assets/it/04.webp)



Para añadir un contacto basta con:




- Mostrar el código QR
- Escanear el
- Invitar mediante enlace (compartir enlace de invitación).



![image](assets/it/05.webp)



Una vez establecida la conexión, se configura automáticamente el cifrado de extremo a extremo. La interfaz de usuario del chat es muy similar a la de WhatsApp:




- mensajes de texto y de voz
- fotos, vídeos y archivos
- respuestas a los mensajes
- reacciones
- mensajes emergentes
- notificaciones personalizables.



![image](assets/it/06.webp)



## WebXDC: aplicaciones en chats:



Delta Chat permite utilizar WebXDC, es decir, pequeñas aplicaciones incrustadas en las conversaciones. He aquí una breve lista de las más útiles identificadas:




- encuestas
- tableros de dibujo
- chats privados temporales
- partidas con puntuaciones compartidas en el chat



También se pueden iniciar juegos más complejos, lo que demuestra la flexibilidad de esta herramienta.



![image](assets/it/07.webp)



## Grupos, canales y funciones avanzadas



Puedes crear grupos, usar pegatinas (sobre todo en los escritorios) y, activando las opciones experimentales, incluso canales, similares a los de Telegram.



En la configuración avanzada se puede activar:




- llamadas de voz (aún experimental)
- gestión avanzada de perfiles de correo electrónico
- copias de seguridad completas.



![image](assets/it/08.webp)



## Multidispositivo y copia de seguridad



Delta Chat es totalmente compatible con multidispositivo:




- puedes añadir un segundo dispositivo mediante un código QR
- puedes realizar una transferencia completa a través de la copia de seguridad.



En segundos volverás a encontrar tus chats, grupos e historial completo, sin depender de un servidor central.



![image](assets/it/09.webp)




## Conclusión



En un momento en que se habla cada vez más de controlar las comunicaciones privadas, Delta Chat representa una respuesta concreta: mensajería descentralizada y cifrada que puede utilizarse realmente todos los días.



Es la solución que, de todas las que he probado, más me ha convencido por sencillez, privacidad y libertad. Si quieres, también puedes contactar conmigo en Delta Chat a través del siguiente [enlace de invitación](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Si te ha gustado esta guía, puedes apoyarme donando y dejando un pulgar hacia arriba. Y recuerda: solo utilizando y explorando Delta Chat tanto desde el móvil como desde el escritorio descubrirás realmente toda su funcionalidad.



Hasta la próxima.