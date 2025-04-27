---
term: BIP0330
---

Proposition connue sous le nom de « *Erlay* » qui a pour objectif d'optimiser la propagation des transactions non confirmées dans le réseau Bitcoin. Actuellement, les transactions sont diffusées à tous les pairs d’un nœud, ce qui entraîne des redondances et une surutilisation de la bande passante. Le BIP330 propose de limiter cette diffusion à 8 pairs par défaut, puis d'utiliser un mécanisme de réconciliation pour partager efficacement les transactions manquantes. Erlay réduit la consommation de bande passante d'environ 40 %. Il permet également de ne pas avoir une augmentation linéaire de la consommation de bande passante avec le nombre de pairs connectés au nœud.
