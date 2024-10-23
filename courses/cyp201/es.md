---
name: Introducción a los algoritmos criptográficos de Bitcoin
goal: Comprender la creación de una billetera de Bitcoin desde una perspectiva criptográfica
objectives:
  - Desmitificar la terminología criptográfica relacionada con Bitcoin.
  - Dominar la creación de una billetera de Bitcoin.
  - Comprender la estructura de una billetera de Bitcoin.
  - Comprender las direcciones y los caminos de derivación.
---

# Un Viaje a la Criptografía

¿Te fascina Bitcoin? ¿Te preguntas cómo funciona una billetera de Bitcoin? ¡Prepárate para embarcarte en un cautivador viaje a la criptografía! Loïc, nuestro experto, te guiará a través de las complejidades de la creación de una billetera de Bitcoin, desentrañando los misterios detrás de términos técnicos intimidantes como el hashing, la derivación de claves y las curvas elípticas.

Este entrenamiento no solo te equipará con el conocimiento para comprender la estructura de una billetera de Bitcoin, sino que también te preparará para adentrarte en el emocionante mundo de la criptografía. Entonces, ¿estás listo para embarcarte en este viaje? ¡Únete a nosotros y convierte tu curiosidad en experiencia!

+++

# Introducción
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introducción a la Criptografía
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### ¿Este entrenamiento es para ti? ¡SÍ!

Nos complace darte la bienvenida al nuevo curso de entrenamiento titulado "Crypto 301: Introducción a la Criptografía y Billetera HD", dirigido por el experto en el campo, Loïc Morel. Este curso te sumergirá en el fascinante mundo de la criptografía, la disciplina fundamental de las matemáticas que garantiza la encriptación y seguridad de tus datos.

En nuestra vida diaria, y particularmente en el ámbito de Bitcoin, la criptografía desempeña un papel crucial. Conceptos relacionados con la criptografía, como claves privadas, claves públicas, direcciones, caminos de derivación, semilla y entropía, son fundamentales para usar y crear una billetera de Bitcoin. A lo largo de este curso, Loïc explicará en detalle cómo se generan las claves privadas y cómo están vinculadas a las direcciones. Loïc también dedicará una hora a explicar los detalles matemáticos de las curvas elípticas. Además, comprenderás por qué el uso de HMAC SHA512 es importante para asegurar tu billetera y cuál es la diferencia entre una semilla y una frase mnemotécnica.
El objetivo final de este entrenamiento es permitirte comprender los procesos técnicos involucrados en la creación de una billetera HD y los métodos criptográficos utilizados. A lo largo de los años, las billeteras de Bitcoin han evolucionado para ser más fáciles de usar, más seguras y estandarizadas gracias a BIPs específicos. Loïc te ayudará a comprender estos BIPs para comprender las decisiones tomadas por los desarrolladores de Bitcoin y los criptógrafos. Como todos los entrenamientos ofrecidos por nuestra universidad, este es completamente gratuito y de código abierto. Esto significa que eres libre de tomarlo y usarlo como desees. Esperamos recibir tus comentarios al final de este emocionante curso.

### ¡El turno es tuyo, profesor!

Hola a todos, soy Loïc Morel, su guía en esta exploración técnica de la criptografía utilizada en las billeteras de Bitcoin.

Nuestro viaje comienza con una inmersión en las profundidades de las funciones hash criptográficas. Juntos, desglosaremos el funcionamiento interno del esencial SHA256 y exploraremos varios algoritmos dedicados a la derivación.

Continuaremos nuestra aventura descifrando el misterioso mundo de las firmas digitales. Descubrirás cómo se aplica la magia de las curvas elípticas a estas firmas, y arrojaremos luz sobre cómo calcular la clave pública a partir de la clave privada. Y, por supuesto, nos adentraremos en el proceso de firma digital.
A continuación, retrocederemos en el tiempo para ver la evolución de las carteras de Bitcoin y nos adentraremos en los conceptos de entropía y números aleatorios. Repasaremos la famosa frase mnemotécnica, al tiempo que también hablaremos de la frase de contraseña. ¡Incluso tendrás la oportunidad de experimentar algo único creando una semilla a partir de 128 lanzamientos de dados!

Con estas sólidas bases, estaremos listos para la parte crucial: crear una cartera de Bitcoin. Desde el nacimiento de la semilla y la clave maestra, hasta el estudio de las claves extendidas y la derivación de pares de claves secundarias, cada paso será analizado en detalle. También discutiremos la estructura de la cartera y las rutas de derivación.

Para rematar, concluiremos nuestro viaje examinando las direcciones de Bitcoin. Explicaremos cómo se crean y cómo desempeñan un papel esencial en el funcionamiento de las carteras de Bitcoin.

Acompáñame en este cautivador viaje y prepárate para explorar el mundo de la criptografía como nunca antes. Deja tus preconcepciones en la puerta y abre tu mente a una nueva forma de entender Bitcoin y su estructura fundamental.

# Funciones de Hash
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introducción a las funciones de hash criptográficas relacionadas con Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Bienvenido a la sesión de hoy dedicada a una inmersión profunda en el mundo criptográfico de las funciones de hash, una piedra angular crucial de la seguridad del protocolo Bitcoin. Imagina una función de hash como un robot criptográfico de descifrado ultraeficiente que transforma información de cualquier tamaño en una huella digital única y de tamaño fijo, llamada "hash", "digest" o "checksum".
En resumen, una función de hash toma un mensaje de entrada de tamaño arbitrario y lo convierte en una huella digital de tamaño fijo.

Describir el perfil de las funciones de hash criptográficas requiere comprender dos cualidades esenciales: su irreversibilidad y su resistencia a la falsificación.

La irreversibilidad, o resistencia a la preimagen, significa que calcular la salida dada la entrada se puede hacer fácilmente, pero calcular la entrada a partir de la salida es imposible.
Es una función unidireccional.

![imagen](assets/image/section1/0.webp)

La resistencia a la falsificación proviene del hecho de que incluso la más mínima modificación de la entrada dará como resultado una salida profundamente diferente.
Estas funciones permiten verificar la integridad del software descargado.

![imagen](assets/image/section1/1.webp)

Otra característica crucial que poseen es su resistencia a las colisiones y a la segunda preimagen. Una colisión ocurre cuando dos entradas distintas producen la misma salida.
Ciertamente, en el universo de las funciones de hash, las colisiones son inevitables, pero una excelente función de hash criptográfica las minimiza significativamente. El riesgo debe ser tan bajo que se pueda considerar insignificante. Es como si cada hash fuera una casa en una ciudad vasta; a pesar del enorme número de casas, una buena función de hash asegura que cada casa tenga una dirección única.

La resistencia a la segunda preimagen depende de la resistencia a las colisiones; si hay resistencia a las colisiones, entonces hay resistencia a la segunda preimagen.
Dada una información de entrada que se nos impone, debemos encontrar una segunda entrada, diferente de la primera, que produzca una colisión en el hash de salida de la función. La resistencia a la segunda preimagen es similar a la resistencia a las colisiones, excepto que la entrada se impone.

Ahora navegaremos por las aguas tumultuosas de las funciones de hash obsoletas. SHA0, SHA1 y MD5 ahora se consideran conchas oxidadas en el océano de la criptografía de hash. A menudo se desaconsejan, ya que han perdido su resistencia a las colisiones. El principio del palomar explica por qué, a pesar de nuestros mejores esfuerzos, evitar las colisiones es imposible debido a la limitación del tamaño de salida. Para considerarse verdaderamente segura, una función de hash debe resistir las colisiones, las segundas preimágenes y las preimágenes.

Un elemento clave en el protocolo Bitcoin, la función hash SHA-256 es el capitán del barco. Otras funciones, como SHA-512, se utilizan para la derivación con HMAC y PBKDF. Además, RIPMD160 se utiliza para reducir una huella digital a 160 bits. Cuando nos referimos a HASH256 y HASH160, nos referimos al uso de doble hash con SHA-256 y RIPMD.

Para HASH256, es un doble hash del mensaje utilizando la función SHA256.
$$
SHA256(SHA256(mensaje))
$$
Para HASH160, es un doble hash del mensaje utilizando primero SHA256 y luego RIPMD160.
$$
RIPMD160(SHA256(mensaje))
$$
El uso de HASH160 es particularmente ventajoso ya que permite la seguridad de SHA-256 al tiempo que reduce el tamaño de la huella digital.

