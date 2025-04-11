---
term: P2SH-P2WPKH

---
P2SH-P2WPKH står for *Pay to Script Hash - Pay to Witness Public Key Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO, også kjent som "Nested SegWit".

P2SH-P2WPKH ble introdusert med implementeringen av SegWit i august 2017. Dette skriptet er en P2WPKH pakket inn i en P2SH. Det låser bitcoins basert på hashen til en offentlig nøkkel. Forskjellen fra den klassiske P2WPKH er at skriptet er pakket inn i `redeemScript` i en klassisk P2SH.

Dette skriptet ble opprettet ved lanseringen av SegWit for å gjøre det lettere å ta det i bruk. Det gjør det mulig å bruke denne nye standarden, selv med tjenester eller lommebøker som ennå ikke er kompatible med SegWit. Det er et slags overgangsskript mot den nye standarden. I dag er det derfor ikke lenger veldig relevant å bruke denne typen innpakkede SegWit-skript, siden de fleste lommebøker har implementert native SegWit. P2SH-P2WPKH-adresser er skrevet med `Base58Check`-koding og starter alltid med `3`, som alle P2SH-adresser.

> ► * `P2SH-P2WPKH` kalles også noen ganger `P2WPKH-nested-in-P2SH`