---
term: OP_TOALTSTACK (0X6B)

definition: Opcode som flytter toppen av hovedstakken til den alternative stakken.
---
Tar toppen av hovedstakken (*main stack*) og flytter den til den alternative stakken (*alt stack*). Denne opkoden brukes til å lagre data midlertidig for senere bruk i skriptet. Det flyttede elementet fjernes dermed fra hovedstakken. `OP_FROMALTSTACK` vil deretter bli brukt til å legge det tilbake på toppen av hovedstakken.