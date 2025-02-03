---
name: Trezor model One
description: Configuración y uso del Trezor modelo One
---

![cover](assets/cover.webp)

Billetera física en frío: 60€ - Principiante - Seguridad entre 2 000€ y 50 000€.

Como billetera física en frío, Trezor es ideal para comenzar en Bitcoin. Es fácil de usar, no demasiado caro y funcional.

Ya hemos realizado tutoriales sobre cómo usarlo:

1. Configuración
2. Recuperación de bitcoins
3. Uso, envío y recepción de bitcoins

¿Te gustaría tener tu propio Trezor también?
¡Puedes contribuir al proyecto haciendo clic a continuación!

configuración: https://www.youtube.com/watch?v=q-BlT6R4_bE

recuperación: https://www.youtube.com/watch?v=3n4d4egjiFM

uso: https://www.youtube.com/watch?v=syouZjLC1zY

## guía de escritura

guía propuesta por https://armantheparman.com/trezor/

## Configuración del Trezor

El Trezor viene con su propio cable micro USB. Asegúrate de usar ese y no cualquier otro cable viejo que tengas por ahí. Algunos cables USB son solo de alimentación. Este transmite datos Y energía. Si usas el dispositivo con un cable USB para cargar el teléfono, es posible que el dispositivo no se conecte.

Conéctalo a tu computadora y el dispositivo se encenderá. Obtendrás un mensaje que dice "Ve a Trezor.io/start". Haz eso y descarga Trezor Suite en tu computadora.

![image](assets/0.webp)

Haz clic en el botón de descarga ("Obtener aplicación de escritorio")

![image](assets/1.webp)

Observa los enlaces de Firma y Clave de firma. Para verificar la descarga (comprobar que no se haya manipulado tu descarga), hay pasos adicionales que son opcionales si estás comenzando, pero OBLIGATORIOS si tienes una riqueza significativa para proteger. Las instrucciones para eso se encuentran en el Apéndice A (final de la guía).

Conecta el Trezor a la computadora con el cable micro USB e instala y ejecuta el programa. Así es como se ve en una Mac:

![image](assets/2.webp)

Obtendrás una advertencia tonta después de ejecutar el programa, simplemente continúa:

![image](assets/3.webp)

Haz clic en Configurar Trezor

![image](assets/4.webp)

Si el firmware está desactualizado, permite que Trezor actualice el firmware.

A continuación, puedes crear una nueva semilla o restaurar una billetera desde otro dispositivo con una semilla que ya tengas. Voy a explicar cómo crear una nueva semilla.

![image](assets/5.webp)

Haz clic en "Crear nueva billetera" - y confirma que quieres hacer esto en el propio dispositivo haciendo clic en el botón de confirmación.

Luego haz clic en la única opción "Copia de seguridad de semilla estándar"

![image](assets/6.webp)

Luego haz clic en "crear copia de seguridad"

![image](assets/7.webp)

Haz clic en las tres marcas de verificación para que se vuelvan verdes (por supuesto, lee cada mensaje) y luego haz clic en "comenzar copia de seguridad".

![image](assets/8.webp)

A continuación, verás esto:

![image](assets/9.webp)

En el dispositivo, ve las palabras que se te presentan una por una y escríbelas ORDENADAS y DE FORMA LEGIBLE.

![image](assets/10.webp)

Establece un PIN para bloquear el dispositivo (esto no forma parte de tu semilla, solo sirve para bloquear el dispositivo para que nadie pueda acceder a la semilla que contiene).

![image](assets/11.webp)

Tienes opciones para agregar shitcoins a tu billetera, te insto a que no lo hagas y ahorres solo en Bitcoin, como explico aquí (por qué bitcoin) y aquí (por qué solo bitcoin).

![image](assets/12.webp)

Nombra tu billetera y haz clic en "Acceder a Suite":

![image](assets/13.webp)

Es más sencillo crear una billetera sin frase de contraseña, pero es mejor crear una con una frase de contraseña (tu billetera real) y otra sin una frase de contraseña (tu billetera señuelo). Cada vez que accedas al dispositivo a través de Trezor Suite, se te preguntará si deseas "aplicar" la frase de contraseña o no.

