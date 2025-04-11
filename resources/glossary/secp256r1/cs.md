---
term: SECP256R1

---
Název eliptické křivky definované standardem NIST pro kryptografii s veřejným klíčem. Používá pole prvočísel o délce 256 bitů a rovnici eliptické křivky $y^2 = x^3 + ax + b$ s konstantami:

```text
a = -3
```

a

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Křivka `secp256r1` je široce používána v mnoha protokolech, ale v Bitcoinu se nepoužívá. Satoshi Nakamoto se totiž rozhodl pro křivku `secp256k1`, která byla v roce 2009 tehdy málo známá. Přesný důvod této volby není znám, ale možná šlo o snahu minimalizovat riziko zadních vrátek. Parametry křivky $k1$ jsou skutečně mnohem jednodušší než parametry křivky $r1$, zejména konstanta $b$.

> ►Tato křivka se někdy také nazývá "P-256".*