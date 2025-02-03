---
term: BIP43

---
Návrh na zlepšení, který zavádí použití úrovně cesty odvození pro popis pole účelu ve struktuře peněženek HD, dříve zavedené v BIP32. Podle BIP43 je první úroveň derivace HD peněženky, hned za hlavním klíčem označeným jako `m/`, vyhrazena pro číslo účelu, které označuje standard derivace použitý pro zbytek cesty. Toto číslo je zaznamenáno jako zpevněný index. Například pokud se peněženka řídí standardem SegWit (BIP84), bude začátek její derivační cesty následující: `m/84'/`. BIP43 tak umožňuje vyjasnit standardy, které dodržují jednotlivé softwary peněženek, aby mezi nimi byla lepší interoperabilita. Standardizace zbytku odvozovací cesty je popsána v BIP44.