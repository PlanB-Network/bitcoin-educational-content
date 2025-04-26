---
term: SECP256R1

---
Nome dado a uma curva elíptica definida pela norma NIST para criptografia de chave pública. Utiliza um campo primo de 256 bits e uma equação de curva elíptica $y^2 = x^3 + ax + b$ com as constantes:

```text
a = -3
```

e

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

A curva `secp256r1` é amplamente utilizada em muitos protocolos, mas não é utilizada no Bitcoin. De facto, Satoshi Nakamoto optou pela curva `secp256k1`, que era então pouco conhecida em 2009. A razão exacta para esta escolha é desconhecida, mas pode ter sido para minimizar o risco de backdoors. Os parâmetros da curva $k1$ são de facto muito mais simples do que os da curva $r1$, especialmente a constante $b$.

> ► *Esta curva é por vezes também designada por "P-256"