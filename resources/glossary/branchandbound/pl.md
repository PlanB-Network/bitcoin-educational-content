---
term: BRANCH-AND-BOUND
---

Metoda używana do wybierania danych wejściowych w Bitcoin Core Wallet od wersji 0.17 i wynaleziona przez Murcha. Branch-and-Bound (BnB) to wyszukiwanie w celu znalezienia zestawu UTXO, który pasuje do dokładnej ilości wyjść, które mają zostać zrealizowane w transakcji, w celu zminimalizowania zmian i związanych z nimi opłat. Jego celem jest zmniejszenie kryterium marnotrawstwa, które uwzględnia zarówno natychmiastowy koszt, jak i przyszłe koszty oczekiwane w związku ze zmianą. Metoda ta jest bardziej dokładna pod względem opłat w porównaniu do poprzednich heurystyk, takich jak *Knapsack Solver*. Metoda *Branch-and-Bound* jest inspirowana metodą rozwiązywania problemów o tej samej nazwie, wynalezioną w 1960 roku przez Ailsę Land i Alison Harcourt.


> metoda ta jest również czasami nazywana "algorytmem Murcha" w odniesieniu do jej wynalazcy