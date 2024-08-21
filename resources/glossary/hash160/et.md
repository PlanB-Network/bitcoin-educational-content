---
term: HASH160
---

Krüptograafiline funktsioon, mida kasutatakse Bitcoinis, eriti Legacy ja SegWit v0 vastuvõtu aadresside genereerimiseks. See ühendab kaks järjestikku sisendil käivitatavat räsifunktsiooni: esmalt SHA256, seejärel RIPEMD160. Selle funktsiooni väljund on seega 160 bitti.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$