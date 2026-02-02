---
term: Blocco Merkle

definition: Struttura che fornisce una prova compatta dell'inclusione di una transazione in un blocco per i client leggeri.
---
Struttura di dati utilizzata nel contesto del BIP37 (*Transaction Bloom Filtering*) per fornire una prova compatta dell'inclusione di transazioni specifiche in un blocco. È utilizzata in particolare per i portafogli SPV. Il blocco Merkle contiene le intestazioni del blocco, le transazioni filtrate e un albero di Merkle parziale, consentendo ai client leggeri di verificare rapidamente se una transazione appartiene a un blocco senza scaricare tutte le transazioni.