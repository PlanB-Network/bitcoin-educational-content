---
name: Mempool
description: Explora todo el ecosistema Bitcoin.
---

![cover](assets/cover.webp)



El protocolo Bitcoin es una red seudónima, descentralizada y abierta a consultas. Los miembros (nodos), es decir, los ordenadores con una instancia del software Bitcoin, tienen acceso sin restricciones a todos los datos publicados en Bitcoin. Sin embargo, en los primeros años de Bitcoin, el protocolo no era tan ampliamente accesible como lo es hoy.


En los primeros días de Bitcoin, era necesario ejecutar un nodo Bitcoin para acceder a las herramientas adecuadas (bitcoin-cli) para interrogar a la red desde las líneas de comandos.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Por ello, se han puesto en marcha proyectos para ampliar la comunidad de Bitcoin, haciéndola más accesible a cualquiera que no posea un nodo y/o no tenga los conocimientos técnicos necesarios.



En este tutorial, veremos el proyecto **Mempool.space**, sus características y el impacto que ha tenido en el ecosistema Bitcoin.



## ¿Qué es Mempool.space?



**Mempool.space** es un explorador de código abierto que proporciona información útil sobre transacciones, tasas de transacción, bloques y mineros en las distintas redes del protocolo Bitcoin. Lanzado en 2020, aporta una mejora significativa de la experiencia de usuario mediante gráficos representativos, animaciones fluidas e interfaces despejadas.



Para entender el proyecto, una Mempool (reserva de memoria) es un espacio virtual en el que se almacenan todas las transacciones pendientes de confirmación en la red Bitcoin. Una Mempool es como una "sala de espera" en la que las transacciones de Bitcoin aguardan a ser confirmadas. Cada ordenador de la red (nodo) tiene su propia sala de espera, lo que explica por qué no todas las transacciones son visibles para todos al mismo tiempo.



El principal impacto de la plataforma en el ecosistema Bitcoin es que permite acceder a la variada información existente en las zonas de memoria de la mayoría de los nodos presentes en Bitcoin sin necesidad de ejecutar ninguno. Mempool.space es un repositorio para ver y buscar redes de protocolos de Bitcoin.



El uso cada vez más extendido en el ecosistema y el hecho de que Mempool.space sea de código abierto han permitido que se integre en cada vez más sistemas de alojamiento personales. Ahora puedes tener tu propia instancia de Mempool.space directamente en tu nodo personal. Vea a continuación nuestro tutorial sobre la configuración de Mempool.space en su nodo Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Los fundamentos de Mempool.space



