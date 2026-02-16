---
term: Assume utxo

definition: Bitcoin Core'i parameeter, mis lubab uue sõlme kiiresti sünkroniseerida, kasutades UTXO komplekti hetktõmmist, mida eeldatakse kehtivaks, enne ajaloo kontrollimist taustal.
---
Konfiguratsiooniparameeter enamus-kliendis Bitcoin Core, mis võimaldab äsja initsialiseeritud sõlmel (kuid mis pole veel IBD-d teinud) lükata edasi tehingute ja UTXO komplekti kontrollimise enne antud snapshot'i. Kontseptsioon põhineb Core'i poolt pakutava ja täpseks peetava UTXO komplekti (kõigi antud ajahetkel eksisteerivate UTXO-de loend) kasutamisel, mis võimaldab sõlmel sünkroonida väga kiiresti ahelaga, millel on kõige rohkem kogunenud tööd. Kuna sõlm jätab pika IBD etapi vahele, on see oma kasutaja jaoks väga kiiresti töökõlblik.

Assume UTXO jagab sünkroonimise (IBD) kaheks osaks: Esiteks teostab sõlm Header First Sync (ainult päiste kontrollimine) ja peab Core'i poolt pakutavat UTXO komplekti kehtivaks; Seejärel, kui see on töökorras, kontrollib sõlm taustal täielikku plokkide ajalugu, värskendades uut UTXO komplekti, mida ta on ise kontrollinud. Kui viimane ei vasta Core'i pakutavale UTXO komplektile, annab see veateate.

Assume UTXO võimaldab seega kiirendada uue Bitcoin-sõlme ettevalmistamist, lükates tehingute ja UTXO komplekti kontrollimise protsessi edasi tänu Core'is pakutavale uuendatud snapshot'ile.





