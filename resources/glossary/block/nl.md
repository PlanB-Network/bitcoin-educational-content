---
term: BLOK
---

Datastructuur in het Bitcoin systeem. Een blok bevat een verzameling geldige transacties en metadata in de kop. Elk blok is verbonden met het volgende door de Hash van zijn header, en vormt zo de Blockchain. De Blockchain fungeert als een tijdstempelserver die elke gebruiker in staat stelt alle transacties uit het verleden te kennen, om te controleren of een transactie niet heeft plaatsgevonden en om dubbele uitgaven te voorkomen. Transacties worden georganiseerd in een Merkle Tree. Deze cryptografische accumulator maakt de productie mogelijk van een digest van alle transacties in een blok, de "Merkle Root" genoemd De header van een blok bevat 6 Elements:


- De versie van het blok;
- De afdruk van het vorige blok;
- De wortel van de Merkle Tree van transacties;
- De Timestamp van het blok;
- De moeilijkheidsgraad;
- De Nonce.


Om geldig te zijn moet een blok een kop hebben die, na gehasht te zijn met `SHA256d`, een digest produceert die kleiner is dan of gelijk is aan het moeilijkheidsdoel.