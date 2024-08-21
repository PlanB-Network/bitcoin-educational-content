---
termi: BLK*.DAT
---

Bitcoin Coren tiedostojen nimi, jotka tallentavat lohkoketjun raakalohkotiedot. Jokainen tiedosto on yksilöity ainutlaatuisella numerolla sen nimessä. Näin ollen lohkot tallennetaan kronologisessa järjestyksessä, alkaen tiedostosta blk00000.dat. Kun tämä tiedosto saavuttaa maksimikapasiteettinsa, seuraavat lohkot tallennetaan tiedostoon blk00001.dat, sitten blk00002.dat, ja niin edelleen. Jokaisella blk-tiedostolla on maksimikapasiteetti 128 mebibittiä (MiB), mikä vastaa hieman yli 134 megabittiä (MB). Nämä tiedostot on siirretty `/blocks` kansioon versiosta 0.8.0 lähtien.