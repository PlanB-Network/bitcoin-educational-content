---
name: Olvid
description: Mensajería privada para todos
---
![cover](assets/cover.webp)



Olvid es una aplicación francesa de mensajería instantánea lanzada en 2019, diseñada para ofrecer un alto nivel de seguridad, sin comprometer la privacidad. A diferencia de WhatsApp o Signal, Olvid no pide datos personales al registrarse: ni número de teléfono, ni correo electrónico, nada. La identificación entre usuarios se basa en un Exchange de claves, sin servidor de directorio ni libro Address compartido.



Todos los mensajes se cifran de extremo a extremo mediante un protocolo criptográfico original, diseñado para proteger también los metadatos: nadie sabe con quién habla ni cuándo. El código del cliente es de código abierto, pero el servidor central utilizado para enrutar los mensajes cifrados sigue siendo propietario y está alojado en AWS.

El modelo de seguridad de Olvid se basa en un principio clave: la ausencia total de terceros de confianza en el establecimiento de identidades digitales. A diferencia de la mayoría de las aplicaciones de mensajería cifrada que dependen de un directorio centralizado para gestionar las identidades de los usuarios, Olvid no depende de ninguna infraestructura centralizada para garantizar la integridad de las comunicaciones. Esta arquitectura elimina así los riesgos asociados a una posible vulneración del directorio.

No obstante, Olvid utiliza un servidor central para la distribución de mensajes, pero éste cumple únicamente una función logística: la transmisión asíncrona de mensajes cifrados. Este servidor no interviene en ninguna etapa del cifrado, no conoce la identidad real de los usuarios ni el contenido o los metadatos de los mensajes (salvo la clave pública del destinatario, necesaria para el enrutamiento). Por tanto, puede considerarse como potencialmente hostil sin comprometer la seguridad del conjunto. Incluso si se viera comprometido, no permitiría el acceso al contenido de las comunicaciones. Olvid asume así una centralización en la distribución de mensajes (por razones de eficiencia y calidad de servicio), pero garantiza una seguridad independiente de dicha infraestructura.


Olvid ofrece una versión gratuita y otra de suscripción a 4,99 euros al mes. La versión gratuita ofrece funcionalidad completa, con la excepción de hacer llamadas de audio y vídeo (aunque es posible recibirlas), y no permite sincronizar la cuenta en varios dispositivos. Así que si piensas usar exclusivamente tu smartphone y no necesitas hacer llamadas, Olvid es una solución excelente.



Olvid está certificada por la ANSSI (autoridad francesa de ciberseguridad). Esta aplicación es una excelente alternativa a los servicios de mensajería tradicionales (WhatsApp, Facebook Messenger, WeChat...) para quienes buscan privacidad sin renunciar a la sencillez de uso.


| Aplicación           | E2EE 1:1      | E2EE grupos   | Registro anónimo | Licencia cliente open-source | Licencia servidor open-source | Servidor descentralizado | Año de creación |
| -------------------- | ------------- | ------------- | ---------------- | ---------------------------- | ----------------------------- | ------------------------ | --------------- |
| WhatsApp             | ✅             | ✅             | ❌                | ❌                            | ❌                             | ❌                        | 2009            |
| WeChat               | ❌             | ❌             | ❌                | ❌                            | ❌                             | ❌                        | 2011            |
| Facebook Messenger   | ✅             | 🟡 (opcional) | ❌                | ❌                            | ❌                             | ❌                        | 2011            |
| Telegram             | 🟡 (opcional) | ❌             | 🟡               | ✅                            | ❌                             | ❌                        | 2013            |
| LINE                 | ✅             | ✅             | ❌                | ❌                            | ❌                             | ❌                        | 2011            |
| Signal               | ✅             | ✅             | ❌                | ✅                            | ✅                             | ❌                        | 2014            |
| Threema              | ✅             | ✅             | ✅                | ✅                            | ❌                             | ❌                        | 2012            |
| Element (Matrix)     | ✅             | ✅             | ✅                | ✅                            | ✅                             | 🟡 (federado)            | 2016            |
| Delta Chat           | ✅             | ✅             | ✅                | ✅                            | N/A                           | 🟡 (vía email)           | 2017            |
| Conversations (XMPP) | ✅             | ✅             | ✅                | ✅                            | ✅                             | 🟡 (federado)            | 2014            |
| Session              | ✅             | ✅             | ✅                | ✅                            | ✅                             | ✅                        | 2020            |
| SimpleX              | ✅             | ✅             | ✅                | ✅                            | ✅                             | ✅                        | 2021            |
| **Olvid**            | **✅**         | **✅**         | **✅**            | **✅**                        | **❌**                         | 🟡(sin directorio)       | **2019**        |
| Keet                 | ✅             | ✅             | ✅                | ❌                            | N/A                           | ✅                        | 2022            |
| Jami                 | ✅             | ✅             | ✅                | ✅                            | N/A                           | ✅                        | 2005            |
| Briar                | ✅             | ✅             | ✅                | ✅                            | N/A                           | ✅                        | 2018            |
| Tox                  | ✅             | ✅             | ✅                | ✅                            | N/A                           | ✅                        | 2013            |

