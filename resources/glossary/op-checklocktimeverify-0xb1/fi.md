---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Tekee tapahtumasta pätemättömän, elleivät kaikki nämä ehdot täyty:


- Pino ei ole tyhjä;
- Arvo pinon yläreunassa on suurempi tai yhtä suuri kuin `0`;
- Aikasulun tyyppi on sama `nLockTime`-kentän ja pinon yläosassa olevan arvon välillä (reaaliaika tai lohkon numero);
- Syötteen `nSequence`-kenttä ei ole yhtä suuri kuin `0xffffffffffff`;
- Pinon yläosassa oleva arvo on suurempi tai yhtä suuri kuin tapahtuman `nLockTime`-kentän arvo.

Jos jokin näistä ehdoista ei täyty, `OP_CHECKLOCKTIMEVERIFY`-ohjelman sisältävää komentosarjaa ei voida täyttää. Jos kaikki nämä ehdot täyttyvät, `OP_CHECKLOCKTIMEVERIFY` toimii `OP_NOP`:na, eli se ei tee mitään toimenpiteitä skriptille. Se ikään kuin katoaa. `OP_CHECKLOCKTIMEVERIFY` asettaa siis aikarajoituksen UTXO:n ja sen sisältävän skriptin välille. Se voi tehdä tämän joko Unix-aikapäivämäärän tai lohkonumeron muodossa. Tätä varten se rajoittaa sitä käyttävän transaktion `nLockTime`-kentän mahdollisia arvoja, ja tämä `nLockTime`-kenttä itse rajoittaa sitä, milloin transaktio voidaan sisällyttää lohkoon.

> ► *Tämä op-koodi korvaa koodin `OP_NOP`. Se on sijoitettu `OP_NOP2`:n tilalle. Siihen viitataan usein lyhenteellä "CLTV". Huomaa, että `OP_CLTV` ei pidä sekoittaa transaktion `nLockTime`-kenttään. Ensin mainittu käyttää jälkimmäistä, mutta niiden luonne ja toiminta on erilainen.*