En resumen, el objetivo final de una función hash criptográfica es transformar información de tamaño arbitrario en una huella digital de tamaño fijo. Para ser reconocida como segura, debe tener varias fortalezas: irreversibilidad, resistencia a la manipulación, resistencia a colisiones y resistencia a segundas preimágenes.

![imagen](assets/image/section1/2.webp)

Al final de esta exploración, hemos desmitificado las funciones hash criptográficas, destacado sus usos en el protocolo Bitcoin y analizado sus objetivos específicos. Hemos aprendido que para que las funciones hash se consideren seguras, deben ser resistentes a preimágenes, segundas preimágenes, colisiones y manipulación. También hemos cubierto la variedad de diferentes funciones hash utilizadas en el protocolo Bitcoin. En nuestra próxima sesión, profundizaremos en el núcleo de la función hash SHA256 y descubriremos las fascinantes matemáticas que le otorgan sus características únicas.

## El funcionamiento interno de SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Bienvenidos a la continuación de nuestro fascinante viaje a través de los laberintos criptográficos de la función hash. Hoy, revelamos los misterios de SHA256, un proceso complejo pero ingenioso que presentamos anteriormente.
-> 950 + 1 + P + 64 = 1024-> P = 1024 - 1 - 64 - 950
-> P = 9

Por lo tanto, se deben agregar 9 bits de relleno para que el mensaje sea igual a un múltiplo de 512.

Y ahora?
Justo después del mensaje inicial, se debe agregar el separador 1 seguido de P, que en nuestro ejemplo son nueve 0s.

mensaje + 1 000 000 000

#### Relleno de tamaño

Ahora pasamos a la segunda fase de preprocesamiento, que implica agregar la representación binaria del tamaño del mensaje inicial en bits.

Revisemos el ejemplo con una entrada de 950 bits:

La representación binaria del número 950 es: 11 1011 0110

Usamos nuestros 64 bits reservados del paso anterior. Agregamos ceros para redondear nuestros 64 bits a nuestra entrada igualada. Luego, fusionamos el mensaje inicial, los bits de relleno y el relleno de tamaño para obtener nuestra entrada igualada.

Aquí está el resultado:

![image](assets/image/section1/4.webp)

### Procesamiento

#### Entendiendo los requisitos previos

##### Constantes e vectores de inicialización

Ahora, nos estamos preparando para los primeros pasos del procesamiento de la función SHA-256. Al igual que en cualquier buena receta, necesitamos algunos ingredientes básicos, que llamamos constantes y vectores de inicialización.

Los vectores de inicialización, de A a H, son los primeros 32 bits de las partes decimales de las raíces cuadradas de los primeros 8 números primos. Servirán como valores base en los pasos iniciales del procesamiento. Sus valores están en formato hexadecimal.

Las constantes K, de 0 a 63, representan los primeros 32 bits de las partes decimales de las raíces cúbicas de los primeros 64 números primos. Se utilizan en cada ronda de la función de compresión. Sus valores también están en formato hexadecimal.

![image](assets/image/section1/5.webp)

##### Operaciones utilizadas

Dentro de la función de compresión, utilizamos operadores específicos como XOR, AND y NOT. Procesamos los bits uno por uno según su posición, utilizando el operador XOR y una tabla de verdad. El operador AND se utiliza para devolver 1 solo si ambos operandos son iguales a 1, y el operador NOT se utiliza para devolver el valor opuesto de un operando. También utilizamos la operación SHR para desplazar los bits hacia la derecha según un número elegido.

La tabla de verdad:

![image](assets/image/section1/6.webp)

Operaciones de desplazamiento de bits:

![image](assets/image/section1/7.webp)

#### La función de compresión

Antes de aplicar la función de compresión, dividimos la entrada en bloques de 512 bits. Cada bloque se procesará de forma independiente de los demás.

Cada bloque de 512 bits se divide en fragmentos de 32 bits llamados W. De esta manera, W(0) representa los primeros 32 bits del bloque de 512 bits. W(1) representa los siguientes 32 bits, y así sucesivamente, hasta llegar a los 512 bits del bloque.

Una vez definidas todas las constantes K y los fragmentos W, podemos realizar los siguientes cálculos para cada fragmento W en cada ronda.

Realizamos 64 rondas de cálculos en la función de compresión. En la última ronda, en el nivel "Salida de la función", tendremos un estado intermedio que se sumará al estado inicial de la función de compresión.

Luego, repetimos todos estos pasos de la función de compresión en el siguiente bloque de 512 bits, hasta el último bloque.
Todas las adiciones en la función de compresión son adiciones módulo 2^32 para mantener siempre una suma de 32 bits.

![image](assets/image/section1/9.webp)

![image](assets/image/section1/8.webp)

##### Una ronda de la función de compresión

![image](assets/image/section1/11.webp)

![image](assets/image/section1/10.webp)

La función de compresión se realizará 64 veces. Tenemos nuestras piezas W y nuestras constantes K previamente definidas como entrada.
Los cuadrados/cruces rojos corresponden a una adición de 32 bits módulo 2^32.

Las entradas A, B, C, D, E, F, G, H se asociarán con un valor de 32 bits para hacer un total de 32 * 8 = 256 bits.
También tenemos una nueva secuencia A, B, C, D, E, F, G, H como salida. Esta salida luego se utilizará como entrada para la siguiente ronda y así sucesivamente hasta el final de la 64ª ronda.

Los valores de la secuencia de entrada para la primera ronda de la función de compresión corresponden a los vectores de inicialización predefinidos mencionados anteriormente.
Como recordatorio, los vectores de inicialización representan los primeros 32 bits de las partes decimales de las raíces cuadradas de los primeros 8 números primos.

Aquí hay un ejemplo de una ronda:

![image](assets/image/section1/12.1.webp)

##### Estado intermedio

Como recordatorio, el mensaje se divide en bloques de 512 bits, que luego se dividen en piezas de 32 bits. Para cada bloque de 512 bits, aplicamos las 64 rondas de la función de compresión.
El estado intermedio corresponde al final de las 64 rondas de un bloque. Los valores de la secuencia de salida de esta 64ª ronda se utilizan como valores iniciales para la secuencia de entrada de la primera ronda del siguiente bloque.

![image](assets/image/section1/12.2.webp)

#### Resumen de la función hash

![image](assets/image/section1/13.webp)

Podemos observar que la salida de la primera pieza de mensaje de 512 bits corresponde a nuestros vectores de inicialización como entrada para la segunda pieza de mensaje de 512 bits, y así sucesivamente.

La salida de la última ronda, de la última pieza, corresponde al resultado final de la función SHA256.

En conclusión, nos gustaría enfatizar el papel crucial de los cálculos realizados en las cajas CH, MAJ, σ0 y σ1. Estas operaciones, entre otras, son los guardianes que aseguran la robustez de la función hash SHA256 contra ataques, lo que la convierte en una opción preferida para asegurar muchos sistemas digitales, especialmente dentro del protocolo Bitcoin. Es evidente que, aunque compleja, la belleza de SHA256 radica en su capacidad para encontrar la entrada a partir del hash, mientras que verificar el hash para una entrada dada es una acción mecánicamente simple.

## Los algoritmos utilizados para la derivación
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Los algoritmos de derivación HMAC y PBKDF2 son componentes clave en el mecanismo de seguridad del protocolo Bitcoin. Previenen una variedad de posibles ataques y aseguran la integridad de las carteras de Bitcoin.
HMAC y PBKDF2 son herramientas criptográficas utilizadas para diversas tareas en Bitcoin. HMAC se utiliza principalmente para contrarrestar ataques de extensión de longitud al derivar carteras determinísticas jerárquicas (HD), mientras que PBKDF2 se utiliza para convertir una frase mnemotécnica en una semilla.

#### HMAC-SHA512

El par HMAC-SHA512 tiene dos entradas: un mensaje m (Entrada 1) y una clave K elegida arbitrariamente por el usuario (Entrada 2). También tiene una salida de tamaño fijo: 512 bits.

Notemos:
- m: mensaje de tamaño arbitrario elegido por el usuario (entrada 1)
- K: clave arbitraria elegida por el usuario (entrada 2)
- K': clave igualada a K. Se ha ajustado al tamaño B de los bloques.
- ||: operación de concatenación.
- opad: constante definida por el byte 0x5c repetido B veces.
- ipad: constante definida por el byte 0x36 repetido B veces.
- B: tamaño de los bloques de la función hash utilizada.

