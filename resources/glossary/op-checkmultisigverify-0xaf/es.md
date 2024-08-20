---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Combina un `OP_CHECKMULTISIG` y un `OP_VERIFY`. Toma múltiples firmas y claves públicas para verificar que `M` de `N` firmas sean válidas, justo como lo hace `OP_CHECKMULTISIG`. Luego, al igual que `OP_VERIFY`, si la verificación falla, el script se detiene inmediatamente con un error. Si la verificación es exitosa, el script continúa sin añadir ningún valor a la pila. Este opcode fue eliminado en Tapscript.