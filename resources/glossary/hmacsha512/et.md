---
term: HMAC-SHA512
---

`HMAC-SHA512` tähistab "Hash-based Message Authentication Code - Secure Hash Algorithm 512". See on krüptograafiline algoritm, mida kasutatakse sõnumite vahetamisel kahe osapoole vahel nende terviklikkuse ja autentsuse kontrollimiseks. See ühendab krüptograafilise räsifunktsiooni `SHA512` jagatud salajase võtmega, et genereerida iga sõnumi jaoks unikaalne sõnumi autentimiskood (MAC).

Bitcoin'i kontekstis on `HMAC-SHA512` kasutus natuke erinev. Seda algoritmi kasutatakse krüptograafilise võtmepuu deterministlikus ja hierarhilises tuletusprotsessis rahakotis. `HMAC-SHA512` on eriti kasutusel seemnest peamise võtmeni liikumisel ja seejärel iga tuletuse puhul vanemapaarilt lastepaaridele. Seda algoritmi leidub ka teises tuletusalgoritmis nimega `PBKDF2`, mida kasutatakse taastefraasi ja paroolifraasi seemneks muutmiseks.