---
name: El protocolo RGB, de la teoría a la práctica
goal: Adquirir los conocimientos necesarios para comprender y utilizar el RGB
objectives: 

  - Comprender los conceptos fundamentales del protocolo RGB
  - Dominar los principios de validación del lado del cliente y los compromisos de Bitcoin
  - Aprende a crear, gestionar y transferir contratos RGB
  - Cómo manejar un nodo Lightning compatible con RGB

---
# Descubrir el protocolo RGB

Sumérjase en el mundo de RGB, un protocolo diseñado para implementar y hacer cumplir los derechos digitales, en forma de contratos y activos, basado en las reglas de consenso y las operaciones de la blockchain de Bitcoin. Este completo curso de formación le guiará a través de los fundamentos técnicos y prácticos de RGB, desde los conceptos de "Validación del lado del cliente" y "Sellos de un solo uso", hasta la implementación de contratos inteligentes avanzados.

A través de un programa estructurado paso a paso, descubrirá los mecanismos de validación del lado del cliente, los compromisos deterministas en Bitcoin y los patrones de interacción entre usuarios. Aprenda a crear, gestionar y transferir tokens RGB en Bitcoin o la Lightning Network.

Tanto si eres un desarrollador, un entusiasta de Bitcoin, o simplemente tienes curiosidad por aprender más sobre esta tecnología, este curso de formación te proporcionará las herramientas y conocimientos que necesitas para dominar RGB y construir soluciones innovadoras sobre Bitcoin.

El curso se basa en un seminario en directo organizado por Fulgur'Ventures e impartido por tres profesores de renombre y expertos en RGB.

+++
# Introducción

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Presentación del curso

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Hola a todos, y bienvenidos a este curso de formación dedicado a RGB, un sistema de contrato inteligente validado del lado del cliente que se ejecuta en Bitcoin y la Red Lightning. La estructura de este curso está diseñada para permitir la exploración en profundidad de este complejo tema. Así es como está organizado el curso:

**Sección 1: Teoría

La primera sección está dedicada a los conceptos teóricos necesarios para entender los fundamentos de la validación del lado del cliente y RGB. Como descubrirá en este curso, RGB introduce una serie de conceptos técnicos que no suelen verse en Bitcoin. En esta sección también encontrará un glosario con definiciones de todos los términos específicos del protocolo RGB.

**Sección 2: Práctica

La segunda sección se centrará en la aplicación de los conceptos teóricos vistos en la sección 1. Aprenderemos a crear y manipular contratos RGB. También veremos cómo programar con estas herramientas. Estas dos primeras secciones están presentadas por Maxim Orlovsky.

**Sección 3: Aplicaciones

La sección final corre a cargo de otros ponentes que presentan aplicaciones concretas basadas en RGB, para poner de relieve casos de uso de la vida real.

