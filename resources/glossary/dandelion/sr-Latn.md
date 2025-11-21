---
term: MASLAČAK
---

Predlog usmeren na poboljšanje privatnosti rutiranja transakcija u Bitcoin mreži kako bi se suprotstavilo deanonimizaciji. U standardnom radu Bitcoin, transakcije se odmah emituju na više čvorova. Ovaj fenomen potencijalno može omogućiti posmatračima da povežu transakcije, koje su inače anonimne, sa IP adresama. Cilj BIP156 je da Address ovaj problem. Da bi to postigao, uvodi dodatnu fazu u procesu emitovanja kako bi se očuvala anonimnost pre javne propagacije. Tako Dandelion prvo koristi fazu "stem" gde se transakcija šalje kroz nasumičan put čvorova, pre nego što se emituje celokupnoj mreži u "fluff" fazi. Stem i fluff su reference na ponašanje propagacije transakcije kroz mrežu, podsećajući na oblik maslačka. Ovaj metod rutiranja zamagljuje trag koji vodi nazad do izvornog čvora, otežavajući praćenje transakcije kroz mrežu do njenog porekla.


![](../../dictionnaire/assets/36.webp)