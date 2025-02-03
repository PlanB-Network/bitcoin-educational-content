---
term: SECP256R1

---
Nombre dado a una curva elíptica definida por la norma NIST para la criptografía de clave pública. Utiliza un campo primo de 256 bits y una ecuación de curva elíptica $y^2 = x^3 + ax + b$ con las constantes:

```text
a = -3
```

y

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

La curva `secp256r1` se utiliza ampliamente en muchos protocolos, pero no en Bitcoin. De hecho, Satoshi Nakamoto optó por la curva `secp256k1`, que entonces era poco conocida en 2009. Se desconoce la razón exacta de esta elección, pero puede que fuera para minimizar el riesgo de puertas traseras. En efecto, los parámetros de la curva $k1$ son mucho más sencillos que los de la curva $r1$, especialmente la constante $b$.

> ► *Esta curva a veces también se denomina "P-256"*