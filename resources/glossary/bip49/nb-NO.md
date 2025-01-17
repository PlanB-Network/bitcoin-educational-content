---
term: BIP49

---
BIP49 er en informativ BIP som introduserer avledningsmetoden som brukes til å generere nestede SegWit-adresser i en HD-lommebok. Den foreslåtte avledningsveien følger standardene i BIP43 og BIP44, med indeksen "49" (herdet avledning) på dybden av målet. For eksempel vil den første adressen til en P2SH-P2WPKH-konto bli avledet fra banen: `m/49'/0'/0'/0/0`. Nested SegWit-skript ble oppfunnet ved lanseringen av SegWit for å gjøre det enklere å ta den i bruk. De gjør det mulig å bruke denne nye standarden, selv på lommebøker som ennå ikke er kompatible med SegWit.