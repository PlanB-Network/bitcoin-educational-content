---
term: OUTPOINT

---
Jedinečný odkaz na výstup nevyčerpané transakce (UTXO). Skládá se ze dvou prvků:


- `txid`: identifikátor transakce, která vytvořila výstup;
- `vout`: index výstupu v transakci.

Kombinace těchto dvou prvků přesně identifikuje UTXO. Pokud má například transakce `txid` `abc...123` a výstupní index je `0`, bude výstupní bod zaznamenán jako:

```text
abc...123:0
```

Outpoint se používá ve vstupech (`vin`) nové transakce k označení, které UTXO se vynakládá.

> ► *Termín "outpoint" se často používá jako synonymum pro "UTXO".*