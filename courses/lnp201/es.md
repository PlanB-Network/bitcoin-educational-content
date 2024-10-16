---
name: Introducción teórica al Lightning Network
goal: Descubrir el Lightning Network desde un enfoque técnico
objectives:
  - Comprender el funcionamiento de los canales de la red.
  - Familiarizarse con los términos HTLC, LNURL y UTXO.
  - Asimilar la gestión de la liquidez y las tarifas del LNN.
  - Reconocer el Lightning Network como una red.
  - Comprender los usos teóricos del Lightning Network.
---

# Un viaje hacia la segunda capa de Bitcoin

Este curso es una formación teórica sobre el funcionamiento técnico del Lightning Network.

Bienvenido al emocionante mundo del Lightning Network, una segunda capa de Bitcoin, que es una avanzada tecnológica sofisticada y rica en potencialidades. Nos estamos preparando para sumergirnos en las profundidades técnicas de esta tecnología, sin centrarnos en tutoriales o escenarios de uso específicos. Para aprovechar al máximo esta formación, es indispensable tener una sólida comprensión de Bitcoin. Es una experiencia que requiere un enfoque serio y concentrado. También puede considerar tomar el curso LN 202 en paralelo, que ofrece un aspecto más práctico a esta exploración. Prepárese para embarcarse en un viaje que podría cambiar su percepción del ecosistema Bitcoin.

¡Buen descubrimiento!

+++

