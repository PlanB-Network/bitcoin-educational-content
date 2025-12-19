---
name: Programación Bitcoin
goal: Construir una biblioteca Bitcoin completa desde cero y comprender los fundamentos criptográficos de Bitcoin
objectives: 

 - Implementación de aritmética de campos finitos y operaciones con curvas elípticas en Python
 - Construcción y análisis sintáctico de transacciones Bitcoin mediante programación
 - Creación de direcciones testnet y difusión de transacciones a través de la red
 - Dominar los fundamentos matemáticos del modelo de seguridad de Bitcoin

---
# Un viaje a los guiones y programas de Bitcoin


Este curso intensivo de dos días, impartido por Jimmy Song, le llevará a profundizar en los fundamentos técnicos de Bitcoin mediante la construcción de una biblioteca Bitcoin completa desde cero. Empezando por las matemáticas esenciales de los campos finitos y las curvas elípticas, progresarás a través del análisis sintáctico de transacciones, la ejecución de scripts y la comunicación en red. A través de ejercicios prácticos de codificación en cuadernos Jupyter, crearás tu propia dirección de red de prueba, construirás transacciones manualmente y las transmitirás directamente a la red, todo ello mientras adquieres una profunda comprensión de los principios criptográficos que hacen que Bitcoin sea seguro y fiable.


¡Disfrute del viaje!


+++

# Introducción


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Resumen del curso


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Bienvenido al curso PRO 202 _**Programación de Bitcoin**_, un viaje intensivo que le llevará desde la aritmética de campos finitos hasta la construcción y emisión de transacciones reales en Testnet de Bitcoin.


En este curso, construirás progresivamente una biblioteca Bitcoin en Python mientras adquieres los fundamentos criptográficos, de protocolo y de software necesarios para razonar con precisión sobre la seguridad y el funcionamiento interno de Bitcoin. El enfoque de PRO 202 es completamente práctico: cada concepto se implementa inmediatamente en cuadernos Jupyter, asegurando que la teoría y el código se refuercen mutuamente.


### Conceptos matemáticos esenciales para Bitcoin


Esta primera sección establece las bases matemáticas indispensables. Implementarás la aritmética de campos finitos y las operaciones de curva elíptica (ley de grupos, suma, duplicación, multiplicación escalar...) - los prerrequisitos para ECDSA. El objetivo es doble: entender la estructura algebraica que hace posible las firmas criptográficas y construir herramientas fiables en Python para manipularlas.


A continuación, formalizará los componentes de ECDSA: generación de claves, formateo de puntos, hashing, creación de firmas y verificación. Esta sección conecta directamente la teoría con la práctica, haciendo hincapié en los detalles de implementación y en la solidez del modelo de seguridad subyacente.


### Funcionamiento interno de las transacciones Bitcoin


En la segunda sección, diseccionará la estructura de una transacción Bitcoin: UTXOs, entradas/salidas, secuencias, scripts, codificaciones y más. Escribirás código para construir, firmar y verificar transacciones, obteniendo una comprensión precisa de lo que es comprometido por el hash y por qué.


A continuación, implementará un ejecutor _Script_ mínimo, revisará los opcodes clave y validará las rutas de gasto. El objetivo es que seas capaz de auditar el comportamiento de las transacciones, diagnosticar fallos de validación y razonar sobre la seguridad de las políticas de gasto.


### Funcionamiento interno de la red Bitcoin


En la tercera sección, situará las transacciones dentro del sistema más amplio: estructura de bloques, cabeceras, dificultad y el mecanismo Proof-of-Work. Manejarás mensajes de protocolo, cabeceras de bloque y árboles de Merkle.


Por último, estudiará la comunicación entre nodos peer-to-peer, la optimización de mensajes y la introducción de SegWit.


Como en todos los cursos sobre Plan ₿ Academy, la sección final incluye una evaluación diseñada para consolidar sus conocimientos. ¿Listo para descubrir el funcionamiento interno de Bitcoin y escribir el código que lo impulsa? Comencemos










# Conceptos matemáticos esenciales para Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matemáticas para la aplicación de Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Fundamentos de programación: Estructuras matemáticas básicas


Este curso condensa las matemáticas esenciales detrás de los sistemas criptográficos de Bitcoin en un flujo de trabajo muy práctico. Los conceptos se explican, se demuestran con ejemplos y luego se implementan en Jupyter Notebook. La idea rectora es simple: sólo se entiende realmente una primitiva criptográfica una vez que se codifica. A lo largo de los dos días que dura el curso, los alumnos generate prueban las direcciones de la red, construyen y transmiten transacciones y, finalmente, interactúan con la red sin exploradores de bloques. Todo ello requiere una base sólida en campos finitos y curvas elípticas.


### Campos finitos: El motor aritmético de la criptografía


