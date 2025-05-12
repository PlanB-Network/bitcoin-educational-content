---
term: INDEX (NØKKEL)
---

I forbindelse med en HD-portefølje refererer dette til det løpenummeret som er tilordnet en underordnet nøkkel generert fra en overordnet nøkkel. Denne indeksen brukes i kombinasjon med den overordnede nøkkelen og den overordnede strengkoden for å utlede unike underordnede nøkler på en deterministisk måte. Den muliggjør strukturert organisering og reproduserbar generering av flere par søskenbarnøkler fra en enkelt overordnet nøkkel. Det er et 32-biters heltall som brukes i avledningsfunksjonen `HMAC-SHA512`. Dette tallet kan brukes til å skille mellom underordnede nøkler i en HD-portefølje.