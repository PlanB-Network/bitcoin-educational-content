---
term: PBKDF2
---

`PBKDF2` staat voor *Password-Based Key Derivation Function 2*. Het is een methode om cryptografische sleutels te maken van een wachtwoord met behulp van een afleidingsfunctie. Het neemt als invoer een wachtwoord, een cryptografische salt en past iteratief een vooraf bepaalde functie toe (vaak een Hash functie zoals `SHA256` of een `HMAC`) op deze gegevens. Dit proces wordt vele malen herhaald om generate een cryptografische sleutel te maken.


In de context van Bitcoin wordt `PBKDF2` gebruikt in combinatie met de `HMAC-SHA512` functie om de seed van een deterministische en hiërarchische Wallet (seed) te maken van een herstelzin van 12 of 24 woorden. De cryptografische salt die in dit geval wordt gebruikt is de BIP39 passphrase en het aantal iteraties is `2048`.