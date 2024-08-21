---
term: CIOH
---

Zkratka pro "*Common Input Ownership Heuristic*" (Heuristika společného vlastnictví vstupů). Jedná se o heuristiku používanou v oblasti analýzy Bitcoinového řetězce, která předpokládá, že všechny vstupy transakce patří téže entitě nebo uživateli. Při pozorování veřejných dat Bitcoinové transakce, a jsou-li zaznamenány vícečetné vstupy, pak, pokud neexistují žádné vzorce nebo jiné informace, které by to vyvrátily, lze odhadnout, že všechny vstupy této transakce patřily jedné osobě (nebo entitě).

Tuto analytickou heuristiku objevil sám Satoshi Nakamoto, který ji diskutuje v části 10 Bílé knihy:

> "Avšak spojení je nevyhnutelné u transakcí s více vstupy, které nutně odhalují, že jejich vstupy vlastnil tentýž majitel. Riziko je, že pokud je odhalen majitel klíče, spojení mohou odhalit další transakce, které patřily témuž majiteli." - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konzultováno na https://bitcoin.org/bitcoin.pdf.

I dnes zůstává CIOH hlavní heuristikou používanou společnostmi pro analýzu řetězce, společně s opětovným používáním adres.

![](../../dictionnaire/assets/13.png)

> ► *V angličtině lze "CIOH" přeložit jako "Common Input Ownership Heuristic".*