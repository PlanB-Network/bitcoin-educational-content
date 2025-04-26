---
term: HASH256

---
Kryptografisk funksjon som brukes til ulike applikasjoner på Bitcoin. Det innebærer å bruke SHA256-funksjonen to ganger på inngangsdataene. Meldingen sendes gjennom SHA256 én gang, og resultatet av denne operasjonen brukes som input for en andre passering gjennom SHA256. Resultatet av denne funksjonen er derfor 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$$\text{SHA256}(x)