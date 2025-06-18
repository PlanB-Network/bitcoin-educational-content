---
term: HORODATAGE
---

Vremensko označavanje, ili "Timestamp" na engleskom, je mehanizam za povezivanje precizne vremenske oznake sa događajem, podacima ili porukom. U opštem kontekstu računarskih sistema, vremensko označavanje se koristi za određivanje hronološkog reda operacija i za verifikaciju integriteta podataka tokom vremena.


U specifičnom slučaju Bitcoin, vremenske oznake se koriste za uspostavljanje hronologije transakcija i blokova. Svaki blok u Blockchain sadrži Timestamp koji ukazuje na približno vreme njegovog kreiranja. Satoshi Nakamoto čak govori o "Timestamp serveru", u svom Belom Papiru, da opiše ono što bismo danas nazvali "Blockchain". Uloga vremenskog označavanja na Bitcoin je da odredi hronologiju transakcija, tako da, bez intervencije centralnog autoriteta, može biti određeno koja transakcija je prva stigla. Ovaj mehanizam omogućava svakom korisniku da verifikuje nepostojanje transakcije u prošlosti, i tako spreči zlonamernog korisnika da izvrši dvostruku potrošnju. Ovaj mehanizam je opravdan od strane Satoshi Nakamoto u njegovom Belom Papiru sa čuvenom rečenicom: "*Ovaj standard se zasniva na Unix vremenu, koje predstavlja ukupan broj sekundi proteklih od 1. januara 1970.


> ► *Vremenske oznake blokova su relativno fleksibilne na Bitcoin, jer da bi Timestamp bio smatran važećim, dovoljno je da bude veći od srednjeg vremena 11 blokova koji mu prethode (MTP) i manji od srednjeg vremena koje vraćaju čvorovi (mrežno prilagođeno vreme) plus 2 sata.*