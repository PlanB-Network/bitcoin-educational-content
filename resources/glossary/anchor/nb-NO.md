---
term: Anchor
---

I RGB-protokollen representerer en Anchor et sett med data på klientsiden som brukes til å bevise at en enkelt Commitment er inkludert i en transaksjon. I RGB-protokollen består en Anchor av følgende Elements:




- transaction ID Bitcoin (txid) fra Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Ekstra transaksjonsbevis (ETP) hvis Tapret Commitment-mekanismen brukes.


En Anchor tjener derfor til å etablere en verifiserbar kobling mellom en spesifikk Bitcoin-transaksjon og private data som er validert av RGB-protokollen. Den garanterer at disse dataene faktisk er inkludert i Blockchain, uten at det nøyaktige innholdet offentliggjøres.