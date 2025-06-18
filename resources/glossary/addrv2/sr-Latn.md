---
term: ADDRV2
---

Predložena evolucija sa BIP155 `addr` poruke na Bitcoin mreži. `addr` poruka je korišćena za emitovanje adresa čvorova koji prihvataju dolazne veze, ali je bila ograničena na 128-bitne adrese. Ova veličina je bila adekvatna za IPv6, IPv4 i Tor V2 adrese, ali nedovoljna za druge protokole. Ažurirana verzija `addrv2` je dizajnirana da podrži duže adrese, uključujući 256-bitne Tor v3 skrivene servise, kao i druge mrežne protokole kao što su I2P ili budući protokoli.