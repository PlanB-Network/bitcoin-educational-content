---
term: OP_CHECKSIGADD (0XBA)

---
Extrae los tres valores superiores de la pila: una `clave pública`, un `CScriptNum` `n`, y una `firma`. Si la firma no es el vector vacío y no es válida, el script termina con un error. Si la firma es válida o es el vector vacío (`OP_0`), se presentan dos escenarios:


- Si la firma es el vector vacío: un `CScriptNum` con el valor de `n` es empujado a la pila, y la ejecución continúa;
- Si la firma no es el vector vacío y sigue siendo válida: un `CScriptNum` con el valor de `n + 1` es empujado a la pila, y la ejecución continúa.

Para simplificar, `OP_CHECKSIGADD` realiza una operación similar a `OP_CHECKSIG`, pero en lugar de poner verdadero o falso en la pila, añade `1` al segundo valor en la parte superior de la pila si la firma es válida, o deja este valor sin cambios si la firma representa el vector vacío. `OP_CHECKSIGADD` permite la creación de las mismas políticas de multifirma en Tapscript que con `OP_CHECKMULTISIG` y `OP_CHECKMULTISIGVERIFY` pero de una manera verificable por lotes, lo que significa que elimina el proceso de búsqueda en la verificación de una multifirma tradicional y, por lo tanto, acelera la verificación al tiempo que reduce la carga operativa en las CPU de los nodos. Este opcode fue añadido en Tapscript únicamente para las necesidades de Taproot.