---
term: SECP256K1

---
Nimi tietylle elliptiselle käyrälle, jota käytetään Bitcoin-protokollassa ECDSA- (*Elliptic Curve Digital Signature Algorithm*) ja Schnorr-digitaalisen allekirjoitusalgoritmin toteuttamiseen. Bitcoinin keksijä Satoshi Nakamoto valitsi "secp256k1"-käyrän. Sillä on joitakin mielenkiintoisia ominaisuuksia, erityisesti suorituskykyetuja.

`secp256k1`:n käyttö Bitcoinissa tarkoittaa, että jokainen yksityinen avain (satunnainen 256-bittinen luku) yhdistetään vastaavaan julkiseen avaimeen lisäämällä ja kaksinkertaistamalla yksityisen avaimen piste `secp256k1`-käyrän generaattoripisteellä. Tämä operaatio on helppo suorittaa yhteen suuntaan, mutta käytännössä mahdotonta kääntää, mikä on Bitcoinin digitaalisten allekirjoitusten turvallisuuden perusta.

Käyrä `secp256k1` on määritelty elliptisen käyrän yhtälöllä $y^2 = x^3 + 7$, mikä tarkoittaa, että sen kertoimet $a$ ovat $0$ ja $b$ $7$ elliptisen käyrän yhtälön yleisessä muodossa $y^2 = x^3 + ax + b$. `secp256k1` on määritelty äärellisessä kentässä, jonka järjestysluku on hyvin suuri alkuluku, tarkemmin sanottuna $p = 2^{256} - 2^{32} - 977$. Käyrällä on myös ryhmäjärjestys, joka on käyrän erillisten pisteiden lukumäärä, ennalta määritelty generaattoripiste (tai piste $G$), jota käytetään kryptografisissa operaatioissa avainparien tuottamiseen, ja kofaktori, joka on yhtä suuri kuin $1$.

> ► *"SEC" tarkoittaa "Standards for Efficient Cryptography". "P256" tarkoittaa, että käyrä on määritelty kentässä $\mathbb{Z}_p$, jossa $p$ on 256-bittinen alkuluku. "K" viittaa sen keksijän Neal Koblitzin nimeen. Lopuksi "1" tarkoittaa, että tämä on tämän käyrän ensimmäinen versio.*