![image](assets/14.webp)

Seleccioné "Billetera oculta" y escribí una frase de contraseña que inventé "craigwrightisaliarandafraud"

![image](assets/15.webp)

Me gusta cómo se llama una billetera "oculta", ya que explica en parte cómo funcionan las frases de contraseña.

Confirma la frase de contraseña en el dispositivo.

Como esta billetera está vacía, se me pidió que confirmara que la frase de contraseña es correcta:

![image](assets/16.webp)

Luego se te preguntará si deseas habilitar el etiquetado. No es algo que haya explorado, pero suena como una forma de etiquetar tus transacciones y guardar los datos en tu computadora o en la nube.

![image](assets/17.webp)

Finalmente, tu billetera estará disponible:

![image](assets/18.webp)

Lo que tienes en tu computadora se llama "billetera de observación", porque tiene tus claves públicas (y direcciones), pero no tus claves privadas. Necesitas las claves privadas para gastar (firmando transacciones con las claves privadas). La forma de hacerlo es conectando la billetera de hardware. El punto de la billetera de hardware es que las transacciones pueden pasar de ida y vuelta entre la computadora y Trezor, se puede aplicar una firma dentro de Trezor y la clave privada siempre permanece contenida dentro del dispositivo (para seguridad contra malware informático).

Trezor Suite es una billetera de observación deficiente por varias razones. Está bien para lo mínimo indispensable, pero si quieres avanzar, sigue leyendo y aprende cómo conectar el dispositivo a Sparrow Bitcoin Wallet.

## Billetera de observación

En artículos anteriores, expliqué cómo descargar y verificar Sparrow Bitcoin Wallet y cómo conectarlo a tu propio nodo o a un nodo público. Puedes seguir estas guías:

- Instalar Bitcoin Core
- Instalar Sparrow Bitcoin Wallet
- Conectar Sparrow Bitcoin Wallet a Bitcoin Core

Una alternativa al uso de Sparrow Bitcoin Wallet es Electrum Desktop Wallet, pero procederé a explicar Sparrow Bitcoin Wallet, ya que considero que es la mejor opción para la mayoría de las personas. Los usuarios avanzados pueden optar por utilizar Electrum como alternativa (consulta mi guía).

Ahora cargaremos Sparrow y conectaremos el Trezor (con la frase de recuperación pero ahora con una frase de contraseña). Esta billetera nunca ha sido expuesta a Trezor Suite porque se creará DESPUÉS de conectar el dispositivo a Trezor Suite. Asegúrate de nunca volver a conectarlo a Trezor Suite para no exponer tu nueva billetera. (Puedes conectarlo sin una frase de contraseña porque esa puede ser tu billetera señuelo).

Crea una nueva billetera:

![image](assets/19.webp)

Nómbrala de manera bonita.

![image](assets/20.webp)

Haz clic en "Billetera de hardware conectada".

![image](assets/21.webp)

![image](assets/22.webp)

Haz clic en "Escanear" y luego en "establecer frase de contraseña" en la siguiente pantalla para crear una nueva billetera (usa una nueva frase de contraseña, por ejemplo, la antigua frase de contraseña con un número al final funcionaría). Luego "envía la frase de contraseña" y confírmala en el dispositivo.

'![imagen](assets/23.webp)

Luego haz clic en "importar keystore".

En la siguiente pantalla no hay nada que editar, el Trezor lo ha completado por ti. Haz clic en "Aplicar".

![imagen](assets/24.webp)

En la siguiente pantalla puedes agregar una contraseña. No confundas esto con "frase de contraseña"; muchas personas lo hacen. El nombre es desafortunado. La contraseña te permite bloquear esta billetera en tu computadora. Es específica de este software en esta computadora. No forma parte de tu clave privada de Bitcoin.

Haz clic en "Aplicar".

![imagen](assets/25.webp)

Después de una pausa, mientras la computadora piensa, verás que los botones de la izquierda cambian de gris a azul. Felicidades, tu billetera está lista para usar. Realiza y envía transacciones a tu gusto.

