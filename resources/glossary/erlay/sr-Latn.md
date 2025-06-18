---
term: ERLAY
---

Predloženi mrežni protokol za poboljšanje efikasnosti prenosa nepotvrđenih transakcija između Bitcoin čvorova.


Trenutno se svaka transakcija propagira putem sistema u kojem svaki čvor emituje transakciju za koju zna svim svojim vršnjacima. Problem je što to dovodi do mnogo redundancije i korišćenja propusnog opsega za duplikate. Mnoge emisije transakcija su nepotrebne, jer primalac već zna za te transakcije, a svakom čvoru je potrebno da zna za svaku transakciju samo jednom. Erlay predlaže da se po defaultu ograniči na 8 broj vršnjaka kojima čvor direktno šalje transakcije za koje je svestan, a zatim da se koristi proces usklađivanja zasnovan na minisketch biblioteci kako bi se delile nedostajuće transakcije efikasnije.


Erlay bi smanjio potrošnju propusnog opsega za oko 40%, čineći Full node operaciju pristupačnijom korisnicima sa ograničenim internet konekcijama, i na taj način promovišući bolju decentralizaciju mreže. Ovaj protokol bi takođe održavao skoro konstantnu potrošnju propusnog opsega kako se broj konekcija povećava. To znači da bi bilo mnogo jednostavnije za operatere čvorova da prihvate veoma veliki broj konekcija od svojih vršnjaka, što bi poboljšalo sigurnost Bitcoin mreže smanjenjem rizika od particionisanja, bilo namernog ili slučajnog. Pored toga, Erlay bi otežao određivanje čvora iz kojeg potiče transakcija, čime bi se povećala poverljivost za korisnike čvorova koji ne rade pod Tor-om.


Erlay je predložen u BIP330.