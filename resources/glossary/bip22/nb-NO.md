---
term: BIP22

---
BIP foreslått i 2012 av Luke Dashjr som introduserer en standardisert JSON-RPC-metode for eksterne gruvegrensesnitt, kalt "getblocktemplate". I takt med at utvinning har blitt vanskeligere, har bruken av spesialisert ekstern programvare for å produsere bevis på arbeid utviklet seg. Denne BIP-en foreslår en felles kommunikasjonsstandard for blokkmalen mellom fulle noder og programvare som er spesialisert på utvinning. Denne metoden innebærer å sende hele blokkens struktur, i stedet for bare overskriften, slik at utvinneren kan tilpasse den.