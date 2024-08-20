---
term: OP_ENDIF (0X68)
---

Marca el final de una estructura de control condicional iniciada por un `OP_IF` o un `OP_NOTIF`, usualmente seguido por uno o más `OP_ELSE`. Indica que la ejecución del script debe continuar más allá de la estructura condicional, independientemente de qué rama fue ejecutada. En otras palabras, `OP_ENDIF` sirve para delinear el final de bloques condicionales en scripts.