HMAC-SHA512, que toma un mensaje y una clave como entradas, genera una salida de tamaño fijo. Para garantizar la uniformidad, la clave se ajusta en función del tamaño de los bloques utilizados en la función hash. En el contexto de la derivación de una billetera HD, se utiliza HMAC-SHA-512. Opera con bloques de 1024 bits (128 bytes) y ajusta la clave en consecuencia. Utiliza las constantes OPAD (0x5c) e IPAD (0x36), repetidas según sea necesario para mejorar la seguridad.

El proceso HMAC-SHA-512 implica concatenar el resultado de aplicar SHA-512 a la clave XOR OPAD y la clave XOR IPAD con el mensaje. Cuando se utiliza con bloques de 1024 bits (128 bytes), la clave de entrada se rellena con ceros si es necesario, luego se realiza la operación XOR con IPAD y OPAD. La clave modificada se concatena luego con el mensaje.

La inclusión de una sal en el código de cadena aumenta la seguridad de las claves derivadas. Sin ella, un ataque podría comprometer toda la billetera y robar todos los bitcoins.

PBKDF2 se utiliza para convertir una frase mnemotécnica en una semilla. Este algoritmo realiza 2048 rondas utilizando HMAC SHA512. A través de estos algoritmos de derivación, diferentes entradas pueden producir una salida única y fija, lo que mitiga el problema de posibles ataques de extensión de longitud en las funciones de la familia SHA-2.
Un ataque de extensión de longitud explota una propiedad específica de ciertas funciones hash criptográficas. En dicho ataque, un atacante que ya posee el hash de un mensaje desconocido puede usarlo para calcular el hash de un mensaje más largo, que es una extensión del mensaje original. Esto a menudo es posible sin conocer el contenido del mensaje original, lo que puede llevar a vulnerabilidades de seguridad significativas si se utiliza este tipo de función hash para tareas como la verificación de integridad.

En conclusión, los algoritmos HMAC y PBKDF2 desempeñan roles esenciales en la seguridad de la derivación de billeteras HD en el protocolo Bitcoin. HMAC-SHA-512 se utiliza para protegerse contra ataques de extensión de longitud, mientras que PBKDF2 permite la conversión de la frase mnemotécnica en una semilla. El código de cadena agrega una fuente adicional de entropía en la derivación de claves, asegurando la solidez del sistema.

# Firmas Digitales
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Firmas Digitales y Curvas Elípticas
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

¿Dónde se almacenan estos famosos bitcoins? No en una billetera de Bitcoin, como se podría pensar. En realidad, una billetera de Bitcoin almacena las claves privadas necesarias para demostrar la propiedad de los bitcoins. Los bitcoins en sí se registran en la cadena de bloques, una base de datos descentralizada que archiva todas las transacciones.
En el sistema Bitcoin, la unidad de cuenta es el bitcoin (nota la "b" minúscula). Es divisible hasta ocho lugares decimales, siendo la unidad más pequeña el satoshi. UTXOs, o "Unspent Transaction Outputs" (Salidas de Transacción No Gastadas), representan las salidas de transacción no gastadas que pertenecen a una clave pública que está matemáticamente vinculada a una clave privada. Para gastar estos bitcoins, uno debe poder satisfacer la condición de gasto de la transacción. Una condición de gasto típica implica demostrar al resto de la red que el usuario es el legítimo propietario de la clave pública asociada con el UTXO. Para hacer esto, el usuario debe demostrar la posesión de la clave privada correspondiente a la clave pública vinculada a cada UTXO sin revelar la clave privada.

Aquí es donde entra la firma digital. Sirve como prueba matemática de la posesión de una clave privada asociada a una clave pública específica. Esta técnica de protección de datos se basa principalmente en un fascinante campo de la criptografía llamado criptografía de curva elíptica (ECC).

La firma puede ser verificada matemáticamente por otros participantes en la red Bitcoin.

![image](assets/image/section2/0.webp)

Para garantizar la seguridad de las transacciones, Bitcoin se basa en dos protocolos de firma digital: ECDSA (Algoritmo de Firma Digital de Curva Elíptica) y Schnorr. ECDSA ha sido un protocolo de firma integrado en Bitcoin desde su lanzamiento en 2009, mientras que las firmas Schnorr se agregaron más recientemente en noviembre de 2021. Aunque ambos protocolos se basan en criptografía de curva elíptica y utilizan mecanismos matemáticos similares, principalmente difieren en términos de estructura de firma.

En este curso, presentaremos el algoritmo ECDSA.

### ¿Qué es una curva elíptica?

La criptografía de curva elíptica es un conjunto de algoritmos que utilizan una curva elíptica por sus diversas propiedades geométricas y matemáticas en un contexto criptográfico, con seguridad basada en la dificultad de calcular el logaritmo discreto.

Las curvas elípticas son útiles en una variedad de aplicaciones criptográficas en el protocolo Bitcoin, que van desde intercambios de claves hasta cifrado asimétrico y firmas digitales.

Las curvas elípticas tienen propiedades interesantes:

- Simetría: Cualquier línea no vertical que intersecte dos puntos en la curva elíptica intersectará la curva en un tercer punto.
- Cualquier línea no vertical tangente a la curva en un punto siempre intersectará la curva en un segundo punto único.

El protocolo Bitcoin utiliza una curva elíptica específica llamada Secp256k1 para sus operaciones criptográficas.

Antes de adentrarnos más en estos mecanismos de firma, es importante entender qué es una curva elíptica. Una curva elíptica se define por la ecuación y² = x³ + ax + b. Cada punto en esta curva tiene una simetría distintiva que es clave para su utilidad en criptografía.

![image](assets/image/section2/1.webp)

En última instancia, se reconocen varias curvas elípticas como seguras para su uso criptográfico. La más conocida puede ser la curva secp256r1. Sin embargo, para Bitcoin, Satoshi Nakamoto optó por una curva diferente: secp256k1.

Esta curva se define por los parámetros a=0 y b=7, y su ecuación es y² = x³ + 7 módulo n, donde n representa el número primo que determina el orden de la curva.

![image](assets/image/section2/2.webp)

La primera imagen representa la curva secp256k1 sobre el campo real y su ecuación.
La segunda imagen es una representación de la curva secp256k1 sobre el campo ZP, el campo de números naturales positivos, módulo p donde p es un número primo. Parece una nube de puntos. Utilizamos este campo de números naturales positivos para evitar aproximaciones.
p es un número primo y es el orden de la curva que se utiliza.
Finalmente, la ecuación utilizada en el protocolo de Bitcoin es: $$y^2 = (x^3 + 7) mod(p)$$
La ecuación de la curva elíptica en Bitcoin corresponde a la última ecuación en la imagen anterior.

En la siguiente sección de este curso, utilizaremos curvas que están en el campo real simplemente para facilitar la comprensión.

## Calculando la clave pública a partir de la clave privada
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Para comenzar, adentrémonos en el mundo del Algoritmo de Firma Digital de Curva Elíptica (ECDSA, por sus siglas en inglés). Bitcoin utiliza este algoritmo de firma digital para vincular claves privadas y públicas. En este sistema, la clave privada es un número aleatorio o pseudoaleatorio de 256 bits. El número total de posibilidades para una clave privada es teóricamente 2^256, pero en realidad es ligeramente menor que eso. Para ser precisos, algunas claves privadas de 256 bits no son válidas para Bitcoin.

Para ser compatible con Bitcoin, una clave privada debe estar entre 1 y n-1, donde n representa el orden de la curva elíptica. Esto significa que el número total de posibilidades para una clave privada de Bitcoin es casi igual a 1.158 x 10^77. Para poner esto en perspectiva, es aproximadamente la misma cantidad de átomos presentes en el universo observable.

![imagen](assets/image/section2/3.webp)

La clave privada única, denotada como k, se utiliza luego para determinar una clave pública.

La clave pública, denotada como K, es un punto en la curva elíptica que se deriva de la clave privada utilizando algoritmos irreversibles como ECDSA. Cuando tenemos conocimiento de la clave privada, es muy fácil recuperar la clave pública, pero cuando solo tenemos la clave pública, es imposible recuperar la clave privada. Esta irreversibilidad es la piedra angular de la seguridad de las billeteras de Bitcoin.

La clave pública tiene una longitud de 512 bits, ya que corresponde a un punto en la curva con una coordenada x de 256 bits y una coordenada y de 256 bits. Sin embargo, se puede comprimir en un número de 264 bits.

![imagen](assets/image/section2/4.webp)

El punto generador (G) es el punto en la curva a partir del cual se generan todas las claves públicas en el protocolo de Bitcoin. Tiene coordenadas x e y específicas, generalmente representadas en hexadecimal. Para secp256k1, las coordenadas de G son, en hexadecimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Este punto es útil para derivar todas las claves públicas. Para calcular la clave pública K, simplemente multiplicamos el punto G por la clave privada k, de la siguiente manera: K = k.G