*E2EE = Cifrado de extremo a extremo*



## Instalar la aplicación Olvid



Olvid está disponible en todas las plataformas. Puedes descargar la aplicación directamente desde la tienda de aplicaciones de tu teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



En Android, también es posible [instalar vía APK](https://www.olvid.io/download/).



En este tutorial, nos centraremos en la versión móvil, pero ten en cuenta que [también hay versiones para ordenador](https://www.olvid.io/download/) (MacOS, Linux y Windows). Si eliges la versión de pago, podrás sincronizar tu cuenta en varios dispositivos.



![Image](assets/fr/01.webp)



## Crear una cuenta en Olvid



Cuando inicies la aplicación por primera vez, haz clic en el botón "*Soy un nuevo usuario*".



![Image](assets/fr/02.webp)



Elige un apodo o introduce tu nombre y apellidos.



![Image](assets/fr/03.webp)



Añade una foto de perfil.



![Image](assets/fr/04.webp)



Su cuenta ya está creada.



![Image](assets/fr/05.webp)



Para evitar cualquier pérdida de acceso a tu cuenta de Olvid, te recomendamos que configures copias de seguridad automáticas. Para ello, abre la configuración haciendo clic en los tres puntos de la parte superior derecha de Interface y, a continuación, selecciona "*Configuración*".

⚠️ **Atención**: desde la versión 3.7 de Olvid, el procedimiento para respaldar sus perfiles y contactos ha sido reemplazado por uno nuevo. Este tutorial aún presenta la versión antigua. Puede descubrir la nueva versión en su FAQ: [💾 Respaldar sus perfiles](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Accede al menú "*Guardar teclas y contactos*".



![Image](assets/fr/07.webp)



A continuación, haz clic en "*generate a backup key*". Esta clave cifrará tus copias de seguridad. Si necesitas recuperar tu cuenta en otro dispositivo y ya no tienes acceso a ella, necesitarás tanto una copia de seguridad como esta clave para descifrarla.



![Image](assets/fr/08.webp)



Guarde esta llave en un lugar seguro. También puede hacer una copia en papel.



![Image](assets/fr/09.webp)



A continuación, puedes elegir entre crear una copia de seguridad local o una copia de seguridad automática en un servicio en la nube. Esta segunda opción es muy recomendable para garantizar el acceso a tu cuenta de Olvid en cualquier circunstancia, incluso si pierdes el teléfono.



![Image](assets/fr/10.webp)



Asegúrate de que la opción "*Habilitar copia de seguridad automática*" está marcada.



![Image](assets/fr/11.webp)



También puedes explorar los demás ajustes disponibles para personalizar la aplicación según tus necesidades.



![Image](assets/fr/12.webp)



## Envío de mensajes con Olvid



Para poder enviar mensajes, primero debes añadir contactos. En la página de inicio, haz clic en el botón azul "*+*".



![Image](assets/fr/13.webp)



A continuación, Olvid muestra tu ID de usuario. A continuación, puedes pasárselo a las personas con las que desees comunicarte para que te añadan como contacto.



Para añadir a una persona, escanea su DNI con la cámara o pégalo manualmente haciendo clic en los tres puntitos de la esquina superior derecha.



![Image](assets/fr/14.webp)



Una vez escaneado el ID, puedes hacer que tu contacto escanee el código QR que se muestra o enviarle una solicitud de conexión remota pulsando en "*Contacto remoto*".



![Image](assets/fr/15.webp)



La conexión ya está establecida.



![Image](assets/fr/16.webp)



Ya puedes empezar a intercambiar mensajes y otros contenidos con tu corresponsal



![Image](assets/fr/17.webp)



En la página de inicio encontrarás todas tus conversaciones.



![Image](assets/fr/18.webp)



La segunda pestaña contiene todos tus contactos.



![Image](assets/fr/19.webp)



También puedes crear debates en grupo.



![Image](assets/fr/20.webp)



Enhorabuena, ya estás al día en el uso de la mensajería Olvid, ¡una gran alternativa a WathsApp! Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. ¡Muchas gracias!



También te recomiendo este otro tutorial, en el que te presento Proton Mail, una alternativa mucho más respetuosa con la privacidad que Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2