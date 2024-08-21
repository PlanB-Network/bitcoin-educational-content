---
termi: SETTINGS.JSON
---

Tiedosto, jota käytetään Bitcoin Core:ssa graafisen käyttöliittymän (GUI) asetusten tallentamiseen. Se säilyttää tietoa käyttäjän konfiguraatioista, kuten esimerkiksi avoimista lompakoista. Kun Bitcoin Core käynnistetään uudelleen, tämä tiedosto mahdollistaa aiemmin aktiivisten lompakoiden automaattisen uudelleenavauksen sovelluksen sulkeutumisen jälkeen. Jos lompakko suljetaan GUI:n kautta, se poistetaan myös tästä tiedostosta, eikä sitä näin ollen avata automaattisesti seuraavalla käynnistyskerralla.