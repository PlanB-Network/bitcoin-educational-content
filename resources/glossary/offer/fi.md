---
term: TARJOUS
---

BOLT12:ssa *tarjoukset* ovat staattisia QR-koodeja, joilla voi suorittaa useita maksuja Lightning Network:lla. Toisin kuin perinteisiä laskuja, *tarjouksia* voidaan käyttää uudelleen. Niitä voidaan käyttää generate:n useisiin Invoice-pyyntöihin. Kun käyttäjä skannaa *tarjouksen* sisältävän QR-koodin, se lähettää uutta Invoice-pyyntöä koskevan viestin siihen liittyvälle Lightning-solmulle. Solmu vastaa Invoice:lla, jota maksaja voi käyttää. *Tarjoukset* tarjoavat siten yksilöllisen tunnisteen, jonka avulla Lightningissa voidaan vastaanottaa useita maksuja eri käyttäjiltä.