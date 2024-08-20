---
term: SECP256R1
---

Nombre dado a una curva elíptica definida por el estándar NIST para criptografía de clave pública. Utiliza un campo primo de 256 bits y una ecuación de curva elíptica $y^2 = x^3 + ax + b$ con las constantes:

```text
a = -3
```

y

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

La curva `secp256r1` es ampliamente utilizada en muchos protocolos, pero no se usa en Bitcoin. De hecho, Satoshi Nakamoto optó por la curva `secp256k1`, que era entonces poco conocida en 2009. La razón precisa de esta elección es desconocida, pero podría haber sido para minimizar el riesgo de puertas traseras. Los parámetros de la curva $k1$ son de hecho mucho más simples que los de la curva $r1$, especialmente la constante $b$.

> ► *Esta curva a veces también se denomina "P-256".*