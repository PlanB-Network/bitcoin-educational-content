---
term: OP_IF (0X63)

---
Ejecuta la siguiente parte del script si el valor en la parte superior de la pila es distinto de cero (true). Si el valor es cero (false), estas operaciones se saltan, pasando directamente a las que siguen a `OP_ELSE`, si está presente. `OP_IF` permite lanzar una estructura de control condicional dentro de un script. Determina el flujo de control en un script basándose en una condición proporcionada en el momento de la ejecución de la operación. `OP_IF` se utiliza con `OP_ELSE` y `OP_ENDIF` de la siguiente manera:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```