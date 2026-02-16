---
term: Jednorázová pečeť
definition: Kryptografický mechanismus zaručující jedinečnost validace, používaný v RGB proti double-spendingu.
---

Označuje kryptografický slib Commitment týkající se dosud neznámé zprávy, která bude v budoucnu odhalena pouze jednou a musí být přístupná celému určenému publiku. Cílem tohoto mechanismu je zabránit vytvoření více konkurenčních závazků pro tentýž Seal, a tím zaručit jedinečnost každého ověření. Zavedením tohoto omezení na jedno použití se Single-Use Seal používá na RGB, aby se zabránilo použití Double-spending.