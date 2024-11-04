---
term: OBSOLÈTE (BLOC)
---

Fait référence à un bloc sans enfant : un bloc valide, mais exclu de la chaîne principale de Bitcoin. Il se produit lorsque deux mineurs trouvent un bloc valide sur une même hauteur de chaîne durant un court laps de temps et le diffusent sur le réseau. Les nœuds finissent par choisir un seul bloc à inclure dans la chaîne, selon le principe de la chaîne avec le plus de travail accumulé, rendant l'autre « obsolète ». Le processus menant à la production d'un bloc obsolète est le suivant :
* Deux mineurs trouvent un bloc valide à une même hauteur de chaîne durant un court intervalle de temps. Nommons-les `Bloc A` et `Bloc B` ;
* Chacun diffuse son bloc au réseau de nœuds Bitcoin. Chaque nœud dispose maintenant de 2 blocs à une même hauteur. Il existe donc deux chaînes valides ;
* Les mineurs continuent de chercher des preuves de travail pour les blocs suivants, mais pour ce faire, ils doivent obligatoirement choisir un seul bloc entre le `Bloc A` et le `Bloc B` au-dessus duquel ils vont miner ;
* Un mineur trouve finalement un bloc valide au-dessus du `Bloc B`. Appelons le `Bloc B+1` ;
* Il diffuse `Bloc B+1` aux nœuds du réseau ;
* Puisque les nœuds suivent la chaîne la plus longue (avec le plus de travail accumulé), ils vont estimer que la `Chaîne B` est celle qu'il faut suivre ;
* Ils vont abandonner le `Bloc A` qui ne fait plus partie de la chaîne principale. Il est donc devenu un bloc obsolète.

![](../../dictionnaire/assets/9.webp)

> ► *En anglais, on parle de « Stale Block ». En français, on peut également dire « bloc périmé » ou « bloc abandonné ». Même si je ne suis pas en accord avec cet usage, certains bitcoiners utilisent le terme de « bloc orphelin » pour désigner ce qui est en réalité un bloc obsolète.*

