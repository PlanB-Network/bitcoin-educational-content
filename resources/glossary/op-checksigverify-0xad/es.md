---
term: OP_CHECKSIGVERIFY (0XAD)
---

Realiza la misma operación que `OP_CHECKSIG`, pero si la verificación de la firma falla, el script se detiene inmediatamente con un error y la transacción se considera inválida. Si la verificación tiene éxito, el script continúa sin añadir un valor `1` (verdadero) en la pila. En resumen, `OP_CHECKSIGVERIFY` realiza la operación `OP_CHECKSIG` seguido por `OP_VERIFY`. Este opcode fue modificado en Tapscript para verificar firmas Schnorr.