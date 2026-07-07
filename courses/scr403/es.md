---
name: Profundizando en Simplicity
goal: Dominar la filosofía de diseño, el sistema de tipos y el ciclo de vida completo de Simplicity
objectives:
  - Comprender los tres métodos fundamentales de composición y los nueve combinadores que forman un lenguaje completo
  - Construir lógica booleana, aritmética y SHA-256 a partir del sistema de tipos mínimo de Simplicity
  - Entender cómo los efectos secundarios Failure y Reader permiten la interacción real con la blockchain
  - Aprender cómo los programas de Simplicity se convierten en direcciones Taproot y se redimen con datos de testigo
---

# Profundizando en Simplicity

Una inmersión profunda en la teoría y las decisiones de diseño detrás del lenguaje Simplicity, basada en la serie completa de cinco artículos ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) del [Dr. Russell O'Connor](https://r6.ca/), el creador de Simplicity en Blockstream Research. Este curso explica *por qué* Simplicity fue diseñado como fue, no cómo escribirlo.

El curso sigue los artículos del Dr. O'Connor a través de las tres formas fundamentales de combinar computaciones, el sistema de tipos mínimo y su teorema de completitud, la construcción de tipos de datos prácticos y aritmética desde primeros principios, la cuidadosa introducción de efectos secundarios para la interacción con la blockchain, y finalmente cómo los programas se comprometen a direcciones y se redimen en la cadena.

+++

# Introducción

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Descripción general del curso

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

¡Bienvenido a SCR403 — Profundizando en Simplicity!

Este curso se basa en la serie de artículos **"Delving Simplicity"** escrita por el [Dr. Russell O'Connor](https://r6.ca/), Infrastructure Tech Developer en [Blockstream](https://blockstream.com/) y creador de Simplicity. Los artículos originales se publicaron en el foro [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) y constituyen el material fuente principal de este curso. Agradecemos su trabajo pionero, que hizo posible este contenido educativo.

### Qué aprenderás

Este curso explora la filosofía de diseño y los fundamentos matemáticos detrás de Simplicity, el lenguaje de scripting de nueva generación activado en la [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) en julio de 2025. Sigue la serie completa de cinco artículos y está estructurado en dos secciones de contenido principales:

1. **Fundamentos de Simplicity** — Por qué la computación en blockchain exige un lenguaje fundamentalmente distinto, las tres formas de combinar operaciones (secuencial, paralela, condicional) y los nueve combinadores centrales que forman un lenguaje matemáticamente completo
2. **De los tipos de datos a los programas** — Construir lógica booleana, aritmética y SHA-256 desde primeros principios; entender los efectos secundarios Failure y Reader que permiten la interacción con la blockchain; y aprender cómo los programas se comprometen a direcciones Taproot mediante Commitment Merkle Roots y se redimen con datos de testigo

### Requisitos previos

Este es un curso de **nivel experto** (aproximadamente 10 horas). Deberías sentirte cómodo con:
- Conceptos básicos de Bitcoin Script (qué hace la validación de transacciones)
- Conceptos fundamentales de programación (tipos, funciones, composición)
- Cierta familiaridad con la notación matemática es útil pero no obligatoria. Introducimos todo sobre la marcha

### Recursos clave

- **Artículos originales**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) del Dr. Russell O'Connor en Delving Bitcoin
- **Repositorio de Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — código fuente y pruebas formales en Rocq
- **Sitio web oficial**: [simplicity-lang.org](https://simplicity-lang.org/) — documentación y referencia de SimplicityHL
- **Blog de Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — visión técnica general

¿Listo para sumergirte en una de las piezas más elegantes de la ingeniería de Bitcoin? ¡Vamos!

## ¿Qué es Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Si llegas a este curso sin experiencia previa en Simplicity, este capítulo te orientará antes de que nos adentremos en lo más profundo.

### Simplicity en pocas palabras

Simplicity es un **lenguaje de contratos inteligentes nativo de Bitcoin**, activo hoy en la Liquid Network. Concebido por primera vez por el Dr. Russell O'Connor alrededor de 2012 y detallado en su artículo de 2017 *Simplicity: A New Language for Blockchains*, se activó en la Liquid Network en julio de 2025 tras años de verificación formal y desarrollo.

A diferencia de Solidity de Ethereum, que es un lenguaje de contratos de alto nivel Turing-completo, Simplicity es intencionalmente mínimo. Tiene:
- **Tres formadores de tipos** (unidad, suma, producto)
- **Nueve combinadores** (operaciones básicas y reglas de composición)
- **Sin bucles, sin recursión, sin memoria dinámica**

A partir de estas primitivas, puedes construir cualquier computación que necesites para la validación de transacciones, desde lógica booleana hasta el hashing SHA-256 completo.

### ¿Qué puedes hacer con Simplicity hoy?

Simplicity ya está impulsando aplicaciones reales en la Liquid Network. La más destacada es [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), un mercado de opciones sin oráculo donde los usuarios negocian opciones call sobre L-BTC usando USDt como colateral (el contrato subyacente también soporta puts). Otros proyectos de Simplicity en producción incluyen [Swaption](https://swaption.io/) de SideSwap (opciones) y el proyecto de código abierto [Deadcat](https://github.com/Resolvr-io/deadcat) de Resolvr (mercados de predicción). Más allá de las finanzas descentralizadas, Simplicity permite condiciones de gasto avanzadas como vaults, covenants y esquemas multisig complejos que serían imposibles o inseguros en Bitcoin Script.

### Qué es este curso — y qué no es

Esto **no** es un tutorial práctico de programación. Aquí no escribirás programas de Simplicity. Si buscas eso, consulta:
- [simplicity-lang.org](https://simplicity-lang.org/) — documentación oficial y el lenguaje de alto nivel SimplicityHL
- El [repositorio de Simplicity en GitHub](https://github.com/BlockstreamResearch/simplicity) — implementación de referencia, ejemplos y pruebas en Rocq
- La [entrada del blog de Blockstream](https://blog.blockstream.com/en-simplicity-github/) sobre cómo empezar

De lo que **sí** trata este curso: las **decisiones filosóficas y técnicas** detrás del diseño de Simplicity. ¿Por qué se creó este lenguaje de esta manera? ¿Por qué solo nueve combinadores? ¿Por qué ninguna recursión? ¿Por qué importa que el sistema de tipos se conecte con el cálculo de secuentes de Gentzen?

Piénsalo como entender **por qué el motor se construyó así**, en lugar de aprender a conducir el coche.

### ¿Para quién es esto?

Este curso es ideal para:
- **Desarrolladores de protocolo** que quieren entender los fundamentos de Simplicity antes de escribir código
- **Investigadores de Bitcoin** interesados en el enfoque de verificación formal y teoría de tipos
- **Informáticos** curiosos sobre la conexión entre el cálculo de secuentes y la computación en blockchain
- **Bitcoiners avanzados** que quieren ir más allá de una comprensión superficial de las capacidades de scripting de Liquid

Si términos como "tipos suma", "combinadores" o "cálculo de secuentes" te son completamente nuevos, no te preocupes: lo explicamos todo desde cero. Pero prepárate para un viaje denso y matemático.

### De artículos a curso

La serie original "Delving Simplicity" del Dr. O'Connor está estructurada como cinco artículos técnicos. Este curso reorganiza y anota ese material en un itinerario de aprendizaje progresivo con cuestionarios para poner a prueba tu comprensión a lo largo del camino. Las ideas, definiciones y pruebas son suyas; hemos adaptado el formato para una educación estructurada.

# Fundamentos de Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Formas fundamentales de combinar computaciones

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Ahora que Simplicity se ha activado en la Liquid Network, me gustaría hacer una inmersión profunda en la filosofía y el diseño del lenguaje Simplicity.

La validación de transacciones de Bitcoin es una aplicación significativamente distinta del diseño de lenguajes de programación habituales. El espacio de bloque tiene un coste alto, así que los programas deben ser compactos. Los programas en las transacciones de Bitcoin solo se ejecutan sobre una única entrada, y todos ejecutan el programa sobre la misma entrada. Además, el agente que autoriza la transacción ya conoce de antemano el resultado de la computación: que la transacción es válida.

Normalmente, el agente autorizante ejecutará computaciones mucho más costosas para obtener datos de testigo que certifiquen la validez de la transacción, mientras que los programas ejecutados en la blockchain necesitan comprobar la validez de esos datos de testigo. Comprobar la validez suele ser mucho más barato que demostrar la validez.

Hemos diseñado Simplicity teniendo en cuenta este tipo de retos únicos de diseño de lenguajes. Por ejemplo, Simplicity exige que las ramas no ejecutadas se poden para que no aparezcan en la blockchain. Los pasos de preprocesamiento están cuidadosamente diseñados para exhibir complejidad temporal (cuasi-)lineal respecto al tamaño del programa Simplicity. Se usa análisis estático en lugar de "gas", que no puede computarse sin ejecutar el código de una manera prescrita, de modo que los detalles del modelo de ejecución no se vuelvan críticos para el consenso. No hay asignación dinámica de memoria durante la ejecución. Y así sucesivamente.

Antes de adentrarnos en los detalles de diseño de Simplicity, quiero comenzar esta serie con algo de filosofía de programación sobre las formas generales de combinar bloques básicos de construcción para crear nueva funcionalidad.

### Composición

Supongamos que se está diseñando un lenguaje para transacciones programables en una blockchain como Bitcoin. En particular, los programas solo tienen acceso a los datos de la transacción y a los datos UTXO de las entradas, y la ejecución solo determina la validez de la transacción (lo cual permite que el resultado de la ejecución se pueda cachear). Digamos que se parte de un conjunto de operaciones básicas que pueden realizar diversas tareas, como computaciones básicas, leer y/o procesar datos de la transacción, y verificación de firmas. Cada operación consume algún tipo de entrada (posiblemente vacía) y devuelve algún tipo de salida. ¿De qué formas podemos combinar estas operaciones básicas en operaciones más complejas?

### Composición secuencial

![Sequential Composition](assets/en/001.webp)

El método de composición más fundamental es la composición secuencial. Si tenemos dos operaciones básicas, una cuyo tipo de dato de salida coincide con el tipo de dato de entrada de la otra, entonces podemos combinar estas dos operaciones en una nueva operación compuesta. Esta nueva operación ejecuta estas dos operaciones básicas en secuencia, tomando como entrada la entrada de la primera operación, pasando la salida de esa primera operación a la entrada de la segunda, y finalmente devolviendo la salida de esa segunda operación.

Por supuesto, no necesitamos limitarnos a combinar solo operaciones básicas. Ahora que tenemos algunas operaciones compuestas, también podemos combinarlas usando composición funcional.

En matemáticas, esta composición secuencial suele llamarse simplemente "composición", y uno podría pensar que esta es la única forma de componer cosas. Sin embargo, tenemos otras formas de componer operaciones.

### Composición paralela

![Parallel Composition](assets/en/002.webp)

Supongamos que tenemos dos operaciones, que pueden ser básicas o complejas, y que ambas toman el mismo tipo de entrada. Una segunda forma fundamental de componer estas dos operaciones es ejecutarlas ambas sobre la misma entrada. Esto se llama composición paralela, y el tipo de la salida es el "producto" de los tipos de las salidas de las operaciones originales, y contiene el par de las dos salidas.

Aunque se llama composición "paralela", y las dos operaciones podrían en principio ejecutarse en paralelo, la ejecución en paralelo no es un requisito operacional. Podemos implementar la composición paralela "secuencialmente" ejecutando una operación primero y luego la segunda. No nos importan los detalles de cómo se implementa la composición paralela, siempre que la salida sea la misma.

### Composición condicional

![Conditional Composition](assets/en/003.webp)

La composición condicional es la dual de la composición paralela. En este caso tenemos dos operaciones que producen la misma salida, y las componemos eligiendo una de ellas para ejecutar. La entrada de esta operación compuesta es la "suma" o "unión etiquetada" de los tipos de las entradas de las operaciones originales. En este caso la etiqueta, "Izquierda" o "Derecha", es un único bit en los datos de la entrada que determina qué tipo de dato se está transportando, y por tanto cuál de las dos operaciones puede ejecutarse.

La composición condicional funciona de la misma manera incluso cuando la entrada es la suma de dos tipos idénticos. El tipo suma sigue conteniendo una etiqueta, y el valor de esa etiqueta determina cuál de las dos operaciones se ejecuta.

### Composición en Bitcoin Script

Hay muchas formas de realizar estos tres tipos de composición en distintos lenguajes de programación. En Bitcoin Script, la composición secuencial se realiza (aproximadamente) mediante la concatenación de dos rutinas (por eso Bitcoin Script se llama un lenguaje de programación concatenativo), ya que la salida de una rutina queda en la pila para ser consumida por la rutina siguiente. La composición paralela se logra mediante el uso de operaciones de duplicado y de intercambio para manipular la pila, de modo que dos rutinas puedan ejecutarse sobre la misma entrada. Las cosas no son del todo sencillas, ya que lo que llamamos el "producto" de tipos normalmente se realiza utilizando múltiples elementos de la pila. Esperamos que puedas ver la idea general.

La composición condicional se realiza, por supuesto, mediante `OP_IF`, que ramifica según el valor en la pila. En este caso el elemento superior de la pila juega el papel de etiqueta, y normalmente el siguiente elemento o elementos de la pila son de distintos "tipos" que dependen del valor de la etiqueta. En cada caso los tipos de los elementos de la pila pueden ser adecuados solo para el procesamiento en una de las ramas del `OP_IF`. Sin embargo, tras llegar a `OP_ENDIF` los elementos de la pila deben tener un "tipo" consistente, de modo que el resto del script pueda continuar de forma independiente a cuál rama se tomó anteriormente.

### Composición en Simplicity

Diseñamos Simplicity con combinadores que implementan directamente estas tres formas de composición. Junto con algunos combinadores más para dar soporte a otras operaciones básicas relacionadas con los tipos producto y suma, el lenguaje central de Simplicity termina consistiendo en nueve combinadores que son suficientes para expresar cualquier computación finita. Discutiremos esto con más detalle en el próximo capítulo.

### Un cuarto tipo de composición

Antes de terminar, deberíamos mencionar que hay al menos un tipo más de composición que se encuentra en Ciencias de la Computación, que es la "composición recursiva". En la composición recursiva una operación se itera múltiples veces.

Nótese que Bitcoin Script no admite la composición recursiva, y de manera similar, hemos excluido explícitamente la recursión no acotada del diseño de Simplicity. Nuestra tesis es que la computación iterativa no acotada se implementa mejor mediante covenants recursivos que computan a través de múltiples transacciones. Esto permite a los usuarios evitar las restricciones de espacio de bloque y de estándar (*standardness*), y predecir mejor los costes de las transacciones.

Dicho esto, hay formas de abusar de la funcionalidad de delegación de Simplicity para proporcionar algo que se asemeja a una composición recursiva no acotada, lo cual podríamos discutir más adelante en esta serie.

### Conclusión

Repasamos las tres formas principales de composición para transformar operaciones básicas en operaciones complejas:

- composición secuencial
- composición paralela
- composición condicional

Discutimos cómo estas formas de composición se realizan en Bitcoin Script, y apuntamos a cómo han influido en el diseño del lenguaje Simplicity. Señalamos que el cuarto tipo de composición, la composición recursiva, está específicamente excluido tanto de Simplicity como de Bitcoin Script.

En el próximo capítulo describiremos los nueve combinadores que conforman el núcleo del lenguaje Simplicity, cómo sirven para realizar directamente estas tres formas de composición, y cómo esto conforma un lenguaje completo para describir cualquier computación finita.

## Completitud de combinadores de Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

En este capítulo presentamos el lenguaje central de Simplicity y mostramos que el lenguaje es completo, es decir, que cualquier computación finita puede expresarse dentro de él.

### Tipos de Simplicity

Simplicity admite tres constructores de tipos fundamentales. El tipo producto `A × B` representa las salidas de la composición paralela, mientras que el tipo suma `A + B` (unión etiquetada) gestiona las entradas de la composición condicional. El tercer tipo es el tipo unidad.

### Tipo unidad

El tipo unidad, denotado `𝟙` u `ONE`, contiene exactamente un valor: la tupla vacía `⟨⟩` o `()`. Este tipo de dato de cero bits no transporta ninguna información.

### Tipo suma

Un tipo suma `A + B` combina dos tipos con etiquetas que indican "izquierda" o "derecha". Los valores se escriben como `σᴸ(a)` o `inl(a)` para valores etiquetados a la izquierda, y `σᴿ(b)` o `inr(b)` para valores etiquetados a la derecha. Las etiquetas permanecen distintas incluso al combinar tipos idénticos.

#### Tipo booleano

El tipo `𝟙 + 𝟙`, denotado `𝟚` o `TWO`, representa un tipo de un bit con dos valores. Por convención, `σᴸ⟨⟩` representa falso/cero, mientras que `σᴿ⟨⟩` representa verdadero/uno.

### Tipo producto

Los tipos producto `A × B` contienen pares de valores escritos como `⟨a, b⟩` o `(a, b)`. El tipo `𝟚 × 𝟚` tiene cuatro valores, distintos de los cuatro valores en `𝟚 + 𝟚`.

### Expresiones centrales de Simplicity

Las operaciones se denotan como `f : A ⊢ B`, lo que significa tipo de entrada `A` y tipo de salida `B`. Simplicity es "de primer orden" — carece de tipos función.

### Dos operaciones básicas

El lenguaje central proporciona dos operaciones básicas:

**Identidad (`iden`).** La operación identidad hace pasar su entrada sin cambios:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unidad (`unit`).** La operación unidad descarta su entrada y devuelve la tupla vacía:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Estas forman familias con una operación por tipo.

### Tres combinadores de composición

La composición secuencial usa `comp f g` (escrito `f ⨾ g` o `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

La composición paralela usa `pair f g` (escrito `f ▵ g` o `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

La composición condicional usa `case f g : (A + B) × C ⊢ D`, que da a las ramas acceso a un entorno compartido `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

¿Por qué la composición condicional adopta esta forma — una suma emparejada con un entorno compartido `C` — en lugar de un `copair f g : A + B ⊢ C` más simple que solo elige una rama? Porque un `copair` desnudo no puede expresar la **distribución**: la función `dist : (A + B) × C ⊢ A × C + B × C` que empuja una entrada compartida hacia la rama que se tome. Al incorporar el entorno `C` directamente en `case`, Simplicity obtiene composición condicional *y* distribución a partir de un único combinador — una de las decisiones de diseño clave que mantiene el lenguaje central en solo nueve combinadores.

### Cuatro combinadores más

El consumo de productos usa `take` y `drop`:

**take** extrae el elemento izquierdo:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrae el elemento derecho:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

La producción de sumas usa `injl` e `injr`:

**injl** envuelve con una etiqueta izquierda:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** envuelve con una etiqueta derecha:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Los nueve combinadores centrales

En total, Simplicity tiene exactamente nueve combinadores centrales:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity y el cálculo de secuentes

El diseño de Simplicity deriva del fragmento conjuntivo-disyuntivo del cálculo de secuentes de Gentzen. Más precisamente, es una variante de la *interpretación funcional* del cálculo de secuentes, que a su vez es análoga a la correspondencia de Curry-Howard entre la deducción natural y el cálculo lambda. Las reglas de los combinadores exhiben "tipos más pequeños en las premisas que en las conclusiones", lo que permite a la Bit Machine — el intérprete de máquina de pila abstracta de Simplicity — minimizar la copia de datos durante la ejecución.

### Los valores no son expresiones

Las expresiones de Simplicity denotan operaciones, no valores. La notación `scribe b : A ⊢ B` representa una expresión única que siempre devuelve el valor `b`, sirviendo como conveniencia notacional más que como combinador. Esto refleja lo que ocurre en Bitcoin Script, donde operaciones como `OP_1` empujan valores en lugar de expresarlos directamente.

### El teorema de completitud de Simplicity

Con los nueve combinadores en mano, ¿cómo sabemos que no nos falta algo — que estos nueve realmente son suficientes? El teorema de completitud de Simplicity responde a esto: para cualquier función entre tipos (finitos) de Simplicity, alguna expresión de Simplicity la denota. La prueba es constructiva — muestra cómo construir la expresión:

1. **Descomponer la entrada**: Usando expresiones `case` anidadas, descomponer completamente cualquier entrada de cualquier tipo en sus bits constituyentes
2. **Construir una tabla de consulta**: Para cada entrada posible, usar `scribe` para producir la salida correspondiente
3. **Ensamblar**: Los `case` anidados y los `scribe` juntos forman una tabla de consulta gigante que implementa la función

Este teorema está formalmente verificado en el asistente de pruebas Rocq (antes Coq). La prueba forma parte del repositorio oficial de Simplicity y ha sido comprobada mecánicamente por su corrección.

Si bien el teorema de completitud garantiza que los nueve combinadores de Simplicity pueden expresar cualquier función entre tipos (finitos) de Simplicity, las expresiones resultantes de la construcción por tabla de consulta son impracticablemente grandes. Una función sobre entradas de 256 bits requeriría una tabla de consulta con 2²⁵⁶ entradas. Por eso los próximos capítulos se centran en construir expresiones eficientes que exploten la estructura de las computaciones, en lugar de resolver todo por fuerza bruta con tablas de consulta.

### Conclusión

El lenguaje central de Simplicity incluye un sistema de tipos y combinadores que permiten cualquier computación finita. Aunque el teorema de completitud garantiza la expresividad, las expresiones resultantes de la construcción genérica son impracticablemente grandes. El desarrollo práctico en Simplicity implica explotar la estructura computacional para lograr expresiones concisas. Los próximos capítulos exploran estructuras de datos, interacciones con transacciones y combinadores adicionales.

# De los tipos de datos a los programas

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Construyendo tipos de datos

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

En los capítulos anteriores, mostramos cómo el conjunto central de combinadores de Simplicity basta para implementar cualquier computación pura finita. Este capítulo muestra cómo construir estructuras de datos y computaciones prácticas a partir de estas primitivas — de la misma forma en que los ordenadores se construyen a partir de puertas lógicas.

### Lógica booleana

El tipo booleano, denotado `𝟚`, es igual a `𝟙 + 𝟙` y tiene dos valores: `σᴸ⟨⟩` (falso) y `σᴿ⟨⟩` (verdadero). Usando los combinadores centrales, se pueden construir los operadores de lógica booleana.

#### Operación And

La operación lógica `and : 𝟚 × 𝟚 ⊢ 𝟚` toma dos bits y devuelve un bit. La implementación ramifica según el primer bit: si es falso, devuelve falso; en caso contrario, devuelve el segundo bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Probando con `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Probando con `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Otras operaciones lógicas

La operación `not` requiere un combinador auxiliar:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

El `iden ▵ unit : A ⊢ A × 𝟙` inicial añade un "entorno" vacío a la entrada, permitiendo que el combinador `case` se aplique. El uso de `take` en las dos ramas descarta este entorno vacío para ejecutar `f` o `g`.

Otras operaciones lógicas booleanas:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Sumadores de bits

Un "semisumador" (half-adder) toma dos bits y los suma, produciendo una salida de dos bits: un bit de acarreo y un bit de suma.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Un "sumador completo" (full-adder) suma tres bits, produciendo una salida de dos bits. La entrada usa la tupla anidada `(𝟚 × 𝟚) × 𝟚`.

Para tuplas anidadas, se usa una notación compacta:

- `O f` denota `take f`
- `I f` denota `drop f`
- `H` denota `iden`

Por ejemplo, `I O H` significa `drop (take iden) : A × (B × C) ⊢ B`, extrayendo el valor del medio. La notación evoca dígitos binarios: al pensar en las tuplas anidadas como árboles binarios, la notación representa los dígitos binarios invertidos de las posiciones del árbol. Estas expresiones forman índices de De Bruijn para Simplicity.

**Nota:** La notación `I`, `O` y `H` solo se aplica a subexpresiones compuestas únicamente por `take`, `drop` e `iden`.

El sumador completo compone dos semisumadores, tomando el `or` lógico de los bits de acarreo:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

En la primera línea, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` ejecuta el semisumador sobre los dos primeros bits, guardando el último bit.

En la segunda línea, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` guarda el primer bit (el acarreo de salida del primer semisumador) y ejecuta el semisumador sobre los dos últimos bits.

En la última línea, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` toma el OR lógico de los dos primeros bits (los acarreos de salida de ambos semisumadores) y devuelve el bit de suma de salida del segundo semisumador.

Esto demuestra la programación en Simplicity: usar la notación `I`, `O` y `H` para referenciar bits de datos, formando "entornos" adecuados para llamar a otras funciones mediante composición secuencial.

Los usuarios no definen operaciones de bajo nivel directamente. Más adelante en esta serie se discuten los jets de la biblioteca estándar que implementan funciones comunes. No se espera que los usuarios finales programen directamente en Simplicity, de forma similar a Bitcoin Script. En su lugar, lenguajes de más alto nivel como SimplicityHL generan código Simplicity, gestionando los "entornos" de las subexpresiones y traduciendo variables con nombre en las secuencias apropiadas de `take` y `drop`.

### Vectores

Los vectores de longitud fija se definen formando productos iterados del tipo `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Estos pueden escribirse como `A^2`, `A^4`, `A^8`, etc.

Los vectores se definen solo para longitudes que son potencias de dos. Otras potencias requieren elegir convenciones de agrupación.

Dada una expresión `f : A ⊢ B`, el emparejamiento repetido "mapea" sobre vectores de longitud fija:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Dada la función `f : A × B ⊢ B`, la iteración o "pliegue" (folding) sobre vectores de longitud fija:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Existen muchas variantes. Dada `f : A × B ⊢ C`, "zip" sobre vectores emparejados con `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Dada `f : (A × B) × C ⊢ C`, pliegue sobre vectores emparejados con `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combinando `map` y `fold-right` se crean combinadores acumulativos: `f : A × C ⊢ C × B` produce `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Son posibles muchas más variantes.

#### Palabras multi-bit

Un vector de bits produce enteros de múltiples bits. Por ejemplo, `𝟚³²` es un tipo palabra de 32 bits. `𝟚²⁵⁶` es un tipo palabra de 256 bits, adecuado para hashes y operaciones criptográficas.

Usando el sumador completo, una variante de las operaciones de vector define un "sumador de acarreo en cascada" (ripple carry adder) sobre palabras multi-bit:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` toma dos números binarios de n bits y una entrada de acarreo de un bit, devolviendo un indicador de acarreo de salida de un bit y una suma de n bits.

#### SHA-256

Definiendo recursivamente operaciones aritméticas sobre palabras multi-bit — resta, multiplicación, división — y operaciones lógicas bit a bit como AND, OR, XOR lógicos, y combinando repetidamente estas operaciones, incluso la función de compresión de bloque de SHA-256 puede construirse:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

La compresión SHA-256 está formalmente definida usando Simplicity dentro del asistente de pruebas Rocq (antes Coq), con una prueba formal de que la implementación de `sha256-hash-block` es correcta.

La compresión se ejecuta demasiado lento como Simplicity puro. Los jets ejecutan funciones comunes como la compresión SHA-256 de forma nativa. Las implementaciones puras en Simplicity sirven como especificaciones formales para los jets.

### Tipos opción

Los tipos opción resultan de tomar una suma con el tipo unidad:

```
Option A ≔ 𝟙 + A
```

El tipo `Option A` puede escribirse como `A?` o `𝕊 A` (donde `𝕊` significa "sucesor"). Las funciones se mapean sobre tipos opción:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Se pueden definir combinadores monádicos como bind:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Búferes de longitud variable

Los "búferes" son tipos para vectores parcialmente llenos:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

El tipo `Xᑉ⁸` se expande a `(1 + X⁴) × ((1 + X²) × (1 + X))`. Tratando esto como un polinomio y expandiéndolo se obtiene `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretado como un tipo, representa la suma de todas las tuplas posibles de X hasta 7, incluyendo la tupla vacía. Este es exactamente el tipo de listas con longitud estrictamente menor que 8.

Al igual que con los vectores, se pueden definir operaciones de mapeo y pliegue sobre búferes. Las operaciones de pila incluyen `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` y `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` añade un elemento al búfer, devolviendo un vector completo si se produce desbordamiento. `pop-<n` elimina un elemento, devolviendo el búfer más pequeño y el elemento eliminado, devolviendo opcionalmente nada si el búfer original estaba vacío.

La definición de `push-<n`, de forma recursiva:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

El Simplicity puro se vuelve difícil de seguir más allá de ciertos niveles de complejidad. Los usuarios finales utilizan lenguajes de más alto nivel como SimplicityHL que generan estas expresiones idiomáticas.

### Conclusión

Este capítulo mostró cómo construir operaciones lógicas a partir de bits. A partir de estas, surgió la aritmética a nivel de bit, permitiendo razonar sobre la ejecución. Se desarrollaron tipos vector, demostrando la iteración sobre palabras multi-bit para la definición aritmética. Continuando, operaciones criptográficas como SHA-256 y la validación de firmas Schnorr pueden definirse usando únicamente combinadores de Simplicity — todas, de hecho, definidas usando Simplicity.

Este capítulo no es una guía exhaustiva de todos los tipos de datos y operaciones posibles que se pueden construir en Simplicity, pero ilustra cómo lograr funcionalidad práctica dentro de las restricciones de Simplicity. A pesar de tener tipos finitamente acotados, se pueden definir vectores útiles, tipos búfer y operaciones que iteran sobre estas estructuras.

Las especificaciones reales de las operaciones de la biblioteca estándar difieren ligeramente de las definiciones aquí presentadas. Por ejemplo, el sumador completo usa un XOR de 3 vías y una función lógica de "mayoría" en lugar de dos semisumadores.

En la práctica, los programas de Simplicity usan jets para operaciones aritméticas y criptográficas. Sin embargo, los jets solo reemplazan expresiones. Los combinadores que iteran sobre búferes y vectores no pueden ser reemplazados por jets, y aparecen en los programas reales de Simplicity. Aunque, en lugar de usarlos directamente, los usuarios finales emplean lenguajes de más alto nivel como SimplicityHL que generan tales expresiones.

Los combinadores definidos recursivamente parecen crecer exponencialmente en tamaño de expresión. Esto no es problemático. Durante la serialización, las expresiones se codifican como DAGs (grafos acíclicos dirigidos) en lugar de árboles. La representación real crece solo linealmente.

Hasta ahora, solo se consideraron computaciones puras. La interacción con los datos de la transacción para tareas como firmar transacciones requiere alguna forma de que los programas fallen si las firmas son inválidas. El próximo capítulo discute los efectos secundarios en Simplicity.

## Dos efectos secundarios

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

En los capítulos anteriores, mostramos cómo construir algunas estructuras de datos y computaciones usando el conjunto central de combinadores de Simplicity. Como señalamos, los combinadores centrales bastan para implementar cualquier computación pura finita. Esto plantea la pregunta: ¿qué más se puede lograr? Podemos añadir efectos secundarios adicionales a nuestras expresiones.

Hay varios tipos de posibles efectos secundarios para las expresiones: actualización de estado, escritura en un registro (log), lanzamiento de una excepción, lectura desde un entorno, llamada a una continuación, etc. Los efectos secundarios disponibles en Simplicity dependerán de la aplicación.

Para las aplicaciones de Bitcoin y Liquid, actualmente tenemos dos efectos secundarios: el efecto Failure, que es un efecto de excepción donde la excepción tiene tipo `𝟙`, y el efecto Reader, que permite acceder a datos del entorno de la transacción. Nuestros combinadores centrales son "puros"; no tienen efectos secundarios. Sin embargo, los jets pueden introducir nuevas primitivas que sí tienen efectos secundarios.

### Jets con efectos

Hablaremos más sobre los jets más adelante en este curso, pero aquí presentamos algunos jets de ejemplo para ilustrar sus efectos secundarios.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` es un jet para una expresión que toma una clave pública x-only, un mensaje de 256 bits y una firma Schnorr, ¡y no devuelve nada! Según su tipo, debería comportarse igual que un `unit`. La diferencia radica en el efecto secundario del jet: si la validación de la firma falla, entonces toda la computación se aborta lanzando una excepción (de tipo unidad). Este es el efecto Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` es un jet elemental para expresar el efecto Failure. Si la entrada de `verify` es `false`, toda la computación se aborta lanzando una excepción. Si la entrada es `true`, no se devuelve nada, pero la computación puede continuar.

#### Hashes de transacción

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` parece ser una función constante, ya que solo hay un valor de entrada posible: la tupla vacía. Sin embargo, este jet lee del entorno de la transacción y produce un hash de los datos de la transacción análogo al digest de mensaje `SIGHASH_ALL` usado en la verificación de firmas de Bitcoin Script. Este es un ejemplo del efecto Reader: el valor devuelto depende del entorno de la transacción dentro del cual se ejecuta el jet. Existen varios otros jets de hashing que hacen hash de distintos subconjuntos de los datos del entorno de la transacción para ayudar a construir digests de mensaje personalizados para firmas.

#### Jets de introspección

`input-sequence : 𝟚³² ⊢ 𝟚³²?` es una función que toma un índice de entrada y devuelve el número de secuencia de la transacción para esa entrada, devolviendo opcionalmente nada si el índice está fuera de rango. De nuevo, el valor de salida no es una función pura del índice de entrada, sino que la operación usa el efecto Reader para acceder al entorno de la transacción y así determinar el valor de salida. Existen varios otros jets de introspección que devuelven distintos fragmentos de los datos del entorno de la transacción.

### Clasificando los efectos

No todos los efectos secundarios son iguales. Algunos efectos secundarios se comportan mejor que otros. Podemos clasificar los efectos según cuán susceptibles son a las transformaciones de programas.

#### Efectos conmutativos

Un efecto conmutativo es aquel en el que, si intercambias las salidas de dos expresiones, puedes intercambiar de forma segura las propias expresiones sin cambiar el efecto de la expresión. Considera `swap = I H ▵ O H : A × B ⊢ B × A`. Si `f ▵ g ⨾ swap = g ▵ f` para toda expresión `f` y `g` con efectos secundarios, entonces los efectos son conmutativos.

Leer datos de la transacción desde el entorno es un efecto conmutativo porque el resultado de leer del entorno es el mismo, sin importar en qué orden ejecutemos la lectura.

En general, lanzar una excepción no es un efecto conmutativo. Si `f` lanza alguna excepción `e₁` y `g` lanza otra excepción `e₂`, entonces qué excepción se lanza desde el par de `f` y `g` depende del orden en que se ejecuten.

Sin embargo, en el caso especial del efecto Failure, en el que solo puede lanzarse una excepción de tipo unidad, el efecto es conmutativo. Sin importar cuál de `f` o `g` lance una excepción, la excepción resultante será la misma, porque solo hay un posible valor de excepción.

#### Efectos idempotentes

Un efecto idempotente es aquel en el que, si duplicas la salida de una expresión, puedes duplicar de forma segura la propia expresión sin cambiar el efecto de la expresión. Considera `dup = iden ▵ iden : A ⊢ A × A`. Si `f ⨾ dup = dup ⨾ f ▵ f` para toda `f` con efectos secundarios, entonces los efectos son idempotentes.

Leer datos de la transacción desde el entorno es un efecto idempotente. Lanzar una excepción también es un efecto idempotente. Aunque solo se ejecutará una de las dos expresiones duplicadas, cualquier excepción lanzada por `dup ⨾ f ▵ f` será la misma que la excepción lanzada por `f ⨾ dup`.

Sin embargo, escribir en un registro (log) puede no ser idempotente, ya que duplicar el efecto haría que el mensaje del log apareciera dos veces. No obstante, si el log consiste en un _conjunto_ de mensajes en lugar de una _lista_ de mensajes, entonces el efecto sería idempotente (y conmutativo), porque la inserción en un conjunto es en sí misma una operación idempotente.

#### Efectos unitarios

Un efecto unitario es aquel en el que, si descartas la salida de una expresión, puedes descartar de forma segura la propia expresión sin cambiar los efectos de la expresión. Si siempre se cumple que `f ⨾ unit = unit` para toda `f` con efectos secundarios, entonces tus efectos son unitarios.

Leer datos del entorno es uno de los pocos tipos de efectos unitarios. Si el resultado de leer los datos de la transacción desde el entorno se descarta, toda la expresión que realiza la lectura puede descartarse.

El efecto Failure no es unitario. Si `f` lanza una excepción, entonces también lo hará `f ⨾ unit`; la ejecución ni siquiera llegará al combinador `unit` antes de que la computación se aborte. Por otro lado, `unit` obviamente no lanzaría ninguna excepción, así que los efectos de `f ⨾ unit` y `unit` serían distintos.

En resumen, así se comportan los efectos discutidos anteriormente frente a estas tres propiedades:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Efectos permitidos en Simplicity

Cuantas más propiedades bien comportadas tenga un tipo de efecto, más margen tendrá un optimizador de Simplicity para transformar programas que usen esos efectos. Idealmente solo permitiríamos efectos que tuvieran las tres propiedades: conmutativos, idempotentes y unitarios. Esto permitiría a un optimizador realizar cualquier tipo de transformación de programa que quisiera. Sin embargo, leer de un entorno es el único efecto que satisface las tres propiedades.

En cambio, exigimos que los efectos de Simplicity sean conmutativos e idempotentes. Ambos efectos que usamos en Simplicity, el efecto Failure y el efecto Reader, son conmutativos e idempotentes. Esto permite realizar una amplia clase de optimizaciones sobre el código de Simplicity.

Sin embargo, la transformación de "descarte" descrita anteriormente, que intenta reemplazar `f ⨾ unit` con `unit`, o cualquier transformación similar, no está permitida si `f` puede producir un efecto Failure. En efecto, imagina que `f` contuviera una aserción `bip0340-verify`. Sería desastroso intentar optimizar esa comprobación.

### ¿Por qué permitir efectos secundarios en absoluto?

¿Por qué permite Simplicity efectos secundarios en absoluto? ¿No sería mejor que cada programa tomara toda la transacción como entrada y devolviera una salida booleana que decidiera si una transacción es válida o no?

#### Verificación por lotes

Una razón por la que tenemos el efecto Failure es dar soporte a la [verificación por lotes](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) de firmas Schnorr. En la verificación por lotes, muchas comprobaciones individuales de firmas Schnorr se agrupan de tal manera que si falla una sola comprobación de firma, todo el lote falla.

Este procedimiento de agrupación mejora la eficiencia frente a verificar cada firma individualmente. La desventaja es que si la verificación por lotes falla, no sabemos qué comprobación o comprobaciones de firma específicas fallaron.

Al usar el efecto secundario Failure, `bip0340-verify` garantiza que si una comprobación de firma falla, toda la transacción falla. Si `bip0340-verify` en su lugar devolviera `𝟚`, un tipo booleano, para éxito o fallo, entonces una comprobación de firma fallida podría seguir llevando a una rama donde el script tiene éxito. En tal caso necesitaríamos saber si la firma en particular es válida o no, y por tanto no podríamos aprovechar la verificación por lotes.

#### Datos de transacción precomputados

Un problema en las primeras versiones de Bitcoin Script era que la función de hash usada para crear digests de mensaje para las firmas era lineal en el tamaño de la transacción. Normalmente cada entrada crea al menos un digest de mensaje para la verificación de firma, así que en general la cantidad de hashing era cuadrática en el tamaño de la transacción.

Este problema se solucionó en Segwit y en iteraciones posteriores de Bitcoin Script redefiniendo los digests de mensaje de forma que pudieran calcularse en tiempo constante por comprobación de firma. Esto se basa en tener `PrecomputedTransactionData`, que precomputa los hashes de los datos de la transacción una vez y luego se comparte entre las computaciones de sighash de cada entrada. Los jets de hashing de transacciones de Simplicity dependen del mismo tipo de datos de transacción precomputados para garantizar que los jets se ejecuten en tiempo constante.

Supongamos que `sig-all-hash` no usara el efecto Reader. Supongamos que de alguna manera lográramos construir un tipo de Simplicity para el entorno de la transacción. Llamémoslo `TxEnv`, de modo que `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` fuera el tipo del jet. Tal definición requeriría que el jet `sig-all-hash` pudiera calcular el hash de cualquier transacción, no solo de la transacción con la que está relacionado. Los programas de Simplicity podrían copiar el `TxEnv` dado y pasar una copia modificada de este a `sig-all-hash`. En tal caso `sig-all-hash` no podría depender de `PrecomputedTransactionData`, y volveríamos a requerir tiempo lineal respecto a los datos de la transacción que se pasaran a esta versión de `sig-all-hash`.

Debido a que `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` usa el efecto Reader para acceder a los datos de la transacción, _solo_ obtiene acceso a un entorno de transacción fijo. Por esa razón, la implementación del jet puede usar de forma segura `PrecomputedTransactionData` y operar en tiempo constante.

### Agregación de firmas entre entradas

Aunque ni Liquid ni Bitcoin admiten actualmente la [agregación de firmas entre entradas](https://hrf.org/latest/cisa-research-paper/) (cross-input signature aggregation), nos gustaría comprobar que Simplicity puede ser compatible con ella cuando llegue el momento.

Aunque los detalles no se han resuelto, imaginamos que la semi-agregación se implementaría usando un efecto Writer. Es decir, un nuevo jet con un tipo como `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` tomaría una clave pública, un digest de mensaje y la componente `r` de una firma Schnorr (una firma Schnorr consiste en una componente `r` y una componente `s`) y la escribiría en un registro (log) de la transacción antes de continuar con la ejecución. Luego, en algún otro punto de la transacción o junto con la transacción, se proporcionaría una componente `s` agregada para todas las firmas Schnorr semi-agregadas. La transacción solo sería válida cuando se proporcionara dicha componente `s` agregada para todas las claves, mensajes y componentes `r` registradas.

Para cumplir con los requisitos de Simplicity, este efecto Writer necesita ser idempotente y conmutativo. Esto puede garantizarse tratando el log del escritor como un conjunto de tuplas de clave, mensaje y componente `r`. Esto funciona porque las operaciones de conjunto son idempotentes y conmutativas. Tratar el log como un conjunto de valores sería compatible con el algoritmo de verificación de semi-agregación.

### Conclusión

En este capítulo analizamos la incorporación de efectos secundarios a las computaciones que Simplicity puede realizar. Clasificamos varios tipos de efectos según su buen comportamiento respecto a distintos tipos de transformación de programas. Decidimos restringir los efectos de Simplicity a aquellos que son conmutativos e idempotentes.

Los dos efectos que usamos para las aplicaciones de Bitcoin y Liquid son el efecto Reader, para acceder al entorno de la transacción, y el efecto Failure, para abortar y hacer fallar el programa. Algunos jets utilizan operaciones primitivas donde pueden producirse este tipo de efectos secundarios.

El efecto Failure determina la salida de un programa de Simplicity: el programa falla, invalidando la transacción, o el programa tiene éxito. El efecto Reader proporciona un tipo de entrada a un programa de Simplicity: el entorno que contiene los datos de la transacción. Pero también necesitamos proporcionar otras entradas, como firmas digitales, a los programas de Simplicity.

En el próximo capítulo veremos qué son los programas de Simplicity, cómo se convierten en direcciones y cómo añadimos otras entradas, como firmas, a los programas de Simplicity.

## Programas y direcciones

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

En el capítulo anterior describimos dos efectos secundarios usados en Simplicity: el efecto Failure, que determina el éxito o fracaso de un programa, y el efecto Reader, que da acceso al entorno de la transacción. Ahora pasamos a la pregunta práctica: ¿qué es exactamente un programa de Simplicity, y cómo se convierte en una dirección en la blockchain?

### Programas de Simplicity

Un programa de Simplicity se define como una expresión de Simplicity de tipo `𝟙 ⊢ 𝟙`. Esta firma de tipo significa que el programa no toma ninguna entrada significativa (solo el valor unidad) y no produce ninguna salida significativa (solo el valor unidad). El efecto Reader captura la entrada del entorno de la transacción, mientras que el efecto Failure indica éxito o fracaso. Estos efectos gestionan la E/S en lugar de los propios tipos de Simplicity.

### Commitment Merkle Root

En lugar de almacenar programas completos en la cadena, Bitcoin emplea compromisos (*commitments*) — una práctica que se extiende desde Pay-to-Script-Hash (P2SH). Simplicity usa un Commitment Merkle Root (CMR).

Cada combinador recibe una etiqueta SHA-256 derivada del patrón: `Simplicity␟Commitment␟[identifier]`, donde `␟` representa el código ASCII 31 (el separador de unidad).

Cada etiqueta es el hash SHA-256 de la cadena de preimagen correspondiente listada a continuación:

| Combinator | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Una expresión de Simplicity se hashea de forma recursiva a un CMR de 256 bits computando un midstate SHA-256 etiquetado para cada combinador junto con los CMR de sus argumentos (escribimos `#ᶜ(e)` para el CMR de la expresión `e`, y `∥` para la concatenación de bytes):

| Combinator | CMR rule |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Los combinadores binarios (`comp`, `pair`, `case`) concatenan los CMR de ambos hijos; los combinadores unarios (`take`, `drop`, `injl`, `injr`) concatenan el CMR de su único hijo tras un relleno de 32 bytes de `0x00`; y las hojas nularias (`iden`, `unit`) hashean su etiqueta sola. Dos convenciones mantienen este cálculo barato: se usan midstates SHA-256 de modo que **cada expresión requiere como máximo una llamada a la función de compresión SHA-256** (asumiendo que el midstate hasta las etiquetas constantes está precomputado), y los constructores de un solo argumento prefijan su argumento con 32 bytes de relleno `0x00`, lo que permite algo de precomputación adicional a las implementaciones que la deseen.

Para el combinador `unit` — un constructor nularia sin subexpresiones argumento — esta regla se especializa a `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, donde `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (la etiqueta se introduce dos veces). El CMR resultante para el programa trivial `unit` es:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Fundamentalmente, el CMR no compromete los tipos de las expresiones de Simplicity, y se apoya en la inferencia de tipos durante la redención.

### Direcciones

Las direcciones emplean el mecanismo Taproot de BIP-0341 con CMRs comprometidos bajo la versión de TapLeaf `0xbe`. El proceso implica:

1. Calcular un hash etiquetado de TapLeaf combinando el byte de versión, la longitud del CMR y el propio CMR
2. Ajustar (*tweak*) una clave pública interna (usando un punto NUMS cuando no se desea una ruta de gasto por clave)
3. Convertir a formato bech32m
4. Añadir las sumas de verificación (checksums) correspondientes

Cuando no se desea una ruta de gasto por clave, la clave pública interna se fija en un punto **NUMS** ("Nothing-Up-My-Sleeve"): un punto de curva elegido deliberadamente de modo que nadie conoce su logaritmo discreto — en otras palabras, un punto sin clave privada correspondiente. Como nadie puede producir jamás una firma para él, la ruta de gasto por clave queda demostrablemente inutilizable, y la salida solo puede gastarse a través de la ruta de script comprometida de Simplicity. En una aplicación real, este punto NUMS debería aleatorizarse tal como recomienda BIP-0341, de modo que las salidas sin ruta de gasto por clave sean indistinguibles de las salidas Taproot ordinarias (un beneficio de privacidad).

#### De Simplicity a dirección

Recorramos toda la derivación para el programa más simple posible: `unit : 𝟙 ⊢ 𝟙`, una operación no-op que siempre tiene éxito.

**1. Etiqueta del combinador.** Primero calcula la etiqueta de `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Introduce la etiqueta dos veces para obtener el CMR del programa:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash de TapLeaf.** Prefija el CMR con la versión de TapLeaf de Simplicity `0xbe` y la longitud del CMR `0x20` (32 bytes), y luego toma el hash etiquetado de TapLeaf de Elements (un hash etiquetado es `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Con solo esta única hoja no hay TapBranches, así que este hash ya es la raíz del TapTree.

**4. TapTweak.** Dado que no queremos ruta de gasto por clave, usamos el punto NUMS de BIP-0341 como clave interna y lo ajustamos (*tweak*) con la raíz del TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Clave de salida.** Ajusta la clave interna sobre la curva, `output_pk = lift_x(internal_pk) ⊕ t·G` (la aritmética de curva elíptica se resume aquí), obteniendo la clave de salida x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Dirección Bech32m.** Codifica la clave de salida x-only, prefija con una `p` (el carácter de versión de testigo SegWit v1), añade el prefijo legible por humanos de la Liquid-testnet `tex1`, y añade la suma de verificación Bech32m. La dirección final es:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Fue mucho trabajo — pero gran parte lo exige el propio Taproot, no Simplicity.

### Expresiones de testigo

Un nuevo tipo de combinador aborda la ausencia de entrada en los programas de Simplicity: la expresión de testigo (*witness expression*). El combinador `witness` permite integrar en los programas datos de firma y otro material de testigo.

```
      w : B
-----------------
witness w : A ⊢ B
```

La semántica de la expresión de testigo es sencilla: ignora su entrada y simplemente devuelve el valor `w` (que puede ser de cualquier tipo de Simplicity), es decir, `⟦witness w⟧(a) = w`. Esto no añade **ninguna nueva expresividad** — por el teorema de completitud, Simplicity ya puede construir cualquier función constante de este tipo (recuerda la macro `scribe` de los capítulos anteriores). El sentido del combinador `witness` reside enteramente en su **CMR**: el valor `w` queda **excluido** del CMR de la expresión, de modo que la dirección puede calcularse antes de que se conozca `w`, y `w` se proporciona en el momento de la redención.

Esta decisión de diseño da soporte a la poda (*pruning*) — las ramas condicionales no ejecutadas no necesitan revelarse en la cadena, incluidas sus expresiones de testigo asociadas. Cuando se poda una rama, el verificador solo necesita el CMR del subárbol podado, no su contenido real.

### Valores de testigo

Podría parecer una limitación que una expresión de testigo solo pueda contener un *valor*, y no una expresión de Simplicity más general. Pero los programas para blockchains basadas en UTXO se ejecutan una sola vez. No hay necesidad de pasar toda una subexpresión a un nodo de testigo: el usuario simplemente puede ejecutar esa subexpresión por su cuenta, fuera de la cadena, y transcribir su salida en el valor de testigo para obtener el mismo resultado.

(Más adelante en este curso conoceremos el combinador `disconnect`, que se comporta de forma muy similar a una expresión de testigo que *sí* toma toda una expresión de Simplicity como argumento).

Un diseño alternativo alimentaría todos los datos de testigo como un argumento del programa de Simplicity de nivel superior. Se prefieren las expresiones de testigo por dos razones. Primero, la **poda**: las ramas no ejecutadas de las expresiones `case` nunca se revelan en la cadena, y cualquier expresión de testigo dentro de esas ramas se poda junto con ellas. Segundo, la **localidad**: las expresiones de testigo nos permiten colocar cada valor de testigo exactamente donde se usa, en lugar de tener que propagarlo desde la entrada de nivel superior del programa.

### Inferencia de tipos

Dado que los CMR no comprometen los tipos, el sistema de tipos se reconstruye durante la redención. El algoritmo de inferencia de tipos de Simplicity determina los tipos mínimos para cada subexpresión basándose en la estructura de combinadores. Más precisamente, la inferencia calcula el tipo *principal* (más general) de cada subexpresión; cualquier variable de tipo que quede libre se instancia entonces al tipo unidad `𝟙`, lo que produce un tipo único y mínimo para el programa.

### Conclusión

En este capítulo establecimos que los programas de Simplicity son expresiones de tipo `𝟙 ⊢ 𝟙`, explicamos cómo se construyen los Commitment Merkle Roots a partir de hashes SHA-256 etiquetados de cada combinador, y mostramos cómo los CMR se convierten en direcciones en cadena mediante Taproot (BIP-0341). Presentamos las expresiones de testigo como el mecanismo para proporcionar datos de firma y otras entradas en el momento del gasto, sin comprometerse con sus valores en el momento de la creación de la dirección.

# Sección final

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Reseñas y valoraciones

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusión

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
