---
term: PBKDF2
definition: Funktion för att härleda kryptografiska nycklar från ett lösenord genom iterationer.
---

`PBKDF2` står för *Password-Based Key Derivation Function 2*. Det är en metod för att skapa kryptografiska nycklar från ett lösenord med hjälp av en härledningsfunktion. Den tar som indata ett lösenord, ett kryptografiskt salt och tillämpar iterativt en förutbestämd funktion (ofta en Hash-funktion som `SHA256` eller en `HMAC`) på dessa data. Denna process upprepas många gånger för att generate en kryptografisk nyckel.


I samband med Bitcoin används `PBKDF2` tillsammans med funktionen `HMAC-SHA512` för att skapa seed av en deterministisk och hierarkisk Wallet (seed) från en återställningsfras med 12 eller 24 ord. Det kryptografiska salt som används i detta fall är BIP39 passphrase och antalet iterationer är `2048`.