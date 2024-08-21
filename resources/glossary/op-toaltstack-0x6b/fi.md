---
termi: OP_TOALTSTACK (0X6B)
---

Siirtää pääpinon (*main stack*) päällimmäisen alkion vaihtoehtoiseen pinoon (*alt stack*). Tätä operaatiokoodia käytetään väliaikaisesti tietojen sivuun tallentamiseen myöhempää käyttöä varten skriptissä. Siirretty alkio poistetaan näin ollen pääpinosta. `OP_FROMALTSTACK` käytetään sitten sen palauttamiseen takaisin pääpinon päälle.