Ahora estudiaremos cómo sumar y multiplicar puntos en curvas elípticas.

#### Suma y duplicación de puntos en curvas elípticas

##### Sumando dos puntos M + L

Una de las propiedades notables de las curvas elípticas es que una línea no vertical que intersecta la curva en dos puntos también la intersectará en un tercer punto, llamado punto O en nuestro ejemplo. Esta propiedad se utiliza para determinar el punto U, que es el opuesto del punto O.

M + L = U

![imagen](assets/image/section2/5.webp)

##### Sumando un punto consigo mismo = Duplicación de puntos
Agregar un punto G a sí mismo se hace trazando una tangente a la curva en ese punto. Esta tangente, según las propiedades de las curvas elípticas, intersectará la curva en un segundo punto único -J. El opuesto de este punto, J, es el resultado de agregar el punto G a sí mismo.
G + G = J

De hecho, el punto G es el punto de partida para calcular todas las claves públicas de los usuarios del sistema Bitcoin.

![image](assets/image/section2/6.webp)

#### Multiplicación escalar en curvas elípticas

La multiplicación escalar de un punto por n es equivalente a agregar ese punto a sí mismo n veces.

Similar al duplicado de puntos, la multiplicación escalar del punto G por un punto n se realiza trazando una tangente a la curva en el punto G. Esta tangente, según las propiedades de las curvas elípticas, intersectará la curva en un segundo punto único -2G. El opuesto de este punto, 2G, es el resultado de agregar el punto G a sí mismo.

Si n = 4, entonces la operación se repite hasta alcanzar 4G.

![image](assets/image/section2/7.webp)

Aquí hay un ejemplo de cálculo para 3G:

![image](assets/image/section2/8.webp)

Estas operaciones en puntos de una curva elíptica son la base para calcular claves públicas. Derivar una clave pública conociendo la clave privada es muy fácil.
Una clave pública es un punto en la curva elíptica, es el resultado de nuestra adición y duplicación del punto G k veces. Con k = clave privada.

En este ejemplo:

- La clave privada k = 4
- La clave pública K = kG = 4G

![image](assets/image/section2/9.webp)

Conociendo la clave privada k, es fácil calcular la clave pública K. Sin embargo, es imposible recuperar la clave privada basándose en la clave pública. ¿Es este el resultado de una adición o una duplicación de puntos?

En nuestra próxima lección, exploraremos cómo se crea una firma digital utilizando el algoritmo ECDSA con una clave privada para gastar bitcoins.

## Firmar con la clave privada
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

El proceso de firma digital es un método clave para demostrar que eres el titular de una clave privada sin revelarla. Esto se logra utilizando el algoritmo ECDSA, que implica determinar un nonce único, calcular un número específico V y crear una firma digital compuesta por dos partes, S1 y S2.
Es crucial siempre usar un nonce único para evitar ataques de seguridad. Un ejemplo notorio de lo que puede suceder cuando no se sigue esta regla es el pirateo de PlayStation 3, que se vio comprometido debido a la reutilización de nonces.

![](assets/image/section2/10.webp)

Pasos:

- Determinar un nonce v, que es un número aleatorio único.
  Nonce = Número Usado Solo Una Vez.
  Es determinado por quien realiza la firma.
- Calcular mediante la adición y duplicación de puntos en una curva elíptica desde el punto G, la posición de V en la curva elíptica.
  Tal que V = v.G
  x e y son las coordenadas de V en el plano.
- Calcular S1.
  S1 = x mod n con n = el orden de la curva y x una coordenada de V en el plano.
  Nota: El número de posibles claves públicas es mayor que el número de puntos en la curva elíptica en el campo finito de enteros positivos utilizado en Bitcoin.
  El orden de la curva corresponde solo a las posibilidades que la clave pública puede tomar en la curva.
- Calcular S2.
  H(Tx) = Hash de la transacción
k = la clave privada: calcular la firma, que es la concatenación de S1 + S2.
- Calcular P, el cálculo de verificación de la firma.
  K = la clave pública

Por ejemplo, para obtener la clave pública 3G, trazas una tangente al punto G, calculas el opuesto de -G para obtener 2G, y luego sumas G y 2G. Para realizar una transacción, debes demostrar que conoces el número 3 desbloqueando los bitcoins asociados con la clave pública 3G.
Para crear una firma digital y demostrar que conoces la clave privada asociada con la clave pública 3G, primero calculas un nonce y luego el punto V asociado con este nonce (en el ejemplo dado, es 4G). Luego, calculas el punto T sumando la clave pública 3G y el punto V, lo que da como resultado 7G.

![image](assets/image/section2/11.webp)

Simplifiquemos el proceso de firma digital.
En la imagen anterior, la clave privada k = 3.
Podemos calcular fácilmente la clave pública K asociada con esta clave privada: K = 3G.
Luego, generamos un nonce de forma pseudoaleatoria: v = 4.
A partir de este nonce, es posible calcular V de tal manera que: V = v.G = 4G.

A partir de este punto V, calculamos el punto T de tal manera que:
T = t.G = 7G (con t = 7).

Ahora es el momento de proceder con la verificación de la firma digital.

Verificar una firma digital es un paso crucial en el uso del algoritmo ECDSA, que permite confirmar la autenticidad de un mensaje firmado sin necesidad de la clave privada del remitente. Así es como funciona en detalle:

En nuestro ejemplo, tenemos dos valores importantes: t y V.
t es un valor numérico (7 en este ejemplo), y V es un punto en la curva elíptica (representado por 4G aquí). Estos valores se generan durante la creación de la firma digital y luego se envían junto con el mensaje para permitir la verificación.

Cuando el verificador recibe el mensaje, también recibirá estos dos valores, t y V.

Estos son los pasos que seguirá el verificador para validar la firma:

1. Primero, calculará el hash del mensaje, al que llamaremos H.
2. Luego, calculará u1 y u2. Para hacer esto, utilizará las siguientes fórmulas:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Donde S2 es la segunda parte de la firma digital, n es el orden de la curva elíptica y (S2)^-1 es el inverso de S2 mod n.
3. Luego, el verificador calculará un punto P' en la curva elíptica utilizando la fórmula: P' = u1 _ G + u2 _ K
   - G es el punto generador de la curva
   - K es la clave pública del remitente
4. Luego, el verificador calculará I', que es simplemente la coordenada x del punto P' módulo n.
5. Finalmente, el verificador confirmará que I' es igual a t. Si este es el caso, la firma se considera válida. Si no, la firma es inválida.
Este procedimiento asegura que solo el remitente que posee la clave privada correspondiente podría haber producido una firma que pase este proceso de verificación.

![image](assets/image/section2/12.webp)

En términos más simples:
La persona que produce la firma proporcionará el número t (en nuestro ejemplo, t = 7) y el punto V a la persona que lo verifica.
Es imposible determinar la clave pública o privada a partir del número 7 y el número V.

Los pasos para verificar la firma digital son los siguientes:

- En la curva, el verificador suma el punto de la clave pública al punto V para obtener el punto T'.
- El verificador calcula el número t.G.
- El verificador verifica que el resultado de t.G sea efectivamente igual al número T'.

En conclusión, verificar una firma digital es un procedimiento esencial en las transacciones de Bitcoin. Asegura que el mensaje firmado no haya sido alterado durante la transmisión y que el remitente sea realmente el titular de la clave privada. Esta técnica de autenticación digital se basa en principios matemáticos complejos, incluida la aritmética de curvas elípticas, al tiempo que mantiene la confidencialidad de la clave privada. Proporciona una base sólida de seguridad para transacciones criptográficas.

Dicho esto, la gestión de estas claves, así como su creación, es otra cuestión esencial en Bitcoin. ¿Cómo generar un nuevo par de claves? ¿Cómo organizar de manera segura y eficiente una multitud de claves? ¿Cómo recuperarlas si es necesario?

Para responder a estas preguntas y profundizar en su comprensión de la seguridad criptográfica, nuestro próximo curso se centrará en el concepto de Carteras Determinísticas Jerárquicas (HD wallets) y el uso de frases mnemotécnicas. Estos mecanismos ofrecen formas elegantes de gestionar eficazmente las claves de su criptomoneda al tiempo que mejoran la seguridad.

# La frase mnemotécnica
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evolución de las carteras de Bitcoin
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

