---
term: CHECKSUM

---
Un checksum è un valore calcolato da un insieme di dati, utilizzato per verificare l'integrità e la validità di tali dati durante la loro trasmissione o archiviazione. Gli algoritmi di checksum sono progettati per rilevare errori accidentali o alterazioni non intenzionali dei dati, come errori di trasmissione o corruzione dei file. Esistono vari tipi di algoritmi di checksum, come i controlli di parità, i checksum modulari, le funzioni hash crittografiche o i codici BCH (*Bose, Ray-Chaudhuri e Hocquenghem*).

In Bitcoin, i checksum sono utilizzati a livello di applicazione per garantire l'integrità degli indirizzi ricevuti. Un checksum viene calcolato a partire dal payload dell'indirizzo di un utente, quindi aggiunto a questo indirizzo per rilevare eventuali errori durante il suo inserimento. Un checksum è presente anche nelle frasi di recupero (mnemoniche).

> *La traduzione inglese di "somme de contrôle" è "checksum". È generalmente accettato l'uso diretto del termine "checksum" in francese