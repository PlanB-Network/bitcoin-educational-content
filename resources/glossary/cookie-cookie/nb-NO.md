---
term: INFORMASJONSKAPSEL (.COOKIE)

---
Fil som brukes til RPC (*Remote Procedure Call*)-autentisering i Bitcoin Core. Når bitcoind starter, genererer den en unik informasjonskapsel for autentisering og lagrer den i denne filen. Klienter eller skript som ønsker å samhandle med bitcoind via RPC-grensesnittet, kan bruke denne informasjonskapselen til å autentisere seg på en sikker måte. Denne mekanismen muliggjør sikker kommunikasjon mellom bitcoind og eksterne applikasjoner (som for eksempel lommebokprogramvare), uten å kreve manuell håndtering av brukernavn og passord. Filen `.cookie` regenereres ved hver omstart av bitcoind og slettes ved avslutning.