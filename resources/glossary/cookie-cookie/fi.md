---
termi: COOKIE (.COOKIE)
---

Tiedosto, jota käytetään RPC (*Remote Procedure Call*, etäproseduurikutsu) -autentikointiin Bitcoin Core:ssa. Kun bitcoind käynnistyy, se luo yksilöllisen autentikointievästeen ja tallentaa sen tähän tiedostoon. Asiakasohjelmat tai skriptit, jotka haluavat olla vuorovaikutuksessa bitcoind:n kanssa RPC-rajapinnan kautta, voivat käyttää tätä evästettä turvalliseen autentikointiin. Tämä mekanismi mahdollistaa turvallisen kommunikoinnin bitcoind:n ja ulkoisten sovellusten (kuten lompakko-ohjelmiston, esimerkiksi) välillä ilman, että käyttäjänimien ja salasanojen manuaalista hallintaa tarvitaan. `.cookie`-tiedosto luodaan uudelleen joka kerta, kun bitcoind käynnistetään uudelleen, ja se poistetaan sammutettaessa.