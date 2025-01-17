---
name: Boltzmann Calculator
description: Comprender el concepto de entropía y cómo usar Boltzmann
---
![cover](assets/cover.webp)

***ADVERTENCIA:** Tras la detención de los fundadores de Samourai Wallet y la incautación de sus servidores el 24 de abril, el sitio web KYCP.org no está actualmente accesible. El Gitlab que alojaba el código del Python Boltzmann Calculator también ha sido incautado. Actualmente ya no es posible descargar esta herramienta. Sin embargo, es posible que el código sea republicado por otras personas en las próximas semanas. Mientras tanto, aún puedes aprovechar este tutorial para entender el funcionamiento del Boltzmann Calculator. Los indicadores proporcionados por esta herramienta son aplicables a cualquier transacción Bitcoin y también pueden ser calculados manualmente. Proporcionaré todos los cálculos necesarios en este tutorial. Si ya habías descargado la herramienta Python en tu máquina o si utilizas un RoninDojo, puedes continuar utilizando la herramienta y seguir este tutorial normalmente, todavía funciona.*

_Estamos siguiendo de cerca la evolución de este caso así como los desarrollos relacionados con las herramientas asociadas. Ten la seguridad de que actualizaremos este tutorial a medida que estén disponibles nuevas informaciones._

_Este tutorial se proporciona únicamente con fines educativos e informativos. No respaldamos ni alentamos el uso de estas herramientas para fines criminales. Es responsabilidad de cada usuario cumplir con las leyes en su jurisdicción._

---

La Calculadora de Boltzmann es una herramienta para analizar una transacción de Bitcoin midiendo su nivel de entropía junto con otras métricas avanzadas. Proporciona perspectivas sobre las conexiones entre las entradas y salidas de una transacción. Estos indicadores ofrecen una evaluación cuantificada de la privacidad de una transacción y ayudan a identificar posibles errores.

Esta herramienta Python fue desarrollada por los equipos de Samourai Wallet y OXT, pero se puede utilizar en cualquier transacción de Bitcoin.

## ¿Cómo usar la Calculadora de Boltzmann?
Para usar la Calculadora de Boltzmann, tienes dos opciones disponibles. La primera es instalar la herramienta Python directamente en tu máquina. Alternativamente, puedes optar por el sitio web KYCP.org (_Conoce la Privacidad de tu Moneda_), que ofrece una plataforma de uso simplificado. Para los usuarios de RoninDojo, ten en cuenta que esta herramienta ya está integrada en tu nodo.

Usar el sitio KYCP es bastante fácil: solo ingresa el identificador de la transacción (TXID) que deseas analizar en la barra de búsqueda y presiona `ENTER`.
![KYCP](assets/1.webp)
Luego encontrarás diferentes información sobre la transacción, incluyendo los enlaces entre las entradas y salidas. Haz clic en `enlaces determinísticos`.
![KYCP](assets/2.webp)
Llegarás a la página dedicada a los indicadores de la Calculadora de Boltzmann.
![KYCP](assets/3.webp)
Para aquellos que prefieren usar la herramienta directamente desde su nodo RoninDojo, es accesible a través de `RoninCLI > Samourai Toolkit > Calculadora de Boltzmann`.

Al igual que con el sitio KYCP.org, una vez instalada la herramienta Python, simplemente necesitarás pegar el TXID de la transacción que deseas analizar.

![KYCP](assets/7.webp)

Luego, presiona la tecla `ENTER` para obtener los resultados.

![KYCP](assets/8.webp)

## ¿Cuáles son los indicadores de la Calculadora de Boltzmann?
### Combinaciones / Interpretaciones:
El primer indicador que calcula el software es el número total de combinaciones posibles, indicado bajo `nb combinations` o `interpretations` en la herramienta.

Teniendo en cuenta los valores de los UTXOs involucrados en la transacción, este indicador calcula el número de formas en que las entradas pueden asociarse con las salidas. En otras palabras, determina el número de interpretaciones plausibles que una transacción puede suscitar desde la perspectiva de un observador externo que la analiza.
Por ejemplo, un coinjoin estructurado según el modelo Whirlpool 5x5 presenta `1,496` combinaciones posibles: ![KYCP](assets/4.webp)
Un coinjoin de Ciclo de Aumento Whirlpool 8x8, por otro lado, presenta `9,934,563` interpretaciones posibles: ![KYCP](assets/5.webp)
En contraste, una transacción más tradicional con 1 entrada y 2 salidas solo presentará una única interpretación: ![KYCP](assets/6.webp)

