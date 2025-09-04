---
name: Tox
description: Abrir conversaciones sin intermediarios en el protocolo descentralizado Tox
---
![cover](assets/cover.webp)



El cifrado de extremo a extremo es un servicio que ofrecen muchas aplicaciones de mensajería como WhatsApp y Telegram. En este caso, cifrar significa que antes de que el remitente envíe el mensaje, éste se asegura mediante un candado criptográfico del que sólo el destinatario tiene la clave. Hoy vamos a descubrir una aplicación de mensajería cifrada de extremo a extremo totalmente descentralizada, basada en principios similares a Blockchain, para ofrecer una comunicación cifrada segura de extremo a extremo sin intermediarios: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Cifrado de extremo a extremo*



## ¿Qué es el tóxico?



Tox es un protocolo de comunicaciones descentralizado y gratuito (de código abierto) que utiliza la tecnología *Networking and Cryptography Library* (NaCl) más combinaciones de algoritmos de cifrado para garantizar la seguridad y confidencialidad de sus usuarios. Tox te permite Exchange mensajes de texto, hacer llamadas de audio y vídeo, compartir archivos y compartir tu pantalla con amigos de forma segura, descentralizada y sin intermediarios.



La tecnología que utiliza el protocolo Tox es similar a la de las redes peer-to-peer como blockchain, lo que favorece la descentralización de la infraestructura del protocolo. A diferencia de las redes sociales y las aplicaciones de mensajería cifrada de extremo a extremo, la aplicación de chat Tox se basa en un protocolo descentralizado que no tiene servidor central. Todos los usuarios se comunican en una red entre iguales sin intermediarios y resistente a la censura. Para comunicarse, cada usuario se identifica mediante un identificador único (ToxID) derivado de su clave pública, que se almacena en una tabla Hash distribuida.



## Únete a Tox



Puede utilizar el protocolo Tox a través de un cliente de mensajería instantánea que puede descargar del sitio [Tox Chat site](https://tox.chat).



![download](assets/fr/01.webp)



Dependiendo de su sistema operativo, puede descargar e instalar un cliente Tox que coincida con:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), un cliente Tox escrito en Kotlin disponible sólo en Android



![aTox](assets/fr/02.webp)





