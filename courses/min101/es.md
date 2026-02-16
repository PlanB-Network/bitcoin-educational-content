---
name: Introducción a Bitcoin mining
goal: Entender Bitcoin mining y proof-of-work desde cero
objectives: 


  - Comprender proof-of-work y su papel en Bitcoin.
  - Analizar el mecanismo de ajuste de la dificultad.
  - Sepa qué significan realmente los términos técnicos asociados a la mining.
  - Describa los pasos necesarios para construir un bloque Bitcoin y sus componentes.
  - Identificar los principales avances de la industria del mining.


---

# Descubra los fundamentos de Bitcoin mining



Entender la proof of work es entender cómo funciona la Bitcoin. Sin este invento y su ingenioso uso, Bitcoin simplemente no podría haber existido. Este curso te proporciona toda la teoría de la mining que necesitas para tu viaje bitcoin.



MIN 101 está dirigido principalmente a principiantes, ya que explica todos los conceptos partiendo precisamente de cero. Sin embargo, si ya tiene un nivel intermedio de conocimientos, este curso le permitirá consolidar su comprensión, corregir algunas intuiciones aproximadas y explorar detalles que a menudo faltan en las explicaciones convencionales.



Al final de este curso, será capaz de explicar cómo funciona proof-of-work de forma sencilla y rigurosa. MIN 101 es también una introducción ideal a todos los demás cursos más avanzados dedicados a Bitcoin mining sobre Plan ₿ Academy, ya sean teóricos o prácticos.



+++


# Introducción


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Resumen del curso


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Bienvenido al curso MIN 101, en el que descubrirás los conceptos teóricos fundamentales de mining y Proof-of-Work dentro del sistema Bitcoin. Este curso es el primer paso en tu viaje bitcoiner para entender cómo funciona mining. Una vez que lo hayas completado, podrás pasar a cursos teóricos más avanzados, ¡o ponerte manos a la obra y convertirte tú mismo en un minero de bitcoin!



En este curso MIN 101, no volveremos sobre los conceptos básicos de Bitcoin, ya que iremos directamente al meollo de la cuestión: mining. Si nunca has oído hablar de la Bitcoin, o si sus fundamentos aún no te quedan claros, te recomiendo encarecidamente que empieces con nuestro curso introductorio BTC 101. Una vez que hayas adquirido estos fundamentos, podrás abordar MIN 101 con confianza:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Parte 1 - Introducción



Vamos a empezar este curso con un primer capítulo opcional, en el que ofrezco una explicación muy simplificada de mining, para darte una imagen mental clara antes de entrar en los mecanismos técnicos.



El objetivo no es darte todos los detalles técnicos (vendrán más adelante en el curso), sino ofrecerte un hilo conductor. Una vez establecido este marco, cada concepto más avanzado que se introduzca después encajará de forma natural en esta estructura.



### Parte 2 - Funcionamiento del proof of work



Tras la introducción, la Parte 2 es la base técnica del programa de formación. Su objetivo es explicar, paso a paso, cómo Bitcoin produce bloques válidos. Empezaremos por descubrir la estructura de un bloque, antes de adentrarnos en el mecanismo de proof-of-work: el papel del target, el nonce y la función hash. Por último, veremos cómo Bitcoin consigue mantener una tasa de producción de bloques estable a pesar de las variaciones en la potencia hash, gracias al mecanismo de ajuste de la dificultad. Al final de esta sección, tendrás una comprensión completa de los principios fundamentales de proof-of-work de Bitcoin.



### Parte 3 - El sistema de incentivos Bitcoin mining



En la tercera parte, veremos por qué se anima a los mineros a participar honestamente en mining. Detallaremos el principio de la recompensa por bloque, su composición y método de cálculo, su evolución en el tiempo a través de halvings y el papel específico de la transacción coinbase.



### Parte 4 - La industria Bitcoin mining



La cuarta parte devuelve mining a su realidad operativa. Recorre la evolución de las máquinas de mining, desde los inicios de Bitcoin hasta la moderna ASIC, con el fin de comprender las limitaciones actuales del hardware. También examinamos los fundamentos de los pools de mining, para entender cómo se las arreglan los mineros para reducir la varianza de sus ingresos.



### Parte 5 - Sección final



En la parte final del curso, podrá poner a prueba sus conocimientos de mining mediante la obtención de un diploma.



El objetivo de este curso MIN 101 es, por tanto, permitirle salir de él con una comprensión clara, estructurada y duradera del Bitcoin mining, tanto desde el punto de vista técnico como económico.



¿Listo para descubrir Bitcoin mining? Empecemos




## Bitcoin mining más fácil


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Antes de pasar a una explicación detallada y más técnica de la Bitcoin mining, me gustaría ofrecerle una visión general del principio, deliberadamente sencilla y esquemática. Si ya tienes algunos conocimientos básicos, puedes ir directamente al meollo de la cuestión en el capítulo siguiente, después de responder a las preguntas del cuestionario. Este capítulo está dirigido sobre todo a los principiantes, para que empiecen con buen pie.



Imagina Bitcoin como un gran cuaderno público, compartido por todos, donde anotamos quién envió bitcoins a quién. Este cuaderno se llama blockchain. No puede estar en manos de una sola persona, pues de lo contrario habría que confiar en ella. En su lugar, Bitcoin funciona de forma colectiva: miles de ordenadores verifican y mantienen la misma versión de este cuaderno.



![Image](assets/fr/049.webp)



En Bitcoin, cuando se realiza un pago, se crea una transacción. Esta transacción no se añade instantáneamente al cuaderno. Primero se envía a la red y luego espera a ser integrada en el siguiente paquete de transacciones. Este paquete se denomina bloque.



![Image](assets/fr/050.webp)



Un bloque es simplemente un conjunto de transacciones agrupadas. Cuando un bloque está listo, no basta con publicarlo. Hay que demostrar a la red que el bloque merece ser añadido al pool. Aquí es donde entra en juego mining.



Mining es el trabajo de validar un bloque consumiendo energía. Unos actores llamados mineros utilizan ordenadores especializados. Estas máquinas consumen electricidad para realizar un número muy elevado de pruebas, en bucle, hasta que encuentran una prueba que la red acepta. Cuando un minero encuentra esta prueba, su bloque se considera válido.



Una vez validado, el bloque se transmite a la red. Los demás nodos comprueban rápidamente que cumple las normas y lo añaden a la secuencia de bloques anteriores. Por eso se llama "cadena de bloques": cada nuevo bloque viene después de los demás, en orden secuencial, y esta cadena crece poco a poco.



![Image](assets/fr/051.webp)



En resumen, primero se crean las transacciones. A continuación, se agrupan en un bloque. A continuación, un minero valida este bloque consumiendo electricidad. Por último, este bloque se añade a la cadena de bloques y las transacciones que contiene se confirman.



Si los mineros consumen electricidad, no es porque sean voluntarios. Lo hacen porque hay una recompensa. Cuando un minero valida un bloque, recibe dos tipos de ingresos. Por un lado, recibe bitcoins recién creados. Por otro, cobra las tasas que pagan los usuarios por las transacciones incluidas en el bloque. En otras palabras, el minero es compensado tanto a través de la emisión monetaria programada, como por las tasas de transacción determinadas por un mercado.



En esta fase, se le ofrece deliberadamente una visión muy simple de mining. Todavía no se explica cómo se construye el bloque en detalle, ni cómo funciona exactamente la prueba que buscan los mineros, ni cómo Bitcoin mantiene un ritmo constante, ni cómo se calcula con precisión la recompensa, ni cómo se reclama. No pasa nada, ¡eso es todo lo que vamos a ver en el resto de este curso MIN 101!



El objetivo de este capítulo era simplemente darte una estructura mental clara: transacciones → bloques → mining → blockchain → recompensa. Mantén esta cadena de ideas en mente. En el resto del curso, cada capítulo añadirá una capa de detalles técnicos sobre uno de estos elementos, hasta que entiendas no solo qué está pasando, sino cómo y por qué funciona de forma fiable, a escala, sin jefe y sin necesidad de confianza.



# Cómo funciona proof of work


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## La ruta de transacción Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Para entender en qué consiste Bitcoin mining, primero tenemos que seguir la ruta de una transacción típica de Bitcoin. Esto le mostrará exactamente dónde entra en juego el bloque y por qué está en el corazón del sistema. Esto le mostrará exactamente dónde entra en juego el bloque, y por qué está en el corazón del sistema. Eso es lo que quiero que descubras en este primer capítulo.



En Bitcoin, una transacción es una estructura de datos que transfiere la propiedad de bitcoins de un usuario a otro. En concreto, consume "salidas" de transacciones anteriores (las denominadas UTXO), denominadas "entradas", y crea nuevas "salidas" que definen a quién pertenecen ahora esos bitcoins y en qué condiciones pueden gastarse posteriormente.



![Image](assets/fr/001.webp)



Un punto importante sobre Bitcoin es la autorización para gastar. Las Bitcoin no están en una cuenta, como podría estarlo su dinero en el banco, sino que están bloqueadas por condiciones de gasto. Cuando una wallet quiere utilizar una UTXO como entrada, debe proporcionar una prueba criptográfica de que tiene derecho a desbloquearla. Esta prueba suele adoptar la forma de una firma digital generated a partir de una clave privada. Por eso los bitcoiners insisten en asegurar sus claves privadas: son éstas las que desbloquean el acceso a sus bitcoins y, en consecuencia, les permiten gastarlos.



![Image](assets/fr/002.webp)



La firma digital de Bitcoin desempeña dos funciones importantes:




- Autorizar el gasto: demuestra que el usuario posee la clave privada esperada por la condición de gasto UTXO;
- Protección de la integridad: vincula la autorización a los detalles precisos de la transacción (destinatarios, importes, comisiones, etc.). Si alguien altera la transacción después, la firma dejará de ser válida.



Una vez que la transacción ha sido correctamente construida y firmada por la Bitcoin del usuario, debe ser difundida en la red Bitcoin.



### El papel del nodo Bitcoin en la distribución



Bitcoin es una red entre iguales: no hay un servidor central que reciba y procese todas las transacciones. Este papel lo desempeñan colectivamente los nodos. Un nodo de Bitcoin es una pieza de software (por ejemplo, Bitcoin Core) conectada a otros nodos de la red Bitcoin, cuya misión principal es verificar, almacenar y retransmitir transacciones y bloques.



Cuando envías una transacción desde una wallet, ésta la reenvía a un nodo (el tuyo o el de un servicio). Este nodo comprobará primero que la transacción cumple varias normas, como:




- las firmas son válidas;
- las entradas hacen referencia a UTXO existentes (es decir, bitcoins que existen);
- estos UTXO no se hayan gastado ya en otro sitio;
- la cantidad de salidas es menor o igual que la cantidad de entradas (los bitcoins no se crean de la nada);
- etc.



