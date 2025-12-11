---
name: Blockstream Explorer
description: Explorar la capa principal de Bitcoin y Liquid Network
---

![cover](assets/cover.webp)



El Blockstream Explorer es un proyecto que facilita la exploración de las transacciones y el estado global del protocolo Bitcoin, así como del [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid desarrollado por la empresa Blockstream.



Iniciado en 2014 por Blockstream, una empresa fundada por Adam Back, el explorador [blockstream.info](https://blockstream.info) tiene como objetivo proporcionar una infraestructura robusta para Bitcoin, garantizando la interoperabilidad y el seguimiento de transacciones entre capas (on-chain y Liquid), al tiempo que mejora la seguridad y la privacidad del usuario.



En este tutorial, veremos en qué se diferencia, sus servicios y cómo ofrece una supervisión perfecta de las operaciones y el estado de las capas on-chain y Liquid de Bitcoin.



## Introducción al explorador de Blockstream



### Navegar por el canal principal



Cuando accedes al explorador de Blockstream.info, en el "**Dashboard**", la cadena principal del protocolo Bitcoin está seleccionada por defecto. Desde esta interfaz, tiene una visión general de los protocolos :





- Tamaño de la cadena principal: Bloques minados recientemente.



![blocks](assets/fr/01.webp)



Esta sección proporciona información sobre los bloques minados recientemente, la marca de tiempo, el número de transacciones incluidas en cada bloque, el tamaño en kilobytes (kB) y la medida de cada bloque en unidades de peso (**WU** = *Weight Units*). Esta última medida es de interés, ya que nos permite evaluar la optimización del bloque, dado que cada bloque de la cadena principal está limitado a `4.000.000 WU`, o `4.000 kWU`.





- Transacciones recientes.



![transactions](assets/fr/02.webp)



La sección de transacciones proporciona información sobre el identificador único de la transacción, el valor de bitcoin implicado, el tamaño en bytes virtuales (vB) -que representa la suma de todos los datos (entrada y salida)- y la tarifa asociada. Por ejemplo, una transacción con un tamaño de `153 vB` a una tasa de `2 sat/vB` tendrá una tasa de `306 satoshis`.



### Exploración de fluidos



Desde el menú "**Bloques**", puede seguir la historia de toda la cadena principal hasta el último bloque extraído.



![blocs](assets/fr/03.webp)



Si hace clic en un bloque concreto, podrá obtener más detalles sobre la información y las transacciones que incluye. Por ejemplo, para el bloque 919330: verá el hash del bloque. También puede navegar al bloque anterior, ya que cada bloque minado (salvo Genesis) está vinculado al anterior, conservando el hash de su predecesor.



![metadata](assets/fr/04.webp)



Al hacer clic en el botón **"Detalles "**, puede obtener más información sobre este bloque, como su estado, que confirma que se ha añadido a la cadena principal conservada y propagada. También dispone de la dificultad a la que se mina este bloque: esta dificultad representa la potencia de cálculo necesaria para resolver el problema criptográfico de mining y se ajusta cada 2016 bloques (unas 2 semanas).



![details](assets/fr/05.webp)



Debajo de esta sección de detalles, encontramos todas las transacciones incluidas en este bloque.



La primera transacción del bloque se denomina **transacción coinbase**. Se utiliza para asignar la recompensa mining del minero (todas las comisiones asociadas a las transacciones incluidas en el bloque y la concesión del bloque). Los bitcoins creados por esta transacción sólo pueden gastarse una vez que se hayan minado otros 100 bloques consecutivos. En otras palabras, para poder utilizarlos, el minero tendrá que esperar a la producción del bloque **919430**. Esto se conoce como [*"periodo de madurez "*](https://planb.academy/fr/resources/glossary/maturity-period).



La coinbase es una transacción especial: es la única sin entrada real, ya que no gasta ningún bitcoin de una transacción anterior.




![coinbase](assets/fr/06.webp)



Todas las demás transacciones se dividen en dos secciones: entradas y salidas.



Para que los bitcoins puedan utilizarse como entradas en una nueva transacción, el iniciador de la misma debe demostrar su posesión proporcionando una firma que corresponda a un guión específico. Cada pieza de bitcoins (UTXO) contiene un script que generalmente requiere una firma específica que sólo la clave privada del titular puede proporcionar. Estos scripts son ***scriptSig*** (en ASM), escritos en Bitcoin Script, y pueden ser de varios tipos. En este ejemplo, podemos ver que los UTXOs utilizados eran de tipo P2SH a una salida de tipo P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Puede rastrear el historial de una UTXO específica utilizando heurísticas. Le invitamos a descubrir las diferentes heurísticas de Bitcoin y las formas de reforzar la confidencialidad de sus transacciones en Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Tomemos el ejemplo del gasto saliente de esta transacción. Al hacer clic en el identificador de la transacción, se nos redirige a la sección **Transacciones** de la página de detalles de la transacción.



![transaction](assets/fr/08.webp)



Desde esta página, puede averiguar en qué bloque se incluyó la transacción. Dependiendo del tipo de dirección utilizada, la transacción puede optimizar sus datos (*bytes virtuales*) y, por tanto, pagar menos tasas de transacción. Esta transacción, por ejemplo, ahorró un 53% en comisiones al utilizar un formato de dirección nativo de SegWit Bech32 que empieza por `bc1q`.



![trx_details](assets/fr/09.webp)



## Capa Liquid



Liquid Network es una [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) y una solución de código abierto de nivel 2 para el protocolo Bitcoin. En concreto, permite transacciones bitcoin más rápidas y confidenciales.



En el explorador de Blockstream.info, haz clic en el botón **"Liquid"** para cambiar a la red Liquid.



![liquid](assets/fr/10.webp)



Al hacer clic en una de las transacciones que queremos rastrear, vemos que los importes de los trozos de bitcoin se sustituyen por las palabras "**Confidencial**". En esta red, las transacciones pueden ser confidenciales, por lo que no podemos ver las cantidades de cada UTXO, ni dentro ni fuera de la transacción.



![liquid_trx](assets/fr/11.webp)



Sin embargo, observamos que los principios y mecanismos presentes en la capa principal del protocolo Bitcoin son los mismos: scripts de bloqueo bitcoin y trazabilidad UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network también proporciona activos digitales no depositarios que pueden ser utilizados por las organizaciones. En el menú **"Activos "**, encontrará una lista de los activos registrados, su total y el dominio al que se refieren.



![assets](assets/fr/13.webp)



Para cada activo, puede trazar el historial de transacciones de emisión y quema (eliminando el total en circulación).



![assets_trxs](assets/fr/14.webp)




## Más opciones



El explorador Blockstream.info también incluye visualizaciones y seguimiento de las transacciones en Testnet, Bitcoin, on-chain y Liquid Network.



![testnet](assets/fr/15.webp)



Cuando vas a la red Testnet, no utilizas bitcoins reales, pero tienes todas las características descritas anteriormente.



![liquid_testnet](assets/fr/16.webp)



Esta red presenta una longitud de cadena diferente, a la que puede conectar y probar el funcionamiento de los mecanismos Bitcoin y Liquid.





- La sección API está dedicada a quien desee integrar determinadas funciones del Explorador en su propia aplicación. A través de esta API se puede interrogar a la cadena principal de las distintas capas (on-chain y Liquid), realizar un seguimiento de las transacciones y averiguar las comisiones medias de las transacciones de un bloque, por ejemplo.



![api](assets/fr/17.webp)



Ya estás listo para explotar todo el potencial de Blockstream Explorer para consultar blockchains en las capas on-chain y Liquid. Esperamos que este tutorial te haya resultado informativo, y te recomendamos nuestro tutorial sobre otro explorador Bitcoin:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f