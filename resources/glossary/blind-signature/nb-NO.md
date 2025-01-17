---
term: BLIND SIGNATUR

---
Chaums blindsignaturer er en form for digital signatur der utstederen av signaturen ikke kjenner innholdet i meldingen han eller hun signerer. Signaturen kan imidlertid senere verifiseres med den opprinnelige meldingen. Denne teknikken ble utviklet av kryptografen David Chaum i 1983.

Et eksempel er en bedrift som ønsker å autentisere et konfidensielt dokument, for eksempel en kontrakt, uten å avsløre innholdet. Bedriften bruker en maskeringsprosess som kryptografisk omdanner originaldokumentet på en reversibel måte. Det modifiserte dokumentet sendes til en sertifiseringsinstans som bruker en blind signatur uten å kjenne til det underliggende innholdet. Etter å ha mottatt det maskerte, signerte dokumentet, fjerner selskapet maskeringen av signaturen. Resultatet er et originaldokument som er autentisert med autoritetens signatur, uten at autoriteten noen gang har sett det opprinnelige innholdet.

Chaums blindsignaturer gjør det dermed mulig å sertifisere et dokuments autentisitet uten å kjenne innholdet, noe som sikrer både konfidensialiteten til brukerens data og integriteten til det signerte dokumentet.

I Bitcoin brukes denne protokollen i systemer med chaumianske banker som et overlegg (Cashu, Fedimint osv.), men spesielt i chaumianske coinjoin-protokoller, for å sikre at koordinatoren ikke er i stand til å koble en inngang til en utgang.