---
term: SHA512
---

Acroniem voor "*Veilig Hash Algoritme 512 bits*". Het is een cryptografische Hash functie die een 512-bits digest produceert. Het is ontworpen door de *National Security Agency* (NSA) in de vroege jaren 2000. Voor Bitcoin wordt de `SHA512` functie niet direct binnen het protocol gebruikt, maar wel in de context van het afleiden van kindsleutels op applicatieniveau, volgens BIP32 en BIP39. In deze processen wordt de functie meerdere keren gebruikt in het `HMAC` algoritme en in de `PBKDF2` sleutelafleidingsfunctie. De `SHA512` functie is onderdeel van de SHA 2 familie, net als `SHA256`. De werking lijkt erg op die van de laatste.