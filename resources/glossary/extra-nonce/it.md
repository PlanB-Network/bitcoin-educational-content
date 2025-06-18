---
term: EXTRA-Nonce
---

Campo usato nello `scriptSig` del Coinbase Transaction di un blocco, che permette di testare un maggior numero di possibilità per avere un Hash inferiore all'obiettivo di difficoltà, oltre al classico Nonce, che si trova direttamente nell'intestazione di ogni blocco.


La modifica dell'extra-Nonce nel Coinbase Transaction cambia l'identificatore di questa transazione, e quindi il Merkle Root di tutte le transazioni del blocco, modificando anche l'intestazione del blocco. Ciò consente al Miner di continuare a cercare gli hash quando l'intervallo del Nonce classico è già esaurito, senza modificare la struttura del blocco candidato.


Nei pool Mining, l'extra-Nonce è spesso diviso in due parti: una generata dal pool per identificare ogni chopper, e un'altra modificata dal chopper alla ricerca di una quota valida. Ciò consente ai diversi chopper del pool di lavorare contemporaneamente sullo stesso blocco candidato con l'intera gamma di nonces, senza duplicare il lavoro a livello di pool.