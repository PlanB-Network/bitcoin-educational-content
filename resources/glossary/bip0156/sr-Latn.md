---
term: BIP0156
---

Predlog, poznat kao Dandelion, koji ima za cilj poboljšanje privatnosti usmeravanja transakcija u Bitcoin mreži kako bi se suprotstavio deanonimizaciji. U standardnom radu Bitcoin, transakcije se odmah emituju na više čvorova. Ako posmatrač može videti svaku transakciju koju prenosi svaki čvor na mreži, mogao bi pretpostaviti da je prvi čvor koji šalje transakciju takođe i izvorni čvor te transakcije, i stoga da dolazi od operatera čvora. Ovaj fenomen bi potencijalno mogao omogućiti posmatračima da povežu transakcije, koje su inače anonimne, sa IP adresama.


Cilj BIP156 je da Address ovaj problem. Da bi to postigao, uvodi dodatnu fazu u emitovanju kako bi se očuvala anonimnost pre javne propagacije. Tako Dandelion prvo koristi fazu "stem" gde se transakcija šalje kroz nasumičan put čvorova, pre nego što se emituje celokupnoj mreži u fazi "fluff". Stem i fluff su reference na ponašanje propagacije transakcije kroz mrežu, podsećajući na oblik maslačka (*a dandelion* na engleskom).


Ova metoda rutiranja prikriva trag koji vodi nazad do izvornog čvora, otežavajući praćenje transakcije kroz mrežu do njenog porekla. Dandelion tako poboljšava privatnost ograničavanjem sposobnosti protivnika da deanonimizuju mrežu. Ova metoda je još efikasnija kada transakcija prelazi tokom "stem" faze čvor koji šifrira svoje mrežne komunikacije, kao što je slučaj sa Tor-om ili *P2P Transport V2*. BIP156 još uvek nije dodat u Bitcoin Core.