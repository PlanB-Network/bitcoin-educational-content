---
term: SPV ČVOR (LAKI ČVOR)
---

Čvor SPV (*Simple Payment Verification*), ponekad nazvan "laki čvor," je lagani klijent čvora Bitcoin koji omogućava korisnicima da verifikuju transakcije bez potrebe za skladištenjem celog Blockchain. Umesto toga, SPV čvor skladišti samo zaglavlja blokova i dobija informacije o specifičnim transakcijama upitom ka punim čvorovima kada je to potrebno. Ovaj princip verifikacije je omogućen strukturom transakcija u Bitcoin blokovima, koje su organizovane unutar kriptografskog akumulatora (Merkle Tree).


Ovaj pristup je povoljan za uređaje sa ograničenim resursima, kao što su mobilni telefoni. Međutim, SPV čvorovi se oslanjaju na pune čvorove za dostupnost informacija, što podrazumeva dodatni nivo poverenja i, samim tim, manju sigurnost u poređenju sa punim čvorovima. SPV čvorovi ne mogu autonomno validirati transakcije, ali mogu proveriti da li je transakcija uključena u blok konsultovanjem Merkle dokaza.