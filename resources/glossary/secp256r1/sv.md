---
term: SECP256R1
definition: Elliptisk kurva av NIST-standard, som inte används av Bitcoin som föredrar secp256k1.
---

Namn på en elliptisk kurva som definieras av NIST-standarden för kryptografi med offentlig nyckel. Den använder ett primfält på 256 bitar och en elliptisk kurveekvation $y^2 = x^3 + ax + b$ med konstanterna:


```text
a = -3
```


och


```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```


Kurvan `secp256r1` används ofta i många protokoll, men den används inte i Bitcoin. I Satoshi valde Nakamoto istället kurvan `secp256k1`, som då 2009 var föga känd. Det exakta skälet till detta val är okänt, men det kan ha varit att minimera risken för bakdörrar. Parametrarna för $ k1 $ -kurvan är verkligen mycket enklare än de för $ r1 $ -kurvan, särskilt konstanten $ b $.


> ► *Den här kurvan kallas ibland också "P-256".*