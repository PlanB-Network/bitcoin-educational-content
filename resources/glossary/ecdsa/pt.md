---
term: ECDSA
---

Acrônimo para "Elliptic Curve Digital Signature Algorithm" (Algoritmo de Assinatura Digital de Curva Elíptica). É um algoritmo de assinatura digital baseado na criptografia de curva elíptica (ECC). É uma variante do DSA (Digital Signature Algorithm). O ECDSA utiliza as propriedades das curvas elípticas para fornecer níveis de segurança comparáveis aos dos algoritmos de chave pública tradicionais, como o RSA, enquanto usa tamanhos de chave significativamente menores. O ECDSA permite a geração de pares de chaves (chaves públicas e privadas) bem como a criação e verificação de assinaturas digitais.

No contexto do Bitcoin, o ECDSA é usado para derivar chaves públicas a partir de chaves privadas. Também é usado para assinar transações, a fim de satisfazer um script para desbloquear bitcoins e gastá-los. A curva elíptica usada no ECDSA do Bitcoin é a `secp256k1`, definida pela equação $y^2 = x^3 + 7$. Este algoritmo tem sido usado desde a criação do Bitcoin em 2009. Hoje, ele divide seu lugar com o protocolo Schnorr, outro algoritmo de assinatura digital introduzido com o Taproot em 2021.