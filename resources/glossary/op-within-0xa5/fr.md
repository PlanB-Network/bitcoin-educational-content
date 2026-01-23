---
term: OP_WITHIN (0XA5)
definition: Opcode vérifiant si une valeur se trouve dans un intervalle défini par deux autres valeurs.
---

Vérifie si le premier élément en haut de la pile se trouve dans l'intervalle défini par les deuxième et troisième éléments supérieurs. Autrement dit, `OP_WITHIN` vérifie si le premier élément est supérieur ou égal au deuxième et inférieur au troisième. Si cette condition est vraie, il pousse `1` (vrai) sur la pile, sinon, il pousse `0` (faux).
