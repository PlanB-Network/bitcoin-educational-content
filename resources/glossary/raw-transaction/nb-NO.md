---
term: RÅ TRANSAKSJON

---
En Bitcoin-transaksjon som er bygget og signert, og som eksisterer i sin binære form. En rå transaksjon (*raw TX*) er den endelige representasjonen av en transaksjon, rett før den sendes ut på nettverket. Denne transaksjonen inneholder all nødvendig informasjon for at den skal kunne inkluderes i en blokk:


- Versjonen;
- Flagget;
- Inngangene;
- Resultatene;
- Låsetiden;
- Vitnet.

Det som omtales som en "*råtransaksjon*", representerer rådataene som sendes gjennom SHA256-hashfunksjonen to ganger for å generere transaksjonens TXID. Disse dataene brukes deretter i blokkens Merkle-tre for å integrere transaksjonen i blokkjeden.

> dette konseptet kalles også noen ganger "Serialized Transaction". På fransk kan disse begrepene oversettes med henholdsvis "transaction brute" og "transaction sérialisée"