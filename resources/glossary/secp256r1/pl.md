---
term: SECP256R1
---

Nazwa nadana krzywej eliptycznej zdefiniowanej przez standard NIST dla kryptografii klucza publicznego. Wykorzystuje ona pole pierwsze 256 bitów i równanie krzywej eliptycznej $y^2 = x^3 + ax + b$ ze stałymi:


```text
a = -3
```


oraz


```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```


Krzywa `secp256r1` jest szeroko stosowana w wielu protokołach, ale nie jest używana w Bitcoin. Rzeczywiście, w Satoshi Nakamoto zdecydował się na krzywą `secp256k1`, która była wówczas mało znana w 2009 roku. Dokładny powód tego wyboru nie jest znany, ale być może chodziło o zminimalizowanie ryzyka backdoorów. Parametry krzywej $k1$ są rzeczywiście znacznie prostsze niż parametry krzywej $r1$, zwłaszcza stała $b$.


> krzywa ta jest czasami nazywana również "P-256"