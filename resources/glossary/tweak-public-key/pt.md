---
term: TWEAK (CHAVE PÚBLICA)
---

No campo da criptografia, "tweak" (ajustar) uma chave pública envolve modificar essa chave usando um valor aditivo chamado "tweak" para que ela permaneça utilizável com o conhecimento da chave privada original e do tweak. Tecnicamente, um tweak é um valor escalar que é adicionado à chave pública inicial. Se $P$ é a chave pública e $t$ é o tweak, a chave pública ajustada torna-se:

$$
P' = P + tG
$$

Onde $G$ é o gerador da curva elíptica usada. Esta operação permite obter uma nova chave pública derivada da chave original, mantendo certas propriedades criptográficas que a tornam utilizável. Por exemplo, este método é usado para endereços Taproot (P2TR) para permitir gastos tanto apresentando uma assinatura Schnorr da maneira tradicional quanto cumprindo uma das condições declaradas em uma árvore de Merkle, também chamada de "MAST".

![](../../dictionnaire/assets/26.png)