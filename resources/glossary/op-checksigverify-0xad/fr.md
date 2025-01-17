---
term: OP_CHECKSIGVERIFY (0XAD)
---

Effectue la même opération que `OP_CHECKSIG`, mais si la vérification de la signature échoue, le script s'arrête immédiatement avec une erreur et la transaction est donc invalide. Si la vérification réussit, le script continue sans pousser de valeur `1` (vrai) sur la pile. Pour résumer, `OP_CHECKSIGVERIFY` réalise l'opération `OP_CHECKSIG` suivie de `OP_VERIFY`. Cet opcode a été modifié dans Tapscript afin de vérifier des signatures de Schnorr.

