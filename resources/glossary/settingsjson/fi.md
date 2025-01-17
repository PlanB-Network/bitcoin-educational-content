---
term: JSON

---
Tiedosto, jota käytetään Bitcoin Coressa graafisen käyttöliittymän (GUI) asetusten tallentamiseen. Se säilyttää tietoja käyttäjän asetuksista, kuten esimerkiksi avoimista lompakoista. Kun Bitcoin Core käynnistetään uudelleen, tämä tiedosto mahdollistaa sellaisten lompakoiden automaattisen avaamisen uudelleen, jotka olivat aktiivisia ennen sovelluksen sulkemista. Jos lompakko suljetaan graafisen käyttöliittymän kautta, se poistetaan myös tästä tiedostosta, eikä sitä näin ollen avata automaattisesti uudelleen seuraavalla käynnistyksellä.