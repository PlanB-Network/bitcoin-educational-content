---
term: PRAVILA STANDARDIZACIJE
---

Pravila standardizacije pojedinačno usvaja svaki Bitcoin čvor, pored pravila konsenzusa, kako bi definisao strukturu nepotvrđenih transakcija koje prihvata u svoj Mempool i emituje svojim vršnjacima. Ova pravila su stoga konfigurisana i izvršena lokalno od strane svakog čvora i mogu se razlikovati od jednog čvora do drugog. Ona se primenjuju isključivo na nepotvrđene transakcije. Dakle, čvor će prihvatiti transakciju koju smatra nestandardnom samo ako je već uključena u važeći blok.


Primećeno je da većina čvorova ostavlja podrazumevane konfiguracije kako su uspostavljene u Bitcoin Core, čime se stvara uniformnost standardizovanih pravila širom mreže. Transakcija koja, iako je u skladu sa pravilima konsenzusa, ne poštuje ova pravila standardizacije, imaće poteškoća da bude emitovana preko mreže. Međutim, ona i dalje može biti uključena u važeći blok ako stigne do Miner. U praksi, ove transakcije, poznate kao "nestandardne", često se prenose direktno do Miner putem eksternih sredstava van Bitcoin peer-to-peer mreže. Ovo je često jedini način da se potvrdi ova vrsta transakcije.


Na primer, transakcija koja ne dodeljuje naknade je i dalje validna prema pravilima konsenzusa i nestandardna jer je podrazumevana politika Bitcoin Core za parametar `minRelayTxFee` `0.00001` (u BTC/kB).


> ► *Termin "Mempool pravila" se takođe ponekad koristi za označavanje pravila standardizacije.*