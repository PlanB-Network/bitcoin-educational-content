---
term: MEMPOOL

---
En sammentrekning av begrepene "minne" og "pool". Dette refererer til et virtuelt område der Bitcoin-transaksjoner som venter på å bli inkludert i en blokk, grupperes sammen. Når en transaksjon opprettes og sendes ut i Bitcoin-nettverket, blir den først verifisert av nodene i nettverket. Hvis den anses som gyldig, plasseres den i Mempoolen til hver node, hvor den blir liggende til den blir valgt av en utvinner til å bli inkludert i en blokk.

Det er viktig å merke seg at hver node i Bitcoin-nettverket opprettholder sin egen Mempool, og derfor kan det være variasjoner i innholdet i Mempool mellom forskjellige noder til enhver tid. Parameteren "maxmempool" i filen "bitcoin.conf" på hver node gjør det mulig for operatørene å kontrollere hvor mye RAM (random access memory) noden skal bruke til å lagre ventende transaksjoner i Mempool. Ved å begrense størrelsen på Mempool kan nodeoperatørene forhindre at den bruker for mye ressurser på systemet. Denne parameteren angis i megabyte (MB). Standardverdien for Bitcoin Core er 300 MB.

Transaksjoner i Mempool er midlertidige. De bør ikke betraktes som uforanderlige før de er inkludert i en blokk, og etter et visst antall bekreftelser. Disse kan ofte byttes ut eller renses.