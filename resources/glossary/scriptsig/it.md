---
termine: SCRIPTSIG
---

Un elemento in una transazione Bitcoin situato negli input. Lo `scriptSig` fornisce i dati necessari per soddisfare le condizioni imposte dallo `scriptPubKey` della transazione precedente da cui i fondi vengono spesi. Gioca quindi un ruolo complementare rispetto allo `scriptPubKey`. Tipicamente, lo `scriptSig` contiene una firma digitale e una chiave pubblica. La firma è generata dal proprietario dei bitcoin utilizzando la loro chiave privata e dimostra che hanno l'autorizzazione a spendere l'UTXO. In questo caso, lo `scriptSig` dimostra che il detentore dell'input possiede la chiave privata corrispondente alla chiave pubblica associata all'indirizzo specificato nello `scriptPubKey` della precedente transazione in uscita.

Quando la transazione viene verificata, i dati dello `scriptSig` vengono eseguiti nello corrispondente `scriptPubKey`. Se il risultato è valido, significa che le condizioni per spendere i fondi sono state soddisfatte. Se tutti gli input della transazione forniscono uno `scriptSig` che valida il loro `scriptPubKey`, la transazione è valida e può essere aggiunta a un blocco per l'esecuzione.

Per esempio, ecco un classico `scriptSig` P2PKH:

```text
<firma> <chiave pubblica>
```

Lo `scriptPubKey` corrispondente sarebbe:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <indirizzo> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *Lo `scriptSig` è talvolta chiamato anche "script di sblocco" in inglese.*