La Cartera Determinística Jerárquica, más conocida como cartera HD, desempeña un papel destacado en el ecosistema de las criptomonedas. El término "cartera" puede parecer confuso para aquellos que son nuevos en este campo, ya que no implica tener dinero o monedas. En cambio, se refiere a una colección de claves privadas criptográficas.

Las primeras carteras eran software que agrupaban claves determinadas de forma privada de manera pseudoaleatoria pero no tenían conexión entre ellas. Estas carteras se llaman "Just a Bunch Of Keys" (JBOK).

Dado que las claves no tienen conexión entre ellas, se requiere que el usuario haga una nueva copia de seguridad para cada nuevo par de claves generado. Ya sea que el usuario siempre use el mismo par de claves y comprometa la confidencialidad, o genere un nuevo par de claves al azar y, por lo tanto, necesite hacer una nueva copia de seguridad de estas claves.

Sin embargo, la complejidad de gestionar estas claves se compensa con un conjunto de protocolos llamados Propuestas de Mejora de Bitcoin (BIP, por sus siglas en inglés). Estas propuestas de mejora son fundamentales para la funcionalidad y seguridad de las carteras HD. Por ejemplo, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lanzado en 2012, revolucionó la forma en que se generan y almacenan estas claves al introducir el concepto de claves derivadas de manera determinista y jerárquica. La idea es derivar todas las claves de manera determinista y jerárquica a partir de una única pieza de información: la semilla. Esto simplifica en gran medida el proceso de copia de seguridad de estas claves al tiempo que mantiene su nivel de seguridad.

Posteriormente, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introdujo una innovación significativa: la frase mnemotécnica de 24 palabras. Este sistema transformó una secuencia de números compleja y difícil de recordar en una serie de palabras comunes, lo que facilitó mucho su memorización y almacenamiento. Además, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) propuso agregar una frase de contraseña adicional para mejorar la seguridad de las claves individuales. Estas mejoras sucesivas llevaron a los estándares BIP43 y BIP44, que estandarizaron la estructura y jerarquización de las billeteras HD, haciéndolas más accesibles y fáciles de usar para el público en general.

En las siguientes secciones, profundizaremos en el funcionamiento de las billeteras HD. Discutiremos los principios de derivación de claves y examinaremos los conceptos fundamentales de entropía y generación de números aleatorios, que son esenciales para garantizar la seguridad de su billetera HD.

En resumen, es esencial destacar el papel central de BIP32 y BIP39 en el diseño y la seguridad de las billeteras HD. Estos protocolos permiten la generación de múltiples claves a partir de una única semilla, que se supone que es un número aleatorio o pseudoaleatorio. Hoy en día, estos estándares son adoptados por la mayoría de las billeteras de criptomonedas, ya sea que estén dedicadas a una sola criptomoneda o que admitan varios tipos de monedas.

## Entropía y número aleatorio
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

La importancia de la seguridad de la clave privada en el ecosistema de Bitcoin es innegable. De hecho, son la piedra angular que garantiza la seguridad de las transacciones de Bitcoin. Para evitar cualquier vulnerabilidad asociada con la previsibilidad, estas claves deben generarse de manera verdaderamente aleatoria, lo que puede convertirse rápidamente en un ejercicio laborioso. El problema es que en la informática, es imposible generar un número verdaderamente aleatorio, ya que necesariamente se deriva de un proceso determinista; un código. Es por eso que es esencial aprender sobre los diferentes Generadores de Números Aleatorios (RNG, por sus siglas en inglés). Los tipos de RNG varían, desde Generadores de Números Pseudoaleatorios (PRNG) hasta Generadores de Números Verdaderamente Aleatorios (TRNG), así como PRNG que incorporan una fuente de entropía.

La entropía se refiere al estado de "desorden" de un sistema. A partir de una entropía externa, es decir, una fuente externa de información, es posible utilizar un generador de números aleatorios para obtener un número aleatorio.

![imagen](assets/image/section3/2.webp)

Veamos cómo funciona un Generador de Números Pseudoaleatorios (PRNG).

Toma una semilla como entrada, que corresponde al estado interno 0.
Sobre este estado interno, se aplica una función de transformación, y el resultado, que es un número pseudoaleatorio, corresponde al estado interno 1.
Sobre este estado interno 1, nuevamente se aplica una función de transformación, lo que resulta en un nuevo número aleatorio = estado interno 2.
Y así sucesivamente.

La principal desventaja es que cualquier semilla idéntica siempre producirá la misma salida. Además, si conocemos el resultado de las funciones de transformación iniciales, podremos recuperar el número aleatorio en la salida del proceso.

Un ejemplo de función de transformación es la función PBKDF2.

**En resumen, un PRNG criptográficamente seguro debe:**

- ser estadísticamente aleatorio
- ser impredecible
- ser resistente incluso si se revelan los resultados
- tener un período suficientemente largo

![imagen](assets/image/section3/3.webp)

En el caso de Bitcoin, las claves privadas se generan a partir de una única pieza de información en la base de la billetera. Esta información permite la derivación determinista y jerárquica de pares de claves secundarias. La entropía es la base de cada billetera HD, aunque no existe un estándar para generar este número aleatorio. Por lo tanto, la generación de números aleatorios es un desafío importante en la seguridad de las transacciones de Bitcoin.

## La frase mnemotécnica
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

La seguridad de una billetera de Bitcoin es una preocupación importante para todos sus usuarios. Una forma esencial de asegurar la copia de seguridad de la billetera es generar una frase mnemotécnica basada en la entropía y la suma de verificación.

![imagen](assets/image/section3/5.webp)

Para convertir la entropía en una frase mnemotécnica, simplemente calcula la suma de verificación de la entropía y concatena la entropía y la suma de verificación.

Una vez que se genera la entropía, se utiliza la función SHA256 en la entropía para crear un hash. 
Se recuperan los primeros 8 bits del hash, que es la suma de verificación.
La frase mnemotécnica es el resultado de la entropía agregada a la suma de verificación.

La suma de verificación garantiza la verificación de la precisión de la frase de recuperación. Sin esta suma de verificación, un error en la frase podría resultar en la creación de una billetera diferente y, por lo tanto, en la pérdida de fondos. La suma de verificación se obtiene pasando la entropía a través de la función SHA256 y recuperando los primeros 8 bits del hash.

![imagen](assets/image/section3/6.webp)

Existen diferentes estándares para la frase mnemotécnica según el tamaño de la entropía. El estándar más utilizado para una frase de recuperación de 24 palabras es una entropía de 256 bits. El tamaño de la suma de verificación se determina dividiendo el tamaño de la entropía por 32.

Por ejemplo, una entropía de 256 bits genera una suma de verificación de 8 bits. La concatenación de la entropía y la suma de verificación conduce a tamaños respectivos de 128 bits, 160 bits, etc. Dependiendo del tamaño de la entropía, la frase de recuperación constará de 12 palabras para 128 bits, 15 palabras para 160 bits y 24 palabras para 256 bits.

**Codificación de la frase mnemotécnica:**

![imagen](assets/image/section3/7.webp)

Los últimos 8 bits corresponden a la suma de verificación.
Cada segmento de 11 bits se convierte en decimal.
Cada decimal corresponde a una palabra de una lista de 2048 palabras en BIP39. Es importante tener en cuenta que ninguna palabra tiene el mismo orden de las primeras cuatro letras.

Es esencial hacer una copia de seguridad de la frase de recuperación de 24 palabras para preservar la integridad de la billetera de Bitcoin. Los dos estándares más utilizados se basan en una entropía de 128 o 256 bits y una concatenación de 12 o 24 palabras. Agregar una frase de paso es una opción adicional para mejorar la seguridad de la billetera.

En conclusión, generar una frase mnemotécnica para asegurar una billetera de Bitcoin es un proceso crucial. Es importante adherirse a los estándares de la frase mnemotécnica según el tamaño de la entropía. Hacer una copia de seguridad de la frase de recuperación de 24 palabras es esencial para evitar cualquier pérdida de fondos.

## La frase de paso
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

La frase de paso es una contraseña adicional que se puede integrar en una billetera de Bitcoin para aumentar su seguridad. Su uso es opcional y está a discreción del usuario. Al agregar información arbitraria que, junto con la frase mnemotécnica, permite el cálculo de la semilla de la billetera, la frase de paso mejora su seguridad.

![imagen](assets/image/section3/8.webp)

