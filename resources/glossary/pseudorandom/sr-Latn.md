---
term: PSEUDO-RANDOM
---

Ovaj pridev se koristi za opisivanje niza brojeva koji, iako su rezultat determinističkog procesa, pokazuju karakteristike koje su bliske onima idealnog zaista nasumičnog niza. Koncept idealne nasumičnosti podrazumeva potpuni izostanak predvidljivosti i korelacije između sukcesivnih Elements. Pseudo-nasumičan broj generiše se determinističkim algoritmom i stoga je, u teoriji, potpuno predvidljiv ako se zna početno stanje generatora.


Algoritam za generisanje pseudo-slučajnih brojeva (PRNG) koristi se za proizvodnju takvih brojeva. Obično počinje od početne vrednosti, ili "seed," i zatim primenjuje niz matematičkih transformacija kako bi proizveo niz brojeva. Zbog ove determinisanosti, važno je za kriptografsku sigurnost da početni seed ostane tajan. Pseudo-slučajni nizovi se široko koriste u raznim oblastima, uključujući kriptografiju, jer pokazuju naizgled slučajno ponašanje koje je dovoljno za mnoge primene. Evaluacija kvaliteta PRNG-a zasniva se na meri u kojoj njegov izlaz prilazi pravoj slučajnosti u smislu distribucije, korelacija i drugih statističkih svojstava. U kontekstu Bitcoin, pseudo-slučajni brojevi se koriste za proizvodnju privatnih ključeva, ili za generate seed za determinističke i hijerarhijske novčanike.