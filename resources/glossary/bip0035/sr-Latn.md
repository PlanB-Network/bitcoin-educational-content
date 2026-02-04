---
term: BIP0035
definition: Predlog koji omogućava čvorovima da dele informacije o svom mempool-u (transakcije na čekanju) sa drugim učesnicima u mreži.
---

Predlog koji omogućava čvoru Bitcoin da otvori informacije o svom Mempool, što znači transakcije koje čekaju potvrdu. Zahvaljujući tome, drugi učesnici mogu primati podatke u realnom vremenu o nepotvrđenim transakcijama slanjem specifične poruke čvoru. Pre usvajanja BIP35, čvorovi su mogli pristupiti informacijama samo o već potvrđenim transakcijama. Ovo poboljšanje nudi SPV novčanicima mogućnost primanja informacija o nepotvrđenim transakcijama, omogućava Miner da izbegne propuštanje transakcija sa visokim naknadama tokom ponovnog pokretanja, i olakšava analizu informacija Mempool od strane eksternih servisa.