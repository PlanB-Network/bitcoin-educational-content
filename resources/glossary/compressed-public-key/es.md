---
term: CLAVE PÚBLICA COMPRIMIDA

---
Una clave pública se utiliza en los scripts (ya sea directamente en forma de clave pública o como dirección) para recibir y asegurar bitcoins. Una clave pública en bruto está representada por un punto de una curva elíptica, formado por dos coordenadas (`x, y`) de 256 bits cada una. En formato bruto, una clave pública mide 512 bits, sin contar el byte adicional para identificar el formato. En cambio, una clave pública comprimida es una forma más compacta de representación de una clave pública. Sólo utiliza la coordenada `x` y un prefijo (`02` o `03`) que indica la paridad de la coordenada `y` (par o impar).

Si simplificamos esto al campo de los números reales, dado que la curva elíptica es simétrica respecto al eje x, para cualquier punto $P$ (`x, y`) de la curva, existe un punto $P'$ (`x, -y`) que también estará en esta misma curva. Esto significa que para cada `x`, sólo hay dos valores posibles de `y`, positivo y negativo. Por ejemplo, para una abscisa `x` dada, habría dos puntos $P1$ y $P2$ en la curva elíptica, compartiendo la misma abscisa pero con ordenadas opuestas:

![](../../dictionnaire/assets/29.webp)

Para elegir entre los dos posibles puntos de la curva, se añade a `x` un prefijo que especifica qué `y` elegir. Este método permite reducir el tamaño de una clave pública de 520 bits a sólo 264 bits (8 bits de prefijo + 256 bits para `x`). Esta representación se conoce como la forma comprimida de la clave pública.

Sin embargo, en el contexto de la criptografía de curva elíptica, no utilizamos los números reales, sino un campo finito de orden `p` (un número primo). En este contexto, el "signo" de "y" viene determinado por su paridad, es decir, si "y" es par o impar. El prefijo `0x02` indica entonces un `y` par, mientras que `0x03` indica un `y` impar.

Considere el siguiente ejemplo de una clave pública sin procesar (un punto de la curva elíptica) en hexadecimal:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Podemos aislar el prefijo, `x`, y `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Base 16 (hexadecimal): f

Base 10 (decimal): 15

y es impar

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```