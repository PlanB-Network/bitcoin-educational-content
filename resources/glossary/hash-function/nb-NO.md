---
term: HASH FUNCTION

---
En matematisk funksjon som tar en variabel størrelse input (kalt en melding) og produserer en fast størrelse output (kalt hash, hashing, digest eller fingeravtrykk). Hash-funksjoner er mye brukte primitiver innen kryptografi. De har spesifikke egenskaper som gjør dem egnet for bruk i sikre sammenhenger:


- Preimage-resistens: Det må være svært vanskelig å finne en melding som produserer en bestemt hash, dvs. å finne et preimage $m$ for en hash $h$ slik at $h = H(m)$, der $H$ er hashfunksjonen;
- Andre preimage-motstand: Gitt en melding $m_1$, må det være svært vanskelig å finne en annen melding $m_2$ (forskjellig fra $m_1$) slik at $H(m_1) = H(m_2)$;
- Kollisjonsmotstand: Det må være svært vanskelig å finne to forskjellige meldinger $m_1$ og $m_2$ slik at $H(m_1) = H(m_2)$;
- Motstandsdyktighet mot sabotasje: Små endringer i inngangssignalet må føre til betydelige og uforutsigbare endringer i utgangssignalet.

I Bitcoinsammenheng brukes hashfunksjoner til flere formål, blant annet til proof-of-work-mekanismen (*Proof-of-Work*), transaksjonsidentifikatorer, adressegenerering, sjekksumberegninger og opprettelse av datastrukturer som Merkle-trær. På protokollsiden bruker Bitcoin utelukkende `SHA256d`-funksjonen, også kalt `HASH256`, som består av en dobbel `SHA256`-hash. `HASH256` brukes også i beregningen av visse sjekksummer, særlig for utvidede nøkler (`xpub`, `xprv`...). På lommeboksiden brukes også følgende:


- Enkel `SHA256` for sjekksummer av mnemoniske fraser;
- `SHA512` i algoritmene `HMAC` og `PBKDF2` som brukes i prosessen med å utlede deterministiske og hierarkiske lommebøker;
- `HASH160`, som beskriver en suksessiv bruk av en `SHA256` og en `RIPEMD160`. `HASH160` brukes i prosessen med å generere mottakeradresser (unntatt P2PK og P2TR) og til å beregne fingeravtrykk av overordnede nøkler for utvidede nøkler.

> på engelsk kalles det en "hash-funksjon"