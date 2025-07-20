---
term: Address SPOOFING
---

Ataque en el que un actor malicioso crea un Address (u otro identificador de pago) muy parecido al de la víctima. El objetivo es engañar al usuario para que copie este Address erróneo durante una transacción, lo que provoca el envío de bitcoins al atacante en lugar del destino previsto.


El atacante aprovecha la precipitación del usuario para copiar el Address erróneo si realiza la transacción sin comprobar su exactitud. En general, para implementar este ataque, el atacante realiza pagos con pequeñas sumas a la Wallet de la víctima para integrar la Address falsa en su historial de transacciones. Este ataque suele utilizarse con altcoins, donde es práctica común reutilizar las mismas direcciones receptoras, a diferencia de Bitcoin, donde el uso de direcciones en blanco para cada transacción es una práctica más extendida. Sin embargo, los usuarios de Bitcoin no son inmunes a este ataque.


Otro método para poner el Address equivocado delante de la víctima es el uso de software de gestión de Wallet fraudulento que imita al software legítimo, o cambiar el Address cuando una máquina está comprometida, entre el momento en que se copia y el momento en que se construye la transacción. Esto se denomina a veces "*Address swapping*".


Para protegerse contra estos diferentes métodos de ataque, es importante comprobar varios caracteres del Address, especialmente su suma de comprobación (al final), en la pantalla del dispositivo de firma antes de firmar la transacción.


> ► *Este ataque también se conoce a veces como Envenenamiento Address