---
term: PAYLOAD

---
Arvutite üldises kontekstis viitab kasuliku koormuse all suuremates andmepakettides edastatavatele olulistele andmetele. Näiteks Bitcoini SegWit V0-aadressi puhul vastab kasulik koormus avaliku võtme hashile, välja arvatud mitmesugused metaandmed (HRP, eraldaja, SegWit-versioon ja kontrollsumma). Näiteks aadressil `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` on meil:


- "bc" : inimloetav osa (HRP);
- `1` : eraldaja;
- `q` : SegWit versioon. Siin on see versioon 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : tasuline koormus, siinkohal avaliku võtme hash;
- `ys50gj` : kontrollsumma.