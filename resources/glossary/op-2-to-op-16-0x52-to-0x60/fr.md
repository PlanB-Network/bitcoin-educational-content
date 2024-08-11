---
term: OP_2 À OP_16 (0X52 À 0X60)
---

Les opcodes de `OP_2` jusqu'à `OP_16` poussent les valeurs numériques respectives de 2 à 16 sur la pile. On les utilise pour simplifier les scripts en permettant l'insertion de petites valeurs numériques. Ce type d'opcode est notamment utilisé dans les scripts multisignatures. Voici un exemple de `scriptPubKey` pour un multisig 2/3 : 

```text
OP_2
<Clé publique A>
<Clé publique B>
<Clé publique C>
OP_3
OP_CHECKMULTISIG
```

> ► *Tous ces opcodes sont parfois également nommés OP_PUSHNUM_N.*