# Los fundamentales
<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Comprender el Lightning Network
<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![video](https://youtu.be/w9y0WsioH2c)

La red Lightning es una infraestructura de pago de segunda capa, construida sobre la red Bitcoin, que permite transacciones rápidas y económicas. Para comprender completamente cómo funciona la red Lightning, es esencial entender qué son los canales de pago y cómo funcionan.

Un canal de pago en Lightning es una especie de "vía privada" entre dos usuarios, que permite transacciones Bitcoin rápidas y repetitivas. Cuando se abre un canal, se le asigna una capacidad fija, que es definida de antemano por los usuarios. Esta capacidad representa la cantidad máxima de Bitcoin que se puede transmitir en el canal en un momento dado.

Los canales de pago son bidireccionales, lo que significa que tienen dos "lados". Por ejemplo, si Alice y Bob abren un canal de pago, Alice puede enviar Bitcoin a Bob y Bob puede enviar Bitcoin a Alice. Las transacciones dentro del canal no modifican la capacidad total del canal, pero sí modifican la distribución de esa capacidad entre Alice y Bob.

![explication](assets/chapitre1/0.webp)

Para que una transacción sea posible en un canal de pago Lightning, el usuario que envía los fondos debe tener suficiente Bitcoin en su lado del canal. Si Alice desea enviar 1 Bitcoin a Bob a través de su canal, debe tener al menos 1 Bitcoin en su lado del canal.
Límites y Funcionamiento de los Canales de Pago en Lightning
Aunque la capacidad de un canal de pago Lightning es fija, esto no limita el número total de transacciones ni el volumen total de Bitcoin que se puede transmitir a través del canal. Por ejemplo, si Alice y Bob tienen un canal con una capacidad de 1 Bitcoin, pueden realizar cientos de transacciones de 0,01 Bitcoin o miles de transacciones de 0,001 Bitcoin, siempre y cuando la capacidad total del canal no se exceda en un momento dado.

A pesar de estas limitaciones, los canales de pago Lightning son una forma eficaz de realizar transacciones de Bitcoin rápidas y económicas. Permiten a los usuarios enviar y recibir Bitcoin sin tener que pagar altas tarifas de transacción o esperar largos períodos de confirmación en la red de Bitcoin.

En resumen, los canales de pago en Lightning ofrecen una solución poderosa para aquellos que desean realizar transacciones de Bitcoin rápidas y económicas. Sin embargo, es esencial comprender su funcionamiento y limitaciones para poder aprovecharlos al máximo.

![explication](assets/chapitre1/1.webp)

Ejemplo:

- Alice tiene 100,000 SAT
- Bob tiene 30,000 SAT

Este es el estado actual del canal. En una transacción, Alice decide enviar 40,000 SAT a Bob. Puede hacerlo porque 40,000 < 100,000.

El nuevo estado del canal es:

- Alice 60,000 SAT
- Bob 70,000 SAT

```
Estado inicial del canal:
Alice (100,000 SAT) ============== Bob (30,000 SAT)

Después de la transferencia de Alice a Bob de 40,000 SAT:
Alice (60,000 SAT) ============== Bob (70,000 SAT)

```

![explication](assets/chapitre1/2.webp)

Ahora, Bob quiere enviar 80,000 SAT a Alice. Como no tiene la liquidez, no puede hacerlo. La capacidad máxima del canal es de 130,000 SAT, con un gasto posible de hasta 60,000 SAT para Alice y 70,000 SAT para Bob.

![explication](assets/chapitre1/3.webp)

## Bitcoin, direcciones, UTXO y transacciones
<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![video](https://youtu.be/zS_isbMwT28)

En este segundo capítulo, nos tomamos el tiempo para estudiar cómo funcionan realmente las transacciones de Bitcoin, lo que nos será muy útil para entender Lightning. También nos detenemos un momento en la noción de dirección multi-firma, que es fundamental para entender el próximo capítulo dedicado a la apertura de canales en la red Lightning.

- Clave privada > Clave pública > Dirección: En una transacción, Alice envía dinero a Bob. Este último proporciona una dirección dada por su clave pública. Alice, que ella misma recibió el dinero en una dirección a través de su clave pública, ahora usa su clave privada para firmar la transacción y desbloquear los bitcoins de la dirección.
- En una transacción, en Bitcoin todos los bitcoins deben moverse. Llamado UTXO (Unspent Transaction Output), los fragmentos de bitcoin se moverán todos para luego volver al propietario mismo.
  Alice tiene 0.002 BTC y Bob no tiene nada. Alice decide enviar 0.0015 BTC a Bob. Ella firma una transacción de 0.002 BTC donde 0.0015 van a Bob y 0.0005 vuelven a su billetera.

![explication](assets/chapitre2/0.webp)

Aquí, de una UTXO (Alice tiene 0.0002 BTC en una dirección), hemos creado 2 UTXO (Bob tiene 0.0015 y Alice ha recuperado una nueva UTXO (independiente de la anterior) de 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Transacción de Bitcoin (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (nueva UTXO: 0.0005 BTC)
```

En Lightning Network, se utilizan multisig. Por lo tanto, se necesitan 2 firmas para desbloquear los fondos, es decir, dos claves privadas para mover el dinero. Por lo tanto, pueden ser Alice y Bob quienes, juntos, deben aceptar desbloquear el dinero (UTXO). En LN específicamente, son transacciones 2/2, por lo que se necesitan absolutamente las 2 firmas, a diferencia de los multisig 2/3 o 3/5 donde solo se necesita una combinación del número completo de claves.

![explication](assets/chapitre2/1.webp)

# Apertura y cierre de canales
<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura de canal
<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![video](https://youtu.be/G9Fz1C4xf4Q)

Ahora, nos enfocamos más detalladamente en la apertura de canal y cómo se realiza a través de una transacción de Bitcoin.

Lightning Network tiene diferentes niveles de comunicación:

- Comunicación p2p (protocolo Lightning Network)
- Canal de pago (protocolo Lightning Network)
- Transacción de Bitcoin (protocolo Bitcoin)

![explication](assets/chapitre3/0.webp)

Para abrir un canal, los dos pares hablan a través de un canal de comunicación:

- Alice: "¡Hola, quiero abrir un canal!"
- Bob: "De acuerdo, aquí está mi dirección pública".

![explication](assets/chapitre3/1.webp)

Ahora, Alice tiene 2 direcciones públicas para crear una dirección multisig 2/2. Ahora puede hacer una transacción de Bitcoin para enviar dinero allí.

Supongamos que Alice tiene una UTXO de 0.002 BTC y quiere abrir un canal con Bob de 0.0013 BTC. Por lo tanto, creará una transacción con 2 UTXO de salida:

- un UTXO de 0.0013 hacia la dirección multisig 2/2
- un UTXO de 0.0007 hacia una de sus direcciones de cambio (retorno de UTXO).

Esta transacción aún no es pública porque, en este punto, confía en Bob para poder desbloquear el dinero de la multisig.

¿Pero cómo hacerlo?

Alice creará una segunda transacción llamada "transacción de retiro" antes de publicar el depósito de fondos en la multisig.

![explication](assets/chapitre3/2.webp)

La transacción de retiro gastará los fondos de la dirección multisig hacia una dirección suya (esto antes de que todo se publique).
Une vez construidas las dos transacciones, Alice le informa a Bob que está hecho y le pide que firme con su clave pública explicándole que así podrá recuperar sus fondos si algo sale mal. Bob acepta porque no es deshonesto.
Por lo tanto, Alice puede recuperar los fondos sola, ya tiene la firma de Bob. Luego publica las transacciones. El canal está abierto con 0.0013 BTC (130,000 SAT) del lado de Alice.

![explication](assets/chapitre3/3.webp)

## Transacción Lightning y de compromiso
<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![video](https://youtu.be/1sHUdqA7J04)

Ahora analicemos lo que realmente sucede detrás de escena cuando se transfieren fondos de un lado a otro de un canal en la red Lightning, con la noción de transacción de compromiso. La transacción de retiro/cierre on-chain representa el estado del canal, lo que garantiza quién posee los fondos después de cada transferencia. Por lo tanto, después de una transferencia en la red Lightning, hay una actualización de esta transacción/contrato no realizado entre los dos pares, Alice y Bob, creando una misma transacción con el estado actual del canal en caso de cierre:

![cover](assets/chapitre4/1.webp)

- Alice crea un canal con Bob con 130,000 SAT de su lado. La transacción de retiro aceptada por ambos en caso de cierre dice que 130,000 SAT irán a Alice al cierre, Bob está de acuerdo porque es justo.

![cover](assets/chapitre4/2.webp)

- Alice envía 30,000 SAT a Bob. Por lo tanto, hay una nueva transacción de retiro que dice que en caso de cierre, Alice recibirá 100,000 SAT y Bob 30,000 SAT. Ambos están de acuerdo porque es justo.

![cover](assets/chapitre4/3.webp)

- Alice envía 10,000 SAT a Bob, se crea una nueva transacción de retiro para decir que Alice recuperará 90,000 SAT y Bob 40,000 SAT. Ambos están de acuerdo porque es justo.

![cover](assets/chapitre4/4.webp)


```
Estado inicial del canal:
Alice (130,000 SAT) =============== Bob (0 SAT)

Después de la primera transferencia:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Después de la segunda transferencia:
Alice (90,000 SAT) =============== Bob (40,000 SAT)

```

El dinero nunca se mueve, pero el saldo final se actualiza a través de una transacción firmada pero no publicada on-chain. Por lo tanto, la transacción de retiro es una transacción de compromiso. Las transferencias de satoshis son otra transacción de compromiso más reciente que actualiza el saldo.

## Transacciones de compromiso
<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

![video](https://youtu.be/GrXSB-nLvjE)

Si las transacciones de compromiso dictan un estado del canal con la liquidez en el momento X, ¿se puede hacer trampa publicando un estado antiguo? La respuesta es sí, porque ya se tiene la pre-firma de los dos participantes en la transacción no publicada.


![instruction](assets/Chapitre5/0.webp)

Para resolver este problema, agregaremos complejidad:

- Timelock = fondos bloqueados hasta el bloque N
- Clave de revocación = secreto de Alice y secreto de Bob'

Esos dos élémentos son añadidos a la transacción de compromiso. Por lo tanto, Alice debe esperar necesariamente el final del Timelock, y cualquier persona que tenga la clave de revocación puede mover los fondos sin esperar el final del Timelock. Si Alice intenta hacer trampa, Bob usa la clave de revocación para robar y castigar a Alice.

![instruction](assets/Chapitre5/1.webp)

A partir de ahora (y en realidad), la transacción de compromiso no es la misma para Alice y Bob, son simétricos pero cada uno con diferentes restricciones, se dan mutuamente su secreto para crear la clave de revocación de la transacción de compromiso anterior. Por lo tanto, al crear el canal con Bob, Alice crea 130,000 SAT de su lado, tiene un Timelock que le impide recuperar su dinero de inmediato, debe esperar un poco. La clave de revocación puede desbloquear el dinero, pero solo Alice la tiene (transacción de compromiso de Alice). Una vez que hay una transferencia, Alice proporcionará su antiguo secreto a Bob y, por lo tanto, este último podrá vaciar el canal al estado anterior en caso de trampa de Alice (Alice es castigada).

![instruction](assets/Chapitre5/2.webp)

De la misma manera, Bob proporcionará su secreto a Alice para que si intenta hacer trampa, Alice pueda castigarlo. La operación se repite en cada nueva transacción de compromiso. Se decide un nuevo secreto y una nueva clave de revocación. Por lo tanto, para cada nueva transacción, es necesario destruir la transacción de compromiso anterior dando el secreto de revocación. Por lo tanto, si Alice o Bob intentan hacer trampa, el otro puede actuar antes (gracias al Timelock) y evitar un engaño. En la transacción n°3, se da el secreto de la transacción n°2 para permitir que Alice y Bob se defiendan contra Alice o Bob.

![instruction](assets/Chapitre5/3.webp)

La persona que crea la transacción con el Timelock (quien envía el dinero) solo puede usar la clave de revocación después del Timelock. Sin embargo, la persona que recibe el dinero puede usarlo antes del Timelock en caso de trampa de un lado a otro de un canal en la Red Lightning. En particular, detallamos los mecanismos que permiten protegerse contra una posible trampa por parte de su par dentro del canal.

## Cierre del canal
<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![video](https://youtu.be/zg-7PXwNRPc)

Nos interesamos por el cierre del canal a través de una transacción de Bitcoin, que puede tomar diferentes formas según el caso. Existen 3 tipos de cierre de canal:

- El bueno: cierre cooperativo
- El malo: cierre forzado (no cooperativo)
- El feo: cierre por un tramposo

![instruction](assets/chapitre6/1.webp)
![instruction](assets/chapitre6/0.webp)


### El bueno

Los dos pares hablan y acuerdan cerrar el canal. Por lo tanto, detienen todas las transacciones y validan un estado final del canal. Acuerdan las tarifas de red (la persona que abre el canal paga las tarifas de cierre). Ahora crean la transacción de cierre. Por lo tanto, hay una transacción de cierre, diferente de las transacciones de compromiso porque no hay Timelock ni clave de revocación. La transacción se publica y Alice y Bob reciben sus respectivos saldos. Este tipo de cierre es rápido (porque no hay Timelock) y generalmente de bajo costo.

![instruction](assets/chapitre6/3.webp)

### El bruto

Alice quiere cerrar el canal, se comunica pero Bob no responde porque está desconectado (corte de internet o electricidad). Por lo tanto, Alice publicará la transacción de compromiso más reciente (la última). La transacción se publica y se activa el Timelock. Entonces, ¡las tarifas se decidieron cuando se creó esta transacción hace X tiempo en el pasado! La MemPool es la red que ha cambiado desde entonces, por defecto el protocolo utiliza tarifas 5 veces superiores a las actuales en el momento de la creación de la transacción. Creación de tarifas a 10 SAT, por lo que la transacción consideró 50 SAT. En el momento de la publicación forzada, la transacción de cierre de la red es:

- 1 SAT = sobrepagado por 50\*
- 100 SAT = subpagado por 2\*

Esto hace que el cierre forzado sea más largo (Timelock) y sobre todo más arriesgado en términos de tarifas y, por lo tanto, posible validación por parte de los mineros.

![instruction](assets/chapitre6/4.webp)

### El tramposo

Alice intenta hacer trampa publicando una transacción de compromiso antigua. Pero Bob vigila la MemPool y espera si hay transacciones que intentan publicar antiguas. Si encuentra alguna, utiliza la clave de revocación para castigar a Alice y tomar todos los SAT del canal.

![instruction](assets/chapitre6/5.webp)

En conclusión, el cierre del canal en Lightning Network es un paso crucial que puede tomar diversas formas. En un cierre cooperativo, ambas partes se comunican y acuerdan un estado final del canal. Es la opción más rápida y menos costosa. Por otro lado, un cierre forzado ocurre cuando una de las partes no responde. Es una situación más costosa y más larga debido a las tarifas de transacción impredecibles y la activación del Timelock. Finalmente, si un participante intenta hacer trampa publicando una transacción de compromiso antigua, el tramposo, puede ser castigado perdiendo todos los SAT del canal. Por lo tanto, es crucial comprender estos mecanismos para una utilización eficaz y justa de Lightning Network.

# Una red de liquidez
<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network
<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![video](https://youtu.be/4UGonGv0toY)

En este séptimo capítulo, estudiamos el funcionamiento de Lightning como una red de canales y cómo se enrutan los pagos desde su origen hasta su destino.
Lightning es una red de canales de pago. Miles de pares con sus propios canales de liquidez están conectados entre sí, y así se autoutilizan para realizar transacciones entre pares no conectados.

![cover](assets/Chapitre7/0.webp)
![cover](assets/Chapitre7/1.webp)

La liquidez de los canales no puede transferirse a otros canales de liquidez.

`Alice -> Eden - > Bob`. Los satoshis no se movieron de `Alice -> Bob`, sino de `Alice -> Edén` y de `Edén -> Bob`.

Así que cada persona y cada canal tienen una liquidez diferente. Para hacer pagos, hay que encontrar una ruta en la red con suficiente liquidez. Si no hay suficiente, el pago no se realizará.

Consideremos la siguiente red:

```
Estado inicial de la red:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.webp)

Si Alice va a realizar una transferencia de 40 SAT a Bob, la liquidez se redistribuirá a lo largo de la ruta entre las dos partes.

```
Después de que Alice transfiera 40 SAT a Bob :
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.webp)

Sin embargo, en el estado inicial, Bob no puede enviar 40 SAT a Alice porque Susie no tiene liquidez con Alice para enviarle 40 SAT, por lo que el pago no es posible a través de esta ruta. Por tanto, necesitamos otra ruta en la que la transacción sea imposible.

En el primer ejemplo, está claro que Susie y Eden no han ganado ni perdido nada. Para aceptar ser utilizados como ruta de la transacción, los nodos de la Lightning Network cobran una comisión.

Existen diferentes tarifas en función de dónde se encuentre la liquidez

Alice - Bob

- Comisión de Alice = Alice -> Bob
- Comisión de Bob = Bob -> Alice

![cover](assets/Chapitre7/5.webp)

Existen dos tipos de comisión

- una comisión fija independientemente del importe: 1 SAT (por defecto, pero puede modificarse)
- una comisión variable (0,01% por defecto)

Ejemplo de tasa:

- Alice - Susie; 1/1 (1 cargo fijo y 1 cargo variable)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Por lo tanto :

- Comisión 1: (pagada por Alice a sí misma) 1 + (40.000\*0,000001)
- Coste 2: 0 + 40.000 \* 0,0002 = 8 SAT
- Coste 3: 1 + 40.000\* 0,000001 = 0,4 SAT

![cover](assets/Chapitre7/6.webp)

Envío :

1. Envío de 40.009,04 Alice -> Susie; Alice paga sus propios gastos, por lo que no cuenta.
2. Susie le hace el favor a Eden de enviar 40.001,04, se lleva esta comisión de 8 SAT
3. Eden hace el servicio de enviar 40.000 a Bob, se lleva su comisión de 1,04 SAT.

Alice pagó una comisión de 9,04 SAT y Bob recibió 40.000 SAT.

![cover](assets/Chapitre7/7.webp)

En el LN, es el nodo de Alice el que decide la ruta antes del envío. Por lo tanto, hay una búsqueda de la mejor ruta y Alice es la única que conoce la ruta y el precio. El pago se envía pero Susie no tiene información.

![cover](assets/Chapitre7/9.webp)

Para Susie o Eden: no saben quién es el destinatario final ni quién envía. Esto es un enrutamiento en cebolla. El nodo debe mantener un plan de la red para encontrar su ruta, pero ninguno de los intermediarios tiene información.

## HTLC - Contrato de tiempo bloqueado y hash
<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![video](https://youtu.be/5ZGKt6O5gGo)

En un sistema de enrutamiento clásico, ¿cómo asegurarse de que Eden no haga trampa y cumpla con su parte del contrato?

Por lo tanto, HTLC es un contrato de pago en el que solo se puede desbloquear con un secreto. Si no se revela, entonces el contrato expira. Es, por lo tanto, un pago condicional. ¿Cómo se utilizan?

![instruction](assets/chapitre8/0.webp)

Consideremos la siguiente situación
`Alice (100 000 SAT) ==== (30 000 SAT) Susie (250 000 SAT) ==== (0 SAT) Bob`

- Bob genera un secreto S (la preimagen) y calcula el hash r = hash(s)
- Bob envía una factura a Alice con "r"
- Alice envía un HTLC de 40,000 SAT a Susie con la condición de revelar "s'" tal que hash(s') = r
- Susie envía un HTLC similar a Bob
- Bob desbloquea el HTLC de Susie mostrándole "s"
- Susie desbloquea el HTCL de Alice mostrándole "S"

Si Bob está desconectado y nunca recupera el secreto que le da la legitimidad de recibir el dinero, en este caso, el HTLC expirará después de un cierto número de bloques.

![instruction](assets/chapitre8/1.webp)

Los HTLC expiran en orden inverso: por lo tanto, la expiración de Susie - Bob y luego Alice - Susie.
De esta manera, si Bob regresa, no cambia nada. De lo contrario, si Alice cancela mientras Bob regresa, será un desastre y la gente puede haber trabajado para nada.

Bueno, ¿y entonces, qué pasa en caso de cierre? De hecho, nuestras transacciones de compromiso son aún más complejas. Es necesario representar el equilibrio intermedio si el canal se cierra.

Por lo tanto, hay un HTLC-out de 40,000 satoshis (con las limitaciones vistas anteriormente) en la transacción de compromiso a través de una salida n°3.

![instruction](assets/chapitre8/2.webp)

Por lo tanto, Alice tiene en la transacción de compromiso:

- Salida n°1: 60,000 SAT para Alice a través de un Timelock y una clave de revocación (lo que le queda)
- Salida n°2: 30,000 que ya pertenecen a Susie
- Salida n°3: 40,000 en HTLC

La transacción de compromiso de Alice es con un HTCL-out porque envía a la destinataria, Susie, un HTLC-in.

![instruction](assets/chapitre8/3.webp)

Por lo tanto, si publicamos esta transacción de compromiso, Susie puede recuperar el dinero de HTCL con la imagen "s". Si no tiene la preimagen, Alice recupera el dinero una vez que el HTCL expire. Piense en las salidas (UTXO) como diferentes pagos con diferentes condiciones.
Una vez que se realiza el pago (vencimiento o ejecución), el estado del canal cambia y la transacción con HTCL ya no existe. Volvemos a algo clásico.
En caso de cierre cooperativo: se detienen los pagos y, por lo tanto, se espera la ejecución de las transferencias / HTCL, la transacción es ligera, por lo que es menos costosa porque hay un máximo de 1 o 2 salidas.
Si el cierre es forzado: se publica con todos los HTLC en curso, por lo que se vuelve muy pesado y costoso. Y es un lío.

En resumen, el sistema de enrutamiento de Lightning Network utiliza Contratos Hash Time-Locked (HTLC) para garantizar un pago seguro y verificable. Los HTLC permiten pagos condicionales donde el dinero solo se puede desbloquear con un secreto, lo que garantiza que los participantes cumplan con sus compromisos.
En el ejemplo presentado, Alice desea enviar SAT a Bob a través de Susie. Bob genera un secreto, crea un hash de él y lo transmite a Alice. Alice y Susie establecen un HTLC basado en este hash. Una vez que Bob desbloquea el HTLC de Susie mostrándole el secreto, Susie puede desbloquear el HTLC de Alice.
En caso de que Bob no revele el secreto en un cierto período de tiempo, el HTLC expira. La expiración ocurre en orden inverso, asegurando que si Bob vuelve en línea, no haya consecuencias no deseadas.

Al cerrar el canal, si es una clausura cooperativa, los pagos se interrumpen y los HTLC se resuelven, lo que generalmente es menos costoso. Si el cierre es forzado, se publican todas las transacciones HTLC en curso, lo que puede volverse muy costoso y desordenado.
En resumen, el mecanismo HTLC agrega una capa adicional de seguridad en Lightning Network, asegurando que los pagos se ejecuten correctamente y que los usuarios cumplan con sus compromisos.

## Encontrar tu camino
<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![video](https://youtu.be/_7UuCI9TwlQ)

El único dato público es la capacidad total del canal (Alice + Bob) pero no sabemos dónde está la liquidez.
Para obtener más información, nuestro nodo escucha el canal de comunicación de LN para anuncios de nuevos canales y actualizaciones de tarifas de canales. Su nodo también mira la cadena de bloques para el cierre de canales.

Como no tenemos toda la información, debemos buscar una ruta de gráfico con la información que tenemos (capacidad máxima de los canales y no dónde está la liquidez).

Criterios:

- Probabilidad de éxito - Tasas
- Tiempo de expiración de HTLC
- Número de nodos intermedios
- Aleatorio

![graph](assets/chapitre9/1.webp)

Por lo tanto, si hay 3 rutas posibles

- Alice > 1 > 2 > 5 > Bob
- Alicia > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Por tanto, buscamos la mejor ruta en teoría con las menores tasas y las mayores probabilidades de éxito: máxima liquidez y el menor número de saltos posible.

Por ejemplo, si 2-3 sólo tiene una capacidad de 130.000 SAT, enviar 100.000 es muy improbable, por lo que la opción nº 3 no tiene ninguna posibilidad de éxito.

![graph](assets/chapitre9/2.webp)

Ahora el algoritmo ha hecho sus 3 elecciones y por lo tanto intentará la primera:

Elección 1:

- Alice envía un HTLC a 1 por 100.000 SAT;
- 1 hace un HTLC de 100.000 SAT para 2;
- 2 hace un HTLC de 100.000 SAT a 5, pero 5 no puede hacerlo, así que lo anuncia.

La información es devuelta, por lo que Alice decide probar la segunda ruta:

- Alice envía un HTLC de 100.000 a 1
- 1 hace un HTLC de 100.000 a 2
- 2 envía un HTLC de 100.000 a 4
- 4 hace un HTLC de 100.000 a Bob. Bob tiene la liquidez, así que está bien.
- Bob utiliza la preimagen (hash) del HTLC y por tanto utiliza el secreto para recuperar los 100.000 SAT
- 5 ahora tiene el secreto del HTLC para recuperar el HTLC bloqueado de 4
- 4 tiene ahora el secreto del HTLC para recuperar el HTLC bloqueado de 2
- 2 tiene ahora el secreto del HTLC para recuperar el HTLC bloqueado de 1
- 1 tiene ahora el secreto del HTLC para recuperar el HTLC bloqueado de Alice

Alice no vio el fallo de la ruta 1, sólo esperó un segundo más. Un fallo de pago se produce cuando no hay ninguna ruta posible. Para facilitar la búsqueda de una ruta, Bob puede proporcionar información a Alice para ayudarla con su factura:

- El importe
- Su dirección
- El hash de la preimagen para que Alice pueda crear el HTLC
- Indicaciones sobre los canales de Bob

Bob conoce la liquidez de los canales 5 y 3 porque está directamente conectado a ellos, puede indicárselo a Alice. Avisa a Alice de que el nodo 3 es inútil, lo que evita que Alice pueda hacer su ruta.Otro elemento serían los canales privados (por tanto no publicados en la red) que pueda tener Bob. Si Bob tiene un canal privado con 1, puede decirle a Alice que lo use y le daría a Alice > 1 > Bob.


![graph](assets/chapitre9/3.webp)

En conclusión, el enrutamiento de transacciones en la Red Lightning es un proceso complejo que requiere tener en cuenta varios factores. Aunque la capacidad total de los canales es pública, la distribución precisa de la liquidez no es directamente accesible. Esto obliga a los nodos a estimar las rutas más probables de éxito, teniendo en cuenta criterios como las tarifas, el plazo de vencimiento de HTLC, el número de nodos intermedios y un factor aleatorio. Cuando hay varias rutas posibles, los nodos buscan minimizar las tarifas y maximizar las posibilidades de éxito eligiendo canales con suficiente liquidez y un número mínimo de saltos. Si una transacción falla debido a una liquidez insuficiente, se intenta otra ruta hasta que se logra una transacción exitosa.

Además, para facilitar la búsqueda de ruta, el destinatario puede proporcionar información adicional, como la dirección, la cantidad, el hash de la preimagen y las indicaciones sobre sus canales. Esto puede ayudar a identificar los canales con suficiente liquidez y evitar intentos de transacciones innecesarias. En última instancia, el sistema de enrutamiento de la Red Lightning está diseñado para optimizar la velocidad, la seguridad y la eficiencia de las transacciones, al tiempo que se preserva la privacidad de los usuarios.

# Herramientas de la Lightning Network
<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Factura, LNURL, Keysend
<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![video](https://youtu.be/V2NsdO0Zig8)

Una factura LN (o invoice) es larga y no es agradable de leer, pero permite representar de manera densa una solicitud de pago.

![cover](assets/chapitre10/0.webp)

Ejemplo:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = parte legible
- 1 = separación con el resto
- Luego el resto
- Bc1 = Codificación Bech32 (base 32), por lo tanto se utilizan 32 caracteres.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = no el "b-i-o" y no el "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = cantidad
- M = milli (10*-3 / u = micro 10*-6 / n = nano 10*-9 / p = pico 10*-12)
  Aquí 1m = 1 \* 0.0001btc = 100 000 BTC
  "Por favor, pague 100 000 SAT en la red Lightning de la mainnet de Bitcoin a pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Timestamp (cuando fue creado)

Contiene 0 o más partes adicionales:

- Hash de la preimagen
- Secreto de pago (enrutamiento en cebolla)
- Datos arbitrarios
- Clave pública LN del destinatario
- Duración de vencimiento (por defecto 1h)
- Indicaciones de enrutamiento
- Firma del conjunto

Existen otros tipos de facturas. El meta-protocolo LNURL permite proporcionar una cantidad de satoshis directamente en lugar de hacer una solicitud. Es muy flexible y permite muchas mejoras en términos de experiencia de usuario.

![cover](assets/chapitre10/2.webp)

Un Keysend permite a Alice enviar dinero a Bob sin tener la solicitud de Bob. Alice obtiene la ID de Bob, crea una preimagen sin preguntar a Bob e incluye en su envío. Por lo tanto, Bob recibirá una solicitud sorpresa donde puede desbloquear el dinero porque Alice ya ha hecho el trabajo.

![cover](assets/chapitre10/3.webp)

En conclusión, una factura de Lightning Network, aunque compleja a primera vista, codifica de manera efectiva una solicitud de pago. Cada sección de la factura contiene información clave, incluyendo la cantidad a pagar, el destinatario, el timestamp de creación y potencialmente otra información como el hash de la preimagen, el secreto de pago, las indicaciones de enrutamiento y la duración de vencimiento. Los protocolos como LNURL y Keysend ofrecen mejoras significativas en términos de flexibilidad y experiencia de usuario, permitiendo, por ejemplo, enviar fondos sin una solicitud previa de la otra parte. Estas tecnologías hacen que el proceso de pago sea más fluido y eficiente en la Lightning Network.

## Gestionar la liquidez
<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![video](https://youtu.be/v3tMehXZ4R0)

Damos algunas pautas generales para responder a la sempiterna pregunta de la gestión de la liquidez en Lightning.

![instruction](assets/chapitre11/0.webp)

En LN, hay 3 tipos de personas:

- Los compradores: tienen liquidez saliente, es lo más sencillo porque solo tienen que abrir canales.
- Los comerciantes: es más complicado porque necesitan liquidez entrante a través de otros nodos y otros actores. Deben tener personas conectadas a ellos.
- Los nodos de enrutamiento: quieren estar equilibrados con liquidez en ambos lados y una buena conexión con muchos nodos para ser utilizados lo más posible.

Por lo tanto, si necesita liquidez entrante, puede comprarla a servicios.

![instruction](assets/chapitre11/1.webp)

Alice compra un canal con Susie por 1 millón de satoshis, por lo que abre un canal con 1 000 000 SAT directamente del lado entrante. Luego puede aceptar hasta 1 millón de SAT de pago de los clientes que estén conectados con Susie (que está muy conectada).

Otra solución sería hacer pagos; paga 100 000 por X razón, ahora puede recibir 100 000.

![instruction](assets/chapitre11/2.webp)

### Solución Loop Out: Atomic swap LN - BTC

Alice 2 millones - Susie 0

![instruction](assets/chapitre11/3.webp)

Alice quiere enviar la liquidez a Susie, por lo que hace un Loop out (un nodo especial que ofrece un servicio profesional de reequilibrio LN/BTC).
Alice envía 1 millón a Loop a través del nodo de Susie, por lo que Susie tiene la liquidez y Loop devuelve el equilibrio on-chain al nodo de Alice.

![instruction](assets/chapitre11/4.webp)

Por lo tanto, los 1 millón van a Susie, esta envía 1 millón a Loop, Loop envía 1 millón a Alice. Alice ha movido la liquidez hacia Susie a cambio de algunas tarifas pagadas a Loop por el servicio.

Lo más complicado en LN es mantener la liquidez.

![instruction](assets/chapitre11/5.webp)

En conclusión, la gestión de la liquidez en la red Lightning Network es un desafío clave que depende del tipo de usuario: comprador, comerciante o nodo de enrutamiento. Los compradores, que necesitan liquidez saliente, tienen la tarea más sencilla: simplemente abren canales. Los comerciantes, que necesitan liquidez entrante, deben estar conectados a otros nodos y actores. Los nodos de enrutamiento, por su parte, buscan mantener un equilibrio de liquidez en ambos lados. Existen varias soluciones para gestionar la liquidez, como la compra de canales o el pago para aumentar la capacidad de recepción. La opción "Loop Out", que permite un Atomic Swap entre LN y BTC, ofrece una solución interesante para reequilibrar la liquidez. A pesar de estas estrategias, mantener la liquidez en la red Lightning Network sigue siendo un desafío complejo.

# Vamos mas alla
<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Resumen de la formación
<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![video](https://youtu.be/9VowzzMU1UA)

Nuestro objetivo era explicar cómo funciona la red Lightning y cómo se basa en Bitcoin para funcionar.

La red Lightning es una red de canales de pago. Vimos cómo funciona un canal de pago entre dos partes interesadas, pero también ampliamos nuestra visión a toda la red, a la noción de red de canales de pago.

![instruction](assets/chapitre12/0.webp)

Los canales se abren mediante una transacción de Bitcoin y pueden alojar tantas transacciones como sea posible. El estado del canal se representa mediante una transacción de compromiso que envía a cada una de las partes interesadas lo que posee de su lado del canal. Cuando ocurre una transacción dentro del canal, las partes interesadas se comprometen con el nuevo estado revocando el estado anterior y construyendo una nueva transacción de compromiso.

![instruction](assets/chapitre12/1.webp)

Las parejas se protegen del fraude con claves de revocación y un bloqueo temporal. El cierre mutuo acordado es preferido para cerrar el canal. En caso de cierre forzado, se publica la última transacción de compromiso.

![instruction](assets/chapitre12/3.webp)

Los pagos pueden tomar prestados los canales de otros nodos intermedios. Los pagos condicionales a la hora de cierre (HTLC) permiten bloquear los fondos mientras se espera la resolución completa del pago. El enrutamiento en cebolla se utiliza en Lightning Network. Los nodos intermedios no conocen el destino final de los pagos. Alice debe calcular la ruta del pago, pero no tiene toda la información sobre la liquidez en los canales intermedios.

![instruction](assets/chapitre12/4.webp)

Hay una componente de probabilidad cuando se envía un pago a través de Lightning Network. 

![instruction](assets/chapitre12/5.webp)

Para recibir pagos, es necesario gestionar la liquidez en los canales, lo que se puede hacer pidiendo a otras personas que abran canales hacia nosotros, abriendo canales nosotros mismos y utilizando herramientas como Loop o comprando/alquilando canales en marketplaces.

## Entrevista con Fanis
<chapterId>077cb5f5-1626-5da5-9964-e67b1de503bf</chapterId>

Aquí hay un resumen de la entrevista:

Lightning Network es una solución de pago ultrarrápida en Bitcoin que permite superar las limitaciones relacionadas con la escalabilidad de la red. Sin embargo, los bitcoins en Lightning no son tan seguros como los de la cadena Bitcoin, ya que la descentralización y la seguridad se priorizan en detrimento de la escalabilidad.

El aumento excesivo del tamaño de los bloques no es una buena solución, ya que tiene compromisos en términos de nodos y capacidad de datos. En su lugar, Lightning Network permite crear canales de pago entre dos usuarios de Bitcoin sin que las transacciones aparezcan en la cadena de bloques, ahorrando espacio en los bloques y permitiendo que Bitcoin se escale hoy en día.

Sin embargo, hay críticas sobre la escalabilidad y la centralización de Lightning Network, con posibles problemas relacionados con el cierre de canales y las altas tarifas de transacción. Para resolver estos problemas, se recomienda evitar la apertura de canales pequeños para evitar problemas futuros y aumentar las tarifas de transacción con Child Pay for Parent.

Las soluciones consideradas para el futuro de Lightning Network son el batching y la creación de canales en grupos para reducir las tarifas de transacción, así como el aumento del tamaño de los bloques a largo plazo. Sin embargo, es importante tener en cuenta que los bitcoins en Lightning no son tan seguros como los bitcoins en la cadena Bitcoin.

La privacidad en Bitcoin y Lightning están relacionadas, con el enrutamiento en cebolla garantizando cierto nivel de privacidad para las transacciones. Sin embargo, en Bitcoin, todo es transparente por defecto, con heurísticas utilizadas para rastrear los Bitcoins de dirección en dirección en la cadena Bitcoin.

Las compras de Bitcoins con KYC permiten al exchange conocer las transacciones de retiro, mientras que las cantidades redondas y las direcciones de cambio permiten saber qué parte de una transacción está destinada a otra persona y qué parte está destinada a uno mismo.

Para mejorar la privacidad, las acciones conjuntas y los coinjoins permiten romper los cálculos de probabilidad haciendo transacciones donde varias personas hacen una transacción juntas. Las empresas de análisis de cadenas tienen más dificultades para determinar lo que haces con tus bitcoins siguiéndote.

En Lightning, solo dos personas están al tanto de la transacción y es más confidencial que Bitcoin. El enrutamiento en cebolla significa que un nodo intermedio no conoce al emisor y al destinatario del pago.

Para usar Lightning Network, se recomienda seguir una formación en tu canal de YouTube o directamente en el sitio descubre Bitcoin, o usar la formación en Umbrell. También es posible enviar texto arbitrario durante un pago en Lightning usando un campo dedicado para ello, lo que puede ser útil para donaciones o para mensajería.
Sin embargo, es importante tener en cuenta que los nodos de enrutamiento en Lightning podrían ser regulados en el futuro, con algunos estados que intentarán regular los nodos de enrutamiento.
Para los comerciantes, es necesario gestionar la liquidez para aceptar pagos en Lightning Network, con limitaciones actuales que pueden superarse con soluciones adecuadas.

Por último, el futuro de Bitcoin es prometedor con una posible proyección de un millón en cinco años. Para asegurar la profesionalización de la industria y la creación de un sistema alternativo al sistema bancario existente, es importante contribuir a la red y dejar de confiar.



## Danos tu opinión sobre este curso
<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Examen Final
<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Agradecimientos y sigue excavando la madriguera del conejo
<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

¡Felicidades! 🎉
¡Has completado el curso LN 201 - Introducción a Lightning Network!
Puedes estar orgulloso de ti mismo porque no es fácil. Sepa que son pocas las personas que bajan tan profundo en la madriguera de Bitcoin.

En primer lugar, un gran agradecimiento a Fanis Makalakis por ofrecernos este gran curso gratuito sobre un aspecto más étnico de Lightning. No dudes en seguirlo en Twitter, en su blog o a través de su trabajo en LN market.

Luego, si desea ayudar al proyecto, no dude en patrocinarnos en Patreon. Sus donaciones se utilizarán para producir contenido para nuevos cursos y, por supuesto, serán los primeros en ser informados (¡incluyendo el próximo de Fanis que está en proceso!).

La aventura de Lightning Network continúa con el curso sobre Umbrel y la configuración de un nodo de Lightning Network. ¡Se acabó la teoría y es hora de la práctica con el curso LN 202!

¡Besos y nos vemos pronto!

Rogzy
