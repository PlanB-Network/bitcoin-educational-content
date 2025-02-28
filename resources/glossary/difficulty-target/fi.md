---
term: VAIKEUSTAVOITE

---
Vaikeuskerroin, joka tunnetaan myös nimellä vaikeuskohde, on parametri, jota käytetään Bitcoinin konsensusmekanismissa todisteellisella työllä (Proof of Work, PoW). Tavoite edustaa numeerista arvoa, joka määrittää, kuinka vaikeaa louhijoiden on ratkaista tietty kryptografinen ongelma, jota kutsutaan todisteeksi työstä, luodessaan uutta lohkoa lohkoketjuun.

Vaikeustavoite on säädettävä 256-bittinen (64 tavua) luku, joka määrittää hyväksyttävän rajan lohko-otsikoiden hakkeroinnille. Toisin sanoen, jotta lohko olisi kelvollinen, sen otsikon hash-arvon `SHA256d`:llä (kaksinkertainen `SHA256`) on oltava numeerisesti pienempi tai yhtä suuri kuin vaikeustavoite. Työn todentaminen koostuu lohko-otsikon tai coinbase-transaktion `nonce`-kentän muuttamisesta, kunnes tuloksena oleva hash on pienempi kuin tavoitearvo.

Tätä tavoitetta mukautetaan vuoden 2016 lohkojen välein (noin kahden viikon välein) tapahtuman nimeltä "mukautus" aikana Vaikeuskerroin lasketaan uudelleen sen ajan perusteella, joka kului edellisen vuoden 2016 lohkojen louhimiseen. Jos kokonaisaika on alle kaksi viikkoa, vaikeusaste kasvaa säätämällä tavoitetta alaspäin. Jos kokonaisaika on yli kaksi viikkoa, vaikeusaste laskee säätämällä tavoitetta ylöspäin. Tavoitteena on säilyttää keskimääräinen louhinta-aika 10 minuutissa lohkoa kohti. Tämä lohkojen välinen aika auttaa estämään Bitcoin-verkon jakautumisen, mikä johtaa laskentatehon tuhlaamiseen. Vaikeustavoite löytyy kunkin lohkon otsikosta, `nBits`-kentästä. Koska tämä kenttä on pienennetty 32 bittiin ja tavoite on itse asiassa 256 bittiä, tavoite on tiivistetty epätarkempaan tieteelliseen muotoon.

![](../../dictionnaire/assets/34.webp)

> ► * Vaikeustavoitetta kutsutaan joskus myös "vaikeustekijäksi" Laajennuksena siihen voidaan viitata sen koodauksen kanssa lohko-otsikoissa termillä "nBits" *