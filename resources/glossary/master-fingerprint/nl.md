---
term: HOOFDVINGERAFDRUK
---

Een 4-byte (32-bit) vingerafdruk van de Master Private Key in een Hierarchical Deterministic (HD) Wallet. Deze wordt verkregen door de `SHA256` Hash van de Master Private Key te berekenen. Deze wordt verkregen door het berekenen van de `SHA256` Hash van de private hoofdsleutel, gevolgd door een `RIPEMD160` Hash, een proces waarnaar verwezen wordt als `HASH160` op Bitcoin. De Master Fingerprint wordt gebruikt om een HD Wallet te identificeren, onafhankelijk van de afleidingspaden, maar rekening houdend met de aan- of afwezigheid van een passphrase. Het is beknopte informatie die het mogelijk maakt om te verwijzen naar de oorsprong van een set sleutels, zonder gevoelige informatie over de Wallet te onthullen.