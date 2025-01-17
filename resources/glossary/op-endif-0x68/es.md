---
term: OP_ENDIF (0X68)

---
Marca el final de una estructura de control condicional iniciada por un `OP_IF` o un `OP_NOTIF`, normalmente seguido por uno o más `OP_ELSE`. Indica que la ejecución del script debe continuar más allá de la estructura condicional, independientemente de la rama que se haya ejecutado. En otras palabras, `OP_ENDIF` sirve para delinear el final de los bloques condicionales en los scripts.