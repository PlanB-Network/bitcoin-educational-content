---
term: HASH160
---

Kriptografska funkcija korišćena u Bitcoin, posebno za generisanje Legacy i SegWit v0 adresa za primanje. Kombinuje dve Hash funkcije koje se sukcesivno izvršavaju na ulazu: prvo SHA256, zatim RIPEMD160. Izlaz ove funkcije je stoga 160 bita.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$