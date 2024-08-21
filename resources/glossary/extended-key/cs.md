---
term: ROZŠÍŘENÝ KLÍČ
---

Sekvence znaků, která kombinuje klíč (veřejný nebo soukromý), jemu přidružený řetězec kódů a sérii metadat. Rozšířený klíč kompiluje všechny prvky nezbytné pro odvození dětských klíčů do jednoho identifikátoru. Používají se v deterministických a hierarchických peněženkách a mohou být dvou typů: rozšířený veřejný klíč (používaný k odvození dětských veřejných klíčů) nebo rozšířený soukromý klíč (používaný k odvození obou, dětských soukromých a veřejných klíčů). Rozšířený klíč tedy zahrnuje několik různých datových prvků, popsaných v BIP32, v pořadí:
* Předpona: `prv` a `pub` jsou HRP (Human Readable Part - část čitelná člověkem) označující, zda se jedná o rozšířený soukromý klíč (`prv`) nebo rozšířený veřejný klíč (`pub`). První písmeno předpony určuje verzi rozšířeného klíče: `x` pro Legacy nebo SegWit V1 na Bitcoinu, `t` pro Legacy nebo SegWit V1 na Bitcoin Testnetu, `y` pro Nested SegWit na Bitcoinu, `u` pro Nested SegWit na Bitcoin Testnetu, `z` pro SegWit V0 na Bitcoinu, `v` pro SegWit V0 na Bitcoin Testnetu.
* Hloubka, která udává počet odvození od hlavního klíče k dosažení rozšířeného klíče;
* Odtisk rodiče. Představuje první 4 bajty `HASH160` veřejného klíče rodiče;
* Index. Jedná se o číslo páru mezi jeho sourozenci, z něhož je rozšířený klíč odvozen;
* Řetězec kódů;
* Doplněk bajtu, pokud jde o soukromý klíč `0x00`;
* Soukromý nebo veřejný klíč;
* Kontrolní součet. Představuje první 4 bajty `HASH256` zbytku rozšířeného klíče.

V praxi se rozšířený veřejný klíč používá k generování přijímacích adres a k pozorování transakcí účtu bez vystavení přidružených soukromých klíčů. To může umožnit například vytvoření takzvané "pouze pro sledování" peněženky. Je však důležité poznamenat, že rozšířený veřejný klíč je citlivá informace pro soukromí uživatele, protože jeho zveřejnění může umožnit třetím stranám sledovat transakce a vidět zůstatek přidruženého účtu.