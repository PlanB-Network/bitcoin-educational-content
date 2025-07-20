---
term: Pedersen commitment
---

Um Pedersen commitment é um tipo de Commitment criptográfico com a propriedade de ser homomórfico à operação de adição. Isto significa que é possível validar a soma de dois compromissos sem revelar os valores individuais.


Formalmente, se :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


depois :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Esta propriedade torna-se útil, por exemplo, para ocultar as quantidades de fichas trocadas em sistemas de criptomoeda, como o RGB, sem deixar de ser possível verificar os totais.