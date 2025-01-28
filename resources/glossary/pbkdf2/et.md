---
term: PBKDF2

---
`PBKDF2` tähistab *Password-Based Key Derivation Function 2*. See on meetod krüptograafiliste võtmete loomiseks paroolist tuletamisfunktsiooni abil. See võtab sisendiks parooli, krüptograafilise soola ja rakendab nende andmete suhtes iteratiivselt eelnevalt määratud funktsiooni (sageli hash-funktsiooni nagu `SHA256` või `HMAC`). Seda protsessi korratakse mitu korda, et genereerida krüptograafiline võti.

Bitcoini kontekstis kasutatakse `PBKDF2` koos `HMAC-SHA512` funktsiooniga, et luua deterministliku ja hierarhilise rahakoti seemne (seemne) 12 või 24 sõnast koosnevast taastamisfraasist. Krüptograafiline sool, mida sel juhul kasutatakse, on BIP39 paroolifraas ja iteratsioonide arv on `2048`.