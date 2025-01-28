---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Tekee tapahtuman mitättömäksi, jos jokin näistä ominaisuuksista havaitaan:


- Pino on tyhjä;
- Arvo pinon yläosassa on pienempi kuin `0`;
- Pinon yläreunassa olevan arvon deaktivointilippu on määrittelemätön ja; tapahtuman versio on pienempi kuin `2` tai; syötteen `nSequence`-kentän deaktivointilippu on asetettu tai; timelock-tyyppi ei ole sama `nSequence`-kentän ja pinon yläreunassa olevan arvon välillä (reaaliaika tai lohkojen lukumäärä) tai; pinon yläreunassa oleva arvo on suurempi kuin syötteen `nSequence`-kentän arvo.

Jos yksi tai useampi näistä ominaisuuksista havaitaan, `OP_CHECKSEQUENCEVERIFY`-ohjelman sisältävää komentosarjaa ei voida täyttää. Jos kaikki ehdot ovat voimassa, `OP_CHECKSEQUENCEVERIFY` toimii `OP_NOP`:na, eli se ei tee mitään toimenpiteitä skriptille. Se ikään kuin katoaa. `OP_CHECKSEQUENCEVERIFY` asettaa siis suhteellisen aikarajoituksen UTXO:n ja sen sisältävän skriptin väliselle käytölle. Se voi tehdä tämän joko reaaliaikana tai lohkojen lukumääränä. Tätä varten se rajoittaa sen käyttämän syötteen `nSequence`-kentän mahdollisia arvoja, ja tämä `nSequence`-kenttä itse rajoittaa sitä, milloin tapahtuma, joka sisältää tämän syötteen, voidaan sisällyttää lohkoon.

> ► *Tämä op-koodi korvaa koodin `OP_NOP`. Se on sijoitettu `OP_NOP3`:n tilalle. Siihen viitataan usein lyhenteellä "CSV". Huomaa, että `OP_CSV` ei pidä sekoittaa transaktion `nSequence`-kenttään. Ensin mainittu käyttää jälkimmäistä, mutta niiden luonne ja toiminta on erilainen.*