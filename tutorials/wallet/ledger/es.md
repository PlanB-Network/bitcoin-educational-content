---
name: Ledger Nano S

description: Cómo configurar tu dispositivo Ledger Nano S
---

![image](assets/cover.webp)

Billetera física fría - €60 - Principiante - Para asegurar €2,000 a €50,000

Ledger es la solución francesa para asegurar bitcoins de manera sencilla.

En este tutorial, también discutiremos la sección de frases de contraseña, una solución de seguridad avanzada para almacenar grandes sumas: 20,000€ - 100,000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Conectar Ledger a Sparrow Bitcoin Wallet (guía de escritura)

Asegúrate de leer primero la otra parte "Usando billeteras de hardware de Bitcoin". Repasaré algunos pasos y me centraré principalmente en lo que es específico de Ledger aquí.

## Configuración del dispositivo

El Ledger viene con su propio cable USB. Asegúrate de usar ese y no cualquier otro cable viejo. Algunos cables USB solo transmiten energía. Este transmite datos Y energía. Cuando he usado el dispositivo con un cable USB de carga de teléfono que tenía por ahí, el dispositivo no se ha conectado.

Conéctalo a tu computadora y el dispositivo se encenderá.

![image](assets/1.webp)

Recorre las opciones. Verás

1. Configurar como dispositivo nuevo
2. Restaurar desde frase de recuperación

Básicamente, está preguntando si quieres que el dispositivo cree una semilla para ti o si ya tienes una que te gustaría usar. Es mejor práctica hacer tu propia semilla, pero hacerlo de manera segura es muy avanzado y está fuera del alcance de este artículo. Elige "Configurar como dispositivo nuevo".

Luego se te pedirá que elijas un PIN. Esto no forma parte de tu semilla de Bitcoin y es específico de este dispositivo solamente. Bloquea el dispositivo.

Luego te presentará 24 palabras que debes recorrer y anotar.

Curiosamente, cuando llegas al final, dice "presiona izquierda para verificar tus palabras". Eso no describe cómo confirmar para proceder, solo significa que puedes volver atrás y ver las palabras nuevamente. Presiona derecha en su lugar y confirma presionando izquierda y derecha simultáneamente.

La siguiente parte es muy molesta. Mezcla las 24 palabras y debes confirmar cada una, del 1 al 24, recorriendo todas las palabras para cada selección. Una vez que hayas terminado, te permitirá confirmar con una pulsación de dos botones y continuar.

![image](assets/2.webp)

Verás en tu panel que tienes un botón de configuración y un botón de signo más que te permite instalar aplicaciones. Pero primero necesitas conectarte a Ledger Live. Haremos eso a continuación...

## Descargar Ledger Live

Podrías descargar Ledger Live desde su página web, pero es mejor obtenerlo de GitHub, donde se guarda el código fuente.

Busca en Google "ledger live GitHub" o haz clic en este enlace https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Desplázate hacia abajo hasta que veas el encabezado "Descargas"...

![image](assets/4.webp)

