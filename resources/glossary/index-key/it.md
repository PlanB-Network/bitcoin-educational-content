---
term: INDICE (CHIAVE)
---

Nel contesto di un portafoglio HD, si riferisce al numero sequenziale assegnato a una chiave figlia generata da una chiave genitore. Questo indice viene utilizzato in combinazione con la chiave genitore e il codice stringa genitore per ricavare in modo deterministico chiavi figlio uniche. Consente un'organizzazione strutturata e la generazione riproducibile di più coppie di chiavi figlio sorelle da un'unica chiave padre. È un numero intero di 32 bit utilizzato nella funzione di derivazione `HMAC-SHA512`. Questo numero può essere utilizzato per differenziare le chiavi figlio all'interno di un portafoglio HD.