- qTox: Un cliente Tox de [código abierto](https://github.com/TokTok/qTox) basado en el Qt Framework (C++) disponible en Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) es un cliente Tox escrito en C y que funciona en sistemas con interfaces de línea de comandos.



![Toxic](assets/fr/04.webp)



En este tutorial, utilizaremos clientes qTox en Windows y aTox para comunicarnos.



## Primeros pasos con qTox



Una vez descargado, instala tu cliente Tox y crea tu perfil.



![qTox-acount](assets/fr/05.webp)



Enhorabuena, acaba de unirse al protocolo Tox. En el software qTox, puedes encontrar la información de tu perfil haciendo clic en tu nombre de usuario.



![profil](assets/fr/06.webp)



En particular, encontrarás tu ID de Tox, que puedes guardar como código QR y compartir con las personas que quieran ponerse en contacto contigo.



Exporte su archivo de perfil Tox para tener una copia de seguridad de su perfil y de la información de contacto que puede utilizar para restaurar. Haga clic en el botón **Exportar** y, a continuación, elija la ruta de su archivo de copia de seguridad.



![export](assets/fr/07.webp)



Desde el menú **Más**, añade amigos, importa contactos y gestiona las solicitudes de amistad que recibas.



![friends](assets/fr/08.webp)



Puedes ponerte en contacto conmigo a través de este ID de Tox, por ejemplo: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Una vez enviada la solicitud de amistad, el destinatario tendrá que aceptar o rechazar tu solicitud antes de que puedas ponerte en contacto con él.



![request](assets/fr/09.webp)



Su cliente Tox incluye todas las opciones que ofrecen las aplicaciones de mensajería instantánea:





- Videollamadas





- Llamadas de voz





- Intercambio de archivos





- emojis



![chat](assets/fr/10.webp)



### Grupos inter pares



Tus clientes Tox también te permiten comunicarte con un grupo de personas de forma totalmente descentralizada: son las llamadas conferencias. En el menú **Grupos**, crea una nueva conferencia o consulta la lista de invitaciones para unirte a conferencias que hayas recibido.



![conferences](assets/fr/11.webp)



Una vez creada la conferencia, puedes invitar a tus amigos a unirse a la conferencia en tu cliente Tox. En tu lista de amigos, haz clic con el botón derecho del ratón en el nombre de usuario del amigo que deseas invitar. Haga clic en la opción **Invitar a la conferencia** y seleccione el nombre de la conferencia que ha creado. También puede invitar a un amigo creando implícitamente una conferencia con la opción **Crear una nueva conferencia**.



⚠️ Los clientes Tox aún están en fase de desarrollo, por lo que es posible que se produzcan errores al interactuar con el software. Las funcionalidades de conferencia y videollamada aún no están disponibles en el cliente Tox para Android (aTox).



![invite](assets/fr/12.webp)



### Transferencias de archivos



En el menú **Transferencias de archivos**, encontrarás un historial de los archivos que has enviado y de los que has recibido de tus contactos.



![files](assets/fr/13.webp)



También puedes personalizar la configuración para compartir archivos en cada conversación que mantengas. Haz clic con el botón derecho en el nombre de usuario de tu destinatario y selecciona "Mostrar más detalles".



![details](assets/fr/14.webp)



Desde los detalles de Interface, puede gestionar las autorizaciones que concede a su destinatario para:





- Aceptación automática de invitaciones a conferencias.





- Aceptación automática de archivos.





- Rutas de copia de seguridad de los archivos de discusión.



![permissions](assets/fr/15.webp)



### Más parámetros



En el menú **Configuración**, puede personalizar la configuración de su cliente Tox.





- En la sección **General**, cambie el idioma básico de su cliente Tox, defina las rutas de copia de seguridad de los archivos y el tamaño máximo de archivo que se aceptará automáticamente.



![general](assets/fr/16.webp)





- En la sección **Usuario Interface**, modifique los tipos y tamaños de letra de sus mensajes. También puedes cambiar el tema de tu cliente Tox.



![ui](assets/fr/17.webp)





- La pestaña **Privacidad** te permite definir mensajes efímeros desmarcando la casilla "Conservar historial de chat". También puedes cambiar tu código Nospam cuando notes que recibes spam de solicitudes de amistad haciendo clic en el botón "generate código NoSpam aleatorio".



![privacy](assets/fr/18.webp)



### ¿Qué garantiza la confidencialidad en Tox?



El protocolo Tox utiliza la Tabla Distribuida Hash para crear una red de nodos descentralizados. Cada cliente Tox forma parte de la red DHT y almacena información sobre otros nodos. En el caso de Tox, la DHT almacena direcciones IP como valores asociados a claves públicas Tox (Tox ID). Esto facilita la búsqueda de un dispositivo cliente Tox sin tener que consultar a un servidor central.



Imagina que escribimos a nuestro usuario `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` al que llamaremos **usuario B**. Su cliente Tox localizará este identificador en la tabla Hash Distributed y recuperará la IP Address asociada. Una vez encontrada la IP Address, tu cliente Tox creará un canal de comunicación directo y encriptado con la máquina de nuestro **usuario B**, o utilizará otros nodos como relés para alcanzar al **usuario B**. Los algoritmos de cifrado garantizan que, independientemente del canal de comunicación, sólo el **usuario B** podrá leer el contenido de su mensaje.



Si te ha gustado descubrir Tox y has sido capaz de entender su utilidad para reforzar tu privacidad, no dudes en darle un pulgar hacia arriba a este tutorial. También te recomendamos nuestro tutorial sobre Simple Login, una herramienta que te permite recibir y enviar correos electrónicos de forma anónima.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41