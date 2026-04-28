---
term: Txid (identificatore di transazione)

definition: Identificatore univoco di una transazione Bitcoin calcolato tramite l'hash SHA256d dei suoi dati.
---
Un identificatore unico associato a ogni transazione Bitcoin. Viene generato calcolando l'hash `SHA256d` dei dati della transazione. Il TXID serve come riferimento per trovare una transazione specifica all'interno della blockchain. Viene anche usato per riferirsi a un UTXO, che è essenzialmente la concatenazione del TXID di una transazione precedente e dell'indice dell'output designato (chiamato anche "vout"). Per le transazioni successive a SegWit, il TXID non tiene più conto del testimone della transazione, eliminando così la malleabilità.