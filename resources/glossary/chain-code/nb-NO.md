---
term: KJEDEKODE

---
I forbindelse med hierarkisk deterministisk (HD) avledning av Bitcoin-lommebøker er kjedekoden en 256-bits kryptografisk saltverdi som brukes til å generere underordnede nøkler fra en overordnet nøkkel, i henhold til BIP32-standarden. Kjedekoden brukes i kombinasjon med den overordnede nøkkelen og barnets indeks for å generere et nytt nøkkelpar (privat nøkkel og offentlig nøkkel) på en deterministisk måte uten å avsløre den overordnede nøkkelen eller andre avledede underordnede nøkler.

Derfor finnes det en unik kjedekode for hvert nøkkelpar. Kjedekoden oppnås enten ved å hashe lommebokens seed og ta den høyre halvdelen av bitene. I dette tilfellet kalles den en hovedkjedekode, som er knyttet til den private hovednøkkelen. Alternativt kan den fås ved å hashe en overordnet nøkkel med den overordnede kjedekoden og en indeks, og deretter beholde de høyre bitene. Dette kalles da en underordnet kjedekode.

Det er umulig å utlede nøkler uten å kjenne kjedekoden som er knyttet til hvert foreldrepar. Den introduserer pseudotilfeldige data i utledningsprosessen for å sikre at genereringen av kryptografiske nøkler forblir uforutsigbar for angripere, samtidig som den er deterministisk for lommebokinnehaveren.

> på engelsk kalles en "code de chaîne" for en "chain code", og en "code de chaîne maître" kalles en "master chain code"