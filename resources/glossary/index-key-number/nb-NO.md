---
begrep INDEKS (NØKKELNUMMER)

---
I forbindelse med en HD-lommebok refererer det til det løpenummeret som er tilordnet en underordnet nøkkel generert fra en overordnet nøkkel. Denne indeksen brukes i kombinasjon med den overordnede nøkkelen og den overordnede kjedekoden for å utlede unike underordnede nøkler på en deterministisk måte. Den muliggjør strukturert organisering og reproduserbar generering av flere søskenbarnøkkelpar fra samme overordnede nøkkel. Det er et 32-biters heltall som brukes i avledningsfunksjonen `HMAC-SHA512`. Dette nummeret skiller dermed mellom søskenbarnøkler i en HD-lommebok.