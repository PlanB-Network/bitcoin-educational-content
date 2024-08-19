---
termine: INDEX (NUMERO CHIAVE)
---

Nel contesto di un portafoglio HD, si riferisce al numero sequenziale assegnato a una chiave figlio generata da una chiave genitore. Questo indice viene utilizzato in combinazione con la chiave genitore e il codice catena genitore per derivare deterministicamente chiavi figlio uniche. Permette una organizzazione strutturata e la generazione riproducibile di molteplici coppie di chiavi figlio dalla stessa chiave genitore. È un intero a 32 bit utilizzato nella funzione di derivazione `HMAC-SHA512`. Questo numero quindi differenzia le chiavi figlio all'interno di un portafoglio HD.