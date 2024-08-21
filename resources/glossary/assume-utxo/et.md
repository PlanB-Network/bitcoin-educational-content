---
term: ASSUME UTXO
---

Konfiguratsiooniparameeter juhtivas Bitcoin Core kliendis, mis võimaldab äsja initsialiseeritud sõlmel (mis ei ole veel läbinud IBD-d) edasi lükata tehingute ja UTXO komplekti kinnitamist kuni antud hetktõmmiseni. Kontseptsioon tugineb UTXO komplekti kasutamisele (nimekiri kõigist antud ajahetkel olemasolevatest UTXO-dest), mille on pakkunud Core ja mida peetakse täpseks, mis võimaldab sõlmel väga kiiresti sünkroniseerida kõige rohkem tööd kogunenud ahelaga. Kuna sõlm jätta vahele pikaajaline IBD etapp, muutub see oma kasutaja jaoks väga kiiresti operatiivseks. Assume UTXO jagab sünkroniseerimise (IBD) kaheks osaks:
* Esiteks teostab sõlm Header First Sync (ainult päiste kinnitamine) ja peab Core'i poolt pakutud UTXO komplekti kehtivaks;
* Seejärel, kui see on operatiivne, kontrollib sõlm taustal täielikku plokkide ajalugu, uuendades uut UTXO komplekti, mille ta on ise kinnitanud. Kui see uus UTXO komplekt ei ühti Core'i poolt pakutuga, genereerib see veateate.

Seega kiirendab Assume UTXO uue Bitcoin sõlme ettevalmistamist, lükates tehingute kinnitamise protsessi ja UTXO komplekti edasi uuendatud hetktõmmise kaudu, mida pakutakse Core'is.