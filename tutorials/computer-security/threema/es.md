---
name: Threema
description: Mensajería instantánea segura y anónima
---
![cover](assets/cover.webp)



Fundada en 2012 en Suiza, Threema es una app de mensajería instantánea diseñada para garantizar la privacidad y la seguridad. A diferencia de WhatsApp, Telegram o Signal, Threema no requiere número de teléfono ni correo electrónico Address para crear una cuenta. Cada usuario tiene un identificador único, lo que permite un registro completamente anónimo.



Desde el punto de vista técnico, las comunicaciones a través de Threema están cifradas de extremo a extremo. El código de la aplicación móvil es de código abierto desde 2020, pero la infraestructura del servidor sigue siendo patentada y centralizada. Los servidores están alojados exclusivamente en Suiza (un país famoso por su marco jurídico para la protección de datos).



![Image](assets/fr/01.webp)



Threema dispone de clientes básicos para Android e iOS. También hay una aplicación web, así como software disponible para Windows, Linux y macOS. Sin embargo, para utilizarlos, primero debes registrarte en un dispositivo móvil.



La aplicación Threema no es gratuita. Funciona con un modelo de compra única: 5,99 euros para usar la aplicación de por vida (o 4,99 euros si la compras directamente). Para utilizar realmente Threema de forma anónima, el pago también tiene que ser anónimo. Por eso puedes comprar una clave de activación en bitcoins o en efectivo en la "*Threema Shop*" para activar la versión de Android. En iOS, en cambio, la compra debe realizarse a través de la App Store, debido a las restricciones de Apple sobre la monetización de aplicaciones.



También existe una versión para empresas llamada "*Threema Work*". En este tutorial, nos centraremos en la versión doméstica.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
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



## Instalar la aplicación Threema



Threema está disponible en todas las plataformas. Puedes descargar la aplicación directamente desde la tienda de aplicaciones de tu teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



