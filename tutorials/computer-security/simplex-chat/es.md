---
name: Chat SimpleX
description: El primer buzón sin identificación de usuario
---
![cover](assets/cover.webp)



Lanzada en 2021, SimpleX es una aplicación de mensajería instantánea gratuita con un enfoque radicalmente distinto de la privacidad. A diferencia de WhatsApp, Signal y otros servicios de mensajería centralizados, SimpleX destaca por su gestión de usuarios: no hay identificadores de usuario, seudónimos, números ni claves públicas visibles. Esta ausencia total de identificadores hace prácticamente imposible correlacionar a los usuarios, garantizando un alto nivel de privacidad.



A diferencia de la mayoría de las aplicaciones que requieren una cuenta o un número de teléfono, SimpleX te permite iniciar conversaciones compartiendo un enlace o un código QR efímero. Cada enlace crea un canal cifrado único, y los contactos no pueden encontrar o volver a ponerse en contacto con el remitente sin un Exchange explícito. Los mensajes se cifran de extremo a extremo y pasan por servidores de retransmisión que los borran tras su envío y no ven ni al remitente ni al destinatario, ni sus claves.



![Image](assets/fr/01.webp)



La arquitectura de la red es totalmente descentralizada y no federada: los servidores no se conocen entre sí, no mantienen un directorio global y no alojan ningún perfil de usuario. Mejor aún, cada usuario puede instalar y utilizar su propio servidor de retransmisión, sin dejar de ser interoperable con los de la red pública.



SimpleX es completamente de código abierto (clientes, protocolos y servidores), disponible en Android, iOS, Linux, Windows y macOS. Su almacenamiento local está cifrado y es portátil, por lo que puedes transferir un perfil de un dispositivo a otro sin depender de un servidor centralizado.



SimpleX integra todas las funciones clásicas de las aplicaciones de mensajería. Sin embargo, su ergonomía sigue siendo menos fluida que la de WhatsApp o Signal. También puede resultar más restrictiva de usar, sobre todo a la hora de añadir contactos. Así pues, en mi opinión, es una alternativa pertinente a WhatsApp o Signal para los usuarios que sitúan la confidencialidad en el centro de sus prioridades, y que están dispuestos, por esa razón, a hacer algunas concesiones en la comodidad cotidiana de uso.



| Aplicación           | E2EE 1:1       | E2EE grupos    | Registro anónimo    | Licencia cliente open-source | Licencia servidor open-source | Servidor descentralizado | Año de creación   |
| -------------------- | -------------- | -------------- | ------------------- | ---------------------------- | ----------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                            | ❌                             | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                            | ❌                             | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opcional) | ❌                   | ❌                            | ❌                             | ❌                        | 2011              |
| Telegram             | 🟡 (opcional) | ❌              | 🟡                  | ✅                            | ❌                             | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                            | ❌                             | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                            | ✅                             | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                            | ❌                             | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                            | ✅                             | 🟡 (federado)           | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                            | N/A                           | 🟡 (vía email)          | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                            | ✅                             | 🟡 (federado)           | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                            | ✅                             | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                            | ✅                             | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                            | ❌                             | 🟡(sin directorio)      | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                            | N/A                           | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                            | N/A                           | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                            | N/A                           | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                            | N/A                           | ✅                        | 2013              |

*E2EE = Cifrado de extremo a extremo*



## Instalar la aplicación SimpleX Chat



SimpleX Chat está disponible en todas las plataformas. Puedes descargar la aplicación directamente desde la tienda de aplicaciones de tu teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



