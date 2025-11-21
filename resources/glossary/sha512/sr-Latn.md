---
term: SHA512
---

Akronim za "*Secure Hash Algorithm 512 bits*". To je kriptografska Hash funkcija koja proizvodi 512-bitni sažetak. Dizajnirana je od strane *National Security Agency* (NSA) početkom 2000-ih. Za Bitcoin, funkcija `SHA512` se ne koristi direktno unutar protokola, ali se koristi u kontekstu derivacije podključeva na nivou aplikacije, prema BIP32 i BIP39. U ovim procesima, koristi se više puta u `HMAC` algoritmu, kao i u `PBKDF2` funkciji za derivaciju ključeva. Funkcija `SHA512` je deo SHA 2 porodice, kao i `SHA256`. Njeno delovanje je veoma slično potonjem.