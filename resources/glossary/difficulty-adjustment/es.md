---
term: AJUSTE DE DIFICULTAD
---

El ajuste de dificultad es un proceso periódico que redefine el objetivo de dificultad para el mecanismo de prueba de trabajo (minería) en Bitcoin. Este evento ocurre cada 2016 bloques (aproximadamente cada dos semanas). Sirve para aumentar o disminuir el factor de dificultad (también llamado objetivo de dificultad), dependiendo de la rapidez con la que se encontraron los últimos 2016 bloques. El ajuste tiene como objetivo mantener una tasa de producción de bloques estable y predecible, a una frecuencia de un bloque cada 10 minutos, a pesar de las variaciones en el poder computacional desplegado por los mineros. El cambio en la dificultad durante el ajuste está limitado a un factor de 4. La fórmula ejecutada por los nodos para calcular el nuevo objetivo es la siguiente:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Donde:
* $N$: El nuevo objetivo;
* $A$: El objetivo antiguo de los últimos 2016 bloques;
* $T$: El tiempo total real de los últimos 2016 bloques en segundos;
* $1,209,600$: El tiempo objetivo en segundos para producir 2016 bloques con un intervalo de 10 minutos entre cada uno.

> ► *En francés, el término "reciblage" a veces también se utiliza para referirse al ajuste. En inglés, se le denomina "Difficulty Adjustment".*