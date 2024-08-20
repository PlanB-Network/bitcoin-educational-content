---
term: KNAPSACK SOLVER
---

Um método antigo utilizado para selecionar moedas na carteira Bitcoin Core antes da versão 0.17. O Knapsack Solver tenta resolver o problema de seleção de moedas iterativamente e de forma aleatória, escolhendo UTXOs e somando-os por subconjuntos, com o objetivo de minimizar as taxas e o tamanho da transação. Este método foi substituído pelo *Branch-and-Bound*.