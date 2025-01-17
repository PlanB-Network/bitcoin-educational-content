---
term: ACCIONES

---
En el contexto de los pools de minería, una cuota es un indicador utilizado para cuantificar la contribución de un minero individual dentro del pool. Esta medida sirve de base para calcular la recompensa que el pool redistribuye a cada minero. Cada cuota corresponde a un hash que satisface un objetivo de dificultad inferior al de la red Bitcoin.

Para explicarlo con una analogía, considere un dado de 20 caras. En Bitcoin, supongamos que la prueba de trabajo requiere sacar un número inferior a 3 para validar un bloque (es decir, lograr un resultado de 1 o 2). Ahora, imagine que dentro de un pool de minería, el objetivo de dificultad para una acción se establece en 10. Así, para un minero individual del pool, cada tirada de dados que dé como resultado un número inferior a 10 cuenta como una participación válida. Estas acciones son transmitidas al pool por el minero, con el fin de reclamar su recompensa, incluso si no corresponden a un resultado válido para un bloque en Bitcoin.

Para cada hash calculado, un minero individual de un pool puede encontrarse con tres escenarios diferentes:


- Si el valor hash es mayor o igual que el objetivo de dificultad establecido por el pool para una acción, entonces este hash no sirve. El minero entonces cambia su nonce para intentar un nuevo hash: `hash > acción > bloque`.
- Si el hash es menor que el objetivo de dificultad de la acción, pero mayor o igual que el objetivo de dificultad de Bitcoin, entonces este hash constituye una acción válida que, sin embargo, no es suficiente para validar un bloque. El minero puede enviar este hash a su pool para reclamar la recompensa asociada a la acción: `acción > hash > bloque`.
- Si el hash es inferior al objetivo de dificultad de la red Bitcoin, se considera tanto una acción como un bloque válidos. El minero transmite este hash a su pool, que se apresura a difundirlo en la red Bitcoin. Este hash también se cuenta como una acción válida para el minero: `share > bloc > hash`.

![](../../dictionnaire/assets/32.webp)

Este sistema de acciones se utiliza para estimar el trabajo realizado por cada minero individual dentro de un pool, sin tener que recalcular individualmente todos los hashes generados por un minero, lo que sería completamente ineficiente para el pool.

Los pools de minería ajustan la dificultad de las participaciones para equilibrar la carga de verificación y garantizar que cada minero, ya sea pequeño o grande, envíe participaciones aproximadamente cada pocos segundos. Esto permite calcular con precisión el hashrate de cada minero y distribuir las recompensas según el método de cálculo de compensación elegido (PPS, PPLNS, TIDES...).

> ► *En francés, "shares" puede traducirse por "parte "*