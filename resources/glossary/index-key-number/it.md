---
term: INDICE (NUMERO CHIAVE)

---
Nel contesto di un portafoglio HD, si riferisce al numero sequenziale assegnato a una chiave figlio generata da una chiave genitore. Questo indice viene utilizzato in combinazione con la chiave genitore e il codice di catena genitore per ricavare in modo deterministico chiavi figlio uniche. Consente un'organizzazione strutturata e la generazione riproducibile di più coppie di chiavi figlio fratelli a partire dalla stessa chiave genitore. È un numero intero di 32 bit utilizzato nella funzione di derivazione `HMAC-SHA512`. Questo numero consente di differenziare le chiavi figlio fratello all'interno di un portafoglio HD.