---
name: Explorador BLOCKSTREAM
description: Explorar la Layer principal de Bitcoin y Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer es un proyecto que facilita la exploración de las transacciones y el Global State del protocolo Bitcoin, así como el [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid desarrollado por la empresa BLOCKSTREAM.



Iniciado en 2014 por BLOCKSTREAM, una empresa fundada por Adam Back, el explorador [BLOCKSTREAM.info](https://BLOCKSTREAM.info) tiene como objetivo proporcionar una infraestructura robusta para Bitcoin, garantizando la interoperabilidad y el seguimiento de transacciones entre capas (On-Chain y Liquid), al tiempo que mejora la seguridad y la privacidad de los usuarios.



En este tutorial, presentamos en qué se diferencia, sus servicios y cómo ofrece una supervisión sin fisuras de las operaciones y el estado de las capas On-Chain y Liquid de Bitcoin.



## Primeros pasos con BLOCKSTREAM



### Navegar por el canal principal



Cuando vaya al explorador BLOCKSTREAM.info, en el "**Dashboard**", el canal principal del protocolo Bitcoin está seleccionado por defecto. Desde este Interface, se tiene una visión general de :





- Tamaño de la cadena principal: Bloques minados recientemente.



![blocks](assets/fr/01.webp)



Esta sección proporciona información sobre los bloques minados recientemente, el Timestamp, el número de transacciones incluidas en cada BLOCK, el tamaño en kilobytes (kB) y la medida de cada BLOCK en unidades de peso (**WU** = *Weight Units*). Esta última medida es de interés, ya que nos permite evaluar la optimización de la BLOCK, dado que cada BLOCK de la cadena principal está limitada a `4.000.000 WU`, o `4.000 kWU`.





- Transacciones recientes.



![transactions](assets/fr/02.webp)



La sección de transacciones proporciona información sobre el identificador único de la transacción, el valor Bitcoin implicado, el tamaño en bytes virtuales (vB) -que representa la suma de todos los datos (entrada y salida)- y la tarifa asociada. Por ejemplo, una transacción con un tamaño de `153 vB` a una tasa de `2 sat/vB` tendrá un coste de `306 satoshis`.



### Exploración de fluidos



En el menú "**Bloques**" se puede seguir la historia de toda la cadena principal hasta el último BLOCK extraído.



![blocs](assets/fr/03.webp)



Haciendo clic en un BLOCK concreto, puede obtener más detalles sobre la información y las transacciones incluidas en él. Por ejemplo, para el BLOCK 919330: tienes el Hash del BLOCK. También puede navegar al BLOCK anterior, ya que cada BLOCK minado (salvo el Genesis) está vinculado al anterior, conservando el Hash de su predecesor.



![metadata](assets/fr/04.webp)



Al hacer clic en el botón **"Detalles "**, puede obtener más información sobre esta BLOCK, como su estado, que confirma que se ha añadido a la cadena principal retenida y propagada. También dispone de la dificultad a la que se mina este BLOCK: esta dificultad representa la potencia de cálculo necesaria para resolver el problema criptográfico del Mining y se ajusta cada 2016 bloques (unas 2 semanas).



![details](assets/fr/05.webp)



Debajo de esta sección de detalles, encontramos todas las transacciones incluidas en este BLOCK.



La primera transacción de la BLOCK se denomina **transacción coinbase**. Se utiliza para asignar la recompensa Mining de la Miner (todas las comisiones asociadas a las transacciones incluidas en la BLOCK y la subvención BLOCK). Los bitcoins creados por esta transacción sólo pueden gastarse una vez que se hayan minado otros 100 bloques consecutivos. En otras palabras, para poder utilizarlos, el Miner tendrá que esperar a que se produzca el BLOCK **919430**. Esto se conoce como [*"periodo de maduración "*](https://planb.network/fr/resources/glossary/maturity-period).



La coinbase es una transacción especial: es la única sin entrada real, ya que no gasta ningún bitcoin de una transacción anterior.




![coinbase](assets/fr/06.webp)



Todas las demás transacciones se dividen en dos secciones: entradas y salidas.



Para que los bitcoins puedan utilizarse como entradas en una nueva transacción, el iniciador de la misma debe demostrar su posesión proporcionando una firma que corresponda a un guión específico. Cada pieza de bitcoins (UTXO) contiene un script que generalmente requiere una firma específica que sólo la clave privada del titular puede proporcionar. Estos scripts son ***scriptSig*** (en ASM), escritos en Bitcoin Script, y pueden ser de varios tipos. En este ejemplo, podemos ver que los UTXOs utilizados eran de tipo P2SH a una salida de tipo P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Puede rastrear el historial de una UTXO concreta utilizando la heurística. Le invitamos a descubrir las diferentes heurísticas de Bitcoin y cómo reforzar la confidencialidad de sus transacciones de Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Tomemos el ejemplo del gasto saliente de esta transacción. Al hacer clic en el identificador de la transacción, se nos redirige a la sección **Transacciones** de la página de detalles de la transacción.



![transaction](assets/fr/08.webp)



Desde esta página, puede averiguar en qué BLOCK se incluyó la transacción. Dependiendo del tipo de Address utilizado, la transacción puede optimizar sus datos (*virtual bytes*) y, por tanto, pagar menos tasas de transacción. Esta transacción, por ejemplo, ahorró un 53% en comisiones al utilizar un formato nativo SegWit BECH32 Address que empieza por `bc1q`.



![trx_details](assets/fr/09.webp)



## Revestimiento Liquid



Liquid Network es un [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) y una solución de código abierto de nivel 2 para el protocolo Bitcoin. En concreto, permite transacciones Bitcoin más rápidas y confidenciales.



En el explorador BLOCKSTREAM.info, haga clic en el botón **"Liquid"** para pasar al Liquid Network.



![liquid](assets/fr/10.webp)



Al hacer clic en una de las transacciones que deseamos seguir, vemos que las cantidades de las piezas de Bitcoin se sustituyen por las palabras "**Confidencial**". En esta red, las transacciones pueden ser confidenciales, por lo que no podemos ver las cantidades de cada UTXO, ni dentro ni fuera de la transacción.



![liquid_trx](assets/fr/11.webp)



Sin embargo, observamos que los principios y mecanismos presentes en la Layer principal del protocolo Bitcoin son los mismos: guiones de bloqueo Bitcoin y trazabilidad UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network también proporciona activos digitales no depositarios que pueden ser utilizados por las organizaciones. En el menú **"Activos "**, encontrará una lista de los activos registrados, su total y el dominio al que se refieren.



![assets](assets/fr/13.webp)



Para cada activo, puede trazar el historial de transacciones de emisión y quema (eliminando el total en circulación).



![assets_trxs](assets/fr/14.webp)




## Más opciones



El explorador BLOCKSTREAM.info también incluye visualizaciones y seguimiento de transacciones en Testnet, Bitcoin, On-Chain y Liquid Network.



![testnet](assets/fr/15.webp)



Cuando vas a la red Testnet, no utilizas bitcoins reales, pero tienes todas las características descritas anteriormente.



![liquid_testnet](assets/fr/16.webp)



Esta red presenta una longitud de cadena diferente, a la que puede conectar y probar el funcionamiento de los mecanismos Bitcoin y Liquid.





- La sección API está dedicada a quien desee integrar determinadas funciones del Explorer en su propia aplicación. A través de esta API se puede interrogar a la cadena principal de las distintas capas (On-Chain y Liquid), realizar un seguimiento de las transacciones y averiguar las comisiones medias de las transacciones en una BLOCK, por ejemplo.



![api](assets/fr/17.webp)



Ya estás listo para explotar todo el potencial de BLOCKSTREAM Explorer para consultar blockchains en las capas On-Chain y Liquid. Esperamos que este tutorial te haya resultado informativo, y te recomendamos nuestro tutorial sobre otra Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f