---
term: OP_CHECKSIG (0XAC)

---
Verifica la validez de una firma frente a una clave pública determinada. Toma los dos elementos superiores de la pila: la firma y la clave pública, y evalúa si la firma es correcta para el hash de la transacción y la clave pública especificada. Si la verificación tiene éxito, coloca el valor `1` (verdadero) en la pila, de lo contrario `0` (falso). Este opcode fue modificado en Tapscript para verificar firmas Schnorr.