---
name: Lipa
description: Configuración y uso del monedero móvil Lipa lightning
---
![cover](assets/cover.webp)

Un monedero Bitcoin Lightning es una aplicación móvil que permite realizar transacciones instantáneas y de bajo coste en la red Lightning de Bitcoin. A diferencia de las transacciones en la cadena de bloques principal (on-chain), los pagos Lightning son casi instantáneos y requieren comisiones mínimas, lo que los hace especialmente adecuados para pagos pequeños y cotidianos.

Los monederos Lightning, como todos los monederos móviles, se consideran monederos "calientes" porque están conectados a Internet. Por lo tanto, están pensados principalmente para gestionar pequeñas cantidades de dinero para tus gastos diarios. Para cantidades mayores, es preferible utilizar soluciones de almacenamiento más seguras, como los monederos físicos.

Si quieres saber más sobre la red Lightning y entender cómo funciona técnicamente, te recomiendo que sigas este curso:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
En este tutorial, echaremos un vistazo a **Lipa**, un monedero Lightning sencillo y eficaz desarrollado en Suiza.

## Presentación de Lipa

Lipa es un monedero Lightning sin custodia que se distingue por su sencillez de uso y su interfaz despejada. Desarrollada por un equipo suizo, hace hincapié en la confidencialidad y la facilidad de uso para principiantes.

Las características clave incluyen:


- Interfaz de usuario intuitiva
- Gestión autónoma de canales de rayos
- Compatibilidad con el protocolo LNURL
- Posibilidad de comprar bitcoins directamente en la aplicación

## Instalación y configuración de Lipa

El primer paso es descargar la aplicación Lipa. Por el momento, solo está disponible en iOS :


