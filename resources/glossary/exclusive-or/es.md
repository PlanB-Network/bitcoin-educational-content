---
term: EXCLUSIVO O

---
Función fundamental de la lógica booleana. La operación `O exclusivo` o XOR ("*O exclusivo*") toma dos operandos booleanos, cada uno verdadero o falso, y produce una salida verdadera sólo cuando los dos operandos son diferentes. En otras palabras, la salida de la operación `XOR` es verdadera si exactamente uno (pero no ambos) de los operandos es verdadero. Por ejemplo, la operación `XOR` entre `1` y `0` dará como resultado `1`. Observamos: 1$ \oplus 0 = 1$. Del mismo modo, la operación "XOR" se puede realizar en secuencias más largas de bits. Por ejemplo, $10110 \oplus 01110 = 11000$. Cada bit de la secuencia se compara con su homólogo y se aplica la operación "XOR". Esta es la tabla verdadero-falso de la operación "XOR":

<div align="center">

| ...$A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

La operación `XOR` se utiliza en muchas áreas de la informática, especialmente en criptografía, por sus interesantes atributos como:


- Su conmutatividad: el orden de los operandos no afecta al resultado. Para dos variables dadas $D$ y $E$: $D \oplus E = E \oplus D$;
- Su asociatividad: la agrupación de operandos no afecta al resultado. Para tres variables dadas $A$, $B$ y $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Tiene un elemento neutro `0`: un operando xorado con 0 siempre será igual al operando. Para una variable dada $A$: $A \oplus 0 = A$;
- Cada elemento es su propio inverso. Para una variable dada $A$: $A \oplus A = 0$.

En el contexto de Bitcoin, la operación `XOR` se utiliza obviamente en muchos lugares. Por ejemplo, `XOR` se utiliza masivamente en la función `SHA256`, que es ampliamente utilizada en el protocolo Bitcoin. Algunos protocolos como *SeedXOR* de Coldcard también utilizan esta primitiva para otras aplicaciones. También se encuentra en BIP47 para encriptar el código de pago reutilizable durante su transmisión.

En el campo más amplio de la criptografía, "XOR" puede utilizarse tal cual como algoritmo de cifrado simétrico. Este algoritmo se denomina "One-Time Pad" o "Cifrado de Vernam", en honor a su inventor. Aunque poco práctico debido a la longitud de la clave, este algoritmo es uno de los únicos algoritmos de cifrado reconocidos como incondicionalmente seguros.