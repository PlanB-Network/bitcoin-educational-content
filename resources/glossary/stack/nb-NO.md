---
term: BATTERI
---

I forbindelse med skriptspråket som brukes til å knytte utgiftsbetingelser til Bitcoin UTXO-er, er stakken en LIFO-datastruktur (*Last In, First Out*) som brukes til å lagre midlertidige Elements under skripteksekvering. Hver operasjon i skriptet manipulerer disse stablene, der Elements kan legges til (*push*) eller fjernes (*pop*). Skript bruker stabler til å evaluere uttrykk, lagre midlertidige variabler og håndtere betingelser.


Når du kjører et Bitcoin-skript, kan du bruke to stabler: hovedstakken og alt-stakken (alternativstakken). Hovedstakken brukes til de fleste skriptoperasjoner. Det er i denne stakken skriptoperasjoner legger til, fjerner eller manipulerer data. Den alternative stakken brukes derimot til midlertidig lagring av data under skripteksekvering. Spesifikke opkoder, som `OP_TOALTSTACK` og `OP_FROMALTSTACK`, gjør det mulig å overføre Elements fra hovedstakken til den alternative stakken og omvendt.


Når en transaksjon valideres, skyves for eksempel signaturer og offentlige nøkler inn i hovedstakken og behandles av påfølgende opkoder for å verifisere at signaturene stemmer overens med transaksjonsnøklene og -dataene.