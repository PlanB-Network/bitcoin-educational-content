---
term: TWEAK (CHAVE PÚBLICA)

---
No domínio da criptografia, "ajustar" uma chave pública implica modificar esta chave utilizando um valor aditivo denominado "tweak", de modo a que continue a ser utilizável com o conhecimento da chave privada original e do tweak. Tecnicamente, um tweak é um valor escalar que é adicionado à chave pública inicial. Se $P$ é a chave pública e $t$ é o tweak, a chave pública tweaked torna-se:

$$
P' = P + tG
$$

Onde $G$ é o gerador da curva elíptica utilizada. Esta operação permite obter uma nova chave pública derivada da chave original, mantendo certas propriedades criptográficas que a tornam utilizável. Por exemplo, este método é utilizado para os endereços Taproot (P2TR) para permitir a despesa através da apresentação de uma assinatura Schnorr da forma tradicional ou através do cumprimento de uma das condições indicadas numa árvore Merkle, também designada "MAST".

![](../../dictionnaire/assets/26.webp)