Si la transacción supera todas estas comprobaciones, el nodo la propaga a los demás nodos de la red con los que está conectado. Éstos, a su vez, la comprueban y la retransmiten, y así sucesivamente. En cuestión de segundos, la transacción se propaga y pasa a ser conocida por toda la red Bitcoin, o al menos por una gran parte de ella.



![Image](assets/fr/003.webp)



### El mempool: la sala de espera de las transacciones



Entre el momento en que se emite una transacción y el momento en que se confirma en un bloque, debe esperar. Esta zona de espera se denomina **mempool** (contracción de `memory` y `pool`). Un mempool es, por tanto, un espacio de almacenamiento temporal para transacciones válidas, pero aún no confirmadas.



Punto importante: no existe un único mempool, sólo mempools. Cada nodo mantiene su propia mempool, con sus propias restricciones locales. Esto significa que, en un momento dado, dos nodos pueden tener contenidos de mempool ligeramente diferentes (dependiendo de lo que hayan recibido, lo que hayan rechazado o lo que hayan purgado).



![Image](assets/fr/004.webp)



En esta fase, la red conoce la transacción, la ha verificado y la mantiene en memoria hasta que se confirma. Pero la confirmación de esta transacción sólo se producirá cuando un minero la inserte en un bloque y éste sea aceptado por la red.



### Blockchain: un registro público de sellado de tiempo



Como bitcoin es una moneda intangible, tiene que resolver un problema: evitar el doble gasto sin una autoridad central. Si dos transacciones intentan gastar la misma UTXO, todas deben poder converger en un estado único y coherente. Satoshi Nakamoto resume esta cuestión con esta famosa frase:



> La única manera de confirmar la ausencia de una transacción es estar al tanto de todas las transacciones.

En otras palabras, para saber que un bitcoin no se ha gastado ya, se necesita un registro común de gastos anteriores.



Esta es la función de la cadena de bloques: un registro público que contiene el historial de transacciones. Pero en lugar de escribir cada transacción a medida que se produce, Bitcoin las agrupa en bloques. Cada bloque actúa como una página del historial, y el sistema funciona así como un servidor de marcas de tiempo: ordena las transacciones a lo largo del tiempo de forma verificable.



Este registro no puede reescribirse, gracias a un sencillo principio: cada bloque incluye la huella criptográfica (hash) del bloque anterior. Así, los bloques están vinculados: si se modifica un bloque del pasado, su hash cambia, lo que rompe el vínculo con el bloque siguiente, que a su vez rompe el vínculo con el bloque posterior, y así sucesivamente. Es esta cadena de dependencias la que da nombre a la "*cadena de bloques*".



![Image](assets/fr/005.webp)



Una vez comprendidos estos principios básicos de la Bitcoin, podemos describir el objetivo de un minero en términos más concretos: construir un nuevo bloque que amplíe la cadena existente, inscribiendo las transacciones pendientes, y luego intentar que sea válido (es la famosa "proof of work" que estudiaremos en un capítulo posterior). Pero antes, descubramos juntos en el próximo capítulo cómo se construye un bloque candidato.



## Construcción de un bloque Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Ahora ya has entendido cómo funciona una transacción Bitcoin y el papel de la blockchain. Sin embargo, antes de ver con más detalle cómo funciona la proof-of-work, todavía hay un paso esencial que el minero debe realizar: la construcción de un bloque candidato. Averigüemos juntos qué es un bloque candidato y cómo lo construye el minero, antes de embarcarnos en la búsqueda de una prueba válida.



### El bloque candidato



Los Miner tienen que construir ellos mismos sus bloques antes de intentar minarlos. Cada minero, a su vez, construye lo que se conoce como bloque candidato a partir de las transacciones pendientes en su mempool. La construcción de un bloque candidato consiste, por tanto, en:




- elegir qué transacciones incluir;
- organizar estas transacciones de forma compatible con las normas de Bitcoin;
- producir los metadatos del bloque, almacenados en su cabecera.



La elección de las transacciones sigue una lógica económica simple: un bloque tiene una capacidad limitada por el protocolo Bitcoin, por lo que el minero busca maximizar lo que gana por este espacio. Selecciona prioritariamente las transacciones que ofrecen las tasas más elevadas en relación con el espacio que ocupan en el bloque (lo que se conoce como "tasa de tasas", expresada en sats/vB). Los detalles de las comisiones se tratarán más adelante; basta con recordar la idea de clasificación por eficiencia espacial.



Por lo tanto, un bloque Bitcoin consta de dos partes principales:




- una lista de transacciones;
- una cabecera de bloque, que sirve, en cierto modo, como documento de identidad del bloque.



![Image](assets/fr/006.webp)



La cabecera es esencial, ya que se utiliza como base para la proof-of-work: en la Bitcoin, no se mina un bloque entero directamente; sólo se mina la cabecera de un bloque, que resume la información necesaria para vincular el bloque a la cadena y consignar su contenido. Para que la cabecera represente todas las transacciones, Bitcoin utiliza una herramienta criptográfica: el árbol de Merkle.



### El árbol de Merkle: resumir un gran conjunto de transacciones



Listar todas las transacciones en la cabecera sería imposible: un bloque puede contener miles de transacciones, mientras que la cabecera tiene un tamaño fijo (80 bytes). Por tanto, la solución consiste en calcular un hash único que depende de todas las transacciones del bloque: es la raíz de Merkle.



El principio es el siguiente:




- se calcula la huella criptográfica (hash) de cada transacción;
- estos hashes se emparejan, se concatenan y se vuelven a hashear para formar una nueva capa de hashes;
- este proceso se repite hasta obtener un único hash final: la raíz de Merkle.



![Image](assets/fr/007.webp)



Así, si una transacción cambia, aunque sea un solo bit, el resultado es una modificación de su huella digital, que se propaga a la raíz Merkle. Esta raíz está incluida en la cabecera del bloque. Por lo tanto, modificar una transacción pasada significa modificar la cabecera del bloque en el que está incluida, y por lo tanto la huella del bloque, y luego el enlace con los bloques posteriores.



Desde SegWit, hemos separado las firmas del resto. Así que, en realidad, hay 2 árboles de Merkle anidados dentro de cada bloque. Esta separación tiene consecuencias para la forma en que contamos el tamaño de un bloque y para ciertos compromisos criptográficos, pero la idea básica sigue siendo la misma: la cabecera debe comprometer, de forma compacta, todo el contenido del bloque.



### Cabecera de bloque



La cabecera del bloque tiene 80 bytes y contiene exactamente 6 campos. Son estos seis elementos los que se hashearán al buscar un proof of work (véase el capítulo siguiente):





- La versión (`version`): Indica a qué reglas o señales de actualización se adhiere el bloque. Sirve como mecanismo para mantener la compatibilidad y evolución del protocolo.




- Hash del bloque anterior (`previousblockhash`): Es el hash de la cabecera del bloque anterior. Es lo que une los bloques. Sin este campo, tendríamos bloques independientes. Al incluir el hash de la cabecera del bloque anterior, obtenemos una cadena, en la que cada nuevo bloque se basa en el anterior.





- Raíz de Merkle (`merkleroot`): Es la huella digital de todas las transacciones del bloque (a través del árbol de Merkle). Vincula la cabecera al contenido: si el minero modifica la selección o el orden de las transacciones, la raíz cambia.





- Marca de tiempo: Se trata de una marca de tiempo (hora Unix) elegida por el minero (con restricciones de validez), que debe indicar cuándo se minó el bloque. No tiene que ser perfectamente exacta al segundo, pero debe cumplir ciertas condiciones para seguir siendo aceptable para la red.





- Objetivo de dificultad codificado (`nbits`): Este campo codifica el objetivo de dificultad actual. Entraremos en más detalle en el capítulo sobre dificultad, pero recuerda que este parámetro forma parte de la cabecera.





- Nonce (`nonce`): Es un valor que el minero puede modificar libremente. Sirve como variable ajustable durante proof-of-work. Explicaré su función con más detalle en el próximo capítulo, pero es importante entender que el nonce forma parte de la cabecera del bloque y está diseñado para permitir intentos sucesivos.



Para que esto sea más fácil de visualizar, he aquí un ejemplo de una cabecera de bloque en formato hexadecimal (80 bytes):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



He aquí un desglose campo por campo:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Este encabezado de bloque candidato, construido por el minero, constituye la base de su trabajo. Cuando se busca un proof-of-work válido, no es toda la lista de transacciones la que se somete directamente a hash en un bucle, sino este bloque de 80 bytes, que contiene todo lo necesario para vincular el bloque al pasado y consignar su contenido, al tiempo que incluye los parámetros necesarios para el mecanismo mining, que exploraremos en el próximo capítulo.



## El hash, el objetivo y el nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



En los capítulos anteriores, has seguido el camino de una transacción Bitcoin: creada y firmada por un wallet, retransmitida por nodos, almacenada en mempools, y luego confirmada cuando un minero la incluye en un bloque aceptado por la red. Pero aún no hemos visto cómo un minero puede añadir su bloque a la cadena de bloques. ¿Cuál es el proceso detrás de mining?



Entender el proceso mining es bastante sencillo. Se reduce a 3 conceptos que van de la mano: una función hash, un valor objetivo y una variable que el minero puede modificar. Veamos cómo funciona todo.



### La función hash



Una función hash es una herramienta que toma un mensaje como entrada y produce una salida de tamaño fijo, llamada "*fingerprint*" o "*hash*".



![Image](assets/fr/010.webp)



La función hash es interesante en los sistemas informáticos porque tiene ciertas propiedades:





- Si cambias un solo bit de la entrada, el hash de salida resultante cambia completamente y de forma impredecible;



![Image](assets/fr/011.webp)





- Es imposible pasar de la salida a la entrada: la función es irreversible;



![Image](assets/fr/012.webp)





- Es imposible encontrar dos mensajes diferentes que den exactamente el mismo hash.



![Image](assets/fr/013.webp)



La función hash utilizada en Bitcoin para mining es `SHA256`, aplicada dos veces seguidas. Esto se conoce como doble SHA256, o "SHA256d". Este doble hash es el que produce la huella digital del bloque.



```text
hash = SHA256(SHA256(message))
```



En nuestro caso, el `mensaje` corresponde de hecho a la cabecera del bloque, que ya viste en el capítulo anterior. Como recordatorio, la cabecera es una pequeña estructura que resume todo lo que hay en el bloque.



![Image](assets/fr/014.webp)



### Prueba de trabajo: encontrar un hash más pequeño que el objetivo



A menudo se dice que Proof-of-Work resuelve un problema complejo. En realidad, no se trata tanto de un problema como de una búsqueda por ensayo y error: el minero debe encontrar una versión de la cabecera cuyo hash (tras pasar por la función hash `SHA256d`) respete una sencilla condición: debe ser menor que un determinado objetivo.



Esta condición se formula del siguiente modo:




