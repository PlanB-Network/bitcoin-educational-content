---
term: PIKENDATUD KEY

---
Tähemärkide jada, mis ühendab võtme (avaliku või privaatse), sellega seotud ahelakoodi ja rea metaandmeid. Laiendatud võti koondab kõik lapsvõtmete tuletamiseks vajalikud elemendid ühte identifikaatorisse. Neid kasutatakse deterministlikes ja hierarhilistes rahakottides ning neid võib olla kahte tüüpi: laiendatud avalik võti (mida kasutatakse avalike allvõtmete tuletamiseks) või laiendatud privaatne võti (mida kasutatakse nii privaatsete kui ka avalike allvõtmete tuletamiseks). Laiendatud võti sisaldab seega mitmeid erinevaid andmeid, mida on kirjeldatud BIP32-s, ja seda järgmises järjekorras:


- Eesliide: `prv` ja `pub` on HRP (Human Readable Part), mis näitab, kas tegemist on laiendatud privaatvõtmega (`prv`) või laiendatud avaliku võtmega (`pub`). Eesliite esimene täht tähistab laiendatud võtme versiooni: `x` Legacy või SegWit V1 puhul Bitcoinis, `t` Legacy või SegWit V1 puhul Bitcoin Testnetis, `y` Nested SegWit puhul Bitcoinis, `u` Nested SegWit puhul Bitcoin Testnetis, `z` SegWit V0 puhul Bitcoinis, `v` SegWit V0 puhul Bitcoin Testnetis.
- Sügavus, mis näitab, kui palju tuletusi tuleb teha põhivõttest, et jõuda laiendatud võtmeni;
- Vanema sõrmejälg. See kujutab endast vanema avaliku võtme "HASH160" esimesed 4 baiti;
- Indeks. See on selle paari number, millest laiendatud võti on tuletatud;
- Ketikood;
- Täitebait, kui tegemist on privaatvõtmega `0x00`;
- Privaatne või avalik võti;
- Kontrollsumma. See kujutab endast laiendatud võtme ülejäänud osa "HASH256" esimesed 4 baiti.

Praktikas kasutatakse laiendatud avalikku võtit vastuvõtuaadresside genereerimiseks ja konto tehingute jälgimiseks, ilma et sellega seotud isiklikke võtmeid avalikustataks. See võimaldab näiteks luua niinimetatud "ainult jälgimise" rahakoti. Siiski on oluline märkida, et laiendatud avalik võti on kasutaja eraelu puutumatuse seisukohast tundlik teave, sest selle avalikustamine võib võimaldada kolmandatel isikutel jälgida tehinguid ja näha seotud konto saldot.