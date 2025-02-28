---
term: SHA512

---
Acronym for "*Secure Hash Algorithm 512 bits*". It is a cryptographic hash function producing a 512-bit digest. It was designed by the *National Security Agency* (NSA) in the early 2000s. For Bitcoin, the `SHA512` function is not used directly within the protocol, but it is used in the context of deriving child keys at the application level, according to BIP32 and BIP39. In these processes, it is used multiple times in the `HMAC` algorithm, as well as in the `PBKDF2` key derivation function. The `SHA512` function is part of the SHA 2 family, like `SHA256`. Its operation is very similar to the latter.