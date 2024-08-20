---
term: DURAÇÃO MÉDIA DA RODADA
---

A duração média da rodada é um indicador usado para estimar o tempo necessário para um pool de mineração encontrar um bloco, baseado na dificuldade da rede e no hashrate do pool. É calculado pegando o número de shares esperadas para encontrar um bloco e dividindo-o pelo hashrate do pool. Por exemplo, se um pool de mineração tem 200 mineradores, e cada um gera em média 4 shares por segundo, o poder computacional total do pool é de 800 shares por segundo:

```text
200 * 4 = 800
```

Assumindo que, em média, são necessárias 1 milhão de shares para encontrar um bloco válido, a *Duração Média da Rodada* do pool seria de 1.250 segundos, ou cerca de 21 minutos:

```text
1.000.000 / 800 = 1.250
```

Em termos práticos, isso significa que, em média, o pool de mineração deve encontrar um bloco a cada 21 minutos, aproximadamente. Este indicador flutua com mudanças no hashrate do pool: um aumento no hashrate reduz a *Duração Média da Rodada*, enquanto uma diminuição a prolonga. Ele também flutuará com cada ajuste periódico do alvo de dificuldade do Bitcoin (a cada 2016 blocos). Esta medida não leva em conta blocos encontrados por outros pools e foca exclusivamente no desempenho interno do pool sendo estudado.