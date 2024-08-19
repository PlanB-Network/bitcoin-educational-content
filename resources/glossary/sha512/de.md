---
term: SHA512
---

Akronym für "*Secure Hash Algorithm 512 bits*". Es handelt sich um eine kryptografische Hash-Funktion, die einen 512-Bit-Digest produziert. Sie wurde vom *National Security Agency* (NSA) in den frühen 2000er Jahren entworfen. Für Bitcoin wird die `SHA512` Funktion nicht direkt im Protokoll verwendet, aber sie findet Anwendung auf der Ebene der Ableitung von Kinderschlüsseln, gemäß BIP32 und BIP39. In diesen Prozessen wird sie mehrfach im `HMAC` Algorithmus sowie in der `PBKDF2` Schlüsselableitungsfunktion verwendet. Die `SHA512` Funktion ist Teil der SHA-2-Familie, wie auch `SHA256`. Ihre Funktionsweise ist der letzteren sehr ähnlich.