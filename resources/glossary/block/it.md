---
term: BLOCCO

---
Struttura di dati nel sistema Bitcoin. Un blocco contiene un insieme di transazioni valide e di metadati contenuti nella sua intestazione. Ogni blocco è collegato al successivo tramite l'hash della sua intestazione, formando così la blockchain. La blockchain funge da server di cronometraggio che consente a ogni utente di conoscere tutte le transazioni passate, al fine di verificare l'inesistenza di una transazione e prevenire la doppia spesa. Le transazioni sono organizzate in un albero di Merkle. Questo accumulatore crittografico consente di produrre un digest di tutte le transazioni in un blocco, chiamato "radice di Merkle" L'intestazione di un blocco contiene 6 elementi:


- La versione del blocco;
- L'impronta del blocco precedente;
- La radice dell'albero di Merkle delle transazioni;
- Il timestamp del blocco;
- L'obiettivo di difficoltà;
- Il nonce.

Perché un blocco sia valido, deve avere un'intestazione che, una volta sottoposta a hash con `SHA256d`, produca un digest inferiore o uguale all'obiettivo di difficoltà.