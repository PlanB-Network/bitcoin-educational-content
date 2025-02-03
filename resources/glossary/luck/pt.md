---
term: SORTE

---
Um indicador utilizado em pools de mineração para medir o desempenho de um pool em relação às suas expectativas teóricas. Como o seu nome sugere, avalia a sorte do grupo em encontrar um bloco. A sorte é calculada comparando o número de acções teoricamente necessárias para encontrar um bloco válido, com base na dificuldade atual da Bitcoin, com o número real de acções produzidas para encontrar esse bloco. Um número de acções inferior ao esperado indica boa sorte, enquanto um número superior indica má sorte.

Ao correlacionar a dificuldade da Bitcoin com o seu número de acções produzidas a cada segundo e a dificuldade de cada ação, a pool pode calcular o número de acções que são teoricamente necessárias para encontrar um bloco válido. Por exemplo, suponhamos que, teoricamente, são necessárias 100.000 acções para que um grupo encontre um bloco. Se a pool produzir efetivamente 200.000 antes de encontrar um bloco, a sua sorte é de 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Por outro lado, se este grupo encontrou um bloco válido depois de produzir apenas 50.000 acções, então a sua sorte é de 200%:

```text
100,000 / 50,000 = 2 = 200%
```

O Luck é um indicador que só pode ser atualizado depois de um bloco ser descoberto pela pool, o que faz dele um indicador estático que é atualizado periodicamente.