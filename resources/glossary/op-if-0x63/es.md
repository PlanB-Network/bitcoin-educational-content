---
term: OP_IF (0X63)
---

Ejecuta la siguiente porción del script si el valor en la cima de la pila es no cero (verdadero). Si el valor es cero (falso), estas operaciones se omiten, moviéndose directamente a las que están después de `OP_ELSE`, si está presente. `OP_IF` permite el lanzamiento de una estructura de control condicional dentro de un script. Determina el flujo de control en un script basado en una condición proporcionada en el momento de la ejecución de la transacción. `OP_IF` se utiliza con `OP_ELSE` y `OP_ENDIF` de la siguiente manera:

```text
<condición>
OP_IF
<operaciones si la condición es verdadera>
OP_ELSE
<operaciones si la condición es falsa>
OP_ENDIF
```