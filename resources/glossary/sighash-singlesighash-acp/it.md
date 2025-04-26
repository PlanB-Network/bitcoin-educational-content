---
term: SIGHASH_SINGOLO/SIGHASH_ACP

---
Tipo di flag SigHash (`0x83`) combinato con il modificatore `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilizzato nelle firme delle transazioni Bitcoin. Questa combinazione specifica che la firma si applica solo a un singolo ingresso specifico e solo all'uscita che ha lo stesso indice di questo ingresso. Altri input e output possono essere aggiunti o modificati da altre parti. Questa configurazione è utile per le transazioni collaborative in cui i partecipanti possono aggiungere i propri input per finanziare un output specifico.