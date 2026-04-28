---
term: Knapsack solver
definition: Gammal metod för mynturval i Bitcoin Core, ersatt av Branch-and-Bound.
---

En gammal metod som användes för att välja mynt i Bitcoin Core Wallet före version 0.17. Knapsack Solver försöker lösa myntvalsproblemet genom att iterativt och slumpmässigt välja UTXO:er och lägga ihop dem i delmängder, med målet att minimera avgifterna och storleken på transaktionen. Denna metod har sedan dess ersatts av *Branch-and-Bound*.