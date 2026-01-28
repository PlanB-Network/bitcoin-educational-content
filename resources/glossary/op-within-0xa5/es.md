---
term: OP_WITHIN (0XA5)

definition: Opcode que comprueba si un valor se encuentra dentro de un intervalo definido por otros dos valores.
---
Comprueba si el elemento superior de la pila está dentro del rango definido por el segundo y tercer elemento superior. En otras palabras, `OP_WITHIN` comprueba si el elemento superior es mayor o igual que el segundo y menor que el tercero. Si esta condición es verdadera, coloca `1` (verdadero) en la pila, de lo contrario, coloca `0` (falso).