Un campo finito F(p) es un sistema aritmético definido por un número primo p, que contiene los elementos 0 a p-1. Los campos primos garantizan que cada elemento distinto de cero tenga un inverso y que todas las operaciones se realicen dentro del campo. La aritmética se basa en el módulo p para sumar, restar y multiplicar. La función `pow(base, exp, mod)` de Python permite una exponenciación modular eficiente, crucial para exponentes grandes utilizados en operaciones criptográficas reales.


#### Comportamiento multiplicativo

La multiplicación de cualquier elemento k distinto de cero por todos los elementos de un campo primo produce una permutación del campo. Esta propiedad garantiza la uniformidad y evita debilidades estructurales, por lo que los campos primos son ideales para la generación segura de claves y firmas digitales.


#### La división y el pequeño teorema de Fermat

La división se realiza mediante inversos multiplicativos. El pequeño teorema de Fermat afirma que

n^(p-1) ≡ 1 (mod p),

por lo que la inversa es n^(p-2). Python lo soporta directamente con `pow(n, -1, p)`. Estas operaciones aparecen constantemente en las rutinas criptográficas subyacentes de ECDSA y Bitcoin.


### Curvas elípticas: Estructuras no lineales para la seguridad de las claves públicas


Las curvas elípticas siguen la ecuación y² = x³ + ax + b. Bitcoin utiliza secp256k1, definida como y² = x³ + 7 sobre un campo finito. Los puntos de una curva elíptica forman un grupo matemático bajo adición de puntos. Una línea trazada a través de dos puntos P y Q interseca la curva en un tercer punto R; reflejando R a través del eje x se obtiene P + Q. Este sistema es asociativo e incluye un elemento de identidad: el punto en el infinito.


Al duplicar un punto se utiliza una recta tangente en lugar de una recta secante, con pendiente derivada de la derivada de la curva. Aunque estas fórmulas implican el cálculo sobre números reales, se vuelven totalmente discretas y exactas cuando la curva se define sobre un campo finito, el contexto utilizado en la Bitcoin.


### De las matemáticas a la criptografía Bitcoin


Los campos finitos proporcionan una aritmética determinista e invertible; las curvas elípticas proporcionan una estructura no lineal en la que calcular k-P es fácil, pero invertirlo es inviable desde el punto de vista computacional. La combinación de ambos elementos constituye la base de las claves públicas y privadas de Bitcoin, las firmas ECDSA y la seguridad de las transacciones. La comprensión de estos fundamentos prepara a los estudiantes para implementar claves, transacciones y firmas directamente, sin abstracciones ni herramientas externas.


## Criptografía de curva elíptica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Este capítulo presenta las curvas elípticas definidas sobre campos finitos y explica por qué constituyen la columna vertebral matemática de la criptografía de Bitcoin. Mientras que las curvas elípticas sobre números reales parecen suaves y continuas, la aplicación de las mismas ecuaciones sobre un campo finito crea un conjunto discreto y disperso de puntos. A pesar de la diferencia visual, todas las fórmulas de suma de puntos, pendientes y reglas algebraicas se comportan exactamente igual, sólo cambia la aritmética a aritmética modular. Bitcoin utiliza la curva y² = x³ + 7 (secp256k1), que preserva la simetría y el comportamiento no lineal esenciales para la seguridad criptográfica.


### Verificación de puntos e implementación del campo finito


Un punto se encuentra en una curva elíptica de campo finito si sus coordenadas satisfacen la ecuación de la curva bajo el módulo p. Verificar un punto como (73,128) en F₁₃₇ requiere comprobar que y² mod p es igual a x³ + 7 mod p. Implementar esto en código implica crear clases para elementos de campo finito y puntos de curva. La sobrecarga de operadores garantiza que toda la aritmética -suma, multiplicación, exponenciación, división- se realice automáticamente modulo p. Una vez que existen estas abstracciones, resulta sencillo escribir y razonar sobre operaciones criptográficas más avanzadas.


#### Propiedades de grupo y adición de puntos

Los puntos de la curva elíptica forman un grupo matemático bajo adición. El grupo cumple las condiciones de cierre, asociatividad, identidad (el punto en el infinito) e inversa (reflexión a través del eje x). Las construcciones geométricas confirman estas propiedades, haciendo que la multiplicación escalar (P sumado a sí mismo repetidamente) esté bien definida. Estas reglas de grupo permiten la criptografía de curva elíptica y garantizan un comportamiento coherente y predecible en operaciones puntuales repetidas.


### Grupos cíclicos y el problema del logaritmo discreto


La elección de un punto generador G en una curva nos permite generate un grupo cíclico: G, 2G, 3G, ..., nG = 0. Los puntos parecen no lineales e impredecibles, incluso cuando se generan secuencialmente. Esta imprevisibilidad crea la base del problema del logaritmo discreto: calcular P = sG es fácil, pero determinar s a partir de P es inviable desde el punto de vista computacional para grupos grandes. Esta función unidireccional es lo que hace que la criptografía de clave pública sea segura. Las escalares (claves privadas) se escriben en minúsculas; los puntos (claves públicas), en mayúsculas.


