---
term: PAYLOAD
---

Nel contesto generale dell'informatica, il termine payload si riferisce ai dati essenziali trasportati all'interno di un pacchetto di dati più grande. Ad esempio, in un indirizzo SegWit V0 su Bitcoin, il payload corrisponde all'hash della chiave pubblica, escludendo vari metadati (l'HRP, il separatore, la versione SegWit e il checksum). Per esempio, nell'indirizzo `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, abbiamo:
* `bc` : la parte leggibile dall'uomo (HRP);
* `1` : il separatore;
* `q` : la versione SegWit. Qui, è la versione 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : il payload, qui, l'hash della chiave pubblica;
* `ys50gj` : il checksum.