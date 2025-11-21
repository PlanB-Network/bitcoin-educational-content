---
term: PATHFINDING
---

Proces používaný uzlem k určení optimální cesty pro směrování platby v síti kanálů Lightning. Určení cesty provádí uzel plátce, který musí vybrat nejvhodnější mezilehlé uzly pro dosažení příjemce. Tento výběr je založen na řadě kritérií, jako jsou poplatky, kapacita kanálu a časové zámky.


Algoritmy pro hledání cesty vytvářejí graf topologie sítě z drbů a vyhodnocují různé možné trasy mezi uzlem plátce a uzlem příjemce. Tyto trasy jsou seřazeny od nejlepší po nejhorší podle různých kritérií. Uzel pak tyto trasy testuje, dokud se mu nepodaří provést platbu po jedné z nich.