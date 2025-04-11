---
term: HASH256

---
Bitcoini erinevate rakenduste jaoks kasutatav krüptograafiline funktsioon. See hõlmab SHA256-funktsiooni kahekordset rakendamist sisendandmete suhtes. Sõnum läbib SHA256-funktsiooni üks kord ja selle operatsiooni tulemust kasutatakse sisendina teise SHA256-funktsiooni läbimise korral. Selle funktsiooni väljundiks on seega 256 bitti.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$$