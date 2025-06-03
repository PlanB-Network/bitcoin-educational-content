---
term: CHAUMIAN CoinJoin
---

Protokol CoinJoin koji koristi slepe potpise Davida Chauma i Tor za komunikaciju između učesnika i servera koordinatora. Cilj Chaumian CoinJoin je da osigura učesnicima da koordinator ne može ukrasti bitkoine, niti povezati ulaze i izlaze zajedno.


Da bi se to postiglo, korisnici šalju svoj unos i kriptografski blinded prijem Address koordinatoru. Ovaj Address, nekada unblinded, je namenjen za primanje bitkoina kao izlaz iz CoinJoin. Koordinator potpisuje ove tokene i vraća ih korisnicima. Korisnici se zatim anonimno ponovo povezuju na koordinatorov server sa novim Tor identitetom i otkrivaju svoje izlazne adrese u običnom tekstu za konstrukciju transakcije. Koordinator može da verifikuje da sve ove prijemne adrese dolaze od legitimnih korisnika, jer je prethodno potpisao njihovu blinded verziju svojim privatnim ključem. Međutim, on ne može da poveže određeni izlazni Address sa datim ulaznim korisnikom. Stoga, ne postoji veza između ulaza i izlaza, čak ni iz koordinatorove perspektive. Kada koordinator konstruira transakciju, šalje je nazad učesnicima koji je potpisuju kako bi otključali svoj unos, nakon što verifikuju da je njihov izlaz zaista u toj transakciji. Učesnici šalju potpis koordinatoru. Kada se prikupe svi potpisi, koordinator može emitovati CoinJoin transakciju na Bitcoin mreži.


![](../../dictionnaire/assets/38.webp)


Ova metoda osigurava da koordinator ne može ugroziti anonimnost učesnika niti ukrasti bitkoine tokom celog CoinJoin procesa.


Teško je sa sigurnošću utvrditi ko je prvi uveo ideju CoinJoin na Bitcoin, i ko je imao ideju da koristi slepe potpise Davida Chauma u ovom kontekstu. Često se misli da je Gregory Maxwell prvi o tome diskutovao u [poruci na BitcoinTalk-u 2013. godine](https://bitcointalk.org/index.php?topic=279249.0):


> *"Korišćenjem Chaum slepih potpisa: Korisnici se povezuju i pružaju ulaze (i menjaju adrese) kao i kriptografski blinded verziju Address na koju žele da pošalju svoje privatne novčiće; server potpisuje tokene i vraća ih. Korisnici se anonimno ponovo povezuju, otkrivaju svoje izlazne adrese i vraćaju ih serveru. Server može videti da su svi izlazi potpisani od strane njega i da, prema tome, svi izlazi dolaze od validnih učesnika. Kasnije, ljudi se ponovo povezuju i potpisuju."*

Maxwell, G. (2013, August 22). *CoinJoin: Bitcoin privatnost za stvarni svet*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Međutim, postoje i raniji spomeni, kako za Chaumove potpise u kontekstu mešanja, tako i za coinjoins. [U junu 2011, Duncan Townsend je predstavio na BitcoinTalk-u](https://bitcointalk.org/index.php?topic=12751.0) mikser koji koristi Chaumove potpise na način vrlo sličan modernim Chaumian coinjoins. U istoj temi, postoji [poruka od hashcoin-a kao odgovor na Duncan Townsend-a](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) za poboljšanje njegovog miksera. Ova poruka precizno predstavlja ono što najviše podseća na coinjoins. Takođe postoji spomen sličnog sistema u [poruci od Alex Mizrahi iz 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), dok je savetovao kreatore Tenebrix-a. Sam termin "CoinJoin" ne bi bio izmišljen od strane Greg Maxwell-a, već bi potekao od ideje Petera Todd-a.