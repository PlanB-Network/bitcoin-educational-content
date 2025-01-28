---
term: BIP49

---
BIP49 je informativní BIP, který představuje metodu odvozování používanou ke generování vnořených adres SegWit v peněžence HD. Navrhovaná cesta derivace se řídí standardy BIP43 a BIP44, přičemž v hloubce cíle je uveden index `49` (hardened derivation). Například první adresa účtu P2SH-P2WPKH by byla odvozena z cesty: `m/49'/0'/0'/0/0`. Vnořené skripty SegWit byly vynalezeny při spuštění SegWit, aby usnadnily jeho přijetí. Umožňují používat tento nový standard i na peněženkách, které ještě nejsou nativně kompatibilní se SegWit.