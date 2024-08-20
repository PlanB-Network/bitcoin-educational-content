---
term: OP_NOP (0X61)
---

No produce ningún efecto en la pila o en el estado del script. No realiza movimientos, comprobaciones ni modificaciones. Simplemente no hace nada a menos que se decida lo contrario mediante un soft fork. De hecho, desde su modificación por Satoshi Nakamoto en 2010, los comandos `OP_NOP` (`OP_NOP1` (`0XB0`) hasta `OP_NOP10` (`0XB9`)) se utilizan para agregar nuevos opcodes en forma de un soft fork.

Así, `OP_NOP2` (`0XB1`) y `OP_NOP3` (`0XB2`) ya han sido utilizados para implementar `OP_CHECKLOCKTIMEVERIFY` y `OP_CHECKSEQUENCEVERIFY`, respectivamente. Se utilizan en combinación con `OP_DROP` para eliminar los valores temporales asociados de la pila, permitiendo así que la ejecución del script continúe, ya sea que el nodo esté actualizado o no. Los comandos `OP_NOP`, por lo tanto, permiten la inserción de un punto de interrupción en un script para verificar condiciones adicionales que ya existen o pueden ser agregadas con futuros soft forks. Desde Tapscript, el uso de `OP_NOP` ha sido reemplazado por el más eficiente `OP_SUCCESS`.