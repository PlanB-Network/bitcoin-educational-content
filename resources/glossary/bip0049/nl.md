---
term: BIP0049
---

BIP49 is een informatieve BIP die de afleidingsmethode introduceert die gebruikt wordt om generate geneste SegWit adressen in een HD Wallet te krijgen. Het voorgestelde afleidingspad volgt de standaarden van BIP43 en BIP44, met de index `49'` (verharde afleiding) op de diepte van het doel. Bijvoorbeeld, de eerste Address van een P2SH-P2WPKH rekening zou worden afgeleid van het pad: `m/49'/0'/0'/0/0`. Geneste SegWit scripts werden uitgevonden bij de lancering van SegWit om de adoptie ervan te vergemakkelijken. Ze maken het gebruik van deze nieuwe standaard mogelijk, zelfs op wallets die nog niet compatibel zijn met SegWit.