La frase de contraseña es una sal criptográfica opcional de un tamaño elegido por el usuario. Mejora la seguridad de una billetera HD al agregar información arbitraria que, combinada con la frase mnemotécnica, permitirá el cálculo de la semilla.
Una vez establecida durante la creación de una billetera, es necesaria para la derivación de todas las claves de la billetera. La función pbkdf2 se utiliza para generar la semilla a partir de la frase de contraseña. Esta semilla permite la derivación de todos los pares de claves secundarias de la billetera. Si se cambia la frase de contraseña, la billetera de Bitcoin se vuelve completamente diferente.

La frase de contraseña es una herramienta esencial para mejorar la seguridad de las billeteras de Bitcoin. Puede permitir la implementación de diversas estrategias de seguridad. Por ejemplo, se puede utilizar para crear duplicados y facilitar copias de seguridad de la frase mnemotécnica. También puede mejorar la seguridad de la billetera al mitigar los riesgos asociados con la generación aleatoria de la frase mnemotécnica.

Una frase de contraseña efectiva debe ser larga (de 20 a 40 caracteres) y diversa (utilizando letras mayúsculas, letras minúsculas, números y símbolos). No debe estar directamente relacionada con el usuario o su entorno. Es más seguro utilizar una secuencia aleatoria de caracteres en lugar de una palabra simple como frase de contraseña.

![image](assets/image/section3/9.webp)

Una frase de contraseña es más segura que una contraseña simple. La frase de contraseña ideal es larga, variada y aleatoria. Puede mejorar la seguridad de una billetera o software en caliente. También se puede utilizar para crear copias de seguridad redundantes y seguras.

Es crucial cuidar las copias de seguridad de la frase de contraseña para evitar perder el acceso a la billetera. Una frase de contraseña es una opción para una billetera HD. Se puede generar aleatoriamente con dados u otro generador de números pseudoaleatorios. No se recomienda memorizar una frase de contraseña o frase mnemotécnica.

En nuestra próxima lección, examinaremos en detalle el funcionamiento de la semilla y el primer par de claves generado a partir de ella. No dudes en seguir este curso para continuar tu aprendizaje. Esperamos verte nuevamente muy pronto.

# Creación de billeteras de Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Creación de la semilla y la clave maestra
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

En esta parte del curso, exploraremos los pasos para derivar una Billetera Determinista Jerárquica (HD Wallet), que permite la creación y gestión jerárquica y determinista de claves privadas y públicas.

![image](assets/image/section4/0.webp)

La base de la Billetera HD se basa en dos elementos esenciales: la frase mnemotécnica y la frase de contraseña (contraseña adicional opcional). Juntos, constituyen la semilla, una secuencia alfanumérica de 512 bits que sirve como base para derivar las claves de la billetera. A partir de esta semilla, es posible derivar todos los pares de claves secundarias de la billetera de Bitcoin. La semilla es la clave que otorga acceso a todos los bitcoins asociados con la billetera, ya sea que se use una frase de contraseña o no.

![image](assets/image/section4/1.webp)

Para obtener la semilla, se utiliza la función pbkdf2 (Función de Derivación de Clave Basada en Contraseña 2) con la frase mnemotécnica y la frase de contraseña. La salida de pbkdf2 es una semilla de 512 bits.

A partir de la semilla, es posible determinar la clave privada maestra y el código de cadena utilizando el algoritmo HMAC SHA-512 (Código de Autenticación de Mensaje Basado en Hash Algoritmo Seguro 512). Este algoritmo requiere un mensaje y una clave como entrada para generar un resultado. La clave privada maestra se calcula a partir de la semilla y la frase "Bitcoin SEED". Esta frase es idéntica para todas las derivaciones de todas las billeteras HD, asegurando consistencia entre las billeteras.

Inicialmente, la función SHA-512 no estaba implementada en el protocolo de Bitcoin, por lo que se utiliza HMAC SHA-512. El uso de HMAC SHA-512 con la frase "Bitcoin SEED" limita al usuario a generar una billetera específica para Bitcoin. El resultado de HMAC SHA-512 es un número de 512 bits, dividido en dos partes: los 256 bits más a la izquierda representan la clave privada maestra, mientras que los 256 bits más a la derecha representan el código de cadena maestro.

![imagen](assets/image/section4/2.webp)

La clave privada maestra es la clave principal de todas las claves futuras en la billetera, mientras que el código de cadena maestro está involucrado en la derivación de las claves secundarias. Es importante tener en cuenta que es imposible derivar un par de claves secundarias sin conocer el código de cadena correspondiente del par principal.

Un par de claves en la billetera consta de una clave privada, una clave pública y un código de cadena. El código de cadena introduce una fuente de aleatoriedad en la derivación de las claves secundarias y aísla cada par de claves para evitar cualquier filtración de información.
Es importante tener en cuenta que la clave privada maestra es la primera clave privada derivada de la semilla y no tiene conexión con las claves extendidas de la billetera.

En la próxima lección, exploraremos las claves extendidas en detalle, como xPub, xPRV, zPub, y entenderemos por qué se utilizan y cómo se construyen.

## Claves Extendidas
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

En esta parte de la lección, estudiaremos las claves extendidas (xPub, zPub, yPub) y sus prefijos, que desempeñan un papel importante en la derivación de claves secundarias en una Billetera Determinista Jerárquica (HD Wallet).

![imagen](assets/image/section4/3.webp)

Las claves extendidas son distintas de las claves maestras. Una billetera HD genera una frase mnemotécnica y una semilla para obtener la clave maestra y el código de cadena maestro. Las claves extendidas se utilizan para derivar claves secundarias y requieren tanto la clave principal como el código de cadena correspondiente. Una clave extendida combina estas dos piezas de información para simplificar el proceso de derivación.

![imagen](assets/image/section4/4.webp)

Las claves públicas extendidas solo pueden derivar claves públicas normales, mientras que las claves privadas extendidas pueden derivar tanto claves públicas como claves privadas secundarias, ya sea a través de una derivación normal o endurecida. La derivación endurecida es la derivación a partir de la clave privada principal, mientras que la derivación normal corresponde a la derivación a partir de la clave pública principal.

El uso de claves extendidas con el prefijo XPUB permite la derivación de nuevas direcciones sin tener que volver a las claves privadas correspondientes, lo que proporciona una mejor seguridad. Los metadatos asociados con las claves extendidas proporcionan información importante sobre su función y posición en la jerarquía de claves.

Las claves extendidas se identifican mediante prefijos específicos (XPRV, XPUB, YPUB, ZPUB) que indican si es una clave privada o pública extendida, así como su propósito específico. Los metadatos asociados con una clave extendida incluyen la versión (prefijo), profundidad, huella digital de la clave principal, índice y carga útil (código de cadena y clave principal).

![imagen](assets/image/section4/5.webp)

La versión corresponde al tipo de clave: xpub, xprv, ...

La profundidad corresponde al número de derivaciones entre las claves principal y secundaria desde la clave maestra.

La huella digital del padre son los primeros 4 bytes del hash 160 de la clave principal.
El índice es el número de la pareja que se utiliza para generar la clave extendida entre sus hermanos. (hermanos = claves de la misma profundidad) Por ejemplo, si queremos derivar el xpub de nuestra tercera cuenta, su índice será 2 (porque el índice comienza en 0).
La carga útil está compuesta por el código de cadena (32 bytes) y la clave principal (33 bytes).
Las claves públicas comprimidas tienen un tamaño de 33 bytes, mientras que las claves públicas sin procesar tienen 512 bits. Las claves públicas comprimidas conservan la misma información que las claves sin procesar, pero con un tamaño reducido. Las claves extendidas tienen un tamaño de 82 bytes y su prefijo se representa en base 58 a través de una conversión a hexadecimal. El checksum se calcula utilizando la función hash HASH256.

![imagen](assets/image/section4/6.webp)

Las derivaciones mejoradas comienzan desde índices que son potencias de 2 (2^31). Es interesante destacar que los prefijos más utilizados son xpub y zpub, que corresponden respectivamente a los estándares heredados y segwit v1 y segwit v0.

En nuestra próxima lección, nos centraremos en la derivación de pares de claves secundarias utilizando los conocimientos adquiridos sobre claves extendidas y la clave maestra de la billetera.

## Derivación de pares de claves secundarias
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Como recordatorio, hemos discutido el cálculo de la semilla y la clave maestra, que son los primeros elementos esenciales para la organización jerárquica y la derivación de la billetera HD (Determinista Jerárquica). La semilla, con una longitud de 128 a 256 bits, se genera de forma aleatoria o a partir de una frase secreta. Juega un papel determinista en la derivación de todas las demás claves. La clave maestra es la primera clave derivada de la semilla y permite la derivación de todos los demás pares de claves secundarias.

