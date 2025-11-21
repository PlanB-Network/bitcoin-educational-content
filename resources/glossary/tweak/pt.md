---
term: TWEAK
---

Em criptografia, "ajustar" uma chave pública é modificá-la utilizando um valor aditivo chamado "tweak", de modo a que continue a ser utilizável com o conhecimento da chave privada original e do tweak. Tecnicamente, um tweak é um valor escalar que é adicionado à chave pública original. Se $P$ é a chave pública e $t$ é o tweak, a chave pública tweaked torna-se :


$$
P' = P + tG
$$


Onde $G$ é o gerador da curva elíptica utilizada. Esta operação produz uma nova chave pública derivada da original, mantendo certas propriedades criptográficas que permitem a sua utilização. Por exemplo, este método é utilizado para os endereços Taproot (P2TR), para permitir a despesa quer através da apresentação de uma assinatura Schnorr da forma tradicional, quer através do cumprimento de uma das condições estabelecidas num Merkle Tree, também conhecido como "MAST".