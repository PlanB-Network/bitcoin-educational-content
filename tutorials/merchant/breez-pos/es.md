---
name: Punto de venta Breez

description: Guía para comenzar a aceptar bitcoin utilizando Breez POS
---

![cover](assets/cover.jpeg)

# Punto de venta Breez

_Este texto proviene del sitio web de documentación de Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## ¿Qué es Breez POS?

**Breez** es una aplicación de Lightning de servicio completo y no custodial. Veamos qué significa eso:

- **Lightning** es una red de pago de bitcoin que reduce los tiempos de transacción de minutos a milisegundos y las tarifas de transacción de varios dólares a unos pocos centavos o menos. Lightning convierte bitcoin de oro digital en moneda digital mientras conserva todos los beneficios que hacen que bitcoin sea genial.
- **No custodial** significa que Breez no se hace cargo del dinero de los usuarios. Muchas aplicaciones de Lightning se hacen cargo del dinero de sus usuarios. Básicamente son bancos de bitcoin. Con una aplicación no custodial como Breez, todos los usuarios son sus propios bancos.
- **Servicio completo** significa que Breez se encarga de casi todas las operaciones técnicas de forma automática y en segundo plano. Cosas como la creación de canales, la liquidez entrante y el enrutamiento se mantienen bajo el capó. (Pero Breez también es de código abierto, por lo que aquellos interesados en auditar la tecnología son bienvenidos a hacerlo).

**Breez POS** es la abreviatura de nuestro modo de punto de venta. En otras palabras, Breez funciona como una caja registradora digital para empresas y comerciantes que desean aceptar pagos de Lightning (además de su modo "estándar", que es como la versión digital de una billetera de cuero para bitcoin, y un reproductor de podcast de próxima generación). Ahora veamos cómo configurar Breez como una caja registradora de Lightning para tu negocio.

## Cómo empezar con Breez?

1. El primer paso es descargar la aplicación. Está disponible para Android e iOS (instala TestFlight y haz clic en el enlace desde tu dispositivo).
2. Breez puede hacer una copia de seguridad automáticamente en Google Drive, iCloud o cualquier servidor WebDav.
   > Ten en cuenta que cada dispositivo ejecuta su propio nodo de Lightning. Puedes ejecutar el modo POS en tantos dispositivos como desees, pero los saldos se mantendrán separados.
3. Con la aplicación abierta, haz clic en el icono en la parte superior izquierda para encontrar el modo de Punto de Venta.

## Configuración de POS

1. Haz clic en ese icono en la parte superior izquierda y luego en Punto de Venta > Configuración de POS.

### La contraseña del gerente

En la Configuración de POS, tienes la opción de crear una contraseña de gerente. La contraseña del gerente hace que sea imposible enviar pagos salientes desde la aplicación Breez sin autorización. El personal de ventas solo podrá recibir pagos desde el dispositivo. Ten en cuenta que si estás utilizando esta opción, es posible que también desees evitar el acceso a la copia de seguridad de Breez, por lo que se recomienda utilizar una cuenta externa de WebDav (por ejemplo, Nextcloud) para este caso de uso.

### La lista de artículos

La lista de artículos es un catálogo de artículos en venta y sus precios. Hay dos formas de agregar artículos a la lista:

- Para ingresar artículos uno por uno, haz clic en Artículos cerca de la parte superior de la vista principal de POS, luego en el signo "+" en la parte inferior derecha. Aquí puedes ingresar el nombre de un solo tipo de artículo, el precio (mostrado en la moneda equivalente de tu elección) y el SKU (un identificador interno único para ese tipo de artículo; es opcional).
- Para ingresar muchos artículos a la vez, haz clic en el ícono de la calculadora en la parte superior izquierda, luego en Punto de Venta > Preferencias > Configuración de POS, y luego haz clic en los tres puntos a la derecha de la Lista de Artículos, y luego en Importar desde CSV. Esto te permitirá importar un archivo CSV que hayas preparado previamente con los nombres, precios y SKUs de tus artículos.

### Pantalla de Fiat

