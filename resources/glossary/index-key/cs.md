---
term: Index (klíč)
definition: Sekvenční číslo přiřazené dceřinému klíči pro jeho odlišení od ostatních v HD peněžence.
---

V kontextu portfolia HD označuje pořadové číslo přiřazené podřízenému klíči vygenerovanému z nadřazeného klíče. Tento index se používá v kombinaci s rodičovským klíčem a kódem rodičovského řetězce k deterministickému odvození jedinečných podřízených klíčů. Umožňuje strukturovanou organizaci a reprodukovatelné generování více párů sesterských podřízených klíčů z jednoho rodičovského klíče. Jedná se o 32bitové celé číslo používané v odvozovací funkci `HMAC-SHA512`. Toto číslo lze použít k rozlišení podřízených klíčů v rámci portfolia HD.