---
term: CISA
---

Lyhenne sanoista "Cross-Input Signature Aggregation". Tämä on tekninen ehdotus, jonka tarkoituksena on optimoida Bitcoin-tapahtumien koko vähentämällä niiden validointiin tarvittavien allekirjoitusten määrää.


Tällä hetkellä Bitcoin:ssä jokaisella tapahtuman syötteellä on oltava oma allekirjoituksensa, ennen kuin sitä voidaan käyttää. Tämä osoittaa, että kyseisen UTXO:n omistaja on hyväksynyt tapahtuman. CISA:n avulla pyritään yhdistämään yhden transaktion kaikkien syötteiden allekirjoitukset yhdeksi allekirjoitukseksi, joka kattaa kaikki syötteet. Näin voitaisiin pienentää useita panoksia sisältävien tapahtumien kokoa ja siten myös niiden kustannuksia. Tämä olisi erityisen hyödyllistä niille, jotka suorittavat kolikoiden yhdistämisiä tai konsolidointeja, ja samalla mahdollistaisi useampien transaktioiden vahvistamisen Bitcoin:llä muuttamatta lohkojen kokoa tai aikaväliä. CISA perustuu Schnorr-protokollaan, joka mahdollistaa allekirjoitusten lineaarisen yhdistämisen. Tämä tarkoittaa, että yksi allekirjoitus voi todistaa useiden toisistaan riippumattomien avainten hallussapidon.


CISA:n toteuttaminen Bitcoin:lla on kuitenkin hyvin monimutkaista, sillä se edellyttää syvällisiä muutoksia skriptien työskentelytapaan. Tällä hetkellä komentosarjojen tarkistus Bitcoin:ssa tehdään syöttö kerrallaan. Siirtyminen malliin, jossa koko tapahtuma tarkistetaan kerralla, kuten CISA:ssa ehdotetaan, ei ole mitenkään yksinkertainen muutos.