---
term: STACK

---
I forbindelse med skriptspråket som brukes til å bruke utgiftsbetingelser på Bitcoin UTXO-er, er stakken en "LIFO"-datastruktur (*Last In, First Out*) som brukes til å lagre midlertidige elementer under utførelsen av et skript. Hver operasjon i skriptet manipulerer disse stablene, der elementer kan legges til (*push*) eller fjernes (*pop*). Skript bruker stabler til å evaluere uttrykk, lagre midlertidige variabler og håndtere betingelser.

Under kjøringen av et Bitcoin-skript kan to stabler brukes: hovedstakken og alt-stakken (alternativstakken). Hovedstakken brukes til de fleste av skriptets operasjoner. Det er i denne stakken skriptoperasjoner legger til, fjerner eller manipulerer data. Den alternative stakken brukes derimot til midlertidig lagring av data under skriptets kjøring. Spesifikke opkoder, som `OP_TOALTSTACK` og `OP_FROMALTSTACK`, gjør det mulig å overføre elementer fra hovedstakken til den alternative stakken og omvendt.

Under valideringen av en transaksjon skyves for eksempel signaturer og offentlige nøkler inn i hovedstakken og behandles av etterfølgende opkoder for å verifisere at signaturene stemmer overens med nøklene og transaksjonsdataene.

> ► * På engelsk er oversettelsen av "pile" "stack". Den engelske termen brukes vanligvis også på fransk i tekniske diskusjoner*