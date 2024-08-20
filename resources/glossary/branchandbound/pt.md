---
term: BRANCH-AND-BOUND
---

Método usado para selecionar entradas na carteira Bitcoin Core desde a versão 0.17 e inventado por Murch. Branch-and-Bound (BnB) é uma busca para encontrar um conjunto de UTXOs que corresponda exatamente à quantidade de saídas a serem cumpridas em uma transação, a fim de minimizar o troco e as taxas associadas. Seu objetivo é reduzir um critério de desperdício que leva em conta tanto o custo imediato quanto os custos futuros esperados para o troco. Este método é mais preciso em termos de taxas comparado a heurísticas anteriores como o *Knapsack Solver*. O *Branch-and-Bound* é inspirado no método de resolução de problemas de mesmo nome, inventado em 1960 por Ailsa Land e Alison Harcourt.

> ► *Este método também é às vezes chamado de "Algoritmo de Murch" em referência ao seu inventor.*