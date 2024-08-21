---
term: DERIVATION
---

Viitab protsessile, kus genereeritakse lapse võtmepaarid (privaatvõti ja avalik võti) ning ahelakood vanemvõtmepaarist (privaatvõti ja avalik võti) deterministlikus ja hierarhilises (HD) rahakotis. See protsess võimaldab harude segmenteerimist ja rahakoti korraldamist erinevatele tasanditele arvukate lapse võtmepaaridega, mida kõiki saab taastada teades ainult baast taastamisinfot (mnemooniline fraas ja võimalik parool). Lapse võtme tuletamiseks kasutatakse `HMAC-SHA512` funktsiooni vanema ahelakoodiga ja vanemvõtme ning 32-bitise indeksi konkatenatsiooniga. On kaks tüüpi tuletisi:
* Tavaline tuletis, mis kasutab `HMAC-SHA512` funktsiooni alusena vanema avalikku võtit;
* Tugevdatud tuletis, mis kasutab `HMAC-SHA512` funktsiooni alusena vanema privaatvõtit;

HMAC-SHA512 tulemus jagatakse kaheks: esimesed 256 bitti saavad lapse võtmeks (privaat- või avalikuks pärast töötlemist läbi ECDSA) ja ülejäänud 256 bitti saavad lapse ahelakoodiks.