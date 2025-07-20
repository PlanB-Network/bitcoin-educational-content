---
term: SHA512
---

Skrót od "*Secure Hash Algorithm 512 bits*". Jest to kryptograficzna funkcja Hash generująca 512-bitowy skrót. Została zaprojektowana przez *National Security Agency* (NSA) na początku XXI wieku. W przypadku Bitcoin funkcja `SHA512` nie jest używana bezpośrednio w protokole, ale jest używana w kontekście wyprowadzania kluczy potomnych na poziomie aplikacji, zgodnie z BIP32 i BIP39. W tych procesach jest ona używana wielokrotnie w algorytmie `HMAC`, a także w funkcji wyprowadzania klucza `PBKDF2`. Funkcja `SHA512` jest częścią rodziny SHA 2, podobnie jak `SHA256`. Jej działanie jest bardzo podobne do tej ostatniej.