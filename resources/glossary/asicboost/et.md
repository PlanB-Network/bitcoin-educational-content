---
term: ASICBOOST
---

ASICBOOST on algoritmilise optimeerimise meetod, mis leiutati 2016. aastal eesmärgiga suurendada Bitcoini kaevandamise efektiivsust umbes 20% võrra, vähendades iga päise hash-katse jaoks vajalike arvutuste hulka. See tehnika kasutab ära SHA256 hash-funktsiooni omadust, mida kasutatakse kaevandamisel, mis jagab andmed enne nende töötlemist plokkideks. ASICBOOST jätab ühe neist plokkidest mitme hashimiskatse vältel muutmata, võimaldades kaevuril teha selle ploki jaoks tööd ainult osaliselt mitme katse jooksul. See andmete jagamine võimaldab eelnevate arvutuste tulemuste taaskasutamist, vähendades seeläbi vajalike arvutuste koguarvu, et leida kehtiv hash.

ASICBOOSTi saab kasutada kahel kujul: Avalik ASICBOOST ja Varjatud ASICBOOST. Avalik ASICBOOST on kõigile nähtav, kuna see hõlmab `nVersion` välja kasutamist plokis kui nonce'i, ilma tegelikku `Nonce` muutmata. Varjatud vorm püüab neid muudatusi peita, kasutades Merkle'i puid. Siiski on see teine meetod muutunud vähem efektiivseks pärast SegWiti kasutuselevõttu, kuna teine Merkle'i puu suurendab arvutuste hulka, mida selle kasutamiseks on vaja.

Kokkuvõttes võimaldab ASICBOOST kaevuritel mitte teha tõelist täielikku SHA256 arvutust kõigi hashimiskatsete jaoks, kuna osa tulemusest jääb muutmata, mis kiirendab kaevurite tööd.