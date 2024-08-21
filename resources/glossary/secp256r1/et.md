---
term: SECP256R1
---

Nimeks antud elliptiline kõver, mille on defineerinud NIST standard avaliku võtme krüptograafia jaoks. See kasutab 256-bitist primaarvälja ja elliptilise kõvera võrrandit $y^2 = x^3 + ax + b$ koos konstantidega:

```text
a = -3
```

ja

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Kõver `secp256r1` on laialdaselt kasutusel paljudes protokollides, kuid seda ei kasutata Bitcoinis. Tõepoolest, Satoshi Nakamoto valis kõvera `secp256k1`, mis oli 2009. aastal veel vähe tuntud. Täpne põhjus selle valiku taga on teadmata, kuid see võis olla soov minimeerida tagauste riski. $k1$ kõvera parameetrid on tõepoolest palju lihtsamad kui $r1$ kõvera omad, eriti konstant $b$.

> ► *Seda kõverat nimetatakse mõnikord ka "P-256".*