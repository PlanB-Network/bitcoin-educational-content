---
term: SIGHASH_ANYPREVOUT

---
Proposta per l'implementazione di un nuovo modificatore del flag SigHash in Bitcoin, introdotto con BIP118. il flag `SIGHASH_ANYPREVOUT` consente una maggiore flessibilità nella gestione delle transazioni, in particolare per applicazioni avanzate come i canali di pagamento sulla Lightning Network e l'aggiornamento di Eltoo. La funzione `SIGHASH_ANYPREVOUT` consente alla firma di non essere legata a uno specifico UTXO precedente (*Any Previous Output*). Usato in combinazione con `SIGHASH_ALL`, permetterebbe di firmare tutti gli output di una transazione, ma nessuno degli input. Ciò consentirebbe di riutilizzare la firma per transazioni diverse, purché siano soddisfatte alcune condizioni specifiche.

> ► *Questo modificatore SigHash SIGHASH_ANYPREVOUT è derivato dall'idea di SIGHASH_NOINPUT inizialmente proposta da Joseph Poon nel 2016 per migliorare il suo concetto di Lightning Network.*