---
term: EXCLUSIVE OR
---

Una función fundamental de la lógica Booleana. El "O exclusivo" o XOR ("*Exclusive or*") toma dos operandos Booleanos, cada uno siendo verdadero o falso, y produce una salida verdadera solo cuando los dos operandos difieren. En otras palabras, la salida de la operación `XOR` es verdadera si exactamente uno (pero no ambos) de los operandos es verdadero. Por ejemplo, la operación `XOR` entre `1` y `0` resultará en `1`. Notamos: $1 \oplus 0 = 1$. De manera similar, la operación `XOR` puede realizarse en secuencias más largas de bits. Por ejemplo, $10110 \oplus 01110 = 11000$. Cada bit de la secuencia se compara con su contraparte, y se aplica la operación `XOR`. Aquí está la tabla de verdad para la operación `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

La operación `XOR` se utiliza en muchas áreas de la informática, especialmente en criptografía, por sus atributos interesantes tales como:
* Su conmutatividad: el orden de los operandos no afecta el resultado. Para dos variables dadas $D$ y $E$: $D \oplus E = E \oplus D$;
* Su asociatividad: la agrupación de operandos no afecta el resultado. Para tres variables dadas $A$, $B$ y $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Tiene un elemento neutro `0`: un operando xoreado con 0 siempre será igual al operando. Para una variable dada $A$: $A \oplus 0 = A$;
* Cada elemento es su propio inverso. Para una variable dada $A$: $A \oplus A = 0$.

En el contexto de Bitcoin, la operación `XOR` obviamente se utiliza en muchos lugares. Por ejemplo, `XOR` se utiliza masivamente en la función `SHA256`, que es ampliamente utilizada en el protocolo de Bitcoin. Algunos protocolos como el *SeedXOR* de Coldcard también utilizan esta primitiva para otras aplicaciones. También se encuentra en BIP47 para encriptar el código de pago reutilizable durante su transmisión.
En el campo más amplio de la criptografía, `XOR` puede utilizarse tal cual como un algoritmo de encriptación simétrica. Este algoritmo se llama "One-Time Pad" o el "Cifrado de Vernam", nombrado así por su inventor. Aunque es impráctico debido a la longitud de la clave, este algoritmo es uno de los únicos algoritmos de encriptación reconocidos como incondicionalmente seguros.