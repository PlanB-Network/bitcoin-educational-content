---
term: ECDSA

---
Acrónimo de "Elliptic Curve Digital Signature Algorithm" (Algoritmo de assinatura digital de curva elíptica) É um algoritmo de assinatura digital baseado na criptografia de curva elíptica (ECC). É uma variante do DSA (Digital Signature Algorithm - algoritmo de assinatura digital). O ECDSA utiliza as propriedades das curvas elípticas para fornecer níveis de segurança comparáveis aos dos algoritmos de chave pública tradicionais, como o RSA, embora utilizando tamanhos de chave significativamente mais pequenos. O ECDSA permite a geração de pares de chaves (chaves públicas e privadas), bem como a criação e verificação de assinaturas digitais.

No contexto da Bitcoin, o ECDSA é utilizado para derivar chaves públicas de chaves privadas. Também é utilizado para assinar transacções, de modo a satisfazer um script para desbloquear bitcoins e gastá-los. A curva elíptica usada no ECDSA do Bitcoin é a `secp256k1`, definida pela equação $y^2 = x^3 + 7$. Este algoritmo tem sido usado desde o início do Bitcoin em 2009. Atualmente, partilha o seu lugar com o protocolo Schnorr, outro algoritmo de assinatura digital introduzido com o Taproot em 2021.