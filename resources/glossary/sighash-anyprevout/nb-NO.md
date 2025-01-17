---
term: SIGHASH_ANYPREVOUT

---
Forslag til implementering av en ny SigHash-flaggmodifikator i Bitcoin, introdusert med BIP118. `SIGHASH_ANYPREVOUT` gir større fleksibilitet i transaksjonshåndteringen, spesielt for avanserte applikasjoner som betalingskanaler på Lightning Network og Eltoo-oppdateringen. Med `SIGHASH_ANYPREVOUT` kan signaturen ikke knyttes til noen spesifikk tidligere UTXO (*Any Previous Output*). Brukt i kombinasjon med `SIGHASH_ALL`, vil den gjøre det mulig å signere alle utdataene i en transaksjon, men ingen av inndataene. Dette gjør det mulig å gjenbruke signaturen for forskjellige transaksjoner, så lenge visse spesifiserte betingelser er oppfylt.

> denne SigHash-modifikatoren SIGHASH_ANYPREVOUT er avledet fra ideen om SIGHASH_NOINPUT, som opprinnelig ble foreslått av Joseph Poon i 2016 for å forbedre konseptet hans Lightning Network