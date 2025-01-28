---
term: SECP256R1

---
Navnet på en elliptisk kurve som er definert av NIST-standarden for offentlig nøkkelkryptografi. Den bruker et primfelt på 256 bits og en elliptisk kurvelikning $y^2 = x^3 + ax + b$ med konstantene:

```text
a = -3
```

og

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

Kurven `secp256r1` er mye brukt i mange protokoller, men den brukes ikke i Bitcoin. Satoshi Nakamoto valgte nemlig kurven `secp256k1`, som den gang var lite kjent i 2009. Den nøyaktige årsaken til dette valget er ukjent, men det kan ha vært for å minimere risikoen for bakdører. Parametrene til $k1$-kurven er faktisk mye enklere enn parametrene til $r1$-kurven, spesielt konstanten $b$.

> denne kurven kalles noen ganger også "P-256"