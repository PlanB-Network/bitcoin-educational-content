term: CHECKSUM
---

Un checksum è un valore calcolato a partire da un insieme di dati, utilizzato per verificare l'integrità e la validità di tali dati durante la loro trasmissione o memorizzazione. Gli algoritmi di checksum sono progettati per rilevare errori accidentali o alterazioni non intenzionali dei dati, come errori di trasmissione o corruzioni di file. Esistono vari tipi di algoritmi di checksum, come i controlli di parità, i checksum modulari, le funzioni hash crittografiche o i codici BCH (*Bose, Ray-Chaudhuri e Hocquenghem*).

In Bitcoin, i checksum sono utilizzati a livello applicativo per garantire l'integrità degli indirizzi di ricezione. Un checksum viene calcolato a partire dal payload di un indirizzo dell'utente, poi aggiunto a questo indirizzo per rilevare possibili errori durante il suo inserimento. Un checksum è presente anche nelle frasi di recupero (mnemoniche).

> ► *La traduzione in inglese di "somme de contrôle" è "checksum". È generalmente accettato utilizzare direttamente il termine "checksum" in francese.*