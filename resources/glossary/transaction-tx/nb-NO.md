---
term: TRANSAKSJON (TX)

---
I Bitcoinsammenheng er en transaksjon (forkortet "TX") en operasjon som registreres i blokkjeden, og som overfører eierskapet til bitcoins fra én eller flere innganger til én eller flere utganger. Hver transaksjon bruker UTXO-er (Unspent Transaction Outputs) som input, som er output fra tidligere transaksjoner, og skaper nye UTXO-er som output, som kan brukes som input i fremtidige transaksjoner.

Hver input inneholder en referanse til en eksisterende output sammen med et signaturskript (`scriptSig`) som oppfyller utgiftsbetingelsene (`scriptPubKey`) som er etablert av outputen den refererer til. Det er dette som gjør det mulig å låse opp bitcoins. Utgangene definerer nye bruksbetingelser (`scriptPubKey`) for de overførte bitcoinsene, ofte i form av en offentlig nøkkel eller en adresse som bitcoinsene nå er knyttet til.