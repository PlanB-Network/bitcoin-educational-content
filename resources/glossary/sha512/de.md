---
term: SHA512

---
Akronym für "*Secure Hash Algorithm 512 bits*". Es handelt sich um eine kryptografische Hash-Funktion, die einen 512-Bit-Digest erzeugt. Sie wurde von der *National Security Agency* (NSA) in den frühen 2000er Jahren entwickelt. Bei Bitcoin wird die Funktion "SHA512" nicht direkt innerhalb des Protokolls verwendet, sondern im Zusammenhang mit der Ableitung von Unterschlüsseln auf der Anwendungsebene gemäß BIP32 und BIP39. In diesen Prozessen wird sie mehrfach im "Hmac"-Algorithmus sowie in der Schlüsselableitungsfunktion "PBKDF2" verwendet. Die Funktion `SHA512` gehört wie `SHA256` zur SHA 2 Familie. Ihre Funktionsweise ist der letzteren sehr ähnlich.