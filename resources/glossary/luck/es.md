---
term: LUCK

---
Indicador utilizado en los pools de minería para medir el rendimiento de un pool en relación con sus expectativas teóricas. Como su nombre indica, evalúa la suerte del pool a la hora de encontrar un bloque. La suerte se calcula comparando el número de acciones teóricamente necesarias para encontrar un bloque válido, basado en la dificultad actual de Bitcoin, con el número real de acciones producidas para encontrar ese bloque. Un número de acciones inferior al esperado indica buena suerte, mientras que un número superior indica mala suerte.

Al correlacionar la dificultad en Bitcoin con el número de acciones producidas cada segundo y la dificultad de cada acción, el pool puede calcular el número de acciones que son teóricamente necesarias para encontrar un bloque válido. Por ejemplo, supongamos que teóricamente se necesitan 100.000 acciones para que un pool encuentre un bloque. Si la peña produce realmente 200.000 antes de encontrar un bloque, su suerte es del 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Por el contrario, si este pool encontró un bloque válido después de producir sólo 50.000 acciones, entonces su suerte es del 200%:

```text
100,000 / 50,000 = 2 = 200%
```

La suerte es un indicador que sólo puede actualizarse después de que el pool descubra un bloque, por lo que es un indicador estático que se actualiza periódicamente.