---
term: NODE
---

W sieci Bitcoin węzeł (lub "node" w języku angielskim) to komputer z uruchomionym klientem protokołu Bitcoin (takim jak na przykład Bitcoin Core). Uczestniczy on w sieci, utrzymując kopię Blockchain, przekazując i weryfikując transakcje i nowe bloki oraz opcjonalnie uczestnicząc w procesie Mining. Suma wszystkich węzłów Bitcoin reprezentuje samą sieć Bitcoin.


W Bitcoin istnieje kilka rodzajów węzłów, w tym węzły pełne i węzły lekkie. Pełne węzły przechowują pełną kopię Blockchain, weryfikują wszystkie transakcje i bloki zgodnie z zasadami konsensusu i aktywnie uczestniczą w rozpowszechnianiu transakcji i bloków w całej sieci. Z drugiej strony, lekkie węzły lub węzły SPV (*Simple Payment Verification*) przechowują tylko nagłówki bloków i polegają na pełnych węzłach w celu uzyskania informacji o transakcjach.


> niektórzy rozróżniają również tak zwane "przycięte węzły" ("pruned node" w języku angielskim). Są to pełne węzły, które pobierają i weryfikują wszystkie bloki z bloku Genesis, ale przechowują w pamięci tylko najnowsze bloki