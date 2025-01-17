---
term: POLICY (MINISCRIPT)
---

A high-level, user-oriented language that allows for the simple specification of conditions under which a UTXO can be unlocked within the framework of Miniscript. The policy is an abstract description of the spending rules. It can then be compiled into miniscript, which is a one-to-one equivalent with operations from Bitcoin's native script language.

![](../../dictionnaire/assets/30.webp)

The policy language is slightly different from the miniscript language. For example, imagine a security system with a primary path being key A, and a recovery path being key B, but under a timelock of one year (approximately 52,560 blocks). In policy, this would be:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Once compiled into miniscript, it would be:

```plaintext
andor(pk(B),older(52560),pk(A))
```

And once converted into native script, it would be:

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

