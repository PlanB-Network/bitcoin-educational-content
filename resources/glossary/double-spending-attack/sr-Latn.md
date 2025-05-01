---
term: DVOSTRUKO TROŠENJE (NAPAD)
---

Napad u kojem zlonamerni korisnik pokušava da iskoristi isti UTXO (*Unspent Transaction Output*) više puta kako bi se obogatio na račun strana uključenih u transakcije. U principu, kada je transakcija potvrđena u bloku i dodata u Blockchain, korišćenje tih bitkoina je trajno zabeleženo, sprečavajući bilo kakvo dalje trošenje istih bitkoina. Sprečavanje dvostrukog trošenja je čak primarna korisnost Blockchain.


U kontekstu napada dvostrukog trošenja, napadač prvo obavi legitimnu transakciju sa trgovcem, a zatim kreira drugu konkurentsku transakciju trošeći iste novčiće, bilo tako što ih šalje nazad sebi da povrati iznos ili ih koristi za kupovinu drugog dobra ili usluge od drugog trgovca.


Postoje dva glavna scenarija koja mogu omogućiti ovaj napad. Prvi, i najjednostavniji za napadača, uključuje izvršenje lažne transakcije pre nego što legitimna transakcija bude uključena u blok. Da bi osigurali da njihova lažna transakcija bude prva potvrđena, napadač povezuje znatno veće naknade za transakciju sa njom nego sa legitimnom transakcijom. Ovo je vrsta lažnog RBF. Ovaj scenario je moguć samo ako trgovac pristane da finalizuje prodaju u "zeroconf," što znači bez ikakvih potvrda za transakciju plaćanja. Zbog toga se snažno preporučuje čekanje na nekoliko potvrda pre nego što se transakcija smatra nepromenljivom. Drugi scenario, mnogo složeniji, je 51% napad. Ako napadač kontroliše značajan deo računarske snage mreže, može iskopati konkurentski lanac onom koji sadrži legitimnu transakciju, ali uključujući njihovu lažnu transakciju. Kada trgovac prihvati prodaju i napadač uspe da stvori duži lanac (sa više akumuliranog rada) od legitimnog lanca, tada može emitovati svoj lažni lanac, koji će mrežni čvorovi prepoznati kao važeći.