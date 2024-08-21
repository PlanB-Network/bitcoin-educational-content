---
termi: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Tekee transaktion mitättömäksi, ellei kaikkia näitä ehtoja täytetä:
* Pino ei ole tyhjä;
* Pinon päällimmäisen arvo on suurempi tai yhtä suuri kuin `0`;
* Aikalukon tyyppi on sama sekä `nLockTime`-kentässä että pinon päällimmäisessä arvossa (todellinen aika tai lohkon numero);
* Syötteen `nSequence`-kenttä ei ole yhtä suuri kuin `0xffffffff`;
* Pinon päällimmäisen arvo on suurempi tai yhtä suuri kuin transaktion `nLockTime`-kentän arvo.

Jos jokin näistä ehdoista ei täyty, skripti, joka sisältää `OP_CHECKLOCKTIMEVERIFY`:n, ei voi tulla täytetyksi. Jos kaikki nämä ehdot ovat voimassa, `OP_CHECKLOCKTIMEVERIFY` toimii kuin `OP_NOP`, mikä tarkoittaa, että se ei suorita mitään toimintoa skriptissä. Se on kuin se katoaisi. `OP_CHECKLOCKTIMEVERIFY` asettaa siis aikarajoituksen UTXO:n käyttämiselle, joka on turvattu sitä sisältävällä skriptillä. Se voi tehdä tämän joko Unix-ajan päivämäärän tai lohkon numeron muodossa. Tämän vuoksi se rajoittaa mahdollisia arvoja transaktion `nLockTime`-kentässä, joka sitä käyttää, ja tämä `nLockTime`-kenttä itsessään rajoittaa, milloin transaktio voidaan sisällyttää lohkoon.

> ► *Tämä operaatiokoodi on korvaaja `OP_NOP`:lle. Se sijoitettiin `OP_NOP2`:een. Sitä kutsutaan usein lyhenteellään "CLTV". Huomaa, että `OP_CLTV`:tä ei tule sekoittaa transaktion `nLockTime`-kenttään. Edellinen käyttää jälkimmäistä, mutta niiden luonteet ja toiminnot ovat erilaiset.*