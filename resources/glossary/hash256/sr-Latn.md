---
term: HASH256
---

Kriptografska funkcija koja se koristi za razne primene na Bitcoin. Uključuje primenu SHA256 funkcije dvaput na ulazne podatke. Poruka se jednom prosledi kroz SHA256, a rezultat ove operacije koristi se kao ulaz za drugi prolaz kroz SHA256. Izlaz ove funkcije je stoga 256 bita.


$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$