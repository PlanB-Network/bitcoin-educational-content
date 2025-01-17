---
term: DIFICULTAD

---
Parámetro ajustable que determina la complejidad de la prueba de trabajo necesaria para añadir un nuevo bloque a la cadena de bloques y obtener la recompensa asociada. Esta dificultad está representada por el objetivo de dificultad, un valor de 256 bits que establece el límite superior que debe cumplir el hash de la cabecera del bloque para considerarse válido. El objetivo es que el hash, obtenido mediante una doble ejecución de SHA256 (SHA256d), sea inferior o igual a este objetivo. Para alcanzar este hash, los mineros manipulan el `nonce` de la cabecera del bloque. La dificultad se ajusta cada 2016 bloques, o aproximadamente cada dos semanas, para mantener el tiempo medio de creación de bloques en unos 10 minutos.