### Entropía:
El segundo indicador calculado es la entropía de una transacción, designada por `Entropía`.
En el contexto general de la criptografía y la información, la entropía es una medida cuantitativa de la incertidumbre o imprevisibilidad asociada con una fuente de datos o un proceso aleatorio. En otras palabras, la entropía es una forma de medir cuán difícil es predecir o adivinar la información.

En el contexto específico del análisis de cadenas, la entropía también es el nombre de un indicador, derivado de la entropía de Shannon y [inventado por LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), que se calcula con la herramienta Boltzmann.

Cuando una transacción presenta un alto número de combinaciones posibles, a menudo es más relevante referirse a su entropía. Este indicador permite medir la falta de conocimiento de los analistas sobre la configuración exacta de la transacción. En otras palabras, cuanto mayor es la entropía, más difícil se vuelve para los analistas la tarea de identificar movimientos de bitcoin entre entradas y salidas.

En la práctica, la entropía revela si, desde la perspectiva de un observador externo, una transacción presenta múltiples interpretaciones posibles, basándose únicamente en las cantidades de entradas y salidas, sin considerar otros patrones y heurísticas externos o internos. Una alta entropía es entonces sinónimo de mejor confidencialidad para la transacción.

La entropía se define como el logaritmo binario del número de combinaciones posibles. Aquí está la fórmula utilizada:
```plaintext
E: la entropía de la transacción
C: el número de combinaciones posibles para la transacción

E = log2(C)
```

En matemáticas, el logaritmo binario (logaritmo base-2) corresponde a la operación inversa de elevar 2. En otras palabras, el logaritmo binario de `x` es el exponente al que se debe elevar `2` para obtener `x`. Este indicador se expresa así en bits.

Tomemos el ejemplo de calcular la entropía para una transacción coinjoin estructurada según el modelo Whirlpool 5x5, que, como se mencionó anteriormente, ofrece un número de combinaciones posibles de `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```
Así, esta transacción coinjoin muestra una entropía de `10.5469 bits`, lo cual se considera muy satisfactorio. Cuanto mayor sea este valor, más interpretaciones diferentes admite la transacción, fortaleciendo así su nivel de privacidad.
Para una transacción coinjoin 8x8 que presenta `9,934,563` interpretaciones, la entropía sería:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```

Tomemos otro ejemplo con una transacción más convencional, con una entrada y dos salidas: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) En el caso de esta transacción, la única interpretación posible es: `(In.0) > (Out.0 ; Out.1)`. En consecuencia, su entropía se establece en `0`:
```plaintext
C = 1
E = log2(1)
E = 0 bits
```

### Eficiencia:
El tercer indicador proporcionado por el Calculador Boltzmann se denomina `Eficiencia de la Cartera`. Este indicador evalúa la eficiencia de la transacción comparándola con la transacción óptima concebible en una configuración idéntica.
Esto nos lleva a discutir el concepto de entropía máxima, que corresponde a la mayor entropía que una estructura de transacción específica podría teóricamente alcanzar. La eficiencia de la transacción se calcula entonces confrontando esta entropía máxima con la entropía real de la transacción analizada.
La fórmula utilizada es la siguiente:
```plaintext
ER: la entropía real de la transacción expresada en bits
EM: la entropía máxima posible para una estructura de transacción dada expresada en bits
Ef: la eficiencia de la transacción en bits

Ef = ER - EM
```

Por ejemplo, para una estructura de coinjoin tipo Whirlpool 5x5, la entropía máxima se establece en `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```

Este indicador también se expresa como un porcentaje, su fórmula es entonces:
```plaintext
CR: el número real de combinaciones posibles
CM: el número máximo de combinaciones posibles con la misma estructura
Ef: la eficiencia expresada como un porcentaje

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Una eficiencia del `100%` indica así que la transacción maximiza su potencial de privacidad según su estructura.

