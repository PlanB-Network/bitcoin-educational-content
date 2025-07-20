---
term: SECP256R1
---

Ime dato eliptičnoj krivi definisanoj NIST standardom za kriptografiju javnog ključa. Koristi prostorno polje od 256 bita i jednačinu eliptične krive $y^2 = x^3 + ax + b$ sa konstantama:


```text
a = -3
```


i


```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```


Kriva `secp256r1` je široko korišćena u mnogim protokolima, ali se ne koristi u Bitcoin. Naime, Satoshi Nakamoto se odlučio za krivu `secp256k1`, koja je tada bila malo poznata 2009. godine. Tačan razlog za ovaj izbor nije poznat, ali je možda bio da se minimizuje rizik od backdoor-a. Parametri krive $k1$ su zaista mnogo jednostavniji od onih krive $r1$, posebno konstanta $b$.


> ► *Ova kriva se ponekad naziva i "P-256".*