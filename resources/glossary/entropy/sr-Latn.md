---
term: ENTROPIJA
---

Entropija, u kontekstu kriptografije i informacija, je kvantitativna mera nesigurnosti ili nepredvidljivosti povezane sa izvorom podataka ili slučajnim procesom. Entropija igra ključnu ulogu u bezbednosti kriptografskih sistema, posebno u generisanju ključeva i slučajnih brojeva. Visoka entropija osigurava da su generisani ključevi dovoljno nepredvidljivi i otporni na napade grube sile, gde napadač pokušava sve moguće kombinacije da pogodi ključ.


U kontekstu Bitcoin, entropija se koristi za generate privatne ključeve ili seed-ove. Kada se kreira deterministički i hijerarhijski Wallet, konstrukcija Mnemonic fraze se vrši iz slučajnog broja, koji je sam izveden iz izvora entropije. Fraza se zatim koristi za generate više privatnih ključeva, na deterministički i hijerarhijski način, kako bi se kreirali uslovi trošenja na UTXO-ima.


Od suštinskog je značaja imati kvalitetan izvor entropije kako bi se osigurala bezbednost kriptografskih sistema. Izvori entropije mogu biti fizički procesi, kao što su elektronska buka ili toplotne varijacije, ili softverski procesi, kao što su pseudo-slučajni generatori brojeva.