En la parte inferior, verás el enlace: Las instrucciones para verificar el hash y las firmas de los paquetes de instalación están disponibles en esta página. Haz clic en ese enlace. (https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

En la parte superior, hay opciones de enlace para el paquete de software que necesitas, según tu sistema operativo. Haz clic en el adecuado para descargar.

A continuación, queremos verificar el hash de la descarga, para mayor seguridad.
'Ledger publica el hash de cada uno de los archivos disponibles en esta página. Ahora vamos a hacer el hash de la descarga y comparar el resultado. Necesita ser idéntico para asegurarnos de que el archivo no ha sido manipulado.
Abre la terminal en una Mac o CMD en Windows. Sigue estos comandos...

cd Descargas

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Para Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Para Windows
```

<Enter>

Esperemos que sea obvio que los comandos comienzan después de las flechas. Asegúrate, si este artículo está desactualizado, de cambiar el nombre del archivo en los comandos por el nombre exacto del archivo que descargaste. Necesitas presionar la tecla <Enter> después de cada comando. Los comandos tal como se ven aquí pueden no caber en una línea en tu navegador web. Ten en cuenta que todo está escrito en una línea.

Mira la salida del hash y asegúrate de que sea idéntica a la publicada en GitHub.

Idealmente, quieres ser un poco más sofisticado y asegurarte de que los hashes que se publican no sean falsos. Hacemos esto con firmas gpg, pero está fuera del alcance de este artículo. Si quieres aprender sobre eso (y te sugiero que eventualmente lo hagas), entonces lee este artículo.

## Conéctate a Ledger Live

Antes de ejecutar Ledger Live, ayuda un poco a la privacidad activar una VPN. Ledger seguirá obteniendo todas tus direcciones, pero no conocerán tu dirección IP, que revela tu dirección de casa. Mullvad VPN es un excelente servicio de VPN y no es muy caro (no estoy haciendo publicidad, es solo lo que uso).

Instala el software en tu computadora y ejecútalo.

![image](assets/6.webp)

Selecciona tu dispositivo y selecciona "Primera vez que lo uso..."

![image](assets/7.webp)

Luego se te guiará a través de un asistente, pero ya hemos realizado todos estos pasos para que puedas avanzar rápidamente.

![image](assets/8.webp)

Después de muchos pasos y un cuestionario, se verificará que el dispositivo sea genuino. Debes asegurarte de estar conectado e ingresar el PIN, y luego te preguntará en el dispositivo si permites que Ledger Live se conecte. Debes confirmarlo, por supuesto.

![image](assets/9.webp)

A continuación, apareció algo de publicidad de shitcoin disfrazada de "notas de lanzamiento". Descártala y luego deberías llegar a esta pantalla.

![image](assets/10.webp)

Debes hacer clic en "Agregar cuenta" para obtener una billetera de Bitcoin.

![image](assets/11.webp)

Asegúrate de elegir Bitcoin, no Bitcoin Cash ni ninguna otra shitcoin. Se verificará el dispositivo y debes confirmar para continuar EN EL DISPOSITIVO. Calculará las direcciones durante un par de minutos. Luego haz clic en HECHO.

![image](assets/12.webp)
![image](assets/13.webp)

Genial. Ahora tienes un administrador de billeteras de shitcoin que contiene una billetera de Bitcoin en tu computadora. En realidad, ya no necesitas esto y puedes deshacerte de él. El verdadero propósito era obtener la aplicación de Bitcoin en el propio dispositivo, y esta era la única forma, a menos que realices algunas técnicas extremas de ingeniería de software.

Recuerda que antes, en el dispositivo, teníamos un botón de configuración y un botón de signo más. Ahora tenemos un botón adicional: el botón de la aplicación de Bitcoin.

Puedes cerrar Ledger Live ahora.

## Agregar una frase de contraseña'

Ahora que tenemos la aplicación de Bitcoin, podemos agregar una frase de contraseña a nuestra frase de recuperación. Antes no podíamos hacerlo cuando se creó la frase de recuperación porque al principio no teníamos la aplicación de Bitcoin y necesitábamos conectarnos a Ledger Live para obtenerla.

Ve al menú "configuración" dentro del dispositivo, luego al submenú "seguridad". Luego selecciona "frase de contraseña". Verás "Función avanzada". Haz clic en el botón derecho, verás "leer manual..." y luego después de hacer clic en el botón derecho, verás "atrás". Pero eso no es todo. Intuitivamente, pensarías eso, pero haz clic en el botón derecho nuevamente. Verás "configurar frase de contraseña".

Puedes decidir "adjuntar al PIN" o "establecer temporalmente". Recomiendo "adjuntar al PIN". De esa manera, puedes acceder a diferentes billeteras dependiendo del PIN que ingreses cuando enciendes el dispositivo por primera vez. Si "estableces temporalmente", deberás ingresar la frase de contraseña cada vez que desees acceder a esa billetera, pero siempre será desde el PIN predeterminado.

Ingresa la frase de contraseña y confírmala.

Te pedirá el "PIN actual". Este no es el PIN que estás asociando con la nueva frase de contraseña. Es el PIN que ingresaste cuando encendiste el dispositivo para esta sesión.

Ahora puedes salir al menú principal seleccionando la opción de retroceso varias veces.

## Observando la billetera

En artículos anteriores, expliqué cómo descargar y verificar la billetera Sparrow, y cómo conectarla a tu propio nodo o a un nodo público. Debes seguir estas guías:

- Instalar Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Instalar la billetera Sparrow Bitcoin (https://armantheparman.com/download-sparrow/)

- Conectar la billetera Sparrow Bitcoin a Bitcoin Core (https://armantheparman.com/sparrowcore/)

Una alternativa al uso de la billetera Sparrow Bitcoin es la billetera de escritorio Electrum, pero procederé a explicar la billetera Sparrow Bitcoin ya que considero que es la mejor para la mayoría de las personas. Los usuarios avanzados pueden optar por utilizar Electrum como alternativa.

Ahora la cargaremos y conectaremos el Ledger, con la billetera que contiene la frase de contraseña. Esta billetera nunca ha sido expuesta a Ledger Live porque se creó DESPUÉS de conectar el dispositivo a Ledger Live. Asegúrate de nunca volver a conectarla a Ledger Live para no exponer tu nueva billetera privada.

Crear una nueva billetera:

![image](assets/14.webp)

Ponle un nombre bonito

![image](assets/15.webp)

Observa la casilla de verificación "Tiene transacciones existentes". Si esta es una billetera que has utilizado antes, marca esta casilla, de lo contrario, tu saldo se mostrará incorrectamente como cero. Marcar esta casilla le pide a Sparrow que examine la base de datos de Bitcoin Core (el blockchain) en busca de transacciones anteriores. Para esta guía, estamos utilizando una billetera completamente nueva, por lo que puedes dejar la casilla sin marcar.

![image](assets/16.webp)

Haz clic en "Billetera de hardware conectada" y asegúrate de que el dispositivo esté realmente conectado, encendido, con el PIN ingresado y que hayas ingresado a la aplicación de Bitcoin.

![image](assets/17.webp)

Haz clic en "Escanear" y luego en "Importar almacén de claves" en la siguiente pantalla.

![image](assets/18.webp)

No hay nada que editar en la siguiente pantalla, el Ledger lo ha completado por ti. Haz clic en "Aplicar"

![image](assets/19.webp)

La siguiente pantalla te permite agregar una contraseña. No confundas esto con "frase de contraseña"; muchas personas lo hacen. La denominación es desafortunada. La contraseña te permite bloquear esta billetera en tu computadora. Es específica de este software en esta computadora. No forma parte de tu clave privada de Bitcoin.

'![image](assets/20.webp)

Después de una pausa, mientras la computadora piensa, verás que los botones de la izquierda cambian de gris a azul. Felicidades, tu billetera está lista para usar. Realiza y envía transacciones a tu gusto.

![image](assets/21.webp)

## Recepción

Para recibir bitcoins, ve a la pestaña "Direcciones" a la izquierda y elige una de las direcciones para recibir. Haz clic derecho en la dirección que desees y selecciona "copiar dirección". Luego ve a tu exchange desde donde se enviará el dinero y pégalo allí. O puedes darle la dirección a un cliente que pueda usarla para pagarte.

Cuando uses la billetera por primera vez, deberías recibir una cantidad muy pequeña, practica gastándola en otra dirección, ya sea dentro de la billetera o de vuelta al exchange, para comprobar que la billetera funciona como se espera.

Una vez que hagas eso, debes hacer una copia de seguridad de las palabras que anotaste. Una sola copia no es suficiente. Ten al menos dos copias en papel (mejor si es de metal) y guárdalas en dos ubicaciones diferentes y seguras. Esto reduce el riesgo de que un desastre natural destruya tu HWW y la copia de seguridad en papel en un solo incidente. Consulta "Usar billeteras de hardware de Bitcoin" para obtener una discusión completa sobre esto.

## Envío

![image](assets/22.webp)

Al realizar un pago, debes pegar la dirección a la que estás pagando en el campo "Pagar a". En realidad, no puedes dejar en blanco la etiqueta, solo es para los registros de tus propias billeteras, pero Sparrow no lo permite; simplemente ingresa algo (solo tú lo verás). Ingresa la cantidad y también puedes ajustar manualmente la tarifa que deseas.

La billetera no puede firmar la transacción a menos que el HWW esté conectado. Ese es el trabajo del HWW: recibir la transacción, firmarla y devolverla firmada. Asegúrate de que cuando firmes en el dispositivo, inspecciones visualmente que la dirección a la que estás pagando sea la misma en el dispositivo y en la pantalla de la computadora, y la factura que recibas (por ejemplo, es posible que hayas recibido un correo electrónico para pagar una cierta dirección).

También presta atención de que si eliges usar una moneda que sea mayor que el monto del pago, el resto se enviará de vuelta a una de las direcciones de cambio de tus billeteras. Algunas personas no sabían esto y buscaron su transacción en una cadena de bloques pública, y pensaron que se enviaron bitcoins a la dirección de un atacante, pero en realidad era su propia dirección de cambio.

## Firmware

Para actualizar el firmware, debes conectarte a Ledger Live. Si deseas hacer esto, debes borrar el dispositivo primero y asegurarte de tener tus palabras de respaldo y frase de contraseña disponibles para restaurar el dispositivo. La razón por la que prefiero borrar el dispositivo primero es que debes conectar tu dispositivo a Ledger Live para actualizar el firmware, y prefiero no exponer tu nueva billetera (la que tiene la frase de contraseña) a Ledger Live, nunca. Simplemente no confío en que Ledger no extraiga mi información de clave pública del dispositivo cuando me conecto a Ledger Live. Ellos afirman que no lo hacen, pero no puedo verificarlo por mí mismo a menos que lea el código y comprenda el hardware interno también.

## Conclusión

Este artículo te mostró cómo usar un HWW de Ledger de una manera más segura y privada de lo anunciado, pero este artículo solo no es suficiente. Como dije al principio, debes combinarlo con la información proporcionada en "Usar billeteras de hardware de Bitcoin".
Consejos:

Dirección estática de Lightning: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/'

Para profundizar en este tema y reforzar la seguridad de su cartera en un Ledger Nano con una passphrase BIP39, le invito a consultar este tutorial completo:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49