- el hash de la cabecera del bloque se calcula utilizando una función hash;
- interpretamos este hash como un número;
- para que el bloque sea válido, este número debe ser menor o igual que un valor llamado "*objetivo de dificultad*".



En otras palabras, un bloque es válido si:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



El objetivo es un número de 256 bits. Como el hash producido por `SHA256d` también es de 256 bits, pueden compararse como dos números. Cuanto más bajo sea el objetivo, más difícil será la condición, ya que hay menos resultados posibles por debajo de este umbral. Por el contrario, cuanto más alto sea el objetivo, más fácil será satisfacer la condición y más fácil será minar un bloque. Veremos más detenidamente cómo se determina este objetivo en capítulos posteriores.



En este sistema, la función hash es interesante. Recuerda que es fácil calcular la salida a partir de la entrada, pero imposible encontrar una entrada conociendo sólo la salida de la función. En mining, a los mineros no se les pide que encuentren un hash preciso, sino que encuentren un hash por debajo de un valor objetivo. La única forma de conseguirlo es realizar un gran número de intentos, hasta que un encabezado concreto de su bloque candidato, al ser sometido a hash, produzca un hash menor que este objetivo.



Una vez que el objetivo es suficientemente bajo, este proceso se vuelve costoso. El minero calcula el hash de la cabecera de su bloque candidato, comprueba el resultado y, si no se cumple la condición, modifica la cabecera y repite el cálculo. Este bucle se repite hasta que se encuentra una cabecera válida. Cuando el hash de la cabecera cumple finalmente la condición, se establece la proof of work, el bloque se considera válido y puede difundirse en la red Bitcoin para que los nodos lo añadan a su blockchain. El minero ganador recibe entonces la recompensa asociada (detallaremos su composición más adelante), mientras que todos los mineros parten inmediatamente en busca de una nueva cabecera válida para el siguiente bloque.



La ventaja fundamental de este mecanismo reside en su asimetría. Producir un proof of work es costoso para los mineros, ya que requiere un gran número de cálculos hash. En cambio, para los verificadores, es decir, los nodos de la red, la verificación es extremadamente sencilla: todo lo que tienen que hacer es hacer un hash de la cabecera del bloque suministrada por el minero y comprobar que el hash resultante es efectivamente inferior al objetivo. Por tanto, encontrar una prueba requiere mucho trabajo y recursos, mientras que verificar su validez es rápido y barato. Es precisamente esta propiedad la que define un sistema proof-of-work eficiente.



### El nonce



Queda una cuestión práctica: si la cabecera del bloque candidato construida por el minero no da un hash válido, ¿cómo puede el minero volver a intentarlo? Necesita modificar algo en la cabecera para obtener un hash diferente. Esta es precisamente la función del nonce.



Recuerda la primera propiedad de una función hash: basta con cambiar un solo bit de la entrada para producir un hash de salida totalmente diferente e impredecible. Por lo tanto, cada cálculo hash es similar a un sorteo aleatorio.



![Image](assets/fr/016.webp)



Para volver a probar suerte, el minero no necesita modificar toda la cabecera de su bloque candidato: sólo necesita cambiar una pequeña parte de ella, porque incluso un solo bit diferente dará lugar a un hash completamente nuevo, potencialmente válido si es más pequeño que el objetivo.



Esta es precisamente la razón por la que la cabecera del bloque contiene un nonce. El nonce es un valor de 32 bits que se utiliza una vez y luego se sustituye. En la práctica, para un mismo bloque candidato, un minero puede probar unos 4.290 millones de valores posibles (de `0` a `2^32 - 1`). Cada variación del nonce modifica la cabecera del bloque y, en consecuencia, cambia por completo el hash producido tras aplicar la función hash `SHA256d`.



El proceso mining es muy sencillo:




- el minero construye un bloque candidato (transacciones + cabecera);
- calcula el hash del `SHA256d(header)`;
- si el resultado es mayor que el objetivo, cambia el nonce;
- comienza de nuevo;
- etc.



![Image](assets/fr/017.webp)



De hecho, el nonce no es el único campo que puede modificarse. Cualquier modificación dentro de las transacciones de un bloque provoca un cambio en la raíz del árbol de Merkle y, por tanto, una modificación de la cabecera de ese bloque. Con la potencia informática moderna, recorrer los 4.290 millones de valores posibles del nonce puede hacerse con relativa rapidez. Por eso existe otro campo, generalmente denominado "*extra-nonce*", que multiplica aún más las posibilidades de variación de la cabecera. Volveremos sobre este mecanismo con más detalle en un capítulo posterior.



### ¿Qué sentido tiene proof of work?



Lo llamamos "prueba" porque el resultado es inmediatamente verificable: una vez producido un bloque, cualquier nodo puede comprobar, en una fracción de segundo, que el hash criptográfico de su cabecera está efectivamente por debajo del objetivo exigido. Lo llamamos "trabajo" porque lograr este hash requiere multitud de intentos y, por tanto, un coste real en términos de computación y energía.



En el Libro Blanco de Bitcoin, Satoshi Nakamoto presenta dos ventajas de utilizar un sistema proof-of-work en Bitcoin:





- Sealing la historia económica:**



Una vez gastada la carga computacional, el bloque queda bloqueado: modificarlo exigiría rehacer el proof of work de ese bloque. Y como los bloques están encadenados, alterar un bloque antiguo también implicaría recalcular todos los bloques posteriores, y entonces alcanzar y superar el trabajo en curso de la cadena honesta.



En otras palabras, la proof-of-work sirve de columna vertebral del sistema de sellado de tiempo, haciendo cada vez más costosa la falsificación del pasado a medida que se acumulan bloques. Cuando se extrae un nuevo bloque, la seguridad proporcionada por la proof of work se aplica simultánea y uniformemente a todas las UTXO existentes. Con cada bloque añadido, cada UTXO acumula así una cantidad adicional de seguridad de la Proof-of-Work.





- Definir la regla de la mayoría (consenso) y neutralizar Sybil:**



Proof-of-Work también permite a Bitcoin llegar a un consenso sin depender de la regla de votación "un ID = un voto", que podría ser fácilmente falseada por la creación masiva de identidades (IPs, nodos, claves...).



