---
term: POLITICA (MINISCRITTO)

---
Un linguaggio di alto livello, orientato all'utente, che consente di specificare in modo semplice le condizioni in cui un UTXO può essere sbloccato nell'ambito di Miniscript. La politica è una descrizione astratta delle regole di spesa. Può quindi essere compilata in miniscript, che è un equivalente uno a uno con le operazioni del linguaggio di script nativo di Bitcoin.

![](../../dictionnaire/assets/30.webp)

Il linguaggio dei criteri è leggermente diverso da quello dei miniscript. Ad esempio, immaginiamo un sistema di sicurezza con un percorso primario che sia la chiave A e un percorso di recupero che sia la chiave B, ma con un blocco temporale di un anno (circa 52.560 blocchi). In termini di politica, questo sarebbe:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Una volta compilato in miniscript, sarebbe:

```plaintext
andor(pk(B),older(52560),pk(A))
```

E una volta convertito in scrittura nativa, lo sarebbe:

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