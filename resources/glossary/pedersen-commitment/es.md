---
term: Pedersen commitment
---

Una Pedersen commitment es un tipo de Commitment criptográfica con la propiedad de ser homomórfica a la operación de suma. Esto significa que es posible validar la suma de dos compromisos sin revelar los valores individuales.


Formalmente, si :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


entonces :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Esta propiedad resulta útil, por ejemplo, para ocultar las cantidades de tokens intercambiados en sistemas de criptomoneda, como RGB, sin dejar de poder verificar los totales.