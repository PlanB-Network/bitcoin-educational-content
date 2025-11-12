---
term: UITGEBREIDE TOETS
---

Een reeks tekens die een sleutel (publiek of privé), de bijbehorende chain code en een reeks metadata combineert. Een uitgebreide sleutel compileert alle Elements die nodig zijn voor het afleiden van kindsleutels in een enkele identificator. Ze worden gebruikt in deterministische en hiërarchische portemonnees en kunnen van twee types zijn: een uitgebreide publieke sleutel (gebruikt om publieke kindsleutels af te leiden) of een uitgebreide private sleutel (gebruikt om zowel private als publieke kindsleutels af te leiden). Een uitgebreide sleutel bevat dus verschillende stukjes gegevens, beschreven in BIP32, in de volgorde:


- Het voorvoegsel: `prv` en `pub` zijn HRP (Human Readable Part) die aangeven of het een uitgebreide private sleutel (`prv`) of een uitgebreide publieke sleutel (`pub`) is. De eerste letter van het voorvoegsel geeft de versie van de uitgebreide sleutel aan: `x` voor Legacy of SegWit V1 op Bitcoin, `t` voor Legacy of SegWit V1 op Bitcoin Testnet, `y` voor Geneste SegWit op Bitcoin, `u` voor Geneste SegWit op Bitcoin Testnet, `z` voor SegWit V0 op Bitcoin, `v` voor SegWit V0 op Bitcoin Testnet.
- De diepte, die het aantal afleidingen van de hoofdsleutel aangeeft om de uitgebreide sleutel te bereiken;
- De oudervingerafdruk. Dit zijn de eerste 4 bytes van de `HASH160` van de openbare sleutel van de ouder;
- De index. Dit is het nummer van het paar onder zijn broers en zussen waarvan de uitgebreide sleutel is afgeleid;
- De chain code;
- Een opvulbyte als het een privésleutel `0x00` is;
- De private of publieke sleutel;
- Een controlesom. Het vertegenwoordigt de eerste 4 bytes van de `HASH256` van de rest van de uitgebreide sleutel.


In de praktijk wordt de uitgebreide openbare sleutel gebruikt om generate adressen te ontvangen en de transacties van een account te observeren zonder de bijbehorende privésleutels bloot te geven. Dit kan bijvoorbeeld het creëren van een zogenaamde "watch-only" Wallet mogelijk maken. Het is echter belangrijk op te merken dat de uitgebreide openbare sleutel gevoelige informatie is voor de privacy van de gebruiker, omdat derden door het vrijgeven ervan transacties kunnen traceren en het saldo van de gekoppelde rekening kunnen zien.