En Android, también es posible [instalar vía APK](https://github.com/simplex-chat/simplex-chat/releases).



En este tutorial, nos centraremos en la versión móvil, pero ten en cuenta que [las versiones de escritorio también están disponibles](https://simplex.chat/downloads/) (MacOS, Linux y Windows). Es posible vincular la versión de escritorio a un perfil de usuario móvil existente, pero para que esta sincronización funcione, ambos dispositivos deben estar conectados a la misma red local.



![Image](assets/fr/02.webp)



## Crear una cuenta en SimpleX Chat



Cuando inicies la aplicación por primera vez, haz clic en el botón "*Crea tu perfil*".



![Image](assets/fr/03.webp)



Elige un nombre de usuario, que puede ser tu nombre real o un seudónimo, y haz clic en "*Crear*".



![Image](assets/fr/04.webp)



A continuación, establece la frecuencia con la que la aplicación comprobará si hay mensajes nuevos. Si la duración de la batería de tu teléfono no es un problema, selecciona "*Instantáneo*" para recibir mensajes en tiempo real. Si prefieres ahorrar batería y evitar que la aplicación se ejecute en segundo plano, selecciona "*Cuando la aplicación se está ejecutando*": sólo recibirás mensajes cuando la aplicación esté abierta. Un posible compromiso es optar por una comprobación periódica cada 10 minutos.



Una vez hecha tu elección, haz clic en "*Usar chat*".



![Image](assets/fr/05.webp)



Ya estás conectado a SimpleX Chat y listo para empezar a chatear.



![Image](assets/fr/06.webp)



## Configuración de SimpleX Chat



En primer lugar, accede a la configuración haciendo clic en tu foto de perfil, en la esquina inferior derecha, y luego en "*Configuración*".



![Image](assets/fr/07.webp)



La configuración por defecto suele ser adecuada para la mayoría de los usuarios. Sin embargo, te recomiendo que vayas al menú "*Base de datos passphrase y exportación*". Aquí es donde puedes exportar la base de datos de tu cuenta SimpleX para realizar copias de seguridad.



También puedes modificar el passphrase utilizado para cifrar esta base de datos. Por defecto, se genera aleatoriamente y se almacena localmente en tu dispositivo. Si lo prefieres, puedes definir tu propio passphrase y eliminar la copia de seguridad del passphrase local: entonces tendrás que introducirlo manualmente cada vez que abras la aplicación, así como cuando migres a otro dispositivo.



**Tenga en cuenta**: si elige esta opción, la pérdida del passphrase supondrá la pérdida permanente de todos sus perfiles y mensajes SimpleX.



![Image](assets/fr/08.webp)



También te recomiendo que vayas al menú "*Privacidad y seguridad*", donde podrás activar la opción "*Bloqueo SimpleX*". Esto protege el acceso a la aplicación con un código de bloqueo.



![Image](assets/fr/09.webp)



Por último, los menús "*Notificaciones*" y "*Apariencia*" te permiten personalizar SimpleX Chat para adaptarlo a tus preferencias.



![Image](assets/fr/10.webp)



## Enviar mensajes con SimpleX Chat



Para conectar con otra persona en SimpleX, tienes dos opciones:




- Utilice un enlace de un solo uso;
- Utilice un Address estático reutilizable.



Una Address estática permite a cualquiera que la conozca ponerse en contacto contigo en SimpleX. Es un Address persistente, que puede ser utilizado varias veces, por diferentes personas, sin límite de tiempo. Es esta persistencia la que lo hace más vulnerable al spam. Sin embargo, a diferencia de otras aplicaciones de mensajería, basta con borrar tu Address de SimpleX para detener todo el spam, sin afectar a las conversaciones existentes. De hecho, esta Address sólo se utiliza para establecer la conexión inicial, y deja de ser necesaria una vez iniciada la Exchange.



En cambio, los enlaces de un solo uso sólo pueden ser utilizados una vez por cualquier usuario. Una vez que un contacto lo utiliza, el enlace deja de ser válido. Tendrás que generate uno nuevo para cada nueva conexión.



### Con Address estático



Si desea utilizar la Address, haga clic en su foto de perfil en la parte inferior izquierda de la Interface y, a continuación, seleccione "*Crear SimpleX Address*". A continuación, vuelva a hacer clic en "*Crear SimpleX Address*".



![Image](assets/fr/11.webp)



Ya has creado tu Address reutilizable. Puedes compartirla con las personas que quieran ponerse en contacto contigo, mostrándoles el código QR o enviándoles el enlace.



![Image](assets/fr/12.webp)



Pulse el botón "*Configuración Address*". Aquí puedes configurar los permisos asociados a tu Address. La opción "*Compartir con contactos*" hace que tu Address sea visible en tu perfil de SimpleX. Así, tus contactos podrán consultarla y reenviarla a otras personas que deseen ponerse en contacto contigo.



La opción "*Aceptar automáticamente*" acepta automáticamente las conexiones entrantes a través de tu Address. Esto significa que cualquiera que tenga tu Address podrá ver tu perfil y enviarte un mensaje, a menos que actives la opción "*Aceptar de incógnito*". Esto oculta tu nombre y foto de perfil cuando se establece una nueva conexión, sustituyéndolos por un seudónimo aleatorio, distinto para cada interlocutor.



![Image](assets/fr/13.webp)



### Con eslabón reutilizable



La segunda forma de conectar con una persona es crear un enlace de un solo uso. Para ello, haz clic en el icono del lápiz situado en la esquina inferior derecha de Interface y, a continuación, selecciona "*Crear enlace de 1 sola vez*".



Si tu contacto te ha enviado un enlace, haz clic en "*Escanear / Pegar enlace*" para escanearlo o pegarlo.



![Image](assets/fr/14.webp)



SimpleX genera entonces un enlace de un solo uso. Puedes reenviarlo a tu contacto por cualquier medio: Exchange físico, otro tipo de mensajería, etc.



![Image](assets/fr/15.webp)



También puede elegir qué perfil desea asociar a este enlace de invitación. Para ello, haga clic en su perfil justo debajo del código QR. A continuación podrá :




- seleccione uno de sus perfiles existentes (veremos cómo crear varios perfiles en la siguiente sección);
- o elige el modo "*Incógnito*", que oculta tu nombre y foto de perfil con un seudónimo generado aleatoriamente para tu interlocutor.



Aquí, elijo el modo "*Incógnito*".



![Image](assets/fr/16.webp)



Mi contacto utilizó el enlace. Por su parte, no activó el modo "*Incógnito*", razón por la cual veo su nombre de perfil, "*Bob*". Por otro lado, Bob no ve mi nombre real "*Loïc Morel*", sino un seudónimo aleatorio, en este caso "*RealSynergy*".



![Image](assets/fr/17.webp)



Podría empezar a chatear inmediatamente, pero primero me gustaría comprobar que estoy hablando con Bob, y no con algún malintencionado que pueda haber interceptado el enlace o llevado a cabo un ataque MITM.



Para ello, vamos a verificar nuestro enlace de seguridad **fuera de la aplicación**. Esto es importante, porque en caso de un ataque MITM, la verificación interna se vería comprometida. Así que utiliza otro sistema de mensajería segura, o incluso mejor, comprueba los códigos en persona.



En el chat, haz clic en la foto de Bob y luego en "*Verificar código de seguridad*". Bob tiene que hacer lo mismo por su parte.



![Image](assets/fr/18.webp)



Si trabajas a distancia, compara los códigos en otro sistema de mensajería segura (deben ser idénticos). O mejor aún, si puedes reunirte cara a cara, escanea el código QR de tu contacto haciendo clic en "*Escanear código*".



![Image](assets/fr/19.webp)



Si la verificación se realiza correctamente, aparecerá un icono en forma de escudo con una marca de verificación junto al nombre de tu contacto. Esta es la garantía de que estás intercambiando con Bob. Si la verificación no se realiza correctamente, aparecerá la alerta "*Código de seguridad incorrecto*".



![Image](assets/fr/20.webp)



Ahora puedes Exchange libremente mensajes, llamadas y archivos con Bob, dependiendo de los permisos que hayas establecido para esta conversación.



## Personaliza tus perfiles de SimpleX Chat



Una de las características más potentes de SimpleX es la posibilidad de gestionar varios perfiles de usuario completamente independientes, todos accesibles desde la misma cuenta local. Esto te permite separar ordenadamente tus distintas identidades, sin complicar la gestión de mensajes.



Por ejemplo, puede crear un archivo :




- Un perfil con tu nombre real y una foto real para tus intercambios profesionales;
- Un perfil con tu nombre real y una foto divertida para tus intercambios familiares;
- Un perfil con una foto falsa y un seudónimo para tus conversaciones personales;
- Otro perfil seudónimo para chatear con desconocidos.



Eso es lo que vamos a hacer aquí. Empiezo configurando mi perfil principal, el vinculado a mi identidad real. Para ello, hago clic en mi foto de perfil, en la esquina inferior derecha, y luego en mi nombre de usuario.



![Image](assets/fr/21.webp)



A continuación, hago clic en mi foto de perfil para cambiarla y añadir una nueva.



![Image](assets/fr/22.webp)



Para añadir otros perfiles, haz clic en el menú "*Tus perfiles de chats*".



![Image](assets/fr/23.webp)



Aquí verás todos tus perfiles. Haz clic en "*Añadir perfil*" para crear uno nuevo.



![Image](assets/fr/24.webp)



A continuación, elige la información para tu nuevo perfil: nombre, foto, etc. Aquí utilizo un seudónimo y una imagen diferente para ocultar mi identidad real en determinados intercambios.



![Image](assets/fr/25.webp)



Si mantienes el dedo pulsado sobre un perfil, puedes ocultarlo. Esto lo hará invisible en la aplicación, junto con todas las conversaciones asociadas. También puedes optar por "*Silenciarlo*" para dejar de recibir notificaciones.



![Image](assets/fr/26.webp)



Una vez creados sus perfiles, puede gestionarlos de forma independiente. En la página de inicio, sólo tienes que seleccionar el perfil activo que deseas mostrar.



![Image](assets/fr/27.webp)



Cuando creas un enlace de invitación o Address estático, ahora puedes elegir qué perfil asociar a él. Por ejemplo, si selecciono el perfil "*Satoshi Nakamoto*" para generate un enlace y se lo envío a Alice, ella sólo verá mi identidad seudónima "*Satoshi Nakamoto*", sin conocer nunca mi identidad real "*Loïc Morel*". Por el contrario, si le proporciono un enlace desde mi perfil real, ella no tendrá forma de enlazar con mi perfil seudónimo.



![Image](assets/fr/28.webp)



Enhorabuena, ya conoces la mensajería SimpleX, una excelente alternativa a WathsApp



También recomiendo este otro tutorial, en el que presento Threema, otra alternativa interesante para tu aplicación de mensajería:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74