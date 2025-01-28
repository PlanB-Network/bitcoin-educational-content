---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Combina un `OP_CHECKMULTISIG` y un `OP_VERIFY`. Toma múltiples firmas y claves públicas para verificar que `M` de `N` firmas son válidas, tal y como hace `OP_CHECKMULTISIG`. Entonces, al igual que `OP_VERIFY`, si la verificación falla, el script se detiene inmediatamente con un error. Si la verificación tiene éxito, el script continúa sin poner ningún valor en la pila. Este opcode fue eliminado en Tapscript.