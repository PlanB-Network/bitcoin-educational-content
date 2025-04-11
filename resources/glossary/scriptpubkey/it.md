---
term: SCRIPTPUBKEY

---
Uno script situato nella parte di output di una transazione Bitcoin che definisce le condizioni in cui l'UTXO associato può essere speso. Questo script protegge quindi i bitcoin. Nella sua forma più comune, lo `scriptPubKey` contiene una condizione che richiede alla transazione successiva di fornire la prova del possesso della chiave privata corrispondente a un indirizzo Bitcoin specificato. Questo viene spesso ottenuto con uno script che richiede una firma corrispondente alla chiave pubblica associata all'indirizzo utilizzato per garantire i fondi. Quando una transazione tenta di utilizzare questo UTXO come input, deve fornire una `scriptSig` che, una volta combinata con la `scriptPubKey`, soddisfi le condizioni impostate e produca uno script valido.

Ad esempio, ecco un classico `scriptPubKey` di P2PKH:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Il corrispondente `scriptSig` sarebbe:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> *Questo script viene talvolta chiamato anche "script di blocco" in inglese