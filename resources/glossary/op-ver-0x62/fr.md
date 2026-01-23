---
term: OP_VER (0X62)
definition: Opcode désactivé qui poussait la version du client, converti en OP_SUCCESS.
---

Permettait de pousser la version du client sur la pile. Cet opcode a été désactivé, car s'il avait été utilisé, chaque mise à jour aurait conduit à un hard fork. Le BIP342 a modifié cet opcode en `OP_SUCCESS`.
