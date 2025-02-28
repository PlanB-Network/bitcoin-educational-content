---
term: ENTROPIA (ANÁLISE)

---
No contexto específico da análise de cadeias, entropia é também o nome de um indicador, derivado da entropia de Shannon, inventado por LaurentMT. Este indicador permite medir a falta de conhecimento que os analistas têm sobre a configuração exacta de uma transação Bitcoin. Por outras palavras, quanto mais elevada for a entropia de uma transação, mais difícil se torna para os analistas identificar os movimentos de bitcoins entre entradas e saídas.

Na prática, a entropia revela se, na perspetiva de um observador externo, uma transação apresenta múltiplas interpretações possíveis, baseadas apenas nas quantidades de entradas e saídas, sem considerar outros padrões e heurísticas externos ou internos. Uma entropia elevada é então sinónimo de melhor confidencialidade para a transação.

A entropia é definida como o logaritmo binário do número de combinações possíveis. Eis a fórmula utilizada com $E$ a representar a entropia da transação e $C$ o número de interpretações possíveis:

$$
E = \log_2(C)
$$

Tendo em conta os valores dos UTXOs envolvidos na transação, o número de interpretações $C$ representa o número de formas em que os inputs podem ser associados aos outputs. Por outras palavras, determina o número de interpretações que uma transação pode suscitar do ponto de vista de um observador externo que a analisa.