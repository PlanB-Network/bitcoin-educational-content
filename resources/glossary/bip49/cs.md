---
term: BIP49
---

BIP49 je informativní BIP, který představuje metodu derivace používanou pro generování vnořených SegWit adres v HD peněžence. Navrhovaná cesta derivace sleduje standardy BIP43 a BIP44, s indexem `49'` (pevná derivace) na úrovni cíle. Například první adresa účtu P2SH-P2WPKH by byla odvozena z cesty: `m/49'/0'/0'/0/0`. Vnořené SegWit skripty byly vynalezeny při spuštění SegWit, aby usnadnily jeho adopci. Umožňují použití tohoto nového standardu, dokonce i na peněženkách, které ještě nejsou s SegWit nativně kompatibilní.