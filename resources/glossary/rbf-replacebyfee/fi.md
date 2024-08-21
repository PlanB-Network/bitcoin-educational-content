---
termi: RBF (REPLACE-BY-FEE)
---

Transaktiomekanismi, joka mahdollistaa lähettäjän korvata yhden transaktion toisella maksamalla korkeampia kuluja, jotta sen vahvistuminen nopeutuisi. Jos transaktio jää jumiin liian alhaisten kulujen vuoksi, lähettäjä voi käyttää *Replace-By-Fee* -toimintoa korottaakseen kuluja ja priorisoidakseen korvaavan transaktion mempoolissa.

RBF on sovellettavissa niin kauan kuin transaktio on mempoolissa; kerran lohkoon lisättynä sitä ei voi enää korvata. Alkuperäisessä lähetyksessä transaktion on määritettävä korvattavuutensa säätämällä `nSequence`-arvoa numeroon, joka on pienempi kuin `0xfffffffe`. Tätä kutsutaan RBF-"lipuksi". Tämä asetus viestittää mahdollisuudesta päivittää transaktiota sen lähettämisen jälkeen, mikä mahdollistaa RBF:n käytön. Joskus on kuitenkin mahdollista korvata transaktio, joka ei ole merkinnyt RBF:ää. Solmut, jotka käyttävät konfiguraatioparametria `mempoolfullrbf=1`, hyväksyvät tämän korvauksen, vaikka RBF:ää ei alun perin olisikaan merkitty.

Toisin kuin CPFP (*Child Pays For Parent*), jossa vastaanottaja voi toimia nopeuttaakseen transaktiota, RBF (*Replace-By-Fee*) antaa lähettäjälle mahdollisuuden ottaa aloite omien transaktioidensa nopeuttamiseen korottamalla kuluja.