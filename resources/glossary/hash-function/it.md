---
term: FUNZIONE HASH

---
Una funzione matematica che prende un input di dimensioni variabili (chiamato messaggio) e produce un output di dimensioni fisse (chiamato hash, hashing, digest o impronta digitale). Le funzioni hash sono primitive ampiamente utilizzate in crittografia. Presentano proprietà specifiche che le rendono adatte all'uso in contesti sicuri:


- Resistenza alle preimmagini: deve essere molto difficile trovare un messaggio che produca un hash specifico, cioè trovare una preimmagine $m$ per un hash $h$ tale che $h = H(m)$, dove $H$ è la funzione hash;
- Resistenza alla seconda preimmagine: dato un messaggio $m_1$, deve essere molto difficile trovare un altro messaggio $m_2$ (diverso da $m_1$) tale che $H(m_1) = H(m_2)$;
- Resistenza alla collisione: deve essere molto difficile trovare due messaggi distinti $m_1$ e $m_2$ tali che $H(m_1) = H(m_2)$;
- Resistenza alle manomissioni: piccole variazioni dell'ingresso devono causare variazioni significative e imprevedibili dell'uscita.

Nel contesto di Bitcoin, le funzioni hash sono utilizzate per diversi scopi, tra cui il meccanismo di prova del lavoro (*Proof-of-Work*), gli identificatori delle transazioni, la generazione degli indirizzi, il calcolo dei checksum e la creazione di strutture dati come gli alberi di Merkle. Dal punto di vista del protocollo, Bitcoin utilizza esclusivamente la funzione `SHA256d`, chiamata anche `HASH256`, che consiste in un doppio hash `SHA256`. la funzione `HASH256` è utilizzata anche per il calcolo di alcuni checksum, in particolare per le chiavi estese (`xpub`, `xprv`...). Per quanto riguarda il portafoglio, vengono utilizzati anche i seguenti elementi:


- Semplice `SHA256` per le somme di controllo delle frasi mnemoniche;
- `SHA512` all'interno degli algoritmi `HMAC` e `PBKDF2` utilizzati nel processo di derivazione dei portafogli deterministici e gerarchici;
- `HASH160`, che descrive un uso successivo di un `SHA256` e di un `RIPEMD160`. la `HASH160` viene utilizzata nel processo di generazione degli indirizzi di ricezione (eccetto P2PK e P2TR) e nel calcolo delle impronte delle chiavi genitore per le chiavi estese.

> *In inglese, si parla di "funzione hash"