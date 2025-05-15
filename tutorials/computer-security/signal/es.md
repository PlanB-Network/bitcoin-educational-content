---
name: Señal
description: Exprésate libremente
---
![cover](assets/cover.webp)



Signal es una aplicación de mensajería cifrada de extremo a extremo, diseñada para ofrecer una buena confidencialidad por defecto. Cada mensaje, llamada y archivo está protegido por el protocolo Signal, reconocido como uno de los protocolos de mensajería más robustos. Es reutilizado por muchas otras aplicaciones, como WathsApp, Facebook Messenger, Skype y Google Messages para comunicaciones RCS.



Signal fue lanzada en 2014 por Moxie Marlinspike (seudónimo) y desarrollada desde 2018 por la Signal Foundation, una organización sin ánimo de lucro creada con el apoyo de Brian Acton (cofundador de WhatsApp).



![Image](assets/fr/01.webp)



En comparación con WhatsApp, Signal destaca por su transparencia: el código de la aplicación, tanto del lado del cliente como del servidor, es totalmente de código abierto. Esto permite que cualquiera pueda auditarla y, en particular, comprobar que el cifrado se aplica como se anuncia.



Sin embargo, Signal se basa en el uso de un número de teléfono, lo que constituye su principal punto débil en materia de anonimato en comparación con otras soluciones. A pesar de ello, la aplicación es, en mi opinión, una de las más fiables en términos de seguridad y confidencialidad, gracias a su arquitectura totalmente abierta y a un protocolo de cifrado ampliamente adoptado y, por tanto, probado y auditado, a diferencia de otras aplicaciones más marginales.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| **Signal**           | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Cifrado de extremo a extremo*




## Instalar la aplicación Signal



Signal está disponible en todas las plataformas. Puedes descargar la aplicación directamente desde la tienda de aplicaciones de tu teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



En Android, también es posible [instalar vía APK](https://github.com/signalapp/Signal-Android/releases).



En este tutorial nos centraremos en la versión móvil, pero ten en cuenta que [también hay versiones de escritorio](https://signal.org/fr/download/) (MacOS, Linux y Windows). No obstante, tendrás que configurar primero la aplicación móvil antes de poder sincronizar tu cuenta con la versión de escritorio.



## Crear una cuenta en Signal



Cuando inicie la aplicación por primera vez, pulse el botón "*Continuar*".



![Image](assets/fr/02.webp)



Introduzca su número de teléfono y pulse "*Siguiente*".



![Image](assets/fr/03.webp)



Se te enviará un código de verificación por SMS. Introduce este código en la aplicación Signal.



![Image](assets/fr/04.webp)



Elige un código PIN para proteger tu cuenta Signal. Este código encripta tus datos y puede utilizarse para restaurar el acceso a tu cuenta si pierdes tu dispositivo. Por eso es importante que elijas un código PIN robusto, lo más largo y aleatorio posible, y que guardes un registro fiable del mismo.



![Image](assets/fr/05.webp)



Confirme este código PIN por segunda vez.



![Image](assets/fr/06.webp)



Ahora puedes personalizar tu perfil de usuario. Elige una foto, introduce tu nombre o un apodo. En esta fase, también puedes definir quién puede encontrarte en Signal a través de tu número. Selecciona "*Todos*" si quieres ser visible, o "*Nadie*" para permanecer ilocalizable a través del número de teléfono (entonces sólo podrás ser añadido con tu "*Nombre de usuario*"). Una vez hecha tu selección, haz clic en "*Siguiente*".



![Image](assets/fr/07.webp)



Ya estás conectado a Signal y listo para enviar mensajes Exchange.



![Image](assets/fr/08.webp)



## Configuración de su cuenta Signal



Haz clic en tu foto de perfil en la esquina superior izquierda para acceder a los ajustes de la aplicación.



![Image](assets/fr/09.webp)



El menú "*Cuenta*" te permite gestionar la configuración de tu perfil. Te aconsejo que mantengas la configuración por defecto. También puedes activar la opción "*Bloqueo de registro*", que protege tu cuenta contra determinados tipos de ataques. Este menú también contiene las opciones que necesitas para transferir tu cuenta a un nuevo dispositivo.



![Image](assets/fr/10.webp)



Si vuelves a hacer clic en tu foto de perfil en los ajustes, accederás a las opciones para personalizar tu perfil. Te recomiendo que pongas un "*Nombre de usuario*": así podrás ponerte en contacto con otras personas sin exponer tu número de teléfono.



![Image](assets/fr/11.webp)



Seleccionando "*Código QR o enlace*", obtendrás la información que necesitas para compartirla con alguien que quiera añadirte a Signal.



![Image](assets/fr/12.webp)



El menú "*Privacidad*" es especialmente importante. Aquí encontrarás opciones para controlar la visibilidad de tu número, la gestión de tus mensajes con tus contactos, así como diversas autorizaciones concedidas en la aplicación.



![Image](assets/fr/13.webp)



Y no dudes en explorar los menús "*Apariencia*", "*Chats*" y "*Notificaciones*" para adaptar Interface y el funcionamiento de la aplicación a tus necesidades personales.



## Conectar aplicación de escritorio



Para conectar la aplicación de escritorio, empieza por instalar el software en tu ordenador (consulta la primera parte de este tutorial). A continuación, en tu teléfono, ve a Ajustes y abre la sección "*Dispositivos conectados*".



![Image](assets/fr/14.webp)



Haz clic en el botón "*Enlazar un nuevo dispositivo*".



![Image](assets/fr/15.webp)



En su ordenador, inicie el software y, a continuación, escanee el código QR que aparece en la pantalla con su teléfono. Si deseas importar tus conversaciones, selecciona la opción "*Transferir historial de mensajes*".



![Image](assets/fr/16.webp)



Tus dispositivos ya están totalmente sincronizados.



![Image](assets/fr/17.webp)



## Enviar mensajes con Signal



Para comunicarte con alguien en Signal, primero tienes que añadirlo como contacto. Hay varias opciones: puedes añadirlos a través de su número de teléfono (si la persona ha activado la opción de ser encontrada por este medio), o utilizar su ID de Signal.



Haga clic en el icono del lápiz situado en la esquina inferior derecha de Interface.



![Image](assets/fr/18.webp)



En mi caso, quiero añadir a la persona por nombre de usuario. Así que hago clic en "*Buscar por nombre de usuario*".



![Image](assets/fr/19.webp)



A continuación, puede pegar su nombre de usuario o escanear su código QR.



![Image](assets/fr/20.webp)



Envíale un mensaje para establecer contacto.



![Image](assets/fr/21.webp)



La conversación aparecerá entonces en la página de inicio. Si la persona acepta tu solicitud de contacto, verás su nombre y su foto de perfil.



![Image](assets/fr/22.webp)



Enhorabuena, ya estás al día en el uso de la mensajería Signal, ¡una gran alternativa a WathsApp! Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. ¡Muchas gracias!



También te recomiendo este otro tutorial, en el que te presento Proton Mail, una alternativa mucho más respetuosa con la privacidad que Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2