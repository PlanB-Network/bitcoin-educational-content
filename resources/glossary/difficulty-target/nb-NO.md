---
term: VANSKELIGHETSMÅL

---
Vanskelighetsfaktoren, også kjent som vanskelighetsmålet, er en parameter som brukes i konsensusmekanismen ved proof of work (Proof of Work, PoW) på Bitcoin. Målet representerer en numerisk verdi som bestemmer hvor vanskelig det er for utvinnere å løse et spesifikt kryptografisk problem, kalt proof of work, når de oppretter en ny blokk på blokkjeden.

Vanskelighetsgraden er et justerbart 256-biters (64 byte) tall som fastsetter en akseptabel grense for hashing av blokkhoder. Med andre ord, for at en blokk skal være gyldig, må hashingen av overskriften med `SHA256d` (dobbel `SHA256`) være numerisk lavere eller lik vanskelighetsmålet. Beviset på arbeidet består i å endre `nonce`-feltet i blokkoverskriften eller coinbase-transaksjonen til den resulterende hashen er lavere enn målverdien.

Dette målet justeres hver 2016-blokk (omtrent annenhver uke), under en hendelse som kalles "justering" Vanskelighetsgraden beregnes på nytt basert på tiden det tok å utvinne de foregående 2016-blokkene. Hvis den totale tiden er mindre enn to uker, øker vanskelighetsgraden ved at målet justeres nedover. Hvis den totale tiden er mer enn to uker, reduseres vanskelighetsgraden ved å justere målet oppover. Målet er å opprettholde en gjennomsnittlig utvinningstid på 10 minutter per blokk. Denne tiden mellom hver blokk bidrar til å forhindre splittelse av Bitcoin-nettverket, noe som resulterer i sløsing med datakraft. Målet for vanskelighetsgrad finnes i hvert blokkhode, i feltet `nBits`. Siden dette feltet er redusert til 32 bits og målet faktisk er 256 bits, er målet komprimert til et mindre presist vitenskapelig format.

![](../../dictionnaire/assets/34.webp)

> ► *Svårighetsmålet kalles noen ganger også "vanskelighetsfaktoren" I forlengelsen av dette kan det refereres til med kodingen i blokkoverskriftene med betegnelsen "nBits"