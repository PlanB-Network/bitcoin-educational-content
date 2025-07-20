---
term: CARICO UTILE
---

Nel contesto generale dell'informatica, un payload è il dato essenziale trasportato in un pacchetto di dati più grande. Ad esempio, in un SegWit V0 su Bitcoin Address, il payload corrisponde al Hash della chiave pubblica, senza i vari metadati (HRP, separatore, versione SegWit e checksum). Ad esempio, al Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, abbiamo :




- `bc`: la parte leggibile dall'uomo (HRP) ;
- `1`: il separatore ;
- `q`: Versione SegWit. Questa è la versione 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: il payload, in questo caso il Hash della chiave pubblica;
- `ys50gj`: checksum.