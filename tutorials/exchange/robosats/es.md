---
name: Robosats

description: Cómo usar Robosats
---

![cover](assets/cover.jpeg)

# Robosats

RoboSats (https://learn.robosats.com/) es una forma fácil de intercambiar Bitcoin por monedas nacionales de forma privada. Simplifica la experiencia peer-to-peer y utiliza facturas de retención de rayos para minimizar los requisitos de custodia y confianza.

![video](https://youtu.be/XW_wzRz_BDI)

## Guía

> Esta guía es de Bitocin Q&A (https://bitcoiner.guide/robosats/). Todo el crédito para él, apóyalo allí (https://bitcoiner.guide/contribute); BitcoinQ&A también es un mentor de Bitcoin. ¡Contáctalo para recibir mentoría!

![image](assets/0.png)

RoboSats - Un intercambio P2P simple y privado basado en Lightning

## Antes de comenzar

### Cosas que necesitas saber

| Término                    | Definición                                                                                                                                                                                                                  |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot                      | Tu identidad de intercambio privado generada automáticamente. No reutilices el mismo robot más de una vez, ya que esto puede degradar tu privacidad.                                                                        |
| Token                      | Una cadena de caracteres aleatorios utilizada para generar tu robot único.                                                                                                                                                  |
| Creador                    | Un usuario que crea una oferta para comprar o vender Bitcoin.                                                                                                                                                               |
| Tomador                    | Un usuario que acepta la oferta de otro usuario para comprar o vender Bitcoin.                                                                                                                                              |
| Fianza                     | Una cantidad de Bitcoin bloqueada por ambos pares como garantía para jugar limpio y completar su parte del intercambio. Las fianzas suelen ser el 3% del monto total del intercambio y están respaldadas por facturas Hodl. |
| Fideicomiso de intercambio | Utilizado por el vendedor como un método para retener la cantidad de Bitcoin del intercambio, nuevamente utilizando facturas Hodl.                                                                                          |
| Tarifas                    | RoboSats cobra el 0,2% del monto del intercambio, que se divide entre el creador y el tomador. El tomador paga el 0,175% y el creador paga el 0,025%.                                                                       |

## Cosas que necesitas tener

### Una billetera Lightning

RoboSats es nativo de Lightning, por lo que necesitarás una billetera Lightning para financiar la fianza y recibir los sats comprados como comprador. Debes tener cuidado al elegir tu billetera, debido a la tecnología utilizada para que RoboSats funcione, no todas son compatibles.

Si eres un operador de nodo, Zeus es, con mucho, la mejor opción. Si no tienes tu propio nodo, te recomendaría Phoenix, una billetera móvil multiplataforma con una configuración sencilla y acceso a Lightning. Phoenix se utilizó en la producción de esta guía.

### Algunos Bitcoin

Los compradores y vendedores deben financiar una fianza antes de que se pueda realizar cualquier intercambio. Esto suele ser una cantidad muy pequeña (~3% del monto del intercambio), pero es un requisito previo de todos modos.

¿Usando RoboSats para comprar tus primeros sats? ¿Por qué no pedirle a un amigo que te preste la pequeña cantidad necesaria para comenzar? Si estás solo, aquí tienes algunas otras opciones excelentes para obtener algunos sats sin KYC para comenzar.

### Acceso a RoboSats

¡Obviamente necesitarás acceder a RoboSats! Hay cuatro formas principales en las que puedes hacer esto:

1. A través del navegador Tor (¡Recomendado!)
2. A través de un navegador web regular (¡No recomendado!)
3. A través del APK de Android
4. Tu propio cliente

Si eres nuevo en el navegador Tor, obtén más información y descárgalo [aquí](https://www.torproject.org/download/).
Una nota rápida para los usuarios de iOS que deseen acceder a RoboSats a través de Tor desde sus teléfonos. 'Onion Browser' no es Tor Browser. En su lugar, utiliza Orbot + Safari y Orbot + DuckDuckGo.

## Compra de Bitcoin

Los siguientes pasos se realizaron en mayo de 2023 utilizando la versión 0.5.0, accedida a través del navegador Tor. Los pasos deberían ser idénticos para los usuarios que acceden a RoboSats a través del APK de Android.

En el momento de escribir esto, RoboSats todavía está en desarrollo activo, por lo que la interfaz puede cambiar un poco en el futuro, pero los pasos básicos necesarios para completar la transacción deberían permanecer en gran medida sin cambios.

> Cuando cargues RoboSats por primera vez, te encontrarás con esta página de inicio. Haz clic en "Start".

![image](assets/2.png)

Genera tu token y guárdalo en un lugar seguro, como una aplicación de notas encriptadas o un gestor de contraseñas. Este token se puede utilizar para recuperar tu ID de Robot temporal en caso de que tu navegador o aplicación se cierre a mitad de una transacción.

![image](assets/3.png)

Conoce a tu nueva identidad de Robot, luego haz clic en "Continue".

![image](assets/4.png)

Haz clic en "Offers" para navegar por el libro de órdenes. En la parte superior de la página, puedes filtrar según tus preferencias. Asegúrate de tomar nota de los porcentajes de garantía y la prima sobre la tasa de cambio promedio.

- Elige "Buy"
- Elige tu moneda
- Elige tu(s) método(s) de pago

![image](assets/5.png)

> Haz clic en la oferta que deseas aceptar. Ingresa la cantidad (en tu moneda fiduciaria elegida) que deseas comprar al vendedor, luego revisa los detalles por última vez y haz clic en "Take Order".

Si el vendedor no está en línea (indicado por un punto rojo en su imagen de perfil), verás una advertencia de que la transacción podría llevar más tiempo de lo habitual. Si continúas y el vendedor no procede a tiempo, se te compensará con el 50% del monto de su garantía por tu tiempo perdido.

![image](assets/6.png)

A continuación, debes bloquear tu garantía de transacción pagando la factura en pantalla. Esta es una factura de retención que se congela en tu billetera. Solo se te cobrará si no completas tu parte de la transacción.

![image](assets/7.png)

En tu billetera Lightning, escanea el código QR y paga la factura.

![image](assets/8.png)

A continuación, en tu billetera Lightning, genera una factura por la cantidad mostrada y pégala en el espacio proporcionado.

![image](assets/9.png)

Espera a que el vendedor bloquee la cantidad de su transacción. Cuando esto ocurra, RoboSats pasará automáticamente al siguiente paso, donde se abrirá la ventana de chat. Saluda y pide al vendedor su información de pago en moneda fiduciaria. Una vez proporcionada, envía el pago a través del método elegido y confírmalo en RoboSats. Todo el chat en RoboSats está encriptado con PGP, lo que significa que solo tú y tu compañero de transacción pueden leer los mensajes.

![image](assets/10.png)

Una vez que el vendedor confirme la recepción del pago, RoboSats liberará automáticamente el pago utilizando la factura proporcionada anteriormente.

![image](assets/11.png)

Cuando se pague la factura, la transacción estará terminada y tu garantía se desbloqueará. Luego verás un resumen de la transacción.

![image](assets/12.png)

Verifica en tu billetera Lightning que los sats hayan llegado.

![image](assets/13.png)

## Funciones adicionales

Además de la obvia compra y venta de Bitcoin, RoboSats tiene algunas otras características que debes conocer.
Garaje de Robots
¿Quieres tener múltiples operaciones al mismo tiempo, pero no quieres compartir la misma identidad en todas ellas? ¡No hay problema! Haz clic en la pestaña de Robot, genera un Robot adicional y crea o toma tu próxima orden.
![image](assets/14.png)

### Creación de órdenes

Además de aceptar la oferta de otra persona, puedes crear la tuya propia y esperar a que otro Robot venga a ti.

- Abre la página de Crear.
- Define si tu orden es para comprar o vender Bitcoin.
- Ingresa la cantidad y la moneda con la que deseas comprar/vender.
- Ingresa el método de pago que estás dispuesto a utilizar.
- Ingresa el porcentaje de 'Prima sobre el mercado' que estás dispuesto a aceptar. Ten en cuenta que este puede ser un número negativo para ofertar a un descuento respecto al precio actual del mercado.
- Haz clic en Crear Orden.
- Paga la factura de Lightning para bloquear tu Fianza de Creador.
- Tu orden ahora está activa. Siéntate y espera a que alguien la acepte.

![image](assets/15.png)

### Pagos en cadena

RoboSats se centra en Lightning, pero los compradores tienen la opción de recibir sus sats en una dirección de Bitcoin en cadena. Los compradores pueden seleccionar esta opción después de bloquear su fianza. Después de seleccionar en cadena, el comprador verá una descripción general de las tarifas. Las tarifas adicionales para este servicio incluyen:

- Una tarifa de intercambio recolectada por RoboSats: esta tarifa es dinámica y varía según lo ocupada que esté la red de Bitcoin.
- Una tarifa de minería para la transacción de pago: esto es configurable por el comprador.

![image](assets/16.png)

### Intercambios P2P

RoboSats permite a los usuarios intercambiar sats dentro o fuera de su billetera Lightning. Simplemente haz clic en el botón de intercambio en la parte superior de la página de ofertas para ver las ofertas de intercambio actuales.

Como comprador de una oferta de 'Intercambio de entrada', envías Bitcoin en cadena al par y recibes sats de vuelta, menos las tarifas y/o primas anunciadas, en tu billetera Lightning. Como comprador de una oferta de 'Intercambio de salida', envías sats a través de Lightning y recibes Bitcoin, menos cualquier tarifa y/o prima, en tu dirección en cadena. Los usuarios de Samourai o Sparrow Wallet también pueden aprovechar la función Stowaway para completar un intercambio.

Las ofertas de intercambio de RoboSats también pueden incorporar alternativas vinculadas a Bitcoin que incluyen RBTC, LBTC y WBTC. Debes tener mucho cuidado al interactuar con estos tokens, ya que todos tienen diferentes compensaciones. ¡El Bitcoin vinculado no es Bitcoin!

![image](assets/17.png)

### Ejecuta tu propio cliente de RoboSats

Los usuarios de nodos Umbrel, Citadel y Start9 pueden instalar su propio cliente de RoboSats directamente en su nodo. Los beneficios de hacerlo se enumeran como:

- Tiempos de carga dramáticamente más rápidos.
- Más seguro: tú controlas qué aplicación de cliente de RoboSats ejecutas.
- Accede a RoboSats de forma segura desde cualquier navegador/dispositivo. No es necesario usar TOR si estás en tu red local o utilizando una VPN: tu backend de nodo se encarga de la torificación necesaria para la anonimización.
- Permite controlar a qué coordinador de mercado P2P te conectas (por defecto, robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.png)

## Preguntas frecuentes

### ¿Puedo ser estafado?

Como comprador, si has enviado el dinero fiat requerido para tu parte del intercambio, pero el vendedor no te libera los sats, puedes abrir una disputa. Si durante este proceso de disputa puedes demostrar a los árbitros de RoboSats que enviaste el dinero fiat, los fondos en garantía del vendedor y su bono de intercambio serán liberados para ti. ¿Cómo cancelo un intercambio?

Puedes cancelar un intercambio después de publicar tu bono haciendo clic en el botón de Cancelación Colaborativa dentro del menú de intercambio. Si tu compañero de intercambio está de acuerdo en cancelar, no incurrirás en ninguna tarifa. Pero si tu compañero de intercambio quiere completar el intercambio y tú decides cancelarlo de todos modos, perderás tu bono de intercambio.

### ¿RoboSats funciona con el método de pago 'X'?

No hay restricciones en los métodos de pago en RoboSats. Si no ves ninguna oferta en tu método deseado, ¡crea tu propia oferta usándolo!

![image](assets/19.png)

### ¿Qué información obtiene RoboSats sobre mí cuando lo uso?

¡Si utilizas RoboSats a través de Tor o la aplicación de Android, no obtiene ninguna información sobre ti! Obtén más información aquí.

- Tor protege tu privacidad en la red.
- El cifrado PGP mantiene privado tu chat de intercambio.
- No hay cuentas, lo que significa un Robot por intercambio. Esto significa que RoboSats no puede relacionar múltiples intercambios con una sola entidad.

Sin embargo, hay algunas advertencias. Lightning es bastante privado como remitente, pero no como receptor. Si recibes en tu propio nodo Lightning, tu ID de nodo se comparte en tus facturas. Este ID de nodo le da a cualquier persona con conocimiento de él un punto de partida para intentar vincular tu actividad en la cadena. Esto también es cierto si un usuario elige recibir su intercambio a través de un pago en la cadena.

Para mitigar esto, los usuarios pueden optar por utilizar una solución como una billetera Proxy para Lightning o Coinjoin para la cadena.

### Federación

Actualmente hay un único coordinador de RoboSats operado por el equipo de desarrollo de RoboSats. En Bitcoin, cualquier forma de centralización facilita el objetivo de los gobiernos o reguladores que pueden no ver con buenos ojos un servicio específico.

Siendo RoboSats un proyecto de código abierto, cualquiera podría tomar el código y comenzar a ejecutar su propio coordinador. Si bien esto descentraliza en cierta medida el riesgo de un único objetivo, también fragmenta un mercado de liquidez ya escaso.

El equipo de RoboSats es consciente de esto y ha comenzado a trabajar en un modelo federado. Como usuario final, esto no debería cambiar mucho el flujo de intercambio demostrado anteriormente, pero habrá vistas o pantallas adicionales para que agregues o elimines diferentes coordinadores que surjan.

FIN de la guía
https://bitcoiner.guide/robosats/
