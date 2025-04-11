---
term: RAMIFICAÇÃO E VINCULAÇÃO

---
Método utilizado para selecionar entradas na carteira Bitcoin Core desde a versão 0.17 e inventado por Murch. Branch-and-Bound (BnB) é uma pesquisa para encontrar um conjunto de UTXOs que corresponda à quantidade exacta de outputs a serem preenchidos numa transação, de forma a minimizar o troco e as taxas associadas. O seu objetivo é reduzir um critério de desperdício que tem em conta tanto o custo imediato como os custos futuros previstos para a mudança. Este método é mais preciso em termos de taxas em comparação com heurísticas anteriores como o *Knapsack Solver*. O *Branch-and-Bound* é inspirado no método de resolução de problemas com o mesmo nome, inventado em 1960 por Ailsa Land e Alison Harcourt.

> ► *Este método também é por vezes designado por "Algoritmo de Murch", em referência ao seu inventor