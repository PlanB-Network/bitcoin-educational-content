---
term: DER
---

Lyhenne sanoista *Distinguished Encoding Rules*. Se on tiukka osajoukko ASN.1-koodaussäännöistä, jotka on määritelty eritelmässä [ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) ja joita käytetään minkä tahansa tietotyypin koodaamiseen binäärisekvenssiksi. DER:ää käytetään pääasiassa tietyillä aloilla, kuten salauksessa, jossa tiedot on koodattava standardoidulla, ennustettavalla tavalla.


Bitcoin:ssä ECDSA-allekirjoitukset on koodattu DER-muodossa. Ne koostuvat kahdesta 32 tavun koodatusta numerosta (`r`, `s`). Allekirjoitusmuoto koostuu seuraavista Elements (71 tavua):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Kanssa :




- 0x30` (1 tavu): Yhdistelmärakenteen tunniste;
- length` (1 tavu): seuraavien tietojen pituus ;
- 0x02` (1 tavu): datatunnisteen tyyppi `INTEGER` (kokonaisluku) ;
- `r-length` (1 tavu): seuraavan `r`-arvon pituus (32 tavua) ;
- r` (32 tavua): r`:n arvo big-endian kokonaislukuna;
- 0x02` (1 tavu): datatunnisteen tyyppi `INTEGER` (kokonaisluku) ;
- `s-length` (1 tavu): seuraavan `s`-arvon pituus (32 tavua) ;
- `s` (32 tavua): `s`-arvo big-endian kokonaislukuna.


Bitcoin-transaktiossa DER-allekirjoituksen loppuun lisätään tavu, joka osoittaa käytetyn SigHash-tyypin.