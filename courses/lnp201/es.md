---
name: Introducción Teórica a la Red Lightning
goal: Descubrir la Red Lightning desde una perspectiva técnica
objectives:
  - Entender el funcionamiento de los canales de la red.
  - Familiarizarse con los términos HTLC, LNURL y UTXO.
  - Asimilar la gestión de la liquidez y las comisiones de la LNN.
  - Reconocer la Red Lightning como una red.
  - Entender los usos teóricos de la Red Lightning.
---

# Un Viaje hacia la Segunda Capa de Bitcoin

Sumérgete en el corazón de la Red Lightning, un sistema esencial para el futuro de las transacciones de Bitcoin. LNP201 es un curso teórico sobre el funcionamiento técnico de Lightning. Revela los fundamentos y mecanismos de esta red de segunda capa, diseñada para hacer que los pagos de Bitcoin sean rápidos, económicos y escalables.

Gracias a su red de canales de pago, Lightning permite transacciones rápidas y seguras sin registrar cada intercambio en la blockchain de Bitcoin. A lo largo de los capítulos, aprenderás cómo funciona la apertura, gestión y cierre de canales, cómo se enrutan los pagos a través de nodos intermediarios de manera segura mientras se minimiza la necesidad de confianza, y cómo gestionar la liquidez. Descubrirás qué son las transacciones de compromiso, los HTLCs, las llaves de revocación, los mecanismos de castigo, el enrutamiento cebolla y las facturas.

Ya seas un principiante en Bitcoin o un usuario más experimentado, este curso proporcionará información valiosa para entender y usar la Red Lightning. Aunque cubriremos algunos fundamentos del funcionamiento de Bitcoin en las primeras partes, es esencial dominar los conceptos básicos de la invención de Satoshi antes de sumergirse en LNP201.

¡Disfruta tu descubrimiento!

+++

