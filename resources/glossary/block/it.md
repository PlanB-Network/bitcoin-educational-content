Struttura dati nel sistema Bitcoin. Un blocco contiene un insieme di transazioni valide e metadati contenuti nel suo intestazione. Ogni blocco è collegato al successivo tramite l'hash del suo intestazione, formando così la blockchain. La blockchain funge da server di timestamping che permette a ogni utente di conoscere tutte le transazioni passate, al fine di verificare la non esistenza di una transazione e prevenire il doppio spesa. Le transazioni sono organizzate in un albero di Merkle. Questo accumulatore crittografico permette la produzione di un digest di tutte le transazioni in un blocco, chiamato "radice di Merkle". L'intestazione di un blocco contiene 6 elementi:
* La versione del blocco;
* L'impronta del blocco precedente;
* La radice dell'albero di Merkle delle transazioni;
* Il timestamp del blocco;
* L'obiettivo di difficoltà;
* Il nonce.

Perché un blocco sia valido, deve avere un'intestazione che, una volta hashata con `SHA256d`, produce un digest che è minore o uguale all'obiettivo di difficoltà.