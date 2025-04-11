---
term: ČAS UPRAVENÝ PODLE SÍTĚ (NAT)

---
Odhad univerzálního času na základě hodin uzlů sítě. Každý uzel vypočítá svůj NAT tak, že vezme medián časových rozdílů mezi svými místními hodinami (UTC) a hodinami uzlů, ke kterým je připojen, a poté k mediánu těchto rozdílů přičte své místní hodiny, maximálně však 70 minut. Čas upravený podle sítě je tedy mediánem časů uzlů vypočtených lokálně každým uzlem. Tento referenční rámec se pak používá k ověření platnosti časových značek bloků. Aby byl blok uzlem přijat, musí se jeho časová značka nacházet mezi MTP (medián času posledních 11 vytěžených bloků) a NAT plus 2 hodiny:

```text
MTP < Valid Timestamp < (NAT + 2h)
```