---
term: LUCK
---

Um indicador usado em pools de mineração para medir o desempenho de uma pool em relação às suas expectativas teóricas. Como o nome sugere, avalia a sorte da pool em encontrar um bloco. A sorte é calculada comparando o número de participações teoricamente necessárias para encontrar um bloco válido, com base na dificuldade atual do Bitcoin, ao número real de participações produzidas para encontrar esse bloco. Um número de participações menor que o esperado indica boa sorte, enquanto um número maior indica má sorte.

Correlacionando a dificuldade no Bitcoin com o número de suas participações produzidas por segundo e a dificuldade de cada participação, a pool pode calcular o número de participações que são teoricamente necessárias para encontrar um bloco válido. Por exemplo, suponha teoricamente, que sejam necessárias 100.000 participações para uma pool encontrar um bloco. Se a pool realmente produzir 200.000 antes de encontrar um bloco, sua sorte é de 50%:

```text
100.000 / 200.000 = 0,5 = 50%
```

Por outro lado, se essa pool encontrar um bloco válido após produzir apenas 50.000 participações, então sua sorte é de 200%:

```text
100.000 / 50.000 = 2 = 200%
```

A sorte é um indicador que só pode ser atualizado após um bloco ser descoberto pela pool, tornando-se um indicador estático que é atualizado periodicamente.