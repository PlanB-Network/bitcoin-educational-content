---
name: Trezor U2F y FIDO2
description: Refuerce su seguridad en línea con Trezor
---
![cover](assets/cover.webp)



Los dispositivos Trezor son monederos de hardware diseñados originalmente para asegurar una Bitcoin Wallet, pero también cuentan con opciones avanzadas para una autenticación fuerte en la web. Gracias a su compatibilidad con los protocolos **U2F** y **FIDO2**, le permiten asegurar el acceso a sus cuentas en línea sin depender únicamente de contraseñas.



El protocolo U2F (*Universal 2nd Factor*) fue introducido por Google y Yubico en 2014, y posteriormente estandarizado por la FIDO Alliance. Permite añadir un segundo factor de autenticación física (2FA) al iniciar sesión. Una vez activado, además de la contraseña clásica, los usuarios deben aprobar cada intento de conexión a su cuenta pulsando un botón en su Trezor. En este contexto, el Trezor funciona de forma similar a un Yubikey.



Este método se basa en la criptografía asimétrica: no se transmiten datos secretos, lo que hace ineficaces los ataques de suplantación de identidad o interceptación. U2F ya es compatible con muchos servicios en línea.



Además de U2F, que permite la autenticación de dos factores, los Trezors también son compatibles con FIDO2 (*Fast IDentity Online 2.0*), una evolución de U2F. Se trata de un protocolo de autenticación estandarizado a partir de 2018, que amplía la lógica de U2F y pretende sustituir por completo a las contraseñas. Se basa en dos componentes: *WebAuthn* (lado del navegador) y *CTAP2* (lado de la clave física). FIDO2 permite la autenticación "sin contraseña": los usuarios se identifican únicamente a través de su dispositivo Trezor, que actúa como token criptográfico único, sin contraseña adicional. Este protocolo es ahora compatible con numerosos servicios en línea, en particular los orientados a las empresas.



Además de la funcionalidad "sin contraseña*", FIDO2 también permite la autenticación de dos factores de forma similar a U2F.



FIDO2 también introduce la noción de credenciales residentes, es decir, identificadores almacenados directamente en el Trezor, que incluyen tanto la clave privada que permite la conexión como la información de identificación del usuario. Este mecanismo permite una autenticación realmente sin contraseña: basta con conectar el Trezor y confirmar el acceso, sin introducir ni el identificador ni la contraseña. Por el contrario, las credenciales no residentes, más convencionales, sólo almacenan la clave privada en el dispositivo; el ID de usuario permanece almacenado en el lado del servidor y, por tanto, debe introducirse en cada conexión. Más adelante veremos cómo guardarlas con su Trezor.



En este tutorial descubriremos cómo activar U2F o FIDO2 para la autenticación de dos factores y, a continuación, cómo configurar FIDO2 para acceder a tus cuentas sin contraseña, directamente con tu Trezor.



**Nota:** U2F es compatible con todos los modelos de Trezor, pero FIDO2 sólo es compatible con Safe 3, Safe 5 y Model T, no con Model One.



## Usar U2F/FIDO2 para 2FA en un Trezor



Antes de empezar, asegúrate de haber configurado tu Bitcoin Wallet en tu Trezor. Es importante guardar correctamente tu Mnemonic, ya que las claves utilizadas para U2F y FIDO2 en la autenticación de dos factores se derivan de esta Mnemonic. Si pierdes o se daña tu Trezor, puedes recuperar el acceso a tus claves introduciendo tu frase Mnemonic en otro dispositivo Trezor (ten en cuenta que para las credenciales FIDO2 en modo "*sin contraseña*", la seed por sí sola no es suficiente, como veremos en las próximas secciones).



Conecta tu Trezor al ordenador y desbloquéalo.



![Image](assets/fr/01.webp)



Accede a la cuenta que quieres proteger con la autenticación de dos factores. Por ejemplo, voy a utilizar una cuenta de Bitwarden. Normalmente encontrarás la opción 2FA en la configuración del servicio, en las pestañas "*autenticación*", "*seguridad*", "*inicio de sesión*" o "*contraseña*".



![Image](assets/fr/02.webp)