En Android, también es posible [instalar vía APK](https://shop.threema.ch/en/download).



También existen [versiones para ordenador](https://threema.ch/download) (MacOS, Linux y Windows). Este tutorial le mostrará cómo sincronizarlas.



## Comprar licencia de Threema



Una vez instalada la aplicación, si has ido directamente a través de una tienda de aplicaciones, ya has pagado la licencia y deberías tener acceso inmediato a ella. Si has ido a través de F-Droid o de la APK, ahora tienes que comprar una licencia en el sitio web oficial.



[Ve a la "*Threema Shop*"(https://shop.threema.ch/) y haz clic en el botón "*Buy Threema for Android*".



![Image](assets/fr/02.webp)



Seleccione el número de licencias que desea comprar (sólo una si es sólo para usted), elija la moneda y seleccione el método de entrega de la licencia. Puede elegir recibir la licencia por correo electrónico, o directamente en el sitio si desea permanecer en el anonimato. A continuación, haga clic en "*Proceder al pago*".



![Image](assets/fr/03.webp)



Elige tu método de pago. En mi caso, voy a pagar en bitcoins, lo que también te recomiendo que hagas, ya que te permite permanecer en el anonimato (siempre que utilices Bitcoin adecuadamente) y es mucho más cómodo que un pago en efectivo a distancia. A continuación, haz clic en "*Siguiente*".



![Image](assets/fr/04.webp)



Si no necesita una Invoice, vuelva a hacer clic en "*Siguiente*" sin introducir ningún dato personal.



A continuación, confirme su compra haciendo clic en "*Confirmar pago*".



![Image](assets/fr/05.webp)



A continuación, deberá enviar el importe indicado a la Bitcoin Address proporcionada (lamentablemente, Lightning aún no es compatible). Una vez confirmada la transacción en la Blockchain, haga clic en "*Cerrar*" junto a la Invoice.



A continuación, tendrá acceso a su clave de licencia. Atención: si no ha introducido un correo electrónico Address, esta clave sólo se mostrará aquí. No olvide guardar la URL de la página para poder acceder a ella más tarde en caso necesario.



![Image](assets/fr/06.webp)



## Crear una cuenta en Threema



Ahora que tiene su clave de licencia, puede finalmente iniciar la aplicación. En el primer inicio, si no has comprado Threema a través de una tienda de aplicaciones, se te pedirá que introduzcas tu clave de licencia, adquirida en el sitio.



![Image](assets/fr/07.webp)



A continuación, haz clic en el botón "*Instalar ahora*".



![Image](assets/fr/08.webp)



Mueve el dedo por la pantalla para generate una fuente de entropía, necesaria para crear tu "*Threema ID*".



![Image](assets/fr/09.webp)



Aparecerá entonces tu "*ID de Treema*". Te permitirá contactar con otros usuarios. Haz clic en "*Siguiente*".



![Image](assets/fr/10.webp)



Elija una contraseña. Te permitirá restablecer el acceso a tu cuenta en caso de necesidad. Haz que tu contraseña sea lo más larga y aleatoria posible, y guarda una copia segura de ella, por ejemplo en un gestor de contraseñas.



![Image](assets/fr/11.webp)



A continuación, elige un nombre de usuario, que puede ser tu nombre real o un seudónimo.



![Image](assets/fr/12.webp)



A continuación, puedes vincular tu Threema ID a tu número de teléfono. Esto te facilita la búsqueda entre tus contactos, pero si utilizas Threema, también es para preservar tu anonimato: así que es mejor no vincularlo. Haz clic en "*Siguiente*".



![Image](assets/fr/13.webp)



Una vez completado este paso, haga clic en "*Finalizar*".



![Image](assets/fr/14.webp)



Ya estás conectado a Threema y puedes empezar a comunicarte.



![Image](assets/fr/15.webp)



## Configurar Threema



En primer lugar, accede a los ajustes haciendo clic en los tres puntitos de la esquina superior derecha y selecciona "*Ajustes*".



![Image](assets/fr/16.webp)



En la pestaña "*Privacidad*" encontrarás varias opciones que podrás ajustar a tus necesidades:




- Sincronizar los contactos del teléfono ;
- Aceptar mensajes de desconocidos;
- Indicador de escritura durante la introducción de datos ;
- Aviso de recepción de mensajes..



![Image](assets/fr/17.webp)



En la pestaña "*Seguridad*", recomiendo activar la opción "*Mecanismo de bloqueo*" para proteger el acceso a la aplicación. También es aconsejable activar passphrase para proteger las copias de seguridad locales.



![Image](assets/fr/18.webp)



No dudes en explorar las demás secciones de la configuración para personalizar la aplicación según tus preferencias.



![Image](assets/fr/19.webp)



## Copia de seguridad de su cuenta Threema



Antes de empezar a intercambiar mensajes, es importante planificar una forma de recuperar tu cuenta, sobre todo si cambias de teléfono o lo pierdes. Para ello, haz clic en los tres puntos de la parte superior derecha de Interface y, a continuación, accede al menú "*Copias de seguridad*".



![Image](assets/fr/20.webp)



Aquí encontrarás dos opciones para hacer copias de seguridad de tus datos:




- "*Threema Safe*";
- "Copia de seguridad de datos".



"Threema Safe*" guarda toda la información de tu cuenta, excepto tus conversaciones, en los servidores de Threema. Estos datos se cifran con la contraseña que elegiste al crear tu cuenta, lo que garantiza que Threema no tenga acceso a ellos. Las copias de seguridad se realizan de forma automática y periódica.



Con "*Threema Safe*", para recuperar tu cuenta en un nuevo dispositivo, basta con que introduzcas tu "*Threema ID*" y tu contraseña. Si falta alguno de estos dos datos, será imposible recuperar tu cuenta.



Esta opción sólo te permite recuperar tu ID, perfil, contactos, grupos y ciertos ajustes, pero **no tu historial de conversaciones**.



Para activar "*Threema Safe*", basta con marcar la opción en el menú "*Copias de seguridad*".



![Image](assets/fr/21.webp)



Si también quieres hacer una copia de seguridad y restaurar tu historial de conversaciones, tendrás que utilizar la opción "*Copia de seguridad de datos*". Esto genera una copia de seguridad completa de tu cuenta, almacenada localmente en tu teléfono. Tendrás que transferir esta copia de seguridad a tu nuevo dispositivo y utilizar tu contraseña (y posiblemente tu passphrase) para restaurar toda tu cuenta.



Dado que esta copia de seguridad es sólo local, es necesario copiarla regularmente en un soporte externo. De lo contrario, si se pierde el dispositivo, la recuperación será imposible. Por tanto, este método es más adecuado para una transferencia planificada de un dispositivo a otro que para situaciones de emergencia.



Nota: "*Copia de seguridad de datos*" sólo funciona si utilizas el mismo sistema operativo. No podrás utilizarla, por ejemplo, para migrar de un Samsung a un iPhone.



## Personaliza tu perfil Threema



En la esquina superior izquierda de Interface, haz clic en tu foto de perfil y selecciona "*Mi perfil*".



![Image](assets/fr/22.webp)



Aquí puedes personalizar tu perfil: añadir una foto, elegir quién puede verlo o ver tus datos de acceso a Threema.



![Image](assets/fr/23.webp)



## Sincronizar el software del PC



Si quieres acceder a tus conversaciones en tu PC, puedes sincronizar tu cuenta Threema con el software dedicado. Descarga el software para tu sistema operativo [desde el sitio web oficial](https://threema.ch/en/download).



![Image](assets/fr/24.webp)



En tu teléfono, haz clic en los tres puntos de la parte superior derecha y, a continuación, abre el menú "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Haz clic en "*Añadir dispositivo*" y, a continuación, utiliza tu teléfono para escanear el código QR que muestra el software en tu ordenador.



![Image](assets/fr/26.webp)



Para confirmar la sincronización, haz clic en el grupo emoji que aparece en el software.



![Image](assets/fr/27.webp)



En su ordenador, inicie sesión con su contraseña.



![Image](assets/fr/28.webp)



Además de la aplicación móvil, ahora puede acceder a su cuenta Threema directamente desde su ordenador.



![Image](assets/fr/29.webp)



## Enviar mensajes con Threema



Ahora que todo está configurado correctamente, puedes empezar a comunicarte. Haz clic en el botón "*Iniciar chat*".



![Image](assets/fr/30.webp)



Seleccione "*Nuevo contacto*".



![Image](assets/fr/31.webp)



Introduzca o escanee el "*ID de Treema*" de su corresponsal.



![Image](assets/fr/32.webp)



Haz clic en el icono de mensaje.



![Image](assets/fr/33.webp)



Envíe un primer mensaje a su corresponsal.



![Image](assets/fr/34.webp)



Cuando tu interlocutor responda, se establecerá la conexión y podrás ver su nombre y su foto de perfil. A continuación podrás Exchange mensajes, archivos multimedia e incluso hacer llamadas.



![Image](assets/fr/35.webp)



Enhorabuena, ya estás al día en el uso de la mensajería Threema, ¡una gran alternativa a WathsApp! Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. ¡Muchas gracias!



También te recomiendo este otro tutorial, en el que te presento Proton Mail, una alternativa mucho más respetuosa con la privacidad que Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2