---
term: PAKATTU JULKINEN AVAIN

---
Julkista avainta käytetään skripteissä (joko suoraan julkisen avaimen tai osoitteen muodossa) bitcoinien vastaanottamiseen ja suojaamiseen. Raakaa julkista avainta edustaa elliptisen käyrän piste, joka koostuu kahdesta koordinaatista (`x, y`), joiden kummankin pituus on 256 bittiä. Raakamuodossa julkisen avaimen koko on siis 512 bittiä, kun ei oteta huomioon ylimääräistä tavua muodon tunnistamiseksi. Pakattu julkinen avain on puolestaan kompaktimpi julkisen avaimen esitysmuoto. Siinä käytetään vain `x`-koordinaattia ja etuliitettä (`02` tai `03`), joka ilmaisee `y`-koordinaatin pariteetin (parillinen tai pariton).

Jos yksinkertaistamme tämän reaalilukujen kenttään, elliptisen käyrän ollessa symmetrinen x-akselin suhteen, on olemassa piste $P$ (`x, y`), joka on samalla käyrällä, ja piste $P'$ (`x, -y`), joka on myös samalla käyrällä. Tämä tarkoittaa, että jokaiselle `x`:lle on vain kaksi mahdollista arvoa `y`:lle, positiivinen ja negatiivinen. Esimerkiksi tietyllä absissalla `x` elliptisellä käyrällä on kaksi pistettä $P1$ ja $P2$, joilla on sama absissa mutta vastakkaiset ordinaatit:

![](../../dictionnaire/assets/29.webp)

Jos halutaan valita käyrän kahden mahdollisen pisteen välillä, "x"-arvoon lisätään etuliite, joka määrittää, mikä "y"-piste valitaan. Tällä menetelmällä voidaan pienentää julkisen avaimen kokoa 520 bitistä vain 264 bittiin (8 bittiä etuliitettä + 256 bittiä `x`:lle). Tätä esitystapaa kutsutaan julkisen avaimen pakatuksi muodoksi.

Elliptisen käyrän kryptografiassa ei kuitenkaan käytetä reaalilukuja, vaan äärellistä kenttää, jonka järjestys on `p` (alkuluku). Tässä yhteydessä `y`:n "merkki" määräytyy sen pariteetin mukaan, eli onko `y` parillinen vai pariton. Etuliite `0x02` tarkoittaa siis parillista `y`, kun taas `0x03` tarkoittaa paritonta `y`.

Tarkastellaan seuraavaa esimerkkiä raa'asta julkisesta avaimesta (elliptisen käyrän pisteestä) heksadesimaalisessa muodossa:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Voimme eristää etuliitteet `x` ja `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Perus 16 (heksadesimaaliluku): f

Perus 10 (desimaaliluku): 15

y on pariton

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```