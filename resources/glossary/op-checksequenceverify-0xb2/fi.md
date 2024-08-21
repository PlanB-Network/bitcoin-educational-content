---
termi: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Tekee transaktiosta kelvottoman, jos havaitaan jokin seuraavista ominaisuuksista:
* Pino on tyhjä;
* Pinon päällimmäisen arvo on pienempi kuin `0`;
* Pinon päällimmäisen arvon poistokytkin on määrittelemätön ja; Transaktion versio on pienempi kuin `2` tai; Syötteen `nSequence`-kentän poistokytkin on asetettu tai; Aikalukon tyyppi ei ole sama `nSequence`-kentän ja pinon päällimmäisen arvon välillä (oikea aika tai lohkojen määrä) tai; Pinon päällimmäinen arvo on suurempi kuin syötteen `nSequence`-kentän arvo.

Jos yksi tai useampi näistä ominaisuuksista havaitaan, skripti, joka sisältää `OP_CHECKSEQUENCEVERIFY`-käskyn, ei voi täyttyä. Jos kaikki ehdot ovat voimassa, `OP_CHECKSEQUENCEVERIFY` toimii kuin `OP_NOP`, mikä tarkoittaa, että se ei suorita mitään toimintoa skriptissä. Se on kuin se katoaisi. `OP_CHECKSEQUENCEVERIFY` asettaa siis suhteellisen aikarajoituksen skriptillä turvatun UTXO:n käyttämiselle. Se voi tehdä tämän joko oikean ajan muodossa tai lohkojen määränä. Tämän vuoksi se rajoittaa mahdollisia arvoja syötteen `nSequence`-kentälle, joka käyttää sitä, ja tämä `nSequence`-kenttä itse rajoittaa, milloin transaktio, joka sisältää tämän syötteen, voidaan sisällyttää lohkoon.

> ► *Tämä operaatiokoodi on korvaaja `OP_NOP`:lle. Se sijoitettiin `OP_NOP3`:een. Sitä kutsutaan usein lyhenteellään "CSV". Huomaa, että `OP_CSV` ei tule sekoittaa transaktion `nSequence`-kenttään. Edellinen käyttää jälkimmäistä, mutta niiden luonteet ja toiminnot ovat erilaiset.*