#### Multiplicación escalar eficiente

Para calcular sG de forma eficiente, las implementaciones utilizan el algoritmo de doble suma: escanear la representación binaria del escalar, duplicar el punto en cada paso y sumar G sólo cuando el bit es 1. Esto reduce el cálculo de O(n) sumas a O(log n), lo que permite realizar operaciones criptográficas prácticas incluso con escalares de 256 bits.


#### La curva secp256k1 en Bitcoin


Bitcoin utiliza la curva secp256k1, definida por y² = x³ + 7 sobre un campo primo donde p = 2²⁵⁶ - 2³² - 977. El punto generador G tiene coordenadas fijas elegidas mediante un procedimiento determinista NUMS ("nada en la manga"). El orden de grupo n es un primo grande cercano a 2²⁵⁶, lo que garantiza que cada punto distinto de cero genera el mismo grupo. El tamaño de 2²⁵⁶ (~10⁷⁷) es astronómicamente grande, lo que hace físicamente imposible forzar las claves privadas. Ni siquiera un trillón de superordenadores funcionando durante un trillón de años reduciría significativamente el espacio de claves.


### Claves públicas, claves privadas y serialización SEC


Una clave privada es un escalar aleatorio s; la clave pública es P = sG. Dado que resolver el problema del logaritmo discreto es inviable, P puede compartirse sin revelar s. Las claves públicas deben serializarse para su transmisión utilizando el formato SEC. El formato SEC sin comprimir utiliza 65 bytes: prefijo 0x04 + coordenada x + coordenada y. El formato comprimido utiliza sólo 33 bytes: prefijo 0x02 o 0x03 (dependiendo de la paridad de y) + coordenada x. Bitcoin utilizaba originalmente claves sin comprimir, pero ahora prefiere las comprimidas por eficiencia.


#### Bitcoin Address Creación


Las direcciones Bitcoin son hashes de claves públicas, no las propias claves en bruto. Para generate una dirección, serialice la clave pública en formato SEC, calcule el hash160 (SHA-256 y luego RIPEMD-160), añada el prefijo de red (0x00 para mainnet, 0x6F para testnet), calcule una suma de comprobación utilizando doble SHA-256, añada los cuatro primeros bytes de suma de comprobación y codifique el resultado utilizando Base58. Esta codificación elimina los caracteres ambiguos e incluye la suma de comprobación para evitar errores de transcripción. El proceso en varios pasos oculta la clave pública hasta que se produce un gasto, añade identificación de red y garantiza direcciones legibles por humanos y resistentes a errores.


# Funcionamiento interno de las transacciones Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Análisis de transacciones y firmas ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA: la base de la firma digital de Bitcoin


Bitcoin se basa en ECDSA, un esquema de firma basado en curvas elípticas que ofrece una gran seguridad con claves mucho más pequeñas que RSA. Su seguridad se basa en el problema del logaritmo discreto de curva elíptica: dado P = eG, calcular P es fácil, pero obtener e a partir de P es inviable desde el punto de vista computacional. Esta asimetría permite la criptografía de clave pública manteniendo la seguridad de las claves privadas.


#### Codificación DER de firmas ECDSA


Bitcoin codifica las firmas ECDSA utilizando el formato DER:


- 0x30 (marcador de secuencia)
- longitud byte
- 0x02 + longitud + R bytes
- 0x02 + longitud + S bytes


Esto añade sobrecarga, ampliando una firma de 64 bytes a ~71-72 bytes. Taproot elimina esta ineficiencia adoptando firmas Schnorr de tamaño fijo.


### Compromisos de firma y proceso de firma


Las firmas ECDSA se basan en una ecuación de compromiso: UG + VP = KG. El firmante selecciona valores U y V distintos de cero, y un nonce aleatorio K, demostrando que conoce la clave privada sin revelarla. El mensaje se codifica en Z, se genera un K aleatorio, R es la coordenada x de KG y S = (Z + RE)/K. La firma es el par (R, S). La seguridad depende en gran medida de que se utilice un K único e impredecible: si K se reutiliza o se filtra, la clave privada queda comprometida. Las implementaciones modernas utilizan la generación determinista de K (RFC 6979) para evitar fallos del RNG.


#### Verificación de firmas

Dados Z, (R, S) y la clave pública P, el verificador calcula U = Z/S y V = R/S, y comprueba si la coordenada x de UG + VP es igual a R. Esto funciona porque el álgebra de verificación reconstruye KG sin necesidad de la clave privada. La falsificación de firmas requeriría resolver el problema del registro discreto o romper la función hash.


