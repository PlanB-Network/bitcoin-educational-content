---
term: HMAC-SHA512

---
`HMAC-SHA512` tähendab "Hash-based Message Authentication Code - Secure Hash Algorithm 512". See on krüptograafiline algoritm, mida kasutatakse kahe osapoole vahel vahetatud sõnumite terviklikkuse ja autentsuse kontrollimiseks. See kombineerib krüptograafilise hash-funktsiooni "SHA512" ja jagatud salajase võtme, et genereerida iga sõnumi jaoks unikaalne sõnumi autentimise kood (MAC).

Bitcoini kontekstis on `HMAC-SHA512` loomulik kasutamine veidi tuletatud. Seda algoritmi kasutatakse rahakoti krüptograafilise võtmepuu deterministlikus ja hierarhilises tuletamisprotsessis. `HMAC-SHA512`t kasutatakse eelkõige selleks, et minna seemnest peavõti ja seejärel iga tuletamise puhul vanempaarist lapspaarini. Seda algoritmi kasutatakse ka teises tuletamisalgoritmis nimega `PBKDF2`, mida kasutatakse taastamisfraasist ja salasõnast seemneni jõudmiseks.