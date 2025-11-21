---
term: UTXO SET
---

Odnosi se na zbirku svih postojećih UTXO-a u bilo kom trenutku. Drugim rečima, to je velika lista svih različitih delova bitkoina koji čekaju da budu potrošeni. Ako saberete iznose svih UTXO-a u skupu UTXO, dobijamo ukupnu monetarnu masu bitkoina u opticaju. Svaki čvor u mreži Bitcoin održava svoj sopstveni skup UTXO u realnom vremenu. Ažurira ga kako se potvrđuju novi validni blokovi, sa transakcijama koje uključuju, koje troše neke UTXO-e iz skupa UTXO i stvaraju nove zauzvrat.


Ovaj UTXO set čuva svaki čvor kako bi brzo proverio da li su UTXO-ovi potrošeni u transakcijama zaista legitimni. Ovo im omogućava da otkriju i odbace Double-spending pokušaje. UTXO set je često u centru zabrinutosti oko decentralizacije Bitcoin, jer njegova veličina prirodno veoma brzo raste. Pošto se deo njega mora čuvati u RAM-u kako bi se transakcije proveravale u razumnom vremenu, UTXO set bi postepeno mogao učiniti rad Full node previše skupim. UTXO set takođe ima značajan uticaj na IBD (*Initial Block Download*). Što se više UTXO seta može smestiti u RAM, to je IBD brži. Na Bitcoin Core, UTXO set je smešten u fascikli pod nazivom `/chainstate`.


> ► *Na srpskom, "UTXO set" bi mogao biti preveden kao "UTXO set".*