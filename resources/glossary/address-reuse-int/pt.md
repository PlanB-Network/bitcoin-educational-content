---
term: REUTILIZAÇÃO DE ENDEREÇOS (INT)

---
Diz-se que a reutilização de endereços é "interna" quando ocorre dentro da mesma transação, tanto como entrada como como saída. Nesta configuração, a reutilização interna de endereços é uma heurística de análise da cadeia de blocos que permite uma hipótese plausível sobre a alteração da transação. Com efeito, se existirem dois outputs e um deles utilizar o mesmo endereço de receção que o input, é provável que o segundo output esteja a sair da posse do utilizador inicial. A saída com o endereço reutilizado provavelmente representa a mudança.

![](../../dictionnaire/assets/10.webp)