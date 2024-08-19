---
termine: FUNZIONE HASH
---

Una funzione matematica che prende un input di dimensione variabile (chiamato messaggio) e produce un output di dimensione fissa (chiamato hash, hashing, digest o impronta digitale). Le funzioni hash sono primitive ampiamente utilizzate in crittografia. Esse mostrano specifiche proprietà che le rendono adatte all'uso in contesti sicuri:
* Resistenza alla pre-immagine: deve essere molto difficile trovare un messaggio che produce uno specifico hash, ovvero, trovare una pre-immagine $m$ per un hash $h$ tale che $h = H(m)$, dove $H$ è la funzione hash;
* Resistenza alla seconda pre-immagine: dato un messaggio $m_1$, deve essere molto difficile trovare un altro messaggio $m_2$ (diverso da $m_1$) tale che $H(m_1) = H(m_2)$;
* Resistenza alle collisioni: deve essere molto difficile trovare due messaggi distinti $m_1$ e $m_2$ tali che $H(m_1) = H(m_2)$;
* Resistenza alla manomissione: piccole modifiche nell'input devono causare cambiamenti significativi e imprevedibili nell'output.

Nel contesto di Bitcoin, le funzioni hash sono utilizzate per diversi scopi, inclusi il meccanismo di prova di lavoro (*Proof-of-Work*), gli identificatori di transazione, la generazione di indirizzi, il calcolo di checksum e la creazione di strutture dati come gli alberi di Merkle. Sul lato del protocollo, Bitcoin utilizza esclusivamente la funzione `SHA256d`, anche denominata `HASH256`, che consiste in un doppio hash `SHA256`. `HASH256` è utilizzato anche nel calcolo di certi checksum, in particolare per le chiavi estese (`xpub`, `xprv`...). Sul lato del portafoglio, sono inoltre utilizzati:
* Semplice `SHA256` per i checksum delle frasi mnemoniche;
* `SHA512` all'interno degli algoritmi `HMAC` e `PBKDF2` utilizzati nel processo di derivazione di portafogli deterministici e gerarchici;
* `HASH160`, che descrive un uso successivo di un `SHA256` e un `RIPEMD160`. `HASH160` è utilizzato nel processo di generazione di indirizzi di ricezione (eccetto P2PK e P2TR) e nel calcolo delle impronte digitali delle chiavi genitrici per le chiavi estese.

> ► *In inglese, è definita come "hash function".*