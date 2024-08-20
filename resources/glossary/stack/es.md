---
term: STACK
---

En el contexto del lenguaje de script utilizado para aplicar condiciones de gasto en los UTXOs de Bitcoin, el stack es una estructura de datos "LIFO" (*Last In, First Out*, Último en Entrar, Primero en Salir) que sirve para almacenar elementos temporales durante la ejecución de un script. Cada operación en el script manipula estos stacks, donde los elementos pueden ser añadidos (*push*) o eliminados (*pop*). Los scripts usan stacks para evaluar expresiones, almacenar variables temporales y gestionar condiciones.

Durante la ejecución de un script de Bitcoin, se pueden utilizar 2 stacks: el stack principal y el stack alt (alternativo). El stack principal se utiliza para la mayoría de las operaciones de un script. Es en este stack donde las operaciones del script añaden, eliminan o manipulan datos. El stack alternativo, por otro lado, sirve para almacenar temporalmente datos durante la ejecución del script. Opcodes específicos, como `OP_TOALTSTACK` y `OP_FROMALTSTACK`, permiten la transferencia de elementos del stack principal al stack alternativo y viceversa.

Por ejemplo, durante la validación de una transacción, las firmas y claves públicas se introducen en el stack principal y son procesadas por opcodes sucesivos para verificar que las firmas coincidan con las claves y los datos de la transacción.

> ► *En inglés, la traducción de «pile» es «stack». El término en inglés se utiliza generalmente incluso en francés durante discusiones técnicas.*