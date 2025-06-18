---
term: BATERÍA
---

En el contexto del lenguaje de script utilizado para fijar condiciones de gasto a Bitcoin UTXOs, la pila es una estructura de datos LIFO (*Last In, First Out*) utilizada para almacenar Elements temporales durante la ejecución del script. Cada operación en el script manipula estas pilas, donde Elements puede ser añadido (*push*) o eliminado (*pop*). Los scripts utilizan pilas para evaluar expresiones, almacenar variables temporales y gestionar condiciones.


Cuando se ejecuta un script de Bitcoin, se pueden utilizar 2 pilas: la pila principal y la pila alt (alternativa). La pila principal se utiliza para la mayoría de las operaciones de script. Es en esta pila donde las operaciones de script añaden, eliminan o manipulan datos. La pila alternativa, por otro lado, se utiliza para almacenar temporalmente datos durante la ejecución del script. Códigos operativos específicos, como `OP_TOALTSTACK` y `OP_FROMALTSTACK`, permiten transferir Elements de la pila principal a la pila alternativa y viceversa.


Por ejemplo, cuando se valida una transacción, las firmas y las claves públicas se introducen en la pila principal y se procesan mediante opcodes sucesivos para verificar que las firmas coinciden con las claves y los datos de la transacción.