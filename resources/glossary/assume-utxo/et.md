---
term: ASSUME UTXO

---
Juhtiva Bitcoin Core'i kliendi konfiguratsiooniparameeter, mis võimaldab just initsialiseeritud (kuid IBD-d veel mitte läbinud) sõlme tehingu ja UTXO komplekti kontrollimist edasi lükata kuni konkreetse hetkefoto tegemiseni. Kontseptsioon tugineb Core'i poolt esitatud ja eeldatavalt täpse UTXO-komplekti (nimekiri kõigist antud hetkel olemasolevatest UTXO-dest) kasutamisele, mis võimaldab sõlme väga kiiresti sünkroniseerida ahelaga, kus on kõige rohkem tööd kogunenud. Kuna sõlme puhul jäetakse pikk IBD samm vahele, muutub see kasutaja jaoks väga kiiresti töökõlblikuks. Oletame, et UTXO jagab sünkroniseerimise (IBD) kaheks osaks:


- Kõigepealt teostab sõlmpunkt Header First Sync (ainult päiste kontrollimine) ja loeb Core'i esitatud UTXO-komplekti kehtivaks;
- Seejärel, kui see on töökorras, kontrollib sõlmpunkt taustal kogu plokkide ajalugu, ajakohastades uut UTXO-komplekti, mida ta ise on kontrollinud. Kui see uus UTXO-komplekt ei vasta Core'i esitatud komplektile, annab ta veateate.

Seega, Oletame, et UTXO kiirendab uue Bitcoini sõlme ettevalmistamist, lükates edasi tehingu kontrollimise protsessi ja UTXO komplekti läbi Core'is esitatud ajakohastatud hetkeseisu.