---
term: Address spoofing
definition: Un ataque en el que un actor malicioso crea una dirección que se parece mucho a la de la víctima para engañarlo y desviar sus pagos.
---

Ataque en el que un actor malicioso crea un Address (u otro identificador de pago) muy parecido al de la víctima. El objetivo es engañar al usuario para que copie este Address erróneo durante una transacción, lo que provoca el envío de bitcoins al atacante en lugar del destino previsto.



El atacante aprovecha la precipitación del usuario para copiar el Address erróneo si realiza la transacción sin comprobar su exactitud. En general, para implementar este ataque, el atacante realiza pagos con pequeñas sumas a la Wallet de la víctima para integrar la Address falsa en su historial de transacciones. Este ataque suele utilizarse con altcoins, donde es práctica común reutilizar las mismas direcciones receptoras, a diferencia de Bitcoin, donde el uso de direcciones en blanco para cada transacción es una práctica más extendida. Sin embargo, los usuarios de Bitcoin no son inmunes a este ataque.



Otro método para presentar una dirección incorrecta a la víctima es el uso de software fraudulento de gestión de carteras que imita a programas legítimos, o la modificación de la dirección cuando una máquina está comprometida, entre el momento en que se copia y aquel en que se construye la transacción. A esto a veces se le denomina '"*address swapping*"'.



Para protegerse contra estos diferentes métodos de ataque, es importante comprobar varios caracteres del Address, especialmente su suma de comprobación (al final), en la pantalla del dispositivo de firma antes de firmar la transacción.



Esta ataque también se denomina a veces '"*address poisoning*"'.