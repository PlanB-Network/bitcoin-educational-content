---
term: SECP256R1
---

Nimi, joka on annettu elliptiselle käyrälle, jonka on määritellyt NIST-standardi julkisen avaimen kryptografiaa varten. Se käyttää 256 bitin pääkenttää ja elliptisen käyrän yhtälöä $y^2 = x^3 + ax + b$ vakioilla:

```text
a = -3
```

ja

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Käyrää `secp256r1` käytetään laajasti monissa protokollissa, mutta sitä ei käytetä Bitcoinissa. Itse asiassa Satoshi Nakamoto valitsi käyrän `secp256k1`, joka oli tuolloin vuonna 2009 vähän tunnettu. Tarkkaa syytä tähän valintaan ei tiedetä, mutta se on saattanut olla takaporttien riskin minimoimiseksi. $k1$ käyrän parametrit ovat todellakin paljon yksinkertaisemmat kuin $r1$ käyrän, erityisesti vakio $b$.

> ► *Tätä käyrää kutsutaan joskus myös nimellä "P-256".*