---
termi: VAIKEUSTASO
---

Vaikeustekijä, joka tunnetaan myös nimellä vaikeustaso, on parametri, jota käytetään konsensusmekanismissa työn todistamisen (Proof of Work, PoW) menetelmällä Bitcoinissa. Taso edustaa numeerista arvoa, joka määrittää vaikeuden louhijoille ratkaista tietty kryptografinen ongelma, kutsuttu työn todistamiseksi, luodessaan uutta lohkoa lohkoketjuun.

Vaikeustaso on säädettävä 256-bittinen (64 tavua) numero, joka määrittää hyväksyttävyyden rajan lohkojen otsikoiden hajautukselle. Toisin sanoen, jotta lohko olisi validi, sen otsikon `SHA256d` (kaksois `SHA256`) hajautusarvon on oltava numeerisesti pienempi tai yhtä suuri kuin vaikeustaso. Työn todistaminen koostuu lohkon otsikon `nonce`-kentän tai coinbase-siirron muokkaamisesta, kunnes tuloksena oleva hajautusarvo on pienempi kuin tavoitearvo.

Tätä tasoa säädetään joka 2016 lohkon jälkeen (noin joka kaksi viikkoa), tapahtumassa, jota kutsutaan "säädöksi". Vaikeustekijä lasketaan uudelleen perustuen aikaan, joka kului edellisten 2016 lohkon louhimiseen. Jos kokonaisaika on alle kaksi viikkoa, vaikeus kasvaa säätämällä tasoa alaspäin. Jos kokonaisaika on yli kaksi viikkoa, vaikeus vähenee säätämällä tasoa ylöspäin. Tavoitteena on ylläpitää keskimääräistä louhinta-aikaa 10 minuuttia per lohko. Tämä aika jokaisen lohkon välillä auttaa estämään Bitcoin-verkon jakautumisia, mikä johtaisi laskentatehon hukkaan. Vaikeustaso löytyy jokaisen lohkon otsikosta, `nBits`-kentästä. Koska tämä kenttä on supistettu 32 bittiin ja taso on itse asiassa 256 bittiä, taso tiivistetään vähemmän tarkkaan tieteelliseen muotoon.

![](../../dictionnaire/assets/34.png)

> ► *Vaikeustasoa kutsutaan joskus myös "vaikeustekijäksi". Jatkossa sitä voidaan viitata sen koodauksella lohkojen otsikoissa termillä "nBits".*