#### Firmas Schnorr y contexto histórico


Las firmas Schnorr son matemáticamente más limpias y admiten funciones de agregación, pero estaban patentadas cuando se lanzó Bitcoin. ECDSA ofrecía una alternativa gratuita, aunque con más complejidad y firmas más grandes. Una vez expiradas las patentes, Bitcoin añadió las firmas Schnorr a través de Taproot, proporcionando firmas fijas de 64 bytes y una mayor privacidad. ECDSA sigue siendo compatible con el legado.



### Estructura de las transacciones y entradas/salidas


Una transacción Bitcoin consiste en:


- versión (4 bytes, little-endian)
- lista de entradas
- lista de salida
- locktime (4 bytes)


Las entradas hacen referencia a UTXO anteriores por su hash de transacción e índice de salida, e incluyen un script de desbloqueo (scriptSig) y un número de secuencia utilizado para timelocks o RBF. Las salidas especifican el importe (8 bytes) y el script de bloqueo (scriptPubKey), definiendo las condiciones de gasto. Las direcciones Bitcoin son representaciones de estos scripts.


#### El modelo UTXO

Bitcoin realiza el seguimiento de los productos no gastados en lugar de los saldos de las cuentas. Los UTXOs deben gastarse en su totalidad, es imposible un gasto parcial. Para gastar 1 BTC de un UTXO de 100 BTC, una transacción debe incluir una salida de cambio. Si se olvida la salida de cambio, el resto se convierte en una tasa de minero.


#### Serialización y análisis sintáctico de transacciones


Las transacciones utilizan un formato binario compacto. Tras el campo de versión, un varint codifica el número de entradas. Las entradas incluyen:


- hash tx anterior (32 bytes)
- índice de salida (4 bytes)
- scriptSig (varstr)
- secuencia (4 bytes)


Las salidas incluyen una cantidad de 8 bytes y scriptPubKey (varstr). Locktime controla cuando la transacción se convierte en válida. La serialización utiliza el orden little-endian para la mayoría de los enteros. Los analizadores consumen bytes secuencialmente y delegan en clases especializadas para entradas, salidas y scripts.


### Tasas, cambios y maleabilidad


Las tasas están implícitas:

tasa = suma(valores de entrada) - suma(valores de salida).

Cualquier valor no asignado se convierte en la tasa, lo que hace esencial la construcción correcta de la salida de cambio. Antes de SegWit, las firmas permitían la maleabilidad: la modificación de S a N-S producía una nueva transacción válida con un ID diferente. Bitcoin ahora impone una regla de S bajo, y SegWit aísla las firmas del cálculo de txid, haciendo que los ID sean estables y permitiendo protocolos de segunda capa como Lightning.


## Bitcoin Validación de scripts y transacciones

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script es un pequeño lenguaje de contrato inteligente basado en pilas que define cómo se pueden gastar las monedas. Cada salida lleva un scriptPubKey (script de bloqueo) y cada entrada lleva un scriptSig (script de desbloqueo). Juntos forman un programa que debe evaluarse a "true" para que el gasto sea válido. El script no es intencionadamente Turing-completo para que todas las rutas de ejecución sean predecibles y fáciles de validar en la red.


### Operaciones de script y modelo de ejecución


Un script es una secuencia de elementos de datos y opcodes. Los elementos de datos (firmas, claves públicas, hashes) se colocan en la pila, mientras que los opcodes que empiezan por `OP_` transforman la pila. Tras la ejecución, el elemento superior de la pila debe ser distinto de cero para tener éxito. Ejemplos: `OP_DUP` duplica el elemento superior, `OP_HASH160` aplica SHA256 y luego RIPEMD160, y `OP_CHECKSIG` verifica una firma contra el sighash de la transacción y una clave pública, empujando 1 para válido, 0 para inválido. Las reglas de análisis distinguen entre datos brutos (de longitud prefijada) y códigos de operación (buscados por valor de byte), y una pequeña máquina virtual los ejecuta de forma determinista en cada nodo.


### P2PK y P2PKH: patrones de pago básicos


El primer patrón, Pay-to-Public-Key (P2PK), bloqueaba las monedas directamente a una clave pública completa: el scriptPubKey es `<pubkey> OP_CHECKSIG`, y el scriptSig es sólo una firma. Es simple pero ineficiente en cuanto a espacio y expone la clave pública antes de que se gasten las monedas.


#### P2PKH y Direcciones

