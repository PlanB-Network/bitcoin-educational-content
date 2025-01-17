---
term: CLÉ PUBLIQUE COMPRESSÉE
---

Une clé publique est utilisée dans les scripts (soit directement sous la forme d'une clé publique, soit sous la forme d'une adresse) pour recevoir et sécuriser des bitcoins. Une clé publique brute est représentée par un point sur une courbe elliptique, composé de deux coordonnées (`x, y`) chacune de 256 bits. En format brut, une clé publique mesure donc 512 bits, sans compter l'octet supplémentaire pour identifier le format. Une clé publique compressée, en revanche, est une forme plus compacte de représentation d'une clé publique. Elle utilise seulement la coordonnée `x` et un préfixe (`02` ou `03`) qui indique la parité de la coordonnée `y` (pair ou impair). 

Si l'on simplifie cela au corps des réels, la courbe elliptique étant symétrique par rapport à l’axe des abscisses, pour tout point $P$ (`x, y`) sur la courbe, il existe un point $P'$ (`x, -y`) qui sera également sur cette même courbe. Cela signifie qu'à chaque `x` correspondent seulement deux valeurs possibles de `y`, positive et négative. Par exemple, pour une abscisse `x` donnée, il y aurait deux points $P1$ et $P2$ sur la courbe elliptique, qui partagent la même abscisse, mais avec des ordonnées opposées :

![](../../dictionnaire/assets/29.webp)
Pour choisir entre les deux points potentiels sur la courbe, on ajoute à `x` un préfixe spécifiant quel `y` choisir. Cette méthode permet de réduire la taille d'une clé publique de 520 bits à seulement 264 bits (8 bits de préfixe + 256 bits pour `x`). Cette représentation est connue sous le nom de forme compressée de la clé publique.

Cependant, dans le cadre de la cryptographie sur les courbes elliptiques, nous utilisons non pas les réels, mais un corps fini d'ordre `p` (un nombre premier). Dans ce contexte, le « signe » de `y` est déterminé par sa parité, c'est-à-dire si `y` est pair ou impair. Le préfixe `0x02` indique alors un `y` pair, tandis que `0x03` indique un `y` impair.

Considérons l'exemple suivant d'une clé publique brute (un point sur la courbe elliptique) en hexadécimal :
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

On peut isoler le préfixe, `x`, et `y` :
```plaintext
Préfixe = 04
x = 678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
y = 49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Pour déterminer la parité de `y`, on examine le dernier caractère hexadécimal de `y` :
```plaintext
Base 16 (hexadécimal) : f
Base 10 (décimal) : 15
y est impair
```

Le préfixe pour la clé publique compressée sera `03`. La clé publique compressée en hexadécimal devient :
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

