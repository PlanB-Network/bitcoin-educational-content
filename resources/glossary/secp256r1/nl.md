---
term: SECP256R1
definition: Elliptische curve van de NIST-standaard, niet gebruikt door Bitcoin, dat de voorkeur geeft aan secp256k1.
---

Naam gegeven aan een elliptische curve gedefinieerd door de NIST standaard voor publieke sleutel cryptografie. Het gebruikt een priemveld van 256 bits en een elliptische krommevergelijking $y^2 = x^3 + ax + b$ met de constanten:


```text
a = -3
```


en


```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```


De curve `secp256r1` wordt veel gebruikt in veel protocollen, maar niet in Bitcoin. In Satoshi koos Nakamoto namelijk voor de curve `secp256k1`, die toen in 2009 nog weinig bekend was. De precieze reden voor deze keuze is onbekend, maar het kan zijn dat het was om het risico op backdoors te minimaliseren. De parameters van de $k1$ curve zijn inderdaad veel eenvoudiger dan die van de $r1$ curve, vooral de constante $b$.


> deze curve wordt soms ook "P-256" genoemd