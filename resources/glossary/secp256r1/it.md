---
term: SECP256R1

---
Nome dato a una curva ellittica definita dallo standard NIST per la crittografia a chiave pubblica. Utilizza un campo di primi di 256 bit e l'equazione della curva ellittica $y^2 = x^3 + ax + b$ con le costanti:

```text
a = -3
```

e

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

La curva `secp256r1` è ampiamente utilizzata in molti protocolli, ma non in Bitcoin. Satoshi Nakamoto ha infatti optato per la curva `secp256k1`, allora poco conosciuta nel 2009. Il motivo preciso di questa scelta è sconosciuto, ma potrebbe essere stato quello di minimizzare il rischio di backdoor. I parametri della curva $k1$ sono infatti molto più semplici di quelli della curva $r1$, soprattutto la costante $b$.

> *Questa curva è talvolta denominata anche "P-256"