El código de cadena maestro juega un papel importante en la recuperación de la billetera a partir de la semilla. Cabe destacar que todas las claves derivadas de la misma semilla tendrán el mismo código de cadena maestro.

![imagen](assets/image/section4/7.webp)

La organización jerárquica y la derivación de la billetera HD ofrecen una gestión más eficiente de las claves y las estructuras de la billetera. Las claves extendidas permiten la derivación de un par de claves secundarias a partir de un par de claves principales mediante cálculos matemáticos y algoritmos específicos.
Existen diferentes tipos de pares de claves secundarias, incluyendo claves reforzadas y claves normales. La clave pública extendida solo permite la derivación de claves públicas secundarias normales, mientras que la clave privada extendida permite la derivación de todas las claves secundarias, tanto públicas como privadas, ya sea en modo normal o reforzado. Cada par de claves tiene un índice que les permite diferenciarse entre sí.

![imagen](assets/image/section4/8.webp)

La derivación de claves secundarias utiliza la función HMAC-SHA512 utilizando la clave principal concatenada con el índice y el código de cadena asociado con el par de claves. Las claves secundarias normales tienen un índice que va desde 0 hasta 2 elevado a la potencia de 31 menos 1, mientras que las claves secundarias reforzadas tienen un índice que va desde 2 elevado a la potencia de 31 hasta 2 elevado a la potencia de 32 menos 1.

![imagen](assets/image/section4/9.webp)

![imagen](assets/image/section4/10.webp)

Existen dos tipos de pares de claves secundarias: pares reforzados y pares normales. El proceso de derivación de claves secundarias utiliza claves públicas para generar condiciones de gasto, mientras que las claves privadas se utilizan para firmar. La clave pública extendida solo permite la derivación de claves públicas secundarias normales, mientras que la clave privada extendida permite la derivación de todas las claves secundarias, tanto públicas como privadas, en modo normal o reforzado.

![imagen](assets/image/section4/11.webp)
![imagen](assets/image/section4/12.webp)

La derivación reforzada utiliza la clave privada principal, mientras que la derivación normal utiliza la clave pública principal. Se utiliza la función HMAC-SHA512 para la derivación reforzada, mientras que la derivación normal utiliza un resumen de 512 bits. La clave pública secundaria se obtiene multiplicando la clave privada secundaria por el generador de la curva elíptica.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

La derivación jerárquica y la derivación de muchas parejas de claves de manera determinista permiten la creación de una estructura de árbol para la derivación jerárquica. En la próxima lección de este entrenamiento, estudiaremos la estructura de la billetera HD, así como los caminos de derivación, con un enfoque particular en las notaciones de los caminos de derivación.

## Estructura de la billetera y caminos de derivación
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

En este capítulo, estudiaremos la estructura del árbol de derivación en una Billetera Determinista Jerárquica (HD Wallet). Ya hemos explorado el cálculo de la semilla, la clave maestra y la derivación de parejas de claves secundarias. Ahora, nos enfocaremos en organizar las claves dentro de la billetera.

La billetera HD utiliza capas de profundidad para organizar las claves. Cada derivación de una pareja principal a una pareja secundaria corresponde a una capa de profundidad.

![image](assets/image/section4/15.webp)

- La capa de profundidad 0 corresponde a la clave maestra y el código de cadena maestra.

- La capa de profundidad 1 se utiliza para derivar claves secundarias para un propósito específico, determinado por el índice. Los propósitos cumplen con los estándares BIP 84 y Segwit v0/v1.

- La capa de profundidad 2 permite la diferenciación de cuentas para diferentes criptomonedas o redes. Esto permite organizar la billetera en función de diferentes fuentes de fondos. Para bitcoin, el índice será 0.

- La capa de profundidad 3 se utiliza para organizar la billetera en diferentes cuentas, proporcionando una estructura más clara y organizada.

- La capa de profundidad 4 corresponde a las cadenas externas e internas, que se utilizan para direcciones destinadas a ser comunicadas públicamente. El índice 0 está asociado con la cadena externa, mientras que el índice 1 está asociado con la cadena interna. Cada cuenta tiene dos cadenas: la cadena externa (0) y la cadena interna (1). La capa de profundidad 4 también se utiliza para gestionar tipos de scripts en el caso de billeteras de múltiples firmas.

- La capa de profundidad 5 se utiliza para recibir direcciones en una billetera estándar. En la próxima sección, examinaremos la derivación de parejas de claves secundarias con más detalle.

![image](assets/image/section4/16.webp)

Para cada capa de profundidad, utilizamos índices para diferenciar las parejas de claves secundarias.

El índice sin apóstrofe corresponde al índice utilizado real, mientras que el índice con apóstrofe corresponde al índice real + 2^31. Las derivaciones reforzadas utilizan índices de 2^31 a 2^32-1. Por ejemplo, el índice 44' corresponde al índice real 2^31 + 44.

Para generar una dirección de recepción específica, derivamos una pareja de claves secundarias a partir de la clave maestra y el código de cadena maestra. Luego, utilizamos el índice para diferenciar entre diferentes parejas de claves secundarias en la misma capa de profundidad.
Las claves extendidas, como XPUB, te permiten compartir tu billetera con varias personas. El camino de derivación se utiliza para diferenciar entre la cadena externa (direcciones destinadas a ser compartidas) y la cadena interna (direcciones de cambio).

En el próximo capítulo, estudiaremos las direcciones de recepción, sus ventajas de uso y los pasos involucrados en su construcción.

# ¿Qué es una dirección de Bitcoin?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Direcciones de Bitcoin
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

En este capítulo, exploraremos las direcciones de recepción, las cuales desempeñan un papel crucial en el sistema Bitcoin. Permiten recibir fondos en una transacción y se generan a partir de pares de claves privadas y públicas. Aunque existe un tipo de script llamado Pay2PublicKey que permite bloquear bitcoins a una clave pública, los usuarios generalmente prefieren utilizar direcciones de recepción en lugar de este script.

![image](assets/image/section5/0.webp)

Cuando un destinatario desea recibir bitcoins, proporciona una dirección de recepción al remitente en lugar de su clave pública. En realidad, una dirección es un hash de una clave pública, con un formato específico. La clave pública se deriva de la clave privada hija utilizando operaciones matemáticas como la suma de puntos y la duplicación en curvas elípticas.

![image](assets/image/section5/1.webp)

Es importante tener en cuenta que no es posible revertir una dirección a la clave pública, ni de la clave pública a la clave privada. El uso de una dirección reduce el tamaño de la información de la clave pública, que inicialmente es de 512 bits.

Las direcciones de Bitcoin se han reducido en tamaño para facilitar su uso. Tienen un checksum, que permite detectar errores tipográficos y reducir el riesgo de perder bitcoins. Por otro lado, las claves públicas no tienen un checksum, lo que significa que los errores tipográficos pueden resultar en la pérdida de los fondos correspondientes.

Las direcciones también proporcionan una segunda capa de seguridad entre la información pública y privada, lo que dificulta el control de la clave privada.

Es esencial enfatizar que cada dirección debe ser utilizada solo una vez. Reutilizar la misma dirección plantea problemas de privacidad y debe evitarse.

Se utilizan diferentes prefijos para las direcciones de Bitcoin. Por ejemplo, BC1Q corresponde a una dirección Segwit V0, BC1P a una dirección Taproot/Segwit V1, y los prefijos 1 y 3 están asociados con direcciones Pay2PublicKeyH/Pay2ScriptH (legacy). En la próxima lección, explicaremos paso a paso cómo derivar una dirección a partir de una clave pública.

## ¿Cómo crear una dirección de Bitcoin?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

En este capítulo, discutiremos la construcción de una dirección de recepción para transacciones de Bitcoin. Una dirección de recepción es una representación alfanumérica de una clave pública comprimida. La conversión de una clave pública en una dirección de recepción implica varios pasos.

### Paso 1: Compresión de la clave pública

![image](assets/image/section5/14.webp)

Una dirección se deriva de una clave pública hija.

Una clave pública es un punto en la curva elíptica. Gracias a la simetría de la curva elíptica, un punto en la curva elíptica tendrá una coordenada x asociada con solo dos posibles valores para y: positivo o negativo. 
Sin embargo, en el protocolo Bitcoin, trabajamos con un conjunto finito de enteros positivos en lugar del conjunto de números reales. Para distinguir entre los dos posibles valores de y, es suficiente indicar si y es par o impar.

La compresión de una clave pública reduce su tamaño de 520 bits a 264 bits.

Utilizamos el prefijo 0x02 para un y par y 0x03 para un y impar. Esta es la forma comprimida de la clave pública.

