---
term: SIGHASH_ALL

definition: SigHash Flag che indica che la firma copre tutti gli input e gli output della transazione.
---
Tipo di flag SigHash utilizzato nelle firme delle transazioni Bitcoin per indicare che la firma si applica a tutti i componenti della transazione. Utilizzando `SIGHASH_ALL`, il firmatario copre tutti gli input e tutti gli output. Ciò significa che né gli input né gli output possono essere modificati dopo la firma senza invalidarla. Questo tipo di flag SigHash è il più comune nelle transazioni Bitcoin, in quanto garantisce la completa finalità e integrità della transazione.