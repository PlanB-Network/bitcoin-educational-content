---
term: LUCK
---

Indicateur utilisé dans les pools de minage pour mesurer la performance d'une pool par rapport à ses attentes théoriques. Comme son nom l'indique, il évalue la chance qu'a la pool de trouver un bloc. La luck est calculée en comparant le nombre de shares théoriquement nécessaire pour trouver un bloc valide, établi sur la difficulté actuelle de Bitcoin, au nombre réel de shares produites pour trouver ce bloc. Un nombre de shares inférieur à celui attendu indique une bonne chance, tandis qu'un nombre supérieur indique une mauvaise chance.

En mettant en rapport la difficulté sur Bitcoin avec son nombre de shares produites chaque seconde et la difficulté de chaque shares, la pool peut calculer le nombre de shares qui sont théoriquement nécessaires pour trouver un bloc valide. Par exemple, supposons que théoriquement, il faut 100 000 shares pour qu'une pool trouve un bloc. Si la pool en réalité en produit 200 000 avant de trouver un bloc, sa luck est de 50 % :

```text
100 000 / 200 000 = 0.5 = 50 %
```

À l'inverse, si cette pool a trouvé un bloc valide après avoir seulement produit 50 000 shares, alors sa luck est de 200 % :

```text
100 000 / 50 000 = 2 = 200 %
```

La luck est un indicateur qui ne peut être actualisé qu'après la découverte d'un bloc par la pool, ce qui en fait un indicateur statique mis à jour périodiquement.

