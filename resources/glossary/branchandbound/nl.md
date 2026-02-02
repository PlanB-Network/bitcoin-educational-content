---
term: Branch-and-bound
definition: Algoritme voor muntselectie in Bitcoin Core om wisselgeld en transactiekosten te minimaliseren.
---

Methode gebruikt voor het selecteren van inputs in de Bitcoin core Wallet sinds versie 0.17 en uitgevonden door Murch. Branch-and-Bound (BnB) is een zoektocht om een set UTXO's te vinden die overeenkomt met de exacte hoeveelheid outputs die moeten worden vervuld in een transactie, om de verandering en de bijbehorende kosten te minimaliseren. Het doel is om een afvalcriterium te verminderen dat rekening houdt met zowel de onmiddellijke kosten als de verwachte toekomstige kosten voor de wijziging. Deze methode is nauwkeuriger in termen van kosten in vergelijking met eerdere heuristieken zoals de *Knapsack Solver*. De *Branch-and-Bound* is geïnspireerd op de gelijknamige probleemoplossingsmethode, in 1960 uitgevonden door Ailsa Land en Alison Harcourt.


> ► *Deze methode wordt soms ook "Murch's Algoritme" genoemd, naar de uitvinder ervan.*