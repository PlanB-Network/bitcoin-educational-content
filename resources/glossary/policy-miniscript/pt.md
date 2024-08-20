---
termo: POLICY (MINISCRIPT)
---

Uma linguagem de alto nível, orientada para o usuário, que permite a especificação simples de condições sob as quais um UTXO pode ser desbloqueado dentro do framework do Miniscript. A policy é uma descrição abstrata das regras de gasto. Ela pode então ser compilada em miniscript, que é um equivalente um-para-um com operações da linguagem de script nativa do Bitcoin.

![](../../dictionnaire/assets/30.png)

A linguagem de policy é ligeiramente diferente da linguagem de miniscript. Por exemplo, imagine um sistema de segurança com um caminho primário sendo a chave A, e um caminho de recuperação sendo a chave B, mas sob um timelock de um ano (aproximadamente 52.560 blocos). Em policy, isso seria:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Uma vez compilado em miniscript, seria:

```plaintext
andor(pk(B),older(52560),pk(A))
```

E uma vez convertido em script nativo, seria:

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```