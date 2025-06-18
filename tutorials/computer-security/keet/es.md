---
name: Tecla
description: Chat entre iguales
---
![cover](assets/cover.webp)



Keet es una aplicación de mensajería instantánea diseñada para funcionar sin servidores. Lanzada en 2022 por Holepunch (una empresa financiada por Tether y Bitfinex), la aplicación se basa por completo en una red entre pares y presenta un enfoque radicalmente descentralizado: los mensajes, las llamadas y los archivos se intercambian directamente entre los usuarios, sin intermediarios.



Keet encripta todas las comunicaciones de extremo a extremo y no pide datos personales. El registro es anónimo, sin necesidad de número de teléfono ni correo electrónico. Además de intercambiar mensajes de texto, Keet ofrece videollamadas de muy alta calidad, así como la posibilidad de compartir archivos de forma ilimitada. Por tanto, la aplicación puede utilizarse de forma híbrida, tanto para uso personal como profesional.



![Image](assets/fr/01.webp)



Por el momento (abril de 2025), Keet no es totalmente de código abierto. Parte del código fuente está disponible en [Holepunch's GitHub repository](https://github.com/holepunchto), especialmente los componentes criptográficos y de red, pero el cliente Interface todavía no. Holepunch, sin embargo, ha anunciado su intención de hacer que toda la aplicación sea de código abierto con el tiempo. Dependiendo de cuando descubras este tutorial, puede que esto ya se haya hecho.




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



## Instalar Keet



Keet está disponible en todas las plataformas. Puede descargar la aplicación directamente desde la tienda de aplicaciones de su teléfono:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



En Android, también es posible [instalar vía APK](https://github.com/holepunchto/keet-mobile-releases/releases).



En este tutorial, nos centraremos en la versión móvil, pero ten en cuenta que [también hay versiones para ordenador](https://keet.io/) (MacOS, Linux y Windows). También es posible sincronizar tu cuenta en varios dispositivos.



## Crear una cuenta en Keet



En el primer lanzamiento, puedes ignorar las pantallas de presentación.



![Image](assets/fr/02.webp)



Haz clic en el botón "*Soy un nuevo usuario*".



![Image](assets/fr/03.webp)



Acepta las condiciones de uso y haz clic en "*Instalación rápida*".



![Image](assets/fr/04.webp)



Elige un nombre o apodo y haz clic en "*Finalizar configuración*".



![Image](assets/fr/05.webp)



Tu perfil ya está creado. Vuelve a hacer clic en "*Finalizar configuración*" para finalizar.



![Image](assets/fr/06.webp)



Puedes personalizar tu perfil en cualquier momento desde la pestaña "*Perfil*".



## Guarda tu cuenta Keet



Lo primero que debes hacer con tu nueva cuenta Keet es guardar tu frase de recuperación. Se trata de una secuencia de 24 palabras que te permitirá recuperar el acceso a tu cuenta en caso de pérdida o cambio de dispositivo. Esta frase da acceso completo a tu cuenta a cualquiera que la conozca, por lo que es importante hacer una copia de seguridad fiable y no divulgarla nunca.



Para ello, haz clic en la pestaña "*Perfil*" situada en la parte inferior derecha de Interface.



![Image](assets/fr/07.webp)



A continuación, accede al menú "*Configuración*".



![Image](assets/fr/08.webp)



Seleccione "*Privacidad y seguridad*".



![Image](assets/fr/09.webp)



A continuación, haz clic en "*Frase de recuperación*".



![Image](assets/fr/10.webp)



Pulsa el botón "*Ver frase*" para mostrar tu frase de recuperación. Cópiala con cuidado y guárdala en un lugar seguro.



![Image](assets/fr/11.webp)



## Enviar mensajes con Keet



Para comunicarte en Keet, tienes que crear "*Salas*". Para ello, haz clic en el icono del lápiz situado en la parte superior derecha de Interface.



![Image](assets/fr/12.webp)



Selecciona "*Nuevo chat de grupo*".



![Image](assets/fr/13.webp)



Elige un nombre y una descripción para tu "*Sala*" y haz clic en "*Crear chat de grupo*".



![Image](assets/fr/14.webp)



Su "*Sala*" ya está creada. Haga clic en el icono "*+*" de la parte superior derecha para invitar a los participantes.



![Image](assets/fr/15.webp)



Defina los derechos que concede a los nuevos miembros a través del enlace de invitación, así como la duración de la validez del enlace. A continuación, haga clic en "*generate invitar*".



![Image](assets/fr/16.webp)



Keet enviará a generate un enlace para unirse a tu "*Sala*". Puedes copiarlo y compartirlo, o hacer que las personas a las que quieras invitar escaneen su código QR.



![Image](assets/fr/17.webp)



Ya puedes empezar a intercambiar mensajes y archivos multimedia. Para iniciar una llamada, pulsa el icono del teléfono en la esquina superior derecha.



![Image](assets/fr/18.webp)



Desde este grupo también puedes enviar mensajes privados a un miembro concreto. Haga clic en la imagen de perfil del grupo y, a continuación, seleccione el miembro deseado en la sección "*Miembros*".



![Image](assets/fr/19.webp)



Haz clic en el botón "*Enviar solicitud de DM*" e introduce tu mensaje.



![Image](assets/fr/20.webp)



Una vez aceptada la solicitud de DM, encontrarás este contacto en la página de inicio, donde podrás hablar con él en privado.



![Image](assets/fr/21.webp)



## Sincroniza tu cuenta en varios dispositivos



Ahora que ya sabes cómo utilizar Keet y tienes una cuenta, también puedes sincronizarlo en otro dispositivo, como un ordenador. Para ello, abre la aplicación en tu móvil, pulsa "*Perfil*" y accede a "*Configuración*".



![Image](assets/fr/22.webp)



A continuación, ve al menú "*Mis dispositivos*".



![Image](assets/fr/23.webp)



Haz clic en "*Añadir dispositivo*". Keet generate un enlace para sincronizar un nuevo dispositivo. Copia este enlace.



![Image](assets/fr/24.webp)



En tu segundo dispositivo, instala Keet. En la pantalla de inicio, selecciona la opción "*Soy usuario actual*".



![Image](assets/fr/25.webp)



A continuación, haz clic en "*Enlazar dispositivo*".



![Image](assets/fr/26.webp)



Pega el enlace proporcionado por tu primer dispositivo y haz clic en "*Iniciar sincronización*".



![Image](assets/fr/27.webp)



En el primer dispositivo, haz clic en "*Confirmar dispositivos de enlace*" para autorizar la conexión.



![Image](assets/fr/28.webp)



En el segundo dispositivo, completa el proceso haciendo clic en "*Enlazar dispositivos*".



![Image](assets/fr/29.webp)



Ahora puedes acceder a todas tus "*Salas*" y conversaciones desde este nuevo dispositivo.



![Image](assets/fr/30.webp)



Enhorabuena, ya estás al día en el uso de la mensajería Keet, ¡una gran alternativa a WathsApp! Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. ¡Muchas gracias!



También te recomiendo este otro tutorial, en el que te presento Proton Mail, una alternativa mucho más respetuosa con la privacidad que Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2