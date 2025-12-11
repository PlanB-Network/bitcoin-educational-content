---
name: Programación Bitcoin
goal: Construir una biblioteca Bitcoin completa desde cero y comprender los fundamentos criptográficos de Bitcoin
objectives: 

 - Implementación de aritmética de campos finitos y operaciones con curvas elípticas en Python
 - Construcción y análisis sintáctico de transacciones Bitcoin mediante programación
 - Creación de direcciones Testnet y difusión de transacciones en la red
 - Dominar los fundamentos matemáticos del modelo de seguridad de Bitcoin

---
# Un viaje a los guiones y programas de Bitcoin


Este curso intensivo de dos días, impartido por Jimmy Song, te adentra en los fundamentos técnicos de Bitcoin mediante la construcción de una biblioteca Bitcoin completa desde cero. Empezando por las matemáticas esenciales de los campos finitos y las curvas elípticas, progresarás a través del análisis sintáctico de transacciones, la ejecución de scripts y la comunicación en red. A través de ejercicios prácticos de codificación en cuadernos Jupyter, crearás tu propio Testnet Address, construirás transacciones manualmente y las transmitirás directamente a la red, todo ello mientras adquieres una profunda comprensión de los principios criptográficos que hacen que Bitcoin sea seguro y Trustless.


Disfrute de su descubrimiento


+++

# Introducción

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Descripción general del curso

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Bienvenido al curso PRO 202 _**Programming Bitcoin**_, un viaje intensivo que te lleva desde la aritmética de campos finitos hasta la creación y transmisión de transacciones reales en la red de prueba de Bitcoin.

En este curso, construirás progresivamente una biblioteca de Bitcoin en Python mientras adquieres las bases criptográficas, de protocolo y de software necesarias para razonar con precisión sobre la seguridad y el funcionamiento interno de Bitcoin. El enfoque del PRO 202 es completamente práctico: cada concepto se implementa de inmediato en cuadernos Jupyter, garantizando que la teoría y el código se refuercen mutuamente.

### Conceptos matemáticos esenciales para Bitcoin

Esta primera sección establece los fundamentos matemáticos indispensables. Implementarás aritmética de campos finitos y operaciones en curvas elípticas (ley de grupo, suma, duplicación, multiplicación escalar...) — los prerrequisitos para ECDSA. El objetivo es doble: comprender la estructura algebraica que hace posibles las firmas criptográficas y construir herramientas fiables en Python para manipularlas.

A continuación, formalizarás los componentes de ECDSA: generación de claves, formato de puntos, hashing, creación y verificación de firmas. Esta sección conecta directamente la teoría con la práctica, destacando los detalles de implementación y la solidez del modelo de seguridad subyacente.

### Funcionamiento interno de una transacción de Bitcoin

En la segunda sección, analizarás la estructura de una transacción de Bitcoin: UTXOs, entradas/salidas, secuencias, scripts, codificaciones y más. Escribirás código para construir, firmar y verificar transacciones, obteniendo una comprensión precisa de lo que se compromete mediante el hash y por qué.

A continuación, implementarás un ejecutor _Script_ mínimo, revisarás los principales opcodes y validarás las rutas de gasto. El objetivo es que seas capaz de auditar el comportamiento de las transacciones, diagnosticar fallos de validación y razonar sobre la seguridad de las políticas de gasto.

### Funcionamiento interno de la red de Bitcoin

En la tercera sección, situarás la transacción dentro del sistema más amplio: estructura de bloques, encabezados, dificultad y el mecanismo de Prueba de Trabajo (Proof-of-Work). Manejarás mensajes de protocolo, encabezados de bloques y árboles de Merkle.

Finalmente, estudiarás la comunicación entre nodos peer-to-peer, la optimización de mensajes y la introducción de SegWit.

Como en todos los cursos de Plan ₿ Academy, la sección final incluye una evaluación diseñada para consolidar tu comprensión. ¿Listo para descubrir el funcionamiento interno de Bitcoin y escribir el código que lo impulsa? ¡Empecemos!

# Conceptos matemáticos esenciales para Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matemáticas para la aplicación de Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Criptografía de curva elíptica

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Transacciones internas de Bitcoin

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Análisis de transacciones y firmas ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Validación de scripts y transacciones

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Construcción de transacciones y Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Red Bitcoin

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Bloques y Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicación en red y árboles de Merkle

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicación avanzada entre nodos y testigos segregados

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sección final


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Opiniones y valoraciones


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusión


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
