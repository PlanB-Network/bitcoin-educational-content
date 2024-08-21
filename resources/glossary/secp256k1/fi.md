---
termi: SECP256K1
---

Nimi, joka on annettu tiettyä elliptistä käyrää varten, jota käytetään Bitcoin-protokollassa ECDSA (*Elliptic Curve Digital Signature Algorithm*) ja Schnorr digitaalisten allekirjoitusalgoritmien toteuttamiseen. `secp256k1` käyrä valittiin Bitcoinin keksijän, Satoshi Nakamoton toimesta. Siinä on joitakin mielenkiintoisia ominaisuuksia, erityisesti suorituskykyhyödyt.

`secp256k1`:n käyttö Bitcoinissa tarkoittaa, että jokainen yksityinen avain (satunnainen 256-bittinen numero) kuvataan vastaavaan julkiseen avaimen kautta yksityisen avaimen pisteen lisäämisen ja kaksinkertaistamisen avulla `secp256k1` käyrän generaattoripisteen toimesta. Tämä operaatio on helppo suorittaa yhteen suuntaan, mutta käytännössä mahdotonta kääntää, mikä muodostaa Bitcoinin digitaalisten allekirjoitusten turvallisuuden perustan.

`secp256k1` käyrä määritellään elliptisen käyrän yhtälöllä $y^2 = x^3 + 7$, mikä tarkoittaa, että sillä on kertoimet $a$ yhtä suuri kuin $0$ ja $b$ yhtä suuri kuin $7$ yleisessä elliptisen käyrän yhtälön muodossa $y^2 = x^3 + ax + b$. `secp256k1` on määritelty äärellisellä kentällä, jonka järjestys on erittäin suuri alkuluku, erityisesti $p = 2^{256} - 2^{32} - 977$. Käyrällä on myös ryhmäjärjestys, joka on käyrän erillisten pisteiden määrä, ennalta määritelty generaattoripiste (tai piste $G$), jota käytetään kryptografisissa operaatioissa avainparien generoimiseen, ja kofaktori yhtä suuri kuin $1$.

> ► *“SEC” tarkoittaa “Standards for Efficient Cryptography”. “P256” osoittaa, että käyrä on määritelty kentän $\mathbb{Z}_p$ yli, missä $p$ on 256-bittinen alkuluku. “K” viittaa sen keksijän, Neal Koblitzin, nimeen. Lopuksi, “1” osoittaa, että tämä on tämän käyrän ensimmäinen versio.*