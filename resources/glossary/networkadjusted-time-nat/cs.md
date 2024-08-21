---
term: NETWORK-ADJUSTED TIME (NAT)
---

Odhad univerzálního času založený na hodinách uzlů sítě. Každý uzel vypočítá svůj NAT tak, že vezme medián časových rozdílů mezi svými lokálními hodinami (UTC) a hodinami uzlů, ke kterým je připojen, a poté k tomuto mediánu přičte své lokální hodiny, až do maximálního rozdílu 70 minut. Síťově upravený čas je tedy medián časů uzlů vypočítaný lokálně každým uzlem. Tento referenční rámec je pak použit k ověření platnosti časových razítek bloků. Skutečně, aby byl blok uzlem přijat, jeho časové razítko musí být mezi MTP (medián času posledních 11 těžených bloků) a NAT plus 2 hodiny:

```text
MTP < Platné Časové Razítko < (NAT + 2h)
```