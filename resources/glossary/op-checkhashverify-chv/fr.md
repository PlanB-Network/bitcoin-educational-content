---
term: OP_CHECKHASHVERIFY (CHV)
definition: Opcode proposé en 2012 pour des fonctionnalités similaires à P2SH, jamais implémenté.
---

Nouvel opcode proposé en 2012 dans le BIP17 par Luke Dashjr qui permet de disposer des mêmes fonctionnalités que `OP_EVAL` ou P2SH. Il aurait dû permettre de hacher la fin du `scriptSig`, de comparer le résultat avec le haut de la pile et rendre la transaction invalide si les deux hachages ne correspondaient pas. Cet opcode n'a jamais été implémenté.
