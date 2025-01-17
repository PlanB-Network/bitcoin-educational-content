---
term: SCRIPTSIG

---
Elemento di una transazione Bitcoin situato negli input. Lo `scriptSig` fornisce i dati necessari per soddisfare le condizioni stabilite dallo `scriptPubKey` della transazione precedente da cui vengono spesi i fondi. Svolge quindi un ruolo complementare alla `scriptPubKey`. In genere, lo `scriptSig` contiene una firma digitale e una chiave pubblica. La firma è generata dal proprietario dei bitcoin utilizzando la sua chiave privata e dimostra che ha l'autorizzazione a spendere l'UTXO. In questo caso, la `scriptSig` dimostra che il titolare dell'input possiede la chiave privata corrispondente alla chiave pubblica associata all'indirizzo specificato nella `scriptPubKey` della precedente transazione in uscita.

Quando la transazione viene verificata, i dati dello `scriptSig` vengono eseguiti nel corrispondente `scriptPubKey`. Se il risultato è valido, significa che le condizioni per spendere i fondi sono state soddisfatte. Se tutti gli input della transazione forniscono un `scriptSig` che convalida la loro `scriptPubKey`, la transazione è valida e può essere aggiunta a un blocco per l'esecuzione.

Ad esempio, ecco un classico `scriptSig' di P2PKH:

```text
<signature> <public key>
```

La corrispondente `scriptPubKey` sarebbe:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *Lo `scriptSig` è talvolta chiamato anche "script di sblocco" in inglese