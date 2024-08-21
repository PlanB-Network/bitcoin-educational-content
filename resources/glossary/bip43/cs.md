---
term: BIP43
---

Návrh na zlepšení, který zavádí použití úrovně odvozovací cesty k popisu pole účelu ve struktuře HD peněženek, dříve představené v BIP32. Podle BIP43 je první úroveň odvození HD peněženky, hned po hlavním klíči označeném jako `m/`, vyhrazena pro číslo účelu, které udává použitý standard odvození pro zbytek cesty. Toto číslo je zaznamenáno jako zpevněný index. Například, pokud peněženka následuje standard SegWit (BIP84), začátek její odvozovací cesty by byl: `m/84'/`. BIP43 tak umožňuje objasnit, kterých standardů se každý software peněženky drží, aby mezi nimi byla lepší interoperabilita. Standardizace zbytku odvozovací cesty je popsána v BIP44.