---
term: Knapsack solver

definition: Vana müntide valimise meetod Bitcoin Core'is, asendatud Branch-and-Bound meetodiga.
---
Vana meetod, mida kasutati müntide valimiseks Bitcoin Core'i rahakotis enne versiooni 0.17. Knapsack Solver üritab lahendada mündi valiku probleemi, valides iteratiivselt ja juhuslikult UTXOsid ning liites neid alamkogumite kaupa kokku, eesmärgiga minimeerida tasusid ja tehingu suurust. See meetod on vahepeal asendatud *Branch-and-Bound*-iga.