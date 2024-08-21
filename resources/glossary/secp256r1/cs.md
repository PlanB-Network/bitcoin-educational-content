---
term: SECP256R1
---

Název daný eliptické křivce definované standardem NIST pro veřejný klíčový kryptosystém. Používá prvotní pole o velikosti 256 bitů a rovnici eliptické křivky $y^2 = x^3 + ax + b$ s konstantami:

```text
a = -3
```

a

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Křivka `secp256r1` je široce používána v mnoha protokolech, ale v Bitcoinu použita není. Satoshi Nakamoto skutečně zvolil křivku `secp256k1`, která byla v roce 2009 málo známá. Přesný důvod této volby není znám, ale mohlo to být kvůli minimalizaci rizika zadních vrátek. Parametry křivky $k1$ jsou skutečně mnohem jednodušší než parametry křivky $r1$, zejména konstanta $b$.

> ► *Tato křivka je někdy také nazývána "P-256".*