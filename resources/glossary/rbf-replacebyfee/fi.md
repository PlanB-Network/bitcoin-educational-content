---
term: RBF (REPLACE-BY-FEE) (KORVAUS MAKSULLA)

---
Transaktiomekanismi, jonka avulla lähettäjä voi korvata yhden transaktion toisella maksamalla korkeampia maksuja, jotta sen vahvistaminen nopeutuisi. Jos transaktio, jonka maksut ovat liian alhaiset, jää jumiin, lähettäjä voi käyttää *Replace-By-Fee* -toimintoa korottaakseen maksuja ja priorisoidakseen korvaavan transaktionsa mempoolissa.

RBF:ää sovelletaan niin kauan kuin transaktio on mempoolissa; kun se on kerran lohkossa, sitä ei voi enää korvata. Alkuperäisessä lähetyksessä transaktion on määriteltävä, että se on korvattavissa säätämällä `nSequence`-arvo pienemmäksi kuin `0xfffffffffffe`. Tätä kutsutaan RBF-"lipuksi". Tämä asetus ilmoittaa mahdollisuudesta päivittää transaktio sen lähettämisen jälkeen, mikä mahdollistaa RBF:n myöhemmän lähettämisen. Joskus on kuitenkin mahdollista korvata transaktio, joka ei ole antanut RBF-signaalia. Solmut, jotka käyttävät konfiguraatioparametria `mempoolfullrbf=1`, hyväksyvät tämän korvaamisen, vaikka RBF:ää ei olisi alun perin signaloitu.

Toisin kuin CPFP (*Child Pays For Parent*), jossa vastaanottaja voi toimia nopeuttaakseen maksutapahtumaa, RBF (*Replace-By-Fee*) antaa lähettäjän tehdä aloitteen oman maksutapahtumansa nopeuttamiseksi korottamalla maksuja.