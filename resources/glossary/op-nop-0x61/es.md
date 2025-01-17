---
term: OP_NOP (0X61)

---
No produce ningún efecto en la pila ni en el estado del script. No realiza ningún movimiento, comprobación o modificación. Simplemente no hace nada a menos que se decida lo contrario a través de un soft fork. De hecho, desde su modificación por Satoshi Nakamoto en 2010, los comandos `OP_NOP` (`OP_NOP1` (`0XB0`) a `OP_NOP10` (`0XB9`)) se utilizan para añadir nuevos opcodes en forma de soft fork.

Así, `OP_NOP2` (`0XB1`) y `OP_NOP3` (`0XB2`) ya se han utilizado para implementar `OP_CHECKLOCKTIMEVERIFY` y `OP_CHECKSEQUENCEVERIFY`, respectivamente. Se utilizan en combinación con `OP_DROP` para eliminar de la pila los valores temporales asociados, permitiendo así que continúe la ejecución del script, esté o no actualizado el nodo. Los comandos `OP_NOP`, por lo tanto, permiten la inserción de un punto de interrupción en un script para comprobar condiciones adicionales que ya existen o que pueden añadirse con futuras bifurcaciones suaves. Desde Tapscript, el uso de `OP_NOP` ha sido reemplazado por el más eficiente `OP_SUCCESS`.