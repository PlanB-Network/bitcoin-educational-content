---
term: LIBSECP256K1
---

C-bibliotek med høy ytelse og sikkerhet for digitale signaturer og andre kryptografiske primitiver på den elliptiske kurven `secp256k1`. Siden denne kurven aldri har vært mye brukt utenfor Bitcoin (i motsetning til den ofte foretrukne `secp256r1`-kurven), tar dette biblioteket sikte på å være den mest omfattende referansen for bruken av den. Utviklingen av libsecp256k1 var primært rettet mot behovene til Bitcoin, og funksjoner som er beregnet på andre bruksområder, kan være mindre testet eller verifisert. Riktig bruk av dette biblioteket krever nøye oppmerksomhet for å sikre at det er egnet for de spesifikke formålene til andre applikasjoner enn Bitcoin.


Biblioteket libsecp256k1 tilbyr en rekke funksjoner, blant annet




- ECDSA-secp256k1-signatur og -verifisering, og generering av kryptografiske nøkler ;
- Additive og multiplikative operasjoner på hemmelige og offentlige nøkler ;
- Serialisering og analyse av hemmelige nøkler, offentlige nøkler og signaturer ;
- Signering og generering av offentlige nøkler i konstant tid med konstant tilgang til minnet;
- Og en rekke andre kryptografiske primitiver.