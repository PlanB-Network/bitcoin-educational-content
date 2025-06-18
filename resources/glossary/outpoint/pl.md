---
term: OUTPOINT
---

Unikalne odniesienie do niewydanego wyniku transakcji (UTXO). Składa się z dwóch Elements:


- `txid`: identyfikator transakcji, która utworzyła dane wyjściowe;
- `vout`: indeks wyjścia w transakcji.


Kombinacja tych dwóch Elements dokładnie identyfikuje UTXO. Na przykład, jeśli transakcja ma `txid` `abc...123`, a indeks wyjściowy to `0`, punkt wyjściowy zostanie odnotowany jako:


```text
abc...123:0
```


Outpoint jest używany w danych wejściowych (`vin`) nowej transakcji, aby wskazać, który UTXO jest wydawany.


> termin "outpoint" jest często używany jako synonim "UTXO"