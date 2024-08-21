---
term: PBKDF2
---

`PBKDF2` tähistab *Password-Based Key Derivation Function 2* ehk paroolipõhist võtmegeneratsiooni funktsiooni 2. See on meetod krüptograafiliste võtmete loomiseks paroolist, kasutades tuletusfunktsiooni. Sisendina võetakse parool, krüptograafiline sool ja iteratiivselt rakendatakse eelnevalt määratud funktsiooni (tihti hash-funktsioon nagu `SHA256` või `HMAC`) nendele andmetele. See protsess korratakse palju kordi, et genereerida krüptograafiline võti.

Bitcoin'i kontekstis kasutatakse `PBKDF2` koos `HMAC-SHA512` funktsiooniga, et luua deterministliku ja hierarhilise rahakoti (seemne) seeme 12 või 24 sõnast koosneva taastefraasi põhjal. Sel juhul kasutatav krüptograafiline sool on BIP39 paroolifraas ja iteratsioonide arv on `2048`.