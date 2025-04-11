---
term: AVG. DURACIÓN DE LA RONDA

---
La duración media de las rondas es un indicador utilizado para estimar el tiempo que tarda un pool de minería en encontrar un bloque, basándose en la dificultad de la red y el hashrate del pool. Se calcula tomando el número de acciones esperadas para encontrar un bloque y dividiéndolo por el hashrate del pool. Por ejemplo, si un pool de minería tiene 200 mineros y cada uno genera una media de 4 participaciones por segundo, la potencia de cálculo total del pool es de 800 participaciones por segundo:

```text
200 * 4 = 800
```

Suponiendo que, por término medio, se tarda 1 millón de acciones en encontrar un bloque válido, la *Duración media de la ronda* del pool sería de 1.250 segundos, es decir, unos 21 minutos. Round Duration* sería de 1.250 segundos, unos 21 minutos:

```text
1,000,000 / 800 = 1,250
```

En la práctica, esto significa que, de media, el pool de minería debería encontrar un bloque cada 21 minutos aproximadamente. Este indicador fluctúa con los cambios en el hashrate del pool: un aumento en el hashrate reduce la *Avg. Round Duration*, mientras que una disminución la amplía. También fluctuará con cada ajuste periódico del objetivo de dificultad de Bitcoin (cada 2016 bloques). Esta medida no tiene en cuenta los bloques encontrados por otros pools y se centra únicamente en el rendimiento interno del pool estudiado.