---
term: Commitment
---

Un Commitment (en el sentido criptográfico) es un objeto matemático, denotado $C$, derivado determinísticamente de una operación sobre datos estructurados $m$ (el mensaje) y un valor aleatorio $r$. Escribimos :


$$
C = \text{commit}(m, r)
$$


Este mecanismo comprende dos operaciones principales:




- Compromiso: aplicamos una función criptográfica a un mensaje $m$ y a un valor aleatorio $r$ para producir $C$ ;
- Verificar: utilizamos $C$, el mensaje $m$ y el valor $r$ para comprobar que este Commitment es correcto. La función devuelve `Verdadero` o `Falso`.


Una Commitment debe respetar dos propiedades:




- Vinculación: debe ser imposible encontrar dos mensajes diferentes que produzcan el mismo $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Tales como :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Ocultación: el conocimiento de $C$ no debe revelar el contenido de $m$.


En el caso del protocolo RGB, se incluye una Commitment en una transacción Bitcoin para demostrar la existencia de una determinada información en un momento dado, sin revelar la información en sí.