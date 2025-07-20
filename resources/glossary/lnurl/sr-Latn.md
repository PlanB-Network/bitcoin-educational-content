---
term: LNURL
---

Protokol komunikacije koji specificira skup funkcija dizajniranih da pojednostave interakcije između Lightning čvorova i klijenata, kao i aplikacija trećih strana. Ovaj protokol je zasnovan na HTTP-u i omogućava kreiranje linkova za razne operacije, kao što su zahtev za plaćanje, zahtev za povlačenje ili druge funkcionalnosti koje poboljšavaju korisničko iskustvo. Svaki LNURL je URL kodiran u bech32 sa prefiksom `lnurl`, koji, kada se skenira, pokreće niz automatskih akcija na Lightning Wallet.


Na primer, LNURL-withdraw (LUD-03) vam omogućava da povučete sredstva sa usluge skeniranjem QR koda, bez potrebe da ručno generate Invoice. Ili LNURL-auth (LUD-04) vam omogućava da se povežete na online usluge koristeći privatni ključ na vašem Lightning Wallet umesto lozinke.