En la sección dedicada a la autenticación de dos factores, selecciona la opción "*Passkey*" (el término puede variar según el sitio que utilices).



![Image](assets/fr/03.webp)



A menudo se le pedirá que confirme su contraseña actual.



![Image](assets/fr/04.webp)



Asigne un nombre a su clave de seguridad para facilitar su reconocimiento y, a continuación, haga clic en "*Leer clave*".



![Image](assets/fr/05.webp)



Los datos de su cuenta aparecerán en la pantalla del Trezor. Toque la pantalla o pulse el botón para confirmar. También se le pedirá que confirme su código PIN.



![Image](assets/fr/06.webp)



Registre esta clave de seguridad.



![Image](assets/fr/07.webp)



A partir de ahora, cuando quieras conectarte a tu cuenta, además de tu contraseña habitual, se te pedirá que conectes tu Trezor.



![Image](assets/fr/08.webp)



A continuación, puede pulsar la pantalla de su Trezor para confirmar la autenticación.



![Image](assets/fr/09.webp)



La ventaja de utilizar un Trezor Hardware Wallet para la autenticación de dos factores es que puede recuperar fácilmente sus claves gracias a la frase Mnemonic. Además de esta copia de seguridad básica, también puede utilizar un código de emergencia proporcionado por cada servicio en el que haya activado 2FA. Este código de emergencia te permite conectarte a tu cuenta si pierdes tu clave de seguridad. Por tanto, sustituye a la 2FA para una conexión en caso necesario.



En Bitwarden, por ejemplo, puede acceder a este código haciendo clic en "*Ver código de recuperación*".



![Image](assets/fr/10.webp)



Te recomiendo que guardes este código en un lugar distinto de donde guardas tu contraseña principal, para evitar que te los roben juntos. Por ejemplo, si tu contraseña está guardada en un gestor de contraseñas, guarda tu código de emergencia 2FA en papel, por separado.



Este enfoque le ofrece dos niveles de copia de seguridad en caso de pérdida de su Trezor para la autenticación 2FA: una primera copia de seguridad utilizando la frase Mnemonic para todas sus cuentas, y una segunda específica para cada cuenta con los códigos de emergencia. Sin embargo, es importante **no confundir la función del Mnemonic con la del código de emergencia** :




- La frase Mnemonic de 12 o 24 palabras te da acceso no sólo a las claves utilizadas para 2FA en todas tus cuentas, sino también a tus bitcoins asegurados con tu Trezor ;
- El código de emergencia le permite eludir temporalmente la solicitud 2FA sólo en la cuenta en cuestión (en este ejemplo, sólo en Bitwarden).



## Uso de FIDO2 en un Trezor



Además de la autenticación de dos factores, FIDO2 también permite la autenticación "sin contraseña", es decir, sin tener que introducir una contraseña al iniciar sesión en un sitio. Sólo tiene que conectar su Trezor a su ordenador para acceder de esta forma a su cuenta segura. A continuación se explica cómo configurar esta función.



Antes de empezar, asegúrate de haber configurado tu Bitcoin Wallet en tu Trezor. Es importante guardar la Mnemonic, ya que los identificadores FIDO2 "*passwordless*" están encriptados con tu seed (veremos cómo guardar correctamente estos identificadores en la siguiente sección).



Conecta el Trezor al ordenador y desbloquéalo.



![Image](assets/fr/01.webp)



Acceda a la cuenta que desea proteger en modo "*sin contraseña*". Utilizaré una cuenta de Bitwarden como ejemplo. Esta opción suele encontrarse en la configuración del servicio, a menudo en una pestaña "*autenticación*", "*seguridad*" o "*contraseña*".



En Bitwarden, por ejemplo, la opción se encuentra en la pestaña "*Contraseña maestra*". Haz clic en "*Encender*" para activar la autenticación mediante FIDO2.



![Image](assets/fr/11.webp)



A menudo se le pedirá que confirme su contraseña.



![Image](assets/fr/12.webp)



Los datos de su cuenta aparecerán en la pantalla del Trezor. Toca la pantalla o pulsa el botón para confirmar. También tendrás que confirmar tu código PIN.



![Image](assets/fr/13.webp)



