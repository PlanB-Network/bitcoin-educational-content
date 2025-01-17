---
term: ATOMIC SWAP

---
Teknologi som gjør det mulig å utveksle kryptovalutaer direkte mellom to parter, uten behov for tillit og uten mellomledd. Disse vekslingene kalles "atomære" fordi de bare kan resultere i to utfall:


- Enten er utvekslingen vellykket, og begge deltakerne har effektivt utvekslet kryptovalutaene sine;
- Eller så mislykkes utvekslingen, og begge deltakerne drar med sine opprinnelige kryptovalutaer.

Atomic Swaps kan utføres enten med samme kryptovaluta, i så fall kalles det også en "*coinswap*", eller mellom ulike kryptovalutaer. Historisk sett har de basert seg på "Hash Time-Locked Contracts" (HTLC), et tidslåsingssystem som garanterer fullføring eller total kansellering av utvekslingen, og dermed bevarer integriteten til midlene til de involverte partene. Denne metoden krevde protokoller som kunne håndtere både skript og tidslåsing. De siste årene har imidlertid trenden gått i retning av bruk av *Adaptor Signatures*. Denne andre metoden har den fordelen at den eliminerer behovet for skript, noe som reduserer driftskostnadene. En annen stor fordel er at den ikke krever bruk av identisk hashing for begge deler av transaksjonen, noe som bidrar til å unngå å avsløre en kobling mellom dem.