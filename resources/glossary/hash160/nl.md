---
term: HASH160
---

Cryptografische functie gebruikt in Bitcoin, met name voor het genereren van Legacy en SegWit v0 ontvangstadressen. Het combineert twee Hash functies die achtereenvolgens op de invoer worden uitgevoerd: eerst SHA256, dan RIPEMD160. De uitvoer van deze functie is daarom 160 bits.


$${HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$