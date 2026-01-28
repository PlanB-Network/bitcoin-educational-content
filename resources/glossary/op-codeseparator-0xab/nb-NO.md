---
term: OP_CODESEPARATOR (0XAB)

definition: Opcode som segmenterer et skript for å tillate uavhengige signaturer for hver del.
---
Endrer det gjeldende utdataskriptet, og angir at bare operasjonene som følger etter denne opkoden, vil bli vurdert i verifiseringen av signaturene for de tilsvarende inndataene. Dette gjør det mulig å segmentere et komplekst skript i flere deler, der hvert segment kan signeres uavhengig av hverandre.