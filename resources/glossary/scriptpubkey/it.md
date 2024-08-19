---
term: SCRIPTPUBKEY
---

Uno script situato nella parte di output di una transazione Bitcoin che definisce le condizioni secondo le quali l'UTXO associato può essere speso. Questo script, quindi, protegge i bitcoin. Nella sua forma più comune, lo `scriptPubKey` contiene una condizione che richiede alla prossima transazione di fornire prova del possesso della chiave privata corrispondente a un determinato indirizzo Bitcoin. Questo è spesso ottenuto tramite uno script che richiede una firma corrispondente alla chiave pubblica associata all'indirizzo usato per proteggere questi fondi. Quando una transazione tenta di utilizzare questo UTXO come input, deve fornire uno `scriptSig` che, una volta combinato con lo `scriptPubKey`, soddisfa le condizioni stabilite e produce uno script valido.

Per esempio, ecco un classico `scriptPubKey` P2PKH:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <indirizzo> OP_EQUALVERIFY OP_CHECKSIG
```

Lo `scriptSig` corrispondente sarebbe:

```text
<firma> <chiave pubblica>
```

![](../../dictionnaire/assets/35.png)

> ► *Questo script è talvolta chiamato anche "locking script" in inglese.*