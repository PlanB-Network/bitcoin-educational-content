---
term: SHA512

---
Forkortelse for "*Secure Hash Algorithm 512 bits*". Det er en kryptografisk hash-funksjon som produserer et 512-biters sammendrag. Den ble utviklet av *National Security Agency* (NSA) på begynnelsen av 2000-tallet. I Bitcoin brukes ikke "SHA512"-funksjonen direkte i protokollen, men den brukes i forbindelse med utledning av underordnede nøkler på applikasjonsnivå, i henhold til BIP32 og BIP39. I disse prosessene brukes den flere ganger i `HMAC`-algoritmen, samt i `PBKDF2`-nøkkelderiveringsfunksjonen. `SHA512`-funksjonen er en del av SHA 2-familien, i likhet med `SHA256`. Den fungerer på samme måte som sistnevnte.