En el sitio, añada un nombre para recordar su clave de seguridad y, a continuación, haga clic en "*Encender*".



![Image](assets/fr/14.webp)



A continuación, se le pedirá que se identifique para comprobar que la llave funciona correctamente.



![Image](assets/fr/15.webp)



A partir de ahora, cuando acceda a su cuenta, ya no será necesario que introduzca su correo electrónico Address o su nombre de usuario. Basta con hacer clic en el botón para autenticarse con una llave física en el formulario de inicio de sesión.



![Image](assets/fr/16.webp)



Confirme la conexión con su Trezor introduciendo su PIN Hardware Wallet.



![Image](assets/fr/17.webp)



Se conectará a su cuenta sin tener que introducir su contraseña.



![Image](assets/fr/18.webp)



**Tenga en cuenta que aunque active la autenticación "sin contraseña" mediante FIDO2 en su Trezor, la contraseña principal de su cuenta en línea seguirá siendo válida para iniciar sesión**



## Guarda tus credenciales FIDO2 (residentes de credenciales)



Si está utilizando FIDO2 o U2F para la autenticación de dos factores, es decir, para iniciar sesión en cuentas que requieren una contraseña además de la validación 2FA a través de su Trezor, entonces la frase Mnemonic por sí sola recuperará el acceso a sus claves. Sin embargo, si está utilizando FIDO2 en modo "*sin contraseña*" como se describe en la sección anterior, será necesario hacer una copia de sus credenciales FIDO además de hacer una copia de seguridad de su frase Mnemonic que cifra estas credenciales.



Para ello, necesitará un ordenador con Python instalado. Abre un terminal y ejecuta el siguiente comando para instalar el software Trezor necesario:



```shell
pip3 install --upgrade trezor
```



Conecte su Trezor al ordenador mediante USB y desbloquéelo utilizando su código PIN.



![Image](assets/fr/01.webp)



Para recuperar la lista de identificadores FIDO2 almacenados en el Trezor, ejecute el siguiente comando:



```shell
trezorctl fido credentials list
```



Confirma la exportación en tu Trezor.



![Image](assets/fr/19.webp)



Su información de acceso FIDO2 se mostrará en su terminal. Por ejemplo, para mi cuenta Bitwarden, tengo esta información:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Copia y guarda toda esta información en un archivo de texto. No hay ningún riesgo significativo asociado a esta copia de seguridad, aparte de revelar que estás utilizando estos servicios con FIDO2. El "*Credential ID*" está encriptado usando el seed de tu Wallet, lo que significa que un atacante que obtuviera esta copia de seguridad no podría conectarse a tus cuentas, sino sólo darse cuenta de que estás usando estas cuentas. Para desencriptar estos IDs, necesitas el seed en tu Wallet.



Por lo tanto, puede crear varias copias de este archivo de texto y almacenarlas en distintos lugares, por ejemplo, localmente en su ordenador, en un servicio de alojamiento de archivos y en un soporte externo como una memoria USB. Sin embargo, tenga en cuenta que esta copia de seguridad no se actualiza automáticamente, por lo que deberá renovarla cada vez que establezca una nueva conexión "*sin contraseña*" con su Trezor.



Ahora imaginemos que has roto tu Trezor. Para recuperar tus credenciales FIDO2, primero tendrás que recuperar tu Wallet utilizando tu frase Mnemonic en un nuevo dispositivo Trezor compatible con FIDO2.



Una vez completada la recuperación, para importar tus identificadores FIDO2 en el nuevo dispositivo, ejecuta el siguiente comando en tu terminal:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Simplemente sustituya `<ID_CREDENCIAL>` por uno de sus identificadores. Por ejemplo, en mi caso, esto daría :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Su Trezor le pedirá que importe su identificador FIDO2. Confírmelo pulsando en la pantalla.



![Image](assets/fr/20.webp)



Su identificador FIDO2 ya está operativo en su Trezor. Repita este procedimiento para cada uno de sus identificadores.



Enhorabuena, ya sabes cómo usar tu Trezor con U2F y FIDO2 Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. ¡Muchas gracias!



También te recomiendo este otro tutorial, en el que vemos otra solución para la autenticación U2F y FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e