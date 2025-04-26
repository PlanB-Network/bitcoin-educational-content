---
term: P2SH-P2WSH

---
P2SH-P2WSH står for *Pay to Script Hash - Pay to Witness Script Hash*. Det er en standard skriptmodell som brukes til å etablere utgiftsbetingelser på en UTXO, også kjent som "Nested SegWit".

P2SH-P2WSH ble introdusert med implementeringen av SegWit i august 2017. Dette skriptet beskriver en P2WSH pakket inn i en P2SH. Det låser bitcoins basert på hashen til et skript. Forskjellen fra en klassisk P2WSH er at skriptet er pakket inn i `redeemScript` i en klassisk P2SH.

Dette skriptet ble opprettet ved lanseringen av SegWit for å gjøre det lettere å ta det i bruk. Det gjør det mulig å bruke denne nye standarden, selv med tjenester eller lommebøker som ennå ikke er kompatible med SegWit. I dag er det derfor ikke lenger veldig relevant å bruke denne typen innpakkede SegWit-skript, siden de fleste lommebøker har implementert opprinnelig SegWit. P2SH-P2WSH-adresser er skrevet med `Base58Check`-koding og starter alltid med `3`, som alle P2SH-adresser.