### Densidad de Entropía:
El cuarto indicador es la densidad de entropía, anotada en la herramienta como `Densidad de Entropía`. Proporciona una perspectiva sobre la entropía relativa a cada entrada o salida de la transacción. Este indicador resulta útil para evaluar y comparar la eficiencia de transacciones de diferentes tamaños. Para calcularlo, simplemente se divide la entropía total de la transacción por el número total de entradas y salidas involucradas:
```plaintext
ED: la densidad de entropía expresada en bits
E: la entropía de la transacción expresada en bits
T: el número total de entradas y salidas en la transacción

ED = E / T
```

Tomemos el ejemplo de un coinjoin Whirlpool 5x5:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```

Calculemos también la densidad de entropía para un coinjoin Whirlpool 8x8:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Puntuación Boltzmann:
La quinta pieza de información entregada por el Calculador Boltzmann es la tabla de probabilidades de coincidencia entre las entradas y salidas. Esta tabla indica, a través de la puntuación Boltzmann, la probabilidad condicional de que una entrada específica esté relacionada con una salida dada.

Por lo tanto, es una medida cuantitativa de la probabilidad condicional de que una asociación entre una entrada y una salida en una transacción ocurra, basada en la relación del número de ocurrencias favorables de este evento al número total de ocurrencias posibles, en un conjunto de interpretaciones.

Tomando el ejemplo de un coinjoin Whirlpool nuevamente, la tabla de probabilidades condicionales resaltaría las chances de enlace entre cada entrada y salida, proporcionando una medida cuantitativa de la ambigüedad de las asociaciones en la transacción:

| %       | Salida 0 | Salida 1 | Salida 2 | Salida 3 | Salida 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Entrada 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Entrada 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Entrada 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Entrada 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Entrada 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Aquí, podemos ver claramente que cada entrada tiene la misma probabilidad de estar asociada con cualquier salida, lo que mejora la confidencialidad de la transacción.
Calcular el puntaje de Boltzmann implica dividir el número de interpretaciones en las que ocurre un cierto evento por el número total de interpretaciones disponibles. Así, para determinar el puntaje que asocia la entrada N.º 0 con la salida N.º 3 (`512` interpretaciones), se utiliza el siguiente procedimiento:
```plaintext
Interpretaciones (IN.0 > OUT.3) = 512
Interpretaciones Totales = 1496
Puntaje = 512 / 1496 = 34%
```

Tomando el ejemplo de un coinjoin Whirlpool 8x8 (ciclo de aumento), la tabla de Boltzmann se vería así:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Sin embargo, en el caso de una transacción simple con una sola entrada y dos salidas, la situación es diferente:

| %       | Salida 0 | Salida 1 |
|---------|----------|----------|
| Entrada 0 | 100%     | 100%     |


Aquí, se observa que la probabilidad de que cada salida provenga de la entrada N.º 0 es del `100%`. Por lo tanto, una probabilidad menor se traduce en una mayor privacidad al diluir los vínculos directos entre entradas y salidas.

### Enlaces Deterministas:
La sexta pieza de información proporcionada es el número de enlaces deterministas, complementado por la proporción de estos enlaces. Este indicador revela cuántas conexiones entre las entradas y salidas en la transacción analizada son indiscutibles, con una probabilidad del `100%`. La proporción, por otro lado, ofrece una perspectiva sobre el peso de estos enlaces deterministas dentro del conjunto total de enlaces de transacción.
Por ejemplo, una transacción de tipo coinjoin de Whirlpool no tiene enlaces deterministas, y por lo tanto muestra un indicador y una proporción del `0%`. Por el contrario, en nuestra segunda transacción simple examinada (con una entrada y dos salidas), el indicador se establece en `2` y la proporción alcanza el `100%`. Así, un indicador nulo señala una excelente confidencialidad debido a la ausencia de enlaces directos e indiscutibles entre entradas y salidas.

**Recursos Externos:**

- Código Boltzmann en Samourai
- [Transacciones de Bitcoin y Privacidad (Parte I) por Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Transacciones de Bitcoin y Privacidad (Parte II) por Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Transacciones de Bitcoin y Privacidad (Parte III) por Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Sitio Web de KYCP
- [Artículo en Medium sobre una Introducción al Script de Boltzmann por Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)