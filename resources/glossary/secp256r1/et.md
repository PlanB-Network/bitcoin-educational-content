---
term: SECP256R1

---
Nimi, mis on antud elliptilisele kõverale, mis on määratletud NISTi avaliku võtme krüptograafia standardis. See kasutab 256-bitist primaarvälja ja elliptilise kõvera võrrandit $y^2 = x^3 + ax + b$ koos konstantidega:

```text
a = -3
```

ja

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Kõverat `secp256r1` kasutatakse laialdaselt paljudes protokollides, kuid seda ei kasutata Bitcoinis. Satoshi Nakamoto valis 2009. aastal vähetuntud kõvera `secp256k1`. Selle valiku täpne põhjus on teadmata, kuid see võis olla tagauste riski minimeerimine. $k1$ kõvera parameetrid on tõepoolest palju lihtsamad kui $r1$ kõvera omad, eriti konstant $b$.

> ► *Seda kõverat nimetatakse mõnikord ka "P-256".*