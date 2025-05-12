---
term: LNURL
---

Kommunikasjonsprotokoll som spesifiserer et sett med funksjoner som er utformet for å forenkle samhandlingen mellom Lightning-noder og klienter, samt tredjepartsapplikasjoner. Denne protokollen er basert på HTTP og gjør det mulig å opprette lenker for ulike operasjoner, for eksempel en betalingsforespørsel, en uttaksforespørsel eller andre funksjoner som forbedrer brukeropplevelsen. Hver LNURL er en URL kodet i bech32 med prefikset `lnurl`, som, når den skannes, utløser en rekke automatiske handlinger på Lightning Wallet.


Med LNURL-withdraw (LUD-03) kan du for eksempel ta ut penger fra en tjeneste ved å skanne en QR-kode, uten å måtte bruke en generate eller Invoice manuelt. Eller LNURL-auth (LUD-04) lar deg koble deg til nettbaserte tjenester ved hjelp av en privat nøkkel på Lightning Wallet i stedet for et passord.