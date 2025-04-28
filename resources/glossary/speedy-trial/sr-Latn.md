---
term: BRZO SUĐENJE
---

Metod aktivacije Soft Fork inicijalno konceptualizovan za Taproot početkom 2021. od strane Davida A. Hardinga na osnovu ideje Russella O'Connora. Njegov princip je korišćenje BIP8 metode sa `LOT` parametrom postavljenim na `false`, dok se period aktivacije smanjuje na samo 3 meseca. Ovaj skraćeni period glasanja omogućava brzu verifikaciju odobrenja Miner. Ako se tokom jednog od perioda dostigne potreban prag odobrenja, Soft Fork se tada zaključava. Biće aktiviran nekoliko meseci kasnije, čime se rudarima daje potrebno vreme za ažuriranje njihovog softvera.


Uspeh ove metode za Taproot, koja je uživala širok konsenzus unutar Bitcoin zajednice, međutim, ne garantuje njenu efikasnost za sva ažuriranja. Iako metoda Speedy Trial omogućava bržu aktivaciju, neki developeri izražavaju zabrinutost zbog njene buduće upotrebe. Oni se plaše da bi to moglo dovesti do prebrzog niza Soft forkova, što bi potencijalno moglo ugroziti stabilnost i sigurnost Bitcoin protokola. U poređenju sa BIP8 sa `LOT=true` parametrom, metoda Speedy Trial je mnogo manje preteća za rudare. Nije planiran automatski UASF. Ova metoda aktivacije još nije formalizovana unutar BIP-a.


> ► *Termin "Speedy Trial" je preuzet iz pravne terminologije i označava "ubrzano suđenje." Ovo ukazuje na činjenicu da se predlog za poboljšanje brzo iznosi pred sud rudara, kako bi se utvrdile njihove namere. Generalno je prihvaćeno da se engleski termin direktno koristi u francuskom.*