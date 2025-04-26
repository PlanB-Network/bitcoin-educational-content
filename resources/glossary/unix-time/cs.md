---
term: UNIX TIME

---
Čas Unixu nebo časové razítko Unixu představuje počet sekund, které uplynuly od 1. ledna 1970 o půlnoci UTC (epocha Unixu). Tento systém se používá v operačních systémech Unix a jejich odvozeninách k univerzálnímu a standardizovanému označování času. Umožňuje synchronizaci hodin a správu událostí založených na čase bez ohledu na časová pásma.

V kontextu Bitcoinu se používá pro místní hodiny uzlů, a tedy pro výpočet NAT (Network-Adjusted Time). Síťově upravený čas je mediánem časů uzlů vypočtených lokálně každým uzlem a tato reference se pak používá k ověření platnosti časových značek bloků. Aby byl blok uzlem přijat, musí se jeho časová značka skutečně nacházet mezi MTP (mediánem času minulého z posledních 11 vytěžených bloků) a NAT plus 2 hodiny:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unixový čas se také používá k vytváření časových zámků, pokud jsou založeny na reálném čase, nikoli na počtu bloků.