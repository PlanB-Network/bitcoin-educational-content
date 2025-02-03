---
term: ASICBOOST

---
ASICBOOST on vuonna 2016 keksitty algoritminen optimointimenetelmä, joka on suunniteltu lisäämään Bitcoin-louhinnan tehokkuutta noin 20 prosentilla vähentämällä kunkin otsikon hash-yrityksen edellyttämien laskutoimitusten määrää. Tässä tekniikassa hyödynnetään louhinnassa käytettävän SHA256-hash-funktion ominaisuutta, joka jakaa tiedot lohkoihin ennen niiden käsittelyä. ASICBOOST säilyttää yhden näistä lohkoista muuttumattomana useiden hashausyritysten aikana, jolloin louhijan on tehtävä vain osa tämän lohkon työstä useiden yritysten aikana. Tämä tietojen jakaminen mahdollistaa aiempien laskutoimitusten tulosten uudelleenkäytön, mikä vähentää kelvollisen hash-tunnisteen löytämiseen tarvittavien laskutoimitusten kokonaismäärää.

ASICBOOSTia voidaan käyttää kahdessa muodossa: Overt ASICBOOST ja Covert ASICBOOST. Overt ASICBOOST -muoto on kaikkien nähtävissä, koska siinä käytetään lohkon `nVersion`-kenttää nonce-kenttänä eikä todellista `Nonce`-kenttää muuteta. Covert-muodossa nämä muutokset pyritään piilottamaan käyttämällä Merkle-puita. Tämä toinen menetelmä on kuitenkin heikentynyt SegWitin käyttöönoton jälkeen, koska toinen Merkle-puu lisää sen käyttämiseen tarvittavien laskutoimitusten määrää.

Yhteenvetona voidaan todeta, että ASICBOOSTin ansiosta kaivostyöläisten ei tarvitse suorittaa todellista täydellistä SHA256-määritystä kaikkien hakkerointiyritysten osalta, sillä osa tuloksesta pysyy muuttumattomana, mikä nopeuttaa kaivostyöläisten työtä.