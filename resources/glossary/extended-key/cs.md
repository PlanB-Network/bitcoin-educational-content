---
term: EXTENDED KEY

---
Sekvence znaků, která kombinuje klíč (veřejný nebo soukromý), přidružený řetězový kód a řadu metadat. Rozšířený klíč sdružuje všechny prvky potřebné k odvození podřízených klíčů do jediného identifikátoru. Používají se v deterministických a hierarchických peněženkách a mohou být dvou typů: rozšířený veřejný klíč (slouží k odvození podřízených veřejných klíčů) nebo rozšířený soukromý klíč (slouží k odvození podřízených soukromých i veřejných klíčů). Rozšířený klíč tedy obsahuje několik různých údajů popsaných v BIP32 v tomto pořadí:


- Předpony: `prv` a `pub` jsou HRP (Human Readable Part) označující, zda se jedná o rozšířený soukromý klíč (`prv`) nebo rozšířený veřejný klíč (`pub`). První písmeno prefixu označuje verzi rozšířeného klíče: `x` pro Legacy nebo SegWit V1 na Bitcoinu, `t` pro Legacy nebo SegWit V1 na Bitcoin Testnet, `y` pro Nested SegWit na Bitcoinu, `u` pro Nested SegWit na Bitcoin Testnet, `z` pro SegWit V0 na Bitcoinu, `v` pro SegWit V0 na Bitcoin Testnet.
- Hloubka, která udává počet odvození od hlavního klíče k dosažení rozšířeného klíče;
- Otisk prstu rodiče. Představuje první 4 bajty `HASH160` rodičovského veřejného klíče;
- Index. Jedná se o číslo páru mezi jeho sourozenci, z něhož je odvozen rozšířený klíč;
- Řetězový kód;
- Výplňový bajt, pokud se jedná o soukromý klíč `0x00`;
- Soukromý nebo veřejný klíč;
- Kontrolní součet. Představuje první 4 bajty `HASH256` zbytku rozšířeného klíče.

V praxi se rozšířený veřejný klíč používá ke generování přijímacích adres a ke sledování transakcí účtu, aniž by byly odhaleny související soukromé klíče. To může umožnit například vytvoření takzvané "watch-only" peněženky. Je však důležité si uvědomit, že rozšířený veřejný klíč je citlivou informací pro soukromí uživatele, protože jeho zveřejnění může umožnit třetím stranám sledovat transakce a vidět zůstatek na souvisejícím účtu.