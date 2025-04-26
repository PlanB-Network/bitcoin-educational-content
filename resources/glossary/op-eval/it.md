---
term: OP_EVAL

---
Opcode proposto da Gavin Andresen nel 2011. Prende lo script che si trova in cima allo stack, lo esegue come se fosse parte della `scriptPubKey` e mette il risultato sullo stack. `OP_EVAL` è stato abbandonato a causa delle preoccupazioni legate alla complessità di questo opcode, che alla fine sarebbe stato sostituito da P2SH.