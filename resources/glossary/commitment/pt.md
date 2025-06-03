---
term: Commitment
---

Um Commitment (no sentido criptográfico) é um objeto matemático, denotado $C$, derivado deterministicamente de uma operação sobre dados estruturados $m$ (a mensagem) e um valor aleatório $r$. Escrevemos :


$$
C = \text{commit}(m, r)
$$


Este mecanismo compreende duas operações principais:




- Compromisso: aplicamos uma função criptográfica a uma mensagem $m$ e a um valor aleatório $r$ para produzir $C$ ;
- Verificar: utilizamos $C$, a mensagem $m$ e o valor $r$ para verificar se este Commitment está correto. A função retorna `True` ou `False`.


Um Commitment deve respeitar duas propriedades:




- Vinculação: deve ser impossível encontrar duas mensagens diferentes que produzam o mesmo $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Tais como :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Ocultação: o conhecimento de $C$ não deve revelar o conteúdo de $m$.


No caso do protocolo RGB, um Commitment é incluído numa transação Bitcoin para provar a existência de uma determinada informação num dado momento, sem revelar a própria informação.