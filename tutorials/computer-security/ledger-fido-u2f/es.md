---
name: Ledger U2F & FIDO2
description: Aumente su seguridad en línea con Ledger
---
![cover](assets/cover.webp)



Los dispositivos Ledger son monederos de hardware diseñados originalmente para asegurar un Bitcoin Wallet, pero también cuentan con opciones avanzadas para una autenticación fuerte en la web. Gracias a su compatibilidad con los protocolos **U2F** y **FIDO2**, le permiten proteger el acceso a sus cuentas en línea estableciendo un segundo factor de autenticación.



El protocolo U2F (Universal 2nd Factor) fue introducido por Google y Yubico en 2014, y posteriormente estandarizado por la FIDO Alliance. Permite añadir un segundo factor de autenticación física (2FA) al iniciar sesión. Una vez activado, además de la contraseña clásica, los usuarios deben aprobar cada intento de conexión a su cuenta pulsando un botón en su Ledger. En este contexto, la Ledger funciona de forma similar a un Yubikey. De hecho, U2F es un subcomponente de la norma FIDO2, que la engloba a la vez que aporta mejoras significativas, como la compatibilidad nativa con los navegadores modernos y una mayor flexibilidad en la gestión de las claves de autenticación.



Estos métodos se basan en la criptografía asimétrica: no se transmiten datos secretos, lo que hace ineficaces los ataques de suplantación de identidad o interceptación. U2F y FIDO2 ya son compatibles con muchos servicios en línea.



En este tutorial, te mostraremos cómo activar U2F y FIDO2 para la autenticación de dos factores con tu Ledger.



**Nota:** U2F y FIDO2 son compatibles con todos los dispositivos Ledger equipados con firmware reciente: a partir de la versión 2.1.0 para el Nano X y el Nano S classic, y a partir de la versión 1.1.0 para el Nano S Plus. Los modelos Stax y Flex son compatibles de forma nativa.



## Instale la aplicación Ledger Security Key



Si utiliza un dispositivo Ledger, probablemente sabrá que el firmware por sí solo no contiene todas las funciones necesarias para gestionar criptocarteras. Por ejemplo, para utilizar un Bitcoin Wallet, necesitará instalar la aplicación "*Bitcoin*". Del mismo modo, para gestionar claves MFA, necesitarás instalar la aplicación "*Security Key*".



Antes de empezar, asegúrate de que has configurado tu Bitcoin Wallet en tu Ledger. Es importante guardar correctamente tu Mnemonic, ya que las claves utilizadas para 2FA se derivan de esta Mnemonic. Si tu Ledger se pierde o se daña, puedes recuperar el acceso a tus claves introduciendo tu frase Mnemonic en otro dispositivo Ledger (por el momento, los identificadores FIDO2 en modo "*sin contraseña*" aún no están soportados en Ledgers, por lo que no hay identificadores residentes).



Conecta tu Ledger al ordenador y desbloquéalo.



![Image](assets/fr/01.webp)



Para instalar la aplicación, abra el software [Ledger Live] (https://www.Ledger.com/Ledger-live) y, a continuación, vaya a la pestaña "*Mi Ledger*". Busca la aplicación "*Llave de seguridad*" e instálala en tu dispositivo.



![Image](assets/fr/02.webp)



La aplicación "*Llave de seguridad*" debería aparecer ahora junto a las demás aplicaciones instaladas en su Ledger.



![Image](assets/fr/03.webp)



Haga clic en la aplicación para dejarla abierta para los siguientes pasos del tutorial.



![Image](assets/fr/04.webp)



## Utilizar U2F/FIDO2 para 2FA con un Ledger



Accede a la cuenta que quieres proteger con la autenticación de dos factores. Por ejemplo, voy a utilizar una cuenta de Bitwarden. Normalmente encontrarás la opción 2FA en la configuración del servicio, en las pestañas "*autenticación*", "*seguridad*", "*inicio de sesión*" o "*contraseña*".



![Image](assets/fr/05.webp)



En la sección dedicada a la autenticación de dos factores, selecciona la opción "*Passkey*" (el término puede variar según el sitio que utilices).



![Image](assets/fr/06.webp)



A menudo se le pedirá que confirme su contraseña actual.



![Image](assets/fr/07.webp)



Asigne un nombre a su clave de seguridad para facilitar su reconocimiento y, a continuación, haga clic en "*Leer clave*".



![Image](assets/fr/08.webp)



Los datos de su cuenta aparecerán en la pantalla de Ledger. Pulse el botón "*Registrar*" para confirmar (o ambos botones simultáneamente, según el modelo que esté utilizando).



![Image](assets/fr/09.webp)



La clave de acceso se ha registrado correctamente.



![Image](assets/fr/10.webp)



Registre esta clave de seguridad.



![Image](assets/fr/11.webp)



A partir de ahora, cuando te conectes a tu cuenta, además de tu contraseña habitual, se te pedirá que conectes tu Ledger.



![Image](assets/fr/12.webp)



A continuación, puedes pulsar el botón "*Iniciar sesión*" de la pantalla de tu Ledger para confirmar la autenticación (o ambos botones simultáneamente, según el modelo que estés utilizando).



![Image](assets/fr/13.webp)



La ventaja de utilizar una Hardware Wallet Ledger para la autenticación de dos factores es que puedes recuperar fácilmente tus claves gracias a la frase Mnemonic. Además de esta copia de seguridad básica, también puede utilizar un código de emergencia suministrado por cada servicio en el que haya activado 2FA. Este código de emergencia te permite conectarte a tu cuenta si pierdes tu clave de seguridad. Por tanto, sustituye a la 2FA para una conexión en caso de necesidad.



En Bitwarden, por ejemplo, puede acceder a este código haciendo clic en "*Ver código de recuperación*".



![Image](assets/fr/14.webp)



Te recomiendo que guardes este código en un lugar distinto de donde guardas tu contraseña principal, para evitar que te los roben juntos. Por ejemplo, si tu contraseña está guardada en un gestor de contraseñas, guarda tu código de emergencia 2FA en papel, por separado.



Este enfoque le ofrece dos niveles de copia de seguridad en caso de pérdida de su Ledger para la autenticación 2FA: una primera copia de seguridad utilizando la frase Mnemonic para todas sus cuentas, y una segunda copia de seguridad específica para cada cuenta utilizando los códigos de emergencia. Sin embargo, es importante **no confundir la función de la Mnemonic con la del código de emergencia** :




- La frase Mnemonic de 12 o 24 palabras le da acceso no sólo a las claves utilizadas para 2FA en todas sus cuentas, sino también a sus bitcoins asegurados con su Ledger ;
- El código de emergencia le permite eludir temporalmente la solicitud 2FA sólo en la cuenta en cuestión (en este ejemplo, sólo en Bitwarden).



Enhorabuena, ¡ya estás al día en el uso de tu Ledger para MFA! Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar Green a continuación. No dudes en compartir este tutorial en tus redes sociales. Muchas gracias



También te recomiendo este otro tutorial, en el que vemos otra solución para la autenticación U2F y FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e