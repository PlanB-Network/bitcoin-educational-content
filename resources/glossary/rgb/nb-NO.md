---
term: RGB
---

Desentralisert, konfidensielt Smart contract-system designet for å fungere med Bitcoin og Lightning Network. RGB fungerer på en Client-side Validation-modell og skiller lagringen av Contract State fra Blockchain, slik at bare kryptografiske forpliktelser lagres på den. På denne måten holdes hele tilstandshistorikken utenfor kjeden, noe som gir større skalerbarhet og konfidensialitet. RGB gjør det dermed mulig å opprette komplekse kontrakter for å lagre tokens, NFT-er, desentraliserte identiteter eller DeFi-løsninger direkte på toppen av Bitcoin.


På RGB sikres motstanden mot Double-spending ved bruk av Single-Use Seal, en kryptografisk mekanisme som utnytter det faktum at UTXO-er på Bitcoin bare kan brukes én gang. Når det gjelder tokenautentisitet, garanteres dette ved hjelp av verifisering på klientsiden av tilstandshistorikken, fra Contract ble opprettet til den siste tilstanden.