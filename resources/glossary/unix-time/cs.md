---
term: UNIX TIME
---

Unix Time nebo Unixový časový otisk představuje počet sekund, které uplynuly od 1. ledna 1970 o půlnoci UTC (Unix Epoch). Tento systém se používá v operačních systémech Unix a jejich derivátech pro univerzální a standardizované označování času. Umožňuje synchronizaci hodin a správu časově závislých událostí bez ohledu na časové pásma.

V kontextu Bitcoinu se používá pro místní hodiny uzlů a tedy pro výpočet NAT (Network-Adjusted Time - Síťově upravený čas). Síťově upravený čas je medián časů uzlů vypočítaný lokálně každým uzlem, a tato reference je pak použita pro ověření platnosti časových otisků bloků. Skutečně, aby byl blok uzlem přijat, musí jeho časový otisk být mezi MTP (Median Time Past posledních 11 těžených bloků) a NAT plus 2 hodiny:

```text
MTP < Platný časový otisk < (NAT + 2h)
```

Unixový čas se také používá pro nastavení časových zámků, když jsou založeny na reálném čase, spíše než na počtu bloků.