Breez solo envía y recibe bitcoin, y para la mayoría de las transacciones en Lightning, que tienden a ser de cantidades más pequeñas, la suma se muestra generalmente en Satoshis, también conocidos como sats (1 BTC = 100,000,000 sats). Sin embargo, muchos comerciantes encuentran práctico poder ver (y mostrar a los clientes) el valor de la compra en la moneda fiduciaria local.

En la vista principal de POS, la moneda que se muestra actualmente está visible en el lado derecho (el valor predeterminado es SAT). También hay una lista desplegable de otras monedas disponibles para mostrar. Para agregar o eliminar monedas de esta lista desplegable, haz clic en Punto de Venta > Preferencias > Monedas Fiat. Luego simplemente marca las monedas que te gustaría tener en tu menú desplegable y desmarca aquellas que desees omitir.

Los valores mostrados provienen de yadio, una fuente respetada de datos de tipo de cambio, y se actualizan casi en tiempo real. Pero recuerda: sin importar el valor de la moneda que se muestre actualmente, el pago en sí es en bitcoin.

### Cobrar un Pedido

Para componer el pedido, agrega artículos de la lista de artículos o simplemente ingresa una suma en el teclado. Luego haz clic en Cobrar en la parte superior de la vista principal de POS. A continuación, verás un código QR que el cliente puede escanear con su aplicación de Lightning, que puedes compartir directamente desde otra aplicación en tu dispositivo, o que puedes copiar y pegar donde sea necesario.

Al escanear ese código o hacer clic en la factura compartida/pegada, el cliente verá la factura en su aplicación de Lightning y tendrá la opción de pagarla y liquidar la transacción de inmediato.

Una vez que veas la animación ¡Pago aprobado! en la aplicación Breez en el dispositivo del comerciante, puedes hacer clic en el ícono de la impresora para generar un recibo para el cliente. Para usar una impresora de recibos en Android, intenta usar este controlador. Ten en cuenta que también puedes imprimir transacciones pasadas a través de la pantalla de Transacciones.

### Informe de Ventas

Para ver un informe diario/semanal/mensual de tus ventas (con fines contables u otros), haz clic en el ícono en la parte superior izquierda, y luego haz clic en Transacciones. Haz clic en el ícono de Informe para mostrar el informe y en el ícono de Calendario para cambiar el rango de fechas seleccionado.

### Exportar Transacciones

Para ver una lista de los pagos recibidos en Breez, haz clic en el ícono en la parte superior izquierda, y luego haz clic en Transacciones. Haz clic en los tres puntos en la parte superior derecha, luego en Exportar para exportar una lista de pagos entrantes en formato CSV. Para restringir la lista a un período de tiempo determinado, haz clic en el ícono de calendario para establecer un rango de fechas.

### Imprimir Recibos

Para imprimir un recibo de venta, haz clic en el ícono de impresión en la parte superior derecha del cuadro de confirmación de pago. Alternativamente, haz clic en el ícono en la parte superior izquierda, y luego haz clic en Transacciones. Localiza la venta que deseas imprimir, ábrela y haz clic en el ícono de impresión en la parte superior derecha.

> Nota: utiliza este controlador para imprimir en una impresora térmica portátil de 58 mm/80 mm Bluetooth/USB.

## Quiero aprender más

- Para obtener más información sobre Lightning y Breez, visita nuestro [blog](https://breez.technology/blog).
- Para obtener más consejos técnicos sobre cómo aprovechar al máximo la aplicación y realizar operaciones comunes, consulta nuestra [documentación](https://breez.technology/documentation).
- Si te quedas atascado y no puedes encontrar la respuesta en ninguno de nuestros materiales de ayuda, puedes encontrarnos en [Telegram](https://t.me/breez_labs) o enviarnos un [correo electrónico](mailto:support@breez.technology).
- Si quieres ver algunos videos de demostración del modo POS de Breez en acción realizados por nuestros fans y usuarios, [aquí](https://www.youtube.com/watch?v=xxxx) tienes uno corto y genial, y [aquí](https://www.youtube.com/watch?v=xxxx) tienes uno más largo y detallado.