- [Para Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

La versión para Android está actualmente en desarrollo y estará disponible en breve.

![Installation de Lipa](assets/fr/01.webp)

Una vez que hayas lanzado la aplicación, llegarás a la pantalla de inicio, que te ofrece dos opciones:


- Crear una nueva cartera
- Restaurar una cartera existente a partir de una copia de seguridad

Una vez elegida la opción, la aplicación te pedirá que actives las notificaciones. Este paso es importante, ya que las notificaciones son necesarias para :


- Reciba alertas cuando se reciban pagos, incluso cuando la aplicación esté cerrada
- Infórmese de los pasos necesarios para comprar bitcoin a través de su solución integrada

A continuación, la aplicación presenta sus principales funciones a través de una serie de pantallas introductorias:


- Recepción de pagos sin problemas**: Los usuarios pueden recibir pagos Bitcoin incluso cuando la aplicación está cerrada, garantizando fiabilidad y comodidad.
- Direcciones Lightning no custodiadas**: Lipa ahora admite direcciones Lightning no custodiadas, lo que mejora la privacidad y la seguridad al ofrecer a los usuarios un control total sobre sus bitcoins.
- Control de los datos analíticos** : Para que la transparencia y la confidencialidad sean primordiales, los usuarios pueden ver los tipos de datos recopilados y elegir sus preferencias de compartición.
- Enviar a través del número de teléfono**: Sin necesidad de direcciones complejas: simplemente selecciona un contacto, introduce la cantidad y envía bitcoins directamente a su número de teléfono.

La aplicación también se beneficia de mejoras continuas en términos de estabilidad, seguridad y fiabilidad, para garantizar una experiencia de usuario óptima.

## Navegación por la aplicación

La interfaz de Lipa se organiza en torno a 4 pestañas principales accesibles a través de la barra de navegación situada en la parte inferior de la pantalla:

![Navigation principale](assets/fr/02.webp)


- Inicio**: Muestra el saldo actual y el historial de transacciones
- Escáner**: Permite escanear códigos QR para realizar pagos
- Mapa**: Muestra un mapa interactivo de los negocios que aceptan Bitcoin en tu zona
- Ajustes**: Acceso a los ajustes de la aplicación, copia de seguridad y preferencias

Se puede acceder a un menú adicional tirando hacia abajo de la pantalla de inicio:

![Menu supplémentaire](assets/fr/03.webp)

Este gesto revela funciones adicionales como :


- Comprar bitcoins
- Depósito de bitcoins en la cadena
- Creación de facturas Lightning para recibir bitcoins
- Pago de facturas relámpago

## Guarde su cartera

Para hacer una copia de seguridad de tu cartera, ve a la pestaña "Configuración" y selecciona "Frase de recuperación". Lipa utiliza una frase de recuperación que es imprescindible anotar cuidadosamente en un soporte físico (papel, metal). Esta frase es la única forma de recuperar tus fondos si pierdes o te roban el teléfono. Para validar tu copia de seguridad, la aplicación te pedirá que confirmes 3 palabras aleatorias de tu frase.

![Backup](assets/fr/04.webp)

Para más información sobre cómo hacer copias de seguridad y gestionar correctamente tu frase de recuperación, te recomiendo encarecidamente que sigas este otro tutorial, especialmente si eres principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Recibir bitcoins

Para recibir bitcoins, tienes dos opciones. Para acceder a estas opciones, vuelve a la pantalla de inicio y baja la pantalla. A continuación, puede :


- Selecciona "Transferir BTC" para recibir bitcoins en la cadena. A continuación, simplemente escanea el código QR con tu otro monedero y completa la transacción.
- Seleccione "Solicitar" para recibir a través de la red Lightning e introduzca el importe que desea recibir.

En ambos casos, tendrá que pagar una tasa equivalente al 0,4% del importe, o alrededor de 2.500 sats si la aplicación tiene que abrir un nuevo canal de pago (lo que inevitablemente ocurrirá con el primer pago).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Enviar bitcoins

Para enviar bitcoins, vaya a la pantalla de inicio, baje la pantalla y seleccione "Pagar". A continuación, simplemente :


- introduzca una dirección LNURL de rayos
- escanear un código QR de iluminación para efectuar el pago.

También puedes ir a la segunda pestaña de la parte inferior de la pantalla para escanear directamente un código QR.

![Envoi de bitcoins](assets/fr/07.webp)

## Comprar bitcoins

Lipa ofrece la posibilidad de comprar bitcoins directamente en la aplicación por una comisión del 1,5%. Para realizar una compra, ve a la pantalla de inicio y tira hacia abajo para desplegar el menú. A continuación, selecciona "Comprar BTC". Tres pantallas introductorias le guiarán a través del proceso de compra.

![Menu d'achat](assets/fr/08.webp)

A continuación, introduzca los datos bancarios de la cuenta que utilizará para realizar la compra. Elija la divisa e introduzca su dirección de correo electrónico.

Tras la pantalla de carga, encontrarás el número de referencia que debes incluir en la transferencia que vas a realizar, así como los datos bancarios para el canje.

![Sélection du montant](assets/fr/09.webp)

Sólo tienes que utilizar tu banco para transferir el importe deseado, configurar la transferencia indicando el RIB previamente recuperado e indicar la referencia en el momento de la transacción para que Lipa pueda asociar este movimiento bancario a tu monedero Lipa.

![Confirmation d'achat](assets/fr/10.webp)

## Ventajas e inconvenientes

### Beneficios


- Interfaz intuitiva
- Gastos de servicio correctos
- Sin custodia
- Solución integrada de compra en bitcoin
- Integración de BTCmap
- Compatibilidad con NFC

### Desventajas


- No es posible enviar bitcoins en cadena
- Pago ligeramente superior a la media

Lipa es una excelente opción para iniciarse en la red Lightning, especialmente indicada para usuarios que buscan una solución sencilla para los pagos cotidianos. Su facilidad de uso y su interfaz despejada la convierten en una cartera ideal para principiantes, al tiempo que ofrece las funciones esenciales para el uso diario de Lightning.

## Recursos


- [Sitio web oficial de Lipa](https://lipa.swiss/)
- [Apoyo a Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)