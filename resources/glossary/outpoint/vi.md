---
term: OUTPOINT

---
A unique reference to an unspent transaction output (UTXO). It consists of two elements:


- `txid`: the identifier of the transaction that created the output;
- `vout`: the index of the output in the transaction.

The combination of these two elements precisely identifies a UTXO. For example, if a transaction has a `txid` of `abc...123` and the output index is `0`, the outpoint will be noted as:

```text
abc...123:0
```

The outpoint is used in the inputs (`vin`) of a new transaction to indicate which UTXO is being spent.

> ► *The term "outpoint" is often used synonymously with "UTXO."*