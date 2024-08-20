---
term: OP_CHECKSIG (0XAC)
---

Verifica la validez de una firma contra una clave pública dada. Toma los dos elementos superiores de la pila: la firma y la clave pública, y evalúa si la firma es correcta para el hash de la transacción y la clave pública especificada. Si la verificación es exitosa, empuja el valor `1` (verdadero) a la pila, de lo contrario `0` (falso). Este opcode fue modificado en Tapscript para verificar firmas Schnorr.