### Paso 2: Hashing de la clave pública comprimida

![image](assets/image/section5/3.webp)

El hashing de la clave pública comprimida se realiza utilizando la función SHA256. Luego se aplica la función RIPEMD160 al resumen.

### Paso 3: La carga útil = Carga útil de la dirección

El resumen binario de RIPEMD160(SHA256(K)) se utiliza para formar grupos de 5 bits. Cada grupo se transforma en base16 (Hexadecimal) y/o base 10.

### Paso 4: Agregar metadatos para el cálculo del checksum con el programa BCH

![imagen](assets/image/section5/5.webp)

En el caso de las direcciones heredadas, utilizamos el hash doble SHA256 para generar el checksum de la dirección. Sin embargo, para las direcciones Segwit V0 y V1, confiamos en la tecnología de checksum BCH para garantizar la detección de errores. El programa BCH es capaz de sugerir y corregir errores con una probabilidad extremadamente baja de error. Actualmente, el programa BCH se utiliza para detectar y sugerir modificaciones que deben realizarse, pero no las realiza automáticamente en nombre del usuario.
El programa BCH requiere varias informaciones de entrada, incluyendo el HRP (Parte Legible por Humanos) que necesita ser extendido. La extensión del HRP implica codificar cada letra en base 2 según su código ASCII. Luego, tomando los primeros 3 bits del resultado para cada letra y convirtiéndolos a base 10 (en azul en la imagen). Insertar un separador 0. Luego concatenar los siguientes 5 bits de cada letra previamente convertida a base 10 (en amarillo en la imagen).

La extensión del HRP en base 10 permite aislar los últimos cinco bits de cada carácter, reforzando así el checksum.

La versión Segwit V0 está representada por el código 00 y el "payload" está en negro, en base 10. A esto le siguen seis caracteres reservados para el checksum.

### Paso 5: Cálculo del checksum con el programa BCH

![imagen](assets/image/section5/6.webp)

La entrada que contiene los metadatos se envía al programa BCH para obtener el checksum en base 10.

Aquí tenemos el checksum.

### Paso 6: Construcción de la dirección y conversión a Bech32

![imagen](assets/image/section5/7.webp)

La concatenación de la versión, el payload y el checksum permite construir la dirección. Los caracteres en base 10 se convierten luego en caracteres Bech32 utilizando una tabla de correspondencia. El alfabeto Bech32 incluye todos los caracteres alfanuméricos, excepto 1, b, i y o, para evitar cualquier confusión.

### Paso 7: Agregar el HRP y el separador

![imagen](assets/image/section5/8.webp)

En rosa, el checksum.
En negro, el payload = el hash de la clave pública.
En azul, la versión.

Todo se convierte a Bech32, luego se agrega 'bc' para bitcoin y '1' como separador, y aquí está la dirección.

# Ir más allá
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## ¡Crear una semilla a partir de 128 lanzamientos de dados!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Crear una frase mnemotécnica es un paso crucial para asegurar tu billetera de criptomonedas. Hay varios métodos para generar una frase mnemotécnica, sin embargo, nos centraremos en el método de generación manual utilizando dados. Es importante tener en cuenta que este método no es adecuado para una billetera de alto valor. Se recomienda utilizar software de código abierto o una billetera de hardware para generar la frase mnemotécnica. Para crear una frase mnemotécnica, utilizaremos dados para generar información binaria. El objetivo es comprender el proceso de creación de la frase mnemotécnica.

**Paso 1 - Preparación:**
Asegúrate de tener una distribución de Linux amnésica, como Tails OS, instalada en una llave USB para mayor seguridad. Ten en cuenta que este tutorial no debe utilizarse para crear una billetera principal.
**Paso 2 - Generar un número binario aleatorio:**
Usaremos dados para generar información binaria. Lanza un dado 128 veces y registra cada resultado (1 para impar, 0 para par).
**Paso 3 - Organización de números binarios:**
Organiza los números binarios obtenidos en filas de 11 dígitos para facilitar cálculos adicionales. La duodécima fila solo debe tener 7 dígitos.

**Paso 4 - Cálculo del checksum:**
Los últimos 4 dígitos de la duodécima fila corresponden al checksum. Para calcular este checksum, necesitamos usar una terminal de una distribución Linux. Se recomienda usar [TailOs](https://tails.boum.org/index.fr.html), que es una distribución sin memoria de arranque desde una memoria USB. Una vez en tu terminal, ingresa el comando `echo <número binario> | shasum -a 254 -0`. Reemplaza `<número binario>` con tu lista de 128 ceros y unos. La salida es un hash hexadecimal. Toma nota del primer carácter de este hash y conviértelo a binario. Puedes usar esta [tabla](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) para ayudarte. Agrega el checksum binario (4 dígitos) a la duodécima fila de tu hoja.

**Paso 5 - Conversión a decimal:**
Para encontrar las palabras asociadas con cada una de tus filas, primero debes convertir cada serie de 11 bits a decimal. Aquí, no puedes usar un convertidor en línea porque estos bits representan tu frase mnemotécnica. Por lo tanto, deberás convertirlos usando una calculadora y un truco de la siguiente manera: cada bit está asociado con una potencia de 2, por lo que de izquierda a derecha, tenemos 11 rangos correspondientes a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Para convertir tu serie de 11 bits a decimal, simplemente suma solo los rangos que contengan un 1. Por ejemplo, para la serie 00110111011, esto corresponde a la siguiente suma: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Ahora puedes convertir cada fila a decimal. Y antes de pasar a la codificación en palabras, suma +1 a todas las filas porque el índice de la lista de palabras BIP39 comienza desde 1, no desde 0.

**Paso 8 - Generación de la frase mnemotécnica:**
Comienza imprimiendo la [lista de 2048 palabras](https://seedxor.com/files/wordlist.pdf) para convertir entre tus números decimales y las palabras BIP39. La singularidad de esta lista es que ninguna palabra comparte las primeras 4 letras con ninguna otra palabra en este diccionario. Luego, busca la palabra asociada con cada número decimal de tus líneas.
**Paso 9 - Prueba de la frase mnemotécnica:**
Prueba inmediatamente tu frase mnemotécnica en Sparrow Wallet creando una billetera a partir de ella. Si recibes un error de checksum inválido, es probable que hayas cometido un error de cálculo. Corrige este error volviendo al paso 4 y prueba nuevamente en Sparrow Wallet. ¡Voilà! Acabas de crear una nueva billetera de Bitcoin a partir de 128 lanzamientos de dados.

Generar una frase mnemotécnica es un proceso importante para asegurar tu billetera de criptomonedas. Se recomienda utilizar métodos más seguros, como el uso de software de código abierto o una billetera de hardware, para generar la frase mnemotécnica. Sin embargo, completar este taller ayuda a comprender mejor cómo podemos crear una billetera de Bitcoin a partir de un número aleatorio.

## BONUS: Entrevista con Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Otro método criptográfico ampliamente utilizado en el protocolo Bitcoin es el método de firmas digitales.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Danos tu opinión sobre este curso
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Examen Final
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Conclusión y final
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Gracias y sigue profundizando en la madriguera del conejo

Nos gustaría agradecerte sinceramente por completar el curso Crypto 301. Esperamos que esta experiencia haya sido enriquecedora y educativa para ti. Hemos cubierto muchos temas emocionantes, desde matemáticas hasta criptografía y el funcionamiento del protocolo Bitcoin.

Si deseas adentrarte más en el tema, tenemos un recurso adicional para ofrecerte. Realizamos una entrevista exclusiva con Théo Pantamis y Loïc Morel, dos expertos reconocidos en el campo de la criptografía. Esta entrevista explora varios aspectos del tema en profundidad y proporciona perspectivas interesantes.

Siéntete libre de ver esta entrevista para seguir explorando el fascinante campo de la criptografía. Esperamos que sea útil e inspiradora en tu camino. Una vez más, gracias por tu participación y compromiso durante todo este curso.

### Apóyanos

Este curso, junto con todo el contenido de esta universidad, te ha sido proporcionado de forma gratuita por nuestra comunidad. Para apoyarnos, puedes compartirlo con otros, convertirte en miembro de la universidad e incluso contribuir a su desarrollo a través de GitHub. ¡En nombre de todo el equipo, gracias!

### Califica el curso
¡Pronto se integrará un sistema de calificación para el entrenamiento en esta nueva plataforma de aprendizaje en línea! Mientras tanto, muchas gracias por tomar el curso y, si te gustó, considera compartirlo con otros.