# Los Fundamentos

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Entendiendo la Red Lightning

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Entendiendo la Red Lightning](https://youtu.be/PszWk046x-I)

Bienvenido al curso LNP201, que tiene como objetivo explicar el funcionamiento técnico de la Red Lightning.

La Red Lightning es una red de canales de pago construida sobre el protocolo de Bitcoin, con el objetivo de habilitar transacciones rápidas y de bajo costo. Permite la creación de canales de pago entre participantes, dentro de los cuales las transacciones pueden realizarse casi instantáneamente y con comisiones mínimas, sin necesidad de registrar cada transacción individualmente en la blockchain. Así, la Red Lightning busca mejorar la escalabilidad de Bitcoin y hacerlo utilizable para pagos de bajo valor.

Antes de explorar el aspecto de "red", es importante entender el concepto de un **canal de pago** en Lightning, cómo funciona y sus especificidades. Este es el tema de este primer capítulo.

### El Concepto de Canal de Pago

Un canal de pago permite a dos partes, aquí **Alice** y **Bob**, intercambiar fondos a través de la Red Lightning. Cada protagonista tiene un nodo, simbolizado por un círculo, y el canal entre ellos está representado por un segmento de línea.

![LNP201](assets/en/01.webp)

En nuestro ejemplo, Alice tiene 100,000 satoshis de su lado del canal, y Bob tiene 30,000, para un total de 130,000 satoshis, lo que constituye la **capacidad del canal**.

**Pero, ¿qué es un satoshi?**

El **satoshi** (o "sat") es una unidad de cuenta en Bitcoin. Similar a un centavo para el euro, un satoshi es simplemente una fracción de Bitcoin. Un satoshi equivale a **0.00000001 Bitcoin**, o una centésima millonésima parte de un Bitcoin. Usar el satoshi se vuelve cada vez más práctico a medida que el valor de Bitcoin aumenta.

### La Asignación de Fondos en el Canal

Regresemos al canal de pago. El concepto clave aquí es el "**lado del canal**". Cada participante tiene fondos en su lado del canal: Alice 100,000 satoshis y Bob 30,000. Como hemos visto, la suma de estos fondos representa la capacidad total del canal, una cifra establecida cuando se abre.

![LNP201](assets/en/02.webp)

Tomemos un ejemplo de una transacción de Lightning. Si Alice quiere enviar 40,000 satoshis a Bob, esto es posible porque ella tiene suficientes fondos (100,000 satoshis). Después de esta transacción, Alice tendrá 60,000 satoshis en su lado y Bob 70,000.

![LNP201](assets/en/03.webp)

La **capacidad del canal**, en 130,000 satoshis, permanece constante. Lo que cambia es la asignación de fondos. Este sistema no permite enviar más fondos de los que uno posee. Por ejemplo, si Bob quisiera enviar de vuelta 80,000 satoshis a Alice, no podría, porque solo tiene 70,000.

Otra manera de imaginar la asignación de fondos es pensar en un **deslizador** que indica dónde están los fondos en el canal. Inicialmente, con 100,000 satoshis para Alice y 30,000 para Bob, el deslizador está lógicamente en el lado de Alice. Después de la transacción de 40,000 satoshis, el deslizador se moverá ligeramente hacia el lado de Bob, quien ahora tiene 70,000 satoshis.

![LNP201](assets/en/04.webp)

Esta representación puede ser útil para imaginar el equilibrio de fondos en un canal.

### Las Reglas Fundamentales de un Canal de Pago

El primer punto a recordar es que la **capacidad del canal** es fija. Es algo así como el diámetro de una tubería: determina la cantidad máxima de fondos que se pueden enviar a través del canal de una sola vez.
Tomemos un ejemplo: si Alice tiene 130,000 satoshis en su lado, solo puede enviar un máximo de 130,000 satoshis a Bob en una sola transacción. Sin embargo, Bob puede luego enviar estos fondos de vuelta a Alice, ya sea parcial o totalmente.

Lo importante que hay que entender es que la capacidad fija del canal limita la cantidad máxima de una sola transacción, pero no el número total de transacciones posibles, ni el volumen total de fondos intercambiados dentro del canal.

**¿Qué debes recordar de este capítulo?**

- La capacidad de un canal es fija y determina la cantidad máxima que se puede enviar en una sola transacción.
- Los fondos en un canal se distribuyen entre los dos participantes, y cada uno solo puede enviar al otro los fondos que poseen en su lado.
- La Red Lightning permite así el intercambio rápido y eficiente de fondos, respetando las limitaciones impuestas por la capacidad de los canales.

Este es el final de este primer capítulo, donde hemos sentado las bases para la Red Lightning. En los próximos capítulos, veremos cómo abrir un canal y profundizaremos en los conceptos discutidos aquí.

## Bitcoin, Direcciones, UTXO y Transacciones

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, direcciones, utxo y transacciones](https://youtu.be/cadCJ2V7zTg)
Este capítulo es un poco especial ya que no estará dedicado directamente a Lightning, sino a Bitcoin. De hecho, la Red Lightning es una capa sobre Bitcoin. Por lo tanto, es esencial entender ciertos conceptos fundamentales de Bitcoin para comprender adecuadamente el funcionamiento de Lightning en los capítulos subsiguientes. En este capítulo, revisaremos los conceptos básicos de las direcciones de recepción de Bitcoin, los UTXOs, así como el funcionamiento de las transacciones de Bitcoin.

### Direcciones de Bitcoin, Claves Privadas y Claves Públicas

Una dirección de Bitcoin es una serie de caracteres derivados de una **clave pública**, que a su vez se calcula a partir de una **clave privada**. Como seguramente sabes, se utiliza para bloquear bitcoins, lo cual equivale a recibirlos en nuestra billetera.

La clave privada es un elemento secreto que **nunca debe ser compartido**, mientras que la clave pública y la dirección pueden ser compartidas sin riesgo de seguridad (su divulgación solo representa un riesgo para tu privacidad). Aquí hay una representación común que adoptaremos a lo largo de este entrenamiento:

- Las **claves privadas** serán representadas **verticalmente**.
- Las **claves públicas** serán representadas **horizontalmente**.
- Su color indica quién las posee (Alice en naranja y Bob en negro...).

### Transacciones de Bitcoin: Enviar Fondos y Scripts

En Bitcoin, una transacción implica enviar fondos de una dirección a otra. Tomemos el ejemplo de Alice enviando 0.002 Bitcoin a Bob. Alice usa la clave privada asociada con su dirección para **firmar** la transacción, demostrando así que efectivamente puede gastar esos fondos. Pero, ¿qué sucede exactamente detrás de esta transacción? Los fondos en una dirección de Bitcoin están bloqueados por un **script**, una especie de mini-programa que impone ciertas condiciones para gastar los fondos.

El script más común requiere una firma con la clave privada asociada a la dirección. Cuando Alice firma una transacción con su clave privada, ella **desbloquea el script** que bloquea los fondos, y estos pueden entonces ser transferidos. La transferencia de fondos implica añadir un nuevo script a estos fondos, estipulando que para gastarlos esta vez, se requerirá la firma de la clave privada de **Bob**.

![LNP201](assets/en/05.webp)

### UTXOs: Salidas de Transacción No Gastadas

En Bitcoin, lo que realmente intercambiamos no son directamente bitcoins, sino **UTXOs** (_Unspent Transaction Outputs_), que significa "salidas de transacción no gastadas".

Un UTXO es una pieza de bitcoin que puede ser de cualquier valor, por ejemplo, **2,000 bitcoins**, **8 bitcoins**, o incluso **8,000 sats**. Cada UTXO está bloqueado por un script, y para gastarlo, se deben satisfacer las condiciones del script, a menudo una firma con la clave privada correspondiente a una dirección de recepción dada.

Los UTXOs no pueden dividirse. Cada vez que se utilizan para gastar la cantidad en bitcoins que representan, debe hacerse en su totalidad. Es un poco como un billete de banco: si tienes un billete de €10 y le debes al panadero €5, no puedes simplemente cortar el billete por la mitad. Tienes que darle el billete de €10, y él te dará €5 de cambio. ¡Este es exactamente el mismo principio para los UTXOs en Bitcoin! Por ejemplo, cuando Alice desbloquea un script con su clave privada, desbloquea el UTXO completo. Si desea enviar solo una parte de los fondos representados por este UTXO a Bob, puede "fragmentarlo" en varios más pequeños. Luego enviará 0.0015 BTC a Bob y enviará el resto, 0.0005 BTC, a una **dirección de cambio**.

Aquí hay un ejemplo de una transacción con 2 salidas:

- Un UTXO de 0.0015 BTC para Bob, bloqueado por un script que requiere la firma de la clave privada de Bob.
- Un UTXO de 0.0005 BTC para Alice, bloqueado por un script que requiere su propia firma.

![LNP201](assets/en/06.webp)

### Direcciones Multi-firma

Además de las direcciones simples generadas a partir de una única clave pública, es posible crear **direcciones multi-firma** a partir de múltiples claves públicas. Un caso particularmente interesante para la Red Lightning es la **dirección multi-firma 2/2**, generada a partir de dos claves públicas:

![LNP201](assets/en/07.webp)

Para gastar los fondos bloqueados con esta dirección multi-firma 2/2, es necesario firmar con las dos claves privadas asociadas a las claves públicas.

![LNP201](assets/en/08.webp)

Este tipo de dirección es precisamente la representación en la blockchain de Bitcoin de los canales de pago en la Red Lightning.

**¿Qué debes recordar de este capítulo?**

- Una **dirección de Bitcoin** se deriva de una clave pública, que a su vez se deriva de una clave privada.
- Los fondos en Bitcoin están bloqueados por **scripts**, y para gastar estos fondos, uno debe satisfacer el script, lo que generalmente implica proporcionar una firma con la clave privada correspondiente.
- Los **UTXOs** son porciones de bitcoins bloqueadas por scripts, y cada transacción en Bitcoin consiste en desbloquear un UTXO y luego crear uno o más nuevos a cambio.
- Las **direcciones multi-firma 2/2** requieren la firma de dos claves privadas para gastar los fondos. Estas direcciones específicas se utilizan en el contexto de Lightning para crear canales de pago.

Este capítulo sobre Bitcoin nos ha permitido revisar algunas nociones esenciales para lo que sigue. En el próximo capítulo, descubriremos específicamente cómo funciona la apertura de canales en la Red Lightning.

# Apertura y Cierre de Canales

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Apertura de Canal

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![abrir un canal](https://youtu.be/B2caBC0Rxko)

En este capítulo, veremos más precisamente cómo abrir un canal de pago en la Red Lightning y entender el vínculo entre esta operación y el sistema subyacente de Bitcoin.

### Canales de Lightning

Como vimos en el primer capítulo, un **canal de pago** en Lightning puede compararse con un "tubo" para intercambiar fondos entre dos participantes (**Alice** y **Bob** en nuestros ejemplos). La capacidad de este canal corresponde a la suma de los fondos disponibles de cada lado. En nuestro ejemplo, Alice tiene **100,000 satoshis** y Bob tiene **30,000 satoshis**, dando una **capacidad total** de **130,000 satoshis**.

![LNP201](assets/en/09.webp)

### Niveles de Intercambio de Información

Es crucial distinguir claramente los diferentes niveles de intercambio en la Red Lightning:

- **Comunicaciones entre pares (protocolo Lightning)**: Estos son los mensajes que los nodos de Lightning se envían entre sí para comunicarse. Representaremos estos mensajes con líneas negras punteadas en nuestros diagramas.
- **Canales de pago (protocolo Lightning)**: Estos son los caminos para intercambiar fondos en Lightning, que representaremos con líneas negras sólidas.
- **Transacciones de Bitcoin (protocolo Bitcoin)**: Estas son las transacciones realizadas en la cadena, que representaremos con líneas naranjas.

![LNP201](assets/en/10.webp)
Es importante señalar que un nodo Lightning puede comunicarse a través del protocolo P2P sin abrir un canal, pero para intercambiar fondos, es necesario un canal.

### Pasos para Abrir un Canal Lightning

1. **Intercambio de mensajes**: Alice quiere abrir un canal con Bob. Ella le envía un mensaje que contiene la cantidad que quiere depositar en el canal (130,000 sats) y su clave pública. Bob responde compartiendo su propia clave pública.

![LNP201](assets/en/11.webp)

2. **Creación de la dirección de multifirma**: Con estas dos claves públicas, Alice crea una **dirección de multifirma 2/2**, lo que significa que los fondos que luego se depositen en esta dirección requerirán ambas firmas (de Alice y Bob) para ser gastados.

![LNP201](assets/en/12.webp)

3. **Transacción de depósito**: Alice prepara una transacción de Bitcoin para depositar fondos en esta dirección de multifirma. Por ejemplo, puede decidir enviar **130,000 satoshis** a esta dirección de multifirma. Esta transacción está **construida pero aún no publicada** en la blockchain.

![LNP201](assets/en/13.webp)

4. **Transacción de retiro**: Antes de publicar la transacción de depósito, Alice construye una transacción de retiro para poder recuperar sus fondos en caso de un problema con Bob. De hecho, una vez que Alice publica la transacción de depósito, sus sats quedarán bloqueados en una dirección de multifirma 2/2 que requiere ambas firmas, la de ella y la de Bob, para ser desbloqueados. Alice se protege contra este riesgo de pérdida construyendo la transacción de retiro que le permite recuperar sus fondos.

![LNP201](assets/en/14.webp)

5. **Firma de Bob**: Alice envía la transacción de depósito a Bob como prueba y le pide que firme la transacción de retiro. Una vez obtenida la firma de Bob en la transacción de retiro, Alice tiene la seguridad de poder recuperar sus fondos en cualquier momento, ya que ahora solo se necesita su propia firma para desbloquear la multifirma.

![LNP201](assets/en/15.webp)

6. **Publicación de la transacción de depósito**: Una vez obtenida la firma de Bob, Alice puede publicar la transacción de depósito en la blockchain de Bitcoin, abriendo oficialmente el canal Lightning entre los dos usuarios.

![LNP201](assets/en/16.webp)

### ¿Cuándo se considera abierto el canal?

El canal se considera abierto una vez que la transacción de depósito se incluye en un bloque de Bitcoin y ha alcanzado una cierta profundidad de confirmaciones (número de bloques siguientes).

**¿Qué debes recordar de este capítulo?**

- Abrir un canal comienza con el intercambio de **mensajes** entre las dos partes (intercambio de cantidades y claves públicas).
- Un canal se forma creando una **dirección de multifirma 2/2** y depositando fondos en ella a través de una transacción de Bitcoin.
- La persona que abre el canal se asegura de poder **recuperar sus fondos** a través de una transacción de retiro firmada por la otra parte antes de publicar la transacción de depósito.

En el próximo capítulo, exploraremos el funcionamiento técnico de una transacción Lightning dentro de un canal.

## Transacción de Compromiso

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Transacción Lightning & transacción de compromiso](https://youtu.be/aPqI34tpypM)

En este capítulo, descubriremos el funcionamiento técnico de una transacción dentro de un canal en la Red Lightning, es decir, cuando los fondos se mueven de un lado del canal al otro.

### Recordatorio del ciclo de vida del canal

Como se ha visto anteriormente, un canal Lightning comienza con una **apertura** a través de una transacción de Bitcoin. El canal puede ser **cerrado** en cualquier momento, también a través de una transacción de Bitcoin. Entre estos dos momentos, se pueden realizar un número casi infinito de transacciones dentro del canal, sin pasar por la blockchain de Bitcoin. Veamos qué sucede durante una transacción en el canal.
![LNP201](assets/en/17.webp)

### El estado inicial del canal

En el momento de abrir el canal, Alice depositó **130,000 satoshis** en la dirección de multisignatura del canal. Así, en el estado inicial, todos los fondos están del lado de Alice. Antes de abrir el canal, Alice también hizo que Bob firmara una **transacción de retiro**, lo que le permitiría recuperar sus fondos si deseaba cerrar el canal.

![LNP201](assets/en/18.webp)

### Transacciones no publicadas: Las Transacciones de Compromiso

Cuando Alice realiza una transacción en el canal para enviar fondos a Bob, se crea una nueva transacción de Bitcoin para reflejar este cambio en la distribución de fondos. Esta transacción, llamada **transacción de compromiso**, no se publica en la blockchain pero representa el nuevo estado del canal tras la transacción Lightning.

Tomemos un ejemplo con Alice enviando 30,000 satoshis a Bob:

- **Inicialmente**: Alice tiene 130,000 satoshis.
- **Después de la transacción**: Alice tiene 100,000 satoshis, y Bob 30,000 satoshis.
  Para validar esta transferencia, Alice y Bob crean una nueva **transacción de Bitcoin no publicada** que enviaría **100,000 satoshis a Alice** y **30,000 satoshis a Bob** desde la dirección de multisignatura. Ambas partes construyen esta transacción de forma independiente, pero con los mismos datos (cantidades y direcciones). Una vez construida, cada uno firma la transacción e intercambia su firma con el otro. Esto permite que cualquiera de las partes publique la transacción en cualquier momento si es necesario para recuperar su parte del canal en la blockchain principal de Bitcoin.
  ![LNP201](assets/en/19.webp)

### Proceso de Transferencia: La Factura

Cuando Bob quiere recibir fondos, envía a Alice una **_factura_** por 30,000 satoshis. Alice procede entonces a pagar esta factura iniciando la transferencia dentro del canal. Como hemos visto, este proceso se basa en la creación y firma de una nueva **transacción de compromiso**.

Cada transacción de compromiso representa la nueva distribución de fondos en el canal después de la transferencia. En este ejemplo, después de la transacción, Bob tiene 30,000 satoshis y Alice tiene 100,000 satoshis. Si cualquiera de los dos participantes decidiera publicar esta transacción de compromiso en la blockchain, resultaría en el cierre del canal y los fondos se distribuirían de acuerdo con esta última distribución.

![LNP201](assets/en/20.webp)

### Nuevo Estado Después de una Segunda Transacción

Tomemos otro ejemplo: después de la primera transacción donde Alice envió 30,000 satoshis a Bob, Bob decide enviar **10,000 satoshis de vuelta a Alice**. Esto crea un nuevo estado del canal. La nueva **transacción de compromiso** representará esta distribución actualizada:

- **Alice** ahora tiene **110,000 satoshis**.
- **Bob** tiene **20,000 satoshis**.

![LNP201](assets/en/21.webp)

Nuevamente, esta transacción no se publica en la blockchain pero puede serlo en cualquier momento en caso de que el canal se cierre.

En resumen, cuando se transfieren fondos dentro de un canal Lightning:

- Alice y Bob crean una nueva **transacción de compromiso**, que refleja la nueva distribución de fondos. - Esta transacción de Bitcoin es **firmada** por ambas partes, pero **no publicada** en la blockchain de Bitcoin mientras el canal permanezca abierto.
- Las transacciones de compromiso aseguran que cada participante pueda recuperar sus fondos en cualquier momento en la blockchain de Bitcoin publicando la última transacción firmada.

Sin embargo, este sistema tiene un posible defecto, el cual abordaremos en el próximo capítulo. Veremos cómo cada participante puede protegerse contra un intento de engaño por parte de la otra parte.

## Revocation Key

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transacciones parte 2](https://youtu.be/RRvoVTLRJ84)
En este capítulo, profundizaremos en cómo funcionan las transacciones en la Red Lightning discutiendo los mecanismos establecidos para protegerse contra el engaño, asegurando que cada parte se adhiera a las reglas dentro de un canal.

### Recordatorio: Transacciones de Compromiso

Como se vio anteriormente, las transacciones en Lightning dependen de **transacciones de compromiso** no publicadas. Estas transacciones reflejan la distribución actual de fondos en el canal. Cuando se realiza una nueva transacción de Lightning, se crea y firma una nueva transacción de compromiso por ambas partes para reflejar el nuevo estado del canal.

Tomemos un ejemplo simple:

- **Estado inicial**: Alice tiene **100,000 satoshis**, Bob **30,000 satoshis**.
- Después de una transacción donde Alice envía **40,000 satoshis** a Bob, la nueva transacción de compromiso distribuye los fondos de la siguiente manera:
  - Alice: **60,000 satoshis**
  - Bob: **70,000 satoshis**

![LNP201](assets/en/22.webp)

En cualquier momento, ambas partes pueden publicar la **última transacción de compromiso** firmada para cerrar el canal y recuperar sus fondos.

### El Defecto: Engañar Publicando una Transacción Antigua

Surge un problema potencial si una de las partes decide **engañar** publicando una transacción de compromiso antigua. Por ejemplo, Alice podría publicar una transacción de compromiso más antigua donde ella tenía **100,000 satoshis**, aunque ahora solo tiene **60,000** en realidad. Esto le permitiría robar **40,000 satoshis** a Bob.

![LNP201](assets/en/23.webp)

Peor aún, Alice podría publicar la primera transacción de retiro, la que se hizo antes de que se abriera el canal, donde ella tenía **130,000 satoshis**, y así robar todos los fondos del canal.

![LNP201](assets/en/24.webp)

### Solución: Revocation Key y Timelock

Para prevenir este tipo de engaño por parte de Alice, en la Red Lightning, se añaden **mecanismos de seguridad** a las transacciones de compromiso:

1. **El timelock**: Cada transacción de compromiso incluye un timelock para los fondos de Alice. El timelock es una primitiva de contrato inteligente que establece una condición de tiempo que debe cumplirse para que una transacción se añada a un bloque. Esto significa que Alice no puede recuperar sus fondos hasta que haya pasado un cierto número de bloques si publica una de las transacciones de compromiso. Este timelock comienza a aplicarse desde la confirmación de la transacción de compromiso. Su duración es generalmente proporcional al tamaño del canal, pero también puede configurarse manualmente.
2. **Revocation Key**: Los fondos de Alice también pueden ser gastados inmediatamente por Bob si él posee la **revocation key**. Esta clave consiste en un secreto mantenido por Alice y un secreto mantenido por Bob. Note que este secreto es diferente para cada transacción de compromiso.
   Gracias a estos 2 mecanismos combinados, Bob tiene tiempo para detectar el intento de Alice de engañar y castigarla recuperando su salida con la llave de revocación, lo que para Bob significa recuperar todos los fondos del canal. Nuestra nueva transacción de compromiso ahora se verá así:
   ![LNP201](assets/en/25.webp)

Detallemos el funcionamiento de este mecanismo juntos.

### Proceso de Actualización de Transacción

Cuando Alice y Bob actualizan el estado del canal con una nueva transacción de Lightning, intercambian de antemano sus respectivos **secretos** para la transacción de compromiso anterior (la que se volverá obsoleta y podría permitir que uno de ellos engañe). Esto significa que, en el nuevo estado del canal:

- Alice y Bob tienen una nueva transacción de compromiso que representa la distribución actual de fondos después de la transacción de Lightning.
- Cada uno tiene el secreto del otro para la transacción anterior, lo que les permite usar la llave de revocación solo si uno de ellos intenta engañar publicando una transacción con un estado antiguo en los mempools de los nodos de Bitcoin. De hecho, para castigar a la otra parte, es necesario tener ambos secretos y la transacción de compromiso del otro, que incluye la entrada firmada. Sin esta transacción, la llave de revocación por sí sola es inútil. La única forma de obtener esta transacción es recuperarla de los mempools (en las transacciones esperando confirmación) o en las transacciones confirmadas en la blockchain durante el timelock, lo que demuestra que la otra parte está intentando engañar, ya sea intencionalmente o no.

Tomemos un ejemplo para entender bien este proceso:

1. **Estado Inicial**: Alice tiene **100,000 satoshis**, Bob **30,000 satoshis**.

![LNP201](assets/en/26.webp)

2. Bob quiere recibir 40,000 satoshis de Alice a través de su canal de Lightning. Para hacer esto:
   - Él le envía una factura junto con su secreto para la llave de revocación de su transacción de compromiso anterior.
   - En respuesta, Alice proporciona su firma para la nueva transacción de compromiso de Bob, así como su secreto para la llave de revocación de su transacción anterior.
   - Finalmente, Bob envía su firma para la nueva transacción de compromiso de Alice.
   - Estos intercambios permiten a Alice enviar **40,000 satoshis** a Bob en Lightning a través de su canal, y las nuevas transacciones de compromiso ahora reflejan esta nueva distribución de fondos.

![LNP201](assets/en/27.webp)

3. Si Alice intenta publicar la antigua transacción de compromiso donde aún poseía **100,000 satoshis**, Bob, habiendo obtenido la llave de revocación, puede recuperar inmediatamente los fondos usando esta llave, mientras que Alice está bloqueada por el timelock.

![LNP201](assets/en/28.webp)

Incluso si, en este caso, Bob no tiene interés económico en intentar engañar, si lo hace de todos modos, Alice también se beneficia de la protección simétrica que le ofrece las mismas garantías.

**¿Qué debes recordar de este capítulo?**

Las **transacciones de compromiso** en la Red Lightning incluyen mecanismos de seguridad que reducen tanto el riesgo de engaño como los incentivos para hacerlo. Antes de firmar una nueva transacción de compromiso, Alice y Bob intercambian sus respectivos **secretos** para las transacciones de compromiso anteriores. Si Alice intenta publicar una transacción de compromiso antigua, Bob puede usar la **llave de revocación** para recuperar todos los fondos antes de que Alice pueda (porque está bloqueada por el timelock), lo que la castiga por intentar engañar.

Este sistema de seguridad asegura que los participantes se adhieran a las reglas de la Red Lightning, y no puedan beneficiarse de publicar transacciones de compromiso antiguas.
En este punto del entrenamiento, ya sabes cómo se abren los canales Lightning y cómo funcionan las transacciones dentro de estos canales. En el próximo capítulo, descubriremos las diferentes maneras de cerrar un canal y recuperar tus bitcoins en la blockchain principal.

## Cierre de Canal

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![cerrar un canal](https://youtu.be/FVmQvNpVW8Y)

En este capítulo, discutiremos **cerrar un canal** en la Red Lightning, lo cual se hace a través de una transacción de Bitcoin, justo como al abrir un canal. Después de ver cómo funcionan las transacciones dentro de un canal, ahora es momento de ver cómo cerrar un canal y recuperar los fondos en la blockchain de Bitcoin.

### Recordatorio del ciclo de vida del canal

El **ciclo de vida de un canal** comienza con su **apertura**, a través de una transacción de Bitcoin, luego se realizan transacciones Lightning dentro de él, y finalmente, cuando las partes desean recuperar sus fondos, el canal se **cierra** mediante una segunda transacción de Bitcoin. Las transacciones intermedias realizadas en Lightning están representadas por **transacciones de compromiso** no publicadas.

![LNP201](assets/en/29.webp)

### Los tres tipos de cierre de canal

Hay tres maneras principales de cerrar este canal, que pueden llamarse **el bueno, el malo y el tramposo** (inspirado por Andreas Antonopoulos en _Mastering the Lightning Network_):

1. **El Bueno**: el **cierre cooperativo**, donde Alice y Bob acuerdan cerrar el canal.
2. **El Malo**: el **cierre forzado**, donde una de las partes decide cerrar el canal honestamente, pero sin el acuerdo de la otra.
3. **El Feo**: el **cierre con trampa**, donde una de las partes intenta robar fondos publicando una transacción de compromiso antigua (cualquiera excepto la última, que refleja la distribución justa y actual de los fondos).

Tomemos un ejemplo:

- Alice posee **100,000 satoshis** y Bob **30,000 satoshis**.
- Esta distribución se refleja en **2 transacciones de compromiso** (una por usuario) que no se publican, pero podrían serlo en caso de cierre del canal.

![LNP201](assets/en/30.webp)

### El Bueno: el cierre cooperativo

En un **cierre cooperativo**, Alice y Bob acuerdan cerrar el canal. Así es como sucede:

1. Alice envía un mensaje a Bob a través del protocolo de comunicación Lightning para proponer cerrar el canal.
2. Bob está de acuerdo, y ambas partes no realizan más transacciones en el canal.

![LNP201](assets/en/31.webp)

3. Alice y Bob negocian juntos las tarifas de la **transacción de cierre**. Estas tarifas generalmente se calculan basadas en el mercado de tarifas de Bitcoin en el momento del cierre. Es importante notar que **siempre es la persona que abrió el canal** (Alice en nuestro ejemplo) quien paga las tarifas de cierre.
4. Ellos construyen una nueva **transacción de cierre**. Esta transacción se parece a una transacción de compromiso, pero sin bloqueos de tiempo o mecanismos de revocación, ya que ambas partes están cooperando y no hay riesgo de trampa. Esta transacción de cierre cooperativo es, por lo tanto, diferente de las transacciones de compromiso.
   Por ejemplo, si Alice posee **100,000 satoshis** y Bob **30,000 satoshis**, la transacción de cierre enviará **100,000 satoshis** a la dirección de Alice y **30,000 satoshis** a la dirección de Bob, sin restricciones de timelock. Una vez que esta transacción es firmada por ambas partes, es publicada por Alice. Una vez que la transacción es confirmada en la blockchain de Bitcoin, el canal Lightning será oficialmente cerrado.
   ![LNP201](assets/en/32.webp)

El **cierre cooperativo** es el método preferido de cierre porque es rápido (sin timelock) y las tarifas de la transacción se ajustan de acuerdo con las condiciones actuales del mercado de Bitcoin. Esto evita pagar demasiado poco, lo que podría arriesgar el bloqueo de la transacción en los mempools, o pagar en exceso innecesariamente, lo que lleva a una pérdida financiera innecesaria para los participantes.

### Lo malo: el cierre forzado

Cuando el nodo de Alice envía un mensaje al de Bob pidiendo un cierre cooperativo, si él no responde (por ejemplo, debido a una caída de internet o un problema técnico), Alice puede proceder con un **cierre forzado** publicando la **última transacción de compromiso firmada**.
En este caso, Alice simplemente publicará la última transacción de compromiso, que refleja el estado del canal en el momento en que tuvo lugar la última transacción de Lightning con la distribución correcta de fondos.

![LNP201](assets/en/33.webp)

Esta transacción incluye un **timelock** para los fondos de Alice, haciendo el cierre más lento.

![LNP201](assets/en/34.webp)

Además, las tarifas de la transacción de compromiso pueden ser inadecuadas en el momento del cierre, ya que se establecieron cuando se creó la transacción, a veces varios meses antes. Generalmente, los clientes de Lightning sobreestiman las tarifas para evitar problemas futuros, pero esto puede llevar a tarifas excesivas, o por el contrario demasiado bajas.

En resumen, el **cierre forzado** es una opción de último recurso cuando el par ya no responde. Es más lento y menos económico que un cierre cooperativo. Por lo tanto, se debe evitar tanto como sea posible.

### La trampa: el engaño

Finalmente, un cierre con **engaño** ocurre cuando una de las partes intenta publicar una transacción de compromiso antigua, a menudo donde tenían más fondos de los que deberían. Por ejemplo, Alice podría publicar una transacción antigua donde poseía **120,000 satoshis**, mientras que en realidad ahora solo posee **100,000**.

![LNP201](assets/en/35.webp)

Bob, para prevenir este engaño, monitorea la blockchain de Bitcoin y su mempool para asegurarse de que Alice no publique una transacción antigua. Si Bob detecta un intento de engaño, puede usar la **llave de revocación** para recuperar los fondos de Alice y castigarla tomando la totalidad de los fondos del canal. Dado que Alice está bloqueada por el timelock en su salida, Bob tiene tiempo para gastarlo sin un timelock de su lado para recuperar la suma completa en una dirección que posee.

![LNP201](assets/en/36.webp)

Obviamente, el engaño puede tener éxito potencialmente si Bob no actúa dentro del tiempo impuesto por el timelock en la salida de Alice. En este caso, la salida de Alice se desbloquea, permitiéndole consumirla para crear una nueva salida a una dirección que controla.

**¿Qué debes llevar de este capítulo?**

Hay tres maneras de cerrar un canal:

1. **Cierre Cooperativo**: Rápido y menos costoso, donde ambas partes acuerdan cerrar el canal y publicar una transacción de cierre a medida.
2. **Cierre Forzado**: Menos deseable, ya que se basa en publicar una transacción de compromiso, con tarifas potencialmente inadecuadas y un timelock, lo que ralentiza el cierre.
3. **Hacer trampa**: Si una de las partes intenta robar fondos publicando una transacción antigua, la otra puede usar la llave de revocación para castigar esta trampa.
   En los próximos capítulos, exploraremos la Red Lightning desde una perspectiva más amplia, enfocándonos en cómo opera su red.

# Una Red de Liquidez

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Red Lightning

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![red lightning](https://youtu.be/RAZAa3v41DM)

En este capítulo, exploraremos cómo los pagos en la Red Lightning pueden llegar a un destinatario incluso si no están conectados directamente por un canal de pago. Lightning es, de hecho, una **red de canales de pago**, que permite enviar fondos a un nodo distante a través de los canales de otros participantes. Descubriremos cómo se enrutan los pagos a través de la red, cómo se mueve la liquidez entre canales y cómo se calculan las tarifas de transacción.

### La Red de Canales de Pago

En la Red Lightning, una transacción corresponde a una transferencia de fondos entre dos nodos. Como se vio en capítulos anteriores, es necesario abrir un canal con alguien para realizar transacciones Lightning. Este canal permite realizar un número casi infinito de transacciones fuera de la cadena antes de cerrarlo para reclamar el saldo en la cadena. Sin embargo, este método tiene la desventaja de requerir un canal directo con la otra persona para recibir o enviar fondos, lo que implica una transacción de apertura y una transacción de cierre para cada canal. Si planeo hacer un gran número de pagos con esta persona, abrir y cerrar un canal se vuelve rentable. Por el contrario, si solo necesito realizar unas pocas transacciones Lightning, abrir un canal directo no es ventajoso, ya que me costaría 2 transacciones en la cadena por un número limitado de transacciones fuera de la cadena. Este caso podría ocurrir, por ejemplo, cuando se desea pagar con Lightning en un comercio sin planear volver.

Para resolver este problema, la Red Lightning permite enrutar un pago a través de varios canales y nodos intermediarios, lo que permite realizar una transacción sin un canal directo con la otra persona.

Por ejemplo, imagina que:

- **Alice** (en naranja) tiene un canal con **Suzie** (en gris) con **100,000 satoshis** de su lado y **30,000 satoshis** del lado de Suzie.
- **Suzie** tiene un canal con **Bob** en el que posee **250,000 satoshis** y donde Bob no tiene satoshis.

![LNP201](assets/en/37.webp)

Si Alice quiere enviar fondos a Bob sin abrir un canal directo con él, tendrá que pasar por Suzie, y cada canal necesitará ajustar la liquidez de cada lado. **Los satoshis enviados permanecen dentro de sus respectivos canales**; en realidad no "cruzan" los canales, pero la transferencia se realiza mediante un ajuste de la liquidez interna en cada canal.

Supongamos que Alice quiere enviar **50,000 satoshis** a Bob:

1. **Alice** envía 50,000 satoshis a **Suzie** en su canal común.
2. **Suzie** replica esta transferencia enviando 50,000 satoshis a **Bob** en su canal.

![LNP201](assets/en/38.webp)
Así, el pago se enruta a Bob mediante un movimiento de liquidez en cada canal. Al final de la operación, Alice termina con 50,000 sats. De hecho, ha transferido 50,000 sats ya que inicialmente tenía 100,000. Bob, por su parte, termina con 50,000 sats adicionales. Para Suzie (el nodo intermedio), esta operación es neutral: inicialmente, tenía 30,000 sats en su canal con Alice y 250,000 sats en su canal con Bob, un total de 280,000 sats. Después de la operación, mantiene 80,000 sats en su canal con Alice y 200,000 sats en su canal con Bob, que es la misma suma que al inicio.
Esta transferencia está así limitada por la **liquidez disponible** en la dirección de la transferencia.

### Cálculo de la Ruta y Límites de Liquidez

Tomemos un ejemplo teórico de otra red con:

- **130,000 satoshis** del lado de Alice (en naranja) en su canal con **Suzie** (en gris).
- **90,000 satoshis** del lado de **Suzie** y **200,000 satoshis** del lado de **Carol** (en rosa).
- **150,000 satoshis** del lado de **Carol** y **100,000 satoshis** del lado de **Bob**.

![LNP201](assets/en/39.webp)

El máximo que Alice puede enviar a Bob en esta configuración es **90,000 satoshis**, ya que está limitada por la menor liquidez disponible en el canal de **Suzie a Carol**. En la dirección opuesta (de Bob a Alice), no es posible ningún pago porque el lado de **Suzie** en el canal con **Alice** no contiene satoshis. Por lo tanto, no hay **ruta** utilizable para una transferencia en esta dirección.
Alice envía **40,000 satoshis** a Bob a través de los canales:

1. Alice transfiere 40,000 satoshis a su canal con Suzie.
2. Suzie transfiere 40,000 satoshis a Carol en su canal compartido.
3. Carol finalmente transfiere 40,000 satoshis a Bob.

![LNP201](assets/en/40.webp)

Los **satoshis enviados** en cada canal **permanecen en el canal**, así que los satoshis enviados por Carol a Bob no son los mismos que los enviados por Alice a Suzie. La transferencia se realiza solo ajustando la liquidez dentro de cada canal. Además, la capacidad total de los canales permanece sin cambios.

![LNP201](assets/en/41.webp)

Como en el ejemplo anterior, después de la transacción, el nodo fuente (Alice) tiene 40,000 satoshis menos. Los nodos intermedios (Suzie y Carol) retienen la misma cantidad total, haciendo la operación neutral para ellos. Finalmente, el nodo destino (Bob) recibe 40,000 satoshis adicionales.

El papel de los nodos intermedios es, por lo tanto, muy importante en el funcionamiento de la Lightning Network. Facilitan las transferencias ofreciendo múltiples caminos para los pagos. Para incentivar a estos nodos a proporcionar su liquidez y participar en el enrutamiento de pagos, se les pagan **tarifas de enrutamiento**.

### Tarifas de Enrutamiento

Los nodos intermedios aplican tarifas para permitir que los pagos pasen a través de sus canales. Estas tarifas son establecidas por **cada nodo para cada canal**. Las tarifas consisten en 2 elementos:

1. "**Tarifa base**": una cantidad fija por canal, a menudo **1 sat** por defecto, pero personalizable.
2. "**Tarifa variable**": un porcentaje del monto transferido, calculado en **partes por millón (ppm)**. Por defecto, es **1 ppm** (1 sat por millón de satoshis transferidos), pero también puede ajustarse.
   Las tarifas también varían dependiendo de la dirección de la transferencia. Por ejemplo, para una transferencia de Alice a Suzie, se aplican las tarifas de Alice. Por el contrario, de Suzie a Alice, se utilizan las tarifas de Suzie.

Por ejemplo, para un canal entre Alice y Suzie, podríamos tener:

- **Alice**: tarifa base de 1 sat y 1 ppm para tarifas variables.
- **Suzie**: tarifa base de 0.5 sat y 10 ppm para tarifas variables.

![LNP201](assets/en/42.webp)

Para entender mejor cómo funcionan las tarifas, estudiemos la misma Red Lightning que antes, pero ahora con las siguientes tarifas de enrutamiento:

- Canal **Alice - Suzie**: tarifa base de 1 satoshi y 1 ppm para Alice.
- Canal **Suzie - Carol**: tarifa base de 0 satoshi y 200 ppm para Suzie.
- Canal **Carol - Bob**: tarifa base de 1 satoshi y 1 ppm para Suzie 2.
  ![LNP201](assets/en/43.webp)

Para el mismo pago de **40,000 satoshis** a Bob, Alice tendrá que enviar un poco más, ya que cada nodo intermediario deducirá sus tarifas:

- **Carol** deduce 1.04 satoshis en el canal con Bob:
  $$ f*{\text{Carol-Bob}} = \text{tarifa base} + \left(\frac{\text{ppm} \times \text{monto}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ sats} $$

- **Suzie** deduce 8 satoshis en tarifas en el canal con Carol:
  $$ f*{\text{Suzie-Carol}} = \text{tarifa base} + \left(\frac{\text{ppm} \times \text{monto}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ sats} $$

Las tarifas totales para este pago en este camino son, por lo tanto, **9.04 satoshis**. Así, Alice debe enviar **40,009.04 satoshis** para que Bob reciba exactamente **40,000 satoshis**.

![LNP201](assets/en/44.webp)

La liquidez se actualiza por lo tanto:

![LNP201](assets/en/45.webp)

### Enrutamiento Cebolla

Para enrutar un pago del emisor al receptor, la Red Lightning utiliza un método llamado "**enrutamiento cebolla**". A diferencia del enrutamiento de datos clásicos, donde cada enrutador decide la dirección de los datos basándose en su destino, el enrutamiento cebolla funciona de manera diferente:

- **El nodo emisor calcula toda la ruta**: Alice, por ejemplo, determina que su pago debe pasar por Suzie y Carol antes de llegar a Bob.
- **Cada nodo intermediario solo conoce a su vecino inmediato**: Suzie solo sabe que recibió fondos de Alice y que debe transferirlos a Carol. Sin embargo, Suzie no sabe si Alice es el nodo fuente o un nodo intermediario, y tampoco sabe si Carol es el nodo receptor o simplemente otro nodo intermediario. Este principio también se aplica a Carol y todos los demás nodos en el camino. El enrutamiento de cebolla (onion routing) preserva así la confidencialidad de las transacciones al enmascarar la identidad del remitente y del destinatario final. Para asegurar que el nodo transmisor pueda calcular una ruta completa hasta el destinatario en el enrutamiento de cebolla, debe mantener un **gráfico de red** para conocer su topología y determinar posibles rutas.
  **¿Qué debes llevar contigo de este capítulo?**

1. En Lightning, los pagos pueden ser enrutados entre nodos indirectamente conectados a través de canales intermediarios. Cada uno de estos nodos intermediarios facilita la retransmisión de liquidez.
2. Los nodos intermediarios reciben una comisión por su servicio, consistente en tarifas fijas y variables.
3. El enrutamiento de cebolla permite al nodo transmisor calcular la ruta completa sin que los nodos intermediarios conozcan la fuente o el destino final.

En este capítulo, exploramos el enrutamiento de pagos en la Red Lightning. Pero surge una pregunta: ¿qué impide que los nodos intermediarios acepten un pago entrante sin reenviarlo al siguiente destino, con el objetivo de interceptar la transacción? Este es precisamente el papel de los HTLCs que estudiaremos en el siguiente capítulo.

## HTLC – Contrato de Tiempo Bloqueado con Hash

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

En este capítulo, descubriremos cómo Lightning permite que los pagos transiten a través de nodos intermediarios sin necesidad de confiar en ellos, gracias a los **HTLC** (_Hashed Time-Locked Contracts_ o Contratos de Tiempo Bloqueado con Hash). Estos contratos inteligentes aseguran que cada nodo intermediario solo recibirá los fondos de su canal si reenvía el pago al destinatario final, de lo contrario, el pago no será validado.

El problema que surge para el enrutamiento de pagos es, por lo tanto, la confianza necesaria en los nodos intermediarios, y entre los propios nodos intermediarios. Para ilustrar esto, revisemos nuestro ejemplo simplificado de la red Lightning con 3 nodos y 2 canales:

- Alice tiene un canal con Suzie.
- Suzie tiene un canal con Bob.

Alice quiere enviar 40,000 sats a Bob pero no tiene un canal directo con él y no desea abrir uno. Busca una ruta y decide pasar por el nodo de Suzie.

![LNP201](assets/en/46.webp)

Si Alice envía ingenuamente 40,000 satoshis a Suzie esperando que Suzie transfiera esta suma a Bob, Suzie podría quedarse con los fondos para sí misma y no transmitir nada a Bob.

![LNP201](assets/en/47.webp)
Para evitar esta situación, en Lightning, usamos HTLCs (Contratos de Tiempo Bloqueado con Hash), que hacen el pago al nodo intermediario condicional, lo que significa que Suzie debe cumplir ciertas condiciones para acceder a los fondos de Alice y transferirlos a Bob.

### Cómo Funcionan los HTLCs

Un HTLC es un contrato especial basado en dos principios:

- **Condición de acceso**: El destinatario debe revelar un secreto para desbloquear el pago que le corresponde.
- **Expiración**: Si el pago no se completa totalmente dentro de un período definido, se cancela y los fondos regresan al remitente.

Así es como funciona este proceso en nuestro ejemplo con Alice, Suzie y Bob:

![LNP201](assets/en/48.webp)
**Creando el secreto**: Bob genera un secreto aleatorio denotado como _s_ (la preimagen), y calcula su hash denotado como _r_ con la función hash denotada como _h_. Tenemos:

$$
r = h(s)
$$

Usar una función hash hace imposible encontrar _s_ con solo _h(s)_, pero si se proporciona _s_, es fácil verificar que corresponde a _h(s)_.

![LNP201](assets/en/49.webp)

**Enviando la solicitud de pago**: Bob envía una **factura** a Alice solicitando un pago. Esta factura incluye notablemente el hash _r_.

![LNP201](assets/en/50.webp)

**Enviando el pago condicional**: Alice envía un HTLC de 40,000 satoshis a Suzie. La condición para que Suzie reciba estos fondos es que ella proporcione a Alice un secreto _s'_ que satisfaga la siguiente ecuación:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Transfiriendo el HTLC al destinatario final**: Suzie, para obtener los 40,000 satoshis de Alice, debe transferir un HTLC similar de 40,000 satoshis a Bob, quien tiene la misma condición, es decir, que debe proporcionar a Suzie un secreto _s'_ que satisfaga la ecuación:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validación por el secreto _s_**: Bob proporciona _s_ a Suzie para recibir los 40,000 satoshis prometidos en el HTLC. Con este secreto, Suzie puede entonces desbloquear el HTLC de Alice y obtener los 40,000 satoshis de Alice. El pago es entonces correctamente dirigido a Bob.

![LNP201](assets/en/53.webp)
Este proceso evita que Suzie se quede con los fondos de Alice sin completar la transferencia a Bob, ya que debe enviar el pago a Bob para obtener el secreto _s_ y así desbloquear el HTLC de Alice. La operación permanece igual incluso si la ruta incluye varios nodos intermediarios: simplemente se trata de repetir los pasos de Suzie para cada nodo intermediario. Cada nodo está protegido por las condiciones de los HTLCs, porque desbloquear el último HTLC por el destinatario desencadena automáticamente el desbloqueo de todos los demás HTLCs en cascada.

### Expiración y gestión de HTLCs en caso de problemas

Si durante el proceso de pago, uno de los nodos intermediarios, o el nodo destinatario, deja de responder, especialmente en caso de un corte de internet o de energía, entonces el pago no puede completarse, porque el secreto necesario para desbloquear los HTLCs no se transmite. Tomando nuestro ejemplo con Alice, Suzie y Bob, este problema ocurre, por ejemplo, si Bob no transmite el secreto _s_ a Suzie. En este caso, todos los HTLCs aguas arriba del camino están bloqueados, y los fondos que aseguran también.

![LNP201](assets/en/54.webp)

Para evitar esto, los HTLCs en Lightning tienen una expiración que permite la eliminación del HTLC si no se completa después de cierto tiempo. La expiración sigue un orden específico ya que comienza primero con el HTLC más cercano al destinatario, y luego progresivamente se mueve hacia el emisor de la transacción. En nuestro ejemplo, si Bob nunca da el secreto _s_ a Suzie, esto primero causaría que el HTLC de Suzie hacia Bob expire.

![LNP201](assets/en/55.webp)

Luego el HTLC de Alice a Suzie.
![LNP201](assets/en/56.webp)
Si el orden de expiración se invirtiera, Alice podría recuperar su pago antes de que Suzie pudiera protegerse de un posible engaño. De hecho, si Bob regresa para reclamar su HTLC mientras Alice ya ha eliminado el suyo, Suzie estaría en desventaja. Este orden cascada de expiración de HTLCs asegura que ningún nodo intermediario sufra pérdidas injustas.

### Representación de HTLCs en transacciones de compromiso

Las transacciones de compromiso representan los HTLCs de tal manera que las condiciones que imponen sobre Lightning pueden transferirse a Bitcoin en el evento de un cierre forzado del canal durante la vida útil de un HTLC. Como recordatorio, las transacciones de compromiso representan el estado actual del canal entre los dos usuarios y permiten un cierre forzado unilateral en caso de problemas. Con cada nuevo estado del canal, se crean 2 transacciones de compromiso: una para cada parte. Revisemos nuestro ejemplo con Alice, Suzie y Bob, pero miremos más de cerca qué sucede a nivel de canal entre Alice y Suzie cuando se crea el HTLC.
![LNP201](assets/en/57.webp)

Antes del inicio del pago de 40,000 sats entre Alice y Bob, Alice tiene 100,000 sats en su canal con Suzie, mientras que Suzie tiene 30,000. Sus transacciones de compromiso son las siguientes:

![LNP201](assets/en/58.webp)

Alice acaba de recibir la factura de Bob, que contiene notablemente _r_, el hash del secreto. Así, ella puede construir un HTLC de 40,000 satoshis con Suzie. Este HTLC está representado en las últimas transacciones de compromiso como una salida llamada "**_HTLC Out_**" en el lado de Alice, ya que los fondos están saliendo, y "**_HTLC In_**" en el lado de Suzie, ya que los fondos están entrando.

![LNP201](assets/en/59.webp)

Estas salidas asociadas con el HTLC comparten exactamente las mismas condiciones, a saber:

- Si Suzie es capaz de proporcionar el secreto _s_, puede desbloquear esta salida inmediatamente y transferirla a una dirección que ella controle.
- Si Suzie no posee el secreto _s_, no puede desbloquear esta salida, y Alice podrá desbloquearla después de un timelock para enviarla a una dirección que ella controle. El timelock, por lo tanto, otorga a Suzie un período para reaccionar si obtiene _s_.

Estas condiciones aplican solo si el canal se cierra (es decir, una transacción de compromiso se publica en la cadena) mientras el HTLC todavía está activo en Lightning, lo que significa que el pago entre Alice y Bob aún no se ha finalizado, y los HTLCs aún no han expirado. Gracias a estas condiciones, Suzie puede recuperar los 40,000 satoshis del HTLC que le deben proporcionando _s_. De lo contrario, Alice recupera los fondos después de la expiración del timelock, porque si Suzie no conoce _s_, significa que no ha transferido los 40,000 satoshis a Bob, y por lo tanto, los fondos de Alice no le son debidos a ella.

Además, si el canal se cierra mientras varios HTLCs están pendientes, habrá tantas salidas adicionales como HTLCs en curso.
Si el canal no se cierra, entonces después de la expiración o el éxito del pago de Lightning, se crean nuevas transacciones de compromiso para reflejar el nuevo estado ahora estable del canal, es decir, sin ningún HTLC pendiente. Las salidas relacionadas con los HTLCs pueden, por lo tanto, eliminarse de las transacciones de compromiso.
![LNP201](assets/en/60.webp)
Finalmente, en el caso de un cierre cooperativo del canal mientras un HTLC está activo, Alice y Suzie dejan de aceptar nuevos pagos y esperan la resolución o expiración de los HTLCs en curso. Esto les permite publicar una transacción de cierre más ligera, sin las salidas relacionadas con los HTLCs, reduciendo así las comisiones y evitando la espera por un posible bloqueo de tiempo.

**¿Qué debes recordar de este capítulo?**

Los HTLCs permiten el enrutamiento de pagos a través de Lightning mediante múltiples nodos sin necesidad de confiar en ellos. Aquí están los puntos clave a recordar:

1. Los HTLCs aseguran la seguridad de los pagos mediante un secreto (preimagen) y un tiempo de expiración.
2. La resolución o expiración de los HTLCs sigue un orden específico: luego desde el destino hacia la fuente, para proteger a cada nodo.
3. Mientras un HTLC no se resuelve ni expira, se mantiene como una salida en las transacciones de compromiso más recientes.

En el próximo capítulo, descubriremos cómo un nodo que emite una transacción Lightning encuentra y selecciona rutas para que su pago alcance al nodo receptor.

## Encontrando tu Camino

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![encontrando tu camino](https://youtu.be/wnUGJjOxd9Q)

En los capítulos anteriores, vimos cómo usar los canales de otros nodos para enrutamiento de pagos y alcanzar un nodo sin estar directamente conectado a él a través de un canal. También discutimos cómo asegurar la seguridad de la transferencia sin confiar en los nodos intermediarios. En este capítulo, nos centraremos en encontrar la mejor ruta posible para alcanzar un nodo objetivo.

### El Problema del Enrutamiento en Lightning

Como hemos visto, en Lightning, es el nodo que envía el pago el que debe calcular la ruta completa hasta el destinatario, porque utilizamos un sistema de enrutamiento tipo cebolla. Los nodos intermediarios no conocen ni el punto de origen ni el destino final. Solo saben de dónde viene el pago y a qué nodo deben transferirlo a continuación. Esto significa que el nodo emisor debe mantener una topología local dinámica de la red, con los nodos Lightning existentes y los canales entre cada uno, teniendo en cuenta aperturas, cierres y actualizaciones de estado.

![LNP201](assets/en/61.webp)
Incluso con esta topología de la Red Lightning, hay información esencial para el enrutamiento que permanece inaccesible para el nodo emisor, que es la distribución exacta de liquidez en los canales en cualquier momento dado. De hecho, cada canal solo muestra su **capacidad total**, pero la distribución interna de fondos solo es conocida por los dos nodos participantes. Esto plantea desafíos para un enrutamiento eficiente, ya que el éxito del pago depende notablemente de si su cantidad es menor que la liquidez más baja en la ruta elegida. Sin embargo, las liquideces no son todas visibles para el nodo emisor.
![LNP201](assets/en/62.webp)

### Actualización del Mapa de la Red

Para mantener su mapa de la red actualizado, los nodos intercambian regularmente mensajes a través de un algoritmo llamado "**_gossip_**" (chismorreo). Este es un algoritmo distribuido utilizado para difundir información de manera epidémica a todos los nodos en la red, lo que permite el intercambio y sincronización del estado global de los canales en unos pocos ciclos de comunicación. Cada nodo propaga información a uno o más vecinos elegidos al azar o no, estos, a su vez, propagan la información a otros vecinos y así sucesivamente hasta que se logra un estado sincronizado a nivel global.

Los 2 mensajes principales intercambiados entre los nodos Lightning son los siguientes:

- "**Anuncios de Canal**": mensajes que señalan la apertura de un nuevo canal.
- "**Actualizaciones de Canal**": mensajes de actualización sobre el estado de un canal, particularmente sobre la evolución de las comisiones (pero no sobre la distribución de la liquidez).
  Los nodos de Lightning también monitorean la blockchain de Bitcoin para detectar transacciones de cierre de canal. El canal cerrado se elimina entonces del mapa ya que no puede ser utilizado para enrutar nuestros pagos.

### Enrutando un Pago

Tomemos el ejemplo de una pequeña Red Lightning con 7 nodos: Alice, Bob, 1, 2, 3, 4 y 5. Imagina que Alice quiere enviar un pago a Bob pero debe pasar por nodos intermediarios.

![LNP201](assets/en/63.webp)

Aquí está la distribución actual de fondos en estos canales:

- **Canal entre Alice y 1**: 250,000 sats del lado de Alice, 80,000 del lado de 1 (capacidad total de 330,000 sats).
- **Canal entre 1 y 2**: 300,000 sats del lado de 1, 200,000 del lado de 2 (capacidad total de 500,000 sats).
- **Canal entre 2 y 3**: 50,000 sats del lado de 2, 60,000 del lado de 3 (capacidad total de 110,000 sats).
- **Canal entre 2 y 5**: 90,000 sats del lado de 2, 160,000 del lado de 5 (capacidad total de 250,000 sats).
- **Canal entre 2 y 4**: 180,000 sats del lado de 2, 110,000 del lado de 4 (capacidad total de 290,000 sats).
- **Canal entre 4 y 5**: 200,000 sats del lado de 4, 10,000 del lado de 5 (capacidad total de 210,000 sats).
- **Canal entre 3 y Bob**: 50,000 sats del lado de 3, 250,000 del lado de Bob (capacidad total de 300,000 sats).
- **Canal entre 5 y Bob**: 260,000 sats del lado de 5, 100,000 del lado de Bob (capacidad total de 360,000 sats).

![LNP201](assets/en/64.webp)

Para hacer un pago de 100,000 sats de Alice a Bob, las opciones de enrutamiento están limitadas por la liquidez disponible en cada canal. La ruta óptima para Alice, basada en las distribuciones de liquidez conocidas, podría ser la secuencia `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Pero dado que Alice no conoce la distribución exacta de fondos en cada canal, debe estimar la ruta óptima de manera probabilística, teniendo en cuenta los siguientes criterios:

- **Probabilidad de éxito**: un canal con una mayor capacidad total es más probable que contenga suficiente liquidez. Por ejemplo, el canal entre el nodo 2 y el nodo 3 tiene una capacidad total de 110,000 sats, por lo que es improbable encontrar 100,000 sats o más del lado del nodo 2, aunque sigue siendo posible.
- **Comisiones de transacción**: al elegir la mejor ruta, el nodo emisor también considera las comisiones aplicadas por cada nodo intermedio y busca minimizar el costo total de enrutamiento.
- **Expiración de HTLCs**: para evitar pagos bloqueados, el tiempo de expiración de los HTLCs también es un parámetro a considerar.
- **Número de nodos intermedios**: finalmente, de manera más general, el nodo emisor buscará encontrar una ruta con el menor número posible de nodos para reducir el riesgo de fallo y limitar las comisiones de transacción de Lightning.
  Al analizar estos criterios, el nodo emisor puede probar las rutas más probables e intentar optimizarlas. En nuestro ejemplo, Alice podría clasificar las mejores rutas de la siguiente manera:

1. `Alice → 1 → 2 → 5 → Bob`, porque es la ruta más corta con la mayor capacidad.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, porque esta ruta ofrece buenas capacidades, aunque es más larga que la primera.
3. `Alice → 1 → 2 → 3 → Bob`, porque esta ruta incluye el canal `2 → 3`, que tiene una capacidad muy limitada, pero sigue siendo potencialmente utilizable.

### Ejecución del Pago

Alice decide probar su primera ruta (`Alice → 1 → 2 → 5 → Bob`). Por lo tanto, envía un HTLC de 100,000 sats al nodo 1. Este nodo verifica que tiene suficiente liquidez con el nodo 2 y continúa la transmisión. El nodo 2 luego recibe el HTLC del nodo 1, pero se da cuenta de que no tiene suficiente liquidez en su canal con el nodo 5 para enrutar un pago de 100,000 sats. Entonces envía un mensaje de error de vuelta al nodo 1, quien lo transmite a Alice. Esta ruta ha fallado.

![LNP201](assets/en/66.webp)

Alice luego intenta enrutar su pago usando su segunda ruta (`Alice → 1 → 2 → 4 → 5 → Bob`). Envía un HTLC de 100,000 sats al nodo 1, quien lo transmite al nodo 2, luego al nodo 4, al nodo 5 y finalmente a Bob. Esta vez, la liquidez es suficiente y la ruta es funcional. Cada nodo desbloquea su HTLC en cascada usando el preimagen proporcionado por Bob (el secreto _s_), lo que permite que el pago de Alice a Bob se finalice con éxito.

![LNP201](assets/en/67.webp)

La búsqueda de una ruta se lleva a cabo de la siguiente manera: el nodo emisor comienza por identificar las mejores rutas posibles, luego intenta pagos sucesivamente hasta encontrar una ruta funcional.

Vale la pena mencionar que Bob puede proporcionar a Alice información en la **factura** para facilitar el enrutamiento. Por ejemplo, puede indicar canales cercanos con suficiente liquidez o revelar la existencia de canales privados. Estas indicaciones permiten a Alice evitar rutas con pocas posibilidades de éxito y primero intentar los caminos recomendados por Bob.

**¿Qué debes recordar de este capítulo?**

1. Los nodos mantienen un mapa de la topología de la red a través de anuncios y monitoreando el cierre de canales en la blockchain de Bitcoin.
2. La búsqueda de una ruta óptima para un pago sigue siendo probabilística y depende de muchos criterios.
3. Bob puede proporcionar indicaciones en la **factura** para guiar el enrutamiento de Alice y ahorrarle probar rutas poco probables.

En el siguiente capítulo, estudiaremos específicamente el funcionamiento de las facturas, además de algunas otras herramientas utilizadas en la Red Lightning.

# Las Herramientas de la Red Lightning

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Factura, LNURL y Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![factura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
En este capítulo, vamos a examinar más de cerca el funcionamiento de las **facturas** de Lightning, es decir, solicitudes de pago enviadas por el nodo receptor al nodo emisor. El objetivo es entender cómo pagar y recibir pagos en Lightning. También discutiremos 2 alternativas a las facturas clásicas: LNURL y Keysend.
![LNP201](assets/en/68.webp)

### La Estructura de las Facturas de Lightning

Como se explicó en el capítulo sobre HTLCs, cada pago comienza con la generación de una **factura** por parte del receptor. Esta factura se transmite luego al pagador (a través de un código QR o copiando y pegando) para iniciar el pago. Una factura consta de dos partes principales:

1. **La Parte Legible por Humanos**: esta sección contiene metadatos claramente visibles para mejorar la experiencia del usuario.
2. **El Payload**: esta sección incluye información destinada a que las máquinas procesen el pago.

La estructura típica de una factura comienza con un identificador `ln` por "Lightning", seguido de `bc` por Bitcoin, luego la cantidad de la factura. Un separador `1` distingue la parte legible por humanos de la parte de datos (payload).

Tomemos la siguiente factura como ejemplo:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Ya podemos dividirla en 2 partes. Primero, está la Parte Legible por Humanos:

```invoice
lnbc100u
```

Luego, la parte destinada al payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Las dos partes están separadas por un `1`. Este separador fue elegido en lugar de un carácter especial para permitir el copiado y pegado fácil de toda la factura con doble clic.
En la primera parte, podemos ver que:

- `ln` indica que es una transacción Lightning.
- `bc` indica que la red Lightning está en la blockchain de Bitcoin (y no en la testnet o en Litecoin).
- `100u` indica la cantidad de la factura, expresada en **microsatoshis** (`u` significando "micro"), que aquí equivale a 10,000 sats.

Para designar la cantidad de pago, se expresa en subunidades de bitcoin. Aquí están las unidades utilizadas:

- **Millibitcoin (denotado `m`):** Representa una milésima parte de un bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (denotado `u`):** También a veces llamado "bit", representa una millonésima parte de un bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (denotado `n`):** Representa una milmillonésima parte de un bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (denotado `p`):** Representa una billonésima parte de un bitcoin.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### El Cuerpo de una Factura

El cuerpo de una factura incluye varias piezas de información necesarias para procesar el pago:

- **La marca de tiempo:** El momento de la creación de la factura, expresado en Timestamp Unix (el número de segundos que han transcurrido desde el 1 de enero de 1970).
- **Hashing el Secreto**: Como vimos en la sección sobre HTLCs, el nodo receptor debe proporcionar al nodo emisor el hash de la preimagen. Esto se utiliza en HTLCs para asegurar la transacción. Nos referimos a ello como "_r_".
- **El Secreto de Pago**: Otro secreto es generado por el receptor, pero esta vez se transmite al nodo emisor. Se utiliza en el enrutamiento de cebolla para evitar que los nodos intermedios adivinen si el próximo nodo es el destinatario final o no. Esto mantiene así una forma de confidencialidad para el destinatario con respecto al último nodo intermedio en la ruta.
- **La Clave Pública del Destinatario**: Indica al pagador el identificador de la persona a ser pagada.
- **La Duración de Expiración**: El tiempo máximo para que la factura sea pagada (1 hora por defecto).
- **Indicaciones de Enrutamiento**: Información adicional proporcionada por el receptor para ayudar al emisor a optimizar la ruta de pago.
- **La Firma**: Garantiza la integridad de la factura autenticando toda la información.

Las facturas se codifican entonces en **bech32**, el mismo formato que para las direcciones SegWit de Bitcoin (formato que comienza con `bc1`).

### LNURL Retiro

En una transacción tradicional, como una compra en tienda, se genera una factura por el monto total a pagar. Una vez que se presenta la factura (en forma de código QR o cadena de caracteres), el cliente puede escanearla y finalizar la transacción. El pago sigue entonces el proceso tradicional que estudiamos en la sección anterior. Sin embargo, este proceso a veces puede ser muy engorroso para la experiencia del usuario, ya que requiere que el receptor envíe información al emisor a través de la factura.
Para ciertas situaciones, como retirar bitcoins de un servicio en línea, el proceso tradicional es demasiado engorroso. En tales casos, la solución de retiro **LNURL** simplifica este proceso al mostrar un código QR que la billetera del destinatario escanea para crear automáticamente la factura. El servicio luego paga la factura, y el usuario simplemente ve un retiro instantáneo.

![LNP201](assets/en/69.webp)

LNURL es un protocolo de comunicación que especifica un conjunto de funcionalidades diseñadas para simplificar las interacciones entre nodos Lightning y clientes, así como aplicaciones de terceros. El retiro LNURL, como acabamos de ver, es solo un ejemplo entre otras funcionalidades.
Este protocolo se basa en HTTP y permite la creación de enlaces para varias operaciones, como una solicitud de pago, una solicitud de retiro u otras funcionalidades que mejoran la experiencia del usuario. Cada LNURL es una URL codificada en bech32 con el prefijo lnurl, que, una vez escaneada, desencadena una serie de acciones automáticas en la billetera Lightning.
Por ejemplo, la característica LNURL-withdraw (LUD-03) permite retirar fondos de un servicio escaneando un código QR, sin la necesidad de generar manualmente una factura. De manera similar, LNURL-auth (LUD-04) permite iniciar sesión en servicios en línea usando una clave privada en la billetera Lightning en lugar de una contraseña.

### Enviando un Pago Lightning sin una Factura: Keysend

Otro caso interesante es la transferencia de fondos sin haber recibido una factura de antemano, conocido como "**Keysend**". Este protocolo permite enviar fondos agregando una preimagen en los datos del pago encriptado, accesible solo por el destinatario. Esta preimagen permite al destinatario desbloquear el HTLC, recuperando así los fondos sin haber generado una factura de antemano.

Para simplificar, en este protocolo, es el emisor quien genera el secreto utilizado en los HTLCs, en lugar del destinatario. Prácticamente, esto permite al emisor realizar un pago sin haber tenido que interactuar con el destinatario de antemano.

![LNP201](assets/en/70.webp)

**¿Qué debes recordar de este capítulo?**

1. Una **Factura Lightning** es una solicitud de pago que consta de una parte legible por humanos y una parte de datos de máquina.
2. La factura está codificada en **bech32**, con un separador `1` para facilitar la copia y una parte de datos que contiene toda la información necesaria para procesar el pago.
3. Existen otros procesos de pago en Lightning, notablemente **LNURL-Withdraw** para facilitar retiros, y **Keysend** para transferencias directas sin factura.

En el siguiente capítulo, veremos cómo un operador de nodo puede gestionar la liquidez en sus canales, para nunca estar bloqueado y siempre poder enviar y recibir pagos en la Red Lightning.

## Gestionando Tu Liquidez

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![gestionando tu liquidez](https://youtu.be/YuPrbhEJXbg)

En este capítulo, exploraremos estrategias para gestionar efectivamente la liquidez en la Red Lightning. La gestión de la liquidez varía dependiendo del tipo de usuario y contexto. Veremos los principios principales y las técnicas existentes para entender mejor cómo optimizar esta gestión.

### Necesidades de Liquidez

Existen tres perfiles principales de usuarios en Lightning, cada uno con necesidades específicas de liquidez:

1. **El Pagador**: Es quien realiza pagos. Necesitan liquidez saliente para poder transferir fondos a otros usuarios. Por ejemplo, esto podría ser un consumidor.
2. **El Vendedor (o Beneficiario)**: Es quien recibe pagos. Necesitan liquidez entrante para poder aceptar pagos en su nodo. Por ejemplo, esto podría ser un negocio o una tienda en línea.
3. **El Enrutador**: Un nodo intermediario, a menudo especializado en el enrutamiento de pagos, que debe optimizar su liquidez en cada canal para enrutador tantos pagos como sea posible y ganar comisiones.

Estos perfiles obviamente no son fijos; un usuario puede cambiar entre pagador y beneficiario dependiendo de las transacciones. Por ejemplo, Bob podría recibir su salario en Lightning de su empleador, colocándolo en la posición de un "vendedor" que requiere liquidez entrante. Posteriormente, si quiere usar su salario para comprar comida, se convierte en un "pagador" y debe entonces tener liquidez saliente.

Para entender mejor, tomemos el ejemplo de una red simple compuesta por tres nodos: el comprador (Alice), el enrutador (Suzie) y el vendedor (Bob).

![LNP201](assets/en/71.webp)

Imagina que el comprador quiere enviar 30,000 sats al vendedor y que el pago pasa por el nodo del enrutador. Cada parte debe entonces tener una cantidad mínima de liquidez en la dirección del pago:

- El pagador debe tener al menos 30,000 satoshis de su lado del canal con el enrutador.
- El vendedor debe tener un canal donde 30,000 satoshis estén del lado opuesto para poder recibirlos.
- El enrutador debe tener 30,000 satoshis del lado del pagador en su canal, y también 30,000 satoshis de su lado en el canal con el vendedor, para poder enrutador el pago.

![LNP201](assets/en/72.webp)

### Estrategias de Gestión de Liquidez

Los pagadores deben asegurarse de mantener suficiente liquidez de su lado de los canales para garantizar la liquidez saliente. Esto resulta ser relativamente simple, ya que es suficiente abrir nuevos canales Lightning para tener esta liquidez. De hecho, los fondos iniciales bloqueados en el multisig on-chain están completamente del lado del pagador en el canal Lightning al inicio. La capacidad de pago está así asegurada mientras se abran canales con fondos suficientes. Cuando la liquidez saliente se agota, es suficiente abrir nuevos canales.
Por otro lado, para el vendedor, la tarea es más compleja. Para poder recibir pagos, deben tener liquidez del lado opuesto de sus canales. Por lo tanto, abrir un canal no es suficiente: también deben realizar un pago en este canal para mover la liquidez al otro lado antes de que puedan recibir pagos ellos mismos. Para ciertos perfiles de usuarios de Lightning, como los comerciantes, existe una clara desproporción entre lo que su nodo envía y lo que recibe, ya que el objetivo de un negocio es principalmente recaudar más de lo que gasta, con el fin de generar una ganancia. Afortunadamente, para estos usuarios con necesidades específicas de liquidez entrante, existen varias soluciones:

- **Atraer canales**: El comerciante se beneficia de una ventaja debido al volumen de pagos entrantes esperados en su nodo. Teniendo esto en cuenta, pueden intentar atraer a nodos enrutadores que buscan ingresos de las comisiones por transacción y que podrían abrir canales hacia ellos, esperando enrutador sus pagos y cobrar las comisiones asociadas.
- **Movimiento de liquidez**: El vendedor también puede abrir un canal y transferir parte de los fondos al lado opuesto realizando pagos ficticios a otro nodo, el cual devolverá el dinero de otra manera. Veremos en la próxima parte cómo llevar a cabo esta operación.
- **Apertura triangular**: Existen plataformas para nodos que desean abrir canales de manera colaborativa, permitiendo a cada uno beneficiarse de liquidez entrante y saliente inmediata. Por ejemplo, [LightningNetwork+](https://lightningnetwork.plus/) ofrece este servicio. Si Alice, Bob y Suzie quieren abrir un canal con 100,000 sats, pueden acordarlo en esta plataforma para que Alice abra un canal hacia Bob, Bob hacia Suzie y Suzie hacia Alice. De esta manera, cada uno tiene 100,000 sats de liquidez saliente y 100,000 sats de liquidez entrante, habiendo bloqueado solo 100,000 sats.

![LNP201](assets/en/73.webp)

- **Comprar canales**: También existen servicios para alquilar canales de Lightning para obtener liquidez entrante, como [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) o [Lightning Labs Pool](https://lightning.engineering/pool/). Por ejemplo, Alice puede comprar un canal de un millón de satoshis hacia su nodo para poder recibir pagos.

![LNP201](assets/en/74.webp)

Finalmente, para los routers, cuyo objetivo es maximizar el número de pagos procesados y las comisiones recogidas, deben:

- Abrir canales bien financiados con nodos estratégicos.
- Ajustar regularmente la distribución de fondos en los canales según las necesidades de la red.

### El Servicio Loop Out

El servicio [Loop Out](https://lightning.engineering/loop/), ofrecido por Lightning Labs, permite mover la liquidez al lado opuesto del canal mientras se recuperan los fondos en la blockchain de Bitcoin. Por ejemplo, Alice envía 1 millón de satoshis a través de Lightning a un nodo loop, el cual luego le devuelve esos fondos en bitcoins en cadena. Esto equilibra su canal con 1 millón de satoshis en cada lado, optimizando su capacidad para recibir pagos.

![LNP201](assets/en/75.webp)

Por lo tanto, este servicio permite la liquidez entrante mientras se recuperan los bitcoins en cadena, lo que ayuda a limitar la inmovilización de efectivo necesaria para aceptar pagos con Lightning.

**¿Qué debes recordar de este capítulo?**

- Para enviar pagos en Lightning, debes tener suficiente liquidez de tu lado en tus canales. Para aumentar esta capacidad de envío, simplemente abre nuevos canales.
- Para recibir pagos, necesitas tener liquidez del lado opuesto en tus canales. Aumentar esta capacidad de recepción es más complejo, ya que requiere que otros abran canales hacia ti, o hacer pagos (ficticios o reales) para mover la liquidez al otro lado.
- Mantener la liquidez donde se desea puede ser aún más desafiante dependiendo del uso de los canales. Por eso existen herramientas y servicios para ayudar a equilibrar los canales según se desee.

En el próximo capítulo, propongo revisar los conceptos más importantes de esta formación.

# Ir Más Allá

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Conclusión del Entrenamiento

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![conclusión](https://youtu.be/MaWpD0rbkVo)
En este capítulo final que marca el fin del entrenamiento LNP201, propongo revisar los conceptos importantes que hemos cubierto juntos.
El objetivo de este entrenamiento era proporcionarte una comprensión comprensiva y técnica de la Red Lightning. Descubrimos cómo la Red Lightning depende de la blockchain de Bitcoin para realizar transacciones fuera de la cadena, mientras retiene las características fundamentales de Bitcoin, notablemente la ausencia de la necesidad de confiar en otros nodos.

### Canales de Pago

En los capítulos iniciales, exploramos cómo dos partes, al abrir un canal de pago, pueden realizar transacciones fuera de la blockchain de Bitcoin. Aquí están los pasos cubiertos:

1. **Apertura del Canal**: La creación del canal se realiza a través de una transacción de Bitcoin que bloquea los fondos en una dirección multisignatura 2/2. Este depósito representa el canal Lightning en la blockchain.

![LNP201](assets/en/76.webp) 2. **Transacciones en el Canal**: En este canal, entonces es posible llevar a cabo numerosas transacciones sin tener que publicarlas en la blockchain. Cada transacción Lightning crea un nuevo estado del canal reflejado en una transacción de compromiso.
![LNP201](assets/en/77.webp)

3. **Aseguramiento y Cierre**: Los participantes se comprometen con el nuevo estado del canal intercambiando llaves de revocación para asegurar los fondos y prevenir cualquier engaño. Ambas partes pueden cerrar el canal cooperativamente haciendo una nueva transacción en la blockchain de Bitcoin, o como último recurso a través de un cierre forzado. Esta última opción, aunque menos eficiente porque es más larga y a veces mal evaluada en términos de comisiones, aún permite la recuperación de fondos. En caso de engaño, la víctima puede castigar al tramposo recuperando todos los fondos del canal en la blockchain.

![LNP201](assets/en/78.webp)

### La Red de Canales

Después de estudiar canales aislados, extendimos nuestro análisis a la red de canales:

- **Enrutamiento**: Cuando dos partes no están conectadas directamente por un canal, la red permite el enrutamiento a través de nodos intermediarios. Los pagos entonces transitan de un nodo a otro.

![LNP201](assets/en/79.webp)

- **HTLCs**: Los pagos que transitan a través de nodos intermediarios están asegurados por "_Hash Time-Locked Contracts_" (HTLC), que permiten que los fondos estén bloqueados hasta que el pago se complete de extremo a extremo.

![LNP201](assets/en/80.webp)

- **Enrutamiento Onion**: Para asegurar la confidencialidad del pago, el enrutamiento onion enmascara el destino final a los nodos intermediarios. El nodo emisor debe, por lo tanto, calcular toda la ruta, pero en ausencia de información completa sobre la liquidez de los canales, procede a través de pruebas sucesivas para enrutamiento del pago.

![LNP201](assets/en/81.webp)

### Gestión de Liquidez

Hemos visto que la gestión de liquidez es un desafío en Lightning para asegurar el flujo suave de pagos. Enviar pagos es relativamente simple: solo requiere abrir un canal. Sin embargo, recibir pagos requiere tener liquidez en el lado opuesto de los canales propios. Aquí algunas estrategias discutidas:

- **Atraer Canales**: Alentando a otros nodos a abrir canales hacia uno mismo, un usuario obtiene liquidez entrante.

- **Mover Liquidez**: Enviando pagos a otros canales, la liquidez se mueve al lado opuesto.

![LNP201](assets/en/82.webp)

- **Usar Servicios como Loop y Pool**: Estos servicios permiten reequilibrar o comprar canales con liquidez en el lado opuesto.
  ![LNP201](assets/en/83.webp)
- **Aperturas Colaborativas**: También hay plataformas disponibles para conectarse para realizar aperturas triangulares y tener liquidez entrante.

![LNP201](assets/en/84.webp)

# Conclusión

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Evalúe este curso

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusión

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
¡Felicitaciones! 🎉

¡Has completado la formación LNP 201 - Introducción a Lightning Network!

Puedes estar orgulloso de ti mismo, ya que no es un tema fácil.

Pocas personas se adentran tan profundamente en la madriguera de Bitcoin.

Un gran agradecimiento a **Fanis Michalakis** por brindarnos este excelente curso gratuito sobre el funcionamiento técnico de Lightning Network.

No dudes en seguirlo en [Twitter](https://x.com/FanisMichalakis), en [su blog](https://fanismichalakis.fr/) o a través de su trabajo en [LN Markets](https://lnmarkets.com/).

Ahora que dominas Lightning Network, te invito a explorar nuestros otros cursos gratuitos en Plan ₿ Network para profundizar en otros aspectos del invento de Satoshi Nakamoto:

#### Comprende cómo funciona una billetera Bitcoin con

https://planb.network/courses/cyp201

#### Descubre la historia de los orígenes de Bitcoin con

https://planb.network/courses/his201

#### Configura un servidor de pago BTC con

https://planb.network/courses/btc305

#### Domina los principios de privacidad en Bitcoin

https://planb.network/courses/btc204

#### Descubre los fundamentos de la minería con

https://planb.network/courses/min201

#### Aprende a crear tu comunidad Bitcoin con

https://planb.network/courses/btc302

