---
term: TRANSACTION STANDARD
---

Transakcija Bitcoin koja, pored pridržavanja pravila konsenzusa, takođe spada u pravila standardizacije postavljena podrazumevano na Bitcoin Core čvorovima. Ova pravila standardizacije nameće pojedinačno svaki Bitcoin čvor, pored pravila konsenzusa, kako bi definisao strukturu nepotvrđenih transakcija koje prihvata u svom Mempool i prenosi svojim vršnjacima.


Ova pravila su tako konfigurisana i izvršavaju se lokalno od strane svakog čvora i mogu se razlikovati od jednog čvora do drugog. Ona se primenjuju isključivo na nepotvrđene transakcije. Stoga, čvor će prihvatiti transakciju koju smatra nestandardnom samo ako je već uključena u važeći blok.


Primećeno je da većina čvorova ostavlja podrazumevane konfiguracije kako su uspostavljene u Bitcoin Core, čime se stvara uniformnost standardizovanih pravila širom mreže. Transakcija koja, iako je u skladu sa pravilima konsenzusa, ne poštuje ova pravila standardizacije, imaće poteškoća u propagaciji kroz mrežu. Međutim, ona i dalje može biti uključena u važeći blok ako stigne do Miner. U praksi, ove transakcije, kvalifikovane kao nestandardne, često se prenose direktno na Miner putem eksternih sredstava prema Bitcoin peer-to-peer mreži. Ovo je često jedini način da se potvrdi takva transakcija. Na primer, transakcija koja ne dodeljuje naknade je i validna prema pravilima konsenzusa i nestandardna, jer je podrazumevana politika Bitcoin Core za `minRelayTxFee` parametar `0.00001` (u BTC/kB).