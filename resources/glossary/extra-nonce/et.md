---
term: EXTRA-Nonce
---

Välja, mida kasutatakse ploki Coinbase Transaction `scriptSig`is, mis võimaldab lisaks klassikalisele Nonce-le, mis asub otse iga ploki päises, testida suuremat arvu võimalusi, et saavutada raskuse eesmärgist madalam Hash.


Coinbase Transaction ekstra-Nonce muutmine muudab selle tehingu identifikaatorit ja seega ka kõigi plokis olevate tehingute Merkle Root identifikaatorit, mis muudab ka ploki päise. See võimaldab Miner-l jätkata hashide otsimist, kui klassikalise Nonce vahemik on juba ammendunud, muutmata selle kandidaatbloki struktuuri.


Mining poolides jaguneb ekstra-Nonce sageli kaheks: üks on pooli poolt genereeritud, et tuvastada iga hakklihamasinat, ja teine on muudetud hakklihamasinate poolt kehtiva osa otsimiseks. See võimaldab koondisesse kuuluvatel erinevatel hakkijatel töötada üheaegselt ühe ja sama kandidaatblokiga kogu nonce'i vahemiku ulatuses, ilma et koondise tasandil dubleeritaks sama tööd.