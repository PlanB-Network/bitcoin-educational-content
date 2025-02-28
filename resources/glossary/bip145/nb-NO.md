---
term: BIP145

---
Oppdaterer JSON-RPC-kallet `getblocktemplate` for å inkludere støtte for SegWit, i samsvar med BIP141. Denne oppdateringen gjør det mulig for utvinnere å konstruere blokker ved å ta hensyn til den nye "vekt"-målingen av transaksjoner og blokker introdusert av SegWit, og andre parametere som beregning av sigops-grensen.