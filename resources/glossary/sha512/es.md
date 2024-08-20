---
term: SHA512
---

Acrónimo de "*Secure Hash Algorithm 512 bits*" (Algoritmo de Hash Seguro de 512 bits). Es una función de hash criptográfico que produce un resumen de 512 bits. Fue diseñado por la *Agencia de Seguridad Nacional* (NSA) a principios de los años 2000. Para Bitcoin, la función `SHA512` no se utiliza directamente dentro del protocolo, pero se usa en el contexto de derivación de claves secundarias a nivel de aplicación, según BIP32 y BIP39. En estos procesos, se utiliza múltiples veces en el algoritmo `HMAC`, así como en la función de derivación de clave `PBKDF2`. La función `SHA512` es parte de la familia SHA 2, al igual que `SHA256`. Su operación es muy similar a la de este último.