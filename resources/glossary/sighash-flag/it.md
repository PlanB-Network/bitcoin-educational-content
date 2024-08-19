---
term: SIGHASH FLAG
---

Un parametro in una transazione Bitcoin che determina quali componenti di una transazione (input e output) sono coperti dalla firma associata, diventando così immutabili. Il SigHash Flag è un byte aggiunto alla firma digitale di ogni input. Pertanto, la scelta del SigHash Flag influisce direttamente su quali parti della transazione sono congelate dalla firma e quali possono ancora essere modificate successivamente. Questo meccanismo garantisce che le firme impegnino precisamente e in modo sicuro i dati della transazione secondo l'intenzione del firmatario. Esistono tre principali SigHash Flags:

- `SIGHASH_ALL` (`0x01`): La firma si applica a tutti gli input e output della transazione, bloccandoli completamente;

- `SIGHASH_NONE` (`0x02`): La firma si applica a tutti gli input ma a nessuno degli output, permettendo che gli output possano essere modificati dopo la firma;

- `SIGHASH_SINGLE` (`0x03`): La firma copre tutti gli input e solo un output corrispondente all'indice dell'input firmato.

Oltre a questi tre SigHash Flags, il modificatore `SIGHASH_ANYONECANPAY` (`0x80`) può essere combinato con ciascuno dei tipi precedenti. Quando questo modificatore viene utilizzato, solo una parte degli input viene firmata, lasciando gli altri aperti a modifiche. Ecco le combinazioni esistenti con il modificatore:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): La firma si applica a un singolo input coprendo tutti gli output della transazione;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): La firma copre un singolo input, senza impegnarsi su alcun output;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): La firma si applica a un singolo input e solo all'output che ha lo stesso indice di questo input.

> ► *Un sinonimo talvolta utilizzato per "SigHash" è "Tipi di Hash della Firma".*