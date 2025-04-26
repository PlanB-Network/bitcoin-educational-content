---
term: BLOCK

---
Datastruktur i Bitcoin-systemet. En blokk inneholder et sett med gyldige transaksjoner og metadata i overskriften. Hver blokk er knyttet til den neste ved hjelp av hashen i overskriften, og danner dermed blokkjeden. Blokkjeden fungerer som en tidsstemplingsserver som gjør det mulig for alle brukere å kjenne til alle tidligere transaksjoner, slik at de kan verifisere at en transaksjon ikke eksisterer og forhindre dobbeltbruk. Transaksjonene er organisert i et Merkle-tre. Denne kryptografiske akkumulatoren gjør det mulig å produsere et sammendrag av alle transaksjonene i en blokk, kalt "Merkle-roten" Overskriften til en blokk inneholder seks elementer:


- Versjonen av blokken;
- Avtrykket av den forrige blokken;
- Roten til Merkle-treet av transaksjoner;
- Tidsstempelet for blokken;
- Vanskelighetsgraden er målet;
- Noncen.

For at en blokk skal være gyldig, må den ha en header som, når den er hashet med `SHA256d`, gir et digest som er mindre enn eller lik vanskelighetsmålet.