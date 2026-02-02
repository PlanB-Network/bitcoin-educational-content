---
term: Nyttolast
definition: Väsentlig data som bärs inom ett större datapaket.
---

I det allmänna databehandlingssammanhanget är en nyttolast de väsentliga data som transporteras i ett större datapaket. I en SegWit V0 över Bitcoin Address motsvarar t.ex. nyttolasten Hash för den offentliga nyckeln, utan de olika metadata (HRP, separator, SegWit-version och kontrollsumma). Till exempel, vid Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, har vi :




- `bc`: den maskinläsbara delen (HRP) ;
- `1`: separatorn ;
- `q`: SegWit version. Detta är version 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: nyttolasten, i det här fallet Hash för den offentliga nyckeln ;
- `ys50gj`: checksumma.