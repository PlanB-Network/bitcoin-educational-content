---
term: SHA512

---
Acronimo di "*Secure Hash Algorithm 512 bits*". È una funzione di hash crittografico che produce un digest di 512 bit. È stata progettata dalla *National Security Agency* (NSA) nei primi anni 2000. Per Bitcoin, la funzione `SHA512` non viene utilizzata direttamente all'interno del protocollo, ma viene utilizzata nel contesto della derivazione delle chiavi figlio a livello di applicazione, secondo BIP32 e BIP39. In questi processi, viene utilizzata più volte nell'algoritmo `HMAC` e nella funzione di derivazione delle chiavi `PBKDF2`. La funzione `SHA512` fa parte della famiglia SHA 2, come `SHA256`. Il suo funzionamento è molto simile a quest'ultimo.