Como ya se ha mencionado, [Mempool.space](https://Mempool.space) es un explorador de protocolos Bitcoin que le permite supervisar sus transacciones y su propagación en la red Bitcoin elegida en tiempo real, desde un Interface gráfico.



Mempool.space es compatible con muchas redes de protocolo Bitcoin.


En la barra de menús, encontrará las siguientes redes:




- **Mainnet**: La red principal de Bitcoin donde tienen lugar las transacciones reales de Bitcoin.
- **Signet**: Una red de prueba que utiliza firmas digitales para validar bloques sin requerir los recursos que necesita la red principal.
- **Testnet 3**: Una red de pruebas y desarrollo sin riesgos sobre el protocolo Bitcoin.
- **Testnet 4**: La nueva versión de Testnet 3 aporta mayor estabilidad y nuevas reglas de consenso al entorno de pruebas.



![reseaux](assets/fr/01.webp)



En la página de inicio, a la izquierda en Green, verás los posibles futuros bloques (grupos de transacciones) listos para ser validados e integrados (minados) en la red Bitcoin. Por término medio, se mina un bloque cada diez minutos: conserve esta información, ya que le resultará útil más adelante en nuestro desarrollo.


En morado, a la derecha, encontrará los bloques minados recientemente en Bitcoin, con el número del último bloque minado representando la altura actual de la red.



![blocs](assets/fr/02.webp)



La sección **Tasas de transacción** es una estimación de las tasas de transacción. Cuanto más altas sean las comisiones asignadas a su transacción, más probable será que su transacción se añada al siguiente bloque listo para ser minado.


Las comisiones por transacción representan el coste que le supondrá a Miner insertar su transacción en un bloque candidato para Mining. Se define mediante un ratio de sat/vB (Satoshi/Virtual Bytes) que representa el número de satoshis que pagas por el espacio que ocupará tu transacción en el bloque candidato.



⚠️ IMPORTANTE: En caso de saturación de Mempool, los mineros dan prioridad a las transacciones que ofrezcan la mejor relación Satoshi/vByte. Cuanto más pesada (grande) sea tu transacción, más satoshis necesitará para ser incluida rápidamente.



![fees-visualizer](assets/fr/03.webp)



La sección **Gafas Mempool** permite visualizar el espacio ocupado por una transacción.



![mempool](assets/fr/04.webp)



Se mina un bloque aproximadamente cada diez minutos debido a la dificultad del Proof of Work que los mineros deben proporcionar para añadir su bloque candidato a la cadena de bloques minados. Esta dificultad varía cada **2016 bloques**, lo que equivale a unas **2 semanas**. Puede ver la evolución de esta dificultad aquí.



![difficulty](assets/fr/05.webp)



La adición de un nuevo bloque a la cadena principal da derecho al Miner del bloque validado a una recompensa compuesta por una parte fija (dividida a la mitad cada 210.000 bloques**, lo que equivale a unos 4 años** durante las divisiones) y las comisiones de transacción.



![halving](assets/fr/06.webp)



## Acceda a los detalles de su transacción



En la barra de búsqueda de Mempool.space, puede introducir su Bitcoin Address o su transaction ID para saber más sobre su historial.



![search](assets/fr/07.webp)



En la página de detalles de la transacción, encontrará información general sobre su transacción:




- **Estado**: Confirmado cuando se añade a un bloque, sin confirmar cuando espera en un Mempool.
- **Comisiones de transacción**.
- **Tiempo estimado de llegada (ETA)**: El tiempo aproximado que tardará su transacción en añadirse a un bloque. Se calcula en función del ratio que constituyen las comisiones asociadas a esta transacción.



![general-txinfo](assets/fr/08.webp)



La sección **Flujo** muestra un gráfico de los componentes de su transacción.



Entradas (UTXO anteriores), utilizadas para su transacción, y salidas que dan a los destinatarios el derecho a utilizar los bitcoins de cada salida presentando la firma requerida para su gasto.



![flow](assets/fr/09.webp)



Encontrará más detalles sobre las direcciones utilizadas en la sección **Entradas y Salidas**.



![address](assets/fr/10.webp)



Descubra los diferentes esquemas de transacción Bitcoin para mejorar su confidencialidad.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Agilice sus transacciones



En el ecosistema Bitcoin, el aspecto de la validación de transacciones por parte de los mineros está intrínsecamente ligado a las tasas de transacción asociadas a esa transacción. Los mineros dan prioridad a las transacciones con un mayor ratio de tasas (satoshis/vBytes), lo que podría afectar a la validez de su transacción si no paga tasas razonables aceptadas por los mineros. Su transacción quedaría atascada en Mempool a la espera de un bloque que acepte su ratio de tasas.



Afortunadamente, hay dos métodos disponibles en la red Bitcoin para acelerar la confirmación de su transacción.





- **RBF** - Sustitución por comisión: Método que le permite gastar las mismas entradas que su transacción de baja comisión, pero esta vez aumentando la comisión de la transacción para acelerar la validación. Su nueva transacción se validará más rápidamente y se incluirá en un bloque, invalidando la transacción de tarifa baja.



Puede realizar una acción de sustitución de comisiones con carteras que acepten este mecanismo. Por ejemplo, consulte nuestro artículo sobre la cartera Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Un enfoque inspirado en RBF, pero del lado del receptor. Cuando la transacción de la que eres receptor se bloquea en una Mempool, tienes la opción de gastar las salidas (UTXOs) de esta transacción, a pesar de que aún no se haya confirmado, asignando más comisiones a esta nueva transacción para que las comisiones medias -de la transacción de la que eres receptor y de la transacción iniciada- animen a los mineros a incluir ambas transacciones en un bloque.



⚠️ La primera transacción debe incluirse en un bloque para permitir que se confirme la segunda transacción.



Si todos estos términos le parecen demasiado técnicos, le recomiendo que [consulte nuestro glosario](https://planb.academy/resources/glossary), que contiene definiciones de todos los términos técnicos relacionados con Bitcoin y su ecosistema.



Además de estos métodos, Mempool.space, gracias a sus conexiones con más del 80% de los mineros presentes en la red Bitcoin, también le permite acelerar cualquiera de sus transacciones **sin confirmar**, incluso aquellas que no activen RBF, pagando una contraprestación a los mineros de Exchange por insertar su transacción de bajo coste en el siguiente bloque listo para ser minado.



En la página de detalles de la transacción, haga clic en el botón **Accelerar** y proceda a pagar su contrapartida a los mineros.



![accelerate-section](assets/fr/11.webp)


## Menores



Un Miner se refiere a una persona que gestiona una mina, es decir, un ordenador que participa en el proceso Mining, que consiste en participar en Proof-of-Work. El Miner agrupa las transacciones pendientes en su Mempool para formar un bloque candidato. A continuación, busca un Hash válido, menor o igual que el objetivo, para la cabecera de este bloque modificando los distintos nonces. Si encuentra un Hash válido, difunde su bloque a la red Bitcoin y se embolsa la recompensa pecuniaria asociada, compuesta por la subvención del bloque (creación de nuevos bitcoins ex-nihilo), y la tasa de transacción.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

los mineros son como "validadores" que verifican y agrupan las transacciones en bloques. Para añadir un nuevo bloque a la red Bitcoin, tienen que resolver un complejo rompecabezas matemático (el Proof-of-Work). El primer Miner que resuelva el rompecabezas gana una recompensa Bitcoin (subvención del bloque + comisiones por las transacciones incluidas en el bloque).



La dificultad de este Proof of Work se monitoriza, lo que permite visualizar la evolución de la potencia de cálculo necesaria para los mineros. Usted encontrará en las secciones a continuación :





- Una estimación de las recompensas totales cosechadas por los mineros durante el último ajuste de dificultad, así como estimaciones del próximo Halving de la concesión de bloques, que se produce cada 210.000 bloques (aprox. 04 años).



![rewards](assets/fr/12.webp)



Esta dificultad se ajusta cada 2016 bloques (unas dos semanas). Es inversamente proporcional al tiempo medio que tardan los mineros en Miner cada 2016 bloques.


Cuando el tiempo medio empleado por los mineros es inferior a 10 minutos, la dificultad aumenta, lo que demuestra que a los mineros les resultó más fácil validar los bloques de Miner. Por el contrario, cuando el tiempo medio empleado es superior a 10 minutos, la dificultad disminuye. Por el contrario, cuando el tiempo medio empleado es superior a 10 minutos, la dificultad disminuye.



![mining-pool](assets/fr/13.webp)





- Grupos de mineros: Dada la dificultad que entraña, un grupo de mineros colabora para ayudar a encontrar la Proof of Work en Bitcoin, en lo que llamamos un **pool**. Cuando un bloque es minado por el grupo, la recompensa obtenida se distribuye según el porcentaje de éxito en la búsqueda de la solución parcial de cada Miner, es decir, la contribución en potencia de cálculo en la búsqueda de Proof-of-Work, o según el método de remuneración acordado por la cooperación.





![mining](assets/fr/14.webp)



## Infraestructura Lightning Network



Mempool no sólo proporciona información sobre la infraestructura de red de Bitcoin (cadena principal). También integra herramientas de visualización y exploración de la superposición Lightning de Bitcoin.



En la sección **Lightning**, puede ver todas las conexiones existentes entre los nodos Lightning.



![network-stats](assets/fr/15.webp)



Esta Interface proporciona información sobre :





- Estadísticas Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **IMPORTANTE**: La capacidad de un canal de pago designa la cantidad máxima que un nodo puede enviar a otro nodo durante una transacción Lightning.





- Los nodos de rayos se asignan en función del proveedor de servicios de Internet (servicio de alojamiento) y, opcionalmente, en función de la capacidad del canal de pago.



![distribution](assets/fr/17.webp)





- La historia de la capacidad global del Lightning Network.


También encontrará una clasificación de estos nodos según la capacidad de sus canales de pago.



![ranking](assets/fr/18.webp)



## Más gráficos



Mempool.space es la plataforma ideal para disfrutar de la interacción con las redes del protocolo Bitcoin. Los gráficos no sólo ofrecen datos visuales que le ayudarán a decidir cuándo realizar transacciones, sino también parámetros precisos que le permitirán visualizar, en tiempo real, la solidez y la salud de la red Bitcoin y las infraestructuras Lightning asociadas.



En la sección **Gráficos**, puede ver datos esenciales sobre la red Bitcoin:




- Evolución del tamaño de Mempool: Puedes observar cómo fluctúa el tamaño de Mempool, lo que puede indicar periodos de alta o baja actividad en la red.



![graphs](assets/fr/19.webp)






- La evolución de las transacciones y las comisiones por transacción en la red elegida: El seguimiento de las variaciones de las transacciones por segundo permite anticiparse a los periodos de congestión o baja actividad y optimizar las comisiones por transacción. Este gráfico te da una perspectiva de la capacidad de la red para gestionar el volumen de transacciones.



![graphs](assets/fr/20.webp)



Ahora que ha llegado al final de su viaje en Mempool.space, conviértase en su propio explorador y siga sus transacciones en tiempo real. A continuación encontrarás nuestro artículo sobre el explorador de Bitcoin **Public Pool**.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1