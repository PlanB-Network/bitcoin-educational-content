---
name: Session
description: Enviar mensajes cifrados, no metadatos
---
![cover](assets/cover.webp)



Session es una aplicación de mensajería cifrada creada en 2020, diseñada para ofrecer un mayor nivel de confidencialidad que la mensajería tradicional. Primero fue desarrollada por la *Oxen Privacy Tech Foundation* y después por la *Session Technology Foundation*.



Session cuenta con algunas características técnicas interesantes: Cifrado de extremo a extremo de los mensajes, una red descentralizada organizada para garantizar la disponibilidad y la redundancia, y enrutamiento Onion inspirado en Tor. Además, a diferencia de WathsApp o Signal, que exigen un número de teléfono para registrarse, Session no pide información personal (ni número, ni correo electrónico, sólo un par de claves criptográficas).



Session te permite enviar mensajes, archivos, mensajes de voz, llamadas de audio, así como grupos de hasta 100 miembros (y comunidades más allá), al tiempo que minimiza las filtraciones de metadatos.



![Image](assets/fr/01.webp)



Session se dirige sobre todo a los usuarios que sitúan la confidencialidad en el centro de sus prioridades. Este servicio de mensajería representa una alternativa seria a WhatsApp, con una arquitectura diseñada para resistir a los modelos de vigilancia modernos.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Cifrado de extremo a extremo*



## Instalar la aplicación Session



Session está disponible en todas las plataformas. Puedes descargar la aplicación directamente desde la tienda de aplicaciones de tu teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



