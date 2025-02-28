---
term: PAYLOAD

---
I generell datasammenheng refererer en nyttelast til de essensielle dataene som transporteres i en større datapakke. I en SegWit V0-adresse på Bitcoin tilsvarer nyttelasten for eksempel hashen til den offentlige nøkkelen, unntatt ulike metadata (HRP, separatoren, SegWit-versjonen og kontrollsummen). I adressen `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` har vi for eksempel:


- `bc` : den menneskelesbare delen (HRP);
- `1` : skilletegnet;
- `q` : SegWit-versjonen. Her er det versjon 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : nyttelasten, her hashen til den offentlige nøkkelen;
- `ys50gj` : sjekksummen.