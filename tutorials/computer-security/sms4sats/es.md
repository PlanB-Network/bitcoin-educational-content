---
name: SMS4Sats
description: Recibe y envía SMS de forma anónima pagando en Bitcoin Lightning
---

![cover](assets/cover.webp)



La verificación por SMS se ha convertido en una obligación para muchos servicios en línea. Ya sea para crear una cuenta en una plataforma, validar un registro o confirmar una identidad, los sitios web exigen casi sistemáticamente un número de teléfono. Esta práctica generalizada plantea un grave problema a quien desee preservar su intimidad: su número personal se convierte en un identificador permanente, que vincula sus diversas actividades digitales a su identidad real y abre la puerta a solicitudes comerciales no deseadas.



**SMS4Sats** responde a este problema ofreciendo números de teléfono temporales para recibir y enviar mensajes SMS. El servicio destaca por su modelo sin registro y el pago exclusivo Bitcoin mediante Lightning Network. Por unos pocos satoshis, se obtiene un número desechable que permite validar un registro sin revelar nunca el número personal.



Este tutorial te guía a través de las tres funciones de SMS4Sats: recibir un SMS de verificación, enviar un SMS anónimo y alquilar un número temporal durante varias horas.



## ¿Qué es SMS4Sats?



SMS4Sats es un servicio en línea accesible en [sms4sats.com](https://sms4sats.com), que permite la gestión anónima de SMS mediante pago en Bitcoin Lightning. El servicio ofrece tres funcionalidades distintas: recepción de códigos de verificación de un solo uso, envío de SMS a cualquier número y alquiler de números temporales durante varias horas.



### Filosofía y modelo operativo



El proyecto está diseñado para garantizar la máxima confidencialidad y soberanía financiera. Al no requerir la creación de una cuenta y aceptar únicamente pagos con Bitcoin Lightning, SMS4Sats elimina por completo la necesidad de facilitar datos personales. No se requiere dirección de correo electrónico, ni tarjeta de crédito, ni información personal. Sólo se requiere el pago Lightning para acceder a los servicios.



El servicio es compatible con más de 400 sitios y aplicaciones en unos 120 países, lo que cubre la mayoría de las necesidades de verificación habituales. Esta amplia cobertura geográfica permite validar registros en diversas plataformas, desde redes sociales a servicios de mensajería.



### Modelo de pago condicional



SMS4Sats utiliza facturas relámpago condicionales (facturas hodl) para su funcionalidad de recepción de SMS. Este mecanismo garantiza que sólo se le cobre si el SMS se recibe realmente. Si no llega ningún mensaje en el tiempo asignado (20 minutos como máximo), el pago se cancela automáticamente y los satoshis se devuelven a su wallet. Esta garantía no se aplica a las funciones de envío y alquiler, que no son reembolsables.



## Las tres características de SMS4Sats



La interfaz de SMS4Sats está organizada en torno a tres pestañas que corresponden a tres usos distintos: **RECEIVE** para recibir códigos de verificación, **SEND** para enviar SMS anónimos y **RENT** para alquilar un número temporal.



### Recibir un SMS



La función principal le permite obtener un número temporal para recibir un código de verificación único. Una vez recibido y utilizado el código, el número se desactiva permanentemente.



### Enviar un SMS



Esta función te permite enviar un SMS a cualquier número de teléfono sin revelar tu identidad. El destinatario recibirá el mensaje desde un número anónimo.



### Alquilar un acto



Para los usuarios que necesitan recibir varios mensajes SMS en un solo número, SMS4Sats ofrece una opción de alquiler temporal. Esta opción permite recibir y enviar varios mensajes durante el periodo de alquiler.



**Nota sobre los precios** : Los precios que figuran en este tutorial son indicativos. Varían según el país del número, el servicio de destino y la demanda actual. Por ejemplo, un SMS a Telegram Francia puede costar entre 1.500 y 5.000 satoshis, según las condiciones. Compruebe siempre el importe exacto de la factura Lightning antes de pagar.



## Recibir un SMS de verificación



Veamos en detalle cómo utilizar SMS4Sats para recibir un código de verificación, ilustrado con la creación de una cuenta Telegram.



### Paso 1: Seleccionar país y servicio



Vaya a [sms4sats.com](https://sms4sats.com) y permanezca en la pestaña **RECIBIR**. Seleccione el país del número deseado en el menú desplegable. Si el servicio de destino de su suscripción aparece en la lista, selecciónelo para optimizar las posibilidades de recepción.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



En este ejemplo, seleccionamos Francia como país y Telegram como servicio de destino. Haga clic en **NEXT** para pasar al siguiente paso.



### Paso 2: Pagar la factura Lightning



Se muestra una factura relámpago en forma de código QR. El importe varía según el país y el servicio seleccionados. Escanea el código QR con tu Lightning wallet o copia la factura para pagar manualmente.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Fíjese en el mensaje importante: "Sin código SMS = No hay pago". Si no recibe un SMS, su pago se cancelará automáticamente y se le reembolsará en un plazo máximo de 20 minutos.



### Paso 3: Obtener el número temporal



Una vez confirmado el pago, se muestra inmediatamente el número de teléfono temporal. Un contador muestra el tiempo restante para recibir el SMS.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Copie este número (aquí +33 7 74 70 09 66) para utilizarlo en el servicio en el que desea inscribirse.



### Paso 4: Utilizar el número en el servicio de destino



Introduzca el número temporal en la aplicación o sitio web donde cree su cuenta. En nuestro ejemplo de Telegram, introduce el número, confírmalo y espera al código de verificación.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



El proceso es idéntico al registro convencional: se introduce el número, Telegram envía un código de verificación por SMS y, a continuación, se finaliza la creación de la cuenta.



### Paso 5: Recuperar el código de verificación



Vuelva a la interfaz SMS4Sats. En cuanto reciba el SMS, aparecerá automáticamente el código de activación. Haga clic en **COPIAR CÓDIGO** para copiarlo fácilmente.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Introduzca este código en el servicio de destino para finalizar su registro. El número temporal se desactivará de forma permanente.



## Enviar un SMS anónimo



SMS4Sats también te permite enviar mensajes SMS a cualquier número sin revelar tu identidad.



### Paso 1: Redactar el mensaje



Haga clic en la pestaña **ENVIAR**. Introduzca el número de teléfono de destino con su prefijo internacional y escriba su mensaje (máximo 1600 caracteres).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Pulse **SIGUIENTE** para proceder al pago.



### Paso 2: Pagar y enviar



Pague la factura relámpago mostrada. Una vez confirmado el pago, el SMS se envía inmediatamente al destinatario.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Aparecerá un código de confirmación para confirmar que el mensaje se ha enviado. El destinatario recibirá el SMS desde un número anónimo.



## Alquilar un número temporal



Para los usos que requieren varios mensajes SMS en el mismo número, la función ALQUILAR le permite alquilar un número durante varias horas.



### Configuración de alquiler



Haga clic en la pestaña **ALQUILER**. Seleccione el país y la duración.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Puntos importantes a tener en cuenta:**




- Los precios varían según el país y la duración de la estancia
- Los alquileres no son reembolsables**, a diferencia de los SMS de un solo uso
- Los números alquilados no suelen funcionar con Telegram
- Esta opción es adecuada para abonarse a varios servicios seguidos



Una vez que hayas hecho clic en **SIGUIENTE** y hayas pagado la factura relámpago, obtendrás un número que podrás utilizar durante el periodo de alquiler para recibir y enviar mensajes SMS.



## Ventajas y limitaciones



### Destacados



**No se requieren datos personales**: El modelo de no registro garantiza que no se recopile información personal.



**Tres funciones adicionales**: Recibir, enviar y alquilar cubren la mayoría de las necesidades.



**Pago sólo en Bitcoin** : Lightning Network permite transacciones instantáneas y seudónimas.



**Reembolso automático**: Al recibir mensajes SMS, el sistema de facturas hodl le garantiza que sólo pagará si llega el SMS.



### Limitaciones a tener en cuenta



**Seguridad relativa al canal SMS**: Los códigos SMS no son un método de autenticación robusto y no deben utilizarse para cuentas sensibles.



**Compatibilidad variable**: Muchos sitios detectan y bloquean los números virtuales. Pueden ser necesarios varios intentos.



**Números no reutilizables**: Después de un solo uso, el número se recicla y no se puede recuperar.



**Alquileres no reembolsables**: A diferencia de los mensajes SMS únicos, los alquileres no tienen garantía de devolución del dinero.



## Buenas prácticas



### Utiliza Tor para más privacidad



SMS4Sats es accesible a través de [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Esta configuración enmascara su dirección IP cuando accede al servicio.



### Evite las cuentas críticas



Nunca utilices un número desechable para tus cuentas importantes (banco, correo electrónico principal). Si estas plataformas te obligan a revalidar tu número más adelante, perderás el acceso a la cuenta.



### Separe sus identidades digitales



Para las cuentas seudónimas, combine el número temporal con una dirección de correo electrónico desechable y un navegador aislado de su uso habitual.



### Elige un 2FA robusto



Una vez creada su cuenta, active las soluciones de autenticación reforzada: Aplicación TOTP (Aegis, Ente Auth) o llave de seguridad física FIDO2.



## Conclusión



SMS4Sats es una solución completa para la gestión confidencial de SMS. Tanto si desea recibir un código de verificación, enviar un mensaje anónimo o alquilar un número temporal, el servicio responde a una amplia gama de necesidades de confidencialidad, gracias al pago en Bitcoin Lightning.



Sin embargo, hay que tener en cuenta sus limitaciones: el servicio no garantiza el anonimato absoluto y no es adecuado para cuentas sensibles o a largo plazo. Utilizado con prudencia y conociendo sus limitaciones, SMS4Sats es una herramienta práctica para recuperar el control de tus comunicaciones telefónicas.



## Recursos





- [Sitio web oficial de SMS4Sats](https://sms4sats.com)
- [Servicio FAQ](https://sms4sats.com/faq)
- [Dirección Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)