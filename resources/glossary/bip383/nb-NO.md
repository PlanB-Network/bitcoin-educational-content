---
term: BIP383

---
Innfører funksjonene `multi(NUM, KEY, ..., KEY)` og `sortedmulti(NUM, KEY, ..., KEY)` for deskriptorer. Disse funksjonene gjør det mulig å beskrive multisignaturskript i deskriptorene, med `sortedmulti` som sorterer de offentlige nøklene i leksikografisk rekkefølge for å sikre kompatibilitet under import. BIP383 ble implementert sammen med alle andre descriptor-relaterte BIP-er (unntatt BIP386) i versjon 0.17 av Bitcoin Core.