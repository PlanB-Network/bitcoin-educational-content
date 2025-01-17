---
term: RÉUTILISATION D'ADRESSE (INT)
---

On dit d'une réutilisation d'adresse qu'elle est "interne" lorsqu'elle survient au sein d'une même transaction en input et en output. Dans cette configuration, la réutilisation d'adresse interne est une heuristique d'analyse de chaîne qui permet d'émettre une hypothèse vraisemblable sur le change de la transaction. En effet, s'il y a deux outputs et que l'un d'eux utilise la même adresse de réception qu'en input, alors il est vraisemblable que le second output quitte la possession de l'utilisateur initial. L'output avec l'adresse réutilisée représente vraisemblablement le change.

![](../../dictionnaire/assets/10.webp)

