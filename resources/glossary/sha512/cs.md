---
term: SHA512

---
Zkratka pro "*Secure Hash Algorithm 512 bits*". Jedná se o kryptografickou hašovací funkci, která vytváří 512bitový digest. Byla navržena *Národní bezpečnostní agenturou* (NSA) na počátku roku 2000. U Bitcoinu se funkce `SHA512` nepoužívá přímo v rámci protokolu, ale používá se v souvislosti s odvozováním podřízených klíčů na úrovni aplikace podle BIP32 a BIP39. V těchto procesech je několikrát použita v algoritmu `HMAC` a také ve funkci `PBKDF2` pro odvozování klíčů. Funkce `SHA512` je součástí rodiny SHA 2, stejně jako `SHA256`. Její činnost je velmi podobná posledně jmenované funkci.