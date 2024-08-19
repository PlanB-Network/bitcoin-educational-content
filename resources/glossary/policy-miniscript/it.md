---
termine: POLICY (MINISCRIPT)
---

Un linguaggio di alto livello, orientato all'utente, che consente la specifica semplice delle condizioni sotto le quali un UTXO può essere sbloccato all'interno del framework di Miniscript. La policy è una descrizione astratta delle regole di spesa. Può poi essere compilata in miniscript, che è equivalente uno a uno con le operazioni del linguaggio script nativo di Bitcoin.

![](../../dictionnaire/assets/30.png)

Il linguaggio delle policy è leggermente diverso dal linguaggio miniscript. Per esempio, immagina un sistema di sicurezza con un percorso primario che sia la chiave A, e un percorso di recupero che sia la chiave B, ma sotto un timelock di un anno (circa 52.560 blocchi). In policy, questo sarebbe:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Una volta compilato in miniscript, sarebbe:

```plaintext
andor(pk(B),older(52560),pk(A))
```

E una volta convertito in script nativo, sarebbe:

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