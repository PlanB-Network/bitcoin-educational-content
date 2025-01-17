---
term: SHA512

---
Acrónimo de "*Secure Hash Algorithm 512 bits*". Es una función hash criptográfica que produce un compendio de 512 bits. Fue diseñada por la *Agencia Nacional de Seguridad* (NSA) a principios de la década de 2000. Para Bitcoin, la función `SHA512` no se usa directamente dentro del protocolo, pero se usa en el contexto de derivar claves hijas a nivel de aplicación, según BIP32 y BIP39. En estos procesos, se utiliza varias veces en el algoritmo `HMAC`, así como en la función de derivación de claves `PBKDF2`. La función `SHA512` forma parte de la familia SHA 2, al igual que `SHA256`. Su funcionamiento es muy similar al de esta última.