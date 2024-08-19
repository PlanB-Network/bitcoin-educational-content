---
term: DUSTRELAYFEE
---

Una regola di standardizzazione utilizzata dai nodi della rete per determinare quello che considerano il "limite di polvere" (dust limit). Questo parametro stabilisce una tariffa in sats per kilobyte virtuale (sats/kvB) che funge da riferimento per calcolare se il valore di un UTXO è inferiore alle tariffe necessarie per includerlo in una transazione. Infatti, un UTXO è considerato "polvere" su Bitcoin se richiede in tariffe più del valore che rappresenta. Il calcolo di questo limite è il seguente:

```text
limite = (dimensione input + dimensione output) * tariffa
```

Poiché la tariffa richiesta affinché una transazione sia inclusa in un blocco Bitcoin varia costantemente, il parametro `DustRelayFee` permette a ciascun nodo di definire la tariffa utilizzata in questo calcolo. Per impostazione predefinita, su Bitcoin Core, questo valore è fissato a 3.000 sats/kvB. Ad esempio, per calcolare il limite di polvere per un input e output P2PKH, che misurano rispettivamente 148 e 34 byte, il calcolo sarebbe:

```text
limite (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Questo significa che il nodo in questione non trasmetterà transazioni che includono un UTXO protetto da P2PKH il cui valore è inferiore a 546 sats.