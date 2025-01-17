---
term: SECP256R1

---
NIST:n julkisen avaimen salausstandardissa määritellylle elliptiselle käyrälle annettu nimi. Siinä käytetään 256 bitin prime-kenttää ja elliptisen käyrän yhtälöä $y^2 = x^3 + ax + b$, jossa on vakiot:

```text
a = -3
```

ja

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Käyrää `secp256r1` käytetään laajalti monissa protokollissa, mutta sitä ei käytetä Bitcoinissa. Satoshi Nakamoto valitsikin käyrän `secp256k1`, joka oli silloin vuonna 2009 vielä vähän tunnettu. Tarkkaa syytä tähän valintaan ei tiedetä, mutta se saattoi johtua takaovien riskin minimoimisesta. $k1$-käyrän parametrit ovat todellakin paljon yksinkertaisemmat kuin $r1$-käyrän parametrit, erityisesti vakio $b$.

> ► *Tätä käyrää kutsutaan joskus myös nimellä "P-256".*