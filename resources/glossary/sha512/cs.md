---
term: SHA512
---

Akronym pro "*Secure Hash Algorithm 512 bits*" (Bezpečný hašovací algoritmus 512 bitů). Jedná se o kryptografickou hašovací funkci, která produkuje 512bitový otisk. Byla navržena *National Security Agency* (NSA) na počátku 2000. let. Pro Bitcoin funkce `SHA512` není přímo používána v rámci protokolu, ale používá se v kontextu odvozování dětských klíčů na aplikační úrovni, podle BIP32 a BIP39. V těchto procesech je používána několikrát v algoritmu `HMAC`, stejně jako ve funkci odvození klíče `PBKDF2`. Funkce `SHA512` je součástí rodiny SHA 2, stejně jako `SHA256`. Její provoz je velmi podobný tomu posledně jmenovanému.