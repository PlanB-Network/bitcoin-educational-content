---
term: BANDIERA SIGHASH

---
Un parametro di una transazione Bitcoin che determina quali componenti di una transazione (ingressi e uscite) sono coperti dalla firma associata, diventando così immutabili. Il flag SigHash è un byte aggiunto alla firma digitale di ciascun ingresso. Pertanto, la scelta del flag SigHash influisce direttamente su quali parti della transazione sono congelate dalla firma e quali possono essere modificate in seguito. Questo meccanismo garantisce che le firme impegnino in modo preciso e sicuro i dati della transazione secondo l'intenzione del firmatario. Esistono tre flag SigHash principali:


- `SIGHASH_ALL` (`0x01`): La firma si applica a tutti gli ingressi e le uscite della transazione, bloccandoli completamente;
- `SIGHASH_NONE` (`0x02`): La firma si applica a tutti gli ingressi ma a nessuna delle uscite, consentendo di modificare le uscite dopo la firma;
- `SIGHASH_SINGLE` (`0x03`): La firma copre tutti gli ingressi e solo un'uscita corrispondente all'indice dell'ingresso firmato.

Oltre a questi tre flag SigHash, il modificatore `SIGHASH_ANYONECANPAY` (`0x80`) può essere combinato con ciascuno dei tipi precedenti. Quando si utilizza questo modificatore, solo una parte degli ingressi viene firmata, lasciando gli altri aperti alla modifica. Ecco le combinazioni esistenti con il modificatore:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): La firma si applica a un singolo ingresso e copre tutte le uscite della transazione;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): La firma copre un singolo ingresso, senza impegnarsi in alcun output;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): La firma si applica a un singolo ingresso e solo all'uscita che ha lo stesso indice di questo ingresso.

> *Un sinonimo talvolta usato per "SigHash" è "Signature Hash Types"