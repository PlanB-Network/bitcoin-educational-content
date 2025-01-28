---
term: FORMBARHET (TRANSAKSJON)

---
Refererer til muligheten til å endre strukturen til en Bitcoin-transaksjon uten å endre effekten av den, men samtidig endre transaksjonsidentifikatoren (*TXID*). Denne egenskapen kan utnyttes til å villede interessenter om statusen til en transaksjon, og dermed forårsake problemer som dobbeltbruk. Fleksibiliteten i den digitale signaturen som ble brukt, gjorde det mulig å manipulere. SegWit soft fork ble introdusert for å forhindre at Bitcoin-transaksjoner kunne manipuleres, noe som gjorde implementeringen av Lightning Network komplisert. Dette oppnås ved å fjerne de formbare dataene fra transaksjonen fra TXID-beregningen.

> selv om det er sjeldent, brukes begrepet "foranderlighet" noen ganger om det samme konseptet