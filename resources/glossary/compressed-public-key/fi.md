---
term: TIIVISTETTY JULKINEN AVAIN
---

Julkista avainta käytetään skripteissä (joko suoraan julkisen avaimen muodossa tai osoitteena) vastaanottamaan ja turvaamaan bitcoineja. Raaka julkinen avain esitetään pisteenä elliptisellä käyrällä, joka koostuu kahdesta koordinaatista (`x, y`), kumpikin 256 bittiä. Raakamuodossa julkinen avain on siis 512 bittiä pitkä, formaatin tunnistavaa lisäbittiä ei lasketa mukaan. Tiivistetty julkinen avain sen sijaan on tiiviimpi muoto julkisen avaimen esittämiseen. Se käyttää vain `x`-koordinaattia ja etuliitettä (`02` tai `03`), joka ilmaisee `y`-koordinaatin pariteetin (parillinen tai pariton).

Jos yksinkertaistamme tämän reaalilukujen alueelle, ottaen huomioon, että elliptinen käyrä on symmetrinen x-akselin suhteen, jokaiselle pisteelle $P$ (`x, y`) käyrällä on olemassa piste $P'$ (`x, -y`), joka myös sijaitsee samalla käyrällä. Tämä tarkoittaa, että jokaiselle `x`:lle on vain kaksi mahdollista `y`-arvoa, positiivinen ja negatiivinen. Esimerkiksi annetulle abskissalle `x` olisi kaksi pistettä $P1$ ja $P2$ elliptisellä käyrällä, jotka jakavat saman abskissan, mutta niillä on vastakkaiset ordinaatat:

![](../../dictionnaire/assets/29.png)
Valitakseen kahden mahdollisen pisteen välillä käyrällä, `x`:ään lisätään etuliite, joka määrittää, kumman `y`:n valita. Tämä menetelmä mahdollistaa julkisen avaimen koon pienentämisen 520 bitistä vain 264 bittiin (8 bitin etuliite + 256 bittiä `x`:lle). Tätä esitystapaa kutsutaan julkisen avaimen tiivistetyksi muodoksi.

Kuitenkin elliptisen käyrän kryptografiassa emme käytä reaalilukuja, vaan äärellistä kenttää järjestyksessä `p` (alkuluku). Tässä yhteydessä `y`:n "merkki" määräytyy sen pariteetin perusteella, eli onko `y` parillinen vai pariton. Etuliite `0x02` ilmaisee tällöin parillisen `y`:n, kun taas `0x03` ilmaisee parittoman `y`:n.

Harkitse seuraavaa esimerkkiä raakajulkisesta avaimesta (piste elliptisellä käyrällä) heksadesimaalimuodossa:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Voimme erottaa etuliitteen, `x`:n ja `y`:n:
```plaintext
Etuliite = 04
`y`:n pariteetin määrittämiseksi tarkastelemme `y`:n viimeistä heksadesimaalimerkkiä:
```plaintext
Base 16 (heksadesimaali): f
Base 10 (desimaali): 15
y on pariton
```

Tiivistetyn julkisen avaimen etuliite on `03`. Tiivistetty julkinen avain heksadesimaalimuodossa tulee olemaan:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```