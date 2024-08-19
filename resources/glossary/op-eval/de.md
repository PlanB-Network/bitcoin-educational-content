---
term: OP_EVAL
---

Opcode, vorgeschlagen von Gavin Andresen im Jahr 2011. Er nimmt das Skript, das sich oben auf dem Stapel befindet, führt es aus, als ob es Teil des `scriptPubKey` wäre, und legt sein Ergebnis auf den Stapel. `OP_EVAL` wurde aufgrund von Bedenken bezüglich der Komplexität dieses Opcode aufgegeben, die letztendlich durch P2SH überholt werden würde.