Pay-to-Public-Key-Hash (P2PKH) mejora esto bloqueando un hash de 20 bytes de la clave pública. El scriptPubKey es `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, y el scriptSig proporciona `<signature> <pubkey>`. La ejecución comprueba que el hash de la clave pública proporcionada coincide con el valor comprometido y, a continuación, verifica la firma. Esto oculta la clave pública hasta el momento del gasto, reduce el tamaño, y coincide con el familiar "1..." mainnet formato de dirección.


### Validación de transacciones y hashing de firmas


Un nodo que valida una transacción debe garantizar:

1) Cada entrada hace referencia a una salida existente no utilizada.

2) Valor total de entrada ≥ valor total de salida (la diferencia es la tasa).

3) Cada scriptSig desbloquea correctamente su scriptPubKey de referencia.


La verificación de firmas requiere construir el mensaje exacto que fue firmado, llamado sighash. Para ECDSA heredado, la validación vacía todos los scriptSigs, sustituye el scriptSig de la entrada actual por el scriptPubKey correspondiente, añade un tipo de hash de 4 bytes (normalmente `SIGHASH_ALL`) y realiza un doble hash del resultado. Ese valor de 256 bits es el que utiliza `OP_CHECKSIG`. Los tipos hash alternativos (por ejemplo, `SINGLE`, `NONE`, con o sin `ANYONECANPAY`) cambian qué partes de la transacción se comprometen, permitiendo casos de uso específicos como la financiación colaborativa o transacciones parcialmente especificadas, pero en la práctica se utilizan raramente.


#### Hashing cuadrático y SegWit

Dado que cada entrada de una transacción heredada requiere su propio cálculo sighash sobre una estructura que incluye todas las entradas, el tiempo de validación puede crecer cuadráticamente con el número de entradas. En el pasado, las grandes transacciones con múltiples entradas provocaban retrasos notables en la validación. SegWit rediseñó el cálculo de sighash para almacenar en caché las partes compartidas y reducir la complejidad al tiempo lineal, mejorando la escalabilidad y dificultando los ataques de denegación de servicio.


### Enigmas de script y lecciones de seguridad


Script puede expresar mucho más que un simple "una firma desbloquea estas monedas" Los rompecabezas Script lo demuestran codificando condiciones arbitrarias -problemas matemáticos, retos de preimagen hash o incluso recompensas por colisión- en las que cualquiera que proporcione los datos correctos puede gastar las monedas. Sin embargo, los resultados que sólo se basan en datos públicos (sin firmas) son vulnerables a los mineros: una vez que una solución válida aparece en el mempool, cualquier minero puede copiarla y redirigir el pago a sí mismo.


La lección práctica es que los contratos del mundo real casi siempre incluyen comprobaciones de firma, incluso cuando contienen lógica más compleja como multisig, timelocks o hashlocks. Las firmas vinculan la solución a una parte específica, preservando los incentivos y evitando que otros roben el pago. Comprender el modelo de pila de Script, los patrones estándar y las sutiles trampas es esencial para diseñar contratos inteligentes Bitcoin seguros y para razonar sobre cómo se validan realmente las transacciones en la red.


## Construcción de transacciones y Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Edificio Bitcoin Transacciones y P2SH


La construcción de transacciones Bitcoin tiende un puente entre el conocimiento teórico del protocolo y la implementación práctica. Una transacción selecciona UTXOs para gastar, construye salidas con scripts de bloqueo, crea firmas para cada entrada y serializa todo en el formato exacto que esperan los nodos. El proceso requiere comprender la generación de sighash, el comportamiento de los scripts y la correcta gestión de tasas y cambios.


### Construcción de transacciones básicas


Cada entrada de transacción hace referencia a una salida anterior por txid e índice. Las salidas especifican importes en satoshis y secuencias de bloqueo. La diferencia entre el total de entradas y el total de salidas es la tasa. Para firmar una entrada, se serializa una versión modificada de la transacción, se calcula su sighash y la clave privada la firma. La firma resultante y la clave pública forman el ScriptSig. Una vez firmada cada entrada, la transacción en bruto puede difundirse a la red.


### Transacciones multifirma


Bare multisig utiliza `OP_CHECKMULTISIG` para requerir m-de-n firmas. Debido a un error inicial, OP_CHECKMULTISIG consume un elemento extra de la pila, requiriendo un `OP_0` inicial en el ScriptSig. Bare multisig es funcional pero ineficiente: todas las claves públicas aparecen on-chain, lo que hace que las scriptPubKeys sean grandes, caras y difíciles de codificar como direcciones. Estas limitaciones motivaron la introducción de pay-to-script-hash.


#### Arquitectura P2SH

P2SH oculta los scripts complejos tras un HASH160 de 20 bytes. La scriptPubKey es fija: `OP_HASH160 <hash de 20 bytes> OP_EQUAL`. El script de redención subyacente -que contiene multisig, timelocks u otras condiciones- sólo se revela y ejecuta cuando se gasta. El emisor sólo ve el hash, mientras que el receptor gestiona el script de canje de forma privada. Este diseño reduce el tamaño de on-chain, mejora la privacidad y permite contratos complejos sin sobrecargar a los remitentes.


### P2SH Gasto y aplicación


Para pasar una salida P2SH, el ScriptSig debe incluir los datos de desbloqueo necesarios *más* el propio script de canje. La validación se produce en dos pasos:

1) HASH160(redeem_script) debe coincidir con el hash scriptPubKey.

2) Tras la verificación, se ejecuta el script de redención con los datos proporcionados.


Al generar firmas para una entrada P2SH, el proceso sighash utiliza el script redeem en lugar del scriptPubKey. Cada firmante debe poseer el script redeem completo para que las firmas generate sean válidas. Las direcciones P2SH utilizan el byte de versión 0x05 en mainnet (direcciones "3...") y 0xC4 en testnet (direcciones "2...").


#### Consideraciones prácticas sobre seguridad


Perder un script de canje significa perder fondos: para gastar se necesitan tanto las claves privadas como el propio script de canje. Los participantes de Multisig deben verificar que sus claves públicas están correctamente incluidas antes de aceptar depósitos. P2SH admite construcciones avanzadas como multisig, timelocks y hashlocks, pero los errores en la lógica del script pueden bloquear los fondos permanentemente, por lo que es esencial realizar pruebas en testnet.


P2SH mejora la privacidad ocultando las condiciones de gasto hasta el primer gasto, pero una vez que aparece la secuencia de comandos de canje on-chain, se hace visible de forma permanente. A pesar de ello, las ventajas de tamaño reducido, compatibilidad con versiones anteriores y compatibilidad con contratos flexibles hicieron de P2SH un hito importante, que influyó en actualizaciones posteriores como SegWit y Taproot.


# Funcionamiento interno de la red Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Bloques y Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Los bloques Bitcoin agrupan transacciones y las aseguran mediante proof of work. Cada bloque incluye una cabecera de 80 bytes y una lista de transacciones. A pesar del elevado coste energético de producir un bloque válido, verificarlo es barato: almacenar todas las ~900k cabeceras requiere sólo ~72 MB, lo que permite que incluso los dispositivos pequeños verifiquen la proof of work de la cadena con eficacia.


### Transacciones en Coinbase y recompensas en bloque


Cada bloque comienza exactamente con una transacción de Coinbase, la única forma de que entren nuevos bitcoins en circulación. Tiene un hash prev-tx a cero y un índice de 0xffffffff, que lo identifica de forma única. La subvención comenzó en 50 BTC y se reduce a la mitad cada 210.000 bloques (50, 25, 12,5, 6,25, 3,125, ...). Los mineros también incluyen comisiones por transacción. Dado que el nonce de 4 bytes es demasiado pequeño para los ASIC modernos, los mineros modifican los datos de la transacción de Coinbase para cambiar la raíz de Merkle y crear un espacio de búsqueda adicional. BIP34 requiere incrustar la altura del bloque en el scriptSig de Coinbase para asegurar que cada txid de Coinbase es único.


### Campos de cabecera de bloque y señalización Soft Fork


La cabecera de 80 bytes contiene:


- versión (4 bytes)
- hash del bloque anterior (32 bytes)
- Raíz Merkle (32 bytes)
- marca de tiempo (4 bytes)
- bits (objetivo de dificultad, 4 bytes)
- nonce (4 bytes)


Los números de versión evolucionaron hasta convertirse en un sistema de señalización de campos de bits a través de BIP9, permitiendo a los mineros coordinar la preparación del soft-fork. La marca de tiempo es un valor de tiempo Unix de 32 bits y deberá actualizarse en torno al año 2106.


#### Bits Campo y Objetivos

El campo bits codifica el objetivo de forma compacta: objetivo = coeficiente × 256^(exponente-3). Los hashes de bloque válidos deben estar numéricamente por debajo de este objetivo. Dado que los hashes se interpretan como enteros little-endian, los hashes válidos suelen aparecer con muchos ceros al final cuando se muestran en hexadecimal.


### Dificultad, validación y ajustes


La dificultad se define como objetivo_más_bajo / objetivo_actual, expresando cuánto más difícil es mining hoy en día comparado con la dificultad más fácil posible. La validación sólo requiere comparar el hash de la cabecera con el objetivo, lo que resulta extremadamente barato en comparación con mining.


Cada bloque de 2016, Bitcoin ajusta la dificultad para apuntar a intervalos de bloque de ~10 minutos. El ajuste compara el tiempo real de los bloques anteriores de 2016 con las dos semanas previstas. Los límites limitan los ajustes a un factor de cuatro. Acontecimientos importantes del mundo real, como la prohibición de mining en China, demostraron la resistencia de este mecanismo cuando la tasa de hash cayó bruscamente y la dificultad se ajustó a la baja para compensar.


### Subvención en bloque y total Supply


La subvención a la altura h se calcula como: subvención = 5_000_000_000 >> (h // 210_000). Así se obtiene el programa de reducción a la mitad que converge hacia una oferta total de ~21 millones de BTC. La suma de las series geométricas (50 + 25 + 12,5 + ...) × 210.000 explica el tope. Los mineros pueden reclamar menos de la subvención permitida, pero nunca más, o el bloque deja de ser válido. A medida que las subvenciones se reducen en las sucesivas mitades, las comisiones por transacción se convierten en un componente cada vez más importante de los ingresos de los mineros y de la seguridad de la red a largo plazo.


## Comunicación en red y árboles de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Arquitectura de red


La red peer-to-peer de Bitcoin funciona como un sistema de cotilleo descentralizado en el que los nodos retransmiten transacciones y bloques sin confiar los unos en los otros. Los nuevos nodos arrancan poniéndose en contacto con semillas DNS codificadas y mantenidas por los desarrolladores del núcleo. Estas semillas DNS devuelven las IP de los pares activos, lo que permite a los nodos descubrir la red y solicitar pares adicionales a través de getaddr. Intencionadamente, la red no es crítica para el consenso, por lo que las implementaciones pueden diferir siempre que las reglas de consenso permanezcan inalteradas.


### Estructura del mensaje y Handshake


Todos los mensajes Bitcoin P2P utilizan una envoltura fija: un valor mágico de 4 bytes (F9BEB4D9 para mainnet), un comando ASCII de 12 bytes, una longitud de carga útil little-endian de 4 bytes, una suma de comprobación de 4 bytes (los 4 primeros bytes de hash256) y la carga útil. Los comandos más comunes son version, verack, inv, getdata, tx, block, getheaders, headers, ping y pong.


El apretón de manos comienza cuando un nodo de conexión envía un mensaje de versión. El receptor responde con verack y su propia versión. Una vez que ambas partes intercambian estos dos mensajes, la conexión está activa y los nodos pueden empezar a transmitir inventarios y datos.


### Árboles de Merkle y raíces de Merkle


Bitcoin almacena una única raíz Merkle de 32 bytes en la cabecera de cada bloque como compromiso de todas las transacciones del bloque. Las transacciones se someten a hash (hash256), se emparejan, se concatenan y se someten a hash repetidamente hasta que queda un hash. Cuando un nivel tiene un recuento impar, se duplica el último hash. Internamente, los hashes son big-endian, mientras que los datos serializados del bloque utilizan little-endian, lo que requiere inversiones antes y después de la construcción del árbol.


#### Pruebas de Merkle y SPV

Las pruebas Merkle permiten verificar que una transacción está incluida en un bloque sin necesidad de descargar el bloque completo. La prueba consiste en hashes hermanos a lo largo de la ruta hasta la raíz. Los clientes SPV ligeros sólo almacenan las cabeceras de bloque y solicitan estas pruebas a los nodos completos. Dado que un árbol de Merkle crece logarítmicamente, demostrar la inclusión en un bloque con miles de transacciones sólo requiere unos cientos de bytes.


Taproot amplía este concepto comprometiendo las condiciones de gasto a un árbol de scripts Merklized (MAST), revelando sólo la rama ejecutada junto con una prueba Merkle. Esto mejora tanto la eficiencia como la privacidad.


### Operaciones de red y sincronización de bloques


Los nodos utilizan getdata para solicitar transacciones o bloques, especificando un identificador de tipo (1=tx, 2=bloque, 3=bloque filtrado, 4=bloque compacto) más un identificador de 32 bytes. Para la sincronización en cadena, los nodos envían getheaders con un hash de bloque inicial, recibiendo como respuesta hasta 2000 cabeceras. Cada cabecera devuelta consta de 80 bytes seguidos de un recuento de transacciones ficticio de cero.


La verificación completa de los bloques recibidos requiere dos comprobaciones:

1. El hash del bloque debe estar por debajo del objetivo codificado en el campo bits.

2. La raíz Merkle calculada a partir de todas las transacciones (con un tratamiento adecuado de la endogeneidad) debe coincidir con la raíz de la cabecera.


Sólo si se cumplen ambas condiciones acepta un nodo el bloque, lo que refleja el principio de Bitcoin de "no confiar, verificar".


## Comunicación avanzada entre nodos y testigos segregados

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Esta sesión unifica las redes avanzadas P2P con Segregated Witness, mostrando cómo el software moderno Bitcoin interactúa directamente con los nodos a la vez que utiliza estructuras de transacción SegWit-aware. Los desarrolladores aprenderán a recuperar bloques, buscar transacciones relevantes y construir transacciones utilizando únicamente comunicación de red sin procesar, sin necesidad de exploradores de bloques.


### Recuperación de transacciones basadas en bloques y privacidad


Los monederos deben detectar los pagos entrantes escaneando bloques en busca de salidas que coincidan con su scriptPubKey. La recuperación de bloques completos protege la privacidad mejor que la solicitud de transacciones individuales, que filtra fuertes señales sobre la actividad del usuario. Incluso las solicitudes de bloques pueden filtrar información en cadenas de bajo volumen, lo que hace que los filtros de bloques compactos (BIP158) sean esenciales para los clientes ligeros que preservan la privacidad. Los filtros pueden producir falsos positivos pero nunca falsos negativos, permitiendo a los clientes descargar sólo bloques potencialmente relevantes sin revelar direcciones específicas.


### Trustless Interacción en red


El flujo de trabajo `get_block` demuestra el uso adecuado de la red: enviar getdata, recibir un bloque y, a continuación, verificar de forma independiente su raíz Merkle y proof of work. Un bloque sólo se acepta si el hash de cabecera recibido coincide con el hash solicitado y su raíz Merkle calculada coincide con la cabecera. De este modo, se garantiza que ni siquiera los pares maliciosos puedan engañar a los nodos para que acepten datos alterados.


#### Recuperación de transacciones de bloques

Las transacciones de un bloque pueden escanearse en busca de scriptPubKeys coincidentes mediante una simple iteración. Los monederos de producción realizan esto continuamente a medida que llegan nuevos bloques, demostrando la propiedad de las salidas estrictamente a través de la validación criptográfica en lugar de depender de API de terceros.


### SegWit Objetivos y diseño


El Testigo Segregado (SegWit) solucionó la maleabilidad de las transacciones eliminando los datos de firma del cálculo del txid. Esto permitió cadenas de transacciones prefirmadas fiables e hizo que Lightning Network resultara práctico. SegWit también aumentó la capacidad de bloques mediante el "peso del bloque": los nodos antiguos siguen viendo bloques de ≤1 MB, mientras que los nodos actualizados validan hasta 4 MB, incluidos los datos del testigo. Los programas testigo versionados (v0-v1 hasta ahora) crean una ruta de actualización estructurada para futuros tipos de script.


#### P2WPKH (Nativo SegWit)


P2WPKH sustituye la estructura P2PKH heredada por una secuencia de 22 bytes: OP_0 + push20 + hash160(pubkey). Spending traslada la firma y la pubkey a un campo testigo independiente.


- Nodos anteriores a SegWit: ver "cualquiera puede gastar", tratarlo como válido.
- Nodos post-SegWit: reconocen OP_0 + hash de 20 bytes y validan usando datos testigo.


Esta separación soluciona la maleabilidad y reduce las tasas. El testigo utiliza un recuento varint seguido de la firma y la pubkey.


#### P2SH-P2WPKH (Compatible con SegWit)


Para permitir que los monederos antiguos envíen a direcciones SegWit, los scripts P2WPKH pueden envolverse en P2SH.


- scriptPubKey: estándar P2SH hash160(redeemScript)
- scriptSig: el redeemScript (el programa P2WPKH)
- testigo: firma + pubkey


Capas de validación:

1. Los nodos anteriores al BIP16 aceptan el redeemScript como válido.

2. Los nodos post-BIP16 lo evalúan, dejando OP_0 + hash en la pila.

3. Los nodos SegWit realizan una validación completa de testigos.


#### P2WSH para scripts complejos


P2WSH generaliza SegWit para multisig y scripts avanzados al comprometerse con SHA256(script) en lugar de hash160. Una típica pila de testigos multisig 2-de-3:


- elemento vacío (error CHECKMULTISIG)
- sig1
- sig2
- guión testigo (el guión multisig)


Los nodos SegWit verifican que SHA256(witnessScript) coincide con el hash scriptPubKey y luego lo ejecutan. El uso de SHA256 y un hash de 32 bytes permite distinguir P2WSH de P2WPKH y refuerza la seguridad.


#### P2SH-P2WSH (Compatibilidad máxima)


Las secuencias de comandos complejas de SegWit también pueden envolverse con P2SH:


- scriptSig: redeemScript (OP_0 + hash de 32 bytes)
- testigo: firmas + witnessScript


La validación pasa por tres generaciones de reglas exactamente igual que con P2SH-P2WPKH. Esta envoltura era esencial para las primeras implantaciones de Lightning que necesitaban multisig sin maleabilidad. Aunque hoy en día se prefiere P2WSH nativo, la forma envolvente garantiza la compatibilidad con los sistemas wallet más antiguos.


### Impacto de SegWit


SegWit proporcionado:


- identificadores de transacción estables
- reducción de las tasas mediante descuentos en los datos de los testigos
- mayor rendimiento de los bloques gracias a su peso
- compatibilidad para nodos antiguos
- una vía de actualización limpia para Taproot y futuras ampliaciones


Junto con la interacción en red sin confianza, estas herramientas forman la espina dorsal del desarrollo moderno de Bitcoin.



# Sección final


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Opiniones y valoraciones


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusión



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>