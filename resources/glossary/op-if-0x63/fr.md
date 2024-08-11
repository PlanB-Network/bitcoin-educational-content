---
term: OP_IF (0X63)
---

Exécute la portion suivante du script si la valeur au sommet de la pile est non nulle (vraie). Si la valeur est nulle (fausse), ces opérations sont sautées, passant directement à celles après `OP_ELSE`, s'il est présent. `OP_IF` permet de lancer une structure de contrôle conditionnelle dans un script. Il détermine le flux de contrôle dans un script en fonction d'une condition fournie au moment de l'exécution de la transaction. `OP_IF` s'utilise avec `OP_ELSE` et `OP_ENDIF` de la manière suivante : 

```text
<condition>
OP_IF
<opérations si la condition est vraie>
OP_ELSE
<opérations si la condition est fausse>
OP_ENDIF
```

