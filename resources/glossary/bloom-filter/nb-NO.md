---
term: BLOOM FILTER

---
En probabilistisk datastruktur som brukes til å teste om et element er en del av et sett. Bloom-filtre gjør det mulig å sjekke medlemskap raskt uten å teste hele datasettet. De er spesielt nyttige i sammenhenger der plass og hastighet er avgjørende, samtidig som en lav og kontrollert feilrate er akseptabel. Bloom-filtre produserer ikke falske negativer, men de genererer en viss mengde falske positiver. Når et element legges til i filteret, genererer flere hashfunksjoner posisjoner i en bitmatrise. De samme hashfunksjonene brukes for å sjekke medlemskap. Hvis alle de tilsvarende bitene er satt, er elementet sannsynligvis i settet, men med en risiko for falske positiver. Bloom-filtre er mye brukt i databaser og nettverk. Det er særlig kjent at Google bruker dem i sitt komprimerte databasehåndteringssystem *BigTable*. I Bitcoin-protokollen brukes de spesielt for SPV-lommebøker i henhold til BIP37.

> ► *Når man spesifikt snakker om bruk av Bloom-filtre i forbindelse med Bitcoin-transaksjoner, bruker man noen ganger begrepet "Transaction Bloom Filtering"