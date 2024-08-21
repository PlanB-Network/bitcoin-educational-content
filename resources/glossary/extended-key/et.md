---
term: LAIENDATUD VÕTI
---

Tegemist on tähemärkide jadaga, mis ühendab võtme (avalik või privaatne), sellega seotud ahelakoodi ja mitmesugust metaandmete seeriat. Laiendatud võti koondab kõik lapsevõtmete tuletamiseks vajalikud elemendid ühte identifikaatorisse. Neid kasutatakse deterministlikes ja hierarhilistes rahakottides ning neid võib olla kahte tüüpi: laiendatud avalik võti (kasutatakse lapse avalike võtmete tuletamiseks) või laiendatud privaatvõti (kasutatakse nii lapse privaat- kui ka avalike võtmete tuletamiseks). Laiendatud võti sisaldab seega mitmeid erinevaid andmeid, mida kirjeldatakse BIP32-s, järgmises järjekorras:
* Eesliide: `prv` ja `pub` on HRP (Human Readable Part), mis näitab, kas tegemist on laiendatud privaatvõtmega (`prv`) või laiendatud avaliku võtmega (`pub`). Eesliite esimene täht määrab laiendatud võtme versiooni: `x` Bitcoin'i Legacy või SegWit V1 jaoks, `t` Bitcoin Testnet'i Legacy või SegWit V1 jaoks, `y` Bitcoin'i Nested SegWit jaoks, `u` Bitcoin Testnet'i Nested SegWit jaoks, `z` Bitcoin'i SegWit V0 jaoks, `v` Bitcoin Testnet'i SegWit V0 jaoks.
* Sügavus, mis näitab tuletuste arvu peavõtmest laiendatud võtmeni;
* Vanema sõrmejälg. See esindab vanema avaliku võtme `HASH160` esimesi 4 baiti;
* Indeks. See on paari number tema vendade seas, millest laiendatud võti on tuletatud;
* Ahelakood;
* Täitebait, kui tegemist on privaatvõtmega `0x00`;
* Privaat- või avalik võti;
* Kontrollsumma. See esindab laiendatud võtme ülejäänud osa `HASH256` esimesi 4 baiti.

Praktikas kasutatakse laiendatud avalikku võtit vastuvõtvate aadresside genereerimiseks ja konto tehingute jälgimiseks ilma seotud privaatvõtmeid paljastamata. See võimaldab näiteks luua nn "ainult-vaatamise" rahakoti. Siiski on oluline märkida, et laiendatud avalik võti on kasutaja privaatsuse seisukohast tundlik teave, kuna selle avalikustamine võib võimaldada kolmandatel osapooltel tehinguid jälgida ja näha seotud konto jääki.