En Android, también es posible [instalar vía APK](https://github.com/session-foundation/session-android/releases).



En este tutorial, nos centraremos en la versión móvil, pero ten en cuenta que [las versiones para ordenador también están disponibles](https://getsession.org/download) (MacOS, Linux y Windows). Más adelante veremos cómo sincronizar una cuenta en varios dispositivos.



## Crear una cuenta en Session



En el primer inicio, haga clic en "*Crear cuenta*".



![Image](assets/fr/02.webp)



Elige un nombre para tu perfil. Puede ser un seudónimo o tu nombre real.



![Image](assets/fr/03.webp)



A continuación, tendrá que elegir entre dos modos de gestión de las notificaciones:





- **Modo rápido ("*Firebase Cloud Messaging/Apple Push Notification Service*")**: Permite recibir notificaciones de mensajes casi en tiempo real, gracias a los servicios de notificación proporcionados por Google o Apple (dependiendo de tu sistema). Para que esto funcione, tu IP Address y un ID de notificación único se transmiten a Google o Apple, y el ID de cuenta de sesión también se registra en un servidor STF (a través de Tor). Este modo implica una exposición (ciertamente mínima) de metadatos, pero no compromete el contenido de los mensajes ni los contactos, y no permite rastrear tu actividad real. Este modo es por tanto más eficiente en términos de capacidad de respuesta, pero depende de una infraestructura centralizada y es ligeramente menos efectivo en términos de confidencialidad.





- **Modo lento (*background polling*)**: la aplicación Session permanece activa en segundo plano, sondeando periódicamente la red en busca de nuevos mensajes. Este enfoque garantiza una mayor confidencialidad que el primero, ya que no se transmiten datos a servidores de terceros; ni Google, ni Apple, ni los servidores de STF reciben información alguna. Por otro lado, este modo presenta dos inconvenientes: las notificaciones pueden retrasarse (hasta varios minutos) y el consumo de energía suele ser mayor debido a la actividad de la aplicación en segundo plano.



![Image](assets/fr/04.webp)



Ya estás conectado a la aplicación Session y puedes empezar a intercambiar mensajes.



![Image](assets/fr/05.webp)



## Guardar tu cuenta de Session



Lo primero que debes hacer antes de empezar a utilizar Session es guardar tu cuenta para poder recuperarla si pierdes tu dispositivo. Para ello, haz clic en el botón "*Continuar*" situado junto a "*Guarda tu contraseña de recuperación*".



![Image](assets/fr/06.webp)



Session mostrará entonces una frase Mnemonic. Cópiala cuidadosamente y guárdala en un lugar seguro. Esta frase proporciona acceso completo a tu cuenta Session, por lo que es importante no divulgarla. La necesitarás para acceder a tu cuenta desde otro dispositivo, especialmente si pierdes o te cambian tu teléfono actual.



![Image](assets/fr/07.webp)



Esta frase funciona de forma similar a las frases Mnemonic utilizadas en las carteras Bitcoin. Por ello, te recomendamos que consultes este otro tutorial, en el que explico las mejores prácticas para guardar una frase Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Nota**: A diferencia de las frases Mnemonic utilizadas en las carteras Bitcoin, en Session, **debes guardar absolutamente cada palabra en su totalidad**. Las 4 primeras letras no son suficientes



## Configuración de la aplicación Session



Para acceder a la configuración de la aplicación, haz clic en tu foto de perfil en la parte superior izquierda de la interfaz. Aquí es donde puedes añadir una foto de perfil.



![Image](assets/fr/08.webp)



En el menú "*Privacidad*", puedes activar o desactivar varias funciones (cuidado, algunas pueden exponer tu dirección IP). También te recomendamos activar la opción "*Bloquear App*", que requiere autenticación para acceder a la aplicación.



![Image](assets/fr/09.webp)



En el menú "*Notificación*" podrás elegir entre "*Modo rápido*" y "*Modo lento*" (consulta las partes anteriores del tutorial). También puedes personalizar las notificaciones según tus preferencias.



![Image](assets/fr/10.webp)



Por último, ve al menú "*Apariencia*" para adaptar la interfaz a tu gusto. El menú "*Contraseña de recuperación*" permite recuperar tu frase Mnemonic si deseas hacer una nueva copia de seguridad.



![Image](assets/fr/11.webp)



## Envío de mensajes con Session



Para ponerte en contacto con otras personas, pulsa el botón "*+*" de la página de inicio.



![Image](assets/fr/12.webp)



Hay varias opciones disponibles. Si deseas crear un grupo o unirte a uno, selecciona "*Crear grupo*" o "*Unirse a una comunidad*".



![Image](assets/fr/13.webp)



Si quieres que alguien te añada como contacto, puedes pedirle que escanee tu ID de Session como código QR.



![Image](assets/fr/14.webp)



Para enviar tu identificación de Session a distancia, haz clic en "*Invitar a un amigo*". A continuación, puedes copiar tu identificador de Session y enviarlo a través de otro canal de comunicación. También puedes recuperar esta información haciendo clic en tu foto de perfil desde la página de inicio.



![Image](assets/fr/15.webp)



Si tienes el ID de Session de otra persona y deseas añadirlo, haz clic en "*Nuevo mensaje*".



![Image](assets/fr/16.webp)



A continuación, puedes pegar el identificador en texto, o escanearlo directamente si lo tienes como código QR.



![Image](assets/fr/17.webp)



A continuación, envía un mensaje inicial a esta persona.



![Image](assets/fr/18.webp)



En cuanto la persona acepte tu solicitud, verás aparecer su nombre de usuario y podrás chatear libremente con ella.



![Image](assets/fr/19.webp)



## Sincronizar software de escritorio



Para sincronizar tu cuenta en tu ordenador, necesitas instalar el software. [Descárgalo del sitio web oficial](https://getsession.org/download). Te aconsejamos que compruebes su autenticidad e integridad antes de instalarlo.



![Image](assets/fr/20.webp)



En el primer inicio, haz clic en "*Tengo una cuenta*".



![Image](assets/fr/21.webp)



Introduce tu frase Mnemonic, asegurándote de dejar un espacio entre cada palabra.



![Image](assets/fr/22.webp)



Ahora puedes acceder a tus conversaciones desde tu ordenador.



![Image](assets/fr/23.webp)



Enhorabuena, ya le has cogido el truco a la mensajería de Session, una excelente alternativa a WhatsApp



También te recomendamos este otro tutorial, en el que presentamos Threema, otra alternativa interesante para tu aplicación de mensajería:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74
