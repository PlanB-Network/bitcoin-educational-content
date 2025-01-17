---
term: OP_TOALTSTACK (0X6B)
---

Prend le sommet de la pile principale (*main stack*) et le déplace vers la pile alternative (*alt stack*). Cet opcode permet de stocker temporairement des données à part pour une utilisation ultérieure dans le script. L'élément déplacé est donc supprimé de la pile principale. On utilisera ensuite `OP_FROMALTSTACK` pour le remettre au sommet de la pile principale.

