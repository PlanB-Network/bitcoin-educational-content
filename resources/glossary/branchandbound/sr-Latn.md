---
term: BRANCH-AND-BOUND
---

Metod korišćen za odabir ulaza u Bitcoin Core Wallet od verzije 0.17 i izumljen od strane Murch-a. Branch-and-Bound (BnB) je pretraga za pronalaženje skupa UTXO-a koji odgovara tačnom iznosu izlaza koji treba ispuniti u transakciji, kako bi se minimizirala promena i povezane naknade. Njegov cilj je smanjenje kriterijuma otpada koji uzima u obzir i trenutne troškove i očekivane buduće troškove za promenu. Ova metoda je preciznija u smislu naknada u poređenju sa prethodnim heuristikama kao što je *Knapsack Solver*. *Branch-and-Bound* je inspirisan metodom rešavanja problema istog imena, koju su 1960. godine izumeli Ailsa Land i Alison Harcourt.


> ► *Ovaj metod se ponekad naziva i "Murchov algoritam" u znak priznanja njegovom pronalazaču.*