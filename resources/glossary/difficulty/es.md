---
term: DIFICULTAD
---

Un parámetro ajustable que determina la complejidad de la prueba de trabajo requerida para añadir un nuevo bloque a la cadena de bloques y ganar la recompensa asociada. Esta dificultad está representada por el objetivo de dificultad, un valor de 256 bits que establece el límite superior que el hash del encabezado del bloque debe cumplir para ser considerado válido. El objetivo es que el hash, logrado a través de una doble ejecución de SHA256 (SHA256d), sea menor o igual a este objetivo. Para alcanzar este hash, los mineros manipulan el `nonce` en el encabezado del bloque. La dificultad se ajusta cada 2016 bloques, o aproximadamente cada dos semanas, para mantener el tiempo promedio de creación de bloques en unos 10 minutos.