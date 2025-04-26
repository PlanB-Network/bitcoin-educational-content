---
term: COIN SELECTION

---
Prosessen der en Bitcoin-lommebokprogramvare velger hvilke UTXO-er som skal brukes som input for å tilfredsstille outputen i en transaksjon. Metoden for myntvalg er viktig fordi den har konsekvenser for kostnadene ved en transaksjon og brukerens personvern. Målet er ofte å minimere antallet inndata som brukes, for å redusere transaksjonsstørrelsen og tilhørende gebyrer, samtidig som man prøver å bevare personvernet ved å unngå å slå sammen mynter fra ulike kilder (CIOH). Det finnes flere metoder for myntvalg, for eksempel *Knapsack Solver* eller *Branch-and-Bound*. Når myntvalget utføres manuelt av brukeren, kalles det "*Coin Control*".

> på engelsk kalles det "Coin Selection"