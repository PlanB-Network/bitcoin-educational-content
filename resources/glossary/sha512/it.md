---
termine: SHA512
---

Acronimo di "*Secure Hash Algorithm 512 bits*". Si tratta di una funzione di hash crittografico che produce un digest di 512 bit. È stata progettata dalla *National Security Agency* (NSA) nei primi anni 2000. Per Bitcoin, la funzione `SHA512` non viene utilizzata direttamente all'interno del protocollo, ma viene impiegata nel contesto della derivazione di chiavi figlie a livello applicativo, secondo BIP32 e BIP39. In questi processi, viene utilizzata più volte nell'algoritmo `HMAC`, così come nella funzione di derivazione chiave `PBKDF2`. La funzione `SHA512` fa parte della famiglia SHA 2, come `SHA256`. Il suo funzionamento è molto simile a quest'ultimo.