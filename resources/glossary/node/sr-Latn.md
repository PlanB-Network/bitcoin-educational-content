---
term: NODE
---

U Bitcoin mreži, čvor (ili "node" na engleskom) je računar koji pokreće Bitcoin protokol klijent (kao što je Bitcoin Core, na primer). Učestvuje u mreži održavanjem kopije Blockchain, prosleđivanjem i verifikacijom transakcija i novih blokova, i opcionalno, učestvovanjem u Mining procesu. Zbir svih Bitcoin čvorova predstavlja samu Bitcoin mrežu.


Postoji nekoliko tipova čvorova u Bitcoin, uključujući pune čvorove i lake čvorove. Puni čvorovi čuvaju kompletnu kopiju Blockchain, verifikuju sve transakcije i blokove prema pravilima konsenzusa i aktivno učestvuju u širenju transakcija i blokova preko mreže. S druge strane, laki čvorovi, ili SPV (*Simple Payment Verification*) čvorovi, čuvaju samo zaglavlja blokova i oslanjaju se na pune čvorove za dobijanje informacija o transakcijama.


> ► *Neki takođe razlikuju takozvane "pruned nodes" ("pruned node" na engleskom). To su puni čvorovi, koji preuzimaju i verifikuju sve blokove od Genesis bloka, ali čuvaju samo najnovije blokove u memoriji.*