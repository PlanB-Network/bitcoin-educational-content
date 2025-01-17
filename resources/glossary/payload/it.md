---
term: CARICO

---
Nel contesto generale dell'informatica, un payload si riferisce ai dati essenziali trasportati all'interno di un pacchetto di dati più grande. Ad esempio, in un indirizzo SegWit V0 su Bitcoin, il payload corrisponde all'hash della chiave pubblica, esclusi vari metadati (l'HRP, il separatore, la versione SegWit e il checksum). Ad esempio, nell'indirizzo `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, abbiamo:


- `bc` : la parte leggibile dall'uomo (HRP);
- `1` : il separatore;
- `q` : la versione di SegWit. Qui è la versione 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : il payload, in questo caso l'hash della chiave pubblica;
- `ys50gj` : il checksum.