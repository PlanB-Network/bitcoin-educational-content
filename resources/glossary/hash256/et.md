---
term: HASH256
---

Krüptograafiline funktsioon, mida kasutatakse mitmesugustel rakendustel Bitcoinis. See hõlmab SHA256 funktsiooni kahekordset rakendamist sisendandmetele. Sõnum läbib SHA256 ühe korra ja selle operatsiooni tulemust kasutatakse sisendina teiseks läbimiseks läbi SHA256. Seega on selle funktsiooni väljund 256 bitti.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$