---
term: POLÍTICA (MINISCRIPT)

---
Uma linguagem de alto nível, orientada para o utilizador, que permite a especificação simples das condições em que um UTXO pode ser desbloqueado no âmbito do Miniscript. A política é uma descrição abstrata das regras de despesa. Pode então ser compilada em miniscript, que é um equivalente de um para um com operações da linguagem de script nativa do Bitcoin.

![](../../dictionnaire/assets/30.webp)

A linguagem de política é ligeiramente diferente da linguagem de miniscript. Por exemplo, imagine um sistema de segurança com um caminho primário sendo a chave A, e um caminho de recuperação sendo a chave B, mas com um bloqueio de tempo de um ano (aproximadamente 52.560 blocos). Em termos de política, isto seria:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Uma vez compilado em miniscript, seria:

```plaintext
andor(pk(B),older(52560),pk(A))
```

E, uma vez convertido em script nativo, seria:

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