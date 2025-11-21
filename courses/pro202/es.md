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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matemáticas para la aplicación de Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Criptografía de curva elíptica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Transacciones internas de Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Análisis de transacciones y firmas ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Validación de scripts y transacciones

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Construcción de transacciones y Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Red Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Bloques y Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicación en red y árboles de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicación avanzada entre nodos y testigos segregados

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sección final


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Opiniones y valoraciones


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Conclusión


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
