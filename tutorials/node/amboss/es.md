---
name: Amboss
description: Explorar y analizar Lightning Network
---

![cover](assets/cover.webp)



Lightning Network es una Layer del protocolo Bitcoin, que se desarrolló principalmente para promover la adopción de los pagos Bitcoin en el día a día aumentando la velocidad de procesamiento de cada transacción. Basado en el principio de descentralización, Lightning Network consiste en nodos (ordenadores que ejecutan una implementación de Lightning) que se comunican de igual a igual, retransmitiendo datos (pagos y verificación de pagos) entre sí.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Al igual que en la cadena principal, se ha vuelto esencial permitir a los usuarios conocer la información y el estado de la red, con el fin de facilitar las conexiones entre nodos y minimizar el problema de liquidez que suele surgir en la red. De hecho, en Lightning Network, se recomiendan micropagos de importes relativamente más pequeños que los de las transacciones en la cadena principal Bitcoin.



Es importante tener en cuenta que no todos los nodos Lightning están disponibles en la plataforma Amboss.



Al igual que [Mempool Space](https://Mempool.space), que proporciona información útil sobre la cadena principal del protocolo Bitcoin, desde 2022 [Amboss](https://amboss.space) proporciona información sobre :





- Nodos en Lightning Network
- Canales de pago y su capacidad de pago
- Evolución de Lightning Network a lo largo del tiempo
- Estadísticas sobre los cargos a los nodos de retransmisión por sus pagos.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

En este tutorial, te daremos un paseo por esta plataforma, que es un recurso esencial para los usuarios de Lightning Network, los que quieren conectar su nodo para ampliar la red, etc.




## Encontrar parejas



Uno de los objetivos de la plataforma Amboss es permitir que los distintos nodos de la red se conecten y comuniquen información entre sí. En la página de inicio de la plataforma, puedes buscar directamente el nombre de un nodo que ya conozcas, o encontrar nodos de las carteras Lightning más populares que utilices.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

En la página de inicio también encontrará nodos clasificados según :




- Evolución de la capacidad: la cantidad de Bitcoin asociada a la clave pública del nodo y el total disponible en todos sus canales.
- Evolución del canal: número de nuevas conexiones con otros nodos de la red.
- Popularidad del nodo: frecuencia de uso del nodo.



![nodes](assets/fr/03.webp)



Por tanto, para elegir el nodo al que conectarse hay que comprobar los siguientes criterios:





- Asegúrese de que el nodo tiene una cantidad suficiente de bitcoins; cuanto mayor sea la capacidad del nodo, mayor será la cantidad de bitcoins que podrá pagar.





- Asegúrese de que el nodo tiene un gran número de conexiones y canales abiertos con otros nodos de la red.





- Asegúrate de que el nodo está activo y sigue siendo apreciado por sus pares comprobando el número de canales nuevos; cuantos más canales nuevos tenga abiertos este nodo, más apreciado será por los demás nodos de la red.



Una vez que haya encontrado el nodo correcto, haga clic en su nombre para ser redirigido a la página de información del nodo.



En esta Interface, comprobando la Timestamp del canal recién creado, obtendrás una pista sobre la actividad de este nodo. También encontrarás información sobre la capacidad de los canales de este nodo: esta información es vital si quieres utilizar activamente este nodo para realizar tus pagos.




![node_info](assets/fr/04.webp)



En la sección de la izquierda, encontrará más detalles sobre la ubicación de este nodo. Por ejemplo, puede ver :




- La clave pública: el identificador situado justo debajo del nombre del nodo.
- La posición geográfica de este nodo.




![channels](assets/fr/05.webp)



Esta Interface le indica la Address de conexión para este nodo: toma la forma `pubkey@ip:port`. En nuestro ejemplo, queremos conectarnos al nodo cuyo :




- la clave pública `pubkey` es: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- El puerto: `9735`



![geoinfo](assets/fr/06.webp)



En la sección **Canales**, verás la lista de canales abiertos y las conexiones del nodo con otros nodos de la red. En este Interface, varios datos son vitales para confirmar que este nodo se corresponde con nuestras necesidades o es fiable:





- Ratio de entrada**: La cantidad que te cobrará el nodo por cada millón de Satoshi que reciba, en función del canal elegido.
- El ratio (partes por millón)** : que representa el número de Satoshi por millón de unidades que el nodo te cobrará cuando decidas hacer un pago a través de uno de sus canales. Digamos que decides hacer un pago de `10_000 Sats` a través de un canal cuyo ratio ppm es de `500 Sats`, tendrás que pagar al nodo `10_000 * 500 / 1_000_000` satoshis, equivalente a `5 Sats`.
- El máximo [HTLC](https://planb.academy/resources/glossary/htlc)** : La cantidad máxima que este nodo le permite transitar a través de uno de estos canales.



Consultando la tabla de este Interface, también puedes encontrar toda esta información sobre el nodo al que está emparejado.



![channels_info](assets/fr/07.webp)



En la sección **Mapas de canales**, puede ver la distribución y capacidad de los distintos canales de este nodo. Puede cambiar los criterios de distribución mostrados seleccionando una de las opciones de la lista desplegable de la derecha.



![cha_maps](assets/fr/08.webp)



La sección **Canales cerrados** agrupa todos los antiguos canales del nodo según el tipo de cierre:




- Cierre mutuo**: representa el acuerdo de ambas partes, que utilizan su clave privada para firmar la transacción que marca el cierre del canal y la distribución de saldos dentro del mismo
- Un **cierre forzado**: representa el cierre abrupto y unilateral de una parte del canal. Este tipo de cierre no es recomendable, ya que Lightning Network es un protocolo basado en el castigo: cuando intentas defraudar el saldo de un canal, te arriesgas a perder todo tu saldo disponible en ese canal.



![closed](assets/fr/09.webp)



Obtenga información sobre las tasas de tránsito por encaminar sus pagos a través de un canal en el nodo que utiliza



![fees](assets/fr/10.webp)



## Información sobre la red



Amboss no sólo se centra en la información de los miembros de la red, sino también en el estado de la propia red.



En la sección **Estadísticas**, en el menú de la izquierda "Simulaciones", encontrará un gráfico que muestra la probabilidad de éxito de un pago en función del importe del pago.



De hecho, observará que la curva es decreciente porque, a medida que aumenta el importe de su pago, tiene menos posibilidades de que ese pago se haga efectivo. Esto refleja el verdadero problema de liquidez de Lightning Network. Por ejemplo, un pago de 10.000 satoshis tiene un 79% de posibilidades de realizarse. Por otro lado, para un pago de 3.000.000 satoshis tienes menos del 13% de posibilidades de éxito.



![network](assets/fr/11.webp)



El menú **Estadísticas de red** permite visualizar gráficamente las estadísticas de :




- Medios de pago
- Nodos
- Capacidad
- Tarifas
- Evolución del canal.



![network_stat](assets/fr/12.webp)



En el menú **Estadísticas del mercado**, la opción **Detalles de las órdenes** le permite ver la demanda de liquidez en el Lightning Network. Este gráfico también puede mostrar qué canales son los más demandados y/o cuáles tienen una capacidad considerable.



![markets](assets/fr/13.webp)




## Herramientas



Amboss ofrece una serie de herramientas para ayudarle a optimizar sus búsquedas y acciones.



### Decodificador Lightning Network



Esta herramienta se encarga principalmente de ofrecerle detalles sobre la estructura de un Lightning Invoice, Lightning Address o Lightning URL.



En la página de inicio, en la sección **Herramientas**, envíe su Lightning Address, por ejemplo.



![decoder](assets/fr/14.webp)



A partir de este descodificador, puede obtener información como :




- la clave pública del nodo asociada a su Address Lightning;
- El tiempo de expiración de un Invoice de su Address;
- El mínimo y el máximo que puedes enviar;
- El nodo Nostr asociado con su Address, si Nostr está habilitado en este nodo.



![decode](assets/fr/15.webp)



### Magma IA



Descubra la última herramienta presentada por Amboss para gestionar eficazmente sus conexiones a los nodos Lightning Network. Magma AI utiliza inteligencia artificial dedicada para centrarse en un problema importante: hacer una buena selección de nodos a los que conectarse.



![magma](assets/fr/16.webp)



### Calculadora Satoshi



Averigüe el precio actual de Bitcoin en su moneda local (EUR / USD). En la página de inicio, utilice la calculadora de satoshis para averiguar el precio de mercado actual.



![calculator](assets/fr/17.webp)




Ya ha realizado un recorrido completo por las funciones y herramientas de análisis de la plataforma. A continuación encontrará nuestro artículo sobre el explorador Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f