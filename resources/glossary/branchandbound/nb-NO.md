---
term: GREN-OG-BUNDET

---
Metode som brukes for å velge innganger i Bitcoin Core-lommeboken siden versjon 0.17, og som ble oppfunnet av Murch. Branch-and-Bound (BnB) er et søk for å finne et sett med UTXO-er som samsvarer med den nøyaktige mengden utganger som skal oppfylles i en transaksjon, for å minimere endring og tilhørende avgifter. Målet er å redusere et sløsingskriterium som tar hensyn til både de umiddelbare kostnadene og de forventede fremtidige kostnadene for endringen. Denne metoden er mer nøyaktig når det gjelder gebyrer sammenlignet med tidligere heuristikker som *Knapsack Solver*. *Branch-and-Bound* er inspirert av problemløsningsmetoden med samme navn, som ble oppfunnet i 1960 av Ailsa Land og Alison Harcourt.

> denne metoden kalles også noen ganger "Murchs algoritme", etter oppfinneren av den