![imagen](assets/26.webp)

Recepción

Para recibir bitcoins, ve a la pestaña "Direcciones" a la izquierda y elige una de las direcciones para recibir. Haz clic derecho en la dirección que desees y selecciona "copiar dirección". Luego ve a tu exchange desde donde se enviará el dinero y pégalo allí. O puedes proporcionar la dirección a un cliente que pueda usarla para pagarte.

Cuando uses la billetera por primera vez, deberías recibir una cantidad muy pequeña, practica gastándola en otra dirección, ya sea dentro de la billetera o de vuelta al exchange, para demostrar que la billetera funciona como se espera.

Una vez que hagas eso, debes hacer una copia de seguridad de las palabras que anotaste. Una sola copia no es suficiente. Ten al menos dos copias en papel (mejor si es metal) y guárdalas en dos ubicaciones diferentes y bien seguras. Esto reduce el riesgo de que un desastre natural destruya tu HWW y la copia de seguridad en papel en un solo incidente. Consulta "Usar billeteras de hardware de Bitcoin" para obtener una discusión completa al respecto.

## Envío

![imagen](assets/27.webp)

Al realizar un pago, debes pegar la dirección a la que estás pagando en el campo "Pagar a". En realidad, no puedes dejar en blanco la etiqueta, solo es para los registros de tus propias billeteras, pero Sparrow no lo permite, solo ingresa algo (solo tú lo verás). Ingresa la cantidad y también puedes ajustar manualmente la tarifa que deseas.

La billetera no puede firmar la transacción a menos que el HWW esté conectado. Ese es el trabajo del HWW: recibir la transacción, firmarla y devolverla firmada. Asegúrate de que cuando firmes en el dispositivo, inspecciones visualmente que la dirección a la que estás pagando sea la misma en el dispositivo y en la pantalla de la computadora, y la factura que recibas (por ejemplo, es posible que hayas recibido un correo electrónico para pagar a una cierta dirección).

También presta atención de que si eliges usar una moneda que sea mayor que el monto del pago, el resto se enviará de vuelta a una de las direcciones de cambio de tus billeteras. Algunas personas no sabían esto y buscaron su transacción en una cadena de bloques pública, y pensaron que se enviaron bitcoins a la dirección de un atacante, pero en realidad era su propia dirección de cambio.
Firmware

Para actualizar el firmware, debes conectarte a Trezor Suite. Si deseas hacer esto, asegúrate de tener tus palabras de respaldo y frase de contraseña disponibles para restaurar el dispositivo, en caso de que se reinicie.
Conclusión

Este artículo te mostró cómo usar un HWW Trezor de una manera más segura y privada de lo anunciado, pero este artículo solo no es suficiente. Como dije al principio, debes combinarlo con la información proporcionada en "Usar billeteras de hardware de Bitcoin".
Apéndice A - Verificar la descarga del software

## Apéndice A - Verificar la descarga del software

![imagen](assets/28 .webp)

Descarga la Firma (un archivo de texto) y la Clave de firma (un archivo de texto) y toma nota de los nombres de archivo y de dónde descargaste el archivo.

A continuación, para Mac, deberás descargar GPG Suite (Ver instrucciones aquí).

Para Windows, necesitarás GPG4win (Ver instrucciones aquí).

Para Linux, GPG ya forma parte de cada paquete. En caso de que no lo tengas, obténlo con el comando: sudo apt-get install gpg

A continuación, para Mac/Windows o Linux, abre la terminal e ingresa el siguiente comando:

```bash
gpg –import XXXXXXXXXX
```

donde XXXXXXXXXX es la ruta completa al archivo de clave de firma (ruta completa significa el directorio y el nombre de archivo donde se encuentra). Deberías ver una confirmación de una importación de clave exitosa.

Luego

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

donde ZZZZZZZZZZ es la ruta completa al archivo de firma y WWWWWWWWWW es la ruta completa al programa Trezor Suite que descargaste.

Deberías ver un mensaje "Firma válida de SatoshiLabs" en algún lugar de la salida. Hay una advertencia al final que es seguro ignorar.
