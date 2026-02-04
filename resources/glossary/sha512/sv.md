---
term: SHA512
definition: Kryptografisk hashfunktion som producerar ett 512-bitars sammandrag, används för härledningar.
---

Akronym för "*Secure Hash Algorithm 512 bits*". Det är en kryptografisk Hash-funktion som producerar ett 512-bitars digest. Den utformades av *National Security Agency* (NSA) i början av 2000-talet. För Bitcoin används inte funktionen `SHA512` direkt i protokollet, men den används i samband med att underordnade nycklar härleds på applikationsnivå, enligt BIP32 och BIP39. I dessa processer används den flera gånger i algoritmen `HMAC` samt i funktionen `PBKDF2` för härledning av nycklar. Funktionen `SHA512` ingår i SHA 2-familjen, precis som `SHA256`. Dess funktion är mycket lik den sistnämnda.