---
term: HASH160

definition: Funktsioon, mis kombineerib SHA256 ja seejärel RIPEMD160, mida kasutatakse Bitcoini aadresside genereerimiseks.
---
Bitcoinis kasutatav krüptograafiline funktsioon, eelkõige Legacy ja SegWit v0 vastuvõtuaadresside genereerimiseks. See kombineerib kaks hash-funktsiooni, mida täidetakse järjestikku sisendil: kõigepealt SHA256, seejärel RIPEMD160. Selle funktsiooni väljundiks on seega 160 bitti.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$$