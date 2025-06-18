---
term: RESINHRONIZACIJA
---

Odnosi se na fenomen u kojem Blockchain prolazi kroz modifikaciju svoje strukture zbog postojanja konkurentskih blokova na istoj visini. Ovo se dešava kada se deo Blockchain zameni drugim lancem sa većom količinom akumuliranog rada.


Ove resinhronizacije su deo prirodnog funkcionisanja Bitcoin, gde različiti rudari mogu pronaći nove blokove gotovo istovremeno, čime se Bitcoin mreža deli na dva dela. U takvim slučajevima, mreža se može privremeno podeliti na konkurentske lance. Na kraju, kada jedan od tih lanaca akumulira više rada, drugi lanci bivaju napušteni od strane čvorova, a njihovi blokovi postaju ono što se naziva "zastareli blokovi" ili "blokovi siročad". Ovaj proces zamene jednog lanca drugim je resinhronizacija.


![](../../dictionnaire/assets/9.webp)


Resinhronizacije mogu imati različite posledice. Prvo, ako je korisnik imao transakciju potvrđenu u bloku koji se ispostavi da je napušten, ali ta transakcija nije pronađena u konačno validnom lancu, tada njihova transakcija ponovo postaje nepotvrđena. Zbog toga se savetuje da se uvek sačeka najmanje 6 potvrda kako bi se transakcija smatrala zaista nepromenljivom. Nakon 6 blokova dubine, resinhronizacije su toliko malo verovatne da se šansa za njihovo dešavanje može smatrati praktično ništavnom.


Štaviše, na nivou globalnog sistema, resinhronizacije podrazumevaju rasipanje računarske snage rudara. Naime, kada dođe do razdvajanja, neki rudari će biti on chain `A`, a drugi on chain `B`. Ako lanac `B` bude na kraju napušten tokom resinhronizacije, tada je sva računarska snaga koju su rudari uložili u taj lanac, po definiciji, protraćena. Ako ima previše resinhronizacija na Bitcoin mreži, ukupna sigurnost mreže je stoga smanjena. Ovo je delimično razlog zašto povećanje veličine bloka ili smanjenje intervala između svakog bloka (10 minuta) može biti opasno.


> ► *Neki bitkoineri preferiraju da koriste "Orphan block" za označavanje isteka bloka. Takođe, iako je anglicizam, u uobičajenom jeziku, "reorganizacija" ili "reorg" se često preferira nad "resinhronizacijom."*