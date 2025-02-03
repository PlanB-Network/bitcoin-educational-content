---
term: MERKLE BLOCK

---
En datastruktur som brukes i forbindelse med BIP37 (*Transaction Bloom Filtering*) for å gi et kompakt bevis på at spesifikke transaksjoner er inkludert i en blokk. Den brukes særlig for SPV-lommebøker. Merkle-blokken inneholder blokkoverskriftene, filtrerte transaksjoner og et delvis Merkle-tre, slik at lette klienter raskt kan verifisere om en transaksjon tilhører en blokk uten å laste ned alle transaksjonene.