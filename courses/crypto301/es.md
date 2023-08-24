---
name: Introducción a la criptografía
goal: Comprender la creación de una billetera Bitcoin desde una perspectiva criptográfica
objectives:
  - Desmitificar la terminología de la criptografía relacionada con Bitcoin.
  - Dominar la creación de una billetera Bitcoin.
  - Comprender la estructura de una billetera Bitcoin.
  - Comprender las direcciones y la ruta de derivación.
---

# Un viaje al corazón de la criptografía

**Atención: este curso ha sido traducido íntegramente por AI y aún no ha sido revisado. Si desea hacerlo, por favor contribuya al [github] (https://github.com/DecouvreBitcoin/sovereign-university-data/tree/main/courses/crypto301).**

¿Estás fascinado por Bitcoin? ¿Te preguntas cómo funciona una billetera Bitcoin? ¡Prepárate para embarcarte en un viaje cautivador al corazón de la criptografía! Loïc, nuestro experto, te guiará a través de los entresijos de la creación de una billetera Bitcoin, revelando los misterios detrás de los términos técnicos intimidantes como el hash, la derivación de claves y las curvas elípticas.

Este curso no solo te proporcionará los conocimientos para comprender la estructura de una billetera Bitcoin, sino que también te preparará para sumergirte más profundamente en el apasionante mundo de la criptografía. Entonces, ¿estás listo para emprender este viaje? ¡Únete a nosotros y convierte tu curiosidad en habilidad!

+++

# Introducción a la criptografía

![introducción por Rogzy](https://youtu.be/ul8zU5QWIXg)

Nos complace darles la bienvenida al nuevo curso titulado "Crypto 301: Introducción a la criptografía y a la billetera HD", dirigido por el experto en la materia, Loïc Morel. Este curso te sumergirá en el fascinante mundo de la criptografía, esta disciplina fundamental de las matemáticas que garantiza el cifrado y la seguridad de tus datos.

En nuestra vida cotidiana y especialmente en el campo de los Bitcoins, la criptografía juega un papel primordial. Los conceptos relacionados con ella, como las claves privadas, públicas, las direcciones, las rutas de derivación, la semilla y la entropía, son fundamentales para el uso y la creación de una billetera Bitcoin. A lo largo de este curso, Loïc te explicará en detalle cómo se crean las claves privadas y cómo están relacionadas con las direcciones. Loïc también dedicará una hora a explicarte los detalles matemáticos de la curva elíptica. Además, comprenderás por qué es importante utilizar HMAC SHA512 para asegurar tu billetera y cuál es la diferencia entre la semilla y la frase mnemotécnica.
El objetivo final de esta formación es permitirle comprender técnicamente los procesos de creación de una cartera HD y los métodos criptográficos utilizados. A lo largo de los años, las carteras de Bitcoin han evolucionado para ser más fáciles de usar, más seguras y estandarizadas gracias a BIP específicos. Loïc le ayudará a comprender estos BIP para comprender las decisiones de los desarrolladores de Bitcoin y los criptógrafos. Como todos los cursos ofrecidos por nuestra universidad, este es completamente gratuito y de código abierto. Esto significa que puede tomarlo y usarlo libremente a su gusto. Esperamos recibir sus comentarios al final de este emocionante curso.
![intro por loïc](https://youtu.be/mwuxXLk4Kws)

Hola a todos, soy Loïc Morel, su guía en este viaje técnico de exploración de la criptografía utilizada en las carteras de Bitcoin.

Nuestro viaje comienza con una inmersión en las profundidades de las funciones de hash criptográficas. Juntos desmontaremos los engranajes del imprescindible SHA256 y exploraremos varios algoritmos dedicados a la derivación.

Continuaremos nuestra aventura descifrando el mundo misterioso de las firmas digitales. Descubrirá cómo la magia de las curvas elípticas se aplica a estas firmas, y arrojaremos luz sobre cómo calcular la clave pública a partir de la clave privada. Y, por supuesto, abordaremos el proceso de firma digital.

Luego, retrocederemos en el tiempo para ver la evolución de las carteras de Bitcoin, y nos aventuraremos en los conceptos de entropía y números aleatorios. Repasaremos la famosa frase mnemotécnica, mientras abrimos un paréntesis sobre la frase de contraseña. ¡Incluso tendrás la oportunidad de vivir una experiencia única creando una semilla a partir de 128 lanzamientos de dados!

Con estas bases sólidas, estaremos listos para la parte crucial: la creación de una cartera de Bitcoin. Desde el nacimiento de la semilla y la clave maestra, pasando por el estudio de las claves extendidas, hasta la derivación de pares de claves secundarias, cada paso será analizado en detalle. También discutiremos la estructura de la cartera y las rutas de derivación.

Para coronarlo todo, terminaremos nuestro recorrido examinando las direcciones de Bitcoin. Explicaremos cómo se crean y cómo desempeñan un papel fundamental en el funcionamiento de las carteras de Bitcoin.

Embárquese conmigo en este fascinante viaje y prepárese para explorar el mundo de la criptografía como nunca antes. Deje sus preconcepciones en la puerta y abra su mente a una nueva forma de comprender Bitcoin y su estructura fundamental.

# Las funciones de hash

## Introducción a las funciones de hash criptográfico relacionadas con Bitcoin

![2.1 - les fonctions de hachage cryptographiques](https://youtu.be/dvnGArYvVr8)

Bienvenidos a nuestra sesión de hoy dedicada a sumergirnos en el mundo criptográfico de las funciones de hash, un elemento fundamental para la seguridad del protocolo Bitcoin. Imagina una función de hash como un robot descifrador criptográfico altamente eficiente que transforma información de cualquier tamaño en una huella digital única y de tamaño fijo, llamada "hash", "huella" o "resumen".

En resumen, una función de hash toma como entrada un mensaje de tamaño arbitrario y lo convierte en una huella de tamaño fijo como salida.

Describir el perfil de las funciones de hash criptográficas requiere entender dos cualidades esenciales: su irreversibilidad y su resistencia a la falsificación.

La irreversibilidad, o resistencia a la preimagen, significa que el cálculo de la salida a partir de la entrada se puede realizar fácilmente, pero el cálculo inverso, es decir, encontrar la entrada a partir de la salida, es imposible. Es una función de sentido único.

![image](assets/image/section1/0.JPG)

La resistencia a la falsificación proviene del hecho de que cualquier modificación en la entrada dará como resultado una salida completamente diferente. Estas funciones permiten verificar la integridad de los software descargados.

![image](assets/image/section1/1.JPG)

Otra característica crucial que poseen es su resistencia a las colisiones y a la segunda preimagen. Una colisión ocurre cuando dos entradas distintas producen la misma salida. Si bien en el mundo de las funciones de hash las colisiones son inevitables, una excelente función de hash criptográfica las minimiza considerablemente. El riesgo debe ser tan bajo que se pueda considerar nulo. Es como si cada hash fuera una casa en una ciudad enorme; a pesar del gran número de casas, una buena función de hash garantiza que cada casa tenga una dirección única.
La resistencia a la segunda preimagen depende de la resistencia a las colisiones; si hay resistencia a las colisiones, entonces hay resistencia a la segunda preimagen. Dado un dato de entrada impuesto, se debe encontrar una segunda entrada diferente de la primera que produzca una colisión en la salida del hash. La resistencia a la segunda preimagen es similar a la resistencia a las colisiones, excepto por el hecho de que la entrada está impuesta.
Ahora naveguemos por las turbulentas aguas de las funciones de hash obsoletas. SHA0, SHA1 y MD5 son consideradas hoy en día como cascarones oxidados en el océano de la criptografía de hash. A menudo se desaconsejan porque han perdido su resistencia a las colisiones. El principio de los cajones explica por qué, a pesar de nuestros mejores esfuerzos, es imposible evitar las colisiones debido a la limitación del tamaño de la salida. Para ser verdaderamente considerada segura, una función de hash debe resistir las colisiones, la segunda preimagen y la preimagen.

Como elemento clave en el protocolo Bitcoin, la función de hash SHA-256 es el capitán del barco. Otras funciones, como SHA-512, se utilizan para la derivación con HMAC y PBKDF. Además, RIPMD160 se utiliza para reducir una huella a 160 bits. Cuando hablamos de HASH256 y HASH160, nos referimos al uso de una doble hash con SHA-256 y RIPMD.

Para HASH256, es una doble hash del mensaje con la función SHA256.

$$
SHA256(SHA256(mensaje))
$$

Para HASH160, es una doble hash del mensaje utilizando primero la función SHA256 y luego RIPMD160.

$$
RIPMD160(SHA256(mensaje))
$$

El uso de HASH160 es especialmente ventajoso porque permite beneficiarse de la seguridad de SHA-256 mientras se reduce el tamaño de la huella.

En resumen, el objetivo final de una función de hash criptográfica es transformar una información de tamaño arbitrario en una huella de tamaño fijo. Para ser reconocida como segura, debe tener varias características: irreversibilidad, resistencia a la falsificación, resistencia a las colisiones y resistencia a la segunda preimagen.

![imagen](assets/image/section1/2.JPG)

Al final de esta exploración, hemos desmitificado las funciones de hash criptográficas, destacado su uso en el protocolo Bitcoin y analizado sus objetivos específicos. Hemos aprendido que para considerarse seguras, las funciones de hash deben ser resistentes a la preimagen, a la segunda preimagen, a las colisiones y a la falsificación. También hemos recorrido el espectro de las diferentes funciones de hash utilizadas en el protocolo Bitcoin. En nuestra próxima sesión, nos sumergiremos en el corazón de la función de hash SHA256 y descubriremos las fascinantes matemáticas que le confieren sus características únicas.

## Los engranajes de SHA256

![Los engranajes de SHA256](https://youtu.be/74SWg_ZbUj4)

Bienvenidos a la continuación de nuestro fascinante viaje a través de los laberintos criptográficos de la función de hash. Hoy levantamos el velo sobre los misterios de SHA256, un proceso complejo pero ingenioso que presentamos anteriormente.
Para recordar, el objetivo de la función de hash SHA256 es tomar un mensaje de cualquier tamaño como entrada y generar un hash de 256 bits como salida.

### Preprocesamiento

Avancemos un paso más en este laberinto, comenzando por el preprocesamiento de SHA256.

#### Bits de relleno

El objetivo de este primer paso es tener un mensaje igualado a un múltiplo de 512 bits. Para lograr esto, agregaremos bits de relleno al mensaje.

Sea M el tamaño del mensaje inicial.
Sea 1 un bit reservado para el separador.
Sea P el número de bits utilizados para el relleno y 64 el número de bits reservados para la segunda fase de preprocesamiento.
El total debe ser un múltiplo de 512 bits, que es lo que representa n.

![image](assets/image/section1/3.JPG)

Ejemplo con un mensaje de entrada de 950 bits:

```
Paso 1: Determinar el tamaño; el número final de bits ideal.
El primer múltiplo de 512 > (M + 64 + 1) (con M = 950) es 1024.
1024 = 2 * 512
Entonces n = 2.

Paso 2: Determinar P, el número de bits de relleno necesarios para alcanzar el número final de bits ideal.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 940 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Por lo tanto, se deben agregar 9 bits de relleno para tener un mensaje igualado a un múltiplo de 512.
```

¿Y ahora?
Justo después del mensaje inicial, debemos agregar el separador 1 seguido de P, que en nuestro ejemplo es igual a nueve 0.

```
mensaje + 1 000 000 000
```

#### Relleno del tamaño

Ahora pasamos a la segunda fase del preprocesamiento, que implica agregar la representación binaria del tamaño del mensaje inicial, en bits.

Retomemos el ejemplo con una entrada de 950 bits:

```
La representación binaria del número 950 es: 11 1011 0110

Utilizamos nuestros 64 bits reservados en el paso anterior. Agregamos ceros para redondear nuestros 64 bits a nuestra entrada equilibrada. Luego, fusionamos el mensaje inicial, el relleno de bits y el relleno del tamaño para obtener nuestra entrada igualada.
```

Aquí está el resultado:

![image](assets/image/section1/4.JPG)

### El procesamiento

#### Requisitos previos para la comprensión

##### Las constantes y vectores de inicialización

Ahora nos estamos preparando para los primeros pasos en el procesamiento de la función SHA-256. Como con cualquier buena receta, necesitamos algunos ingredientes básicos, que llamamos constantes y vectores de inicialización.
Los vectores de inicialización, de A a H, son los 32 primeros bits de las partes decimales de las raíces cuadradas de los 8 primeros números primos. Se utilizarán como valores base en las primeras etapas del proceso. Sus valores están en formato hexadecimal.

Las constantes K, de 0 a 63, representan los 32 primeros bits de las partes decimales de las raíces cúbicas de los 64 primeros números primos. Se utilizan en cada ronda de la función de compresión. Sus valores también están en formato hexadecimal.

![image](assets/image/section1/5.JPG)

##### Las operaciones utilizadas

Dentro de la función de compresión, utilizamos operadores específicos como XOR, AND y NOT. Procesamos los bits uno a uno según su rango, utilizando el operador XOR y una tabla de verdad. El operador AND se utiliza para devolver 1 sólo si ambos operandos son iguales a 1, y el operador NOT para devolver el valor opuesto de un operando. También utilizamos la operación SHR para desplazar los bits a la derecha un número determinado.

La tabla de verdad :

![image](assets/image/section1/6.JPG)

Operaciones de desplazamiento de bits :

![image](assets/image/section1/7.JPG)

#### La función de compresión

Antes de aplicar la función de compresión, dividimos la entrada en bloques de 512 bits. Cada bloque se procesará independientemente de los demás.

A continuación, cada bloque de 512 bits se divide en W trozos de 32 bits. De este modo, W(0) representa los 32 primeros bits del bloque de 512 bits. W(1) representa los 32 bits siguientes y así sucesivamente hasta alcanzar los 512 bits del bloque.

Una vez definidas todas las constantes K y los trozos W, podemos procesar los siguientes cálculos para cada trozo W en cada ronda.

Realizamos 64 rondas de cálculo en la función de compresión. En la última ronda, en la "Salida de la función", tendremos un estado intermedio que se añadirá al estado inicial de la función de compresión.

A continuación, repetimos todos estos pasos en la función de compresión en el siguiente bloque de 512 bits, hasta llegar al último bloque.

Todas las sumas de la función de compresión son sumas en módulo 2^32 para mantener siempre una suma de 32 bits.

![image](assets/image/section1/9.JPG)

![image](activos/imagen/sección1/8.JPG)

##### Un recorrido por la función de compresión

![image](assets/image/section1/11.JPG)

![image](assets/image/section1/10.JPG)
El recorrido de la función de compresión se realizará 64 veces. En la entrada encontramos nuestras piezas W y nuestras constantes K definidas anteriormente.
Los cuadrados/cruces rojos corresponden a una suma módulo 2^32 bits.

Las entradas A, B, C, D, E, F, G, H se asociarán con un valor de 32 bits para hacer un total de 32 \* 8 = 256 bits.
También encontramos, como salida, una nueva secuencia A, B, C, D, E, F, G, H. Esta salida luego se utilizará como entrada en la siguiente ronda y así sucesivamente hasta el final de la 64ª ronda.

Los valores de la secuencia de entrada en la primera ronda de la función de compresión corresponden a los vectores de inicialización predefinidos mencionados anteriormente.
Como recordatorio, los vectores de inicialización representan los 32 primeros bits de las partes decimales de las raíces cuadradas de los primeros 8 números primos.

Aquí está el ejemplo de una ronda:

![image](assets/image/section1/12.1.png)

##### El estado intermedio

Como recordatorio, el mensaje se divide en bloques de 512 bits que luego se dividen en piezas de 32 bits. Para cada bloque de 512 bits, aplicamos las 64 rondas de la función de compresión.
El estado intermedio corresponde al final de las 64 rondas de un bloque. Los valores de la secuencia de salida de esta 64ª ronda se utilizan como valores iniciales de la secuencia de entrada en la primera ronda del siguiente bloque.

![image](assets/image/section1/12.2.png)

#### Visión general de la función de hash

![image](assets/image/section1/13.JPG)

Notaremos que la salida de la primera pieza de mensaje de 512 bits corresponde a nuestros vectores de inicialización en la entrada de la segunda pieza de mensaje, y así sucesivamente.

La salida de la última ronda, de la última pieza, corresponde al resultado final de la función SHA256.

En conclusión, nos gustaría destacar el papel crucial de los cálculos realizados en las cajas CH, MAJ, σ0 y σ1. Estas operaciones, entre otras, son los guardianes que aseguran la robustez de la función de hash SHA256 frente a ataques, lo que la convierte en una elección preferida para la seguridad de muchos sistemas digitales, especialmente dentro del protocolo Bitcoin. Es evidente que, aunque sea compleja, la belleza de SHA256 radica en su capacidad para encontrar la entrada a partir del hash, mientras que la verificación del hash para una entrada dada es una acción mecánicamente simple.

## Los algoritmos utilizados para la derivación

![Los algoritmos utilizados para la derivación](https://youtu.be/ZF1_BMsOJXc)

Los algoritmos de derivación HMAC y PBKDF2 son componentes clave en la mecánica de seguridad del protocolo Bitcoin. Previenen una variedad de posibles ataques y garantizan la integridad de las carteras de Bitcoin.
HMAC y PBKDF2 son herramientas criptográficas utilizadas para diferentes tareas en Bitcoin. HMAC se utiliza principalmente para contrarrestar los ataques de extensión de longitud durante la derivación de las carteras deterministas jerárquicamente (HD), mientras que PBKDF2 se utiliza para convertir una frase mnemotécnica en una semilla.

#### HMAC-SHA512

El par HMAC-SHA512 tiene dos entradas: un mensaje m (Entrada 1) y una clave K elegida arbitrariamente por el usuario (Entrada 2).
También tiene una salida de tamaño fijo: 512 bits

```
Notemos:
- m: mensaje de tamaño arbitrario elegido por el usuario (entrada 1)
- K: clave arbitraria elegida por el usuario (entrada 2)
- K': la clave K igualada. Se ha ajustado al tamaño B de los bloques.
- ||: operación de concatenación.
- opad: constante definida por el byte 0x5c repetido B veces.
- ipad: constante definida por el byte 0x36 repetido B veces.
- B: el tamaño de los bloques de la función hash utilizada.
```

![image](assets/image/section1/14.JPG)

HMAC-SHA512, que toma un mensaje y una clave como entradas, genera una salida de tamaño fijo. Para asegurar la uniformidad, la clave se ajusta según el tamaño de los bloques utilizados en la función hash. En el contexto de la derivación de carteras HD, se utiliza HMAC-SHA-512. Este último funciona con bloques de 1024 bits (128 bytes) y ajusta la clave en consecuencia. Utiliza las constantes OPAD (0x5c) e IPAD (0x36), repetidas tantas veces como sea necesario para reforzar la seguridad.

El proceso de HMAC-SHA-512 implica la concatenación del resultado de aplicar SHA-512 a la clave XOR OPAD y la clave XOR IPAD con el mensaje. Cuando se utiliza con bloques de 1024 bits (128 bytes), la clave de entrada se completa con ceros si es necesario, y luego se realiza una operación XOR con IPAD y OPAD. La clave modificada de esta manera se concatena luego con el mensaje.

![image](assets/image/section1/15.JPG)

El código de cadena, al integrar una fuente adicional de entropía, aumenta la seguridad de las claves derivadas. Sin él, un ataque podría comprometer toda la cartera y robar todos los bitcoins.

#### PBKDF2

PBKDF2 se utiliza para convertir una frase mnemotécnica en una semilla. En este caso, en la entrada 1, podemos encontrar la frase mnemotécnica y en la entrada 2, la frase de paso.'
Este algoritmo realiza 2048 rondas utilizando HMAC SHA512. Gracias a estos algoritmos de derivación, dos entradas diferentes pueden producir una salida única y fija, lo que soluciona el problema de posibles ataques de extensión de longitud en las funciones de la familia SHA-2. Un ataque de extensión de longitud aprovecha una propiedad específica de algunas funciones de hash criptográficas. En dicho ataque, un atacante que ya posee el hash de un mensaje desconocido puede utilizarlo para calcular el hash de un mensaje más largo, que es una extensión del mensaje original. Esto a menudo es posible sin conocer el contenido del mensaje original, lo que puede llevar a importantes vulnerabilidades de seguridad si este tipo de función de hash se utiliza para tareas como la verificación de integridad.

![image](assets/image/section1/16.JPG)

En conclusión, los algoritmos HMAC y PBKDF2 desempeñan roles esenciales en la seguridad de la derivación de las carteras HD en el protocolo Bitcoin. El HMAC-SHA-512 se utiliza para protegerse contra los ataques de extensión de longitud, mientras que PBKDF2 permite convertir la frase mnemotécnica en una semilla. El código de cadena agrega una fuente adicional de entropía en la derivación de claves, asegurando así la robustez del sistema.

# Las firmas digitales

## Firmas digitales y curvas elípticas

![Firmas digitales y curvas elípticas](https://youtu.be/gOjYiPkx4z8)

¿Dónde se almacenan esos famosos bitcoins? No en una cartera Bitcoin, como se podría pensar. En realidad, una cartera Bitcoin guarda las claves privadas necesarias para demostrar la posesión de los bitcoins. Los propios bitcoins se registran en la cadena de bloques, una base de datos descentralizada que archiva todas las transacciones.

En el sistema Bitcoin, la unidad de cuenta es el bitcoin (nota la "b" minúscula). Este último es divisible hasta ocho decimales, siendo la unidad más pequeña el satoshi. Los UTXO, o "Unspent Transaction Output" (Salida de Transacción No Gastada), representan las salidas de transacciones no gastadas que pertenecen a una clave pública que está matemáticamente vinculada a una clave privada. Para gastar estos bitcoins, es necesario cumplir con la condición de gasto de la transacción. Una condición de gasto típica consiste en demostrar al resto de la red que el usuario es el propietario legítimo de la clave pública asociada a los UTXO. Para hacerlo, deberá demostrar que está en posesión de la clave privada correspondiente a la clave pública vinculada a cada UTXO sin revelar la clave privada.
Esto es lo que permite la firma digital. Sirve como prueba matemática que demuestra la posesión de una clave privada asociada a una clave pública específica. Esta técnica de protección de datos se basa principalmente en un fascinante campo de la criptografía llamado criptografía de curva elíptica (ECC).

La firma puede ser verificada matemáticamente por las otras partes involucradas en la red de Bitcoin.

![image](assets/image/section2/0.JPG)

Para asegurar la seguridad de las transacciones, Bitcoin utiliza dos protocolos de firma digital: ECDSA (Elliptic Curve Digital Signature Algorithm) y Schnorr. ECDSA es un protocolo de firma incorporado en Bitcoin desde su lanzamiento en 2009, mientras que las firmas de Schnorr fueron agregadas más recientemente, en noviembre de 2021. Aunque ambos protocolos se basan en la criptografía de curva elíptica y utilizan mecanismos matemáticos similares, difieren principalmente en términos de estructura de firma.

En este curso, presentaremos el algoritmo ECDSA.

### ¿Qué es una curva elíptica?

La criptografía de curva elíptica es un conjunto de algoritmos que utilizan una curva elíptica por sus diferentes propiedades geométricas y matemáticas con fines criptográficos, y cuya seguridad se basa en la dificultad de calcular el logaritmo discreto.

Las curvas elípticas son útiles en una variedad de aplicaciones criptográficas en el protocolo Bitcoin, desde intercambios de claves hasta cifrado asimétrico y firmas digitales.

Las curvas elípticas tienen propiedades interesantes:

- Simetría: Cualquier línea no vertical que corte dos puntos en la curva elíptica, también cortará la curva en un tercer punto.
- Cualquier línea no vertical y tangente a la curva en un punto, siempre cortará la curva en un segundo punto único.

El protocolo Bitcoin utiliza una curva elíptica particular llamada Secp256k1 para realizar sus operaciones criptográficas.

Antes de adentrarnos más en estos mecanismos de firma, es importante comprender qué es una curva elíptica. Una curva elíptica se define por la ecuación y² = x³ + ax + b. Cada punto en esta curva tiene una simetría distintiva que es clave para su utilidad en criptografía.

![image](assets/image/section2/1.JPG)

En última instancia, varias curvas elípticas son reconocidas como seguras para su uso criptográfico. La más conocida quizás sea la curva secp256r1. Sin embargo, para Bitcoin, Satoshi Nakamoto optó por otra curva: secp256k1.

Esta curva se define por los parámetros a=0 y b=7, y su ecuación es y² = x³ + 7 módulo n, donde n representa el número primo que determina el orden de la curva.

![image](assets/image/section2/2.JPG)
La première image representa la curva secp256k1 en el cuerpo de los números reales y su ecuación. La segunda imagen es una representación de la curva secp256k1 en el cuerpo ZP, el cuerpo de los números enteros naturales y positivos, módulo p donde p es un número primo. Esto se asemeja a una nube de puntos. Utilizamos este cuerpo de números enteros y positivos para evitar aproximaciones.
p es un número primo, es el orden de la curva que se utiliza.
Finalmente, la ecuación que se utiliza en el protocolo Bitcoin es:

$$
y^2 = (x^3 + 7) mod(p)
$$

La ecuación de la curva elíptica en Bitcoin corresponde a la última ecuación en la imagen anterior.

En la próxima sección de este curso, utilizaremos curvas que están en el cuerpo de los números reales simplemente para facilitar la comprensión.

### Calcular la clave pública a partir de la clave privada

![Calculer la clé publique depuis la clé privée](https://youtu.be/NJENwFU889Y)

Para comenzar, sumerjámonos en el mundo del algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin utiliza este algoritmo de firma digital para vincular las claves privadas y públicas. En este sistema, la clave privada es un número aleatorio o pseudoaleatorio de 256 bits. El número total de posibilidades para una clave privada es teóricamente de 2^256, pero en realidad es ligeramente inferior a eso. Para ser precisos, algunas claves privadas de 256 bits no son válidas para Bitcoin.

Para ser compatible con Bitcoin, una clave privada debe estar entre 1 y n-1, donde n representa el orden de la curva elíptica. Esto significa que el número total de posibilidades para una clave privada de Bitcoin es casi igual a 1,158 x 10^77. Para poner esto en perspectiva, es aproximadamente la misma cantidad de átomos presentes en el universo observable.

![image](assets/image/section2/3.JPG)

La clave privada única, denotada como k, luego se utiliza para determinar una clave pública.

La clave pública, denotada como K, es un punto en la curva elíptica que se deriva de la clave privada utilizando algoritmos irreversibles como ECDSA. Cuando tenemos conocimiento de la clave privada, es muy fácil encontrar la clave pública, pero cuando solo tenemos la clave pública, es imposible encontrar la clave privada. Esta irreversibilidad es la piedra angular de la seguridad de la billetera Bitcoin.

La clave pública tiene 512 bits ya que corresponde a un punto en la curva con una coordenada x de 256 bits y una coordenada y de 256 bits. Sin embargo, puede comprimirse en un número de 264 bits.

![image](assets/image/section2/4.JPG)
El punto generador (G) es el punto en la curva a partir del cual se generan todas las claves públicas en el protocolo Bitcoin. Tiene coordenadas x e y específicas, generalmente representadas en hexadecimal. Para secp256k1, las coordenadas G son, en hexadecimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Este punto es útil para derivar todas las claves públicas. Para calcular la clave pública K, simplemente se multiplica el punto G por la clave privada k, de la siguiente manera: K = k.G

Ahora vamos a estudiar cómo sumar y multiplicar puntos en las curvas elípticas.

#### Suma y duplicación de puntos en las curvas elípticas

##### Sumar dos puntos M + L

Una de las propiedades notables de las curvas elípticas es que una línea no vertical que intersecta la curva en dos puntos también intersectará la curva en un tercer punto, llamado punto O en nuestro ejemplo. Esta propiedad se utiliza para determinar el punto U, que es el opuesto del punto O.

M + L = U

![image](assets/image/section2/5.JPG)

##### Sumar un punto consigo mismo = Duplicación de punto

La suma de un punto G consigo mismo se realiza trazando una tangente a la curva en ese punto. Esta tangente, según las propiedades de las curvas elípticas, intersectará la curva en un segundo punto único -J. El opuesto de este punto, J, es el resultado de sumar el punto G consigo mismo.
G + G = J

De hecho, el punto G es el punto de partida para calcular todas las claves públicas de los usuarios del sistema Bitcoin.

![image](assets/image/section2/6.JPG)

#### Producto escalar en curvas elípticas

El producto escalar de un punto por n implica sumar ese punto consigo mismo n veces.

De la misma manera que en la duplicación de punto, el producto escalar del punto G por un punto n se realiza trazando una tangente a la curva en el punto G. Esta tangente, según las propiedades de las curvas elípticas, intersectará la curva en un segundo punto único -2G. El opuesto de este punto, 2G, es el resultado de sumar el punto G consigo mismo.

Si n = 4, entonces se repite la operación hasta llegar a 4G.

![image](assets/image/section2/7.JPG)

Aquí hay un ejemplo de cálculo para 3G:

![image](assets/image/section2/8.JPG)
Estas operaciones en los puntos de una curva elíptica son la base para el cálculo de claves públicas. La derivación de una clave pública sabiendo la clave privada es muy fácil. Una clave pública es un punto en la curva elíptica, es el resultado de nuestra adición y duplicación del punto G k veces. Con k = clave privada.

En este ejemplo:

- La clave privada k = 4
- La clave pública K = kG = 4G

![image](assets/image/section2/9.JPG)

Conociendo la clave privada k, es fácil calcular la clave pública K. Sin embargo, es imposible recuperar la clave privada a partir de la clave pública. ¿Es el resultado de una adición o de una duplicación de punto?

En nuestra próxima lección, exploraremos cómo se realiza una firma digital utilizando el algoritmo ECDSA con una clave privada para gastar bitcoins.

## Firmar con la clave privada

![Firmar con la clave privada](https://youtu.be/h2hIyGgPqkM)

El proceso de firma digital es un método clave para demostrar que eres el titular de una clave privada sin tener que revelarla. Esto se logra utilizando el algoritmo ECDSA, que incluye la determinación de un nonce único, el cálculo de un número específico, V, y la creación de una firma digital compuesta por dos partes, S1 y S2.
Es crucial siempre utilizar un nonce único para evitar ataques de seguridad. Un ejemplo notorio de lo que puede suceder cuando esta regla no se cumple es el caso del pirateo de la PlayStation 3, que fue comprometida debido a la reutilización del nonce.

![](assets/image/section2/10.JPG)

Pasos:

- Determinar un nonce v, es decir, un número único aleatorio.
  Nonce = Number Only Use Once.
  Es determinado por quien realiza la firma.
- Calcular mediante adición y duplicación de punto en la curva elíptica a partir del punto G, la posición de V en la curva elíptica.
  Tal que V = v.G
  x e y son las coordenadas de V en el plano.
- Calcular S1.
  S1 = x mod n con n = el orden de la curva y x una coordenada de V en el plano.
  Nota: El número de posibilidades de la clave pública es mayor que el número de puntos en la curva elíptica en el cuerpo finito de los enteros positivos que se utiliza en Bitcoin.
  El orden de la curva corresponde únicamente a las posibilidades que puede tomar la clave pública en la curva.
- Calcular S2.
  H(Tx) = Hash de la transacción
  k = la clave privada
- Calcular la firma: la concatenación de S1 + S2.
- Calcular P, el cálculo de verificación de la firma.
  K = la clave pública.
  Por ejemplo, para obtener la clave pública 3G, dibujas una tangente al punto G, calculas el opuesto de -G para obtener 2G, luego sumas G y 2G. Para realizar una transacción, debes demostrar que conoces el número 3 desbloqueando los bitcoins asociados a la clave pública 3G.
  Para crear una firma digital y demostrar que conoces la clave privada asociada a la clave pública 3G, primero calculas un nonce, luego el punto V asociado a este nonce (en el ejemplo dado, es 4G). Luego, calculas el punto T sumando la clave pública 3G y el punto V, lo que da 7G.

![image](assets/image/section2/11.JPG)

Vamos a simplificar el proceso de firma digital.
En la imagen anterior, la clave privada k = 3.
Podemos calcular fácilmente la clave pública K asociada a esta clave privada: K = 3G
Luego, generamos pseudoaleatoriamente un nonce: v = 4.
A partir de este nonce, es posible calcular V tal que: V = v.G = 4G.

A partir de este punto V, calculamos el punto T tal que:
T = t.G = 7G (con t = 7)

Es hora de proceder a la verificación de la firma digital.

La verificación de una firma digital es un paso crucial en el uso del algoritmo ECDSA, que permite confirmar la autenticidad de un mensaje firmado sin necesidad de la clave privada del remitente. Esto es cómo se lleva a cabo en detalle:

En nuestro ejemplo, tenemos dos valores importantes: t y V.
t es un valor numérico (7 en este ejemplo), y V es un punto en la curva elíptica (representado por 4G aquí). Estos valores se generan durante la creación de la firma digital y luego se envían junto con el mensaje para permitir la verificación.

Cuando el verificador recibe el mensaje, también recibirá estos dos valores, t y V.

Estos son los pasos que el verificador seguirá para validar la firma:

1. Primero calculará el hash del mensaje, que llamaremos H.
2. Luego calculará u1 y u2. Para hacer esto, utilizará las siguientes fórmulas:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Donde S2 es la segunda parte de la firma digital, n es el orden de la curva elíptica y (S2)^-1 es el inverso de S2 mod n.
3. Luego, el verificador calculará un punto P' en la curva elíptica utilizando la fórmula: P' = u1 _ G + u2 _ K
   - G es el punto de generación de la curva
   - K es la clave pública del remitente
4. El verificador calculará entonces I', que es simplemente la coordenada x del punto P' módulo n. 5. Finalmente, el verificador confirmará que I' es igual a t. Si es así, la firma se considera válida. Si no es así, la firma es inválida.

Esta procedimiento garantiza que solo el remitente que posee la clave privada correspondiente podría haber producido una firma que pase este proceso de verificación.

![image](assets/image/section2/12.JPG)

Simplificando:
Quien produce la firma proporcionará al verificador el número t (en nuestro ejemplo, t = 7) y el punto V.

Es imposible determinar la clave pública o la clave privada a partir del número 7 y el número V.

Los pasos para verificar la firma digital son los siguientes:

- En la curva, se suma el punto de la clave pública con el punto V para obtener el punto T'.
- Se calcula el número t.G
- Se verifica que el resultado de t.G sea igual al número T'

En conclusión, la verificación de una firma digital es un procedimiento esencial en las transacciones de Bitcoin. Permite garantizar que el mensaje firmado no ha sido alterado durante su transmisión y que el remitente es el titular de la clave privada. Esta técnica de autenticación digital se basa en principios matemáticos complejos, como la aritmética de curva elíptica, al tiempo que mantiene la confidencialidad de la clave privada. Ofrece una sólida base de seguridad para las transacciones criptográficas.

Dicho esto, la gestión de estas claves, así como su creación, es otra cuestión esencial en Bitcoin. ¿Cómo generar un nuevo par de claves? ¿Cómo organizar de manera segura y eficiente una multitud de claves? ¿Cómo recuperarlas si es necesario?

Para responder a estas preguntas y profundizar en su comprensión de la seguridad de la criptografía, nuestro próximo curso se centrará en el concepto de Billetera Determinista Jerárquica (HD wallets) y el uso de frases mnemotécnicas. Estos mecanismos ofrecen formas elegantes de gestionar eficientemente sus claves de criptomonedas mientras refuerzan la seguridad.

# La frase mnemotécnica

## Evolución de las billeteras de Bitcoin

![Evolución de las billeteras de Bitcoin](https://youtu.be/6tmu1R9cXyk)

La Billetera Determinista Jerárquica, o comúnmente conocida como billetera HD, desempeña un papel fundamental en el ecosistema de las criptomonedas. El término "billetera" puede parecer engañoso para aquellos que son novatos en este campo, ya que no implica la posesión de dinero o moneda. Más bien se refiere a una colección de claves criptográficas privadas.
Los primeros monederos eran software que agrupaba claves privadas generadas de manera pseudoaleatoria pero que no tenían ninguna conexión entre ellas. Estos monederos se llaman "Just a Bunch Of Keys" (JBOK).

Como las claves no tienen ninguna conexión entre ellas, el usuario está obligado a realizar una nueva copia de seguridad para cada nuevo par de claves generado.

Ya sea que el usuario utilice siempre el mismo par de claves y pierda en confidencialidad, o que genere un nuevo par de claves de manera aleatoria y, por lo tanto, deba realizar una nueva copia de seguridad de estas claves.

![image](assets/image/section3/0.JPG)

Sin embargo, la complejidad de la gestión de estas claves se compensa con un conjunto de protocolos llamados Propuestas de Mejora de Bitcoin (BIP, por sus siglas en inglés). Estas propuestas de actualización son fundamentales para la funcionalidad y seguridad de los monederos HD. Por ejemplo, el [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanzado en 2012, revolucionó la forma en que se generan y almacenan estas claves, al introducir el concepto de claves derivadas de manera determinista y jerárquica. La idea es derivar todas las claves de forma determinista y jerárquica a partir de una única información: la semilla. De esta manera, el proceso de copia de seguridad de estas claves se simplifica enormemente, manteniendo al mismo tiempo su nivel de seguridad.

![image](assets/image/section3/1.JPG)

Posteriormente, el [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introdujo una innovación destacada: la frase mnemotécnica de 24 palabras. Este sistema permitió transformar una secuencia de números compleja y difícil de recordar en una serie de palabras comunes, mucho más fáciles de memorizar y almacenar. Además, el [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) propuso agregar una frase adicional para fortalecer la seguridad de las claves individuales. Estas mejoras sucesivas llevaron a las normas BIP43 y BIP44, que estandarizaron la estructura y jerarquía de los monederos HD, haciéndolos más accesibles y fáciles de usar para el público en general.

En las siguientes secciones, profundizaremos en el funcionamiento de los monederos HD. Abordaremos los principios de derivación de claves y examinaremos los conceptos fundamentales de la entropía y la generación de números aleatorios, que son esenciales para garantizar la seguridad de su monedero HD.
En resumen, es esencial destacar el papel central de BIP32 y BIP39 en el diseño y la seguridad de las carteras HD. Estos protocolos permiten generar múltiples claves a partir de una única semilla, que se supone que es un número aleatorio o pseudoaleatorio. Hoy en día, estas normas son adoptadas por la mayoría de las carteras de criptomonedas, ya sea que estén dedicadas a una sola criptomoneda o que admitan varios tipos de monedas.

## Entropía y número aleatorio

![Entropía y número aleatorio](https://youtu.be/k18yH18w2TE)

La importancia de la seguridad de las claves privadas en el ecosistema de Bitcoin es innegable. De hecho, son la piedra angular que garantiza la seguridad de las transacciones de Bitcoin. Para evitar cualquier vulnerabilidad asociada a la previsibilidad, estas claves deben generarse de manera verdaderamente aleatoria, lo cual puede resultar rápidamente en un ejercicio laborioso. El problema es que en informática es imposible generar un número verdaderamente aleatorio, ya que inevitablemente proviene de un proceso determinista; un código.
Por eso es esencial informarse sobre los diferentes Generadores de Números Aleatorios (RNG). Los tipos de RNG varían, desde los Generadores de Números Pseudoaleatorios (PRNG) hasta los Generadores de Números Verdaderamente Aleatorios (TRNG), así como los PRNG que incorporan una fuente de entropía.

La entropía se refiere al estado de "desorden" de un sistema. A partir de una entropía externa, es decir, una fuente de información externa, es posible utilizar un generador de números aleatorios para obtener un número aleatorio.

![imagen](assets/image/section3/2.JPG)

Veamos juntos cómo funciona un Generador de Números Pseudoaleatorios (PRNG).

Toma como entrada una semilla, es decir, una información que corresponderá al estado interno 0.
En este estado interno, se aplica una función de transformación y el resultado, que es un número pseudoaleatorio, corresponde al estado interno 1.
En este estado interno 1, nuevamente se aplica una función de transformación que resulta en un nuevo número aleatorio = estado interno 2.
Y así sucesivamente.

La principal desventaja es que cualquier semilla idéntica siempre dará el mismo resultado de salida. Y también, si conocemos el resultado de las funciones de transformación desde el principio, podremos recuperar el número aleatorio en la salida del proceso.

Un ejemplo de función de transformación es la función PBKDF2.

**En resumen, un PRNG criptográficamente seguro debe:**

- ser estadísticamente aleatorio
- ser impredecible
- ser resistente incluso si los resultados se revelan
- tener un período lo suficientemente largo

![imagen](assets/image/section3/3.JPG)
En el caso de Bitcoin, las claves privadas se generan a partir de una única información en la base de la billetera. Esta información permite una derivación determinista y jerárquica de pares de claves secundarias. La entropía es la base de todas las billeteras HD, aunque no existe un estándar para la generación de este número aleatorio. Por lo tanto, la generación de números aleatorios es un desafío importante para asegurar las transacciones de Bitcoin.
![image](assets/image/section3/4.JPG)

La fase de verificación de la generación de claves es crucial para garantizar la seguridad y autenticidad de la generación de números aleatorios, un paso fundamental para prevenir cualquier vulnerabilidad asociada a la previsibilidad. Por lo tanto, se recomienda encarecidamente utilizar billeteras de código abierto para permitir esta verificación.

Sin embargo, es importante tener en cuenta que algunas billeteras de hardware pueden ser "de código cerrado", lo que hace imposible verificar la generación del número aleatorio. Una posible solución sería generar su propia frase mnemotécnica utilizando dados, aunque este enfoque puede presentar ciertos riesgos.

El uso de una frase de contraseña generada aleatoriamente puede ayudar a mitigar estos riesgos.

En última instancia, la aleatoriedad ocupa un lugar central en la criptografía y la informática, y la capacidad de generar aleatoriedad de manera segura es crucial para garantizar la seguridad de las claves privadas y las transacciones de Bitcoin. La entropía, que es el corazón de la billetera HD de Bitcoin, es esencial para su seguridad. En nuestra próxima lección, continuaremos explorando este tema, abordando más en detalle cómo la entropía contribuye a la seguridad de las billeteras HD.

## La frase mnemotécnica

![La frase mnemotécnica](https://youtu.be/uJERqH9Xp7I)

La seguridad de una billetera de Bitcoin es una preocupación importante para todos sus usuarios. Una forma esencial de asegurar la copia de seguridad de la billetera es generar una frase mnemotécnica basada en la entropía y la suma de verificación.

![image](assets/image/section3/5.JPG)

Para convertir la entropía en una frase mnemotécnica, simplemente se calcula la suma de verificación de la entropía y se concatena la entropía y la suma de verificación.

Una vez que se genera la entropía, se utiliza la función SHA256 en la entropía para crear un hash. Se obtienen los primeros 8 bits del hash, que son la suma de verificación. La frase mnemotécnica es el resultado de la entropía más la suma de verificación.

La suma de verificación asegura la verificación de la precisión de la frase de recuperación. Sin esta suma de verificación, un error en la frase podría resultar en la creación de una billetera diferente y, por lo tanto, en la pérdida de fondos. Se obtiene la suma de verificación pasando la entropía por la función SHA256 y obteniendo los primeros 8 bits del hash.

![image](assets/image/section3/6.JPG)

Existen diferentes estándares para la frase mnemotécnica según el tamaño de la entropía. El estándar más comúnmente utilizado para una frase de recuperación de 24 palabras es una entropía de 256 bits. El tamaño del checksum se determina dividiendo el tamaño de la entropía por 32.

Por ejemplo, una entropía de 256 bits genera un checksum de 8 bits. La concatenación de la entropía y el checksum resulta en tamaños respectivos de 128 bits, 160 bits, etc. Según el tamaño de la entropía, la frase de recuperación contendrá 12 palabras para 128 bits, 15 palabras para 160 bits y 24 palabras para 256 bits.

**Codificación de la frase mnemotécnica:**

![image](assets/image/section3/7.JPG)

Los últimos 8 bits corresponden al checksum.
Cada segmento de 11 bits se convierte en decimal.
Cada decimal corresponde a una palabra de una lista de 2048 palabras en BIP39. Es importante destacar que ninguna palabra tiene las cuatro primeras letras en el mismo orden.

Es esencial guardar la frase de recuperación de 24 palabras para preservar la integridad de la billetera de Bitcoin. Los dos estándares más comúnmente utilizados se basan en una entropía de 128 o 256 bits y una concatenación de 12 o 24 palabras. Agregar una passphrase constituye una opción adicional para fortalecer la seguridad de la billetera.

En conclusión, la generación de una frase mnemotécnica para asegurar una billetera de Bitcoin es un proceso crucial. Es importante cumplir con los estándares de la frase mnemotécnica según el tamaño de la entropía. La copia de seguridad de la frase de recuperación de 24 palabras es esencial para evitar cualquier pérdida de fondos.

## La passphrase

![La passphrase](https://youtu.be/dZkOYO7MXwc)

La passphrase es una contraseña adicional que se puede agregar a una billetera de Bitcoin para aumentar su seguridad. Su uso es opcional y queda a discreción del usuario. Al agregar información arbitraria que, junto con la frase mnemotécnica, permite calcular la semilla de la billetera, la passphrase refuerza la seguridad de la misma.

![image](assets/image/section3/8.JPG)

La passphrase es una sal criptográfica opcional de un tamaño elegido por el usuario. Permite mejorar la seguridad de una billetera HD al agregar información arbitraria que, una vez agregada a la frase mnemotécnica, permitirá calcular la semilla.
Cuando se establece al crear una cartera, es necesario para la derivación de todas las claves de la cartera. La función pbkdf2 se utiliza para generar la semilla a partir de la frase de contraseña. Esta semilla permite derivar todas las claves secundarias de la cartera. Si se modifica la frase de contraseña, la cartera de Bitcoin se vuelve completamente diferente.
La frase de contraseña es una herramienta esencial para fortalecer la seguridad de las carteras de Bitcoin. Puede permitir la aplicación de diversas estrategias de seguridad. Por ejemplo, se puede utilizar para crear duplicados y facilitar las copias de seguridad de la frase mnemotécnica. También puede mejorar la seguridad de la cartera al mitigar los riesgos asociados con la generación aleatoria de la frase mnemotécnica.

Una frase de contraseña efectiva debe ser larga (de 20 a 40 caracteres) y diversa (utilizando mayúsculas, minúsculas, números y símbolos). No debe estar directamente relacionada con el usuario o su entorno. Es más seguro utilizar una secuencia aleatoria de caracteres en lugar de una palabra simple como frase de contraseña.

![image](assets/image/section3/9.JPG)

Una frase de contraseña es más segura que una simple contraseña. La frase de contraseña ideal es larga, variada y aleatoria. Puede fortalecer la seguridad de una cartera o software caliente. También se puede utilizar para crear copias de seguridad redundantes y seguras.

Es crucial cuidar las copias de seguridad de la frase de contraseña para evitar perder el acceso a la cartera. Una frase de contraseña es una opción para una cartera HD. Puede generarse aleatoriamente con dados u otro generador de números pseudoaleatorios.

# Creación de una cartera de Bitcoin

## Creación de la semilla y la clave maestra

![Creación de la semilla y la clave maestra](https://youtu.be/56yAt_JDWhY)

En esta parte del curso, exploraremos los pasos para derivar una cartera HD (Hierarchical Deterministic Wallet), que permite crear y gestionar claves privadas y públicas de manera jerárquica y determinista.

![image](assets/image/section4/0.JPG)

La base de la cartera HD se basa en dos elementos esenciales: la frase mnemotécnica y la frase de contraseña (opcional). Juntos, forman la semilla, una secuencia alfanumérica de 512 bits que sirve como base para derivar las claves de la cartera. A partir de esta semilla, es posible derivar todas las claves secundarias de la cartera de Bitcoin. La semilla es la clave para acceder a todos los bitcoins asociados con la cartera, ya sea que se utilice una frase de contraseña o no.

![image](assets/image/section4/1.JPG)
Para obtener la semilla, se utiliza la función pbkdf2 (Password-Based Key Derivation Function 2) con la frase mnemotécnica y la frase de contraseña. La salida de pbkdf2 es una semilla de 512 bits.
A partir de la semilla, es posible determinar la clave privada maestra y el código de cadena utilizando el algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Este algoritmo requiere un mensaje y una clave de entrada para generar un resultado. La clave privada maestra se calcula a partir de la semilla y la frase "Bitcoin SEED". Esta frase es idéntica para todas las derivaciones de todas las carteras HD, garantizando así una coherencia entre las carteras.

Inicialmente, la función SHA-512 no estaba implementada en el protocolo Bitcoin, por eso se utiliza HMAC SHA-512. El uso de HMAC SHA-512 con la frase "Bitcoin SEED" obliga al usuario a generar una cartera específica para Bitcoin. El resultado de HMAC SHA-512 es un número de 512 bits, dividido en dos partes: los 256 bits de la izquierda representan la clave privada maestra, mientras que los 256 bits de la derecha representan el código de cadena maestro.

![image](assets/image/section4/2.JPG)

La clave privada maestra es la clave principal de todas las futuras claves de la cartera, mientras que el código de cadena maestro interviene en la derivación de las claves hijas. Es importante destacar que es imposible derivar un par de claves hijas sin conocer el código de cadena correspondiente del par padre.

Un par de claves en la cartera incluye una clave privada, una clave pública y un código de cadena. El código de cadena permite introducir una fuente de aleatoriedad en la derivación de las claves hijas y aislar cada par de claves para evitar cualquier fuga de información.

Es importante señalar que la clave privada maestra es la primera clave privada derivada a partir de la semilla y no tiene ninguna relación con las claves extendidas de la cartera.

En el próximo curso, exploraremos en detalle las claves extendidas, como xPub, xPRV, zPub, y entenderemos por qué se utilizan y cómo se construyen.

## Las claves extendidas

![Las claves extendidas](https://youtu.be/TRz760E_zUY)

En esta parte del curso, estudiaremos las claves extendidas (xPub, zPub, yPub) y sus prefijos, que desempeñan un papel importante en la derivación de las claves hijas en una cartera HD (Hierarchical Deterministic Wallet).

![image](assets/image/section4/3.JPG)

Las claves extendidas se distinguen de las claves maestras. Una billetera HD genera una frase mnemotécnica y una semilla para obtener la clave maestra y el código de cadena maestro. Las claves extendidas se utilizan para derivar claves hijas y requieren tanto la clave padre como el código de cadena correspondiente. Una clave extendida combina esta información para simplificar el proceso de derivación.

![image](assets/image/section4/4.JPG)

Las claves públicas extendidas solo pueden derivar claves públicas hijas normales, mientras que las claves privadas extendidas permiten derivar claves públicas y privadas hijas, ya sea en una derivación normal o endurecida.
La derivación endurecida es la derivación desde la clave padre privada. La derivación normal corresponde a la derivación desde la clave padre pública.

El uso de claves extendidas con el prefijo XPUB permite derivar nuevas direcciones sin retroceder hasta las claves privadas correspondientes, lo que ofrece una mayor seguridad. Los metadatos asociados con las claves extendidas proporcionan información importante sobre su función y posición en la jerarquía de claves.

Las claves extendidas se identifican por prefijos específicos (XPRV, XPUB, YPUB, ZPUB) que indican si es una clave extendida privada o pública, así como su propósito específico. Los metadatos asociados con una clave extendida incluyen la versión (prefijo), la profundidad, la huella de la clave pública, el índice y la carga útil (código de cadena y clave padre).

![image](assets/image/section4/5.JPG)

La versión corresponde al tipo de clave: xpub, xprv, ...

La profundidad corresponde al número de derivaciones entre padre-hijo que ha habido desde la clave maestra.

La huella del padre son los primeros 4 bytes del hash 160 de la clave padre.

El índice es el número de par que se utiliza para generar la clave extendida entre sus hermanas. (hermanas = claves del mismo nivel)
ejemplo: si queremos derivar el xpub de nuestra tercera cuenta, su índice será 2 (porque el índice comienza en 0).

La carga útil está compuesta por el código de cadena (32 bytes) y la clave padre (33 bytes).

Las claves públicas comprimidas tienen un tamaño de 33 bytes, mientras que las claves públicas sin procesar son de 512 bits. Las claves públicas comprimidas conservan la misma información que las claves sin procesar, pero con un tamaño reducido. Las claves extendidas tienen un tamaño de 82 bytes y su prefijo se representa en base 58 mediante una conversión hexadecimal. El checksum se calcula utilizando la función de hash HASH256.

![image](assets/image/section4/6.JPG)

Las derivaciones reforzadas comienzan a partir de los índices que son potencias de 2 (2^31). Es interesante destacar que los prefijos más comúnmente utilizados son xpub y zpub, que corresponden respectivamente a los estándares legacy y segwit v1 y segwit v0.
En nuestra próxima lección, nos enfocaremos en la derivación de pares de claves hijas utilizando los conocimientos adquiridos sobre claves extendidas y la clave maestra de la billetera.

## Derivación de pares de claves hijas

![Derivación de pares de claves hijas](https://youtu.be/FXhI-GmE9Aw)

Como recordatorio, hemos abordado el cálculo de la semilla y la clave maestra, que son los primeros elementos esenciales para la jerarquización y derivación de la billetera HD (Hierarchical Deterministic Wallet). La semilla, de longitud de 128 a 256 bits, se genera de forma aleatoria o a partir de una frase secreta. Juega un papel determinista en la derivación de todas las demás claves. La clave maestra es la primera clave derivada de la semilla y permite derivar todos los demás pares de claves hijas.

El código de cadena maestra juega un papel importante en la recuperación de la billetera a partir de la semilla. Es importante destacar que todas las claves derivadas de la misma semilla tendrán el mismo código de cadena maestra.

![imagen](assets/image/section4/7.JPG)

La jerarquización y derivación de la billetera HD ofrecen una gestión más eficiente de las claves y las estructuras de la billetera. Las claves extendidas permiten la derivación de un par de claves hijo a partir de un par padre utilizando cálculos matemáticos y algoritmos específicos.

Existen diferentes tipos de pares de claves hijas, incluyendo claves reforzadas y claves normales. La clave pública extendida solo permite la derivación de claves públicas hijas normales, mientras que la clave privada extendida permite la derivación de todas las claves hijas, tanto públicas como privadas, ya sea en modo normal o reforzado. Cada par de claves tiene un índice que permite diferenciarlas entre sí.

![imagen](assets/image/section4/8.JPG)

La derivación de claves hijas utiliza la función HMAC-SHA512 utilizando la clave padre concatenada con el índice y el código de cadena asociado al par de claves. Las claves hijas normales tienen un índice que va desde 0 hasta 2 elevado a la potencia 31 menos 1, mientras que las claves hijas reforzadas tienen un índice que va desde 2 elevado a la potencia 31 hasta 2 elevado a la potencia 32 menos 1.

![imagen](assets/image/section4/9.JPG)

![imagen](assets/image/section4/10.JPG)

Existen dos tipos de pares de claves secundarias: pares reforzados y pares normales. El proceso de derivación de las claves secundarias utiliza las claves públicas para generar las condiciones de gasto, mientras que las claves privadas se utilizan para la firma. La clave pública extendida solo permite la derivación de claves secundarias públicas normales, mientras que la clave privada extendida permite la derivación de todas las claves secundarias, tanto públicas como privadas, en modo normal o reforzado.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

La derivación reforzada utiliza la clave privada principal, mientras que la derivación normal utiliza la clave pública principal. La función HMAC-SHA512 se utiliza para la derivación reforzada, mientras que la derivación normal utiliza un resumen de 512 bits. La clave pública secundaria se obtiene multiplicando la clave privada secundaria por el generador de la curva elíptica.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

La jerarquización y derivación de múltiples pares de claves de manera determinista permite crear un esquema de árbol para la derivación jerárquica. En el próximo curso de esta formación, estudiaremos la estructura de la cartera HD y los caminos de derivación, centrándonos especialmente en las notaciones de los caminos de derivación.

## Estructura de la cartera y caminos de derivación

![Estructura de la cartera y caminos de derivación](https://youtu.be/etO9UxwyE2I)

En este capítulo, estudiaremos la estructura del árbol de derivación en una cartera HD (Hierarchical Deterministic Wallet). Ya hemos explorado el cálculo de la semilla, la clave maestra y la derivación de los pares de claves secundarias. Ahora nos centraremos en la organización de las claves dentro de la cartera.

La cartera HD utiliza capas de profundidad para organizar las claves. Cada derivación de un par principal a un par secundario corresponde a una capa de profundidad.

![image](assets/image/section4/15.JPG)

- La profundidad 0 corresponde a la clave maestra y al código de cadena maestro.

- La profundidad 1 se utiliza para derivar claves secundarias según un objetivo específico, que está determinado por el índice. Los objetivos cumplen con los estándares BIP 84 y Segwit v0/v1.

- La profundidad 2 permite diferenciar las cuentas de diferentes criptomonedas o redes. Esto permite organizar la cartera según las diferentes fuentes de fondos. Para bitcoin, el índice será 0.

- La profundidad 3 se utiliza para organizar la cartera en diferentes cuentas, ofreciendo así una estructura más clara y organizada.
- La profundidad 4 corresponde a las cadenas interna y externa, que se utilizan para las direcciones destinadas a ser comunicadas públicamente. El índice 0 está asociado a la cadena externa, mientras que el índice 1 está asociado a la cadena interna. Cada cuenta tiene dos cadenas: la cadena externa (0) y la cadena interna (1). La profundidad 4 también se utiliza para gestionar los tipos de script en el caso de las carteras multi firma.
- La profundidad 5 se utiliza para las direcciones de recepción en una cartera clásica. En la siguiente sección, examinaremos más detalladamente la derivación de pares de claves hijas.

![image](assets/image/section4/16.JPG)

Para cada capa de profundidad, utilizamos índices para diferenciar los pares de claves hijas.

El índice sin apóstrofe corresponde al índice real utilizado, mientras que el índice con apóstrofe corresponde al índice real + 2^31. Las derivaciones reforzadas utilizan índices de 2^31 a 2^32-1. Por ejemplo, el índice 44' corresponde al índice real 2^31 + 44.

Para generar una dirección de recepción específica, derivamos un par de claves hijas de la clave maestra y el código de cadena maestra. Luego, utilizamos el índice para diferenciar los diferentes pares de claves hijas de la misma profundidad.

Las claves extendidas, como XPUB, permiten compartir su cartera con varias personas. La cadena de derivación se utiliza para diferenciar la cadena externa (direcciones destinadas a ser comunicadas) y la cadena interna (direcciones de cambio).

En el próximo capítulo, estudiaremos las direcciones de recepción, sus ventajas de uso y los pasos para su construcción.

# ¿Qué es una dirección Bitcoin?

## Las direcciones Bitcoin

![Las direcciones Bitcoin](https://youtu.be/nqGBMjPtFNI)

![image](assets/image/section5/0.JPG)

En este capítulo, exploraremos las direcciones de recepción, que desempeñan un papel crucial en el sistema Bitcoin. Permiten recibir fondos y se generan a partir de pares de claves privadas y públicas. Aunque existe un tipo de script llamado Pay2PublicKey que permite bloquear bitcoins en una clave pública, los usuarios suelen preferir utilizar direcciones de recepción en lugar de este script.

Cuando un destinatario desea recibir bitcoins, proporciona una dirección de recepción al remitente en lugar de su clave pública. Una dirección es en realidad un hash de una clave pública, con un formato específico.

![image](assets/image/section5/1.JPG)
Es importante tener en cuenta que no es posible retroceder desde la dirección hacia la clave pública, ni desde la clave pública hacia la clave privada. El uso de una dirección permite reducir el tamaño de la información de la clave pública, que inicialmente es de 512 bits.
Las direcciones de Bitcoin se han reducido en tamaño para facilitar su uso. Tienen un checksum, lo que permite detectar errores tipográficos y reducir los riesgos de pérdida de bitcoins. Por otro lado, las claves públicas no tienen un checksum, lo que significa que los errores tipográficos pueden resultar en la pérdida de los fondos correspondientes.

Las direcciones también ofrecen una segunda capa de seguridad entre la información pública y privada, lo que dificulta la toma de control de la clave privada.

Es esencial destacar que cada dirección debería ser de uso único. Reutilizar la misma dirección plantea problemas de privacidad y debe evitarse.

Se utilizan diferentes prefijos para las direcciones de Bitcoin. Por ejemplo, BC1Q corresponde a una dirección Segwit V0, BC1P a una dirección Taproot/Segwit V1, y los prefijos 1 y 3 están asociados con las direcciones Pay2PublicKeyH/Pay2ScriptH (legacy). En el próximo curso, explicaremos paso a paso la derivación de una dirección a partir de una clave pública.

## ¿Cómo crear una dirección de Bitcoin?

![¿Cómo crear una dirección de Bitcoin?](https://youtu.be/ewMGTN8dKjI)

En este capítulo, abordaremos la construcción de una dirección de recepción para las transacciones de Bitcoin. Una dirección de recepción es una representación en forma de caracteres alfanuméricos de una clave pública comprimida. La conversión de una clave pública en una dirección de recepción pasa por varias etapas.

### Etapa 1: Compresión de la clave pública

![imagen](assets/image/section5/14.png)

Una dirección se deriva de una clave pública secundaria.

Una clave pública es un punto en la curva elíptica. Gracias a la simetría de la curva elíptica, un punto en la curva elíptica tendrá una abscisa x asociada únicamente a dos posibles valores para y: positivo o negativo.
Sin embargo, en el protocolo Bitcoin, trabajamos con un cuerpo de enteros positivos finitos en lugar del cuerpo de los reales. Para distinguir entre los dos posibles valores de y, solo es necesario indicar si y es par o impar.

La compresión de una clave pública permite reducir su tamaño de 520 bits a 264 bits.

Utilizamos el prefijo 0x02 para un y par y 0x03 para un y impar. Esta es la forma comprimida de la clave pública.

### Etapa 2: Hash de la clave pública comprimida

![imagen](assets/image/section5/3.JPG)
El hash de la clave pública comprimida se realiza con la función SHA256. Luego se aplica la función RIPEMD160 al resumen.

### Etapa 3: El payload = Carga útil de la dirección

![image](assets/image/section5/4.JPG)

El resumen binario de RIPEMD160(SHA256(K)) se utiliza para formar grupos de 5 bits. Cada grupo se convierte a base16 (Hexadecimal) y/o a base 10.

### Etapa 4: Agregar metadatos para el cálculo de la suma de comprobación con el programa BCH

![image](assets/image/section5/5.JPG)

En el caso de las direcciones heredadas, utilizamos el doble hash SHA256 para generar la suma de comprobación de la dirección. Sin embargo, para las direcciones Segwit V0 y V1, utilizamos la tecnología de suma de comprobación BCH para garantizar la detección de errores. El programa BCH es capaz de sugerir y corregir errores con una probabilidad de error extremadamente baja. Actualmente, el programa BCH se utiliza para detectar y sugerir modificaciones, pero no las realiza automáticamente en lugar del usuario.

El programa BCH requiere varias entradas de información, incluido el HRP (Parte legible por humanos) que debe ser ampliado. La ampliación del HRP implica codificar cada letra en base 2 según su código ASCII. Luego, tomando los 3 primeros bits del resultado para cada letra en base 10 (en azul en la imagen). Insertar un separador 0. Luego concatenar los últimos 5 bits de cada letra previamente convertidos a base 10 (en amarillo en la imagen).

La ampliación del HRP en base 10 permite aislar los últimos cinco bits de cada carácter, fortaleciendo así la suma de comprobación.

La versión Segwit V0 está representada por el código 00 y el "payload" está en negro, en base 10. Esto es seguido por seis caracteres reservados para la suma de comprobación.

### Etapa 5: Cálculo de la suma de comprobación con el programa BCH

![image](assets/image/section5/6.JPG)

La entrada que contiene los metadatos se envía al programa BCH para obtener la suma de comprobación en base 10.

Aquí tenemos la suma de comprobación.

### Etapa 6: Construcción de la dirección y conversión a Bech32

![image](assets/image/section5/7.JPG)

La concatenación de la versión, el payload y la suma de comprobación permite construir la dirección. Luego, los caracteres en base 10 se convierten en caracteres bech32 utilizando una tabla de correspondencia. El alfabeto bech32 incluye todos los caracteres alfanuméricos, excepto 1, b, i y o, para evitar confusiones.

### Etapa 7: Agregar el HRP y el separador

![image](assets/image/section5/8.JPG)

En rosa la suma de comprobación.
En negro, el payload = el hash de la clave pública.
En azul, la versión.
El todo se convierte en Bech32, luego se agrega 'bc' para bitcoin y '1' como separador y aquí está la dirección.
Así, hemos recorrido los pasos para construir una dirección de recepción, utilizando la tecnología de checksum BCH, así como la construcción de una dirección que comienza con bc1q o bc1p utilizando la variante BCH32 de la base 32 específica de Bitcoin.

## Resumen de la criptografía para las carteras de Bitcoin

![síntesis de la formación](https://youtu.be/NkAYoVUMvOs)

Las funciones hash utilizadas en el protocolo Bitcoin tienen características necesarias para la seguridad del protocolo. Deben ser irreversibles (resistencia a la preimagen), resistentes a la falsificación, resistentes a la colisión y a la segunda preimagen.

![imagen](assets/image/section5/11.JPG)

Otro método criptográfico ampliamente utilizado en el protocolo Bitcoin es el método de las firmas digitales.

![imagen](assets/image/section5/12.JPG)

A lo largo de esta formación, hemos estudiado en profundidad la cartera determinista jerárquica (HD) con el BIP32. La entropía juega un papel central en este tipo de cartera, ya que se utiliza para generar una frase mnemotécnica a partir de un número aleatorio.

Este número aleatorio se formatea en un formato de 256 bits utilizando la función hash SHA256. El checksum corresponde a los primeros 8 bits de este resultado.
La frase mnemotécnica es la concatenación del número aleatorio con el checksum. Gracias a la lista de 2048 palabras proporcionadas en el BIP39, esta frase mnemotécnica se puede codificar en una serie de palabras fáciles de recordar. La frase mnemotécnica, junto con una posible frase de paso, son necesarias para generar la semilla de la cartera. La frase de paso actúa como una sal criptográfica que agrega una capa adicional de protección a la cartera.

La función pbkdf2 se utiliza para generar la semilla a partir de la frase mnemotécnica y la frase de paso, utilizando un HMAC-SHA512 y 2048 iteraciones. La clave maestra y el código de cadena maestro se derivan luego de esta semilla utilizando nuevamente la función HMAC-SHA512 con la frase "bitcoin seed". La clave privada maestra y el código de cadena maestro son los elementos más altos en la jerarquía de la cartera HD.

La derivación de una clave hija depende de varios factores, incluida la clave padre y el código de cadena correspondiente. Se obtiene una clave extendida concatenando una clave padre con su código de cadena, mientras que una clave maestra es una clave independiente.
Para derivar una dirección, primero se aplica una función hash SHA256 y RIPMD160 a la clave pública comprimida, luego se calcula un checksum. El doble hash SHA256 se utiliza para calcular el checksum en el caso de un estándar legacy, mientras que se utiliza el programa BCH (Bose-Chaudhuri-Hocquenghem) para calcular el checksum en el caso de un estándar segwit. Luego, se utiliza una representación en formato base 58 para un estándar legacy, mientras que se utiliza el formato bech32 para un estándar segwit, con el fin de obtener la dirección de la billetera HD.
![image](assets/image/section5/13.JPG)

En resumen, hemos explorado en detalle las funciones de hash y sus características, así como las firmas digitales y las curvas elípticas. Luego nos sumergimos en el mundo de la billetera determinista jerárquica (HD) con el BIP32, utilizando la entropía y la frase de contraseña para generar la semilla de la billetera. También aprendimos cómo derivar las claves secundarias y obtener la dirección de la billetera HD. Espero que esta información haya sido útil y ahora te animo a realizar la evaluación para poner a prueba tus conocimientos adquiridos durante el curso Crypto 301. Gracias por tu atención.
