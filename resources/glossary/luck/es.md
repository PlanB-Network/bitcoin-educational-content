---
term: LUCK
---

Un indicador utilizado en los grupos de minería para medir el rendimiento de un grupo en relación con sus expectativas teóricas. Como su nombre sugiere, evalúa la suerte del grupo en encontrar un bloque. La suerte se calcula comparando el número de participaciones teóricamente necesarias para encontrar un bloque válido, basado en la dificultad actual de Bitcoin, con el número real de participaciones producidas para encontrar ese bloque. Un número de participaciones menor al esperado indica buena suerte, mientras que un número mayor indica mala suerte.

Al correlacionar la dificultad en Bitcoin con su número de participaciones producidas cada segundo y la dificultad de cada participación, el grupo puede calcular el número de participaciones que teóricamente son necesarias para encontrar un bloque válido. Por ejemplo, supongamos teóricamente, se necesitan 100,000 participaciones para que un grupo encuentre un bloque. Si el grupo realmente produce 200,000 antes de encontrar un bloque, su suerte es del 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Por el contrario, si este grupo encontrara un bloque válido después de producir solo 50,000 participaciones, entonces su suerte es del 200%:

```text
100,000 / 50,000 = 2 = 200%
```

La suerte es un indicador que solo puede actualizarse después de que un bloque es descubierto por el grupo, lo que lo convierte en un indicador estático que se actualiza periódicamente.