En Bitcoin, la "*mayoría*" no es el mayor número de participantes, sino la **cadena que acumula más trabajo**. Como dice Satoshi, se trata de un principio de "una CPU = un voto", es decir, un voto ponderado por la potencia de cálculo real gastada para producir bloques válidos. Por tanto, desplegar miles de nodos no aporta ninguna ventaja en sí mismo sobre Bitcoin. Sin potencia de cálculo adicional, no se acumulan más pruebas de trabajo, y el ataque Sybil se vuelve inútil, mientras que la regla de decisión sigue siendo objetiva y no requiere la identificación de los participantes.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008), *Bitcoin: A Peer-to-Peer Electronic Cash System* (https://bitcoin.org/bitcoin.pdf)



Los principios relativos a la utilidad y las facultades de los menores son un tema muy complejo, en el que no profundizaré en este curso. No obstante, volveremos a tratar este tema en profundidad en futuros cursos de formación MIN 201.



Por el momento, se puede resumir cómo funciona mining así: los mineros construyen un bloque candidato con las transacciones pendientes en los mempools, y luego buscan un hash de su cabecera (mediante `SHA256d`) que sea menor o igual que un objetivo. Lo consiguen probando nonces mediante ensayo y error.



En el próximo capítulo, daremos un breve rodeo histórico por el principio proof-of-work para comprender sus antecedentes y, a continuación, veremos cómo determina el sistema el objetivo de dificultad.



## La historia de proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



La prueba de trabajo no se inventó para Bitcoin. Satoshi Nakamoto retomó y ensambló varias ideas anteriores, ya exploradas en diferentes contextos.



### Hashcash



A finales de la década de 1990, el problema del spam por correo electrónico adquirió gran importancia. En efecto, si enviar un correo electrónico no cuesta casi nada, un spammer puede enviar millones. Pero si cada mensaje requiere un pequeño esfuerzo computacional, enviar un solo mensaje legítimo sigue siendo fácil para un usuario normal, mientras que enviar millones de mensajes resulta muy caro.



Este es el objetivo de Hashcash, propuesto por Adam Back en 1997, que se considera la invención del principio proof-of-work. El principio de Hashcash es muy similar al de mining: producir un hash que respete una condición (tener un cierto número de ceros al principio del hash). La prueba acompaña entonces al mensaje y puede ser verificada muy rápidamente por el destinatario. Si se recibe un correo electrónico que no contiene esta prueba, puede considerarse inmediatamente spam y, por tanto, filtrarse. Los spammers se ven entonces obligados a gastar una cantidad considerable de energía para enviar millones de mensajes, lo que reduce drásticamente (o incluso anula por completo) la rentabilidad de este tipo de operaciones, ya sean de marketing o fraudulentas.



Hoy en día, Hashcash no se utiliza para el correo electrónico. El filtrado de spam se basa ahora en gran medida en sistemas centralizados. La ventaja de Hashcash sobre las soluciones actuales radica en que no requiere un filtrado centralizado: cualquiera puede ajustar los parámetros según sus propios criterios. Tampoco requiere identificación, ya que la búsqueda de hash puede realizarse de forma anónima. Sobre todo, no se basa en un sistema de reputación, que tiende a introducir formas subjetivas de filtrado.



Hashcash no pretendía crear dinero. Pretendía imponer un coste marginal a una acción digital fácilmente automatizable.



![Image](assets/fr/008.webp)



### Bit Oro



A finales de la década de 1990 y principios de la de 2000, Nick Szabo exploró la idea de la escasez digital basada en la proof of work. Su proyecto conceptual, denominado Bit Gold, prevé la creación de unidades de valor mediante la resolución de una costosa proof of work y la posterior inscripción de estas pruebas en un registro para establecer una forma de propiedad.



Bit Gold no dio lugar a un sistema desplegado como Bitcoin, pero sí contiene varias ideas importantes: la idea de que la computación puede producir escasez, y la idea de marcar el tiempo de los elementos a lo largo del tiempo para crear una historia difícil de reescribir.



### RPOW



En 2004, Hal Finney propuso RPOW (*Reusable Proofs of Work*). La idea era producir pruebas de trabajo que pudieran intercambiarse, en lugar de simplemente consumirse. RPOW pretendía crear token digitales basadas en proof of work, con un sistema para verificar y transferir estas token sin duplicarlas. RPOW, de nuevo, no resolvió satisfactoriamente el problema de un registro totalmente descentralizado como haría más tarde Bitcoin, pero sigue siendo uno de los grandes precursores de Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold y RPOW utilizan proof-of-work para imponer un coste y crear una forma de escasez. Bitcoin retoma este mecanismo, pero le otorga un papel central y colectivo: proof-of-work no sólo se utiliza para crear algo, sino también para decidir quién tiene derecho a escribir la siguiente página del registro (el siguiente bloque), y para hacer que este registro sea costoso de falsificar.



## Ajustar el objetivo de dificultad


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



En capítulos anteriores se ha visto el corazón de la proof-of-work: los mineros hacen hash de la cabecera de su bloque candidato con `SHA256d`, y el bloque sólo se considera válido si el hash resultante es numéricamente menor o igual que un valor de referencia llamado objetivo. La pregunta sigue siendo: ¿de dónde procede este objetivo y cómo garantiza el sistema que se mantenga constante a lo largo del tiempo?



Bitcoin aspira a un ritmo medio de un bloque encontrado cada 10 minutos. Obviamente, este ritmo no está garantizado al segundo. En la práctica, algunos bloques se encuentran unos segundos después del anterior, mientras que otros se encuentran después de más de una hora. Lo que importa aquí es la media durante un periodo suficientemente largo.



![Image](assets/fr/019.webp)



Esta variabilidad se debe a la naturaleza probabilística de mining: cada hash es un intento independiente, con una probabilidad constante (suponiendo que el objetivo permanezca invariable) de producir un resultado inferior al objetivo. Por tanto, puede compararse a una lotería con un sorteo continuo: cuantos más hashes hagan los mineros por segundo, menor será el retraso esperado antes de la aparición de un bloque válido, pero sin eliminar nunca la aleatoriedad de un sorteo al siguiente.



### ¿Por qué 10 minutos entre bloque y bloque?



Aunque no hay pruebas de ello, Satoshi Nakamoto seguramente eligió 10 minutos como compromiso práctico entre eficacia y seguridad. Un intervalo más corto daría confirmaciones más frecuentes, pero provocaría más divisiones temporales de la red. Para entender este punto, tenemos que volver a la forma en que se propaga un bloque.



Cuando un minero encuentra un bloque válido, lo distribuye inmediatamente a sus pares. Los nodos que lo reciben comprueban su validez (transacciones, proof of work, reglas de consenso, etc.), y luego lo retransmiten a su vez. Esta propagación lleva cierto tiempo, limitado por la latencia de Internet, el ancho de banda y la capacidad de cada nodo para verificar el bloque.



![Image](assets/fr/020.webp)



Si, durante este retraso en la difusión, otro minero también descubre un bloque válido a la misma altura, la red puede dividirse temporalmente: una parte de los nodos y mineros confían en el bloque A, mientras que la otra confía en el bloque B. Se trata de una división temporal de la red.



![Image](assets/fr/021.webp)



Estas divisiones no son catastróficas. El consenso Nakamoto predice que, a largo plazo, sólo prevalecerá una rama: la que acumule más trabajo. De hecho, en cuanto se mina un nuevo bloque encima del bloque A, por ejemplo, toda la red se resincroniza en esta rama y abandona el bloque B, que se convierte entonces en un "*bloque rancio*", a veces llamado erróneamente "*bloque huérfano*" en el lenguaje cotidiano.



![Image](assets/fr/022.webp)



Por otro lado, tienen un coste: durante unos minutos, una fracción de los mineros trabaja en una rama que será abandonada. Este trabajo se desperdicia entonces desde el punto de vista de la seguridad global, ya que no ha contribuido a la cadena final. Cuanto más rápido sea el intervalo entre cada bloque, mayor será la probabilidad de que se produzcan estas divisiones, ya que el tiempo de propagación representa una mayor proporción del tiempo entre cada bloque.



El intervalo de 10 minutos suele dar tiempo suficiente para que el bloque ganador se propague ampliamente antes de que se encuentre un bloque competidor a la misma altura. Es un compromiso que limita las divisiones, reduce la potencia de cálculo desperdiciada y ayuda a la red a mantenerse sincronizada a escala global.



### Comprender hashrate



*"Hashrate*" se refiere a la cantidad de computación hash producida por segundo, ya sea por un solo minero, un grupo de mineros, o todos los mineros en Bitcoin. Se expresa en `H/s` (hashes por segundo), con múltiplos como `TH/s` (terahashes por segundo) o `EH/s` (exahashes por segundo). Esto representa el número de intentos que los mineros pueden hacer cada segundo para intentar obtener un hash inferior al objetivo.



Si el objetivo permanece fijo, entonces:




- cada intento tiene una probabilidad fija de éxito;
- hacer más intentos por segundo aumenta la probabilidad de que aparezca rápidamente un intento ganador


En otras palabras, si la red Bitcoin de mañana duplica su potencia de cálculo conectando el doble de máquinas mining, sin un mecanismo corrector, los bloques se encontrarían por término medio el doble de rápido. Por tanto, el objetivo debe ajustarse para compensar las variaciones de hashrate.



### Ajustar el objetivo de dificultad



Bitcoin resuelve este problema con un mecanismo de ajuste periódico del objetivo, que ajusta la dificultad de mining. El principio es el siguiente: cada 2016 bloques (aproximadamente cada 2 semanas), cada nodo vuelve a calcular el objetivo de dificultad observando cuánto tiempo se necesitó realmente para producir esos 2016 bloques.



El objetivo de este mecanismo es reducir el tiempo medio de producción de un bloque a unos 10 minutos, mientras que la hashrate global de la red cambia constantemente, debido a que se desconectan máquinas o, por el contrario, se añaden otras nuevas.



![Image](assets/fr/023.webp)



El cálculo se basa en el tiempo observado durante el periodo transcurrido:




- si los últimos bloques de 2016 se encontraron demasiado rápido, esto significa que hashrate aumentó durante este periodo; entonces Bitcoin dificulta la condición reduciendo el objetivo para el siguiente periodo;
- si los bloques de 2016 se encontraron demasiado despacio, significa que hashrate ha disminuido; Bitcoin alivia la condición aumentando el objetivo.



La fórmula es la siguiente:



```txt
Tn = To * (Ta / Tt)
```



Con:




- `tn`: nuevo objetivo
- `to`: objetivo antiguo
- `Ta`: tiempo real transcurrido de los últimos 2016 bloques
- `Tt`: tiempo objetivo (en segundos)



Con un tiempo objetivo de dos semanas, es decir, `Tt = 1.209.600` segundos:



```txt
Tn = To * (Ta / 1 209 600)
```



Para entender cómo ajustar la dificultad de Bitcoin mining, he aquí un ejemplo con valores ficticios:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Con:



- `**Hasta = 18.045.755.102**`: Antiguo objetivo, es decir, el valor de referencia antes del ajuste.
- `**ta = 1.000.000 segundos**`: Tiempo realmente empleado en producir los últimos 2016 bloques. Como este tiempo es inferior al tiempo objetivo, la red ha minado demasiado rápido.
- `**1.209.600 segundos**`: Tiempo objetivo correspondiente a 10 minutos por bloque para los bloques de 2016, utilizado como referencia para el ajuste.
- `**tn = 14.918.779.020**`: Nuevo objetivo calculado tras el ajuste de dificultad.



En este caso, el nuevo objetivo es inferior al anterior, lo que significa que mining se vuelve más dura para frenar la producción de bloques en el próximo periodo.


*Los valores objetivo de este ejemplo están simplificados y escalados con fines didácticos; el objetivo real utilizado en Bitcoin es un entero de 256 bits de un orden de magnitud completamente distinto.*



Este cálculo lo realiza localmente cada nodo, basándose en las marcas de tiempo introducidas en los bloques. Como todos los nodos aplican las mismas reglas, llegan al mismo resultado, y el nuevo objetivo se convierte en la referencia común para los siguientes bloques de 2016.



Hay que tener en cuenta un detalle importante sobre este ajuste: **está limitado**. Bitcoin limita la variación de la dificultad por periodo para evitar cambios demasiado bruscos que podrían bloquearla. De hecho, el tiempo real que se tiene en cuenta está constreñido a permanecer dentro de un rango equivalente a un factor de 4 (mínimo una cuarta parte del objetivo antiguo, máximo cuatro veces el objetivo antiguo). De este modo se evita un reajuste extremo si las marcas de tiempo son muy atípicas o están muy manipuladas.



### Representación de objetivos



En la cabecera del bloque, el objetivo no aparece en su forma completa de 256 bits, ya que ocuparía demasiado espacio. En su lugar, el campo `nBits` de 32 bits codifica el objetivo en un formato compacto, comparable a la notación científica de base 256: un exponente (1 byte) y un coeficiente (3 bytes). El objetivo completo se reconstruye a partir de estos dos valores. No entraremos aquí en detalles, ya que el tema es relativamente complejo y no aporta nada a la comprensión de mining. Sólo hay que recordar que el objetivo no se almacena en bruto en la cabecera del bloque, sino en forma compacta.



Con este último capítulo de la Parte I, hemos hecho un recorrido por el funcionamiento de proof-of-work en Bitcoin: el minero construye un bloque candidato seleccionando transacciones de su mempool, calcula la cabecera del bloque candidato, lo hashea, compara el hash resultante con el objetivo del periodo y vuelve a empezar modificando el nonce hasta obtener un hash válido. Por último, cada 2016 bloques, la red recalcula un nuevo objetivo para mantener un tiempo medio de unos 10 minutos por bloque, a pesar de las constantes variaciones de hashrate.




# El sistema de incentivos Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Como puede imaginar, Bitcoin mining no es una actividad altruista. Los Miner tienen costes reales: electricidad para hacer funcionar sus ordenadores mining, compra de equipos especializados, nóminas para el mantenimiento, a veces locales y sistemas de refrigeración. Para que el sistema de Bitcoin funcione, los intereses privados de los mineros deben alinearse con los intereses colectivos de la red. Esta es exactamente la función de la recompensa de mining. Anima a los mineros a invertir en proof of work, a incluir transacciones válidas y a respetar las reglas del protocolo en lugar de intentar corromperlo.



Esta lógica se basa en la teoría de juegos: el protocolo hace que la honradez sea racional. Un minero gana dinero cuando produce un bloque válido aceptado por los nodos. Por el contrario, si intenta hacer trampas, su bloque será rechazado por los nodos y no ganará nada. Como producir un bloque tiene un coste, un bloque rechazado representa una pérdida directa. En un entorno competitivo en el que miles de jugadores buscan simultáneamente un bloque válido, la estrategia más rentable, la mayoría de las veces, es por tanto seguir estrictamente las reglas y maximizar sus ingresos honestamente.



Para conseguirlo, el protocolo Bitcoin estipula que el minero que encuentre un bloque válido gana el derecho a incluir en él una transacción concreta, lo que le otorga una determinada suma de BTC. Esto se conoce como **recompensa de bloque**. Esto se conoce como **recompensa de bloque**. En este primer capítulo de esta sección, el objetivo es entender de qué se compone y cómo se determina. Más adelante, veremos cómo evoluciona la parte de la creación del dinero a lo largo del tiempo (con los halvings) y cómo se cobra realmente desde el punto de vista técnico (a través de la transacción coinbase).



### ¿En qué consiste la recompensa en bloque?



En capítulos anteriores vimos cómo los mineros consiguen encontrar un bloque válido. Una vez que un minero ha encontrado una cabecera cuyo hash es menor que el objetivo, su bloque candidato se considera válido. Entonces puede distribuirlo a toda la red Bitcoin. El bloque se añade al resto de la cadena de bloques, confirmando las transacciones que contiene.



Es precisamente este acontecimiento (la adición real del bloque a la cadena de bloques) el que desencadena la entrega de una recompensa al minero ganador. Esta recompensa se compone de dos elementos distintos que se suman:




- subvención en bloque**;
- gastos de transacción**.



![Image](assets/fr/024.webp)



Veamos a qué corresponden estas dos partes de la recompensa.



### Subvención en bloque



La subvención por bloque corresponde a la parte de creación monetaria de la recompensa. Cuando un minero produce un bloque válido, el protocolo le autoriza a crear un cierto número de nuevos bitcoins y a asignárselos a sí mismo como recompensa. Estos bitcoins se crean ex nihilo. No existían antes.



Sin embargo, la cantidad de bitcoins de nueva creación no es en absoluto arbitraria. Está estrictamente definida por las reglas del protocolo Bitcoin y es idéntica para todos los mineros. Analizaremos más detenidamente este mecanismo en el próximo capítulo, ya que la subvención no es un valor fijo indefinidamente: se reparte periódicamente según un calendario preciso. Por ahora, basta con recordarlo:




- la subvención por bloque es uno de los dos componentes de la recompensa por bloque;
- está limitado y determinado por el protocolo, no por el minero (aunque técnicamente el minero puede solicitar menos de la cantidad máxima);
- crea bitcoins de la nada.



Esta subvención desempeña dos funciones principales dentro del protocolo Bitcoin. La primera es animar a los jugadores a participar en mining. En los primeros años de Bitcoin (y a veces todavía hoy), las comisiones por transacción eran muy bajas. Por tanto, la subvención ha garantizado una compensación suficiente para atraer a los mineros y mantener un nivel de seguridad para el sistema.



La segunda función está relacionada con la distribución de la moneda. Toda nueva moneda se enfrenta a la cuestión de cómo distribuir equitativamente las unidades monetarias entre la población. La subvención por bloques ofrece una respuesta a este problema. Al crear bitcoins mediante la mining, permite su distribución inicial de forma abierta y neutral: cualquiera puede obtenerlos, siempre que participe en la mining, sin necesidad de autorización ni identificación previas.



Por otra parte, como estos bitcoins se crean de la nada, su valor no carece de base. Al aumentar la cantidad de dinero en circulación, la subvención diluye mecánicamente el valor de los bitcoins existentes. Por tanto, introduce una forma de inflación monetaria. Sin embargo, veremos en el próximo capítulo que esta subvención está destinada a desaparecer gradualmente, y que la inflación acabará por cesar.



![Image](assets/fr/025.webp)



### Comisiones de transacción



El segundo componente de la recompensa por bloque está vinculado al uso del sistema: cuando un usuario publica una transacción, quiere que se confirme. Sin embargo, el espacio en bloque es limitado, y los bloques sólo aparecen por término medio cada 10 minutos aproximadamente. El espacio de bloques es, por tanto, un recurso escaso. Cuando la demanda supera a la oferta, el precio sube: es el mercado de comisiones por transacción. Cada minero que consigue producir un bloque válido obtiene el derecho a cobrar, por su cuenta, la totalidad de las tasas de transacción asociadas a todas las transacciones que ha incluido en su bloque.



Se puede pensar en él como un sistema de subastas: cada transacción propone un importe de comisión, y los mineros dan prioridad a las que maximizan sus ingresos, con limitaciones de espacio. Este mecanismo alinea los intereses de forma natural:




- los usuarios con prisa pagan más para ser incluidos rápidamente;
- se anima a los mineros a incluir transacciones que paguen las tasas más altas por el espacio de bloque.
- la red evita el spam, porque publicar una transacción tiene un coste.



#### ¿Cómo se calculan las comisiones por transacción?



Contrariamente a la creencia popular, las comisiones no son un producto de una transacción Bitcoin. De hecho, una transacción gasta entradas y crea salidas. Las entradas representan el origen de los bitcoins utilizados, mientras que las salidas representan el destino de los pagos. Las comisiones de transacción son simplemente **la diferencia entre el total de entradas y el total de salidas**.



En otras palabras, las entradas de bitcoin del usuario, que le pertenecen, crean salidas para los receptores, pero no reproducen la cantidad total consumida por las entradas. La diferencia entre ambas representa las tasas de transacción que puede cobrar el minero.



Veamos un ejemplo. Una transacción consume dos entradas, una de `100.000 sats` y otra de `150.000 sats`, y crea tres salidas de `35.000 sats`, `42.000 sats` y `170.000 sats`.



![Image](assets/fr/027.webp)



La suma de las entradas es, por tanto, de 250.000 sats`, mientras que la suma de las salidas es de 247.000 sats`. Esto significa que se han consumido `3.000 sats` en entradas sin que se hayan vuelto a crear en salidas: esta cantidad corresponde a las tasas propuestas por esta operación.



![Image](assets/fr/028.webp)



Si un minero incluye esta transacción en un bloque válido, tendrá derecho a recuperar estos `3.000 sats`, además de las tasas de todas las demás transacciones incluidas en el bloque. Sin embargo, no existe un vínculo directo on-chain entre la transacción que paga la tasa y los sats realmente cobrados por el minero. Técnicamente, los 3.000 sats` en comisiones se destruyen y, a cambio, el minero obtiene el derecho a volver a crear la misma cantidad para sí mismo.



#### La tasa



Un bloque no está limitado por el número de transacciones, sino por su capacidad total (hoy, en la práctica, por el peso del bloque). Algunas transacciones ocupan más espacio que otras: una transacción con muchas entradas y salidas será mayor que una simple transacción con una sola entrada y dos salidas. Los scripts utilizados también influirán en el tamaño.



![Image](assets/fr/026.webp)



Por tanto, dos transacciones pueden pagar la misma cantidad de tasas en términos absolutos, pero no ser económicamente equivalentes desde el punto de vista del minero. Si una es el doble de grande, cuesta el doble de espacio en el bloque. El espacio es escaso, por lo que el minero busca maximizar sus ingresos por unidad de espacio.



Por eso, en la práctica, expresamos la competitividad de una transacción con un ratio de tasas, normalmente en `sats/vB` (satoshis por byte virtual). Calcular este ratio es sencillo:



```text
fee rate = fee / weight (in vB)
```



Por ejemplo, si tenemos una transacción que pesa 141 vB y que asigna 1.974 sats en comisiones, tendrá una tasa de comisión de 14 sats/vB.



```text
1 974 / 141 ≈ 14 sats/vB
```



Esta relación explica las decisiones económicas tomadas por los mineros: con una capacidad fija, incluir transacciones de alto coste maximiza las tasas totales del bloque y, por tanto, la compensación del minero. También explica por qué las transacciones de bajo coste permanecen en cola en los mempools durante largos periodos: compiten con otras transacciones que pagan más por unidad de espacio.



### Protección de la red contra el spam



Las tarifas también sirven a un propósito de seguridad operativa: introducen un coste a la multiplicación de transacciones. Si publicar una transacción fuera gratis, sería fácil inundar la red de transacciones inútiles y saturar los mempools, aumentando la carga de los nodos.



En la práctica, los nodos aplican políticas locales de retransmisión (reglas de mempool) y a menudo fijan un umbral mínimo de tarifa por debajo del cual no retransmitirán una transacción (por defecto, `0,1 sat/vB` en Bitcoin Core a través de `minRelayTxFee`). Una transacción puede ser válida en el sentido estricto de las reglas de consenso, pero no ser retransmitida por la mayoría de los nodos si sus tarifas son demasiado bajas. Como resultado, no circula, no llega a los mineros y tiene muy pocas posibilidades de ser confirmada.



Llegados a este punto, ya tienes lo esencial de la recompensa por bloque: corresponde a la compensación para el minero ganador y se compone de dos elementos distintos. Por un lado, una subvención por bloque, definida por las reglas del protocolo, que crea nuevos bitcoins ex nihilo. Y por otro, las tasas de las transacciones incluidas en el bloque minado.



En el próximo capítulo, nos centraremos con más detalle en la subvención por bloque, para entender con precisión cómo se calcula y cómo evoluciona con el tiempo según las reglas del protocolo Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



En el capítulo anterior vimos que los mineros que producen un bloque válido reciben una recompensa consistente en las comisiones de las transacciones incluidas en el bloque, más un subsidio por bloque. Sin embargo, aún no hemos explicado cómo se determina el importe de este subsidio. El mecanismo que establece y evoluciona este valor se conoce como ***halving***.



### ¿Qué es reducir a la mitad?



Halving es un evento programado en el protocolo Bitcoin que reduce a la mitad la subvención por bloque, es decir, la cantidad máxima de bitcoins nuevos que el minero ganador puede crear con cada bloque. No afecta a las tarifas de transacción: las tarifas existen de forma independiente y siguen estando determinadas por la actividad de los usuarios y la competencia por el espacio de los bloques.



Cuando se lanzó Bitcoin en 2009, la subvención por bloque se fijó en 50 BTC por cada bloque extraído. Desde entonces, esta subvención se ha reducido a la mitad en varias ocasiones.



![Image](assets/fr/029.webp)



Halving no se activa por una fecha, sino por la altura del bloque. Se ejecuta **cada 210.000 bloques**. Dado que Bitcoin tiene como objetivo un intervalo medio de unos 10 minutos por bloque, 210.000 bloques corresponden aproximadamente a cuatro años.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Así, si anotamos `n` el número de mitades ya ocurridas, la subvención en bloque en BTC puede calcularse del siguiente modo:



```text
subsidy(n) = 50 / 2^n
```



### Mitades anteriores



He aquí un cuadro recapitulativo de las reducciones que ya se han producido, con su altura en bloque, la fecha y la nueva subvención en bloque aplicable tras el suceso:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### ¿Cuándo y cómo finaliza la subvención?



Halving se repite siempre que la subvención pueda expresarse en la unidad mínima del sistema: satoshi.



```text
1 BTC = 100 000 000 sats
```



A medida que la subvención se reduce a la mitad, acabamos alcanzando fracciones de bitcoin tan pequeñas que llegan a ser inferiores a 1 satoshi. En este punto, ya no es posible crear media unidad de satoshi. La creación de dinero a través de la subvención de bloques se detiene, y los mineros son compensados únicamente sobre la base de las comisiones por transacción. A partir de este momento, todos los bitcoins estarán en circulación, y ya no será posible producir nuevas unidades.



El fin definitivo de las subvenciones a los bloques llegará en el nivel de bloque 6.930.000, es decir, en la 33ª y última reducción a la mitad. Se espera que este acontecimiento tenga lugar en torno al año 2140, aunque es imposible dar una fecha exacta, ya que dependerá de la velocidad real a la que se encuentren bloques de aquí a entonces.



Dado que la subvención por bloque sigue una secuencia geométrica con una proporción de 1/2 en cada reducción a la mitad, la creación de dinero fue extremadamente alta en los primeros días de Bitcoin, y luego disminuye muy rápidamente. En la séptima reducción a la mitad, más del 99% de los bitcoins ya se habrán puesto en circulación. Se espera que el umbral del 99% se supere entre 2032 y 2036. Esto significa que se tardará más de 100 años en extraer el último 1% de bitcoins restante. Mientras que la inflación monetaria era muy alta cuando se lanzó la Bitcoin, para permitir la distribución generalizada de la moneda, ahora es muy baja y seguirá bajando, hasta alcanzar el nivel de una verdadera moneda fuerte, cuya oferta circulante ya no puede aumentar.



![Image](assets/fr/030.webp)



### ¿Por qué nunca habrá 21 millones de BTC?



La oferta monetaria máxima de Bitcoin se presenta a menudo como 21 millones de BTC. Se trata de una buena aproximación para entender su política monetaria, pero desde un punto de vista estrictamente técnico, la oferta total nunca alcanzará exactamente los 21.000.000 de bitcoins.



La razón principal es mecánica. A través de sucesivas divisiones por la mitad, la subvención por bloque acaba cayendo por debajo del valor mínimo de 1 sat, lo que pone fin a la emisión antes de alcanzar el total teórico exacto. Como resultado de esta granularidad mínima y de las reglas de redondeo, el número total de bitcoins creados por el subsidio es ligeramente inferior a 21 millones.



Además, también pueden sumarse desviaciones marginales relacionadas con el protocolo. Por ejemplo, en raras ocasiones, algunos mineros pueden no haber reclamado la totalidad de su subvención, lo que reduce definitivamente la cantidad de bitcoins realmente emitidos. También podemos mencionar el bloque génesis, producido por Satoshi el 3 de enero de 2009, cuyos bitcoins creados no forman parte del UTXO set, así como ciertos acontecimientos históricos relacionados con bugs, como los identificadores de transacción coinbase duplicados.



Por último, también hay que tener en cuenta todos los bitcoins que han sido destruidos o bloqueados:




- bitcoins encerrados en guiones irresolubles;
- los destruidos deliberadamente por los scripts `OP_RETURN`;
- o pérdida de claves privadas a nivel de aplicación.



En teoría, la oferta de Bitcoin está limitada a 21 millones. En la práctica, sin embargo, nunca habrá 21 millones de bitcoins en circulación.



## La transacción coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



En los capítulos anteriores presentamos dos puntos importantes. En primer lugar, el minero que consigue producir y distribuir un bloque válido recibe una recompensa. Por otro lado, vimos que esta recompensa se compone de dos elementos distintos:




- una subvención por bloque (bitcoins creados ex nihilo, cuyo importe máximo lo fija el protocolo y se reduce gradualmente mediante halvings);
- todas las comisiones de transacción pagadas por los usuarios cuyas transacciones se han incluido en el bloque.



Sin embargo, queda una pregunta por responder: ¿mediante qué mecanismo cobra el minero esta recompensa en Bitcoin? Esta es precisamente la función de una transacción concreta denominada "coinbase".



### Cómo funciona la transacción coinbase



Como vimos en la primera parte del curso, cada bloque Bitcoin contiene una lista de transacciones pendientes que confirmará. La primera de ellas es siempre la transacción coinbase. Es la que permite al minero ganador recibir su recompensa.



![Image](assets/fr/031.webp)



A primera vista, parece una transacción Bitcoin clásica: tiene un TXID, salidas y está incluida en el árbol Merkle del bloque. Sin embargo, difiere en un aspecto importante: no gasta ninguna UTXO existente.



En una transacción Bitcoin clásica, las "entradas" hacen referencia a salidas anteriores no gastadas (UTXO), que proporcionan el valor de entrada. A continuación, las salidas redistribuyen este valor a nuevas UTXO, con nuevas condiciones de gasto. En otras palabras, para enviar bitcoins, ya debes poseerlos. En cambio, la transacción coinbase no consume bitcoins de entrada: crea bitcoins de salida directamente desde cero.



Es precisamente este mecanismo el que permite introducir nuevos bitcoins en circulación a través del subsidio del bloque, y abona al minero las tasas asociadas a las transacciones incluidas en el bloque. La transacción de coinbase no puede hacer referencia a una UTXO real existente (de hecho, hace referencia a una UTXO ficticia), ya que su función es precisamente crear parte del valor (el subsidio) y recuperar la otra parte (las tasas), sin recibirlas de una transacción anterior. Para que todo el sistema se mantenga coherente, la parte correspondiente a las tasas debe ser exactamente igual a la suma de bitcoins consumidos en entradas pero no recreados en salidas en las demás transacciones del bloque.



![Image](assets/fr/032.webp)



Esta transacción no es opcional. Un bloque que no contenga una transacción coinbase no es válido y será rechazado sistemáticamente por los nodos de la red.



⚠️ Atención: el término "*coinbase*" no tiene ninguna relación con la plataforma de intercambio del mismo nombre. En Bitcoin, "*coinbase*" se refiere históricamente a la transacción que crea la recompensa del bloque. La empresa simplemente ha adoptado este término para su nombre.



En realidad, la transacción coinbase cumple varias funciones simultáneamente:




- La primera es la que acabamos de detallar: asigna al minero la recompensa a la que tiene derecho por haber producido un bloque válido.
- Su segunda función, más técnica, es anclar el compromiso criptográfico a los testigos (firmas) de las transacciones SegWit incluidas en el bloque.
- Una tercera función, esta vez no directamente relacionada con el protocolo, sino vinculada a la industrialización moderna de mining, es que la coinbase se utiliza ahora con frecuencia para anclar datos técnicos arbitrarios. Estos datos suelen estar relacionados con el funcionamiento de los pools mining y su organización interna.



Para ayudarle a entender estos diferentes usos, vamos a echar un vistazo más de cerca a la estructura de la transacción coinbase.



### La estructura básica de la transacción coinbase



Una transacción coinbase debe contener exactamente una entrada. Para simplificar, a veces decimos que no tiene entrada, porque esta entrada no gasta ningún UTXO real. En realidad, hay una entrada con una fuente referenciada, pero apunta deliberadamente a una UTXO inexistente.



Como ya hemos visto, cada transacción Bitcoin debe consumir UTXOs como entrada para crear salidas válidas. En la transacción Bitcoin, este consumo adopta la forma de referenciar una UTXO existente como entrada. Esta referenciación se realiza simplemente indicando el identificador de la transacción anterior (aquella en la que se creó el UTXO), así como su índice entre las salidas de esta transacción. Concretamente, una UTXO se define mediante un hash (el TXID anterior) y un índice.



Pero en el caso de la transacción de coinbase, en lugar de hacer referencia a una UTXO real existente, la entrada debe apuntar necesariamente a esta UTXO falsa en particular, con un TXID lleno de ceros, que no se corresponde con ningún TXID real:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Directamente seguido por el falso índice:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



En el protocolo básico Bitcoin, descrito en Satoshi Nakamoto, esta entrada falsa es la única restricción impuesta a la transacción coinbase.



Como cualquier UTXO referenciada en la entrada de una transacción, está asociada a un campo `scriptSig`. En una transacción convencional, este campo `scriptSig` contiene los elementos necesarios para satisfacer la `scriptPubKey` y desbloquear así la UTXO gastada. Pero en el caso particular de coinbase, como la UTXO a la que se hace referencia es deliberadamente ficticia, el campo `scriptSig` es totalmente libre. Por lo tanto, los Miner pueden introducir los datos que quieran. Más adelante veremos cómo se utiliza esta libertad.


Además de esta entrada falsa, hay una o más salidas perfectamente estándar, que permiten al minero recoger los bitcoins de la recompensa en una de sus direcciones Bitcoin. Estas salidas son UTXO bloqueadas por una `scriptPubKey` (por ejemplo, un script que apunta a una dirección controlada por el minero o el pool). La única peculiaridad reside en la regla de cálculo de su valor: la suma total de las salidas de la coinbase nunca debe superar la subvención máxima permitida, a la que se añaden las comisiones por bloque.



Históricamente, por tanto, la transacción coinbase se reduce a este sencillo esquema: una entrada falsa que hace referencia a un UTXO inexistente, y una o más salidas diseñadas para distribuir la recompensa del bloque al minero ganador. Hoy en día, sin embargo, la coinbase ya no se limita a este papel de distribución. Su posición especial en el bloque y la gran flexibilidad de su estructura han dado lugar a nuevos usos, tanto en el propio protocolo como en los mecanismos de gestión de pools de mining.



### Otros usos de coinbase



Con el tiempo, la transacción coinbase se ha convertido en un punto de inserción especialmente conveniente para integrar una variedad de información útil para mining y para la propia estructura de bloques. Echémosles un vistazo para comprender mejor la organización general de coinbase.



#### La BIP-34



BIP-34 es un soft fork desplegado en marzo de 2013, a partir del bloque 227.930, que introdujo la versión 2 de los bloques Bitcoin. Esta nueva versión requiere que cada bloque incluya, en el `scriptSig` de la transacción coinbase, la altura del bloque que se está creando.



Por un lado, esta evolución aclara la forma en que la red acuerda evolucionar la estructura de bloques y las reglas de consenso. En segundo lugar, garantiza la unicidad de cada bloque y transacción coinbase.



Por lo tanto, el `scriptSig` de coinbase no es totalmente libre. Desde la activación de BIP-34, simplemente se limita a comenzar con la altura del bloque en el que se incluye esta transacción de coinbase.



![Image](assets/fr/035.webp)



#### El extra-nonce



Como vimos en los primeros capítulos de este curso, el minero dispone de un campo nonce de 32 bits en la cabecera del bloque, que modifica por ensayo y error para encontrar un hash menor o igual al objetivo. Este espacio de 32 bits ya permite explorar un número muy grande de combinaciones, pero cuando la dificultad mining es alta, este rango puede agotarse por completo en un tiempo relativamente corto y, por tanto, puede que no se obtenga ninguna combinación que produzca un hash válido. Si todos los valores posibles del `nonce` han sido probados sin éxito, el minero debe entonces modificar otro elemento para cambiar la cabecera del bloque y comenzar una nueva serie de intentos.



Como la transacción coinbase ofrece un campo libre a través del `scriptSig` de su entrada, la solución utilizada para ampliar el espacio del nonce es explotar parte de este `scriptSig`. Esto se conoce generalmente como el extra-nonce. Al modificar el extra-nonce, el minero modifica el `scriptSig` de la coinbase, es decir, el identificador de la transacción, luego la raíz Merkle del bloque y, por último, la propia cabecera del bloque. De este modo, obtienen un nuevo espacio de búsqueda de hashes para explorar, sin tener que modificar los demás componentes de su bloque candidato.



![Image](assets/fr/036.webp)



#### Identificación de pools y mineros



En la actualidad, una parte muy importante del hashrate mundial se organiza en pools de mining. Estas estructuras reúnen a mineros individuales para combinar su trabajo y reducir la varianza de sus ingresos.



Por razones operativas, los pools mining también explotan el campo libre de la entrada `scriptSig` de coinbase para insertar diversas piezas de información. Éstas varían de un pool a otro y de un protocolo de red a otro, pero generalmente incluyen un identificador único (a menudo un nonce extra estructurado en varias subpartes) asignado a cada minero, para evitar la duplicación de trabajo dentro del pool. Suele añadirse una etiqueta de identificación del pool, que se utiliza para la atribución pública de los bloques encontrados, las estadísticas mining y otros fines de seguimiento.



![Image](assets/fr/037.webp)



#### El compromiso de SegWit



Desde que se habilitó la SegWit soft fork en 2017, los datos de los testigos (es decir, generalmente las firmas) se han separado de los datos maestros de las transacciones, en particular para corregir el problema de maleabilidad de las transacciones Bitcoin. Esta separación introduce, por tanto, un nuevo elemento que debe consignarse en el bloque.



Para ello, los testigos se agrupan en otro árbol de Merkle dedicado, cuya raíz se consigna en la transacción coinbase a través de una salida `OP_RETURN`.



![Image](assets/fr/038.webp)



No entraré en más detalles sobre este mecanismo en este curso, ya que está fuera del alcance de este artículo, pero basta con recordar que desde la introducción de SegWit, la transacción coinbase sirve como vehículo para anclar en el bloque una huella digital que resume todos los testigos SegWit. Los testigos se colocan en un árbol Merkle independiente, la raíz de este árbol se escribe en una salida de la transacción coinbase, y esta transacción coinbase se incluye a su vez en el árbol Merkle principal junto con todas las demás transacciones, cuya raíz aparece en la cabecera del bloque. De este modo, los testigos, almacenados por separado de los datos de la transacción principal, se siguen consignando en la cabecera del bloque.



![Image](assets/fr/039.webp)



#### Mensajes arbitrarios



Dado que el `scriptSig` permite insertar libremente información arbitraria elegida por el minero, algunos han aprovechado la oportunidad para añadir mensajes de carácter más personal que técnico. El caso más famoso es, por supuesto, el de Satoshi Nakamoto, con su ya icónico mensaje:



> The Times 03/Ene/2009 El canciller, al borde del segundo rescate bancario

Este mensaje, presente en el bloque Genesis (el primer bloque de Bitcoin) está codificado en hexadecimal en el `scriptSig` de la transacción coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### El plazo de vencimiento


Una vez que el bloque ha sido minado y distribuido, la transacción coinbase aparece en la blockchain como cualquier otra transacción. Crea UTXO para el minero ganador, lo que le permite cobrar su recompensa. Sin embargo, estos UTXO no se pueden gastar inmediatamente: están sujetos a un periodo de vencimiento. Este vencimiento se fija en 100 bloques después del bloque que contiene la coinbase. En concreto, la transacción coinbase debe sumar 101 confirmaciones para que el minero ganador pueda gastar sus resultados.


![Image](assets/fr/040.webp)


El objetivo de esta regla es limitar el impacto de las reorganizaciones de la cadena en la economía. Como hemos visto en capítulos anteriores, puede ocurrir que, a la misma altura, dos bloques válidos distintos sean encontrados casi simultáneamente por mineros diferentes. Durante un breve momento, la red puede dividirse: algunos nodos reciben primero el bloque A, mientras que otros ven primero el bloque B. Luego, en el transcurso de los bloques siguientes, una de las dos ramas acumula más trabajo y se convierte en la rama de referencia. La otra rama se abandona y sus bloques quedan obsoletos. Las transacciones que contenía pueden entonces, en teoría, volver a los mempools en espera de confirmación.



En la práctica, esto rara vez ocurre, porque el mercado de comisiones suele dar lugar a que casi las mismas transacciones aparezcan en dos bloques que compiten a la misma altura. Esta es una de las razones por las que se suele considerar que una transacción Bitcoin es inmutable después de seis confirmaciones: las reorganizaciones de más de seis bloques son tan improbables que pueden considerarse razonablemente imposibles.



![Image](assets/fr/041.webp)



El problema de estas reorganizaciones en el caso de la transacción de Coinbase es que no es una transacción ordinaria. Introduce bitcoins completamente nuevos en circulación. Si la recompensa del bloque pudiera gastarse inmediatamente, podría producirse una situación problemática en cascada:




- un minero gasta bitcoins de una coinbase,
- estos bitcoins circulan en la economía,
- y finalmente se abandonó el bloque original durante una reorganización.



Los bitcoins en circulación nunca habrían existido entonces en la cadena final, y una serie de transacciones que eran válidas en el momento de su emisión pasarían a ser inválidas a posteriori.



El periodo de vencimiento impone un plazo lo suficientemente largo como para que esta hipótesis no sea realista. Una reorganización de 101 bloques se considera, en la práctica, imposible (aunque quede una probabilidad infinitesimal). No sabemos exactamente por qué Satoshi eligió un valor tan alto para la madurez, pero es probable que se eligiera para que el mecanismo siguiera siendo funcional, incluso en caso de averías importantes en la red.



Esta regla impide que el dinero de recompensa por bloque recién creado empiece a circular antes de que el bloque que generated lo haya enterrado de forma segura bajo una gran cantidad de trabajo acumulado.



---

Hemos llegado al final de nuestra explicación del funcionamiento de Bitcoin mining. Ahora debería tener una idea clara de los mecanismos básicos implicados.



En la última parte del curso, volveremos a aspectos más concretos, para mostrarte cómo se materializa Bitcoin mining en el mundo real: su industrialización, las máquinas utilizadas, la agrupación de jugadores, etc. El objetivo será darte una visión global de Bitcoin mining, tanto desde la perspectiva teórica y protocolaria que acabamos de ver, como desde su vertiente práctica y operativa.



# La industria Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## La evolución de las máquinas mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



En los inicios de Bitcoin, mining no era una actividad industrial. Formaba parte del software de Bitcoin, lanzado en un ordenador personal, a menudo por curiosidad, a veces para apoyar la red y, en segundo lugar, para obtener bitcoins que entonces no tenían prácticamente valor de mercado.



Con el paso de los años, esta actividad ha sufrido una transformación: las máquinas han cambiado, la dificultad se ha disparado y la mining se ha convertido en una industria por derecho propio. Echemos un vistazo a los aspectos operativos de Bitcoin mining.



### Primeros pasos: mining con una CPU



En 2009 y en los primeros años, mining se realizaba principalmente utilizando la CPU de un ordenador convencional. Bitcoin era entonces una simple pieza de software que hacía las veces de wallet, nodo y minero. Bastaba con ejecutar el software de Satoshi Nakamoto en el ordenador personal para participar en el proceso de mining y, en muchos casos, encontrar bloques.



Una CPU puede hacer de todo, pero no está optimizada para nada. Ejecuta instrucciones muy generales, con una lógica compleja. Para una tarea como el hashing repetitivo de cabeceras de bloque, no es la herramienta ideal, pero en el arranque de la red, la dificultad es tan baja que es más que suficiente para encontrar bloques.



Este periodo es importante, porque nos recuerda un punto importante: proof of work no depende de una categoría concreta de equipos. Lo que cuenta es la capacidad de calcular hashes más rápidamente que los demás, a un coste determinado. En cuanto aparece una ventaja técnica, se transforma automáticamente en una ventaja económica. Pero en términos absolutos, todavía es posible hoy intentar encontrar bloques Bitcoin utilizando una CPU convencional. Este es el enfoque adoptado por el proyecto NerdMiner, por ejemplo. Las posibilidades de encontrar un bloque son prácticamente nulas, pero sigue habiendo una probabilidad infinitesimal.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Cambio a la GPU



Muy pronto, los mineros se dieron cuenta de que el cuello de botella no era la potencia, sino la capacidad de realizar un gran número de operaciones similares en paralelo. Esto era exactamente lo que podían hacer las unidades de procesamiento gráfico (GPU). Originalmente, una GPU se había diseñado para realizar las mismas operaciones en grandes cantidades de datos. Esta arquitectura se adaptaba perfectamente a una tarea como el hash repetido: en lugar de tener unos pocos núcleos muy versátiles, tienes cientos, y luego miles, de unidades capaces de ejecutar las mismas instrucciones simultáneamente.



Con un consumo de energía comparable, una GPU puede producir muchos más hashes por segundo que una CPU. Al mismo tiempo, el bitcoin tenía un tipo de cambio frente al dólar, su valor aumentaba y aparecían plataformas de intercambio. A partir de entonces, la naturaleza de mining empezó a cambiar. Ya no se trataba sólo de participar, sino de ganar dinero. Aparecieron configuraciones dedicadas: máquinas construidas en torno a varias tarjetas gráficas, a veces sin pantalla, con un sistema mínimo y software especializado, cuyo único fin era minar.



Fue entonces cuando la dificultad de la mining empezó a dispararse. Entre mediados de 2010 y mediados de 2011, incluso se multiplicó por 1.000. Mecánicamente, comienza la especialización, al igual que las primeras formas de industrialización, y los usuarios ordinarios -que se contentan con ejecutar el software Bitcoin en sus ordenadores personales- tienen ahora muy pocas posibilidades de encontrar un bloque válido.



![Image](assets/fr/044.webp)



*Fuente: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Entre la era de la GPU y la moderna ASIC, hubo una fase intermedia: el uso de FPGAs. Una FPGA es un componente reprogramable: puede configurarse para implementar directamente un circuito lógico dedicado a un cálculo concreto, en este caso `SHA256d`. La idea era alejarse aún más del hardware de propósito general (CPU/GPU) para ganar en eficiencia energética. Pero pronto, las mejoras introducidas virtualmente en las FPGA se aplicarían físicamente a los propios chips: es la llegada de ASIC.



### La llegada de ASIC



La última etapa en la especialización del hardware de mining fue la aparición de los ASIC (*Circuitos Integrados para Aplicaciones Específicas*). Un ASIC es un chip diseñado para una única tarea. En el caso de Bitcoin mining, esta tarea es precisamente la ejecución de `SHA256d` a máxima velocidad y con una eficiencia energética óptima. A diferencia de una GPU, una ASIC no se utiliza para ejecutar juegos, renderizado 3D o IA. Sirve para hacer hashing, y nada más.



![Image](assets/fr/045.webp)



*ASIC S21 XP fabricado por Bitmain*



Esta especialización tiene dos consecuencias importantes:




- El primero es un salto en rendimiento y eficiencia. Para dispositivos de generación comparable, una ASIC produce un número mucho mayor de hashes por segundo que una GPU, al tiempo que consume menos energía. Mining con una GPU pronto dejó de ser competitiva: aunque funcionaba técnicamente, el coste de electricidad superaba con creces los ingresos esperados en la mayoría de los contextos;
- El segundo es un cambio de modelo: la inversión se ha desplazado principalmente hacia el hardware de calidad industrial. Mining implica ahora comprar máquinas diseñadas para este fin, alimentarlas continuamente, refrigerarlas, mantenerlas y absorber su obsolescencia. Porque una ASIC no es económicamente eterna: cuando sale al mercado una nueva generación más eficiente, las viejas máquinas se vuelven progresivamente menos rentables, aunque sigan siendo funcionales.



A partir de ahí, ya no hablamos sólo de un hobby. Hablamos de un sector en el que la competitividad depende de una ecuación:




- coste de la electricidad;
- coste del equipamiento y amortización;
- capacidad de refrigeración y funcionamiento a gran escala;
- disponibilidad y fiabilidad de las máquinas;
- velocidad de las comunicaciones;
- etc.



### Granjas Mining



Una máquina aislada puede minar, pero al agrupar cientos, luego miles de ASIC en una única ubicación, compartimos los costes fijos, optimizamos la logística y nos acercamos a un modelo de centro de datos especializado.



Una granja de mining, en su forma más simple, es un edificio (o conjunto de contenedores) lleno de ASIC funcionando 24 horas al día, 7 días a la semana. El reto ahora es mantener unas condiciones de funcionamiento estables:




- suministrar grandes cantidades de energía eléctrica estable y de bajo coste;
- gestionar el calor para evitar el estrangulamiento, ya que la densidad energética es considerable;
- filtrar el polvo, controlar la humedad, limpiar;
- supervisión en tiempo real del rendimiento de la máquina (temperaturas, errores de hardware, caídas de hashrate, etc.).



![Image](assets/fr/043.webp)



*Uno de los siete edificios dedicados a Bitcoin mining en las instalaciones de Riot Platforms en Rockdale, cerca de Austin, Texas. Éste está dedicado específicamente a la inmersión mining*



La Mining está ahora impulsada por actores industriales, algunos de ellos cotizados en bolsa, que construyen y explotan granjas a muy gran escala. Entre ellos figuran MARA Holdings (Nasdaq: `MARA`) y Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Incluso sin entrar en los detalles de los modelos de rentabilidad, es importante entender por qué mining ha adoptado esta forma. Proof-of-work es un mecanismo competitivo: la probabilidad de encontrar un bloque, y por tanto de ganar dinero, es proporcional a la cuota de hashrate que se despliegue. En consecuencia, existe una presión constante para aumentar la potencia de cálculo, reducir el coste por unidad de cálculo y limitar las pérdidas. En consecuencia, los entornos que ofrecen electricidad más barata, un clima propicio a la refrigeración o una infraestructura energética abundante se vuelven naturalmente más atractivos.



Mining Bitcoin ha pasado así de ser una actividad accesible a cualquiera en sus inicios, a estar dominada por equipos especializados y operaciones profesionales. Esto no cambia las reglas del protocolo. En teoría, cualquiera puede minar con cualquier máquina. Pero en la práctica, el nivel de dificultad y eficacia de la ASIC ha hecho que la mining doméstica deje de ser competitiva en la mayoría de los contextos.



Por supuesto, sigue habiendo situaciones en las que la mining doméstica puede ser interesante, por ejemplo si se beneficia de electricidad muy barata, o si utiliza el calor generated por su minero para calentar su casa en invierno. Pero en cualquier caso, seguirá necesitando comprar una máquina equipada con un chip ASIC. Además, como tu potencia mining seguirá siendo extremadamente pequeña en relación con la red Bitcoin, tendrás que encontrar la manera de reducir la varianza de tus ingresos: éste es precisamente el papel de los pools mining, de los que hablaremos en el próximo capítulo.



Si quieres explorar soluciones domésticas de mining con recuperación de calor, tenemos tutoriales sobre varias herramientas, tanto listas para usar como de bricolaje:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Agrupación en grupos mining


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin implica gastos permanentes e inevitables, entre los que destaca el consumo de energía de las máquinas. Estos gastos se producen independientemente de los resultados, aunque los ingresos de mining son, por su propia naturaleza, escasos y aleatorios. El descubrimiento de un bloque depende exclusivamente de la cuota de hashrate del minero, lo que hace que los ingresos sean tanto más impredecibles cuanto menor sea esa cuota. Es precisamente este problema práctico el que llevó rápidamente al uso generalizado de los pools de mining. En este último capítulo del curso MIN 101, ofrezco una introducción a los principios y el funcionamiento de los pools mining en Bitcoin.



### ¿Qué es una piscina mining?



Un pool mining es una organización (a menudo un servicio en línea) que agrega la potencia de cálculo de muchos mineros independientes, con el fin de aumentar la frecuencia con la que su grupo encuentra bloques. Cuando el pool encuentra un bloque, la recompensa del bloque se redistribuye entre los participantes de acuerdo con las reglas internas del pool (que se tratarán en el curso MIN 201, ya que son demasiado complejas para MIN 101).



A los participantes en un pool mining se les suele denominar "hashers", en lugar de "mineros", puesto que ya no realizan todo el trabajo de mining, sino que simplemente hacen hash de los datos que les transmite el pool.



Tenga cuidado de no confundir el grupo mining con la granja mining. Se trata de dos conceptos diferentes. Como vimos en el capítulo anterior, una granja es un sitio físico en el que una única entidad explota numerosas máquinas mining. Un pool, en cambio, es ante todo una agrupación virtual: miles de máquinas, a menudo dispersas geográficamente, trabajan bajo una coordinación común. Sin embargo, una granja puede, y a menudo lo hace, participar en un pool.



![Image](assets/fr/048.webp)



### Reducción de las diferencias de ingresos



Entonces, ¿por qué unirse a un pool? Sencillamente porque el resultado de la actividad de mining es probabilístico: con cada intento de hash, hay una probabilidad muy pequeña de que cumpla el objetivo de dificultad y, por tanto, produzca un bloque válido.



A muy largo plazo, tus ganancias medias deberían ser proporcionales a tu parte del hashrate global. Este principio se deriva directamente de las leyes de la probabilidad: cada cálculo de hash constituye un sorteo aleatorio independiente y, por la ley de los grandes números, la frecuencia con la que descubres bloques converge matemáticamente hacia tu fracción del hashrate total de la red. A corto y medio plazo, sin embargo, tus ganancias reales pueden ser extremadamente irregulares. Es esta discrepancia entre la media teórica y la realidad aleatoria lo que llamamos **varianza** en matemáticas.



He aquí un ejemplo sencillo para ilustrar el principio:




- La red Bitcoin produce una media de 144 bloques al día (aproximadamente un bloque cada 10 minutos);
- Si tiene el `0,0001 %` del total de hashrate, su expectativa es de `144 × 0,000001`, es decir, `0,000144` bloque/día;
- En otras palabras, debería encontrar un bloque de media cada `1 / 0,000144` días, es decir, cada 6.944 días, o unos 19 años.



Pero este valor sólo corresponde a una expectativa matemática: la distribución de los tiempos de descubrimiento sigue una ley aleatoria, por lo que es perfectamente posible, en la práctica, no descubrir nunca un solo bloque, incluso durante un periodo muy largo. Puedes tener mala suerte y no encontrar nada durante mucho tiempo, mientras pagas costes recurrentes (electricidad, mantenimiento, depreciación del equipo...).



La agrupación mining cambia la naturaleza de este problema: al combinar hashrate, la agrupación encuentra bloques con más frecuencia. Cada participante acepta entonces recibir sólo una fracción de cada bloque encontrado, pero con mucha más frecuencia. Se trata de pasar de unos ingresos muy volátiles y espaciados a otros más regulares, a costa de repartir las recompensas y pagar comisiones de servicio.



### ¿Por qué disminuye la varianza cuando se agrupan?



Cuanto mayor sea su potencia de cálculo, mayor será la frecuencia esperada de los bloques encontrados. Y lo que es más importante, cuanto mayor sea la frecuencia, más se acercarán los resultados observados a la media estadística de un periodo determinado.



En solitario, un minero a pequeña escala puede pasar años sin encontrar un solo bloque, obtener un gran pago un día y luego nada. En un pool, la misma realidad probabilística sigue aplicándose, pero se suaviza a escala colectiva: el pool encuentra bloques más a menudo, y la redistribución convierte estos eventos en pagos más regulares para cada participante. **Por tanto, el pool mining vende previsibilidad en la actividad mining**.



### Hitos históricos



Como vimos en el capítulo anterior, al principio, mining se podía hacer en solitario con un ordenador convencional, ya que la dificultad era muy baja. Pero a medida que la hashrate global explotó (GPU, y luego ASIC), la mining en solitario se convirtió en una apuesta que requería mucho tiempo para la mayoría de los participantes.



Los primeros pools se crearon precisamente en respuesta a esta nueva realidad. Braiins Pool (antes Slush Pool / Bitcoin.cz) es el primer pool de Bitcoin mining: minó su primer bloque el 16 de diciembre de 2010. El éxito de este primer pool mining fue rápido, ya que en pocos días captó casi el 3,5% del hashrate global.



![Image](assets/fr/047.webp)



Desde el punto de vista técnico, los pools se estructuraron en torno a protocolos de comunicación especializados entre el pool y los mineros (por ejemplo, Stratum, y luego Stratum V2), con el fin de orquestar eficazmente el trabajo distribuido. Profundizaremos en estos conceptos en nuestro curso de formación MIN 201.



### La situación actual



En el momento de escribir estas líneas (principios de 2026), el Bitcoin hashrate global está a un orden de magnitud de zetta-hash por segundo (= 1.000 EH/s = 1.000.000.000.000.000.000 hashes por segundo), y casi todos los bloques encontrados proceden de pools mining.



He aquí una clasificación, hasta la fecha, de los principales pools de mining y su respectiva cuota de hashrate. Es probable que esta clasificación cambie para cuando usted lea este curso. Para obtener datos actualizados, visite [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Fuente [mempool.space](https://mempool.space/graphs/mining/pools), datos de un mes, del 16 de diciembre de 2025 al 16 de enero de 2025.*



En un curso más avanzado, profundizaremos en el funcionamiento interno de los pools (acciones, protocolos de red, métodos de pago...), porque es aquí donde entran en juego los detalles que determinan tanto la rentabilidad del minero como las posibles implicaciones para Bitcoin.



---

Hemos llegado al final de MIN 101. Gracias por seguirlo hasta el final. Si quieres evaluar los conocimientos que has adquirido a lo largo del curso, te espera un examen final en la siguiente sección.



Con los conocimientos básicos que acabas de adquirir, ahora puedes seguir cursos más avanzados sobre mining en Plan ₿ Academy, ya sean teóricos, como éste, o más prácticos, ¡para que tú también puedas empezar a participar en Bitcoin mining!



# Parte final


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Opiniones y valoraciones


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusión


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>