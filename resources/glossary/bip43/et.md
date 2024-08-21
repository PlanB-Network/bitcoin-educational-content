---
term: BIP43
---

Ettepanek täiustuseks, mis tutvustab tuletustee taseme kasutamist HD rahakottide struktuuris eesmärgi välja kirjeldamiseks, mida varem tutvustati BIP32-s. BIP43 kohaselt on HD rahakoti esimene tuletustase, kohe pärast peamist võtit, mida tähistatakse kui `m/`, reserveeritud eesmärgi numbrile, mis näitab ülejäänud tee jaoks kasutatud tuletusstandardit. See number registreeritakse kui kõvastunud indeks. Näiteks, kui rahakott järgib SegWit standardit (BIP84), oleks selle tuletustee algus: `m/84'/`. BIP43 võimaldab seega selgitada, milliseid standardeid iga rahakottide tarkvara järgib, et parandada nende vahelist koostalitlusvõimet. Ülejäänud tuletustee standardiseerimine on kirjeldatud BIP44-s.