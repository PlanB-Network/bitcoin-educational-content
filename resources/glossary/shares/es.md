---
term: SHARES
---

En el contexto de los grupos de minería, una "share" (participación) es un indicador utilizado para cuantificar la contribución individual de un minero dentro del grupo. Esta medida sirve como base para calcular la recompensa que el grupo redistribuye a cada minero. Cada "share" corresponde a un hash que satisface un objetivo de dificultad menor que el de la red de Bitcoin.

Para explicarlo con una analogía, considera un dado de 20 caras. En Bitcoin, supongamos que la prueba de trabajo requiere lanzar un número menor que 3 para validar un bloque (es decir, lograr un resultado de 1 o 2). Ahora, imagina que dentro de un grupo de minería, el objetivo de dificultad para una "share" se establece en 10. Así, para un minero individual en el grupo, cada lanzamiento de dado que resulte en un número menor que 10 cuenta como una "share" válida. Estas "shares" son luego transmitidas al grupo por el minero, para reclamar su recompensa, incluso si no corresponden a un resultado válido para un bloque en Bitcoin.

Para cada hash calculado, un minero individual en un grupo puede encontrarse con tres escenarios diferentes:
* Si el valor del hash es mayor o igual al objetivo de dificultad establecido por el grupo para una "share", entonces este hash no sirve. El minero cambia su nonce para intentar un nuevo hash: `hash > share > block`.
* Si el hash es menor que el objetivo de dificultad de la "share", pero mayor o igual al objetivo de dificultad de Bitcoin, entonces este hash constituye una "share" válida que, sin embargo, no es suficiente para validar un bloque. El minero puede enviar este hash a su grupo para reclamar la recompensa asociada con la "share": `share > hash > block`.
* Si el hash es menor que el objetivo de dificultad de la red de Bitcoin, se considera tanto una "share" válida como un bloque válido. El minero transmite este hash a su grupo, que se apresura a difundirlo en la red de Bitcoin. Este hash también se cuenta como una "share" válida para el minero: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Este sistema de "shares" se utiliza para estimar el trabajo realizado por cada minero individual dentro de un grupo, sin tener que recalcular individualmente todos los hashes generados por un minero, lo cual sería completamente ineficiente para el grupo.

Los grupos de minería ajustan la dificultad de las "shares" para equilibrar la carga de verificación y asegurar que cada minero, ya sea pequeño o grande, envíe "shares" aproximadamente cada pocos segundos. Esto permite un cálculo preciso del hashrate de cada minero y la distribución de recompensas según el método elegido de cálculo de compensación (PPS, PPLNS, TIDES...).

> ► *En francés, "shares" se puede traducir como "part".*