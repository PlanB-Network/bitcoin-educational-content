---
term: BLK*.DAT

---
Niiden tiedostojen nimi Bitcoin Coressa, jotka tallentavat lohkoketjun raakalohkodataa. Kukin tiedosto tunnistetaan sen nimessä olevalla yksilöllisellä numerolla. Lohkot tallennetaan siis aikajärjestyksessä alkaen tiedostosta blk00000.dat. Kun tämä tiedosto saavuttaa maksimikapasiteettinsa, seuraavat lohkot tallennetaan tiedostoon blk00001.dat, sitten blk00002.dat ja niin edelleen. Kunkin blk-tiedoston enimmäiskapasiteetti on 128 megatavua (MiB), mikä vastaa hieman yli 134 megatavua (MB). Nämä tiedostot on siirretty `/blocks`-kansioon versiosta 0.8.0 lähtien.