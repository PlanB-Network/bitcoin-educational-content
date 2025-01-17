---
term: TASSA DI SPOLVERAMENTO

---
Regola di standardizzazione utilizzata dai nodi della rete per determinare quello che considerano il "limite di polvere" Questo parametro stabilisce una tariffa in sats per kilobyte virtuale (sats/kvB) che serve come riferimento per calcolare se il valore di un UTXO è inferiore alle tariffe necessarie per includerlo in una transazione. Infatti, un UTXO è considerato "polvere" su Bitcoin se richiede più commissioni per essere trasferito rispetto al valore che esso stesso rappresenta. Il calcolo di questo limite è il seguente:

```text
limit = (input size + output size) * fee rate
```

Poiché il tasso di commissione richiesto per l'inclusione di una transazione in un blocco Bitcoin varia costantemente, il parametro `DustRelayFee` consente a ciascun nodo di definire il tasso di commissione utilizzato nel calcolo. Per impostazione predefinita, su Bitcoin Core, questo valore è impostato su 3.000 sats/kvB. Ad esempio, per calcolare il limite di polvere per un ingresso e un'uscita P2PKH, che misurano rispettivamente 148 e 34 byte, il calcolo sarebbe:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Ciò significa che il nodo in questione non trasmetterà le transazioni che includono un UTXO protetto da P2PKH il cui valore è inferiore a 546 sats.