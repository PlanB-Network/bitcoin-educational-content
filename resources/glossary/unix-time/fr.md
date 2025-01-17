---
term: UNIX (HEURE)
---

L'Heure Unix ou Temps Unix représente le nombre de secondes écoulées depuis le 1er janvier 1970 à minuit UTC (Époque Unix). Ce système est utilisé dans les systèmes d'exploitation Unix et dérivés pour marquer le temps de manière universelle et standardisée. Il permet la synchronisation des horloges et la gestion des événements dans le temps, indépendamment des fuseaux horaires.

Dans le cadre de Bitcoin, on l'utilise pour l'horloge locale des nœuds, et donc pour le calcul du NAT. Le network-adjusted time est une médiane du temps des nœuds calculée en local par chaque nœud, et ce référentiel est ensuite utilisé pour vérifier la validité des horodatages des blocs. En effet, pour qu'un bloc soit accepté par un nœud, son horodatage doit se situer entre le MTP (temps médian des 11 derniers blocs minés) et le NAT plus 2 heures :

```text
MTP < Horodatage valide < (NAT + 2h)
```

On utilise également l'Heure Unix pour établir des timelocks, lorsque ceux-ci se basent sur l'heure réelle, et non pas sur un nombre de blocs. 

