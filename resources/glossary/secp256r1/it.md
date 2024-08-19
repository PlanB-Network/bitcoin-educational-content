Nome dato a una curva ellittica definita dallo standard NIST per la crittografia a chiave pubblica. Utilizza un campo primo di 256 bit e un'equazione di curva ellittica $y^2 = x^3 + ax + b$ con le costanti:

```text
a = -3
```

e

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

La curva `secp256r1` è ampiamente utilizzata in molti protocolli, ma non è utilizzata in Bitcoin. Infatti, Satoshi Nakamoto ha optato per la curva `secp256k1`, che allora era poco conosciuta nel 2009. La ragione precisa di questa scelta è sconosciuta, ma potrebbe essere stata per minimizzare il rischio di backdoor. I parametri della curva $k1$ sono infatti molto più semplici di quelli della curva $r1$, specialmente la costante $b$.

> ► *Questa curva è talvolta chiamata anche "P-256".*