---
term: BCH-KODE
---

En klasse feilkorrigeringskoder som brukes til å oppdage og korrigere feil i en datasekvens. Med andre ord brukes BCH-feilrettingskoder til å finne og korrigere tilfeldige feil i overført informasjon, for å sikre at den kommer intakt frem til bestemmelsesstedet. Akronymet "BCH" står for initialene til navnene på oppfinnerne av disse kodene: Bose, Ray-Chaudhuri og Hocquenghem.


Dette verktøyet brukes på mange områder innen databehandling, blant annet SSD-er, DVD-er og QR-koder. Takket være disse feilkorrigerende kodene er det for eksempel fortsatt mulig å hente ut informasjonen i en QR-kode selv om den er delvis tildekket.


Som en del av Bitcoin brukes BCH-koder for sjekksummen i Bech32 og Bech32m (post-SegWit) Address-formatene. De representerer et bedre kompromiss mellom størrelsen på kontrollsummen og feildeteksjonsevnen enn de enkle Hash-funksjonene som tidligere ble brukt på Legacy-adresser. I Bitcoin-sammenheng brukes BCH-koder kun til feildeteksjon, ikke til feilretting. Bitcoin-porteføljeprogramvaren vil dermed identifisere og rapportere til brukeren eventuelle feil i en mottakende Address, men vil ikke endre den feilaktige Address automatisk. Dette valget er motivert av det faktum at integrering av feilretting uunngåelig påvirker algoritmens evne til feildeteksjon.