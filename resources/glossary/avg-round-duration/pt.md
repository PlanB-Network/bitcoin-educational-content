---
term: MÉD. DURAÇÃO DA VOLTA

---
A duração média da ronda é um indicador utilizado para estimar o tempo que demora um grupo de mineração a encontrar um bloco, com base na dificuldade da rede e na taxa de hash do grupo. É calculado tomando o número de acções esperadas para encontrar um bloco e dividindo-o pelo hashrate do grupo. Por exemplo, se um grupo de mineração tiver 200 mineiros, e cada um gerar uma média de 4 acções por segundo, o poder computacional total do grupo é de 800 acções por segundo:

```text
200 * 4 = 800
```

Assumindo que, em média, são necessários 1 milhão de acções para encontrar um bloco válido, a *Duração média da ronda* da pool seria de 1250 segundos ou cerca de 21 minutos. Round Duration* do pool seria de 1.250 segundos, ou cerca de 21 minutos:

```text
1,000,000 / 800 = 1,250
```

Em termos práticos, isso significa que, em média, o pool de mineração deve encontrar um bloco a cada 21 minutos, aproximadamente. Este indicador flutua com as mudanças no hashrate do pool: um aumento no hashrate reduz a *Avg. Round Duration*, enquanto uma diminuição o prolonga. Também flutuará com cada ajuste periódico do objetivo de dificuldade do Bitcoin (a cada 2016 blocos). Esta medida não tem em conta os blocos encontrados por outros pools e centra-se apenas no desempenho interno do pool em estudo.