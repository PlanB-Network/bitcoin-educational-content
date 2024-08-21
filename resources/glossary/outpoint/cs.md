---
term: OUTPOINT
---

Unikátní odkaz na nevyužitý výstup transakce (UTXO). Skládá se ze dvou prvků:
* `txid`: identifikátor transakce, která vytvořila výstup;
* `vout`: index výstupu v transakci.

Kombinace těchto dvou prvků přesně identifikuje UTXO. Například, pokud má transakce `txid` `abc...123` a index výstupu je `0`, outpoint bude označen jako:

```text
abc...123:0
```

Outpoint je použit ve vstupech (`vin`) nové transakce k označení, které UTXO je využíváno.

> ► *Termín "outpoint" je často používán synonymně s "UTXO."*