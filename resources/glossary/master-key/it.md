---
term: CHIAVE MASTER

---
Nel contesto dei portafogli HD (Hierarchical Deterministic), la chiave privata master è una chiave privata unica derivata dal seme del portafoglio. Per ottenere la chiave master, la funzione `HMAC-SHA512` viene applicata al seme, usando le parole "*seme di Bitcoin*" letteralmente come chiave. Il risultato di questa operazione produce un output di 512 bit, con i primi 256 bit che costituiscono la chiave master e i restanti 256 bit che formano il codice della catena master. La chiave principale e il codice della catena principale servono come punto di partenza per ricavare tutte le chiavi private e pubbliche secondarie nella struttura ad albero del portafoglio HD. Pertanto, la chiave privata master si trova alla profondità 0 della derivazione.

![](../../dictionnaire/assets/19.webp)