---
Este curso de formación surgió originalmente de un bootcamp de desarrollo avanzado de dos semanas en Viareggio, Toscana, organizado por [Fulgur'Ventures](https://fulgur.ventures/). La primera semana, centrada en Rust y SDKs, se puede encontrar en este otro curso:

https://planb.network/courses/lnp402
En este curso, nos centraremos en la segunda semana del bootcamp, que se centra en RGB.

**Semana 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Semana 2 - Formación actual CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Muchas gracias a los organizadores de estos cursos en directo y a los 3 profesores que participaron:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, IA, robótica, transhumanismo. Creador de RGB, Prime, Radiant y lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo *Desarrollador, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Aporto mi granito de arena para convertir el mundo en una distopía cypherpunk. Actualmente trabajo en RGB en Bitfinex*.

La versión escrita de este curso de formación se redactó utilizando 2 recursos principales:


- Vídeos del seminario de Maxim Orlovsky, Hunter Trujilo y Frederico Tenga en Lightning Bootcamp ;
- La documentación RGB, cuya producción fue patrocinada por [Bitfinex](https://www.bitfinex.com/).

# RGB en teoría

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introducción a los conceptos de informática distribuida

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB es un protocolo diseñado para aplicar y hacer cumplir derechos digitales (en forma de contratos y activos) de forma escalable y confidencial, basado en las reglas de consenso y las operaciones de la blockchain de Bitcoin. El objetivo de este primer capítulo es presentar los conceptos básicos y la terminología en torno al protocolo RGB, destacando en particular sus estrechos vínculos con conceptos básicos de computación distribuida como la Validación del lado del cliente y los Sellos de un solo uso.

En este capítulo, exploramos los fundamentos de los **sistemas de consenso distribuido** y vemos cómo RGB encaja en esta familia de tecnologías. También introduciremos los principios fundamentales que nos ayudan a entender por qué RGB pretende ser extensible e independiente del propio mecanismo de consenso de Bitcoin, mientras se apoya en él cuando es necesario.

### Introducción

La informática distribuida, una rama específica de la informática, estudia los protocolos utilizados para hacer circular y procesar información en una red de nodos. En conjunto, estos nodos y las reglas del protocolo constituyen lo que se conoce como un sistema distribuido. Entre las propiedades esenciales que caracterizan a un sistema de este tipo se encuentran :


- La **capacidad de verificación y validación independientes** de determinados datos por cada nodo;
- Posibilidad de que los nodos construyan (según el protocolo) una vista completa o parcial de la información. Estas vistas son los **estados** del sistema distribuido;
- El **orden cronológico** de las operaciones, para que los datos lleven un sello de tiempo fiable y haya consenso sobre la secuencia de acontecimientos (secuencia de estados).

En particular, la noción de **consenso** en un sistema distribuido abarca dos aspectos:


- Reconocimiento de la validez** de los cambios de estado (según las normas del protocolo);
- El **acuerdo sobre el orden** de estos cambios de estado, que hace imposible reescribir o invertir a posteriori las operaciones validadas (esto también se conoce en Bitcoin como "protección contra el doble gasto").

La primera implementación funcional y sin permisos de un mecanismo de consenso distribuido fue introducida por Satoshi Nakamoto con Bitcoin, gracias al uso combinado de una estructura de datos blockchain y un algoritmo Proof-of-Work (PoW). En este sistema, la credibilidad del historial de bloques depende de la potencia de cálculo que le dediquen los nodos (mineros). Bitcoin es, por tanto, un ejemplo importante e histórico de sistema de consenso distribuido abierto a todos (*sin permisos*).

En el mundo del blockchain y la computación distribuida, podemos distinguir dos paradigmas fundamentales: ***blockchain*** en el sentido tradicional, y ***canales de estado***, cuyo mejor ejemplo en producción es la Lightning Network. El blockchain se define como un registro de eventos ordenados cronológicamente, replicados por consenso dentro de una red abierta y libre de permisos. Los canales de estado, por su parte, son canales entre pares que permiten a dos (o más) participantes mantener un estado actualizado fuera de la cadena, utilizando la blockchain sólo al abrir y cerrar estos canales.

En el contexto de Bitcoin, sin duda está familiarizado con los principios de minería, descentralización y finalidad de las transacciones en la blockchain, así como con el funcionamiento de los canales de pago. Con RGB, estamos introduciendo un nuevo paradigma llamado **Validación del lado del cliente**, que, a diferencia de blockchain o Lightning, consiste en almacenar y validar localmente (del lado del cliente) las transiciones de estado de un contrato inteligente. Esto también difiere de otras técnicas "DeFi" (_rollups_, _plasma_, _ARK_, etc.), en que Client-side Validation se basa en la blockchain para evitar el doble gasto y disponer de un sistema de sellado de tiempo, manteniendo el registro de estados y transiciones fuera de la cadena, sólo con los participantes afectados.

![RGB-Bitcoin](assets/fr/003.webp)

Más adelante, también introduciremos un término importante: la noción de "**stash**", que se refiere al conjunto de datos del lado del cliente necesarios para preservar el estado de un contrato, ya que estos datos no se replican globalmente en toda la red. Por último, veremos los fundamentos de RGB, un protocolo que aprovecha la validación del lado del cliente, y por qué complementa los enfoques existentes (blockchain y canales de estado).

### Trilemas de la informática distribuida

Para entender cómo Client-side Validation y RGB abordan problemas no resueltos por blockchain y Lightning, descubramos 3 grandes "trilemas" de la computación distribuida:


- Escalabilidad, descentralización, privacidad** ;
- Teorema CAP** (coherencia, disponibilidad y tolerancia a la partición) ;
- Trilema CIA** (Confidencialidad, Integridad, Disponibilidad).

#### 1. Escalabilidad, descentralización y confidencialidad


- Blockchain (Bitcoin)**

Blockchain está muy descentralizada, pero no es muy escalable. Además, como todo está en un registro público global, la confidencialidad es limitada. Podemos intentar mejorar la confidencialidad con tecnologías de conocimiento cero (transacciones confidenciales, esquemas mimblewimble, etc.), pero la cadena pública no puede ocultar el gráfico de transacciones.


- Rayo/Canales estatales**

Los canales estatales (como Lightning Network) son más escalables y más privados que blockchain, ya que las transacciones tienen lugar fuera de la cadena. Sin embargo, la obligación de anunciar públicamente ciertos elementos (transacciones de financiación, topología de la red) y la supervisión del tráfico de la red pueden comprometer en parte la confidencialidad. La descentralización también se resiente: el enrutamiento requiere mucho dinero y los principales nodos pueden convertirse en puntos de centralización. Este es precisamente el fenómeno que empezamos a ver en Lightning.


- Validación en el lado del cliente (RGB)**

Este nuevo paradigma es aún más escalable y más confidencial, porque no sólo podemos integrar técnicas de prueba de conocimiento de divulgación cero, sino que no existe un grafo global de transacciones, ya que nadie posee todo el registro. Por otro lado, también implica un cierto compromiso sobre la descentralización: el emisor de un contrato inteligente puede tener un papel central (como un "desplegador de contratos" en Ethereum). Sin embargo, a diferencia de blockchain, con Client-side Validation sólo se almacenan y validan los contratos que interesan, lo que mejora la escalabilidad al evitar la necesidad de descargar y verificar todos los estados existentes.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Teorema CAP (Consistencia, Disponibilidad, Tolerancia a la partición)

El teorema CAP subraya que es imposible que un sistema distribuido satisfaga simultáneamente la consistencia (*Consistencia*), la disponibilidad (*Disponibilidad*) y la tolerancia a la partición (*Tolerancia a la partición*).


- Cadena de bloques**

La cadena de bloques favorece la coherencia y la disponibilidad, pero no se lleva bien con la partición de la red: si no puedes ver un bloque, no puedes actuar y tener la misma visión que toda la red.


- Rayo** (en francés)

Un sistema de canales de estado tiene disponibilidad y tolerancia a la partición (ya que dos nodos pueden permanecer conectados entre sí aunque la red se fragmente), pero la coherencia global depende de la apertura y cierre de canales en la blockchain.


- Validación en el lado del cliente (RGB)**

Un sistema como el RGB ofrece coherencia (cada participante valida sus datos localmente, sin ambigüedades) y tolerancia a la partición (mantiene sus datos de forma autónoma), pero no garantiza la disponibilidad global (todo el mundo tiene que asegurarse de que dispone de las piezas pertinentes del historial, y algunos participantes pueden no publicar nada o dejar de compartir cierta información).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilema CIA (Confidencialidad, Integridad, Disponibilidad)

Este trilema nos recuerda que la confidencialidad, la integridad y la disponibilidad no pueden optimizarse al mismo tiempo. Blockchain, Lightning y Client-side Validation entran de forma diferente en este equilibrio. La idea es que ningún sistema puede ofrecerlo todo por sí solo; es necesario combinar varios enfoques (el sellado de tiempo de blockchain, el enfoque síncrono de Lightning y la validación local con RGB) para obtener un paquete coherente que ofrezca buenas garantías en cada dimensión.

![RGB-Bitcoin](assets/fr/006.webp)

### El papel de la cadena de bloques y la noción de fragmentación

El blockchain (en este caso, Bitcoin) sirve principalmente como mecanismo de _estampado de tiempo_ y protección contra el doble gasto. En lugar de insertar los datos completos de un contrato inteligente o sistema descentralizado, simplemente incluimos **compromisos criptográficos** (_commitments_) a las transacciones (en el sentido de Validación del Lado del Cliente, que llamaremos "transiciones de estado"). Así :


- Liberamos la blockchain de una gran cantidad de datos y lógica;
- Cada usuario almacena sólo el historial necesario para su propia parte del contrato (su "*shard*"), en lugar de replicar el estado global.

Sharding es un concepto que tiene su origen en las bases de datos distribuidas (por ejemplo, MySQL para redes sociales como Facebook o Twitter). Para resolver el problema del volumen de datos y las latencias de sincronización, la base de datos se segmenta en _shards_ (EE.UU., Europa, Asia, etc.). Cada segmento es consistente localmente y sólo se sincroniza parcialmente con los demás.

Para los contratos inteligentes de tipo RGB, fragmentamos en función de los propios contratos. Cada contrato es un _shard_ independiente. Por ejemplo, si sólo tienes tokens USDT, no tienes que almacenar o validar todo el historial de otro token como USDC. En Bitcoin, el blockchain no hace _sharding_: tienes un conjunto global de UTXOs. Con la validación del lado del cliente, cada participante conserva sólo los datos del contrato que posee o utiliza.

Por tanto, podemos imaginar el ecosistema de la siguiente manera:


- El blockchain (Bitcoin)** como base que garantiza la replicación completa de un registro mínimo y sirve como capa de sellado de tiempo;
- La Lightning Network** para transacciones rápidas y confidenciales, que sigue basándose en la seguridad y la liquidación final de la blockchain de Bitcoin;
- RGB y Client-side Validation** para añadir una lógica de contrato inteligente más compleja, sin saturar la blockchain ni perder confidencialidad.

![RGB-Bitcoin](assets/fr/007.webp)

Estos tres elementos forman un conjunto triangular, en lugar de una pila lineal de "capa 2", "capa 3" y así sucesivamente. Lightning puede conectarse directamente a Bitcoin, o asociarse a transacciones de Bitcoin que incorporen datos RGB. Del mismo modo, un uso "BiFi" (finanzas en Bitcoin) puede componerse con la blockchain, con Lightning y con RGB según las necesidades de confidencialidad, escalabilidad o lógica contractual.

![RGB-Bitcoin](assets/fr/008.webp)

### Noción de transiciones de estado

En cualquier sistema distribuido, el objetivo del mecanismo de validación es poder **determinar la validez y el orden cronológico de los cambios de estado**. Se trata de verificar que se han respetado las reglas del protocolo, y demostrar que estos cambios de estado se suceden en un orden definitivo e inatacable.

Para entender cómo funciona esta validación en el contexto de **Bitcoin** y, más en general, para comprender la filosofía que hay detrás de la Validación del Lado del Cliente, echemos primero un vistazo a los mecanismos de la blockchain de Bitcoin, antes de ver en qué se diferencia de ellos la Validación del Lado del Cliente y qué optimizaciones posibilita.

![RGB-Bitcoin](assets/fr/009.webp)

En el caso de la cadena de bloques de Bitcoin, la validación de las transacciones se basa en una regla sencilla:


- Todos los nodos de la red descargan cada bloque y transacción;
- Validan estas transacciones para verificar la correcta evolución del conjunto UTXO (todas las salidas no gastadas);
- Almacenan estos datos (en forma de bloques) para poder reproducir el historial en caso necesario.

![RGB-Bitcoin](assets/fr/010.webp)

Sin embargo, este modelo presenta dos grandes inconvenientes:


- Escalabilidad**: dado que cada nodo debe procesar, verificar y archivar las transacciones de todos, existe un límite obvio a la capacidad de transacción, vinculado en particular al tamaño máximo de los bloques (1 MB de media en 10 minutos para Bitcoin, excluyendo las cookies);
- Privacidad**: todo se difunde y almacena públicamente (importes, direcciones de destino, etc.), lo que limita la confidencialidad de los intercambios.

![RGB-Bitcoin](assets/fr/012.webp)

En la práctica, este modelo funciona para Bitcoin como capa base (Capa 1), pero puede resultar insuficiente para usos más complejos que requieran simultáneamente un alto rendimiento de las transacciones y un cierto grado de confidencialidad.

La validación del lado del cliente se basa en la idea contraria: en lugar de exigir a toda la red que valide y almacene todas las transacciones, cada participante (cliente) validará sólo la parte del historial que le concierna:


- Cuando una persona recibe un activo (o cualquier otra propiedad digital), sólo necesita conocer y verificar la cadena de operaciones (transiciones de estado) que conducen a ese activo y probar su legitimidad;
- Esta secuencia de operaciones, desde la ***Génesis*** (emisión inicial) hasta la transacción más reciente, forma un grafo dirigido acíclico (DAG) o shard, es decir, una fracción del historial global.

![RGB-Bitcoin](assets/fr/013.webp)

Al mismo tiempo, para que el resto de la red (o más concretamente, la capa subyacente, como Bitcoin) pueda bloquear el estado final sin ver los detalles de estos datos, la Validación del Lado del Cliente se basa en la noción de ***compromiso***.

Un *compromiso* es un compromiso criptográfico, típicamente un _hash_ (SHA-256 por ejemplo) insertado en una transacción Bitcoin, que prueba que se han incluido datos privados, sin revelar estos datos.

Gracias a estos _compromisos_, podemos demostrar:


- La existencia de información (ya que se compromete a un hash) ;
- La anterioridad de esta información (porque está anclada y sellada en el tiempo en la cadena de bloques, con una fecha y un orden de bloques).

El contenido exacto, sin embargo, no se revela, preservando así su confidencialidad.

En concreto, así es como funciona una transición de estado RGB:


- Se prepara una nueva transición de estado (por ejemplo, la transferencia de una ficha RGB);
- Usted genera un compromiso criptográfico para esta transición y lo inserta en una transacción Bitcoin (estos compromisos se denominan "*anclajes*" en el protocolo RGB);
- La contraparte (el receptor) recupera el historial del lado del cliente asociado a este activo y valida la coherencia de extremo a extremo, desde la génesis del contrato inteligente hasta la transición que le transmites.

![RGB-Bitcoin](assets/fr/014.webp)

La validación en el lado del cliente ofrece dos grandes ventajas:


- Escalabilidad:**

Los compromisos (*commitments*) incluidos en la cadena de bloques son pequeños (del orden de unas pocas docenas de bytes). Esto garantiza que no se sature el espacio del bloque, ya que sólo es necesario incluir el hash. También permite que el protocolo fuera de la cadena evolucione, ya que cada usuario sólo tiene que almacenar su fragmento de historia (su _stash_).


- Privacidad :**

Las transacciones en sí (es decir, su contenido detallado) no se publican en la cadena. Sólo se publican sus huellas dactilares (*hash*). Así, los importes, las direcciones y la lógica de los contratos siguen siendo privados, y el receptor puede verificar, localmente, la validez de su fragmento inspeccionando todas las transiciones anteriores. No hay ninguna razón para que el receptor haga públicos estos datos, excepto en caso de disputa o cuando se requiera una prueba.

En un sistema como RGB, múltiples transiciones de estado de diferentes contratos (o diferentes activos) pueden agregarse en una única transacción Bitcoin a través de un único _commitment_. Este mecanismo establece un vínculo determinista y con fecha y hora entre la transacción en la cadena y los datos fuera de la cadena (las transiciones validadas del lado del cliente), y permite registrar simultáneamente múltiples fragmentos en un único punto de anclaje, reduciendo aún más el coste y la huella en la cadena.

En la práctica, cuando esta transacción de Bitcoin se valida, "bloquea" permanentemente el estado de los contratos subyacentes, ya que resulta imposible modificar el hash ya inscrito en la blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### El concepto de alijo

Un **stash** es el conjunto de datos del lado del cliente que un participante debe conservar absolutamente para mantener la integridad y el historial de un contrato inteligente RGB. A diferencia de un canal Lightning, donde ciertos estados pueden reconstruirse localmente a partir de información compartida, el stash de un contrato RGB no se replica en ningún otro lugar: si lo pierdes, nadie podrá devolvértelo, ya que eres responsable de tu parte del historial. Por eso es necesario adoptar un sistema con procedimientos de copia de seguridad fiables en RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Sello de un solo uso: origen y funcionamiento

A la hora de aceptar un activo como una divisa, son esenciales dos garantías:


- La autenticidad del artículo recibido;
- La unicidad del artículo recibido, para evitar dobles gastos.

En el caso de los activos físicos, como un billete de banco, la presencia física basta para demostrar que no ha sido duplicado. Sin embargo, en el mundo digital, donde los activos son puramente informativos, esta verificación es más compleja, ya que la información puede multiplicarse y duplicarse fácilmente.

Como hemos visto antes, la revelación por parte del emisor del historial de transiciones de estado nos permite garantizar la autenticidad de un token RGB. Al tener acceso a todas las transacciones desde la transacción de génesis, podemos confirmar la autenticidad del token. Este principio es similar al de Bitcoin, donde la historia de las monedas puede rastrearse hasta la transacción original en Coinbase para verificar su validez. Sin embargo, a diferencia de Bitcoin, este historial de transiciones de estado en RGB es privado y se mantiene en el lado del cliente.

Para evitar el doble uso de las fichas RGB, utilizamos un mecanismo denominado "**Sello de un solo uso**". Este sistema garantiza que cada ficha, una vez utilizada, no pueda reutilizarse fraudulentamente una segunda vez.

Los sellos de un solo uso son primitivas criptográficas, propuestas en 2016 por Peter Todd, afines al concepto de los sellos físicos: una vez que se ha colocado un sello en un contenedor, resulta imposible abrirlo o modificarlo sin romper irreversiblemente el sello.

![RGB-Bitcoin](assets/fr/018.webp)

Este enfoque, trasladado al mundo digital, permite demostrar que una secuencia de acontecimientos ha tenido lugar efectivamente, y que ya no puede alterarse a posteriori. Los sellos de un solo uso van así más allá de la simple lógica de `hash + timestamp`, añadiendo la noción de un sello que puede cerrarse **sólo una vez**.

![RGB-Bitcoin](assets/fr/017.webp)

Para que los sellos de un solo uso funcionen, se necesita un medio de prueba de publicación capaz de demostrar la existencia o ausencia de una publicación, y difícil (si no imposible) de falsificar una vez que la información se ha difundido. Una **blockchain** (como Bitcoin) puede desempeñar este papel, al igual que un periódico en papel de tirada pública, por ejemplo. La idea es la siguiente:


- Queremos probar que un cierto compromiso sobre un mensaje `h(m)` ha sido publicado a una audiencia sin revelar el contenido del mensaje `m` ;
- Queremos demostrar que no se ha publicado ningún otro compromiso de mensaje `h(m')` competidor en lugar de `h(m)` ;
- También queremos poder comprobar que el mensaje `m` existe antes de una fecha determinada.

Una cadena de bloques se presta idealmente a esta función: en cuanto una transacción se incluye en un bloque, toda la red tiene la misma prueba infalsificable de su existencia y contenido (al menos en parte, ya que el _compromiso_ puede ocultar los detalles al tiempo que prueba la autenticidad del mensaje).

Por tanto, un Sello de un solo uso puede considerarse una promesa formal de publicar un mensaje (aún desconocido en esta fase) una vez y sólo una vez, de forma que pueda ser verificado por todas las partes interesadas.

A diferencia de los simples _compromisos_ (hash) o sellos de tiempo, que dan fe de una fecha de existencia, un Sello de un solo uso ofrece la garantía adicional de que **no puede coexistir ningún compromiso alternativo**: no se puede cerrar dos veces el mismo sello, ni intentar sustituir el mensaje sellado.

La siguiente comparación ayuda a comprender este principio:


- Compromiso criptográfico (hash)**: Con una función hash, puedes comprometerte con un dato (un número) publicando su hash. Los datos permanecen secretos hasta que revelas la preimagen, pero puedes demostrar que los conocías de antemano;
- Sello de tiempo (blockchain)**: Al insertar este hash en la blockchain, también demostramos que lo conocimos en un momento preciso (el de la inclusión en un bloque);
- Precinto de un solo uso**: Con los sellos de un solo uso, vamos un paso más allá haciendo que el compromiso sea único. Con un único hash, se pueden crear varios compromisos contradictorios en paralelo (el problema del médico que anuncia "*Es un niño*" a la familia y "*Es una niña*" en su diario personal). El sello de un solo uso elimina esta posibilidad conectando el compromiso a un medio de prueba de publicación, como la blockchain de Bitcoin, de modo que un gasto de UTXO sella definitivamente el compromiso. Una vez gastado, el mismo UTXO no puede volver a gastarse para sustituir el compromiso.

| Sellos de un solo uso Marcas de tiempo Compromiso simple (digest/hash) Sellos de un solo uso

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| La publicación del compromiso no revela el mensaje | Sí | Sí | Sí | Sí

| Prueba de la fecha del compromiso / existencia del mensaje antes de una fecha determinada | Imposible | Posible | Posible | Posible

| Prueba de que no puede existir otro compromiso alternativo | Imposible | Posible |

Los precintos de un solo uso funcionan en tres etapas principales:

**Sello Definición :**


- Alice define de antemano las reglas de publicación del sello (cuándo, dónde y cómo se publicará el mensaje);
- Bob acepta o reconoce estas condiciones.

![RGB-Bitcoin](assets/fr/021.webp)

**Sello de cierre :**


- En tiempo de ejecución, Alice cierra el sello publicando el mensaje real (normalmente en forma de _commitment_, por ejemplo un hash);
- También proporciona un **testigo** (prueba criptográfica) que demuestra que el sello está cerrado y es irrevocable.

![RGB-Bitcoin](assets/fr/019.webp)

**Verificación del sello :**


- Una vez cerrado el precinto, Bob ya no puede abrirlo: sólo puede comprobar que se ha cerrado;
- Bob recoge el sello, el **testigo** y el mensaje (o su compromiso) para asegurarse de que todo coincide y de que no hay sellos competidores o versiones diferentes.

El proceso puede resumirse del siguiente modo:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Sin embargo, la validación del lado del cliente va un paso más allá: si la definición de un sello en sí queda fuera de la cadena de bloques, es posible (en teoría) que alguien cuestione la existencia o legitimidad del sello en cuestión. Para superar este problema, se utiliza una cadena de sellos de un solo uso entrelazados:


- Cada sello cerrado contiene la definición del sello siguiente;
- Registramos estos cierres (con sus _compromisos_) dentro del blockchain (en una transacción Bitcoin);
- Por tanto, cualquier intento de modificar un sello anterior contradiría la historia incorporada a Bitcoin.

Esto es precisamente lo que hace el sistema RGB:


- Los mensajes publicados son _compromisos_ con datos validados del lado del cliente;
- La definición del sello está asociada a un Bitcoin UTXO ;
- El precinto se cierra cuando se gasta este UTXO o cuando se acredita una nueva salida al mismo compromiso;
- La cadena de transacciones que gasta estos UTXOs corresponde a la prueba de publicación: cada transición o cambio de estado en RGB queda así anclado en Bitcoin.

Resumiendo:


- La _definición de sellado_ es la UTXO que pretende sellar un compromiso futuro;
- El _cierre del sello_ se produce al gastar este UTXO, creando una transacción que contiene el compromiso;
- El _testigo_ es la propia transacción, que prueba que has cerrado el sello con este contenido;
- No se puede demostrar que un precinto no se haya cerrado (no se puede estar absolutamente seguro de que un UTXO no se haya gastado ya o no se vaya a gastar en un bloque que aún no se ha visto), pero sí se puede demostrar que efectivamente se ha cerrado.

Esta unicidad es importante para la Validación del Lado del Cliente: cuando se valida una transición de estado, se comprueba que corresponde a un UTXO único, no gastado previamente en un compromiso competidor. Esto es lo que garantiza la ausencia de gasto doble en los contratos inteligentes fuera de la cadena.

### Múltiples compromisos y raíces

Un contrato inteligente RGB puede necesitar gastar varios Sellos de un solo uso (varios UTXOs) simultáneamente. Es más, una única transacción Bitcoin puede hacer referencia a varios contratos distintos, cada uno sellando su propia transición de estado. Esto requiere un mecanismo de **compromiso múltiple** para probar, de forma determinista y única, que ninguno de los compromisos existe por duplicado. Aquí es donde la noción de **anclaje** entra en juego en RGB: una estructura especial que vincula una transacción Bitcoin y uno o más compromisos del lado del cliente (transiciones de estado), cada uno potencialmente perteneciente a un contrato diferente. Veremos este concepto con más detalle en el próximo capítulo.

![RGB-Bitcoin](assets/fr/023.webp)

Dos de los principales repositorios GitHub del proyecto (bajo la organización LNPBP) agrupan las implementaciones básicas de estos conceptos estudiados en el primer capítulo:


- validación_del_lado_del_cliente** : Contiene primitivas Rust para la validación local ;
- precintos_de_un_uso**: Implementa la lógica para definir y cerrar estos precintos de forma segura.

![RGB-Bitcoin](assets/fr/020.webp)

Tenga en cuenta que estos ladrillos de software son agnósticos de Bitcoin; en teoría, podrían aplicarse a cualquier otro medio de prueba de publicación (otro registro, una revista, etc.). En la práctica, RGB confía en Bitcoin por su solidez y amplio consenso.

![RGB-Bitcoin](assets/fr/021.webp)

### Preguntas del público

#### Hacia un uso más generalizado de los precintos de un solo uso

Peter Todd también creó el protocolo _Open Timestamps_, y el concepto de sello de un solo uso es una extensión natural de estas ideas. Más allá del RGB, se pueden prever otros casos de uso, como la construcción de _sidechains_ sin recurrir a la _merge mining_ o propuestas relacionadas con el drivechain como BIP300. Cualquier sistema que requiera un único compromiso puede, en principio, explotar esta primitiva criptográfica. En la actualidad, RGB es la primera gran aplicación a gran escala.

#### Problemas de disponibilidad de datos

Dado que en la validación del lado del cliente cada usuario almacena su propia parte del historial, la disponibilidad de los datos no está garantizada globalmente. Si un emisor de contratos retiene o revoca cierta información, es posible que desconozca la evolución real de la oferta. En algunos casos (como las stablecoins), se espera que el emisor mantenga datos públicos para demostrar el volumen en circulación, pero no existe ninguna obligación técnica de hacerlo. Por tanto, es posible diseñar contratos deliberadamente opacos con una oferta ilimitada, lo que plantea cuestiones de confianza.

#### Fragmentación y aislamiento de contratos

Cada contrato representa un "fragmento" aislado: USDT y USDC, por ejemplo, no tienen por qué compartir sus historiales. Los intercambios atómicos siguen siendo posibles, pero no implican la fusión de sus registros. Todo se hace por compromiso criptográfico, sin revelar todo el gráfico del historial a cada participante.

### Conclusión

Hemos visto dónde encaja el concepto de Validación del Lado del Cliente con blockchain y _canales de estado_, cómo responde a los trilemas de la computación distribuida, y cómo aprovecha el blockchain de Bitcoin de forma única para evitar el doble gasto y para el *estampado de tiempo*. La idea se basa en la noción de **Sello de un solo uso**, que permite crear compromisos únicos que no se pueden volver a gastar a voluntad. De este modo, cada participante carga sólo el historial estrictamente necesario, aumentando la escalabilidad y confidencialidad de los contratos inteligentes y conservando la seguridad de Bitcoin como telón de fondo.

El siguiente paso será explicar con más detalle cómo se aplica este mecanismo de sello de un solo uso en Bitcoin (a través de UTXOs), cómo se crean y validan los anclajes y, a continuación, cómo se construyen contratos inteligentes completos en RGB. En particular, veremos el tema de los compromisos múltiples, el desafío técnico de probar que una transacción Bitcoin sella simultáneamente múltiples transiciones de estado en diferentes contratos, sin introducir vulnerabilidades o compromisos dobles.

Antes de sumergirse en los detalles más técnicos del segundo capítulo, no dude en releer las definiciones clave (Validación del lado del cliente, Sello de un solo uso, anclas, etc.) y tenga en cuenta la lógica general: estamos tratando de conciliar los puntos fuertes de la cadena de bloques de Bitcoin (seguridad, descentralización, sellado de tiempo) con los de las soluciones fuera de la cadena (velocidad, confidencialidad, escalabilidad), y esto es precisamente lo que RGB y la Validación del lado del cliente están tratando de lograr.

## El nivel de compromiso

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

En este capítulo, veremos la implementación de la Validación del Lado del Cliente y los Sellos de un solo uso dentro de la blockchain de Bitcoin. Presentaremos los principios fundamentales de la **capa de compromiso** (capa 1) de RGB, con especial atención al esquema **TxO2**, que RGB utiliza para definir y cerrar un sello en una transacción Bitcoin. A continuación, discutiremos dos puntos importantes que aún no han sido tratados en detalle:


- Los _compromisos deterministas de Bitcoin_;
- Compromisos multiprotocolo.

Es la combinación de estos conceptos lo que nos permite superponer varios sistemas o contratos sobre un único UTXO y, por tanto, una única blockchain.

Cabe recordar que las operaciones criptográficas descritas pueden aplicarse, en términos absolutos, a otras blockchains o soportes de publicación, pero las características de Bitcoin (en términos de descentralización, resistencia a la censura y apertura a todos) lo convierten en la base ideal para desarrollar una programabilidad avanzada como la que requiere **RGB**.

### Esquemas de compromiso en Bitcoin y su uso por RGB

Como vimos en el primer capítulo del curso, los sellos de un solo uso son un concepto general: hacemos la promesa de incluir un compromiso (_commitment_) en una ubicación específica de una transacción, y esta ubicación actúa como un sello que cerramos en un mensaje. Sin embargo, en la blockchain de Bitcoin, hay varias opciones para elegir dónde colocar este _compromiso_.

Para entender la lógica, recordemos el principio básico: para cerrar un _sello de un solo uso_, gastamos el área sellada insertando el _compromiso_ en un mensaje dado. En Bitcoin, esto puede hacerse de varias maneras:


- Utilizar una clave pública o una dirección**

Podemos decidir que una determinada clave pública o dirección es el _sello de uso único_. En cuanto esta clave o dirección aparece en la cadena en una transacción, significa que el sello se cierra con un mensaje determinado.


- Utilizar una salida de transacción Bitcoin

Esto significa que un _precinto de un solo uso_ se define como un _punto de salida_ preciso (un par TXID + número de salida). En cuanto se gasta este _outpoint_, el precinto se cierra.

Mientras trabajábamos en RGB, identificamos al menos 4 formas diferentes de implementar estos sellos en Bitcoin:


- Defina el sello mediante una clave pública y ciérrelo en una _salida_ ;
- Define el sello con un _punto de salida_ y ciérralo con un _punto de salida_ ;
- Defina el sello mediante el valor de una clave pública y ciérrelo en un _input_ ;
- Defina el sello mediante un _punto de salida_, y ciérrelo en un _punto de entrada_.

| Definición del precinto | Cierre del precinto | Requisitos adicionales | Aplicación principal | Posibles esquemas de compromiso

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2(W)PKH | Ninguno por el momento | Keytweak, taptweak, opret |

| TxO2 | Salida de transacciones | Requiere compromisos deterministas en Bitcoin | RGBv1 (universal) | Keytweak, tapret, opret |

| PkI | Valor de clave pública | Entrada de transacciones | Taproot only & not compatible with Legacy wallets | Identidades basadas en Bitcoin | Sigtweak, witweak |

| TxO1 | Salida de transacciones | Entrada de transacciones | Sólo Taproot & no compatible con billeteras Legacy | Ninguna por el momento | Sigtweak, witweak |

No entraremos en detalle en cada una de estas configuraciones, ya que en RGB hemos optado por utilizar **un _outpoint_ como definición del sello**, y situar el _commitment_ en la salida de la transacción gastando este _outpoint_. Por lo tanto, podemos introducir los siguientes conceptos para la secuela:


- "Definición del sello "** : Un _punto de salida_ dado (identificado por TXID + nº de salida) ;
- "Cierre del sello "**: La transacción que gasta este _outpoint_, en la que se añade un _commitment_ a un mensaje.

Este esquema se ha seleccionado por su compatibilidad con la arquitectura RGB, pero otras configuraciones podrían ser útiles para diferentes usos.

El "O2" en "TxO2" nos recuerda que tanto la definición como el cierre se basan en el gasto (o creación) de una salida de transacción.

### Ejemplo de diagrama TxO2

Como recordatorio, definir un _sello de un solo uso_ no requiere necesariamente publicar una transacción en la cadena. Basta con que Alice, por ejemplo, tenga ya un UTXO sin gastar. Ella puede decidir: "Este _punto de salida_ (ya existente) es ahora mi sello". Lo anota localmente (_del lado del cliente_), y hasta que este UTXO se gaste, el sello se considera abierto.

![RGB-Bitcoin](assets/fr/024.webp)

El día que quiere cerrar el sello (para señalar un evento, o para anclar un mensaje en particular), gasta este UTXO en una nueva transacción (esta transacción suele llamarse "transacción de testigo_" (no tiene relación con _segwit_, es sólo el término que le damos). Esta nueva transacción contendrá el _compromiso_ con el mensaje.

![RGB-Bitcoin](assets/fr/025.webp)

Tenga en cuenta que en este ejemplo :


- Nadie más que Bob (o las personas a las que Alice decida revelar la prueba completa) sabrá que un determinado mensaje está oculto en esta transacción;
- Todo el mundo puede ver que el _punto de salida_ se ha gastado, pero sólo Bob tiene la prueba de que el mensaje está realmente anclado en la transacción.

Para ilustrar este esquema TxO2, podemos utilizar un _sello de un solo uso_ como mecanismo para revocar una clave PGP. En lugar de publicar un certificado de revocación en los servidores, Alice puede decir: "Esta salida de Bitcoin, si se gasta, significa que mi clave PGP está revocada".

Por lo tanto, Alice tiene un UTXO específico, al que se asocia localmente (en el lado del cliente) un determinado estado o dato (que sólo ella conoce).

Alice informa a Bob de que si se gasta este UTXO, se considerará que se ha producido un evento concreto. Desde fuera, todo lo que vemos es una transacción de Bitcoin; pero Bob sabe que este gasto tiene un significado oculto.

![RGB-Bitcoin](assets/fr/026.webp)

A medida que Alice gasta este UTXO, cierra el sello de un mensaje indicando su nueva clave, o simplemente la revocación de la antigua. De esta forma, cualquiera que monitorice en la cadena verá que el UTXO se ha gastado, pero sólo los que tengan la prueba completa sabrán que se trata precisamente de la revocación de la clave PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Para que Bob o cualquier otra persona implicada pueda comprobar el mensaje oculto, Alice debe proporcionarle información fuera de la cadena.

![RGB-Bitcoin](assets/fr/028.webp)

Por lo tanto, Alice debe proporcionar a Bob :


- El propio mensaje (por ejemplo, la nueva clave PGP) ;
- Prueba criptográfica de que el mensaje participó en la transacción (conocida como _prueba de transacción extra_ o _anclaje_).

![RGB-Bitcoin](assets/fr/029.webp)

Los terceros no disponen de esta información. Sólo ven que se ha gastado un UTXO. Por tanto, la confidencialidad está garantizada.

Para aclarar la estructura, resumamos el proceso en dos transacciones:


- Transacción 1**: Contiene la _definición del sello_, es decir, el _punto de salida_ que servirá de sello.

![RGB-Bitcoin](assets/fr/031.webp)


- Transacción 2**: Pasa este _outpoint_. Esto cierra el sello y, en la misma transacción, inserta el _commitment_ en el mensaje.

![RGB-Bitcoin](assets/fr/033.webp)

Por lo tanto, llamamos a la segunda transacción "transacción de testigos".

Para ilustrarlo desde otro ángulo, podemos representar dos capas:


- La capa superior (blockchain, pública)**: todo el mundo ve la transacción y sabe que se ha gastado un _punto_;
- La capa inferior (del lado del cliente, privada)** : sólo Alice (o la persona en cuestión) sabe que este gasto corresponde a tal o cual mensaje, a través de la prueba criptográfica y del mensaje que conserva localmente.

![RGB-Bitcoin](assets/fr/034.webp)

Pero al cerrar el sello, se plantea la cuestión de dónde debe insertarse el _compromiso_

En la sección anterior, mencionamos brevemente cómo el modelo de Validación del Lado del Cliente puede aplicarse a RGB y otros sistemas. Aquí, abordamos la parte sobre **compromisos deterministas de Bitcoin** y cómo integrarlos en una transacción. La idea es entender por qué estamos intentando insertar un único compromiso en la _transacción testigo_, y sobre todo cómo asegurar que no puede haber otros compromisos competidores no revelados.

### Lugares de compromiso en una transacción

Cuando le das a alguien la prueba de que un determinado mensaje está incrustado en una transacción, necesitas poder garantizar que no hay otra forma de compromiso (un segundo mensaje oculto) en la misma transacción que no te haya sido revelado. Para que la validación del lado del cliente siga siendo robusta, necesitas un mecanismo **determinista** para colocar un único _compromiso_ en la transacción que cierre el _sello de uso único_.

La _transacción testigo_ gasta el famoso UTXO (o _definición del sello_) y este gasto corresponde al cierre del sello. Técnicamente hablando, sabemos que cada punto de salida sólo puede gastarse una vez. Esto es precisamente lo que sustenta la resistencia de Bitcoin al doble gasto. Pero la transacción de gasto puede tener varias _entradas_, varias _salidas_, o estar compuesta de forma compleja (coinjoins, canales Lightning, etc.). Por lo tanto, necesitamos definir claramente dónde insertar el _compromiso_ en esta estructura, de forma inequívoca y uniforme.

Sea cual sea el método (PkO, TxO2, etc.), el _compromiso_ puede insertarse :


- En una entrada** vía :
    - Sigtweak** (modifica el componente `r` de la firma ECDSA, de forma similar al principio "Sign-to-contract") ;
    - Witweak** (se modifican los datos del _testigo_ de la transacción).
- En una salida** a través de :
    - Keytweak** (la clave pública del destinatario se "retoca" con el mensaje) ;
    - Opret** (el mensaje se coloca en una salida no gastable `OP_RETURN`) ;
    - Tapret** (o _Taptweak_), que se basa en taproot para insertar compromiso en la parte de script de una clave taproot, modificando así la clave pública de forma determinista.

![RGB-Bitcoin](assets/fr/035.webp)

He aquí los detalles de cada método:

![RGB-Bitcoin](assets/fr/038.webp)

***Ajustes de seguridad (firma por contrato) :***

Un esquema anterior consistía en explotar la parte aleatoria de una firma (ECDSA o Schnorr) para incrustar el _compromiso_: esta es la técnica conocida como "**Firma-a-contrato**". Se sustituye el nonce generado aleatoriamente por un hash que contiene los datos. De este modo, la firma revela implícitamente tu compromiso, sin espacio adicional en la transacción. Este enfoque tiene una serie de ventajas:


- No hay sobrecarga en la cadena (se utiliza el mismo lugar que el nonce básico);
- En teoría, esto puede ser bastante discreto, ya que el nonce es inicialmente un dato aleatorio.

Sin embargo, han surgido 2 grandes inconvenientes:


- Multisig antes de Taproot: cuando tienes varios firmantes, necesitas decidir qué firma llevará el _commitment_. Las firmas pueden ordenarse de forma diferente, y si un firmante se niega, pierdes el control sobre el resultado del _compromiso_;
- MuSig y el nonce compartido: con Schnorr multisig (*MuSig*), la generación del nonce es un algoritmo multipartito, y resulta prácticamente imposible modificar el nonce individualmente.

En la práctica, **sig tweak** tampoco es muy compatible con el hardware (monederos hardware) y los formatos existentes (Lightning, etc.). Así que esta gran idea es difícil de poner en práctica.

****Reto clave (pago por contrato) :***

El "ajuste de claves" retoma el concepto histórico de "pago por contrato". Tomamos la clave pública `X` y la modificamos añadiendo el valor `H(mensaje)`. En concreto, si `X = x * G` y `h = H(mensaje)`, la nueva clave será `X' = X + h * G`. Esta clave modificada oculta el compromiso con el "mensaje". El poseedor de la clave privada original puede, añadiendo `h` a su clave privada `x`, demostrar que tiene la clave para gastar la salida. En teoría, esto es elegante, porque :


- El _compromiso_ se introduce sin añadir ningún campo adicional;
- No almacenas ningún dato adicional en la cadena.

En la práctica, sin embargo, nos encontramos con las siguientes dificultades:


- Los monederos ya no reconocen la clave pública estándar, puesto que ha sido "retocada", por lo que no pueden asociar fácilmente UTXO con tu clave habitual;
- Los monederos hardware no están diseñados para firmar con una clave que no proceda de su derivación estándar;
- Debe adaptar sus guiones, descriptores, etc.

En el contexto del RGB, esta vía estaba prevista hasta 2021, pero resultó demasiado complicada para hacerla funcionar con las normas y la infraestructura actuales.

****

Otra idea, que algunos protocolos como _inscriptions Ordinals_ han puesto en práctica, consiste en colocar los datos directamente en la sección `testigo` de la transacción (de ahí la expresión "witness tweak"). Sin embargo, este método :


- Hace que el compromiso sea inmediatamente visible (se pegan literalmente los datos brutos en el testigo);
- Puede estar sujeta a censura (los mineros o nodos pueden negarse a retransmitirla si es demasiado grande o cualquier otra característica arbitraria);
- Consume espacio en los bloques, en contra del objetivo de discreción y ligereza del RGB.

Además, el testigo está diseñado para ser podable en determinados contextos, lo que puede complicar la obtención de pruebas sólidas.

***Apertura-retorno (opret) :***

Muy simple en su funcionamiento, un `OP_RETURN` permite almacenar un hash o mensaje en un campo especial de la transacción. Pero es inmediatamente detectable: todo el mundo ve que hay un _commitment_ en la transacción, y puede ser censurado o descartado, además de añadir salida extra. Dado que esto aumenta la transparencia y el tamaño, se considera menos satisfactorio desde el punto de vista de una solución de validación del lado del cliente.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

La última opción es el uso de **Taproot** (introducido con BIP341) con el esquema *Tapret*. *Tapret* es una forma más compleja de compromiso determinista, que aporta mejoras en términos de huella en la blockchain y confidencialidad para las operaciones contractuales. La idea principal es ocultar el compromiso en la parte `Script Path Spend` de una [transacción taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Antes de describir cómo se inserta el compromiso en una transacción taproot, veamos la **forma exacta** del compromiso, que debe **imperativamente** corresponder a una cadena de 64 bytes [construida](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) como sigue:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- Los 29 bytes `OP_RESERVED`, seguidos de `OP_RETURN`, y luego `OP_PUSHBYTE_33`, forman la parte _prefix_ de 31 bytes;
- A continuación viene un _commitment_ de 32 bytes (normalmente la raíz Merkle de **MPC**), al que añadimos 1 byte de **Nonce** (un total de 33 bytes para esta segunda parte).

Así que el método `Tapret` de 64 bytes parece un `Opret` al que hemos prefijado 29 bytes de `OP_RESERVED` y añadido un byte extra como Nonce.

Para mantener la flexibilidad en términos de implementación, confidencialidad y escalado, el esquema Tapret tiene en cuenta varios casos de uso, en función de los requisitos:


- Incorporación única de un compromiso Tapret en una transacción taproot sin una estructura Script Path preexistente;
- Integración de un compromiso Tapret en una transacción Taproot ya equipada con un Script Path.

Veamos más de cerca cada uno de estos dos escenarios.

#### Incorporación de Tapret sin Script Path existente

En este primer caso, partimos de una clave de salida taproot (*Taproot Output Key*) `Q` que contiene únicamente la clave pública interna `P` *(Internal Key*), sin ruta de script asociada (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: la clave pública interna para el _Gasto de la ruta de la clave_.
- `G`: el punto generador de la curva elíptica [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` es el factor de pellizco, calculado mediante un _tagged hash_ (por ejemplo `SHA-256(SHA-256(TapTweak) || P)`), de acuerdo con [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Esto prueba que no hay ningún script oculto.

Para incluir un compromiso de **Tapret**, añada un **Gasto de Ruta de Script** con un **script único**, como sigue:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` se convierte entonces en el nuevo factor de ajuste, incluyendo el **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` representa la raíz de este **script**, que es simplemente un hash de tipo `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

La prueba de inclusión y unicidad en el árbol raíz se reduce aquí a la única clave pública interna `P`.

#### Integración de Tapret en una Script Path preexistente

El segundo escenario se refiere a una salida `Q` taproot** más compleja, que ya contiene varios scripts. Por ejemplo, tenemos un árbol de 3 scripts:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` designa la función hash etiquetada normalizada de un script de hoja.
- a, B, C` representan guiones ya incluidos en la estructura taproot.

Para añadir el compromiso de Tapret, necesitamos insertar un *script no gastable* en el primer nivel del árbol, desplazando los scripts existentes un nivel hacia abajo. Visualmente, el árbol se convierte en :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` representa el hash etiquetado de la agrupación de nivel superior `A, B, C`.
- tHT` representa el hash del script correspondiente al `Tapret` de 64 bytes.

Según las reglas de taproot, cada rama/hoja debe combinarse según un orden hash lexicográfico. Hay dos casos posibles:


- `tHT` > `tHABC`: el compromiso Tapret se desplaza a la derecha del árbol. La prueba de unicidad sólo necesita `tHABC` y `P` ;
- tHT` < `tHABC`**: el compromiso Tapret se sitúa a la izquierda. Para probar que no hay otro compromiso Tapret a la derecha, `tHAB` y `tHC` deben ser revelados para demostrar la ausencia de cualquier otra escritura de este tipo.

Ejemplo visual para el primer caso (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Ejemplo para el segundo caso (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimización con el nonce

Para mejorar la confidencialidad, podemos "minar" (un término más preciso sería "bruteforcing") el valor del `<Nonce>` (el último byte del `Tapret` de 64 bytes) en un intento de obtener un hash `tHT` tal que `tHABC < tHT`. En este caso, el compromiso se coloca a la derecha, ahorrando al usuario tener que divulgar todo el contenido de los scripts existentes para probar la unicidad del Tapret.

En resumen, el `Tapret` ofrece una forma discreta y determinista de incorporar un compromiso a una transacción taproot, respetando al mismo tiempo el requisito de unicidad e inequívoco esencial para la validación del lado del cliente y la lógica de sello de un solo uso de RGB.

#### Salidas válidas

Para las transacciones de compromiso RGB, el requisito principal para un esquema de compromiso Bitcoin válido es el siguiente: La transacción (*transacción testigo*) debe contener de forma demostrable un único compromiso. Este requisito hace imposible construir un historial alternativo para los datos validados del lado del cliente dentro de la misma transacción. Esto significa que el mensaje alrededor del cual se cierra el _sello de uso único_ es único.

Para satisfacer este principio, e independientemente del número de salidas en una transacción, exigimos que **una y sólo una salida** pueda contener un compromiso (*commitment*). Para cada uno de los esquemas utilizados (*Opret* o *Tapret*), las únicas salidas válidas que pueden contener un _compromiso_ RGB son :


- La primera salida `OP_RETURN` (si está presente) para el esquema *Opret*;
- La primera salida taproot (si existe) para el esquema *Tapret*.

Tenga en cuenta que es muy posible que una transacción contenga un único compromiso `Opret` y un único compromiso `Tapret` en dos salidas separadas. Gracias a la naturaleza determinista de Seal Definition, estos dos compromisos corresponden entonces a dos piezas distintas de datos validados en el lado del cliente.

### Análisis y opciones prácticas en RGB

Cuando iniciamos RGB, revisamos todos estos métodos para determinar dónde y cómo colocar un _commitment_ en una transacción de forma determinista. Definimos algunos criterios:


- Compatibilidad con diferentes escenarios (por ejemplo, multisig, Lightning, carteras de hardware, etc.);
- Impacto en el espacio de la cadena ;
- Dificultad de aplicación y mantenimiento ;
- Confidencialidad y resistencia a la censura.

| Dimensionamiento en la cadena | Dimensionamiento en el lado del cliente | Integración de la cartera | Compatibilidad con hardware | Compatibilidad con Lightning | Compatibilidad con Taproot |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (deterministic P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (S2C determinista) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - | |

| Algoritmo Tapret: nodo superior izquierdo | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Algoritmo Tapret #4: cualquier nodo + prueba | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Esquema de compromiso determinista | Estándar | Coste en la cadena | Tamaño de las pruebas del lado del cliente |

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| LNPBP-1, 2 0 bytes 33 bytes (clave sin ajustar)

| Sigtweak (deterministic S2C) | WIP (LNPBP-39) | 0 bytes | 0 bytes |

| Opret (OP_RETURN) | - | 36 (v)bytes (TxOut adicional) | 0 bytes |

| Algoritmo Tapret: nodo superior izquierdo | LNPBP-6 | 32 bytes en testigo (8 vbytes) en cualquier multisig n-de-m y gastar por ruta de script | 0 bytes en scripts taproot scriptless ~270 bytes en un caso de script único, ~128 bytes si más de un script |

| Algoritmo Tapret #4: cualquier nodo + prueba de unicidad | LNPBP-6 | 32 bytes en el testigo (8 vbytes) para casos de un único script, 0 bytes en el testigo en la mayoría de los demás casos | 0 bytes en scripts sin script taproot, 65 bytes hasta que el Taptree tenga una docena de scripts |

| Capa | Coste de la cadena (bytes/vbytes) | Coste de la cadena (bytes/vbytes) | Coste de la cadena (bytes/vbytes) | Coste de la cadena (bytes/vbytes) | Coste de la cadena (bytes/vbytes) | Coste del lado del cliente (bytes) | Coste del lado del cliente (bytes) | Coste del lado del cliente (bytes) | Coste del lado del cliente (bytes) | Coste del lado del cliente (bytes) |

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Type** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Single-sig | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-de-n) | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-de-3 | 32/8 | 32/8 o 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3-de-5 | 32/8 | 32/8 o 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-de-3 con tiempos de espera | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

| Capa | Coste en cadena (vbytes) | Coste en cadena (vbytes) | Coste en cadena (vbytes) | Coste en el lado del cliente (bytes) | Coste en el lado del cliente (bytes) |

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Tipo** | **Base** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** |

| MuSig (n-de-n) | 16,5 | 0 | 0 | 0 | 0 | 0

| FROST (n-de-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-de-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| MuSig rama / Multi_a (n-de-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Con tiempos de espera (n-de-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Método | Confidencialidad y escalabilidad | Interoperabilidad | Compatibilidad | Portabilidad | Complejidad

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (deterministic P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 | 🟡

| Sigtweak (S2C determinista) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 | 🟢

| Algo Tapret: nodo superior izquierdo | 🟠 | 🟢 | 🔴 | 🟠 | 🟠

| Algo Tapret #4: Cualquier nodo + prueba | 🟢 | 🟢 | 🟠 | 🔴 |

En el transcurso del estudio, quedó claro que ninguno de los esquemas de compromiso era totalmente compatible con el actual estándar Lightning (que no emplea Taproot, _muSig2_ ni soporte adicional de _commitment_). Se está intentando modificar la construcción de canales de Lightning (*BiFrost*) para permitir la inserción de compromisos RGB. Esta es otra área en la que necesitamos revisar la estructura de la transacción, las claves y la forma en que se firman las actualizaciones del canal.

El análisis demostró que, de hecho, otros métodos (key tweak, sig tweak, witness tweak, etc.) presentaban otras formas de complicación:


- O tenemos un gran volumen en la cadena;
- O bien hay una incompatibilidad radical con el código de cartera existente;
- O bien la solución no es viable en multisig no cooperativo.

Para RGB, destacan dos métodos en particular: ***Opret*** y ***Tapret***, ambos clasificados como "Transaction Output", y compatibles con el modo TxO2 utilizado por el protocolo.

### Compromisos multiprotocolo - MPC

En esta sección, veremos cómo **RGB** gestiona la agregación de múltiples contratos (o, más concretamente, sus _paquetes de transición_) dentro de un único compromiso (*commitment*) registrado en una transacción Bitcoin mediante un esquema determinista (según `Opret` o `Tapret`). Para conseguirlo, el orden de Merkelización de los distintos contratos tiene lugar en una estructura denominada **Árbol MPC** (_Árbol de Compromisos Multiprotocolo_). En esta sección, veremos la construcción de este Árbol MPC, cómo obtener su raíz, y cómo múltiples contratos pueden compartir la misma transacción de forma confidencial y sin ambigüedades.

El Compromiso Multiprotocolo (MPC) está diseñado para satisfacer dos necesidades:


- La construcción del hash `mpc::Commitment`: se incluirá en la blockchain de Bitcoin según un esquema `Opret` o `Tapret`, y debe reflejar todos los cambios de estado a validar;
- Almacenamiento simultáneo de varios contratos en un único _commitment_, lo que permite gestionar actualizaciones independientes de varios activos o contratos RGB en una única transacción de Bitcoin.

En concreto, cada _paquete de transición_ pertenece a un contrato concreto. Toda esta información se inserta en un **Árbol MPC**, cuya raíz (`mpc::Root`) se somete de nuevo a hash para obtener el `mpc::Commitment`. Es este último hash el que se coloca en la transacción Bitcoin (_transacción testigo_), según el método determinista elegido.

![RGB-Bitcoin](assets/fr/042.webp)

#### Hash raíz MPC

El valor realmente escrito en la cadena (en `Opret` o `Tapret`) se denomina `mpc::Commitment`. Se calcula en forma de [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), según la fórmula :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

donde :


- `mpc_tag` es una etiqueta: `urn:ubideco:mpc:commitment#2024-01-31`, elegida según las [convenciones de etiquetado RGB](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) indica la profundidad del *Árbol del MPC* ;
- cofactor` (16 bits, en Little Endian) es un parámetro utilizado para promover la unicidad de las posiciones asignadas a cada contrato en el árbol;
- `mpc::Root` es la raíz del *Árbol del MPC*, calculada según el proceso descrito en la siguiente sección.

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC Construcción de árboles

Para construir este árbol MPC, tenemos que asegurarnos de que cada contrato corresponde a una única posición de hoja. Supongamos que tenemos :


- c` contratos a incluir, indexados por `i` en `i = {0,1,..,C-1}` ;
- Para cada contrato `c_i`, tenemos un identificador `ContractId(i) = c_i`.

A continuación, construimos un árbol de anchura `w` y profundidad `d` tal que `2^d = w`, con `w > C`, de modo que cada contrato pueda colocarse en una _hoja_ independiente. La posición `pos(c_i)` de cada contrato en el árbol viene determinada por :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

donde `cofactor` es un número entero que aumenta la probabilidad de obtener posiciones distintas para cada contrato. En la práctica, la construcción sigue un proceso iterativo:


- Partimos de una profundidad mínima (`d=3` por convención para ocultar el número exacto de contratos);
- Probamos diferentes `cofactores` (hasta `w/2`, o un máximo de 500 por razones de rendimiento);
- Si no conseguimos posicionar todos los contratos sin colisión, incrementamos `d` y volvemos a empezar.

El objetivo es evitar los árboles demasiado altos, reduciendo al mínimo el riesgo de colisión. Nótese que el fenómeno de la colisión sigue una lógica de distribución aleatoria, vinculada a la [Paradoja del Aniversario](https://en.wikipedia.org/wiki/Birthday_problem).

#### Hojas habitadas

Una vez obtenidas `C` posiciones distintas `pos(c_i)` para los contratos `i = {0,1,..,C-1}`, se rellena cada hoja con una función hash (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

donde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, se elige siempre según las convenciones Merkle de RGB ;
- `0x10` identifica una _hoja de contrato_ ;
- `c_i` es el identificador de contrato de 32 bytes (derivado del hash de Génesis);
- bundleId(c_i)` es un hash de 32 bytes que describe el conjunto de `State Transitions` relativas a `c_i` (reunidas en un *Bundle de Transiciones*).

#### Hojas deshabitadas

Las hojas restantes, no asignadas a un contrato (es decir, las hojas `w - C`), se rellenan con un valor "ficticio" (_hoja de entropía_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

donde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, se elige siempre según las convenciones Merkle de RGB ;
- `0x11` denota una _hoja de entropía_ ;
- `entropy` es un valor aleatorio de 64 bytes, elegido por la persona que construye el árbol;
- `j` es la posición (en Little Endian de 32 bits) de esta hoja en el árbol.

#### Nodos MPC

Tras generar las hojas `w` (habitadas o no), procedemos a la merkelización. Todos los nodos internos se merkelizan de la siguiente manera:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

donde :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, se elige siempre según las convenciones Merkle de RGB ;
- b` es el _factor de ramificación_ (8 bits). En la mayoría de los casos, `b=0x02` porque el árbol es binario y completo;
- d` es la profundidad del nodo en el árbol;
- `w` es la anchura del árbol (en binario Little Endian de 256 bits);
- tH1` y `tH2` son los hashes de los nodos hijos (u hojas), ya calculados como se muestra arriba.

Avanzando de este modo, obtenemos la raíz `mpc::Root`. A continuación, podemos calcular `mpc::Commitment` (como se ha explicado anteriormente) e insertarlo en la cadena.

Para ilustrarlo, imaginemos un ejemplo en el que `C=3` (tres contratos). Se supone que sus posiciones son `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Las otras hojas (posiciones 0, 1, 3, 5, 6) son _hojas de entropía_. El siguiente diagrama muestra la secuencia de hashes hasta la raíz con :


- que representa `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` y así sucesivamente, que representan hojas (unas para contratos, otras para entropía) ;
- Cada rama `tH_MPC_BRANCH(...)` combina los hashes de sus dos hijos.

El resultado final es el **mpc::Root**, y después el `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Comprobación del eje MPC

Cuando un verificador desea asegurarse de que un contrato `c_i` (y su `BundleId`) está incluido en el `mpc::Commitment` final, simplemente recibe una prueba Merkle. Esta prueba indica los nodos necesarios para rastrear las hojas (en este caso, la _hoja de contrato_ de `c_i`) hasta la raíz. No es necesario revelar todo el *Árbol del MPC*: así se protege la confidencialidad de otros contratos.

En el ejemplo, un verificador `c_2` sólo necesita un hash intermedio (`tH_MPC_LEAF(D)`), dos `tH_MPC_BRANCH(...)`, la prueba de posición `pos(c_2)` y el valor `cofactor`. Entonces puede reconstruir localmente la raíz, recalcular el `mpc::Commitment` y compararlo con el escrito en la transacción Bitcoin (dentro de `Opret` o `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Este mecanismo garantiza que :


- El estado relativo a `c_2` sí se incluye en el bloque de información agregada (del lado del cliente);
- Nadie puede construir un historial alternativo con la misma transacción, porque el _compromiso_ en cadena apunta a una única raíz MPC.

#### Resumen de la estructura de los PSM

El Compromiso Multiprotocolo* (MPC) es el principio que permite a RGB agregar múltiples contratos en una única transacción Bitcoin, manteniendo la unicidad de los compromisos y la confidencialidad frente a otros participantes. Gracias a la construcción determinista del árbol, a cada contrato se le asigna una posición única, y la presencia de hojas "ficticias" (*Hojas de Entropía*) enmascara parcialmente el número total de contratos que participan en la transacción.

El árbol de Merkle completo nunca se almacena en el cliente. Nos limitamos a generar una _Ruta Merkle_ para cada contrato en cuestión, que se transmitirá al destinatario (quien podrá validar el compromiso). En algunos casos, puede tener varios activos que hayan pasado por el mismo UTXO. En ese caso, puede fusionar varios _Merkle paths_ en un denominado _bloque de compromiso multiprotocolo_, para evitar duplicar demasiados datos.

Cada _prueba de Merkle_ es por tanto ligera, sobre todo porque la profundidad del árbol no superará los 32 en RGB. También existe la noción de "bloque de Merkle", que conserva más información (sección transversal, entropía, etc.), útil para combinar o separar varias ramas.

Por eso tardamos tanto en finalizar RGB. Teníamos la visión general desde 2019: poner todo en el lado del cliente, hacer circular los tokens fuera de la cadena. Pero detalles como la fragmentación para múltiples contratos, la estructura del árbol de Merkle, cómo gestionar las colisiones y las pruebas de fusión... todo esto requirió iteraciones.

### Anclajes: una asamblea global

Siguiendo con la construcción de nuestros compromisos (`Opret` o `Tapret`) y nuestro MPC (*Multi Protocol Commitment*), necesitamos abordar la noción de **Ancla** en el protocolo RGB. Un Ancla es una estructura validada por el cliente que reúne los elementos necesarios para verificar que un compromiso Bitcoin contiene realmente información contractual específica. En otras palabras, un Ancla resume todos los datos necesarios para validar los _compromisos_ descritos anteriormente.

Un Ancla consta de tres campos ordenados:


- `Txid
- prueba de MPC
- extra Transaction Proof - ETP

Cada uno de estos campos desempeña un papel en el proceso de validación, ya se trate de reconstruir la transacción Bitcoin subyacente o de demostrar la existencia de un compromiso oculto (especialmente en el caso de `Tapret`).

#### TxId

El campo `Txid` corresponde al identificador de 32 bytes de la transacción Bitcoin que contiene el compromiso `Opret` o `Tapret`.

En teoría, sería posible encontrar este `Txid` rastreando la cadena de transiciones de estado que a su vez apuntan a cada transacción testigo, siguiendo la lógica de los Sellos de un solo uso. Sin embargo, para facilitar y acelerar la verificación, este `Txid` simplemente se incluye en el Ancla, ahorrando así al validador tener que retroceder por todo el historial fuera de la cadena.

#### Prueba MPC

El segundo campo, `MPC Proof`, se refiere a la prueba de que este contrato concreto (por ejemplo, `c_i`) está incluido en el _Compromiso Multiprotocolo_. Es una combinación de :


- `pos_i`, la posición de este contrato en el árbol MPC;
- cofactor`, el valor definido para resolver las colisiones de posición;
- la "Prueba de Merkle", es decir, el conjunto de nodos y hashes utilizados para reconstruir la raíz del MPC y verificar que el identificador del contrato y su "Paquete de Transición" están asignados a la raíz.

Este mecanismo se describió en la sección anterior sobre la construcción del *Árbol del CMN*, donde cada contrato obtiene una hoja única gracias a la función :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

A continuación, se utiliza un esquema de merkelización determinista para agregar todas las hojas (contratos + entropía). Al final, el `MPC Proof` permite reconstruir localmente la raíz y compararla con el `mpc::Commitment` incluido en la cadena.

#### Prueba de Transacción Extra - ETP

El tercer campo, el **ETP**, depende del tipo de compromiso utilizado. Si el compromiso es del tipo `Opret`, no se requiere ninguna prueba adicional. El validador inspecciona la primera salida `OP_RETURN` de la transacción y encuentra el `mpc::Commitment` directamente allí.

**Si el compromiso es del tipo `Tapret`**, se debe proporcionar una prueba adicional denominada *Prueba de Transacción Extra - ETP*. Contiene :


- La clave pública interna (`P`) de la salida taproot en la que está incrustado el *commitment*;
- Los nodos compañeros del `Script Path Spend` (cuando el Tapret *commitment* se inserta en un script), para probar la localización exacta de este script en el árbol taproot:
 - Si el *compromiso* de `Tapret` está en la rama de la derecha, revelamos el nodo de la izquierda (por ejemplo, `tHABC`),
 - Si el *compromiso* `Tapret` está a la izquierda, hay que revelar 2 nodos (por ejemplo `tHAB` y `tHC`) para demostrar que no hay ningún otro *compromiso* a la derecha.
- El `nonce` puede ser usado para "minar" la mejor configuración, permitiendo que el *commitment* sea colocado a la derecha del árbol (optimización de la prueba).

Esta prueba adicional es esencial porque, a diferencia de `Opret`, el compromiso `Tapret` está integrado en la estructura de un script taproot, lo que requiere revelar parte del árbol taproot para validar correctamente la ubicación del *compromiso*.

![RGB-Bitcoin](assets/fr/045.webp)

Los **Anchors** encapsulan por tanto toda la información necesaria para validar un compromiso Bitcoin en el contexto de RGB. Indican tanto la transacción relevante (`Txid`) como la prueba de posicionamiento del contrato (`MPC Proof`), al tiempo que gestionan la prueba adicional (`ETP`) en el caso de `Tapret`. De este modo, un Ancla protege la integridad y la unicidad del estado fuera de la cadena garantizando que la misma transacción no pueda ser reinterpretada para otros datos contractuales.

### Conclusión

En este capítulo tratamos :


- Cómo aplicar el concepto de Sellos de un solo uso en Bitcoin (en particular a través de un _outpoint_);
- Los distintos métodos para insertar de forma determinista un _commitment_ en una transacción (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Las razones por las que RGB se centra en los compromisos de Tapret ;
- Gestión multicontrato a través de _multi-protocolo commitments_, esencial si no quieres exponer un estado entero u otros contratos cuando quieras probar un punto específico;
- También hemos visto el papel de los _Anchors_, que reúnen todo (TXID de transacción, prueba del árbol de Merkle y prueba Taproot) en un solo paquete.

En la práctica, la implementación técnica se reparte entre varios _crates_ dedicados a Rust (en _client_side_validation_, _commit-verify_, _bp_core_, etc.). Las nociones fundamentales están ahí:

![RGB-Bitcoin](assets/fr/046.webp)

En el próximo capítulo, veremos el componente puramente fuera de la cadena de RGB, es decir, la lógica del contrato. Veremos cómo los contratos de RGB, organizados como _máquinas de estado finito_ parcialmente replicadas, logran una expresividad mucho mayor que los scripts de Bitcoin, al tiempo que preservan la confidencialidad de sus datos.

## Introducción a los contratos inteligentes y sus estados

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

En este capítulo y en el siguiente, estudiaremos la noción de **contrato inteligente** dentro del entorno RGB y exploraremos las diferentes formas en que estos contratos pueden definir y evolucionar su *estado*. Veremos por qué la arquitectura RGB, utilizando la secuencia ordenada de Sellos de un solo uso, hace posible ejecutar varios tipos de ***Operaciones contractuales*** de forma escalable y sin pasar por un registro centralizado. También veremos el papel fundamental de la ***Lógica Empresarial*** a la hora de enmarcar la evolución del estado del contrato.

### Contratos inteligentes y derechos digitales al portador

El objetivo de RGB es proporcionar una infraestructura para implementar contratos inteligentes en Bitcoin. Por "contrato inteligente" entendemos un acuerdo entre varias partes que se aplica de forma automática y computacional, sin intervención humana para hacer cumplir las cláusulas. En otras palabras, la ley del contrato es aplicada por el software, no por un tercero de confianza.

Esta automatización plantea la cuestión de la descentralización: ¿cómo liberarse de un registro centralizado (por ejemplo, una plataforma o base de datos central) para gestionar la propiedad y la ejecución de los contratos? La idea original, retomada por RGB, es volver a un modo de propiedad conocido como "instrumentos al portador". Históricamente, ciertos títulos (bonos, acciones, etc.) se emitían al portador, lo que permitía a cualquiera que poseyera físicamente el documento hacer valer sus derechos.

![RGB-Bitcoin](assets/fr/055.webp)

RGB aplica este concepto al mundo digital: los derechos (y obligaciones) se encapsulan en datos que se manipulan fuera de la cadena, y el estado de estos datos es validado por los propios participantes. Esto permite, a priori, un grado de confidencialidad e independencia mucho mayor que el que ofrecen otros enfoques basados en registros públicos.

### Introducción al contrato inteligente Estado RGB

Un contrato inteligente en RGB puede verse como una máquina de estados, definida por :


- Un **Estado**, es decir, el conjunto de información que refleja la configuración actual del contrato;
- Una **Lógica de Negocio** (conjunto de reglas), que describe bajo qué condiciones y por quién puede ser modificado el estado.

![RGB-Bitcoin](assets/fr/056.webp)

Es importante entender que estos contratos no se limitan a la simple transferencia de tokens. Pueden incorporar una amplia variedad de aplicaciones: desde activos tradicionales (tokens, acciones, bonos) hasta mecanismos más complejos (derechos de uso, condiciones comerciales, etc.). A diferencia de otras blockchains, en las que el código del contrato es accesible y ejecutable por todos, el enfoque de RGB compartimenta el acceso y el conocimiento del contrato a los participantes ("***participantes en el contrato***"). Existen varios roles:


- El emisor** o creador del contrato, que define la Génesis del contrato y sus variables iniciales;
- Partes con derechos** (*propiedad*) u otras capacidades de ejecución ;
- Observadores**, potencialmente limitados a ver cierta información, pero que no pueden provocar modificaciones.

Esta separación de roles contribuye a la resistencia a la censura, al garantizar que sólo las personas autorizadas puedan interactuar con el estado contractual. También confiere a RGB la capacidad de escalar horizontalmente: la mayoría de las validaciones tienen lugar fuera de la blockchain, y solo los anclajes criptográficos (los *compromisos*) se inscriben en Bitcoin.

### Estado y lógica empresarial en RGB

Desde un punto de vista práctico, la **Lógica Empresarial** del contrato adopta la forma de reglas y guiones, definidos en lo que RGB denomina un **Esquema**. El esquema codifica :


- Estructura del Estado (¿qué ámbitos son públicos? ¿Qué campos son propiedad de qué partes?
- Condiciones de validez (¿qué debe comprobarse antes de autorizar una actualización de estado?) ;
- Autorizaciones (¿quién puede iniciar una *Transición de Estado*? ¿Quién puede limitarse a observar?).

Al mismo tiempo, el **Estado contratante** suele dividirse en dos componentes:


- Un **Estado Global**: parte pública, potencialmente observable por todos (dependiendo de la configuración);
- Estados propios**: partes privadas, asignadas específicamente a los propietarios mediante UTXOs referenciados en la lógica del contrato.

Como veremos en los siguientes capítulos, cualquier actualización de estado (*Operación de contrato*) debe acoplarse a un _compromiso_ de Bitcoin (mediante `Opret` o `Tapret`) y cumplir con los guiones de *Lógica de negocio* para considerarse válida.

### Operaciones contractuales: creación y evolución del Estado

En el universo RGB, una ***Operación de contrato*** es cualquier evento que cambia el contrato de un **estado antiguo** a un **estado nuevo**. Estas operaciones siguen la siguiente lógica:


- Tomamos nota del estado actual del contrato;
- Aplicamos la regla u operación (una ***Transición de Estado***, una ***Génesis*** si es el primer estado, o una ***Extensión de Estado*** si hay una *valencia* pública que volver a activar);
- Anclamos la modificación mediante un nuevo _commitment_ en la blockchain, cerrando un _sello de uso único_ y creando otro ;
- Los titulares de derechos afectados validan localmente (*del lado del cliente*) que la transición se ajusta al *Esquema* y que la transacción Bitcoin asociada está registrada en la cadena.

![RGB-Bitcoin](assets/fr/057.webp)

El resultado final es un contrato actualizado, ahora con un estado diferente. Esta transición no requiere que toda la red Bitcoin se preocupe de los detalles, ya que sólo una pequeña huella criptográfica (el _compromiso_) se registra en la blockchain. La secuencia de Sellos de un solo uso impide cualquier doble gasto o doble uso del Estado.

### Cadena de operaciones: del Génesis al Estado Terminal

Para ponerlo en perspectiva, un contrato inteligente RGB comienza con un **Génesis**, el primer estado. A partir de ahí, se suceden varias operaciones contractuales, formando un DAG (*Gráfico acíclico dirigido*) de operaciones:


- Cada transición se basa en un estado anterior (o en varios, en el caso de las transiciones convergentes);
- El orden cronológico está garantizado por la inclusión de cada transición en un ancla Bitcoin, con sello de tiempo e inalterable gracias al consenso por Proof-of-Work ;
- Cuando no hay más operaciones en curso, se alcanza un **Estado terminal**: el estado más reciente y completo del contrato.

![RGB-Bitcoin](assets/fr/012.webp)

Esta topología DAG (en lugar de una simple cadena lineal) refleja la posibilidad de que distintas partes del contrato evolucionen en paralelo, siempre que no se contradigan entre sí. RGB se encarga entonces de evitar cualquier incoherencia mediante la verificación *del lado del cliente* de cada participante implicado.

### Resumen

Los contratos inteligentes en RGB introducen un modelo de instrumentos digitales al portador, descentralizados pero anclados en Bitcoin para sellar el tiempo y garantizar el orden de las transacciones. La ejecución automatizada de estos contratos se basa en :


- Un **Estado del contrato*, que indica la configuración actual del contrato (derechos, saldos, variables, etc.);
- Una **Lógica de Negocio** (*Esquema*), que define qué transiciones están permitidas y cómo deben ser validadas;
- Operaciones contractuales**, que actualizan este estado paso a paso, gracias a compromisos anclados en transacciones Bitcoin.

En el próximo capítulo, entraremos en más detalle sobre la representación concreta de estos ***estados*** y ***transiciones de estado*** a nivel fuera de la cadena, y cómo se relacionan con los UTXOs y los Sellos de un solo uso incrustados en Bitcoin. Esta será una oportunidad para ver cómo la mecánica interna de RGB, basada en la validación del lado del cliente, consigue mantener la consistencia de los contratos inteligentes a la vez que preserva la confidencialidad de los datos.

## Operaciones contractuales RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

En este capítulo, veremos cómo funcionan las operaciones en los contratos inteligentes y las transiciones de estado, de nuevo dentro del protocolo RGB. También se tratará de entender cómo cooperan varios participantes para transferir la propiedad de un activo.

### Transiciones de estado y su mecánica

El principio general sigue siendo el de la validación del lado del cliente, donde los datos de estado los tiene el propietario y los valida el destinatario. Sin embargo, la especificidad aquí con RGB radica en el hecho de que Bob, como destinatario, pide a Alice que incorpore cierta información a los datos del contrato para tener un control real sobre el bien recibido, a través de una referencia oculta a uno de sus UTXOs.

Para ilustrar el proceso de una *Transición de Estado* (que es una de las ***Operaciones de Contrato*** fundamentales en RGB), tomemos un ejemplo paso a paso de una transferencia de activos entre Alice y Bob:

**Situación inicial:**

Alice tiene un ***stash RGB*** de datos validados localmente (*client-side*). Este alijo se refiere a uno de sus UTXOs en Bitcoin. Esto significa que una _definición de sello_ en estos datos apunta a un UTXO perteneciente a Alice. La idea es permitirle a ella transferir ciertos derechos digitales vinculados a un activo (por ejemplo, tokens RGB) a Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob también tiene UTXOs :**

Bob, por otro lado, tiene al menos un UTXO propio, sin vínculo directo con el de Alice. En el caso de que Bob no tenga UTXO, todavía es posible hacer la transferencia a él utilizando la propia *transacción testigo*: la salida de esta transacción incluirá entonces el compromiso (_commitment_) y asociará implícitamente la propiedad del nuevo contrato con Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Construcción de la nueva propiedad (*Nuevo Estado*) :**

Bob envía a Alice información codificada en forma de ***factura*** (entraremos en más detalle sobre la construcción de facturas en capítulos posteriores), pidiéndole que cree un nuevo estado que se ajuste a las reglas del contrato. Este estado incluirá una nueva *definición de sello* apuntando a uno de los UTXOs de Bob. De este modo, Bob recibe la propiedad de los activos definidos en este nuevo estado, por ejemplo una cierta cantidad de tokens RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Preparación de la transacción de muestra:**

Alice crea entonces una transacción Bitcoin gastando el UTXO referenciado en el sello anterior (el que la legitimó como titular). En la salida de esta transacción, se inserta un *compromiso* (mediante `Opret` o `Tapret`) para anclar el nuevo estado RGB. Los compromisos `Opret` o `Tapret` se derivan de un *árbol MPC* (como se ha visto en capítulos anteriores), que puede agregar varias transiciones de diferentes contratos.

**Transmisión de *Consignación* a Bob:**

Antes de emitir la transacción, Alice envía a Bob una ***Consignación*** que contiene todos los datos *del lado del cliente* necesarios (su *stash*) y la nueva información de estado a favor de Bob. En este punto, Bob aplica las reglas de consenso RGB:


- Valida todos los datos RGB contenidos en la *Consignación*, incluido el nuevo estado que le otorga la propiedad del activo;
- Basándose en los *Anclajes* incluidos en la *Consignación*, verifica la cronología de las transacciones de los testigos (desde Génesis hasta la transición más reciente) y valida los compromisos correspondientes en la blockchain.

**Terminación de la transición:**

Si Bob está satisfecho, puede dar su aprobación (por ejemplo, firmando la *consignación*). Alice puede entonces emitir la transacción de muestra preparada. Una vez confirmada, esto cierra el sello que anteriormente tenía Alice y formaliza la propiedad por parte de Bob. La seguridad contra el doble gasto se basa entonces en el mismo mecanismo que en Bitcoin: el UTXO se gasta, lo que demuestra que Alice ya no puede reutilizarlo.

![RGB-Bitcoin](assets/fr/061.webp)

El nuevo estado ahora hace referencia al UTXO de Bob, dándole a Bob la propiedad que antes tenía Alice. La salida de Bitcoin donde se anclan los datos RGB se convierte en la prueba irrevocable de la transferencia de propiedad.

Un ejemplo de un DAG mínimo (*Gráfico acíclico dirigido*) que comprende dos operaciones contractuales (una **Génesis** y luego una ***Transición de estado***) puede ilustrar cómo el estado RGB (capa *del lado del cliente*, en rojo) se conecta a la blockchain de Bitcoin (capa *Compromiso*, en naranja).

![RGB-Bitcoin](assets/fr/062.webp)

Muestra que un Genesis define un sello (*seal definition*), luego un *State Transition* cierra este sello para crear uno nuevo en otro UTXO.

En este contexto, he aquí algunos recordatorios terminológicos:


- Una ***Asignación*** combina :
    - Un ***Seal Definition*** (que apunta a un UTXO);
    - Estados de propiedad**, es decir, datos vinculados a la propiedad (por ejemplo, la cantidad de fichas transferidas).
- Un **Estado Global** reúne las propiedades generales del contrato, visibles para todos, y garantiza la coherencia global de las evoluciones.

Las Transiciones de Estado**, descritas en el capítulo anterior, son la principal forma de operación contractual. Hacen referencia a uno o más estados anteriores (de Génesis o de otra Transición de Estado) y los actualizan a un nuevo estado.

![RGB-Bitcoin](assets/fr/063.webp)

Este diagrama muestra cómo, en un *Bundle de Transiciones de Estado*, pueden cerrarse varios sellos en una única transacción de muestra, al tiempo que se abren nuevos sellos. De hecho, una característica interesante del protocolo RGB es su capacidad para escalar: varias transiciones pueden agregarse en un Paquete de Transiciones, estando cada agregación asociada a una hoja distinta del *árbol MPC* (un identificador único de paquete). Gracias al mecanismo *Deterministic Bitcoin Commitment* (DBC), el mensaje completo se inserta en una salida `Tapret` u `Opret`, al tiempo que se cierran los sellos anteriores y posiblemente se definen otros nuevos. El `Anchor* sirve de enlace directo entre el compromiso almacenado en la blockchain y la estructura de validación del lado del cliente (*client-side*).

En los siguientes capítulos, veremos todos los componentes y procesos implicados en la construcción y validación de una Transición de Estado. La mayoría de estos elementos forman parte del consenso RGB, implementado en la **RGB Core Library**.

### Paquete de transición

En RGB, es posible agrupar diferentes transiciones de estado que pertenezcan al mismo contrato (es decir, que compartan el mismo **ContractId**, derivado del **OpId** de Génesis). En el caso más sencillo, como entre Alice y Bob en el ejemplo anterior, un **Conjunto de Transiciones** contiene una sola transición. Pero la compatibilidad con operaciones multipago (como coinjoins, aperturas de canales Lightning, etc.) significa que varios usuarios pueden combinar sus transiciones de estado en un único paquete.

Una vez recogidas, estas transiciones se anclan (mediante el mecanismo MPC + DBC) en una única transacción Bitcoin:


- Cada transición de estado se codifica y agrupa en un paquete de transiciones;
- El Paquete de Transición se codifica y se inserta en la hoja del árbol MPC correspondiente a este contrato (un BundleId);
- El árbol MPC se compromete finalmente mediante `Opret` o `Tapret` en la transacción testigo, que cierra así los sellos consumidos y define los nuevos sellos.

Técnicamente hablando, el **BundleId** insertado en la hoja MPC se obtiene a partir de un hash etiquetado aplicado a la serialización estricta del campo *InputMap* del bundle:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

En el que `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` por ejemplo.

El *InputMap* es una estructura de datos que lista, para cada entrada `i` de la transacción de muestra, la referencia al *OpId* de la correspondiente Transición de Estado. Por ejemplo:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- n" es el número total de entradas en la transacción que hacen referencia a un "OpId";
- opId(input_j)` es el identificador de operación de una de las Transiciones de Estado presentes en el paquete.

Al hacer referencia a cada entrada una sola vez y de forma ordenada, evitamos que el mismo sello se gaste dos veces en dos transiciones de estado simultáneas.

### Generación de estados y estado activo

Por tanto, las transiciones de estado pueden utilizarse para transferir la propiedad de un bien de una persona a otra. Sin embargo, no son las únicas operaciones posibles en el protocolo RGB. El protocolo define tres **operaciones de contrato** :


- Transición de estado** ;
- Génesis** ;
- Extensión estatal**.

Entre ellas, **Génesis** y **Extensión de estados** se denominan a veces "*operaciones de generación de estados*", porque crean nuevos estados sin cerrar ninguno inmediatamente. Este es un punto muy importante: **Génesis** y **Extensión de Estado** no implican el cierre de un sello. Más bien, definen un nuevo sello, que luego debe ser gastado por una **Transición de Estado** posterior para ser realmente validado en el historial del blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

El **Estado Activo** de un contrato suele definirse como el conjunto de los últimos estados resultantes del historial (el DAG) de transacciones, empezando por la Génesis y siguiendo por todas las anclas en la blockchain de Bitcoin. Cualquier estado antiguo que ya esté obsoleto (es decir, unido a UTXOs gastados) ya no se considera activo, pero sigue siendo esencial para comprobar la consistencia del historial.

### Génesis

La Génesis es el punto de partida de todo contrato RGB. Es creada por el emisor del contrato y define los parámetros iniciales, de acuerdo con el **Esquema**. En el caso de un token RGB, el Génesis puede especificar, por ejemplo :


- El número de fichas creadas originalmente y sus propietarios;
- Límite máximo total de emisión posible ;
- Las posibles normas de reedición y qué participantes pueden optar a ellas.

Al ser la primera transacción del contrato, el Génesis no hace referencia a ningún estado anterior, ni cierra ningún sello. Sin embargo, para aparecer en el historial y ser validada, la Génesis debe ser **consumida** (cerrada) por una primera Transición de Estado (a menudo una transacción de escaneo/autogiro al propio emisor, o la distribución inicial a los usuarios).

### Extensión estatal

Las Extensiones de Estado** ofrecen una característica original para los contratos inteligentes. Permiten rescatar ciertos derechos digitales (*Valencias*) previstos en la definición del contrato, sin cerrar inmediatamente el sello. En la mayoría de los casos, se trata de :


- Emisión de fichas distribuidas;
- Mecanismos de permuta de activos ;
- Reemisiones condicionales (que pueden incluir la destrucción de otros activos, etc.).

Desde un punto de vista técnico, una Extensión de Estado hace referencia a un *Redeem* (un tipo particular de entrada RGB) que corresponde a una *Valencia* definida previamente (por ejemplo, en Génesis o en otra Transición de Estado). Define un nuevo sello, disponible para la persona o condición que se beneficia de él. Para que este sello se haga efectivo, debe ser gastado por una Transición de Estado posterior.

![RGB-Bitcoin](assets/fr/065.webp)

Por ejemplo: el Génesis crea un derecho de emisión (*Valencia*). Esto puede ser ejercido por un actor autorizado, que luego construye una Extensión del Estado :


- Se refiere a la Valencia (redimir);
- Crea una nueva *asignación* (nuevos datos de *Estado propio*) que apunta a un UTXO ;
- Una futura Transición de Estado, emitida por el propietario de este nuevo UTXO, transferirá o distribuirá realmente los tokens recién emitidos.

### Componentes de una operación contractual

Me gustaría ahora examinar en detalle cada uno de los elementos constitutivos de una **Operación de Contrato** en RGB. Una Operación Contractual es la acción que modifica el estado de un contrato, y que es validada en el lado cliente, de forma determinista, por el destinatario legítimo. En concreto, veremos cómo la Operación de Contrato tiene en cuenta, por un lado, el **estado antiguo** (*Old State*) del contrato, y por otro, la definición de un **nuevo estado** (*New State*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Si observamos el diagrama anterior, podemos ver que una Operación Contractual incluye elementos referidos al **Estado Nuevo** y otros referidos al **Estado Antiguo** actualizado.

Los elementos del **Nuevo Estado** son :


- Asignaciones**, en las que se definen :
 - La **Definición de Sello**;
 - El **Estado propietario**.
- El **Estado Global**, que puede modificarse o enriquecerse ;
- Valencias**, posiblemente definidas en una Transición de Estado o Génesis.

El **Estado Antiguo** está referenciado mediante :


- Entradas**, que apuntan a *Asignaciones* de transiciones de estado anteriores (no presentes en Génesis);
- Redeems**, que hacen referencia a Valencias definidas previamente (sólo en Extensiones de Estado).

Además, una Operación Contractual incluye campos más generales específicos de la operación:


- ffv` (*Versión rápida*): entero de 2 bytes que indica la versión del contrato;
- transitionType` o ExtensionType`: entero de 16 bits que especifica el tipo de Transición o Extensión, según la lógica de negocio;
- `ContractId`: número de 32 bytes que hace referencia al *OpId* del contrato Génesis. Incluido en Transitions y Extensions, pero no en Genesis ;
- schemaId: presente sólo en Genesis, es el hash de 32 bytes que representa la estructura (*Schema*) del contrato;
- testnet`: Booleano que indica si estás en la red Testnet o Mainnet. Sólo Genesis;
- altlayers1`: variable que identifica la capa alternativa (sidechain u otra) utilizada para anclar datos además de Bitcoin. Sólo presente en Genesis ;
- metadatos": campo que puede almacenar información temporal, útil para validar un contrato complejo, pero que no debe registrarse en el historial de estado final.

Por último, todos estos campos se condensan mediante un proceso de hash personalizado, para producir una huella digital única, el `OpId`. Este `OpId` se integra en el paquete de transición, lo que permite autenticarlo y validarlo dentro del protocolo.

Por tanto, cada *Operación de contrato* se identifica mediante un hash de 32 bytes denominado `OpId`. Este hash se calcula mediante un hash SHA256 de todos los elementos que componen la operación. En otras palabras, cada *Operación de Contrato* tiene su propio compromiso criptográfico, que incluye todos los datos necesarios para verificar la autenticidad y consistencia de la operación.

Un contrato RGB se identifica entonces mediante un `ContractId`, derivado del `OpId` de Génesis (ya que no existe ninguna operación previa a Génesis). En concreto, tomamos el `OpId` de Génesis, invertimos el orden de los bytes y aplicamos una codificación Base58. Esta codificación hace que el `ContractId` sea más fácil de manejar y reconocer.

### Métodos y reglas de actualización de estado

El **Estado del contrato** representa el conjunto de informaciones que el protocolo RGB debe seguir para un contrato dado. Se compone de :


- Un único Estado Global**: es la parte pública y global del contrato, visible para todos;
- Uno o más Estados Propios**: cada Estado Propio está asociado a un sello único (y por tanto a un UTXO en Bitcoin). Se distingue entre :
    - Los Estados de propiedad **pública**,
    - Los Estados de propiedad **privada**.

![RGB-Bitcoin](assets/fr/066.webp)

El *Estado Global* se incluye directamente en la *Operación de Contrato* como un único bloque. Los *Owned States* se definen en cada *Assignment*, junto a la *Seal Definition*.

Una característica importante de RGB es la forma en que se modifican el Estado Global y los Estados Propios. En general, existen dos tipos de comportamiento:


- Mutable**: cuando un elemento de estado se describe como mutable, cada nueva operación sustituye el estado anterior por un nuevo estado. Los datos antiguos se consideran entonces obsoletos;
- Acumulación**: cuando un elemento de estado se define como acumulador, cada nueva operación añade nueva información al estado anterior, sin sobrescribirla. El resultado es una especie de historial acumulado.

Si, en el contrato, un elemento de estado no se define como mutable o acumulativo, este elemento permanecerá vacío para las operaciones posteriores (en otras palabras, no hay nuevas versiones para este campo). Es el Esquema del contrato (es decir, la lógica de negocio codificada) el que determina si un estado (Global o Propio) es mutable, acumulativo o fijo. Una vez definida la Génesis, estas propiedades sólo pueden modificarse si el propio contrato lo permite, por ejemplo a través de una Extensión de Estado específica.

La tabla siguiente ilustra cómo cada tipo de Operación de contrato puede manipular (o no) el Estado global y el Estado propio:

| Génesis | Extensión de estado | Transición de estado |

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Añadir Estado Global** | + | - | + |

| n/a | - | + | **Mutación del Estado Global** | - | + |

| **Añadir Estado Propio** | + | - | + |

| **Mutación de Estado Propio** | n/a | No | + |

| **Añadir Valencias** | + | + | + | + |

**`+`** : acción posible si el Esquema del contrato lo permite.

**`-`**: la operación debe ser confirmada por una Transición de Estado posterior (la Extensión de Estado por sí sola no cierra el Sello de un solo uso).

Además, el ámbito temporal y los derechos de actualización de cada tipo de datos pueden distinguirse en la siguiente tabla:

| Metadatos | Estado Global | Estado Propio |

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Definido para una única Operación de Contrato | Definido globalmente para el contrato | Definido para cada sello (*Asignación*) | Definido para una única Operación de Contrato | Definido globalmente para el contrato | Definido para cada sello (*Asignación*) | Definido para cada contrato

| No actualizable (datos efímeros) | Transacción emitida por actores (emisor, etc.) | Depende del titular legítimo del sello (el que puede gastarlo en una transacción posterior) | Transacción emitida por actores (emisor, etc.) | Depende del titular legítimo del sello (el que puede gastarlo en una transacción posterior) | Transacción emitida por actores (emisor, etc.)

| El estado se define antes de la operación (por la *Seal Definition* de la operación anterior) | El estado se establece al final de la operación

### Estado mundial

El Estado Global se describe a menudo como "nadie posee, todo el mundo conoce". Contiene información general sobre el contrato, que es públicamente visible. Por ejemplo, en un contrato de emisión de tokens, puede contener :


- El ticker (abreviatura simbólica del token): `ticker` ;
- El nombre completo del token: `name` ;
- Precisión (número de decimales): `precisión` ;
- Oferta inicial (y/o límite máximo de tokens): `ofertaemitida` ;
- Fecha de emisión: `created` ;
- Datos legales u otra información pública: `data`.

Este Estado Global puede colocarse en recursos públicos (sitios web, IPFS, Nostr, Torrent, etc.) y distribuirse a la comunidad. Además, el incentivo económico (la necesidad de mantener y transferir estos tokens, etc.) impulsa de forma natural a los usuarios contratantes a mantener y propagar estos datos por sí mismos.

### Asignaciones

La *Asignación* es la estructura básica para definir :


- El sello (*Seal Definition*), que apunta a un UTXO específico;
- El *Estado de propiedad*, es decir, la propiedad o los datos asociados a este sello.

Una *Asignación* puede verse como el análogo de una salida de transacción de Bitcoin, pero con más flexibilidad. Aquí reside la lógica de la transferencia de propiedad: la *Asignación* asocia un tipo particular de activo o derecho (`Tipo de Asignación`) con un sello. Quien posea la clave privada del UTXO vinculado a este sello (o quien pueda gastar este UTXO) se considera propietario de este *Estado de propiedad*.

Uno de los grandes puntos fuertes de RGB reside en la capacidad de revelar (*revelar*) u ocultar (*ocultar*) los campos *Seal Definition* y *Owned State* a voluntad. Esto ofrece una potente combinación de confidencialidad y selectividad. Por ejemplo, puedes demostrar que una transición es válida sin revelar todos los datos, proporcionando la versión revelada a la persona que tiene que validarla, mientras que terceros sólo ven la versión oculta (un hash). En la práctica, el `OpId` de una transición siempre se calcula a partir de los datos *ocultos*.

![RGB-Bitcoin](assets/fr/067.webp)

#### Definición de foca

La *Seal Definition*, en su forma revelada, tiene cuatro campos básicos: `txptr`, `vout`, `blinding` y `method` :


- txptr**: es una referencia a un UTXO en Bitcoin :
    - En el caso de un **sello Génesis**, apunta directamente a un UTXO existente (el asociado al Génesis);
    - En el caso de un **sello gráfico**, podemos tener :
        - Un simple `txid`, si apunta a un UTXO específico,
        - O un `WitnessTx`, que designa una autorreferencia: el sello apunta a la propia transacción. Esto resulta especialmente útil cuando no se dispone de un UTXO externo, por ejemplo en las transacciones de apertura de canales Lightning, o si el destinatario no dispone de UTXO.
- vout** : el número de salida de la transacción indicada por `txptr`. Presente sólo para un sello Graph estándar (no para `WitnessTx`);
- cegador**: un número aleatorio de 8 bytes, para reforzar la confidencialidad y evitar intentos de fuerza bruta sobre la identidad del UTXO;
- método** : indica el método de anclaje utilizado (`Tapret` u `Opret`).

La forma *oculta* de la Definición del Sello es un hash SHA256 (etiquetado) de la concatenación de estos 4 campos, con una etiqueta específica para RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Estados propios

El segundo componente de *Asignación* es el Estado Propio. A diferencia del Estado Global, puede existir en forma pública o privada:


- Estado de titularidad pública**: todo el mundo conoce los datos asociados al sello. Por ejemplo, una imagen pública;
- Estado de propiedad privada**: los datos están ocultos, sólo los conoce el propietario (y potencialmente el validador si es necesario). Por ejemplo, el número de fichas que posee.

RGB define cuatro posibles tipos de estado (*StateTypes*) para un Estado Propio:


- Declarativo**: no contiene datos numéricos, sólo un derecho declarativo (por ejemplo, el derecho de voto). Las formas oculta y revelada son idénticas;
- Fungible**: representa una cantidad fungible (como las fichas). En forma revelada, tenemos "cantidad" y "cegamiento". En forma oculta, tenemos un único *compromiso de Pedersen* que oculta la cantidad y el cegamiento;
- Estructurado**: almacena datos estructurados (hasta 64 kB). En forma revelada, es el blob de datos. En forma oculta, es un hash etiquetado de este blob:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Con, por ejemplo :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Adjuntos**: vincula un archivo (audio, imagen, binario, etc.) al Estado Propio, almacenando el hash del archivo `file_hash`, el tipo MIME `media type` y una sal criptográfica `salt`. El propio archivo se aloja en otro lugar. En forma oculta, es un hash etiquetado con los tres datos anteriores:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Con, por ejemplo :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

En resumen, estos son los 4 tipos de estado posibles en la forma pública y oculta:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Declarativo** | **Fungible** | **Estructurado** | **Anexos** |

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| Ninguno | Entero con signo o sin signo de 64 bits | Cualquier tipo de dato estricto | Cualquier archivo |

| Tipo de información** | Ninguno | Con signo o sin signo | Tipos estrictos | Tipo MIME |

| Compromiso de Pedersen | Hashing con cegamiento | Hashed file ID

| Límites de tamaño** | N/A | 256 bytes | Hasta 64 KB | Hasta ~500 Gb |

### Entradas

Las Entradas de una *Operación de Contratación* se refieren a las *Asignaciones* que se están gastando en esta nueva operación. Una Entrada indica :


- prevOpId` : el identificador (`OpId`) de la operación anterior donde se encontraba la *Asignación*;
- assignmentType` : el tipo de *Assignment* (por ejemplo, `assetOwner` para un token) ;
- `Index`: el índice de la *Asignación* en la lista asociada al `OpId` anterior, determinado tras una ordenación lexicográfica de los sellos ocultos.

Las Entradas nunca aparecen en Génesis, ya que no hay Asignaciones previas. Tampoco aparecen en las Ampliaciones de Estado (porque las Ampliaciones de Estado no cierran sellos, sino que redefinen nuevos sellos basados en Valencias).

Cuando tenemos Estados Propios de tipo `Fungible`, la lógica de validación (a través del script AluVM proporcionado en el Esquema) comprueba la consistencia de las sumas: la suma de tokens entrantes (*Entradas*) debe ser igual a la suma de tokens salientes (en las nuevas *Asignaciones*).

### Metadatos

El campo **Metadatos** puede tener un máximo de 64 KiB y se utiliza para incluir datos temporales útiles para la validación, pero no integrados en el estado permanente del contrato. Por ejemplo, aquí pueden almacenarse variables de cálculo intermedias para scripts complejos. Este espacio no está destinado a ser almacenado en el historial global, por lo que queda fuera del ámbito de los Estados propios o del Estado global.

### Valencias

Las valencias** son un mecanismo original del protocolo RGB. Pueden encontrarse en Génesis, Transiciones de Estado o Extensiones de Estado. Representan derechos numéricos que pueden ser activados por una Extensión de Estado (a través de *Redeems*), y luego finalizados por una Transición posterior. Cada Valencia se identifica mediante un `ValencyType` (16 bits). Su semántica (derecho de reemisión, intercambio de fichas, derecho de quema, etc.) se define en el Esquema.

Concretamente, podríamos imaginar un Génesis que defina una valencia "derecho de reemisión". Una Extensión de Estado la consumirá (*Reemitir*) si se cumplen ciertas condiciones, con el fin de introducir una nueva cantidad de fichas. A continuación, una Transición de Estado emanada del poseedor del sello así creado podrá transferir estas nuevas fichas.

### Redime

Las Redenciones son el equivalente en Valencia de las Entradas para Asignaciones. Sólo aparecen en las Extensiones de Estado, ya que es aquí donde se activa una Valencia previamente definida. Un Canje consta de dos campos:


- `PrevOpId` : el `OpId` de la operación donde se especificó la Valencia;
- `ValencyType`: el tipo de Valency que desea activar (cada `ValencyType` sólo puede ser utilizado una vez por Extensión de Estado).

Ejemplo: un Canje puede corresponder a una ejecución de CoinSwap, dependiendo de lo que se haya codificado en la Valencia.

### Características de estado RGB

Ahora vamos a echar un vistazo a varias características de estado fundamentales en RGB. En particular, veremos :


- El **Sistema de Tipos Estrictos**, que impone una organización precisa y tipificada de los datos;
- La importancia de separar la **validación** de la **propiedad** ;
- El sistema de **evolución consensuada** en RGB, que incluye las nociones de *avance rápido* y *retroceso*.

Como siempre, ten en cuenta que todo lo relacionado con el estado del contrato se valida en el lado del cliente según las reglas de consenso establecidas en el protocolo, y cuya referencia criptográfica última está anclada en las transacciones de Bitcoin.

#### Sistema de tipos estricto

RGB utiliza un *Sistema de Tipos Estricto* y un modo de serialización determinista (*Codificación Estricta*). Esta organización está concebida para garantizar una perfecta reproducibilidad y precisión en la definición, tratamiento y validación de los datos contractuales.

En muchos entornos de programación (JSON, YAML...), la estructura de datos puede ser flexible, incluso demasiado permisiva. En RGB, en cambio, la estructura y los tipos de cada campo se definen con restricciones explícitas. Por ejemplo :


- Cada variable tiene un tipo específico (por ejemplo, un entero sin signo de 8 bits `u8`, o un entero con signo de 16 bits, etc.);
- Los tipos se pueden componer (tipos anidados). Esto significa que puede definir un tipo basado en otros tipos (por ejemplo, un tipo agregado que contenga un campo `u8`, un campo `bool`, etc.);
- También se pueden especificar colecciones: listas (*list*), conjuntos (*set*) o diccionarios (*map*), con un orden de progresión determinista;
- Cada campo está acotado (*límite inferior* / *límite superior*). También imponemos límites al número de elementos de las colecciones (contención);
- Los datos están alineados por bytes y la serialización está estrictamente definida y es inequívoca.

Gracias a este estricto protocolo de codificación :


- El orden de los campos es siempre el mismo, independientemente de la implementación o del lenguaje de programación utilizado;
- Los hashes calculados sobre el mismo conjunto de datos son, por tanto, reproducibles e idénticos (*compromisos* estrictamente deterministas);
- Los límites evitan el crecimiento incontrolado del tamaño de los datos (por ejemplo, demasiados campos);
- Esta forma de codificación facilita la verificación criptográfica, ya que cada participante sabe exactamente cómo serializar y aplicar el hash a los datos.

En la práctica, se compilan la estructura (*Esquema*) y el código resultante (*Interfaz* y lógica asociada). Se utiliza un lenguaje descriptivo para definir el contrato (tipos, campos, reglas) y generar un formato binario estricto. Una vez compilado, el resultado es :


- Un *Memory Layout* para cada campo;
- Identificadores semánticos (que indican si el cambio del nombre de una variable repercute en la lógica, aunque la estructura de memoria siga siendo la misma).

El estricto sistema de tipos también permite un seguimiento preciso de los cambios: cualquier modificación de la estructura (incluso un cambio de nombre de campo) es detectable y puede provocar un cambio en la huella global.

Por último, cada compilación produce una huella digital, un identificador criptográfico que da fe de la versión exacta del código (datos, reglas, validación). Por ejemplo, un identificador de la forma :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Esto permite gestionar las actualizaciones de consenso o de aplicación, garantizando al mismo tiempo una trazabilidad detallada de las versiones utilizadas en la red.

Para evitar que el estado de un contrato RGB resulte demasiado engorroso de validar del lado del cliente, una regla de consenso impone un tamaño máximo de `2^16` bytes (64 Kio) para cualquier dato que intervenga en los cálculos de validación. Esto se aplica a cada variable o estructura: no más de 65536 bytes, o el equivalente en números (32768 enteros de 16 bits, etc.). Esto también se aplica a las colecciones (listas, conjuntos, mapas), que no pueden superar los `2^16` elementos.

Este límite garantiza :


- Controla el tamaño máximo de los datos que se manipularán durante una transición de estado;
- Compatibilidad con la máquina virtual (*AluVM*) utilizada para ejecutar los scripts de validación.

#### El paradigma Validación != Apropiación

Una de las principales innovaciones de RGB es la estricta separación entre dos conceptos:


- Validación**: comprobación de que una transición de estado respeta las reglas del contrato (lógica de negocio, historial, etc.);
- La **propiedad** (ownership, o control): el hecho de poseer el Bitcoin UTXO que permite gastar (o cerrar) el Sello de un solo uso, y por tanto que se produzca la transición de estado.

La validación** tiene lugar a nivel de la pila de software de RGB (bibliotecas, protocolo de *compromisos*, etc.). Su función es garantizar que se respetan las normas internas del contrato (importes, permisos, etc.). Los observadores u otros participantes también pueden validar el historial de datos.

La propiedad**, por otro lado, depende totalmente de la seguridad de Bitcoin. Poseer la clave privada de un UTXO significa controlar la capacidad de lanzar una nueva transición (cerrar el sello de un solo uso). Por lo tanto, aunque alguien pueda ver o validar los datos, no podrá cambiar el estado si no posee el UTXO en cuestión.

![RGB-Bitcoin](assets/fr/069.webp)

Este enfoque limita las vulnerabilidades clásicas encontradas en blockchains más complejas (donde todo el código de un contrato inteligente es público y modificable por cualquiera, lo que a veces ha llevado a hackeos). En RGB, un atacante no puede simplemente interactuar con el estado de la cadena, ya que el derecho a actuar sobre el estado (*propiedad*) está protegido por la capa Bitcoin.

Además, este desacoplamiento permite a RGB integrarse de forma natural con la red Lightning. Los canales Lightning se pueden utilizar para comprometer y mover activos RGB sin comprometer *compromisos* en la cadena cada vez. Veremos más de cerca esta integración de RGB en Lightning en capítulos posteriores del curso.

#### Evolución del consenso en RGB

Además del versionado semántico del código, RGB incluye un sistema de evolución o actualización de las reglas de consenso de un contrato a lo largo del tiempo. Existen dos formas principales de evolución:


- Avance rápido**
- Push-back** (en francés)

Un avance rápido se produce cuando una norma que antes no era válida pasa a serlo. Por ejemplo, si el contrato evoluciona para permitir un nuevo tipo de `AssignmentType` o un nuevo campo :


- Esto no puede compararse con un hardfork clásico de blockchain, ya que RGB funciona en la validación del lado del cliente y no afecta a la compatibilidad general de la blockchain ;
- En la práctica, este tipo de cambio se indica mediante el campo `Ffv` (*versión rápida*) de la operación contractual;
- Los titulares actuales no se ven perjudicados: su estatus sigue siendo válido;
- Los nuevos beneficiarios (o nuevos usuarios), por otra parte, necesitan actualizar su software (su monedero) para reconocer las nuevas normas.

Un "push-back" significa que una norma anteriormente válida pasa a ser inválida. Se trata, por tanto, de un "endurecimiento" de las normas, pero no propiamente de un softfork:


- Los titulares existentes pueden verse afectados (podrían encontrarse con activos obsoletos o inválidos en la nueva versión);
- Podemos considerar que, de hecho, estamos creando un nuevo protocolo: quien adopta la nueva norma se aparta de la antigua;
- El emisor puede decidir volver a emitir activos en este nuevo protocolo, obligando a los usuarios a mantener dos carteras separadas (una para el protocolo antiguo y otra para el nuevo), si quieren gestionar ambas versiones.

En este capítulo sobre las operaciones contractuales RGB, hemos explorado los principios fundamentales que subyacen a este protocolo. Como te habrás dado cuenta, la complejidad inherente al protocolo RGB requiere el uso de muchos términos técnicos. Por ello, en el próximo capítulo, le proporcionaré un glosario que resumirá todos los conceptos tratados en esta primera parte teórica, con definiciones de todos los términos técnicos relacionados con RGB. A continuación, en la siguiente sección, abordaremos de forma práctica la definición y aplicación de los contratos RGB.

## Glosario RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Si necesitas volver a este breve glosario de términos técnicos importantes utilizados en el mundo RGB (enumerados por orden alfabético), te resultará útil. Este capítulo no es esencial si ya has entendido todo lo que hemos tratado en la primera sección.

#### AluVM

La abreviatura AluVM significa "_Algorithmic logic unit Virtual Machine_", una máquina virtual basada en registros diseñada para la validación de contratos inteligentes y la computación distribuida. Se utiliza (pero no se reserva exclusivamente) para la validación de contratos RGB. Los scripts u operaciones incluidos en un contrato RGB pueden así ejecutarse en el entorno AluVM.

Para más información: [Sitio web oficial de AluVM](https://www.aluvm.org/)

#### Ancla

Un Ancla representa un conjunto de datos del lado del cliente utilizados para demostrar la inclusión de un único _compromiso_ en una transacción. En el protocolo RGB, un anclaje consta de los siguientes elementos:


- El identificador de transacción Bitcoin (TXID) de la **transacción testigo** ;
- El **Compromiso Multiprotocolo (MPC)** ;
- El **Compromiso Determinista de Bitcoin (DBC)**;
- El **Extra Transaction Proof (ETP)** si se utiliza el mecanismo de compromiso **Tapret** (véase la sección dedicada a este modelo).

Por lo tanto, un Ancla sirve para establecer un vínculo verificable entre una transacción Bitcoin específica y los datos privados validados por el protocolo RGB. Garantiza que estos datos están efectivamente incluidos en la blockchain, sin que su contenido exacto quede expuesto públicamente.

#### Asignación

En la lógica de RGB, una Asignación es el equivalente de una salida de transacción que modifica, actualiza o crea ciertas propiedades dentro del estado de un contrato. Una asignación consta de dos elementos:


- A **Seal Definition** (referencia a un UTXO específico) ;
- Un **Estado propietario** (datos que describen el estado asociado a este nuevo propietario).

Por lo tanto, una Asignación indica que una parte del estado (por ejemplo, un activo) está ahora asignada a un titular concreto, identificado mediante un Sello de un solo uso vinculado a un UTXO.

#### Lógica empresarial

La lógica empresarial agrupa todas las reglas y operaciones internas de un contrato, descritas por su **esquema** (es decir, la estructura del propio contrato). Dicta cómo puede evolucionar el estado del contrato y en qué condiciones.

#### Validación en el lado del cliente

La validación del lado del cliente se refiere al proceso mediante el cual cada parte (cliente) verifica un conjunto de datos intercambiados de forma privada, de acuerdo con las reglas de un protocolo. En el caso de RGB, estos datos intercambiados se agrupan en lo que se conoce como **consignaciones**. A diferencia del protocolo Bitcoin, que exige que todas las transacciones se publiquen en la cadena, RGB sólo permite que las _consignaciones_ (ancladas en Bitcoin) se almacenen en público, mientras que la información esencial del contrato (transiciones, atestaciones, pruebas) permanece fuera de la cadena, compartida únicamente entre los usuarios implicados.

#### Compromiso

Un Compromiso (en el sentido criptográfico) es un objeto matemático, denotado `C`, derivado determinísticamente de una operación sobre datos estructurados `m` (el mensaje) y un valor aleatorio `r`. Escribimos :

$$
C = \text{commit}(m, r)
$$

Este mecanismo comprende dos operaciones principales:


- Compromiso**: se aplica una función criptográfica a un mensaje `m` y a un número aleatorio `r` para producir `C` ;
- Verificar**: utilizamos `C`, el mensaje `m` y el valor `r` para comprobar que este compromiso es correcto. La función devuelve `True` o `False`.

Un compromiso debe respetar dos propiedades:


- Vinculación**: debe ser imposible encontrar dos mensajes diferentes que produzcan la misma `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Tales como :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Ocultación**: el conocimiento de `C` no debe revelar el contenido de `m`.

En el protocolo RGB, se incluye un compromiso en una transacción Bitcoin para demostrar la existencia de cierta información en un momento dado, sin revelar la información en sí.

#### Consignación

Una **Consignación** agrupa los datos intercambiados entre las partes, sujetos a Validación por el Cliente en RGB. Existen dos categorías principales de consignación:


- Consignación de contrato**: suministrada por el *emisor* (emisor del contrato), incluye información de inicialización como Esquema, Génesis, Interfaz e Implementación de Interfaz.
- Consignación de transferencia**: suministrada por la parte pagadora (*pagador*). Contiene todo el historial de transiciones de estado que conducen a la consignación terminal (es decir, el estado final recibido por el pagador).

Estos envíos no se registran públicamente en la cadena de bloques, sino que se intercambian directamente entre las partes interesadas a través del canal de comunicación que elijan.

#### Contrato

Un Contrato es un conjunto de derechos ejecutados digitalmente entre varios actores a través del protocolo RGB. Tiene un estado activo y una lógica de negocio, definida por un Esquema, que especifica qué operaciones están autorizadas (transferencias, ampliaciones, etc.). El estado de un contrato, así como sus reglas de validez, se expresan en el Esquema. En un momento dado, el contrato evoluciona únicamente de acuerdo con lo permitido por este Esquema y por los scripts de validación (ejecutados, por ejemplo, en AluVM).

#### Operación contractual

Una operación de contrato es una actualización del estado de un contrato realizada de acuerdo con las reglas del esquema. En RGB existen las siguientes operaciones:


- Transición de estado** ;
- Génesis** ;
- Extensión Estatal**.

Cada operación modifica el estado añadiendo o sustituyendo determinados datos (Estado Global, Estado Propio...).

#### Participante en el contrato

Un Participante en el Contrato es un actor que interviene en las operaciones relativas al contrato. En RGB se distingue entre :


- El emisor del contrato, que crea el Génesis (el origen del contrato);
- Las partes del contrato, es decir, los titulares de derechos sobre el estado del contrato;
- Partes públicas, que pueden construir Extensiones del Estado si el contrato ofrece Valencies accesibles al público.

#### Derechos contractuales

Los derechos contractuales se refieren a los diversos derechos que pueden ejercer los implicados en un contrato RGB. Se dividen en varias categorías:


- Derechos de propiedad**, asociados a la propiedad de un UTXO concreto (a través de una _Seal Definition_);
- Derechos ejecutivos**, es decir, la capacidad de construir una o varias transiciones (Transiciones de Estado) de acuerdo con el Esquema ;
- Derechos públicos**, cuando el Esquema autoriza determinados usos públicos, por ejemplo la creación de una Extensión de Estado mediante el canje de una Valencia.

#### Estado del contrato

El Estado del Contrato corresponde al estado actual de un contrato en un momento dado. Puede estar compuesto tanto por datos públicos como privados, reflejando el estado del contrato. RGB distingue entre :


- El **Estado Global**, que incluye las propiedades públicas del contrato (configuradas en Genesis o añadidas mediante actualizaciones autorizadas);
- Estados de propiedad**, que pertenecen a propietarios específicos, identificados por sus UTXO.

#### Compromiso bitcoin determinista - DBC

Deterministic Bitcoin Commitment (DBC) es el conjunto de reglas utilizadas para registrar de forma demostrable y única un _compromiso_ en una transacción Bitcoin. En el protocolo RGB, hay dos formas principales de DBC:


- Opret**
- Tapret**

Estos mecanismos definen con precisión cómo se codifica el _compromiso_ en la salida o estructura de una transacción Bitcoin, para asegurar que este compromiso es determinísticamente rastreable y verificable.

#### Gráfico acíclico dirigido - DAG

Un DAG (o *Gráfico Guiado Acíclico*) es un grafo sin ciclos, que permite la programación topológica. Las Blockchains, como los _shards_ de los contratos RGB, pueden representarse mediante DAGs.

Para más información: [Grafo acíclico dirigido](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Grabado

El grabado es una cadena de datos opcional que los sucesivos propietarios de un contrato pueden introducir en el historial del contrato. Esta función existe, por ejemplo, en la interfaz **RGB21** y permite añadir información conmemorativa o descriptiva al historial del contrato.

#### Prueba de Transacción Extra - ETP

El ETP (*Extra Transaction Proof*) es la parte del Anchor que contiene los datos adicionales necesarios para validar un **Tapret** *commitment* (en el contexto de _taproot_). Incluye, entre otras cosas, la clave pública interna del taproot script (_internal PubKey_) e información específica del _Script Path Spend_.

#### Génesis

Génesis se refiere al conjunto de datos, gobernado por un Esquema, que forma el estado inicial de cualquier contrato en RGB. Puede compararse con el concepto de _Bloque Génesis_ de Bitcoin, o con el concepto de transacción de Coinbase, pero aquí a nivel de _lado del cliente_ y de token RGB.

#### Estado mundial

El Estado Global es el conjunto de propiedades públicas contenidas en el Estado del Contrato. Se define en Génesis y, dependiendo de las reglas del contrato, puede ser actualizado por transiciones autorizadas. A diferencia de los Estados Propios, el Estado Global no pertenece a una entidad en particular; está más cerca de un registro público dentro del contrato.

#### Interfaz

La Interfaz es el conjunto de instrucciones utilizadas para descodificar los datos binarios compilados en un Esquema o en operaciones de contrato y sus estados, con el fin de hacerlos legibles para el usuario o su monedero. Actúa como una capa de interpretación.

#### Aplicación de la interfaz

La implementación de la interfaz es el conjunto de declaraciones que vinculan una **Interfaz** a un **Esquema**. Permite la traducción semántica realizada por la propia Interfaz, de forma que los datos brutos de un contrato puedan ser entendidos por el usuario o el software implicado (los monederos).

#### Factura

Una factura adopta la forma de una URL codificada en [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), que incorpora los datos necesarios para la construcción de una **transición de estado** (por parte del pagador). En otras palabras, es una factura que permite a la contraparte (*pagador*) crear la transición correspondiente para transferir el activo o actualizar el estado del contrato.

#### Red del Rayo

La Lightning Network es una red descentralizada de canales de pago (o _canales de estado_) en Bitcoin, formada por monederos 2/2 multi-firma. Permite transacciones rápidas y de bajo coste _fuera de la cadena_, al tiempo que confía en la Capa 1 de Bitcoin para el arbitraje (o cierre) cuando es necesario.

Para más información sobre cómo funciona Lightning, te recomiendo que sigas este otro curso:

https://planb.network/courses/lnp201
#### Compromiso multiprotocolo - MPC

Multi Protocol Commitment (MPC) se refiere a la estructura de árbol de Merkle utilizada en RGB para incluir, dentro de una única transacción Bitcoin, varios **Transition Bundles** de diferentes contratos. La idea es agrupar varios compromisos (potencialmente correspondientes a diferentes contratos o diferentes activos) en un único punto de anclaje para optimizar la ocupación del espacio de bloque.

#### Estado de propiedad

Un Estado de titularidad es la parte de un Estado de contrato que está incluida en una Asignación y asociada a un titular concreto (mediante un Sello de un solo uso que apunta a un UTXO). Representa, por ejemplo, un activo digital o un derecho contractual específico asignado a esa persona.

#### Propiedad

La propiedad se refiere a la capacidad de controlar y gastar un UTXO referenciado por una Definición de Sello. Cuando un Estado Propio está vinculado a un UTXO, el propietario de este UTXO tiene derecho, potencialmente, a transferir o evolucionar el estado asociado, según las reglas del contrato.

#### Transacción Bitcoin Parcialmente Firmada - PSBT

Una PSBT (_Transacción Bitcoin Parcialmente Firmada_) es una transacción Bitcoin que aún no está totalmente firmada. Puede ser compartida entre varias entidades, cada una de las cuales puede añadir o verificar ciertos elementos (firmas, scripts...), hasta que la transacción se considere lista para su distribución en la cadena.

Para más información: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Compromiso de Pedersen

Un compromiso de Pedersen es un tipo de compromiso criptográfico con la propiedad de ser **homomórfico** con respecto a la operación de suma. Esto significa que es posible validar la suma de dos compromisos sin revelar los valores individuales.

Formalmente, si :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

entonces :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Esta propiedad es útil, por ejemplo, para ocultar las cantidades de fichas intercambiadas, sin dejar de poder verificar los totales.

Para más información: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Canjear

En una Extensión de Estado, un Canje se refiere a la acción de reclamar (o explotar) una **Valencia** previamente declarada. Como una Valencia es un derecho público, el Rescate permite a un participante autorizado reclamar una extensión de estado de contrato específica.

#### Esquema

Un esquema en RGB es un fragmento de código declarativo que describe el conjunto de variables, reglas y lógica de negocio (*Lógica de negocio*) que rigen el funcionamiento de un contrato. El esquema define la estructura de estados, los tipos de transiciones permitidas y las condiciones de validación.

#### Definición de foca

La Definición del Sello es la parte de una Cesión que asocia el _compromiso_ con un UTXO propiedad del nuevo titular. En otras palabras, indica dónde se encuentra la condición (en qué UTXO), y establece la propiedad de un activo o derecho.

#### Fragmento

Un fragmento representa una rama en el DAG del historial de transiciones de estado de un contrato RGB. En otras palabras, es un subconjunto coherente del historial global del contrato, que corresponde, por ejemplo, a la secuencia de transiciones necesarias para demostrar la validez de un determinado activo desde la _Génesis_.

#### Sello de un solo uso

Un sello de un solo uso es una promesa criptográfica de compromiso con un mensaje aún desconocido, que sólo se revelará una vez en el futuro y que debe ser conocido por todos los miembros de un público específico. El objetivo es evitar la creación de múltiples compromisos competidores para el mismo sello.

#### Alijo

El Stash es el conjunto de datos del lado del cliente que un usuario almacena para uno o varios contratos RGB, con fines de validación (*Validación del lado del cliente*). Esto incluye el historial de transiciones, envíos, pruebas de validez, etc. Cada titular conserva sólo las partes del historial que necesita (*shards*).

#### Extensión estatal

Una Extensión de Estado es una operación de contrato que se utiliza para volver a activar actualizaciones de estado mediante el canje de **Valencias** declaradas previamente. Para ser efectiva, una Extensión de Estado debe cerrarse mediante una Transición de Estado (que actualiza el estado final del contrato).

#### Transición de estados

La Transición de Estado es la operación que cambia el estado de un contrato RGB a un nuevo estado. Puede modificar datos del Estado Global y/o del Estado Propio. En la práctica, cada transición se verifica mediante reglas de Esquema y se ancla en la blockchain de Bitcoin mediante un _commitment_.

#### Taproot

Se refiere al formato de transacción Segwit v1 de Bitcoin, introducido por [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) y [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot mejora la confidencialidad y la flexibilidad de los scripts, en particular haciendo que las transacciones sean más compactas y más difíciles de distinguir unas de otras.

#### Terminal Consignación - Terminal Consignación

La Consignación Terminal (o _Punto Final de la Consignación_) es una *consignación de transferencia* que contiene el estado final del contrato, incluida la Transición de Estado creada a partir de la Factura del destinatario (*beneficiario*). Es, por tanto, el punto final de una transferencia, con los datos necesarios para demostrar que se ha transferido la propiedad o el estado.

#### Paquete de transición

Un paquete de transiciones es un conjunto de transiciones de estado RGB (pertenecientes al mismo contrato) que participan en la misma ***transacción de testigo*** Bitcoin. Esto permite agrupar varias actualizaciones o transferencias en un único anclaje en cadena.

#### UTXO

Un Bitcoin UTXO (*Unspent Transaction Output*) se define por el hash de una transacción y el índice de salida (*vout*). También se denomina a veces _outpoint_. En el protocolo RGB, la referencia a un UTXO (a través de una **Seal Definition**) permite la localización del **Owned State**, es decir, la propiedad mantenida en el blockchain.

#### Valencia

Una Valencia es un derecho público que no requiere almacenamiento estatal como tal, pero que puede ser canjeado a través de una **Ampliación Estatal**. Se trata, por tanto, de una forma de posibilidad abierta a todos (o a determinados jugadores), declarada en la lógica del contrato, para llevar a cabo una determinada extensión en una fecha posterior.

#### Transacción con testigos

La Transacción Testigo es la transacción Bitcoin que cierra el Sello de un solo uso en torno a un mensaje que contiene un Compromiso Multiprotocolo (MPC). Esta transacción gasta un UTXO o crea uno, para sellar el compromiso vinculado al protocolo RGB. Actúa como una prueba en la cadena de que el estado se ha establecido en un punto específico en el tiempo.

# Programación en RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implantación de contratos RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

En este capítulo veremos más de cerca cómo se define e implementa un contrato RGB. Veremos cuáles son los componentes de un contrato RGB, cuáles son sus funciones y cómo se construyen.

### Los componentes de un contrato RGB

Hasta ahora, ya hemos hablado de la **Génesis**, que representa el punto de partida de un contrato, y hemos visto cómo encaja con la lógica de una *Operación de contrato* y el estado del protocolo. Sin embargo, la definición completa de un contrato RGB no se limita únicamente a la Génesis: implica tres componentes complementarios que, juntos, forman el corazón de la implementación.

El primer componente se denomina **Esquema**. Se trata de un archivo que describe la estructura fundamental y la lógica empresarial (*lógica empresarial*) del contrato. Especifica los tipos de datos utilizados, las reglas de validación, las operaciones permitidas (por ejemplo, emisión inicial de tokens, transferencias, condiciones especiales, etc.); en resumen, el marco general que dicta cómo funciona el contrato.

El segundo componente es la **Interfaz**. Se centra en cómo los usuarios (y, por extensión, el software de la cartera) interactuarán con este contrato. Describe la semántica, es decir, la representación legible de los distintos campos y acciones. Así, mientras que el Esquema define cómo funciona técnicamente el contrato, la Interfaz define cómo presentar y exponer estas funcionalidades: nombres de métodos, visualización de datos, etc.

El tercer componente es la **implementación de la interfaz**, que complementa a los dos anteriores actuando como una especie de puente entre el esquema y la interfaz. En otras palabras, asocia la semántica expresada por la Interfaz con las reglas subyacentes definidas en el Esquema. Es esta implementación la que gestionará, por ejemplo, la conversión entre un parámetro introducido en el monedero y la estructura binaria impuesta por el protocolo, o la compilación de las reglas de validación en lenguaje máquina.

Esta modularidad es una característica interesante de RGB, ya que permite que diferentes grupos de desarrolladores trabajen por separado en estos aspectos (*Esquema*, *Interfaz*, *Implementación*), siempre que sigan las reglas de consenso del protocolo.

En resumen, cada contrato consta de :


- Genesis**, que es el estado inicial del contrato (y puede asimilarse a una transacción especial que define la primera propiedad de un activo, un derecho o cualquier otro dato parametrizable);
- Esquema**, que describe la lógica empresarial del contrato (tipos de datos, reglas de validación, etc.);
- Interfaz**, que proporciona una capa semántica tanto para los monederos como para los usuarios humanos, aclarando la lectura y ejecución de las transacciones;
- Interfaz de aplicación**, que tiende un puente entre la lógica empresarial y la presentación, para garantizar que la definición del contrato sea coherente con la experiencia del usuario.

![RGB-Bitcoin](assets/fr/070.webp)

Es importante tener en cuenta que para que un monedero pueda gestionar un activo RGB (ya sea un token fungible o un derecho de cualquier tipo), debe tener compilados todos estos elementos: *Schema*, *Interface*, *Interface Implementation* y *Genesis*. Esto se transmite a través de una ***envío de contrato***, es decir, un paquete de datos que contiene todo lo necesario para validar el contrato del lado del cliente.

Para ayudar a aclarar estas nociones, he aquí una tabla resumen que compara los componentes de un contrato RGB con conceptos ya conocidos en la programación orientada a objetos (POO) o en el ecosistema Ethereum:

| Componente de Contrato RGB | Significado | Equivalente OOP | Equivalente Ethereum |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Constructor de clase | Constructor de contrato | Estado inicial del contrato

| Clase | Lógica empresarial contractual

| Semántica contractual | Interfaz (Java) / rasgo (Rust) / protocolo (Swift) | Norma ERC |

| Application Binary Interface (ABI) | Impl (Rust) / Implements (Java) | Mapeo de semántica y lógica

La columna de la izquierda muestra los elementos específicos del protocolo RGB. La columna central muestra la función concreta de cada componente. A continuación, en la columna "Equivalente OOP", encontramos el término equivalente en programación orientada a objetos:


- El **Génesis** desempeña un papel similar al de un *Constructor de clase*: aquí es donde se inicializa el estado del contrato;
- El **Esquema** es la descripción de una clase, es decir, la definición de sus propiedades, métodos y lógica subyacente;
- La **Interfaz** corresponde a *interfaces* (Java), *traits* (Rust) o *protocolos* (Swift): son las definiciones públicas de funciones, eventos, campos... ;
- La **Interface Implementation** corresponde a *Impl* en Rust o *Implements* en Java, donde especificamos cómo el código ejecutará realmente los métodos anunciados en la interfaz.

En el contexto de Ethereum, el Génesis está más cerca del *constructor del contrato*, el Esquema de la definición del contrato, la Interfaz de un estándar como ERC-20 o ERC-721, y la Interfaz de Implementación de la ABI (*Application Binary Interface*), que especifica el formato de las interacciones con el contrato.

La ventaja de la modularidad de RGB reside también en el hecho de que las distintas partes interesadas pueden escribir, por ejemplo, su propia implementación de interfaz, siempre que respeten la lógica del *Esquema* y la semántica de la *Interfaz*. Así, un emisor podría desarrollar un nuevo front-end (Interfaz) más fácil de usar, sin modificar la lógica del contrato, o a la inversa, se podría ampliar el Esquema para añadir funcionalidad, y proporcionar una nueva versión de la Implementación de Interfaz adaptada, mientras que las antiguas implementaciones seguirían siendo válidas para la funcionalidad básica.

Cuando compilamos un nuevo contrato, generamos un Genesis (el primer paso para emitir o distribuir el activo), así como sus componentes (Schema, Interface, Interface Implementation). Después de esto, el contrato es totalmente operativo y puede propagarse a los monederos y a los usuarios. Este método, en el que Génesis se combina con estos tres componentes, garantiza un alto grado de personalización (cada contrato puede tener su propia lógica), descentralización (todo el mundo puede contribuir a un componente determinado) y seguridad (la validación sigue estando estrictamente definida por el protocolo, sin depender de código arbitrario en la cadena, como suele ocurrir en otras blockchains).

Ahora me gustaría examinar más de cerca cada uno de estos componentes: el **Esquema**, la **Interfaz** y la **Implementación de la Interfaz**.

### Esquema

En la sección anterior vimos que, en el ecosistema RGB, un contrato se compone de varios elementos: el Génesis, que establece el estado inicial, y varios otros componentes complementarios. El objetivo del Esquema es describir de forma declarativa toda la lógica de negocio del contrato, es decir, la estructura de datos, los tipos utilizados, las operaciones permitidas y sus condiciones. Es, por tanto, un elemento muy importante para hacer operativo un contrato en el lado del cliente, ya que cada participante (un monedero, por ejemplo) debe comprobar que las transiciones de estado que recibe se ajustan a la lógica definida en el Esquema.

Un esquema puede asimilarse a una "clase" en programación orientada a objetos (POO). En términos generales, sirve como modelo que define los componentes de un contrato, como :


- Los diferentes tipos de Estados propios y asignaciones ;
- Valencias, es decir, derechos especiales que pueden activarse (*redimirse*) para determinadas operaciones;
- Campos de estado global, que describen propiedades globales, públicas y compartidas del contrato;
- La estructura Génesis (la primera operación que activa el contrato) ;
- Las formas permitidas de Transiciones de Estado y Extensiones de Estado, y cómo estas operaciones pueden modificar el ;
- Metadatos asociados a cada operación, para almacenar información temporal o adicional;
- Reglas que determinan cómo pueden evolucionar los datos contractuales internos (por ejemplo, si un campo es mutable o acumulativo);
- Secuencias de operaciones consideradas válidas: por ejemplo, un orden de transiciones que hay que respetar o un conjunto de condiciones lógicas que hay que satisfacer.

![RGB-Bitcoin](assets/fr/071.webp)

Cuando el *emisor* de un activo en RGB publica un contrato, proporciona el Génesis y el Esquema asociado al mismo. Los usuarios o monederos que deseen interactuar con el activo recuperan este Esquema para comprender la lógica que subyace al contrato, y poder verificar posteriormente que las transiciones en las que van a participar son legítimas.

El primer paso, para cualquiera que reciba información sobre un activo RGB (por ejemplo, una transferencia de fichas), es validar esta información con el esquema. Esto implica utilizar la compilación del esquema para :


- Compruebe que los estados propios, las asignaciones y otros elementos están correctamente definidos y que respetan los tipos impuestos (el llamado *sistema de tipos estricto*);
- Comprobar que se cumplen las reglas de transición (scripts de validación). Estos scripts pueden ejecutarse a través de AluVM, que está presente en el lado del cliente y se encarga de validar la coherencia de la lógica empresarial (importe de la transferencia, condiciones especiales, etc.).

En la práctica, Schema no es código ejecutable, como puede verse en blockchains que almacenan código en la cadena (EVM en Ethereum). Por el contrario, RGB separa la lógica de negocio (declarativa) del código ejecutable en la blockchain (que se limita a los anclajes criptográficos). Así, el Esquema determina las reglas, pero la aplicación de estas reglas tiene lugar fuera de la blockchain, en el sitio de cada participante, según el principio de Validación del Lado del Cliente.

Un esquema debe compilarse antes de que pueda ser utilizado por las aplicaciones RGB. Esta compilación produce un archivo binario (por ejemplo `.rgb`) o un archivo binario encriptado (`.rgba`). Cuando el monedero importa este archivo, sabe que :


- Qué aspecto tiene cada tipo de datos (enteros, estructuras, matrices...) gracias al estricto sistema de tipos ;
- Cómo debe estructurarse Génesis (para entender la inicialización de los activos);
- Los distintos tipos de operaciones (transiciones de estado, extensiones de estado) y cómo pueden modificar el estado ;
- Las reglas de scripting (introducidas en el esquema) que el motor AluVM aplicará para comprobar la validez de las operaciones.

Como se ha explicado en capítulos anteriores, el *sistema de tipos estricto* nos proporciona un formato de codificación estable y determinista: todas las variables, ya sean estados propios, estados globales o valencias, se describen con precisión (tamaño, límites inferior y superior si es necesario, tipo con o sin signo, etc.). También es posible definir estructuras anidadas, por ejemplo para dar soporte a casos de uso complejos.

Opcionalmente, el esquema puede hacer referencia a un `SchemaId` raíz, lo que facilita la reutilización de una estructura básica existente (una plantilla). De este modo, se puede hacer evolucionar un contrato o crear variaciones (por ejemplo, un nuevo tipo de ficha) a partir de una plantilla ya probada. Esta modularidad evita la necesidad de recrear contratos enteros y fomenta la estandarización de las mejores prácticas.

Otro punto importante es que la lógica de evolución del estado (transferencias, actualizaciones, etc.) se describe en el Esquema en forma de scripts, reglas y condiciones. Así, si el diseñador del contrato desea autorizar una reemisión o imponer un mecanismo de quema (destrucción de tokens), puede especificar los scripts correspondientes para AluVM en la parte de validación del Esquema.

#### Diferencia con las cadenas de bloques en cadena programables

A diferencia de sistemas como Ethereum, donde el código del contrato inteligente (ejecutable) se escribe en la propia blockchain, RGB almacena el contrato (su lógica) fuera de la cadena, en forma de documento declarativo compilado. Esto implica que :


- No existe una máquina virtual Turing-completa ejecutándose en cada nodo de la red Bitcoin. Las reglas de un contrato RGB no se ejecutan en la blockchain, sino en cada usuario que desea validar un estado;
- Los datos de los contratos no contaminan la blockchain: sólo la evidencia criptográfica (*compromisos*) se incrusta en las transacciones de Bitcoin (a través de `Tapret` u `Opret`);
- El Esquema puede ser actualizado o rechazado (*fast-forward*, *push-back*, etc.), sin requerir una bifurcación en la blockchain de Bitcoin. Los monederos solo tienen que importar el nuevo esquema y adaptarse a los cambios de consenso.

#### Utilización por el emisor y por los usuarios

Cuando un *emisor* crea un activo (por ejemplo, una ficha fungible no inflacionista), prepara :


- Un esquema que describa las normas de emisión, transferencia, etc. ;
- Una Génesis adaptada a este Esquema (con el número total de fichas emitidas, la identidad del propietario inicial, cualquier Valencia especial para la reemisión, etc.).

A continuación, pone a disposición de los usuarios el Esquema compilado (un archivo `.rgb`), para que cualquiera que reciba una transferencia de este token pueda comprobar localmente la coherencia de la operación. Sin este esquema, un usuario no podría interpretar los datos de estado ni comprobar si cumplen las normas del contrato.

De este modo, cuando un nuevo monedero quiere admitir un activo, sólo tiene que integrar el Schema correspondiente. Este mecanismo hace posible añadir compatibilidad a nuevos tipos de activos RGB, sin cambiar invasivamente la base de software del monedero: todo lo que se requiere es importar el binario Schema y entender su estructura.

El Esquema define la lógica de negocio en RGB. Enumera las reglas de evolución de un contrato, la estructura de sus datos (Estados Propios, Estado Global, Valencias) y los scripts de validación asociados (ejecutables por AluVM). Gracias a este documento declarativo, la definición de un contrato (archivo compilado) está claramente separada de la ejecución real de las reglas (del lado del cliente). Este desacoplamiento proporciona a RGB una gran flexibilidad, permitiendo una amplia gama de casos de uso (tokens fungibles, NFT, contratos más sofisticados) al tiempo que evita la complejidad y los defectos típicos de las cadenas de bloques programables.

#### Ejemplo de esquema

Veamos un ejemplo concreto de esquema para un contrato RGB. Se trata de un extracto en Rust del archivo `nia.rs` (iniciales de "*Non-Inflatable Assets*"), que define un modelo para tokens fungibles que no pueden ser reemitidos más allá de su suministro inicial (un activo no inflacionario). Este tipo de token puede considerarse el equivalente, en el universo RGB, del ERC20 en Ethereum, es decir, tokens fungibles que respetan ciertas reglas básicas (por ejemplo, sobre transferencias, inicialización del suministro, etc.).

Antes de entrar en el código, conviene recordar la estructura general de un esquema RGB. Hay una serie de declaraciones que enmarcan :


- Un posible `SchemaId` que indica el uso de otro esquema básico como plantilla;
- Los **Estados globales** y los **Estados propios** (con sus tipos estrictos) ;
- Valencias** (en su caso);
- Las **Operaciones** (Génesis, Transiciones de Estado, Extensiones de Estado) que pueden hacer referencia a estos estados y valencias;
- El **Sistema de Tipos Estrictos** utilizado para describir y validar datos;
- Scripts de validación** (ejecutados a través de AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

El código siguiente muestra la definición completa del esquema Rust. Lo comentaremos parte por parte, siguiendo las anotaciones (1) a (9) a continuación:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Cabecera de función y subesquema**

La función `nia_schema()` devuelve un `SubSchema`, lo que indica que este esquema puede heredar parcialmente de un esquema más genérico. En el ecosistema RGB, esta flexibilidad permite reutilizar ciertos elementos estándar de un esquema maestro, y luego definir reglas específicas para el contrato en cuestión. En este caso, optamos por no permitir la herencia, ya que `subset_of` será `None`.


- (2) - Propiedades generales: ffv, subset_of, type_system**

La propiedad `ffv` corresponde a la versión *fast-forward* del contrato. Un valor de `¡cero!()` aquí indica que estamos en la versión 0 o la versión inicial de este esquema. Si más adelante desea añadir nuevas funcionalidades (nuevo tipo de operación, etc.), puede incrementar esta versión para indicar un cambio de consenso.

La propiedad `subset_of: None` confirma la ausencia de herencia. El campo `type_system` hace referencia al sistema de tipos estricto ya definido en la biblioteca `types`. Esta línea indica que todos los datos utilizados por el contrato utilizan la implementación de serialización estricta proporcionada por la biblioteca en cuestión.


- (3) - Estados globales

En el bloque `global_types` declaramos cuatro elementos. Utilizamos la clave, como `GS_NOMINAL` o `GS_ISSUED_SUPPLY`, para referenciarlos posteriormente:


- gS_NOMINAL" se refiere a un tipo "DivisibleAssetSpec", que describe varios campos de la ficha creada (nombre completo, ticker, precisión...);
- `GS_DATA` representa datos generales, como una cláusula de exención de responsabilidad, metadatos u otro texto;
- gS_TIMESTAMP" se refiere a una fecha de emisión;
- `GS_ISSUED_SUPPLY` establece el suministro total, es decir, el número máximo de fichas que se pueden crear.

La palabra clave `once(...)` significa que cada uno de estos campos sólo puede aparecer una vez.


- (4) - Tipos de propiedad

En `owned_types`, declaramos `OS_ASSET`, que describe un estado fungible. Utilizamos `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, indicando que la cantidad de activos (tokens) se almacena como un entero de 64 bits sin signo. Así, cualquier transacción enviará una cierta cantidad de unidades de este token, que se validará según esta estructura numérica estrictamente tipada.


- (5) - Valencies**

Indicamos `valency_types: none!()`, lo que significa que no hay valencias en este esquema, es decir, ningún derecho especial o extra (como reemisión, quemado condicional, etc.). Si un esquema incluyera alguna, se declararía en esta sección.


- (6) - Génesis: primeras operaciones

Aquí entramos en la parte que declara las Operaciones Contractuales. El Génesis es descrito por :


- La ausencia de `metadatos` (campo `metadatos: Ty::<SemId>::UNIT.id(None)`) ;
- Estados globales que deben estar presentes una vez cada uno (`Once`);
- Una lista de Asignaciones donde `OS_ASSET` debe aparecer `OnceOrMore`. Esto significa que Génesis requiere al menos una asignación `OS_ASSET` (un titular inicial);
- No Valency : `valencias: ¡ninguna!()`.

Así limitamos la definición de la emisión inicial de tokens: debemos declarar el suministro emitido (`GS_ISSUED_SUPPLY`), más al menos un poseedor (un Owned State de tipo `OS_ASSET`).


- (7) - Ampliaciones

El campo `extensions: none!()` indica que en este contrato no está prevista ninguna Extensión de Estado. Esto significa que no hay ninguna operación para redimir un derecho digital (Valency) o para realizar una extensión de estado antes de una Transición. Todo se realiza a través de Génesis o Transiciones de Estado.


- (8) - Transiciones: TS_TRANSFERENCIA

En `transitions`, definimos el tipo de operación `TS_TRANSFER`. Explicamos que :


- No tiene metadatos;
- No modifica el Estado Global (que ya está definido en Génesis);
- Toma uno o más `OS_ASSETs` como entradas. Esto significa que debe gastar Estados Propios existentes;
- Crea (`assignments`) al menos un nuevo `OS_ASSET` (en otras palabras, el destinatario o destinatarios reciben tokens) ;
- No genera ninguna nueva Valencia.

Esto modela el comportamiento de una transferencia básica, que consume tokens en un UTXO, luego crea nuevos Estados Propios a favor de los receptores, y así preserva la igualdad de la cantidad total entre entradas y salidas.


- (9) - Script AluVM y puntos de entrada** (en francés)

Por último, declaramos un script AluVM (`Script::AluVM(AluScript { ... })`). Este script contiene :


- Una o varias bibliotecas externas (`libs`) que se utilizarán durante la validación;
- Puntos de entrada que apuntan a desplazamientos de función en el código AluVM, correspondientes a la validación de la Génesis (`ValidateGenesis`) y de cada Transición declarada (`ValidateTransition(TS_TRANSFER)`).

Este código de validación es responsable de aplicar la lógica de negocio. Por ejemplo, comprobará :


- Que no se supere el `GS_ISSUED_SUPPLY` durante Génesis ;
- Que la suma de `inputs` (tokens gastados) sea igual a la suma de `assignments` (tokens recibidos) para `TS_TRANSFER`.

Si no se respetan estas normas, la transición se considerará inválida.

Este ejemplo de esquema de "*Activo fungible no inflable*" nos permite comprender mejor la estructura de un contrato de token fungible RGB sencillo. Podemos ver claramente la separación entre la descripción de datos (Estados Globales y Propios), la declaración de operaciones (Génesis, Transiciones, Extensiones) y la implementación de la validación (scripts AluVM). Gracias a este modelo, un token se comporta como un token fungible clásico, pero permanece validado en el lado del cliente y no depende de la infraestructura on-chain para ejecutar su código. Sólo los compromisos criptográficos están anclados en la blockchain de Bitcoin.

### Interfaz

La interfaz es la capa destinada a hacer legible y manipulable un contrato, tanto por los usuarios (lectura humana) como por las carteras (lectura informática). Por tanto, la interfaz desempeña un papel comparable al de una interfaz en un lenguaje de programación orientado a objetos (Java, Rust trait, etc.), en el sentido de que expone y aclara la estructura funcional de un contrato, sin revelar necesariamente los detalles internos de la lógica empresarial.

A diferencia de Schema, que es puramente declarativo y se compila en un archivo binario difícil de utilizar tal cual, Interface proporciona las claves de lectura necesarias para :


- Enumere y describa los Estados globales y los Estados propios incluidos en el contrato;
- Acceda a los nombres y valores de cada campo para poder visualizarlos (por ejemplo, para una ficha, averigüe su ticker, su importe máximo, etc.);
- Interpretar y construir Operaciones Contractuales (Génesis, Transición de Estado o Extensión de Estado) asociando datos con nombres comprensibles (por ejemplo, realizar una transferencia especificando claramente "importe" en lugar de un identificador binario).

![RGB-Bitcoin](assets/fr/073.webp)

Gracias a la Interfaz, se puede, por ejemplo, escribir código en un monedero que, en lugar de manipular campos, manipule directamente etiquetas como "número de tokens", "nombre del activo", etc. De esta forma, la gestión de un contrato se vuelve más intuitiva. De este modo, la gestión de un contrato se vuelve más intuitiva.

#### Funcionamiento general

Este método tiene muchas ventajas:


- Normalización:**

El mismo tipo de contrato puede ser soportado por una Interfaz estándar, compartida entre varias implementaciones de monederos. Esto facilita la compatibilidad y la reutilización del código.


- Separación clara entre esquema e interfaz:**

En el diseño RGB, el esquema (lógica de negocio) y la interfaz (presentación y manipulación) son dos entidades independientes. Los desarrolladores que escriben la lógica del contrato pueden concentrarse en el Esquema, sin preocuparse por la ergonomía o la representación de los datos, mientras que otro equipo (o el mismo equipo, pero con un calendario diferente) puede desarrollar la Interfaz.


- Evolución flexible:**

La Interfaz puede modificarse o añadirse después de que el activo haya sido emitido, sin tener que cambiar el propio contrato. Esta es una diferencia importante con respecto a algunos sistemas de contratos inteligentes en cadena, en los que la Interfaz (a menudo mezclada con el código de ejecución) se congela en la blockchain.


- Capacidad multiinterfaz

El mismo contrato podría exponerse a través de diferentes Interfaces adaptadas a distintas necesidades: una Interfaz sencilla para el usuario final, otra más avanzada para el emisor que necesite gestionar operaciones de configuración complejas. El monedero puede entonces elegir qué Interfaz importar, en función de su uso.

![RGB-Bitcoin](assets/fr/074.webp)

En la práctica, cuando el monedero recupera un contrato RGB (a través de un archivo `.rgb` o `.rgba`), también importa la Interfaz asociada, que también se compila. En tiempo de ejecución, el monedero puede, por ejemplo :


- Navegar por la lista de estados y leer sus nombres, para mostrar Ticker, Importe inicial, Fecha de emisión, etc. en la interfaz de usuario, en lugar de un identificador numérico ilegible;
- Construir una operación (como una transferencia) utilizando nombres de parámetros explícitos: en lugar de escribir `asignaciones { OS_ASSET => 1 }`, puede ofrecer al usuario un campo "Importe" en un formulario, y traducir esta información a los campos estrictamente tipados esperados por el contrato.

#### Diferencia con Ethereum y otros sistemas

En Ethereum, la interfaz (descrita a través de la ABI, *Application Binary Interface*) se deriva generalmente del código almacenado en la cadena (el contrato inteligente). Puede resultar costoso o complicado modificar una parte específica de la interfaz sin tocar el propio contrato. Sin embargo, RGB se basa en una lógica totalmente fuera de la cadena, con datos anclados en *compromisos* en Bitcoin. Este diseño hace posible modificar la Interfaz (o su implementación) sin impactar en la seguridad fundamental del contrato, ya que la validación de las reglas de negocio permanece en el Esquema y en el código AluVM referenciado.

#### Compilación de interfaces

Al igual que con Schema, la Interfaz se define en código fuente (a menudo en Rust) y se compila en un archivo `.rgb` o `.rgba`. Este archivo binario contiene toda la información que necesita el monedero para :


- Identificar los campos por su nombre ;
- Vincule cada campo (y su valor) al tipo de sistema estricto definido en el contrato;
- Conocer las diferentes operaciones permitidas y cómo construirlas.

Una vez importada la Interfaz, el monedero puede mostrar correctamente el contrato y proponer interacciones al usuario.

### Interfaces normalizadas por la asociación LNP/BP

En el ecosistema RGB, se utiliza una Interfaz para dar un significado legible y manipulable a los datos y operaciones de un contrato. La Interfaz complementa así al Esquema, que describe internamente la lógica de negocio (tipos estrictos, scripts de validación, etc.). En esta sección, examinaremos las interfaces estándar desarrolladas por la asociación LNP/BP para los tipos de contrato más comunes (fichas fungibles, NFT, etc.).

Como recordatorio, la idea es que cada Interfaz describa cómo mostrar y manipular un contrato en el lado del monedero, nombrando claramente los campos (como `spec`, `ticker`, `issuedSupply`...) y definiendo las posibles operaciones (como `Transfer`, `Burn`, `Rename`...). Varias interfaces ya están operativas, pero habrá más y más en el futuro.

#### Algunas interfaces listas para usar

**RGB20** es la interfaz para activos fungibles, que puede compararse con el estándar ERC20 de Ethereum. Sin embargo, va un paso más allá, ofreciendo una funcionalidad más amplia:


- Por ejemplo, la posibilidad de cambiar el nombre del activo (cambio de *etiqueta* o nombre completo) después de su emisión, o de ajustar su precisión (*división de acciones*);
- También puede describir mecanismos de reemisión secundaria (limitada o ilimitada) y de quema y posterior sustitución, con el fin de autorizar al emisor a destruir y luego volver a crear activos en determinadas condiciones;

Por ejemplo, la Interfaz RGB20 puede vincularse al esquema **Activo no hinchable (NIA)**, que impone un suministro inicial no hinchable, o a otros esquemas más avanzados según las necesidades.

**RGB21** se refiere a los contratos de tipo NFT, o más ampliamente, a cualquier contenido digital único, como la representación de medios digitales (imágenes, música, etc.). Además de describir la emisión y transferencia de un activo único, incluye características como :


- Soporte integrado para la inclusión directa de un archivo (de hasta 16 MB) en el contrato (para recuperación del lado del cliente);
- Posibilidad de que el propietario introduzca un "*grabado*" en el historial para demostrar la propiedad pasada de una NFT.

**RGB25** es un estándar híbrido que combina aspectos fungibles y no fungibles. Está diseñado para activos parcialmente fungibles, como la tokenización inmobiliaria, en la que se desea dividir una propiedad conservando un vínculo a un único activo raíz (en otras palabras, se tienen piezas fungibles de una casa, vinculadas a una casa no fungible). Técnicamente, esta interfaz puede vincularse al esquema **Collectible Fungible Asset* (CFA)**, que tiene en cuenta la noción de división al tiempo que rastrea el activo original.

#### Interfaces en desarrollo

Están previstas otras interfaces para usos más especializados, pero aún no están disponibles:


- RGB22**, dedicado a las identidades digitales, para gestionar identificadores y perfiles en cadena en el ecosistema RGB;
- RGB23**, para el sellado de tiempo avanzado, utilizando algunas de las ideas de *Opentimestamps*, pero con características de trazabilidad;
- RGB24**, que aspira al equivalente de un sistema de nombres de dominio (DNS) descentralizado similar al *Servicio de Nombres de Ethereum* ;
- RGB26**, diseñado para gestionar DAOs (*Organización Autónoma Descentralizada*) en un formato más complejo (gobierno, votación, etc.);
- RGB30**, muy similar a RGB20, pero con la particularidad de tener en cuenta la emisión inicial descentralizada y de utilizar extensiones estatales. Se utilizaría para activos cuya reemisión es gestionada por varias entidades, o sujeta a condiciones más finas.

Por supuesto, dependiendo de la fecha en la que consulte este curso, es posible que estas interfaces ya estén operativas y accesibles.

#### Ejemplo de interfaz

Este fragmento de código Rust muestra una interfaz [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (activo fungible). Este código está tomado del archivo `rgb20.rs` de la biblioteca estándar RGB. Echémosle un vistazo para entender la estructura de una Interfaz y cómo proporciona un puente entre, por un lado, la lógica de negocio (definida en el Esquema) y, por otro, las funcionalidades expuestas a los monederos y usuarios.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

En esta interfaz, notamos similitudes con la estructura del Esquema: encontramos una declaración de Estado Global, Estados Propios, Operaciones de Contrato (Génesis y Transiciones), así como manejo de errores. Pero la Interfaz se centra en la presentación y manipulación de estos elementos para un monedero o cualquier otra aplicación.

La diferencia con Schema radica en la naturaleza de los tipos. Schema utiliza tipos estrictos (como `FungibleType::Unsigned64Bit`) e identificadores más técnicos. La interfaz utiliza nombres de campo, macros (`fname!()`, `tn!()`) y referencias a clases de argumentos (`ArgSpec`, `OwnedIface::Rights`...). El objetivo es facilitar la comprensión funcional y la organización de los elementos para la cartera.

Además, la Interfaz puede introducir funcionalidades adicionales al Esquema básico (por ejemplo, la gestión de un derecho `burnEpoch`), siempre que esto siga siendo coherente con la lógica final validada del lado del cliente. La sección "script" de AluVM en el Esquema garantizará la validez criptográfica, mientras que la Interfaz describe cómo el usuario (o el monedero) interactúa con estos estados y transiciones.

#### Estado global y asignaciones

En la sección `global_state`, encontramos campos como `spec` (descripción del activo), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Son campos que el monedero puede leer y presentar. Por ejemplo:


- `spec` mostrará la configuración del token;
- `issuedSupply` o `burnedSupply` nos dan el número total de fichas emitidas o quemadas, etc.

En la sección `asignaciones`, definimos varios roles o derechos. Por ejemplo:


- `assetOwner` corresponde a la tenencia de fichas (es el fungible *Owned State*) ;
- `burnRight` corresponde a la capacidad de quemar fichas ;
- updateRight` corresponde al derecho a renombrar el activo.

La palabra clave `public` o `private` (por ejemplo, `AssignIface::public(...)`) indica si estos estados son visibles (`public`) o confidenciales (`private`). En cuanto a `Req::NoneOrMore`, `Req::Optional`, indican la ocurrencia esperada.

#### Génesis y transiciones

La parte "génesis" describe cómo se inicializa el activo:


- Los campos `spec`, `data`, `created`, `issuedSupply` son obligatorios (`ArgSpec::required()`) ;
- Asignaciones como `assetOwner` pueden estar presentes en múltiples copias (`ArgSpec::many()`), permitiendo que los tokens sean distribuidos a múltiples poseedores iniciales;
- Campos como `inflationAllowance` o `burnEpoch` pueden (o no) incluirse en Genesis.

A continuación, para cada Transición (`Transferir`, `Emitir`, `Quemar`...), la Interfaz define qué campos espera la operación como entrada, qué campos producirá la operación como salida y cualquier error que pueda producirse. Por ejemplo:

**Transición :**


- Entradas : `previous` → debe ser un `assetOwner` ;
- Asignaciones : `beneficiario` → será un nuevo `propietario de activos` ;
- Error: `NON_EQUAL_AMOUNTS` (el monedero podrá así manejar casos en los que la suma de entrada no se corresponda con la suma de salida).

**Transición `Issue` :**


- Opcional (`optional: true`), ya que la emisión adicional no se activa necesariamente;
- Entradas: `used` → an `inflationAllowance`, es decir, permiso para añadir más tokens ;
- Asignaciones: `beneficiario` (nuevos tokens recibidos) y `futuro` (`inflationAllowance` restante) ;
- Posibles errores: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.

**Transición de quemado :**


- Entradas : `used` → a `burnRight` ;
- Globales : `burnedSupply` requerido ;
- Asignaciones: `future` → una posible continuación del `burnRight` si no hemos quemado todo ;
- Errores: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Por tanto, cada operación se describe de forma legible para un monedero. Esto permite mostrar una interfaz gráfica en la que el usuario puede ver claramente: "Tiene derecho a quemar. ¿Desea quemar una determinada cantidad? El código sabe que debe rellenar un campo `burnedSupply` y comprobar que el `burnRight` es válido.

En resumen, es importante tener en cuenta que una Interfaz, por completa que sea, no define por sí misma la lógica interna del contrato. El núcleo del trabajo lo realiza el **Esquema**, que incluye los tipos estrictos, la estructura de Génesis, las transiciones, etcétera. La Interfaz simplemente expone estos elementos de una forma más intuitiva y nombrada, para su uso en una aplicación.

Gracias a la modularidad de RGB, la interfaz puede actualizarse (por ejemplo, añadiendo una transición `Rename`, corrigiendo la visualización de un campo, etc.) sin tener que reescribir todo el contrato. Los usuarios de esta interfaz pueden beneficiarse inmediatamente de estas mejoras, tan pronto como actualicen el archivo `.rgb` o `.rgba`.

Pero una vez declarada una interfaz, hay que vincularla al esquema correspondiente. Esto se hace a través de la ***Interface Implementation***, que especifica cómo asignar cada campo con nombre (como `fname!("assetOwner")`) al ID estricto (como `OS_ASSET`) definido en el Esquema. Esto asegura, por ejemplo, que cuando un monedero manipula un campo `burnRight`, este es el estado que, en el Esquema, describe la capacidad de quemar tokens.

### Aplicación de la interfaz

En la arquitectura RGB, hemos visto que cada componente (esquema, interfaz, etc.) puede desarrollarse y compilarse de forma independiente. Sin embargo, todavía hay un elemento indispensable que une estos diferentes bloques de construcción: la ***Implementación de la Interfaz***. Esto es lo que mapea explícitamente los identificadores o campos definidos en el Esquema (en el lado de la lógica de negocio) a los nombres declarados en la Interfaz (en el lado de la presentación y la interacción con el usuario). Así, cuando un monedero carga un contrato, puede entender exactamente qué campo corresponde a qué, y cómo una operación nombrada en la Interfaz se relaciona con la lógica del Esquema.

Un punto importante es que la implementación de la interfaz no pretende necesariamente exponer todas las funcionalidades del esquema, ni todos los campos de la interfaz: puede limitarse a un subconjunto. En la práctica, esto permite restringir o filtrar determinados aspectos del esquema. Por ejemplo, se puede tener un esquema con cuatro tipos de operación, pero una interfaz de implementación que sólo asigne dos de ellos en un contexto determinado. A la inversa, si una Interfaz propone puntos finales adicionales, podemos optar por no implementarlos aquí.

He aquí un ejemplo clásico de implementación de interfaces, en el que asociamos un esquema *Non-Inflatable Asset* (NIA) con la interfaz RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

En esta interfaz de aplicación :


- Hacemos referencia explícita al esquema, mediante `nia_schema()`, y a la interfaz, mediante `Rgb20::iface()`. Las llamadas `schema.schema_id()` y `iface.iface_id()` se usan para anclar la implementación de la interfaz en la compilación (esto asocia los identificadores criptográficos de estos dos componentes);
- Se establece una correspondencia entre los elementos del esquema y los elementos de la interfaz. Por ejemplo, el campo `GS_NOMINAL` del Esquema se vincula a la cadena `"spec"` en la Interfaz (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Hacemos lo mismo para las operaciones, como `TS_TRANSFER`, que enlazamos a `"Transfer"` en la Interfaz... ;
- Podemos ver que no hay valencias (`valencies: none!()`) ni extensiones (`extensions: none!()`), lo que refleja el hecho de que este contrato NIA no utiliza estas características.

El resultado tras la compilación es un archivo `.rgb` o `.rgba` independiente, que se importará en el monedero además del Esquema y la Interfaz. Así, el software sabe cómo conectar concretamente este contrato NIA (cuya lógica está descrita por su Esquema) con la Interfaz "RGB20" (que proporciona nombres humanos y un modo de interacción para tokens fungibles), aplicando esta Implementación de Interfaz como pasarela entre ambos.

#### ¿Por qué separar la implementación de interfaces?

La separación aumenta la flexibilidad. Un único esquema puede tener varias implementaciones de interfaz distintas, cada una de ellas con un conjunto diferente de funcionalidades. Además, la propia implementación de la interfaz puede evolucionar o reescribirse sin necesidad de modificar ni el esquema ni la interfaz. De este modo se mantiene el principio de modularidad de RGB: cada componente (esquema, interfaz, implementación de interfaz) puede versionarse y actualizarse independientemente, siempre que se respeten las normas de compatibilidad impuestas por el protocolo (mismos identificadores, coherencia de tipos, etc.).

En el uso concreto, cuando el monedero carga un contrato, debe :


- Cargar el **Esquema** compilado (para conocer la estructura de la lógica de negocio) ;
- Cargar **Interfaz** compilada (para entender nombres y operaciones del lado del usuario) ;
- Cargar **Implementación de Interfaz** compilada (para vincular la lógica del Esquema a los nombres de Interfaz, operación por operación, campo por campo).

Esta arquitectura modular hace posibles escenarios de uso como :


- Limitar ciertas operaciones a determinados usuarios: ofrecer una interfaz de aplicación parcial que sólo dé acceso a las transferencias básicas, sin ofrecer funciones de grabación o actualización, por ejemplo;
- Presentación de cambios: diseñar una implementación de interfaz que cambie el nombre de un campo de la interfaz o lo asigne de forma diferente, sin alterar la base del contrato;
- Soporta múltiples esquemas: un monedero puede cargar múltiples Implementaciones de Interfaz para el mismo tipo de Interfaz, para manejar diferentes esquemas (diferentes lógicas de token), siempre que su estructura sea compatible.

En el próximo capítulo veremos cómo funciona una transferencia de contrato y cómo se generan las facturas RGB.

## Transferencias contractuales

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

En este capítulo, vamos a analizar el proceso de transferencia de un contrato en el ecosistema RGB. Para ilustrarlo, veremos a Alice y Bob, nuestros protagonistas habituales, que desean intercambiar un activo RGB. También mostraremos algunos extractos de comandos de la herramienta de línea de comandos `rgb`, para ver cómo funciona en la práctica.

### Comprender la transferencia de contratos RGB

Veamos un ejemplo de transferencia entre Alice y Bob. En este ejemplo, asumimos que Bob está empezando a usar RGB, mientras que Alice ya tiene activos RGB en su cartera. Veremos cómo Bob configura su entorno, importa el contrato relevante, después solicita una transferencia a Alice, y finalmente cómo Alice lleva a cabo la transacción real en la blockchain de Bitcoin.

#### 1) Instalación de la cartera RGB

En primer lugar, Bob necesita instalar un monedero RGB, es decir, un software compatible con el protocolo. Al principio, éste no contiene ningún contrato. Bob también necesitará :


- Un monedero Bitcoin para gestionar tus UTXOs;
- Una conexión a un nodo Bitcoin (o a un servidor Electrum), para que pueda identificar sus UTXOs y propagar sus transacciones en la red.

Como recordatorio, los **Estados Propios** en RGB se refieren a UTXOs de Bitcoin. Por tanto, siempre debemos poder gestionar y gastar UTXOs en una transacción Bitcoin que incorpore compromisos criptográficos (`Tapret` u `Opret`) que apunten a datos RGB.

#### 2) Adquisición de información contractual

Bob necesita entonces recuperar los datos del contrato que le interesan. Estos datos pueden circular por cualquier canal: página web, correo electrónico, aplicación de mensajería... En la práctica, se agrupan en una ***consigna***, es decir, un pequeño paquete de datos que contiene :


- La **Génesis**, que define el estado inicial del contrato;
- El **Esquema**, que describe la lógica de negocio (tipos estrictos, scripts de validación, etc.);
- La **Interfaz**, que define la capa de presentación (nombres de campos, operaciones accesibles);
- La **implementación de la interfaz**, que vincula concretamente el esquema con la interfaz.

![RGB-Bitcoin](assets/fr/075.webp)

El tamaño total suele ser del orden de unos pocos kilobytes, ya que cada componente suele pesar menos de 200 bytes. También puede ser posible difundir esta remesa en Base58, a través de canales resistentes a la censura (como Nostr o a través de Lightning Network, por ejemplo), o en forma de código QR.

#### 3) Importación y validación de contratos

Una vez que Bob ha recibido el envío, lo importa a su cartera RGB. Esto hará que :


- Compruebe que el Génesis y el Esquema son válidos;
- Interfaz de carga e implementación de la interfaz ;
- Actualiza tu almacén de datos del lado del cliente.

Ahora Bob puede ver el activo en su cartera (aunque aún no sea de su propiedad) y comprender qué campos están disponibles, qué operaciones son posibles... A continuación, debe ponerse en contacto con la persona que posee el activo que desea transferir. En nuestro ejemplo, se trata de Alice.

El proceso de descubrir quién posee un determinado activo RGB es similar al de encontrar un pagador Bitcoin. Los detalles de esta conexión dependen del uso (mercados, canales de chat privados, facturación, venta de bienes y servicios, salario...).

#### 4) Emitir una factura

Para iniciar la transferencia de un activo RGB, Bob debe emitir primero una factura. Esta factura se utiliza para :


- Indique a Alice el tipo de operación a realizar (por ejemplo, una `Transferencia` desde una interfaz RGB20);
- Proporcionar a Alice la *definición de sello* de Bob (es decir, el UTXO donde desea recibir el activo);
- Especifique la cantidad de principio activo necesaria (por ejemplo, 100 unidades).

Bob utiliza la herramienta `rgb` en la línea de comandos. Supongamos que quiere 100 unidades de un token cuyo `ContractId` es conocido, quiere confiar en `Tapret`, y especifica su UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Al final de este capítulo veremos con más detalle la estructura de las facturas RGB.

#### 5) Transmisión de facturas

La factura generada (por ejemplo, como URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) contiene toda la información que Alice necesita para preparar la transferencia. Al igual que el envío, puede codificarse de forma compacta (Base58 u otro formato) y enviarse a través de una aplicación de mensajería, correo electrónico, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Preparación de la transacción por parte de Alice

Alice recibe la factura de Bob. En su monedero RGB, tiene un alijo que contiene el activo a transferir. Para gastar el UTXO que contiene el activo, primero debe generar una PSBT (*Transacción Bitcoin Parcialmente Firmada*), es decir, una transacción Bitcoin incompleta, utilizando el UTXO que tiene:

```bash
alice$ wallet construct tx.psbt
```

Esta transacción básica (sin firmar por el momento) se utilizará para anclar el compromiso criptográfico vinculado a la transferencia a Bob. El UTXO de Alice será así gastado, y en la salida, colocaremos el compromiso `Tapret` u `Opret` para Bob.

#### 7) Generación de la remesa de transferencia

A continuación, Alice construye la consigna ***terminal*** (a veces llamada "consigna de transferencia") mediante el comando :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Este nuevo archivo `consignment.rgb` contiene :


- El historial completo de Transiciones de Estado necesarias para validar el activo hasta el momento actual (desde Génesis);
- La nueva Transición de Estado que transfiere activos de Alice a Bob, de acuerdo con la factura que Bob ha emitido;
- La transacción Bitcoin incompleta (*transacción testigo*) (`tx.psbt`), que gasta el Sello de un solo uso de Alice, modificada para incluir el compromiso criptográfico con Bob.

En esta fase, la transacción aún no se difunde en la red Bitcoin. La consignación es mayor que una consignación básica, ya que incluye todo el historial (*cadena de prueba*) para demostrar la legitimidad del activo.

#### 8) Bob comprueba y acepta el envío

Alice transmite este **envío terminal** a Bob. Bob entonces :


- Compruebe la validez de la transición de estado (asegúrese de que el historial es coherente, de que se respetan las normas contractuales, etc.);
- Añádelo a tu alijo local;
- Posiblemente genere una firma (`sig:...`) en el envío, para demostrar que ha sido examinado y aprobado (a veces llamada "*ficha de pago*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Opción: Bob envía la confirmación a Alice (*factura de pago*)

Si Bob lo desea, puede enviar esta firma a Alice. Esto indica:


- Que reconozca la transición como válida;
- Que está de acuerdo con que se difunda la transacción de Bitcoin.

Esto no es obligatorio, pero puede ofrecer a Alice la seguridad de que no habrá disputas posteriores sobre la transferencia.

#### 10) Alice firma y publica la transacción

Alice puede entonces :


- Comprobar la firma de Bob (`rgb check <sig>`) ;
- Firmar la *transacción testigo* que sigue siendo un PSBT (`firma de cartera`) ;
- Publica la transacción testigo en la red Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Una vez confirmada, esta transacción marca la conclusión de la transferencia. Bob se convierte en el nuevo propietario del activo: ahora tiene un Estado de Propiedad que apunta al UTXO que controla, demostrado por la presencia del compromiso en la transacción.

A modo de resumen, he aquí el proceso completo de transferencia:

![RGB-Bitcoin](assets/fr/079.webp)

### Ventajas de las transferencias RGB


- Confidencialidad** :

Sólo Alice y Bob tienen acceso a todos los datos de Transición de Estado. Intercambian esta información fuera de la blockchain, mediante consignaciones. Los compromisos criptográficos en la transacción Bitcoin no revelan el tipo de activo ni la cantidad, lo que garantiza una confidencialidad mucho mayor que otros sistemas de tokens en cadena.


- Validación por el cliente** :

Bob puede comprobar la consistencia de la transferencia comparando la *consignación* con los *anclajes* en la blockchain de Bitcoin. No necesita la validación de terceros. Alice no tiene que publicar el historial completo en la blockchain, lo que reduce la carga del protocolo base y mejora la confidencialidad.


- Atomicidad simplificada** :

Los intercambios complejos (swaps atómicos entre BTC y un activo RGB, por ejemplo) pueden realizarse en una sola transacción, evitando la necesidad de scripts HTLC o PTLC. Si el acuerdo no se emite, todo el mundo puede reutilizar sus UTXO de otras formas.

### Diagrama resumido de transferencia

Antes de examinar las facturas con más detalle, he aquí un diagrama resumido del flujo global de una transferencia RGB:


- Bob instala una cartera RGB y obtiene la consignación inicial del contrato;
- Bob emite una factura mencionando el UTXO donde recibir el activo;
- Alice recibe la factura, construye el PSBT y genera la remesa terminal;
- Bob lo acepta, lo comprueba, añade los datos a su alijo y firma (*ficha de pago*) si es necesario;
- Alice publica la transacción en la red Bitcoin;
- La confirmación de la transacción oficializa la transferencia.

![RGB-Bitcoin](assets/fr/080.webp)

La transferencia ilustra toda la potencia y flexibilidad del protocolo RGB: un intercambio privado, validado en el lado del cliente, anclado de forma mínima y discreta en la blockchain de Bitcoin, y conservando lo mejor de la seguridad del protocolo (sin riesgo de doble gasto). Esto convierte a RGB en un ecosistema prometedor para transferencias de valor más confidenciales y escalables que las blockchains programables en cadena.

### Facturas RGB

En esta sección, explicaremos en detalle cómo funcionan las **facturas** en el ecosistema RGB y cómo permiten realizar operaciones (en particular transferencias) con un contrato. En primer lugar, veremos los identificadores utilizados, luego cómo se codifican y, por último, la estructura de una factura expresada como URL (un formato bastante práctico para su uso en monederos).

#### Identificadores y codificación

Se define un identificador único para cada uno de los siguientes elementos:


- Un contrato RGB;
- Su esquema (lógica empresarial) ;
- Su interfaz y la implementación de la interfaz ;
- Sus activos (tokens, NFT, etc.),

Esta unicidad es muy importante, ya que cada componente del sistema debe ser distinguible. Por ejemplo, un contrato X no debe confundirse con otro contrato Y, y dos interfaces diferentes (RGB20 frente a RGB21, por ejemplo) deben tener identificadores distintos.

Para que estos identificadores sean a la vez eficientes (tamaño reducido) y legibles, utilizamos :


- Codificación Base58, que evita el uso de caracteres confusos (por ejemplo, `0` y la letra `O`) y proporciona cadenas relativamente cortas;
- Prefijo que indica la naturaleza del identificador, normalmente en forma de `rgb:` o un URN similar.

Por ejemplo, un `ContractId` podría representarse con algo como :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

El prefijo `rgb:` confirma que se trata de un identificador RGB, y no de un enlace HTTP u otro protocolo. Gracias a este prefijo, los monederos pueden interpretar la cadena correctamente.

#### Segmentación de identificadores

Los identificadores RGB suelen ser bastante largos, ya que la seguridad (criptográfica) subyacente puede requerir campos de 256 bits o más. Para facilitar la lectura y verificación por parte de los humanos, *cortamos* estas cadenas en varios bloques separados por un guión (`-`). Así, en lugar de tener una cadena de caracteres larga e ininterrumpida, la dividimos en bloques más cortos. Esta práctica es habitual en el caso de las tarjetas de crédito o los números de teléfono, y también se aplica aquí para facilitar la verificación. Así, por ejemplo, se puede decir a un usuario o socio: "*Por favor, compruebe que el tercer bloque es `9GEgnyMj7`*", en lugar de tener que compararlo todo de una vez. El último bloque suele utilizarse como **checksum**, para disponer de un sistema de detección de errores o erratas.

Como ejemplo, un `ContractId` en base58 codificado y segmentado podría ser :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Cada uno de los guiones divide la cadena en secciones. Esto no afecta a la semántica del código, sólo a su presentación.

#### Utilización de URL para las facturas

Una factura RGB se presenta como una URL. Esto significa que puede pulsarse o escanearse (como un código QR), y un monedero puede interpretarla directamente para realizar una transacción. Esta sencillez de interacción difiere de otros sistemas en los que hay que copiar y pegar varios datos en distintos campos del software.

Una factura de una ficha fungible (por ejemplo, una ficha RGB20) podría tener este aspecto:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Analicemos esta URL:


- `rgb:`** (prefijo): indica un enlace que invoca el protocolo RGB (análogo a `http:` o `bitcoin:` en otros contextos);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: representa el `ContractId` del token que desea manipular;
- `/RGB20/100`**: indica que se utiliza la interfaz `RGB20` y que se solicitan 100 unidades del activo. La sintaxis es: `/Interfaz/cantidad` ;
- `+utxob:`**: especifica que se añada información sobre el UTXO receptor (o, más concretamente, la definición del Sello de un solo uso);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: este es el UTXO *enmascarado* (o definición del sello). En otras palabras, Bob ha enmascarado su UTXO exacto, por lo que el remitente (Alice) no sabe cuál es la dirección exacta. Ella solo sabe que hay un sello valido refiriendose a un UTXO controlado por Bob.

El hecho de que todo quepa en una única URL facilita la vida al usuario: un simple clic o escaneado en el monedero, y la operación está lista para ejecutarse.

Se podrían imaginar sistemas en los que se utilizara un simple ticker (por ejemplo, `USDT`) en lugar del `ContractId`. Sin embargo, esto plantearía importantes problemas de confianza y seguridad: un ticker no es una referencia única (varios contratos podrían reclamar llamarse `USDT`). Con RGB, queremos un identificador criptográfico único e inequívoco. De ahí la adopción de la cadena de 256 bits, codificada en base58 y segmentada. El usuario sabe que está manipulando precisamente el contrato cuyo ID es `2WBcas9-yjz...` y no cualquier otro.

#### Parámetros URL adicionales

También puede añadir parámetros adicionales a la URL, del mismo modo que con HTTP, como :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: representa, por ejemplo, una firma asociada a la factura, que algunos monederos pueden verificar;
- Si un monedero no gestiona esta firma, simplemente ignora este parámetro.

Tomemos el caso de un NFT a través de la interfaz RGB21. Por ejemplo, podríamos tener :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Aquí vemos :


- `rgb:`**: Prefijo URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: ID del contrato (NFT) ;
- rGB21**: interfaz para activos no fungibles (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: una referencia explícita a la parte única del NFT, por ejemplo un hash del blob de datos (medios, metadatos...) ;
- `+utxob:egXsFnw-...`**: la definición del sello.

La idea es la misma: transmitir un enlace único que el monedero pueda interpretar, identificando claramente el activo único que se va a transferir.

#### Otras operaciones vía URL

Las URL RGB no sólo se utilizan para solicitar una transferencia. También pueden codificar operaciones más avanzadas, como la emisión de nuevos tokens (*issuance*). Por ejemplo:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Aquí encontramos :


- `rgb:` : protocolo ;
- `2WBcas9-...`: Contrato ID ;
- `/RGB20/issue/100000`: indica que desea invocar la transición "*Issue*" para crear 100.000 fichas adicionales;
- `+utxob:`: la definición del sello.

Por ejemplo, la cartera podría decir: "Me han pedido que realice una operación de `emisión` desde la interfaz `RGB20`, en tal y tal contrato, por 100.000 unidades, en beneficio de tal y tal Sello de un solo uso*"

Ahora que ya hemos visto los principales elementos de la programación RGB, en el siguiente capítulo te explicaré cómo redactar un contrato RGB.

## Redacción de contratos inteligentes

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

En este capítulo, tomaremos un enfoque paso a paso para escribir un contrato, utilizando la herramienta de línea de comandos `rgb`. El objetivo es mostrar cómo instalar y manipular la CLI, compilar un **Esquema**, importar la **Interfaz** y la **Implementación de la Interfaz**, y luego emitir (*emitir*) un activo. También veremos la lógica subyacente, incluyendo la compilación y la validación del estado. Al final de este capítulo, deberías ser capaz de reproducir el proceso y crear tus propios contratos RGB.

Como recordatorio, la lógica interna de RGB se basa en bibliotecas de Rust que ustedes, como desarrolladores, pueden importar a sus proyectos para gestionar la parte de validación del lado del cliente. Además, el equipo de la Asociación LNP/BP está trabajando en bindings para otros lenguajes, pero aún no se ha finalizado. Además, otras entidades como Bitfinex están desarrollando sus propias pilas de integración (hablaremos de ellas en los 2 últimos capítulos del curso). Por el momento, por lo tanto, la CLI `rgb` es la referencia oficial, incluso si sigue estando relativamente sin pulir.

### Instalación y presentación de la herramienta rgb

El comando principal se llama simplemente `rgb`. Está diseñado para recordar a `git`, con un conjunto de subcomandos para manipular contratos, invocarlos, emitir activos, etc. Bitcoin Wallet no está integrado actualmente, pero lo estará en una versión inminente (0.11). Esta próxima versión permitirá a los usuarios crear y gestionar sus monederos (a través de descriptores) directamente desde `rgb`, incluyendo la generación de PSBT, compatibilidad con hardware externo (por ejemplo, un monedero hardware) para firmar, e interoperabilidad con software como Sparrow. Esto simplificará todo el escenario de emisión y transferencia de activos.

#### Instalación a través de Cargo

Instalamos la herramienta en Rust con :

```bash
cargo install rgb-contracts --all-features
```

(Nota: el crate se llama `rgb-contracts`, y el comando instalado se llamará `rgb`. Si ya existía un crate llamado `rgb`, podría haber habido una colisión, de ahí el nombre)

La instalación compila un gran número de dependencias (por ejemplo, análisis sintáctico de comandos, integración de Electrum, gestión de pruebas de conocimiento-cero, etc.).

Una vez finalizada la instalación, el archivo :

```bash
rgb
```

Al ejecutar `rgb` (sin argumentos) aparece una lista de subcomandos disponibles, como `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. Puede cambiar el directorio de almacenamiento local (un alijo que contiene todos los registros, esquemas e implementaciones), elegir la red (testnet, mainnet) o configurar su servidor Electrum.

![RGB-Bitcoin](assets/fr/081.webp)

#### Primera visión general de los controles

Cuando ejecutes el siguiente comando, verás que ya viene integrada por defecto una interfaz `RGB20`:

```bash
rgb interfaces
```

Si esta interfaz no está integrada, clone el archivo :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compílalo:

```bash
cargo run
```

A continuación, importe la interfaz que desee:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Por otro lado, se nos dice que aún no se ha importado ningún esquema al programa. Tampoco hay ningún contrato en el almacén. Para verlo, ejecute el comando :

```bash
rgb schemata
```

A continuación, puede clonar el repositorio para recuperar determinados esquemas:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Este repositorio contiene, en su directorio `src/`, varios archivos Rust (por ejemplo `nia.rs`) que definen esquemas (NIA para "*Activo No Inflable*", UDA para "*Activo Digital Único*", etc.). Para compilar, puede ejecutar :

```bash
cd rgb-schemata
cargo run
```

Esto genera varios archivos `.rgb` y `.rgba` correspondientes a los esquemas compilados. Por ejemplo, encontrarás `NonInflatableAsset.rgb`.

#### Importación de esquemas e interfaces

Ahora puede importar el esquema en `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Esto lo añade al almacén local. Si ejecutamos el siguiente comando, veremos que ahora aparece el esquema:

```bash
rgb schemata
```

### Creación de contratos (emisión)

Existen dos enfoques para crear un nuevo activo:


- O bien utilizamos un script o código en Rust que construye un Contrato rellenando los campos del esquema (estado global, Estados Propios, etc.) y produce un archivo `.rgb` o `.rgba`;
- O utilice directamente el subcomando `issue`, con un archivo YAML (o TOML) que describa las propiedades del token.

Puedes encontrar ejemplos en Rust en la carpeta `examples`, que ilustran cómo se construye un `ContractBuilder`, se rellena el `global state` (nombre del activo, ticker, suministro, fecha, etc.), se define el Owned State (a qué UTXO está asignado), y luego se compila todo esto en una *contratación de consignación* que puedes exportar, validar e importar a un alijo.

La otra forma es editar manualmente un archivo YAML para personalizar el `ticker`, el `name`, el `supply`, etc. Supongamos que el archivo se llama `RGB20-demo.yaml`. Puede especificar :


- `spec`: ticker, nombre, precisión ;
- `terms`: un campo para avisos legales ;
- `issuedSupply` : la cantidad de fichas emitidas ;
- `assignments`: indica el precinto de un solo uso (*definición del precinto*) y la cantidad desbloqueada.

He aquí un ejemplo de archivo YAML a crear:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

A continuación, basta con ejecutar el comando :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

En mi caso, el identificador único del esquema (que debe ir entre comillas simples) es `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` y no he puesto ningún emisor. Así que mi orden es :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Si no conoce el ID del esquema, ejecute el comando :

```bash
rgb schemata
```

La CLI responde que se ha emitido un nuevo contrato y se ha añadido al alijo. Si tecleamos el siguiente comando, veremos que ahora hay un contrato adicional, correspondiente al que se acaba de emitir:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

A continuación, el siguiente comando muestra los estados globales (nombre, ticker, suministro...) y la lista de estados propios, es decir, asignaciones (por ejemplo, 1 millón de fichas `PBN` definidas en UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Exportación, importación y validación

Para compartir este contrato con otros usuarios, puede exportarse desde el alijo a un archivo :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

El archivo `myContractPBN.rgb` puede pasarse a otro usuario, que puede añadirlo a su alijo con el comando :

```bash
rgb import myContractPBN.rgb
```

En la importación, si se trata de un simple *envío de contrato*, obtendremos un mensaje "`Importing consignment rgb`". Si se trata de un *envío de transición de estado* más grande, el comando será diferente (`rgb accept`).

Para garantizar la validez, también puede utilizar la función de validación local. Por ejemplo, puede ejecutar :

```bash
rgb validate myContract.rgb
```

#### Uso, verificación y visualización del alijo

Como recordatorio, el alijo es un inventario local de esquemas, interfaces, implementaciones y contratos (Génesis + transiciones). Cada vez que ejecutas "importar", añades un elemento al alijo. Este alijo puede verse en detalle con el comando :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Esto generará una carpeta con los detalles de todo el alijo.

### Transferencia y PSBT

Para realizar una transferencia, necesitará manipular un monedero Bitcoin local para gestionar los compromisos `Tapret` u `Opret`.

#### Generar una factura

En la mayoría de los casos, la interacción entre los participantes en un contrato (por ejemplo, Alice y Bob) tiene lugar a través de la generación de una factura. Si Alice quiere que Bob ejecute algo (una transferencia de tokens, una reemisión, una acción en un DAO, etc.), Alice crea una factura detallando sus instrucciones a Bob. Así tenemos :


- Alice** (el emisor de la factura) ;
- Bob** (que recibe y ejecuta la factura).

A diferencia de otros ecosistemas, una factura RGB no se limita a la noción de pago. Puede incluir cualquier solicitud vinculada al contrato: revocar una clave, votar, crear un grabado (*grabado*) en una NFT, etc. La operación correspondiente puede describirse en la interfaz del contrato. La operación correspondiente puede describirse en la interfaz del contrato.

El siguiente comando genera una factura RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Con :


- `$CONTRACT`: Identificador del contrato (*ContractId*) ;
- `$INTERFACE`: la interfaz que debe utilizarse (por ejemplo, `RGB20`) ;
- `$ACTION`: el nombre de la operación especificada en la interfaz (para una simple transferencia de token fungible, podría ser "Transfer"). Si la interfaz ya proporciona una acción por defecto, no es necesario volver a introducirla aquí;
- `$STATE`: los datos de estado que se van a transferir (por ejemplo, una cantidad de tokens si se transfiere un token fungible);
- `$SEAL`: el sello de un solo uso del beneficiario (Alice), es decir, una referencia explícita a un UTXO. Bob utilizará esta información para construir la transacción testigo, y la salida correspondiente pertenecerá entonces a Alice (en forma *de UTXO cegado* o sin cifrar).

Por ejemplo, con los siguientes comandos

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

La CLI generará una factura como :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Puede transmitirse a Bob a través de cualquier canal (texto, código QR, etc.).

#### Realizar una transferencia

Para transferir desde esta factura :


- Bob (que tiene los tokens en su alijo) tiene un monedero Bitcoin. Necesita preparar una transacción Bitcoin (en forma de PSBT, por ejemplo `tx.psbt`) que gaste los UTXOs donde se encuentran los tokens RGB necesarios, más un UTXO para la moneda (intercambio) ;
- Bob ejecuta el siguiente comando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Esto genera un archivo `consignment.rgb` que contiene :
 - El historial de transición prueba a Alice que las fichas son auténticas;
 - La nueva transición que transfiere fichas al Sello de un solo uso de Alice ;
 - Una transacción testigo (sin firma).
- Bob envía este archivo `consignment.rgb` a Alice (por correo electrónico, un servidor de intercambio o un protocolo RGB-RPC, Storm, etc.);
- Alice recibe `consigna.rgb` y lo acepta en su propio alijo :

```bash
alice$ rgb accept consignment.rgb
```


- La CLI comprueba la validez de la transición y la añade al alijo de Alice. Si no es válida, el comando falla con mensajes de error detallados. De lo contrario, tiene éxito, e informa de que la transacción de muestra aún no se ha emitido en la red Bitcoin (Bob está esperando la luz verde de Alice);
- A modo de confirmación, el comando `accept` devuelve una firma (*ficha de pago*) que Alice puede enviar a Bob para demostrarle que ha validado la *consignación* ;
- Bob puede entonces firmar y publicar (`--publish`) su transacción Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Tan pronto como esta transacción se confirma en la cadena, la propiedad del activo se considera transferida a Alice. El monedero de Alice, monitorizando el minado de la transacción, ve aparecer en su alijo el nuevo Owned State.

En el próximo capítulo, veremos más de cerca la integración de RGB en la Red Lightning.

## RGB en la Red Lightning

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

En este capítulo, propongo examinar cómo se puede utilizar RGB dentro de la Lightning Network, para integrar y mover activos RGB (tokens, NFTs, etc.) a través de canales de pago fuera de la cadena.

La idea básica es que la transición de estado RGB (*Transición de estado*) puede confirmarse en una transacción Bitcoin que, a su vez, puede permanecer fuera de la cadena hasta que se cierre el canal Lightning. Así, cada vez que se actualiza el canal, se puede incorporar una nueva transición de estado RGB a la nueva transacción de confirmación, que invalida la transición anterior. De este modo, los canales Lightning pueden utilizarse para transferir activos RGB, y pueden enrutarse del mismo modo que los pagos Lightning convencionales.

### Creación de canales y financiación

Para crear un canal Rayo que lleve activos RGB, necesitamos dos elementos:


- Financiación Bitcoin para crear el multisig 2/2 del canal (el UTXO básico para el canal);
- RGB, que envía activos al mismo multisig.

En términos de Bitcoin, la transacción de financiación debe existir para definir el UTXO de referencia, incluso si sólo contiene una pequeña cantidad de sats (es sólo cuestión de que cada salida en futuras transacciones de compromiso se mantenga por encima del límite de polvo igualmente). Por ejemplo, Alice puede decidir proporcionar 10k sats y 500 USDT (emitidos como un activo RGB). En la transacción de financiación, añadimos un compromiso (`Opret` o `Tapret`) que ancla la transición de estado RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Una vez preparada la transacción de financiación (pero aún no emitida), se crean transacciones de compromiso para que cualquiera de las partes pueda cerrar el canal unilateralmente en cualquier momento. Estas transacciones se parecen a las transacciones de compromiso clásicas de Lightning, salvo que añadimos una salida adicional que contiene el ancla RGB (OP_RETURN o Taproot) vinculada a la nueva transición de estado.

La transición de estado RGB traslada entonces los activos del multisig 2/2 de la financiación a las salidas de la transacción de compromiso. La ventaja de este proceso es que la seguridad del estado RGB coincide exactamente con la mecánica punitiva de Lightning: si Bob transmite un estado de canal antiguo, Alice puede castigarle y gastar la salida, con el fin de recuperar tanto los sats como las fichas RGB. Por tanto, el incentivo es aún mayor que en un canal Lightning sin activos RGB, ya que un atacante puede perder no sólo los sats, sino también los activos RGB del canal.

Por lo tanto, una transacción de compromiso firmada por Alice y enviada a Bob tendría el siguiente aspecto:

![RGB-Bitcoin](assets/fr/092.webp)

Y la transacción de compromiso adjunta, firmada por Bob y enviada a Alice, tendrá este aspecto:

![RGB-Bitcoin](assets/fr/093.webp)

### Actualización del canal

Cuando se produce un pago entre dos participantes del canal (o desean cambiar la asignación de activos), crean un nuevo par de transacciones de compromiso. La cantidad en sats en cada salida puede o no permanecer inalterada, dependiendo de la implementación, ya que su papel principal es permitir la construcción de UTXOs válidos. Por otro lado, la salida OP_RETURN (o Taproot) debe modificarse para contener el nuevo ancla RGB, que representa la nueva distribución de activos en el canal.

Por ejemplo, si Alice transfiere 30 USDT a Bob en el canal, la nueva transición de estado reflejará un saldo de 400 USDT para Alice y 100 USDT para Bob. La transacción de confirmación se añade a (o es modificada por) el ancla OP_RETURN/Taproot para incluir esta transición. Tenga en cuenta que, desde el punto de vista de RGB, la entrada a la transición sigue siendo el multisig inicial (donde los activos en la cadena se asignan realmente hasta que el canal se cierra). Sólo cambian las salidas de RGB (asignaciones), dependiendo de la redistribución decidida.

La transacción de compromiso firmada por Alice, lista para ser distribuida por Bob :

![RGB-Bitcoin](assets/fr/094.webp)

La transacción de compromiso firmada por Bob, lista para ser distribuida por Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### Gestión de HTLC

En realidad, la Lightning Network permite enrutar los pagos a través de múltiples canales, utilizando HTLCs (*Hashed Time-Locked Contracts*). Ocurre lo mismo con RGB: por cada pago en tránsito por el canal, se añade una salida HTLC a la transacción que se compromete, y una asignación RGB vinculada a este HTLC. Así, quien gasta la salida HTLC (gracias al secreto o tras la expiración del timelock) recupera tanto la saturación como los activos RGB asociados. Por otro lado, es obvio que se necesita tener suficiente dinero en el camino, tanto en términos de sats como de activos RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Por tanto, el funcionamiento de RGB en Lightning debe considerarse en paralelo al de la propia Red Lightning. Si quieres profundizar en este tema, te recomiendo encarecidamente que eches un vistazo a este otro completo curso de formación:

https://planb.network/courses/lnp201
### Mapa de códigos RGB

Por último, antes de pasar a la siguiente sección, me gustaría darte una visión general del código utilizado en RGB. El protocolo se basa en un conjunto de bibliotecas Rust y especificaciones de código abierto. Aquí tienes una visión general de los principales repositorios y crates:

![RGB-Bitcoin](assets/fr/097.webp)

#### Validación en el lado del cliente


- Repositorio**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Cajas** : [validación_del_lado_del_cliente](https://crates.io/crates/client_side_validation), [sellos_de_uso_único](https://crates.io/crates/single_use_seals)

Gestión de la validación fuera de la cadena y lógica de los sellos de un solo uso.

#### Compromisos deterministas de Bitcoin (DBC)


- Repositorio**: [bp-core](https://github.com/BP-WG/bp-core)
- Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)

Gestión del anclaje determinista en las transacciones Bitcoin (Tapret, OP_RETURN, etc.).

#### Compromiso multiprotocolo (MPC)


- Repositorio**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)

Múltiples combinaciones de compromiso e integración con distintos protocolos.

#### Tipos estrictos y codificación estricta


- Especificaciones**: [sitio web strict-types.org](https://www.strict-types.org/)
- Repositorios**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Cajas** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

El sistema de tipado estricto y la serialización determinista utilizados para la validación del lado del cliente.

#### Núcleo RGB


- Repositorio**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Crate**: [rgb-core](https://crates.io/crates/rgb-core)

El núcleo del protocolo, que engloba la lógica principal de la validación RGB.

#### Biblioteca y cartera estándar RGB


- Repositorio**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Caja** : [rgb-std](https://crates.io/crates/rgb-std)

Implementaciones estándar, gestión de alijos y carteras.

#### RGB CLI


- Repositorio**: [rgb](https://github.com/RGB-WG/rgb)
- Cajas**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

La cartera `rgb` CLI y crate, para la manipulación de contratos desde la línea de comandos.

#### Esquema RGB


- Repositorio**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Contiene ejemplos de esquemas (NIA, UDA, etc.) y sus implementaciones.

#### ALuVM


- Información** : [aluvm.org](https://www.aluvm.org/)
- Repositorios**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Cajas**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Máquina virtual basada en el registro utilizada para ejecutar scripts de validación.

#### Protocolo Bitcoin - BP


- Repositorios** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Complementos para soportar el protocolo Bitcoin (transacciones, desvíos, etc.).

#### Computación ubicua determinista - UBIDECO


- Repositorio**: [UBIDECO](https://github.com/UBIDECO)

Ecosistema vinculado a desarrollos deterministas de código abierto.

# Basándose en RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA y el proyecto Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Esta sección final del curso se basa en las presentaciones realizadas por varios ponentes en el RGB bootcamp. Incluye testimonios y reflexiones sobre RGB y su ecosistema, así como presentaciones de herramientas y proyectos basados en el protocolo. Este primer capítulo está moderado por Hunter Beast, y los dos siguientes por Frederico Tenga.

### De JavaScript a Rust, y al ecosistema Bitcoin

Al principio, Hunter Beast trabajaba principalmente en JavaScript. Entonces descubrió **Rust**, cuya sintaxis le pareció poco atractiva y frustrante al principio. Sin embargo, llegó a apreciar la potencia del lenguaje, el control sobre la memoria (*heap* y *stack*), y la seguridad y el rendimiento que conlleva. Destaca que Rust es un excelente campo de entrenamiento para comprender en profundidad cómo funciona un ordenador.

Hunter Beast cuenta su experiencia en varios proyectos del ecosistema *altcoin*, como Ethereum (con Solidity, TypeScript, etc.), y más tarde Filecoin. Explica que al principio le impresionaron algunos de los protocolos, pero que acabó sintiéndose desilusionado por la mayoría de ellos, sobre todo por su tokenómica. Denuncia los dudosos incentivos financieros, la creación inflacionaria de tokens que diluye a los inversores y el aspecto potencialmente explotador de estos proyectos. Así que acabó adoptando una postura **máximalista de Bitcoin**, entre otras cosas porque algunas personas le abrieron los ojos a los mecanismos económicos más sólidos de Bitcoin, y a la solidez de este sistema.

### El atractivo del RGB y la construcción por capas

Lo que le convenció definitivamente de la relevancia de Bitcoin, según sus palabras, fue el descubrimiento de RGB y el concepto de capas. Cree que las funcionalidades existentes en otras blockchains podrían reproducirse en capas superiores, por encima de Bitcoin, sin alterar el protocolo básico.

En febrero de 2022, se unió a **DIBA** para trabajar específicamente en RGB, y en particular en el monedero **Bitmask**. En aquel momento, Bitmask aún estaba en la versión 0.01 y ejecutaba RGB en la versión 0.4, sólo para la gestión de tokens individuales. Señala que esto estaba menos orientado a la autocustodia que hoy en día, ya que la lógica se basaba en parte en el servidor. Desde entonces, la arquitectura ha evolucionado hacia este modelo, muy apreciado por los bitcoiners.

### Las bases del protocolo RGB

El protocolo **RGB** es la plasmación más reciente y avanzada del concepto _colored coins_, ya explorado en torno a 2012-2013. Por aquel entonces, varios equipos buscaban asociar distintos valores de bitcoin en UTXOs, lo que dio lugar a múltiples implementaciones dispersas. Esta falta de estandarización y la escasa demanda de entonces impidieron que estas soluciones se afianzaran de forma duradera.

En la actualidad, RGB destaca por su solidez conceptual y sus especificaciones unificadas a través de la asociación LNP/BP. El principio se basa en la validación del lado del cliente. La blockchain de Bitcoin sólo almacena los compromisos criptográficos (_commitments_, vía Taproot u OP_RETURN), mientras que la mayoría de los datos (definiciones de contratos, historiales de transferencias, etc.) son almacenados por los usuarios interesados. De este modo, se distribuye la carga de almacenamiento y se refuerza la confidencialidad de los intercambios, sin sobrecargar la blockchain. Este enfoque permite la creación de activos fungibles (norma **RGB20**) o únicos (norma **RGB21**), dentro de un marco modular y escalable.

### La función testigo (RGB20) y los activos únicos (RGB21)

Con **RGB20**, definimos un token fungible en Bitcoin. El emisor elige una _oferta_, una _precisión_, y crea un _contrato_ en el que luego puede realizar transferencias. Cada transferencia está referenciada a un Bitcoin UTXO, que actúa como un *Sello de un solo uso*. Esta lógica garantiza que el usuario no podrá gastar el mismo activo dos veces, ya que sólo la persona capaz de gastar el UTXO posee la clave para actualizar el estado del contrato del lado del cliente.

**RGB21** se dirige a activos únicos (o "NFT"). El activo tiene un suministro de 1, y puede asociarse a metadatos (archivo de imagen, audio, etc.) descritos a través de un campo específico. A diferencia de los NFT en blockchains públicos, los datos y sus identificadores MIME pueden permanecer privados, distribuidos peer-to-peer a discreción del propietario.

### La solución Bitmask: un monedero para RGB

Para explotar las capacidades de RGB en la práctica, el proyecto **DIBA** ha diseñado un monedero llamado [Bitmask](https://bitmask.app/). La idea es proporcionar una herramienta no custodial, basada en Taproot, accesible como aplicación web o extensión del navegador. Bitmask gestiona activos RGB20 y RGB21, e integra varios mecanismos de seguridad:


- El código del núcleo está escrito en Rust y luego se compila en WebAssembly para ejecutarse en un entorno JavaScript (React);
- Las claves se generan localmente y se almacenan cifradas localmente;
- Los datos de estado (stash) se guardan en memoria, se serializan y se cifran mediante la biblioteca **Carbonado**, que realiza la compresión, corrección de errores, cifrado y verificación del flujo utilizando Blake3.

Gracias a esta arquitectura, todas las transacciones de activos tienen lugar en el lado del cliente. Desde el exterior, la transacción de Bitcoin no es más que una clásica transacción de gasto en Taproot, de la que nadie sospecharía que también conlleva una transferencia de tokens fungibles o NFT. La ausencia de sobrecarga en la cadena (no hay metadatos almacenados públicamente) garantiza un cierto grado de discreción y hace más fácil resistir posibles intentos de censura.

### Seguridad y arquitectura distribuida

En la medida en que el protocolo RGB exige que cada participante conserve su historial de transacciones (para probar la validez de las transferencias que recibe), se plantea la cuestión del almacenamiento. Bitmask propone serializar este alijo localmente, y luego enviarlo a varios servidores o nubes (opcional). Los datos permanecen encriptados por el usuario a través de **Carbonado**, por lo que un servidor no puede leerlos. En caso de corrupción parcial, la capa de corrección de errores puede reconstituir el contenido.

El uso de CRDT (_Conflict-free replicated data type_) permite fusionar distintas versiones del alijo, en caso de que diverjan. Todo el mundo es libre de alojar estos datos donde desee, ya que ningún nodo completo contiene toda la información vinculada al activo. Esto refleja exactamente la filosofía *Client-side Validation*, en la que cada propietario es responsable de almacenar pruebas de la validez de su activo RGB.

### Hacia un ecosistema más amplio: mercado, interoperabilidad y nuevas funciones

La empresa que está detrás de Bitmask no se limita al simple desarrollo de un monedero. DIBA pretende desarrollar :


- Un **mercado** de intercambio de fichas, especialmente en formato **RGB21**;
- Compatibilidad con otros monederos (como *Iris Wallet*);
- Técnicas de transferencia por lotes**, es decir, la posibilidad de incluir varias transferencias RGB sucesivas en una sola transacción.

Al mismo tiempo, estamos trabajando en **WebBTC** o **WebLN** (estándares que permiten a los sitios web pedir al monedero que firme transacciones Bitcoin o Lightning), así como en la capacidad de "telequemar" entradas Ordinales (si queremos repatriar Ordinales a un formato RGB más discreto y flexible).

### Conclusión

Todo el proceso muestra cómo el ecosistema RGB puede desplegarse y hacerse accesible a los usuarios finales mediante soluciones técnicas sólidas. La transición de una perspectiva altcoin a una visión más centrada en Bitcoin, unida al descubrimiento de *Client-side Validation*, ilustra un camino bastante lógico: entendemos que es posible implementar diversas funcionalidades (tokens fungibles, NFT, contratos inteligentes...) sin bifurcar la blockchain, simplemente aprovechando los compromisos criptográficos en transacciones Taproot u OP_RETURNs.

El monedero **Bitmask** forma parte de este enfoque: en el lado de la blockchain, todo lo que se ve es una transacción ordinaria de Bitcoin; en el lado del usuario, se manipula una interfaz web en la que se crean, intercambian y almacenan todo tipo de activos fuera de la cadena. Este modelo disocia claramente la infraestructura monetaria (Bitcoin) de la lógica de emisión y transferencia (RGB), al tiempo que garantiza un alto nivel de confidencialidad y una mejor escalabilidad.

## El trabajo de Bitfinex en RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

En este capítulo, basado en una presentación de Frederico Tenga, examinamos un conjunto de herramientas y proyectos creados por el equipo de Bitfinex dedicados al RGB, con el objetivo de fomentar la aparición de un ecosistema rico y diverso en torno a este protocolo. El objetivo inicial del equipo no es lanzar un producto comercial específico, sino proporcionar bloques de construcción de software, contribuir al propio protocolo RGB y proponer referencias de implementación concretas, como un monedero móvil (*Iris Wallet*) o un nodo Lightning compatible con RGB.

### Antecedentes y objetivos

Desde alrededor de 2022, el equipo RGB de Bitfinex se ha concentrado en desarrollar la pila tecnológica que permite explotar y probar RGB de manera eficiente. Se han realizado varias contribuciones:


- Participación en las especificaciones del código fuente y los protocolos, incluida la redacción de propuestas de mejora, la corrección de errores, etc;
- Herramientas para que los desarrolladores simplifiquen la integración de RGB en sus aplicaciones;
- Diseño de un monedero móvil llamado [Iris](https://iriswallet.com/) para experimentar e ilustrar las mejores prácticas de uso de RGB ;
- Creación de un nodo Lightning personalizado, capaz de gestionar canales con activos RGB;
- Apoyar a otros equipos que construyen soluciones en RGB, para fomentar la diversidad y un ecosistema fuerte.

Este enfoque pretende cubrir toda la cadena de necesidades: desde la biblioteca de bajo nivel (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), que permite la implementación de un monedero, hasta el aspecto de producción (un nodo Lightning, un monedero para Android, etc.).

### La biblioteca RGBlib: simplificación del desarrollo de aplicaciones RGB

Un punto importante para democratizar la creación de monederos y aplicaciones RGB es poner a disposición una abstracción lo suficientemente simple como para que los desarrolladores no tengan que aprender todo sobre la lógica interna del protocolo. Este es precisamente el objetivo de **RGBlib**, escrito en Rust.

RGBlib actúa como puente entre los requisitos altamente flexibles (pero a veces complejos) de RGB que hemos podido estudiar en capítulos anteriores, y las necesidades concretas de un desarrollador de aplicaciones. En otras palabras, un monedero (o servicio) que desee gestionar transferencias de tokens, emisión de activos, verificación, etc., puede confiar en RGBlib sin conocer cada detalle criptográfico o cada parámetro personalizable de RGB.

La librería ofrece :


- Funciones llave en mano para la emisión (_emisión_) de activos (fungibles o no);
- La capacidad de transferir (enviar/recibir) activos mediante la manipulación de objetos simples (direcciones, importes, UTXOs, etc.);
- Mecanismo para almacenar y cargar la información de estado (*consignaciones*) necesaria para la validación del lado del cliente.

RGBlib se apoya por tanto en nociones complejas propias de RGB (Client-side Validation, anclajes Tapret/Opret), pero las encapsula para que la aplicación final no tenga que reprogramarlo todo o tomar decisiones arriesgadas. Además, RGBlib ya está enlazado en varios lenguajes (Kotlin y Python), lo que abre la puerta a usos más allá de un simple universo Rust.

### Iris Wallet: un ejemplo de monedero RGB en Android

Para demostrar la eficacia de RGBlib, el equipo de Bitfinex ha desarrollado **Iris Wallet**, exclusivamente en Android en esta fase. Se trata de un monedero móvil que ilustra una experiencia de usuario similar a la de un monedero Bitcoin ordinario: se puede emitir un activo, enviarlo, recibirlo y ver su historial, mientras se mantiene un modelo de autocustodia.

Iris tiene una serie de características interesantes:

**Utilizando un servidor Electrum:**

Como cualquier monedero, Iris necesita conocer las confirmaciones de transacciones en la blockchain. En lugar de integrar un nodo completo, Iris utiliza por defecto un servidor Electrum mantenido por el equipo de Bitfinex. Sin embargo, los usuarios pueden configurar su propio servidor u otro servicio de terceros. De esta forma, las transacciones de Bitcoin pueden ser validadas y la información recuperada (indexación) de forma modular.

**El servidor proxy RGB:**

A diferencia de Bitcoin, RGB requiere el intercambio de metadatos fuera de la cadena (*consignaciones*) entre emisor y receptor. Para simplificar este proceso, Iris ofrece una solución en la que la comunicación tiene lugar a través de un servidor proxy. El monedero receptor genera una *factura* que menciona dónde debe enviar el remitente los datos *del lado del cliente*. Por defecto, la URL apunta a un proxy alojado por el equipo de Bitfinex, pero puedes cambiar este proxy (o alojar el tuyo propio). La idea es volver a una experiencia de usuario familiar en la que el destinatario muestra un código QR, y el remitente escanea este código para la transacción, sin manipulaciones adicionales complejas.

**Copia de seguridad continua:**

En un contexto estrictamente Bitcoin, hacer una copia de seguridad de la semilla suele ser suficiente (aunque actualmente recomendamos hacer una copia de seguridad de la semilla y los descriptores). Con RGB, esto no es suficiente: también necesitas guardar el historial local (las *consignaciones*) que prueban que realmente posees un activo RGB. Cada vez que recibes un recibo, el dispositivo almacena nuevos datos, que son esenciales para los gastos posteriores. Iris gestiona automáticamente una copia de seguridad cifrada en Google Drive del usuario. Esto no requiere ninguna confianza especial en Google, ya que la copia de seguridad está cifrada, y en el futuro se prevén opciones más sólidas (como un servidor personal) para evitar cualquier riesgo de censura o eliminación por parte de un operador tercero.

**Otras características:**


- Cree un grifo para probar o distribuir rápidamente fichas para experimentación o promoción;
- Un sistema de certificación (actualmente centralizado) para distinguir un token legítimo de uno falso copiando un ticker famoso. En el futuro, esta certificación podría descentralizarse (mediante DNS u otros mecanismos).

En definitiva, Iris ofrece una experiencia de usuario cercana a la de un monedero Bitcoin clásico, enmascarando la complejidad adicional (gestión del alijo, historial de *consignaciones*, etc.) gracias a RGBlib y al uso de un servidor proxy.

### Servidor proxy y experiencia del usuario

El servidor proxy introducido anteriormente merece ser detallado, ya que es la clave para una experiencia de usuario fluida. En lugar de que el remitente tenga que transmitir manualmente las *consignas* al destinatario, la transacción RGB tiene lugar en segundo plano a través de un servidor proxy :


- El destinatario genera una *factura* (que contiene, entre otras cosas, la dirección del proxy);
- El remitente envía (mediante una petición HTTP) un proyecto de transición (la *consignación*) al proxy ;
- El destinatario recupera este proyecto, ejecuta la validación *del lado del cliente* localmente;
- A continuación, el destinatario publica, a través del proxy, la aceptación (o posible rechazo) de la transición de estado ;
- El remitente puede ver el estado de validación y, si es aceptada, emitir la transacción Bitcoin finalizando la transferencia.

De este modo, el monedero se comporta casi como un monedero normal. El usuario desconoce todos los pasos intermedios. Es cierto que el proxy actual no está cifrado ni autenticado (lo que plantea problemas de confidencialidad e integridad), pero estas mejoras son posibles en versiones posteriores. El concepto de proxy sigue siendo extremadamente útil para recrear la experiencia de "yo envío un código QR, tú lo escaneas para pagar".

### Integración RGB en la Red Lightning

Otro punto clave del trabajo del equipo de Bitfinex es hacer que la red Lightning sea compatible con los activos RGB. El objetivo es habilitar canales Lightning en USDT (o cualquier otro token), y beneficiarse de las mismas ventajas que bitcoin en Lightning (transacciones casi instantáneas, enrutamiento, etc.). En concreto, se trata de crear un nodo Lightning modificado para :


- Abra un canal colocando no sólo satoshis, sino también uno o más activos RGB en la financiación UTXO multisig ;
- Generar transacciones de compromiso Lightning (lado Bitcoin) acompañadas de las correspondientes transiciones de estado RGB. Cada vez que se actualiza el canal, una transición RGB redefine la distribución de activos en las salidas de Lightning;
- Permitir el cierre unilateral, en el que el activo se recupera en un UTXO exclusivo, de conformidad con las normas de la Red del Rayo (HTLC, bloqueo temporal, castigo, etc.).

Esta solución, denominada "**RGB Lightning Node**", utiliza LDK (*Lightning Dev Kit*) como base, y añade los mecanismos necesarios para inyectar tokens RGB en los canales. Los compromisos Lightning conservan la estructura clásica (salidas puntuables, timelock...), y además anclan una transición de estado RGB (vía `Opret` o `Tapret`). Para el usuario, esto abre el camino a los canales Lightning en stablecoins o en cualquier otro activo emitido vía RGB.

### Potencial de DEX e impacto en Bitcoin

Una vez que varios activos se gestionan a través de Lightning, se hace posible imaginar un **intercambio atómico** en una única ruta de enrutamiento Lightning, utilizando la misma lógica de secretos y timelocks. Por ejemplo, el usuario A tiene bitcoin en un canal Lightning y el usuario B tiene USDT RGB en otro canal Lightning. Pueden construir una ruta que conecte sus dos canales e intercambiar simultáneamente BTC por USDT, sin necesidad de confianza. Esto no es más que un **intercambio atómico** que tiene lugar en varios saltos, haciendo que los participantes externos sean casi ajenos al hecho de que están realizando una operación, no sólo un enrutamiento. Este enfoque ofrece :


- Latencia muy baja, ya que todo permanece fuera de cadena en Lightning.
- Una **privacidad** superior: nadie sabe que se trata de un comercio, y no de un encaminamiento normal ;
- Evitar el frontrunning, un problema recurrente de las DEX en cadena ;
- Costes reducidos (no pagas espacio en bloque, sólo las tarifas de enrutamiento Lightning).

Podemos imaginar entonces un ecosistema en el que los nodos Lightning ofrezcan precios de intercambio (proporcionando liquidez). Cada nodo, si lo desea, puede desempeñar el papel de _market maker_, comprando y vendiendo diversos activos en Lightning. Esta perspectiva de una DEX de _capa-2_ refuerza la idea de que no es necesario bifurcar o utilizar blockchains de terceros para obtener intercambios de activos descentralizados.

El impacto sobre Bitcoin podría ser positivo: La infraestructura de Lightning (nodos, canales y servicios) se utilizaría más plenamente gracias a los volúmenes generados por estas *stablecoins*, derivados y otros tokens. Los comerciantes interesados en los pagos de USDT en Lightning descubrirían mecánicamente los pagos de BTC en Lightning (gestionados por la misma pila). El mantenimiento y la financiación de la infraestructura de la red Lightning también podrían beneficiarse de la multiplicación de estos flujos no BTC, lo que beneficiaría indirectamente a los usuarios de Bitcoin.

### Conclusión y recursos

El equipo de Bitfinex dedicado a RGB ilustra con su trabajo la diversidad de lo que se puede hacer sobre el protocolo. Por un lado, está RGBlib, una biblioteca que facilita el diseño de monederos y aplicaciones. Por otro, tenemos Iris Wallet, una demostración práctica en Android de una cuidada interfaz de usuario final. Por último, la integración de RGB con Lightning demuestra que los canales stablecoin son posibles, y abre el camino a una potencial DEX descentralizada en Lightning.

Este enfoque sigue siendo en gran medida experimental y continúa evolucionando: la biblioteca RGBlib se perfecciona a medida que avanzamos, Iris Wallet recibe mejoras periódicas y el nodo Lightning dedicado aún no es un cliente Lightning convencional.

Quienes deseen saber más o contribuir, tienen a su disposición varios recursos, entre ellos :


- [Repositorios GitHub RGB Tools](https://github.com/RGB-Tools);
- [Un sitio de información dedicado a Iris Wallet](https://iriswallet.com/) para probar el monedero en Android.

En el próximo capítulo, veremos más detenidamente cómo lanzar un nodo RGB Lightning.

## RLN - Nodo de rayos RGB

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

En este capítulo final, Frederico Tenga te lleva paso a paso a través de la configuración de un nodo Lightning RGB en un entorno Regtest, y te muestra cómo crear tokens RGB en él. Al lanzar dos nodos separados, también descubrirás cómo abrir un canal Lightning entre ellos e intercambiar activos RGB.

Este vídeo sirve de tutorial, similar al que cubrimos en un capítulo anterior, pero esta vez centrado específicamente en Lightning

El principal recurso para este vídeo es el repositorio de Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), que facilita el lanzamiento de esta configuración en Regtest.

### Despliegue de un nodo Lightning compatible con RGB

El proceso retoma y pone en práctica todos los conceptos tratados en los capítulos anteriores:


- La idea de que **UTXO** bloqueado en un multisig 2/2 de un canal Lightning puede recibir no sólo bitcoins, sino también ser un Sello de un solo uso de activos RGB (fungibles o no) ;
- La adición, en cada operación de Rayo, de una salida (`Tapret` u `Opret`) dedicada a anclar la transición de estado RGB;
- La infraestructura asociada (bitcoind/indexer/proxy) para validar transacciones Bitcoin e intercambiar datos *del lado del cliente*.

### Presentación del nodo rgb-lightning

El proyecto **`rgb-lightning-node`** es un demonio Rust basado en un fork de `rgb-lightning` (LDK) modificado para tener en cuenta la existencia de activos RGB en un canal. Cuando se abre un canal, se puede especificar la presencia de activos, y cada vez que se actualiza el estado del canal, se crea una transición RGB que refleja la distribución del activo en las salidas de Lightning. Esto permite :


- Abrir canales Lightning en USDT, por ejemplo;
- Encaminar estas fichas a través de la red, siempre que las vías de encaminamiento tengan suficiente liquidez;
- Explotar la lógica de castigo y timelock de Lightning sin modificaciones: basta con anclar la transición RGB en una salida adicional de la transacción de compromiso.

El código aún está en fase alfa: recomendamos utilizarlo únicamente en **regtest** o en la **testnet**.

### Instalación de nodos

Para compilar e instalar el binario `rgb-lightning-node`, comenzamos clonando el repositorio y sus submódulos, luego ejecutamos el archivo :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- La opción `--recurse-submodules` también clona los subdispositivos necesarios (incluida la versión modificada de `rust-lightning`);
- La opción `--shallow-submodules` restringe la profundidad del clon para acelerar la descarga, al tiempo que proporciona acceso a los commits esenciales.

Desde la raíz del proyecto, ejecute el siguiente comando para compilar e instalar el binario :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` garantiza que se respete estrictamente la versión de las dependencias;
- `--debug` no es obligatorio, pero puede ayudarle a centrarse (puede utilizar `--release` si lo prefiere) ;
- `--path .` indica a `cargo install` que instale desde el directorio actual.

Al final de este comando, un ejecutable `rgb-lightning-node` estará disponible en su `$CARGO_HOME/bin/`. Asegúrese de que esta ruta está en su `$PATH` para que pueda invocar el comando desde cualquier directorio.

### Requisitos de rendimiento

Para funcionar, el demonio `rgb-lightning-node` requiere la presencia y configuración de :


- Un nodo `bitcoind`**

Cada instancia de RLN deberá comunicarse con `bitcoind` para difundir y supervisar sus transacciones en la cadena. Será necesario proporcionar al demonio la autenticación (nombre de usuario/contraseña) y la URL (host/puerto).


- Un indexador** (Electrum o Esplora)

El demonio debe ser capaz de listar y explorar transacciones en la cadena, en particular para encontrar el UTXO en el que se ha anclado un activo. Deberá especificar la URL de su servidor Electrum o Esplora.


- Un proxy RGB

Como se ha visto en capítulos anteriores, el **servidor proxy** es un componente (opcional, pero muy recomendable) para simplificar el intercambio de *consignas* entre pares Lightning. Una vez más, hay que especificar una URL.

Los ID y las URL se introducen cuando el demonio se _desbloquea_ a través de la API. Más sobre esto más adelante.

### Lanzamiento de Regtest

Para un uso sencillo, hay un script `regtest.sh` que inicia automáticamente, a través de Docker, un conjunto de servicios: `bitcoind`, `electrs` (indexador), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Permite lanzar un entorno local, aislado y preconfigurado. Crea y destruye contenedores y directorios de datos en cada reinicio. Comenzaremos iniciando el :

```bash
./regtest.sh start
```

Este script :


- Crea un directorio `docker/` para almacenar los archivos ;
- Ejecute `bitcoind` en regtest, así como el indexador `electrs` y el `rgb-proxy-server` ;
- Espere hasta que todo esté listo para usar.

![RGB-Bitcoin](assets/fr/101.webp)

A continuación, lanzaremos varios nodos RLN. En shells separados, ejecute, por ejemplo (para lanzar 3 nodos RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- El parámetro `--network regtest` indica el uso de la configuración regtest;
- `--daemon-listening-port` indica en qué puerto REST escuchará el nodo Lightning las llamadas a la API (JSON);
- `--ldk-peer-listening-port` especifica en qué puerto Lightning p2p escuchar;
- `dataldk0/`, `dataldk1/` son las rutas a los directorios de almacenamiento (cada nodo almacena su información por separado).

También puede ejecutar comandos en sus nodos RLN desde su navegador:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Para que un nodo abra un canal, primero debe tener bitcoins en una dirección generada con el siguiente comando (para el nodo n°1, por ejemplo):

```bash
curl -X POST http://localhost:3001/address
```

La respuesta le proporcionará una dirección.

![RGB-Bitcoin](assets/fr/103.webp)

En el Regtest `bitcoind`, vamos a minar algunos bitcoins. Ejecutar :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Envíe los fondos a la dirección del nodo generada anteriormente:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Luego minar un bloque para confirmar la transacción:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Lanzamiento de Testnet (sin Docker)

Si desea probar un escenario más realista, puede lanzar 3 nodos RLN en la Testnet en lugar de en Regtest, apuntando a servicios públicos :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Por defecto, si no se encuentra ninguna configuración, el demonio intentará utilizar el archivo :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Con inicio de sesión :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

También puedes personalizar estos elementos a través de la API `init`/`unlock`.

### Emisión de una ficha RGB

Para emitir un token, empezaremos creando UTXOs "coloreables":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Por supuesto, puede adaptar el pedido. Para confirmar la transacción, minamos un :

```bash
./regtest.sh mine 1
```

Ahora podemos crear un activo RGB. El comando dependerá del tipo de activo que desee crear y sus parámetros. Aquí estoy creando un token NIA (*Non Inflatable Asset*) llamado "PBN" con un suministro de 1000 unidades. La `precisión` le permite definir la divisibilidad de las unidades.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

La respuesta incluye el identificador del activo recién creado. No olvide anotar este identificador. En mi caso, es :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

A continuación, puedes transferirlo a la cadena o asignarlo a un canal Lightning. Eso es exactamente lo que vamos a hacer en la siguiente sección.

### Abrir un canal y transferir un activo RGB

Primero debe conectar su nodo a un peer de la red Lightning mediante el comando `/connectpeer`. En mi ejemplo, controlo ambos nodos. Así que recuperaré la clave pública de mi segundo nodo Lightning con este comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

El comando devuelve la clave pública de mi nodo n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

A continuación, abriremos el canal especificando el activo correspondiente (`PBN`). El comando `/openchannel` permite definir el tamaño del canal en satoshis y optar por incluir el activo RGB. Depende de lo que quieras crear, pero en mi caso, el comando es :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Más información aquí:


- `peer_pubkey_and_opt_addr`: Identificador del peer al que queremos conectarnos (la clave pública que encontramos antes);
- `capacidad_sat`: Capacidad total del canal en satoshis ;
- `push_msat`: Cantidad en milisatoshis transferida inicialmente al peer cuando se abre el canal (aquí transfiero inmediatamente 10.000 sats para que pueda hacer una transferencia RGB más tarde) ;
- `asset_amount`: Cantidad de activos RGB a comprometer en el canal ;
- `asset_id` : Identificador único del activo RGB involucrado en el canal;
- público Indica si el canal debe hacerse público para su enrutamiento en la red.

![RGB-Bitcoin](assets/fr/111.webp)

Para confirmar la transacción, se minan 6 bloques:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

El canal Lightning ya está abierto y también contiene 500 tokens `PBN` por parte del nodo n°1. Si el nodo n°2 desea recibir tokens `PBN`, debe generar una factura. He aquí cómo hacerlo:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Con :


- `amt_msat`: Importe de la factura en milisatoshis (mínimo 3000 sats) ;
- `expiry_sec` : Tiempo de expiración de la factura en segundos ;
- `asset_id` : Identificador del activo RGB asociado a la factura ;
- `importe_activo`: Importe del activo RGB que se va a transferir con esta factura.

En respuesta, obtendrá una factura RGB (como se ha descrito en capítulos anteriores):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Ahora pagaremos esta factura desde el primer nodo, que tiene el efectivo necesario con el token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Se ha efectuado el pago. Esto puede verificarse ejecutando el comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

He aquí cómo desplegar un nodo Lightning modificado para transportar activos RGB. Esta demostración se basa en :


- Un entorno regtest (mediante `./regtest.sh`) o testnet ;
- Un nodo Lightning (`rgb-lightning-node`) basado en un `bitcoind`, un indexador y un `rgb-proxy-server` ;
- Una serie de API REST JSON para abrir/cerrar canales, emitir tokens, transferir activos a través de Lightning, etc.

Gracias a este proceso :


- Las transacciones de compromiso relámpago incluyen una salida adicional (OP_RETURN o Taproot) con el anclaje de una transición RGB;
- Las transferencias se realizan exactamente igual que los pagos Lightning tradicionales, pero añadiendo un token RGB;
- Múltiples nodos RLN pueden estar vinculados para enrutar y experimentar con pagos a través de múltiples nodos, siempre que haya suficiente liquidez tanto en bitcoins como en activos RGB en el camino.

El proyecto sigue en fase alfa. Por tanto, se recomienda encarecidamente limitarse a los entornos de prueba (regtest, testnet).

Las oportunidades que abre esta compatibilidad LN-RGB son considerables: stablecoins en Lightning, DEX layer-2, transferencia de tokens fungibles o NFT a muy bajo coste... Los capítulos anteriores han esbozado la arquitectura conceptual y la lógica de validación. Ahora tienes una visión práctica de cómo poner en marcha un nodo de este tipo, para tus futuros desarrollos o pruebas.

# Conclusión

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Opiniones y valoraciones

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>verdadero</isCourseReview>

## Conclusión

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isConclusionCurso>true</isConclusionCurso>
