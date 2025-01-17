---
term: COOKIE (.COOKIE)

---
Tiedosto, jota käytetään RPC (*Remote Procedure Call*) -todennukseen Bitcoin Coressa. Kun bitcoind käynnistyy, se luo yksilöllisen todennusevästeen ja tallentaa sen tähän tiedostoon. Asiakkaat tai skriptit, jotka haluavat olla vuorovaikutuksessa bitcoindin kanssa RPC-rajapinnan kautta, voivat käyttää tätä evästettä todennukseen turvallisesti. Tämä mekanismi mahdollistaa turvallisen viestinnän bitcoindin ja ulkoisten sovellusten (kuten esimerkiksi lompakko-ohjelmistojen) välillä ilman, että käyttäjätunnusten ja salasanojen manuaalista hallintaa tarvitaan. `.cookie`-tiedosto luodaan uudelleen jokaisella bitcoindin uudelleenkäynnistyksellä ja poistetaan sammutuksen yhteydessä.