---
term: AVG. ROUND DURATION
---

La duración promedio de una ronda es un indicador utilizado para estimar el tiempo que tarda un grupo de minería en encontrar un bloque, basado en la dificultad de la red y el hashrate del grupo. Se calcula tomando el número de participaciones esperadas para encontrar un bloque y dividiéndolo por el hashrate del grupo. Por ejemplo, si un grupo de minería tiene 200 mineros, y cada uno genera un promedio de 4 participaciones por segundo, el poder computacional total del grupo es de 800 participaciones por segundo:

```text
200 * 4 = 800
```

Asumiendo que, en promedio, se necesitan 1 millón de participaciones para encontrar un bloque válido, la *Duración Promedio de una Ronda* del grupo sería de 1,250 segundos, o aproximadamente 21 minutos:

```text
1,000,000 / 800 = 1,250
```

En términos prácticos, esto significa que, en promedio, el grupo de minería debería encontrar un bloque cada 21 minutos aproximadamente. Este indicador fluctúa con cambios en el hashrate del grupo: un aumento en el hashrate reduce la *Duración Promedio de una Ronda*, mientras que una disminución la extiende. También fluctuará con cada ajuste periódico del objetivo de dificultad de Bitcoin (cada 2016 bloques). Esta medida no toma en cuenta los bloques encontrados por otros grupos y se centra únicamente en el rendimiento interno del grupo que se está estudiando.