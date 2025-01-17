---
term: PILA

---
En el contexto del lenguaje de scripts utilizado para aplicar condiciones de gasto en los UTXOs de Bitcoin, la pila es una estructura de datos "LIFO" (*Last In, First Out*) que sirve para almacenar elementos temporales durante la ejecución de un script. Cada operación en el script manipula estas pilas, donde los elementos pueden ser añadidos (*push*) o eliminados (*pop*). Los scripts utilizan pilas para evaluar expresiones, almacenar variables temporales y gestionar condiciones.

Durante la ejecución de un script Bitcoin, se pueden utilizar 2 pilas: la pila principal y la pila alt (alternativa). La pila principal se utiliza para la mayoría de las operaciones de un script. Es en esta pila donde las operaciones del script añaden, eliminan o manipulan datos. La pila alternativa, por otro lado, sirve para almacenar temporalmente datos durante la ejecución del script. Códigos operativos específicos, como `OP_TOALTSTACK` y `OP_FROMALTSTACK`, permiten transferir elementos de la pila principal a la pila alternativa y viceversa.

Por ejemplo, durante la validación de una transacción, las firmas y las claves públicas se introducen en la pila principal y se procesan mediante opcodes sucesivos para verificar que las firmas coinciden con las claves y los datos de la transacción.

> ► *En inglés, la traducción de " pile " es " stack ". El término inglés se utiliza generalmente incluso en francés durante las discusiones técnicas.*